---
name: patentrecht
description: "patentrecht: Großes Patentrechts-Plugin für Erfindungsaufnahme, Patentanmeldung, Anspruchsentwurf, Recherche, Neuheit, erfinderische Tätigkeit, FTO, Abmahnung, Claim Chart, Vorbenutzungsrecht, Lizenz, Erfinderbenennung, Einspruch, Nichtigkeit, Register und Fristen. Use this opencode router for patentrecht requests; it selects source skills through skills-index/patentrecht.md and then reads the matching SKILL.md files."
---

# patentrecht opencode skill router

> Generated router for the source plugin `patentrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `patentrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/patentrecht.md`
- Source skill root: `patentrecht/skills/`
- Source skills: 54

Plugin description: Großes Patentrechts-Plugin für Erfindungsaufnahme, Patentanmeldung, Anspruchsentwurf, Recherche, Neuheit, erfinderische Tätigkeit, FTO, Abmahnung, Claim Chart, Vorbenutzungsrecht, Lizenz, Erfinderbenennung, Einspruch, Nichtigkeit, Register und Fristen.

## Routing workflow

1. Read `skills-index/patentrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `patentrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
