# Asset Approval Tracker

This file is a focused approval log for Lord Judah's production assets. Use it alongside `master-asset-registry.md` whenever an avatar, voice, image, generated identity preset, scene preset, or performance preset is approved, restricted, revised, or retired.

The master registry stores the current state. This tracker stores the **decision history** behind that state.

## Approval Categories

| Decision type | Meaning | Registry action |
|---|---|---|
| Approved as default | Asset can be used automatically for its category | Mark as **Approved default** in the master registry |
| Approved with conditions | Asset is approved only for certain workflows or moods | Mark as **Approved conditional** and document the constraint |
| Task-only approval | Asset worked for one project but is not yet reusable by default | Mark as **Task-specific** |
| Revision required | Asset is promising but needs changes before reuse | Keep as **Pending review** |
| Retired | Asset should no longer be selected automatically | Mark as **Retired** |

## Decision Log

| Date | Asset label | Asset type | Decision type | Approved for | Not approved for | Reason | Confirmed by | Follow-up action |
|---|---|---|---|---|---|---|---|---|
| To be filled | Golden Hour Mural Street | Scene preset | Approved as default | Walk-and-talk clips, uplifting artist promos | Dark grief scenes unless restyled | Strong result in HeyGen walk-and-talk test | Lord Judah | Keep as default urban walk-and-talk preset |
| To be filled | Lord Judah Main Talking Avatar | Avatar | Approved as default | General speaking videos | To be filled | To be filled | Lord Judah | Fill exact ID when confirmed |
| To be filled | Lord Judah Main Voice | Voice | Approved as default | Standard Lord Judah delivery | To be filled | To be filled | Lord Judah | Fill exact ID when confirmed |

## Update Rule

Whenever the user says a result is **great**, **that works**, **use this going forward**, or gives an equally clear approval signal, capture the asset decision here and then update the matching approval state in `master-asset-registry.md`.

Whenever the user says an asset is **wrong**, **not that one**, **too static**, **too artificial**, or otherwise rejects it, record the outcome here and reduce or remove its default status in the master registry.

## Review Habit

At the start of future production tasks, scan this tracker for previously approved defaults before asking unnecessary asset-selection questions.
