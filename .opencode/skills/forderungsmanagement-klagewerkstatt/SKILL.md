---
name: forderungsmanagement-klagewerkstatt
description: "forderungsmanagement-klagewerkstatt: Klagewerkstatt für Forderungsmanagement mit Zuständigkeitsprüfung, Mahnvorlauf, Inkasso-Zahlungsklage und Anspruchs-Gatekeeper: Nur klare, fällige und belegte Forderungen werden zur Klage freigegeben. Use this opencode router for forderungsmanagement-klagewerkstatt requests; it selects source skills through skills-index/forderungsmanagement-klagewerkstatt.md and then reads the matching SKILL.md files."
---

# forderungsmanagement-klagewerkstatt opencode skill router

> Generated router for the source plugin `forderungsmanagement-klagewerkstatt`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `forderungsmanagement-klagewerkstatt/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/forderungsmanagement-klagewerkstatt.md`
- Source skill root: `forderungsmanagement-klagewerkstatt/skills/`
- Source skills: 54

Plugin description: Klagewerkstatt für Forderungsmanagement mit Zuständigkeitsprüfung, Mahnvorlauf, Inkasso-Zahlungsklage und Anspruchs-Gatekeeper: Nur klare, fällige und belegte Forderungen werden zur Klage freigegeben.

## Routing workflow

1. Read `skills-index/forderungsmanagement-klagewerkstatt.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `forderungsmanagement-klagewerkstatt/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
