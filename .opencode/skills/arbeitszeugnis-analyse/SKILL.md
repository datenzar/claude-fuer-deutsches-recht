---
name: arbeitszeugnis-analyse
description: "arbeitszeugnis-analyse: Analyse deutscher Arbeitszeugnisse nach Ampelsystem (Rot/Orange/Grün). Geheimcodes, Schaufenster-Drift, negative Codeworte, Steigerungsadverbien. Satzweise Notenmatrix, begründete Gesamtnotenspanne. Vollständiger Mandatsablauf: Erstgespräch, Mandantenbericht, Aufforderungsschreiben, Klagestrategie. Use this opencode router for arbeitszeugnis-analyse requests; it selects source skills through skills-index/arbeitszeugnis-analyse.md and then reads the matching SKILL.md files."
---

# arbeitszeugnis-analyse opencode skill router

> Generated router for the source plugin `arbeitszeugnis-analyse`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `arbeitszeugnis-analyse/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/arbeitszeugnis-analyse.md`
- Source skill root: `arbeitszeugnis-analyse/skills/`
- Source skills: 50

Plugin description: Analyse deutscher Arbeitszeugnisse nach Ampelsystem (Rot/Orange/Grün). Geheimcodes, Schaufenster-Drift, negative Codeworte, Steigerungsadverbien. Satzweise Notenmatrix, begründete Gesamtnotenspanne. Vollständiger Mandatsablauf: Erstgespräch, Mandantenbericht, Aufforderungsschreiben, Klagestrategie.

## Routing workflow

1. Read `skills-index/arbeitszeugnis-analyse.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `arbeitszeugnis-analyse/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
