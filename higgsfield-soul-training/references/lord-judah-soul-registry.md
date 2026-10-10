# Lord Judah / Judah Bless Ent — Soul Registry

Working example of a maintained Soul registry. Update this file whenever a Soul is trained or retired.

**Account:** Higgsfield `ultra` plan · namespace `user_31UqBH8Z44fGKMWy0PUhQxaEIFA`

## Souls

| Soul | ID | Images | State | Use |
|---|---|---|---|---|
| **Lord Judah Canon Soul** | `0ab73239-9ba3-445f-b322-cb59f49ac126` | 15 (6 headwear + 9 locs-down) | `ready` | **Production** — renders face and locs correctly against the Canon Architect |
| Lord Judah Soul | `5aa6ece4-0548-4082-b208-abe3c65eed37` | 6 headwear | `ready` | Identity correct, hair close-cropped — superseded |
| Lord Judah Architect Test | `e4b42e73-8b6d-48d6-9f52-9d3f7957fbbe` | 12 headwear | `ready` | Recipe validation only |
| Lord Judah | `1fdce976-6d4a-4f98-a968-712c0dd7a119` | 14 | `failed` | Failed via the flat `images` parameter |
| Lord Judah Core Identity | `7c81e135-a5b4-4d2b-8375-0d718f9c4c2b` | 10 | `failed` | Failed via the flat `images` parameter |

## Production call

```json
{"params": {"model": "soul_2",
            "soul_id": "0ab73239-9ba3-445f-b322-cb59f49ac126",
            "prompt": "<scene, wardrobe, framing, lighting>",
            "aspect_ratio": "9:16"}}
```

Pair with the Lord Judah visual canon for wardrobe, palette, and scene direction. Souls are image-only; for video, pass Canon reference images into the video model instead.

## Era note

Two grooming eras exist in the source archive:

- **Era 1 — headwrap self-portraits:** mature features, full salt-and-pepper beard, headwear. Real-camera, 7.15 MP, mixed environments.
- **Era 2 — locs-down studio / green screen:** long locs visible, leaner facial presentation, dramatic studio lighting.
- **Era 3 — short-fade studio:** short faded haircut, thick dark beard, white studio background. Excluded from all training.

The production Soul blends **Era 1 + Era 2** deliberately, to defeat accessory bias while keeping the locs on canon. That blend is the reason it renders locs correctly.

**Open item:** if Era 3 is ever confirmed as the current look, build a separate Soul for it rather than merging.

## Media IDs

### Headwear set (Era 1)
| Upload | Source | media_id |
|---|---|---|
| lj_train_01 | judahprime_15.jpg | `1173e0ba-9d5f-4de7-8338-8b37352a87ba` |
| lj_train_02 | judahprime_14.jpg | `cf05d636-aed6-4d8c-a607-51d318ec2a73` |
| lj_train_03 | judahprime_13.jpg | `5b89951b-91be-432e-86f8-d37a72a32efd` |
| lj_train_04 | judahprime_12.jpg | `eefcaf54-b036-4a59-ab74-086952e51339` |
| lj_train_05 | judahprime_20.jpg | `d0cbda12-f39e-4d18-8c8b-cb2ceb6408ae` |
| lj_train_06 | judahprime_19.jpg | `0c95520d-986b-4acb-b241-f55964ef718f` |
| lj_train_07 | judahprime_18.jpg | `7031a160-8e1e-4b35-b501-1a1f09c2b1e9` |
| lj_train_08 | judahprime_17.jpg | `2f869a5d-eb38-4f23-9353-c44b4d2cf46e` |
| lj_train_09 | LORD JUDAH TEACHING PRESENTATION.jpg | `80132105-5b88-4a4a-b780-ce6866b29b61` |
| lj_train_10 | LORD JUDAH FOCUSED.jpg | `c1c4e437-4a0c-4237-8c60-288121b81722` |
| lj_train_11 | LORD JUDAH PRESENTATION WITH TRUE HE(ART) ACADEMY.jpg | `790bde61-c301-4699-bf53-f503219f64ce` |
| lj_train_12 | LORD JUDAH WORKING TAKING THE SUBWAY.jpg | `6c5eea33-95a0-41fe-859d-684f8fddb0dc` |
| lj_train_13 | LORD JUDAH CHILL 2.jpg | `c8b7127a-b656-4cf2-b060-81be44927774` |
| lj_train_14 | LORD JUDAH CHILL 1.jpg | `b39031e3-c145-404d-be34-b8681d794ffe` |

### Locs-down set (Era 2)
| Upload | Source | media_id |
|---|---|---|
| lj_locs_01 | judahprime_02.jpg (green screen) | `cb219693-278d-429e-9c91-3a824968d339` |
| lj_locs_02 | IMG_7601.JPG (green screen) | `c539072f-204e-443a-a57e-504eeaad4a5f` |
| lj_locs_03 | IMG_7599.JPG (green screen) | `467f84b4-950b-4d1e-bb4e-ff58f6f08446` |
| lj_locs_04 | judahprime_10.jpg (studio) | `acd78946-01f4-4991-917b-6e787ae66e24` |
| lj_locs_05 | IMG_7364.jpg (studio) | `ab32f3cf-243f-442b-88de-26880ac5294a` |
| lj_locs_06 | IMG_7354.jpg (studio profile) | `77e7eca0-2a9c-47d1-9a4a-cf9b6dbbffc2` |
| lj_locs_07 | IMG_7356.jpg (white blazer) | `a4e16fe5-bdf8-4ae9-a96e-31268963b3ed` |
| lj_locs_08 | IMG_7352.jpg (white jacket) | `874e79d0-5cf7-4edd-a705-ed9fcfc77bca` |
| lj_locs_09 | IMG_7355.jpg (white blazer) | `15c4145b-b0d6-4de8-a845-a5fdced9d929` |

## Source archives

- **Training-quality photo folder:** Drive `144MNwGy6EGdQ9mLupe1L92GeTGiwZgrJ`
- **Canon benchmarks:** the Core Identity Reference Pack — the four pillar images (Architect, Sound Alchemist, Cultural Guardian, Crowned Legacy). Compare against these; never train on them.

## Known gaps in the source archive

1. Only one profile exists across the whole archive (`IMG_7354`) — request more.
2. The Era 1 self-portrait set is front and three-quarter only.
3. Several Era 1 files are near-duplicates from the same outings — de-duplicate before adding.
4. High-value additions: locs-down shots in the **current** era, which would remove the Era 1/2 blend entirely.