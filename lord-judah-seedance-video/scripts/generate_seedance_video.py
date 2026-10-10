#!/usr/bin/env python3
"""
Seedance 2.0 Video Generation Script for Lord Judah / Judah Bless Ent.
This script interfaces with the Fal.ai API to generate cinematic videos using the Seedance 2.0 model.
"""

import os
import sys
import json
import argparse
import requests
import time

def generate_video(mode, prompt, image_url=None, end_image_url=None, aspect_ratio="9:16", duration="auto", resolution="720p", fast=False):
    """
    Call the Fal.ai API to generate a video using Seedance 2.0.
    """
    fal_key = os.environ.get("FAL_KEY")
    if not fal_key:
        print("Error: FAL_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    headers = {
        "Authorization": f"Key {fal_key}",
        "Content-Type": "application/json"
    }

    # Determine endpoint
    base_url = "https://fal.run/fal-ai/seedance-2"
    endpoint_map = {
        "t2v": "/text-to-video",
        "i2v": "/image-to-video",
        "r2v": "/reference-to-video"
    }
    
    if mode not in endpoint_map:
        print(f"Error: Invalid mode '{mode}'. Use t2v, i2v, or r2v.", file=sys.stderr)
        sys.exit(1)
        
    path = endpoint_map[mode]
    if fast:
        path = f"/fast{path}"
        
    url = f"{base_url}{path}"
    
    # Build payload
    payload = {
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "duration": duration,
        "resolution": resolution,
        "generate_audio": True
    }
    
    if mode == "i2v" and image_url:
        payload["image_url"] = image_url
        if end_image_url:
            payload["end_image_url"] = end_image_url

    print(f"Submitting request to {url}...")
    print(f"Payload: {json.dumps({k: v for k, v in payload.items() if k != 'image_url'}, indent=2)}")
    
    try:
        # Use fal.run which is synchronous but might timeout for long jobs
        # For production, fal-client async API is better, but this works for simple scripts
        response = requests.post(url, headers=headers, json=payload, timeout=300)
        
        if response.status_code != 200:
            print(f"API Error ({response.status_code}): {response.text}", file=sys.stderr)
            sys.exit(1)
            
        result = response.json()
        print("\n✅ Generation Complete!")
        print(f"Video URL: {result.get('video', {}).get('url', 'Not found')}")
        print(f"Seed: {result.get('seed', 'Unknown')}")
        
        # Download the video
        video_url = result.get('video', {}).get('url')
        if video_url:
            print("\nDownloading video...")
            timestamp = int(time.time())
            filename = f"seedance_{mode}_{timestamp}.mp4"
            
            vid_resp = requests.get(video_url)
            with open(filename, 'wb') as f:
                f.write(vid_resp.content)
            print(f"Video saved to {os.path.abspath(filename)}")
            
        return result
        
    except Exception as e:
        print(f"Exception during generation: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate videos with Seedance 2.0 via Fal.ai")
    parser.add_argument("--mode", choices=["t2v", "i2v", "r2v"], required=True, help="Generation mode")
    parser.add_argument("--prompt", required=True, help="Text prompt for the video")
    parser.add_argument("--image_url", help="Starting image URL (required for i2v)")
    parser.add_argument("--end_image_url", help="Ending image URL (optional for i2v)")
    parser.add_argument("--aspect_ratio", default="9:16", help="Aspect ratio (default: 9:16)")
    parser.add_argument("--duration", default="auto", help="Duration in seconds or 'auto'")
    parser.add_argument("--resolution", default="720p", choices=["480p", "720p", "1080p"], help="Video resolution")
    parser.add_argument("--fast", action="store_true", help="Use fast endpoint")
    
    args = parser.parse_args()
    
    if args.mode == "i2v" and not args.image_url:
        print("Error: --image_url is required when mode is i2v", file=sys.stderr)
        sys.exit(1)
        
    generate_video(
        mode=args.mode,
        prompt=args.prompt,
        image_url=args.image_url,
        end_image_url=args.end_image_url,
        aspect_ratio=args.aspect_ratio,
        duration=args.duration,
        resolution=args.resolution,
        fast=args.fast
    )
