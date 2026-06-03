---
name: aussenwirtschaft-zoll-sanktionen
description: "aussenwirtschaft-zoll-sanktionen: Freistehendes Plugin für Außenwirtschaft, Sanktionen, Zoll, Exportkontrolle, BAFA, TARIC, CBAM, Verbrauchsteuer, AWV, AML/KYC und Ermittlungen. Use this opencode router for aussenwirtschaft-zoll-sanktionen requests; it selects source skills through skills-index/aussenwirtschaft-zoll-sanktionen.md and then reads the matching SKILL.md files."
---

# aussenwirtschaft-zoll-sanktionen opencode skill router

> Generated router for the source plugin `aussenwirtschaft-zoll-sanktionen`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `aussenwirtschaft-zoll-sanktionen/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/aussenwirtschaft-zoll-sanktionen.md`
- Source skill root: `aussenwirtschaft-zoll-sanktionen/skills/`
- Source skills: 100

Plugin description: Freistehendes Plugin für Außenwirtschaft, Sanktionen, Zoll, Exportkontrolle, BAFA, TARIC, CBAM, Verbrauchsteuer, AWV, AML/KYC und Ermittlungen.

## Routing workflow

1. Read `skills-index/aussenwirtschaft-zoll-sanktionen.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `aussenwirtschaft-zoll-sanktionen/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
