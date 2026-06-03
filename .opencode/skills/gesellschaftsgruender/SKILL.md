---
name: gesellschaftsgruender
description: "gesellschaftsgruender: Anfängerfreundlicher Gründungsassistent für deutsche Gesellschaften: Rechtsformwahl, Satzung, SHA, Cap Table, Notar, Handelsregister, Bank/KYC, Behörden, Steuerstart, IP, Datenschutz, erste 100 Tage und Streitprävention. Use this opencode router for gesellschaftsgruender requests; it selects source skills through skills-index/gesellschaftsgruender.md and then reads the matching SKILL.md files."
---

# gesellschaftsgruender opencode skill router

> Generated router for the source plugin `gesellschaftsgruender`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `gesellschaftsgruender/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/gesellschaftsgruender.md`
- Source skill root: `gesellschaftsgruender/skills/`
- Source skills: 100

Plugin description: Anfängerfreundlicher Gründungsassistent für deutsche Gesellschaften: Rechtsformwahl, Satzung, SHA, Cap Table, Notar, Handelsregister, Bank/KYC, Behörden, Steuerstart, IP, Datenschutz, erste 100 Tage und Streitprävention.

## Routing workflow

1. Read `skills-index/gesellschaftsgruender.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `gesellschaftsgruender/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
