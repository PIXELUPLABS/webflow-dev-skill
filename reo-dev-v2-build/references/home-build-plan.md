# Home page build plan: task cards

One card per Claude session, in order. Each card says what must be true before it starts, the prompt to paste, what the developer checks, and what the lead will look at. Mark a card done in the build log only when its "Done when" list is true.

Read with `home-page-blueprint.md` (what to build) and `developer-playbook.md` (how to run a session).

**Legend:** 🔒 needs the lead's OK before it starts · ⏸ blocked until the lead answers a question

| Card | Task | Depends on | Size |
|---|---|---|---|
| T00 | Environment check | – | 15 min |
| T01 | 🔒 Fonts | T00 | short |
| T02 | Variables | T00 | medium |
| T03 | Shell, structure and typography classes | T01, T02 | medium |
| T04 | Component classes and V2 Global Styles | T03 | medium |
| T05 | 🔒 Style Guide V2 page | T04 | medium |
| T06 | Asset export and upload | T00 | medium, can be split per section |
| T07 | V2 Section Divider | T04, T06 | short |
| T08 | V2 Navbar | T04, T06 | medium |
| T09 | 🔒 Home V2 page, shell, Hero | T05, T07, T08 | medium |
| T10 | Trusted By | T09 | medium |
| T11 | Product Demo | T10 | short |
| T12 | The Problem | T11 | short |
| T13 | Testimonial | T12 | long |
| T14 | Take Reo Anywhere | T13 | medium |
| T15 | Trust & Compliance | T14 | medium |
| T16 | V2 CTA Banner | T15 | short |
| T17 | V2 Footer | T16 | medium |
| T18 | ⏸ V2 Cookie Banner | design from the lead | medium |
| T19 | Whole-page responsive and accessibility pass | T17 | medium |
| T20 | 🔒 Review build QA | T18, T19 | medium |

---

## T00 Environment check

**Prompt**

> Use the reo-dev-v2-build skill. Do the session-start steps only. Confirm you can read the Reo.Dev site (67e6b65ee328bc6b91324c9a), list its variable collections, tell me whether any V2 collection or v2- class exists yet, and take a Figma screenshot of node 191:12340. Change nothing in Webflow.

**You check:** Claude names the right site, reports the legacy collections (Primitives, Theme, UI Styles, Reponsive, Typography 1, Typography 2), and shows the hero screenshot.
**Done when:** both MCPs work and the build log's status table is confirmed as accurate.
**Lead looks at:** nothing; this is a smoke test.

## T01 🔒 Fonts

**Before:** the lead has approved uploading Switzer, Geist, Geist Mono and Source Serif 4.

**Prompt**

> Use the reo-dev-v2-build skill. Task T01: upload the four V2 font families as described in v2-foundation.md "Fonts". Inspect each file with scripts/woff2info.mjs before upload, use font-display swap, keep Source Serif 4's optical-size axis, then list the site's fonts and record the font ids in the build log. Do not touch Inter or Geologica.

**You check:** Site settings → Fonts shows Switzer (400, 500), Geist, Geist Mono, Source Serif 4 as well as the two old fonts.
**Done when:** `list_fonts` shows the new records with status uploaded; ids are in the log.
**Lead looks at:** the font list; that nothing was replaced.

## T02 Variables

**Prompt**

> Use the reo-dev-v2-build skill. Task T02: create the five V2 variable collections, their modes and variables exactly as in v2-foundation.md. Work in small batches and re-query after each. Set every non-base mode value explicitly. Afterwards query for accidental "-2" duplicates inside the V2 collections and remove only the ones you created. Record collection and mode ids in the build log. Do not touch the six legacy collections.

**You check:** the Variables panel shows `V2 Base`, `V2 Theme`, `V2 Typography`, `V2 Layout`, `V2 Sizes` beside the legacy ones; `V2 Theme` has Dark Mode and Brand Mode; `V2 Typography` and `V2 Layout` have Tablet and Mobile Landscape.
**Done when:** every row of the foundation tables exists with the listed value in every mode; no duplicates; legacy collections unchanged (same variable counts as in `legacy-inventory.md`: 99, 24, 62, 18, 5, 5).
**Lead looks at:** three spot values per collection, including one tablet and one mobile value; the legacy counts.

## T03 Shell, structure and typography classes

**Prompt**

> Use the reo-dev-v2-build skill. Task T03: create the shell and structure classes (v2-page-wrapper, v2-main-wrapper, v2-padding-global, v2-container-large, v2-padding-section-*, v2-theme-dark, v2-theme-brand, v2-theme-light) and the typography, text-colour and background classes from v2-foundation.md, bound to V2 variables. Bind the Tablet and Mobile Landscape modes on v2-page-wrapper per breakpoint and the theme modes on the theme classes, and read the bindings back. Lint every name first. Do not create utility classes that are not in the foundation tables.

**You check:** typing `v2-` in the Designer's class field lists the new classes; none of them shows a raw colour or px value where a variable is expected.
**Done when:** `get_style_variable_modes` on `v2-page-wrapper` shows both collections switching at `medium` and `small`; `v2-theme-light` resets the theme (or the fallback "Light Mode" exists and is recorded); linter clean.
**Lead looks at:** `v2-heading-style-h1` and `-h2` (all five typographic properties plus zero margins), the mode bindings.

## T04 Component classes and V2 Global Styles

**Prompt**

> Use the reo-dev-v2-build skill. Task T04: create the global component classes in v2-foundation.md (v2-button with is-secondary, is-dark, is-light and the pseudo-element stripes; v2-link-button; v2-tag; v2-eyebrow with is-inverse; v2-stat; v2-icon-1x1-*; v2-icon-button; v2-button-group) with hover and pressed states, and the V2 Global Styles component with the embed from the foundation file. Replace the focus-ring placeholder with the real cssName from query_variables. Add every class and CSS variable used in the embed to the custom-code ledger, and the button pseudo-elements to "Styles not visible in the Style panel".

**You check:** a `V2 Global Styles` component exists in group `V2 Global`. The legacy `Global Styles` component is untouched.
**Done when:** each link-type class has its own hover state; the embed contains no `REPLACE-` placeholder; ledger updated; linter clean.
**Lead looks at:** the embed code; the ledger; that buttons have stripes only on the variants that should.

## T05 🔒 Style Guide V2 page

**Before:** the lead has approved creating the page.

**Prompt**

> Use the reo-dev-v2-build skill. Task T05: create the page "Style Guide V2" (slug style-guide-v2, draft, sitemap indexing off) with the V2 page shell, and build a specimen of everything created so far: palette swatches for V2 Base and V2 Theme, every type style with its three breakpoint sizes, all button variants and states, tag, eyebrow (both tones), link button, stat, icon sizes, and one block each inside v2-theme-dark and v2-theme-brand. Use v2-styleguide_* classes for the page's own layout. Verify page state and record the page id.

**You check:** the page reads like the Figma type and colour system; dark and brand blocks flip text and button colours on their own.
**Done when:** every foundation class appears at least once on the page; page is draft with indexing off; nothing on it uses a legacy class.
**Lead looks at:** this page is the fastest daily check. Type sizes at Desktop, Tablet and Mobile; the three themes; hover states.

## T06 Asset export and upload

Can be run once for everything or per section just before that section's card.

**Prompt**

> Use the reo-dev-v2-build skill. Task T06: export the assets for [all sections / section N] listed in home-page-blueprint.md "Assets to export" from the Figma nodes given, as SVG for vectors (fills switched to currentColor for UI icons, width and height kept) and WebP at 2x for raster, named as the blueprint says. Upload them to the V2 asset folder, set alt text (empty for decoration), and list asset names and ids in the session report. Do not upload anything without the v2- prefix.

**You check:** the Assets panel has a `V2` folder with sensibly named files; logos are white on transparent; SVG icons are not blurry.
**Done when:** every asset the section needs is uploaded with alt text set; the report lists them.
**Lead looks at:** naming; that customer logos are the right companies; file sizes (no multi-megabyte images).

## T07 V2 Section Divider

**Prompt**

> Use the reo-dev-v2-build skill. Task T07: build the V2 Section Divider component (group V2 Global) from home-page-blueprint.md "Section dividers", with one variant per divider graphic, height from Layout/divider-height, and decorative images with empty alt. Place one instance of each variant on Style Guide V2 to check them at all four breakpoints.

**You check:** six variants; each graphic fills the full width with no gap or seam at any breakpoint; heights are 96 / 72 / 48.
**Done when:** variants named by their transition (for example "Beige to Blue"); no stretched or cropped art.
**Lead looks at:** the dividers on the style guide page against the Figma screenshots.

## T08 V2 Navbar

**Prompt**

> Use the reo-dev-v2-build skill. Task T08: build the V2 Navbar component (group V2 Global) from home-page-blueprint.md "Nav bar" and Figma nodes 312:4653, 191:14328 and 191:17513, using the native Webflow Navbar and Dropdown elements with v2- classes on every part. Desktop shows links, Sign up and Book a demo; tablet shows Book a demo and the menu button; mobile shows the menu button. Leave dropdown panels empty. Put the .w--open styles in a scoped embed and log them. Place an instance on Style Guide V2 to test. Tell me the manual Designer steps I must do.

**You check:** set the Navbar's "Menu collapses at" to Tablet in the Designer (Claude cannot). Then: links fit on one line at 1280; the menu button appears at Tablet; opening the menu works in Preview.
**Done when:** every nav element carries a `v2-` class; hover and focus states exist; ledger updated; link targets listed in the log with the undefined ones marked.
**Lead looks at:** the bar at three widths; that no legacy navbar class is involved; open questions about sticky behaviour and dropdown content.

## T09 🔒 Home V2 page, shell, Hero

**Before:** the lead has approved creating the page.

**Prompt**

> Use the reo-dev-v2-build skill. Task T09: create the page "Home V2" (slug home-v2, draft, sitemap indexing off, SEO and Open Graph copied from the legacy Home page, no duplicateOf), build the page shell with V2 Global Styles and V2 Navbar, then build the Hero from home-page-blueprint.md section 1 and Figma nodes 191:12340, 191:14290 and 191:17486, including the V2 Feature Card component and the hero wave. Check all four breakpoints, verify page state, and write the session report.

**You check:** headline has the serif-italic first line; five tags; two buttons; three feature cards (one white panel on desktop, separate cards below); the wave only on desktop; intro centred on mobile only.
**Done when:** matches Figma at 1440, 768 and 390; one `<h1>`; page draft, indexing off; no legacy class; report written.
**Lead looks at:** the hero at three widths against Figma; page settings; SEO fields.

## T10 Trusted By

**Prompt**

> Use the reo-dev-v2-build skill. Task T10: on Home V2, add the "Beige to Blue" divider and then the Trusted By section from home-page-blueprint.md section 2 and Figma nodes 1:408, 191:14329 and 191:17514, then the divider below it. One column per category on desktop and tablet; each category becomes its own block with a 2 by 2 logo grid on mobile. Dashed grid lines, hover state on logo cells, alt text on every logo. Check all four breakpoints and write the session report.

**You check:** 16 logos in the right categories (table in the blueprint); grid lines meet cleanly with no doubled borders; hovering a cell turns it black; text is white without any manual colour classes.
**Done when:** matches Figma at three widths; section uses `v2-theme-brand`; linter clean.
**Lead looks at:** logo order per category; the mobile layout; border joins.

## T11 Product Demo

**Prompt**

> Use the reo-dev-v2-build skill. Task T11: on Home V2, add the Product Demo section from home-page-blueprint.md section 3 and Figma nodes 1:763, 191:14358 and 191:17550: the v2-browser frame with its bar and a media placeholder with a data-v2-video hook, 16 by 9, then the divider below. No video code. Check all four breakpoints and write the session report.

**You check:** a browser-style frame with dots, a URL pill reading "Reo.dev" and an empty media box; nothing overflows on mobile.
**Done when:** `v2-browser_*` classes are reusable (no section name in them); open question 5 is in the log.
**Lead looks at:** whether the placeholder size is acceptable until the video arrives.

## T12 The Problem

**Prompt**

> Use the reo-dev-v2-build skill. Task T12: on Home V2, add The Problem section from home-page-blueprint.md section 4 and Figma nodes 1:818, 191:14365 and 191:17557: section header, then the two showcases as exported images (one per breakpoint each) with the alt text from the blueprint and a bottom fade, then the divider below. Do not rebuild the product UI as elements. Check all four breakpoints and write the session report.

**You check:** the right image shows at each breakpoint and its small text is readable; only one image per showcase is visible at a time.
**Done when:** images are sharp at 2×; alt text set; white background via `v2-background-color-secondary`.
**Lead looks at:** image quality on a real screen; page weight added by the six images.

## T13 Testimonial

The longest card. If the session gets long, stop after the desktop layout and continue in a new session.

**Prompt**

> Use the reo-dev-v2-build skill. Task T13: on Home V2, add the Testimonial section from home-page-blueprint.md section 5 and Figma nodes 1:2354, 191:15492 and 367:7733, with dividers above and below. Use the native Webflow Tabs element with v2- classes; the card carries v2-theme-light. Tab 1 holds the designed story (logo, quote with highlighted phrase, two stats, portrait with caption); tabs 2 to 4 hold clearly marked placeholders. Style .w--current in a scoped embed and log it. On mobile keep the tab row scrollable above the card. Check all four breakpoints and write the session report.

**You check:** clicking tabs in Preview switches panes; the active tab is black with white text; the quote is dark grey on white, with the last phrase highlighted blue; stats read +200% and 40%; caption overlaps the portrait bottom-left.
**Done when:** matches Figma at three widths; no invented quotes; open questions 7 and 8 in the log; ledger updated.
**Lead looks at:** the card at all widths; decision on content source (static or CMS).

## T14 Take Reo Anywhere

**Prompt**

> Use the reo-dev-v2-build skill. Task T14: on Home V2, add the Take Reo Anywhere section from home-page-blueprint.md section 6 and Figma nodes 1:2740, 191:15844 and 634:3571, then the "Beige to Black" divider. Four integration cards (second one highlighted), four columns on desktop, two on tablet, a scroll-snap track on mobile. Hover state on cards. Check all four breakpoints and write the session report.

**You check:** four cards with the right icons and copy; the "In CRM" card is black with white text; cards scroll sideways on mobile without the page scrolling sideways.
**Done when:** no horizontal page overflow at any width; highlighted style implemented one way and recorded.
**Lead looks at:** mobile carousel feel; whether a pager is wanted.

## T15 Trust & Compliance

**Prompt**

> Use the reo-dev-v2-build skill. Task T15: on Home V2, add the Trust & Compliance section from home-page-blueprint.md section 7 and Figma nodes 1:2817, 191:15852 and 634:3743: heading without eyebrow, then an edge-to-edge scroll-snap track of five trust cards in desktop order with the GDPR card highlighted, and edge fades. Section uses v2-theme-dark. No autoplay. Check all four breakpoints and write the session report.

**You check:** five shields with correct labels; the GDPR card is blue with a white label pill; the track is centred and fades at both edges on desktop; no horizontal page overflow.
**Done when:** badges are SVG and crisp; alt text set; open question 12 in the log.
**Lead looks at:** behaviour decision (static scroll, marquee or slider).

## T16 V2 CTA Banner

**Prompt**

> Use the reo-dev-v2-build skill. Task T16: build the V2 CTA Banner component (group V2 Global) from home-page-blueprint.md section 8 and Figma nodes 1:3107, 191:15864 and 191:18120, with props for heading and both buttons, and place it on Home V2 after Trust & Compliance. The primary button is a plain v2-button and must render black through the brand theme. Check all four breakpoints and write the session report.

**You check:** heading is centred with the serif-italic phrase; "Book a demo" is black, "Try now" white; decorative stripes sit in the corners and never cover the text.
**Done when:** component props work (change the heading on the instance); decor is decorative (empty alt).
**Lead looks at:** the transition from the black section above into the blue banner.

## T17 V2 Footer

**Prompt**

> Use the reo-dev-v2-build skill. Task T17: build the V2 Footer component (group V2 Global) from home-page-blueprint.md section 9 and Figma nodes 90:3905, 191:15866 and 191:18122: newsletter text and social links, three link columns as real lists with the Figma labels as placeholders linked to "#", and the large "Reo.dev" wordmark as live decorative text with a gradient fill and bottom fade. Reset list styles in the list classes. Place it on Home V2. Check all four breakpoints and write the session report.

**You check:** three columns on desktop, two on tablet, one on mobile; links brighten on hover; the wordmark spans the width and is cropped at the bottom; no bullets or stray indents in the lists.
**Done when:** social links have aria-labels and real URLs from the legacy footer; open question 10 in the log.
**Lead looks at:** the real link list, the legal line and the newsletter decision.

## T18 ⏸ V2 Cookie Banner

**Before:** the lead has supplied a design or said to restyle the legacy banner's structure.

**Prompt**

> Use the reo-dev-v2-build skill. Task T18: read the legacy consent banner on the Home page (the fs-consent_component block and its fs-consent-element attributes) without changing it, then build a V2 Cookie Banner component (group V2 Global) with the same Finsweet Consent Pro attributes and v2- classes, following [the design / the lead's instructions]. Place it on Home V2 as the last element in v2-page-wrapper.

**You check:** on a review build, the banner appears on first visit, and accepting it lets analytics load.
**Done when:** every `fs-consent-element` attribute the legacy banner uses exists on the V2 one; no legacy `fs-consent_*` class is used.
**Lead looks at:** consent actually working end to end on staging.

## T19 Whole-page responsive and accessibility pass

**Prompt**

> Use the reo-dev-v2-build skill. Task T19: audit Home V2 without adding features. Check every section at 1440, 1200, 992, 768, 600, 390 and 360 for overflow, wrapping and spacing; run the accessibility checklist in home-page-blueprint.md; confirm heading order, alt text, link targets, focus states and that no element lacks a v2- class where it has text. Fix what you find with v2- classes, list what you fixed and what you could not, and run the linter with --list.

**You check:** drag the Designer canvas width slowly from wide to narrow; nothing jumps, overlaps or scrolls sideways.
**Done when:** the report lists each check with pass or fail; remaining failures have an owner.
**Lead looks at:** the fail list.

## T20 🔒 Review build QA

**Before:** the lead has asked for a review build and will publish it.

**Prompt**

> Use the reo-dev-v2-build skill. Task T20: prepare Home V2 for a review build as described in pages-and-launch.md "Review build": confirm sitemap indexing is off, set the page to non-draft only when I confirm the lead has asked, and tell me exactly which pages will be included in the next publish. Do not publish. After the lead publishes, check the staging URL in a real browser at four widths: fonts, hairlines, embeds, link hover, tabs, menu, carousels, consent banner, and the noindex meta tag. Report results.

**You check:** you can open the page on the staging domain; it looks like the Designer.
**Done when:** the noindex tag is present in the page source; every browser-only item (fonts, embeds, hover reset, tabs, menu) is confirmed or logged as a bug.
**Lead looks at:** the page on staging, then decides on the launch batch.

---

## After the home page

Other pages follow the same pattern: lead supplies the Figma node, Claude writes a short blueprint section for it first (sections, class trees, copy, assets, open questions), the lead skims it, then one card per section. Reuse `V2 Navbar`, `V2 Section Divider`, `V2 CTA Banner`, `V2 Footer`, the section-header pattern and `v2-browser_*` before creating anything new.
