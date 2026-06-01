---
name: workflow-redteam-qualitygate
description: "Red-Team Qualitygate im Plugin regulatorisches-recht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton."
---

# Red-Team Qualitygate

## Aufgabe
Dieser Workflow-Skill für `regulatorisches-recht` Red-Team Qualitygate im Plugin regulatorisches-recht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Regulatorische Red-Team-Checks

- **Zuständigkeitscluster:** Welcher Regulator ist primär, welcher subsidiär? Bei mehreren parallel zuständigen Behörden (BaFin + LfDI bei DSGVO im Finanzsektor; BNetzA + BSI bei TK/Cybersicherheit; EU-Kommission + nationale Behörden bei DMA-Gatekeepern) — Kollision/Vorrang prüfen.
- **Anwendungsrang:** EU-Verordnung > EU-Richtlinie (mit Umsetzungsgesetz) > nationales Gesetz; bei Konflikt unionsrechtskonforme Auslegung, sonst Anwendungsvorrang (EuGH C-6/64).
- **Schwellenwerte verifizieren:** AI Act, DSA, NIS-2 haben individuell unterschiedliche Schwellen — kein Modellwissen ohne Live-Quelle. CSRD-Schwellen sind anders als CSDDD-Schwellen.
- **Übergangsfristen:** Bei AI Act, DORA, NIS-2, CSRD gibt es gestaffelte Anwendungstermine — vor Aussage konkretes Inkrafttreten je Pflichtenbereich prüfen.
- **Sanktionsmodell:** Verwaltungsbußgeld vs. Strafbarkeit vs. zivilrechtliche Haftung; bei mehreren Regimen Kumulation und Doppelbestrafungsverbot (Art. 50 GRCh, ne bis in idem; EuGH C-117/20 bpost SA, sofern frei verifizierbar).
- **Veröffentlichung:** Bei Sanktionen häufig Veröffentlichungspflicht (Pillory-Effekt); Reputationsrisiko separat bewerten.
- **Kein erfundenes Aktenzeichen:** EuGH-/EuG-Az., BaFin-/BNetzA-Bescheid-Az., DSK-Beschluss-Az. immer live verifizieren.

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
