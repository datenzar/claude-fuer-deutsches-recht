---
name: kanzlei-builder-hub
description: "kanzlei-builder-hub: Findet, prüft und installiert Community-Skills mit Security-Review-Gate vor dem Deployment in die Kanzleiumgebung. Use this opencode router for kanzlei-builder-hub requests; it selects source skills through skills-index/kanzlei-builder-hub.md and then reads the matching SKILL.md files."
---

# kanzlei-builder-hub opencode skill router

> Generated router for the source plugin `kanzlei-builder-hub`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `kanzlei-builder-hub/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/kanzlei-builder-hub.md`
- Source skill root: `kanzlei-builder-hub/skills/`
- Source skills: 54

Plugin description: Findet, prüft und installiert Community-Skills mit Security-Review-Gate vor dem Deployment in die Kanzleiumgebung.

## Routing workflow

1. Read `skills-index/kanzlei-builder-hub.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `kanzlei-builder-hub/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
