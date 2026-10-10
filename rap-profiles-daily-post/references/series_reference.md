# Rap Profiles Series Reference

## Source data

Artist data lives in the Manus project "RAP PROFILES" shared files at `/home/ubuntu/projects/rap-profiles-1d0d536b/`:

- `Rapper Profiles by LORD JUDAH.pdf` — the canonical source. 51 artists listed alphabetically/numbered; each entry contains: Alias(es), five criteria scores out of 10 (Lyrical Complexity, Storytelling Ability, Flow, Originality, Impact), Strengths, Associations, and Legacy notes.
- `rapper_rankings.xlsx` — Master Scorecard workbook (Navy/Off-White executive styling) with the same data plus composite averages.

For Volume I, use the numbered PDF/workbook order and existing DAILY POST folders. For Volume II, use the shared `Rap Profiles Volume II — Daily Posting Agent Video Tracker.md` or `VOLUME2_DAILY_POSTING_AGENT_VIDEO_TRACKER.csv` as the roster and release source of truth. The tracker covers 60 daily rows, with the app report gate at 3:00 PM Eastern and the default social-post preference at 4:00 PM Eastern.

Volume II operating rules:

- Confirm the matching tracker row and public report URL only after the 3:00 PM Eastern app gate opens.
- Use the exact day-level report URL in the caption and YouTube description.
- The tracker records verified direct YouTube handoffs; it does not publish, upload, schedule, or alter captions/ManyChat.
- Until an individual YouTube video is public and verified, retain the official playlist fallback. Never invent or substitute a video link.
- Lord Judah handles Instagram posting; the agent handles TikTok only when asked. Default social scheduling is 4:00 PM Eastern daily.
- If a profile card is recreated, the newest approved card replaces the prior version everywhere: daily posting folder, Content Library, recap carousel, and recap reel.
- Before any audio generation, verify the selected voice is the **ElevenLabs Lord Judah Professional Voice Clone**, ID `q2n4EHze5vKn16p2mMV1`. Ask for confirmation if the selected voice cannot be verified; use Hume only as the designated fallback when the clone is unavailable.

## Seventh-day recap cadence

Create a weekly narrated recap on Volume II Days **07, 14, 21, 28, 35, 42, 49, and 56**. Each recap covers the seven completed artist profiles in that block:

| Recap day | Profiles covered |
| ---: | --- |
| 07 | Days 01–07 |
| 14 | Days 08–14 |
| 21 | Days 15–21 |
| 28 | Days 22–28 |
| 35 | Days 29–35 |
| 42 | Days 36–42 |
| 49 | Days 43–49 |
| 56 | Days 50–56 |

The recap package contains: (1) an 8-slide carousel with the official Rap Report Card logo on Slide 1 and the seven completed Style A artist cards on Slides 2–8; (2) a narration script; (3) Lord Judah ElevenLabs narration; (4) a narration-only vertical reel using the carousel; and (5) a caption with exactly five tailored hashtags. The spoken CTA uses `Rap Profiles Dot App`; written captions may use the live URL `https://rapprofiles.app`.

Use this ManyChat CTA in recap captions: `Comment PROFILES to receive the full Rap Profiles experience.` The live **Rap Profiles — PROFILES comment-to-DM** automation accepts `PROFILES`, `profiles`, and `Profiles`, replies publicly with one of its approved rotating lines, then requires the user to tap through the DM buttons before sending the Rap Profiles link. Do not promise a link delivery without that tap sequence.

Approved ManyChat flow: rotating public reply — `Rap Profiles is in your DMs. Study the culture.`, `Check your DMs. The full report card is waiting.`, or `Sent. Step into Rap Profiles.` First DM: `Peace. Tap below and I'll send you the full Rap Profiles experience.` with **Send me the link**. Second DM: `Peace. You just stepped into Rap Profiles, hip-hop's living report card. Full scorecards, the Dojo, and the Songbook are waiting.` with **Enter Rap Profiles** linking to `https://rapprofiles.app`.

## Google Drive structure (gws CLI, IDs confirmed)

| Location | Folder ID |
| --- | --- |
| Main delivery folder | `1FO9ITLftrihRfUCzTKrksqDvBp1nGmKn` |
| DAILY POST (day-of-posting files) | `1l2eUbo9gB4UdLwaprzQZf4rMeHyWQ9KH` |
| Content Library (master archive) | `1HDNOTBADA4QB1qniXa6cCD-9byKqQn3N` |
| Content Library / Day 01 - 21 Savage | `1Yo-xYnXLH9HZwvSvU7oTiIUcl_5Q6Pah` |
| Content Library / Series Intro | `15NAnTGqNpdEYjLS4L0bpM0SO8uC8gETk` |
| Lord Judah Reference Photos | `144MNwGy6EGdQ9mLupe1L92GeTGiwZgrJ` |

Conventions:

- In DAILY POST, create one dated subfolder per day named `YYYY-MM-DD - Day NN - Artist Name`, containing dated files named `YYYY-MM-DD_DayNN_Artist_Type.ext` (e.g. `2026-07-10_Day01_21Savage_ProfileCard.png`, `_Caption.txt`, `_Narration_LordJudah.mp3`, `_NarrationScript.md`, `_Reel.mp4`).
- In Content Library, create one subfolder per artist named `Day NN - Artist Name` with undated master copies.
- Upload: `gws drive files create --upload FILE --json '{"name": "...", "parents": ["FOLDER_ID"]}' --format json`
- Create folder: `gws drive files create --json '{"name": "...", "mimeType": "application/vnd.google-apps.folder", "parents": ["PARENT_ID"]}' --format json`

## Profile card visual spec

Executive Navy Blue + Off-White scheme matching the rapper_rankings.xlsx workbook. Aspect 4:5, generate at high quality (text-heavy). Layout top to bottom:

1. Kicker: `RAP PROFILES: NN` (small, letterspaced, off-white, thin rules either side)
2. Artist name: huge bold condensed off-white typography
3. Cinematic navy-duotone portrait of the artist
4. Five-column score grid: LYRICAL COMPLEXITY / STORYTELLING / FLOW / ORIGINALITY / IMPACT, each with big score and small `/10`
5. LEGACY block: column icon + one-line legacy statement in serif

Prompt pattern that worked: "A highly professional, executive-styled infographic profile card for 'RAP PROFILES', designed for Instagram. Strict Navy Blue and Off-White color scheme... [layout description with exact scores and legacy line] ...polished, educational, premium, resembling a high-end cultural index. Clean lines, strong typography, no messy graffiti."

When casting Lord Judah (series covers, milestone posts): use reference photos from the Drive reference folder (e.g. `LORD JUDAH THE MYSTIC IN THE CITY.jpg`, file ID `10qw1dqRhtKyxXd_LtvJHuHydpICCElwp`); depict him physically fit, long locs, graying beard, authoritative; vary pose and camera angle across posts.

## Narration script template (~30-55s spoken)

```
Peace. Day {N} of Rap Profiles, and we're {location/era hook}: {Artist}.
{2-3 sentences: alias, what defined them, strengths, associations, legacy — conversational, reverent, teacher-through-music voice.}
The breakdown: Lyrical complexity, {x}. Storytelling {hits/clocks} a {x}. Flow at {x}. Originality, {x}. Impact, {x}. A composite score of {avg} out of 10.
{One-line takeaway}. {Engagement CTA — favorite verse/track in the comments}. Let's build.
```

Keep it plain text for TTS (no markdown). Signature opener "Peace." and closer "Let's build." are mandatory brand elements.

**Site pronunciation rule:** When a narration includes the official website CTA, write it as `Rap Profiles Dot App` for ElevenLabs pronunciation. Do not write `www.rapprofiles.app` or `rapprofiles.app` in spoken narration.

## Caption template

```
RAP PROFILES: DAY {N} — {ARTIST NAME}

{Hook line with emoji}

{Short paragraph: artist story, strengths, associations}

THE BREAKDOWN:
[emoji] Lyrical Complexity: {x}/10
[emoji] Storytelling: {x}/10
[emoji] Flow: {x}/10
[emoji] Originality: {x}/10
[emoji] Impact: {x}/10
COMPOSITE: {avg}/10

{Legacy line}

{CTA: agree/disagree + tag a friend + favorite verse}

{Exactly five tailored hashtags: artist name, relevant hip-hop/history context, series identifier, and Judah Bless Ent brand tag as appropriate}
```

## Day 1 data (completed example)

21 Savage — LC 7.0, ST 7.5, Flow 8.0, Orig 7.5, Impact 8.0, composite 7.6. Alias: Saint Laurent Don. Strengths: menacing deadpan delivery, gritty street storytelling, elite trap production synergy. Associations: Metro Boomin, "Issa Album", Atlanta trap scene. Legacy: pioneered modern trap with deadpan delivery; brought immigration commentary to the forefront.
