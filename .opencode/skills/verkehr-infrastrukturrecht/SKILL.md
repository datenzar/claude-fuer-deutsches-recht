---
name: verkehr-infrastrukturrecht
description: "verkehr-infrastrukturrecht: Freistehendes Verkehrs- und Infrastrukturrecht-Plugin für Verkehrsplanung, Planfeststellung, Straßenbahn, Ladeinfrastruktur, Parkraum und Verkehrswende. Use this opencode router for verkehr-infrastrukturrecht requests; it selects source skills through skills-index/verkehr-infrastrukturrecht.md and then reads the matching SKILL.md files."
---

# verkehr-infrastrukturrecht opencode skill router

> Generated router for the source plugin `verkehr-infrastrukturrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `verkehr-infrastrukturrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/verkehr-infrastrukturrecht.md`
- Source skill root: `verkehr-infrastrukturrecht/skills/`
- Source skills: 54

Plugin description: Freistehendes Verkehrs- und Infrastrukturrecht-Plugin für Verkehrsplanung, Planfeststellung, Straßenbahn, Ladeinfrastruktur, Parkraum und Verkehrswende.

## Routing workflow

1. Read `skills-index/verkehr-infrastrukturrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `verkehr-infrastrukturrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
