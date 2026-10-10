#!/usr/bin/env python3
"""council.py — Lord Judah Agent Council engine.

Convenes the Co-Director council (Claude, Muse, Perplexity, Grok) on a brief:
fan-out in parallel, optional cross-critique round, then a synthesis memo that
preserves dissent instead of averaging it away.

Dependency-free (stdlib only).

Usage
-----
    python3 council.py roster
    python3 council.py convene "brief text" [--mode quorum|full|duo] [--critique] [--context file]
    python3 council.py log [--limit 10]
    python3 council.py test

Exit codes: 0 = convened, 1 = error, 3 = no directors available.
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(HERE, "council_log")
TIMEOUT = 180

# --------------------------------------------------------------------------
# Council roster — role, lens, model, credential
# --------------------------------------------------------------------------

DIRECTORS = {
    "claude": {
        "title": "Director of Strategy & Structure",
        "model": "claude-sonnet-4-5-20250929",
        "env": "ANTHROPIC_API_KEY",
        "lens": (
            "You are the Director of Strategy & Structure on Lord Judah's creative council. "
            "Your lens: architecture, reasoning integrity, long-horizon consequences, and "
            "structural critique. You find the load-bearing assumption everyone else missed. "
            "You are precise about tradeoffs and you name the cost of each option. "
            "You care about cultural authenticity and ethical grounding in the work."
        ),
        "best_at": "strategy, brand architecture, long-form, structural critique, risk",
    },
    "muse": {
        "title": "Director of Visual & Social",
        "model": "muse-spark-1.1",
        "env": "META_API_KEY",
        "base_env": "META_API_BASE",
        "lens": (
            "You are the Director of Visual & Social on Lord Judah's creative council. "
            "Your lens: how the work LOOKS, how it FEELS in the feed, and how it travels "
            "on social platforms. You think in images, motion, and scroll-stopping moments. "
            "You judge whether a concept is visually ownable and platform-native."
        ),
        "best_at": "visual direction, social-native creative, multimodal concepting",
    },
    "perplexity": {
        "title": "Director of Research & Grounding",
        "model": "sonar-pro",
        "env": "SONAR_API_KEY",
        "lens": (
            "You are the Director of Research & Grounding on Lord Judah's creative council. "
            "Your lens: verifiable fact, current data, market context, and source quality. "
            "You correct premises that are factually wrong and you supply the evidence "
            "everyone else is guessing at. Cite sources. Flag uncertainty explicitly."
        ),
        "best_at": "live research, fact verification, market/competitor intel, citations",
    },
    "grok": {
        "title": "Director of Culture & Contrarian Stress-Test",
        "model": "grok-4",
        "env": "XAI_API_KEY",
        "lens": (
            "You are the Director of Culture & Contrarian Stress-Test on Lord Judah's "
            "creative council. Your lens: what the culture is ACTUALLY saying right now, "
            "and where this idea could fail or read wrong. You are the productive skeptic. "
            "You pressure-test assumptions, name what's cringe, and find the sharper angle. "
            "Be direct and unsentimental."
        ),
        "best_at": "real-time culture pulse, contrarian critique, trend timing, de-risking",
    },
}

ROLE_PREFIX = """You are speaking as a Co-Director of Judah Bless Ent.
Principal: Cornell "Lord Judah" Carelock — Creative Director, hip-hop artist, producer,
teaching artist. CEO of Judah Bless Ent; Director of True He(ART) Academy.
Voice: conscious hip-hop, boom-bap meets futuristic production, mindfulness, social impact,
cultural authenticity, community empowerment.

Stay in your lane. Do not try to answer as a generalist — the value of this council is that
each director brings a DISTINCT lens. Be specific and opinionated. Skip pleasantries.
"""

OUTPUT_CONTRACT = """
Respond in EXACTLY this structure, with no preamble:

VERDICT: <one sentence — your headline call on this brief>
CONFIDENCE: <high|medium|low>
KEY_POINTS:
- <3 to 5 sharp, specific points from your lens>
BIGGEST_RISK: <the one thing most likely to make this fail, from your lens>
RECOMMENDATION: <the single concrete action you'd take first>
DISSENT: <where you disagree with the likely consensus, or "none">
"""


# --------------------------------------------------------------------------
# provider adapters
# --------------------------------------------------------------------------


class DirectorError(Exception):
    pass


def _post(url, headers, body, timeout=TIMEOUT):
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:300]
        raise DirectorError(f"HTTP {exc.code}: {detail}") from None
    except urllib.error.URLError as exc:
        raise DirectorError(f"network: {exc.reason}") from None


def call_claude(system, user, key):
    out = _post(
        "https://api.anthropic.com/v1/messages",
        {
            "x-api-key": key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        {
            "model": DIRECTORS["claude"]["model"],
            "max_tokens": 2000,
            "system": system,
            "messages": [{"role": "user", "content": user}],
        },
    )
    return "".join(b.get("text", "") for b in out.get("content", []))


def call_openai_compatible(url, key, model, system, user, extra=None):
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "max_tokens": 2000,
    }
    if extra:
        body.update(extra)
    out = _post(url, {"Authorization": f"Bearer {key}", "content-type": "application/json"}, body)
    choice = (out.get("choices") or [{}])[0].get("message", {}) or {}
    text = choice.get("content") or ""
    cites = out.get("citations") or []
    if cites:
        text += "\n\nSOURCES:\n" + "\n".join(f"- {c}" for c in cites[:6])
    return text


def call_grok(system, user, key):
    return call_openai_compatible(
        "https://api.x.ai/v1/chat/completions", key, DIRECTORS["grok"]["model"], system, user
    )


def call_perplexity(system, user, key):
    return call_openai_compatible(
        "https://api.perplexity.ai/chat/completions",
        key,
        DIRECTORS["perplexity"]["model"],
        system,
        user,
    )


def call_muse(system, user, key):
    base = os.environ.get("META_API_BASE", "https://api.meta.ai/v1").rstrip("/")
    return call_openai_compatible(
        f"{base}/chat/completions", key, DIRECTORS["muse"]["model"], system, user
    )


CALLERS = {
    "claude": call_claude,
    "grok": call_grok,
    "perplexity": call_perplexity,
    "muse": call_muse,
}


def director_available(name):
    return bool(os.environ.get(DIRECTORS[name]["env"]))


def roster_status():
    rows = []
    for name, cfg in DIRECTORS.items():
        key = os.environ.get(cfg["env"])
        rows.append(
            {
                "name": name,
                "title": cfg["title"],
                "model": cfg["model"],
                "credential": cfg["env"],
                "online": bool(key),
                "best_at": cfg["best_at"],
            }
        )
    return rows


# --------------------------------------------------------------------------
# deliberation
# --------------------------------------------------------------------------


def parse_response(text):
    """Parse the OUTPUT_CONTRACT block into fields. Tolerant of formatting drift."""
    fields = {"verdict": "", "confidence": "", "key_points": [], "risk": "", "recommendation": "", "dissent": ""}
    if not text:
        return fields
    current = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        upper = line.upper()
        if upper.startswith("VERDICT:"):
            fields["verdict"] = line.split(":", 1)[1].strip()
            current = None
        elif upper.startswith("CONFIDENCE:"):
            fields["confidence"] = line.split(":", 1)[1].strip().lower()
            current = None
        elif upper.startswith("KEY_POINTS:"):
            current = "key_points"
        elif upper.startswith("BIGGEST_RISK:"):
            fields["risk"] = line.split(":", 1)[1].strip()
            current = None
        elif upper.startswith("RECOMMENDATION:"):
            fields["recommendation"] = line.split(":", 1)[1].strip()
            current = None
        elif upper.startswith("DISSENT:"):
            fields["dissent"] = line.split(":", 1)[1].strip()
            current = None
        elif current == "key_points" and line.startswith(("-", "*", "•")):
            fields["key_points"].append(re.sub(r"^[-*•]\s*", "", line))
    if not fields["verdict"]:
        # fall back: first non-empty line
        for raw in text.splitlines():
            if raw.strip():
                fields["verdict"] = raw.strip()[:300]
                break
    return fields


def ask_director(name, system, user):
    cfg = DIRECTORS[name]
    key = os.environ.get(cfg["env"])
    if not key:
        raise DirectorError(f"missing {cfg['env']}")
    started = time.time()
    text = CALLERS[name](system, user, key)
    elapsed = round(time.time() - started, 1)
    return {"director": name, "text": text.strip(), "parsed": parse_response(text), "seconds": elapsed}


def build_user_prompt(brief, context=None, peer_takes=None):
    parts = [f"COUNCIL BRIEF\n{brief.strip()}"]
    if context:
        parts.append(f"\nADDITIONAL CONTEXT\n{context.strip()}")
    if peer_takes:
        parts.append("\nPEER DIRECTOR POSITIONS (critique round — engage directly, don't repeat yourself)")
        for take in peer_takes:
            v = take["parsed"].get("verdict") or take["text"][:400]
            parts.append(f"\n[{take['director'].upper()}]: {v}")
            for point in take["parsed"].get("key_points", [])[:3]:
                parts.append(f"  - {point}")
        parts.append(
            "\nIn this round: state where you AGREE, where you DISAGREE, and what the council "
            "is collectively missing. Put your sharpest disagreement in DISSENT."
        )
    parts.append(OUTPUT_CONTRACT)
    return "\n".join(parts)


def convene(brief, mode="quorum", context=None, critique=False, verbose=True):
    if mode == "full":
        names = [n for n in DIRECTORS if director_available(n)]
    elif mode == "duo":
        names = [n for n in ("claude", "grok") if director_available(n)]
    else:  # quorum — the strategic core
        names = [n for n in ("claude", "grok") if director_available(n)]
        for extra in ("perplexity", "muse"):
            if director_available(extra):
                names.append(extra)
                break

    if not names:
        raise DirectorError("no directors available — no credentials found")

    if verbose:
        print(f"Convening council [{mode}] — {len(names)} director(s): {', '.join(names)}")

    results = []
    with cf.ThreadPoolExecutor(max_workers=len(names)) as pool:
        futures = {
            pool.submit(
                ask_director,
                n,
                ROLE_PREFIX + DIRECTORS[n]["lens"],
                build_user_prompt(brief, context),
            ): n
            for n in names
        }
        for fut in cf.as_completed(futures):
            name = futures[fut]
            try:
                res = fut.result()
                results.append(res)
                if verbose:
                    print(f"  [ok]   {name:11} {res['seconds']:>6}s  {res['parsed']['verdict'][:80]}")
            except DirectorError as exc:
                if verbose:
                    print(f"  [fail] {name:11} {exc}")
                results.append({"director": name, "text": "", "parsed": parse_response(""), "error": str(exc), "seconds": 0})

    results.sort(key=lambda r: names.index(r["director"]))
    live = [r for r in results if not r.get("error")]
    if not live:
        raise DirectorError("every director failed — check credentials")

    critique_round = []
    if critique and len(live) >= 2:
        if verbose:
            print("Critique round — directors respond to each other...")
        with cf.ThreadPoolExecutor(max_workers=len(live)) as pool:
            futures = {
                pool.submit(
                    ask_director,
                    r["director"],
                    ROLE_PREFIX + DIRECTORS[r["director"]]["lens"],
                    build_user_prompt(brief, context, peer_takes=live),
                ): r["director"]
                for r in live
            }
            for fut in cf.as_completed(futures):
                name = futures[fut]
                try:
                    res = fut.result()
                    critique_round.append(res)
                    if verbose:
                        print(f"  [ok]   {name:11} critique  {res['parsed']['dissent'][:70]}")
                except DirectorError as exc:
                    if verbose:
                        print(f"  [fail] {name:11} critique {exc}")
        critique_round.sort(key=lambda r: names.index(r["director"]))

    return {
        "brief": brief,
        "mode": mode,
        "context": context,
        "rounds": {"primary": results, "critique": critique_round},
        "live_directors": [r["director"] for r in live],
        "offline_directors": [r["director"] for r in results if r.get("error")],
        "convened_at": datetime.now(timezone.utc).isoformat(),
    }


# --------------------------------------------------------------------------
# synthesis
# --------------------------------------------------------------------------


def synthesize(session):
    """Hub synthesis: consensus, dissent, and the recommended call."""
    live = session["rounds"]["primary"]
    lines = []
    for r in live:
        p = r["parsed"]
        lines.append(f"[{r['director'].upper()} — {DIRECTORS[r['director']]['title']}]")
        lines.append(f"Verdict: {p['verdict']}")
        lines.append(f"Confidence: {p['confidence'] or 'n/a'}")
        for point in p["key_points"]:
            lines.append(f"  - {point}")
        if p["risk"]:
            lines.append(f"Biggest risk: {p['risk']}")
        if p["recommendation"]:
            lines.append(f"First action: {p['recommendation']}")
        if p["dissent"] and p["dissent"].lower() not in ("none", "n/a", ""):
            lines.append(f"Dissent: {p['dissent']}")
        lines.append("")

    if session["rounds"]["critique"]:
        lines.append("CRITIQUE ROUND")
        for r in session["rounds"]["critique"]:
            p = r["parsed"]
            lines.append(f"[{r['director'].upper()}] {p['verdict']}")
            if p["dissent"]:
                lines.append(f"  Disagreement: {p['dissent']}")
        lines.append("")

    system = (
        "You are the Hub — Lord Judah's chief of staff and council chair. Synthesize the "
        "directors' positions into a decision memo for Lord Judah. Rules: state the consensus "
        "plainly; PRESERVE DISSENT explicitly rather than averaging it away; name the single "
        "recommended path with its cost; end with the one decision he must make. Be concise, "
        "strategic, and free of filler. No preamble."
    )
    user = (
        "COUNCIL BRIEF\n"
        + session["brief"]
        + "\n\nDIRECTOR POSITIONS\n"
        + "\n".join(lines)
        + "\n\nWrite the synthesis memo with these sections exactly:\n"
        "CONSENSUS:\nRECOMMENDED PATH:\nCOST OF THIS PATH:\nDISSENT TO CARRY:\nDECISION NEEDED FROM LORD JUDAH:\n"
    )

    key = os.environ.get(DIRECTORS["claude"]["env"])
    if key:
        try:
            return call_claude(system, user, key).strip()
        except DirectorError:
            pass
    return "\n".join(lines)


# --------------------------------------------------------------------------
# logging
# --------------------------------------------------------------------------


def slug(text, limit=48):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:limit] or "brief"


def write_log(session, memo):
    os.makedirs(LOG_DIR, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    base = f"{stamp}-{slug(session['brief'])}"
    md_path = os.path.join(LOG_DIR, base + ".md")
    json_path = os.path.join(LOG_DIR, base + ".json")

    lines = [
        f"# Council Session — {stamp}Z",
        "",
        f"**Mode:** {session['mode']}  ",
        f"**Directors live:** {', '.join(session['live_directors'])}  ",
    ]
    if session["offline_directors"]:
        lines.append(f"**Directors offline:** {', '.join(session['offline_directors'])}  ")
    lines += ["", "## Brief", "", session["brief"], ""]
    if session.get("context"):
        lines += ["## Context", "", session["context"], ""]

    lines += ["## Director Positions", ""]
    for r in session["rounds"]["primary"]:
        if r.get("error"):
            lines += [f"### {r['director'].upper()} — OFFLINE", "", f"`{r['error']}`", ""]
            continue
        p = r["parsed"]
        lines += [
            f"### {r['director'].upper()} — {DIRECTORS[r['director']]['title']}",
            "",
            f"**Verdict:** {p['verdict']}",
            "",
            f"**Confidence:** {p['confidence'] or 'n/a'}",
            "",
        ]
        if p["key_points"]:
            lines += ["**Key points:**", ""]
            lines += [f"- {x}" for x in p["key_points"]] + [""]
        if p["risk"]:
            lines += [f"**Biggest risk:** {p['risk']}", ""]
        if p["recommendation"]:
            lines += [f"**First action:** {p['recommendation']}", ""]
        if p["dissent"]:
            lines += [f"**Dissent:** {p['dissent']}", ""]

    if session["rounds"]["critique"]:
        lines += ["## Critique Round", ""]
        for r in session["rounds"]["critique"]:
            p = r["parsed"]
            lines += [f"### {r['director'].upper()}", "", p["verdict"], ""]
            if p["dissent"]:
                lines += [f"**Disagreement:** {p['dissent']}", ""]

    lines += ["## Hub Synthesis", "", memo, ""]

    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump({"session": session, "synthesis": memo}, fh, indent=2, ensure_ascii=False)
    return md_path, json_path


# --------------------------------------------------------------------------
# cli
# --------------------------------------------------------------------------


def cmd_roster(args):
    print(f"{'DIRECTOR':<12} {'STATUS':<8} {'MODEL':<28} DOMAIN")
    print("-" * 96)
    for row in roster_status():
        status = "ONLINE" if row["online"] else "OFFLINE"
        print(f"{row['name']:<12} {status:<8} {row['model']:<28} {row['best_at']}")
        if not row["online"]:
            print(f"{'':<12} {'':<8} set {row['credential']} to bring this director online")
    return 0


def cmd_test(args):
    print("Probing each director with a one-line ping...\n")
    brief = "Reply with your role title and one sentence on what you uniquely bring to this council."
    session = convene(brief, mode="full", verbose=True)
    print(f"\nlive: {session['live_directors']}")
    if session["offline_directors"]:
        print(f"offline: {session['offline_directors']}")
    return 0 if session["live_directors"] else 3


def cmd_convene(args):
    context = None
    if args.context:
        if not os.path.isfile(args.context):
            print(f"error: context file not found: {args.context}", file=sys.stderr)
            return 1
        with open(args.context, encoding="utf-8") as fh:
            context = fh.read()
    try:
        session = convene(args.brief, mode=args.mode, context=context, critique=args.critique)
    except DirectorError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 3
    print("\nSynthesizing...\n")
    memo = synthesize(session)
    md_path, json_path = write_log(session, memo)
    print("=" * 78)
    print(memo)
    print("=" * 78)
    print(f"\nlogged: {md_path}")
    print(f"        {json_path}")
    return 0


def cmd_log(args):
    if not os.path.isdir(LOG_DIR):
        print("no sessions logged yet")
        return 0
    files = sorted(
        (f for f in os.listdir(LOG_DIR) if f.endswith(".md")), reverse=True
    )[: args.limit]
    if not files:
        print("no sessions logged yet")
        return 0
    for name in files:
        path = os.path.join(LOG_DIR, name)
        with open(path, encoding="utf-8") as fh:
            head = [l for l in fh.read().splitlines() if l.strip()][:6]
        print(f"\n{name}")
        for line in head:
            print(f"    {line}")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(prog="council.py", description="Lord Judah Agent Council")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("roster", help="show director status")
    p.set_defaults(func=cmd_roster)

    p = sub.add_parser("convene", help="convene the council on a brief")
    p.add_argument("brief")
    p.add_argument("--mode", choices=["quorum", "full", "duo"], default="quorum")
    p.add_argument("--context", help="path to a context file")
    p.add_argument("--critique", action="store_true", help="add a cross-critique round")
    p.set_defaults(func=cmd_convene)

    p = sub.add_parser("log", help="list past sessions")
    p.add_argument("--limit", type=int, default=10)
    p.set_defaults(func=cmd_log)

    p = sub.add_parser("test", help="ping every director")
    p.set_defaults(func=cmd_test)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
