#!/usr/bin/env bash
# Inspect Manus MCP connectors (Zapier, Apify, ...) through the local sandbox bridge.
#
# WHY THIS EXISTS: the MCP tool layer and `manus-mcp-cli` both use short internal
# deadlines. Large servers (Zapier) can exceed them, producing
# "deadline_exceeded" or "executor action timed out". This script talks to the
# same bridge directly with a multi-minute timeout.
#
# The bridge is the sandbox runtime on 127.0.0.1:8350 (service mcp.v1.MCPService).
# Prefer the `mcp` tool for normal tool calls; use this script for enumeration
# and for timeouts.
#
# Usage:
#   mcp_inventory.sh status <server>          # OAuth/auth status
#   mcp_inventory.sh tools  <server>          # full tool list -> stdout + /tmp/<server>_tools.json
#   mcp_inventory.sh raw    <server> <Method> [json]   # any bridge RPC
#
# Example:
#   bash mcp_inventory.sh tools zapier
#   bash mcp_inventory.sh status apify

set -uo pipefail
BRIDGE="http://localhost:8350/mcp.v1.MCPService"
ACTION="${1:-}"
SERVER="${2:-}"

if [[ -z "$ACTION" || -z "$SERVER" ]]; then
  sed -n '2,22p' "$0"
  exit 1
fi

case "$ACTION" in
  status)
    curl -s -m 30 -X POST "$BRIDGE/AuthStatus" \
      -H 'Content-Type: application/json' \
      -d "{\"server_name\":\"$SERVER\"}"
    echo
    ;;
  tools)
    OUT="/tmp/${SERVER}_tools.json"
    CODE=$(curl -s -m 600 -X POST "$BRIDGE/ListTools" \
      -H 'Content-Type: application/json' \
      -d "{\"server_name\":\"$SERVER\"}" \
      -o "$OUT" -w '%{http_code}')
    echo "HTTP:$CODE FILE:$OUT"
    python3 - "$OUT" <<'PY'
import json, sys
d = json.load(open(sys.argv[1]))
if d.get('success') is not True:
    print("FAILED:", json.dumps(d)[:400]); sys.exit(1)
names = [t['name'] for t in d.get('tools', [])]
print("TOOL_COUNT:", len(names))
for i, n in enumerate(names, 1):
    print("{:3d}. {}".format(i, n))
PY
    ;;
  raw)
    METHOD="${3:-ListTools}"
    BODY="${4:-{\"server_name\":\"$SERVER\"}}"
    curl -s -m 600 -X POST "$BRIDGE/$METHOD" \
      -H 'Content-Type: application/json' -d "$BODY"
    echo
    ;;
  *)
    echo "Unknown action: $ACTION" >&2
    exit 1
    ;;
esac