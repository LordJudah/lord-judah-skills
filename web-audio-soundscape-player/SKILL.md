---
name: web-audio-soundscape-player
description: Create, repair, or extend a web background-soundscape experience with original loop generation, accessible playback controls, mode switching, seamless crossfades, and a subtle visualizer. Use for landing pages, campaign sites, portfolios, learning platforms, or brand experiences that need optional background music users can hear and control.
---

# Web Audio Soundscape Player

Build **optional, listener-controlled** background soundscapes that enhance a site without competing with its content.

## Operating Principles

- Use original instrumental loops unless the user explicitly requests licensed material or vocals.
- Start sound only from a clear user action. Do not rely on autoplay with sound.
- Default to a modest volume (about 20–25%) and provide a visible range control.
- Keep the player persistent, compact, keyboard-accessible, and easy to pause.
- Use native `<audio>` playback as the default path. It is the most reliable way to make stored MP3 assets audible across browsers.
- Treat a visualizer as enhancement—not the audio transport layer.

## Creation Workflow

1. **Define the listening roles.**
   - Create one default ambient loop.
   - Add optional modes only when they have distinct jobs, for example:
     - **Focus:** sparse, low-density reading or reflection bed.
     - **Cipher:** subtly rhythmic, warm creative-momentum bed.
   - Keep each loop 45–90 seconds, instrumental, consistent in loudness, and written to repeat without a final hit or fade.

2. **Generate the music.**
   - Read the `music-prompter` skill before generating.
   - Use one generation call per loop at 180 seconds or less.
   - State at the beginning: duration, BPM, key, and `Instrumental only, no vocals`.
   - Specify: begin/end with the same harmony, ambience, pulse, and energy; no fade-out, no silence at the seam.
   - Avoid aggressive percussion, big drops, vocal chops, spoken words, or intrusive melodies unless the user asks for them.

3. **Inspect and store audio.**
   - Keep originals in `/home/ubuntu/webdev-static-assets/`.
   - Inspect each file with `ffprobe` for duration, codec, sample rate, channels, and bitrate.
   - Check loudness with `ffmpeg`/`ebur128`; prioritize consistent relative levels rather than chasing a universal target.
   - Upload only verified assets using:
     ```bash
     manus-upload-file --webdev /absolute/path/to/loop.mp3
     ```
   - Use the returned `/manus-storage/...` path in the project.

4. **Implement direct audio playback.**
   - Render two native `<audio preload="auto">` elements to support crossfades.
   - Set their sources imperatively after mount; do not let React reset a source mid-switch.
   - Use `audio.play()` only in a listener gesture such as the player button or a mode selection.
   - Never set `crossOrigin` or create a `MediaElementAudioSourceNode` just to play storage-hosted audio.
   - Keep `muted` false and set `audio.volume` from the listener-controlled value.
   - Use the dual-player crossfade pattern in `references/implementation-pattern.md`.

5. **Add controls and modes.**
   - Provide one prominent play/pause button, a mode selector, and a labeled volume slider.
   - Update labels as state changes, e.g. `Play Focus Mode`, `Pause Cipher Mode`.
   - Prefetch inactive loop URLs immediately after initial load and after every completed selection.
   - When switching modes while playing, start the inactive element from zero volume, crossfade over about 1–1.5 seconds, then reset the outgoing element to the newly selected source.
   - Finalize every switch through both the animation completion and a short timeout fallback; the finalizer must be idempotent and always restore the incoming element to listener volume.
   - If an incoming `play()` rejects, keep the current loop audible and offer a calm retry status rather than throwing a visible error.
   - For a continuous loop, start the inactive copy about 3.5 seconds before the active track ends and crossfade before its endpoint.

6. **Add a restrained visualizer.**
   - Use a small row of 8–14 brand-colored bars inside the player.
   - Prefer a time-synced visualizer based on the active track’s `currentTime` when assets are cross-origin or CORS is not proven.
   - Use `AnalyserNode` only if CORS is verified **and** the graph routes audio all the way to the destination. Never route audio exclusively through an analyser without testing actual speaker output.
   - Set visualizer bars to rest when paused and honor reduced-motion preferences when practical.

7. **Validate before delivery.**
   - Run all relevant unit tests, type checks, production build, and `git diff --check`.
   - In a real browser, click Play and verify the active audio element reports: `paused: false`, `muted: false`, `readyState: 4`, advancing `currentTime`, and a nonzero volume.
   - Test one live mode switch and one forced near-end crossfade.
   - Confirm all uploaded asset URLs return media content.
   - Capture desktop and mobile previews to verify the fixed player does not obscure key controls.
   - Ask the project owner to confirm audible output on their own device when browser/system audio cannot be monitored remotely.

## Audible Playback Triage

When the player says “playing” but users hear nothing, troubleshoot in this order:

1. **Browser/system state:** inspect site mute state, browser tab mute, OS volume, and output device.
2. **Element state:** confirm `paused === false`, `muted === false`, `volume > 0`, `readyState >= 3`, and advancing `currentTime`.
3. **Native first:** remove or bypass Web Audio routing. Test the same loop using native `<audio>` output directly.
4. **Asset response:** request the storage asset and confirm a valid `audio/mpeg` response, not an HTML error page.
5. **Crossfade state:** ensure only the intended active element carries audible volume after a transition.
6. **CORS/Web Audio:** if using an analyser, verify `Access-Control-Allow-Origin` and route `source -> analyser -> destination` or `source -> destination` plus a safe analysis tap.

## Quality Bar

- The music should feel intentional, ambient, and brand-specific—not generic stock “lo-fi.”
- The player should be optional, not coercive.
- The visualizer should reinforce activity with quiet gold motion, not compete with the hero or calls to action.
- Explain browser autoplay behavior plainly: visitors start audio on their first tap.

## Reference

Read `references/implementation-pattern.md` before implementing dual audio, mode changes, or a visualizer.
