---
name: verlagsredaktion
description: "verlagsredaktion: Verlagsdesk fuer juristische und fachliche Verlage: Eingangskorb, Manuskript, Redaktion, Rechtecheck, Zitate, Bildrechte, Autorenkommunikation, Heftplanung, Buchprojekte, Satzfahnen, Metadaten, Marketing und Produktionsuebergabe. Use this opencode router for verlagsredaktion requests; it selects source skills through skills-index/verlagsredaktion.md and then reads the matching SKILL.md files."
---

# verlagsredaktion opencode skill router

> Generated router for the source plugin `verlagsredaktion`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `verlagsredaktion/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/verlagsredaktion.md`
- Source skill root: `verlagsredaktion/skills/`
- Source skills: 54

Plugin description: Verlagsdesk fuer juristische und fachliche Verlage: Eingangskorb, Manuskript, Redaktion, Rechtecheck, Zitate, Bildrechte, Autorenkommunikation, Heftplanung, Buchprojekte, Satzfahnen, Metadaten, Marketing und Produktionsuebergabe.

## Routing workflow

1. Read `skills-index/verlagsredaktion.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `verlagsredaktion/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
