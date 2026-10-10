#!/usr/bin/env python3
"""Complete Higgsfield media uploads from a saved media_upload tool result.

`media_upload` returns presigned URLs plus media_ids but does not transfer the
bytes. This script performs the PUTs, classifies the response, retries the
failures worth retrying, and prints the ready-to-paste `medias` array for
show_characters(action="train").

Usage:
    python upload_media.py <media_upload_result.json> --dir <folder> [--out uploaded.json]

Status handling
---------------
200  success
412  the object already exists -- treated as uploaded (idempotent re-runs)
000  transient network failure -- retried
5xx / 429  transient server condition -- retried
403  the presigned URL has EXPIRED -- deterministic, cannot be retried
     The URL advertises X-Amz-Expires=86400, but the embedded AWS session
     token governs the real window and lives roughly one hour. Re-run
     media_upload for fresh slots, then run this script immediately.
other  deterministic rejection -- reported, not retried

Never report an upload as complete until the PUT succeeds AND media_confirm ran.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time

SUCCESS = {"200", "412"}
TRANSIENT = {"000", "408", "429", "500", "502", "503", "504"}


def load_uploads(path):
    with open(path) as fh:
        data = json.load(fh)
    if isinstance(data, dict):
        for key in ("structuredContent", "content", "result", "data"):
            if key in data and isinstance(data[key], dict) and "uploads" in data[key]:
                return data[key]["uploads"]
    if isinstance(data, dict) and "uploads" in data:
        return data["uploads"]
    sys.exit(f"Could not locate uploads[] in {path}")


def resolve_url(entry):
    """Prefer an explicit url field; otherwise parse the curl instruction."""
    for key in ("url", "upload_url", "presigned_url"):
        if entry.get(key):
            return entry[key]
    text = entry.get("instructions", "")
    m = re.search(r"--data-binary\s+@\S+?\s+'(\S+?)'", text)
    if m:
        return m.group(1)
    m = re.search(r"(https://\S+)", text)
    if m:
        return m.group(1).rstrip("'").rstrip('"')
    return None


def resolve_filename(entry, directory, index):
    m = re.search(r"--data-binary\s+@(\S+?)\s+'", entry.get("instructions", ""))
    candidates = []
    if m:
        candidates.append(m.group(1))
    for key in ("filename", "file", "name"):
        if entry.get(key):
            candidates.append(os.path.basename(entry[key]))
    candidates.append(f"lj_train_{index:02d}.jpg")
    for cand in candidates:
        p = cand if os.path.isabs(cand) else os.path.join(directory, cand)
        if os.path.exists(p):
            return p
    return None


def put_file(path, url, content_type, attempts=3):
    """PUT the bytes. Returns (status, attempts_used)."""
    code = "000"
    for attempt in range(1, attempts + 1):
        proc = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
             "-X", "PUT", "-H", f"Content-Type: {content_type}",
             "--data-binary", f"@{path}", url],
            capture_output=True, text=True)
        code = (proc.stdout or "").strip()
        if code in SUCCESS:
            return code, attempt
        if code not in TRANSIENT:
            return code, attempt  # deterministic; retrying wastes time
        if attempt < attempts:
            time.sleep(2 ** attempt)
    return code, attempts


def main():
    ap = argparse.ArgumentParser(description="Complete Higgsfield media uploads")
    ap.add_argument("result_json")
    ap.add_argument("--dir", default=".", help="directory containing the files")
    ap.add_argument("--out", default="uploaded.json")
    ap.add_argument("--attempts", type=int, default=3)
    args = ap.parse_args()

    uploads = load_uploads(args.result_json)
    results, missing = [], []

    for i, entry in enumerate(uploads, 1):
        url = resolve_url(entry)
        path = resolve_filename(entry, args.dir, i)
        media_id = entry.get("media_id") or entry.get("mediaId") or entry.get("id")
        ctype = entry.get("content_type", "image/jpeg")

        if not url or not path:
            why = "no presigned URL" if not url else "no local file"
            print(f"[{i:>2}] SKIP  {why} for media_id {media_id}")
            missing.append(media_id)
            continue

        code, tries = put_file(path, url, ctype, args.attempts)

        if code == "403":
            print(f"\n[{i:>2}] 403 Forbidden on {os.path.basename(path)}.")
            print("      The presigned URLs have EXPIRED. They advertise "
                  "X-Amz-Expires=86400, but the embedded")
            print("      AWS session token governs the real window and lives about "
                  "one hour. Call media_upload")
            print("      again for fresh slots, then re-run this script immediately.\n")
            results.append({"file": os.path.basename(path), "media_id": media_id,
                            "http": code, "attempts": tries})
            missing.append(media_id)
            break

        if code in SUCCESS:
            tag = "OK  " if code == "200" else "OK* "
            note = " (already present)" if code == "412" else ""
            print(f"[{i:>2}] {tag} HTTP {code}  {os.path.basename(path)}  ->  "
                  f"{media_id}{note}")
        else:
            note = f" (attempt {tries})" if tries > 1 else ""
            print(f"[{i:>2}] FAIL HTTP {code}  {os.path.basename(path)}  ->  "
                  f"{media_id}{note}")
            missing.append(media_id)

        results.append({"file": os.path.basename(path), "media_id": media_id,
                        "http": code, "attempts": tries})

    ok = [r for r in results if r["http"] in SUCCESS]
    media_ids = [r["media_id"] for r in ok]

    with open(args.out, "w") as fh:
        json.dump({"uploaded": results, "media_ids": media_ids,
                   "missing_media_ids": [m for m in missing if m]}, fh, indent=1)

    print(f"\nUploaded: {len(ok)}/{len(results)}")
    if missing:
        print("NOT uploaded - do not confirm or train on these:")
        for m in missing:
            print(f"  {m}")

    if len(ok) < len(results):
        print("\nFix the failures and re-run before confirming. Partial uploads "
              "must never be trained on.")

    if media_ids:
        medias = [{"role": "image", "value": m} for m in media_ids]
        print("\nNext: call media_confirm with these media_ids and type \"image\", "
              "then train.\n")
        print(json.dumps({"action": "train", "name": "<name>",
                          "type": "soul_2", "medias": medias}, indent=1))


if __name__ == "__main__":
    main()