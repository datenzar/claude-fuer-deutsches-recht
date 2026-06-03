---
name: ki-richtlinie-kanzleien
description: "ki-richtlinie-kanzleien: Erstellt und pflegt eine berufsrechtskonforme KI-Nutzungsrichtlinie für Kanzleien und Rechtsabteilungen mit Anwaelten und Syndikus-Anwaelten. Beruht auf BRAO, BORA, DSGVO, KI-Verordnung sowie BRAK- und DAV-Hinweisen. Use this opencode router for ki-richtlinie-kanzleien requests; it selects source skills through skills-index/ki-richtlinie-kanzleien.md and then reads the matching SKILL.md files."
---

# ki-richtlinie-kanzleien opencode skill router

> Generated router for the source plugin `ki-richtlinie-kanzleien`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `ki-richtlinie-kanzleien/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/ki-richtlinie-kanzleien.md`
- Source skill root: `ki-richtlinie-kanzleien/skills/`
- Source skills: 55

Plugin description: Erstellt und pflegt eine berufsrechtskonforme KI-Nutzungsrichtlinie für Kanzleien und Rechtsabteilungen mit Anwaelten und Syndikus-Anwaelten. Beruht auf BRAO, BORA, DSGVO, KI-Verordnung sowie BRAK- und DAV-Hinweisen.

## Routing workflow

1. Read `skills-index/ki-richtlinie-kanzleien.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `ki-richtlinie-kanzleien/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
