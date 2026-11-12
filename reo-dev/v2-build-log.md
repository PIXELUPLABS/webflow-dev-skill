# Reo.dev V2 build log

Working record of the V2 build inside the live Reo.Dev Webflow project (`67e6b65ee328bc6b91324c9a`). Every session reads this first and updates it last. Keep it factual: what exists, what is half-done, what is waiting on someone.

**Last updated:** 2026-11-12 (read-only audit; skill written; nothing built in the live project yet)

## Status

| Phase | State | Notes |
|---|---|---|
| 0. Foundation (fonts, variables, global classes, global embed, style guide) | not started | Live project has no `V2 …` collections, no `v2-` classes, and only Inter + Geologica fonts (checked 2026-11-12) |
| 1. Shared components (Navbar, Footer, CTA Banner, Section Divider, Cookie Banner) | not started | |
| 2. Pages | not started | |
| 3. Launch batches | none | |
| 4. Cleanup | not started | |

## Ids created in Phase 0

| Thing | Name | Id |
|---|---|---|
| Collection | V2 Base | |
| Collection | V2 Theme | modes: Dark Mode `…`, Brand Mode `…` |
| Collection | V2 Typography | modes: Tablet `…`, Mobile Landscape `…` |
| Collection | V2 Layout | modes: Tablet `…`, Mobile Landscape `…` |
| Collection | V2 Sizes | |
| Font | Switzer 400 / 500 | |
| Font | Geist (variable) | |
| Font | Geist Mono 500 | |
| Font | Source Serif 4 600 italic (opsz) | |
| Component | V2 Global Styles | |
| Page | Style Guide V2 (`style-guide-v2`) | |

## Components

| Component | Group | Id | Props | Notes |
|---|---|---|---|---|

## Pages

| V2 page | Page id | Slug | Legacy twin (id) | Stage (building / review / launched) | Indexing | Notes |
|---|---|---|---|---|---|---|

## Legacy page audits

One block per rebuilt page: custom code, embeds, forms, ids, attributes, CMS lists, and the decision for each (carry over / rebuild / drop).

### Home (`67e6b65fe328bc6b91324d32`), audited 2026-11-12, not yet rebuilt

- Page head: `.fake-cursor` blink animation; `.lottie-control` play / pause button styles.
- Page footer: Lottie play / pause controller (`#hero-lottie`, `.lottie-control*`), prompt-card → `#chatbot-textarea` script, fake-cursor toggle. All select by class or id and are not null-safe.
- Structure: `page-wrapper is-home` → Global Styles, two navbar components (`Navbar Light (rewamped)`, `Navbar White (rewamped)`), `main-wrapper` with 8 sections separated by `section divider` components, `Footer`; page-level `fs-consent_component`.
- Decision: pending. The new hero design decides whether any of these scripts carry over.

## Custom-code ledger

Every class name and CSS custom property that appears in an embed, page code or site code. The cleanup rename does not touch code, so this list is what gets updated by hand.

| Where (component / page / location) | Feature | Class names used | CSS variables used | `data-v2-*` hooks |
|---|---|---|---|---|

## Styles not visible in the Style panel

Pseudo-elements, runtime-state CSS in embeds, anything a designer cannot see by clicking.

| Class | What | Where defined |
|---|---|---|

## CMS

| Collection | Template staging page | Bindings needed (element → field slug) | New fields requested | Lead OK |
|---|---|---|---|---|

## Launch batches

| Batch | Date | Pages | Inbound-link fix (repoint / 301) | Verified on production | Deferred |
|---|---|---|---|---|---|

## Open questions for the lead

| Question | Asked | Answer |
|---|---|---|
| Upload Switzer, Geist, Geist Mono and Source Serif 4 to the live project (Phase 0)? | 2026-11-12 | |
| CMS template pages cannot use the slug swap. OK to stage them on static `template-[slug]-v2` pages and move them into the real template at launch? | 2026-11-12 | |
| At each batch launch: repoint legacy navbar / footer links to the new pages, or add temporary 301s from `/[slug]-old`? | 2026-11-12 | |
| New pages stay **draft** while being built (so the client's routine publishes cannot ship half-built pages) and go non-draft for review. OK? | 2026-11-12 | |
| Which mobile hero option (Figma `638:447`–`638:552`, `633:447`)? | 2026-11-05 | |
| H3 / H4 tablet and mobile sizes are proposals (36/28 and 28/24). Confirm. | 2026-11-05 | |
| Is "Interactions with GSAP" enabled in Site settings? (No IX3 interactions exist yet.) | 2026-11-12 | |

## Deviations and incidents

Anything that did not follow the skill, and any write that touched something legacy. Exact call, time, and how it was resolved.

None. The 2026-11-12 session made no writes to the Webflow project.
