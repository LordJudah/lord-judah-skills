# Higgsfield MCP — Tool Shapes and Gotchas

Exact call shapes for the Higgsfield MCP server. All were verified live.

## `media_upload` — request presigned upload slots

Pass `files: [{filename, content_type}]`. Returns one entry per file with a `media_id` plus an `instructions` string containing the curl command.

It does **not** transfer bytes. Nothing exists on the server until the PUT succeeds and `media_confirm` runs.

```
files: [{content_type: "image/jpeg", filename: "lj_train_01.jpg"}, ...]
```

## Transferring the bytes

```bash
curl -X PUT -H "Content-Type: image/jpeg" --data-binary @lj_train_01.jpg '<presigned url>'
```

**Status handling — each code means something different:**

| Code | Meaning | Action |
|---|---|---|
| `200` | uploaded | proceed |
| `412` | object already present | treat as uploaded; safe for idempotent re-runs |
| `000` | transient network failure | retry with backoff — succeeds on the second attempt in practice |
| `5xx`, `429` | transient server condition | retry with backoff |
| `403` | presigned URL **expired** | not retryable — call `media_upload` again for fresh slots |
| other | deterministic rejection | report it; retrying is wasted time |

> **Presigned URLs expire far sooner than they advertise.** `X-Amz-Expires=86400` appears in the URL, but the embedded AWS **session token** governs the real window and lives about **one hour**. Measured: URLs issued at 06:49 uploaded fine at 06:52 and returned `403` at 08:55. Do the PUTs promptly, and do not debug a `403` as if it were a network fault.

Other constraints:

- Perform the PUT where the bytes already are. Never relay file bytes between environments as base64 or text.
- Use `scripts/upload_media.py` rather than hand-rolling the loop; it classifies statuses and aborts early on `403`.

## `media_confirm` — finalise

```json
{"media_ids": ["<uuid>", "<uuid>"], "type": "image"}
```

Only confirmed media can be used as training input or generation reference.

## `show_characters` — train, list, inspect

### Train

```json
{
  "action": "train",
  "name": "Lord Judah Canon Soul",
  "type": "soul_2",
  "medias": [{"role": "image", "value": "<media_id>"}, ...]
}
```

**Use `medias`, not `images`.** The flat `images` array accepts the same UUIDs and fails reliably; `medias` succeeded consistently at 6, 12, and 15 images. Set size is not the limiting factor.

Returns the new `soul_id` (also echoed as `character_id`).

### Status

```json
{"action": "status", "soul_id": "<id>"}
```

- `status`: `training` → `ready`, or `failed`
- `raw_status`: `queued` → `in_progress` → `completed` / `failed`
- Training takes 8–20 minutes; a long `queued` phase is normal
- **`failed` carries no error message.** Diagnose inputs and parameter shape instead of re-polling

### List

```json
{"action": "list"}
```

## `generate_image` — generate with a Soul

```json
{
  "params": {
    "model": "soul_2",
    "soul_id": "<soul_id>",
    "prompt": "<scene, wardrobe, framing, lighting>",
    "aspect_ratio": "9:16",
    "count": 1
  }
}
```

- **`model` and `soul_id` go inside `params`.** Hoisting them to the top level raises `params: Invalid input`.
- `quality` defaults to `2k` when unset; the server reports the adjustment it applied.
- `count` 1–4 produces variants of the same prompt and inputs; independent prompts need `generate_image_batch`.
- `get_cost: true` preflights the credit cost without submitting.

### `use_unlim`

Controls whether the account's free-trial unlimited generations or its credits pay. **Omit it** and let the server decide; only pass `true` when the user explicitly asks to spend their unlimited allowance. Never set it to save credits on your own initiative. If the server returns an `unlim_choice` question, put it to the user.

## `job_status` — fetch results

```json
{"jobId": "<job id>", "sync": true}
```

**The parameter is `jobId` (camelCase).** `job_id` fails with `expected string, received undefined`.

`sync: true` waits for completion and returns the output URL. If a generation widget is already visible it polls itself — do not add a redundant poll.

## Model constraints

- Souls work with `soul_2` and `soul_cinematic` — **image models only**
- `soul_2` supports `use_unlim: true`
- Verify aspect ratios and media roles per model with `models_explore` before assuming a value

## Diagnosing a failed run

The API gives no failure reason beyond `failed`. Work through these in order:

1. **Wrong parameter shape?** Confirm `medias`, not `images`.
2. **Uploads incomplete?** Every `media_id` must have succeeded on the PUT and been confirmed. A `403` midway leaves a partial set — re-request slots and redo it.
3. **Account limits?** Check `balance` — plan and credit state.
4. **Input quality or provenance?** Re-audit with `preflight_images.py`, and confirm with the user that no file is AI-generated.
5. **Transient backend fault?** If everything above is clean, resubmit once; identical requests have succeeded on retry.