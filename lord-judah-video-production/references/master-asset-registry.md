# Master Asset Registry

This registry is the control center for Lord Judah's future **video**, **music-video**, **avatar-performance**, **image-to-video**, and **hybrid cinematic** workflows. Its purpose is to ensure that asset selection is explicit, traceable, and repeatable.

The governing principle is simple: **every recurring production asset must have a human-readable label, an exact source, a clear use case, and an approval state**. If any of those are missing, the asset should not be treated as a trusted default.

## How This Registry Should Be Used

Before rendering a future video, the production workflow should check this registry and map the user's natural-language request to a named asset. If the user says **use my avatar**, **use my voice**, **use my photo**, or **make it cinematic**, the system should consult the tables below and select the matching approved default for that category. If multiple assets could reasonably fit the request, the workflow should either state the chosen default in the preflight summary or ask one concise clarification question.

## Asset-Selection Priority

| Priority level | Rule | Action |
|---|---|---|
| 1 | User explicitly names the asset | Use the exact named asset |
| 2 | User references a category with a saved default | Use the default for that category |
| 3 | User provides a new upload in the current task | Register the exact file and treat it as task-specific |
| 4 | User asks for a generated version | Use the closest matching generated-identity preset |
| 5 | No reliable mapping exists | Ask one concise clarification question |

## Approval States

| Approval state | Meaning | Usage rule |
|---|---|---|
| Approved default | Safe to use automatically for the named scenario | May be used without re-confirmation |
| Approved conditional | Approved only for certain contexts | Use only within the stated context |
| Pending review | Candidate asset exists but has not been locked in | Do not use automatically |
| Task-specific | Valid only for the current task | Do not reuse as a default unless later promoted |
| Retired | No longer preferred for future production | Do not use unless explicitly requested |

## Avatar Library

Use this table for any talking-head, performance, walk-and-talk, or lip-sync-ready workflow that depends on a Lord Judah avatar.

| Asset label | Asset type | Platform | Exact ID or source | Primary use case | Preferred framing | Default category | Approval state | Notes |
|---|---|---|---|---|---|---|---|---|
| Lord Judah Main Talking Avatar | Avatar | HeyGen | To be filled | General speaking videos, business updates, educational delivery | Medium shot or close-up | General avatar default | Approved default | Use when the user says “use my avatar” for standard speaking content |
| Lord Judah Main Performance Avatar | Avatar | HeyGen | To be filled | Music-video performance, hook visuals, motivational delivery | Medium shot, half-body, performance framing | Music-video avatar default | Approved conditional | Preferred when performance energy matters more than formal presentation |
| Lord Judah Workshop Avatar | Avatar | HeyGen | To be filled | Teaching-artist content, school outreach, academy messaging | Medium shot | Education/workshop default | Pending review | Promote after the user confirms this is the best education-facing asset |
| Lord Judah Promo Avatar | Avatar | HeyGen | To be filled | Short-form campaigns, social promos, branded calls to action | Tight medium shot | Promo avatar default | Pending review | Use after confirmation for faster promo production |

## Voice Library

Use this table to map spoken delivery to the correct Lord Judah voice identity.

| Asset label | Asset type | Platform | Exact ID or source | Primary use case | Tone profile | Default category | Approval state | Notes |
|---|---|---|---|---|---|---|---|---|
| Lord Judah Main Voice | Voice | HeyGen | To be filled | General speaking videos, artist messages, promo clips | Clear, intelligent, grounded, confident | General voice default | Approved default | Use when the user says “use my Lord Judah voice” |
| Lord Judah Performance Voice | Voice preset or mapped audio style | HeyGen or external audio | To be filled | Music-video spoken intros, performance-led transitions, dramatic delivery | Intense, intentional, cinematic | Performance voice default | Approved conditional | Use when the project needs more force than the default speaking tone |
| Lord Judah Reflective Voice | Voice preset or mapped audio style | HeyGen or external audio | To be filled | Mindfulness, spiritual, reflective, or documentary-style delivery | Calm, warm, meditative | Reflective voice default | Pending review | Use only when specifically requested or later approved |

## Photo and Image Library

Use this table when the subject source is a still image rather than a live avatar workflow.

| Asset label | Asset class | Exact file or source | Visual purpose | Best use case | Reuse status | Approval state | Notes |
|---|---|---|---|---|---|---|---|
| Lord Judah Hero Portrait Set | Library photo set | To be filled | Premium artist identity | Posters, cover visuals, cinematic still-to-video work | Reusable | Pending review | Fill with curated photo set once selected |
| Lord Judah Performance Photo Set | Library photo set | To be filled | Strong musical presence | Performance animation, music promos, visualizers | Reusable | Pending review | Best for photo-based performance motion |
| Lord Judah Workshop Photo Set | Library photo set | To be filled | Educational and community-facing identity | Workshops, grants, school outreach | Reusable | Pending review | Keep distinct from artist-forward performance imagery |
| Task Upload A | Uploaded file | Fill at task time | Current-task subject image | Current-task animation | Task-specific | Task-specific | Rename to the real filename or label before reuse |
| Task Upload B | Uploaded file | Fill at task time | Current-task alternate image | Current-task animation | Task-specific | Task-specific | Use only when a second user upload exists |

## Generated Identity Presets

Use this table when the user wants a **generated version** of Lord Judah rather than a direct avatar render or uploaded-photo animation. These entries define how Lord Judah should be represented visually in AI-generated scenes.

| Preset label | Subject model | Style direction | Best use case | Guardrails | Approval state | Notes |
|---|---|---|---|---|---|---|
| Lord Judah Cinematic Futurist | Generated identity | Cinematic, urban, high-contrast, subtle AI-futurist overlays | Music videos, trailers, visionary promo scenes | Must still read recognizably as Lord Judah; avoid generic sci-fi clichés | Approved conditional | Strong fit for future-facing brand visuals |
| Lord Judah Street Philosopher | Generated identity | Realist urban portraiture, cultural texture, dramatic natural light | Conscious bars, reflective videos, documentary-style storytelling | Preserve authenticity and grounded presence | Approved conditional | Best for lyrical or message-driven scenes |
| Lord Judah Royal Minimalist | Generated identity | Black, gold, clean composition, elevated symbolism | Cover visuals, short promos, title cards, prestige branding | Avoid over-decoration or costume-like excess | Approved conditional | Strong fit for iconic branding moments |
| Lord Judah Spiritual Visionary | Generated identity | Deep purple accents, radiant light, wisdom-centered imagery, subtle symbolism | Reflective spoken word, spiritual concepts, higher-consciousness themes | Keep symbolism elegant, not heavy-handed | Pending review | Use once preferred aesthetic is confirmed |

## Scene and Environment Presets

Use this table to accelerate scenery selection and prevent generic backgrounds.

| Preset label | Environment type | Visual tone | Best use case | Motion suggestion | Approval state | Notes |
|---|---|---|---|---|---|---|
| Golden Hour Mural Street | Urban exterior | Warm, cultural, cinematic, uplifting | Walk-and-talk clips, social promos, artist statements | Forward drift, body sway, subtle parallax | Approved default | Strong result from the first HeyGen walk-and-talk test |
| Dramatic Studio Confidence Setup | Studio interior | Clean, powerful, intentional, authority-driven | Talking-head delivery, formal messaging, education content | Gentle push-in, light body motion | Approved default | Best when clarity matters more than scenic complexity |
| Futuristic City Nightscape | Stylized urban exterior | Visionary, metallic, intelligent, future-facing | Music-video hooks, AI-forward branding, teaser scenes | Slow dolly, light streak motion, cinematic pan | Approved conditional | Use for larger-than-life messaging |
| Community Workshop Environment | Real-world educational environment | Warm, trustworthy, engaged, people-centered | Outreach, teaching-artist content, academy materials | Light camera drift, environmental movement | Pending review | Promote after asset examples are curated |
| Symbolic Light-and-Shadow Space | Abstract environment | Reflective, spiritual, minimal, metaphor-rich | Spoken word, bridges, intros, philosophical lines | Slow zoom, silhouette motion, atmospheric drift | Approved conditional | Good for transition or bridge sections |

## Music-Video Performance Presets

Use this table to map recurring performance modes to the right song sections and production methods.

| Preset label | Performance mode | Best use case | Preferred subject source | Audio source | Approval state | Notes |
|---|---|---|---|---|---|---|
| Hook Performance Hero Shot | Direct-to-camera performance | Chorus or refrain with strong artist presence | Main Performance Avatar or approved performance photo | Hook stem or hook acapella | Approved default | Use when the hook needs repeatable signature imagery |
| Verse Intimate Close-Up | Tight lyrical performance | Dense bars, storytelling, vulnerable lines | Main Performance Avatar or close portrait image | Verse acapella | Approved conditional | Best when lyrical detail matters |
| Walk-and-Talk Motivation | Forward-motion performance | Inspirational hooks, movement-based messaging, social clips | Main Talking Avatar or Performance Avatar | Script or short vocal section | Approved default | Honest language should describe it as simulated walking if needed |
| Symbolic Cutaway Sequence | Non-lip-sync cinematic insert | Metaphoric bars, transitions, bridges, ad-libs | Generated identity or generated scene image | Full track timing or instrumental section | Approved default | Use to expand visual world without forcing mouth sync |
| Outro Authority Frame | Final statement or resolution shot | Endings, title moments, closing affirmations | Main Talking Avatar, Hero Portrait, or Royal Minimalist identity | Spoken close or final lyric section | Approved default | Useful for memorable endings |

## Format and Duration Defaults

Use these defaults unless the user explicitly requests something else.

| Content type | Default format | Default duration | Notes |
|---|---|---|---|
| Social promo | 9:16 | 15 to 30 seconds | Designed for reels and vertical distribution |
| Walk-and-talk test | 9:16 | 5 to 10 seconds | Good for motion proof and quick iteration |
| Talking-head statement | 9:16 unless otherwise requested | 30 to 60 seconds | Can expand if the production mode supports it |
| Music-video scene test | 9:16 or 16:9 depending on release plan | 5 to 15 seconds per scene | Use scene packs before full assembly |
| Full music-video build | 16:9 by default, unless social-first | Section-based | Assemble from approved scene units rather than one giant generation |

## Brand Guardrails

All future asset choices should reinforce Lord Judah's visual and creative identity.

| Area | Approved direction | Avoid |
|---|---|---|
| Tone | Cinematic, intelligent, grounded in hip-hop culture, visionary | Generic corporate polish with no soul |
| Lighting | High contrast, dramatic, golden-hour warmth, sculpted studio light | Flat, overexposed, bland lighting |
| Color | Black, gold, white, deep purple, metallic accents, controlled crimson use | Random bright palettes with no brand logic |
| Imagery | Urban texture, murals, studios, symbolism, cultural depth, future-facing detail | Generic stock backdrops or artificial clichés |
| Performance energy | Confident, reflective, authoritative, elevated | Cartoonish exaggeration or empty hype |

## Task Memory Log

Use this table to capture newly discovered asset identifiers and future approvals so the registry becomes more accurate over time.

| Date | Asset label | Change made | Source of confirmation | Updated by |
|---|---|---|---|---|
| To be filled | To be filled | To be filled | To be filled | Manus AI |

## Future Update Rules

Whenever a task reveals a real platform identifier, uploaded filename, preferred avatar, or approved scene formula, replace **To be filled** with the exact value and record the change in the **Task Memory Log**.

If the user says an asset is now the standard choice for a category, update its **Default category** and **Approval state** immediately. If the user dislikes an asset, mark it **Retired** or remove its default role so it is not selected automatically in future production.

## Preflight Output Rule

Before any future render, the workflow should summarize the final production decision in a compact table using the exact labels stored in this registry.

| Field | Value |
|---|---|
| Mode | Chosen workflow |
| Subject asset | Exact avatar, photo, or generated-identity label |
| Voice or audio | Exact voice label or audio filename |
| Scene preset | Exact preset label |
| Format | Aspect ratio |
| Duration | Target length |
| Approval basis | Named default, explicit request, or task-specific selection |

This summary is the final protection against using the wrong avatar, photo, or scene style.
