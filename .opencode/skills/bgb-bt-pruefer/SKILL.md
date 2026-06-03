---
name: bgb-bt-pruefer
description: "bgb-bt-pruefer: Großer BGB-BT-Prüfer für Schuldrecht Besonderer Teil: Kauf, Miete, Pacht, Leihe, Darlehen, Dienst, Werk, Bau, Reise, Makler, Auftrag, Geschäftsbesorgung, Bürgschaft, Schuldversprechen, GoA, Bereicherung, Delikt und Rückabwicklung. Use this opencode router for bgb-bt-pruefer requests; it selects source skills through skills-index/bgb-bt-pruefer.md and then reads the matching SKILL.md files."
---

# bgb-bt-pruefer opencode skill router

> Generated router for the source plugin `bgb-bt-pruefer`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `bgb-bt-pruefer/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/bgb-bt-pruefer.md`
- Source skill root: `bgb-bt-pruefer/skills/`
- Source skills: 54

Plugin description: Großer BGB-BT-Prüfer für Schuldrecht Besonderer Teil: Kauf, Miete, Pacht, Leihe, Darlehen, Dienst, Werk, Bau, Reise, Makler, Auftrag, Geschäftsbesorgung, Bürgschaft, Schuldversprechen, GoA, Bereicherung, Delikt und Rückabwicklung.

## Routing workflow

1. Read `skills-index/bgb-bt-pruefer.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `bgb-bt-pruefer/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
