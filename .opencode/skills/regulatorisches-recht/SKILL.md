---
name: regulatorisches-recht
description: "regulatorisches-recht: Aufsichtsrecht – KWG, ZAG, WpHG, GwG, EnWG, TKG, HeilMWerbG, Umsatzsteuer-Voranmeldung, Inkasso/RDG, Regulator-Feeds, Wochendigest. Use this opencode router for regulatorisches-recht requests; it selects source skills through skills-index/regulatorisches-recht.md and then reads the matching SKILL.md files."
---

# regulatorisches-recht opencode skill router

> Generated router for the source plugin `regulatorisches-recht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `regulatorisches-recht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/regulatorisches-recht.md`
- Source skill root: `regulatorisches-recht/skills/`
- Source skills: 54

Plugin description: Aufsichtsrecht – KWG, ZAG, WpHG, GwG, EnWG, TKG, HeilMWerbG, Umsatzsteuer-Voranmeldung, Inkasso/RDG, Regulator-Feeds, Wochendigest.

## Routing workflow

1. Read `skills-index/regulatorisches-recht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `regulatorisches-recht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
