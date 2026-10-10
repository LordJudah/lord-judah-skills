"""
LJB Course Launch Workflow — Phase 1
Creates a new online course product in the Judah Bless Ent Shopify store.
Set the variables in the CONFIG section before running.
"""

import requests
import json

# ─── CONFIG ───────────────────────────────────────────────────────────────────
COURSE_TITLE = "True He(ART) Academy: Foundations"
COURSE_SUBTITLE = "Foundations"
COURSE_PRICE = "97.00"
COURSE_TAGS = "Online Course, Education, Hip-Hop, True HeART Academy, Lord Judah"
COLLECTION_TITLE = "Online Courses"

COURSE_DESCRIPTION_HTML = """
<h2>The Cypher Is Open.</h2>
<p>True He(ART) Academy: Foundations is a 4-module online course that uses hip-hop as a tool for creative transformation, mindfulness, and community empowerment.</p>
<h3>What You'll Learn</h3>
<ul>
  <li><strong>Module 1 — The Cypher of Self:</strong> Creative identity, mindfulness, and the neuroscience of community.</li>
  <li><strong>Module 2 — The Architecture of the Bar:</strong> Advanced lyricism, song structure, and internal rhyme schemes.</li>
  <li><strong>Module 3 — The Sonic Landscape:</strong> Beat-making foundations, rhythm, and the emotional impact of sound.</li>
  <li><strong>Module 4 — The Digital Cypher:</strong> AI as a creative amplifier and building authentic community online.</li>
</ul>
<h3>Final Project</h3>
<p>Your 16-bar True He(ART) Manifesto — a verse that tells your story, your way.</p>
<h3>What's Included</h3>
<ul>
  <li>Video lessons for each module</li>
  <li>Creative exercises and writing prompts</li>
  <li>Lifetime access</li>
  <li>Certificate of completion</li>
</ul>
<p><em>"This isn't just a course. It's a cypher. And the first verse starts with you."</em></p>
"""
# ──────────────────────────────────────────────────────────────────────────────

# Shopify credentials — supplied via environment variables, never hardcoded.
#   export SHOPIFY_CLIENT_ID=...
#   export SHOPIFY_CLIENT_SECRET=...
#   export SHOPIFY_STORE=your-store.myshopify.com
import os

CLIENT_ID = os.environ.get("SHOPIFY_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("SHOPIFY_CLIENT_SECRET", "")
STORE = os.environ.get("SHOPIFY_STORE", "")

if not (CLIENT_ID and CLIENT_SECRET and STORE):
    raise SystemExit(
        "ERROR: Shopify credentials missing. Set SHOPIFY_CLIENT_ID, "
        "SHOPIFY_CLIENT_SECRET, and SHOPIFY_STORE in the environment "
        "(shopify admin -> Apps -> Develop apps -> your app -> Client credentials)."
    )

BASE = f"https://{STORE}/admin/api/2024-01"

def get_token():
    resp = requests.post(
        f"https://{STORE}/admin/oauth/access_token",
        json={"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET, "grant_type": "client_credentials"}
    )
    return resp.json().get("access_token")

TOKEN = get_token()
HEADERS = {"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"}

# Step 1: Create or find the collection
print(f"Looking for '{COLLECTION_TITLE}' collection...")
colls = requests.get(f"{BASE}/custom_collections.json?limit=250", headers=HEADERS).json()
collection_id = None
for c in colls.get("custom_collections", []):
    if c["title"].lower() == COLLECTION_TITLE.lower():
        collection_id = c["id"]
        print(f"Found existing collection: {collection_id}")
        break

if not collection_id:
    coll_resp = requests.post(
        f"{BASE}/custom_collections.json",
        headers=HEADERS,
        json={"custom_collection": {"title": COLLECTION_TITLE, "published": True}}
    )
    collection_id = coll_resp.json()["custom_collection"]["id"]
    print(f"Created new collection: {collection_id}")

# Step 2: Create the product
print(f"\nCreating product: {COURSE_TITLE}...")
product_payload = {
    "product": {
        "title": COURSE_TITLE,
        "body_html": COURSE_DESCRIPTION_HTML,
        "vendor": "Judah Bless Ent",
        "product_type": "Online Course",
        "tags": COURSE_TAGS,
        "status": "active",
        "variants": [{
            "price": COURSE_PRICE,
            "requires_shipping": False,
            "taxable": True,
            "inventory_management": None,
            "inventory_policy": "continue",
            "fulfillment_service": "manual",
            "sku": f"THA-{COURSE_SUBTITLE.upper().replace(' ', '-')[:20]}-001"
        }]
    }
}
prod_resp = requests.post(f"{BASE}/products.json", headers=HEADERS, json=product_payload)
if prod_resp.status_code not in (200, 201):
    print(f"ERROR creating product: {prod_resp.status_code} — {prod_resp.text[:300]}")
    exit(1)

product = prod_resp.json()["product"]
product_id = product["id"]
print(f"✅ Product created: {product_id}")
print(f"   URL: https://{STORE}/products/{product['handle']}")

# Step 3: Add to collection
collect_resp = requests.post(
    f"{BASE}/collects.json",
    headers=HEADERS,
    json={"collect": {"product_id": product_id, "collection_id": collection_id}}
)
if collect_resp.status_code in (200, 201):
    print(f"✅ Added to '{COLLECTION_TITLE}' collection")
else:
    print(f"⚠️  Could not add to collection: {collect_resp.status_code}")

print(f"\n{'='*50}")
print(f"PRODUCT ID: {product_id}  ← Save this for Phase 3 (image upload)")
print(f"{'='*50}")
