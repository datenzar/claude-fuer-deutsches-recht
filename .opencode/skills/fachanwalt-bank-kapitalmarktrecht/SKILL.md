---
name: fachanwalt-bank-kapitalmarktrecht
description: "fachanwalt-bank-kapitalmarktrecht: Plugin Fachanwalt für Bank- und Kapitalmarktrecht. KWG ZAG WpHG WpIG MiFID-II MAR MiCAR Verbraucherkredit Vermögensanlage Beratungshaftung. Schnittstellen Plugin gesellschaftsrecht regulatorisches-recht. Use this opencode router for fachanwalt-bank-kapitalmarktrecht requests; it selects source skills through skills-index/fachanwalt-bank-kapitalmarktrecht.md and then reads the matching SKILL.md files."
---

# fachanwalt-bank-kapitalmarktrecht opencode skill router

> Generated router for the source plugin `fachanwalt-bank-kapitalmarktrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `fachanwalt-bank-kapitalmarktrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/fachanwalt-bank-kapitalmarktrecht.md`
- Source skill root: `fachanwalt-bank-kapitalmarktrecht/skills/`
- Source skills: 54

Plugin description: Plugin Fachanwalt für Bank- und Kapitalmarktrecht. KWG ZAG WpHG WpIG MiFID-II MAR MiCAR Verbraucherkredit Vermögensanlage Beratungshaftung. Schnittstellen Plugin gesellschaftsrecht regulatorisches-recht.

## Routing workflow

1. Read `skills-index/fachanwalt-bank-kapitalmarktrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `fachanwalt-bank-kapitalmarktrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
