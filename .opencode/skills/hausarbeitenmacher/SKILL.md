---
name: hausarbeitenmacher
description: "hausarbeitenmacher: Didaktisches Plugin für juristische Hausarbeiten und Seminararbeiten. Führt sokratisch durch Zivilrecht öffentliches Recht Strafrecht mit Ausfluegen in Europarecht und Rechtstheorie. Adressaten-Strategie ohne Schleimerei. Liefert keine fertigen Lösungen sondern führt zur eigenen Subsumtion. Use this opencode router for hausarbeitenmacher requests; it selects source skills through skills-index/hausarbeitenmacher.md and then reads the matching SKILL.md files."
---

# hausarbeitenmacher opencode skill router

> Generated router for the source plugin `hausarbeitenmacher`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `hausarbeitenmacher/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/hausarbeitenmacher.md`
- Source skill root: `hausarbeitenmacher/skills/`
- Source skills: 54

Plugin description: Didaktisches Plugin für juristische Hausarbeiten und Seminararbeiten. Führt sokratisch durch Zivilrecht öffentliches Recht Strafrecht mit Ausfluegen in Europarecht und Rechtstheorie. Adressaten-Strategie ohne Schleimerei. Liefert keine fertigen Lösungen sondern führt zur eigenen Subsumtion.

## Routing workflow

1. Read `skills-index/hausarbeitenmacher.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `hausarbeitenmacher/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
