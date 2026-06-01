---
name: workflow-rechtsquellen-livecheck
description: "Rechtsquellen-Livecheck im Plugin kanzlei-builder-hub: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen."
---

# Rechtsquellen-Livecheck

## Aufgabe
Dieser Workflow-Skill für `kanzlei-builder-hub` Rechtsquellen-Livecheck im Plugin kanzlei-builder-hub: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Builder-Hub — Skill-Quellenstandard
- **Frontmatter-Validation:** Vor jedem Commit `validate-yaml-frontmatter.py` und `validate-plugin-structure.mjs` laufen lassen. Nur `name` (≤ 64 ASCII) und `description` (≤ 1024 Zeichen, keine Zahlen-Kommas) im YAML.
- **CLAUDE.md verbindlich:** Quellenpflicht aus `references/zitierweise.md`; Methodik aus `references/methodik-buergerliches-recht.md`.
- **Skill-Innenstruktur** (CLAUDE.md): (1) Zweck und Anwendungsfall, (2) Eingaben, (3) Ablauf/Checkliste, (4) Quellenpflicht, (5) Ausgabeformat, (6) Beispiele.
- **Hallunzinationssperre:** keine erfundenen Aktenzeichen; "BGH ständige Rspr." statt erfundene Az.; Kommentar-/Aufsatz-Fundstellen nur mit Live-Beleg.
- **Spracheinstellung:** Alle Skills auf Deutsch (englische Fachbegriffe nur, wenn etabliert und erklärt: LoI, Term Sheet, Due Diligence).
- **Audit-Tauglichkeit:** Jeder Skill muss reproduzierbar sein — bei Re-Run mit gleichen Eingaben gleiches Ergebnis (innerhalb der Modell-Streuung); deshalb klare Checklisten, keine "kreative Improvisation".
- Falle: Skill-Description mit "1,5 Jahren" → Validator schlägt fehl (Zahlen-Komma); schreibe "1.5 Jahren" oder "eineinhalb Jahren".
