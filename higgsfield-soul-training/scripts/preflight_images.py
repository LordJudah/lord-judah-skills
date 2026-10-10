#!/usr/bin/env python3
"""Preflight QC for Higgsfield Soul training photos.

Audits a folder of candidate images and reports which are training-grade:
resolution, orientation, detail energy, background type (flags green-screen and
pure-white studio composites), and near-duplicate clusters.

Usage:
    python preflight_images.py <folder> [--manifest out.json] [--min-mp 1.0] [--json]

No third-party dependencies beyond Pillow.
"""

import argparse
import json
import os
import sys
from collections import Counter

try:
    from PIL import Image, ImageFilter, ImageOps
except ImportError:
    sys.exit("Pillow is required: sudo pip3 install Pillow")

IMAGE_EXT = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff", ".heic", ".heif"}


def dhash(img, size=8):
    """64-bit difference hash as an int. Cheap perceptual fingerprint."""
    small = img.convert("L").resize((size + 1, size), Image.LANCZOS)
    px = small.tobytes()
    bits = 0
    for row in range(size):
        for col in range(size):
            left = px[row * (size + 1) + col]
            right = px[row * (size + 1) + col + 1]
            bits = (bits << 1) | (1 if left > right else 0)
    return bits


def hamming(a, b):
    return bin(a ^ b).count("1")


def classify_pixel(r, g, b):
    """Bucket a border pixel: white / green / black / other."""
    mx, mn = max(r, g, b), min(r, g, b)
    if mn > 232 and (mx - mn) < 14:
        return "white"
    if g > 110 and g > r * 1.35 and g > b * 1.35:
        return "green"
    if mx < 32:
        return "black"
    return "other"


def background_profile(img):
    """Dominant background class and its share of the border ring."""
    im = img.convert("RGB")
    w, h = im.size
    step_x, step_y = max(1, w // 60), max(1, h // 60)
    ring = []
    for x in range(0, w, step_x):
        ring.append(im.getpixel((x, 0)))
        ring.append(im.getpixel((x, h - 1)))
    for y in range(0, h, step_y):
        ring.append(im.getpixel((0, y)))
        ring.append(im.getpixel((w - 1, y)))
    if not ring:
        return {"class": "unknown", "share": 0.0}
    counts = Counter(classify_pixel(*p) for p in ring)
    cls, n = counts.most_common(1)[0]
    return {"class": cls, "share": round(n / len(ring), 3)}


def detail_energy(img):
    """Edge energy in the centre crop, contrast-normalised. ADVISORY ONLY.

    This does NOT measure focus reliably. Measured against known-good studio
    portraits it tracks scene smoothness and depth of field rather than blur:
    a sharp shallow-DOF portrait with a smooth backdrop scores 9-12, while a
    busy real-world photograph scores 30-76. Do not reject on this number --
    it is reported so the caller can spot genuinely flat or failed images.

    Centre crop, because a portrait subject sits in the middle and letting a
    large flat background dominate the statistic is what breaks this measure.
    """
    g = img.convert("L")
    w, h = g.size
    cw, ch = int(w * 0.6), int(h * 0.6)
    if cw < 16 or ch < 16:
        cw, ch = w, h
    g = g.crop(((w - cw) // 2, (h - ch) // 2, (w - cw) // 2 + cw, (h - ch) // 2 + ch))
    g = ImageOps.autocontrast(g, cutoff=1)
    g = g.resize((min(g.width, 768), min(g.height, 768)))
    edges = g.filter(ImageFilter.FIND_EDGES)
    px = edges.tobytes()
    mean = sum(px) / len(px)
    var = sum((p - mean) ** 2 for p in px) / len(px)
    return round(var ** 0.5, 2)


def audit(path, min_mp):
    rec = {"file": path, "name": os.path.basename(path)}
    try:
        with Image.open(path) as raw:
            exif_orient = raw.getexif().get(274)
            im = ImageOps.exif_transpose(raw).convert("RGB")
        w, h = im.size
        mp = (w * h) / 1_000_000
        rec.update({
            "w": w, "h": h, "mp": round(mp, 2),
            "aspect": round(w / h, 3),
            "orientation": "portrait" if h > w else ("landscape" if w > h else "square"),
            "exif_rotated": bool(exif_orient and exif_orient != 1),
            "detail_energy": detail_energy(im),
            "background": background_profile(im),
            "dhash": dhash(im),
        })
        reasons = []
        if mp < min_mp:
            reasons.append(f"low-resolution ({mp:.2f} MP < {min_mp} MP)")
        if rec["exif_rotated"]:
            reasons.append("EXIF rotation flag set (verify orientation)")
        if rec["detail_energy"] < 4:
            reasons.append(f"almost no image detail (energy {rec['detail_energy']})"
                           f" - blank, flat, or failed export")
        bg = rec["background"]
        if bg["class"] == "green" and bg["share"] > 0.30:
            reasons.append(f"green-screen background ({bg['share']:.0%} of border) "
                           f"- verify it is a genuine photograph, not a composite")
        if bg["class"] == "white" and bg["share"] > 0.55:
            reasons.append(f"pure-white studio background ({bg['share']:.0%} of border) "
                           f"- verify provenance (studio or render?)")
        rec["reject_reasons"] = reasons
        rec["status"] = "review" if reasons else "pass"
        rec["readable"] = True
    except Exception as exc:  # noqa: BLE001
        rec.update({"readable": False, "status": "reject", "reject_reasons":
                    [f"unreadable: {type(exc).__name__}"]})
    return rec


def cluster_duplicates(recs, threshold=6):
    """Group near-identical images by Hamming distance on dhash."""
    hashed = [r for r in recs if r.get("readable") and "dhash" in r]
    parent = list(range(len(hashed)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for i in range(len(hashed)):
        for j in range(i + 1, len(hashed)):
            if hamming(hashed[i]["dhash"], hashed[j]["dhash"]) <= threshold:
                union(i, j)
    groups = {}
    for idx, rec in enumerate(hashed):
        groups.setdefault(find(idx), []).append(rec["name"])
    return [sorted(v) for v in groups.values() if len(v) > 1]


def main():
    ap = argparse.ArgumentParser(description="Soul training photo preflight")
    ap.add_argument("folder")
    ap.add_argument("--manifest", help="write full JSON report here")
    ap.add_argument("--min-mp", type=float, default=1.0)
    ap.add_argument("--json", action="store_true", help="print JSON only")
    args = ap.parse_args()

    files = []
    for root, _, names in os.walk(args.folder):
        for n in sorted(names):
            if os.path.splitext(n)[1].lower() in IMAGE_EXT:
                files.append(os.path.join(root, n))
    if not files:
        sys.exit(f"No images found under {args.folder}")

    full = [audit(f, args.min_mp) for f in files]
    dups = cluster_duplicates(full)
    recs = []
    for r in full:
        r.pop("dhash", None)
        recs.append(r)

    passed = [r for r in recs if r["status"] == "pass"]
    review = [r for r in recs if r["status"] == "review"]
    rejected = [r for r in recs if r["status"] == "reject"]
    passed.sort(key=lambda r: -r.get("mp", 0))

    if args.manifest:
        with open(args.manifest, "w") as fh:
            json.dump({"passed": passed, "review": review,
                       "rejected": rejected, "duplicate_groups": dups}, fh, indent=1)

    if args.json:
        print(json.dumps({"passed": passed, "review": review,
                          "rejected": rejected, "duplicate_groups": dups}, indent=1))
        return

    print(f"Scanned {len(recs)} images under {args.folder}\n")
    print(f"PASS {len(passed)} | REVIEW {len(review)} | REJECT {len(rejected)}\n")
    print("-- PASS (ranked by resolution) --")
    for r in passed:
        print(f"  {r['mp']:>6.2f} MP  {r['w']}x{r['h']:<6} {r['orientation']:<9} "
              f"bg={r['background']['class']:<6} detail={r['detail_energy']:>7}  {r['name']}")
    if review:
        print("\n-- REVIEW (fixable or borderline) --")
        for r in review:
            print(f"  {r['name']}: {'; '.join(r['reject_reasons'])}")
    if rejected:
        print("\n-- REJECT --")
        for r in rejected:
            print(f"  {r['name']}: {'; '.join(r['reject_reasons'])}")
    if dups:
        print("\n-- NEAR-DUPLICATE CLUSTERS (prefer one per cluster) --")
        for g in dups:
            print(f"  {', '.join(g)}")
    print(f"\nSelect 5-20 PASS images (12-16 ideal), spread across angles, environments "
          f"and lighting. One grooming era only.")


if __name__ == "__main__":
    main()
