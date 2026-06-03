---
name: selbstvertreter-sozialgericht
description: "selbstvertreter-sozialgericht: Selbstvertretung vor dem Sozialgericht ohne Anwalt: Anfänger-Workflow, Widerspruch, Klage, Eilantrag, Pflegegrad, Krankenkasse, Bürgergeld, EM-Rente, GdB, Belege, Gutachten, Kostenfreiheit, Sanity-Check, Rechtsprechungschat, Berufung. Use this opencode router for selbstvertreter-sozialgericht requests; it selects source skills through skills-index/selbstvertreter-sozialgericht.md and then reads the matching SKILL.md files."
---

# selbstvertreter-sozialgericht opencode skill router

> Generated router for the source plugin `selbstvertreter-sozialgericht`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `selbstvertreter-sozialgericht/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/selbstvertreter-sozialgericht.md`
- Source skill root: `selbstvertreter-sozialgericht/skills/`
- Source skills: 80

Plugin description: Selbstvertretung vor dem Sozialgericht ohne Anwalt: Anfänger-Workflow, Widerspruch, Klage, Eilantrag, Pflegegrad, Krankenkasse, Bürgergeld, EM-Rente, GdB, Belege, Gutachten, Kostenfreiheit, Sanity-Check, Rechtsprechungschat, Berufung.

## Routing workflow

1. Read `skills-index/selbstvertreter-sozialgericht.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `selbstvertreter-sozialgericht/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
