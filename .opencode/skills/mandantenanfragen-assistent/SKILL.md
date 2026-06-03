---
name: mandantenanfragen-assistent
description: "mandantenanfragen-assistent: Assistent für Anwaltskanzleien zur Erstantwort auf Mandantenanfragen per E-Mail: dankt foermlich übernimmt die Anrede aus der eingehenden E-Mail nennt die telefonische Terminvergabe bittet um Sachverhalt per E-Mail oder bietet eine Telefon-Transkription mit DSGVO-Einwilligungshinweis an. Use this opencode router for mandantenanfragen-assistent requests; it selects source skills through skills-index/mandantenanfragen-assistent.md and then reads the matching SKILL.md files."
---

# mandantenanfragen-assistent opencode skill router

> Generated router for the source plugin `mandantenanfragen-assistent`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `mandantenanfragen-assistent/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/mandantenanfragen-assistent.md`
- Source skill root: `mandantenanfragen-assistent/skills/`
- Source skills: 54

Plugin description: Assistent für Anwaltskanzleien zur Erstantwort auf Mandantenanfragen per E-Mail: dankt foermlich übernimmt die Anrede aus der eingehenden E-Mail nennt die telefonische Terminvergabe bittet um Sachverhalt per E-Mail oder bietet eine Telefon-Transkription mit DSGVO-Einwilligungshinweis an.

## Routing workflow

1. Read `skills-index/mandantenanfragen-assistent.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `mandantenanfragen-assistent/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
