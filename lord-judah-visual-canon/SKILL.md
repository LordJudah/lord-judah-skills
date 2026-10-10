---
name: lord-judah-visual-canon
description: "Apply Lord Judah’s approved visual identity canon to image and video generation. Use whenever creating, directing, reviewing, or planning any visual that depicts Lord Judah, Judah Bless Ent, True He(ART) Academy, Rap Dojo, Hip-Hop History content, or a Lord Judah campaign; activate it when the user says ‘Use the Lord Judah Core Identity Reference Canon.’"
---

# Lord Judah Visual Canon

Use this skill to maintain Lord Judah’s likeness and visual-world continuity across image generation, image-to-video, campaign art direction, and visual approval.

## Canon Source

Retrieve the source assets through Google Drive when the session has access:

- **System folder:** [Lord Judah Visual Reference System — Core + Renegade](https://drive.google.com/drive/folders/1a9jYFiYzVChG0TuELzUCDpZga4HpDZqY)
- **Controlling canon:** [Approved Visual Benchmark Canon — Four Pillars](https://drive.google.com/drive/folders/1zqSzjur14AheZkVJVnkNAeXxvlV2hW0G)

Use the Google Workspace `gws` CLI for Drive operations. Do not use browser navigation for Drive. If required reference files cannot be accessed, ask the user to attach the relevant benchmark or share an accessible Drive link; do not substitute a generic person or silently omit the likeness control.

## Identity Constants

Preserve these attributes in all Core Identity visuals:

- Mature Black male facial geometry: natural forehead, eye spacing, nose bridge, cheek structure, and jaw line.
- Full, naturally shaped beard with salt-and-pepper detail when visible.
- Long natural dark locs with believable density and pattern.
- Natural skin texture and grounded, calm authority.
- Authentic adult proportions and natural anatomy.

Avoid generic AI “king” imagery, overly youthful facial drift, plastic skin, exaggerated musculature, altered loc patterns, duplicate people, distorted hands, text, watermarks, collage borders, and source-sheet labels.

## Four-Pillar Routing

| Pillar | Select when the brief is about | Visual language | Usage guardrail |
| --- | --- | --- | --- |
| **The Architect** | Press, speaker / teaching-artist work, website portraits, general campaigns, creative-director positioning | Dark charcoal, black, subtle crimson/wine-red edge light, refined editorial photography | **Default** public-facing likeness and realism benchmark. |
| **The Sound Alchemist** | Music releases, beat making, DJ / producer narratives, city and studio work | Dusk, studio tools, vinyl, samplers, rooftops, warm city light | Retain working-artist truth; never reduce it to generic nightlife. |
| **The Cultural Guardian** | Hip-hop history, Rap Dojo, education, archives, community and cultural stewardship | Records, listening rooms, archival / classroom motifs, knowledge-rich environments | Keep the person and cultural meaning central—not decorative spectacle. |
| **The Crowned Legacy** | Major releases, anniversaries, album-era mythology, ceremonial legacy moments | Gold, violet, tailored regality, sacred or monumental atmosphere | Reserve for milestones; do not make it the everyday visual default. |

## Workflow

1. **Classify the visual brief.** Select the pillar that carries the campaign’s narrative function. Default to **The Architect** if no other world is explicitly supported.
2. **Retrieve the reference stack.** Start with the chosen pillar benchmark, add the front-neutral Core crop, and add one relevant three-quarter crop. Use **two to four** references total; do not overload generation with the entire library.
3. **Write a bounded prompt.** State the new scene, wardrobe, pose, framing, lighting, and platform format. Require retention of the Identity Constants. Explicitly exclude source-sheet artifacts and unwanted people.
4. **Generate.** Use reference-guided generation whenever available. Treat source assets as identity/art-direction references, not templates to copy.
5. **Apply the approval gate.** Compare the result against The Architect plus front-neutral and three-quarter references. If facial geometry, beard, loc pattern, mature presence, or anatomy does not read as Lord Judah, reject it and run one focused correction.
6. **Archive approved work.** For an approved campaign visual, retain the final asset, prompt, selected pillar, and reference filenames in the relevant campaign folder.

## Standard Prompt Block

Adapt this block rather than copying it blindly:

> Use the **Lord Judah Core Identity Reference Canon**. Preserve the supplied mature facial proportions, forehead and eye structure, full natural beard shape and density, long natural loc pattern, realistic skin texture, and calm grounded presence. Create an original photorealistic image in the **[SELECTED PILLAR]** visual world: **[SCENE / WARDROBE / POSE / LIGHTING]**. Do not copy reference composition or clothing unless requested. No labels, borders, collage layout, text, watermarks, extra people, distorted hands, or generic AI royalty clichés.

## Renegade Boundary

`Renegade Judah` is a separate narrative character variant. Use it **only** when the user explicitly requests the headwrap, dark hoodie, street-veteran / protector archetype, or a Renegade story world. Do not merge it into ordinary Lord Judah Core Identity visuals.

## Training Boundary

The canon is for **reference-guided generation and visual quality control**. Do not use benchmark sheets, collage-derived crops, or the Renegade assets as LoRA training data. Future LoRA training must use sharp, individually sourced, current real-camera photography.

## Activation Phrase

When the user says:

> “Use the Lord Judah Core Identity Reference Canon for this image.”

Treat this as explicit instruction to execute the workflow above, with **The Architect** as the default pillar unless the brief clearly maps to another approved world.
