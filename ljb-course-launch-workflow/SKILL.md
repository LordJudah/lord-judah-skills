---
name: ljb-course-launch-workflow
description: "End-to-end course launch workflow for Judah Bless Ent / True He(ART) Academy. Use when launching a new online course: creates the Shopify product, generates AI cover image and promotional assets (16:9 banner + 9:16 Story), writes platform-optimized launch captions (Instagram, Threads, Twitter/X), and builds the ManyChat keyword automation flow. Covers the full pipeline from product creation to social launch."
---

# LJB Course Launch Workflow

This skill executes the full pipeline to launch a new course on the Judah Bless Ent Shopify store and promote it across social media with ManyChat automation.

## Workflow Overview

| Phase | Action | Tools |
|---|---|---|
| 1 | Create Shopify product | Shopify API script |
| 2 | Generate cover image (4:3) | `generate_image` |
| 3 | Upload cover to Shopify product | Shopify API script |
| 4 | Generate promo banner (16:9) | `generate_image` |
| 5 | Generate Story banner (9:16) | `generate_image` |
| 6 | Write launch captions | Creative writing |
| 7 | Build ManyChat flow | Reference guide |

---

## Phase 1 — Shopify Product Creation

Use the script at `scripts/create_course_product.py`. Set these variables at the top before running:

- `COURSE_TITLE` — e.g., `"True He(ART) Academy: Foundations"`
- `COURSE_PRICE` — e.g., `97.00`
- `COURSE_DESCRIPTION_HTML` — Full HTML product description (see `references/product_description_template.md`)
- `COURSE_TAGS` — e.g., `"Online Course, Education, Hip-Hop"`
- `COLLECTION_TITLE` — e.g., `"Online Courses"` (script creates it if it doesn't exist)

The script outputs the new **Product ID** — save it for Phase 3.

```bash
python3 /home/ubuntu/skills/ljb-course-launch-workflow/scripts/create_course_product.py
```

---

## Phase 2 — Course Cover Image (4:3)

Generate with `generate_image`, `aspect_ratio: "4:3"`, `quality: "high"`.

See `references/image_prompt_templates.md` for the full cover image prompt template. Key variables to fill: `{COURSE_TITLE}`, `{COURSE_SUBTITLE}`, `{INSTRUCTOR}`, `{BRAND_DOMAIN}`.

Save to: `/home/ubuntu/{slug}-course-cover.jpg`

---

## Phase 3 — Upload Cover to Shopify

Use `scripts/upload_course_image.py`. Set `PRODUCT_ID` (from Phase 1) and `IMAGE_PATH` before running.

```bash
python3 /home/ubuntu/skills/ljb-course-launch-workflow/scripts/upload_course_image.py
```

---

## Phase 4 — Promotional Banner (16:9)

Generate with `generate_image`, `aspect_ratio: "16:9"`, `quality: "high"`. Pass the cover image as `references` for visual consistency.

See `references/image_prompt_templates.md` for the 16:9 banner prompt template.

Save to: `/home/ubuntu/{slug}-promo-banner.jpg`

---

## Phase 5 — Story Banner (9:16)

Generate with `generate_image`, `aspect_ratio: "9:16"`, `quality: "high"`. Pass the cover image as `references`.

See `references/image_prompt_templates.md` for the 9:16 Story prompt template.

Save to: `/home/ubuntu/{slug}-story-banner.jpg`

---

## Phase 6 — Launch Captions

Write four caption sets using `references/caption_templates.md`. Fill in:
- `{COURSE_TITLE}`, `{COURSE_SUBTITLE}`, `{INSTRUCTOR}`
- `{MODULE_LIST}` — 4 modules with emoji and one-line description
- `{FINAL_PROJECT}` — what students produce at the end
- `{PRICE}`, `{BRAND_DOMAIN}`, `{PRODUCT_URL}`
- `{KEYWORD}` — ManyChat trigger word (e.g., `ENROLL`)

---

## Phase 7 — ManyChat Flow

See `references/manychat_flow_template.md` for the full setup guide including:
- Trigger configuration (Instagram comment keyword)
- Public comment reply rotation (3 variants)
- Initial DM with CTA button → Shopify product URL
- 24-hour follow-up DM
- Audience tagging (`Course Lead - {COURSE_TITLE}`)

**Key rule:** Always use ManyChat for comment auto-replies — never Make.com.

---

## Shopify API Credentials

Credentials are supplied through environment variables and are **never** committed to source:

| Variable | Value |
|---|---|
| `SHOPIFY_CLIENT_ID` | App client ID (Shopify Admin → Apps → Develop apps → your app) |
| `SHOPIFY_CLIENT_SECRET` | App client secret — treat as sensitive |
| `SHOPIFY_STORE` | Store domain, e.g. `your-store.myshopify.com` |

```bash
export SHOPIFY_CLIENT_ID="..."
export SHOPIFY_CLIENT_SECRET="..."
export SHOPIFY_STORE="your-store.myshopify.com"
```

The access token is short-lived (~24h) — all scripts handle token refresh automatically via the client_credentials grant using the Client ID and Secret from the environment. If any variable is missing, the scripts exit with a clear error rather than falling back to embedded values.

---

## Inflowkit Connection (Post-Launch)

After the Shopify product is live, connect course content in Inflowkit:
1. Shopify Admin → Apps → Inflowkit
2. Create Course → link to the Product ID from Phase 1
3. Add modules and upload video/PDF content per module
4. Publish — students who purchase get automatic access

Note: Inflowkit requires a live Shopify browser session to access. If the browser is not logged in, guide the user to log in at admin.shopify.com first.
