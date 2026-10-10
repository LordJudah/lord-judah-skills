#!/usr/bin/env python3
"""
LJB Blotato Post Scheduler
Uploads images and schedules posts across Instagram, Threads, Twitter/X, and TikTok.

CRITICAL: Uses 'scheduledTime' (NOT 'scheduledAt') — wrong field silently posts immediately.

Usage:
    Edit the POSTS list below, then run:
    python schedule_posts.py

Each post entry:
    {
        "code": "TT-09",
        "image": "/absolute/path/to/image.png",
        "scheduledTime": "2026-05-03T16:00:00-04:00",   # 4PM EDT
        "captions": {
            "instagram": "...",
            "threads":   "...",
            "twitter":   "...",
            "tiktok":    "...",
        }
    }
"""

import subprocess, json, time

# ── CONFIGURE POSTS HERE ──────────────────────────────────────────────────────
POSTS = [
    # Add post dicts here
]

# ── PLATFORM ACCOUNT IDs ──────────────────────────────────────────────────────
ACCOUNTS = {
    "instagram": "1005",   # @lordjudah
    "threads":   "310",    # @lordjudah
    "twitter":   "846",    # @judahblessent
    "tiktok":    "1217",   # @judahblessent
}

# ── HELPERS ───────────────────────────────────────────────────────────────────
def run_mcp(tool, input_data):
    cmd = ["manus-mcp-cli", "tool", "call", tool,
           "--server", "blotato", "--input", json.dumps(input_data)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    for line in result.stdout.strip().split('\n'):
        if line.startswith('{') or line.startswith('['):
            try:
                return json.loads(line)
            except Exception:
                pass
    return {"raw": result.stdout}

def upload_image(image_path: str) -> str:
    """Upload image to Blotato, return public URL."""
    filename = image_path.split("/")[-1]
    presign  = run_mcp("blotato_create_presigned_upload_url", {"filename": filename})
    public_url    = presign.get("publicUrl", "")
    presigned_url = presign.get("presignedUrl", "")
    if not public_url:
        raise RuntimeError(f"No presigned URL returned for {filename}: {presign}")
    upload_cmd = ["curl", "-s", "-X", "PUT", presigned_url,
                  "--data-binary", f"@{image_path}", "-w", "\nHTTP:%{{http_code}}"]
    out = subprocess.run(upload_cmd, capture_output=True, text=True).stdout
    if "HTTP:200" not in out:
        raise RuntimeError(f"Upload failed for {filename}: {out[-60:]}")
    return public_url

def schedule_post(account_id, platform, caption, media_url, scheduled_time, extra=None):
    payload = {
        "accountId":     account_id,
        "platform":      platform,
        "text":          caption,
        "mediaUrls":     [media_url],
        "scheduledTime": scheduled_time,   # CORRECT FIELD
    }
    if extra:
        payload.update(extra)
    return run_mcp("blotato_create_post", payload)

# ── MAIN ──────────────────────────────────────────────────────────────────────
all_results = []

for post in POSTS:
    print(f"\n{'='*55}")
    print(f"  {post['code']} → {post['scheduledTime']}")
    print(f"{'='*55}")

    print("  [1/2] Uploading image...")
    public_url = upload_image(post["image"])
    print(f"  Uploaded → {public_url[:60]}...")

    print("  [2/2] Scheduling posts...")
    post_results = {"code": post["code"], "scheduledTime": post["scheduledTime"], "platforms": {}}

    platforms = [
        ("instagram", ACCOUNTS["instagram"], {}),
        ("threads",   ACCOUNTS["threads"],   {}),
        ("twitter",   ACCOUNTS["twitter"],   {}),
        ("tiktok",    ACCOUNTS["tiktok"],    {
            "privacyLevel": "PUBLIC_TO_EVERYONE",
            "disabledComments": False,
            "disabledDuet": False,
            "disabledStitch": False,
            "isBrandedContent": False,
            "isYourBrand": False,
            "isAiGenerated": True
        }),
    ]

    for platform, account_id, extra in platforms:
        result = schedule_post(account_id, platform,
                               post["captions"][platform],
                               public_url,
                               post["scheduledTime"],
                               extra)
        msg = result.get("message", str(result))
        ok  = "scheduled" in msg.lower()
        post_results["platforms"][platform] = {"message": msg, "scheduled": ok}
        print(f"    {'✅' if ok else '⚠️ '} {platform}: {msg}")
        time.sleep(1)

    all_results.append(post_results)
    time.sleep(2)

# Save results
import os
results_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "schedule_results.json")
with open(results_path, "w") as f:
    json.dump(all_results, f, indent=2)

print(f"\n\n{'='*55}")
print("  COMPLETE — verify queue with blotato_list_schedules")
print(f"{'='*55}")
for r in all_results:
    print(f"\n  {r['code']} → {r['scheduledTime']}")
    for platform, data in r["platforms"].items():
        print(f"    {'✅' if data['scheduled'] else '⚠️ '} {platform}: {data['message'][:60]}")
