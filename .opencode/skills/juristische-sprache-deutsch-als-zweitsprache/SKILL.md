---
name: juristische-sprache-deutsch-als-zweitsprache
description: "juristische-sprache-deutsch-als-zweitsprache: Plugin fuer Menschen im deutschen Recht mit anderer Herkunftssprache: einfache Erklaerungen, Juristendeutsch, Bescheide, Schriftsaetze, Grammatik, Fristen und Verfahrenslogik. Use this opencode router for juristische-sprache-deutsch-als-zweitsprache requests; it selects source skills through skills-index/juristische-sprache-deutsch-als-zweitsprache.md and then reads the matching SKILL.md files."
---

# juristische-sprache-deutsch-als-zweitsprache opencode skill router

> Generated router for the source plugin `juristische-sprache-deutsch-als-zweitsprache`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `juristische-sprache-deutsch-als-zweitsprache/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/juristische-sprache-deutsch-als-zweitsprache.md`
- Source skill root: `juristische-sprache-deutsch-als-zweitsprache/skills/`
- Source skills: 50

Plugin description: Plugin fuer Menschen im deutschen Recht mit anderer Herkunftssprache: einfache Erklaerungen, Juristendeutsch, Bescheide, Schriftsaetze, Grammatik, Fristen und Verfahrenslogik.

## Routing workflow

1. Read `skills-index/juristische-sprache-deutsch-als-zweitsprache.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `juristische-sprache-deutsch-als-zweitsprache/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
