---
name: verfassungsrecht
description: "verfassungsrecht: Deutsches Verfassungsrecht unter dem Grundgesetz aus Sicht einer Spezialkanzlei. Rechtsprechungsgetrieben mit Live-Recherche auf bundesverfassungsgericht.de. Acht Skills für Gesetzgebungskompetenz formelle und materielle Verfassungsmäßigkeit Grundrechte und Verfassungsbeschwerde. Use this opencode router for verfassungsrecht requests; it selects source skills through skills-index/verfassungsrecht.md and then reads the matching SKILL.md files."
---

# verfassungsrecht opencode skill router

> Generated router for the source plugin `verfassungsrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `verfassungsrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/verfassungsrecht.md`
- Source skill root: `verfassungsrecht/skills/`
- Source skills: 54

Plugin description: Deutsches Verfassungsrecht unter dem Grundgesetz aus Sicht einer Spezialkanzlei. Rechtsprechungsgetrieben mit Live-Recherche auf bundesverfassungsgericht.de. Acht Skills für Gesetzgebungskompetenz formelle und materielle Verfassungsmäßigkeit Grundrechte und Verfassungsbeschwerde.

## Routing workflow

1. Read `skills-index/verfassungsrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `verfassungsrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
