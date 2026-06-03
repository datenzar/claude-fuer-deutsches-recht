---
name: bundesnetzagentur-verfahren
description: "bundesnetzagentur-verfahren: Großes Regulierungs-Plugin für anwaltliche Arbeit mit der Bundesnetzagentur in Energie, Telekommunikation, Post, Eisenbahn und Digital Services. Use this opencode router for bundesnetzagentur-verfahren requests; it selects source skills through skills-index/bundesnetzagentur-verfahren.md and then reads the matching SKILL.md files."
---

# bundesnetzagentur-verfahren opencode skill router

> Generated router for the source plugin `bundesnetzagentur-verfahren`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `bundesnetzagentur-verfahren/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/bundesnetzagentur-verfahren.md`
- Source skill root: `bundesnetzagentur-verfahren/skills/`
- Source skills: 221

Plugin description: Großes Regulierungs-Plugin für anwaltliche Arbeit mit der Bundesnetzagentur in Energie, Telekommunikation, Post, Eisenbahn und Digital Services.

## Routing workflow

1. Read `skills-index/bundesnetzagentur-verfahren.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `bundesnetzagentur-verfahren/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
