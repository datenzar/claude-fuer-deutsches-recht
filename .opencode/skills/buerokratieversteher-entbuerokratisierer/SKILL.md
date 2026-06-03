---
name: buerokratieversteher-entbuerokratisierer
description: "buerokratieversteher-entbuerokratisierer: Allgemeiner Bürokratieversteher und Entbürokratisierer für Laien, Menschen mit Deutsch als Zweitsprache und alle, die Bescheide, Anträge, Vorladungen, Behördenbriefe, Jugendamt-, Schul-, Bau-, Sozial-, Familien- oder Kommunalverfahren verstehen und vorsichtig bearbeiten wollen. Use this opencode router for buerokratieversteher-entbuerokratisierer requests; it selects source skills through skills-index/buerokratieversteher-entbuerokratisierer.md and then reads the matching SKILL.md files."
---

# buerokratieversteher-entbuerokratisierer opencode skill router

> Generated router for the source plugin `buerokratieversteher-entbuerokratisierer`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `buerokratieversteher-entbuerokratisierer/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/buerokratieversteher-entbuerokratisierer.md`
- Source skill root: `buerokratieversteher-entbuerokratisierer/skills/`
- Source skills: 100

Plugin description: Allgemeiner Bürokratieversteher und Entbürokratisierer für Laien, Menschen mit Deutsch als Zweitsprache und alle, die Bescheide, Anträge, Vorladungen, Behördenbriefe, Jugendamt-, Schul-, Bau-, Sozial-, Familien- oder Kommunalverfahren verstehen und vorsichtig bearbeiten wollen.

## Routing workflow

1. Read `skills-index/buerokratieversteher-entbuerokratisierer.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `buerokratieversteher-entbuerokratisierer/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
