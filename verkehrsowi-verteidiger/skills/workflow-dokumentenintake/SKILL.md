---
name: workflow-dokumentenintake
description: "Dokumentenintake im Plugin verkehrsowi-verteidiger: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte."
---

# Dokumentenintake

## Aufgabe
Dieser Workflow-Skill für `verkehrsowi-verteidiger` Dokumentenintake im Plugin verkehrsowi-verteidiger: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## OWi-Intake-Bausteine
- **Dokumente sortieren:**
  - Anhoerungsbogen / Zeugenfragebogen (kein Bescheid! Schweigerecht § 55 OWiG; Halterauskunft § 31a StVZO).
  - Bussgeldbescheid § 65 OWiG (Frist § 67 OWiG 2 Wochen!).
  - Verwarnung mit Verwarnungsgeld § 56 OWiG (nur bei Einverstaendnis, max. 55 EUR).
  - Messprotokoll / Messfoto / Eichschein (Bedienerschein / Schulungsnachweis).
  - Tatortskizze, Lichtbilder, Videosequenz.
  - Polizeibericht / Zeugenvernehmungsprotokoll.
  - Akteneinsichtsanforderung an Behoerde (§ 49 OWiG i.V.m. § 147 StPO).
- **Frist rot markieren:** Einspruch § 67 OWiG 2 Wochen ab Zustellung; Wiedereinsetzung § 52 OWiG.
- **Messdaten- / Rohdaten-Bestand:** Rohdaten der Messung (.case / .esa / .traf / .pdf), Statistik-Datei, Bedienerprotokoll, Lebensakte Geraet, Eichschein gueltig im Tatzeitraum, Geraete-Software-Version.
- **Tatvorwurfsspezifika identifizieren:** Geschwindigkeit (Toleranz, Messverfahren); Abstand (BAB / Landstrasse, Strecke); Rotlicht (qualifiziert ab 1 Sekunde, Fahrverbot); Handy (§ 23 Ia StVO Tatbestandsausweitung 2017: alle elektronischen Geraete); Alkohol/Drogen (BAK-Messung, Atemalkohol).
- **Konsequenzeneinschaetzung:** Geldbusse + Punkte FAER (1-3 Punkte) + Fahrverbot 1-3 Monate? Wiederholungstaeter § 4 II StVG (innerhalb 1 Jahres weitere Verstoesse hoeher bewertet)? 8-Punkte-Grenze § 4 V StVG?
- **Anschluss:** Akteneinsicht beantragen / Messverfahren-Pruefung / Einspruchsentscheidung.
