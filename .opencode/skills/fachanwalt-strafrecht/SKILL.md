---
name: fachanwalt-strafrecht
description: "fachanwalt-strafrecht: Plugin Fachanwalt für Strafrecht. Orientierung StPO StGB Nebenstrafrecht. Strafverteidigung Ermittlungsverfahren Hauptverhandlung Revision. Nebenklage Opfervertretung Zeugenbeistand Adhaesion Insolvenzantrag StA. Ergaenzt aktenaufbereiter-strafrecht und kanzlei-allgemein. Use this opencode router for fachanwalt-strafrecht requests; it selects source skills through skills-index/fachanwalt-strafrecht.md and then reads the matching SKILL.md files."
---

# fachanwalt-strafrecht opencode skill router

> Generated router for the source plugin `fachanwalt-strafrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `fachanwalt-strafrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/fachanwalt-strafrecht.md`
- Source skill root: `fachanwalt-strafrecht/skills/`
- Source skills: 177

Plugin description: Plugin Fachanwalt für Strafrecht. Orientierung StPO StGB Nebenstrafrecht. Strafverteidigung Ermittlungsverfahren Hauptverhandlung Revision. Nebenklage Opfervertretung Zeugenbeistand Adhaesion Insolvenzantrag StA. Ergaenzt aktenaufbereiter-strafrecht und kanzlei-allgemein.

## Routing workflow

1. Read `skills-index/fachanwalt-strafrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `fachanwalt-strafrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
