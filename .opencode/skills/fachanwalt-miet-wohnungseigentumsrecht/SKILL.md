---
name: fachanwalt-miet-wohnungseigentumsrecht
description: "fachanwalt-miet-wohnungseigentumsrecht: Großer Fachanwalt-Kompass Miet- und Wohnungseigentumsrecht mit über 200 Skills für Wohnraum, Gewerberaum, Betriebskosten, WEG, Hausverwaltung, Beschlüsse, GEG, Beweise, Fristen und Workflows. Use this opencode router for fachanwalt-miet-wohnungseigentumsrecht requests; it selects source skills through skills-index/fachanwalt-miet-wohnungseigentumsrecht.md and then reads the matching SKILL.md files."
---

# fachanwalt-miet-wohnungseigentumsrecht opencode skill router

> Generated router for the source plugin `fachanwalt-miet-wohnungseigentumsrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `fachanwalt-miet-wohnungseigentumsrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/fachanwalt-miet-wohnungseigentumsrecht.md`
- Source skill root: `fachanwalt-miet-wohnungseigentumsrecht/skills/`
- Source skills: 225

Plugin description: Großer Fachanwalt-Kompass Miet- und Wohnungseigentumsrecht mit über 200 Skills für Wohnraum, Gewerberaum, Betriebskosten, WEG, Hausverwaltung, Beschlüsse, GEG, Beweise, Fristen und Workflows.

## Routing workflow

1. Read `skills-index/fachanwalt-miet-wohnungseigentumsrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `fachanwalt-miet-wohnungseigentumsrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
