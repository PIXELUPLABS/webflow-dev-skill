# Naming: Client-First V3 with the V2 namespace

Every name you create has to do two jobs: follow Client-First V3 so the build reads like any other Client-First site, and carry a marker that keeps it apart from the 3,494 legacy styles living in the same project. At the end of the project the legacy styles are deleted and the marker is stripped mechanically (see `cleanup-runbook.md`), so the marker must be **uniform** and **in one predictable place**.

## Why a prefix, and why on everything

The legacy build already owns almost every standard Client-First name: `page-wrapper`, `main-wrapper`, `padding-global`, `container-large`, `padding-section-large`, `heading-style-h1`–`h5`, `text-size-small`, `button`, `tag`, `hide`, `hide-tablet`, `text-rich-text`, `form_input`, `navbar_component`, `footer_component`, `section_cta`, `icon-1x1-small`, `max-width-large`, plus 191 `section_*` classes and 238 custom folders. Their values are purple-brand, Inter/Geologica, and sized for a fluid root font size. Reusing one drags the old design into a new page; editing one changes live pages.

A **prefix** (not a suffix) because:

- typing `v2-` in the Designer's class field lists only new classes, so nobody picks a legacy class by accident;
- it can be removed with one rule: delete the leading `v2-`;
- it keeps Client-First folders intact: `v2-hero_component` is folder `v2-hero`, and becomes folder `hero` after cleanup.

## The rules

| # | Rule |
|---|---|
| 1 | Every class that is **not** a combo starts with `v2-`. Global utilities, custom classes, section classes, style-guide classes: all of them. |
| 2 | After the prefix, the name is exactly what Client-First V3 would call it. `v2-` + `padding-global`, `v2-` + `hero_component`. |
| 3 | Combo classes start with `is-` and carry **no** prefix: `v2-button is-secondary`. They are scoped to their `v2-` base, so they need no marker and nothing to rename later. |
| 4 | A combo is never one of the **reserved names** below. |
| 5 | Lowercase letters, digits and hyphens only, with **one underscore at most** (custom classes: `folder_element`). No spaces, capitals, dots, `%`, `#` or brackets. |
| 6 | No abbreviations a new developer has to decode (`testimonial`, not `testi`; `comparison`, not `cmprsn`). No version words inside the name (`-new`, `-copy`, `-2`, `-final`, `-revamped`): the prefix is the only version marker. |
| 7 | Never create a class Webflow auto-named (`Div Block 3`, `Text Span`, `Heading 2`). If an element needs no styling, give it no class. |

Regex the linter enforces:

- non-combo: `^v2-[a-z0-9]+(-[a-z0-9]+)*(_[a-z0-9]+(-[a-z0-9]+)*)?$`
- combo: `^is-[a-z0-9]+(-[a-z0-9]+)*$`, and not reserved

### Reserved combo names

These nine exist in the legacy build as **standalone global classes** with their own styles. Webflow applies a global class's CSS to any element that carries the name, so using one as a combo on a V2 element leaks legacy styling into it:

`is-error` · `is-label` · `is-no` · `is-partial` · `is-reodev` · `is-section` · `is-value` · `is-warning` · `is-yes`

Use instead: `is-invalid` (form error), `is-caution` (warning), `is-positive` / `is-negative` (yes / no), `is-partly`, `is-field-label`, `is-highlighted`.

Also never use a legacy utility name as a combo on a V2 base (`hide`, `tag`, `flex`, `margin-0`, `text-weight-medium`, `text-color-white` …). The legacy build stacks utilities as combos; V2 does not. If you need a utility, apply the `v2-` utility class as an extra **global** class.

The legacy build also has a combo literally named `V2` (`.accordion-btn-line.v2`, `.about-courses-academy_accordian-content.v2`) and a component called `Button v2`. Both are legacy. They are unrelated to this namespace; leave them alone.

## Class types

### Global utility classes (no underscore)

`v2-[property]-[value]`. Reusable anywhere, one job each.

| Kind | Pattern | Examples |
|---|---|---|
| Page structure | fixed names | `v2-page-wrapper`, `v2-main-wrapper`, `v2-padding-global`, `v2-container-large` / `-medium` / `-small`, `v2-padding-section-large` / `-medium` / `-small` |
| Headings | `v2-heading-style-[h1–h6]`, `v2-heading-style-accent-[h1/h2]` | `v2-heading-style-h2`, `v2-heading-style-accent-h2` |
| Text | `v2-text-size-[size]`, `v2-text-style-[name]`, `v2-text-weight-[name]`, `v2-text-align-[side]`, `v2-text-color-[role]` | `v2-text-size-large`, `v2-text-style-mono`, `v2-text-color-secondary` |
| Backgrounds | `v2-background-color-[role]` | `v2-background-color-secondary` |
| Themes | `v2-theme-[mode]` | `v2-theme-dark`, `v2-theme-brand` |
| Spacing | `v2-margin-[side]-[size]`, `v2-padding-[side]-[size]`, `v2-gap-[size]`, `v2-spacer-[size]` | `v2-margin-bottom-small`, `v2-padding-vertical-large`, `v2-gap-medium`, `v2-spacer-xlarge` |
| Sizing | `v2-max-width-[size]`, `v2-icon-1x1-[size]`, `v2-icon-height-[size]`, `v2-aspect-ratio-[name]` | `v2-max-width-large`, `v2-icon-1x1-small` |
| Visibility | `v2-hide`, `v2-hide-tablet`, `v2-hide-mobile-landscape`, `v2-hide-mobile-portrait` | |
| Misc | `v2-overflow-hidden`, `v2-z-index-1`, `v2-pointer-events-none`, `v2-align-center`, `v2-button-group` | |
| Small global components | bare noun | `v2-button`, `v2-tag`, `v2-eyebrow`, `v2-link-button`, `v2-stat` |

Sides: `top`, `bottom`, `left`, `right`, `horizontal`, `vertical`. Sizes come from the spacing scale in `v2-foundation.md` (`xxtiny` … `xxhuge`); a spacing class binds to the token of the same name. Spacing is **one class per side and size** (`v2-margin-bottom-small`), not the legacy two-class combo (`margin-bottom` + `margin-small`).

Create a utility **when a section first needs it**, not in bulk. A utility that is never used is a class someone has to audit later.

### Custom classes (one underscore)

`v2-[folder]_[element]`. The folder is the component or section the class belongs to; the element says what it is inside that folder.

```text
v2-hero_component        v2-hero_content        v2-hero_heading-wrapper
v2-hero_media            v2-hero_logo-row       v2-hero_logo
v2-navbar_component      v2-navbar_menu         v2-navbar_link        v2-navbar_dropdown-list
v2-footer_component      v2-footer_column       v2-footer_link-list   v2-footer_legal
v2-trust_card            v2-trust_card-icon     v2-trust_card-title
```

- The outermost custom element of a section is always `v2-[folder]_component`.
- Describe role, not looks: `v2-pricing_card-highlight`, not `v2-pricing_blue-box`.
- Use a hyphen for a sub-part (`v2-trust_card-icon`), never a second underscore.
- A class used by two or more unrelated sections is not custom: promote it to a global component folder (`v2-card_…`, `v2-form_…`, `v2-slider_…`, `v2-tabs_…`, `v2-accordion_…`, `v2-modal_…`).
- Page-specific folders take the page name only when the section name alone would be ambiguous: `v2-pricing-faq_item` vs `v2-faq_item` (global).

### Section classes

`v2-section_[name]`, one per section, on the `<section>` element. It carries the section's background, theme and anything unique to it. Name by content, in the singular, matching the Figma section name: `v2-section_hero`, `v2-section_trusted-by`, `v2-section_product-demo`, `v2-section_problem`, `v2-section_testimonial`, `v2-section_integrations`, `v2-section_trust`, `v2-section_cta`.

When the same section type appears on several pages with different content, add the page as a prefix inside the name: `v2-section_pricing-hero`, `v2-section_blog-hero`. If it is truly identical, it should be a component with one class.

### Combo classes

`is-[state-or-variant]` on a `v2-` base.

```text
v2-button is-secondary     v2-button is-dark        v2-button is-light      v2-button is-small
v2-eyebrow is-inverse      v2-navbar_link is-active v2-trust_card is-wide   v2-hero_media is-mobile
```

- A combo only **changes** its base. If it would restyle more than a few properties, it is a different component: make a new class.
- Webflow's combo CSS is not chain-scoped: `.v2-button.is-alternate` also matches an element with `v2-button is-text is-alternate`. Do not reuse one combo name for two different meanings on the same base. Use distinct names (`is-on-dark`, `is-on-brand`).
- Maximum two combos on one element. Three means the base is doing too much.
- Runtime state classes that Webflow adds (`w--current`, `w--open`, `w--active`) cannot be created through the MCP (names starting with `w-` are sanitised). Style them in a scoped `<style>` embed inside the component, or in the Designer, and log it.

### Style-guide-only classes

`v2-styleguide_[element]` (`v2-styleguide_swatch`, `v2-styleguide_row`). Only on the `style-guide-v2` page. The legacy style guide uses `rl-styleguide_*`; leave it.

### Third-party prefixes

Finsweet and library classes keep their vendor prefix **after** ours only when the library lets you choose the class: `v2-swiper_wrapper`, `v2-swiper_slide` (Swiper accepts custom `wrapperClass` / `slideClass`). Never create bare `swiper`, `swiper-wrapper`, `swiper-slide`, `fs-*` or `ms-*` classes: the legacy build already has them with its own styling. For Finsweet, use **attributes** (`fs-list-element`, `fs-consent-element`), which need no class.

## Variables

| Thing | Convention | Example |
|---|---|---|
| Collections | `V2 ` + Client-First V3 collection name | `V2 Base`, `V2 Theme`, `V2 Typography`, `V2 Layout`, `V2 Sizes` |
| Modes | plain names | `Dark Mode`, `Brand Mode`, `Tablet`, `Mobile Landscape` |
| Variables | `Group/name`, **no** marker | `Brand/blue-500`, `Background/primary`, `H2/font-size`, `Spacing/large`, `Container/large` |

The collection name is part of the generated CSS custom property (legacy example: `--_primitives---base-color-grey--900`), so prefixing the collection is enough to keep every V2 property unique. Never predict a CSS name: read `cssName` back from `query_variables` after creating the variable. If you must write `var(--…)` in an embed, log it, because renaming the collection at cleanup changes the name.

Do not add variables to legacy collections, and do not create a V2 collection called just `Theme`: a collection with that name already exists.

## Components

| Thing | Convention | Example |
|---|---|---|
| Name | `V2 ` + Title Case noun | `V2 Navbar`, `V2 Footer`, `V2 CTA Banner`, `V2 Section Divider`, `V2 Cookie Banner`, `V2 Global Styles`, `V2 Feature Card` |
| Group | `V2 Global` (on every page) · `V2 Sections` (whole sections) · `V2 Elements` (cards, items, small UI) | |
| Properties | Title Case, by content | `Heading`, `Body`, `Button Text`, `Button Link`, `Image`, `Show Eyebrow` |
| Variants | Title Case | `Base`, `On Dark`, `On Brand`, `Compact` |

The marker is in the **name**, not only the group, because the legacy build has components called `Footer`, `Button`, `Nav`, `Banner` and `Badge`, and `get_component` by name must never be ambiguous. Never name a V2 component the same as a legacy one minus the prefix and then look it up by the short name.

## Pages and folders

| Thing | Convention | Example |
|---|---|---|
| Page name | legacy name + ` V2` | `Home V2`, `Book a Demo V2`, `Integrations V2` |
| Slug | live slug + `-v2`; home is `home-v2` | `/book-a-demo` → `/book-a-demo-v2` |
| Nested page | same folder as the legacy page, slug + `-v2` | `/devgtm-academy/about` → `/devgtm-academy/about-v2` |
| Brand-new page (no legacy twin) | the final slug + `-v2` until launch | `/platform-v2` |
| CMS template staging page | `template-[collection-slug]-v2` | `template-blog-v2`, `template-customer-stories-v2` |
| Style guide | `style-guide-v2` (stays draft) | |

Details and the launch swap are in `pages-and-launch.md`.

## Element ids, attributes, assets, interactions

| Thing | Convention | Example |
|---|---|---|
| Element id (anchors, `aria-controls`) | kebab-case, no marker, unique on the page; reuse the legacy id when an anchor link or a script already depends on it | `pricing`, `faq`, `hero-lottie` |
| Script hooks | `data-v2-[feature]` attributes | `data-v2-slider="testimonials"`, `data-v2-tab-trigger` |
| Navigator display names | plain language, no marker | `Hero`, `Logo grid`, `Card: SOC 2` |
| Assets | `v2-[section]-[what]` + size or theme when relevant; SVG for icons and dividers | `v2-hero-product-ui.webp`, `v2-divider-beige-blue.svg`, `v2-icon-sparkle.svg` |
| Asset folder | `V2` at the root of the Assets panel, sub-folders by section | `V2 / Hero` |
| Interactions (IX3) | `V2 / [Component or Page] / [what it does]`; scope is always `component` or `pages`, **never `site`** | `V2 / Navbar / Open menu` |
| Embeds | open and close with `<!-- START: v2-[feature] -->` / `<!-- END: v2-[feature] -->` | |

`data-v2-*` hooks do not need renaming at cleanup; they can stay or be renamed in one search-and-replace.

## Before / after

| Do not | Do |
|---|---|
| `button` (legacy, purple) | `v2-button` |
| `button is-secondary` | `v2-button is-secondary` |
| `section_hero-home` | `v2-section_hero` |
| `hero-new_wrap`, `cta-new_bg` | `v2-hero_content`, `v2-cta_background` |
| `margin-bottom margin-small` | `v2-margin-bottom-small` |
| `text-color-grey-600` | `v2-text-color-secondary` (semantic role, not a palette step) |
| `v2-hero_content_wrapper_inner` | `v2-hero_content-inner` |
| `v2-Hero_Component`, `v2-hero component` | `v2-hero_component` |
| `v2-button-2`, `v2-card-copy` | name the difference: `v2-button is-small`, `v2-card_compact` |
| `v2-form_input is-error` | `v2-form_input is-invalid` |
| `hero_component-v2`, `v2_hero_component`, `V2-hero_component` | `v2-hero_component` |
| component `Navbar` in group `V2` | component `V2 Navbar` in group `V2 Global` |

## Deciding what a new class should be

1. Is there already a `v2-` class that does this? (`query_styles` with `name_path: ["v2-"]` and the property you need.) → reuse it.
2. Is it a single reusable property (a spacing, a text size, a color role)? → global utility.
3. Is it a variant or state of an existing `v2-` class? → `is-` combo.
4. Will the same structure appear in more than one section or page? → global component folder (`v2-card_…`), and probably a Webflow component.
5. Otherwise → custom class in the section's folder (`v2-[section]_[element]`).

If you are about to create a class and step 1 was skipped, stop and run it.
