# Reo.dev V2 build log

Working record of the V2 build inside the live Reo.Dev Webflow project (`67e6b65ee328bc6b91324c9a`). Every session reads this first and updates it last. Keep it factual: what exists, what is half-done, what is waiting on someone.

**Last updated:** YYYY-MM-DD by …

Session reports live in `reo-dev/reports/`, one file per task: `YYYY-MM-DD-[task].md` (template: `assets/session-report-template.md`).

## Status

| Phase | State | Notes |
|---|---|---|
| 0. Foundation (fonts, variables, global classes, global embed, style guide) | not started | |
| 1. Shared components (Navbar, Footer, CTA Banner, Section Divider, Cookie Banner) | not started | |
| 2. Pages | not started | |
| 3. Launch batches | none | |
| 4. Cleanup | not started | |

## Task cards

Copy the card list from `references/home-build-plan.md` (or the plan for the page in progress).

| Card | Task | State | Report | Lead review |
|---|---|---|---|---|

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

## Design questions

Numbered as in the page's blueprint. The default is what gets built until the lead answers.

| # | Question | Default being built | Answer |
|---|---|---|---|

## Deviations and incidents

Anything that did not follow the skill, and any write that touched something legacy. Exact call, time, and how it was resolved.
