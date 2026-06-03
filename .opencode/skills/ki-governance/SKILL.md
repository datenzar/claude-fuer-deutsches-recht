---
name: ki-governance
description: "ki-governance: EU-KI-VO + DSGVO – Use-Case-Triage, KI-Inventar, AIA/DPIA, Vendor-Review, Drift-Monitoring der KI-Richtlinie. Use this opencode router for ki-governance requests; it selects source skills through skills-index/ki-governance.md and then reads the matching SKILL.md files."
---

# ki-governance opencode skill router

> Generated router for the source plugin `ki-governance`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `ki-governance/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/ki-governance.md`
- Source skill root: `ki-governance/skills/`
- Source skills: 54

Plugin description: EU-KI-VO + DSGVO – Use-Case-Triage, KI-Inventar, AIA/DPIA, Vendor-Review, Drift-Monitoring der KI-Richtlinie.

## Routing workflow

1. Read `skills-index/ki-governance.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `ki-governance/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
