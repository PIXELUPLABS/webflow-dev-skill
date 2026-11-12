# Home page blueprint

A pre-read of the homepage design so each build session starts from decisions, not from interpretation. It covers the Figma section **Final LP** (`1:285`) of file `GuQCrycX2KDwenWDwW7FIT` and nothing outside it, read on **2026-11-12**.

How to use it:

1. Find the section you are building. Use its class tree, copy, assets and breakpoint table as the plan.
2. Still open the Figma node for that section (`get_design_context` + screenshot on the node id given here) before you build. The design can change after this file was written; if Figma and this file disagree, **Figma wins, and you tell the lead** so this file gets corrected.
3. Where the design is ambiguous, this file gives a **default**. Build the default, list the question in the build log, and move on. Do not stop the session for a design question that has a default here.

Page: `Home V2`, slug `home-v2`, replaces legacy Home (`67e6b65fe328bc6b91324d32`).

## Frames

| Breakpoint | Frame | Width | Webflow breakpoint |
|---|---|---|---|
| Desktop | `1:286` "Web — 1440" | 1440 | base |
| Tablet | `191:14289` "Tablet — 769" | 768 | `medium` (≤991) |
| Mobile | `191:17485` "Mobile — 391" | 390 | `small` (≤767) and `tiny` (≤479) |

Three more frames sit loose in the section, beside the mobile frame. They are **newer mobile versions** of three sections (see "Open design questions"): Testimonial `367:7733`, Take Reo Anywhere `634:3571`, Trust & Compliance `634:3743`.

## Section map

| # | Section | Desktop | Tablet | Mobile | Background (desktop) | V2 section class |
|---|---|---|---|---|---|---|
| – | Nav bar | `312:4653` (inside hero) | `191:14328` | `191:17513` | white bar on beige | component `V2 Navbar` |
| 1 | Hero | `191:12340` | `191:14290` | `191:17486` | beige | `v2-section_hero` |
| 2 | Trusted By | `1:408` | `191:14329` | `191:17514` | blue | `v2-section_trusted-by` + `v2-theme-brand` |
| 3 | Product Demo | `1:763` | `191:14358` | `191:17550` | beige | `v2-section_product-demo` |
| 4 | The Problem | `1:818` | `191:14365` | `191:17557` | white | `v2-section_problem` + `v2-background-color-secondary` |
| 5 | Testimonial | `1:2354` | `191:15492` | `367:7733` (newer) / `191:17563` (older) | blue | `v2-section_testimonial` + `v2-theme-brand` |
| 6 | Take Reo Anywhere | `1:2740` | `191:15844` | `191:17911` (stacked) / `634:3571` (carousel) | beige | `v2-section_integrations` |
| 7 | Trust & Compliance | `1:2817` | `191:15852` | `191:17919` / `634:3743` (carousel) | black | `v2-section_trust` + `v2-theme-dark` |
| 8 | CTA Banner | `1:3107` | `191:15864` | `191:18120` | blue | component `V2 CTA Banner` (`v2-theme-brand`) |
| 9 | Footer | `90:3905` | `191:15866` | `191:18122` | black | component `V2 Footer` (`v2-theme-dark`) |

### Rhythm (matches the tokens)

| | Desktop | Tablet | Mobile | Token |
|---|---|---|---|---|
| Side padding | 80 | 40 | 24 | `Spacing/global-padding` |
| Section top / bottom | 120 | 96 | 64 | `Section Padding/large` |
| Header → content gap | 80 | 64 | 48 | `Layout/section-gap` |
| Content width | 1280 | 688 | 342 | `Container/large` |
| Divider height | 95–96 | 72 | 48 | `Layout/divider-height` |

Exceptions drawn in Figma: Hero has its own paddings (below). On desktop, sections 6 and 7 have **180** bottom padding instead of 120, and The Problem has 100 bottom padding and a 100 gap. Build the token value and note it; these look like leftovers, not intent (question 9).

## Open design questions

Things the Figma file does not settle. Each has a default so work is not blocked. All of them are listed in the build log for the lead.

| # | Question | Default until answered |
|---|---|---|
| 1 | **Section backgrounds differ by breakpoint.** Desktop: Product Demo beige, The Problem white, Take Reo Anywhere beige. Tablet and mobile: Product Demo white, The Problem beige, Take Reo Anywhere white. | Use the **desktop** backgrounds at every breakpoint. The dividers are only properly drawn for desktop. |
| 2 | **Dividers on tablet and mobile are placeholders**: every instance is the same variant with a recoloured fill. Tablet and mobile also add dividers before and after the CTA and omit the one under the hero. | Reuse the six desktop divider graphics at every breakpoint, at the token height. CTA keeps its own built-in stepped edges. |
| 3 | **Three mobile sections exist twice** (Testimonial, Take Reo Anywhere, Trust & Compliance). | Use the loose, newer frames: `367:7733`, `634:3571` (carousel), `634:3743` (carousel). The Testimonial inside the mobile frame (`191:17563`) has broken copy and is clearly older. |
| 4 | **Nav behaviour**: sticky, fixed, or static? Figma calls the variant "Floating" but shows only the top of the page. Dropdown panels (Intent Signals, GTM Plays) and the open mobile menu are not in this section. | Static at the top of the page, built so that switching to sticky is one property. Build dropdown toggles and the menu button; leave panels empty until the lead links the designs. |
| 5 | **Product Demo media** is a placeholder ("Product demo" text, play button on mobile). Aspect ratios differ per breakpoint. Is it a video, where is it hosted, does it autoplay? | Build the browser frame and a media box with a `data-v2-video` hook and a poster slot. No video code until the lead supplies the source. |
| 6 | **The Problem showcases** are two full product-UI mock-ups (about 960 and 520 layers each), redrawn per breakpoint. Static images, or one interactive module with "Signals / GTM Agents" tabs? | Static images, one per showcase per breakpoint, with descriptive alt text. Do not rebuild the product UI as HTML. |
| 7 | **Testimonial content**: only one story is designed, and it is inconsistent (tab and logo say Aembit, quote and caption say DataHub / Malte Kramer). Three more tabs (NVIDIA, Databricks, Salesforce) have no content. Static or from the CMS (Customer Stories, Testimonial, Quotes collections exist)? | Build the tabs natively with the one designed story as static content in tab 1 and clearly marked placeholders in tabs 2–4. Do not invent quotes. |
| 8 | **Testimonial tabs on mobile** are not designed (the mobile card has no tabs). | Keep the tab row, horizontally scrollable, above the card. |
| 9 | **Odd desktop paddings** (180 bottom on sections 6 and 7; 100 on The Problem). | Token values (120 / gap 80). |
| 10 | **Footer links are placeholder copy from another product** ("Intake and triage", "Matter management", "What can you streamline?"). There is no copyright line, and the newsletter block has text but **no email field**. | Build the structure with the Figma labels as placeholders linked to `#`. Ask the lead for the real link list, a legal line, and whether the newsletter needs a form (the legacy footer has one). |
| 11 | **Feature cards in the hero**: desktop is one white panel with three columns; tablet and mobile are three separate beige cards with a border. Body copy reads like draft text ("Engg roadmap, ++", "etc."). | Build each breakpoint as drawn. Keep the copy verbatim and flag it. |
| 12 | **Trust cards**: order differs per breakpoint, and five cards do not fit 1280 on desktop (they overflow and fade at the edges). Auto-scrolling marquee, draggable slider, or static? | A horizontally scrollable, centred track with scroll-snap and edge fades, desktop order (CNCF, GDPR, SOC 2, Linux Foundation, CCPA). No autoplay. |
| 13 | **Copy differences**: "world-class" (desktop) vs "world class" (tablet, mobile). | Desktop copy. |
| 14 | **Component vs desktop frame drift.** Desktop sections 2, 5, 6 and 7 are drawn with loose frames; tablet and mobile use the real Figma components (`Reo/Section Header`, `Reo/Tab`, `Reo/Integration Card`, `Reo/Trust Card`). Small values differ (eyebrow gap 18 vs 24, card text style, `#171717` vs `#18181b`). | Component values for **styling**; desktop frame for **layout at 1440**. |
| 15 | **Cookie banner** has no V2 design, but every V2 page needs one (see `legacy-inventory.md`). | Blocked: ask the lead. Do not ship a review build without consent UI. |
| 16 | **Link targets** for the nav items, "Sign up", "Try now" and the three feature-card links are not in Figma. | Book a demo → `/book-a-demo`. Everything else → `#`, listed in the build log. |

## Build order

Shared pieces first, then the page top to bottom. Task cards with prompts are in `home-build-plan.md`.

1. Foundation (Phase 0) and the assets for the section you are about to build
2. `V2 Section Divider`, `V2 Navbar`
3. Page shell, then Hero → Trusted By → Product Demo → The Problem → Testimonial → Take Reo Anywhere → Trust & Compliance
4. `V2 CTA Banner`, `V2 Footer`
5. Responsive, accessibility and interaction pass over the whole page

## Shared patterns

### Section header

Figma `Reo/Section Header` (tones Light and Inverse). Not a Webflow component: a class pattern, because the heading mixes two fonts.

```text
div.v2-section-header_component          flex column, align center, text center, gap Spacing/small (24)
├─ div.v2-eyebrow (+ is-inverse on blue or black)
│  └─ div.v2-text-style-mono             "THE PROBLEM"
└─ h2.v2-heading-style-h2
   └─ span.v2-heading-style-accent-h2    the serif-italic words
```

- The heading colour comes from the theme (`Text/primary`), so it turns white inside `v2-theme-brand` / `v2-theme-dark` without extra classes.
- Use a `<br>` only where this file shows `⏎`. Otherwise let the text wrap, and control width with `v2-max-width-*` on the heading if needed.
- Heading sizes are the H2 tokens: 64 / 48 / 36 with the accent at 76 / 60 / 48.

### Light content inside a blue or black section

The Testimonial card is white inside a blue section. Text classes inside it would otherwise resolve to white. Put `v2-theme-light` on the card (defined in `v2-foundation.md`): it resets the Theme mode to light for everything inside.

### Section dividers

Figma `Reo/Section Divider` (`87:3145`). Irregular horizontal stripes that step from one section colour to the next. Vector art: **export, never rebuild**.

| After section | Desktop node | Variant (Base, Stripes, Edge, Flip) | Asset name |
|---|---|---|---|
| Hero → Trusted By | `90:3516` | Blue, Beige, Top, Off | `v2-divider-beige-to-blue.svg` |
| Trusted By → Product Demo | `90:3520` | Blue, Beige, Bottom, On | `v2-divider-blue-to-beige.svg` |
| Product Demo → The Problem | `90:3524` | Beige, White, Bottom, On | `v2-divider-beige-to-white.svg` |
| The Problem → Testimonial | `90:3528` | Blue, White, Top, Off | `v2-divider-white-to-blue.svg` |
| Testimonial → Take Reo Anywhere | `90:3532` | Blue, Beige, Bottom, Off | `v2-divider-blue-to-beige-alt.svg` |
| Take Reo Anywhere → Trust | `90:3536` | Beige, Black, Bottom, Off | `v2-divider-beige-to-black.svg` |
| Trust → CTA, CTA → Footer | part of the CTA banner art (`1:3107`) | stepped black / blue edges | exported with the CTA decor |

Component `V2 Section Divider` (group `V2 Global`), one variant per row above:

```text
div.v2-divider_component        height Layout/divider-height; position relative; overflow hidden; background = the "Base" colour
└─ img.v2-divider_image         position absolute; inset 0; width 100%; height 100%; alt "" (decorative)
```

Place the divider **between** sections as its own element in `v2-main-wrapper`, not inside either section. Keep `width` and `height` attributes in the SVG files.

### Buttons, tags, eyebrows, link buttons

Already specified in `v2-foundation.md`. Variants used on this page:

| Figma | V2 | Where |
|---|---|---|
| Button Primary | `v2-button` | nav, hero |
| Button Outline | `v2-button is-secondary` | hero "Try now" |
| Button Light | `v2-button is-light` | nav "Sign up", CTA "Try now" |
| Button Dark | `v2-button` inside `v2-theme-brand` (resolves to black) | CTA "Book a demo" |
| Tag | `v2-tag` > `v2-text-style-tag` | hero |
| Eyebrow Light / Inverse | `v2-eyebrow` / `v2-eyebrow is-inverse` > `v2-text-style-mono` | section headers |
| Link Button | `v2-link-button` > `v2-text-style-mono` + `v2-icon-1x1-small` arrow | feature cards |
| Icon Button | `v2-icon-button` (40×40, white, 1px `Border/primary`) | nav menu button |

All buttons are 40px tall (12 / 24 padding, 16px line). Button text is uppercase through the class, so type it in sentence case ("Book a demo").

---

## Nav bar: component `V2 Navbar`

Figma `Reo/Nav Bar`, variant Floating, Menu Closed. Desktop `312:4653`, tablet `191:14328`, mobile `191:17513`.

A white bar (`Background/secondary`), 1px `Border/secondary`, 56 tall, padding 8 / 8 / 8 / 16, as wide as the container (1280 / 688 / 342). It sits 24 / 21 / 12 px from the top of the page.

Build it with Webflow's **native Navbar element** (keyboard and mobile-menu behaviour come free) and V2 classes on every part.

```text
[V2 Navbar]
div.v2-navbar_wrapper                    position absolute; top 24 / 21 / 12; left 0; right 0; z-index; padding-left/right global-padding
└─ div.v2-navbar_component  (Navbar)     max-width Container/large; margin auto; flex; space-between; align center
   ├─ div.v2-navbar_left                 flex; align center; gap 32
   │  ├─ a.v2-navbar_logo-link  (Brand)  → home
   │  │  └─ img.v2-navbar_logo           55×22, alt "Reo.dev"
   │  └─ nav.v2-navbar_menu  (Nav Menu)  flex; align center
   │     ├─ div.v2-navbar_dropdown (Dropdown)      "Intent Signals"  ▾
   │     │  ├─ div.v2-navbar_link (Toggle)         padding 8 / 12; gap 4; v2-text-style-label
   │     │  │  └─ div.v2-navbar_caret              12×12 icon
   │     │  └─ nav.v2-navbar_dropdown-list (List)  empty until designed
   │     ├─ a.v2-navbar_link                       "AI Agents"
   │     ├─ div.v2-navbar_dropdown                 "GTM Plays"  ▾
   │     ├─ a.v2-navbar_link                       "Outcomes"
   │     ├─ a.v2-navbar_link                       "Insights"
   │     └─ a.v2-navbar_link                       "Compare"
   └─ div.v2-navbar_actions              flex; gap 8; align center
      ├─ a.v2-button.is-light            "Sign up"        desktop only
      ├─ a.v2-button                     "Book a demo"    desktop and tablet
      └─ div.v2-icon-button (Menu Button) menu icon       tablet and mobile
```

| | Desktop | Tablet | Mobile |
|---|---|---|---|
| Links | visible | in the menu | in the menu |
| Sign up | visible | in the menu | in the menu |
| Book a demo | visible | visible | in the menu |
| Menu button | hidden | visible | visible |

- Link text: Label/16 (Geist 500, 16 / 20), colour `Text/primary`. Give `v2-navbar_link` its own hover state.
- Link targets: Book a demo → `/book-a-demo` (URL link until Book a Demo V2 exists). The other targets are not defined in Figma: link to `#` and list them in the build log.
- **Manual step for the developer:** the menu's collapse breakpoint cannot be set through the MCP. In the Designer select the Navbar → Settings → Menu collapses at **Tablet**.
- The open menu and dropdown states need `.w--open` styling, which goes in a scoped embed inside the component (log it).
- Assets: logo `v2-logo-reo.svg` from the `Reo/Brand/Logo v3` instance (`811:4011` is a loose copy in the section), caret `v2-icon-caret-down.svg`, menu `v2-icon-menu.svg`.

## 1. Hero: `v2-section_hero`

Nodes `191:12340` / `191:14290` / `191:17486`. Background beige (page default). The section clips its overflow.

```text
section.v2-section_hero                  position relative; overflow hidden
├─ img.v2-hero_wave                      decorative; absolute; right side; behind content; desktop only
└─ div.v2-padding-global
   └─ div.v2-container-large
      └─ div.v2-hero_component           flex column; gap 64 / 32 / 48; padding-top 122 / 120 / 96; padding-bottom 80 / 80 / 64
         ├─ div.v2-hero_intro            flex column; gap 32; align start (mobile: center, text center)
         │  ├─ h1.v2-heading-style-h1
         │  │  ├─ span.v2-heading-style-accent-h1   "Intent signals"
         │  │  └─ "⏎for Technical GTM"
         │  ├─ div.v2-hero_tags          flex; wrap; gap 8 (mobile: justify center)
         │  │  └─ div.v2-tag > div.v2-text-style-tag   ×5
         │  └─ div.v2-button-group       flex; gap 12
         │     ├─ a.v2-button            "Book a demo"
         │     └─ a.v2-button.is-secondary  "Try now"
         └─ div.v2-hero_features         see below
            └─ [V2 Feature Card] ×3
```

The top padding leaves room for the nav, which overlays the hero. The three values are local to the hero (not section tokens).

**Copy**

- H1: *Intent signals* (serif accent) ⏎ for Technical GTM
- Tags: Developer tools · AI inference · Data infra · Security infra · Open source
- Buttons: Book a demo (`/book-a-demo`) · Try now (target not defined: `#`, ask)

**Feature cards**: component `V2 Feature Card` (group `V2 Elements`), props Index, Title, Body, Link Text, Link.

```text
div.v2-feature-card_component            flex column; gap 8; padding 28 (tablet, mobile: 20)
├─ div.v2-text-style-mono.v2-text-color-brand        "01"
├─ div.v2-feature-card_content           flex column; gap 24; flex-grow
│  ├─ div.v2-feature-card_text           flex column; gap 8
│  │  ├─ h3.v2-heading-style-h6          title
│  │  └─ p.v2-text-color-secondary       body (default body size 16 / 20)
│  └─ a.v2-link-button                   label + arrow
```

| # | Title | Body | Link label |
|---|---|---|---|
| 01 | Deeply technical intent signals | GitHub, HF, Docker, Engg roadmap, ++ | Signal library |
| 02 | World’s largest developer knowledge graph | 113M developers, skills, contributions, identity, etc. | Browse data |
| 03 | GTM agents that outperform Clay, Claude, Exa | Trained on proprietary data, etc. | Agent library |

| `v2-hero_features` | Desktop | Tablet | Mobile |
|---|---|---|---|
| Layout | 3 equal columns, gap 0 | 3 columns, gap 16, padding 24 top and bottom | 1 column, gap 24 |
| Panel | one white panel (`Background/secondary`) with 1px `Border/secondary`; 1px vertical rule between columns | no panel | no panel |
| Card | transparent | 1px `Border/primary`, transparent | same as tablet |

On desktop the link button sits at the bottom of each card, so the three buttons line up even when titles wrap differently: make the cards equal height and push the button down (`margin-top: auto` on the link button).

**Wave** (`191:12341` "Decor / Wave", about 853×852): export as `v2-hero-wave.svg`. Blue vertical ribbons on the right edge, partly behind the white feature panel. Desktop only (it is off-canvas on tablet and absent on mobile): hide at `medium` and below. `alt=""`.

**Watch for**: the H1 is the only `<h1>` on the page. At mobile the whole intro is centred; on desktop and tablet it is left-aligned.

## 2. Trusted By: `v2-section_trusted-by`

Nodes `1:408` / `191:14329` / `191:17514`. Blue: add `v2-theme-brand`. Divider above and below (table in "Section dividers").

```text
section.v2-section_trusted-by.v2-theme-brand
└─ div.v2-padding-global
   └─ div.v2-container-large
      └─ div.v2-padding-section-large
         └─ div.v2-trusted-by_component          flex column; gap Layout/section-gap
            ├─ div.v2-section-header_component
            │  ├─ div.v2-eyebrow.is-inverse > div.v2-text-style-mono     "Trusted by"
            │  └─ h2.v2-heading-style-h2          "Trusted by world-class " + span.accent "technical GTM teams"
            └─ div.v2-trusted-by_grid             4 columns (mobile: 1 column, gap 24)
               └─ div.v2-trusted-by_category  ×4  flex column
                  ├─ div.v2-trusted-by_category-label     icon 16 + v2-text-style-tag
                  └─ div.v2-trusted-by_logos              1 column of 4 (mobile: 2×2 grid)
                     └─ div.v2-trusted-by_logo-cell  ×4   flex; center
                        └─ img.v2-trusted-by_logo
```

Each **category is one column** on desktop and tablet and becomes its own block on mobile. That one structure covers all three layouts.

| Category (icon) | Logos, top to bottom |
|---|---|
| AI infrastructure (Sparkle) | Mastra, Nebius, n8n, NVIDIA |
| DevTools (Code) | Unleash, GrowthBook, CircleCI, Antithesis |
| Data infra (HardDrives) | Aerospike, MinIO, Synadia, Ververica |
| Security (Shield) | Aembit, Filigran, Tigera, Chainguard |

| | Desktop | Tablet | Mobile |
|---|---|---|---|
| Columns | 4 | 4 | 1 (logos 2×2 inside each category) |
| Logo cell | 320 × 214 | 172 × 144 | 171 × 120 |
| Category label | 32 tall, padding 8 / 12, gap 8 | same | same, full width |

- Grid lines: 1px **dashed**, white at 20% (`Border/primary` in brand mode). Each cell has a right and bottom border; the grid has a top and left border. Webflow's `dashed` style will not match Figma's 4 / 4 pattern exactly; that is accepted.
- Category label text: white at 80% (`Text/secondary` in brand mode).
- Hover on a logo cell: background black (`Background/alternate` in brand mode). Figma shows CircleCI in the hover state; it is not a permanent highlight.
- Assets: 16 logos as white SVGs, `v2-logo-[company].svg`, exported from the tablet `Reo/Logo Cell` instances (`191:14338`–`191:14356`); 4 category icons `v2-icon-sparkle.svg`, `-code`, `-hard-drives`, `-shield` with `fill="currentColor"`. Alt text is the company name.

## 3. Product Demo: `v2-section_product-demo`

Nodes `1:763` / `191:14358` / `191:17550`. Beige (question 1). No section header. Divider below.

```text
section.v2-section_product-demo
└─ div.v2-padding-global > div.v2-container-large > div.v2-padding-section-large
   └─ div.v2-product-demo_component
      └─ div.v2-browser_component            1px Border/secondary; background Background/primary; overflow hidden
         ├─ div.v2-browser_bar               56 tall; padding 16; gap 16; white; 1px bottom border
         │  ├─ div.v2-browser_controls       three 8px dots, gap 6
         │  ├─ div.v2-browser_url            flex-grow; 24 tall; padding 4 / 12; background Background/primary
         │  │  └─ div.v2-text-size-small.v2-text-color-muted   "Reo.dev"
         │  └─ div.v2-browser_menu           vertical dots icon
         └─ div.v2-browser_body              padding 24
            └─ div.v2-product-demo_media     white; 1px Border/secondary; position relative; data-v2-video
               └─ (poster image / play button / video go here once supplied)
```

- `v2-browser_*` is a global folder: the same browser frame is used around The Problem showcases.
- The media is a placeholder in Figma. Give `v2-product-demo_media` an `aspect-ratio` of 16 / 9 for now and note it. Play button on mobile: 72×72.
- Nothing here needs JavaScript until the video source is known.

## 4. The Problem: `v2-section_problem`

Nodes `1:818` / `191:14365` / `191:17557`. White: `v2-background-color-secondary` (question 1). Divider below.

```text
section.v2-section_problem.v2-background-color-secondary
└─ div.v2-padding-global > div.v2-container-large > div.v2-padding-section-large
   └─ div.v2-problem_component               flex column; gap Layout/section-gap
      ├─ div.v2-section-header_component
      │  ├─ div.v2-eyebrow > div.v2-text-style-mono     "The problem"
      │  └─ h2.v2-heading-style-h2            "Tech GTM needs ⏎" + span.accent "purpose-built" + " intent tooling"
      └─ div.v2-problem_showcases             flex column; gap Layout/section-gap
         └─ div.v2-problem_showcase  ×2       position relative; overflow hidden
            ├─ picture / img.v2-problem_showcase-image     one source per breakpoint
            └─ div.v2-problem_showcase-fade                gradient to the section colour at the bottom edge
```

| Showcase | Desktop | Tablet | Mobile | Alt text |
|---|---|---|---|---|
| 1 "How do we uncover silent evaluation?" | `204:4311` 1280×780 | `303:1560` 688×808 | `303:3088` 342×1042 | "Reo.dev signals library: package installs, GitHub interactions, container pulls and other developer intent signals, with a developer profile panel." |
| 2 "Which of your target accounts are worth routing to SDRs?" | `204:5280` 1280×808 | `303:2531` 688×1040 | `303:4058` 342×1120 | "Reo.dev GTM Engineer agent enriching a target account list and routing qualified accounts to SDRs." |

- Export each as an image at 2× (WebP or PNG; the mock-ups contain small text, so check legibility). Names: `v2-problem-signals-desktop.webp`, `-tablet`, `-mobile`; `v2-problem-agents-desktop.webp`, and so on.
- Serve the right one per breakpoint (three images toggled with `v2-hide-*` utilities is acceptable; note it).
- Each mock-up includes its own browser chrome, 1px border and 4px corner radius in Figma; export the whole frame so they stay crisp together, and do not add a second border in Webflow.
- The two gradient rectangles on desktop (`1:2352`, `1:2353`) are the bottom fades.

## 5. Testimonial: `v2-section_testimonial`

Nodes `1:2354` / `191:15492` / mobile `367:7733`. Blue: `v2-theme-brand`. Divider above and below.

```text
section.v2-section_testimonial.v2-theme-brand
└─ div.v2-padding-global > div.v2-container-large > div.v2-padding-section-large
   └─ div.v2-testimonial_component                  flex column; gap Layout/section-gap
      ├─ div.v2-section-header_component
      │  ├─ div.v2-eyebrow.is-inverse > div.v2-text-style-mono     "The testimonial"
      │  └─ h2.v2-heading-style-h2          "See how the " + span.accent "most ambitious" + " tech GTM teams use Reo"
      └─ div.v2-testimonial_card.v2-theme-light  (Tabs)            white; 1px border
         ├─ div.v2-testimonial_tabs  (Tabs Menu)                   flex; 4 equal tabs
         │  └─ a.v2-testimonial_tab  (Tab Link) ×4                 48 tall; padding 12 / 16; space-between
         │     ├─ div.v2-text-style-label-caps                     "Aembit"
         │     └─ div.v2-testimonial_tab-indicator                 8×8 square
         └─ div.v2-testimonial_panes  (Tabs Content)
            └─ div.v2-testimonial_pane  (Tab Pane) ×4
               └─ div.v2-testimonial_story                         flex row; gap 60; padding 60 / 40 (tablet: column, padding 40; mobile: padding 24)
                  ├─ div.v2-testimonial_content                    flex column; space-between; gap 64
                  │  ├─ div.v2-testimonial_quote-block             flex column; gap 40
                  │  │  ├─ img.v2-testimonial_logo                 customer logo, 30px tall
                  │  │  └─ p.v2-text-size-large.v2-text-color-secondary   quote, with span.v2-testimonial_highlight
                  │  └─ div.v2-testimonial_stats                   flex; gap 42 (tablet 64, mobile 24)
                  │     └─ div.v2-stat ×2 > div.v2-text-style-stat + div.v2-text-style-label-caps
                  └─ div.v2-testimonial_portrait                   position relative; 382×460 (tablet 608×521; mobile 294×352)
                     ├─ img.v2-testimonial_portrait-image
                     └─ div.v2-testimonial_caption                 absolute; bottom left; white; padding 8 / 12
                        ├─ div.v2-testimonial_name
                        └─ div.v2-text-style-caption               role
```

**Tabs**: Aembit (active in Figma) · NVIDIA · Databricks · Salesforce.

| Tab state | Background | Text | Indicator | Border |
|---|---|---|---|---|
| Default | `Background/primary` (beige) | `Text/primary` | black at 80% | 1px `Border/primary` |
| Active | black | white | white | 1px `Border/brand` (blue) |

The active state is Webflow's `.w--current`, which the MCP cannot create: style `.v2-testimonial_tab.w--current` in a scoped embed inside the section, and log it. Give the default tab a hover state.

**The one designed story**

- Logo: Aembit (question 7).
- Quote: "DataHub uses Reo.dev to convert open-source adoption into Cloud pipeline. It shows which OSS accounts are deploying, contributing, and gaining momentum, so BDRs time their outreach instead of working every account on a fixed cadence. Reo-signaled accounts generated **$1.01M in pipeline in Q1 alone.**" The bold phrase is the highlight: blue background (`Background/tertiary` resolves to blue in light mode), white text, a little horizontal padding.
- Stats: **+200%** Meetings booked · **40%** Attributed deal pipeline.
- Caption: Malte Kramer · CEO & Co-founder, DataHub. Name is Geist 500, 24px desktop (use 20px at tablet and below); role is `v2-text-style-caption`.
- Portrait: a black-and-white cut-out over blue halftone and thin blue and green rules that run past the card edge. Export the art and the photo together as one transparent image per breakpoint (`v2-testimonial-datahub-portrait-desktop.webp` …) from `191:11650` / `191:15529` / `367:7766`. The card clips it.

**Watch for**: quote text colour is grey on white, so the card must carry `v2-theme-light`. Stats text is near-black, not blue.

## 6. Take Reo Anywhere: `v2-section_integrations`

Nodes `1:2740` / `191:15844` / mobile `634:3571`. Beige (question 1). Divider below (beige → black).

```text
section.v2-section_integrations
└─ div.v2-padding-global > div.v2-container-large > div.v2-padding-section-large
   └─ div.v2-integrations_component                 flex column; gap Layout/section-gap
      ├─ div.v2-section-header_component
      │  ├─ div.v2-eyebrow > div.v2-text-style-mono     "Build in Reo"
      │  └─ h2.v2-heading-style-h2          "Take Reo " + span.accent "anywhere"
      └─ div.v2-integrations_list           4 columns, gap 16 (tablet: 2 columns, gap 20; mobile: scroll track, gap 12)
         └─ div.v2-integration-card_component (+ is-highlighted)  ×4
            ├─ div.v2-integration-card_icons            flex; gap 16–22; icons 40 tall
            ├─ div.v2-integration-card_text             flex column; gap 8
            │  ├─ h3.v2-heading-style-h6
            │  └─ p.v2-text-color-secondary
            └─ img.v2-integration-card_stripes          absolute; bottom; 32 tall; decorative
```

Card: 344 tall on desktop and tablet (320 in the mobile carousel, 280 wide), padding 24 / 24 / 64 / 24, icons at the top and text at the bottom (`justify-content: space-between`), background `Background/primary`, 1px `Border/secondary`. `is-highlighted`: background black, text white. Hover (from the Figma component): background `Background/secondary`, border `Border/brand`.

| Card | Icons | Body |
|---|---|---|
| Via MCP | MCP mark | Reo tracks every technical signal across 50+ sources to identify the right buying intent. |
| In CRM (`is-highlighted`) | Salesforce, HubSpot, Pipedrive | Easily send your data to your CRMs. |
| Via Slack | Slack | Get real-time account, developer, and buyer alerts inside Slack. |
| Via data exports | Webhooks, Snowflake, BigQuery | Pull any data you need into your own systems and workflows. |

- The highlighted card inherits white text by setting the Theme mode: put `v2-theme-dark` on it instead of hand-colouring text, or define `is-highlighted` to do the same. Pick one and record it.
- Mobile carousel (`634:3571`): a horizontal scroll-snap track with 24px side padding, cards 280 wide, and a pager row ("01 / 04" in mono plus four small bars). Build the track with CSS scroll-snap; the pager needs a few lines of script (log it) or can be left static until the lead confirms.
- Assets: icon SVGs `v2-icon-mcp.svg`, `v2-icon-salesforce.svg`, `v2-icon-hubspot.svg`, `v2-icon-pipedrive.svg`, `v2-icon-slack.svg`, `v2-icon-webhooks.svg`, `v2-icon-snowflake.svg`, `v2-icon-bigquery.svg`; stripes `v2-integration-stripes.svg` (white bars; they are white on both card styles). Third-party logos keep their brand colours where Figma shows them.

## 7. Trust & Compliance: `v2-section_trust`

Nodes `1:2817` / `191:15852` / mobile `634:3743`. Black: `v2-theme-dark`. Divider above (beige → black). The track runs edge to edge, so the cards are **outside** the container.

```text
section.v2-section_trust.v2-theme-dark
└─ div.v2-padding-section-large
   └─ div.v2-trust_component                        flex column; gap Layout/section-gap
      ├─ div.v2-padding-global
      │  └─ div.v2-section-header_component         (no eyebrow)
      │     └─ h2.v2-heading-style-h2       span.accent "Built on trust." + "⏎Powered by standards"
      └─ div.v2-trust_carousel                      position relative; overflow hidden
         ├─ div.v2-trust_track                      flex; gap 20 (mobile 12); overflow-x auto; scroll-snap; centred
         │  └─ div.v2-trust-card_component (+ is-highlighted) ×5
         │     ├─ img.v2-trust-card_badge           150×199 shield
         │     └─ div.v2-text-style-tag             label  (highlighted: inside a white pill)
         ├─ div.v2-trust_fade.is-left               gradient black → transparent, about 110 wide (desktop, tablet)
         └─ div.v2-trust_fade.is-right
```

| Card | Label | Style |
|---|---|---|
| CNCF | Cloud Native Computing Foundation | default |
| GDPR | GDPR compliant (white pill, dark text) | `is-highlighted`: blue background, white stripe art behind the badge |
| SOC 2 | SOC 2 | default |
| Linux Foundation | The Linux Foundation | default |
| CCPA | CCPA | default |

Card: about 300 × 320, padding 40 top and bottom, badge above label, background `Background/raised`, 1px `Border/raised` (in dark mode these are the near-black card colours). Mobile cards are 264 × 284.

- Badges are illustrations: export each shield as SVG (`v2-badge-cncf.svg`, `-gdpr`, `-soc2`, `-linux-foundation`, `-ccpa`) and the GDPR stripe art as `v2-trust-gdpr-stripes.svg`. Alt text: "SOC 2 Type 2 badge" and so on.
- Hide the scrollbar with a scoped embed if needed (log it). No autoplay by default (question 12).
- Mobile pager (four small bars) is decorative until the behaviour is confirmed.

## 8. CTA Banner: component `V2 CTA Banner`

Nodes `1:3107` / `191:15864` / `191:18120`. Blue: `v2-theme-brand`. Group `V2 Global`; props Heading (rich text), Primary Text, Primary Link, Secondary Text, Secondary Link.

```text
[V2 CTA Banner]
section.v2-section_cta.v2-theme-brand           position relative; overflow hidden
├─ img.v2-cta_decor.is-left                     decorative stripes
├─ img.v2-cta_decor.is-right
└─ div.v2-padding-global
   └─ div.v2-container-large
      └─ div.v2-cta_component                   flex column; center; gap 24 (tablet, mobile 40); min-height 600 / 480 / 440
         ├─ h2.v2-heading-style-h2              "See the " + span.accent "Technical ⏎GTM Mesh" + " in action"
         └─ div.v2-button-group                 gap 8 (tablet, mobile 12)
            ├─ a.v2-button                      "Book a demo"   (black here, through the theme)
            └─ a.v2-button.is-light             "Try now"
```

- Vertical padding: 80 / 96 / 64.
- Decor: on desktop two large stripe clusters, bottom-left and top-right (`1:3159`, `1:3123`), plus stepped black edges at the top and bottom that join the black sections either side (`1:3122` and the vector in `1:3107`). Export desktop art as `v2-cta-decor-left.svg`, `v2-cta-decor-right.svg`, `v2-cta-edge-top.svg`, `v2-cta-edge-bottom.svg`. On tablet and mobile the component uses small corner stripe blocks (144×124 and 80×72): scale the desktop art down rather than exporting a second set, and note it.
- Links: Book a demo → `/book-a-demo`; Try now → `#` until defined.

## 9. Footer: component `V2 Footer`

Nodes `90:3905` / `191:15866` / `191:18122`. Black: `v2-theme-dark`. Group `V2 Global`.

```text
[V2 Footer]
footer.v2-footer_component.v2-theme-dark        position relative; overflow hidden
├─ div.v2-padding-global
│  └─ div.v2-container-large
│     └─ div.v2-footer_top                      flex; space-between; padding-top about 96 on desktop (measure it in Figma) / 96 / 64 (tablet: wrap; mobile: column, gap 48)
│        ├─ div.v2-footer_newsletter            flex column; gap 18 (tablet, mobile 24); max-width 320
│        │  ├─ p.v2-text-color-secondary        "Want insights from Reo.dev delivered straight to your inbox?"
│        │  └─ div.v2-footer_social             flex; gap 16
│        │     └─ a.v2-footer_social-link ×4    20×20 icon; aria-label
│        └─ div.v2-footer_columns               3 columns of 260, gap 24 (tablet: 2 columns of 332, gap 24 / 48; mobile: 1 column)
│           └─ div.v2-footer_column ×3          flex column; gap 16
│              ├─ div.v2-text-style-tag         "Product"
│              └─ ul.v2-footer_link-list        list reset (no margin, padding, bullets)
│                 └─ li.v2-footer_link-item > a.v2-footer_link
└─ div.v2-footer_wordmark  (aria-hidden)        "Reo.dev"
```

- Footer link: 16 / 20, 1px bottom border (`Border/primary`, white at 20% in dark mode), 12 padding below, rows 32 tall on desktop and 44 on tablet and mobile; rest opacity 50%, hover 100%. Column headings white at 74% (`Text/muted`).
- Social: Facebook, LinkedIn, Instagram, YouTube, 60% opacity at rest. Icons `v2-icon-facebook.svg` … with `fill="currentColor"`. Each link needs an `aria-label`. URLs are not in Figma: take them from the legacy footer.
- **Columns in Figma (placeholder copy, question 10):** Product: AI platform, Intake and triage, Workflow automation, Matter management, Integrations, What can you streamline? · General: About us, Blog, Pricing, Schedule a demo, Security, Careers, Sitemap · Legal: Privacy policy, Terms of use, Sub-processors.
- **Wordmark:** "Reo.dev" in Geist 400 at 432px on a 1440 frame (224 on tablet, 112 on mobile), letter-spacing −4%, a light-to-dark gradient fill, cropped at the bottom with a fade. Build it as live text: `font-size: 30vw; line-height: 1`, gradient through `background-clip: text`, and a gradient overlay for the bottom fade. It is decorative: `aria-hidden="true"`.
- Lists: the legacy `ul` / `li` tag styles add margins and padding, so the list classes must reset them.

---

## Assets to export

Upload to the `V2` asset folder, sub-folder per section. SVG for anything vector; WebP at 2× for raster. Run the Figma export on the node given; do not screenshot.

| Group | Count | Source | Notes |
|---|---|---|---|
| Brand logo | 1 | `Reo/Brand/Logo v3` (`811:4011`) | SVG |
| UI icons | about 8 | caret, menu, arrow, play, sparkle, code, hard-drives, shield | SVG, `currentColor` |
| Social icons | 4 | footer | SVG, `currentColor` |
| Hero wave | 1 | `191:12341` | SVG |
| Customer logos | 16 | tablet logo cells `191:14338`–`191:14356` | SVG, white |
| Section dividers | 6 | `90:3516`, `90:3520`, `90:3524`, `90:3528`, `90:3532`, `90:3536` | SVG, keep width and height |
| Problem showcases | 6 | 2 showcases × 3 breakpoints | WebP 2× |
| Testimonial | 2+ | customer logo, portrait composite per breakpoint | SVG logo, transparent WebP portrait |
| Integration icons | 8 | cards in `191:15846` | SVG |
| Integration stripes | 1 | `Decor / Stripes` in an integration card | SVG |
| Trust badges | 5 + 1 | `Reo/Trust Badge/*`, GDPR stripe art | SVG |
| CTA decor | 4 | `1:3123`, `1:3159`, `1:3122`, edge vector in `1:3107` | SVG |

Set real alt text on meaningful images (logos, badges, showcases, portrait) and an empty alt on decoration (wave, dividers, stripes, CTA decor).

## Interactions and custom code this page needs

| Feature | Approach | Custom code |
|---|---|---|
| Nav menu and dropdowns | native Webflow Navbar and Dropdown | CSS for `.w--open` in an embed |
| Testimonial tabs | native Webflow Tabs | CSS for `.w--current` in an embed |
| Integration and trust carousels | CSS scroll-snap | optional pager script; scrollbar-hiding CSS |
| Product demo video | not defined | none yet |
| Hover states | class `:hover` states | none |
| Entrance animation | none in Figma | none: do not add motion the design does not show |

Everything in the right-hand column goes in the build log's custom-code ledger.

## Accessibility checklist for this page

- One `<h1>` (hero). Section headings are `<h2>`. Card titles are `<h3>`.
- Landmarks: nav in a `<nav>`, page content in `<main>`, footer in a `<footer>`.
- Every link and button has a visible focus ring (from `V2 Global Styles`), on beige, blue and black.
- Text contrast: white at 50% on black (footer links at rest) is below AA for body text. Build as designed and flag it.
- Tabs, dropdowns and the menu work with the keyboard (native elements handle this; verify on a review build).
- Carousels can be scrolled with the keyboard and by touch; no content is reachable only by hover.
- Decorative images have empty alt text; the footer wordmark is `aria-hidden`.

## Done when (whole page)

- All nine sections and the six dividers are on `Home V2`, in order, inside the page shell.
- The page matches Figma at 1440, 768 and 390, and does not break in between (check 1200, 992, 600, 360).
- Every default taken from "Open design questions" is listed in the build log with its question number.
- Linter clean; no legacy class or component on the page; page still draft, indexing off.
- The custom-code ledger lists every embed on the page.
