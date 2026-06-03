---
name: vertragsausfueller
description: "vertragsausfueller: Freistehendes Vertragsausfüller-Plugin: DOCX-Vorlagen und Altverträge strippen, Felder erkennen, Term Sheets mappen, Rückfragen führen, neue Verträge erzeugen und Track-Changes-Fassungen nur nach ausdrücklicher Nachfrage vorbereiten. Use this opencode router for vertragsausfueller requests; it selects source skills through skills-index/vertragsausfueller.md and then reads the matching SKILL.md files."
---

# vertragsausfueller opencode skill router

> Generated router for the source plugin `vertragsausfueller`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `vertragsausfueller/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/vertragsausfueller.md`
- Source skill root: `vertragsausfueller/skills/`
- Source skills: 54

Plugin description: Freistehendes Vertragsausfüller-Plugin: DOCX-Vorlagen und Altverträge strippen, Felder erkennen, Term Sheets mappen, Rückfragen führen, neue Verträge erzeugen und Track-Changes-Fassungen nur nach ausdrücklicher Nachfrage vorbereiten.

## Routing workflow

1. Read `skills-index/vertragsausfueller.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `vertragsausfueller/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
