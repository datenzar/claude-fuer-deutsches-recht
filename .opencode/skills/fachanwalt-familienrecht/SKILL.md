---
name: fachanwalt-familienrecht
description: "fachanwalt-familienrecht: Plugin Fachanwalt für Familienrecht. Orientierung Normen Mandate Fristen Literatur. Familiengericht FamFG Scheidung Sorge Umgang Unterhalt Zugewinn Ehevertrag eingetragene Lebenspartnerschaft. Ergaenzend zum Plugin kanzlei-allgemein. Use this opencode router for fachanwalt-familienrecht requests; it selects source skills through skills-index/fachanwalt-familienrecht.md and then reads the matching SKILL.md files."
---

# fachanwalt-familienrecht opencode skill router

> Generated router for the source plugin `fachanwalt-familienrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `fachanwalt-familienrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/fachanwalt-familienrecht.md`
- Source skill root: `fachanwalt-familienrecht/skills/`
- Source skills: 109

Plugin description: Plugin Fachanwalt für Familienrecht. Orientierung Normen Mandate Fristen Literatur. Familiengericht FamFG Scheidung Sorge Umgang Unterhalt Zugewinn Ehevertrag eingetragene Lebenspartnerschaft. Ergaenzend zum Plugin kanzlei-allgemein.

## Routing workflow

1. Read `skills-index/fachanwalt-familienrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `fachanwalt-familienrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
