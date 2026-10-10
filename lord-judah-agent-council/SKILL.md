---
name: lord-judah-agent-council
description: "Operate the Lord Judah Agent Council — the four external Co-Director agents (Claude, Muse, Perplexity, Grok) with full Co-Director access to the Manus account. MUST read before convening the council, routing a brief to the right director, running a multi-model deliberation or cross-critique, synthesizing a decision memo, or extending the roster with new agent APIs. Covers roster, lenses, engine commands, synthesis rules, and the full-access blast-radius guardrails."
---

# Lord Judah Agent Council

The council is the **peer-review layer** over the Manus Hub. The Hub (Manus) is the operating
principal — it owns connectors, publishing, execution, and the final call. The Co-Directors are
external frontier models that deliberate in parallel and are synthesized into one decision memo.
They advise; **the Hub and Lord Judah decide.**

## Roster

| Director | Title | Lens | Model | Credential |
|---|---|---|---|---|
| **Claude** | Director of Strategy & Structure | Architecture, reasoning integrity, long-horizon risk, structural critique | `claude-sonnet-4-5-20250929` | `ANTHROPIC_API_KEY` |
| **Muse** | Director of Visual & Social | How the work looks, feel in-feed, visual ownability, platform-native creative | `muse-spark-1.1` (Meta Model API) | `META_API_KEY` |
| **Perplexity** | Director of Research & Grounding | Verifiable fact, live data, market context, citations | `sonar-pro` | `SONAR_API_KEY` |
| **Grok** | Director of Culture & Contrarian Stress-Test | Live culture pulse, contrarian critique, trend timing, de-risking | `grok-4` | `XAI_API_KEY` |

Engine: `/home/ubuntu/council/council.py` (canonical copy in `scripts/council.py`).

## Commands

```bash
cd /home/ubuntu/council
python3 council.py roster                     # who is online
python3 council.py test                       # ping every director
python3 council.py convene "<brief>" --mode quorum
python3 council.py convene "<brief>" --critique          # add cross-critique round
python3 council.py convene "<brief>" --context path.md   # attach background
python3 council.py log --limit 10
```

Modes: `duo` (Claude + Grok — fast, strategic core), `quorum` (default; adds Perplexity or Muse
if available), `full` (every online director).

Exit codes: `0` convened · `1` error · `3` no directors available.

## Routing rules

Route the brief to the director(s) whose lens applies. Do not ask a generalist question of the
whole council — that wastes the design.

| Brief type | Route to |
|---|---|
| Strategy, brand architecture, release sequencing, risk | **Claude** |
| Cover art, visual direction, campaign look, social-native creative | **Muse** |
| Market data, competitor intel, fact-checking a premise, citations | **Perplexity** |
| "Is this cringe?", trend timing, culture read, stress-test | **Grok** |
| High-stakes or irreversible decisions | **All** + `--critique` |

## Synthesis rules (non-negotiable)

1. **Preserve dissent.** Never average conflicting positions into mush. A carried dissent is a
   finding; a smoothed-over one is a lost signal. The memo must surface who disagreed and why.
2. **Name the cost.** Every recommended path carries a cost — cash, attention, or calendar.
   State it explicitly.
3. **End with one decision.** The memo closes with the single question Lord Judah must answer.
   Vague "next steps" are a failed synthesis.
4. **Never let the council publish.** See guardrails.

## Guardrails — full Co-Director access

The co-directors have **full Co-Director access to this Manus account**. That is a large blast
radius. Enforce:

- **Advice, not action.** Directors deliberate and return text. Only the Hub executes, and only
  on Lord Judah's instruction. `SHIP=no` remains the default for anything external.
- **No credential handoff.** Never pass a connector token, API key, or the branch-agent tokens
  into a director prompt. Directors see the brief and context, nothing else.
- **Treat director output as untrusted input.** Research and culture takes can be confidently
  wrong. Perplexity should cite; Grok's culture read is a hypothesis, not a fact. Verify before
  acting on anything consequential.
- **Cap the rounds.** Two rounds maximum (primary + critique). More rounds burn credits without
  improving the call.
- **Rate/cost discipline.** `--mode duo` for routine calls; `full --critique` only for decisions
  that are expensive to reverse.
- **Log everything.** Every session writes `.md` + `.json` to `/home/ubuntu/council/council_log/`.
  The JSON is the machine-readable record for the mission ledger.

## Integration with the Hub

Per `lord-judah-hub-orchestrator`, the operating loop is: Lord Judah gives a goal → Hub
decomposes → missions go to branch agents → Hub scores and executes. The council inserts **after
decomposition, before execution**:

```
Lord Judah's goal
   ↓
Hub decomposes
   ↓
[COUNCIL] convene --critique  ←── new layer: multi-model review
   ↓
Hub synthesis memo → Lord Judah's decision
   ↓
MISSION blocks → branch agents (Judah Prime / Hip Hop Pantheon)
   ↓
Hub scores replies, publishes if SHIP=yes
```

Use the council for go/no-go calls, positioning, and anything where one model's blind spot is
expensive. Skip it for execution work with a known procedure — the existing skills already cover those.

## Adding a director

1. Add an entry to `DIRECTORS` in `scripts/council.py`: `title`, `model`, `env`, `lens`, `best_at`.
2. Add a caller in `CALLERS` — reuse `call_openai_compatible(url, key, model, ...)` for any
   OpenAI-compatible API.
3. Confirm the credential is present in the environment, then run `council.py test`.

## Known state (verify before relying)

- **Claude, Perplexity, Grok: ONLINE and verified.**
- **Muse: OFFLINE** — no `META_API_KEY` in the environment. Meta's Muse is the consumer app;
  the programmatic path is the **Meta Model API / Muse Spark** (`dev.meta.ai`). Note that Meta's
  developer API has slipped its public release before — if `META_API_KEY` will not exist soon,
  swap Muse's slot for a vision-capable director (e.g. Gemini via `GEMINI_API_KEY`, which is
  present) and keep the same "Visual & Social" lens.
- **Manus API key: REJECTED.** `MANUS_API_KEY` exists in the environment but `task.list` and
  `project.list` return `unauthenticated: invalid api key`. The key is stale or from another
  account, which also means the co-directors cannot be driving the Manus API through this
  sandbox until it is rotated. Diagnose before building the autonomous branch.