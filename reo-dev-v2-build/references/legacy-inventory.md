# Legacy inventory: what already exists in the Reo.Dev project

Read-only audit of site `67e6b65ee328bc6b91324c9a` taken **2026-11-12** through the Webflow MCP. The client's team keeps editing and publishing the legacy site (last publish 2026-11-08), so treat this as a map, not as live state: confirm an id with the MCP before relying on it.

Everything in this file is **legacy**. You read it; you do not change it.

## At a glance

| | |
|---|---|
| Site | Reo.Dev · short name `reo-dev-2-0` · workspace `63d9ebeb4a5c000bdd5a0d25` · time zone Asia/Calcutta · created 2025-03-28 |
| Domains | `www.reo.dev`, `reo.dev`; staging subdomain derives from the short name (`reo-dev-2-0.webflow.io`, confirm before sharing) |
| Locales | English only (primary locale id `67f245093fcfae53e5bcbd41`, CMS locale id `67f245093fcfae53e5bcbd2f`); localization not enabled |
| Plan | Not Enterprise. Page branching returns `not_enterprise_plan_site`. Do not try branch actions. |
| Pages | 122: 82 static (17 of them draft) and 40 CMS template pages |
| Styles | 3,494: 2,576 global classes, 809 combos, 109 tag / nested-tag styles |
| Components | 85 |
| Variables | 6 collections, 213 variables |
| Fonts | Inter (variable, roman + italic) and Geologica (variable), uploaded as TTF |
| Interactions | No IX3 (Interactions with GSAP) interactions exist. Legacy animation is Classic interactions plus custom code. |
| Agent instructions | None stored on the site |
| Registered scripts | None. All custom code is freeform (site head / footer, page head / footer, embeds). |

## How the legacy build is put together

It started from the **Relume Client-First starter** (the older, two-class spacing system) and grew by hand for a year and a half. Expect inconsistency:

- Standard Client-First names coexist with ad-hoc ones (`btn-new`, `cta-new_wrap`, `primary-btn`, `c-table`, `text-color#6C7085`, `divider purple-50 25%`, `padding-1.5-rem`).
- About 30 Webflow auto-names are in use as real classes (`Div Block`, `Quick Stack 2`, `Text Span`, `button Copy`, `Tab Pane [Tab 1]`).
- Misspelt folders are load-bearing (`testinonials_*`, `referrel_*`, `siganls-header_*`, `carees-header_*`, `partner-directory-comapnies`). Do not "fix" them.
- 535 classes have more than one underscore; capitals appear in ~60 names.
- Utilities are stacked as combos (`hide`, `text-weight-medium`, `margin-small`, `text-color-grey-500` are among the most common combo names).

None of this is yours to tidy. It all disappears at cleanup.

### Page skeleton of a legacy page (Home)

```text
body
├─ div.page-wrapper (.is-home)
│  ├─ [component] Global Styles            ← two <style> embeds, see below
│  ├─ [component] Navbar Light (rewamped)  ← often two navbar components per page
│  ├─ [component] Navbar White (rewamped)
│  ├─ main.main-wrapper
│  │  ├─ section.section_hero-home
│  │  ├─ [component] section divider
│  │  ├─ [component] [section] customer-love
│  │  ├─ section.section_the-problem … section.section_cta-new
│  └─ [component] Footer
└─ div.fs-consent_component                ← Finsweet Consent Pro banner + preferences, a page-level block, NOT a component
```

## Things a V2 page inherits whether you want it or not

A page in this project gets the site's compiled CSS and site-wide code. These are the parts that reach into V2 pages.

### 1. Tag styles (apply to every page)

| Selector | Legacy style | What V2 must do |
|---|---|---|
| `body` | background, font family (Inter), color, size, line height and weight from legacy variables; switches the legacy `Typography 1` mode and, at ≤991 / ≤767, the legacy `Reponsive` modes | `v2-page-wrapper` sets background, color, font family, size, line height, weight and letter spacing explicitly and fills the viewport (`min-height: 100vh`) |
| `h1`–`h6` | Geologica, legacy sizes, weights and line heights; `h2` has `letter-spacing: -2px`; `h1`–`h3` margins 0, **`h4` and `h5` keep Webflow's default margins**, `h6` only margin-bottom 0 | Every heading carries a `v2-heading-style-*` class that sets family, size, line height, weight, letter spacing **and** `margin-top: 0; margin-bottom: 0` |
| `p` | margin-bottom 0 | nothing |
| `a` | legacy link color, `text-decoration: none`, 300ms color transition; **`:hover` changes color and underlines** | `V2 Global Styles` resets `a` and `a:hover` to inherit. Any V2 link class that sets `color` or `text-decoration` must also set its own `:hover` (see `v2-foundation.md`) |
| `ul` / `ol` | margin 1rem / 0.875rem top and bottom, padding-left 1.25rem / 1.5rem | List classes reset margin and padding |
| `li` | margin-bottom 0.125rem, padding-left 0.5rem | List-item classes reset both |
| `blockquote` | 1px border (4px left), 0.75rem radius, white background, padding, italic | Any V2 blockquote class resets border, radius, background, padding, font style and margin |
| `figure`, `figcaption` | margins 0; caption margin-top 0.25rem, centered | reset if used |
| `img` | inline-block, max-width 100% | nothing |
| `strong` | 700 | fine (Geist is variable) |

Nested tag styles also exist under legacy rich-text classes (`.text-rich-text`, `.blog_content-richtext`, `.playbook_content-richtext`, `.callout_content`, `.feature_content`, `.testimonial_heading-richtext`, `.tech-target_content-*`). They only match inside those classes, so they do not touch V2 as long as V2 never uses those classes.

### 2. Site-wide custom code (Site settings → Custom code)

Head: a `* { -webkit-font-smoothing: antialiased; … }` rule; Plausible; Google Ads tag `AW-18294452775`; and, managed by **Finsweet Consent Pro** (`type="fs-consent"`): Crazy Egg, GA4 `G-HS6EZGWKJ5`, HubSpot `39628812`, Clearbit, Ahrefs analytics.

Footer, all behind Consent Pro: the Reo.dev tracking script, a referrer block for `wake-up-network.com`, LinkedIn Insight (partner id `8800692`).

Consequences for V2:

- These load on V2 pages too. Do not add a second copy of any of them in page code.
- Scripts marked `fs-consent` stay blocked until the visitor consents through a banner. The banner is a block on each legacy page, so **a V2 page needs its own consent UI** (`V2 Cookie Banner` component, built with the same `fs-consent-element` attributes) or analytics never fires there.
- Never edit site-wide code. If V2 needs something site-wide, give the lead the exact snippet.

### 3. What V2 pages do NOT inherit (because it sits in the legacy `Global Styles` component)

The `Global Styles` component (`ab488b17-f25a-fbf8-5f54-4a3955eb57e5`, 104 instances) holds two embeds, `style-overrides` and `color-schemes`. The first one contains:

- **A fluid root font size**: `html { font-size: 1.125rem }` scaled with `calc(… + …vw)` below 1920, 1440 and 479px. On legacy pages `1rem` is 16px only at exactly 1440px wide. V2 pages do not include this component, so on V2 pages **1rem = 16px at every width**. This is why legacy components cannot be dropped into V2 pages: every rem in them would resolve differently.
- `a, .w-nav-link, .w-dropdown-link … { color: inherit; text-decoration: inherit; font-size: inherit }`
- focus ring `*[tabindex]:focus-visible { outline: 0.125rem solid #4d65ff }`
- rich-text first / last child margin resets
- `.hide`, `.hide-tablet`, `.hide-mobile-landscape`, `.hide-mobile` with `!important`
- `!important` rules behind the two-class spacing system (`.margin-top`, `.padding-horizontal`, `.margin-0`, `.spacing-clean` …)
- container auto-margins, 2 / 3 line clamps, `.truncate-width`, `select { -webkit-appearance: none }`

V2 has its own embed (`V2 Global Styles`) with the V2 equivalents. Never place the legacy `Global Styles` component on a V2 page.

## Variables (legacy)

| Collection | Id | Modes | Contents |
|---|---|---|---|
| Primitives | `collection-0220e3ad-eb86-03ea-3026-8a5979301dd2` | base | 99: purple brand scale (`Brand/Purple 10`–`900`, default `#6c45dc`), grey 00–900, accent green, info, warning, error, orange, white alphas, gradient stops, font families (Geologica / Inter), font weights |
| Theme | `collection-139f4ef2-8521-8181-4a7f-fc90894e2d6f` | base | 24: `Default/*`, `BG Colors/*`, `Text Colors/*`, `Border/*`. Its CSS names have **no collection prefix** (`--border--primary`, `--text-colors--link`) |
| UI Styles | `collection-08964abb-b13c-a798-071a-663d82b7f0a6` | base | 62: spacing 2–128, radii, shadows, max widths, containers (80 / 64 / 48rem), global padding 5% |
| Reponsive *(sic)* | `collection-1f153719-f065-2ed6-7dd4-535a8494bce4` | base · Tablet · Mobile (L) | 18: responsive font sizes and line heights. `body` switches these modes at ≤991 and ≤767 |
| Typography 1 | `collection-3c6a4911-12c4-e415-7fe0-514cefa2d46d` | base + 11 (Display 1 … Body) | 5: a "type style as mode" system; each heading tag selects a mode |
| Typography 2 | `collection-1cc7cd3c-2eef-aec5-40fb-503a5ae4c44e` | base + 5 (Body 2 … Button Medium) | 5 |

Several legacy values still point at Relume starter variables (`relume-variable--…`). All of it is off-limits: no edits, no new variables in these collections, no V2 class bound to them.

## Legacy class folders (238)

Custom-class folders already in use. A V2 class never needs to avoid these names, because of the prefix (`v2-footer_component` is unrelated to `footer_component`), but the list shows what each page area was called, which helps when you audit a legacy page.

`2col-table`, `404`, `Footer`, `about-acad`, `about-academy`, `about-courses-academy`, `about-problem`, `acad`, `acad-module`, `acad-reward`, `acad-testimonial`, `academy-leaders`, `ad`, `ad-OSS`, `ad-developer-OSS`, `ad-footer`, `ad-header`, `ad-pgrm-unlock`, `ad-security`, `ad-testimonial`, `adlib-cta`, `adlibrary`, `ads`, `ai-agent`, `ai-agent-popup`, `all-agents`, `allpb`, `allplaybooks`, `alltech`, `arrow-icon`, `author`, `author-designation`, `authors`, `banner`, `bc-content`, `bc-header`, `blog`, `blog-author`, `blog-categories`, `blog-header`, `blog-related`, `blogs`, `blogs-header`, `btn-new`, `callout`, `capture-signal`, `career-at-reo`, `career-in-reo`, `career-perks`, `careers-header`, `carees-header`, `case-study`, `cli`, `cli-blind-spot`, `cohort`, `cohort-benefit`, `cohort-instructor`, `cohort-popup-modal`, `cohort-syllabus`, `colored`, `compare`, `contact`, `contact-header`, `conversation`, `conversation-cta`, `conversations`, `conversations-header`, `convos`, `cookie-manager1`, `cookie-manager2`, `country`, `cta`, `cta-new`, `culture-at-reo`, `customer-logos`, `data-sources`, `demo-header`, `devgtm-academy`, `devgtm-footer`, `devtool`, `download`, `elipses`, `empty-state`, `feature`, `features`, `filter`, `footer`, `for-whom-academy`, `form`, `fs-checkbox`, `fs-consent`, `fs-dropdown`, `fs-search`, `fs-toc`, `glosarry`, `glossary`, `glossary-hero`, `glossary-link`, `glossary-next-link`, `glossary-prev-link`, `gtmotion`, `gtmotion-comparison`, `gtmotion-testimonial`, `handbook`, `hero`, `hero-acad`, `hero-academy`, `hero-home`, `home`, `homer-header`, `icp-table`, `img`, `instructor`, `integrations`, `integrations-header`, `integrations-overview`, `integrationslider`, `intent-signals`, `journey`, `label`, `layout352`, `lead`, `lead-header`, `loop`, `lp`, `lp-2col-dark-header`, `lp-competition`, `lp-competitor`, `lp-header`, `lp-lead`, `lp-revenue-flow`, `lp-testimonials`, `lp-testimonials-slider`, `lp-testimonials-wrap`, `lp-wol`, `lvd-by-devs`, `mcp`, `modal-popup`, `module`, `more-stories`, `navbar`, `navbar-dropdown`, `newsletter`, `nvidia-header`, `other-authors`, `padding-section-integrations`, `partner`, `partner-list`, `partner-reo`, `partner-stories`, `pbcollections`, `pc`, `pc-header`, `play-icon`, `playbook`, `playbook-collections`, `playbook-content`, `playbook-header`, `playbook-modal`, `playbooks`, `policy`, `popup`, `popup-modal`, `pp`, `product`, `profile-build`, `ref-hero`, `refereel`, `referral-hero`, `referrel`, `related`, `related-ads`, `related-signals`, `remove-header`, `reo-build-in`, `reo-build-on`, `reo.dev`, `reonaut`, `reovscmnroom`, `report`, `reports`, `reports-header`, `resource`, `resource-list`, `resources`, `reviews`, `rl-styleguide`, `section`, `security`, `security-stnds`, `siganls-header`, `signal`, `signal-header`, `signal-sources`, `signals`, `signup-start-free`, `slider-arrow-icon`, `solo-partner`, `solution`, `solutions`, `solutions-reviews`, `solutions-testimonial`, `speaker`, `start-free`, `stories`, `stories-featured`, `stories-header`, `story`, `stylesystem`, `submit-refrrl`, `tables`, `talk-specialist`, `tech`, `tech-alternatives`, `tech-data`, `tech-faq`, `tech-header`, `tech-job`, `tech-mrkts`, `tech-table`, `tech-target`, `techfilters`, `technology`, `technology-header`, `testimonial`, `testinonials`, `the-problem`, `toc`, `tooltip`, `trust-by-gtms`, `usecases`, `usecases-content`, `usecases-testimonial`, `utility`, `wf-hs`, `wol`, `wol-header`, ` lp-lead`

## Components (85)

Instance counts are from the audit date. `Navbar *` and `Footer` variants are the ones every legacy page uses; the four `Navbar Dropdowns` are nested inside them.

| Group | Component | Instances | Props | Id |
|---|---|---|---|---|
| Ads LP Components | Ad Footer | 12 | 1 | `d614ffd6-3fc8-35a5-6dd2-94796b013564` |
| Ads LP Components | Ad Navbar Transparent | 2 | 0 | `3569d56a-ed4a-9810-06b0-f65b4b375a97` |
| Ads LP Components | Ad/ Book a Demo Calendly code | 1 | 0 | `19ddf7c8-05e6-cd34-0ef3-c842b3790b29` |
| Ads LP Components | Ad/ section logoblock | 9 | 0 | `1b3216f4-b221-e45c-f65f-548c24e2b800` |
| Ads LP Components | Ad/ section program | 10 | 3 | `5e2d95d0-3970-6361-e6cf-db0b65f90509` |
| Ads LP Components | Ad/ section security | 11 | 5 | `051fccb8-6595-42dc-5535-82453207f750` |
| Ads LP Components | Card: LP revenue flow section  | 4 | 5 | `8793f82e-d044-036b-958d-3f00bb1bbd51` |
| Ads LP Components | Dropdown Label | 47 | 2 | `f5867cdf-5ac4-8d17-5577-46eb9152d2d6` |
| Ads LP Components | Slide Item: LP testimonial | 16 | 7 | `9b2ddf1a-058d-37da-71a5-b2850bc0069c` |
| Cookie Banner | Cookie Reject | 1 | 0 | `46fc4c86-c4e7-2776-543a-8295137122ed` |
| Cookie Banner | Cookie Reject Banner Button | 1 | 0 | `12a35c0f-e947-ee1f-a188-6e34aa36d74f` |
| Custom Code | Book a Demo Calendly Widget Code | 2 | 0 | `9196b8db-2cb7-699f-78ff-eb1c91f3ab4c` |
| Custom Code | Global Styles | 104 | 0 | `ab488b17-f25a-fbf8-5f54-4a3955eb57e5` |
| Custom Code | Hidden Form Tracking Fields | 1 | 0 | `452436a2-73ae-98a9-10c0-568b20fb76e4` |
| Essentials |  Cohort Reward Card | 9 | 4 | `51eac747-36be-c158-14af-b42994c9eac7` |
| Essentials | banner content | 0 | 5 | `5f2013e2-5e12-b89f-83f3-763be3f87066` |
| Essentials | DevGTM Academy Card Testimonial | 12 | 13 | `cef23ec7-d9a4-70b4-a079-46d860af1f52` |
| Essentials | DevGTM Academy Feb Live Cohort Application | 2 | 2 | `264c055c-2b1e-c29e-1498-cc9b503c6286` |
| Essentials | DevGTM Academy/ Slider Card (Horizontal)  | 36 | 5 | `658ff6ea-00b3-d377-0fc6-13d7b6b1c53d` |
| Essentials | DevGTM Academy/slider card (Vertical) | 11 | 5 | `84bd5832-b401-296c-3077-f8bc8c6bb99b` |
| Essentials | Footer | 81 | 3 | `14fe3a36-ebb7-0aff-755d-2b70333dad1f` |
| Essentials | Footer - DevGTM Academy | 6 | 0 | `0637566a-488c-aa1b-8f5c-197de19566fe` |
| Essentials | image - absolute wrapper | 1 | 0 | `963468a1-73d7-97bc-8747-cfb325a4a1fe` |
| Essentials | Logos Component | 15 | 0 | `cf61fde0-8129-8974-f6ab-7afecd5530df` |
| Essentials | Nav | 10 | 0 | `dddb00db-e7aa-eb2d-b68c-d5b039a334d8` |
| Essentials | nav temp | 0 | 1 | `9dc93042-0b39-c979-95d7-122927901c56` |
| Essentials | Navbar Dark | 17 | 0 | `0cb940c7-b20b-9fa4-0754-0bf57fc12b03` |
| Essentials | Navbar Light | 64 | 2 | `0bc139d7-d99b-d82a-7d69-9d9d516bec8a` |
| Essentials | Navbar Light DevGTM | 6 | 5 | `41ff7300-eb51-6114-523a-9ea016b8d490` |
| Essentials | Navbar Transparent | 39 | 2 | `e3b96b26-f25f-a46d-f72b-327fb4feeb31` |
| Essentials | Navbar Transparent DevGTM | 1 | 2 | `c3cd5b6c-195c-a477-4f58-52aa36f3232f` |
| Essentials | Navbar White | 41 | 2 | `bb81fd43-1365-6c9f-5fd6-f63e1090abe5` |
| Essentials | Navbar White 100 DVH Bg Blend | 1 | 0 | `795ab824-3002-9826-1da5-2c420c2befdd` |
| Essentials | Navbar White DevGTM | 5 | 5 | `139f25d1-570e-2be8-2173-c04468331cbc` |
| Navbar Dropdowns | Customer Navbar Dropdown | 176 | 0 | `89d634bd-81c6-c18b-d99e-814b6250b3cd` |
| Navbar Dropdowns | Features Navbar Dropdown | 179 | 0 | `10ef23bd-fd9d-90e0-6615-6c6efb04cd7b` |
| Navbar Dropdowns | Resources Navbar Dropdown | 179 | 0 | `7691dee7-dd9b-1e4c-57ec-91de6a88075b` |
| Navbar Dropdowns | Solutions Navbar Dropdown | 179 | 0 | `04a97de1-9d0a-5a4f-2661-1517183c6152` |
| revamped components | Navbar Light (rewamped) | 5 | 3 | `1bb1233b-1679-9945-3fac-78b08b44e029` |
| revamped components | Navbar White (rewamped) | 5 | 2 | `72e81937-0cd7-f14e-b5e6-1ef9e1ea1959` |
| Sections | [section] customer-love | 2 | 7 | `a7bf3fee-653d-bab0-6bff-616e99e8f585` |
| Sections | Feature Item | 0 | 5 | `d11126ad-5bf4-ce1c-4c2d-f85367d28483` |
| Sections | Playbook Subscribe | 2 | 0 | `73402a9f-186c-35c1-49d0-2ea0f4ccba88` |
| Sections | Section Cohort Reward | 0 | 25 | `c8185587-2ca2-7688-2a6a-ac4b730bfb78` |
| Sections | Section CTA | 59 | 13 | `5777f7d4-1719-ee57-52ad-fc69ba955f15` |
| Sections | Section DevGTM CTA | 6 | 11 | `6b3bb843-7be7-b44e-e0e0-9ab7d990481f` |
| Sections | Section G2 Reviews | 1 | 0 | `0c6cba03-9d49-2abc-6344-d166ac1be8ff` |
| Sections | Section Header Light Center | 1 | 0 | `56c13503-b70d-9b52-44c5-2be6f91716c4` |
| Sections | Section Logos Colored | 6 | 1 | `50919260-2f1a-f1a7-d66a-52ce1296181e` |
| Sections | Section Logos Loop Colored | 1 | 0 | `49c53a52-9d6f-44d7-dcb0-a4c59a5ef746` |
| Sections | Section Logos Loop Grey | 26 | 1 | `4f70792b-7316-0385-17e4-da6e07c442eb` |
| Sections | Section WOL | 8 | 0 | `b5e56ef1-da09-cce3-bee6-90c392b6596d` |
| Sections | Section_CTA-devgtm-academy | 0 | 3 | `89d89d4d-6b3e-c4ab-5199-277344f39aea` |
| Sections | Testimonial Slider(Swiper.js) | 3 | 1 | `5c852abd-f077-051b-7b48-9d19cc41e11d` |
| Sections | wol_cta section | 1 | 4 | `4600b78c-8603-74a0-01e7-2f4018a25850` |
| Structures | Image Wrapper | 0 | 0 | `9bfe4e60-505f-9b07-6803-01353ec28737` |
| Structures | ps - Page Structure | 0 | 0 | `8639d770-4e3b-34c6-0cc4-856fa35e4118` |
| Structures | SS Structure | 9 | 0 | `364d5a19-b4bb-09c9-e330-4e35b06542dd` |
| UI Elements | [component] CTA rewamped | 4 | 11 | `22ff2306-c38f-039b-5577-c3aced6358be` |
| UI Elements | Badge | 1 | 1 | `cce68026-732f-26d5-f34f-cce885f0bdc3` |
| UI Elements | Banner | 64 | 5 | `5bd8c43f-dce6-0b02-d89d-6d4f33ff6221` |
| UI Elements | Blog Callout | 1 | 3 | `b4360858-24de-de1f-6c7e-1fff8ed78f18` |
| UI Elements | Button | 4 | 2 | `272515af-fbfc-3aad-7d14-8dc1f958ceb8` |
| UI Elements | Button v2 | 12 | 6 | `fc6a17d3-f64f-1b44-94bb-022103a7282c` |
| UI Elements | Chip Icon SVG | 1 | 2 | `9c7bb44e-047b-274b-13b1-1d1eeb04ad15` |
| UI Elements | faq element | 14 | 4 | `6d9a41f3-22db-31f6-04de-a15adcf8c3c0` |
| UI Elements | Label Chip | 12 | 5 | `7a42a819-fedc-4cf1-4028-9626ef3dc8cb` |
| UI Elements | Play Icon | 1 | 0 | `ba043960-8cb0-31c2-4a81-65880e358bc2` |
| UI Elements | Playbook Callout | 2 | 5 | `159b0272-4a7e-a062-5376-3648f9dde0b6` |
| UI Elements | referral page accordion item | 23 | 2 | `2c011ff5-44cb-5af2-bfb3-2613016cc062` |
| UI Elements | section divider | 17 | 1 | `6d276bc4-ff6b-c09c-9d66-769af8507bb3` |
| UI Elements | wol_testimonial-cards | 1 | 10 | `15041cca-6d41-3a69-db6d-9a78f0dba94e` |
| (none) | footer_content-top | 83 | 2 | `863cf660-c31a-13eb-b095-74e90fe74726` |
| (none) | Form Policy Check Field | 1 | 0 | `913a6723-3d90-aaba-6702-8c8c18524c0d` |
| (none) | Form Policy text | 90 | 0 | `f9ec1a12-11f3-60f4-915f-49313028da5f` |
| (none) | Navbar Ad | 0 | 0 | `1ad285ae-ed97-df2d-f1aa-6a67fc5095f8` |
| (none) | navbar ad sticky | 1 | 0 | `d5558659-c8c0-3a93-9246-736e33dc1caf` |
| (none) | Product Blog Component | 2 | 5 | `6224735b-181d-e0b1-d054-7e15ab722672` |
| (none) | Section Ad Library CTA Component | 2 | 0 | `00cd0704-6975-2b2a-c030-7c9d851579c6` |
| (none) | Section Dark Center | 1 | 0 | `1f11df98-c20b-55b6-ef0f-d4ef7d0db088` |
| (none) | Section Footer Without Form | 2 | 0 | `f0865be2-97b2-4982-81bb-7b73b31c53e9` |
| (none) | Section Signal Temp Remove | 1 | 19 | `6e8b3e28-638c-1a02-b2d5-fbcea049d6e6` |
| (none) | Signal Strength | 0 | 0 | `af31a7dd-639a-cc6d-9f80-95dc19e2e2b9` |
| (none) | Tech Table Filters | 1 | 0 | `39e0a4e8-3e77-f323-53e0-e6fc389a3ede` |
| (none) | Technology Filters Item | 352 | 3 | `74fb06ab-4613-ff29-f71c-fc8156d07d1d` |

Notes:

- `Button v2`, `Navbar Light (rewamped)`, `Navbar White (rewamped)`, `[component] CTA rewamped`, `nav temp`, `Section Signal Temp Remove` are legacy experiments, not part of the V2 namespace.
- `Form Policy text` (90 instances) and `Hidden Form Tracking Fields` show how legacy forms carry consent text and tracking fields. Read them when you rebuild a form.

## Pages

### Static pages (82)

`V2 slug` is the slug the new page gets while it is being built. Draft legacy pages are not live; rebuild them only if the lead asks.

| Legacy page | Page id | Live path | State | V2 slug |
|---|---|---|---|---|
| Home | `67e6b65fe328bc6b91324d32` | `/` | live | `home-v2` |
| 100m Profiles Audience Builder | `6a26ddf3663d063b11523223` | `/100m-profiles-audience-builder` | live | `100m-profiles-audience-builder-v2` |
| 100m Profiles Find the Right Buyer | `6a2a8ef8dc52d9c7f1980fc3` | `/100m-profiles-find-the-right-buyer` | live | `100m-profiles-find-the-right-buyer-v2` |
| Password | `67e6b65fe328bc6b91324d38` | `/401` | live | utility page: rebuilt in place, last batch |
| 404 | `67e6b65fe328bc6b91324d39` | `/404` | live | utility page: rebuilt in place, last batch |
| Agent Intent | `6a08003b3db94866981f8c82` | `/agent-intent` | live | `agent-intent-v2` |
| AI Agent Library | `6a0f3750201b58ccb75884b3` | `/ai-agent-library` | live | `ai-agent-library-v2` |
| All Playbooks | `67f246aa22455a5d04a5a8e3` | `/all-playbooks` | live | `all-playbooks-v2` |
| Archives & Components | `6800d6427edcb8924100d193` | `/archives-components` | draft | `archives-components-v2` |
| Blog | `67f245f82c96e4c56f635e00` | `/blog` | live | `blog-v2` |
| Book a Demo | `67f2444b22455a5d04a44121` | `/book-a-demo` | live | `book-a-demo-v2` |
| Book a Demo OSS Retargeting | `696ca85ee507967758e56a12` | `/book-a-demo-oss-retargeting` | live | `book-a-demo-oss-retargeting-v2` |
| Callouts | `6803b9cd54e3b65201c8cad3` | `/callouts` | draft | `callouts-v2` |
| Reo.Dev Careers | `6a4638bb6683e432065d8545` | `/careers` | live | `careers-v2` |
| Claude Connector | `69e70f6ae1a53a4773639197` | `/claude-connector` | live | `claude-connector-v2` |
| CLI Commands Ad Landing Page | `68740a07192bf0d798b85823` | `/cli-commands` | live | `cli-commands-v2` |
| Code Commands Ad Landing Page | `69c219a0fe2131b52897339f` | `/code-commands` | live | `code-commands-v2` |
| Competitor Fomo Ad landing page | `69d0b536adf0469714e49029` | `/competitor-fomo` | live | `competitor-fomo-v2` |
| Contact | `67f245e73ea707b7c65f20b8` | `/contact` | live | `contact-v2` |
| DevGTM Conversations | `67f248f33f5e55db67620e4c` | `/conversations` | live | `conversations-v2` |
| Cookie Policy | `691c606b86fc3bbc6cb19563` | `/cookie-policy` | live | `cookie-policy-v2` |
| Customer Privacy Policy | `694d0717cf638566883e4bb6` | `/customer-privacy-policy` | live | `customer-privacy-policy-v2` |
| Customer Stories | `67f245c310db00cd6a0c77e1` | `/customer-stories` | live | `customer-stories-v2` |
| Developer Buying Journey - Ad | `687788cd577768691b9f572f` | `/developer-buying-journey` | live | `developer-buying-journey-v2` |
| Developer Knowledge Graph | `6a2659c86c9323bf93599bb3` | `/developer-knowledge-graph` | live | `developer-knowledge-graph-v2` |
| DevGTM Academy | `68c84157918d0a71b85de964` | `/devgtm-academy` | draft | `devgtm-academy-v2` |
| DevGTM Academy Copy | `69282c6f1c6b4b6492486c89` | `/devgtm-academy-copy` | draft | `devgtm-academy-copy-v2` |
| About | `696f968ee6e961377c268945` | `/devgtm-academy/about` | draft | `about-v2` in folder `/devgtm-academy` |
| Live Cohort | `69653ed5fdf8b404aa12191a` | `/devgtm-academy/live-cohort` | draft | `live-cohort-v2` in folder `/devgtm-academy` |
| Self-paced Course | `69698ed9b2bd1fb272f26bbc` | `/devgtm-academy/modules` | draft | `modules-v2` in folder `/devgtm-academy` |
| Resources | `696fc2d3ab339ef02454c865` | `/devgtm-academy/resources` | draft | `resources-v2` in folder `/devgtm-academy` |
| DevGTM Ecosystem | `69ae9183de84e15d0cd7d340` | `/devgtm-ecosystem` | live | `devgtm-ecosystem-v2` |
| DevGTM Magazine | `69fc9ef85203f749e1078d81` | `/devgtm-magazine` | live | `devgtm-magazine-v2` |
| DevTools Ad Examples Library | `6832bfc255c69ed39e24ea60` | `/devtools-ad-examples` | live | `devtools-ad-examples-v2` |
| FAQ | `6929b4569a6d57fc14ed8089` | `/faq` | draft | `faq-v2` |
| Gateway | `6a8544e5d15242140b931072` | `/gateway` | live | `gateway-v2` |
| Integrations | `67f24744394c00c0b1ab1ecb` | `/integrations` | live | `integrations-v2` |
| Navbar | `681cc181c2bae7b88747bde6` | `/navbar` | draft | `navbar-v2` |
| Reo.Dev Modern DevGTM Brew Newsletter | `67f248223fcfae53e5bec79e` | `/newsletter` | live | `newsletter-v2` |
| Nvidia landing page | `6981b4829f2f949a442cc8d8` | `/nvidia-customer` | live | `nvidia-customer-v2` |
| OSS activity - Ad | `69679b01e28bbc7004b5e993` | `/oss-activity` | live | `oss-activity-v2` |
| Book a Demo OSS Intel | `696e602ddaa8fae5943cb67c` | `/oss-intel` | live | `oss-intel-v2` |
| Partner Directory | `6a907afbbbecf745b01aeb18` | `/partner-directory` | live | `partner-directory-v2` |
| DevGTM Playbooks | `67f2468e19e6c7de0a206134` | `/playbooks` | live | `playbooks-v2` |
| Privacy Policy | `67f2464480e9ecbd46c5efc4` | `/privacy-policy` | live | `privacy-policy-v2` |
| Remove | `690da0be97dc7468b1f08b19` | `/privacy-policy/remove` | live | `remove-v2` in folder `/privacy-policy` |
| Referral | `68b850c4708ac773922d3db4` | `/referral` | live | `referral-v2` |
| Referral Terms of Service | `68d2e55cf7a25c6e0b4bf552` | `/referral-tnc` | draft | `referral-tnc-v2` |
| Reo AI Agents | `6a0729e66469f1e78afc56a2` | `/reo-agents` | live | `reo-agents-v2` |
| Reo Claude Builder Challenge | `6a185ea0a5f68864d96eaf50` | `/reo-claude-builder-challenge` | live | `reo-claude-builder-challenge-v2` |
| Reo.dev vs Scarf Campaign ad landing page | `6903827bdf659d8786af8e1d` | `/reo-dev-vs-scarf-campaign` | live | `reo-dev-vs-scarf-campaign-v2` |
| Reo x Claude Connector | `6a4ca37d045f3ae106090a3a` | `/reo-mcp-claude-connector` | live | `reo-mcp-claude-connector-v2` |
| Partnerships | `6a5dce91c0a6a42dbf3e5fdf` | `/reo-partner-program` | live | `reo-partner-program-v2` |
| Reo vs Scarf 3 Ad Landing Page Copy | `686e38dd2fbecdafb7fc519a` | `/reo-vs-scarf` | live | `reo-vs-scarf-v2` |
| ReoDotDev vs Commonroom | `6819eff86ebd43e1888faf5f` | `/reodotdev-vs-commonroom` | live | `reodotdev-vs-commonroom-v2` |
| Reo.Dev vs Koala | `687943a552bb251516488e53` | `/reodotdev-vs-koala` | live | `reodotdev-vs-koala-v2` |
| Reo vs Scarf Ad Landing Page | `6864c1d4e6931e16d82288bb` | `/reodotdev-vs-scarf` | live | `reodotdev-vs-scarf-v2` |
| Reo vs Scarf Ad Landing Page Copy | `686e39716c902953986f0931` | `/reodotdev-vs-scarf-2` | draft | `reodotdev-vs-scarf-2-v2` |
| DevGTM Research Reports | `67f24968ca772d10c79e3c98` | `/reports` | live | `reports-v2` |
| Reo vs Scarf 2 Ad Landing Page | `686ca465fb6c1d10dc6205cb` | `/scarf-vs-reodotdev` | live | `scarf-vs-reodotdev-v2` |
| Signals | `684fd7e2d7f8d2b9a060c26b` | `/signals` | live | `signals-v2` |
| Start for Free landing page | `69bd0342526dd4b174a6cea6` | `/start-for-free-1` | live | `start-for-free-1-v2` |
| Start for Free 1 Signup | `69be3a69f97d1b957d64b57c` | `/start-for-free-1-signup` | live | `start-for-free-1-signup-v2` |
| New Static Page Template | `686d2afa701940c904ab5980` | `/static-template-slug-1751984876529` | draft | `static-template-slug-1751984876529-v2` |
| Style Guide | `67e6b65fe328bc6b91324d3a` | `/style-guide` | draft | `style-guide-v2` |
| Tables | `683805a414b4601e1db972ec` | `/tables` | draft | `tables-v2` |
| Reo.Dev Custom Tags Handbook | `67f247ccbca55282385dc437` | `/tags-handbook` | live | `tags-handbook-v2` |
| Talk Specialist | `6a91348b5ddb889386c081be` | `/talk-to-a-specialist` | live | `talk-to-a-specialist-v2` |
| Technology | `68d108746b7a2ebf395802e4` | `/technology` | live | `technology-v2` |
| Technology Categories | `690b84978e41b7ea28e279e4` | `/technology-categories` | live | `technology-categories-v2` |
| Terms of Service | `67f246543fdd55d2fc378012` | `/terms-of-service` | live | `terms-of-service-v2` |
| Testimonial Appwrite | `697b61e2539d031b030b0eef` | `/testimonial-appwrite` | live | `testimonial-appwrite-v2` |
| Testimonial Fluree | `697b62b59831f5d3ba43db33` | `/testimonial-fluree` | live | `testimonial-fluree-v2` |
| Testimonial Kubegrade | `697b5a448cb424c67e367bd4` | `/testimonial-kubegrade` | live | `testimonial-kubegrade-v2` |
| Testimonial Memgraph | `697b63613a0194a83284bc20` | `/testimonial-memgraph` | live | `testimonial-memgraph-v2` |
| Testimonial Unleash | `697b67aa02c7d9f4cc391179` | `/testimonial-unleash` | live | `testimonial-unleash-v2` |
| Testimonial Unstructured | `6979155e5f78078c98b95e09` | `/testimonial-unstructured` | live | `testimonial-unstructured-v2` |
| Trustcenter | `6987626ab4ddfdfdfce86d37` | `/trustcenter` | live | `trustcenter-v2` |
| Unbinded Tech | `691a48136182cc58941cc195` | `/unbinded-tech` | draft | `unbinded-tech-v2` |
| Unbinded tech - comp delete | `6932dbf90ecdaae308ef1b7b` | `/unbinded-tech---comp-delete` | draft | `unbinded-tech---comp-delete-v2` |
| Wall of love | `686e9a92056ca3acf2ce0e3b` | `/wall-of-love` | live | `wall-of-love-v2` |
| Website Privacy Policy | `694d06f69efc9173794223b8` | `/website-privacy-policy` | live | `website-privacy-policy-v2` |

### CMS collections and template pages (40)

Template pages cannot be duplicated, so each is redesigned through a static staging page named `template-[collection-slug]-v2` (see `pages-and-launch.md`).

| Collection | Collection id | Item URL base | Template page id |
|---|---|---|---|
| Solutions | `67f2450a73cf4cd238114af5` | `/solutions/…` | `67f2450a73cf4cd238114b49` |
| Reports | `67f24e013fcfae53e5c2ce0b` | `/report/…` | `67f24e013fcfae53e5c2ce3c` |
| Blogs | `67f24e2800b7a0c2b33cb448` | `/blog/…` | `67f24e2800b7a0c2b33cb47b` |
| Authors | `67f24e53c2541e7ba0fb1b3f` | `/author/…` | `67f24e53c2541e7ba0fb1b63` |
| Integrations | `67f25013eae41af65fefa97f` | `/integrations/…` | `67f25013eae41af65fefa998` |
| Playbook Collections | `67f250ddaf6e43269dca2233` | `/playbook-collection/…` | `67f250ddaf6e43269dca2250` |
| Playbooks | `67f250ebaa52ad4ca8e9d56a` | `/playbook/…` | `67f250ecaa52ad4ca8e9d5ce` |
| Callouts | `67f25102af6e43269dca3d42` | `/callout/…` | `67f25103af6e43269dca3d60` |
| Signals | `67f251193fcfae53e5c4e748` | `/signal/…` | `67f251193fcfae53e5c4e77c` |
| Speakers | `67f25178ac971640cdafe9c7` | `/speaker/…` | `67f25179ac971640cdafea00` |
| Podcasts | `67f251b7ac971640cdb0114e` | `/podcast/…` | `67f251b8ac971640cdb0115c` |
| Policies | `67f253a3394c00c0b1b32185` | `/policy/…` | `67f253a3394c00c0b1b321b1` |
| Customer Stories | `67f25418bca552823865348b` | `/customer-stories/…` | `67f25419bca5528238653496` |
| Features | `67f27685ebce38c643df99b0` | `/feature/…` | `67f27685ebce38c643df99c8` |
| Blog Categories | `67f376655652c20623c02797` | `/blog-category/…` | `67f376655652c20623c027ac` |
| Quotes | `67f3b55e7a92b5e2e9e5cf87` | `/quotes/…` | `67f3b55f7a92b5e2e9e5d0c7` |
| Reviews | `67f3b8c8b18b103979a0757b` | `/review/…` | `67f3b8c9b18b103979a07585` |
| Webinars | `6809df10c24ac45af784eea6` | `/webinar/…` | `6809df10c24ac45af784eeb8` |
| Demo Days | `6809e16e8fb333d4e534b8ff` | `/demo-day/…` | `6809e16e8fb333d4e534b911` |
| Ad examples | `6832dc8fe5b4f439621ebbad` | `/devtool-ad-examples/…` | `6832dc8fe5b4f439621ebbd7` |
| Ad types | `683ee9997b8af3a62fcd0579` | `/ad-types/…` | `683ee9997b8af3a62fcd0584` |
| Wall of Loves | `686d2d44fa574682f330982b` | `/wall-of-love/…` | `686d2d45fa574682f330984d` |
| Use Cases | `6872b9dfe60c8045124fbf49` | `/use-cases/…` | `6872b9dfe60c8045124fbf4d` |
| GTM Motions | `6873814bd9c584938d6ae0bd` | `/gtm-motion/…` | `6873814bd9c584938d6ae0c1` |
| Resources | `6876511844554e966aa92b8a` | `/resources/…` | `6876511944554e966aa92dcf` |
| Testimonial | `6884fb68c6245e5ad015638b` | `/testimonial/…` | `6884fb68c6245e5ad015638f` |
| Glossaries | `688b50c8524c27923adc6409` | `/developer-marketing-glossary/…` | `688b50c8524c27923adc640d` |
| Technologies | `68ca5e9bfe01c79b90bf7867` | `/technology/…` | `68ca5e9bfe01c79b90bf7876` |
| Technology Categories | `68ca5ebd7de9d5f0b261afe0` | `/technology-category/…` | `68ca5ebd7de9d5f0b261afe9` |
| People | `68ca5f487bbe8c861a94abef` | `/person/…` | `68ca5f487bbe8c861a94ac01` |
| Job functions | `68ca5f9b27f2d96a49961b90` | `/job-function/…` | `68ca5f9c27f2d96a49961b99` |
| Countries | `68ca5fc9ce63864d538532ab` | `/country/…` | `68ca5fcace63864d538532c7` |
| Companies | `68ca6b088fc92afddd871ec2` | `/company/…` | `68ca6b088fc92afddd871eca` |
| Contacts | `68d109bb24bf37c6e1d8618a` | `/contact/…` | `68d109bb24bf37c6e1d86197` |
| DevGTM Ecosystems | `68da9d618666f2e42c798e31` | `/devgtm-ecosystem/…` | `68da9d618666f2e42c798e62` |
| DevGTM Academies | `6978df6f5692884b35e482d1` | `/academy/…` | `6978df6f5692884b35e482d7` |
| Partner Directories | `6a92fe75a47c5a15d5a69429` | `/partner/…` | `6a92fe76a47c5a15d5a69430` |
| Partner CMS company logos | `6a93149c1a26e3c11eb70d51` | `/partner-directory-comapnies/…` | `6a93149c1a26e3c11eb70d61` |
| Contact Partners | `6a933a4a1b2b0d914d45926e` | `/contact-partners/…` | `6a933a4b1b2b0d914d459280` |
| Partner Categories | `6a9557ec50765dc393350ac9` | `/partner-categories/…` | `6a9557ec50765dc393350ae7` |

Draft legacy pages that look like scratch or reference pages (`archives-components`, `callouts`, `navbar`, `tables`, `style-guide`, `static-template-slug-…`, `unbinded-tech…`, `devgtm-academy-copy`) are not part of the redesign unless the lead says so.

## Before you rebuild a page

Read the legacy page first. Record each finding and the decision (carry over / rebuild / drop) in the build log.

1. **Metadata:** `data_pages_tool` → `get_page_metadata` (title, SEO title and description, Open Graph, draft state) and `query_pages_schema_markup` (JSON-LD).
2. **Page code:** `data_scripts_tool` → `get_page_freeform_code`. Legacy page code is real: Home alone has a Lottie play / pause controller, a prompt-card → textarea script and a fake-cursor animation. Legacy scripts select by **class** (`.lottie-control`, `.prompt-card`) and **id** (`#hero-lottie`, `#chatbot-textarea`); when you port one, rewrite the selectors to `data-v2-*` hooks and make it null-safe.
3. **Structure:** `data_element_tool` → `get_all_elements` with `depth` 3, then drill into sections. Note component instances and their props (content often lives in props).
4. **Embeds:** `query_elements` with `element_filter: { type: "HtmlEmbed" }`, then `data_element_settings_tool` → `get_settings` (`query_settings`, `value_type: "code"`) for each.
5. **Forms:** `query_elements` for `FormForm`. Record the form name, every field name, hidden fields, the redirect / action and the success message. Integrations (HubSpot classes `wf-hs_*`, Calendly widget components, tracking fields) depend on these names. Keep names identical in the V2 form unless the lead says the integration is being replaced.
6. **Attributes:** look for `fs-*` (Finsweet), `ms-*`, `data-*` and element ids on the legacy tree. An id that an external link or ad campaign anchors to (`/#pricing`) must exist on the V2 page too.
7. **CMS:** for Collection Lists, note the collection, filters, sort and limit. Read field slugs with `data_cms_tool` → `get_collection_details`; never assume a field name.
8. **Links in:** which legacy components link to this page (navbar, footer, CTA). They matter at launch (see `pages-and-launch.md`).
