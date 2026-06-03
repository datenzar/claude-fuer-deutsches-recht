---
name: fachanwalt-it-recht
description: "fachanwalt-it-recht: Plugin Fachanwalt für Informationstechnologierecht. SaaS Software-Lizenz DSGVO BDSG TTDSG TKG NIS2 DDG DSA DMA EU-KI-VO Open-Source. Schnittstellen Plugin datenschutzrecht ki-governance kanzlei-allgemein. Use this opencode router for fachanwalt-it-recht requests; it selects source skills through skills-index/fachanwalt-it-recht.md and then reads the matching SKILL.md files."
---

# fachanwalt-it-recht opencode skill router

> Generated router for the source plugin `fachanwalt-it-recht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `fachanwalt-it-recht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/fachanwalt-it-recht.md`
- Source skill root: `fachanwalt-it-recht/skills/`
- Source skills: 57

Plugin description: Plugin Fachanwalt für Informationstechnologierecht. SaaS Software-Lizenz DSGVO BDSG TTDSG TKG NIS2 DDG DSA DMA EU-KI-VO Open-Source. Schnittstellen Plugin datenschutzrecht ki-governance kanzlei-allgemein.

## Routing workflow

1. Read `skills-index/fachanwalt-it-recht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `fachanwalt-it-recht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
