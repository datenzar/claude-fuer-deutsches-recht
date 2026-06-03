---
name: dfg-foerderantrag
description: "dfg-foerderantrag: DFG-Förderantragssteller für Sachbeihilfe, adaptive Anfänger-/Profi-Führung, kleine schnelle Anträge, große Koselleck-Strategien, elan-Formalia, Finanzplan, Reviewer-Red-Team, Forschungsdaten, KI-/Ethik-Check und Wiedereinreichung. Use this opencode router for dfg-foerderantrag requests; it selects source skills through skills-index/dfg-foerderantrag.md and then reads the matching SKILL.md files."
---

# dfg-foerderantrag opencode skill router

> Generated router for the source plugin `dfg-foerderantrag`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `dfg-foerderantrag/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/dfg-foerderantrag.md`
- Source skill root: `dfg-foerderantrag/skills/`
- Source skills: 54

Plugin description: DFG-Förderantragssteller für Sachbeihilfe, adaptive Anfänger-/Profi-Führung, kleine schnelle Anträge, große Koselleck-Strategien, elan-Formalia, Finanzplan, Reviewer-Red-Team, Forschungsdaten, KI-/Ethik-Check und Wiedereinreichung.

## Routing workflow

1. Read `skills-index/dfg-foerderantrag.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `dfg-foerderantrag/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
