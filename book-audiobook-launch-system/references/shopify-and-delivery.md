# Shopify and Digital Delivery

## Build Order

1. Inspect existing products to avoid duplicates and match store conventions.
2. Create the new product as Draft.
3. Add one `Format` option with E-Book, Audiobook, and Premium Bundle values.
4. Set digital behavior on every variant.
5. Add gallery media and SEO metadata.
6. Package and attach customer files.
7. Configure post-checkout and account access.
8. Complete a private $0 delivery test.
9. Request publication approval.
10. Publish to the intended channel and audit resource publications.

## Digital Variant Standard

| Field | Required Value |
|---|---|
| `requiresShipping` | `false` |
| inventory tracking | off |
| inventory policy | must not block ongoing digital orders |
| SKU | unique, readable, format-specific |
| price | user-approved |
| option name | `Format` unless another label is required |

Do not infer digital behavior from the product type. Query the actual variant inventory item and verify the fields.

## Customer Packages

| Variant | Recommended Package |
|---|---|
| E-Book | ZIP containing the customer-ready PDF or EPUB and guide |
| Audiobook | ZIP containing numbered MP3 tracks, cover, and guide |
| Premium Bundle | ZIP containing the full e-book, audiobook, cover, and guide |

Test ZIP integrity before upload and test extraction after customer delivery.

## Delivery App Setup

Configure the delivery app at the variant level. Attach only the matching package to each variant. Enable automatic email and add its download block to the Thank You or Order Status experience. When supported, create a customer-account page labeled **Digital Downloads** and add an order-level **Access content** action.

Do not enable paid license-key, personalized-content, or in-browser reader features unless the product needs them.

## Private Test Order

Use one order containing all variants so a single test validates the complete mapping. Either apply a supported order-level custom discount in the draft order or create a one-use 100% order discount and complete a private invoice checkout.

Before submission, verify:

| Field | Expected |
|---|---|
| Quantity | One of every variant |
| Subtotal | Sum of all list prices |
| Discount | Full subtotal |
| Shipping | $0.00 |
| Total | $0.00 |
| Card information | Not requested |

After completion, verify the Thank You block, customer-account page, delivery email, filenames, download count, archive extraction, and internal contents.

## Draft-Order Visibility Recovery

A Draft product might not appear in Shopify’s draft-order product picker. If necessary:

1. Query its current publications and Online Store URL.
2. Temporarily change status to Active without publishing to the Online Store.
3. Set the digital variant fields correctly.
4. Complete the test.
5. Return the product to Draft until publication approval.

Immediately audit channel exposure after every activation.

## Controlled Publication

Shopify separates product status from publication. Identify the Online Store publication ID, activate the product, and publish only to the approved publication.

Query `resourcePublicationsV2` or equivalent immediately after activation. If secondary app catalogs appear, inspect their `autoPublish` value.

### Auto-Publish Recovery

If an app catalog uses `autoPublish: true`, `publishableUnpublish` can be immediately reversed. Use a product-specific catalog update instead:

```graphql
mutation RemoveProduct($publicationId: ID!, $productId: ID!) {
  publicationUpdate(
    id: $publicationId
    input: {publishablesToRemove: [$productId]}
  ) {
    userErrors { field message }
  }
}
```

Apply this only to the requested product. Do not set a publication’s store-wide `autoPublish` value to false without separate approval.

## Final Audit

The final launch record must show:

| Check | Requirement |
|---|---|
| Product status | Active |
| Intended publication | Published |
| Unapproved publications | Absent |
| Product URL | Resolves publicly |
| Direct variant URLs | Resolve with correct selected price |
| Shipping | Not required |
| Inventory tracking | Off |
| Delivery attachments | Preserved |

## References

[1]: https://shopify.dev/docs/apps/build/sales-channels/product-publishing "Shopify — Product and Variant Publishing"
[2]: https://shopify.dev/docs/api/admin-graphql/latest/mutations/publicationUpdate "Shopify Admin GraphQL — publicationUpdate"
