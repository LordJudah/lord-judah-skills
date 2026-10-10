---
name: mailchimp-signup-repair
description: "Repair and validate Mailchimp-connected website signup flows, then configure the related welcome automation. Use for: broken newsletter or lead-magnet forms, missing audience sync, Mailchimp API credential wiring, signup success-state verification, welcome email setup, audience tags, and browser-guided Mailchimp fixes."
---

# Mailchimp Signup Repair

Use this skill when a website form should send contacts into Mailchimp, but the sync is broken, unreliable, incomplete, or missing a post-signup welcome journey. This skill covers both the engineering side of the repair and the Mailchimp-side finishing pass.

## Workflow decision tree

Start by classifying the request.

| Request shape | What to do |
|---|---|
| The website form is broken or not reaching Mailchimp | Follow the **Website-to-Mailchimp repair workflow** first. |
| Contacts are reaching Mailchimp but no follow-up email is sent | Jump to **Welcome automation workflow** after confirming audience sync. |
| The user wants proof that everything works end to end | Follow the **Live validation workflow** after the repair. |
| The user wants reusable campaign structure, tags, or welcome copy | Read `references/welcome-flow-reference.md` before editing Mailchimp content. |

If the user needs access troubleshooting inside Mailchimp or another platform, expect to use a browser handoff. When login, device verification, or protected account actions block progress, open the correct page first and then ask the user to take over from there.

## Core workflow

Mailchimp signup repair usually involves these phases:

1. Audit the website form, backend procedure, database storage, and environment-variable wiring.
2. Identify whether the failure is local form logic, backend API logic, missing credentials, invalid audience configuration, or Mailchimp-side automation/content.
3. Repair the website-to-Mailchimp sync path.
4. Validate the repair with tests, logs, a real browser submission, and a direct Mailchimp membership check.
5. Configure or repair the Mailchimp welcome journey, tags, and first email.
6. Document the final operating state and any remaining manual marketing tasks.

## Website-to-Mailchimp repair workflow

Inspect the website before editing anything. Read the public form component, the server-side handler or router, the database helper, the schema, and the environment mapping. Look for the actual capture flow rather than assuming Mailchimp is the only issue.

Use this checklist while auditing:

| Layer | What to verify |
|---|---|
| Frontend form | Inputs, validation, loading state, success state, error state, and honest user messaging |
| Backend handler | Lead creation, duplicate handling, Mailchimp request, and returned status payload |
| Database | Local lead capture still works even when Mailchimp fails |
| Environment | Mailchimp API key and audience ID are exposed server-side, never client-side |
| Tests | Existing signup tests cover both local storage and Mailchimp sync outcomes |

When implementing the fix, preserve local lead capture as the safe fallback. The best pattern is to store the lead locally first, then attempt Mailchimp sync, then return a structured sync result to the frontend.

Do not expose Mailchimp credentials in frontend code. Keep all Mailchimp requests on the server.

## Mailchimp API repair guidance

Use Mailchimp audience upsert logic rather than brittle one-off subscribe flows. Normalize the email, compute the subscriber hash exactly as Mailchimp expects, and upsert the contact into the configured audience. Return a machine-readable sync status so the UI and tests can distinguish between:

| Sync state | Meaning |
|---|---|
| `synced` | Mailchimp accepted the contact and the audience now contains the member |
| `skipped` | Mailchimp was intentionally bypassed, usually because credentials are missing in a non-production context |
| `failed` | Local capture succeeded, but Mailchimp rejected or failed the sync |

If Mailchimp rejects a clearly fake or placeholder address, treat that as a validation outcome, not automatically as a credential failure.

## Live validation workflow

After code changes, validate in four layers and do not stop at the first green signal.

1. Run the relevant automated tests.
2. Submit the real browser form through the live site or preview.
3. Inspect server and network logs for the actual signup response payload.
4. Verify directly in Mailchimp that the contact exists in the intended audience with the expected status.

Use a real deliverable email address for the final live check. Placeholder `example.com` addresses can cause Mailchimp to reject the contact even when the integration is functioning correctly.

Record the exact outcome, including the returned payload, Mailchimp audience status, and whether the browser showed the intended success message.

## Welcome automation workflow

Only configure the welcome journey after audience sync is proven to work. Otherwise, Mailchimp-side edits can distract from a backend problem.

Inside Mailchimp, inspect the audience’s current automations first. Existing journeys often already exist but are paused, misconfigured, or pointed at the wrong content asset.

Check for these common failure modes:

| Failure mode | Response |
|---|---|
| Existing welcome journey is disabled | Repair the journey and reactivate it instead of creating duplicates unnecessarily |
| Journey has errors | Inspect each step and resolve the broken action or content asset |
| Email editor opens an unexpected HTML/code builder | Inspect what content is actually stored there before replacing it |
| Signups enter the audience but receive nothing | Confirm that the journey is active and that the send-email step is valid |

The clean baseline sequence is simple: signup trigger, source tag, then immediate welcome email. Add more complexity only after the first email is stable.

## Tagging workflow

Keep tags minimal and legible. Prefer a structured naming system over improvised labels.

Read `references/welcome-flow-reference.md` before choosing final tags. By default, organize tags across three concepts: source, offer, and campaign. If only one tag can be added immediately, prioritize the source tag so future reporting remains possible.

## Welcome copy workflow

Treat the first email as orientation plus delivery, not as a full nurture sequence. The first message should confirm that the subscriber is in the right place, deliver the promised next step, and move them toward the primary campaign destination.

Before editing the email, read `references/welcome-flow-reference.md` for reusable subject-line, preview-text, CTA, and message-architecture patterns.

If Mailchimp opens a code-based or HTML-paste editor instead of a drag-and-drop composer, inspect the current asset carefully. It may contain broken embed code or a mistaken import from an earlier campaign setup. Replace it with actual welcome-email content and then verify the preview inside the journey.

## Browser handoff rules

Use the browser to inspect Mailchimp directly when account state, journey status, or email content must be verified. If login, password entry, device approval, CAPTCHA, or other protected steps appear, stop and hand the page to the user after opening the exact screen that needs action.

When the user returns control, resume from the current page and verify what changed before taking the next destructive action.

## Deliverables

A complete run should usually leave behind three artifacts:

| Deliverable | Purpose |
|---|---|
| Repair notes | What was broken, what changed, and what still depends on the user |
| Validation notes | Evidence that browser submission and Mailchimp audience sync both worked |
| Welcome-flow package | Tagging plan, subject line, preview text, CTA structure, and first-email body |

## Reference files

Read `references/welcome-flow-reference.md` when the user needs concrete tagging schemes, example welcome-email structure, validation checklists, or a model for documenting final Mailchimp state.
