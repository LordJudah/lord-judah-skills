#!/usr/bin/env python3
"""Batch-test the BoomBap Futurist transmuter prompt on local thread files.

Dry-run the prompt before wiring it into Apify:

  python3 run_transmuter.py samples/*.txt
  python3 run_transmuter.py --dir ./scraped_threads --out ./outputs --workers 4

Each input .txt is treated as one scraped thread. Outputs are written to the
output directory as <name>.transmuted.md. Uses the sandbox LLM proxy (OpenAI
SDK, env-configured). Default model: gpt-5.5 (frontier class — do not drop to
cheap models for this task; they flatten the voice and leak source phrasing).
"""
import argparse
import concurrent.futures as cf
import pathlib
import time

from openai import OpenAI

PROMPT_PATH = (
    pathlib.Path(__file__).resolve().parent.parent / "templates" / "transmuter-prompt.txt"
)


def run_one(client, template, path, out_dir, model):
    src = path.read_text()
    prompt = template.replace("{{PASTE_THREAD_TEXT_HERE}}", src)
    t0 = time.time()
    resp = client.chat.completions.create(
        model=model,
        max_completion_tokens=4000,
        messages=[{"role": "user", "content": prompt}],
    )
    out = (resp.choices[0].message.content or "").strip()
    dest = out_dir / f"{path.stem}.transmuted.md"
    dest.write_text(out + "\n")
    return path.name, len(src), len(out), time.time() - t0


def main():
    ap = argparse.ArgumentParser(description="Transmute thread files with the LJB prompt.")
    ap.add_argument("files", nargs="*", help="thread text files")
    ap.add_argument("--dir", help="directory of .txt thread files")
    ap.add_argument("--out", default="transmuted", help="output directory")
    ap.add_argument("--model", default="gpt-5.5")
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()

    files = [pathlib.Path(f) for f in args.files]
    if args.dir:
        files += sorted(pathlib.Path(args.dir).glob("*.txt"))
    if not files:
        raise SystemExit("No input files. Pass files or --dir.")

    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    template = PROMPT_PATH.read_text()
    client = OpenAI()

    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = [ex.submit(run_one, client, template, f, out_dir, args.model) for f in files]
        for fut in cf.as_completed(futs):
            name, nsrc, nout, dt = fut.result()
            print(f"{name}: {nsrc} chars in -> {nout} chars out in {dt:.1f}s")


if __name__ == "__main__":
    main()
