---
name: normenkontrolle-bauleitplanung
description: "normenkontrolle-bauleitplanung: Freistehendes Plugin für die Prüfung und Anfechtung von Bebauungsplänen, Flächennutzungsplänen und örtlichen Bauvorschriften nach § 47 VwGO vor BayVGH und OVG. Mandatsperspektive Antragstellervertretung. Use this opencode router for normenkontrolle-bauleitplanung requests; it selects source skills through skills-index/normenkontrolle-bauleitplanung.md and then reads the matching SKILL.md files."
---

# normenkontrolle-bauleitplanung opencode skill router

> Generated router for the source plugin `normenkontrolle-bauleitplanung`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `normenkontrolle-bauleitplanung/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/normenkontrolle-bauleitplanung.md`
- Source skill root: `normenkontrolle-bauleitplanung/skills/`
- Source skills: 54

Plugin description: Freistehendes Plugin für die Prüfung und Anfechtung von Bebauungsplänen, Flächennutzungsplänen und örtlichen Bauvorschriften nach § 47 VwGO vor BayVGH und OVG. Mandatsperspektive Antragstellervertretung.

## Routing workflow

1. Read `skills-index/normenkontrolle-bauleitplanung.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `normenkontrolle-bauleitplanung/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
