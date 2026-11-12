# Reo.dev Webflow development

This repository exists for one job: building the redesigned Reo.dev website inside the live Reo.Dev Webflow project (site `67e6b65ee328bc6b91324c9a`) with the Webflow MCP.

## Before any Reo.dev or Webflow task

1. Load and follow `reo-dev-v2-build/SKILL.md`. Read the reference file it points to for the task; do not work from memory of it.
2. Read `reo-dev/v2-build-log.md` for the current phase, ids and open questions. Update it at the end of the session.
3. Work one task card at a time from `reo-dev-v2-build/references/home-build-plan.md`. End every session that wrote to Webflow with a report in `reo-dev/reports/` (template: `reo-dev-v2-build/assets/session-report-template.md`).

The developer is new to Webflow and the lead reviews from your reports, so check your own work, say what you will do before you write, and never invent content or features.

## Rules that always apply

- Only write to site `67e6b65ee328bc6b91324c9a`. If the Webflow MCP cannot reach it, say so and stop.
- Add, never modify: legacy classes, tag styles, variables, components, pages and site code are read-only.
- Every new class starts with `v2-`; combos are `is-*`. Run `reo-dev-v2-build/scripts/lint_v2_names.py` on names before sending them.
- Never publish, to any domain, without the lead's explicit confirmation in the chat for that publish.
- New pages are draft, on a `-v2` slug, with sitemap indexing off.
- No secrets in this repository: no API tokens, site tokens or OAuth credentials.
