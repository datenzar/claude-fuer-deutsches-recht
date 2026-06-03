---
name: liquiditaetsplanung
description: "liquiditaetsplanung: Liquiditaetsplanung nach deutschem Recht: 3-Wochen-Vorschau, 13/26/52-Wochen-Forecast, Excel-Export, Quote/Luecken-Ampel, Dokumentationspaket und Schnittstellen zu Fortbestehensprognose und Insolvenzrecht. Rechtsprechung nur nach Live-Verifikation. Use this opencode router for liquiditaetsplanung requests; it selects source skills through skills-index/liquiditaetsplanung.md and then reads the matching SKILL.md files."
---

# liquiditaetsplanung opencode skill router

> Generated router for the source plugin `liquiditaetsplanung`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `liquiditaetsplanung/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/liquiditaetsplanung.md`
- Source skill root: `liquiditaetsplanung/skills/`
- Source skills: 54

Plugin description: Liquiditaetsplanung nach deutschem Recht: 3-Wochen-Vorschau, 13/26/52-Wochen-Forecast, Excel-Export, Quote/Luecken-Ampel, Dokumentationspaket und Schnittstellen zu Fortbestehensprognose und Insolvenzrecht. Rechtsprechung nur nach Live-Verifikation.

## Routing workflow

1. Read `skills-index/liquiditaetsplanung.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `liquiditaetsplanung/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
