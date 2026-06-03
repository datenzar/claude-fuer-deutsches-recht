---
name: selbstvertreter-amtsgericht
description: "selbstvertreter-amtsgericht: Selbstvertretung vor dem Amtsgericht ohne Anwalt: Anfänger-Workflow, Fristen, Zuständigkeit, §23 GVG/§511 ZPO-Grenzen, Klage/Erwiderung/Replik, Beweise, PKH, Termin, Sanity-Check, Rechtsprechungschat, Berufung. Use this opencode router for selbstvertreter-amtsgericht requests; it selects source skills through skills-index/selbstvertreter-amtsgericht.md and then reads the matching SKILL.md files."
---

# selbstvertreter-amtsgericht opencode skill router

> Generated router for the source plugin `selbstvertreter-amtsgericht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `selbstvertreter-amtsgericht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/selbstvertreter-amtsgericht.md`
- Source skill root: `selbstvertreter-amtsgericht/skills/`
- Source skills: 86

Plugin description: Selbstvertretung vor dem Amtsgericht ohne Anwalt: Anfänger-Workflow, Fristen, Zuständigkeit, §23 GVG/§511 ZPO-Grenzen, Klage/Erwiderung/Replik, Beweise, PKH, Termin, Sanity-Check, Rechtsprechungschat, Berufung.

## Routing workflow

1. Read `skills-index/selbstvertreter-amtsgericht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `selbstvertreter-amtsgericht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
