---
name: goae-gebuehrenordnung-aerzte
description: "goae-gebuehrenordnung-aerzte: Super-Plugin zur GOÄ: private Arztrechnungen prüfen, erstellen, begründen, beanstanden und prozessual verwerten. Use this opencode router for goae-gebuehrenordnung-aerzte requests; it selects source skills through skills-index/goae-gebuehrenordnung-aerzte.md and then reads the matching SKILL.md files."
---

# goae-gebuehrenordnung-aerzte opencode skill router

> Generated router for the source plugin `goae-gebuehrenordnung-aerzte`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `goae-gebuehrenordnung-aerzte/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/goae-gebuehrenordnung-aerzte.md`
- Source skill root: `goae-gebuehrenordnung-aerzte/skills/`
- Source skills: 65

Plugin description: Super-Plugin zur GOÄ: private Arztrechnungen prüfen, erstellen, begründen, beanstanden und prozessual verwerten.

## Routing workflow

1. Read `skills-index/goae-gebuehrenordnung-aerzte.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `goae-gebuehrenordnung-aerzte/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
