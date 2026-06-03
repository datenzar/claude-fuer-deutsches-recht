---
name: strafzumessung
description: "strafzumessung: Strafzumessung nach deutschem Strafrecht vom Strafbefehl bis zur grossen Strafkammer. § 46 StGB Strafzumessungstatsachen Tagessatz Geldstrafe Freiheitsstrafe Bewaehrung § 56 § 49 Regelbeispiele besonders schwerer Fall Verstaendigung § 257c StPO TOA § 46a Gesamtstrafe § 55 JGG. Use this opencode router for strafzumessung requests; it selects source skills through skills-index/strafzumessung.md and then reads the matching SKILL.md files."
---

# strafzumessung opencode skill router

> Generated router for the source plugin `strafzumessung`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `strafzumessung/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/strafzumessung.md`
- Source skill root: `strafzumessung/skills/`
- Source skills: 54

Plugin description: Strafzumessung nach deutschem Strafrecht vom Strafbefehl bis zur grossen Strafkammer. § 46 StGB Strafzumessungstatsachen Tagessatz Geldstrafe Freiheitsstrafe Bewaehrung § 56 § 49 Regelbeispiele besonders schwerer Fall Verstaendigung § 257c StPO TOA § 46a Gesamtstrafe § 55 JGG.

## Routing workflow

1. Read `skills-index/strafzumessung.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `strafzumessung/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
