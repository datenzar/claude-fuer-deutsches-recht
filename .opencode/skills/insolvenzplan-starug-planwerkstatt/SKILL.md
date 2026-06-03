---
name: insolvenzplan-starug-planwerkstatt
description: "insolvenzplan-starug-planwerkstatt: Freistehendes Plugin für Insolvenzplan und StaRUG-Restrukturierungsplan: Intake, Sanierungskonzept, Vergleichsrechnung, Gruppen, Klassen, darstellender und gestaltender Teil, Anlagen, Abstimmung, Cram-down, Minderheitenschutz, Gericht und Planvollzug. Use this opencode router for insolvenzplan-starug-planwerkstatt requests; it selects source skills through skills-index/insolvenzplan-starug-planwerkstatt.md and then reads the matching SKILL.md files."
---

# insolvenzplan-starug-planwerkstatt opencode skill router

> Generated router for the source plugin `insolvenzplan-starug-planwerkstatt`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `insolvenzplan-starug-planwerkstatt/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/insolvenzplan-starug-planwerkstatt.md`
- Source skill root: `insolvenzplan-starug-planwerkstatt/skills/`
- Source skills: 54

Plugin description: Freistehendes Plugin für Insolvenzplan und StaRUG-Restrukturierungsplan: Intake, Sanierungskonzept, Vergleichsrechnung, Gruppen, Klassen, darstellender und gestaltender Teil, Anlagen, Abstimmung, Cram-down, Minderheitenschutz, Gericht und Planvollzug.

## Routing workflow

1. Read `skills-index/insolvenzplan-starug-planwerkstatt.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `insolvenzplan-starug-planwerkstatt/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
