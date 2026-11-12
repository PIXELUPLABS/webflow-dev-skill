# Webflow MCP: behaviours that bite

Learned on earlier builds with the same MCP server (version 2.2.0 at the time of the audit). Tools change; if one of these no longer holds, note it in the build log.

## Sessions and the Designer bridge

- Call `webflow_guide_tool` once per session with `session_id: "start"`. The result is about 100KB and is often saved to a file instead of returned: grep the file for `ses_` to get the session id, and reuse it on every call.
- Tools that take `pageId` (styles, variables, components, elements) work through the user's open Designer. They can time out for a while when the Designer tab is in the background, while pure data tools (pages, CMS, scripts, fonts, sitemap) keep working. Ask the lead to bring the Designer tab forward. After any timeout or error, **re-query before retrying a write**: a failed action can still leave a half-created element.
- Never run writes in parallel on the same page. It has caused `[Conflict] … component map` errors after which attribute and id writes on existing elements kept failing.
- The user may be editing in the Designer at the same time. Re-read the element or style right before you change it.
- `get_styles` with `query: "all"` returns about 600KB on this site. Do not ask for it with properties. Use `query_styles` with `name_path: ["v2-"]` for day-to-day work.

## Styles

- **The WHTML builder reuses any existing class by name.** A stray `class="button"` or `class="container-large"` in the HTML attaches the legacy class. An unknown class with no CSS is dropped and the element gets no class. Lint every class in a WHTML payload first.
- WHTML takes one root element per action and at most five actions per call.
- `set_style` **replaces** the element's whole style list, and only accepts styles that already exist. Create the style first.
- Combo CSS is not chain-scoped (`.a.is-x` also matches `a is-y is-x`). Do not reuse a combo name for two meanings on one base.
- A global class's CSS applies wherever its name appears, including as a combo. That is why the nine legacy `is-*` global names are reserved.
- Names beginning with `w-` are sanitised (`w--current` → `_w--current`), so Webflow runtime state classes cannot be styled with `data_style_tool`. Use a scoped `<style>` embed inside the component, or the Designer.
- Pseudo-elements work: `update_style` with `pseudo: "before"` / `"after"`, including `content: "\"\""`, and `background-color: inherit`. The Style panel does not show them, so log them.
- Accepted natively: `clip-path`, `filter: drop-shadow(…)`, `aspect-ratio`, `background-clip: text`, `order`, `touch-action`, `min()` / `calc()` values, per-breakpoint pseudo states. Rejected: `text-box-trim`, `text-box-edge` (use a tight line height), `row-gap` with a variable (use `grid-row-gap`).
- A `var(--x)` inside a `box-shadow` string is stored as a binding for the whole property and breaks it. Write shadow colors as rgba.
- Chrome renders a 0.5px border as 1px. Use `box-shadow: inset 0 0 0 0.5px …` for hairlines.
- The Designer paints a grey placeholder on empty divs and adds padding. Decorative absolutely positioned divs need explicit width and height and zero padding.
- The grid `0fr → 1fr` accordion trick collapses to min-content width on the Webflow canvas. Use `max-height` with measured heights.

## Variables

- To write the base mode, omit `mode_id`. Passing `"base"` fails.
- New variables in a multi-mode collection have empty `modeValues`. Set each mode.
- A create batch has been executed twice by the server, leaving `…-2` twins. Keep batches small and check afterwards.
- FontFamily variables take the stack as `static_value`; `custom_value` is rejected.
- `create_variable_mode` with `breakpoint_id` worked for only one collection per site in testing. Create modes plain and apply them with `set_style_variable_mode` on `v2-page-wrapper` per breakpoint.
- `set_style_variable_mode` on an ordinary class without a breakpoint is how theme classes switch the Theme mode.
- Read `cssName` from the tool. Legacy `Theme` variables have no collection prefix in their CSS names; other collections do.

## Elements and components

- `data_element_builder` "TextBlock" creates a Block with a String child: call `set_text` on the String. "Dropdown" creates a toggle, an icon, and a list with three links. "Tabs" creates three links and three panes; style the active link via `.your-class.w--current` in an embed.
- A real `<button>`: `data_element_builder` type `DOM` + `dom_tag: "button"`. `<button>` in WHTML becomes a link. `type` is a reserved attribute name.
- Inline `<svg>` in WHTML becomes native DOM elements (good for icons with `fill="currentColor"`). It also leaves a duplicate custom `class` attribute: `remove_attribute` it. `<a href="#">` leaves an `href` custom attribute that overrides the link setting: remove it after setting the link.
- `<img src>` with an external URL is inserted unmanaged. Upload the asset and bind it with `set_image_asset`. Images from newly uploaded assets stay blank in an already-open Designer until it reloads.
- Image alt defaults to "inherit" from the asset. Setting the asset's alt to null marks it decorative everywhere it is used.
- Navbar brand link: `set_settings` key `link` with `static_link` mode `page`; `set_link` is rejected. The native navbar's collapse breakpoint is not exposed.
- `transform_element_to_component` with `replace: true` turns a built block into a component and leaves an instance behind.
- A component instance's variant is a prop named "Variant"; set it with the variant id as a string.
- HtmlEmbed code is read and written through `data_element_settings_tool` (`get_settings` with `type: "query_settings"`, `queries: [{ value_type: "code" }]`; `set_settings` key `code`). Reading with `all_resolved_settings` inside a component scope has returned an empty error; use `query_settings`.
- Collection Lists: `data_element_builder` type `CMSCollection`, then source, sort, limit and offset through `set_settings`. Item-page link is `static_link` mode `collectionPage` with the template page slug. Draft items never render; API-created items appear in an open Designer only after reload.

## Snapshots and verification

- `element_snapshot_tool` is not a browser. It falls back on fonts, paints inset shadows with spread as fills, never renders embeds, and can hang for minutes on a tall section. Snapshot small blocks. Judge fonts, hairlines, embeds, runtime states and interactions on a published review build or in a local browser harness.
- A local harness can load the hosted `cdn.prod.website-files.com` font files directly for type checks.

## Interactions (IX3)

- `data_interactions_tool` authors Interactions with GSAP headlessly; call its `guide` action first. Scope is `pages` or `component` on this project, **never `site`** (a site-scoped interaction would load on legacy pages).
- Opacity animates under `wf:transform`, not `wf:style`. Easing is a preset index or an object, never a string. There is no per-action delay: use `timing.position`. Respect reduced motion with `conditionalPlayback`.
- A saved interaction is not proof it animates. Check it in Preview or on a review build.
- The legacy site has no IX3 interactions. Whether GSAP is enabled in Site settings is a site-level switch: ask the lead before relying on it, and never load a second GSAP from a CDN.

## Pages, publishing, sitemap

- `create_page` with `duplicateOf` copies a page including its classes. Never duplicate a legacy page into a V2 page.
- `set_page_freeform_code` and `set_site_freeform_code` replace the whole block. `set_page_scripts` / `set_site_scripts` replace the whole list. Read first; never touch the site-level ones.
- `data_sitemap_tool` is beta and covers static pages and CMS items only (not folders, templates, utility pages).
- `publish_site` publishes every non-draft page; single-page publish and branches need Enterprise, which this site is not. You do not call it.
- Page links store page ids. See `pages-and-launch.md` before linking.

## Figma

- Read only the node the lead links (`get_design_context` / `get_screenshot` on that node id), never the whole file. `get_metadata` undercounts large frames.
- Icons: `use_figma` with `node.exportAsync({ format: "SVG_STRING" })` returns SVG text; swap fills to `currentColor`.
- `download_assets` bakes the frame fill behind a node; `get_screenshot` with `contentsOnly: true` and `use_figma` `exportAsync` return the layer on transparency. Exports are cropped to what clipped ancestors show.
