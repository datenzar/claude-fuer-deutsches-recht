---
name: workflow-redteam-qualitygate
description: "Red-Team Qualitygate im Plugin kanzlei-builder-hub: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton."
---

# Red-Team Qualitygate

## Aufgabe
Dieser Workflow-Skill für `kanzlei-builder-hub` Red-Team Qualitygate im Plugin kanzlei-builder-hub: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Builder-Hub Quality-Gate für neue Skills
- **Validator-Lauf:** `python3 scripts/validate-yaml-frontmatter.py` und `node scripts/validate-plugin-structure.mjs` — beide ohne Fehler/Warnungen.
- **Frontmatter:** Genau `name` und `description`. Keine weiteren Felder (kein `triggers`, `when_to_use`, `language`, `rechtsgebiet`, `license`, `argument-hint`, `user-invocable`, `allowed_tools`, `tools`, `model`, `adapted_from`, `version`, `related_skills`).
- **Description-Länge:** max. 1024 Zeichen, KEINE Zahlen-Kommas (statt "1,5" schreibe "1.5" oder "eineinhalb").
- **Skill-Name:** max. 64 ASCII-Zeichen, kein Umlaut, kein Sonderzeichen außer Bindestrich.
- **Innenstruktur:** (1) Zweck/Anwendungsfall, (2) Eingaben, (3) Ablauf/Checkliste, (4) Quellenpflicht, (5) Ausgabeformat, (6) Beispiele.
- **Sprache:** Deutsch. Englische Fachbegriffe nur, wenn etabliert und erklärt.
- **Halluzinationssperre:** Keine erfundenen BGH/EuGH-Az.; "BGH ständige Rspr." statt erfundene Az.; Kommentar-/Aufsatz-Fundstellen nur mit Live-Beleg.
- **Reproduzierbarkeit:** Skill muss auch bei Re-Run mit gleichen Eingaben gleiches Ergebnis liefern (Modell-Streuung minimieren durch klare Checklisten).
- **Plugin-Konsistenz:** Skill verweist auf andere Skills des Plugins; keine Selbstreferenz.
- Falle: Beim Refactoring den Skill-Name ändern, ohne Verweise in anderen Skills nachzuziehen → broken-links nicht prüfbar.
