---
name: einfache-leichte-sprache-jura
description: "einfache-leichte-sprache-jura: Juristische Texte in Einfache Sprache oder Leichte Sprache übertragen: experimentelle Standard-Annäherung, Zielgruppe klären, Rechtsinhalt sichern und Qualitätsgate nutzen. Use this opencode router for einfache-leichte-sprache-jura requests; it selects source skills through skills-index/einfache-leichte-sprache-jura.md and then reads the matching SKILL.md files."
---

# einfache-leichte-sprache-jura opencode skill router

> Generated router for the source plugin `einfache-leichte-sprache-jura`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `einfache-leichte-sprache-jura/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/einfache-leichte-sprache-jura.md`
- Source skill root: `einfache-leichte-sprache-jura/skills/`
- Source skills: 54

Plugin description: Juristische Texte in Einfache Sprache oder Leichte Sprache übertragen: experimentelle Standard-Annäherung, Zielgruppe klären, Rechtsinhalt sichern und Qualitätsgate nutzen.

## Routing workflow

1. Read `skills-index/einfache-leichte-sprache-jura.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `einfache-leichte-sprache-jura/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
