---
name: make-scenario-health-manager
description: "Health-check, diagnose, repair, and validate Make.com scenarios. Use for: auditing scenario fleets, investigating failed runs, tracing broken modules or connections, repairing scenario blueprints, re-running scenarios through Make MCP toolboxes, and reporting scenario status after fixes."
---

# Make Scenario Health Manager

## Overview

Use this skill when a user wants a **Make.com** workspace reviewed for unhealthy scenarios, failed runs, broken connections, or misconfigured modules. Follow this workflow when the task includes both **diagnosis** and **repair**, especially when the environment may require a mix of browser access, Make MCP toolbox access, and authenticated in-page API calls.

Treat the process as a layered access strategy. Start with the least invasive path that exposes actionable information. Escalate only when the current path cannot reveal enough detail to diagnose or repair the scenario.

## Workflow

A Make.com health check usually has five stages:

1. Establish a workable access path.
2. Inventory scenarios and recent failures.
3. Isolate the failing module, connection, or required field.
4. Repair the scenario or unblock the dependency.
5. Validate the repair and summarize the outcome.

Do not report success until a fresh validation has been completed.

## Step 1: Establish Access

Determine which of these access paths is available, in this order:

| Access path | When to use | What it is good for | Main limits |
| --- | --- | --- | --- |
| Browser session in Make | Use first when the user can log in or is already logged in. | Viewing scenarios, logs, connections, and editor state. | Visual loading issues, dynamic UI, limited machine-readable data. |
| Make MCP toolbox | Use when the user provides a toolbox URL and agent key, or has exposed scenarios as on-demand tools. | Fast execution-based health checks across multiple scenarios. | Can run scenarios, but usually cannot edit their internal configuration. |
| Authenticated in-page AJAX from the browser console | Use when the browser is logged in but the visual editor is stuck or incomplete. | Reading scenario metadata, logs, and blueprints, and sometimes patching scenarios. | Depends on app state and current browser session. |
| Direct shell API calls | Use only if you have a valid supported API auth path. | Repeatable scripted access. | Raw cookie copying often fails; avoid assuming browser cookies will work in shell. |

If browser login is required, open the relevant Make page first and ask the user to take over the browser. After login, return to the scenario list immediately.

## Step 2: Inventory and Triage

Start at the scenarios list and build a complete inventory of the workspace or folder under review. Record each scenario name, active state, and visible warning state before drilling into repairs.

Then classify scenarios into three groups:

| Status group | Meaning | Action |
| --- | --- | --- |
| Healthy | No current error signs and recent successful runs. | Confirm and move on. |
| Blocked by shared dependency | Multiple scenarios fail at the same connection, provider, or quota boundary. | Fix the shared dependency before editing blueprints. |
| Scenario-specific failure | Only one workflow or one downstream module fails. | Inspect logs and blueprint details for that scenario. |

When several scenarios fail at the same module family, assume a shared root cause until proven otherwise.

## Step 3: Diagnose the Failure

Use recent run logs before editing anything. Identify the **latest failed execution**, the **exact module**, and the **error class or message**.

Follow this decision tree:

1. If the error is a provider quota, billing, or rate-limit issue such as OpenAI `429`, treat it as an external dependency problem first.
2. If the error is a connection verification or authorization failure, inspect the corresponding Make connection before editing scenario logic.
3. If the error is a validation failure such as `BundleValidationError`, inspect the module blueprint and required mapped fields.
4. If the visual editor is unusable, use the authenticated browser page's own AJAX client to query scenario details and blueprints.

For recurring Make browser problems, remember these patterns:

| Symptom | Likely meaning | Recommended move |
| --- | --- | --- |
| Scenario editor shows only a skeleton UI | The page is loaded enough for scripts but not reliable for visual editing. | Query the page runtime or use authenticated AJAX through the page. |
| `fetch()` returns CSRF errors | Raw fetch is missing the app's internal request handling. | Prefer the page's configured AJAX client instead of manual fetch. |
| Multiple scenarios fail at the same AI module | Shared provider account or budget issue. | Verify the shared connection and confirm billing or quota with the user. |
| A scenario starts working farther downstream after provider payment is restored | Root cause shifted from dependency outage to internal mapping or validation. | Inspect the first newly failing downstream module. |

If this skill is being used repeatedly, read `references/diagnosis-patterns.md` for the short-form diagnosis patterns and phrasing.

## Step 4: Use Make's In-Page AJAX Client When the UI Is Stuck

When the user is logged into Make and the browser page is open, prefer the page's own authenticated request stack rather than raw `fetch()`.

Use browser console execution to call the same scenario endpoints the Make app already uses. The most useful endpoints are:

| Endpoint | Purpose |
| --- | --- |
| `/api/v2/scenarios/{scenarioId}` | Scenario metadata and state. |
| `/api/v2/scenarios/{scenarioId}/logs` | Recent executions. |
| `/api/v2/scenarios/{scenarioId}/logs/{logId}` | A specific failed run. |
| `/api/v2/scenarios/{scenarioId}/blueprint` | Live scenario blueprint. |
| `/api/v2/scenarios/{scenarioId}/blueprint?draft=true` | Draft blueprint if present. |

Use the page's AJAX client with a pattern like this:

```javascript
(async () => {
  const data = await jQuery.ajax({
    url: '/api/v2/scenarios/123456/blueprint',
    method: 'GET'
  });
  return data;
})()
```

When patching a scenario, retrieve the live blueprint first, update only the minimal affected fields, and send the full blueprint back through a `PATCH` request to `/api/v2/scenarios/{scenarioId}`.

Use a pattern like this:

```javascript
(async () => {
  const current = await jQuery.ajax({
    url: '/api/v2/scenarios/123456/blueprint',
    method: 'GET'
  });

  const blueprint = current.response.blueprint;
  const moduleToFix = blueprint.flow.find(x => x.id === 4);
  moduleToFix.mapper.fields.title = '{{ifempty(1.summary; "Untitled Item")}}';

  const payload = { blueprint: JSON.stringify(blueprint) };

  return await jQuery.ajax({
    url: '/api/v2/scenarios/123456',
    method: 'PATCH',
    contentType: 'application/json',
    data: JSON.stringify(payload)
  });
})()
```

Apply only narrowly scoped edits. Do not rewrite unrelated modules, scheduling, or folder settings unless the task explicitly requires it.

## Step 5: Repair Strategy

Repair in this order:

| Repair tier | Examples | Priority |
| --- | --- | --- |
| Shared dependency repair | Restoring provider billing, reconnecting a shared credential, reactivating a disabled scenario after a quota issue. | First |
| Mapping repair | Adding fallback expressions, restoring a required title field, correcting a mapped property key, fixing a data source ID. | Second |
| Structural repair | Replacing a broken module, changing routing logic, updating scheduling, or rebuilding part of the blueprint. | Last |

Prefer resilient repairs over brittle ones. When a required field can occasionally be blank, add a safe fallback instead of relying on the upstream module to always supply data.

A proven example from this workflow was a Notion create-item module that failed validation because the required title field mapped directly to `{{1.summary}}`. Replacing that mapping with `{{ifempty(1.summary; "Untitled Event")}}` prevented future failures when the Google Calendar summary was empty.

## Step 6: Validate the Repair

Always validate with a fresh run or fresh logs.

Use this validation order:

1. Re-run the affected scenario through the Make MCP toolbox when available.
2. Check the newest scenario logs to confirm the latest execution ended with success status and no error object.
3. For scenarios previously blocked by a shared dependency, confirm that at least one formerly failing scenario now succeeds and then spot-check the others.
4. If a scenario runs longer than the immediate response window, inspect its newest logs instead of assuming failure.

Do not stop at “the patch saved successfully.” A saved blueprint is not a validated repair.

## Reporting Standard

Write a compact but information-rich report that includes the workspace scope, the scenarios checked, the root cause categories found, the exact fixes applied, and the validation result for each affected scenario.

Use a table like this in final reporting:

| Scenario | Root cause | Fix applied | Validation result |
| --- | --- | --- | --- |
| Scenario name | Shared quota issue, missing field, broken connection, etc. | Describe the exact action taken. | Successful re-run, successful latest log, still blocked, or needs user input. |

If a fix could not be completed because the user must restore billing, log in, or approve a risky change, say that explicitly and stop short of claiming resolution.

## Guardrails

Do not ask the user for sensitive tokens unless the current access path truly requires them.

Do not perform broad blueprint rewrites when a focused field-level edit is sufficient.

Do not trust browser visuals alone when logs or API responses can provide a stronger answer.

Do not conclude that a connection is broken merely because a scenario failed. Distinguish between **authorization failure**, **quota exhaustion**, and **downstream validation failure**.

Do not mark a scenario healthy without a fresh validation step.

## Bundled Reference

Read `references/diagnosis-patterns.md` when you need compact templates for classifying failures, deciding whether a problem is shared or scenario-specific, or phrasing the final audit summary.

## Deliverables

When the task is complete, deliver a concise final message and attach the main notes or report file if one was created during the workflow.
