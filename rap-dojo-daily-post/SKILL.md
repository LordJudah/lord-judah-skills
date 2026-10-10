---
name: rap-dojo-daily-post
description: "Produce the daily Rap Dojo post (Days 25–51) running alongside Rap Profiles. Use when asked to generate the daily Dojo post, Dojo master study, Dojo kata, or any Rap Dojo series asset. Includes generating the crimson/charcoal Dojo card, Dojo-specific caption with feeler CTAs, ElevenLabs Sensei narration, and 9:16 reel, delivered to Google Drive."
---

# Rap Dojo Daily Post

Produce one complete daily post package for the Rap Dojo series (running Days 25–51 parallel to Rap Profiles) and deliver it to Google Drive. Read `references/dojo_reference.md` first for the 26-day content map, visual spec, script/caption templates, and Drive folder IDs.

## Daily package (5 assets)

| Asset | Format | Notes |
| --- | --- | --- |
| Dojo Card | PNG, 4:5 | Crimson/Charcoal/Gold Dojo style per visual spec |
| Caption | TXT | Caption template + daily Feeler CTA + hashtag stack |
| Narration | MP3 | Lord Judah ElevenLabs voice (The Sensei tone), ~45-60s |
| Narration script | MD | The exact spoken text |
| Reel | MP4, 1080x1920 | Narration-only video of the padded card |

## Workflow

1. **Determine the day.** Check the `rap_dojo_26_day_strategy.md` file (or `references/dojo_reference.md`) to see what today's Dojo Topic is based on the day number (25–51).
2. **Gather data (if Master Study).** If the day is a Master Study (Days 26-51 alongside an artist), pull the corresponding artist's scores and legacy from the `rapper_rankings.xlsx` Master Scorecard.
3. **Generate the Dojo card** with the image generation tool (4:5, high quality) using the visual spec in the reference. Verify all text renders correctly; regenerate if any text is wrong.
4. **Write the caption** (TXT) and **narration script** (plain text, no markdown) from the templates in the reference. **CRITICAL:** Include the specific "Feeler / CTA Focus" question for that day from the content map.
5. **Generate the narration:** Use ElevenLabs with Voice ID `q2n4EHze5vKn16p2mMV1`. Use the `scripts/gen_dojo_narration.py` script.
6. **Build the reel:** The `gen_dojo_narration.py` script automatically pads the image to 9:16 (with `#1A1A1A` background) and builds the MP4 reel.
7. **Deliver to Drive:** Create the dated subfolder in the Rap Dojo `DAILY POST` folder (ID: `1NVEn4r8CyK3bmRclGiO61f-eFLGwkvTN`), upload the 5 assets.
8. **Report** to the user with the card, caption, narration, and reel attached.

## Hard constraints (user-locked preferences)

- **Never bake background music into reels.** Narration-only audio; Lord Judah adds commercially licensed music manually.
- Narration voice is always ElevenLabs voice `q2n4EHze5vKn16p2mMV1` (Hume is fallback only). Narration always opens with "Peace." and closes with "Let's build."
- Keep the Crimson/Charcoal/Gold Dojo identity distinct from the Rap Profiles Navy/Off-White identity.
- User posts to Instagram manually.
