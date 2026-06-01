---
name: workflow-anschluss-skills-router
description: "Anschluss-Skills Router im Plugin jurastudium: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor."
---

# Anschluss-Skills Router

## Aufgabe
Dieser Workflow-Skill leitet nach der ersten Prüfung in die passenden Spezialskills des Plugins `jurastudium`. Er entlastet Studierende und Referendare, indem er Sachverhalt, Klausurformat und Vorbereitungsphase einsortiert.

## Routing-Heuristik
- **Zivilrechtsklausur, Sachverhalt mit Anspruch:** -> `loesungsschemata`, `subsumtionslehre`, `gutachten-uebung`, `methodenlehre-zivilrecht`.
- **Öffentliches Recht (Verfassung/Verwaltung):** -> `methodenlehre-oeffentliches-recht`, `loesungsschemata` (Verfahren: Zulässigkeit, Begründetheit).
- **Strafrecht (Klausur oder AG):** -> `methodenlehre-strafrecht` (Aufbau: TB, RW, Schuld, ggf. Strafe).
- **Lernplanung/Karteikarten:** -> `lernplan`, `karteikarten`, `lernstrategien`, `examens-prognose`.
- **Hausarbeit:** -> `juristisches-schreiben`, Verweis auf Plugin `hausarbeitenmacher`.
- **Mündliche Prüfung / AG-Vortrag:** -> `pruefungsgespraech-ag`, `ag-vorbereitung`.
- **Referendariat (Aktenvortrag, Relation):** -> `jus-referendariat-stationen-spezial`, Plugin `urteilsbauer-relationsmacher`.

## Anti-Muster
- Schemata ohne Subsumtion. Schema ist Gerüst, nicht Ergebnis.
- Anspruchsgrundlagenreihenfolge ignorieren: stets Vertrag, c.i.c., GoA, dinglich, Delikt, Bereicherung.

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
