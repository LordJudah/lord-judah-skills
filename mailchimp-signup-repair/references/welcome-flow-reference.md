# Mailchimp Signup Repair Reference

## When to read this file

Read this file when you need concrete patterns for welcome-flow content, tag naming, live validation, or Mailchimp-specific troubleshooting after the core workflow in `SKILL.md` has already been loaded.

## Table of contents

1. Reusable tag structure
2. Welcome email architecture
3. Welcome email body pattern
4. Live validation checklist
5. Common troubleshooting patterns
6. Example notes structure

## Reusable tag structure

Use a small tag system that remains understandable months later.

| Tag dimension | Pattern | Example | Use |
|---|---|---|---|
| Source | `source:<entrypoint>` | `source:neurochemical-cypher-site` | Identifies where the contact entered |
| Offer | `offer:<lead-magnet-or-promise>` | `offer:workbook` | Identifies what the subscriber requested |
| Campaign | `campaign:<campaign-slug>` | `campaign:proof-in-our-feeds` | Identifies the launch or initiative |

When the project is early and only one tag can be implemented immediately, add the source tag first.

## Welcome email architecture

Use the first welcome email to orient the subscriber, deliver the promised next step, and route them into the core experience.

| Element | Guidance |
|---|---|
| Internal email name | Use a descriptive operational title such as `Project Name — Welcome + Delivery` |
| Subject line | Confirm arrival and value, not just hype |
| Preview text | Clarify what happens next in one sentence |
| Primary CTA | Route to the main campaign hub, download page, or first required step |
| Secondary CTA | Route to the strongest piece of supporting content |
| Closing | Use the creator, brand, or organization signature that matches the audience expectation |

## Welcome email body pattern

Use this structure when drafting or rewriting the first email:

1. Welcome the subscriber and confirm what they joined.
2. Explain the mission or frame in plain language.
3. Deliver the next step with a clear CTA.
4. Offer one supporting route into deeper content.
5. Close with a human signature.

A reusable body pattern is:

> Welcome to **[Project Name]**.
>
> You just joined a project exploring **[problem/theme]** and helping people move toward **[desired transformation]**.
>
> Your best first step is here:
>
> **[Primary CTA label]:** [Primary URL]
>
> If you want to go deeper right away, start here:
>
> **[Secondary CTA label]:** [Secondary URL]
>
> Over this journey, you’ll explore **[three-part promise or thematic arc]**.
>
> Stay tuned,
>
> **[Name / Brand / Organization]**

## Live validation checklist

Use this exact sequence when proving the repair is real:

| Step | Validation target |
|---|---|
| 1 | Automated tests pass for signup flow and Mailchimp helper behavior |
| 2 | Browser submission completes through the public form |
| 3 | Network or server logs show a successful signup payload |
| 4 | Direct Mailchimp lookup confirms the contact exists in the intended audience |
| 5 | Mailchimp journey is active and the welcome step is ready to send |

If the browser spinner hangs or the success state looks wrong, inspect the logs before assuming the sync failed. Sometimes the backend succeeds while the frontend state handling remains incomplete.

## Common troubleshooting patterns

### Mailchimp accepts the contact, but no email is sent

Confirm that the contact entered the correct audience, that the journey is active, and that the send-email step is valid rather than paused or broken.

### Mailchimp rejects the signup during testing

Check whether the test email is fake, disposable, or clearly non-deliverable. A placeholder address can trigger a 400 even when credentials and audience wiring are correct.

### Existing welcome journey opens in a strange HTML editor

Inspect the current content asset before replacing it. It may contain embed code or another incorrect artifact from a past setup. Replace the content with a real welcome message and verify the preview card in the journey afterward.

### There are duplicate welcome journeys

Inspect both before deleting or ignoring either one. Often one is historical and broken while another is recent but paused. Choose the flow that best matches the active audience and repair that one deliberately.

## Example notes structure

When documenting final state, structure notes like this:

| Section | What to capture |
|---|---|
| Current account state | Whether the platform session is active and which audience is in scope |
| Repair findings | What was broken in website sync or automation content |
| Current journey state | Trigger, tags, email step, active/paused status |
| Validation evidence | Browser payload, log response, audience membership confirmation |
| Remaining manual tasks | Optional future segmentation, sequence expansion, or branding refinements |

## Example campaign pattern

The Neurochemical Cypher workflow used this structure:

| Component | Example |
|---|---|
| Source tag | `source:neurochemical-cypher-site` |
| Offer tag | `offer:workbook` |
| Campaign tag | `campaign:proof-in-our-feeds` |
| Welcome subject | `Your Neurochemical Cypher workbook is here` |
| Preview text | `Start the 4-week reset for feeds, nervous systems, and real belonging.` |

Use this pattern as a model, then adapt the naming and copy to the project at hand.
