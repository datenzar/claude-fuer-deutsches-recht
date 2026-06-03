---
name: zwangsvollstreckung
description: "zwangsvollstreckung: Plugin Zwangsvollstreckung §§ 704 ff. ZPO: Mahn-/Vollstreckungsbescheid, PfÜB Bank/Arbeit, § 802l Kontensuche, Vermögensauskunft, Räumung, § 800 ZPO Notar, § 201 InsO, ZVG, EU-Kontenpfändung VO 655/2014, § 765a Härtefall, Schuldnerschutz. Use this opencode router for zwangsvollstreckung requests; it selects source skills through skills-index/zwangsvollstreckung.md and then reads the matching SKILL.md files."
---

# zwangsvollstreckung opencode skill router

> Generated router for the source plugin `zwangsvollstreckung`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `zwangsvollstreckung/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/zwangsvollstreckung.md`
- Source skill root: `zwangsvollstreckung/skills/`
- Source skills: 54

Plugin description: Plugin Zwangsvollstreckung §§ 704 ff. ZPO: Mahn-/Vollstreckungsbescheid, PfÜB Bank/Arbeit, § 802l Kontensuche, Vermögensauskunft, Räumung, § 800 ZPO Notar, § 201 InsO, ZVG, EU-Kontenpfändung VO 655/2014, § 765a Härtefall, Schuldnerschutz.

## Routing workflow

1. Read `skills-index/zwangsvollstreckung.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `zwangsvollstreckung/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
