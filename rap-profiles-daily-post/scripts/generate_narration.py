#!/usr/bin/env python3
"""Generate a Lord Judah narration MP3 from a script text file via ElevenLabs.

Usage:
    python3 generate_narration.py <script_text_file> <output_mp3_path>

Requires env var ELEVENLABS_API_KEY. Uses the confirmed Lord Judah voice
(q2n4EHze5vKn16p2mMV1) with the settings validated on the Rap Profiles series.
Strip markdown headers/formatting from the script file before passing it in,
or pass a plain-text file containing only the words to be spoken.
"""
import os
import sys
import requests

VOICE_ID = "q2n4EHze5vKn16p2mMV1"  # Lord Judah (confirmed by user)


def main() -> None:
    if len(sys.argv) != 3:
        print(__doc__)
        raise SystemExit(1)
    script_path, out_path = sys.argv[1], sys.argv[2]
    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        print("ERROR: ELEVENLABS_API_KEY not set in environment")
        raise SystemExit(1)
    with open(script_path, "r", encoding="utf-8") as f:
        text = f.read().strip()

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {"xi-api-key": api_key, "Content-Type": "application/json"}
    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.45,
            "similarity_boost": 0.85,
            "style": 0.35,
            "use_speaker_boost": True,
        },
        "output_format": "mp3_44100_128",
    }
    resp = requests.post(url, headers=headers, json=payload, timeout=300)
    if resp.status_code != 200:
        print("ERROR", resp.status_code, resp.text[:500])
        raise SystemExit(1)
    with open(out_path, "wb") as f:
        f.write(resp.content)
    print(f"Saved: {out_path} ({len(resp.content)} bytes)")


if __name__ == "__main__":
    main()
