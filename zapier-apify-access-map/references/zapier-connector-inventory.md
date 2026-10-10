# Zapier Connector - Live Inventory (verified snapshot)

Snapshot date: **5 October 2026**. Re-verify with `bash scripts/mcp_inventory.sh tools zapier` and a fresh `inspect_zapier_actions` call before quoting these numbers.

| Metric | Value |
|---|---|
| Apps enabled | 50 |
| App actions enabled | 608 |
| Connected accounts | 66 |
| MCP interface tools | 42 |

## Apps by action depth

| App | Actions | Connected accounts |
|---|---:|---:|
| Slack | 40 | 2 |
| HeyGen | 39 | 3 |
| Google Sheets | 37 | 1 |
| Shopify | 37 | 1 |
| Textmagic | 35 | 1 |
| Notion | 31 | 1 |
| ChatGPT (OpenAI) | 27 | 1 |
| Google Drive | 25 | 5 |
| Microsoft Excel | 23 | 1 |
| Gmail | 22 | 3 |
| Google Calendar | 22 | 1 |
| Spotify | 22 | 1 |
| Airtable | 21 | 1 |
| Mailchimp | 20 | 1 |
| Google Docs | 19 | 4 |
| Canva | 13 | 1 |
| Manychat | 13 | 1 |
| YouTube | 12 | 1 |
| Twilio | 11 | 1 |
| Facebook Pages | 10 | 2 |
| Google AI Studio (Gemini) | 9 | 1 |
| LinkedIn Ads | 9 | 2 |
| WordPress | 9 | 1 |
| Manus | 8 | 1 |
| Google Slides | 6 | 1 |
| Instagram for Business | 6 | 2 |
| Facebook Custom Audiences | 5 | 2 |
| Facebook Lead Ads (for Business admins) | 5 | 1 |
| Google Business Profile | 5 | 1 |
| Grok by xAI | 5 | 1 |
| Telegram | 5 | 1 |
| Zapier Manager | 5 | 0 |
| Facebook Conversions | 4 | 1 |
| Facebook Conversions (for Business admins) | 4 | 1 |
| Google Forms | 4 | 1 |
| Hume AI | 4 | 1 |
| LinkedIn | 4 | 1 |
| MCP Client by Zapier | 4 | 1 |
| Twitch | 4 | 1 |
| Webhooks by Zapier | 4 | 0 |
| Base44 | 3 | 1 |
| ElevenLabs | 3 | 2 |
| Email Parser by Zapier | 2 | 1 |
| Facebook Messenger | 2 | 2 |
| Gravity Forms | 2 | 1 |
| HTML/CSS to Image | 2 | 1 |
| PDF Maker - Automate Documents | 2 | 1 |
| Perplexity | 2 | 1 |
| LinkedIn Conversions | 1 | 1 |
| TikTok Conversions | 1 | 1 |

## Sums to watch

- Deepest surfaces (best candidates for multi-step automation): Slack(40), HeyGen(39), Google Sheets(37), Shopify(37), Textmagic(35), Notion(31), ChatGPT (OpenAI)(27), Google Drive(25)
- Thin surfaces (1-2 actions; enable more in Zapier before promising a workflow): LinkedIn Conversions(1), TikTok Conversions(1), Email Parser by Zapier(2), HTML/CSS to Image(2), Perplexity(2), Facebook Messenger(2), PDF Maker - Automate Documents(2), Gravity Forms(2)
- Zero-connection apps (enabled but unattached): Zapier Manager, Webhooks by Zapier

## The 42 interface tools

```
discover_zapier_actions
enable_zapier_action
disable_zapier_action
inspect_zapier_actions
execute_zapier_read_action
execute_zapier_write_action
list_zapier_connections
manage_zapier_connections
send_feedback
auto_provision_mcp
list_zapier_skills
get_zapier_skill
create_zapier_skill
update_zapier_skill
delete_zapier_skill
write_code_action
create_workflow
import_zap_to_workflow
update_workflow
delete_workflow
enable_workflow
disable_workflow
run_workflow
list_workflows
get_workflow
list_workflow_runs
check_workflow_run
get_run_output
list_workflow_versions
get_workflow_version
list_workflow_drafts
get_workflow_draft
create_workflow_draft
update_workflow_draft
run_workflow_draft
discard_workflow_draft
publish_workflow_draft
search_triggers
get_trigger_fields
get_trigger_field_choices
get_trigger_run
get_configuration_url
```
