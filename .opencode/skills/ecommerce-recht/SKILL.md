---
name: ecommerce-recht
description: "ecommerce-recht: Super-Plugin für Online-Shops, Plattformen, Marktplätze und digitale Verbraucherprozesse. Use this opencode router for ecommerce-recht requests; it selects source skills through skills-index/ecommerce-recht.md and then reads the matching SKILL.md files."
---

# ecommerce-recht opencode skill router

> Generated router for the source plugin `ecommerce-recht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `ecommerce-recht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/ecommerce-recht.md`
- Source skill root: `ecommerce-recht/skills/`
- Source skills: 67

Plugin description: Super-Plugin für Online-Shops, Plattformen, Marktplätze und digitale Verbraucherprozesse.

## Routing workflow

1. Read `skills-index/ecommerce-recht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `ecommerce-recht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
