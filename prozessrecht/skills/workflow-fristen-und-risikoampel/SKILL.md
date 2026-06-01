---
name: workflow-fristen-und-risikoampel
description: "Fristen- und Risikoampel im Plugin prozessrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen."
---

# Fristen- und Risikoampel

## Aufgabe
Dieser Workflow-Skill markiert prozessuale Fristen nach ZPO/FamFG/VwGO/SGG/FGO/StPO und ordnet Risiken nach Eskalationsbedarf (Rot/Gelb/Grün) für die Mandatsakte.

## Wichtige Fristen ZPO
- **Klageerwiderung:** Frist durch Gericht gesetzt (§ 277 ZPO), regelmäßig 2-4 Wochen.
- **Berufung:** Berufungsschrift binnen 1 Monat (§ 517 ZPO), Begründung binnen 2 Monaten (§ 520 Abs. 2 ZPO) -- jeweils ab Zustellung des vollständigen Urteils.
- **Revision:** Einlegung 1 Monat (§ 548 ZPO), Begründung 2 Monate (§ 551 Abs. 2 ZPO).
- **Sofortige Beschwerde:** 2 Wochen (§ 569 ZPO).
- **Wiedereinsetzung:** 2 Wochen ab Wegfall des Hindernisses (§ 234 Abs. 1 ZPO).
- **Einspruch gegen Versäumnisurteil:** 2 Wochen ab Zustellung (§ 339 ZPO).

## Andere Verfahrensordnungen (zur Abgrenzung)
- **VwGO Klage:** 1 Monat nach Bekanntgabe des Widerspruchsbescheids (§ 74 VwGO); Berufung 1 Monat (§ 124a VwGO).
- **SGG:** Klage 1 Monat ab Bekanntgabe (§ 87 SGG); Berufung 1 Monat (§ 151 SGG).
- **FGO:** Klage 1 Monat ab Bekanntgabe der Einspruchsentscheidung (§ 47 FGO).
- **StPO:** Berufung/Revision je nach Verfahren (Berufung 1 Woche nach Verkündung, Revisionsbegründung 1 Monat nach Zustellung).
- **FamFG:** Beschwerde 1 Monat (§ 63 FamFG); Rechtsbeschwerde 1 Monat (§ 71 FamFG).

## Risikoampel
- **Rot:** Frist <= 3 Tage, drohender Fristverlust, Versäumnisurteil-Risiko.
- **Gelb:** Frist innerhalb der nächsten 14 Tage.
- **Grün:** Frist > 14 Tage oder keine harte Frist.

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
