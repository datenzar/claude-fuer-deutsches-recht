---
name: vereinsrecht-vereinsmanager
description: "vereinsrecht-vereinsmanager: Vereinsrechts- und Vereinsmanagement-Plugin für eingetragene und nicht eingetragene Vereine: Gründung, Satzung, Mitgliederversammlung, Vorstand, Protokolle, Beschlüsse, Gemeinnützigkeit, Register, Haftung, Datenschutz, Finanzen, Veranstaltungen und Spezialvereine. Use this opencode router for vereinsrecht-vereinsmanager requests; it selects source skills through skills-index/vereinsrecht-vereinsmanager.md and then reads the matching SKILL.md files."
---

# vereinsrecht-vereinsmanager opencode skill router

> Generated router for the source plugin `vereinsrecht-vereinsmanager`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `vereinsrecht-vereinsmanager/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/vereinsrecht-vereinsmanager.md`
- Source skill root: `vereinsrecht-vereinsmanager/skills/`
- Source skills: 58

Plugin description: Vereinsrechts- und Vereinsmanagement-Plugin für eingetragene und nicht eingetragene Vereine: Gründung, Satzung, Mitgliederversammlung, Vorstand, Protokolle, Beschlüsse, Gemeinnützigkeit, Register, Haftung, Datenschutz, Finanzen, Veranstaltungen und Spezialvereine.

## Routing workflow

1. Read `skills-index/vereinsrecht-vereinsmanager.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `vereinsrecht-vereinsmanager/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
