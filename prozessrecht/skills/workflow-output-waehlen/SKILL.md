---
name: workflow-output-waehlen
description: "Output wählen im Plugin prozessrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung."
---

# Output wählen

## Aufgabe
Dieser Workflow-Skill bestimmt das prozessrechtliche Outputformat: Klage, Klageerwiderung, Replik/Duplik, Antrag auf einstweiligen Rechtsschutz, Berufung, Berufungsbegründung, Beschwerdebegründung, Streitwertfestsetzungsantrag.

## Output-Typen mit ZPO-Anker
- **Klageschrift (§ 253 ZPO):** Parteien, Gericht, bestimmter Antrag (Nr. 2), Klagegrund, Beweisangebote, ggf. Streitwert; bei Geldforderung exakt beziffert.
- **Klageerwiderung (§ 277 ZPO):** Erklärung zur Klage, Bestreiten mit Substanz (§ 138 ZPO), Beweisangebote, Gegenangriffe (Aufrechnung, Widerklage).
- **Replik:** Reaktion auf Klageerwiderung -- konzentriert, nicht Wiederholung.
- **Einstweiliger Rechtsschutz (§§ 935, 940 ZPO):** Verfügungsanspruch und Verfügungsgrund (Eilbedürftigkeit) glaubhaft machen (§ 294 ZPO: alle Beweismittel + eidesstattliche Versicherung).
- **Berufung (§§ 511 ff. ZPO):** Berufungsschrift binnen 1 Monat; Berufungsbegründung binnen 2 Monaten ab Zustellung des Urteils; konkrete Berufungsgründe nach § 520 Abs. 3 ZPO.
- **Beschwerdeschrift (§ 567 ZPO):** sofortige Beschwerde innerhalb von 2 Wochen, einfache Beschwerde unbefristet.
- **Schutzschrift:** vorbeugend gegen eV; Hinterlegung Zentrales Schutzschriftenregister (`schutzschriftenregister.de`).

## Methodik
- **Urteilsstil** (Indikativ) für Schriftsätze, nicht Gutachtenstil.
- **Beweismaß:** § 286 (volle Überzeugung) und § 287 ZPO (überwiegende Wahrscheinlichkeit) klar unterscheiden.
- **Verspätung:** § 296 ZPO -- neue Angriffs- und Verteidigungsmittel können präkludiert werden.

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
