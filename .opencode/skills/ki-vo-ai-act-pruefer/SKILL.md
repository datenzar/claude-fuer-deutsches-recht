---
name: ki-vo-ai-act-pruefer
description: "ki-vo-ai-act-pruefer: Mechanik-Workflow zur KI-VO (EU 2024/1689): KI-System-Definition, Rollen, Risikoklassen, Hochrisiko-Diagnose, GPAI, Art. 43-Konformitätsbewertung, CE/EU-DB, Marktbeobachtung und Konformitäts-Evidence-Pack. Use this opencode router for ki-vo-ai-act-pruefer requests; it selects source skills through skills-index/ki-vo-ai-act-pruefer.md and then reads the matching SKILL.md files."
---

# ki-vo-ai-act-pruefer opencode skill router

> Generated router for the source plugin `ki-vo-ai-act-pruefer`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `ki-vo-ai-act-pruefer/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/ki-vo-ai-act-pruefer.md`
- Source skill root: `ki-vo-ai-act-pruefer/skills/`
- Source skills: 50

Plugin description: Mechanik-Workflow zur KI-VO (EU 2024/1689): KI-System-Definition, Rollen, Risikoklassen, Hochrisiko-Diagnose, GPAI, Art. 43-Konformitätsbewertung, CE/EU-DB, Marktbeobachtung und Konformitäts-Evidence-Pack.

## Routing workflow

1. Read `skills-index/ki-vo-ai-act-pruefer.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `ki-vo-ai-act-pruefer/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
