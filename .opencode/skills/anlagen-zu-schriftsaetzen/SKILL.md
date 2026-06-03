---
name: anlagen-zu-schriftsaetzen
description: "anlagen-zu-schriftsaetzen: Anlagenmanagement fuer gerichtliche Schriftsaetze: sortiert chaotische Mandantenordner, E-Mails, Scans, Tabellen und Vorversionen zu beA-tauglichen K/B/AST/AG-Anlagen mit Verzeichnis, Konvolutdeckblaettern, Stempel-/Dateinamenregeln, Hashlog, Lueckenliste und Qualitygate. Use this opencode router for anlagen-zu-schriftsaetzen requests; it selects source skills through skills-index/anlagen-zu-schriftsaetzen.md and then reads the matching SKILL.md files."
---

# anlagen-zu-schriftsaetzen opencode skill router

> Generated router for the source plugin `anlagen-zu-schriftsaetzen`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `anlagen-zu-schriftsaetzen/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/anlagen-zu-schriftsaetzen.md`
- Source skill root: `anlagen-zu-schriftsaetzen/skills/`
- Source skills: 79

Plugin description: Anlagenmanagement fuer gerichtliche Schriftsaetze: sortiert chaotische Mandantenordner, E-Mails, Scans, Tabellen und Vorversionen zu beA-tauglichen K/B/AST/AG-Anlagen mit Verzeichnis, Konvolutdeckblaettern, Stempel-/Dateinamenregeln, Hashlog, Lueckenliste und Qualitygate.

## Routing workflow

1. Read `skills-index/anlagen-zu-schriftsaetzen.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `anlagen-zu-schriftsaetzen/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
