---
name: weg-hausverwaltung
description: "weg-hausverwaltung: Operatives WEG- und Hausverwaltungs-Plugin fuer Beschluesse, Eigentuemerversammlung, Protokoll, Beschlusssammlung, Wirtschaftsplan, Jahresabrechnung, Hausgeld, Sonderumlage, Betriebskosten, Handwerker, bauliche Veraenderungen, Steckersolar, Wallbox, Verwalter, Beirat und Anwalt-Eskalation. Use this opencode router for weg-hausverwaltung requests; it selects source skills through skills-index/weg-hausverwaltung.md and then reads the matching SKILL.md files."
---

# weg-hausverwaltung opencode skill router

> Generated router for the source plugin `weg-hausverwaltung`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `weg-hausverwaltung/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/weg-hausverwaltung.md`
- Source skill root: `weg-hausverwaltung/skills/`
- Source skills: 54

Plugin description: Operatives WEG- und Hausverwaltungs-Plugin fuer Beschluesse, Eigentuemerversammlung, Protokoll, Beschlusssammlung, Wirtschaftsplan, Jahresabrechnung, Hausgeld, Sonderumlage, Betriebskosten, Handwerker, bauliche Veraenderungen, Steckersolar, Wallbox, Verwalter, Beirat und Anwalt-Eskalation.

## Routing workflow

1. Read `skills-index/weg-hausverwaltung.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `weg-hausverwaltung/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
