---
name: handelsrecht-hgb
description: "handelsrecht-hgb: Reines HGB-Plugin für Handelsrecht: Kaufmann, Handelsregister, Firma, Prokura, Handlungsvollmacht, Handelsgeschäfte, Handelskauf, Handelsvertreter, Makler, Kommission, Fracht, Spedition, Lager, Handelsbücher sowie OHG/KG einschließlich MoPeG-Statuswechsel von GbR zu OHG. Use this opencode router for handelsrecht-hgb requests; it selects source skills through skills-index/handelsrecht-hgb.md and then reads the matching SKILL.md files."
---

# handelsrecht-hgb opencode skill router

> Generated router for the source plugin `handelsrecht-hgb`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `handelsrecht-hgb/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/handelsrecht-hgb.md`
- Source skill root: `handelsrecht-hgb/skills/`
- Source skills: 51

Plugin description: Reines HGB-Plugin für Handelsrecht: Kaufmann, Handelsregister, Firma, Prokura, Handlungsvollmacht, Handelsgeschäfte, Handelskauf, Handelsvertreter, Makler, Kommission, Fracht, Spedition, Lager, Handelsbücher sowie OHG/KG einschließlich MoPeG-Statuswechsel von GbR zu OHG.

## Routing workflow

1. Read `skills-index/handelsrecht-hgb.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `handelsrecht-hgb/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
