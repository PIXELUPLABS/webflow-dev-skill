# Reo.dev V2 build log

Working record of the V2 build inside the live Reo.Dev Webflow project (`67e6b65ee328bc6b91324c9a`). Every session reads this first and updates it last. Keep it factual: what exists, what is half-done, what is waiting on someone.

**Last updated:** 2026-11-12 (read-only audit of the Webflow project and of the Figma home page section; skill, home page blueprint and task cards written; nothing built in the live project yet)

Session reports live in [reports/](reports/), one file per task: `YYYY-MM-DD-[task].md`.

## Status

| Phase | State | Notes |
|---|---|---|
| 0. Foundation (fonts, variables, global classes, global embed, style guide) | not started | Live project has no `V2 …` collections, no `v2-` classes, and only Inter + Geologica fonts (checked 2026-11-12) |
| 1. Shared components (Navbar, Footer, CTA Banner, Section Divider, Cookie Banner) | not started | Cookie Banner is blocked: no V2 design |
| 2. Pages | not started | Home V2 is planned in the skill (`home-page-blueprint.md`, cards T00–T20 in `home-build-plan.md`) |
| 3. Launch batches | none | |
| 4. Cleanup | not started | |

## Home page task cards

| Card | Task | State | Report | Lead review |
|---|---|---|---|---|
| T00 | Environment check | not started | | |
| T01 | Fonts (needs lead OK) | not started | | |
| T02 | Variables | not started | | |
| T03 | Shell, structure and typography classes | not started | | |
| T04 | Component classes and V2 Global Styles | not started | | |
| T05 | Style Guide V2 page (needs lead OK) | not started | | |
| T06 | Asset export and upload | not started | | |
| T07 | V2 Section Divider | not started | | |
| T08 | V2 Navbar | not started | | |
| T09 | Home V2 page, shell, Hero (needs lead OK) | not started | | |
| T10 | Trusted By | not started | | |
| T11 | Product Demo | not started | | |
| T12 | The Problem | not started | | |
| T13 | Testimonial | not started | | |
| T14 | Take Reo Anywhere | not started | | |
| T15 | Trust & Compliance | not started | | |
| T16 | V2 CTA Banner | not started | | |
| T17 | V2 Footer | not started | | |
| T18 | V2 Cookie Banner | blocked on design | | |
| T19 | Whole-page responsive and accessibility pass | not started | | |
| T20 | Review build QA (needs lead OK) | not started | | |

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
| H3 / H4 tablet and mobile sizes are proposals (36/28 and 28/24); the home page does not use H3 or H4. Confirm when a page needs them. | 2026-11-05 | |
| Is "Interactions with GSAP" enabled in Site settings? (No IX3 interactions exist yet.) | 2026-11-12 | |

## Home page design questions (from the Figma read, 2026-11-12)

Numbers match "Open design questions" in the skill's `home-page-blueprint.md`. The default is what gets built until the lead answers.

| # | Question | Default being built | Answer |
|---|---|---|---|
| 1 | Product Demo, The Problem and Take Reo Anywhere have different backgrounds on desktop than on tablet and mobile. Which is right? | Desktop backgrounds everywhere (beige, white, beige) |**Desktop wins** at every breakpoint (lead, 2026-11-12) |
| 2 | Tablet and mobile dividers are placeholders, and add dividers around the CTA that desktop does not have. | Reuse the six desktop dividers at every breakpoint | |
| 3 | Testimonial, Take Reo Anywhere and Trust & Compliance each have two mobile versions. | The newer loose frames (`367:7733`, `634:3571`, `634:3743`) | |
| 4 | Nav: sticky, fixed or static? Where are the dropdown panels and the open mobile menu designed? | Static; empty dropdown panels | |
| 5 | Product Demo: what is the media (video URL, host, autoplay, poster)? | Browser frame with an empty 16:9 media box | |
| 6 | The Problem showcases: static images, or an interactive Signals / GTM Agents module? | Static images per breakpoint | |
| 7 | Testimonial content: real stories for Aembit, NVIDIA, Databricks, Salesforce? The designed one mixes Aembit and DataHub. Static or CMS? | The designed story in tab 1, placeholders in tabs 2–4 | |
| 8 | Testimonial tabs on mobile are not designed. | Scrollable tab row above the card | |
| 9 | Desktop bottom padding is 180 on sections 6 and 7, and 100 on The Problem. Intended? | Token values (120) | |
| 10 | Footer: real link list (Figma has placeholder copy from another product), legal / copyright line, and does the newsletter need an email field? | Figma labels as placeholders linked to `#`; no form | |
| 11 | Hero feature cards: one white panel on desktop, separate bordered cards on tablet and mobile. Body copy looks like draft text. | As drawn per breakpoint; copy verbatim | |
| 12 | Trust cards: order differs per breakpoint; marquee, slider or static? | Centred scroll-snap track, desktop order, no autoplay | |
| 13 | "world-class" (desktop) or "world class" (tablet, mobile)? | world-class | |
| 14 | Where desktop frames and Figma components disagree on small values, which wins? | Component for styling, desktop frame for layout | |
| 15 | Cookie banner has no V2 design. | Blocked; no review build without it | |
| 16 | Link targets for nav items, "Try now", "Sign up" and the feature-card links are not in Figma. | `/book-a-demo` for Book a demo; `#` for the rest | |

## Deviations and incidents

Anything that did not follow the skill, and any write that touched something legacy. Exact call, time, and how it was resolved.

None. The 2026-11-12 session made no writes to the Webflow project.
