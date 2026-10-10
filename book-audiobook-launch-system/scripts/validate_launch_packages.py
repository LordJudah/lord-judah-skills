#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import zipfile
from pathlib import Path
from typing import Any


def probe_video(path: Path) -> dict[str, Any]:
    command = [
        'ffprobe', '-v', 'error', '-select_streams', 'v:0',
        '-show_entries', 'stream=codec_name,width,height,r_frame_rate',
        '-show_entries', 'format=duration', '-of', 'json', str(path),
    ]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    payload = json.loads(result.stdout)
    stream = payload['streams'][0]
    return {
        'codec': stream.get('codec_name'),
        'width': int(stream.get('width') or 0),
        'height': int(stream.get('height') or 0),
        'frame_rate': stream.get('r_frame_rate'),
        'duration': round(float(payload.get('format', {}).get('duration') or 0), 3),
    }


def resolve(root: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else root / path


def main() -> int:
    parser = argparse.ArgumentParser(description='Validate a digital book launch from a JSON manifest.')
    parser.add_argument('manifest', type=Path, help='Launch manifest JSON.')
    parser.add_argument('report', type=Path, help='Markdown validation report.')
    args = parser.parse_args()

    manifest_path = args.manifest.expanduser().resolve()
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    root = resolve(manifest_path.parent, manifest.get('root', '.')).resolve()
    results: list[tuple[str, bool, str]] = []

    for package in manifest.get('packages', []):
        path = resolve(root, package['path'])
        label = f"Package: {package.get('name', path.name)}"
        if not path.is_file():
            results.append((label, False, f'missing: {path}'))
            continue
        try:
            with zipfile.ZipFile(path) as archive:
                corrupt = archive.testzip()
                members = archive.namelist()
            if corrupt:
                results.append((label, False, f'corrupt member: {corrupt}'))
                continue
            missing = [member for member in package.get('required_members', []) if member not in members]
            minimum = int(package.get('minimum_file_count', 1))
            file_count = sum(1 for member in members if not member.endswith('/'))
            if missing:
                results.append((label, False, f'missing members: {", ".join(missing)}'))
            elif file_count < minimum:
                results.append((label, False, f'file count {file_count} is below minimum {minimum}'))
            else:
                results.append((label, True, f'{file_count} files; ZIP integrity passed'))
        except Exception as exc:
            results.append((label, False, str(exc)))

    assets = manifest.get('assets', {})
    for key, spec in assets.items():
        directory = resolve(root, spec['directory'])
        files = sorted(directory.glob(spec.get('glob', '*'))) if directory.is_dir() else []
        expected = int(spec.get('expected_count', 0))
        passed = len(files) == expected if expected else bool(files)
        results.append((f'Asset count: {key}', passed, f'found {len(files)}, expected {expected or "one or more"}'))

        if key == 'reels' and files:
            width = int(spec.get('width', 1080))
            height = int(spec.get('height', 1920))
            codec = spec.get('codec', 'h264')
            failures: list[str] = []
            for path in files:
                try:
                    metadata = probe_video(path)
                    if metadata['width'] != width or metadata['height'] != height or metadata['codec'] != codec:
                        failures.append(f'{path.name}: {metadata}')
                except Exception as exc:
                    failures.append(f'{path.name}: {exc}')
            results.append((
                'Reel specifications',
                not failures,
                'all files passed' if not failures else '; '.join(failures),
            ))

    report_path = args.report.expanduser().resolve()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        '# Launch Package Validation',
        '',
        f'**Manifest:** `{manifest_path}`  ',
        f'**Root:** `{root}`',
        '',
        '| Check | Result | Detail |',
        '|---|---|---|',
    ]
    for label, passed, detail in results:
        safe_detail = detail.replace('|', '\\|').replace('\n', ' ')
        lines.append(f'| {label} | {"PASS" if passed else "FAIL"} | {safe_detail} |')
    passed_all = bool(results) and all(passed for _, passed, _ in results)
    lines.extend(['', f'## Overall Result: {"PASS" if passed_all else "FAIL"}', ''])
    report_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f'overall={"PASS" if passed_all else "FAIL"} report={report_path}')
    return 0 if passed_all else 1


if __name__ == '__main__':
    raise SystemExit(main())
