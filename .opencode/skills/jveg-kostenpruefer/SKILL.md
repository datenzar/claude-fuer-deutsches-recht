---
name: jveg-kostenpruefer
description: "jveg-kostenpruefer: Freistehender JVEG-Kostenprüfer für Zeugenentschädigung, Vorschuss, Fahrtkosten, Übernachtung, Verdienstausfall, Sachverständigen- und Dolmetscherkosten, Fristen, Festsetzung, Beschwerde und belegfeste Rechenprotokolle. Use this opencode router for jveg-kostenpruefer requests; it selects source skills through skills-index/jveg-kostenpruefer.md and then reads the matching SKILL.md files."
---

# jveg-kostenpruefer opencode skill router

> Generated router for the source plugin `jveg-kostenpruefer`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `jveg-kostenpruefer/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/jveg-kostenpruefer.md`
- Source skill root: `jveg-kostenpruefer/skills/`
- Source skills: 54

Plugin description: Freistehender JVEG-Kostenprüfer für Zeugenentschädigung, Vorschuss, Fahrtkosten, Übernachtung, Verdienstausfall, Sachverständigen- und Dolmetscherkosten, Fristen, Festsetzung, Beschwerde und belegfeste Rechenprotokolle.

## Routing workflow

1. Read `skills-index/jveg-kostenpruefer.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `jveg-kostenpruefer/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
