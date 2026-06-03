---
name: subsumtions-pruefer
description: "subsumtions-pruefer: Interaktiver Subsumtions-Workflow für deutsches Recht und Europarecht: Tatbestandsmerkmale zerlegen, Vier-Schritt-Schema anwenden, Rechtsfolgen und Einreden prüfen. Keine Rechtsberatung. Use this opencode router for subsumtions-pruefer requests; it selects source skills through skills-index/subsumtions-pruefer.md and then reads the matching SKILL.md files."
---

# subsumtions-pruefer opencode skill router

> Generated router for the source plugin `subsumtions-pruefer`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `subsumtions-pruefer/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/subsumtions-pruefer.md`
- Source skill root: `subsumtions-pruefer/skills/`
- Source skills: 50

Plugin description: Interaktiver Subsumtions-Workflow für deutsches Recht und Europarecht: Tatbestandsmerkmale zerlegen, Vier-Schritt-Schema anwenden, Rechtsfolgen und Einreden prüfen. Keine Rechtsberatung.

## Routing workflow

1. Read `skills-index/subsumtions-pruefer.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `subsumtions-pruefer/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
