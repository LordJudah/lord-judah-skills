---
name: higgsfield-soul-training
description: "Train, validate, and reuse Higgsfield Soul IDs — reusable AI identities that hold a specific person's face across generations — through the Higgsfield MCP. Use for: training a Soul from reference photos; fixing a Soul that renders the wrong hair, headwear, or accessories; recovering a Soul training run that failed; auditing a photo folder for training-grade images; validating a trained Soul against a brand canon or benchmark; and generating with a saved soul_id. Covers the upload pipeline, the medias-vs-images parameter trap, presigned-URL expiry, accessory-bias and era-split failure modes, and the controlled validation test."
license: Complete terms in LICENSE.txt
---

# Higgsfield Soul Training

A **Soul** is a reusable identity model trained on 5–20 photos of one person. Once trained, `soul_id` reproduces that face in any generation. This skill covers the full pipeline and the failure modes that reliably ruin a Soul.

Souls are **image models only** (`soul_2`, `soul_cinematic`). For video, identity must travel through reference images instead.

## Pipeline overview

```
audit photos → media_upload → curl PUT → media_confirm → show_characters(train) → poll → validate
```

Never skip the audit. Most Soul failures trace to bad input photos or a wrong parameter shape, not to the API.

## Step 1 — Audit candidate photos

```bash
python scripts/preflight_images.py <folder> --manifest out.json
```

Reports resolution, orientation, detail energy (advisory), background type, and clusters near-duplicates by perceptual hash. Read `references/image-selection.md` for acceptance rules.

**Treat its flags as prompts to look, not verdicts to obey.** Two of them are deliberately advisory:

- `detail energy` tracks scene smoothness and depth of field, **not** focus. A perfectly sharp shallow-DOF studio portrait scores lower than a busy outdoor snapshot. Never reject an image for a low value alone.
- `green-screen` / `pure-white background` mark composited or studio work. The background is not what a Soul learns, so these are **verify-provenance** flags, not automatic rejects.

Select 5–20 images. Prefer 12–16. A smaller clean set beats a larger contaminated one.

## Step 2 — Upload

`media_upload` returns presigned URLs plus `media_id`s but does **not** transfer bytes. Complete the PUTs with the bundled helper:

```bash
python scripts/upload_media.py <media_upload_result.json> --dir <folder> --out uploaded.json
```

It classifies every response and retries only what is worth retrying:

| Status | Meaning | Action |
|---|---|---|
| `200` | uploaded | proceed |
| `412` | object already present | treat as uploaded (idempotent re-run) |
| `000`, `5xx`, `429` | transient network/server | retried automatically with backoff |
| `403` | **presigned URL expired** | not retryable — request fresh slots |
| other | deterministic rejection | reported, not retried |

> **URLs expire far sooner than they claim.** The presigned URL advertises `X-Amz-Expires=86400`, but the embedded AWS session token governs the real window and lives roughly **one hour**. Upload promptly; if you see 403, call `media_upload` again for fresh slots rather than retrying.

Then call `media_confirm` with every `media_id` and `type: "image"`.

**Local file paths are never valid training inputs.** The chain must be upload → PUT → confirm. Never train on a partially uploaded set.

## Step 3 — Train

**The single most important detail in this skill.** Pass training photos through the **`medias`** array. The flat `images` array accepts the same UUIDs but fails reliably.

```json
{
  "action": "train",
  "name": "<descriptive name>",
  "type": "soul_2",
  "medias": [
    {"role": "image", "value": "<media_id>"},
    {"role": "image", "value": "<media_id>"}
  ]
}
```

Verified failure pattern: 14 images via `images` → failed; 10 via `images` → failed; 6, 12, and 15 via `medias` → all succeeded. **Set size was never the limiting factor.** Do not respond to a failure by shrinking the set — fix the parameter shape first.

## Step 4 — Poll

```json
{"action": "status", "soul_id": "<returned id>"}
```

- `status` progresses `training` → `ready`, or lands on `failed`
- `raw_status` gives finer detail: `queued` → `in_progress` → `completed` / `failed`
- Expect **8–20 minutes**. Queue depth varies; a long `queued` phase is normal, not a fault
- Poll every few minutes using sleeps in the shell — never in a tight loop
- **`failed` carries no error message.** Diagnose by inspecting inputs and parameter shape, not by re-reading status

## Step 5 — Validate before trusting

Never hand off an unvalidated Soul. Run a **controlled test**: generate with a fixed prompt and compare against the same prompt rendered by the previous Soul or against the brand canon.

```json
{"params": {"model": "soul_2",
            "soul_id": "<soul_id>",
            "prompt": "<fixed test prompt>",
            "aspect_ratio": "1:1"}}
```

`model` and `soul_id` live **inside** `params`. Hoisting them one level up fails validation.

Two rules for a meaningful test:

- **Frame the whole head with headroom.** A crop that cuts the top of the head makes hair impossible to judge — you will conclude "no change" when the fix worked.
- **Hold the prompt constant** across before/after so the only variable is the Soul.

Fetch output with `job_status` — the parameter is **`jobId`** (camelCase), not `job_id`.

## The two failure modes

### 1. Accessory bias — the Soul learns what covers the head

A Soul learns *everything* consistently present in its training photos, not just facial structure. If every photo has a headwrap, hat, or helmet, the Soul treats it as part of the identity and **will not render the actual hair**, even when explicitly prompted for it.

**Diagnostic:** output hair is close-cropped, cut off, or permanently covered despite prompt instructions.

**Fix:** add 6–10 images showing the person's real hair, uncovered, in the same era. Retrain. This works — a headwear-only Soul that rendered cropped hair rendered full locs once uncovered images were added.

**Prevention:** never train on a set where one accessory appears in 100% of photos. Deliberately include covered and uncovered shots so the Soul learns the *face*, independent of accessories.

### 2. Era split — one grooming era per Soul

Beard length, hair length, weight, and age read as identity to a Soul. Mixing visibly different eras of one person produces a face that resembles neither.

**Rule:** train on **one era**. Exclude other eras explicitly rather than diluting the set.

**Exception:** mixing eras is acceptable only when the difference is *deliberate and named* — for example combining covered and uncovered shots of one era specifically to defeat accessory bias. Confirm with the user when two candidate eras exist; never silently blend them.

**Always report** which era you trained on and which you excluded, with filenames, so the user can redirect you.

## Input provenance

**Never train on AI-generated images.** A synthetic render teaches the Soul to reproduce a synthetic average, not the person. Exclude:

- AI-generated or heavily airbrushed renders
- composites and green-screen work — the background itself is not the problem (a Soul barely learns backgrounds), but these files are far likelier to be synthetic or heavily retouched, so **verify provenance before including one**
- multi-angle sheet exports and collages
- brand benchmark or canon images — these are targets to compare *against*, never inputs
- anything where the face is under roughly a quarter of the frame
- archival scans under about 0.5 MP

If provenance is uncertain for a supplied folder, ask the user to confirm which files are genuine photographs. Excluding a genuine photo costs almost nothing; including a synthetic one corrupts the identity and costs a full retrain.

## Reporting

Close with a table of souls (ID, image count, status), the exact working recipe, which photos qualified and why, which were excluded by category, and the era used. Record all IDs durably in a state file — `references/lord-judah-soul-registry.md` is a worked example.

## Bundled resources

| File | Read when |
|---|---|
| `scripts/preflight_images.py` | Auditing a photo folder before training |
| `scripts/upload_media.py` | Completing `media_upload` PUTs with retry and status classification |
| `references/image-selection.md` | Choosing and rejecting training photos |
| `references/higgsfield-mcp-tools.md` | Exact MCP call shapes, parameters, and gotchas |
| `references/lord-judah-soul-registry.md` | Working on Lord Judah / Judah Bless Ent identities |
