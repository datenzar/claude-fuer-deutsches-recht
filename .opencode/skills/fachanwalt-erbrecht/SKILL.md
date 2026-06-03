---
name: fachanwalt-erbrecht
description: "fachanwalt-erbrecht: Plugin Fachanwalt für Erbrecht. BGB Erbrecht §§ 1922 ff. Pflichtteil Testament Erbschein Erbauseinandersetzung Erbschaftsteuer EU-ErbVO. Schnittstellen Plugin steuerrecht-anwalt-und-berater kanzlei-allgemein. Use this opencode router for fachanwalt-erbrecht requests; it selects source skills through skills-index/fachanwalt-erbrecht.md and then reads the matching SKILL.md files."
---

# fachanwalt-erbrecht opencode skill router

> Generated router for the source plugin `fachanwalt-erbrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `fachanwalt-erbrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/fachanwalt-erbrecht.md`
- Source skill root: `fachanwalt-erbrecht/skills/`
- Source skills: 54

Plugin description: Plugin Fachanwalt für Erbrecht. BGB Erbrecht §§ 1922 ff. Pflichtteil Testament Erbschein Erbauseinandersetzung Erbschaftsteuer EU-ErbVO. Schnittstellen Plugin steuerrecht-anwalt-und-berater kanzlei-allgemein.

## Routing workflow

1. Read `skills-index/fachanwalt-erbrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `fachanwalt-erbrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
