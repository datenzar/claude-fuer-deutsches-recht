---
name: bgb-at-pruefer
description: "bgb-at-pruefer: Großes Prüfplugin zum BGB Allgemeiner Teil: Vertragsschluss, Willenserklärung, Zugang, Geschäftsfähigkeit, Form, qES, beA, § 130e ZPO, § 46h ArbGG, Anfechtung, Stellvertretung, Fristen und Verjährung. Use this opencode router for bgb-at-pruefer requests; it selects source skills through skills-index/bgb-at-pruefer.md and then reads the matching SKILL.md files."
---

# bgb-at-pruefer opencode skill router

> Generated router for the source plugin `bgb-at-pruefer`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `bgb-at-pruefer/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/bgb-at-pruefer.md`
- Source skill root: `bgb-at-pruefer/skills/`
- Source skills: 53

Plugin description: Großes Prüfplugin zum BGB Allgemeiner Teil: Vertragsschluss, Willenserklärung, Zugang, Geschäftsfähigkeit, Form, qES, beA, § 130e ZPO, § 46h ArbGG, Anfechtung, Stellvertretung, Fristen und Verjährung.

## Routing workflow

1. Read `skills-index/bgb-at-pruefer.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `bgb-at-pruefer/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
