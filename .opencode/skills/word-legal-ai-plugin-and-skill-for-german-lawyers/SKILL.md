---
name: word-legal-ai-plugin-and-skill-for-german-lawyers
description: "word-legal-ai-plugin-and-skill-for-german-lawyers: Word Legal AI for German Lawyers: Kaltstart, Kanzleistil, makrofreies Word-Finish, Verträge, Schriftsätze, Memos, Redlines, Klauselbibliothek, Defensive Drafting, Term Sheet, DE-EN Bilingual, US/UK Legal Writing und englische Verträge nach deutschem Recht. Use this opencode router for word-legal-ai-plugin-and-skill-for-german-lawyers requests; it selects source skills through skills-index/word-legal-ai-plugin-and-skill-for-german-lawyers.md and then reads the matching SKILL.md files."
---

# word-legal-ai-plugin-and-skill-for-german-lawyers opencode skill router

> Generated router for the source plugin `word-legal-ai-plugin-and-skill-for-german-lawyers`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `word-legal-ai-plugin-and-skill-for-german-lawyers/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/word-legal-ai-plugin-and-skill-for-german-lawyers.md`
- Source skill root: `word-legal-ai-plugin-and-skill-for-german-lawyers/skills/`
- Source skills: 50

Plugin description: Word Legal AI for German Lawyers: Kaltstart, Kanzleistil, makrofreies Word-Finish, Verträge, Schriftsätze, Memos, Redlines, Klauselbibliothek, Defensive Drafting, Term Sheet, DE-EN Bilingual, US/UK Legal Writing und englische Verträge nach deutschem Recht.

## Routing workflow

1. Read `skills-index/word-legal-ai-plugin-and-skill-for-german-lawyers.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `word-legal-ai-plugin-and-skill-for-german-lawyers/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
