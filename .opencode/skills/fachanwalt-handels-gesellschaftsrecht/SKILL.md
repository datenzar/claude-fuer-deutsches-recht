---
name: fachanwalt-handels-gesellschaftsrecht
description: "fachanwalt-handels-gesellschaftsrecht: Plugin Fachanwalt für Handels- und Gesellschaftsrecht nach FAO § 14i. HGB. AktG. GmbHG. PartGG. UmwG. Geschäftsführerhaftung §§ 43 GmbHG 93 AktG. Gesellschafterstreit Beschlussanfechtung. Handelsvertreterausgleich § 89b HGB. MoPeG GbR seit 2024. Schnittstellen kanzlei-allgemein. Use this opencode router for fachanwalt-handels-gesellschaftsrecht requests; it selects source skills through skills-index/fachanwalt-handels-gesellschaftsrecht.md and then reads the matching SKILL.md files."
---

# fachanwalt-handels-gesellschaftsrecht opencode skill router

> Generated router for the source plugin `fachanwalt-handels-gesellschaftsrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `fachanwalt-handels-gesellschaftsrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/fachanwalt-handels-gesellschaftsrecht.md`
- Source skill root: `fachanwalt-handels-gesellschaftsrecht/skills/`
- Source skills: 54

Plugin description: Plugin Fachanwalt für Handels- und Gesellschaftsrecht nach FAO § 14i. HGB. AktG. GmbHG. PartGG. UmwG. Geschäftsführerhaftung §§ 43 GmbHG 93 AktG. Gesellschafterstreit Beschlussanfechtung. Handelsvertreterausgleich § 89b HGB. MoPeG GbR seit 2024. Schnittstellen kanzlei-allgemein.

## Routing workflow

1. Read `skills-index/fachanwalt-handels-gesellschaftsrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `fachanwalt-handels-gesellschaftsrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
