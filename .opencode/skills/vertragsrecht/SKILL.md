---
name: vertragsrecht
description: "vertragsrecht: Vertragsrecht – Lieferanten- und Vertriebsverträge, AGB §§ 305 ff. BGB, NDA, SaaS-/MSA-Review, Renewal-Tracking, Eskalations-Routing, Business-Zusammenfassungen. Use this opencode router for vertragsrecht requests; it selects source skills through skills-index/vertragsrecht.md and then reads the matching SKILL.md files."
---

# vertragsrecht opencode skill router

> Generated router for the source plugin `vertragsrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `vertragsrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/vertragsrecht.md`
- Source skill root: `vertragsrecht/skills/`
- Source skills: 54

Plugin description: Vertragsrecht – Lieferanten- und Vertriebsverträge, AGB §§ 305 ff. BGB, NDA, SaaS-/MSA-Review, Renewal-Tracking, Eskalations-Routing, Business-Zusammenfassungen.

## Routing workflow

1. Read `skills-index/vertragsrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `vertragsrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
