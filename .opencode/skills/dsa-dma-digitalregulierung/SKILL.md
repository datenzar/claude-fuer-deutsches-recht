---
name: dsa-dma-digitalregulierung
description: "dsa-dma-digitalregulierung: Digitalregulierung der EU: DSA (VO 2022/2065) und DMA (VO 2022/1925) plus Data Act DGA AI Act NIS-2 DORA CRA eIDAS 2.0 DDG P2B-VO und § 19a GWB. Gatekeeper-Schwellen VLOP-Einordnung Risikobewertung Art. 34 Forschungsdatenzugang Art. 40 Account-Sperre Art. 20-23 Zustellung Art. 13 DSA Klagewege. Use this opencode router for dsa-dma-digitalregulierung requests; it selects source skills through skills-index/dsa-dma-digitalregulierung.md and then reads the matching SKILL.md files."
---

# dsa-dma-digitalregulierung opencode skill router

> Generated router for the source plugin `dsa-dma-digitalregulierung`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `dsa-dma-digitalregulierung/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/dsa-dma-digitalregulierung.md`
- Source skill root: `dsa-dma-digitalregulierung/skills/`
- Source skills: 54

Plugin description: Digitalregulierung der EU: DSA (VO 2022/2065) und DMA (VO 2022/1925) plus Data Act DGA AI Act NIS-2 DORA CRA eIDAS 2.0 DDG P2B-VO und § 19a GWB. Gatekeeper-Schwellen VLOP-Einordnung Risikobewertung Art. 34 Forschungsdatenzugang Art. 40 Account-Sperre Art. 20-23 Zustellung Art. 13 DSA Klagewege.

## Routing workflow

1. Read `skills-index/dsa-dma-digitalregulierung.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `dsa-dma-digitalregulierung/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
