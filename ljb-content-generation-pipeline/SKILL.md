---
name: ljb-content-generation-pipeline
description: "End-to-end LJB social media content generation pipeline for Lord Judah / Judah Bless Ent. Use when: building a new wardrobe collection from raw screenshots (jerseys, sneakers, backdrops); generating cinematic Lord Judah post images using the 3-layer outfit system; writing brand-aligned captions; scheduling posts via Blotato across Instagram, Threads, Twitter/X, and TikTok; or managing the LJB Content Generation Project Folder. Covers the full workflow from raw asset screenshots to scheduled, platform-optimized social posts."
---

# LJB Content Generation Pipeline

## Overview

This pipeline converts raw product screenshots into a fully scheduled social media campaign. Five stages always run in order: **BUILD → MATCH → GENERATE → CAPTION → SCHEDULE**.

---

## Lord Judah Likeness Rules (CRITICAL — read before any image generation)

- Always depict Lord Judah as **physically fit and athletic** — muscular, broad-shouldered, powerful frame
- Body standard reference: `/home/ubuntu/upload/ref_6.png` (rooftop athletic shot)
- Key features: long flowing dreadlocks, full salt-and-pepper beard, deep brown skin, gold chain
- **NEVER use "LJB" as an image prompt tag** — reserved exclusively for the Replicate LoRA
- Always pass reference photos directly into `generate_image_variation` for likeness consistency

---

## Stage 1 — Build Wardrobe Assets

### Collection Naming
Assign every new wardrobe set a unique code and name before starting.

| Code | Collection | Status |
|------|-----------|--------|
| TT | Tokyo Tiger | Complete — 13 looks |
| Next | Assign thematically | Pending |

### Crop Parameters (raw app screenshots ~1170×2532px)

| Asset | Top | Bottom | Left/Right | Output path |
|-------|-----|--------|------------|-------------|
| Jersey | 30% | 12% | 5% | `shirt_inventory/cropped/` |
| Sneaker | 12–26% | 38–42% | 5% | `shirt_inventory/sneakers/` |
| Backdrop | 28% | 10% | 0% | `shirt_inventory/backdrops/` |

View each sneaker image individually before finalizing crop — UI chrome placement varies per screenshot.

Use `scripts/crop_assets.py` as the template for all cropping operations.

### Export Naming Convention
```
[COLLECTION]_assets/
├── jerseys/    → [CODE]-[##]_jersey.png
├── sneakers/   → [CODE]-[##]_sneaker.png
└── backdrops/  → [CODE]-[##]_backdrop.png
```
ZIP as `[COLLECTION]_assets_CLAUDE_LORD_JUDAH.zip` for extraction to `E:\CLAUDE LORD JUDAH\[COLLECTION]_assets\`.

---

## Stage 2 — Match 3-Layer Looks

Apply all four matching criteria simultaneously:
- **Color harmony** — dominant palette alignment between jersey, sneaker, backdrop
- **Thematic resonance** — subject matter echoes (koi→koi pond, samurai→temple, wave→wave)
- **Cultural depth** — aesthetic consistency within the collection's theme
- **True He(ART) healing energy** — spiritual, reflective, empowering environments

Build the full inventory sheet using `scripts/build_inventory.py`.
Brand colors: BG `(8,8,12)`, accent gold `(200,160,60)`, teal `(80,180,140)`.

See `references/tt_lookup.md` for the complete Tokyo Tiger matching table.

---

## Stage 3 — Generate Post Images

### Prompt Template
```
A cinematic 9:16 portrait of a powerful, muscular Black man with long flowing dreadlocks
and a full salt-and-pepper beard, deep brown skin, broad shoulders, athletic build.
He wears [JERSEY DESCRIPTION]. He wears [SNEAKER DESCRIPTION].
He stands before [BACKDROP DESCRIPTION]. [LIGHTING/MOOD].
Locs flowing, gold chain visible. [VIBE ENERGY].
Cinematic lighting. No text overlays. Portrait 9:16.
```

### References (always include all four)
```python
references=[
    "/home/ubuntu/upload/ref_6.png",
    "/home/ubuntu/TT_assets/jerseys/[CODE]-[##]_jersey.png",
    "/home/ubuntu/TT_assets/backdrops/[CODE]-[##]_backdrop.png",
    "/home/ubuntu/TT_assets/sneakers/[CODE]-[##]_sneaker.png"
]
```

Use `generate_image_variation` — always pass reference images. Output aspect ratio: `9:16`.

Output path: `/home/ubuntu/LJB_Content_Generation/02_Posts/[COLLECTION]_Collection/[CODE]-[##]/[CODE]-[##]_post.png`

---

## Stage 4 — Write Captions

See `references/caption_framework.md` for full brand voice guide and templates.

| Platform | Format |
|----------|--------|
| Instagram | 3–5 lines poetic copy + outfit tag + brand tag + max 5 hashtags |
| Threads | Same as Instagram, slightly condensed |
| Twitter/X | 2–3 punchy lines + outfit code + @judahblessent |
| TikTok | Single flowing paragraph, no line breaks, same hashtags |

Core hashtags: `#LordJudah #JudahBlessEnt #[CollectionName] #TrueHeART`

---

## Stage 5 — Schedule via Blotato

### CRITICAL: Correct Parameter

**Use `scheduledTime`** (NOT `scheduledAt`). Using `scheduledAt` silently fails and posts immediately.

```python
payload = {
    "accountId": account_id,
    "platform": platform,
    "text": caption,
    "mediaUrls": [public_url],
    "scheduledTime": "2026-05-03T16:00:00-04:00",  # ISO 8601 with EDT offset
}
```

### Platform Account IDs

| Platform | Account | ID |
|----------|---------|-----|
| Instagram | @lordjudah | 1005 |
| Threads | @lordjudah | 310 |
| Twitter/X | @judahblessent | 846 |
| TikTok | @judahblessent | 1217 |

### TikTok Extra Fields (always include)
```python
{
    "privacyLevel": "PUBLIC_TO_EVERYONE",
    "disabledComments": False,
    "disabledDuet": False,
    "disabledStitch": False,
    "isBrandedContent": False,
    "isYourBrand": False,
    "isAiGenerated": True
}
```

### Scheduling Workflow
1. Upload: `blotato_create_presigned_upload_url` → PUT to presigned URL
2. Schedule: `blotato_create_post` with `scheduledTime`
3. **Verify**: `blotato_list_schedules` — confirm every post shows a future `scheduledAt`
4. Never confirm to Lord Judah until queue is verified

Default schedule: **4:00 PM EDT** (`T16:00:00-04:00`), one look per day, all four platforms.

Use `scripts/schedule_posts.py` as the template for batch scheduling.

---

## Project Folder Structure

```
LJB_Content_Generation/
├── 00_Brand_Assets/references/   ← Lord Judah reference photos + likeness notes
├── 01_Wardrobe_System/
│   ├── [COLLECTION]_assets/jerseys|sneakers|backdrops/
│   └── inventory_sheets/
├── 02_Posts/[COLLECTION]_Collection/[CODE]-[##]/
├── 03_Captions/
├── 04_Videos/
└── 05_Future_Collections/
```

---

## Post Request Protocol

When Lord Judah says "Post TT-07 — Instagram Reel, motivational caption":
1. Look up TT-07 in `references/tt_lookup.md`
2. Pull the three asset files
3. Generate image (Stage 3)
4. Write captions (Stage 4)
5. Schedule (Stage 5) — verify queue before confirming
