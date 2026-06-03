---
name: fachanwalt-urheber-medienrecht
description: "fachanwalt-urheber-medienrecht: Plugin Fachanwalt für Urheber- und Medienrecht. UrhG UWG KUG Recht am eigenen Bild Presserecht Persoenlichkeitsrecht Medienstaatsvertrag. Schnittstellen Plugin gewerblicher-rechtsschutz verlagsredaktion kanzlei-allgemein. Use this opencode router for fachanwalt-urheber-medienrecht requests; it selects source skills through skills-index/fachanwalt-urheber-medienrecht.md and then reads the matching SKILL.md files."
---

# fachanwalt-urheber-medienrecht opencode skill router

> Generated router for the source plugin `fachanwalt-urheber-medienrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `fachanwalt-urheber-medienrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/fachanwalt-urheber-medienrecht.md`
- Source skill root: `fachanwalt-urheber-medienrecht/skills/`
- Source skills: 54

Plugin description: Plugin Fachanwalt für Urheber- und Medienrecht. UrhG UWG KUG Recht am eigenen Bild Presserecht Persoenlichkeitsrecht Medienstaatsvertrag. Schnittstellen Plugin gewerblicher-rechtsschutz verlagsredaktion kanzlei-allgemein.

## Routing workflow

1. Read `skills-index/fachanwalt-urheber-medienrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `fachanwalt-urheber-medienrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
