---
name: bundeswehrrecht-wehrrecht
description: "bundeswehrrecht-wehrrecht: Super-Plugin für Soldatenrecht, Wehrbeschwerde, Disziplinarrecht, Wehrpflicht, Reservisten, Versorgung und Bundeswehrverwaltung. Use this opencode router for bundeswehrrecht-wehrrecht requests; it selects source skills through skills-index/bundeswehrrecht-wehrrecht.md and then reads the matching SKILL.md files."
---

# bundeswehrrecht-wehrrecht opencode skill router

> Generated router for the source plugin `bundeswehrrecht-wehrrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `bundeswehrrecht-wehrrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/bundeswehrrecht-wehrrecht.md`
- Source skill root: `bundeswehrrecht-wehrrecht/skills/`
- Source skills: 67

Plugin description: Super-Plugin für Soldatenrecht, Wehrbeschwerde, Disziplinarrecht, Wehrpflicht, Reservisten, Versorgung und Bundeswehrverwaltung.

## Routing workflow

1. Read `skills-index/bundeswehrrecht-wehrrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `bundeswehrrecht-wehrrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
