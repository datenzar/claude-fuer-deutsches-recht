---
name: fachanwalt-transport-speditionsrecht
description: "fachanwalt-transport-speditionsrecht: Plugin Fachanwalt für Transport- und Speditionsrecht. HGB §§ 407 ff. Frachtvertrag §§ 453 ff. Spedition CMR COTIF Montrealer Übereinkommen Haager Visby Regeln ADSp. Schnittstelle Plugin kanzlei-allgemein. Use this opencode router for fachanwalt-transport-speditionsrecht requests; it selects source skills through skills-index/fachanwalt-transport-speditionsrecht.md and then reads the matching SKILL.md files."
---

# fachanwalt-transport-speditionsrecht opencode skill router

> Generated router for the source plugin `fachanwalt-transport-speditionsrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `fachanwalt-transport-speditionsrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/fachanwalt-transport-speditionsrecht.md`
- Source skill root: `fachanwalt-transport-speditionsrecht/skills/`
- Source skills: 54

Plugin description: Plugin Fachanwalt für Transport- und Speditionsrecht. HGB §§ 407 ff. Frachtvertrag §§ 453 ff. Spedition CMR COTIF Montrealer Übereinkommen Haager Visby Regeln ADSp. Schnittstelle Plugin kanzlei-allgemein.

## Routing workflow

1. Read `skills-index/fachanwalt-transport-speditionsrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `fachanwalt-transport-speditionsrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
