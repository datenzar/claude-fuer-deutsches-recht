---
name: workflow-anschluss-skills-router
description: "Anschluss-Skills Router im Plugin kanzlei-builder-hub: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor."
---

# Anschluss-Skills Router

## Aufgabe
Dieser Workflow-Skill leitet im Plugin `kanzlei-builder-hub` nach Klärung der Aufgabe in den richtigen Builder-Skill weiter: Neues Plugin anlegen, Skill erweitern, Frontmatter reparieren, Bibliothek erweitern, Tests schreiben.

## Routing nach Bauaufgabe
- **Neues Plugin:** Skeleton mit `plugin.json` (`name`, `version`, `description`), `README.md`, `skills/`-Verzeichnis. Kein Komma in Zahlen in `description`.
- **Neuer Skill:** Frontmatter genau `name` (ASCII, Kebab-Case, max. 64 Zeichen) und `description` (max. 1024 Zeichen).
- **Skill-Refactor:** Inhalt nach Struktur (Zweck, Eingaben, Ablauf, Quellen, Output, Beispiele); Querverweise auf andere Skills im Plugin via Markdown-Link.
- **Frontmatter-Fix:** verbotene Felder entfernen (`triggers`, `when_to_use`, `language`, `rechtsgebiet`, `license`, `argument-hint`, `user-invocable`, `allowed_tools`, `tools`, `model`, `adapted_from`, `version`, `related_skills`).
- **Validator-Lauf:** `python3 scripts/validate-yaml-frontmatter.py`, `node scripts/validate-plugin-structure.mjs`.
- **Skill-Index aktualisieren:** `scripts/generate-skills-md.py`, `scripts/generate-skills-overview.py`.

## Anti-Muster
- Englische Frontmatter-Werte oder erfundene Felder. Repo erwartet **nur** `name` und `description`.
- Beschreibungen mit `1,5` o. ä. (Komma-Zahlen verboten; nutze `1.5` oder `eineinhalb`).

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
