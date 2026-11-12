# Reo.dev Webflow development skill

An agent skill for building the **redesigned Reo.dev website inside the existing live Reo.Dev Webflow project**, using the Webflow MCP. It is specific to this one project; it is not a general Webflow skill.

| | |
|---|---|
| Webflow site | Reo.Dev, id `67e6b65ee328bc6b91324c9a` (serves reo.dev) |
| Figma | `GuQCrycX2KDwenWDwW7FIT` ("Reo.dev (Final)") |
| Class system | Client-First V3 conventions with a `v2-` prefix |
| Skill | [`reo-dev-v2-build/`](reo-dev-v2-build/SKILL.md) |
| Progress log | [`reo-dev/v2-build-log.md`](reo-dev/v2-build-log.md) |

## Why this exists

reo.dev is live in this Webflow project and is being redesigned in batches. Building the new site in a second project would 404 every page that had not moved yet, so the new site is built **beside the old one, in the same project**. That only works if nothing new collides with, or changes, anything old. The skill makes an agent work that way:

- **Add, never modify.** Legacy classes, tag styles, variables, components, pages and site code are read-only.
- **Everything new is namespaced.** `v2-` on every class, `V2 …` variable collections and components, `-v2` page slugs.
- **Nothing goes live by accident.** New pages are draft, out of the index, on a `-v2` slug. The agent never publishes.
- **Launch is a slug swap**, run by the lead, one batch at a time.
- **Cleanup at the end** deletes the legacy build and strips the `v2-` marker mechanically.

## Start here

**If you are the developer:** read [`developer-playbook.md`](reo-dev-v2-build/references/developer-playbook.md) (setup, the daily loop, prompts to paste, which permission prompts to allow or refuse), then work through [`home-build-plan.md`](reo-dev-v2-build/references/home-build-plan.md) one task card per Claude session, starting at T00.

**If you are reviewing:** read [`review-guide.md`](reo-dev-v2-build/references/review-guide.md). Each session leaves a report in [`reo-dev/reports/`](reo-dev/reports/) and updates the [build log](reo-dev/v2-build-log.md); design questions waiting on you are listed there with the default being built.

## What is in the skill

| File | What it covers |
|---|---|
| [`SKILL.md`](reo-dev-v2-build/SKILL.md) | Hard rules, session start and end, build workflow, verification checklist |
| [`references/home-page-blueprint.md`](reo-dev-v2-build/references/home-page-blueprint.md) | The home page, pre-read from Figma: node ids per breakpoint, class tree, copy, assets and responsive behaviour for every section, plus 16 open design questions with defaults |
| [`references/home-build-plan.md`](reo-dev-v2-build/references/home-build-plan.md) | Task cards T00–T20: prompt to paste, what the developer checks, done criteria, what the lead looks at |
| [`references/developer-playbook.md`](reo-dev-v2-build/references/developer-playbook.md) | How to run sessions with Claude: daily loop, prompts, allow / refuse table, common problems |
| [`references/review-guide.md`](reo-dev-v2-build/references/review-guide.md) | The lead's 15-minute daily review, red flags, review-build checklist |
| [`references/naming.md`](reo-dev-v2-build/references/naming.md) | The full naming system: classes, combos, variables, components, pages, assets, interactions |
| [`references/legacy-inventory.md`](reo-dev-v2-build/references/legacy-inventory.md) | Audit of the live project (2026-11-12): pages and ids, components, variables, CMS collections, site code, and what a new page inherits |
| [`references/v2-foundation.md`](reo-dev-v2-build/references/v2-foundation.md) | Phase 0: fonts, tokens, global classes, page shell, global embed |
| [`references/pages-and-launch.md`](reo-dev-v2-build/references/pages-and-launch.md) | Creating pages, linking rules, CMS templates, review builds, launch runbook, rollback |
| [`references/cleanup-runbook.md`](reo-dev-v2-build/references/cleanup-runbook.md) | End-of-project removal of the legacy build and the rename |
| [`references/mcp-gotchas.md`](reo-dev-v2-build/references/mcp-gotchas.md) | Webflow MCP behaviours that cause mistakes |
| [`scripts/lint_v2_names.py`](reo-dev-v2-build/scripts/lint_v2_names.py) | Checks class names against the rules and against a snapshot of every legacy style; `--list` prints every V2 class by folder |
| `scripts/woff2info.mjs`, `scripts/upload_font.py` | Font inspection and upload helpers |
| `assets/legacy-style-baseline.json` | Ids of all 3,494 legacy styles, used by the linter |
| `assets/session-report-template.md`, `assets/build-log-template.md` | The report Claude writes after every session, and the project log |

## Setup

You need the Webflow MCP connected and authorised for the workspace that owns the Reo.Dev site, and the Webflow Designer open on that site while you work. Figma MCP access to the design file is needed for building from Figma.

### Option A: work from this repo (simplest)

Clone it and open the folder in Claude Code or Codex. `AGENTS.md` / `CLAUDE.md` at the root tell the agent to load the skill for any Reo.dev task, and the build log is already in place.

```bash
git clone https://github.com/PIXELUPLABS/webflow-dev-skill.git
```

### Option B: install the skill into your own setup

Claude Code, for one project:

```bash
mkdir -p .claude/skills && cp -R webflow-dev-skill/reo-dev-v2-build .claude/skills/
```

Claude Code, for every project:

```bash
mkdir -p ~/.claude/skills && cp -R webflow-dev-skill/reo-dev-v2-build ~/.claude/skills/
```

Codex and other agents that read `.agents/skills/`:

```bash
mkdir -p .agents/skills && cp -R webflow-dev-skill/reo-dev-v2-build .agents/skills/
```

Claude desktop or claude.ai (upload as a skill): zip the folder and upload the archive.

```bash
cd webflow-dev-skill && zip -r reo-dev-v2-build.skill reo-dev-v2-build -x '*/agents/*'
```

With option B, copy [`reo-dev/v2-build-log.md`](reo-dev/v2-build-log.md) into your working folder at the same path. The skill reads and updates it every session.

## Using it

Ask for the work in plain language and name the page or Figma node:

> Build the Reo.dev V2 foundation (Phase 0).
>
> Build the hero section of Home V2 from this Figma node: …
>
> Prepare batch 1 (Home, Book a Demo) for launch.

The agent should begin every session by reading the build log and checking which phase is done. If it starts creating classes without a `v2-` prefix, or proposes editing a legacy class, stop it: the skill was not loaded.

Check names at any time:

```bash
python3 reo-dev-v2-build/scripts/lint_v2_names.py --names "v2-button is-secondary" v2-hero_component
```

## Naming at a glance

| Thing | Convention | Example |
|---|---|---|
| Classes | `v2-` + Client-First V3 name | `v2-padding-global`, `v2-section_hero`, `v2-hero_component` |
| Combos | `is-*`, no prefix | `v2-button is-secondary` |
| Variable collections | `V2 ` + name | `V2 Theme` |
| Components | `V2 ` + name | `V2 Navbar` |
| Pages | name + ` V2`, slug + `-v2` | `Home V2` at `home-v2` |

"V2" means version 2 of the Reo.dev site. It does not mean Client-First V2.

## Status

As of 2026-11-12 nothing has been built in the live project. The audits behind this skill (the Webflow project and the Figma home page section `1:285`) were read-only. Open decisions for the project lead are listed in the [build log](reo-dev/v2-build-log.md): seven workflow questions and sixteen home page design questions, each with the default that will be built until answered.

## Keeping it current

- The legacy inventory is a snapshot. The client's team still edits the legacy site, so confirm ids with the MCP before relying on them.
- When a rule changes, change it in the skill and push, so every developer and agent picks it up.
- Commit the build log after each working session.

This repository is private. It contains internal ids for a client project; do not make it public.
