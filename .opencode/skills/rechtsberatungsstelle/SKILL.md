---
name: rechtsberatungsstelle
description: "rechtsberatungsstelle: Pro-Bono- und Rechtsberatungsstellen (RDG-konform): Mandantenintake, Fristenkontrolle, Übergabe am Semesterende, mandantenfreundliche Briefe. Use this opencode router for rechtsberatungsstelle requests; it selects source skills through skills-index/rechtsberatungsstelle.md and then reads the matching SKILL.md files."
---

# rechtsberatungsstelle opencode skill router

> Generated router for the source plugin `rechtsberatungsstelle`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `rechtsberatungsstelle/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/rechtsberatungsstelle.md`
- Source skill root: `rechtsberatungsstelle/skills/`
- Source skills: 54

Plugin description: Pro-Bono- und Rechtsberatungsstellen (RDG-konform): Mandantenintake, Fristenkontrolle, Übergabe am Semesterende, mandantenfreundliche Briefe.

## Routing workflow

1. Read `skills-index/rechtsberatungsstelle.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `rechtsberatungsstelle/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
