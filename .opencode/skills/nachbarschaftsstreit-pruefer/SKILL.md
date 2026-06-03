---
name: nachbarschaftsstreit-pruefer
description: "nachbarschaftsstreit-pruefer: Nachbarrecht und Nachbarschaftsstreit: Überbau, Überhang, Äste/Wurzeln, Grenzbaum, Zaun/Mauer/Hecke, Immissionen, Vertiefung, Notweg, Hammerschlagsrecht, Beweise, Aufforderung, Klage und Vergleich. Use this opencode router for nachbarschaftsstreit-pruefer requests; it selects source skills through skills-index/nachbarschaftsstreit-pruefer.md and then reads the matching SKILL.md files."
---

# nachbarschaftsstreit-pruefer opencode skill router

> Generated router for the source plugin `nachbarschaftsstreit-pruefer`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `nachbarschaftsstreit-pruefer/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/nachbarschaftsstreit-pruefer.md`
- Source skill root: `nachbarschaftsstreit-pruefer/skills/`
- Source skills: 54

Plugin description: Nachbarrecht und Nachbarschaftsstreit: Überbau, Überhang, Äste/Wurzeln, Grenzbaum, Zaun/Mauer/Hecke, Immissionen, Vertiefung, Notweg, Hammerschlagsrecht, Beweise, Aufforderung, Klage und Vergleich.

## Routing workflow

1. Read `skills-index/nachbarschaftsstreit-pruefer.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `nachbarschaftsstreit-pruefer/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
