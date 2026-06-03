---
name: gewerblicher-rechtsschutz
description: "gewerblicher-rechtsschutz: Gewerblicher Rechtsschutz – DPMA/EUIPO-Markenrecherche und -anmeldung, Freedom-to-Operate, Patentscreening, UWG- und Urheberrechts-Abmahnung (Versand und Reaktion), Open-Source-Compliance, IP-Klausel-Review, Schutzrechts-Fristen. Use this opencode router for gewerblicher-rechtsschutz requests; it selects source skills through skills-index/gewerblicher-rechtsschutz.md and then reads the matching SKILL.md files."
---

# gewerblicher-rechtsschutz opencode skill router

> Generated router for the source plugin `gewerblicher-rechtsschutz`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `gewerblicher-rechtsschutz/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/gewerblicher-rechtsschutz.md`
- Source skill root: `gewerblicher-rechtsschutz/skills/`
- Source skills: 54

Plugin description: Gewerblicher Rechtsschutz – DPMA/EUIPO-Markenrecherche und -anmeldung, Freedom-to-Operate, Patentscreening, UWG- und Urheberrechts-Abmahnung (Versand und Reaktion), Open-Source-Compliance, IP-Klausel-Review, Schutzrechts-Fristen.

## Routing workflow

1. Read `skills-index/gewerblicher-rechtsschutz.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `gewerblicher-rechtsschutz/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
