---
name: europarecht-kompass
description: "europarecht-kompass: Freistehendes Europarecht-Plugin gegen deutsche Denkfehler: Vorrang, unmittelbare Wirkung, Richtlinien, Verordnungen, Charta, Grundfreiheiten, Beihilfen, Vorlageverfahren und EU-Drafting. Use this opencode router for europarecht-kompass requests; it selects source skills through skills-index/europarecht-kompass.md and then reads the matching SKILL.md files."
---

# europarecht-kompass opencode skill router

> Generated router for the source plugin `europarecht-kompass`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `europarecht-kompass/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/europarecht-kompass.md`
- Source skill root: `europarecht-kompass/skills/`
- Source skills: 54

Plugin description: Freistehendes Europarecht-Plugin gegen deutsche Denkfehler: Vorrang, unmittelbare Wirkung, Richtlinien, Verordnungen, Charta, Grundfreiheiten, Beihilfen, Vorlageverfahren und EU-Drafting.

## Routing workflow

1. Read `skills-index/europarecht-kompass.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `europarecht-kompass/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
