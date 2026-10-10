---
name: ljb-brand-campaign-launcher
description: "End-to-end Lord Judah / Judah Bless Ent brand content campaign launcher. Use when: building a multi-day social media campaign from a theme or brand document (manifesto, brand bible, content calendar); generating cinematic campaign visuals paired with brand-aligned captions; scheduling a full campaign across Instagram and Threads via Blotato. Covers the full pipeline: AI visual generation, caption writing, image upload, Blotato scheduling, and queue verification. Produces scheduled posts at 4PM EDT daily."
---

# LJB Brand Campaign Launcher

## Overview

This skill launches a fully scheduled social media campaign for Lord Judah / Judah Bless Ent from a content brief or brand document. Four stages always run in order:

**GENERATE → CAPTION → UPLOAD → SCHEDULE**

---

## Stage 1 — Generate Campaign Visuals

### Visual Style Rules (CRITICAL)

- **Aspect ratio:** `4:5` for Instagram/Threads posts
- **Brand colors:** Black (foundation), Gold (royalty), Deep Purple (spirituality), Crimson Red (passion), Metallic Silver (technology)
- **Typography in images:** Bold, impactful, minimal words — title/theme only
- **No people required** for symbolic posts (lion, geometry, light rays); use avatar figure for personal/teaching posts
- **Avatar figure:** Powerful muscular Black man, long flowing dreadlocks, full salt-and-pepper beard, deep brown skin, gold chain, broad shoulders
- **Always generate Day 1 visual first**, then use it as a `references` image for all subsequent days to ensure visual consistency across the campaign

### Prompt Template

```
Cinematic 4:5 social media post graphic for Lord Judah / Judah Bless Ent.
[SCENE DESCRIPTION — environment, lighting, mood].
[SUBJECT — symbolic or avatar figure with specific details].
Bold text overlay: '[DAY THEME TITLE]'.
[OPTIONAL BRAND ELEMENT — lion, crown, sacred geometry, soundwaves].
Brand colors: black, gold, deep purple, crimson red, metallic silver.
Cinematic, high contrast, [MOOD WORD]. No extra text.
```

### Output Path

```
/home/ubuntu/campaign_[NAME]/day[N]_[theme].png
```

Generate all visuals in batches of 2–3 using `generate_image` before moving to Stage 2.

---

## Stage 2 — Write Captions

See `references/caption-rules.md` for full platform rules and brand voice guide.

### Quick Reference

| Platform | Max Hashtags | Max Characters | Voice |
|---|---|---|---|
| Instagram | 5 | ~2,200 (practical) | Poetic, layered, brand-rich |
| Threads | No limit | 500 | Punchy, direct, 1–3 hashtags |

**Core hashtags:** `#LordJudah #JudahBlessEnt #TrueHeART`

**Always include** `www.lordjudah.com` as a CTA in at least one post per campaign (Day 1 or Day 7).

---

## Stage 3 — Upload Images

Use `manus-upload-file` to batch-upload all campaign images at once:

```bash
manus-upload-file /home/ubuntu/campaign_[NAME]/day1_*.png /home/ubuntu/campaign_[NAME]/day2_*.png ...
```

Save all returned CDN URLs — they are required for Stage 4.

---

## Stage 4 — Schedule via Blotato

### CRITICAL Rules

- Use `scheduledTime` (NOT `scheduledAt`) — wrong key silently posts immediately
- `accountId` MUST be a **string**, not a number (e.g., `"1005"` not `1005`)
- Instagram: max **5 hashtags** per post — Blotato enforces this strictly
- Threads: max **500 characters** — trim captions before scheduling
- Default schedule: **4:00 PM EDT** = `T16:00:00-04:00`

### Platform Account IDs

| Platform | Account | ID |
|---|---|---|
| Instagram | @lordjudah | `"1005"` |
| Threads | @lordjudah | `"310"` |
| Twitter/X | @judahblessent | `"846"` |
| TikTok | @judahblessent | `"1217"` |

### Schedule Post (MCP call pattern)

```json
{
  "accountId": "1005",
  "platform": "instagram",
  "text": "[CAPTION — max 5 hashtags]",
  "mediaUrls": ["[CDN_URL_FROM_STAGE_3]"],
  "scheduledTime": "2026-07-28T16:00:00-04:00"
}
```

Call `blotato_create_post` once per platform per day. Schedule Instagram first, then Threads.

### Verification (REQUIRED before confirming to Lord Judah)

After all posts are scheduled, call `blotato_list_schedules` and confirm every new post shows a future `scheduledAt` date. Never confirm completion until verified.

---

## Full Campaign Checklist

```
[ ] Stage 1: All N visuals generated (4:5 PNG, brand colors, day theme title)
[ ] Stage 2: Captions written — Instagram (≤5 hashtags) and Threads (≤500 chars)
[ ] Stage 3: All images uploaded via manus-upload-file, CDN URLs saved
[ ] Stage 4: Instagram posts scheduled (blotato_create_post, accountId "1005")
[ ] Stage 4: Threads posts scheduled (blotato_create_post, accountId "310")
[ ] Verified: blotato_list_schedules confirms all posts show future scheduledAt
[ ] Delivered: Confirm to Lord Judah with full schedule table
```

---

## Delivery Format

Always close with a confirmation table:

| Day | Date | Theme | Visual Title | Status |
|---|---|---|---|---|
| 1 | Mon Jul 28 | The Covenant | THE COVENANT | Scheduled 4PM EDT |
| ... | ... | ... | ... | ... |

---

## Common Errors & Fixes

| Error | Cause | Fix |
|---|---|---|
| `invalid_type: accountId` | Passed number not string | Use `"1005"` not `1005` |
| `max 5 hashtags` | Instagram limit | Trim to 5 hashtags max |
| `500 character limit` | Threads limit | Shorten caption to ≤500 chars |
| Post fires immediately | Used `scheduledAt` instead of `scheduledTime` | Always use `scheduledTime` |
