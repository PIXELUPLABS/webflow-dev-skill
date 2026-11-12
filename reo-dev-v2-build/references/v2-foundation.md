# V2 foundation: tokens, fonts, global classes, page shell

The design system for the new Reo.dev, mapped from the Figma file `GuQCrycX2KDwenWDwW7FIT` (section "Final LP", `1:285`; desktop frame `1:286` at 1440, tablet `191:14289` at 768, mobile `191:17485` at 390). The Figma file has its own variable collections (`lp/*` semantic colors, Typography and Spacing & Layout with Desktop / Tablet / Mobile modes), and the values below come from those tokens.

**Status on 2026-11-12: nothing in this file exists in the live project yet.** These values were first built and checked on a separate Client-First V3 prototype site that the current Webflow connection cannot reach. Phase 0 recreates them here, in the `V2` namespace. Any variable or font id from that prototype (for example in `reo-dev/reference/variables.md`) is **invalid on this site**: always take ids from the tool that created the thing.

The values the home page uses were re-checked against the Figma variables of that section on 2026-11-12 and match: brand blue, beige, the black and white alpha steps, H1, H2, H6, body, label, tag, mono, stat and large-text styles, and the padding, section and gap rhythm at all three breakpoints. Values the home page does not show (hover and pressed blues, blue-100, H3–H5, the gutter token) come from the prototype and could not be re-checked from this section. The Figma file also carries a few near-duplicate values (noted where they matter), and the status colours listed as "Others" are not used on the home page.

Once Phase 0 is done, Webflow is the source of truth. Confirm a value with `data_variable_tool` / `query_styles` before relying on this file, and record deliberate changes in the build log.

## How the system works

- **rem, with a fixed root.** V2 pages have no fluid `html` font size, so 1rem = 16px at every width. Enter sizes in rem (px ÷ 16).
- **Responsive by variable mode.** `V2 Typography` and `V2 Layout` have Desktop, Tablet and Mobile Landscape modes. `v2-page-wrapper` switches them: Tablet at `medium` (≤991), Mobile Landscape at `small` (≤767; ≤479 inherits it). Figma Tablet (768) maps to Tablet and Figma Mobile (390) to Mobile Landscape. Never add per-breakpoint font sizes to a class: change the variable.
- **Themes by variable mode.** `V2 Theme` has Base (light), Dark Mode and Brand Mode. `v2-theme-dark` / `v2-theme-brand` on a section wrapper switch text, borders, links, tags, outline buttons and focus rings together.
- **Scoped to V2 pages.** Modes hang on `v2-page-wrapper`, never on `body`. The `body` tag style belongs to the legacy site.

## Phase 0 order

Work top to bottom. Each step is additive and safe for the live site, but confirm the two marked steps with the lead first.

1. **Fonts** *(lead's OK first: adds files to the live project)*
2. **Variable collections and modes**, then variables, then non-base mode values
3. **Shell classes** (`v2-page-wrapper`, `v2-main-wrapper`, structure classes) and the mode bindings on `v2-page-wrapper`
4. **Typography, color, theme and component classes**
5. **`V2 Global Styles` component** (embed)
6. **`style-guide-v2` page** *(lead's OK first: creates a page)*: draft, indexing off; shows the palette, every type style at its three sizes, buttons, small components and both themes
7. **Verify** on the style guide page, run the linter, write ids to the build log

Keep every create batch small (10 or fewer actions) and re-query after each batch: a batch of variable creates once ran twice on the server and left `…-2` twins. After creating variables, run `query_variables` with name `-2` inside the V2 collections and delete only twins you created.

## Fonts

| Role | Family | Weights | Variable | Source |
|---|---|---|---|---|
| Display / headings | Switzer | 400, 500 | `Font Family/heading` = `Switzer, Arial, sans-serif` | Fontshare (ITF Free Font License), full character set, two static files |
| Body, labels, stats | Geist | 400, 500 | `Font Family/body` = `Geist, Arial, sans-serif` | Google Fonts (OFL), one variable file, `wght` 100–900, latin subset |
| Accent (serif italic inside headings) | Source Serif 4 | 600 italic | `Font Family/accent` = `"Source Serif 4", Georgia, serif` | Google Fonts (OFL), variable **`opsz` 8–60**, latin subset |
| Mono (eyebrows, indexes, link buttons) | Geist Mono | 500 | `Font Family/mono` = `"Geist Mono", "Courier New", monospace` | Google Fonts (OFL), latin subset |

The site currently has only Inter and Geologica. Upload the four families as self-hosted **WOFF2** with `font-display: swap`.

- Source Serif 4 must keep its optical-size axis (request `ital,opsz,wght@1,8..60,600`). The fixed instance renders the large accent headings heavier than Figma and the letters collide at −4% tracking.
- The latin subset covers English, punctuation, € and ™. Characters outside it (→ U+2192, Polish or Turkish letters) fall back to Arial or Georgia. If migrated content needs them, add Google's latin-ext files as extra faces.
- Family names in the font records must match the variable stacks exactly.

Upload flow:

1. Get the files. Fontshare: `https://api.fontshare.com/v2/css?f[]=switzer@400,500` returns WOFF2 URLs (it also appends an unrelated "Erode" face; ignore it). Google: request the CSS2 API with a current Chrome user agent and take the `latin` block's WOFF2 URL.
2. Inspect each file: `node scripts/woff2info.mjs <file.woff2>` prints the weight class, axes and names.
3. `data_fonts_tool` → `create_font` with `file_name`, `file_hash` (MD5 hex of the bytes), `font_family`, `weight`, `italic`, `font_display: "swap"`, and `axes` for variable files. The response contains an `upload` object.
4. Save that `upload` object as JSON and run `python3 scripts/upload_font.py <upload.json> <file.woff2>`. It POSTs every `upload.fields` entry plus the file. Success is HTTP **201**.
5. `list_fonts` to confirm the four families, then record the font ids in the build log.

Font stacks sit inside the font family variables so pages stay readable before the fonts load. FontFamily variables reject `custom_value`; pass the whole stack as `static_value`. The heading and body stacks are the ones verified on the prototype; the accent and mono fallbacks (`Georgia, serif` and `"Courier New", monospace`) are suggestions, so check that the stack is accepted and renders before moving on.

## Variable collections

Create five collections. Collection names carry the marker; variable names do not.

| Collection | Modes |
|---|---|
| `V2 Base` | base only |
| `V2 Theme` | base (light) · `Dark Mode` · `Brand Mode` |
| `V2 Typography` | base (Desktop) · `Tablet` · `Mobile Landscape` |
| `V2 Layout` | base (Desktop) · `Tablet` · `Mobile Landscape` |
| `V2 Sizes` | base only |

Create modes **without** `breakpoint_id` (auto-binding a second collection to breakpoints has failed with a "style block store" conflict). Bind them on `v2-page-wrapper` instead (see Shell).

Writing values: to write the base mode, **omit `mode_id`** (passing `"base"` fails). New variables in a multi-mode collection come back with empty `modeValues`: set every non-base mode explicitly, do not trust inheritance.

### V2 Base (primitives)

| Variable | Value | Figma |
|---|---|---|
| Brand/blue-100 | `#f1f5fe` | `blue/100`, surface/brand-subtle |
| Brand/blue-500 | `#1d39f5` | `blue/500`: action/primary, text/brand, border/focus |
| Brand/blue-600 | `#1529cf` | `blue/600`: primary hover |
| Brand/blue-700 | `#0f22a5` | `blue/700`: primary pressed |
| Neutral/white | `#ffffff` | |
| Neutral/black | `#000000` | |
| Neutral/transparent | `transparent` | |
| Neutral/neutral-100 | `#f3f3f1` | page beige, surface/muted |
| Neutral/neutral-300 | `#d9d9d6` | action/disabled |
| Neutral/neutral-600 | `#616160` | |
| Neutral/neutral-900 | `#313131` | border/raised-inverse. The Figma `Reo/Trust Card` component uses `#343330`; treat as the same token |
| Neutral/neutral-950 | `#171717` | surface/raised-inverse. The Figma `Reo/Trust Card` component uses `#18181b`; treat as the same token |
| Black Alpha/black-80, -60, -55, -43, -20, -10 | `rgba(0,0,0,0.80)` … `0.10` | text primary, body, secondary, tertiary; border strong, subtle |
| White Alpha/white-80, -74, -20, -10 | `rgba(255,255,255,0.80)` … `0.10` | inverse body, inverse secondary; inverse borders |
| Others/green, yellow, red (`-light`, `-dark`) | not needed for the home page | success, warning, error. Create them only when a page first needs them, reading the hex from that page's Figma node; do not guess. The only green on the home page is `#05773b`, inside exported testimonial art. |
| Font Family/heading, body, accent, mono | stacks above | |
| Font Weight/normal, medium, semi-bold | 400, 500, 600 | |
| Letter Spacing/tightest, tighter, default, wide, wider, widest | −0.04em, −0.02em, 0, 0.01em, 0.03em, 0.04em | |

### V2 Theme (semantic), per mode

Values are references to `V2 Base` variables (`existing_variable_id`), not hex.

| Variable | Base (light) | Dark Mode | Brand Mode |
|---|---|---|---|
| Background/primary | neutral-100 | black | blue-500 |
| Background/secondary | white | neutral-950 | blue-600 |
| Background/tertiary | blue-500 | blue-500 | white |
| Background/alternate | black | neutral-100 | black |
| Background/raised | white | neutral-950 | white-10 |
| Background/brand-subtle | blue-100 | white-10 | white-10 |
| Text/primary | black-80 | white | white |
| Text/secondary | black-60 | white-80 | white-80 |
| Text/muted | black-55 | white-74 | white-74 |
| Text/tertiary | black-43 | white-74 | white-74 |
| Text/brand | blue-500 | blue-500 | white |
| Text/alternate | white | black-80 | white |
| Border/primary | black-20 | white-20 | white-20 |
| Border/secondary | black-10 | white-10 | white-10 |
| Border/brand | blue-500 | blue-500 | white |
| Border/raised | black-10 | neutral-900 | white-20 |
| Link/primary | blue-500 | white | white |
| Link/secondary | black-80 | white-80 | white-80 |
| Button Primary/background | blue-500 | blue-500 | **black** |
| Button Primary/background-hover | blue-600 | blue-600 | blue-600 |
| Button Primary/background-pressed | blue-700 | blue-700 | blue-700 |
| Button Primary/text | white | white | white |
| Button Secondary/background | transparent | transparent | transparent |
| Button Secondary/text | black-80 | white | white |
| System/focus-state | blue-500 | white | white |
| System/focus-inner | white | black | blue-500 |

**Naming note.** `Text/secondary` holds Figma's `text/body` (60%), the most common paragraph color, so `v2-text-color-secondary` is the paragraph class. Figma's own `text/secondary` (55%) is `Text/muted`.

### V2 Typography

Sizes in px as Desktop / Tablet / Mobile Landscape (store as rem). Line heights are stored as **unitless ratios** that reproduce Figma's px (line height ÷ font size, e.g. 92 ÷ 84 = 1.0952).

| Variable group | Font size | Line height (px) | Weight | Letter spacing |
|---|---|---|---|---|
| H1 | 84 / 72 / 48 | 92 / 80 / 56 | medium | tightest |
| H2 | 64 / 48 / 36 | 72 / 56 / 44 | normal | tightest |
| H3 | 40 / 36 / 28 | 49 / 43 / 34 | medium | tightest |
| H4 | 32 / 28 / 24 | 38 / 34 / 29 | medium | tightest |
| H5 | 24 / 24 / 20 | 32 / 32 / 28 | medium | tighter |
| H6 | 20 / 20 / 20 | 28 / 28 / 24 | medium | tighter |
| Accent XL (with H1) | 96 / 84 / 60 | line box equals H1's: 92 / 80 / 56 | semi-bold italic | tightest |
| Accent LG (with H2) | 76 / 60 / 48 | line box equals H2's: 72 / 56 / 44 | semi-bold italic | tightest |
| Body | 16 | 20 | normal | tighter |
| Font Size + Line Height / large | 24 / 20 / 20 | 36 / 32 / 28 | | |
| … / medium | 20 | 26 | | |
| … / regular | 16 | 24 | | |
| … / small | 12 | 16 | | |
| … / tiny | 10 | 13 | | |
| Stat | 56 / 52 / 40 | 64 / 60 / 48 | medium | tightest |
| Caption | 16 / 16 / 12 | 26 / 26 / 19 | normal | tighter |

Each heading group has four variables: `H1/font-size`, `H1/line-height`, `H1/font-weight`, `H1/letter-spacing` (weight and spacing reference `V2 Base`). The H3 and H4 tablet and mobile values are proposals: Figma defines desktop only. Confirm with the lead before treating them as final.

### V2 Layout

| Variable | Desktop / Tablet / Mobile | Figma |
|---|---|---|
| Spacing/none, xxtiny, xtiny, tiny, xxsmall, xsmall, small, medium, large, xlarge, xxlarge, huge, xhuge, xxhuge | 0, 4, 8, 12, 16, 20, 24, 32, 48, 64, 80, 96, 120, 160 px, **constant** | space scale (does not change by breakpoint) |
| Spacing/global-padding | 80 / 40 / 24 | `layout/margin-x` |
| Section Padding/large | 120 / 96 / 64 | `layout/section-y` |
| Section Padding/medium | 80 / 64 / 48 | |
| Section Padding/small | 48 / 40 / 32 | |
| Layout/section-gap | 80 / 64 / 48 | header-to-content gap |
| Layout/gutter | 20 / 24 / 18 | grid gutters |
| Layout/card-gap | 20 | card grids |
| Layout/divider-height | 96 / 72 / 48 | section dividers |

The Figma 6px and 40px spaces have no token. Use a Layout token or a local value in a custom class.

### V2 Sizes

| Variable | Value |
|---|---|
| Container/large | 1280px (80rem): 1440 minus 2 × 80 margin |
| Container/medium, small | define from Figma when a page first needs them |
| Border Radius/medium | 12px. Buttons, tags and cards are **square** (radius 0) |
| Icon/small, medium, large | 16, 20, 40px |
| Focus/width, offset | 2px, 2px |

## Shell and structure classes

| Class | Properties |
|---|---|
| `v2-page-wrapper` | `background-color: Background/primary` · `color: Text/primary` · `font-family: Font Family/body` · `font-size`, `line-height`, `font-weight`, `letter-spacing` from the Body variables · `min-height: 100vh` · `overflow: clip` only if a section needs it. **Variable modes:** at `medium` → `V2 Typography` Tablet + `V2 Layout` Tablet; at `small` → both Mobile Landscape (`set_style_variable_mode` with `breakpoint_id`) |
| `v2-main-wrapper` | none needed; on the `<main>` tag |
| `v2-padding-global` | `padding-left` / `padding-right`: Spacing/global-padding |
| `v2-container-large` (`-medium`, `-small`) | `width: 100%` · `max-width`: Container/* · `margin-left` / `margin-right: auto` |
| `v2-padding-section-large` (`-medium`, `-small`) | `padding-top` / `padding-bottom`: Section Padding/* |
| `v2-theme-dark` | `background-color: Background/primary` · `color: Text/primary` · Theme mode → Dark Mode (`set_style_variable_mode`, no breakpoint) |
| `v2-theme-brand` | same, Theme mode → Brand Mode |
| `v2-theme-light` | `background-color: Background/secondary` · `color: Text/primary` · Theme mode → **base (light)**. For a light card inside a blue or black section (the testimonial card). |

**Check `v2-theme-light` when you create it.** Setting a nested element back to the base mode has not been tested on this project. Build a small test: a `v2-theme-light` block with a `v2-text-color-primary` text inside a `v2-theme-brand` block; the text must be dark. If the base mode cannot be selected with `set_style_variable_mode`, add a third mode `Light Mode` to `V2 Theme` with the same values as base, point `v2-theme-light` at it, and record that in the build log.

`v2-page-wrapper` exists to override the legacy `body` tag style, which sets a different background, font, color and size on every page of this project. Do not rely on anything inheriting from `body`.

## Typography classes

Every text class sets **all** of family, size, line height, weight and letter spacing, and headings also set `margin-top: 0` and `margin-bottom: 0`. The legacy heading tag styles (Geologica, `letter-spacing: -2px` on `h2`, default margins on `h4` / `h5`) apply to any property a V2 class leaves out.

| Class | Figma style | Uses |
|---|---|---|
| `v2-heading-style-h1` | Display/84 Medium | H1 variables, Switzer |
| `v2-heading-style-accent-h1` (span) | Accent/96 | Accent XL, Source Serif 4 600 italic |
| `v2-heading-style-h2` | Display/64 Regular | H2 variables |
| `v2-heading-style-accent-h2` (span) | Accent/76 | Accent LG |
| `v2-heading-style-h3` | Display/40 Medium | H3 |
| `v2-heading-style-h4` | Heading/32 Medium | H4 |
| `v2-heading-style-h5` | Heading/24 Medium | H5 |
| `v2-heading-style-h6` | Heading/20 Medium (card titles) | H6 |
| `v2-text-size-large` | Body/24 | 24/36 · 20/32 · 20/28 |
| `v2-text-size-medium` | Body/20 | 20/26 |
| `v2-text-size-regular` | Body/16 long-form | 16/24 |
| `v2-text-size-small` | Body/12 | 12/16 |
| `v2-text-size-tiny` | product-UI micro text | 10/13 |
| `v2-text-style-label` | Label/16 | Geist 500, 16/20, spacing 0 |
| `v2-text-style-label-caps` | Label/16 Caps (button text, tabs, stat labels) | Geist 500, 16/16, +4%, uppercase |
| `v2-text-style-tag` | Label/12 Caps | Geist 500, 12/15.6, +3%, uppercase |
| `v2-text-style-mono` | Mono/12 Caps (eyebrows, indexes, link buttons) | Geist Mono 500, 12/16, +1%, uppercase |
| `v2-text-style-mono-large` | Mono 16 caps | Geist Mono 500, 16/20, +1%, uppercase |
| `v2-text-style-caption` | Body/16 Caps | Geist 400, Caption variables, −2%, uppercase |
| `v2-text-style-stat` | Statistic/56 | Geist 500, Stat variables, −4% |
| `v2-text-color-primary`, `-secondary`, `-muted`, `-tertiary`, `-brand`, `-alternate` | | `color`: the Theme Text variable of the same name |
| `v2-background-color-primary`, `-secondary`, `-tertiary`, `-alternate` | | `background-color`: Theme Background variable |

Semantic heading tags and heading classes are independent: the tag is for the document outline, the class is for the look. One `<h1>` per page.

**Two-font headings.** Write the heading with `v2-heading-style-h2` and wrap the serif part in a `<span>` with `v2-heading-style-accent-h2`, usually after a line break. The accent's line height makes its line exactly as tall as the heading's.

The tiny text inside product mockups (6–14px) is illustration. Export mockups as images or give them local classes; do not add them to the type scale.

## Component classes

| Class | Figma | Spec |
|---|---|---|
| `v2-button` | Reo/Button Primary | padding 12/24, square, `v2-text-style-label-caps` typography, background Button Primary/background, hover and pressed variables. **Stripes** (4 + 2 + 2px bars to the right) are `::after` and `::before`, with `background-color: inherit` / `border-color: inherit` so hover, pressed and theme recolor them; `margin-right: 1rem` reserves their space. The Style panel does not show pseudo-elements: note it in the build log. |
| `v2-button is-secondary` | Outline | transparent, 1px Border/primary; hover brand border and text; pressed brand-subtle fill; no stripes |
| `v2-button is-dark` | Dark | black; hover blue-600; pressed blue-700; keeps stripes |
| `v2-button is-light` | Light (on blue) | white, text black-80; hover blue text; pressed blue-100; no stripes |
| `v2-button` inside `v2-theme-brand` | | resolves to Dark automatically through the Theme mode |
| `v2-link-button` | Reo/Link Button | flex, space-between, padding 8/12, 1px Border/primary; children: `v2-text-style-mono` label + 16px arrow in `v2-icon-1x1-small`; hover brand, pressed brand-subtle |
| `v2-tag` + `v2-text-style-tag` | Reo/Tag | padding 8/12, 1px Border/secondary, Text/secondary |
| `v2-eyebrow` + `v2-text-style-mono` | Reo/Eyebrow | padding 1/8, min-height 24px, 0.5px hairline; `is-inverse` on dark or blue |
| `v2-stat` + `v2-text-style-stat` + `v2-text-style-label-caps` | Reo/Stat | column, 8px gap |
| `v2-icon-1x1-small` / `-medium` / `-large` | | 16 / 20 / 40px squares; inline SVG with `fill="currentColor"` |
| `v2-icon-button` | Reo/Icon Button | 40 × 40, centred icon, background `Background/secondary`, 1px `Border/primary`; hover brand border. Used for the nav menu button |
| `v2-button-group` | | flex, wrap, gap 12, align center |
| `v2-section-header_component` | Reo/Section Header | flex column, align and text center, gap `Spacing/small` (24). Holds an optional `v2-eyebrow` and an `h2.v2-heading-style-h2` |

Every link-type class here (`v2-button`, `v2-link-button`, navbar and footer links) must define its own `:hover` color and `text-decoration`, even when hover looks the same as rest. The legacy `a:hover` tag style is neutralised by the global embed with a selector that outranks a plain class but not a class with `:hover`.

Figma's component library ("↳ Components", `140:4753`, outside the home page section) also has Nav Bar, Tab, Feature Card, Section Header, Category Cell, Logo Cell, Integration Card, Trust Card, CTA Banner, Footer, Browser Bar and Product Demo Media. How each one maps to V2 classes and Webflow components on the home page is in `home-page-blueprint.md`.

**Section dividers** (`87:3145`; 96 / 72 / 48px tall) are vector art: export as SVG, do not rebuild. The six used on the home page, their node ids and asset names are in `home-page-blueprint.md`. Keep `width` and `height` attributes on SVGs.

**Disabled states.** Links cannot be `:disabled`. Add disabled styles only where a real `<button>` is used (forms).

## Exceptions to "variables only"

- **Hairlines** (Figma 0.5px strokes on eyebrow, tab, trust card): `box-shadow: inset 0 0 0 0.5px rgba(…)`. Chrome draws a 0.5px border as 1px. A variable cannot be bound inside a box-shadow string, so the color is written as rgba and needs an `is-inverse` combo on dark backgrounds.
- **Button stripes** use pseudo-elements.
- **Font stacks** live inside the font family variables.

## V2 Global Styles component

One component, group `V2 Global`, name `V2 Global Styles`: a `div.v2-global-styles` (display none) holding one HtmlEmbed. Place it first inside `v2-page-wrapper` on every V2 page. This is the only place global CSS for V2 lives.

Starting CSS (extend as the build needs; keep it small):

```html
<!-- START: v2-global-styles -->
<style>
/* --- Neutralise legacy tag styles. Remove this block at cleanup. --- */
a, a:hover { color: inherit; text-decoration: inherit; }
.w-select, .w-tab-link, .w-nav-link, .w-nav-brand, .w-dropdown-btn,
.w-dropdown-toggle, .w-dropdown-link, .w-slider-arrow-left, .w-slider-arrow-right {
  color: inherit; text-decoration: inherit; font-size: inherit;
}

/* --- Focus ring (replace the two custom properties with the cssName values
       query_variables returns for System/focus-state and Focus/offset) --- */
a:focus-visible, button:focus-visible, [tabindex]:focus-visible,
input:focus-visible, select:focus-visible, textarea:focus-visible {
  outline: 2px solid var(--REPLACE-focus-state);
  outline-offset: 2px;
}

/* --- Rich text: no stray margins at the edges --- */
.w-richtext > :not(div):first-child, .w-richtext > div:first-child > :first-child { margin-top: 0 !important; }
.w-richtext > :last-child, .w-richtext ol li:last-child, .w-richtext ul li:last-child { margin-bottom: 0 !important; }

/* --- Utilities that must always win --- */
.v2-hide { display: none !important; }
@media screen and (max-width: 991px) { .v2-hide-tablet { display: none !important; } }
@media screen and (max-width: 767px) { .v2-hide-mobile-landscape { display: none !important; } }
@media screen and (max-width: 479px) { .v2-hide-mobile-portrait { display: none !important; } }
.v2-container-large, .v2-container-medium, .v2-container-small { margin-right: auto !important; margin-left: auto !important; }
.v2-text-style-2lines { display: -webkit-box; overflow: hidden; -webkit-line-clamp: 2; -webkit-box-orient: vertical; }
.v2-text-style-3lines { display: -webkit-box; overflow: hidden; -webkit-line-clamp: 3; -webkit-box-orient: vertical; }

/* --- Motion --- */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; scroll-behavior: auto !important; }
}
</style>
<!-- END: v2-global-styles -->
```

Rules for this embed:

- A class named in the embed must also exist as a Webflow style (create `v2-hide`, `v2-hide-tablet` … with `create_style`), otherwise it cannot be applied in the Designer.
- Every class name and every `var(--…)` in it goes into the build log's custom-code ledger: the cleanup rename does not touch embeds.
- The legacy site head already sets font smoothing on `*`; do not repeat it.
- The Designer canvas does not render embeds. Check the result on the staging URL or in a local harness, not in a snapshot.
- Whether `a, a:hover { … inherit }` fully cancels the legacy link hover is to be confirmed in a real browser on the first review build. If a legacy color still shows on hover, the fix is a `:hover` state on the V2 class, not a change to the `a` tag style.

## Building a section

```text
section.v2-section_[name]            (+ v2-theme-dark / v2-theme-brand)
└─ div.v2-padding-global
   └─ div.v2-container-large
      └─ div.v2-padding-section-large
         └─ div.v2-[name]_component
            ├─ div.v2-[name]_header     v2-eyebrow > v2-text-style-mono, then h2.v2-heading-style-h2 with span.v2-heading-style-accent-h2
            └─ …                        cards and grids with custom classes bound to semantic variables
```

- Section header: the `v2-section-header_component` pattern (eyebrow, then the two-font H2, 24px apart). Header-to-content gap: `Layout/section-gap`.
- Cards use semantic variables. Integration card: Background/primary + Border/secondary; hover Background/secondary + Border/brand. Trust card on dark: Background/raised + Border/raised.
- Section backgrounds, node ids for all three breakpoints, class trees, copy and assets for the home page are in `home-page-blueprint.md`. Do not rely on older notes about section colours: the Figma file changed, and its tablet and mobile frames disagree with desktop (the blueprint says which wins).
