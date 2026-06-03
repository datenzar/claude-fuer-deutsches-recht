---
name: meinungspruefer
description: "meinungspruefer: Meinungsprüfer für Äußerungsrecht: Meinung oder Tatsache, Beleidigung, üble Nachrede, Verleumdung, § 188 StGB, Art. 5 GG, Art. 10 EMRK, Art. 11 GRCh, EGMR/EuGH, OLG-Praxis, US-Supreme-Court-Vergleich, Zivilrecht, Plattformen, Social Media, Arbeitsplatz, Schule und kommunale Machtkritik. Use this opencode router for meinungspruefer requests; it selects source skills through skills-index/meinungspruefer.md and then reads the matching SKILL.md files."
---

# meinungspruefer opencode skill router

> Generated router for the source plugin `meinungspruefer`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `meinungspruefer/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/meinungspruefer.md`
- Source skill root: `meinungspruefer/skills/`
- Source skills: 50

Plugin description: Meinungsprüfer für Äußerungsrecht: Meinung oder Tatsache, Beleidigung, üble Nachrede, Verleumdung, § 188 StGB, Art. 5 GG, Art. 10 EMRK, Art. 11 GRCh, EGMR/EuGH, OLG-Praxis, US-Supreme-Court-Vergleich, Zivilrecht, Plattformen, Social Media, Arbeitsplatz, Schule und kommunale Machtkritik.

## Routing workflow

1. Read `skills-index/meinungspruefer.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `meinungspruefer/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
