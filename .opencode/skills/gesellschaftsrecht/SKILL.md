---
name: gesellschaftsrecht
description: "gesellschaftsrecht: Gesellschaftsrecht – GmbH/AG/Personengesellschaften, M&A-Due-Diligence ohne Discovery (Q&A + Datenraum), Gesellschafterbeschlüsse, HRB/HRA-Anmeldungen, Closing Checklists, Compliance-Fristen. Use this opencode router for gesellschaftsrecht requests; it selects source skills through skills-index/gesellschaftsrecht.md and then reads the matching SKILL.md files."
---

# gesellschaftsrecht opencode skill router

> Generated router for the source plugin `gesellschaftsrecht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `gesellschaftsrecht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/gesellschaftsrecht.md`
- Source skill root: `gesellschaftsrecht/skills/`
- Source skills: 54

Plugin description: Gesellschaftsrecht – GmbH/AG/Personengesellschaften, M&A-Due-Diligence ohne Discovery (Q&A + Datenraum), Gesellschafterbeschlüsse, HRB/HRA-Anmeldungen, Closing Checklists, Compliance-Fristen.

## Routing workflow

1. Read `skills-index/gesellschaftsrecht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `gesellschaftsrecht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
