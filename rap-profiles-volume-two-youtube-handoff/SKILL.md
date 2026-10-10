---
name: rap-profiles-volume-two-youtube-handoff
description: Verify and register an individual YouTube video for a released Rap Profiles Volume II day. Use when Lord Judah or the Daily Posting Agent pastes a Volume II YouTube link, asks to replace a playlist fallback with a direct video, or needs a per-day YouTube handoff repaired.
---

# Rap Profiles Volume II YouTube Handoff

Use this workflow only for **one stated Volume II day and one pasted YouTube URL**. It maintains the direct-video handoff after the Daily Posting Agent publishes; it does not publish, upload, schedule, modify captions, or alter ManyChat.

## Ground rules

- Use YouTube Pro first. Run `manus-config config load --search youtube` only when connector state must be confirmed.
- The official playlist ID is `PLew51Xxv9eLA` on the LORD JUDAH channel.
- The site releases a Volume II report at **3:00 PM Eastern**. Do not add a direct handoff before that day’s report is public.
- A playlist fallback is intentional. Do not substitute an unrelated video or accept an unlisted/private video.
- A pasted link does **not** create an automatic social post, publish a video, or change an automation.

## Verification and update procedure

1. Extract the stated day and pasted URL. If either is missing, ask for only the missing item.
2. Confirm the day, artist, and release status in `/home/ubuntu/rap-report-recovered/client/src/data/volume2Profiles.json` and the live Volume II report. Reject a future day until after its 3:00 PM Eastern release.
3. Verify the URL with the bundled script:

   ```bash
   python /home/ubuntu/skills/rap-profiles-volume-two-youtube-handoff/scripts/verify_volume_two_handoff.py '<PASTED_URL>'
   ```

   Accept only if the result says `"accepted": true`. Confirm the returned public title reasonably corresponds to the scheduled artist.
4. Read `references/registry.md`. Add or update one valid record for the stated day in `client/src/data/volume2VideoHandoffs.json`. Never create duplicate day entries.
5. Run the focused tests and validation:

   ```bash
   cd /home/ubuntu/rap-report-recovered
   pnpm exec vitest run server/volumeTwoRollout.test.ts server/volumeTwo.test.ts
   pnpm check
   pnpm build
   ```

6. Open `/volume-2/day/<DAY>` and confirm the button reads **Watch the official Rap Profiles video**, opens the verified direct URL, and the note says it is a verified direct-video handoff.
7. Save a web project checkpoint. Report the verified day, artist, direct URL, and that no social post or automation was changed.

## Rejection cases

Do not register the URL when it is private, unlisted, deleted, absent from the official playlist, mismatched to the stated artist, already assigned to another day, or the report is still scheduled. State the concrete reason and leave the playlist fallback intact.
