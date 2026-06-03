---
name: common-law-kompass
description: "common-law-kompass: Freistehendes Common-Law-Plugin für deutsche Wirtschaftsjuristen: UK/US-False-Friends, Vertragsbegriffe, Consideration, Suretyship, Indemnity, UCC, Precedent, Discovery und bilinguale Drafting-Reviews. Use this opencode router for common-law-kompass requests; it selects source skills through skills-index/common-law-kompass.md and then reads the matching SKILL.md files."
---

# common-law-kompass opencode skill router

> Generated router for the source plugin `common-law-kompass`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `common-law-kompass/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/common-law-kompass.md`
- Source skill root: `common-law-kompass/skills/`
- Source skills: 54

Plugin description: Freistehendes Common-Law-Plugin für deutsche Wirtschaftsjuristen: UK/US-False-Friends, Vertragsbegriffe, Consideration, Suretyship, Indemnity, UCC, Precedent, Discovery und bilinguale Drafting-Reviews.

## Routing workflow

1. Read `skills-index/common-law-kompass.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `common-law-kompass/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
