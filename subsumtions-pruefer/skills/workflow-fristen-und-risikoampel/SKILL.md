---
name: workflow-fristen-und-risikoampel
description: "Fristen- und Risikoampel im Plugin subsumtions-pruefer: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen."
---

# Fristen- und Risikoampel

## Aufgabe
Dieser Workflow-Skill markiert in einer Subsumtion typische Risiken (Sprung-Subsumtion, fehlende Definition, Zirkelschluss, übersehener Streitstand) und ordnet sie nach Schweregrad.

## Risikoampel Subsumtion
- **Rot:** Sprung-Subsumtion (Tatsache wird direkt unter die Norm gesetzt, ohne Definition). Heilung: Definition mit Quelle einsetzen, dann unter Definition subsumieren.
- **Rot:** Definition ohne Quelle (BGH, hM Kommentar). Heilung: Quelle ergänzen oder als "noch zu belegen" markieren.
- **Rot:** Zirkelschluss (Subsumtion wiederholt die Definition oder die Norm). Heilung: Tatsachen aus dem Sachverhalt zitieren, dann erst werten.
- **Gelb:** Streitstand übersehen, obwohl tragend. Heilung: hM, Mindermeinung, Argumente, Stellungnahme.
- **Gelb:** Konjunktiv im Schluss ("könnte vorliegen") -- Schluss soll Indikativ ("liegt vor").
- **Gelb:** Zwischenergebnis je Tatbestandsmerkmal fehlt -- Leserlichkeit leidet.
- **Grün:** Vollständige Subsumtion mit Quelle, klarer Sprache, Zwischenergebnis.

## Diagnose-Schritte
1. Jeden Satz markieren als "Norm", "Definition", "Tatsache", "Subsumtion" oder "Schluss".
2. Reihenfolge prüfen: Norm → Definition → Tatsache → Subsumtion → Schluss.
3. Lücken anzeigen.
4. Quellen zur Definition verlangen.

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
