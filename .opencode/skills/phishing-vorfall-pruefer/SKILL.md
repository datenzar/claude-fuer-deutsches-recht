---
name: phishing-vorfall-pruefer
description: "phishing-vorfall-pruefer: Freistehender Phishing-Vorfall-Prüfer für Online-Banking: BGB § 675u, § 675v, § 675w, pushTAN, Call-ID-Spoofing, grobe Fahrlässigkeit, Beweislast, Bankpflichten, Schlichtung und Klage. Use this opencode router for phishing-vorfall-pruefer requests; it selects source skills through skills-index/phishing-vorfall-pruefer.md and then reads the matching SKILL.md files."
---

# phishing-vorfall-pruefer opencode skill router

> Generated router for the source plugin `phishing-vorfall-pruefer`. It keeps opencode's visible skill catalog small; it is not a replacement for the source skill bodies.

## Source plugin

- Manifest: `phishing-vorfall-pruefer/.claude-plugin/plugin.json`
- Skill catalog: `skills-index/phishing-vorfall-pruefer.md`
- Source skill root: `phishing-vorfall-pruefer/skills/`
- Source skills: 54

Plugin description: Freistehender Phishing-Vorfall-Prüfer für Online-Banking: BGB § 675u, § 675v, § 675w, pushTAN, Call-ID-Spoofing, grobe Fahrlässigkeit, Beweislast, Bankpflichten, Schlichtung und Klage.

## Routing workflow

1. Read `skills-index/phishing-vorfall-pruefer.md` first. It is the compact catalog for the source skills in this plugin.
2. Match the user request to the smallest useful set of source skills. Prefer specific source skills over broad entry skills when the task is clear.
3. Read every selected source file under `phishing-vorfall-pruefer/skills/<skill-name>/SKILL.md`.
4. Treat the selected source skill body as the operative prompt for the task. Do not answer from this router alone.
5. Keep the repository instructions from `AGENTS.md`, `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` in force.
6. If the user names a concrete source skill, read that source `SKILL.md` directly before working.
