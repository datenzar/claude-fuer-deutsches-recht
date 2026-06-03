---
name: schriftform-und-textform-bgb
description: "schriftform-und-textform-bgb: Formerfordernisse im deutschen Zivilrecht: Schriftform, Textform, qES, Zugang, beA/ERV und Prozessordnungen. Mit Checklisten, Dokumentation und Rechtsprechung nur nach Live-Verifikation. Use this opencode router for schriftform-und-textform-bgb requests; it selects source skills through skills-index/schriftform-und-textform-bgb.md and then reads the matching SKILL.md files."
---

# schriftform-und-textform-bgb opencode skill router

> Generated router for the source plugin `schriftform-und-textform-bgb`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `schriftform-und-textform-bgb/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/schriftform-und-textform-bgb.md`
- Source skill root: `schriftform-und-textform-bgb/skills/`
- Source skills: 54

Plugin description: Formerfordernisse im deutschen Zivilrecht: Schriftform, Textform, qES, Zugang, beA/ERV und Prozessordnungen. Mit Checklisten, Dokumentation und Rechtsprechung nur nach Live-Verifikation.

## Routing workflow

1. Read `skills-index/schriftform-und-textform-bgb.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `schriftform-und-textform-bgb/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
