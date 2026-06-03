---
name: mietrecht
description: "mietrecht: Mietrecht für Mieter und Vermieter mit ausschließlich amtlichen Mietspiegel-Quellen pro Bundesland und für Top- und Universitaetsstaedte. Datenerhebung Mieterhoehungs-Widerspruch Mietsenkungsverlangen Nebenkostenprüfung und Erstellung Mieteranfragen Klageentwurf zum Amtsgericht. Use this opencode router for mietrecht requests; it selects source skills through skills-index/mietrecht.md and then reads the matching SKILL.md files."
---

# mietrecht opencode skill router

> Generated router for the source plugin `mietrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `mietrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/mietrecht.md`
- Source skill root: `mietrecht/skills/`
- Source skills: 54

Plugin description: Mietrecht für Mieter und Vermieter mit ausschließlich amtlichen Mietspiegel-Quellen pro Bundesland und für Top- und Universitaetsstaedte. Datenerhebung Mieterhoehungs-Widerspruch Mietsenkungsverlangen Nebenkostenprüfung und Erstellung Mieteranfragen Klageentwurf zum Amtsgericht.

## Routing workflow

1. Read `skills-index/mietrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `mietrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
