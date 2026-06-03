---
name: krisenfrueherkennung-starug
description: "krisenfrueherkennung-starug: Krisenfrüherkennung und Krisenmanagement nach StaRUG: Pflicht zum 24-Monats-Frühwarnsystem nach § 1 StaRUG, § 102 StaRUG Warnpflicht der Berater, Geschäftsführerhaftung, drohende Zahlungsunfähigkeit, integrierte Planung, Restrukturierungsplan und Stabilisierungsanordnung. Use this opencode router for krisenfrueherkennung-starug requests; it selects source skills through skills-index/krisenfrueherkennung-starug.md and then reads the matching SKILL.md files."
---

# krisenfrueherkennung-starug opencode skill router

> Generated router for the source plugin `krisenfrueherkennung-starug`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `krisenfrueherkennung-starug/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/krisenfrueherkennung-starug.md`
- Source skill root: `krisenfrueherkennung-starug/skills/`
- Source skills: 54

Plugin description: Krisenfrüherkennung und Krisenmanagement nach StaRUG: Pflicht zum 24-Monats-Frühwarnsystem nach § 1 StaRUG, § 102 StaRUG Warnpflicht der Berater, Geschäftsführerhaftung, drohende Zahlungsunfähigkeit, integrierte Planung, Restrukturierungsplan und Stabilisierungsanordnung.

## Routing workflow

1. Read `skills-index/krisenfrueherkennung-starug.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `krisenfrueherkennung-starug/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
