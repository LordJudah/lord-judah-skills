"""
LJB Course Launch Workflow — Phase 3
Uploads a course cover image to a Shopify product.
Set PRODUCT_ID and IMAGE_PATH before running.
"""

import requests
import base64
import os

# ─── CONFIG ───────────────────────────────────────────────────────────────────
PRODUCT_ID = 0          # ← Set to the Product ID from Phase 1
IMAGE_PATH = ""         # ← e.g., "/home/ubuntu/true-heart-course-cover.jpg"
IMAGE_ALT = "Course cover image"
# ──────────────────────────────────────────────────────────────────────────────
# Shopify credentials — supplied via environment variables, never hardcoded.
CLIENT_ID = os.environ.get("SHOPIFY_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("SHOPIFY_CLIENT_SECRET", "")
STORE = os.environ.get("SHOPIFY_STORE", "")

if not (CLIENT_ID and CLIENT_SECRET and STORE):
    raise SystemExit(
        "ERROR: Shopify credentials missing. Set SHOPIFY_CLIENT_ID, "
        "SHOPIFY_CLIENT_SECRET, and SHOPIFY_STORE in the environment."
    )

BASE = f"https://{STORE}/admin/api/2024-01"

def get_token():
    resp = requests.post(
        f"https://{STORE}/admin/oauth/access_token",
        json={"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET, "grant_type": "client_credentials"}
    )
    return resp.json().get("access_token")

if not PRODUCT_ID or not IMAGE_PATH:
    print("ERROR: Set PRODUCT_ID and IMAGE_PATH before running.")
    exit(1)

TOKEN = get_token()
HEADERS = {"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"}

with open(IMAGE_PATH, "rb") as f:
    image_data = base64.b64encode(f.read()).decode("utf-8")

filename = IMAGE_PATH.split("/")[-1]
print(f"Uploading {filename} to product {PRODUCT_ID}...")

img_resp = requests.post(
    f"{BASE}/products/{PRODUCT_ID}/images.json",
    headers=HEADERS,
    json={"image": {
        "attachment": image_data,
        "filename": filename,
        "alt": IMAGE_ALT,
        "position": 1
    }}
)

if img_resp.status_code in (200, 201):
    img = img_resp.json()["image"]
    print(f"✅ Image uploaded successfully!")
    print(f"   Image ID: {img['id']}")
    print(f"   Image URL: {img['src']}")
else:
    print(f"ERROR: {img_resp.status_code} — {img_resp.text[:300]}")
