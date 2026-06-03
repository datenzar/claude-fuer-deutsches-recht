---
name: fluggastrechte
description: "fluggastrechte: Fluggastrechte selber geltend machen nach VO (EG) Nr. 261/2004. Tickets erfassen, Annullierung oder Verspaetung pruefen, aussergewoehnliche Umstaende, Distanz, Ausgleich, Forderungsschreiben, Mahnung und Klage. Rechtsprechung nur nach Live-Verifikation. Use this opencode router for fluggastrechte requests; it selects source skills through skills-index/fluggastrechte.md and then reads the matching SKILL.md files."
---

# fluggastrechte opencode skill router

> Generated router for the source plugin `fluggastrechte`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `fluggastrechte/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/fluggastrechte.md`
- Source skill root: `fluggastrechte/skills/`
- Source skills: 54

Plugin description: Fluggastrechte selber geltend machen nach VO (EG) Nr. 261/2004. Tickets erfassen, Annullierung oder Verspaetung pruefen, aussergewoehnliche Umstaende, Distanz, Ausgleich, Forderungsschreiben, Mahnung und Klage. Rechtsprechung nur nach Live-Verifikation.

## Routing workflow

1. Read `skills-index/fluggastrechte.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `fluggastrechte/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
