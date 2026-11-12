# Pages, links, CMS templates and the batch launch

The new site launches in batches. Until a page's batch launches, its V2 page lives beside the legacy page on a different slug, out of the index. At launch the two swap slugs. There is no page branching on this plan, and a site publish ships **every** non-draft page, so page state is the only thing standing between unfinished work and production.

## Page lifecycle

| Stage | Draft | Slug | Sitemap indexing | Who moves it on |
|---|---|---|---|---|
| 1. Building | **yes** | `[live-slug]-v2` | **off** | you |
| 2. Review build | no | `[live-slug]-v2` | **off** | lead asks for it; lead publishes |
| 3. Launched | no | `[live-slug]` | on | lead, via the launch runbook |
| Legacy page after launch | yes | `[live-slug]-old` | off | lead, same runbook |

Stage 1 is the default. A draft page is skipped by every publish, so a half-built page cannot reach `reo.dev/…-v2` when the client's team publishes the legacy site (they do, regularly). Move a page to stage 2 only when the lead asks for a review build of it; from then on it is public at its `-v2` URL (unlinked and not indexed) after the next publish.

## Creating a V2 page

1. Find the legacy page in `legacy-inventory.md` and read its metadata (`get_page_metadata`, `query_pages_schema_markup`).
2. Check the V2 page does not already exist: `list_pages` (the site has 122+ pages; page through with `offset`) and look for the `-v2` slug.
3. `data_pages_tool` → `create_page`:
   - `title`: legacy name + ` V2` (`Book a Demo V2`)
   - `slug`: live slug + `-v2` (`book-a-demo-v2`); Home is `home-v2`
   - `parentFolderId`: the legacy page's folder, if it has one, so the final path only differs by the suffix
   - `draft: true`
   - `seo` and `openGraph`: copy from the legacy page unless the lead supplied new copy. Do **not** pass `duplicateOf`: duplicating a legacy page copies its legacy elements and classes into the new page.
4. Turn indexing off: `data_sitemap_tool` → `update_page_sitemap_status` with `includeInSitemap: false`, then read it back with `get_page_sitemap_status`. (This tool is in beta and does not work on folders, collection templates or utility pages. If it fails, stop and ask the lead to switch off "Sitemap indexing" in the page settings; do not leave a page with indexing on.)
5. Copy JSON-LD schema from the legacy page if it has any (`bulk_update_pages_schema_markup`), fixing nothing but obvious page-specific URLs.
6. Add the page to the build log (name, id, slug, legacy twin id, state).
7. Switch the Designer to it (`designer_tool` → `switch_page`) and build the shell.

Page shell:

```text
body
└─ div.v2-page-wrapper
   ├─ [component] V2 Global Styles
   ├─ [component] V2 Navbar
   ├─ main.v2-main-wrapper
   │  └─ section.v2-section_… (one per section)
   ├─ [component] V2 Footer
   └─ [component] V2 Cookie Banner
```

Page-level custom code goes in the page's own head / footer (`set_page_freeform_code`, which **replaces the whole block**: read it first and write back the full content). Never touch site-level code.

## Links: which page object to point at

Webflow page links store the **page id**, not the slug. That matters here because the launch swaps which page object owns a slug.

| Link target | How to link it | Why |
|---|---|---|
| A page that has a **V2 page** (any stage) | page reference to the **V2 page** | Before launch it resolves to `/…-v2` (so review builds navigate between V2 pages); after the swap the same object owns the live slug, so the link is right with no edit |
| A page with **no V2 page yet** | link type `url` with the root-relative live path, e.g. `/integrations` | The path stays valid when that page is rebuilt and swapped later. A page reference to the legacy page would follow it to `/…-old` (a draft, so a 404) after its swap |
| A CMS item | the collection item link in a Collection List, or `url` `/blog/[slug]` | Item URLs do not change |
| External | `url`, new tab, `rel="noopener"` | |
| Same-page anchor | page section link to the element, or `url` `#id` | |

Never create a page reference to a legacy page from V2 content. When a V2 page is created for something you previously linked by URL, upgrading that link to a page reference is optional.

## CMS template pages

A collection has exactly one template page and it cannot be duplicated, so the "new page, different slug" method does not work for the 40 template pages (`/blog/…`, `/customer-stories/…`, `/integrations/…` and so on). Editing a live template changes every item page at the next publish.

Method:

1. Build the new template design on a **static staging page** named `template-[collection-slug]-v2` (draft, indexing off), using realistic sample content pasted from one real item. Use V2 classes only. Wrap repeated parts as V2 components where it helps.
2. Rich text: create one class, `v2-text-rich-text`, for long-form CMS content. Its child styles (headings, lists, quotes, images, links inside the rich text) cannot be created as nested selectors through the MCP: either the lead styles them in the Designer with a sample rich text selected, or they go in `V2 Global Styles` as `.v2-text-rich-text h2 { … }` rules and into the ledger. They must reset the legacy tag styles for `ul`, `ol`, `li` and `blockquote`.
3. List every binding the template will need in the build log: element → collection field slug (read slugs with `get_collection_details`; never assume). Note any **new field** the design needs. Adding a field is additive and safe, but only with the lead's OK; never rename, retype or delete an existing field.
4. At that collection's launch, the lead moves the staged layout into the real template page in the Designer (copy and paste between pages keeps classes), removes the legacy tree, and the bindings are applied from your list. This is a lead-run, in-Designer step, done immediately before the launch publish.

Collection Lists on static V2 pages are fine at any time: build them with the Collection List element, bind to the existing collections, and remember draft CMS items never render.

## Utility pages

404 and Password (401) cannot have a second copy. They are rebuilt in place as the last step of the final batch.

## Review build (stage 2)

Only when the lead asks, per page:

1. Confirm indexing is still off (`get_page_sitemap_status`).
2. Set `draft: false` with `update_page_settings`.
3. Tell the lead exactly which pages are now non-draft. They will go to production on the next full publish, at their `-v2` URLs.
4. The lead publishes (to the webflow.io subdomain for a staging-only check, or wherever they decide). You do not publish.
5. Check the published page in a real browser at all four widths: fonts, hairlines, embeds, the link hover reset, interactions, forms, consent banner. Read the page source for `<meta content="noindex" name="robots">`; if it is missing, tell the lead before anything is shared.

## Launch runbook (lead-run)

A batch launch is a set of page swaps followed by one publish. The lead starts it and confirms each destructive step in chat. Your part is preparation, the mechanical edits when told, and verification. Do one batch at a time; write the batch list in the build log first.

### Before launch day

- Every page in the batch has passed review at stage 2.
- SEO title, description, Open Graph image and JSON-LD on each V2 page match the legacy page or the approved new copy.
- Forms tested on staging: submission arrives where the legacy form's did.
- Element ids that external links anchor to exist on the V2 page.
- **Inbound links:** list the legacy components and pages that link to each page in the batch (legacy navbars, footer, CTAs). After the swap those links resolve to the legacy page's new slug (`…-old`), which is a draft and therefore a 404. Fix one of two ways, lead's choice: repoint those legacy links to the V2 page object before publishing, or add a temporary 301 from `/[slug]-old` to `/[slug]` in Site settings → Publishing → 301 redirects. Confirm on staging that the redirect works for a drafted page before depending on it.
- Redirect table reviewed: no existing 301 points **from** a live slug in the batch.

### Swap, per page (in this order, because slugs must be unique)

1. Legacy page → `update_page_settings`: `slug: "[slug]-old"`, `title: "[Name] (old)"`, `draft: true`. Then indexing off.
2. V2 page → `update_page_settings`: `slug: "[slug]"`, `title: "[Name]"`, `draft: false`. Then `update_page_sitemap_status` `includeInSitemap: true`, and read it back.
3. **Home only:** the home page has no slug. The lead sets the V2 page as the home page in the Designer (Pages panel → page settings → "Make home page"); the MCP cannot. The legacy home then needs a slug (`home-old`) and draft.
4. Re-read both pages with `get_page_metadata` and record the result.

Nothing changes on reo.dev until the publish, so the swap can be prepared and checked calmly. If any step fails, stop and report; do not improvise slugs.

### Publish and verify

1. Open Site settings → Publishing → 301 redirects. Changing a slug in Webflow can add an automatic redirect from the old path. A redirect **from** `/[slug]` (the live path) to anywhere must not exist. Remove it before publishing.
2. The lead publishes with the safe-publish workflow.
3. For every page in the batch, on production: 200 at the live URL, the new design, no `noindex` meta, canonical is the live URL, the page is in `sitemap.xml`, forms submit, consent banner works, analytics fires after consent.
4. `/[slug]-v2` now 404s (the slug no longer exists). `/[slug]-old` 404s or redirects, as decided.
5. Spot-check five legacy pages that are still live: their navbar and footer links to the launched pages work.
6. Update the build log: batch, date, pages, anything deferred.

### Rollback

Reverse the swap (V2 back to `-v2` + draft + indexing off; legacy back to the live slug, not draft, indexing on) and publish. Keep the legacy page as a draft until the lead says it can be deleted; do not delete it at launch.
