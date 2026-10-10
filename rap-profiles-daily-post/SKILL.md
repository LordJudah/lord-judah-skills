---
name: rap-profiles-daily-post
description: Produce the daily Rap Profiles post for Lord Judah's 51-artist hip-hop series — profile card image, caption, ElevenLabs narration in the Lord Judah voice, narration-only 9:16 reel, and dated Google Drive delivery. Use when asked to generate the daily post, daily rapper profile, series content, or any Rap Profiles asset (card, caption, narration, reel, Drive upload).
---

# Rap Profiles Daily Post

Produce one complete daily post package for the Rap Profiles series and deliver it to Google Drive. For Volume II, read the shared `Rap Profiles Volume II — Daily Posting Agent Video Tracker.md` (or `VOLUME2_DAILY_POSTING_AGENT_VIDEO_TRACKER.csv`) first, then read `references/series_reference.md` for Drive folder IDs, visual specifications, and asset conventions.

## Daily package (5 assets)

| Asset | Format | Notes |
| --- | --- | --- |
| Profile card | PNG, 4:5 | Navy/Off-White executive style per visual spec |
| Caption | TXT | Caption template + full hashtag stack |
| Narration | MP3 | Lord Judah ElevenLabs voice, ~30-55s |
| Narration script | MD | The exact spoken text |
| Reel | MP4, 1080x1920 | Narration-only video of the card |

## Seventh-day recap package

On Volume II Days **07, 14, 21, 28, 35, 42, 49, and 56**, create a narrated weekly recap using the seven completed artist cards from that block. Build an **8-slide carousel**: Slide 1 uses the official Rap Report Card logo and recap title; Slides 2–8 use the seven Style A artist cards. Create a narration-only vertical reel from the carousel, a recap script, and a caption. The recap tells viewers which seven artists were rated, directs them to `rapprofiles.app` for the full reviews, and invites them to comment **PROFILES** to activate the live ManyChat flow.

## Workflow

1. **Determine the day from the tracker.** Match the Eastern date to the Volume II tracker row. The tracker is the operational source of truth for the 60-day roster, artist, app-release time, report URL, direct-video status, and next action; do not infer the next artist from the older 51-artist PDF when working on Volume II.
2. **Honor the app gate.** Do not use a Volume II report URL in social copy until its daily report has opened at **3:00 PM Eastern** and the public page is reachable. Use the exact day-level URL from the tracker.
3. **Generate the profile card** with the image generation tool (4:5, high quality) using the visual spec and prompt pattern in the reference. Verify all five scores and the legacy line render correctly; regenerate if any text is wrong.
4. **Honor replacement cards.** If Lord Judah requests a card to be recreated, treat the newest approved card as the sole source of truth. Replace the prior card in the daily package, Content Library, recap carousel, and recap reel; never reuse an obsolete card because it was already archived.
5. **Write the caption** (TXT) and **narration script** (plain text, no markdown) from the templates in the reference. Compute the composite as the mean of the five scores, one decimal.
6. **Verify the voice before generating audio.** Confirm that the selected ElevenLabs voice is the user’s **Lord Judah Professional Voice Clone**, voice ID `q2n4EHze5vKn16p2mMV1`. If the selected voice cannot be confirmed, stop and ask before generating; use Hume only as the designated fallback if the clone is unavailable.
7. **Generate the narration:** `python3 scripts/generate_narration.py <script.txt> <output.mp3>` (requires `ELEVENLABS_API_KEY`; voice ID is hardcoded and user-confirmed).
8. **Build the reel:** `bash scripts/build_reel.sh <card.png> <narration.mp3> <output.mp4>`. Extract a frame with ffmpeg and visually QA that the full card is visible.
9. **Schedule/publish according to the division of labor.** Treat **4:00 PM Eastern daily** as the default social-post time unless Lord Judah explicitly changes it. Lord Judah handles Instagram; the agent handles TikTok only when asked.
10. **Deliver to Drive:** create the dated subfolder in DAILY POST and the artist subfolder in Content Library, upload dated copies to the former and undated masters to the latter (naming conventions and folder IDs in the reference).
11. **Handle YouTube links truthfully.** The tracker is a handoff/verification record, not permission to upload or publish. Until a direct video is public and verified, use the official playlist fallback; never fabricate, guess, or substitute a private, unlisted, unrelated, or mismatched URL. After publication, record `Day NN — https://youtube.com/shorts/VIDEO_ID` for verification.
12. **Report** with the card, caption, narration, and reel attached; state which artist is next.

11. **Create the seventh-day recap when due.** Use only the seven preceding completed cards; do not include an unreleased day or fabricate scorecard details. Use the official Rap Report Card logo supplied by the app/brand source—do not create an alternate logo. Keep the carousel and recap reel in Style A.

## Hard constraints (user-locked preferences)

- **Never bake background music into reels.** Narration-only audio; Lord Judah adds commercially licensed music in Instagram edits himself. The standalone bed beat in Content Library is an archive asset only.
- Narration voice is always the user’s **ElevenLabs Lord Judah Professional Voice Clone**, voice ID `q2n4EHze5vKn16p2mMV1`; confirm the selected voice before each new generation. Narration always opens with "Peace." and closes with "Let's build."
- When directing listeners to the official site in narration, write and speak `Rap Profiles Dot App`—never spell or read the URL as `www`, `www.rapprofiles.app`, or `rapprofiles.app`.
- Include exactly five tailored hashtags in each social caption: artist name, relevant hip-hop/history context, series identifier, and Judah Bless Ent brand tag as appropriate.
- Recap captions must include the CTA: `Comment PROFILES to receive the full Rap Profiles experience.` The live ManyChat flow accepts `PROFILES`, `profiles`, and `Profiles`, sends the link only after the user taps through its buttons, and routes to `https://rapprofiles.app`.
- Keep the Navy/Off-White executive identity consistent with the rapper_rankings.xlsx workbook and prior cards.
- When Lord Judah appears in an image (covers, milestones), use his Drive reference photos, depict him physically fit, and vary pose/camera angle across posts.
- User posts to Instagram manually; agent handles TikTok posting if asked.
