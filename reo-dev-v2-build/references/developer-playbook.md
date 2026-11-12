# Developer playbook: building with Claude, day to day

For the developer who drives Claude, and for Claude, which follows the same protocol. The aim is that every session is small, checkable, and leaves a written trail the lead can review in a few minutes the next morning.

## The working agreement

- **You** (developer) choose the task, start the session, keep the Webflow Designer open, look at what Claude built, and say yes or no at the decision points below.
- **Claude** reads the skill, builds through the Webflow MCP, checks its own work, and writes the session report.
- **The lead** reviews the report and the page once a day, answers open questions, approves fonts, review builds and launches, and is the only person who publishes.

Nobody publishes, deletes legacy things, or changes site settings without the lead. If you are unsure whether something needs the lead, it does.

## One-time setup

1. Clone the repository and open the folder in Claude Code (desktop app or terminal). The `AGENTS.md` / `CLAUDE.md` files make Claude load the skill.
2. Connect the **Webflow MCP** and authorise it for the workspace that owns the Reo.Dev site. Check: ask Claude "List the Webflow sites you can see." It must show **Reo.Dev** (`67e6b65ee328bc6b91324c9a`).
3. Connect the **Figma MCP** with access to the design file. Check: ask Claude to take a screenshot of node `191:12340`.
4. Open the Reo.Dev site in the **Webflow Designer** in Chrome and leave that tab in the foreground while Claude works. Most build tools talk to the open Designer; if the tab is hidden they time out.
5. Read `SKILL.md` once yourself, top to bottom. It takes ten minutes and you will recognise it when Claude breaks a rule.

## The daily loop

1. **Start**: open the build log (`reo-dev/v2-build-log.md`) and yesterday's report (`reo-dev/reports/`). Read the lead's answers.
2. **Pick one task card** from `home-build-plan.md`, the next one not marked done. One card per session. Do not combine cards.
3. **Open the right page** in the Designer (the card says which).
4. **Paste the card's prompt** into a new Claude session. Add anything the lead answered that affects it.
5. **Let Claude plan first.** It should tell you what it is about to create. If the plan mentions a class without `v2-`, editing something legacy, or publishing, stop it.
6. **Watch the Designer** while it builds. You do not need to understand every call; you are looking for the page changing in the way the card describes.
7. **Check the result yourself** using the card's "You check" list, at Desktop, Tablet, Mobile L and Mobile in the Designer.
8. **Ask for the session report** if Claude has not written it (prompt below).
9. **Commit and push** the build log and report so the lead sees them.

Stop for the day at a finished card, not in the middle of one. A half-built section with an honest note is fine; a half-built section with no note is not.

## Prompts

Paste these as they are; replace the parts in brackets.

**Start any session**

> Use the reo-dev-v2-build skill. Follow its session-start steps, then tell me the current phase from the build log and what you plan to do for task [T08 Hero] before you write anything to Webflow.

**Build a section**

> Use the reo-dev-v2-build skill. Task [T09: Trusted By] from home-build-plan.md. Read the section in home-page-blueprint.md, then read the Figma node [1:408] (design context and screenshot). Build it on Home V2 after the previous section. Reuse existing v2- classes, lint new names before creating them, check all four breakpoints, then write the session report.

**Fix something you can see is wrong**

> On Home V2, in [section], [describe exactly what is wrong and at which breakpoint, e.g. "the three feature cards do not have equal height at Tablet"]. Compare with Figma node [id]. Find the cause before changing anything, tell me what it is, then fix it using v2- classes only.

**When Claude seems lost or keeps retrying**

> Stop. Do not make any more writes. Re-query the current state of [the element / the page] and tell me what exists, what you were trying to do, and what failed. Then propose one next step and wait.

**End of session**

> Write the session report to reo-dev/reports/[YYYY-MM-DD]-[task].md using assets/session-report-template.md, update reo-dev/v2-build-log.md, and run the name linter. Tell me anything you could not verify.

**Daily check for drift**

> Run the reo-dev-v2-build verification: dump all styles, run scripts/lint_v2_names.py with --list, and confirm Home V2 has no legacy class or component, is still draft and has sitemap indexing off. Report only; change nothing.

## Permission prompts: what to allow and what to refuse

Claude asks before many tool calls. Use this table.

| Claude wants to… | Answer |
|---|---|
| Read anything in Webflow or Figma (get, list, query, search, snapshot) | **Allow** |
| Create or update a style whose name starts with `v2-`, or an `is-` combo on a `v2-` base | **Allow** |
| Create variables, modes or collections named `V2 …` | **Allow** (Phase 0 tasks only) |
| Create or edit elements on a page whose name ends in ` V2`, or inside a `V2 …` component | **Allow** |
| Upload an asset whose name starts with `v2-` | **Allow** |
| Upload fonts | Allow **only** after the lead has said yes |
| Create a page | Allow if the slug ends in `-v2`, it is draft, and the card asks for it |
| Run a script from the skill's `scripts/` folder, or `git` add / commit / push of the log and reports | **Allow** |
| `update_style`, `rename_style` or `remove_style` on a name **without** `v2-` | **Refuse.** This edits the live site's design. |
| Anything on a legacy page, legacy component, legacy variable, or a tag style (`body`, `h1`, `a` …) | **Refuse** |
| `publish_site`, `publish_collection_items`, or any "publish" | **Refuse**, always. Tell the lead. |
| `set_site_freeform_code`, `set_site_scripts`, anything "site" level | **Refuse** |
| `remove_element`, `delete_…`, `unregister_component`, `batch_delete_…` | **Refuse** unless it is clearly something built in the V2 work, and you understand why |
| `update_page_settings` on a page that is not a ` V2` page; any slug change | **Refuse.** Slug changes are launch steps. |
| Create, update or delete CMS collections, fields or items | **Refuse** and ask the lead |

When you refuse, tell Claude why in one line ("that is a legacy class, use a v2- class"). It will usually correct itself.

## Stop and call the lead when

- Claude says it changed, renamed or deleted something legacy, even if it says it reverted it.
- The live site looks different after a session (check reo.dev once at the end of the day).
- The linter reports classes that are neither legacy nor `v2-`, and they are not yours.
- A task needs a design decision that has no default in the blueprint.
- Claude asks to publish, or says a page "is live".
- The Webflow MCP shows a different site, or cannot see Reo.Dev.
- You have refused the same request three times in one session.

## Common problems

| Symptom | Likely cause | What to do |
|---|---|---|
| Tool calls time out | Designer tab in the background, or the Designer is on a different site | Bring the tab forward, reload the Designer, ask Claude to re-query before retrying |
| New text shows in the wrong font (Geologica or Inter) | A heading or text element has no `v2-` class, so the legacy tag style applies | Ask Claude to find elements without a `v2-` class on the page |
| A link turns purple or underlines on hover | The link class has no `:hover` state, so the legacy `a:hover` shows | Ask Claude to add a hover state to that `v2-` class |
| Text is white on white (or dark on dark) | A light card inside a blue or black section without `v2-theme-light` | Add `v2-theme-light` to the card |
| Sizes look slightly off against Figma everywhere | A legacy component or the legacy Global Styles is on the page | Ask Claude to list component instances on the page; remove the legacy one |
| An element got the old purple button | `class="button"` slipped into the HTML Claude sent | Ask Claude to replace it with `v2-button` and to lint its HTML first |
| Fonts look wrong only in Claude's snapshot | Snapshots are not a browser | Ignore the snapshot for fonts; check in the Designer and later on the review build |
| Images are blank in the Designer | Newly uploaded assets need a Designer reload | Reload the Designer tab |
| Two copies of a class, one ending in `-2` | A create call ran twice | Ask Claude to find and remove the unused duplicate it just created |
| Spacing does not change at Tablet or Mobile | The variable modes are not bound on `v2-page-wrapper`, or the element is outside it | Ask Claude to check `get_style_variable_modes` on `v2-page-wrapper` |

## What "done" means for a card

- It looks like Figma at Desktop, Tablet, Mobile L and Mobile in the Designer.
- Claude's report lists what it created, with element or class names you can find in the Designer.
- The linter is clean.
- Anything not verified, and every default taken on an open design question, is written down.
- The build log's status table is updated.

"It looks right at desktop" is not done.

## Habits that save a day

- One session, one card. Long sessions drift; Claude loses track of what it created.
- Start a **new** Claude session for each card, so it re-reads the skill and the log.
- Give Claude the Figma **node id**, not a description of the section.
- When something looks wrong, say where and at what width. "It's broken" costs three rounds.
- Never fix things by hand in the Designer without writing it in the report; Claude and the lead need to know.
- Do not rename classes by hand. If a name is wrong, ask Claude to rename it and re-run the linter.
- Commit the log and report every day, even on a bad day.
