#!/usr/bin/env python3
"""
LJB Wardrobe Asset Cropper
Crops jerseys, sneakers, and backdrops from raw app screenshots.

Usage:
    python crop_assets.py --type jersey  --input /path/to/screenshots/ --output /path/to/output/
    python crop_assets.py --type sneaker --input /path/to/screenshots/ --output /path/to/output/
    python crop_assets.py --type backdrop --input /path/to/screenshots/ --output /path/to/output/

Crop defaults (adjust per collection as needed):
    jersey:   top=30%, bottom=12%, left=5%, right=5%
    sneaker:  top=20%, bottom=40%, left=5%, right=5%  (VIEW EACH — varies per screenshot)
    backdrop: top=28%, bottom=10%, left=0%, right=0%
"""

import argparse
from pathlib import Path
from PIL import Image

CROP_DEFAULTS = {
    "jersey":   {"top": 0.30, "bottom": 0.12, "left": 0.05, "right": 0.05},
    "sneaker":  {"top": 0.20, "bottom": 0.40, "left": 0.05, "right": 0.05},
    "backdrop": {"top": 0.28, "bottom": 0.10, "left": 0.00, "right": 0.00},
}

def crop_image(img_path: Path, asset_type: str, output_dir: Path, prefix: str = "") -> Path:
    params = CROP_DEFAULTS[asset_type]
    img = Image.open(img_path)
    w, h = img.size

    left   = int(w * params["left"])
    right  = int(w * (1 - params["right"]))
    top    = int(h * params["top"])
    bottom = int(h * (1 - params["bottom"]))

    cropped = img.crop((left, top, right, bottom))
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = prefix + img_path.stem if prefix else img_path.stem
    out_path = output_dir / f"{stem}.png"
    cropped.save(out_path, "PNG")
    print(f"  ✅ {img_path.name} → {out_path.name} ({cropped.size[0]}×{cropped.size[1]})")
    return out_path

def main():
    parser = argparse.ArgumentParser(description="LJB Wardrobe Asset Cropper")
    parser.add_argument("--type",   required=True, choices=["jersey", "sneaker", "backdrop"])
    parser.add_argument("--input",  required=True, help="Directory containing raw screenshots")
    parser.add_argument("--output", required=True, help="Directory for cropped output")
    parser.add_argument("--prefix", default="",    help="Optional filename prefix")
    args = parser.parse_args()

    input_dir  = Path(args.input)
    output_dir = Path(args.output)
    images     = sorted(input_dir.glob("*.PNG")) + sorted(input_dir.glob("*.png")) + \
                 sorted(input_dir.glob("*.jpg")) + sorted(input_dir.glob("*.JPG"))

    print(f"\nCropping {len(images)} {args.type} images...")
    for img_path in images:
        crop_image(img_path, args.type, output_dir, args.prefix)
    print(f"\nDone. {len(images)} files saved to {output_dir}")

if __name__ == "__main__":
    main()
