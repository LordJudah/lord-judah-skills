---
name: youtube-pro-primary
description: Designates the YouTube Pro connector as the primary tool for all YouTube, channel, and video-related tasks for Lord Judah. MUST read whenever the user asks to look up YouTube videos, channel stats, comments, or any YouTube data.
---

# YouTube Pro Primary Tool Protocol

This skill establishes the protocol for handling YouTube-related tasks for Lord Judah.

## Core Directive

Whenever Lord Judah requests information about his YouTube channel, video performance, comments, or any other YouTube-related data, **you MUST use the "Youtube Pro" connector** (via the `manus-mcp-cli` tool or direct API access if configured). 

Do NOT ask the user which tool to use. Assume YouTube Pro is the default and proceed directly to execution.

## Execution Workflow

1. **Verify Connector Availability:**
   If you need to verify the connector name or UID, run:
   ```bash
   manus-config config load --search youtube
   ```

2. **Access YouTube Data:**
   Use the available YouTube Pro MCP tools or direct API scripts (via `YOUTUBE_API_KEY` if present) to fetch the requested data.

3. **Target Channels:**
   When searching for Lord Judah's channel, default to looking for the main channel ID (`UCdfDe6MeFh2yj9u0KH-NMcA`) or searching "Lord Judah" as a channel type.

## Why This Skill Exists

Lord Judah has explicitly requested that the system remember "Youtube Pro" is his primary tool for all video-related tasks to streamline future requests and avoid unnecessary clarification questions.
