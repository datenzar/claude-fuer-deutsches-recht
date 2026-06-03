---
name: robotik-recht
description: "robotik-recht: Robotik-Recht Deutschland/EU: Maschinenverordnung, KI-VO, Produkthaftung, ProdSG, Datenschutz, CRA, Data Act, CE, Marktüberwachung, Unfälle, Rückruf, Verträge und Robotik-Testakte. Use this opencode router for robotik-recht requests; it selects source skills through skills-index/robotik-recht.md and then reads the matching SKILL.md files."
---

# robotik-recht opencode skill router

> Generated router for the source plugin `robotik-recht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `robotik-recht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/robotik-recht.md`
- Source skill root: `robotik-recht/skills/`
- Source skills: 143

Plugin description: Robotik-Recht Deutschland/EU: Maschinenverordnung, KI-VO, Produkthaftung, ProdSG, Datenschutz, CRA, Data Act, CE, Marktüberwachung, Unfälle, Rückruf, Verträge und Robotik-Testakte.

## Routing workflow

1. Read `skills-index/robotik-recht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `robotik-recht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
