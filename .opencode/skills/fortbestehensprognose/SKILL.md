---
name: fortbestehensprognose
description: "fortbestehensprognose: Fortbestehensprognose § 19 Abs. 2 InsO als Geschäftsführer-Selbstdokumentation. Bilanzstatus Annahmen Plausibilisierung Zwoelf-Monats-Liquiditaet. Sanierungsbausteine Patronatserklärung Comfortletter Rangrücktritt Stundung Forderungsverzicht. IDW S 11 StaRUG. Eskalation bei negativer Prognose. Use this opencode router for fortbestehensprognose requests; it selects source skills through skills-index/fortbestehensprognose.md and then reads the matching SKILL.md files."
---

# fortbestehensprognose opencode skill router

> Generated router for the source plugin `fortbestehensprognose`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `fortbestehensprognose/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/fortbestehensprognose.md`
- Source skill root: `fortbestehensprognose/skills/`
- Source skills: 54

Plugin description: Fortbestehensprognose § 19 Abs. 2 InsO als Geschäftsführer-Selbstdokumentation. Bilanzstatus Annahmen Plausibilisierung Zwoelf-Monats-Liquiditaet. Sanierungsbausteine Patronatserklärung Comfortletter Rangrücktritt Stundung Forderungsverzicht. IDW S 11 StaRUG. Eskalation bei negativer Prognose.

## Routing workflow

1. Read `skills-index/fortbestehensprognose.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `fortbestehensprognose/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
