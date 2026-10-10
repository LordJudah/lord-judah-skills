---
name: book-audiobook-launch-system
description: End-to-end digital book and audiobook launch workflow. Use when launching an e-book, audiobook, author guide, or educational publication through a three-tier Shopify offer; packaging customer downloads; testing digital fulfillment; creating an audiobook-excerpt social campaign; or building a ManyChat comment-to-DM sales funnel.
---

# Book and Audiobook Launch System

Use this workflow to turn a manuscript, audiobook, and cover into a tested storefront and an excerpt-led campaign. Treat publication, customer messaging, posting, and automation activation as approval-gated actions.

## Required Related Guidance

Read the following before the matching work:

| Work | Required Skill |
|---|---|
| External services, triggers, webhooks, or recurring follow-up | `automation-and-scheduling` |
| Connector inspection or configuration | `manus-config` |
| Social visuals or product gallery images | `imagegen` |
| Reel or video production | `video-generator`; use `html-video-production` for precise kinetic text |
| Shopify connector use | Inspect the live connector tool schemas before every unfamiliar operation |

## Workflow

Complete the phases in order. Do not publish the product before fulfillment tests pass. Do not activate ManyChat until live Shopify URLs resolve.

### 1. Inspect the Sources

Inventory the manuscript, cover, audiobook files, current product listings, store conventions, and intended audience. Run `scripts/audio_inventory.py` against the audiobook source folder. Preserve WAV or lossless masters; work from copies.

Create a source record containing the title, author, publisher, product promise, chapter/rule structure, file formats, track count, runtime, audience, and content-sensitivity notes.

### 2. Define the Three-Tier Offer

Default to the following architecture unless the user specifies another model:

| Tier | Contents | Role |
|---|---|---|
| E-Book | Customer-ready PDF or EPUB | Accessible entry point |
| Audiobook | Ordered MP3 tracks and delivery guide | Voice-led mobile experience |
| Premium Bundle | E-book plus audiobook | Best-value offer |

Calculate the bundle value from the separate prices. Confirm price, format, licensing, tax assumptions, and delivery method before creating the storefront.

### 3. Build Shopify as a Draft

Read `references/shopify-and-delivery.md`. Create one product with a `Format` option and three variants. Verify title, description, SEO, tags, media, price, SKU, and handle.

Set every digital variant to:

- `requiresShipping: false`
- inventory tracking off
- an inventory policy that does not block digital sales

Keep the product in Draft while files and delivery are incomplete.

### 4. Build Customer Delivery Packages

Use clean filenames and include a customer guide. Recommended package names:

- `{SLUG}_Ebook_{AUTHOR}.zip`
- `{SLUG}_Audiobook_{AUTHOR}.zip`
- `{SLUG}_Premium_Bundle_{AUTHOR}.zip`

The audiobook archive should contain numbered MP3 files, cover art, and the guide. The bundle should contain the complete e-book and audiobook. Test every ZIP before attachment.

Use `templates/customer_delivery_guide.txt` as a starting point. Record the expected contents in a launch manifest based on `templates/launch_config.example.json`.

### 5. Attach and Test Digital Fulfillment

Attach each archive to its matching Shopify variant through the selected delivery app. Enable automatic delivery email, Thank You access, Order Status access where supported, and a customer-account downloads page.

Run one private $0 test order containing all variants. Prefer a one-use 100% order discount or a draft-order procedure supported by the delivery app. Confirm:

| Test | Required Result |
|---|---|
| All variants | Present at checkout |
| Shipping | $0.00 |
| Payment | $0.00 test only |
| Thank You page | Download-access block visible |
| Customer account | Download history accessible |
| E-mail delivery | Sent when configured |
| Every download | Opens and contains the expected files |

Stop and repair any failed mapping before continuing.

### 6. Select Audiobook Campaign Excerpts

Read `references/audiobook-campaign.md`. Build a narrative progression rather than choosing disconnected quotes. For a seven-day launch, default to:

> mindset → audience → belief → healing → cultural purpose → self-mastery → responsibility

For each excerpt, record the source track, exact time range, transcript, duration, theme, hook, campaign role, and sensitivity note. Normalize social copies without modifying the masters.

### 7. Produce the Campaign

Create one 9:16 Reel and one matching feed cover per day. Use the author’s original excerpt as the primary audio unless the user asks for added music. Include accurate captions, one clear hook, consistent product imagery, and a three-second conversion card.

Write platform-specific copy rather than duplicating one caption everywhere. Promise comment-trigger automation only on platforms where it is actually enabled. Validate platform character limits and hashtag counts.

Use `templates/campaign_playbook_template.md` to document strategy, assets, schedule, conversion path, and launch controls.

### 8. Build the ManyChat Funnel

Read `references/manychat-funnel.md`. Choose the implementation route before building:

| Route | Use When |
|---|---|
| Single-link quick flow | The Shopify product page already presents all formats and the user wants the fastest reliable launch |
| Advanced three-branch flow | Separate format attribution, interest tags, or direct variant links are required |

For either route, require a regular button or Quick Reply in the initial private response before presenting the external Shopify link. Use one `any post or reel` trigger when a unique keyword should work across the full campaign; use post-specific triggers when source attribution is required.

Do not claim contact tagging or Shopify purchase suppression is active unless the selected implementation actually applies and tests those signals.

### 9. Publish with Channel Control

Request explicit approval before publication. Activate the product and publish it to the intended channel only.

Immediately inspect the product’s resource publications. Some app catalogs can use `autoPublish: true` and silently expose newly active products. If product-level unpublication is reversed, use a product-specific `publicationUpdate` removal. Do not disable a catalog’s store-wide auto-publish setting without separate user approval.

Verify the public product page and every direct variant URL before activating ManyChat.

### 10. Validate and Deliver

Run `scripts/validate_launch_packages.py` against the launch manifest. Deliver the campaign playbook, social assets, customer packages, storefront report, ManyChat flow record, and test report.

## Approval Gates

Obtain explicit user approval before:

1. Publishing or changing channel availability.
2. Sending invoices or customer-facing test messages.
3. Completing even a $0 test checkout when acting in the user’s browser.
4. Activating a ManyChat automation.
5. Publishing or scheduling social posts.
6. Changing a store-wide publication or auto-publish setting.

## Failure Rules

If a Shopify or delivery operation fails, report the exact connector or app error and do not substitute a custom item or unrelated delivery mechanism. If an authenticated browser fails repeatedly, preserve Draft status and guide the user with screenshots. If ManyChat cannot be accessed or lacks a required feature, deliver a complete import/build specification and identify the smallest user action needed to proceed.
