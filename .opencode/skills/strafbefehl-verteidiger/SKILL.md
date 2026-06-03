---
name: strafbefehl-verteidiger
description: "strafbefehl-verteidiger: Freistehendes Strafbefehls-Plugin für Verteidigung gegen Strafbefehl, Einspruch, Akteneinsicht, Tagessätze, Nebenfolgen, Pflichtverteidigung, Wiedereinsetzung, Einstellung, Zeugenstrategie und Hauptverhandlung. Use this opencode router for strafbefehl-verteidiger requests; it selects source skills through skills-index/strafbefehl-verteidiger.md and then reads the matching SKILL.md files."
---

# strafbefehl-verteidiger opencode skill router

> Generated router for the source plugin `strafbefehl-verteidiger`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `strafbefehl-verteidiger/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/strafbefehl-verteidiger.md`
- Source skill root: `strafbefehl-verteidiger/skills/`
- Source skills: 54

Plugin description: Freistehendes Strafbefehls-Plugin für Verteidigung gegen Strafbefehl, Einspruch, Akteneinsicht, Tagessätze, Nebenfolgen, Pflichtverteidigung, Wiedereinsetzung, Einstellung, Zeugenstrategie und Hauptverhandlung.

## Routing workflow

1. Read `skills-index/strafbefehl-verteidiger.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `strafbefehl-verteidiger/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
