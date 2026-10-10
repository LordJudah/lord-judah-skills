# Implementation Pattern: Direct Playback + Dual-Element Crossfade

## Track Model

```ts
type SoundscapeTrack = {
  id: string;
  label: string;
  description: string;
  src: string; // /manus-storage/...mp3
};
```

Use two `<audio>` elements. Keep `activeIndex`, `isPlaying`, `isFading`, and a listener volume value in refs so animation frames do not depend on stale render state.

## Native Playback Rule

```ts
activeAudio.volume = listenerVolume;
await activeAudio.play(); // must run from a user gesture
```

Do **not** send a storage-hosted `<audio>` element through `createMediaElementSource()` unless CORS and destination routing are fully verified. Native audio is the reliable default.

## Continuous Loop Handoff

Start the inactive copy while the active copy has a 3.5–4.5-second tail remaining. Fade one down and the other up using `requestAnimationFrame`. Start early enough that the outgoing copy is stopped before it reaches `ended`.

```ts
const progress = Math.max(0, Math.min(1, elapsed / crossfadeMs));
outgoing.volume = listenerVolume * (1 - progress);
incoming.volume = listenerVolume * progress;
```

On completion: pause and reset the outgoing copy; make the incoming index active.

## Mode Switch Handoff

When changing from a playing track to another:

1. Prefetch all inactive track URLs with `new Audio()` after the initial load and after every completed mode selection.
2. Select the inactive `<audio>` element.
3. Pause it, set `src` to the new track, call `load()`, reset `currentTime` to `0`, and set volume to `0`.
4. Call `play()` from the same listener gesture.
5. Crossfade 1–1.5 seconds with a clamped progress value.
6. Add a completion timeout just beyond the expected fade duration. Both the animation frame and timeout must call the same idempotent finalizer, which pauses/resets the outgoing player and restores the incoming player to the listener volume.
7. If `play()` rejects, preserve the outgoing loop at the listener volume, clear switching state, show a calm retry message, and never surface an unhandled browser error.
8. Update the visible selected mode only after handoff completes.

When not playing, set both sources to the selected track and do not auto-start it.

## Subtle Gold Visualizer

Use 8–14 narrow bars. Drive bar height from `activeAudio.currentTime` with phase offsets; this is stable for any native audio asset and needs no cross-origin analysis permission.

```ts
const level = 0.12 + Math.abs(Math.sin(time * rate + phase)) * 0.38;
```

- Use brand gold for bars.
- Keep maximum scale under about 0.7 of the available height.
- Lower opacity at rest; set all bar levels to zero on pause.
- If true frequency analysis is mandatory, verify CORS first and route the graph to `context.destination` before using the analyser values.

## Browser QA Console Check

```js
const active = [...document.querySelectorAll('audio')].find(a => !a.paused);
({
  paused: active?.paused,
  muted: active?.muted,
  volume: active?.volume,
  currentTime: active?.currentTime,
  readyState: active?.readyState,
  src: active?.currentSrc,
});
```

Expected: `paused: false`, `muted: false`, a nonzero volume, `readyState: 4` when fully buffered, and an advancing `currentTime`.
