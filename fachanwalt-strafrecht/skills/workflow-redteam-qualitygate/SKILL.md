---
name: workflow-redteam-qualitygate
description: "Red-Team Qualitygate im Plugin fachanwalt-strafrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton."
---

# Red-Team Qualitygate

## Aufgabe
Dieser Workflow-Skill für `fachanwalt-strafrecht` Red-Team Qualitygate im Plugin fachanwalt-strafrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Strafrechts-Red-Team-Checks
- **Halluzinations-Check:** Keine erfundenen BGH/BVerfG-Az; bei staendiger Rspr. nur "BGH-Linie / staendige Rspr." schreiben.
- **Frist-Re-Check** alle Verfahrensschritte: Berufung § 314 StPO (1 Woche), Revision § 341 StPO (1 Woche) + § 345 StPO (1 Monat), Strafbefehl-Einspruch § 410 StPO (2 Wochen), Beschwerde § 311 StPO (sofortige 1 Woche; einfache § 304 StPO unbefristet), Wiedereinsetzung § 44 StPO (1 Woche ab Wegfall), Klageerzwingungsverfahren § 172 StPO.
- **Belehrungs-Re-Check:** § 136 StPO Beschuldigtenbelehrung; § 52 StPO Zeugnisverweigerung Angehoeriger; § 55 StPO Auskunftsverweigerung; § 257c V StPO Verstaendigungsbelehrung; qualifizierte Belehrung bei Wiederholung der Vernehmung.
- **Beweisverwertungs-Check:** § 136a StPO verbotene Vernehmungsmethoden; § 252 StPO Sperrwirkung; Beweisverwertungsverbote bei Belehrungsmaengeln (BGH-Linie).
- **Verfahrensruegen-Check fuer Revision:** absoluter Revisionsgrund § 338 StPO (Besetzung, Ausschlussgruende, Sachleitung); relativer § 337 StPO; Verstaendigungsmaengel § 257c StPO; Akteneinsichts-Verletzung § 147 StPO.
- **Vollmachts-Check:** Mandatsvollmacht; Vertretungsvollmacht fuer § 411 II StPO bei Strafbefehl, § 232 StPO bei Abwesenheitsverhandlung.
- **Konsequenzen-Re-Check:** BZRG-Eintrag, FZR-Eintrag, berufsrechtliche Konsequenzen (Beamtenrecht, Aerzte, Rechtsanwaelte), auslaendische Folgen (Visum, Niederlassung).
- **Mandantengeheimnis** § 43a Abs. 2 BRAO, § 203 StGB, § 53 I Nr. 2 StPO Zeugnisverweigerung.
