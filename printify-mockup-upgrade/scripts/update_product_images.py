"""
Update Printify product listings with custom mockups and set cover art as primary image.
"""
import requests
import base64
import time
import json
import os

# --- CONFIGURATION ---
# REPLACE THESE WITH ACTUAL VALUES BEFORE RUNNING
TOKEN = 'YOUR_PRINTIFY_BEARER_TOKEN'
SHOPIFY_SHOP_ID = 'YOUR_PRINTIFY_SHOP_ID'

# List of products to update
# 'shopify_gid' is used to map to the internal Printify ID
# Ensure all file paths exist and point to .png or .jpg files
PRODUCTS = [
    {
        'name': 'Example Product',
        'printify_id': None,  # will be fetched automatically
        'shopify_gid': 'gid://shopify/Product/1234567890',
        'cover': '/path/to/cover.png',
        'mockups': [
            '/path/to/mockup1.png',
            '/path/to/mockup2.png'
        ]
    }
]

# Optional shared flat-lay image to add to all products
FLATLAY = '/path/to/flatlay.png'
# ---------------------

HEADERS = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
BASE_URL = 'https://api.printify.com/v1'

def upload_image(filepath, filename):
    if not os.path.exists(filepath):
        print(f"    UPLOAD FAILED: File not found: {filepath}")
        return None
        
    with open(filepath, 'rb') as f:
        content = base64.b64encode(f.read()).decode('utf-8')
    r = requests.post(f'{BASE_URL}/uploads/images.json', headers=HEADERS,
                      json={'file_name': filename, 'contents': content})
    result = r.json()
    img_id = result.get('id')
    if not img_id:
        print(f"    UPLOAD FAILED for {filename}: {result}")
    return img_id

def main():
    print("=== FETCHING PRINTIFY PRODUCTS ===")
    r = requests.get(f'{BASE_URL}/shops/{SHOPIFY_SHOP_ID}/products.json?limit=50', headers=HEADERS)
    if r.status_code != 200:
        print(f"Failed to fetch products: {r.status_code} - {r.text}")
        return
        
    all_products = r.json().get('data', [])
    print(f"Found {len(all_products)} products in Printify shop")

    printify_by_shopify_id = {}
    for p in all_products:
        ext = p.get('external', {})
        ext_id = ext.get('id', '')
        printify_by_shopify_id[ext_id] = p['id']

    flatlay_id = None
    if os.path.exists(FLATLAY):
        print("\n=== UPLOADING SHARED FLAT-LAY ===")
        flatlay_id = upload_image(FLATLAY, 'shared_flatlay.png')
        print(f"Flat-lay image ID: {flatlay_id}")

    results = []
    for product in PRODUCTS:
        name = product['name']
        shopify_numeric_id = product['shopify_gid'].split('/')[-1]
        printify_id = printify_by_shopify_id.get(shopify_numeric_id)
        
        if not printify_id:
            print(f"\n[{name}] ❌ Could not find Printify ID for Shopify {shopify_numeric_id}")
            results.append({'name': name, 'status': 'NOT FOUND'})
            continue
        
        print(f"\n[{name}] Printify ID: {printify_id}")
        
        # Upload cover art
        print(f"  Uploading cover art...")
        cover_filename = f"cover_{name.lower().replace(' ', '_').replace('-', '_')}.png"
        cover_id = upload_image(product['cover'], cover_filename)
        if not cover_id:
            results.append({'name': name, 'status': 'COVER UPLOAD FAILED'})
            continue
        time.sleep(0.5)
        
        # Upload mockups
        mockup_ids = []
        for i, mockup_path in enumerate(product.get('mockups', [])):
            print(f"  Uploading mockup {i+1}...")
            m_filename = f"mockup_{i+1}_{name.lower().replace(' ', '_').replace('-', '_')}.png"
            m_id = upload_image(mockup_path, m_filename)
            if m_id:
                mockup_ids.append(m_id)
            time.sleep(0.5)
        
        # Build images array: cover first, then mockups, then flat-lay
        images = []
        images.append({'src': cover_id, 'position': 'front', 'is_default': True, 'is_selected_for_publishing': True})
        for m_id in mockup_ids:
            images.append({'src': m_id, 'position': 'front', 'is_default': False, 'is_selected_for_publishing': True})
        if flatlay_id:
            images.append({'src': flatlay_id, 'position': 'front', 'is_default': False, 'is_selected_for_publishing': True})
        
        # Update product images via Printify API
        print(f"  Updating product images (cover first)...")
        update_payload = {'images': images}
        r = requests.put(
            f'{BASE_URL}/shops/{SHOPIFY_SHOP_ID}/products/{printify_id}.json',
            headers=HEADERS,
            json=update_payload
        )
        update_result = r.json()
        
        if r.status_code in [200, 201]:
            print(f"  ✅ Images updated successfully")
            
            # Re-publish to push changes to Shopify
            pub = requests.post(
                f'{BASE_URL}/shops/{SHOPIFY_SHOP_ID}/products/{printify_id}/publish.json',
                headers=HEADERS,
                json={'title': True, 'description': True, 'images': True, 'variants': True, 'tags': True}
            )
            print(f"  Re-published: {pub.status_code}")
            results.append({'name': name, 'status': 'SUCCESS', 'printify_id': printify_id})
        else:
            print(f"  ❌ Update failed: {r.status_code} — {update_result}")
            results.append({'name': name, 'status': f'FAILED: {r.status_code}', 'error': str(update_result)})
        
        time.sleep(1)

    print("\n=== FINAL SUMMARY ===")
    for r in results:
        status_icon = '✅' if r['status'] == 'SUCCESS' else '❌'
        print(f"  {status_icon} {r['name']}: {r['status']}")

if __name__ == "__main__":
    main()
