---
name: lobbyregister-bundestag
description: "lobbyregister-bundestag: Lobbyregister-Bundestag-Superplugin mit 50 geführten Skills für Registrierungspflicht, Ausnahmen, Registereintrag, Regelungsvorhaben, Stellungnahmen, Finanzdaten, Aktualisierung, Verhaltenskodex, Meldung von Verstoessen und Fristen nach LobbyRG. Use this opencode router for lobbyregister-bundestag requests; it selects source skills through skills-index/lobbyregister-bundestag.md and then reads the matching SKILL.md files."
---

# lobbyregister-bundestag opencode skill router

> Generated router for the source plugin `lobbyregister-bundestag`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `lobbyregister-bundestag/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/lobbyregister-bundestag.md`
- Source skill root: `lobbyregister-bundestag/skills/`
- Source skills: 51

Plugin description: Lobbyregister-Bundestag-Superplugin mit 50 geführten Skills für Registrierungspflicht, Ausnahmen, Registereintrag, Regelungsvorhaben, Stellungnahmen, Finanzdaten, Aktualisierung, Verhaltenskodex, Meldung von Verstoessen und Fristen nach LobbyRG.

## Routing workflow

1. Read `skills-index/lobbyregister-bundestag.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `lobbyregister-bundestag/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
