# Cleanup runbook: remove the legacy build and strip the V2 marker

**Do not start this on your own.** It runs once, at the very end, when every page has launched and the lead says so in the chat. It deletes the legacy build and renames the whole V2 system, and parts of it cannot be undone. Before it starts the lead makes a **site backup** (Site settings → Backups) and, ideally, a duplicate of the site.

The whole naming scheme was designed so this is mechanical: after the legacy styles are gone, every `v2-x` becomes `x`.

## Preconditions

- No live page is a legacy page. `list_pages`: every non-draft static page was built in V2; every CMS template has been moved to its V2 layout; 404 and Password are rebuilt.
- The linter passes on a fresh `get_styles` dump.
- The build log's custom-code ledger is complete (every class name and CSS variable used in embeds, page code and site code).
- The lead has confirmed the backup exists.

## Order

### 1. Remove legacy pages

Delete the drafted `…-old` pages and the legacy scratch pages (lead does this in the Designer; the MCP has no page delete). Keep nothing that still uses legacy classes.

### 2. Remove legacy components

For each legacy component (the 85 in `legacy-inventory.md`; re-list first, the client may have added some): confirm `instanceCount` is 0 with `get_all_components` (`includeInstanceCount: true`), then delete it in the Designer's Components panel. Any component with instances left means a legacy element is still on some page: find and resolve it, do not force it.

### 3. Remove legacy styles

In the Designer: Style Manager → **Clean up** removes every class that no element uses. Run it once all legacy pages and components are gone. Then take a fresh `get_styles` dump and check:

- every remaining non-combo class starts with `v2-`, except classes Webflow or Finsweet need verbatim;
- anything else that survived is still used somewhere: find the element (`query_elements` by style), fix the page, clean up again.

Do not delete styles one by one through the MCP by name patterns. "Unused" is the only safe criterion, and the Designer is the tool that knows it.

### 4. Reset tag styles

The tag styles (`body`, `h1`–`h6`, `a`, `ul`, `ol`, `li`, `blockquote` …) still carry legacy values. With the lead, either clear them or set them to V2 values (bind `body` to the V2 Body variables and move the breakpoint mode switches from the page wrapper to `body` if wanted). Then remove the "Neutralise legacy tag styles" block from the global embed and re-check link hover states.

### 5. Rename classes

For every non-combo style whose name starts with `v2-`: `data_style_tool` → `rename_style` to the name without the prefix.

- Generate the list from a fresh dump; do not type it.
- Before each rename, the target name must be free. If it is not, a legacy class survived step 3: stop and resolve it.
- Go in small batches, sequentially, never in parallel. Re-query after each batch.
- Combos (`is-*`) need no rename; they follow their base class.
- Keep a rename log (old → new) in the build log.

### 6. Update custom code

`rename_style` does not touch code. Using the ledger, replace every `v2-` class name in:

- the global styles embed,
- every component embed (runtime-state CSS such as `.v2-tabs_link.w--current`),
- page head / footer code,
- any site-level code the lead added for V2.

`data-v2-*` attributes can stay as they are, or be renamed in one pass (attribute and script together).

### 7. Rename variables, components, pages, assets, interactions

- **Variable collections:** rename `V2 Base` → `Base` and so on in the Designer's Variables panel (the MCP has no collection rename). The legacy collections must be deleted first; a collection named `Theme` already exists until then. Renaming a collection changes its CSS custom property names: Webflow updates its own bindings, but every `var(--…)` in the ledger must be updated by hand. Re-read `cssName` with `query_variables`.
- **Components:** `set_component_metadata` → drop `V2 ` from each name and group (`V2 Global` → `Global`).
- **Pages:** names already lost ` V2` at launch; fix any stragglers. Delete `template-…-v2` staging pages. Rename `style-guide-v2` → `style-guide` once the legacy style guide is gone.
- **Assets:** rename or leave; asset names are not visible to visitors. Delete unused legacy assets only with the lead's OK.
- **Interactions:** rename `V2 / …` if the lead wants.
- **Fonts:** remove Inter and Geologica only after confirming nothing references them (`delete_font` is destructive and has no restore).

### 8. Verify, then publish

- Linter in **post-cleanup mode** (`--post-cleanup`): no `v2-` names remain; names are valid Client-First.
- Every page at four breakpoints on staging; forms; consent; analytics; link hovers; focus rings.
- Compare a handful of pages against pre-cleanup screenshots.
- The lead publishes.
