# Master Asset Registry Usage

The primary source of truth for Lord Judah's asset selection system now lives in the video-production skill at:

`/home/ubuntu/skills/lord-judah-video-production/references/master-asset-registry.md`

Use that registry before any future music-video production task that depends on the correct selection of:

| Asset type | Why it matters |
|---|---|
| Avatar | Ensures the correct Lord Judah on-camera identity is used |
| Voice | Prevents mismatched delivery tone or default voice errors |
| Photo set | Ensures image-to-video scenes use the intended stills |
| Generated identity preset | Keeps AI-generated depictions of Lord Judah stylistically consistent |
| Scene preset | Preserves visual continuity across sections and revisions |
| Performance preset | Maps hooks, verses, bridges, and outros to the right visual mode |
| Approval state | Prevents the automatic reuse of unapproved or task-specific assets |

## Music-Video Rule

Before rendering any scene, the workflow should confirm the following against the master registry.

| Field | Requirement |
|---|---|
| Subject | Exact avatar, photo, or generated identity label |
| Audio | Exact vocal source or named section file |
| Scene | Exact preset label |
| Performance mode | Hook hero shot, verse close-up, symbolic cutaway, etc. |
| Approval basis | Explicit user request, approved default, or task-specific file |

If a requested asset is missing from the registry, the workflow should either register it as **task-specific** or ask one concise clarification question before production.
