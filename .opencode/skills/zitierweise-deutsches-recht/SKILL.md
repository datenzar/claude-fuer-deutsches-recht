---
name: zitierweise-deutsches-recht
description: "zitierweise-deutsches-recht: Deutsche juristische Hauszitierweise v4.0: Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und verifizierbarer Quelle; keine BeckRS-, Kommentar- oder Aufsatz-Blindzitate. Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Use this opencode router for zitierweise-deutsches-recht requests; it selects source skills through skills-index/zitierweise-deutsches-recht.md and then reads the matching SKILL.md files."
---

# zitierweise-deutsches-recht opencode skill router

> Generated router for the source plugin `zitierweise-deutsches-recht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `zitierweise-deutsches-recht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/zitierweise-deutsches-recht.md`
- Source skill root: `zitierweise-deutsches-recht/skills/`
- Source skills: 54

Plugin description: Deutsche juristische Hauszitierweise v4.0: Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und verifizierbarer Quelle; keine BeckRS-, Kommentar- oder Aufsatz-Blindzitate. Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Routing workflow

1. Read `skills-index/zitierweise-deutsches-recht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `zitierweise-deutsches-recht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
