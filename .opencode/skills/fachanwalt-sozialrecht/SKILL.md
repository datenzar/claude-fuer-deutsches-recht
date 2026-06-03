---
name: fachanwalt-sozialrecht
description: "fachanwalt-sozialrecht: Plugin Fachanwalt für Sozialrecht nach FAO § 11. SGB I-XII und Sozialgerichtsbarkeit SGG. Widerspruch § 84 SGG Klage § 87 SGG Eilantrag § 86b SGG. Buergergeld Erwerbsminderung GdB Pflegegrad Hilfsmittel Eingliederungshilfe. Bescheidanalyse Akteneinsicht PKH Fristenbuch. Use this opencode router for fachanwalt-sozialrecht requests; it selects source skills through skills-index/fachanwalt-sozialrecht.md and then reads the matching SKILL.md files."
---

# fachanwalt-sozialrecht opencode skill router

> Generated router for the source plugin `fachanwalt-sozialrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `fachanwalt-sozialrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/fachanwalt-sozialrecht.md`
- Source skill root: `fachanwalt-sozialrecht/skills/`
- Source skills: 83

Plugin description: Plugin Fachanwalt für Sozialrecht nach FAO § 11. SGB I-XII und Sozialgerichtsbarkeit SGG. Widerspruch § 84 SGG Klage § 87 SGG Eilantrag § 86b SGG. Buergergeld Erwerbsminderung GdB Pflegegrad Hilfsmittel Eingliederungshilfe. Bescheidanalyse Akteneinsicht PKH Fristenbuch.

## Routing workflow

1. Read `skills-index/fachanwalt-sozialrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `fachanwalt-sozialrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
