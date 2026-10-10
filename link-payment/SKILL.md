---
name: link-payment
description: |
  Gets a secure, one-time-use virtual card through Link CLI for card-based merchant checkout. Use when the user asks to buy something, pay for something, complete checkout, get a virtual card, or pay through a merchant card form.
---

# Link Payment

Use Link CLI to create a **one-time-use virtual card** for card-based merchant checkout. This skill only supports the `card` credential type.

## Principles

Default to completing the full virtual-card checkout flow. Unless card payment is clearly confirmed to be impossible for the merchant, do not skip, replace, or abandon the card flow, and do not switch to another credential type or machine-payment flow.

The sandbox already contains the Link CLI login state. Do not run installation, MCP setup, or authentication flows. If a command or parameter is unclear, append `--help` to the relevant `link-cli` command before proceeding.

## Workflow

### 1. Inspect checkout requirements

Before creating a spend request, inspect the merchant checkout page and collect the required checkout facts.

**Optional wallet sign-in prompts.**

In the card checkout flow, an automatically opened accelerated-checkout sign-in prompt (for example, Shop Pay's email recognition or verification-code popup) may be optional. Do not treat the presence of an OTP field alone as proof that authentication is required. If the prompt offers a visible Close, Cancel, Not now, or Continue as guest action, dismiss it and inspect the page again before continuing the guest or card checkout flow. Do not ask the user for an optional wallet verification code.

Use the observed dismiss control. If semantic targeting is unavailable but a dismiss control is clearly visible, use the browser tool's supported, screenshot-bound coordinate click when permitted, then inspect the result. If an action reports that its target is blocked or not interactable, inspect the current page for an overlay before retrying the underlying checkout control.

If the user explicitly chose that wallet, do not silently dismiss its sign-in or switch payment flows. Request user input or takeover when authentication is required for the chosen flow, the prompt cannot be safely dismissed after inspecting the result, or the tool reports a capability or permission boundary. Do not bypass required authentication or change payment authorization.

| Required fact | Rule |
|---|---|
| Final payable amount | Use the exact final total in cents, including taxes, shipping, fees, discounts, and other adjustments. |
| Currency | This flow currently supports `usd` only. If the user needs a non-USD payment, tell them this virtual-card spend request flow only supports USD and ask how they want to proceed. |
| Merchant details | Collect the merchant name and merchant URL from the checkout page. |
| Product details | Collect product names, quantities, unit amounts, and useful product identifiers or URLs when available. |
| Shipping or user details | If checkout requires them, retrieve saved data with the commands below and use defaults unless the user chooses otherwise. |

```bash
link-cli shipping-address list --format json
link-cli user-info retrieve --format json
```

### 2. Get the payment method

List the user's Link payment methods and use the default payment method unless the user asks for another one.

```bash
link-cli payment-methods list --format json
```

The selected `payment_method_id` from the command output is used in the spend request.

### 3. Create the card spend request

Create a spend request using the selected payment method and final payable total.

```bash
link-cli spend-request create \
  --credential-type card \
  --payment-method-id <payment_method_id> \
  --amount <total_amount_in_cents> \
  --currency usd \
  --merchant-name '<merchant_name>' \
  --merchant-url '<merchant_url>' \
  --context '<at least 100 characters describing what is being purchased and why; the user sees this when approving>' \
  --line-item 'name:<product_name>,unit_amount:<unit_amount_in_cents>,quantity:<quantity>' \
  --total 'type:total,display_text:Total,amount:<total_amount_in_cents>' \
  --format json
```

Keep text values in single quotes as shown, and leave apostrophes out of them. Inside double quotes the shell expands `$`, so `$8.00` in `--context` would reach the user's approval screen as `.00`.

Use these parameter rules when building the command.

| Parameter | Rule |
|---|---|
| `--credential-type card` | Required because this skill only supports virtual-card checkout. |
| `--payment-method-id` | Use the selected payment method ID from `link-cli payment-methods list --format json`. |
| `--amount` | Amount must be in cents and cannot exceed `50000` cents, i.e. USD 500.00. The amount must match the final payable total. |
| `--currency usd` | Required. Only `usd` is currently supported in this flow. If the user needs a non-USD payment, warn the user instead of proceeding. |
| `--merchant-name` / `--merchant-url` | Required for `card`; get these from the merchant checkout page. |
| `--context` | Minimum 100 characters. Describe the purchase and rationale clearly because the user reads this text when approving the spend request. |
| `--line-item` | Include at least `name`; include `unit_amount` and `quantity` when available. Repeat for multiple products. |
| `--total` | Include at least `type:total,display_text:Total,amount:<total_amount_in_cents>`. Repeat for subtotal, tax, shipping, fee, or other total breakdowns when useful. |
| `--format json` | Required. Keep this flag because the create command must return JSON containing the spend request ID and `approval_url`; it also returns the approval URL instead of entering automatic approval polling. |
| `--request-approval` | Do not explicitly set or modify this parameter. Rely on `--format json` for the create-then-pause approval flow. |

After creating the request, keep the `spend_request_id` from the JSON output for later retrieval. Present the `approval_url` clearly to the user, tell them to approve the spend request, and ask them to reply after approval is complete. This notification is the pause point: do not poll for approval automatically, and do not call `link-cli spend-request retrieve` until the user confirms approval.

### 4. Retrieve the virtual card and complete checkout

After the user confirms approval, retrieve the virtual card details. The expected path is that a single retrieve command returns the card.

```bash
link-cli spend-request retrieve <spend_request_id> \
  --include card \
  --format json
```

Use the returned card details to fill the merchant's checkout form and complete the payment on the website. The card object contains the card number, CVC, expiration month and year, billing address, and validity window.

If the user says they approved the request but the retrieve command does not return a card, inspect the returned status and error details. Do not create a new spend request unless the original request is clearly denied, expired, canceled, failed, or otherwise unusable.
