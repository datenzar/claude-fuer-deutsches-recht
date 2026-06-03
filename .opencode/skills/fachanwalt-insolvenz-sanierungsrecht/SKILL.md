---
name: fachanwalt-insolvenz-sanierungsrecht
description: "fachanwalt-insolvenz-sanierungsrecht: Plugin Fachanwalt für Insolvenz- und Sanierungsrecht nach FAO § 14. InsO Eroeffnung Antragspflicht § 15a Gläubigerantrag § 14 InsO. StaRUG Restrukturierungsplan. Insolvenzanfechtung §§ 129 ff. InsO. Schnittstellen insolvenzrecht und steuerrecht-anwalt-und-berater. Use this opencode router for fachanwalt-insolvenz-sanierungsrecht requests; it selects source skills through skills-index/fachanwalt-insolvenz-sanierungsrecht.md and then reads the matching SKILL.md files."
---

# fachanwalt-insolvenz-sanierungsrecht opencode skill router

> Generated router for the source plugin `fachanwalt-insolvenz-sanierungsrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `fachanwalt-insolvenz-sanierungsrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/fachanwalt-insolvenz-sanierungsrecht.md`
- Source skill root: `fachanwalt-insolvenz-sanierungsrecht/skills/`
- Source skills: 54

Plugin description: Plugin Fachanwalt für Insolvenz- und Sanierungsrecht nach FAO § 14. InsO Eroeffnung Antragspflicht § 15a Gläubigerantrag § 14 InsO. StaRUG Restrukturierungsplan. Insolvenzanfechtung §§ 129 ff. InsO. Schnittstellen insolvenzrecht und steuerrecht-anwalt-und-berater.

## Routing workflow

1. Read `skills-index/fachanwalt-insolvenz-sanierungsrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `fachanwalt-insolvenz-sanierungsrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
