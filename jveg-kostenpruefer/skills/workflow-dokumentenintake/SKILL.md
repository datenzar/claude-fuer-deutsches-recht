---
name: workflow-dokumentenintake
description: "Dokumentenintake im Plugin jveg-kostenpruefer: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte."
---

# Dokumentenintake

## Aufgabe
Dieser Workflow-Skill liest Sachverständigen- und Dolmetscher-Rechnungen, Stundenaufstellungen, Heranziehungsbeschlüsse und Festsetzungsbescheide nach JVEG ein. Er ordnet die Posten nach §§ JVEG zu und markiert kritische Stellen für die Kostenprüfung.

## Dokumentenarten
- **Heranziehungsbeschluss** (§ 404 ZPO / § 73 StPO): definiert Auftragsumfang, ggf. Vorgabe der Honorargruppe (§ 9 JVEG).
- **Rechnung Sachverständige:** Stundenanzahl, Honorargruppe (§ 9 Abs. 1 JVEG, Anlage 1), Auslagen (§§ 5-8 JVEG), Umsatzsteuer (§ 12 JVEG).
- **Rechnung Dolmetscher/Übersetzer:** § 9 Abs. 3 JVEG (Stundensätze), § 11 JVEG (Übersetzung pro Zeile), Wartezeit (§ 19 JVEG).
- **Festsetzungsbeschluss / Anweisung:** § 4 JVEG; daran misst sich die Erinnerung (§ 4 Abs. 3 JVEG).

## Erste Triage
- Welche Honorargruppe wurde herangezogen, welche begehrt? Anlage 1 JVEG vergleichen.
- Wurde Pauschalvergütung (§ 13 JVEG) vereinbart?
- Auslagen (Fahrtkosten § 5 JVEG, Übernachtung § 6 JVEG, Tagegelder § 6 Abs. 1 Nr. 2 JVEG) plausibel und belegt?
- Vorschuss/Anzahlung (§ 3 JVEG) berücksichtigt?

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
