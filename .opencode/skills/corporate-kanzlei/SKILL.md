---
name: corporate-kanzlei
description: "corporate-kanzlei: Corporate-Kanzlei-Plugin: Deal-Kommandocenter, Datenraum, Due Diligence, SPA/APA, Umwandlung, StaRUG, Insolvenzplan, W&I, Signing/Closing, PMI. Use this opencode router for corporate-kanzlei requests; it selects source skills through skills-index/corporate-kanzlei.md and then reads the matching SKILL.md files."
---

# corporate-kanzlei opencode skill router

> Generated router for the source plugin `corporate-kanzlei`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `corporate-kanzlei/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/corporate-kanzlei.md`
- Source skill root: `corporate-kanzlei/skills/`
- Source skills: 50

Plugin description: Corporate-Kanzlei-Plugin: Deal-Kommandocenter, Datenraum, Due Diligence, SPA/APA, Umwandlung, StaRUG, Insolvenzplan, W&I, Signing/Closing, PMI.

## Routing workflow

1. Read `skills-index/corporate-kanzlei.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `corporate-kanzlei/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
