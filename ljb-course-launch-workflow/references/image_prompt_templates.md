# Image Prompt Templates — LJB Course Launch Workflow

All prompts use the Lord Judah brand aesthetic: black background, gold/purple/white palette, cinematic lighting, sacred geometry, hip-hop cypher circle, golden crown. Replace `{VARIABLES}` before use.

---

## Course Cover Image (4:3)

```
Create a cinematic course cover image for an online course titled '{COURSE_TITLE}' by {INSTRUCTOR}.
Feature a glowing golden cypher circle at the center, radiating warm gold and deep purple light
against a rich black background. Inside the circle, subtle sacred geometry patterns and soundwave
frequencies emanate outward. A crown symbol hovers above the circle in gold. Bold text reads
'{COURSE_TITLE}' in gold bold sans-serif, '{COURSE_SUBTITLE}' in white elegant serif below it,
and 'by {INSTRUCTOR}' in silver at the bottom. Values flanking the scene: 'Mind Body Soul Mission'
on the left, 'Creativity Discipline Purpose Legacy' on the right. Cinematic lighting, deep shadows,
gold and purple brand colors, premium educational brand aesthetic.
Mood: powerful, visionary, elevated, transformative.
```

**Settings:** `aspect_ratio: "4:3"`, `quality: "high"`

---

## Promotional Banner (16:9)

Use the cover image as `references` input for visual consistency.

```
Wide cinematic promotional banner (16:9) for '{COURSE_TITLE}' by {INSTRUCTOR}.
Left side: the hip-hop cypher circle scene with sacred geometry and purple soundwaves,
slightly faded as a background element. Right side text hierarchy:
large bold gold 'NOW ENROLLING',
large white bold sans-serif '{COURSE_TITLE}',
large gold serif '{COURSE_SUBTITLE}',
thin gold ornamental divider line,
white medium '{MODULE_COUNT} Modules · Video Lessons · Creative Exercises',
gold rectangular CTA button with black text 'ENROLL NOW — ${PRICE}',
silver small '{BRAND_DOMAIN}'.
Deep black background, gold/purple palette, cinematic vignette, left visual / right text split.
Style: premium educational brand, cinematic hip-hop aesthetic, powerful and elevated.
```

**Settings:** `aspect_ratio: "16:9"`, `quality: "high"`, `references: [cover image path]`

---

## Story Banner (9:16)

Use the cover image as `references` input for visual consistency.

```
Vertical 9:16 Instagram/TikTok Story promotional image for '{COURSE_TITLE}' by {INSTRUCTOR}.
Top: glowing gold crown at the very top center with light rays emanating downward.
Middle: full hip-hop cypher circle scene with sacred geometry flower of life pattern glowing gold
at center, purple soundwave frequencies on both sides, silhouetted figures seated in a circle,
cinematic dramatic lighting.
Bottom text hierarchy:
large bold gold graffiti-style 'NOW ENROLLING',
large white bold sans-serif '{COURSE_TITLE}',
large gold serif '{COURSE_SUBTITLE}',
thin gold ornamental divider,
white '{MODULE_COUNT} Modules · Video Lessons · Creative Exercises',
prominent gold rectangular CTA button with black bold text 'ENROLL NOW — ${PRICE}',
silver small '{BRAND_DOMAIN}'.
Deep black background, centered composition, cinematic vignette, dramatic top-to-bottom flow.
```

**Settings:** `aspect_ratio: "9:16"`, `quality: "high"`, `references: [cover image path]`
