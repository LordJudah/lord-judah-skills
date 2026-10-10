# ManyChat Book Funnel

## Architecture Choice

Use ManyChat’s native Instagram comment automation when the user already has a connected account. This is lighter than building a separate webhook service and keeps comment replies, DMs, tags, and timing in one managed system. Use a separate event integration only when verified Shopify purchase suppression or cross-platform orchestration is required.

| Approach | Tradeoffs | Cost | Setup Complexity |
|---|---|---|---|
| ManyChat native flow | Fastest; managed comment and DM logic; purchase tracking may require another integration | Existing plan limits apply | Low to moderate |
| Custom Shopify and Instagram event service | Full data control; higher maintenance and authentication burden | Hosting and API costs may apply | High |

## Instagram Entry Rule

Create a **User comments on your Post or Reel** trigger. Use a memorable keyword and test capitalization and punctuation variants.

The initial private reply alone does not open the standard messaging window. Require a regular button or Quick Reply before sending purchase links.[1]

## Choose the Flow Type

Use the **single-link quick flow** when the Shopify product page already contains all format choices. Use the **advanced branch flow** when separate interest tags, attribution, or direct variant links are required.

| Capability | Single-Link Quick Flow | Advanced Branch Flow |
|---|---|---|
| Setup speed | Fast | Moderate |
| Customer destination | Main Shopify product page | Direct format-specific pages |
| Format selector | Shopify | ManyChat |
| Interest tags | Not included by default | Included |
| Best use | Ready-to-launch book campaigns | Segmented nurture and measurement |

### Single-Link Quick Flow

1. Choose Instagram **Auto-DM links from comments**.
2. Select **any post or reel** when one unique keyword should cover the campaign.
3. Enter the specific keyword and enable rotated public replies.
4. Write the opening DM and add one opt-in button.
5. Write the product message and link its button to the main Shopify product page.
6. Add one optional non-click follow-up.
7. Activate only after approval, then test with a secondary Instagram account.

### Advanced Branch Flow

| Step | Node | Action |
|---:|---|---|
| 1 | Comment trigger | Match the campaign keyword |
| 2 | Source tag | Add a post- or theme-specific entry tag |
| 3 | Public reply | Confirm that the DM was sent |
| 4 | Initial private reply | Introduce the offer and show one Quick Reply |
| 5 | Quick Reply | Open the opted-in conversation |
| 6 | Lead tag | Add the master campaign lead tag |
| 7 | Format selection | Present E-Book, Audiobook, and Bundle choices |
| 8 | Choice branch | Add a format-interest tag and open the matching Shopify URL |
| 9 | Smart Delay | Wait inside the standard messaging window |
| 10 | Purchase condition | Stop only when a verified purchase tag exists |
| 11 | Follow-up | Offer format guidance or answer a question |

## Copy Template

### Public Replies

Rotate substantive replies:

1. “The transmission is on the way—check your DMs for the three formats.”
2. “Got you. I sent the E-book, Audiobook, and Bundle options.”
3. “The guide is in your inbox. Choose how you want to experience it.”
4. “Message sent. Check your requests if you do not see it immediately.”

Avoid one-word or emoji-only replies.

### Initial Private Reply

> Peace, {{first_name}}. You asked for **{CAMPAIGN PROMISE}**.
>
> **{BOOK TITLE}** is available in three forms: read it, hear it, or own both. Tap below and I’ll show you the options.

**Quick Reply:** `SHOW ME THE OPTIONS`

### Format Selection

> Choose how you want to experience **{BOOK TITLE}**.
>
> **READ IT — {EBOOK PRICE}**  
> {EBOOK VALUE}
>
> **HEAR IT — {AUDIOBOOK PRICE}**  
> {AUDIOBOOK VALUE}
>
> **GET BOTH — {BUNDLE PRICE}**  
> {BUNDLE VALUE}

Use three buttons or three short branches. Apply an interest tag before opening the corresponding direct variant URL.

### Follow-Up

Schedule the follow-up with a buffer before the standard messaging window closes.

> Peace, {{first_name}}—did the book page open correctly?
>
> If you are still choosing, reply with **READ**, **HEAR**, **BOTH**, or any question. I’m here to help you choose the right format.

Do not send an automated promotional follow-up after the applicable window.[2]

## Tag Convention

| Tag Pattern | Purpose |
|---|---|
| `{KEYWORD} Lead - {YEAR} Campaign` | Master audience |
| `{KEYWORD} Entry - D# {THEME}` | Source attribution |
| `{KEYWORD} Interest - E-Book` | Reading preference |
| `{KEYWORD} Interest - Audiobook` | Listening preference |
| `{KEYWORD} Interest - Premium Bundle` | High-value preference |
| `Purchased - {KEYWORD}` | Suppress pre-purchase follow-up after verified order event |

Do not create a purchase condition unless a real integration applies the purchase tag.

## Link Rules

Verify the live product page before entering URLs. Prefer direct variant links:

```text
{PRODUCT_URL}?variant={VARIANT_NUMERIC_ID}
```

Test every link on mobile. Confirm the selected price and format. Do not activate the flow while the Shopify product is Draft or unavailable.

## Testing

Use a non-admin Instagram account where possible. For the single-link route, verify that the Shopify product page exposes the full format selector. For the advanced route, test every direct variant button and tag.

| Test | Expected Result |
|---|---|
| Comment exact keyword | One public reply and one private response |
| Keyword with punctuation | Trigger behavior matches configuration |
| Ignore first private reply | No format message or follow-up |
| Tap opt-in Quick Reply | Lead tag applies and format choices appear |
| Tap each format | Correct interest tag applies and direct variant opens |
| Repeat comment on same post | May not trigger again for the same user |
| Follow-up path | Arrives before the messaging window closes |
| Purchase-tag condition | Suppresses follow-up only after verified tag application |
| Unmatched comment | Does not enter the sales flow |

## Activation Gate

Before activation, verify the trigger post, public replies, opt-in text, three URLs, tags, smart delay, fallback path, and privacy-safe test account. Obtain explicit user confirmation before publishing the automation.

## References

[1]: https://help.manychat.com/hc/en-us/articles/14281316989724-Instagram-Post-and-Reel-Comments-trigger "ManyChat Help — Instagram Post and Reel Comments Trigger"
[2]: https://help.manychat.com/hc/en-us/articles/14281199732892-How-to-send-messages-outside-the-24-hour-and-7-day-windows-in-Messenger-and-Instagram "ManyChat Help — Messaging Windows"
