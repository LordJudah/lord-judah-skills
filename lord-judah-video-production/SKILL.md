---
name: lord-judah-video-production
description: "Create repeatable Lord Judah video workflows with correct avatar, voice, image, and format selection. Use for: HeyGen avatar videos, image-to-video requests, generated-image-to-video pipelines, uploaded-photo animation, and any future task where asset choice must be explicit and consistent."
---

# Lord Judah Video Production

## Overview

Use this skill whenever a task involves creating a video for Lord Judah and the output depends on choosing the correct **avatar**, **voice**, **photo**, **generated image**, **aspect ratio**, or **motion style**. Treat this skill as the operating system for future video production, not just a prompt-writing guide.

The central rule is simple: **never guess the source asset when asset identity matters**. Either use a saved default that has already been defined for Lord Judah, or present a short preflight summary that names the exact asset set before generation.

## Workflow Decision Tree

Use the following decision logic.

| Situation | Action |
|---|---|
| User says to use a known avatar, voice, or image set by name | Match the request to the registry and confirm the exact selection in the preflight summary |
| User wants a HeyGen-style speaking video | Use the avatar-video workflow |
| User wants a generated still image turned into a video | Use the generate-image-first workflow |
| User uploads an image and asks for animation | Use the uploaded-image-to-video workflow |
| User gives no asset preference | Use saved defaults if they exist; otherwise ask one concise clarification question |
| The request mixes avatar performance and cinematic scenery | Use the hybrid workflow |

## Non-Negotiable Preflight

Before generating any video, produce a short internal checklist that identifies the exact production inputs.

| Field | Requirement |
|---|---|
| Video mode | Avatar video, image-to-video, uploaded-image-to-video, or hybrid |
| Subject source | Exact avatar name, exact uploaded file, or exact generated image |
| Voice source | Exact voice name or default Lord Judah voice |
| Aspect ratio | 9:16, 16:9, or 1:1 |
| Duration target | Requested length or recommended default |
| Motion style | Talking head, walk-and-talk simulation, cinematic pan, zoom, parallax, etc. |
| Scene concept | One-sentence scenery description |
| Script/audio source | Written script, generated line, or uploaded audio |

If any of these fields are ambiguous and affect the outcome, ask the user one concise question. If the user explicitly says to choose the rest, choose the remaining fields and proceed.

## Asset Identity Rules

Treat asset identity as a controlled mapping problem.

### Avatar Rules

Maintain a named registry of Lord Judah avatars. Use human-readable labels such as **Main Talking Avatar**, **Workshop Avatar**, **Promo Avatar**, or **Podcast Avatar**. When possible, map each label to the underlying platform identifier in a reference file.

If more than one avatar could fit the request, do not guess silently. Use a brief confirmation step or state which default you are selecting.

### Voice Rules

Maintain a named registry of Lord Judah voice options and preferred use cases. If the user says **use my Lord Judah voice**, use the saved default voice unless another named voice has been specified.

### Image Rules

Treat images as belonging to one of three classes.

| Image class | Meaning | Required handling |
|---|---|---|
| Generated image | Created during the current task | Save the image path and reference that exact file for animation |
| Uploaded image | User-provided file | Confirm the exact uploaded file path or filename before animation |
| Library image | Previously curated asset | Use only when clearly named or previously approved |

Never say **the image** when multiple candidate images exist. Refer to the exact file, label, or source.

## Supported Workflows

## 1. Avatar Video Workflow

Use this workflow when the user wants Lord Judah speaking on camera through a saved avatar.

1. Determine the exact avatar and voice.
2. Determine format, duration, scene, and script.
3. If motion realism is limited by the platform, design for the strongest available illusion: camera drift, push-in, body sway, hand motion, or environmental parallax.
4. Generate the video.
5. Review whether the result is a real walk cycle or a simulated walk-and-talk effect, and report that honestly.

## 2. Generate-Image-First Workflow

Use this workflow when the user says to create the image first and then animate it.

1. Generate the still image based on the requested style and scene.
2. Save the generated image to the working directory with a clear file name.
3. Use that exact image as the source for animation.
4. Preserve a record of the image path in the task notes so the same file can be reused for revisions.

## 3. Uploaded-Image-to-Video Workflow

Use this workflow when the user uploads a photo or artwork and wants it animated.

1. Identify the exact uploaded file.
2. Confirm whether the user wants speech, environmental motion, camera motion, or full character motion.
3. Choose the appropriate video method based on the available toolchain.
4. State the source file in the preflight summary before rendering.

## 4. Hybrid Workflow

Use this workflow when the user wants both a speaking avatar and a generated or cinematic environment.

1. Lock the speaking subject first.
2. Build or select the background or concept image second.
3. Decide whether the final result should prioritize lip sync, realism, or cinematic motion.
4. Explain any platform tradeoff before generation if it materially changes the motion style.

## Duration Guidance

Read `references/video-lengths.md` when the user asks about duration limits or when choosing the best production path for short tests versus longer videos.

Use the practical rule below.

| Goal | Recommended duration |
|---|---|
| Quick test or motion proof | 5 to 10 seconds |
| Social promo or short ad | 15 to 45 seconds |
| Short talking segment | 30 to 90 seconds |
| Longer scripted delivery | Use Studio-style multi-scene workflow instead of a single image-to-video scene |

Do not assume that every workflow supports the same duration ceiling. Photo-to-video and Studio-based avatar workflows may have different limits.

## Quality-Control Rules

Before delivery, review the output for the following.

| Check | Standard |
|---|---|
| Asset correctness | Correct avatar, correct voice, correct image source |
| Motion honesty | Describe motion accurately; do not overclaim true walking if it is simulated |
| Lip sync | Speech should align naturally enough for the requested use case |
| Framing | Match the requested aspect ratio and composition |
| Style continuity | Scene, tone, and wardrobe should fit the prompt and brand intent |

If a revision is needed, specify exactly what should change: for example, **stronger forward drift**, **less static torso**, **warmer lighting**, or **use uploaded image B instead of image A**.

## Registry and Template Files

Read `references/master-asset-registry.md` as the primary source of truth for named avatar, voice, photo, generated-identity, scene-preset, and approval-state mappings.

Read `references/asset-registry.md` only as a bridge for older references that still mention a simpler asset registry.

Use `templates/asset-registration-template.md` whenever a newly discovered avatar, voice, photo set, generated identity preset, or scene preset should be added consistently.

Use `templates/video-request-template.md` when it would help structure a recurring request, intake form, or reusable production brief.

## Output Standard

When responding to Lord Judah before rendering, provide a concise production summary in plain English using this structure:

| Field | Value |
|---|---|
| Mode | Chosen workflow |
| Avatar/Image | Exact asset label or file |
| Voice | Exact voice label |
| Format | Aspect ratio |
| Duration | Target length |
| Scene | One sentence |
| Motion | One sentence |
| Script | Final spoken line or audio source |

Use this summary to prevent asset mix-ups and to make revisions traceable.
