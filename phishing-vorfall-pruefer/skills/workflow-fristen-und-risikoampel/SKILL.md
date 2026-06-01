---
name: workflow-fristen-und-risikoampel
description: "Fristen- und Risikoampel im Plugin phishing-vorfall-pruefer: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen."
---

# Fristen- und Risikoampel

## Aufgabe
Dieser Workflow-Skill für `phishing-vorfall-pruefer` Fristen- und Risikoampel im Plugin phishing-vorfall-pruefer: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Phishing-typische Fristen
- **§ 676b Abs. 2 BGB**: Anzeigepflicht des Zahlers gegenüber der Bank bei nicht autorisierter / fehlerhafter Zahlung **unverzüglich**, spätestens **13 Monate** nach Belastung.
- **§ 675u BGB**: Erstattungsanspruch bei nicht autorisierter Zahlung — Bank muss **unverzüglich**, spätestens am nächsten Geschäftstag erstatten.
- **Art. 33 DSGVO**: 72 Stunden Datenpannenmeldung (falls Datenleck).
- **§ 32 BSIG (NIS2)**: 24h Frühwarnung, 72h Initialbericht, 1 Monat Abschlussbericht (für betroffene Einrichtungen).
- **Strafanzeige**: keine Frist, aber: § 263 StGB Verjährung 5 Jahre nach Tat (§ 78 StGB).
- **Zivilrechtliche Verjährung**: Regelfrist 3 Jahre § 195 BGB, beginnt mit Schluss des Jahres der Kenntnis § 199 BGB.

## Ampelkriterien
- **Rot**: 13-Monats-Frist § 676b BGB läuft ab, Bank verweigert Erstattung, Strafanzeige eilig (Geldverbergung), grobe Datenpanne, NIS2 oder Art. 33 DSGVO unmittelbar offen.
- **Gelb**: Mitverschulden des Kunden möglich (§ 675v BGB), Beweissicherung unvollständig (E-Mail-Header, IP, Screenshots), Versicherung nicht informiert.
- **Grün**: Anzeige bei Bank rechtzeitig, Strafanzeige bei Polizei mit Aktenzeichen, Beweise gesichert, ggf. Cyberversicherung informiert.

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
