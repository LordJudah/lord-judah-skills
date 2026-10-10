---
name: lord-judah-seedance-video
description: Workflow for generating cinematic, brand-aligned videos for Lord Judah / Judah Bless Ent using Seedance 2.0 via the Fal.ai API. Use when the user asks to create short movies, music video scenes, or promotional clips using Seedance, or when visual generation is requested via Fal.ai.
license: Complete terms in LICENSE.txt
---

# Lord Judah - Seedance 2.0 Video Generation

This skill provides the procedural knowledge and tools to generate high-quality, cinematic video content for Lord Judah and Judah Bless Ent using the Seedance 2.0 model via Fal.ai.

## About Seedance 2.0 & Fal.ai

Seedance 2.0 is a state-of-the-art video generation model capable of producing highly realistic, motion-rich, and cinematic video sequences from text and images. By accessing it through the Fal.ai API, we bypass manual UI rendering and can automate full scene-by-scene video pipelines directly in the sandbox.

## When to Use This Skill

- Generating short-form vertical (9:16) video clips for Instagram Reels or TikTok.
- Creating B-roll or cinematic scenes for Lord Judah music videos.
- Animating existing brand photography or AI-generated artwork.
- Rapidly prototyping visual concepts for True He(ART) Academy campaigns.

## Prerequisites

1. **Fal.ai API Key**: Must be set in the environment as `FAL_KEY`. 
   *Note: The key format is usually `key_id:key_secret`.*
2. **fal-client**: The Python SDK must be installed (`sudo pip3 install fal-client`).

## Workflow: Generating a Video

### 1. Define the Scene and Mode
Determine the best generation mode based on the user's request:
- **Text-to-Video (T2V)**: Best for purely conceptual scenes built from scratch.
- **Image-to-Video (I2V)**: Best for animating a specific piece of brand art or a photo.
- **Reference-to-Video (R2V)**: Best when you need to match the style or motion of an existing asset.

### 2. Craft the Prompt
Write a detailed, cinematic prompt. For Lord Judah content, include:
- Lighting (e.g., "cinematic lighting", "neon underglow", "golden hour")
- Camera movement (e.g., "slow pan", "dynamic drone shot", "static locked-off shot")
- Subject details (e.g., "conscious hip-hop artist", "urban environment", "spiritual aura")
- *Do not use overly complex or contradictory prompt engineering; keep the motion description clear.*

### 3. Execute the Generation
Use the bundled Python script to call the API. This script handles the API request, waits for completion, and automatically downloads the resulting `.mp4` file to the sandbox.

```bash
# Example: Text-to-Video
python3 /home/ubuntu/skills/lord-judah-seedance-video/scripts/generate_seedance_video.py \
  --mode t2v \
  --prompt "A cinematic slow pan across a vintage recording studio bathed in warm golden hour light, a classic microphone in the foreground, dust motes dancing in the air." \
  --aspect_ratio 9:16 \
  --resolution 720p
```

```bash
# Example: Image-to-Video
python3 /home/ubuntu/skills/lord-judah-seedance-video/scripts/generate_seedance_video.py \
  --mode i2v \
  --image_url "https://example.com/path/to/image.jpg" \
  --prompt "The subject slowly looks up toward the camera, subtle breathing motion, cinematic atmosphere." \
  --aspect_ratio 9:16
```

### 4. Review and Deliver
Once the script downloads the `.mp4` file, review the output (if possible) or deliver it directly to the user using the `message` tool with the file attached.

## Brand Guidelines (Lord Judah / Judah Bless Ent)

When crafting prompts or selecting reference images for this workflow, ensure alignment with the brand identity:
- **Aspect Ratio**: Default to **9:16** for all social media content unless 16:9 is explicitly requested for YouTube or presentations.
- **Aesthetic**: Blend classic boom-bap hip-hop culture with futuristic, AI-driven innovation and spiritual/mindful themes.
- **Tone**: Empowering, authentic, excellent, and message-driven.

## API Parameters Reference

- **mode**: `t2v`, `i2v`, `r2v`
- **aspect_ratio**: `9:16` (default), `16:9`, `1:1`
- **resolution**: `480p`, `720p` (default), `1080p`
- **duration**: `auto` (default, lets model decide between 4-15s)
- **fast**: Flag to use the `/fast/` endpoints for quicker, slightly lower-quality drafts.
- **generate_audio**: Always defaults to `True` in the script to generate synced sound effects.

## Troubleshooting

- **404 Errors**: Ensure you are hitting the correct endpoint (e.g., `/fal-ai/seedance-2/text-to-video`).
- **Timeout**: Video generation can take several minutes. The bundled script uses a 300-second timeout. If it times out, you may need to use the async `fal-client` library instead of synchronous `requests`.
- **Image URL Issues**: For I2V, ensure the `image_url` is publicly accessible. If you have a local image, you must upload it first (e.g., using `manus-upload-file`).
