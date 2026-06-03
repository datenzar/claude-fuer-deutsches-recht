---
name: commercial-courts-deutschland
description: "commercial-courts-deutschland: Commercial-Courts-Plugin für englischsprachige Wirtschaftsverfahren in Deutschland: Zuständigkeit, Wahlklauseln, Klage, Case Management, Beweis, Geheimnisschutz, Wortprotokoll/Transcript, Rechtsmittel, BGH, Kosten, Vollstreckung und bilingualer Schriftsatz-/Hearing-Workflow. Use this opencode router for commercial-courts-deutschland requests; it selects source skills through skills-index/commercial-courts-deutschland.md and then reads the matching SKILL.md files."
---

# commercial-courts-deutschland opencode skill router

> Generated router for the source plugin `commercial-courts-deutschland`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `commercial-courts-deutschland/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/commercial-courts-deutschland.md`
- Source skill root: `commercial-courts-deutschland/skills/`
- Source skills: 57

Plugin description: Commercial-Courts-Plugin für englischsprachige Wirtschaftsverfahren in Deutschland: Zuständigkeit, Wahlklauseln, Klage, Case Management, Beweis, Geheimnisschutz, Wortprotokoll/Transcript, Rechtsmittel, BGH, Kosten, Vollstreckung und bilingualer Schriftsatz-/Hearing-Workflow.

## Routing workflow

1. Read `skills-index/commercial-courts-deutschland.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `commercial-courts-deutschland/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
