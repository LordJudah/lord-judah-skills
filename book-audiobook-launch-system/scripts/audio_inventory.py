#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path

AUDIO_EXTENSIONS = {'.wav', '.mp3', '.m4a', '.aac', '.flac', '.ogg'}


def probe(path: Path) -> dict[str, str | float | int]:
    command = [
        'ffprobe', '-v', 'error', '-show_streams', '-show_format',
        '-of', 'json', str(path),
    ]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    payload = json.loads(result.stdout)
    streams = [stream for stream in payload.get('streams', []) if stream.get('codec_type') == 'audio']
    if not streams:
        raise ValueError('no audio stream')
    stream = streams[0]
    duration_text = payload.get('format', {}).get('duration') or stream.get('duration') or '0'
    return {
        'duration_seconds': round(float(duration_text), 3),
        'codec': stream.get('codec_name', ''),
        'sample_rate_hz': int(stream.get('sample_rate') or 0),
        'channels': int(stream.get('channels') or 0),
        'bytes': path.stat().st_size,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description='Inventory audiobook audio files with ffprobe.')
    parser.add_argument('source', type=Path, help='Source directory containing audio files.')
    parser.add_argument('output', type=Path, help='Destination TSV file.')
    args = parser.parse_args()

    source = args.source.expanduser().resolve()
    output = args.output.expanduser().resolve()
    if not source.is_dir():
        print(f'ERROR: source directory does not exist: {source}', file=sys.stderr)
        return 2

    files = sorted(path for path in source.rglob('*') if path.is_file() and path.suffix.lower() in AUDIO_EXTENSIONS)
    if not files:
        print(f'ERROR: no supported audio files found in {source}', file=sys.stderr)
        return 3

    rows: list[dict[str, str | float | int]] = []
    errors: list[str] = []
    for path in files:
        try:
            row = probe(path)
            row['relative_path'] = path.relative_to(source).as_posix()
            rows.append(row)
        except Exception as exc:
            errors.append(f'{path}: {exc}')

    output.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ['relative_path', 'duration_seconds', 'codec', 'sample_rate_hz', 'channels', 'bytes']
    with output.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)

    total = sum(float(row['duration_seconds']) for row in rows)
    print(f'files={len(rows)} total_seconds={total:.3f} output={output}')
    if errors:
        print('\n'.join(f'ERROR: {message}' for message in errors), file=sys.stderr)
        return 4
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
