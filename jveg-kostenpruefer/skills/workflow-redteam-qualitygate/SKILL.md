---
name: workflow-redteam-qualitygate
description: "Red-Team Qualitygate im Plugin jveg-kostenpruefer: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton."
---

# Red-Team Qualitygate

## Aufgabe
Dieser Workflow-Skill prüft die fertige JVEG-Kostenfestsetzung gegen typische Fehlerquellen: Honorargruppen-Fehlzuordnung, Stundenzahl-Inplausibilität, Wegegeld-Doppelung, fehlende Belege, Umsatzsteuer-Klippe (§ 12 JVEG).

## JVEG-spezifische Prüfpunkte
- **Honorargruppe nachvollziehbar?** Anlage 1 JVEG: Gruppen 1 bis 12. Begründung im Beschluss vorhanden? (BVerwG, Beschl. v. 31.05.2022 - 9 KSt 1.22 zur Bindung an Heranziehung.)
- **Stundensatz korrekt?** § 9 Abs. 1 JVEG: aktuelle Sätze laut KostRÄG-Stand prüfen unter `gesetze-im-internet.de/jveg`.
- **Zeitaufwand erforderlich?** § 8 Abs. 2 JVEG: nur notwendiger Zeitaufwand vergütungsfähig. Reine Wartezeit nur unter § 19 JVEG.
- **Auslagen belegt?** § 5 JVEG (Fahrt: 0,42 EUR/km Pkw oder BC100), § 6 JVEG (Tage-/Übernachtungsgeld), § 7 JVEG (Schreibauslagen).
- **Umsatzsteuer:** § 12 JVEG (Ust nur bei Steuerpflicht des SV; nicht bei Kleinunternehmer § 19 UStG).
- **Pauschalvereinbarung:** § 13 JVEG nur mit Zustimmung des Sachverständigen und schriftlich.
- **Frist Erinnerung:** § 4 Abs. 1 JVEG -- sechs Monate ab Bekanntgabe der Festsetzung; ohne Aufschub.
- Falle: Vergleich von Stundensätzen aus alten Beschlüssen (vor KostRÄG 2021/2022) ohne Hinweis auf aktuelle Fassung.

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
