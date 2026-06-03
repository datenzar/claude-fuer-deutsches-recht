---
name: grosskanzlei-corporate-ma
description: "grosskanzlei-corporate-ma: Freistehendes Big-Law-Corporate/M&A-Plugin: Deal-Kommandocenter, Anfänger-/First-Year-Modus, Aktenanlage, Datenraum, Legal DD, Tabellenreview, Liquiditätsvorschau, SPA/APA, W&I, Public M&A, UmwG/StaRUG, CP-Kalender, E-Rechnung/GoBD, PMI. Use this opencode router for grosskanzlei-corporate-ma requests; it selects source skills through skills-index/grosskanzlei-corporate-ma.md and then reads the matching SKILL.md files."
---

# grosskanzlei-corporate-ma opencode skill router

> Generated router for the source plugin `grosskanzlei-corporate-ma`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `grosskanzlei-corporate-ma/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/grosskanzlei-corporate-ma.md`
- Source skill root: `grosskanzlei-corporate-ma/skills/`
- Source skills: 56

Plugin description: Freistehendes Big-Law-Corporate/M&A-Plugin: Deal-Kommandocenter, Anfänger-/First-Year-Modus, Aktenanlage, Datenraum, Legal DD, Tabellenreview, Liquiditätsvorschau, SPA/APA, W&I, Public M&A, UmwG/StaRUG, CP-Kalender, E-Rechnung/GoBD, PMI.

## Routing workflow

1. Read `skills-index/grosskanzlei-corporate-ma.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `grosskanzlei-corporate-ma/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
