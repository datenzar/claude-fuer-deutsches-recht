---
name: forschungszulage-antragstellung
description: "forschungszulage-antragstellung: Forschungszulage-Antragstellung nach FZulG: adaptiver Fördercheck, BSFZ-Portaltexte mit Zeichenbudgets, Finanzamt-Antrag, FuE-Abgrenzung, Bemessungsgrundlage 2026, Auszahlung, Verlust-/Insolvenzlage, Dokumentation, Beihilfen, Einspruch und Mehrjahresroadmap. Use this opencode router for forschungszulage-antragstellung requests; it selects source skills through skills-index/forschungszulage-antragstellung.md and then reads the matching SKILL.md files."
---

# forschungszulage-antragstellung opencode skill router

> Generated router for the source plugin `forschungszulage-antragstellung`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `forschungszulage-antragstellung/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/forschungszulage-antragstellung.md`
- Source skill root: `forschungszulage-antragstellung/skills/`
- Source skills: 54

Plugin description: Forschungszulage-Antragstellung nach FZulG: adaptiver Fördercheck, BSFZ-Portaltexte mit Zeichenbudgets, Finanzamt-Antrag, FuE-Abgrenzung, Bemessungsgrundlage 2026, Auszahlung, Verlust-/Insolvenzlage, Dokumentation, Beihilfen, Einspruch und Mehrjahresroadmap.

## Routing workflow

1. Read `skills-index/forschungszulage-antragstellung.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `forschungszulage-antragstellung/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
