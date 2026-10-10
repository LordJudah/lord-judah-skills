# Apify Integration — Wiring the Transmuter

How to run the transmuter inside an **Apify → AI → post** workflow.

---

## Pipeline Map

```
[Scraper] → [Dataset] → [AI step] → [post_text] → [Sheets / Make] → [optional: Blotato scheduling]
```

| Segment | Recommended tool | Notes |
|---|---|---|
| Scrape | Any X/Twitter, Threads, or Reddit scraper actor | One thread per dataset item, or reassemble from parts (below) |
| AI step | LLM Dataset Processor-style actor, Apify AI, or an LLM module in Make/n8n | Load `templates/transmuter-prompt.txt` as the prompt |
| Output | Single column `post_text` (+ `verdict`, `source_url`) | Write back to the same dataset or out to Sheets |
| Route | Google Sheets (Apify integration) or Make | Optional handoff to Blotato for scheduling |

---

## Field Mapping

Map the placeholder `{{PASTE_THREAD_TEXT_HERE}}` to your scraper's text field. Common names by source:

| Source | Common field |
|---|---|
| X / Twitter scrapers | `text`, `fullText`, `full_text`, `tweet.text` |
| Generic single-post scrapers | `content`, `post_text`, `description` |
| Threads scrapers | `text`, `caption` |

### Thread reassembly (when a thread arrives as multiple items)

```
group_by(conversationId or threadId)
  → sort by createdAt (ascending)
  → join with two newlines
  → feed the joined string into the placeholder
```

Store the joined block, not single tweets — the transmuter needs the full arc to enumerate steps correctly.

---

## Model Guidance

- Use a **top-tier creative-writing LLM**. Small/cheap models flatten the voice, drop steps, and leak source phrasing.
- Set temperature moderately high (~0.8–1.0) for voice, but rely on the prompt's hard constraints (step coverage, no verbatim, fixed hashtags, SKIP clause) to keep it disciplined.
- Output column: `post_text`. If your actor supports structured output, request JSON:

```json
{ "verdict": "OK | SKIP", "post_text": "..." }
```

`verdict` lets you auto-filter non-strategy threads in the Sheets/Make step.

---

## Pre-Filter (save tokens before the AI step)

Only send likely strategy threads to the LLM. Signals: "here's how," "steps," "system," "lessons," "framework," "what I learned," numbered lists, "thread." Skip pure news, shout-outs, and promos.

Dedupe by tweet/thread ID or URL before processing.

---

## Demo Mode (required before full automation)

Run the prompt on **3–5 real threads** first. Verify each output:

```
[ ] All source steps present, in order
[ ] Zero verbatim source phrases
[ ] One reframe per step; hook is one line
[ ] No source author's personal facts appearing as Lord Judah's own
[ ] Exactly the 5 signature hashtags; no emojis
[ ] Reads aloud as spoken flow
```

Only scale the batch after the samples pass. Keep all original/rewritten pairs — they become calibration data.

---

## Publishing Guardrails

- **Human review for the first two weeks** of any automated run. Reading time is seconds per post; the cost of one off-voice or off-fact post is high.
- **Never republish another person's personal story as Lord Judah's own.** The prompt converts personal claims to teaching cases; spot-check that it did.
- **Add one original layer when publishing** (an own example, a local reference, a lived lesson). This strengthens the transformation, the originality, and the brand.
- **Platform limits:** Instagram ≤ 5 hashtags (fixed set complies); Threads ≤ 500 characters → use the compressed build in `references/voice-engine.md`.

---

## Optional Blotato Handoff

If transmuted posts flow into the existing scheduling stack, reuse the pipeline rules:

- Use `scheduledTime` (never `scheduledAt`), `accountId` as string
- Accounts: Instagram `"1005"` · Threads `"310"` · X `"846"` · TikTok `"1217"`
- Default slot: 4:00 PM EDT (`T16:00:00-04:00`)
- Verify the queue (`blotato_list_schedules`) before confirming anything

---

## Operations Notes

| Item | Guidance |
|---|---|
| Batch size | Start at 5–10 threads per run; expand after calibration |
| Retries | On model timeout, retry once per item; log failures with source URL |
| Storage | Sheets columns: `source_url`, `source_author`, `post_text`, `verdict`, `reviewed`, `scheduled_date` |
| Drift audit | Monthly: sample 10 outputs against the Quality Gate; log corrections in this skill |
