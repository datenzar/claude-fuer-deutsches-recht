---
name: memorandums-ersteller
description: "memorandums-ersteller: Wandelt Mandantenunterlagen in ein juristisches Memorandum mit Vier-Teile-Gliederung — Sachverhalt mit Quellenreferenz; Ein-Satz-Fragen; Ein-Satz-Antworten; rechtliche Ausführungen mit Pinpoint-Zitierung. Optional Piercing-Questions. Rechtsgebietsneutral. Alias Memorandumsmacher. Use this opencode router for memorandums-ersteller requests; it selects source skills through skills-index/memorandums-ersteller.md and then reads the matching SKILL.md files."
---

# memorandums-ersteller opencode skill router

> Generated router for the source plugin `memorandums-ersteller`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `memorandums-ersteller/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/memorandums-ersteller.md`
- Source skill root: `memorandums-ersteller/skills/`
- Source skills: 54

Plugin description: Wandelt Mandantenunterlagen in ein juristisches Memorandum mit Vier-Teile-Gliederung — Sachverhalt mit Quellenreferenz; Ein-Satz-Fragen; Ein-Satz-Antworten; rechtliche Ausführungen mit Pinpoint-Zitierung. Optional Piercing-Questions. Rechtsgebietsneutral. Alias Memorandumsmacher.

## Routing workflow

1. Read `skills-index/memorandums-ersteller.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `memorandums-ersteller/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
