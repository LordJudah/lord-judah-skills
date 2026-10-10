#!/usr/bin/env python3
"""
gen_day25_narration.py
Generates the Day 25 Rap Dojo launch narration via ElevenLabs
and builds the 9:16 reel video.
"""

import os
import subprocess
from pathlib import Path

VOICE_ID = "q2n4EHze5vKn16p2mMV1"  # Lord Judah ElevenLabs voice
MODEL_ID = "eleven_multilingual_v2"
OUTPUT_DIR = Path("/home/ubuntu/projects/rap-profiles-1d0d536b")
BG_COLOR = "#1A1A1A"  # Rap Dojo charcoal

def generate_audio(script_text, audio_path):
    from elevenlabs import ElevenLabs
    client = ElevenLabs(api_key=os.environ["ELEVENLABS_API_KEY"])
    print("Generating narration via ElevenLabs...")
    audio = client.text_to_speech.convert(
        voice_id=VOICE_ID,
        text=script_text,
        model_id=MODEL_ID,
        output_format="mp3_44100_128",
        voice_settings={
            "stability": 0.55,
            "similarity_boost": 0.85,
            "style": 0.30,
            "use_speaker_boost": True
        }
    )
    with open(audio_path, "wb") as f:
        for chunk in audio:
            f.write(chunk)
    print(f"  Audio saved: {audio_path}")
    return str(audio_path)


def pad_image_to_9x16(cover_path, output_path):
    cmd = [
        "ffmpeg", "-y",
        "-i", cover_path,
        "-vf", f"scale=1080:1350,pad=1080:1920:0:285:color={BG_COLOR}",
        "-update", "1", "-frames:v", "1",
        output_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR padding image: {result.stderr[-300:]}")
        raise RuntimeError("ffmpeg pad failed")
    print(f"  Padded image saved: {output_path}")
    return output_path


def get_duration(audio_path):
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
         "-of", "csv=p=0", audio_path],
        capture_output=True, text=True
    )
    return float(result.stdout.strip())


def build_video(image_path, audio_path, output_path):
    duration = get_duration(audio_path)
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-framerate", "30", "-i", image_path,
        "-i", audio_path,
        "-c:v", "libx264", "-tune", "stillimage",
        "-c:a", "aac", "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-t", str(duration),
        "-shortest",
        output_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR building video: {result.stderr[-300:]}")
        raise RuntimeError("ffmpeg video build failed")
    size_mb = Path(output_path).stat().st_size / (1024 * 1024)
    print(f"  Reel saved: {output_path} ({duration:.1f}s, {size_mb:.1f}MB)")
    return output_path


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate Rap Dojo narration and reel")
    parser.add_argument("--day", required=True, help="Day number (e.g., 26)")
    parser.add_argument("--script_file", required=True, help="Path to text file containing the narration script")
    parser.add_argument("--cover", required=True, help="Path to the 4:5 Dojo card PNG")
    parser.add_argument("--output_dir", required=True, help="Directory to save outputs")
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(args.script_file, "r") as f:
        script_text = f.read().strip()

    cover = args.cover
    audio = str(out_dir / f"day{args.day}_dojo_narration.mp3")
    padded = str(out_dir / f"day{args.day}_dojo_bg_9x16.png")
    reel = str(out_dir / f"day{args.day}_dojo_reel.mp4")

    generate_audio(script_text, audio)
    pad_image_to_9x16(cover, padded)
    build_video(padded, audio, reel)
    print(f"\n✅ Day {args.day} Rap Dojo reel package complete.")
