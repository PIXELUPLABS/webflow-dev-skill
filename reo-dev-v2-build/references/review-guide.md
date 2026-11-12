# Daily review guide (for the lead)

A fifteen-minute routine for checking a day's work without reading every tool call. It relies on two things the skill makes Claude produce: a **session report** per task (`reo-dev/reports/`) and an up-to-date **build log** (`reo-dev/v2-build-log.md`).

If Claude is asked to help with a review, it follows this file too: it reports, it does not fix, unless told to.

## 1. Read the reports (3 min)

Open each new report in `reo-dev/reports/`. For each, check:

- **Task and status.** One task card per report. "Done" must be backed by the checks listed, not just stated.
- **Created.** Classes, components, variables, pages and assets are named. Vague lines ("built the section") are a miss: send it back.
- **Not verified.** There should almost always be something here before a review build (fonts, embeds, hover states and interactions cannot be confirmed in the Designer). An empty list on a section with tabs or embeds is a red flag.
- **Defaults taken.** Each references a question number from the blueprint.
- **Legacy touched.** Must say "None". Anything else: stop and look at it first.
- **Questions for you.** Answer them in the build log so the next session reads them.

## 2. Run the mechanical checks (3 min)

Ask Claude, in a fresh session:

> Use the reo-dev-v2-build skill in review mode. Change nothing. (1) Dump all styles and run scripts/lint_v2_names.py with --list. (2) List all pages whose slug ends in -v2 with draft state and sitemap status. (3) List V2 variable collections with variable counts, and the six legacy collections with theirs. (4) List components in groups starting with "V2" and confirm the legacy component count. (5) For Home V2, list every element that has no v2- class but has text, every legacy class in use, and every component instance. Report as tables.

What good looks like:

| Check | Expect |
|---|---|
| Linter | 0 violations. "Not in baseline and not v2" is empty, or only items your client's team made. "Legacy styles no longer present" is 0. |
| V2 class list | Grows by a believable amount per section (roughly 10–30). Folders match section names. No near-duplicates (`v2-hero_card` and `v2-hero_feature-card`), no `-2`, no one-off utilities with pixel values in the name. |
| Pages | Every `-v2` page is draft (or deliberately in review) with indexing off. No slug changed on a legacy page. |
| Variables | Legacy collections still 99 / 24 / 62 / 18 / 5 / 5 variables. V2 collections only changed if a report says so. |
| Components | V2 components named `V2 …` in `V2 Global`, `V2 Sections` or `V2 Elements`. Legacy components unchanged (85 on 2026-11-12, unless the client's team added some). |
| Home V2 | No legacy class, no legacy component, no classless text. |

## 3. Look at the page (7 min)

In the Designer, on the page worked on:

1. **Navigator.** The tree follows the skeleton: `v2-page-wrapper` → Global Styles → Navbar → `v2-main-wrapper` → sections and dividers → Footer. Sections follow `v2-section_x` → `v2-padding-global` → `v2-container-large` → `v2-padding-section-*` → `v2-x_component`. No "Div Block" names, no deep nests of unnamed wrappers.
2. **Four breakpoints.** Desktop, Tablet, Mobile L, Mobile. Compare with the Figma frames (1440, 768, 390). Then drag the canvas width between them; look for overflow and awkward wraps around 1200, 992 and 600.
3. **Style panel, on three random elements.** Values show as variables (purple pills), not raw numbers, except documented exceptions. Responsive changes come from variable modes, not per-breakpoint overrides on type sizes.
4. **Themes.** In blue and black sections, text is white without manual colour classes. The white testimonial card has dark text.
5. **Class reuse.** Click two similar things (two cards, two section headers). They share classes. A new class per instance is a smell.
6. **Selectors panel / Style Manager.** Filter by `v2-`. Skim for names that describe looks rather than role, or abbreviations.

Then, once a day, open **reo.dev** in a private window and click through three legacy pages. They must look exactly as before. This is the check that matters most.

## 4. Decide (2 min)

For each card: **accept**, **accept with fixes** (list them in the build log under the card), or **redo**. Then answer open questions and set tomorrow's cards.

## Red flags, in order of seriousness

1. Any change to a legacy style, tag style, variable, component, page or site code. Check the live site, then decide whether to restore from a backup (Site settings → Backups).
2. A `-v2` page that is not draft or has indexing on without your instruction.
3. Classes outside the naming rules, or legacy classes on a V2 page.
4. Raw hex or px values where a token exists; type sizes set per breakpoint on classes.
5. Invented content: quotes, statistics, logos, links or copy that are not in Figma.
6. Features nobody designed: entrance animations, extra hover effects, sticky behaviour.
7. A report that says "done" for something only checked at desktop, or only in a snapshot.
8. Hand edits in the Designer that are not in a report.
9. Custom code that is not in the ledger, or that selects elements by class name.
10. The same question asked twice: the answer is not reaching the log.

## Before a review build

- Every card for the pages in the build is accepted.
- `V2 Cookie Banner` is on each page.
- Indexing is off on each page (`get_page_sitemap_status`), and you know exactly which pages are non-draft: **all of them publish**.
- You publish, to the staging subdomain first. Then check the published page source for the `noindex` robots meta tag before sharing the URL.
- On staging, check what the Designer cannot show: fonts (weights, the serif accent), hairlines, link hover (no purple, no underline), embeds (`.w--current`, `.w--open`), tabs, menu, carousels, forms, consent.

## Weekly

- Backup: confirm a recent site backup exists before any larger change.
- Ask Claude for a ledger check: every embed and page-code block on V2 pages is in the custom-code ledger.
- Skim the V2 class list for consolidation candidates while it is still small.
- Update `home-page-blueprint.md` (or the blueprint for the page in progress) with every design answer you gave, so the next session does not ask again.
