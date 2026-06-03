---
name: zwangsverwaltung-zvg
description: "zwangsverwaltung-zvg: Freistehendes ZVG-Plugin für Zwangsverwaltung und Versteigerung: Beschlagnahme, Besitz, Mieten, Treuhandkonto, Berichte, Verteilung, ZVG-Portal-Recherche, Bieterangebote und Versteigerungsteilnahme. Use this opencode router for zwangsverwaltung-zvg requests; it selects source skills through skills-index/zwangsverwaltung-zvg.md and then reads the matching SKILL.md files."
---

# zwangsverwaltung-zvg opencode skill router

> Generated router for the source plugin `zwangsverwaltung-zvg`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `zwangsverwaltung-zvg/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/zwangsverwaltung-zvg.md`
- Source skill root: `zwangsverwaltung-zvg/skills/`
- Source skills: 54

Plugin description: Freistehendes ZVG-Plugin für Zwangsverwaltung und Versteigerung: Beschlagnahme, Besitz, Mieten, Treuhandkonto, Berichte, Verteilung, ZVG-Portal-Recherche, Bieterangebote und Versteigerungsteilnahme.

## Routing workflow

1. Read `skills-index/zwangsverwaltung-zvg.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `zwangsverwaltung-zvg/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
