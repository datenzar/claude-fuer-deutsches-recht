---
name: workflow-output-waehlen
description: "Output wählen im Plugin kanzlei-builder-hub: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung."
---

# Output wählen

## Aufgabe
Dieser Workflow-Skill bestimmt das Builder-Output: neue SKILL.md, Plugin-Skeleton, Refactor eines Bestands-Skills, Test-Akte, Plugin-Manifest (`plugin.json`), CI-/Validator-Konfig.

## Output-Typen Builder-Hub
- **SKILL.md (neu):** Frontmatter genau `name` (ASCII, Kebab-Case, ≤ 64 Zeichen) und `description` (≤ 1024 Zeichen, keine Komma-Zahlen).
- **Plugin-Skeleton:** `plugin.json` (`name`, `version`, `description`), `README.md`, `skills/`, optional `assets/`, `references/`, `tests/`.
- **Refactor bestehender Skill:** Innenstruktur (Zweck, Eingaben, Ablauf, Quellenpflicht, Output, Beispiele); Querverweise prüfen.
- **Test-Akte:** unter `testakten/` oder pluginspezifisch; reproduzierbarer Eingang für Validierung.
- **CI/Validator:** Anpassung in `scripts/`; Lauf `python3 scripts/validate-yaml-frontmatter.py` und `node scripts/validate-plugin-structure.mjs`.

## Konventionen
- Sprache Deutsch (CLAUDE.md). Englische Fachbegriffe nur, wenn etabliert (Letter of Intent, Term Sheet, Due Diligence) -- erklärt.
- Frontmatter strikt: keine zusätzlichen Felder (kein `triggers`, `when_to_use`, `language`, `rechtsgebiet`, `license`, `argument-hint`, `user-invocable`, `allowed_tools`, `tools`, `model`, `adapted_from`, `version`, `related_skills`).
- Querverweise zwischen Skills via Markdown-Link.

## Anti-Muster
- Komma-Zahlen in `description` (`1,5` statt `1.5`).
- Englische Frontmatter-Werte.
- Skill ohne Zweck-Sektion ("ein Helper für ...") -- macht Suche unmöglich.

## Kaltstart
Wenn Material vorliegt, arbeite zuerst mit dem Material. Stelle nur Rückfragen, die für die nächste Weiche nötig sind:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.
