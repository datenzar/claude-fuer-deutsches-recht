---
name: kartellrecht-marktabgrenzung-pruefung
description: "kartellrecht-marktabgrenzung-pruefung: Kritische kartellrechtliche Pruefinstanz fuer Marktabgrenzungen nach Paragraf 18 GWB sowie Art. 101 und 102 AEUV: SSNIP-Test, Nachfrage- und Angebotsumstellung, raeumlicher Markt, Evidenz, Konsistenz, Red Flags und Marktbeherrschung. Rechtsprechung nur nach Live-Verifikation. Use this opencode router for kartellrecht-marktabgrenzung-pruefung requests; it selects source skills through skills-index/kartellrecht-marktabgrenzung-pruefung.md and then reads the matching SKILL.md files."
---

# kartellrecht-marktabgrenzung-pruefung opencode skill router

> Generated router for the source plugin `kartellrecht-marktabgrenzung-pruefung`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `kartellrecht-marktabgrenzung-pruefung/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/kartellrecht-marktabgrenzung-pruefung.md`
- Source skill root: `kartellrecht-marktabgrenzung-pruefung/skills/`
- Source skills: 126

Plugin description: Kritische kartellrechtliche Pruefinstanz fuer Marktabgrenzungen nach Paragraf 18 GWB sowie Art. 101 und 102 AEUV: SSNIP-Test, Nachfrage- und Angebotsumstellung, raeumlicher Markt, Evidenz, Konsistenz, Red Flags und Marktbeherrschung. Rechtsprechung nur nach Live-Verifikation.

## Routing workflow

1. Read `skills-index/kartellrecht-marktabgrenzung-pruefung.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `kartellrecht-marktabgrenzung-pruefung/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
