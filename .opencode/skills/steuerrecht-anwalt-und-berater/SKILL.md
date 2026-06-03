---
name: steuerrecht-anwalt-und-berater
description: "steuerrecht-anwalt-und-berater: Steuerrecht für Anwalt (anw- FAO § 9) und Steuerberater (stb-): Einspruch Klage FG Aussenprüfung Selbstanzeige, Grundsteuer, Grunderwerbsteuer, Share Deals, Signing Closing, BWA SuSa Lohnbuchhaltung Jahresabschluss. Use this opencode router for steuerrecht-anwalt-und-berater requests; it selects source skills through skills-index/steuerrecht-anwalt-und-berater.md and then reads the matching SKILL.md files."
---

# steuerrecht-anwalt-und-berater opencode skill router

> Generated router for the source plugin `steuerrecht-anwalt-und-berater`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `steuerrecht-anwalt-und-berater/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/steuerrecht-anwalt-und-berater.md`
- Source skill root: `steuerrecht-anwalt-und-berater/skills/`
- Source skills: 209

Plugin description: Steuerrecht für Anwalt (anw- FAO § 9) und Steuerberater (stb-): Einspruch Klage FG Aussenprüfung Selbstanzeige, Grundsteuer, Grunderwerbsteuer, Share Deals, Signing Closing, BWA SuSa Lohnbuchhaltung Jahresabschluss.

## Routing workflow

1. Read `skills-index/steuerrecht-anwalt-und-berater.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `steuerrecht-anwalt-und-berater/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
