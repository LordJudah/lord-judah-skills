---
name: printify-mockup-upgrade
description: "Reusable workflow for upgrading Printify product mockups on Shopify. Use for: generating AI lifestyle mockups based on cover art, uploading them via Printify API, and setting the cover art as the primary listing image."
---

# Printify Mockup Upgrade

This skill automates the process of replacing generic Printify mockups with high-quality, culturally diverse AI lifestyle mockups and setting custom cover art as the primary product image.

## Overview

Printify's default mockup generator sets generic images as the primary product photo. This workflow solves that by:
1. Converting any `.webp` cover art to `.png` (Printify API requirement).
2. Generating brand-aligned AI lifestyle mockups composited with the cover art.
3. Uploading all images via the Printify API.
4. Reordering the image array so the cover art is position 1 (primary), followed by lifestyle shots.
5. Re-publishing the product to push changes to Shopify/TikTok Shop.

## Prerequisites

- `OPENAI_API_KEY` or built-in image generation capability for lifestyle mockups.
- Printify Personal Access Token (Bearer token).
- Printify Shop ID.
- Target Shopify product GIDs (to map to Printify internal IDs).

## Workflow Steps

### 1. Prepare Cover Art
Ensure all cover art files are `.png` or `.jpg`. Printify API will reject `.webp` files.
Use `scripts/convert_webp_to_png.py` if needed.

### 2. Generate Lifestyle Mockups
Use AI image generation to create diverse lifestyle mockups.
- **Reference 1:** The specific cover art image.
- **Reference 2:** A blank lifestyle template (e.g., Black man urban setting, Latina woman streetwear setting).
- **Prompt:** "Product mockup photo for a conscious hip-hop streetwear brand. A stylish [Subject] wearing a solid black graphic t-shirt with the '[Design Name]' design... Editorial streetwear photography, warm natural light. 3/4 body shot. No text overlays."

### 3. Execute the Update Script
Use the bundled `scripts/update_product_images.py` to handle the API orchestration.
You must update the `TOKEN`, `SHOPIFY_SHOP_ID`, and the `PRODUCTS` list in the script before running.

## Bundled Resources

- `scripts/update_product_images.py`: The core API orchestration script.
- `scripts/convert_webp_to_png.py`: Utility for format conversion.
- `references/printify_api_guide.md`: Details on the Printify API endpoints used.
