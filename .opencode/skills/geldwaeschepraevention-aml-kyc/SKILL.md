---
name: geldwaeschepraevention-aml-kyc
description: "geldwaeschepraevention-aml-kyc: Freistehendes Plugin für Geldwäscheprävention, AML, KYC, GwG-Risikoanalyse, UBO, PEP, Sanktionen, FIU/goAML, Transparenzregister und Behördenverfahren. Use this opencode router for geldwaeschepraevention-aml-kyc requests; it selects source skills through skills-index/geldwaeschepraevention-aml-kyc.md and then reads the matching SKILL.md files."
---

# geldwaeschepraevention-aml-kyc opencode skill router

> Generated router for the source plugin `geldwaeschepraevention-aml-kyc`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `geldwaeschepraevention-aml-kyc/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/geldwaeschepraevention-aml-kyc.md`
- Source skill root: `geldwaeschepraevention-aml-kyc/skills/`
- Source skills: 54

Plugin description: Freistehendes Plugin für Geldwäscheprävention, AML, KYC, GwG-Risikoanalyse, UBO, PEP, Sanktionen, FIU/goAML, Transparenzregister und Behördenverfahren.

## Routing workflow

1. Read `skills-index/geldwaeschepraevention-aml-kyc.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `geldwaeschepraevention-aml-kyc/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
