# Printify API Guide for Image Updates

When updating product images via the Printify API, you must interact with several endpoints in a specific sequence.

## 1. Upload Images
**Endpoint:** `POST /v1/uploads/images.json`

You must upload images to Printify's media library before attaching them to a product.

**Payload:**
```json
{
  "file_name": "image.png",
  "contents": "base64_encoded_string_here"
}
```

**Response:** Returns an object containing the image `id` which you need for the next step.

*Note: Printify does not support `.webp` uploads via API. Convert to `.png` or `.jpg` first.*

## 2. Update Product Images
**Endpoint:** `PUT /v1/shops/{shop_id}/products/{product_id}.json`

To change the primary image (the one that appears first on Shopify), you must send an array of image objects where the first item is the desired primary image.

**Payload:**
```json
{
  "images": [
    {
      "src": "image_id_from_step_1",
      "position": "front",
      "is_default": true,
      "is_selected_for_publishing": true
    },
    {
      "src": "another_image_id",
      "position": "front",
      "is_default": false,
      "is_selected_for_publishing": true
    }
  ]
}
```

## 3. Publish Changes
**Endpoint:** `POST /v1/shops/{shop_id}/products/{product_id}/publish.json`

Updating the product via API only changes it within Printify. You must trigger a publish event to push those changes to the connected sales channels (Shopify, TikTok Shop, etc.).

**Payload:**
```json
{
  "title": true,
  "description": true,
  "images": true,
  "variants": true,
  "tags": true
}
```
