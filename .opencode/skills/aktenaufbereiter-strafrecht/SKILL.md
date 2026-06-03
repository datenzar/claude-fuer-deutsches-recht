---
name: aktenaufbereiter-strafrecht
description: "aktenaufbereiter-strafrecht: Aktenaufbereiter für die Strafverteidigung. Sechs Excel-fähige Übersichten — Aktenvorblatt; Personenverzeichnis; Tatkomplexe; Beziehungen; Chronologie; Fristen. Fortlaufend ergaenzbar. Erkennt Luecken und Widersprueche. Kein Ersatz für Aktenlektuere. Use this opencode router for aktenaufbereiter-strafrecht requests; it selects source skills through skills-index/aktenaufbereiter-strafrecht.md and then reads the matching SKILL.md files."
---

# aktenaufbereiter-strafrecht opencode skill router

> Generated router for the source plugin `aktenaufbereiter-strafrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `aktenaufbereiter-strafrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/aktenaufbereiter-strafrecht.md`
- Source skill root: `aktenaufbereiter-strafrecht/skills/`
- Source skills: 54

Plugin description: Aktenaufbereiter für die Strafverteidigung. Sechs Excel-fähige Übersichten — Aktenvorblatt; Personenverzeichnis; Tatkomplexe; Beziehungen; Chronologie; Fristen. Fortlaufend ergaenzbar. Erkennt Luecken und Widersprueche. Kein Ersatz für Aktenlektuere.

## Routing workflow

1. Read `skills-index/aktenaufbereiter-strafrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `aktenaufbereiter-strafrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
