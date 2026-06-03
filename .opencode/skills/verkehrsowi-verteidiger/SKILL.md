---
name: verkehrsowi-verteidiger
description: "verkehrsowi-verteidiger: Freistehendes VerkehrsOWi-Plugin für Bußgeldbescheid, Anhörung, Einspruch, Punkte, Fahrverbot, Rotlicht, Geschwindigkeit, Abstand, Handy, Alkohol, Drogen, Akteneinsicht, Messakte, Zeugenstrategie und Amtsgericht. Use this opencode router for verkehrsowi-verteidiger requests; it selects source skills through skills-index/verkehrsowi-verteidiger.md and then reads the matching SKILL.md files."
---

# verkehrsowi-verteidiger opencode skill router

> Generated router for the source plugin `verkehrsowi-verteidiger`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `verkehrsowi-verteidiger/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/verkehrsowi-verteidiger.md`
- Source skill root: `verkehrsowi-verteidiger/skills/`
- Source skills: 54

Plugin description: Freistehendes VerkehrsOWi-Plugin für Bußgeldbescheid, Anhörung, Einspruch, Punkte, Fahrverbot, Rotlicht, Geschwindigkeit, Abstand, Handy, Alkohol, Drogen, Akteneinsicht, Messakte, Zeugenstrategie und Amtsgericht.

## Routing workflow

1. Read `skills-index/verkehrsowi-verteidiger.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `verkehrsowi-verteidiger/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
