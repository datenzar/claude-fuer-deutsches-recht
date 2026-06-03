---
name: immobilienrechtspraxis
description: "immobilienrechtspraxis: Werkzeuge fuer immobilienrechtliche Rechtsabteilungen: musterbasierte Vertragserstellung mit Klauselschutz, Vertragspruefung gegen Playbook, Grundbuchanalyse, Sachverhaltsermittlung, Mieteranfragen, Case Management und AVV-Pruefung. Rechtsprechung nur nach Live-Verifikation. Use this opencode router for immobilienrechtspraxis requests; it selects source skills through skills-index/immobilienrechtspraxis.md and then reads the matching SKILL.md files."
---

# immobilienrechtspraxis opencode skill router

> Generated router for the source plugin `immobilienrechtspraxis`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `immobilienrechtspraxis/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/immobilienrechtspraxis.md`
- Source skill root: `immobilienrechtspraxis/skills/`
- Source skills: 54

Plugin description: Werkzeuge fuer immobilienrechtliche Rechtsabteilungen: musterbasierte Vertragserstellung mit Klauselschutz, Vertragspruefung gegen Playbook, Grundbuchanalyse, Sachverhaltsermittlung, Mieteranfragen, Case Management und AVV-Pruefung. Rechtsprechung nur nach Live-Verifikation.

## Routing workflow

1. Read `skills-index/immobilienrechtspraxis.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `immobilienrechtspraxis/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
