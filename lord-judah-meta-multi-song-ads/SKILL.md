---
name: lord-judah-meta-multi-song-ads
description: "Run a multi-song Meta Ads conversion campaign for Lord Judah music releases using Hypeddit Smart Links and the Meta Pixel. Use when asked to promote multiple songs simultaneously with paid ads, drive streams via conversion campaigns, or set up Hypeddit Smart Links for Meta Ads tracking. Covers Hypeddit Smart Link creation with ROC Nation rnd.fm destinations, Meta Pixel setup, campaign/ad set/ad configuration, and multi-ad duplication workflow. One campaign covers all 4 active releases."
---

# Lord Judah Multi-Song Meta Ads Strategy

## What This Does

Runs **one Meta Ads campaign** with **one ad set** and **multiple ads** (one per song), each pointing to a Hypeddit Smart Link that wraps the ROC Nation `rnd.fm` destination. Meta optimizes budget across all songs automatically — spend shifts to whichever song converts best.

**Conversion event tracked:** Hypeddit Smart Link Click (via Meta Pixel)

---

## Prerequisites

| Requirement | Status |
|---|---|
| Meta Ads Manager account | Must be connected to @lordjudah Facebook Page |
| Meta Pixel | Must be installed and verified in Events Manager |
| Hypeddit account | Set up at hypeddit.com |
| Hypeddit Smart Links (4 songs) | Create before launching campaign |
| Cover art creatives (9:16) | Already available |

---

## Phase 1 — Set Up Hypeddit Smart Links

Create one Smart Link per song. Each Hypeddit link wraps the existing ROC Nation smart link.

### Song → Link Mapping

| Song | Hypeddit URL (to create) | ROC Nation Destination |
|---|---|---|
| Blessed and Grateful | `hypeddit.com/lordjudah/blessed-and-grateful` | `https://rnd.fm/blessed-and-grateful-tblntf` |
| Just Walking With My Dog | `hypeddit.com/lordjudah/just-walking-with-my-dog` | `https://rnd.fm/just-walking-with-my-dog-dtal57` |
| Navigating The Way | `hypeddit.com/lordjudah/navigating-the-way` | `https://rnd.fm/navigating-the-way-tahsw5` |
| Battle For Earth | `hypeddit.com/lordjudah/battle-for-earth` | `https://rnd.fm/battle-for-earth-xjbvjl` |

### Hypeddit Smart Link Setup (per song)

1. Log in at **hypeddit.com** → Dashboard → **"Share Music"**
2. Click **"Select"** next to Smart Link
3. Enter the Spotify URL for the song → click **Next**
4. Select genre: **Hip Hop** → Next
5. Confirm Artist: **Lord Judah**, Title: **[Song Title]** → Next
6. Upload cover art (min 500x500px) → set dark color theme → Next
7. **Links section:** Add a **"Custom"** button → paste the `rnd.fm` URL → label it **"Listen Now"** → add all other streaming platforms if available → Next
8. **Link URL section:** Customize to `lordjudah/[song-slug]` → Next
9. **Tracking Pixels:** Add your **Meta Pixel ID** → Next
10. Confirm → **Create**

Repeat for all 4 songs. Save all 4 Hypeddit URLs before proceeding to Phase 2.

---

## Phase 2 — Build the Meta Ads Campaign

### Step 1 — Create the Campaign

1. Go to **Meta Ads Manager** → business.facebook.com/adsmanager
2. Click **"+ Create"**
3. Objective: **Engagement** → Continue
4. Name: `LJ - Multi-Song Streams - [Date]`
5. **Campaign Budget Optimization:** ON
6. Daily budget: **$10–$20/day** (split across all songs automatically)
7. Click **Next**

### Step 2 — Configure the Ad Set

1. **Name:** `LJ - Multi-Song - Ad Set`
2. **Conversion location:** Website
3. **Performance goal:** Maximize number of conversions
4. **Pixel:** Select your Meta Pixel
5. **Conversion event:** `Hypeddit Smart Link Click`
6. **Schedule:** Start date = today or first release date, End = 14–30 days
7. **Audience:**
   - Age: 18–45
   - Gender: All
   - Locations: United States + Tier 1 countries (UK, Canada, Australia)
   - Interests: Hip hop, conscious rap, Kendrick Lamar, J. Cole, Nas, Boom bap
8. Click **Next**

### Step 3 — Set Placements (CRITICAL)

1. Select **"Manual placements"** (NOT Advantage+)
2. **Turn OFF:** Facebook (all), Audience Network (all), Messenger (all)
3. **Keep ON — Instagram only:**
   - Instagram Feed ✅
   - Instagram Stories ✅
   - Instagram Reels ✅
   - Everything else ❌
4. Click **Next**

### Step 4 — Create the First Ad

1. **Name:** `LJ - Blessed and Grateful`
2. **Facebook Page:** Select the Lord Judah page
3. **Multi-advertiser ads:** Toggle **OFF**
4. **Ad setup:** Single image or video
5. **Creative:** Upload Blessed and Grateful cover art (9:16)
6. **Destination / Website URL:** Paste the Hypeddit Smart Link for Blessed and Grateful
7. **Call to action:** `Listen Now`
8. Preview → confirm correct

### Step 5 — Duplicate for Remaining Songs

1. Click the **three dots (⋯)** next to the first ad name
2. Select **"Quick Duplicate"**
3. In the duplicated ad:
   - Change **Name** to `LJ - Just Walking With My Dog`
   - Change **Website URL** to the JWWMD Hypeddit link
   - Change **Creative** to JWWMD cover art
4. Repeat for **Navigating The Way** and **Battle For Earth**
5. Confirm all 4 ads are in the same ad set

### Step 6 — Publish

1. Click **"Review to publish"**
2. Confirm all 4 ads show correct Hypeddit URLs and creatives
3. Click **Publish**

---

## Phase 3 — Monitor and Optimize (Days 3–7)

Check Ads Manager every 2–3 days:

| Metric | What to Look For |
|---|---|
| **Smart Link Clicks** | Primary conversion — aim for $0.50–$2.00 per click |
| **CPM** | Cost per 1,000 impressions — lower is better |
| **CTR** | Click-through rate — aim for 1%+ |
| **Video completion** | If using video creatives, 50%+ is strong |

**If one song is dramatically outperforming:** Pause the underperforming ads and increase budget on the winner.

---

## How This Works With the Cult Followers Skill

These two strategies run simultaneously and feed each other:

| Skill | Objective | Feeds Into |
|---|---|---|
| `lord-judah-cult-followers` | Video views → 95% viewers → Lookalike | Audience building |
| `lord-judah-meta-multi-song-ads` | Smart Link clicks → Stream conversions | Direct stream growth |

Run both at the same time. The Cult Followers campaign builds the audience; this campaign converts them into streams.

---

## Budget Reference

| Setup | Daily Budget | 14-Day Total |
|---|---|---|
| Minimum (4 songs) | $10/day | $140 |
| Recommended | $20/day | $280 |
| Aggressive | $40/day | $560 |

Combined with the Cult Followers skill ($5/day per song = $20/day for 4 songs), total daily spend across both strategies = **$30–$60/day**.

---

## Rules

- Always use **Manual Placements** — Instagram only
- Always toggle **Multi-advertiser ads OFF**
- Use **Hypeddit Smart Links** as the destination URL — never paste `rnd.fm` links directly (no pixel tracking)
- One ad set, multiple ads — do NOT create separate campaigns per song
- Hypeddit Pixel must be installed before launching the campaign
