---
name: urteilsbauer-relationsmacher
description: "urteilsbauer-relationsmacher: Urteils- und Beschluss-Werkstatt für Amts- Land- und Familienrichter sowie Rechtspfleger. Aktenintake Relation Beweiswürdigung mit Richter-Input Tatbestandsmerkmale Tenor Tatbestand Entscheidungsgründe Rechtsmittelbelehrung. Erzeugt DOCX nach Paragraf 313 ZPO. Use this opencode router for urteilsbauer-relationsmacher requests; it selects source skills through skills-index/urteilsbauer-relationsmacher.md and then reads the matching SKILL.md files."
---

# urteilsbauer-relationsmacher opencode skill router

> Generated router for the source plugin `urteilsbauer-relationsmacher`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `urteilsbauer-relationsmacher/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/urteilsbauer-relationsmacher.md`
- Source skill root: `urteilsbauer-relationsmacher/skills/`
- Source skills: 54

Plugin description: Urteils- und Beschluss-Werkstatt für Amts- Land- und Familienrichter sowie Rechtspfleger. Aktenintake Relation Beweiswürdigung mit Richter-Input Tatbestandsmerkmale Tenor Tatbestand Entscheidungsgründe Rechtsmittelbelehrung. Erzeugt DOCX nach Paragraf 313 ZPO.

## Routing workflow

1. Read `skills-index/urteilsbauer-relationsmacher.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `urteilsbauer-relationsmacher/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
