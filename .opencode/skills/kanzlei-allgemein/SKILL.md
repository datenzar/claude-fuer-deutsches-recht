---
name: kanzlei-allgemein
description: "kanzlei-allgemein: Kanzlei-Allgemein-Plugin (fusioniert mit Cowork): edles Kommandocenter Mandatsannahme/GwG Klage/Replik Vertrag Rechtsprechung Handelsregister beA-Journal Rechnung UStVA Fristenbuch Timesheet RVG Versand-Vor-Check Posteingang Mandantenakte Mahnwesen Tagesbrief Geburtstage Weihnachtskarten. Use this opencode router for kanzlei-allgemein requests; it selects source skills through skills-index/kanzlei-allgemein.md and then reads the matching SKILL.md files."
---

# kanzlei-allgemein opencode skill router

> Generated router for the source plugin `kanzlei-allgemein`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `kanzlei-allgemein/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/kanzlei-allgemein.md`
- Source skill root: `kanzlei-allgemein/skills/`
- Source skills: 50

Plugin description: Kanzlei-Allgemein-Plugin (fusioniert mit Cowork): edles Kommandocenter Mandatsannahme/GwG Klage/Replik Vertrag Rechtsprechung Handelsregister beA-Journal Rechnung UStVA Fristenbuch Timesheet RVG Versand-Vor-Check Posteingang Mandantenakte Mahnwesen Tagesbrief Geburtstage Weihnachtskarten.

## Routing workflow

1. Read `skills-index/kanzlei-allgemein.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `kanzlei-allgemein/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
