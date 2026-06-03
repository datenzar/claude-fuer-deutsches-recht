---
name: wandeldarlehen-lebenszyklus
description: "wandeldarlehen-lebenszyklus: Begleitet den vollständigen Lebenszyklus eines Wandeldarlehens für GmbH und UG: Vertragserstellung (bilingual/einsprachig), Beurkundungsprüfung, Wandelereignisse, Wandlungsberechnung, Cap-Table-Update, Gesellschafterbeschluss und Notar-Paket. Use this opencode router for wandeldarlehen-lebenszyklus requests; it selects source skills through skills-index/wandeldarlehen-lebenszyklus.md and then reads the matching SKILL.md files."
---

# wandeldarlehen-lebenszyklus opencode skill router

> Generated router for the source plugin `wandeldarlehen-lebenszyklus`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `wandeldarlehen-lebenszyklus/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/wandeldarlehen-lebenszyklus.md`
- Source skill root: `wandeldarlehen-lebenszyklus/skills/`
- Source skills: 50

Plugin description: Begleitet den vollständigen Lebenszyklus eines Wandeldarlehens für GmbH und UG: Vertragserstellung (bilingual/einsprachig), Beurkundungsprüfung, Wandelereignisse, Wandlungsberechnung, Cap-Table-Update, Gesellschafterbeschluss und Notar-Paket.

## Routing workflow

1. Read `skills-index/wandeldarlehen-lebenszyklus.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `wandeldarlehen-lebenszyklus/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
