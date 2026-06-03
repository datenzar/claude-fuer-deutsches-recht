---
name: fachanwalt-arbeitsrecht
description: "fachanwalt-arbeitsrecht: Fachanwalt-Arbeitsrecht nach FAO Paragraf 10: KSchG, BetrVG, TzBfG, AGG, EntgTranspG, Urlaub, Betriebsrat, Befristung und Vergleichspraxis. Rechtsprechung nur mit Datum, Aktenzeichen und verifizierter Quelle. Use this opencode router for fachanwalt-arbeitsrecht requests; it selects source skills through skills-index/fachanwalt-arbeitsrecht.md and then reads the matching SKILL.md files."
---

# fachanwalt-arbeitsrecht opencode skill router

> Generated router for the source plugin `fachanwalt-arbeitsrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `fachanwalt-arbeitsrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/fachanwalt-arbeitsrecht.md`
- Source skill root: `fachanwalt-arbeitsrecht/skills/`
- Source skills: 54

Plugin description: Fachanwalt-Arbeitsrecht nach FAO Paragraf 10: KSchG, BetrVG, TzBfG, AGG, EntgTranspG, Urlaub, Betriebsrat, Befristung und Vergleichspraxis. Rechtsprechung nur mit Datum, Aktenzeichen und verifizierter Quelle.

## Routing workflow

1. Read `skills-index/fachanwalt-arbeitsrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `fachanwalt-arbeitsrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
