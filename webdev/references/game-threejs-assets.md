# Three.js project assets

For new or existing Three.js projects: preserve the project, starter identity, build configuration and
custom loaders. Do not reinitialize or run Godot doctor/import/bundling/export/release preparation.

## Legacy build-size checks

Before building or saving an existing Three.js project, inspect `scripts/check-size.mjs` if present.
Only edit an untouched official v1/v2 script with one of these SHA-256 digests:

- v1: `64edc9349af0a26881eb311aabdac518477c31786d0e15911a06b4440df5e502`
- v2: `f255f0da076b668f19fe2daa0a96b20455d736e10c77c7a61936ffe3a1c818ce`

In your normal editing task, remove only `transfer: 4.4 * MB` from `BUDGET` and `transfer` from
`Object.entries({ js, fonts, transfer })`. Preserve JS/font budgets, total size reporting, source files
and template identity. Tell the user about this change and include it in the next Manus checkpoint.
Preserve custom, missing or symlinked checks, including a symlinked parent directory. If editing fails,
report the blocker without claiming the limit was removed. Attachment and runtime recovery do not
modify this file. New v3 projects already omit the aggregate transfer rejection.

If a build-size check fails, report its measured size and overrun; preserve valid manifest entries and
respect user quality/scope constraints. Do not edit frozen starters or claim completion while builds fail.

## Generation decision

New games follow the four saved [Blueprint model choices](game-blueprint.md#threejs-blueprint).
An approved `hybrid`, `ai_generated` or `ai_generated_max` choice requests its model-production method
for the initial Blueprint implementation only; it is not ongoing consent for later requests.
Select individual models from gameplay needs and recorded restrictions. Historical `custom` choices
follow their recorded restrictions. Pending/cancelled choices and missing historical fields are not
generation consent. Preserve narrower supplied-only, no-AI, budget and style restrictions.
This decision does not authorize generated audio; assess need and obtain its separate approval.

Existing games may add models without replacing their Blueprint or restarting setup. A direct request to
generate a model authorizes that model; a generic request to improve visuals does not. Settle only the
new asset decision using the existing Blueprint when it is still pending, or one focused question when
there is no pending card. Preserve settled gameplay and online services. Do not recreate the game.

## Generate, validate, register

Resolve `GAME_RUNTIME` only from the current init/attach/run-start receipt. Before paid generation, read
`$GAME_RUNTIME/asset-capabilities.json`. Require `engines` to include `threejs` and `manifestVersion: 2`.
Read this file before running any script: an older script may ignore unknown flags and perform work.
After that check, `node "$GAME_RUNTIME/sync-assets.mjs" --capabilities` is an optional read-only probe.
If the installed package cannot report this, stop before generation and update the
Addon runtime, then retry in the same project. New UI or a refreshed tool list alone is not proof that
the device package has activated. Preserve the current task and files during update.

Apply this entry-point choice to each authorized new-game or existing-game generation request. Honor an
explicit entry-point choice already made for the request without asking again. Mentioning Tripo alone
does not select the connector: the built-in `manus-tools.generate_3d_model` also uses Tripo.

When the entry point is unsettled, run `manus-config connector search Tripo` to inspect the current
connector's current-task `enabled` state. If more detail is needed, use `manus-config connector get <uid>`
with the UID from that result. Use the reported `enabled` value for this default; do not infer it from
a catalog listing, protected-value placeholders, or absence from the coordinator's tool list. If an older
sandbox reports an unknown search command, fall back to `manus-config config load --search "Tripo"`
only when there are no pending config edits or unconfirmed saves: load overwrites the editable config
and baseline. Do not discard another in-progress configuration change. Do not enable, connect or save
connector configuration merely to perform this check. If the state cannot be read, explain the
uncertainty and ask which entry point to use without a countdown; do not assert it is disconnected.

Current-task enablement determines whether to offer the connector. For an enabled connector, discover its
generation/status/export tools through its supported tool-discovery path before offering a timed
default. Follow manus-config's execution-context rules for connector tools; a coordinator's own tool
list alone does not establish availability in the connector-enabled execution context.

- With `enabled: false` or no Tripo connector result, default to the built-in tool without asking
  whether to use or connect personal Tripo. This also applies when Tripo is connected but disabled
  in the current task. State that model generation deducts Manus credits before generating.
- With `enabled: true` and no settled entry-point choice, use the ask tool to offer
  **My Tripo connector — model generation deducts credits from your connected Tripo account** and
  **Manus built-in — model generation deducts Manus credits**.
  Only when the connector is enabled and its tools are available in the current task, and the available
  ask schema supports `auto_select`, set `seconds: 30` and set `option` to the exact
  personal Tripo option text. State that no response within 30 seconds selects the user's connected
  Tripo account. This timed default applies only to this already-authorized generation request; a
  manual answer wins. Wait for the manual answer or the tool's actual automatic selection before
  generating; do not start a shell timer or treat elapsed time in model reasoning as a reply.
  On an older ask schema without `auto_select`, omit that parameter and wait for the answer before
  generating; do not claim a countdown is active. These are generation charges; do not imply that
  using the connector makes the surrounding Manus task free. State the same charge source before
  using an already explicit choice, without repeating the choice question.
  If the connector is enabled but its tools are unavailable for this task, omit `auto_select`, explain that using it
  may require a setup confirmation, and wait for the user's choice. After an explicit connector choice,
  follow `manus-config connector ensure "Tripo" --uid <uid>` using the inspected UID. If it returns a
  pending configuration card, present it and wait for confirmation; if it reports ready, discover and
  use its tools. Older sandboxes follow manus-config's documented load/edit/save fallback while
  preserving pending edits. Never treat expiry as permission to enable or reauthorize an account.

For the built-in choice, use `manus-tools.generate_3d_model` with an absolute `.glb` output path under
`assets/models/` in the bound project. Text-only uses `prompt`; single-image uses `image`; mixed input uses
both (image editing adds Manus credits). Use a supplied image or a project image as reference; preserve
originals. Follow the tool's actual schema; do not invent a provider API or selectable model parameter.
If it is unavailable, explain that the runtime/tool capability must update; do not retry initialization,
invoke an unregistered tool or silently switch to the connector.

For the user's connector choice, use its registered connector tools and their actual schemas to
generate, check status and export the selected model. Keep the task/result identity and download the
completed GLB into a new absolute path under the bound project's `assets/models/`. If export is needed,
export that existing result as GLB; do not regenerate or rename another format to `.glb`. Preserve any
referenced textures/buffers alongside the model. A connector connection/authorization failure is a
blocker to report, not permission to switch to Manus billing or create a new paid generation task.

For either entry point, generation and device delivery are separate. If generation succeeded but
delivery failed, recover the existing result from its artifact receipt or connector task/result identity;
do not generate or charge again. A session or provider URL is a transfer source only. Land the complete
model in the project and validate it before using it. No placeholder GLB
or in-progress manifest entry. Choose a new filename for each regenerated model,
preserve the old file and change gameplay references only when asked to apply the result.
Asset-panel requests create library assets; the user can use Send to Manus to apply them. Explicit
generate-and-apply requests can do both.

For early registration after files land, run `node "$GAME_RUNTIME/sync-assets.mjs" --engine=threejs`
from the project root; skip it when saving next unless the batch needs grouping first. In Local First,
run sync/save through `webdev.manus_git` to use the Managed Git index; in Cloud use the project terminal.
Sync validates files, uploads changes, restores missing recorded bytes and updates `assets.lock.json` v2,
reusing hashes/storage and preserving groups. Do not invent storage keys. On upload failure, retry with
the existing output; completed uploads survive. Apply [Asset browser groups](#asset-browser-groups)
to the registered batch before saving.

## Save and load assets

Use `node "$GAME_RUNTIME/save-threejs.mjs" --message "Update"` with temporary Manus Git author/committer
identity before each checkpoint. Follow [Git/checkpoints](git-checkpoints.md) for remote integration,
push, receipt verification and uncertain-command recovery. Save returns a local SHA and never pushes. If unavailable, update
the runtime in this project; do not replace it with a raw commit containing assets.

Save synchronizes assets, then commits source, lock, package.json, recovery scripts and .gitignore together.
Resolve staged edits or unfinished merge/rebase first. Sync installs `scripts/manus-game-assets/` before
existing build/dev commands and exact ignore rules for validated registered files. Early sync leaves the
index untouched; save removes tracked assets only from its private candidate index, preserving working
copies and Git history. Never force-add managed binaries or commit after failed synchronization.
Unsupported/unregistered inputs, including separate glTF buffers, remain in Git. No starter upgrade or
automatic compression is needed.

Use package build/dev commands, not direct Vite, to restore missing assets and verify download size/hash
before the original command. Existing local bytes are unchanged; sync/save treats them as edits. History
previews trust files in the selected commit and validate missing Storage downloads through the authorized
operation reader before Vite, without exposing credentials to project code. Hosted builds need
`MANUS_API_URL` / `MANUS_API_KEY`; downloads stream to disk with at most eight transfers and three transient
attempts, using Godot's preview retry/timeout policy. Permission/integrity failures stop restoration.
There is no additional asset baseline, Git-tracking fallback or asset revision counter.

### Asset references

Keep existing local/bundler paths. Source, styles and JSON tables select restored assets. For
`import.meta.glob`, template paths like `assets/models/${name}.glb`, or concatenation after a literal
`assets/models/` prefix, restoration includes every registered file under that prefix, including nested
textures; glob exclusions do not narrow it. Unrelated library directories stay in Storage. Fully computed
paths without a literal directory prefix must be listed explicitly in asset tables.
For stable `/manus-storage/...` addresses and temporary download URLs, follow
[Storage](storage.md#stable-asset-addresses); never persist signed URLs or credentials.
Saved previews freeze only storage paths referenced in the browser build, so retain complete paths in
built code/tables, including dynamically selected models, rather than separate hash/path fragments.

### Version changes and delivery

Before switching Git versions, preserve unsaved asset edits. After materializing another checkpoint or
fast-forwarding to a saved tree, run `node "$GAME_RUNTIME/restore-threejs.mjs" --from-lock` before building,
editing or syncing. This verifies size/hash and restores the selected lock's bytes, including stale
same-name local copies, without upload or manifest changes. It is not a normal build step.
During native forward rollback, preserve the exact target tree; do not sync or use standard save.

Before saving, require a passing build from a clean checkout of the candidate source and pinned lock
without ignored working copies, plus real Preview. For favicon/OG preparation, follow
[Game sharing](game-sharing.md#threejs-preparation); put their PNGs under `assets/` for registration and recovery.
ZIP/remix/copy are post-save operations, not checkpoint prerequisites. When requested, verify exact-version
restoration and destination storage transfer, reporting unverified steps. ZIP contains editable bytes but
does not provision destination storage; complete or verify that transfer before reusing its storage paths.
Never substitute another version or regenerate missing assets.

## Asset browser groups

Choose groups by the game's browsing purpose, not media type, source pack, production method or directory depth.
`assetType` describes the media; `groupId` describes its purpose in the game. Type directories such as
`models`, `images` or `audio` are not useful purpose groups. Keep files in their existing paths; classify
subjects by their actual role rather than imposing a fixed taxonomy or a group for every folder.
Preserve existing user-defined IDs, names, memberships and order unless regrouping is requested;
reserved `assets/template/` media stays in `template`. Automatically inferred directory groups are defaults,
not user-defined categories: assign meaningful groups to the new batch even when sync already supplied one.

After the engine-specific sync has registered the new batch, edit only complete `assets.lock.json` entries.
Never prewrite partial entries with just `groupId` or invent storage facts. Already registered assets need
no extra sync for grouping alone. Assign `groupId` and matching `groups` declarations with human-readable
`name` and `order`. Normalize IDs to lowercase, replace runs of non-letter/non-number characters with `-`,
and trim edge hyphens. Keep recolored/adapted variants with their subject.

Runtime fallback uses the first directory below `assets/`, so `assets/models/` becomes `models` regardless
of content. This is registration fallback, not completed grouping. Change only membership and group
metadata, never storage paths, hashes, sizes, asset types or provenance; no file move or upload is needed.
Check the batch's entries and declarations before saving, then confirm the saved version retains the groups.
A post-save grouping edit needs a new checkpoint. No browser session is required.

## Use and verify

Use the existing loader (or `GLTFLoader`); verify scale, pivot, orientation, textures, color space and
animations in Preview. Reuse geometry/materials, dispose retired resources, use separate simple collision
geometry and show a placeholder on load/failure.

The built-in delivery path accepts up to 64 MiB; connector generation/export limits come from its tool
contract. For either entry point, the asset viewer uses the same 20 MiB per-file read limit for all asset
types. Model preview supports only its current GLB formats/extensions. A valid larger model may be
available as an asset without an inline preview.
Check required GLB extensions against the game's configured decoders; do not claim the asset viewer
supports every runtime format.
