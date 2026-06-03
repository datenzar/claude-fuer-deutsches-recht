---
name: parteienrecht-parteiorganisation
description: "parteienrecht-parteiorganisation: Parteienrechts- und Parteiorganisations-Plugin für formale Parteiarbeit: Parteiengesetz, Satzung, Mitgliederrechte, Parteitage, Kreis- und Bezirksversammlungen, Kandidatenaufstellung, Wahlvorschläge, Parteigerichte, Spenden, Rechenschaft, Abgeordnetenrecht und Wahlleiterkommunikation. Use this opencode router for parteienrecht-parteiorganisation requests; it selects source skills through skills-index/parteienrecht-parteiorganisation.md and then reads the matching SKILL.md files."
---

# parteienrecht-parteiorganisation opencode skill router

> Generated router for the source plugin `parteienrecht-parteiorganisation`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `parteienrecht-parteiorganisation/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/parteienrecht-parteiorganisation.md`
- Source skill root: `parteienrecht-parteiorganisation/skills/`
- Source skills: 75

Plugin description: Parteienrechts- und Parteiorganisations-Plugin für formale Parteiarbeit: Parteiengesetz, Satzung, Mitgliederrechte, Parteitage, Kreis- und Bezirksversammlungen, Kandidatenaufstellung, Wahlvorschläge, Parteigerichte, Spenden, Rechenschaft, Abgeordnetenrecht und Wahlleiterkommunikation.

## Routing workflow

1. Read `skills-index/parteienrecht-parteiorganisation.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `parteienrecht-parteiorganisation/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
