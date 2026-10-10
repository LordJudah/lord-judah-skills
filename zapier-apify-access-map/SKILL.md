---
name: zapier-apify-access-map
description: Verified access map for the Lord Judah Manus MCP connectors — Zapier (50 apps, 608 app actions, 42 interface tools, 66 connections) and Apify (12 tools). Use when auditing or counting connector apps/tools, deciding whether Zapier or Apify can reach a given service, diagnosing Zapier OAuth failures ("requires login", "Invalid authorization request", stale token), or enumerating a large MCP server that times out. Covers routing rules, auth recovery, and the timeout workaround.
---

# Zapier & Apify Access Map

Verified connector intelligence for this account. Numbers here are **snapshots**; re-verify before quoting them to the user.

## Connector registry

| Connector | UID | Enabled | MCP endpoint |
|---|---|---|---|
| Zapier | `433d2fe0-e56d-42b2-8625-9996eab0bb1d` | yes | `https://mcp.zapier.com/api/v1/connect` |
| Apify | (session connector) | yes | Apify-hosted MCP |

## Zapier — verified baseline (5 October 2026)

| Metric | Value |
|---|---|
| Apps enabled | **50** |
| App actions enabled | **608** |
| Connected accounts | **66** |
| Interface tools exposed to Manus | **42** |

Do not confuse the layers: the user sees "apps and actions" in the Zapier MCP dashboard; Manus sees 42 interface tools. **App actions are never exposed as individual tools.**

Full per-app table (actions + connections, deepest/thinnest surfaces): `references/zapier-connector-inventory.md`

### The 3-step execution pattern

1. `inspect_zapier_actions` — lists apps **already enabled** with their action counts and connection totals. This is the audit source of truth.
2. `discover_zapier_actions` — searches 9,000+ apps for actions **not yet enabled**; then `enable_zapier_action` to add them.
3. `execute_zapier_read_action` / `execute_zapier_write_action` — runs the action by key.

**Never display `selected_api` values to the user** — they are internal tool-call identifiers. Show only the app name.

### Auth failure playbook

Symptoms: the MCP server reports `requires login`, exposes zero tools, or `tool.list`/`tool.search` return only the login requirement.

Root cause seen in the runtime log: the stored token is rejected by Zapier with `no valid token available, authorization required` — a **stale/expired** credential, not a disabled connector.

Two traps that waste cycles:
- A pending authorization **expires 5 minutes** after the request is created (`authorization timeout after 5m0s`).
- **Every new login request invalidates the previous link.** Issuing a second login while the user is clicking the first produces `Invalid authorization request`.

Recovery sequence:
1. Issue **one** login request. Do not re-issue while the user is acting.
2. User clicks the **newest** card within 5 minutes and approves on Zapier.
3. Verify with `bash scripts/mcp_inventory.sh status zapier` — expect `"status":"authenticated"`. Do not enumerate until it does.
4. Fallback if no card renders: Manus **Settings → Connectors → Zapier → Reconnect**.
5. `AuthStatus` may report `hasToken:true` while `status` is `unauthenticated` — the token exists but is invalid. Status, not token presence, is the signal.

### Routing rule: Zapier vs Apify

- **Zapier** — authenticated app-to-app business operations: Shopify, Mailchimp, Google Sheets/Drive/Docs/Slides, Slack, Notion, Airtable, HeyGen, WordPress, Meta/Facebook surfaces, LinkedIn Ads, Twilio, Textmagic, Spotify, Microsoft Excel.
- **Apify** — public-data extraction and web research: social platform scraping (Instagram/TikTok/X), store and product scraping, Google Maps, and RAG-style web reading.
- When a task needs data **from the open web**, reach for Apify. When it needs **actions inside a logged-in business app**, reach for Zapier.

## Apify — verified baseline (5 October 2026)

**12 tools.** Full map with usage rules: `references/apify-tool-map.md`

Core loop: `search-actors` → `fetch-actor-details` (authoritative input schema) → `call-actor` → `get-actor-run` / `get-dataset-items`.

Hard requirements:
- `call-actor` needs **both** `actor` and `input`; omitting either fails validation.
- `search-actors` takes **`keywords`** (not `search`); empty string returns Store popularity order.
- MCP-server Actors are addressed as `actorName:toolName`.
- `waitSecs` is an integer 0–45 (default 30).
- Costs are per-run/per-result — set `maxItems` / `maxTotalChargeUsd` in `callOptions`.
- Auth status reads `unknown` until the first call; a successful `search-actors` returning real Actors proves the token works.

## Enumeration and timeout workaround

Prefer the `mcp` tool for ordinary tool calls and discovery. Use the bundled script when enumeration is the goal or when the MCP layer times out.

```bash
bash scripts/mcp_inventory.sh status zapier      # auth status
bash scripts/mcp_inventory.sh tools  zapier      # full tool list + count
bash scripts/mcp_inventory.sh tools  apify
bash scripts/mcp_inventory.sh raw    zapier AuthStatus '{"server_name":"zapier"}'
```

Why it is needed: the MCP tool layer and the MCP CLI share short internal deadlines. Large servers return `deadline_exceeded` / `executor action timed out`. The script calls the same bridge (`127.0.0.1:8350`, service `mcp.v1.MCPService`) with a 10-minute timeout.

Heavy tool results are captured to `/home/ubuntu/.mcp/tool-results/*.json` — read those files for full payloads instead of re-calling.

## Audit checklist

1. `AuthStatus` → `authenticated`? Fix auth first if not.
2. `inspect_zapier_actions` → compare app count and summed `action_count` against the last known baseline (50 apps / 608 actions).
3. Flag **zero-connection apps** (enabled but unattached) and **thin apps** (1–2 actions) before promising a workflow.
4. Apify: `tools apify` → expect 12.
5. Record any delta so the snapshot stays trustworthy.