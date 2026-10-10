---
name: lord-judah-heygen-song-commercial
description: Generate HeyGen avatar song commercials for Lord Judah music releases using the LORD avatar group, LORD voice, and song-specific scripts with ManyChat CTAs. Use when asked to create a song commercial, promo video, or HeyGen video for any Lord Judah single or album release. Covers avatar selection, script writing, API submission, polling, and download. Produces 9:16 MP4 files ready for manual video editing (user adds cover art background in their editor).
---

# Lord Judah HeyGen Song Commercial Workflow

## Confirmed Asset Registry

| Asset | ID |
|---|---|
| Avatar Group (LORD) | `feff43ad5475463ab8e278f40b785d8b` |
| **Default Avatar Look** (Focused creator with microphone) | `bcddb5c992fc47ad813aecea319edae2` |
| LORD Voice | `2bfda2b402224877bdd0010d2d7537a8` |
| Second Avatar (LORD JUDAH photo avatar) | `e9017f7773a2418fbeb49efe65451f55` |

**Background note:** HeyGen's API does not reliably render uploaded image backgrounds. The user handles cover art background compositing manually in their video editor. Do NOT attempt background compositing — generate clean avatar video only.

## Script Template

Each commercial script follows this structure (~30 seconds / ~100–120 words):

```
Peace and power. Lord Judah here.

My new single [SONG TITLE] [drops / is out now] [RELEASE DATE].

[1–2 sentences on song concept/theme — pull from production bible or campaign copy]

[SONG TITLE] — available on all platforms [RELEASE DATE].

Comment [KEYWORD 1] or [KEYWORD 2] to stream this record.

Judah Bless Ent.
```

### ManyChat CTAs by Song

| Song | Keywords |
|---|---|
| Blessed and Grateful | Blessed, Grateful |
| Just Walking With My Dog | dog, dawg |
| Navigating The Way | navigate, way |
| Battle For Earth | battle, earth |

For new songs, use the ManyChat keyword triggers configured in the automation.

## Workflow

### Step 1 — Write the script
Use the template above. Pull concept language from the production bible or campaign copy. Keep under 35 seconds.

### Step 2 — Build the payload JSON

```json
{
  "avatarId": "bcddb5c992fc47ad813aecea319edae2",
  "voiceId": "2bfda2b402224877bdd0010d2d7537a8",
  "script": "[FULL SCRIPT HERE — use \\n for line breaks]",
  "title": "[SONG TITLE] - Commercial",
  "aspectRatio": "9:16"
}
```

Save to `/tmp/[song_slug]_commercial_payload.json`.

### Step 3 — Submit to HeyGen via MCP

```bash
manus-mcp-cli tool call create_video_from_avatar --server heygen --input-file /tmp/[song_slug]_commercial_payload.json
```

Returns: `{"video_id": "...", "status": "waiting"}`

### Step 4 — Poll for completion

```bash
manus-mcp-cli tool call get_video --server heygen --input '{"videoId": "[VIDEO_ID]"}'
```

Poll every 30 seconds. Status: `waiting` → `processing` → `completed`. Typical render time: 2–4 minutes per video. For batch jobs, submit all videos first, then poll all simultaneously.

### Step 5 — Download the video

Use the bundled `scripts/download_heygen_video.py` script. Do NOT use `curl` — it stalls on large HeyGen files.

```bash
python3 /home/ubuntu/skills/lord-judah-heygen-song-commercial/scripts/download_heygen_video.py \
  "[VIDEO_URL]" "/home/ubuntu/upload/[SongName]_Commercial.mp4"
```

### Step 6 — Deliver to user

Attach all MP4 files in the result message. Remind the user to add their cover art as the background layer in their video editor before posting.

## Batch Generation (Multiple Songs)

1. Write all payload JSON files
2. Submit all with `create_video_from_avatar` — one MCP call per song, one at a time
3. Note all video IDs returned
4. Poll all IDs until all show `completed`
5. Download all using the Python script
6. Deliver all as attachments in one result message

## Known Issues

| Issue | Fix |
|---|---|
| Background images via API don't render | Skip — user handles in manual edit |
| `curl` stalls on large video downloads | Use Python `requests` with `stream=True` |
| Signed URL expiry | HeyGen URLs expire in ~24 hours — download immediately |
| Wrong field name | Use `script` field, NOT `inputText` |
| MCP tool name | Use `create_video_from_avatar`, not `create_video` |
