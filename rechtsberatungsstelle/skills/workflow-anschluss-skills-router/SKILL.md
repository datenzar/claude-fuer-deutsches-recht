---
name: workflow-anschluss-skills-router
description: "Anschluss-Skills Router im Plugin rechtsberatungsstelle: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor."
---

# Anschluss-Skills Router

## Aufgabe
Dieser Workflow-Skill leitet Rechtsuchende einer niedrigschwelligen Beratungsstelle in den passenden Folgeschritt: Beratungshilfeschein-Antrag, PKH-Vorbereitung, Mietverein, Sozialverband, Verbraucherzentrale, Schuldnerberatung, Frauenberatungsstelle, Schwerbehindertenberatung oder Verweisung an Anwalt.

## Routing-Heuristik
- **Eilige Frist:** sofortige Triage; bei kurzem Zeitfenster -> Anwalt mit PKH-Antrag.
- **Sozialleistungen / Bürgergeld:** Sozialverband (VdK, SoVD), DGB, Caritas/Diakonie; bei Klage SGG kostenfrei (§ 183 SGG).
- **Mietrecht:** Mieterverein (Mitgliedschaft Voraussetzung); ohne Mitgliedschaft Verbraucherzentrale oder Anwalt mit BerHG.
- **Verbraucherrecht (Vertrag, Reklamation, Versicherung):** Verbraucherzentrale (kostengünstige Erstberatung), `verbraucherzentrale.de`.
- **Schulden:** Schuldnerberatung (städtisch, Caritas, Diakonie); InsoBeratung für Privatinsolvenz.
- **Migration/Aufenthalt:** MBE (Migrationsberatung für Erwachsene), JMD (Jugendmigrationsdienst), Fluechtlingsrat, Verfahrensberatung.
- **Familienrecht (Trennung, Sorge, Unterhalt):** Beratung Jugendamt (§ 17, 18 SGB VIII), Mütter-/Familienberatung; bei Klage Anwalt mit PKH.
- **Gewalt in der Familie:** Frauenhaus, Hilfetelefon 08000 116 016; Polizei für Gewaltschutzanordnung § 1 GewSchG.
- **Schwerbehindertenrecht:** Beratungsstellen der Länder (EUTB -- Ergänzende unabhängige Teilhabeberatung).

## Anti-Muster
- Beratungsstelle uebersteigt Beratungstiefe -> RDG-Grenze beachten (§§ 6, 7 RDG).
- Eilfristen versaeumen, weil Beratungsstelle zu langsam vermittelt -> Eskalation an Anwalt.

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
