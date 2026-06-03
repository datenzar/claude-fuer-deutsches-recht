---
name: factoring-recht
description: "factoring-recht: Super-Plugin für Factoring, Forderungskauf, Aufsichtsrecht, Vertragsgestaltung, Debitorenkommunikation, Insolvenz- und Sanierungsfragen. Use this opencode router for factoring-recht requests; it selects source skills through skills-index/factoring-recht.md and then reads the matching SKILL.md files."
---

# factoring-recht opencode skill router

> Generated router for the source plugin `factoring-recht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `factoring-recht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/factoring-recht.md`
- Source skill root: `factoring-recht/skills/`
- Source skills: 62

Plugin description: Super-Plugin für Factoring, Forderungskauf, Aufsichtsrecht, Vertragsgestaltung, Debitorenkommunikation, Insolvenz- und Sanierungsfragen.

## Routing workflow

1. Read `skills-index/factoring-recht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `factoring-recht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
