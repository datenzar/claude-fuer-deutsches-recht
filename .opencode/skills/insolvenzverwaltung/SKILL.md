---
name: insolvenzverwaltung
description: "insolvenzverwaltung: Freistehendes Insolvenzverwaltungs-Plugin aus Sicht von Insolvenzverwalter, Sachwalter und vorläufiger Verwaltung: Regelverfahren, Eigenverwaltung, Schutzschirm, Anfechtung, § 15b InsO, Masse, Forderungsprüfung, Insolvenzplan, StaRUG-Planwerkstatt, Gutachten, Berichte und Schlussrechnung. Use this opencode router for insolvenzverwaltung requests; it selects source skills through skills-index/insolvenzverwaltung.md and then reads the matching SKILL.md files."
---

# insolvenzverwaltung opencode skill router

> Generated router for the source plugin `insolvenzverwaltung`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `insolvenzverwaltung/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/insolvenzverwaltung.md`
- Source skill root: `insolvenzverwaltung/skills/`
- Source skills: 50

Plugin description: Freistehendes Insolvenzverwaltungs-Plugin aus Sicht von Insolvenzverwalter, Sachwalter und vorläufiger Verwaltung: Regelverfahren, Eigenverwaltung, Schutzschirm, Anfechtung, § 15b InsO, Masse, Forderungsprüfung, Insolvenzplan, StaRUG-Planwerkstatt, Gutachten, Berichte und Schlussrechnung.

## Routing workflow

1. Read `skills-index/insolvenzverwaltung.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `insolvenzverwaltung/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
