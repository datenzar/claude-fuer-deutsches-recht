---
name: krankenhausrecht
description: "krankenhausrecht: Super-Plugin für deutsches Krankenhausrecht: Planung, Finanzierung, Entgelte, Reform, Qualität, MD-Prüfung, Klinikbetrieb und Rechtsstreit. Use this opencode router for krankenhausrecht requests; it selects source skills through skills-index/krankenhausrecht.md and then reads the matching SKILL.md files."
---

# krankenhausrecht opencode skill router

> Generated router for the source plugin `krankenhausrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `krankenhausrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/krankenhausrecht.md`
- Source skill root: `krankenhausrecht/skills/`
- Source skills: 67

Plugin description: Super-Plugin für deutsches Krankenhausrecht: Planung, Finanzierung, Entgelte, Reform, Qualität, MD-Prüfung, Klinikbetrieb und Rechtsstreit.

## Routing workflow

1. Read `skills-index/krankenhausrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `krankenhausrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
