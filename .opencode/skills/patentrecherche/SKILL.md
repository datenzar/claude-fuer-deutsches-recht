---
name: patentrecherche
description: "patentrecherche: Patentrecherche für Patentanwaelte agentisch in Espacenet Google Patents DPMAregister DEPATISnet EPO Register WIPO USPTO. Stand der Technik Neuheit § 3 PatG Art. 54 EPUe erfinderische Tätigkeit § 4 PatG Art. 56 EPUe Problem-Solution-Approach FTO CPC IPC INPADOC Recherchebericht. Use this opencode router for patentrecherche requests; it selects source skills through skills-index/patentrecherche.md and then reads the matching SKILL.md files."
---

# patentrecherche opencode skill router

> Generated router for the source plugin `patentrecherche`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `patentrecherche/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/patentrecherche.md`
- Source skill root: `patentrecherche/skills/`
- Source skills: 54

Plugin description: Patentrecherche für Patentanwaelte agentisch in Espacenet Google Patents DPMAregister DEPATISnet EPO Register WIPO USPTO. Stand der Technik Neuheit § 3 PatG Art. 54 EPUe erfinderische Tätigkeit § 4 PatG Art. 56 EPUe Problem-Solution-Approach FTO CPC IPC INPADOC Recherchebericht.

## Routing workflow

1. Read `skills-index/patentrecherche.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `patentrecherche/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
