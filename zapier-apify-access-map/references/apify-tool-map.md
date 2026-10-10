# Apify MCP - Tool Map (verified snapshot)

Snapshot date: **5 October 2026** - 12 tools exposed. Re-verify with `bash scripts/mcp_inventory.sh tools apify`.

| Tool | Purpose | Notes |
|---|---|---|
| `search-actors` | Find Actors in Apify Store | input key is `keywords` (not `search`); empty string = Store popularity order; avoid ranking words like top/best and bare words like scraper |
| `fetch-actor-details` | Get an Actor input schema - call BEFORE call-actor | Returns the authoritative input schema - never guess Actor inputs |
| `call-actor` | Run an Actor; requires BOTH `actor` and `input` | Omitting either `actor` or `input` fails validation; for MCP-server Actors use actorName:toolName |
| `get-actor-run` | Poll a run status |  |
| `get-dataset-items` | Read scraped results |  |
| `get-key-value-store-record` | Read a run stored record/output |  |
| `abort-actor-run` | Stop a running Actor |  |
| `search-apify-docs` | Search Apify platform docs |  |
| `fetch-apify-docs` | Fetch a specific doc page |  |
| `report-problem` | Send feedback to Apify |  |
| `apify--rag-web-browser` | Google search plus page extraction (markdown/text/html) | Prefer over generic fetching for search-grounded extraction |
| `apify--web-fetch` | Fetch and extract a single web page | Single-page extraction |

## Operating rules

1. Always `fetch-actor-details` before `call-actor` - Actor inputs are schema-validated.
2. `call-actor` needs `actor` AND `input`; `waitSecs` is an integer 0-45 (default 30).
3. Prefer the dedicated `apify--*` tools over generic `call-actor` when they fit.
4. Billing is per-run/per-result - set `maxItems` / `maxTotalChargeUsd` in `callOptions` for pay-per-event Actors.
5. Apify auth reports `unknown` until the first tool call; a successful `search-actors` call is the real proof of a working token.
