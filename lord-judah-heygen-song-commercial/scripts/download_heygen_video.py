#!/usr/bin/env python3
"""
Download a HeyGen video from a signed S3 URL.
Usage: python3 download_heygen_video.py <video_url> <output_path>
"""

import sys
import requests
import os

def download_video(url: str, output_path: str) -> bool:
    """Download a HeyGen video using streaming to handle large files reliably."""
    print(f"Downloading to {output_path}...")
    try:
        r = requests.get(url, stream=True, timeout=120)
        r.raise_for_status()
        os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
        with open(output_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
        size_mb = os.path.getsize(output_path) / 1024 / 1024
        print(f"Done: {size_mb:.1f} MB saved to {output_path}")
        return True
    except Exception as e:
        print(f"Error downloading video: {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 download_heygen_video.py <video_url> <output_path>")
        sys.exit(1)
    video_url = sys.argv[1]
    output_path = sys.argv[2]
    success = download_video(video_url, output_path)
    sys.exit(0 if success else 1)
