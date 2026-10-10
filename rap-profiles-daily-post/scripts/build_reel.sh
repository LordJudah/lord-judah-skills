#!/bin/bash
# Build a narration-only 9:16 reel from a card image + narration audio.
#
# Usage: bash build_reel.sh <card_image> <narration_audio> <output_mp4>
#
# IMPORTANT (user preference, locked Jul 2026): NO background music is baked in.
# Lord Judah adds commercially available music himself in Instagram edits.
# Output: 1080x1920, 30fps. Full card centered over a blurred/darkened echo of
# itself, slow cinematic zoom. Narration delayed 600ms, 0.8s fade-out,
# total duration = narration + 1.5s.
set -e

IMG="$1"
VOICE="$2"
OUT="$3"

if [ -z "$IMG" ] || [ -z "$VOICE" ] || [ -z "$OUT" ]; then
  echo "Usage: bash build_reel.sh <card_image> <narration_audio> <output_mp4>"
  exit 1
fi

DUR=$(ffprobe -v quiet -show_entries format=duration -of csv=p=0 "$VOICE")
TOTAL=$(python3 -c "print(round(float('$DUR') + 1.5, 2))")
FRAMES=$(python3 -c "print(int(float('$TOTAL') * 30))")
FADE_ST=$(python3 -c "print(round(float('$TOTAL') - 0.8, 2))")

ffmpeg -y \
  -loop 1 -framerate 30 -i "$IMG" \
  -i "$VOICE" \
  -filter_complex "\
    [0:v]split=2[bg][fg];\
    [bg]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=30,eq=brightness=-0.15[bgv];\
    [fg]scale=1080:1920:force_original_aspect_ratio=decrease[fgv];\
    [bgv][fgv]overlay=(W-w)/2:(H-h)/2,\
    zoompan=z='min(zoom+0.0003,1.08)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=${FRAMES}:s=1080x1920:fps=30,format=yuv420p[v];\
    [1:a]adelay=600|600,afade=t=out:st=${FADE_ST}:d=0.8[a]" \
  -map "[v]" -map "[a]" \
  -t "$TOTAL" \
  -c:v libx264 -preset medium -crf 19 -r 30 \
  -c:a aac -b:a 192k \
  "$OUT"

echo "Built $OUT (${TOTAL}s)"
