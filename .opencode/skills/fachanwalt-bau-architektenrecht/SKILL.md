---
name: fachanwalt-bau-architektenrecht
description: "fachanwalt-bau-architektenrecht: Plugin Fachanwalt für Bau- und Architektenrecht. BGB Werkvertrag VOB-A VOB-B VOB-C HOAI Bauordnungsrecht. Bauvertrag Maengelhaftung Abnahme Vergaberecht. Schnittstellen Plugin fachanwalt-vergaberecht kanzlei-allgemein. Use this opencode router for fachanwalt-bau-architektenrecht requests; it selects source skills through skills-index/fachanwalt-bau-architektenrecht.md and then reads the matching SKILL.md files."
---

# fachanwalt-bau-architektenrecht opencode skill router

> Generated router for the source plugin `fachanwalt-bau-architektenrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `fachanwalt-bau-architektenrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/fachanwalt-bau-architektenrecht.md`
- Source skill root: `fachanwalt-bau-architektenrecht/skills/`
- Source skills: 54

Plugin description: Plugin Fachanwalt für Bau- und Architektenrecht. BGB Werkvertrag VOB-A VOB-B VOB-C HOAI Bauordnungsrecht. Bauvertrag Maengelhaftung Abnahme Vergaberecht. Schnittstellen Plugin fachanwalt-vergaberecht kanzlei-allgemein.

## Routing workflow

1. Read `skills-index/fachanwalt-bau-architektenrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `fachanwalt-bau-architektenrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
