# Session report: [T00 Task name]

| | |
|---|---|
| Date | YYYY-MM-DD |
| Developer | |
| Task card | T00 … (from `home-build-plan.md`) |
| Page / component | e.g. Home V2 (`page id`) · section `v2-section_hero` |
| Figma nodes read | desktop `…` · tablet `…` · mobile `…` |
| Status | Done / Partly done / Blocked |

## What was built

Two or three sentences a reviewer can check against the page.

## Created

| Type | Name | Notes |
|---|---|---|
| Class | `v2-…` | new / reused |
| Combo | `v2-… is-…` | |
| Component | `V2 …` (group, id) | props |
| Variable | `V2 … / Group/name` | value per mode |
| Page | name, slug, id | draft, indexing |
| Asset | `v2-….svg` (id) | alt text |
| Custom code | where, what | in ledger: yes / no |

Reused without change: list the existing `v2-` classes and components this work relied on.

## Checks run

| Check | Result |
|---|---|
| Name linter (`lint_v2_names.py`) | 0 violations / list |
| Legacy classes on the page | none / list |
| Legacy components on the page | none / list |
| Text elements without a `v2-` class | none / list |
| Desktop (1440) vs Figma | match / differences |
| Tablet (768) vs Figma | match / differences |
| Mobile L and Mobile (390) vs Figma | match / differences |
| In-between widths (1200, 992, 600, 360) | no overflow / issues |
| Page state | draft: yes · sitemap indexing: off · slug ends `-v2` |
| Hover and focus states defined | yes / list missing |

## Not verified

What could not be confirmed in the Designer and needs a review build or a real browser (fonts, hairlines, embeds, runtime states, interactions, forms).

## Defaults taken on open design questions

| Question # (blueprint) | Default built |
|---|---|

## Deviations from Figma or from the skill

Anything built differently from the design or the rules, and why.

## Legacy touched

None. *(If anything other than "None": the exact tool call, what changed, and the current state.)*

## Manual steps for the developer

Things the MCP cannot do (for example: set the navbar collapse breakpoint, reload the Designer).

## Questions for the lead

| Question | Blocks |
|---|---|

## Next

The next card, and anything it needs first.
