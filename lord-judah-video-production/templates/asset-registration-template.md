# Asset Registration Template

Use this template whenever a new **avatar**, **voice**, **photo set**, **generated identity preset**, **scene preset**, or **audio-performance preset** should be added to the master asset registry.

The goal is to capture enough detail that future productions can use the asset correctly without guesswork.

## Registration Header

| Field | Value |
|---|---|
| Registration date | YYYY-MM-DD |
| Asset label | To be filled |
| Asset category | Avatar, Voice, Photo Set, Generated Identity Preset, Scene Preset, Performance Preset, or Audio Asset |
| Added by | Manus AI or user-confirmed update |
| Source task | Short description of the project or render where the asset was confirmed |

## Asset Identity

| Field | Value |
|---|---|
| Human-readable name | To be filled |
| Exact platform | HeyGen, local upload, generated image, other |
| Exact ID or file path | To be filled |
| Backup identifier | Alternate filename, URL, or internal note |
| Approval state | Approved default, Approved conditional, Pending review, Task-specific, or Retired |

## Creative Use Rules

| Field | Value |
|---|---|
| Primary use case | To be filled |
| Secondary use case | To be filled |
| Best format | 9:16, 16:9, 1:1, or multi-format |
| Best duration range | To be filled |
| Preferred framing | Close-up, medium shot, half-body, full-body illusion, etc. |
| Tone profile | To be filled |
| Motion style | Talking-head, walk-and-talk simulation, lip-sync close-up, cinematic drift, etc. |

## Brand Fit

| Field | Value |
|---|---|
| Visual mood | To be filled |
| Color logic | To be filled |
| Best project types | Promo, music video, teaching content, artist message, trailer, documentary, etc. |
| Guardrails | What to avoid when using this asset |
| Related presets | Matching voice, scene, photo, or audio presets |

## Confirmation Notes

| Field | Value |
|---|---|
| Why this asset was approved | To be filled |
| User-confirmed wording | Exact phrase if the user explicitly approved it |
| Revision history | To be filled |
| Promote to default? | Yes or No |
| Default category if yes | General avatar, music-video avatar, promo scene, reflective voice, etc. |

## Quick Registration Example

| Field | Example |
|---|---|
| Asset label | Golden Hour Mural Street |
| Asset category | Scene Preset |
| Exact platform | Generated environment concept |
| Exact ID or file path | N/A |
| Approval state | Approved default |
| Primary use case | Walk-and-talk clips and uplifting artist promos |
| Best format | 9:16 |
| Motion style | Forward drift and subtle environmental parallax |
| Guardrails | Do not use for dark or somber subject matter unless restyled |

Once completed, add the new asset to the correct table in `references/master-asset-registry.md` and, if relevant, mention it in the task memory log.
