---
name: workflow-redteam-qualitygate
description: "Red-Team Qualitygate im Plugin aktenaufbereiter-strafrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton."
---

# Red-Team Qualitygate

## Aufgabe
Dieser Workflow-Skill für `aktenaufbereiter-strafrecht` Red-Team Qualitygate im Plugin aktenaufbereiter-strafrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Strafakte-Red-Team-Checks
- **Halluzinations-Check:** Keine erfundenen BGH-/BVerfG-Az; Fundstellen mit Datum, Gericht und Az pruefen oder als "staendige Rspr."/"BGH-Linie" markieren.
- **Frist-Re-Check:** Berufung § 314 StPO (1 Woche), Revision §§ 341, 345 StPO (1 Woche / 1 Monat), Strafbefehl-Einspruch § 410 StPO (2 Wochen), Wiedereinsetzung § 44 StPO (1 Woche ab Wegfall); Postzustellungsdatum verifizieren.
- **Zustaendigkeits-Re-Check:** GVG - Strafrichter § 25 (bis 2 Jahre Freiheitsstrafe), Schoeffengericht § 28 (bis 4 Jahre), Schwurgericht § 74 GVG (Toetungsdelikte), grosse Strafkammer § 76 GVG (ueber 4 Jahre, schwere Wirtschaftskriminalitaet). Verfahrenshandlung Falschadressiert?
- **Belehrungs-Check** § 136 StPO (Beschuldigtenrechte), § 52 StPO (Zeugnisverweigerung Angehoeriger), § 55 StPO (Auskunftsverweigerung wegen Selbstbelastung): in der Akte protokolliert?
- **Beweisverwertungs-Check:** § 136a StPO (verbotene Vernehmungsmethoden), § 252 StPO (Aussageverweigerung Hauptverhandlung), § 261 StPO Beweiswuerdigungslueckchen, Belehrungsfehler in Beschuldigtenvernehmung.
- **Ton-/Stil-Check:** keine wertende Vorverurteilung; klare Trennung Fakten / Bewertung; Mandantengeheimnis § 43a Abs. 2 BRAO, § 203 StGB.
- **Vollstaendigkeits-Check Anklageschrift § 200 StPO:** Beschuldigter, Tat (Zeit, Ort, gesetzliche Merkmale), Beweismittel, anzuwendende Strafvorschriften.
