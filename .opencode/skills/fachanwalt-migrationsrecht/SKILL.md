---
name: fachanwalt-migrationsrecht
description: "fachanwalt-migrationsrecht: Großer Fachanwalt-Kompass Migrationsrecht mit über 200 Skills für Aufenthalt, Blaue Karte EU, Fachkräfte, Asyl, Dublin/GEAS, Einbürgerung, Staaten-/Gebietschecks und spanische/einfache Erklärung. Use this opencode router for fachanwalt-migrationsrecht requests; it selects source skills through skills-index/fachanwalt-migrationsrecht.md and then reads the matching SKILL.md files."
---

# fachanwalt-migrationsrecht opencode skill router

> Generated router for the source plugin `fachanwalt-migrationsrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `fachanwalt-migrationsrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/fachanwalt-migrationsrecht.md`
- Source skill root: `fachanwalt-migrationsrecht/skills/`
- Source skills: 376

Plugin description: Großer Fachanwalt-Kompass Migrationsrecht mit über 200 Skills für Aufenthalt, Blaue Karte EU, Fachkräfte, Asyl, Dublin/GEAS, Einbürgerung, Staaten-/Gebietschecks und spanische/einfache Erklärung.

## Routing workflow

1. Read `skills-index/fachanwalt-migrationsrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `fachanwalt-migrationsrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
