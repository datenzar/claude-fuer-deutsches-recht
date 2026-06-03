---
name: fachanwalt-gewerblicher-rechtsschutz
description: "fachanwalt-gewerblicher-rechtsschutz: Plugin Fachanwalt für gewerblichen Rechtsschutz nach FAO § 14k. MarkenG. DesignG. UWG. PatG GebrMG. UrhG-Bezuege. Markenanmeldung DPMA EUIPO. UWG-Abmahnung §§ 8 ff. UWG. Designverletzung. Einstweilige Verfuegung Verletzungsklage Lizenzanaloger Schadensersatz. Use this opencode router for fachanwalt-gewerblicher-rechtsschutz requests; it selects source skills through skills-index/fachanwalt-gewerblicher-rechtsschutz.md and then reads the matching SKILL.md files."
---

# fachanwalt-gewerblicher-rechtsschutz opencode skill router

> Generated router for the source plugin `fachanwalt-gewerblicher-rechtsschutz`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `fachanwalt-gewerblicher-rechtsschutz/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/fachanwalt-gewerblicher-rechtsschutz.md`
- Source skill root: `fachanwalt-gewerblicher-rechtsschutz/skills/`
- Source skills: 54

Plugin description: Plugin Fachanwalt für gewerblichen Rechtsschutz nach FAO § 14k. MarkenG. DesignG. UWG. PatG GebrMG. UrhG-Bezuege. Markenanmeldung DPMA EUIPO. UWG-Abmahnung §§ 8 ff. UWG. Designverletzung. Einstweilige Verfuegung Verletzungsklage Lizenzanaloger Schadensersatz.

## Routing workflow

1. Read `skills-index/fachanwalt-gewerblicher-rechtsschutz.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `fachanwalt-gewerblicher-rechtsschutz/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
