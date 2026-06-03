---
name: bank-rechtsabteilung
description: "bank-rechtsabteilung: Rechtsabteilung einer mittelgroßen deutschen Bank: Aufsicht, Kredit, ZAG/PSD2, PSD3/PSR-Vorschau, eWpG, MiCAR, Tokenisierung, BaFin, Vorstand, HV und Kanzleisteuerung. Use this opencode router for bank-rechtsabteilung requests; it selects source skills through skills-index/bank-rechtsabteilung.md and then reads the matching SKILL.md files."
---

# bank-rechtsabteilung opencode skill router

> Generated router for the source plugin `bank-rechtsabteilung`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `bank-rechtsabteilung/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/bank-rechtsabteilung.md`
- Source skill root: `bank-rechtsabteilung/skills/`
- Source skills: 100

Plugin description: Rechtsabteilung einer mittelgroßen deutschen Bank: Aufsicht, Kredit, ZAG/PSD2, PSD3/PSR-Vorschau, eWpG, MiCAR, Tokenisierung, BaFin, Vorstand, HV und Kanzleisteuerung.

## Routing workflow

1. Read `skills-index/bank-rechtsabteilung.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `bank-rechtsabteilung/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
