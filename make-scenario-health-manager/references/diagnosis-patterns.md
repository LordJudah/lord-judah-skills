# Diagnosis Patterns

## Shared-Dependency Pattern

Use this pattern when several scenarios fail at the same provider, connection, or module family.

| Signal | Interpretation | Next move |
| --- | --- | --- |
| Multiple scenarios fail at the same OpenAI module with `429` errors | Billing, credit, or provider quota issue | Verify the shared connection, then ask the user to restore billing or quota before editing blueprints. |
| Several scenarios fail after a credential change | Shared authorization or revoked access | Verify the connection inside Make before changing logic. |
| One scenario is auto-deactivated after repeated failures while similar scenarios also fail | Shared failure escalated into scenario shutdown | Restore the shared dependency first, then reactivate and retest the affected scenario. |

## Scenario-Specific Pattern

Use this pattern when one workflow continues to fail after a shared dependency has been repaired.

| Signal | Interpretation | Next move |
| --- | --- | --- |
| A scenario now fails farther downstream after provider billing is restored | The original blocker is fixed and a local configuration error is now exposed | Inspect the first newly failing downstream module. |
| The error is `BundleValidationError` | A required field, parameter, or mapped value is missing or invalid | Compare the module's required fields to its mapper entries in the blueprint. |
| The logs show upstream modules succeeding and one create/update module failing | Data reached the destination step but required schema fields are wrong | Patch only the destination module mapping. |

## Repair Phrase Templates

Use concise internal phrasing like this during notes and reporting:

| Situation | Suggested phrasing |
| --- | --- |
| Shared quota issue | `The scenario is failing at a shared provider dependency rather than in its internal logic.` |
| Auth issue | `The connection itself is failing verification, so repair should focus on authorization before blueprint edits.` |
| Downstream mapping issue | `The scenario now progresses past the original blocker and fails on a downstream validation step, indicating a local configuration issue.` |
| Successful validation | `A fresh execution completed successfully, which confirms the repair rather than merely saving the configuration.` |

## Validation Standard

Treat a scenario as validated only when one of these is true:

| Validation type | Accept as final? | Notes |
| --- | --- | --- |
| Fresh successful execution | Yes | Best evidence. |
| Latest logs show success after the fix | Yes | Strong fallback when direct outputs are limited. |
| Connection verifies but no fresh run exists | No | Helpful but incomplete. |
| Blueprint saved without a new run | No | Saving alone does not prove the fix worked. |
