# Image Selection for Soul Training

A Soul is only as good as its inputs. This file defines what qualifies, what to exclude, and why.

## Acceptance rules

An image qualifies when **all** of these hold:

| Rule | Threshold | Why |
|---|---|---|
| Resolution | ≥ 1 MP, ideally ≥ 4 MP | Low-res inputs teach blur; the Soul bakes softness into the face |
| Faces | exactly one person | A second face splits the identity across two people |
| Face size | face ≥ ~¼ of the frame | Small faces give the model too few identity pixels |
| Focus | sharp on the eyes and face, **judged by eye** | Soft focus is learned as a real feature |
| Pose | front or three-quarter facing the lens | Profile-heavy sets under-constrain the face |
| Provenance | a genuine photograph | Synthetic inputs produce a synthetic-looking identity |
| Era | one grooming era across the whole set | Beard/hair/weight changes read as identity |

Target **12–16 images**. The floor is 5; past ~20, extra images mostly add redundancy.

## On the preflight metrics — read this before rejecting anything

`scripts/preflight_images.py` produces flags, and two of them are advisory by design:

**`detail energy` does not measure focus.** It was calibrated against known-good
images and it tracks *scene smoothness and depth of field*, not sharpness:

| Image type | Typical detail energy |
|---|---|
| Busy real-world photograph | 30–76 |
| Sharp shallow-DOF studio portrait, smooth backdrop | 9–12 |
| Genuinely flat or failed export | < 4 |

A dramatic studio portrait legitimately scores 9–12 while being perfectly sharp
on the face. **Never reject on this number alone** — view the image. The script
only flags below 4, which catches blank and failed exports.

**Background class is a provenance cue, not a disqualifier.** `green` and `white`
label composited or studio work. A Soul learns faces, not backgrounds, so a
genuine photograph against a green screen can train fine. What the flag really
tells you is: *this file is more likely to be synthetic or heavily retouched —
confirm it is a real photograph before using it.*

## Diversity beats volume

Spread the set across these axes — this is what makes a Soul generalise instead of reproducing one session:

- **Angle** — front, three-quarter left, three-quarter right, and at least one profile
- **Environment** — indoor, outdoor, transit, studio
- **Lighting** — daylight, overhead fluorescent, low key, mixed
- **Expression** — neutral, engaged, speaking, smiling

Near-duplicates from one outing waste slots. Cluster them with `scripts/preflight_images.py` and keep one per cluster. In a 143-image brand archive, 14 near-duplicate pairs were found this way — roughly one in ten files was redundant.

## Reject categories

| Category | Signal | Reason |
|---|---|---|
| Low-resolution crops | under ~1 MP | Teaches blur |
| Collages and contact sheets | grid layout, sheet-derived crops | Each tile carries composite artifacts |
| Brand benchmark / canon images | the approved identity targets | These are what you compare *against*; never train on them |
| Travel and event photos | face tiny in frame or distant | Unusable as face references |
| Archival scans | under ~0.5 MP | Insufficient detail |
| Rotated frames | EXIF orientation flag or visibly turned | Verify orientation before use |
| AI-generated or airbrushed renders | glossy skin, impossible highlights | The Soul learns an average, not the person |
| Green-screen / pure-white backgrounds | border-ring class flag | **Not an automatic reject** — verify provenance, then decide |

## Worked example

A 143-image brand folder, audited with the preflight script:

- **64 candidates** met the raw resolution bar; **45 passed** all checks, **18 needed review**, **1 was unreadable**.
- **Review flags:** 12 green-screen backgrounds, 3 pure-white studio backgrounds, 3 EXIF-rotated frames.
- **14 near-duplicate clusters** found.
- **14 images selected** — one consistent era, all 7.15 MP, real environments (classroom, subway, graffiti wall, office), front and three-quarter only.
- **Excluded by category:** canon and approved-campaign renders (prohibited as inputs); twelve 274 px core crops and eighteen files at 156–295 px; the multi-angle collage sheet; Peru, Egypt and event photos where the face was tiny, distant, or rotated 180°; and 2008–2015 scans at 0.12–0.43 MP.

The first Soul trained on those 14 produced a correct face but cropped hair —
because every one of the 14 had the head covered. Adding 9 uncovered images in
the same era and retraining fixed it. Three of those 9 were green-screen frames:
their background was irrelevant, and the hair and face were exactly what the Soul
needed. See the accessory-bias section in SKILL.md.

## When provenance is unclear

If a folder contains files that might be AI-generated, ask the user to confirm which are genuine photographs before training. Do not attempt to decide by appearance alone — polished studio work and good AI renders are hard to separate visually, and the user knows their own archive.

Never mix uncertain files into a set on a "probably fine" basis. Excluding a genuine photo costs almost nothing; including a synthetic one corrupts the identity and costs a full retrain.