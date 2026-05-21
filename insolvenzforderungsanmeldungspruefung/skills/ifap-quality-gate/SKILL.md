---
name: ifap-quality-gate
description: "Prüft vor Tabelle, Prüfungstermin, Bestreiten, Feststellung und Verteilung die Vollständigkeit, Plausibilität, Quellen und roten Risiken."
---

# Qualitätsgate und Plausibilitätskontrolle

## Aufgabe

Stoppt unvollständige, unplausible oder zu riskante Ausgaben vor Import, Versand und Verteilung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- vor Import
- vor Prüfungstermin
- vor Versand
- vor Verteilung
- bei hohem Risiko

## Workflow

1. Vollständigkeit prüfen: Anmeldung, Belege, Betrag, Rang, Status, Entscheidung, Bearbeiter, Datum.
2. Plausibilität prüfen: Summen, Zinsen, Dubletten, Titel, OPOS, Nachträge, Nachrang, vbuH, Masseabgrenzung.
3. Rechtsquellencheck: Normen nur aus aktueller amtlicher Quelle oder geprüfter Kanzleiquelle verwenden.
4. Ausgabecheck: verständlich, tabellentauglich, keine überschießende Rechtsberatung, keine geheimen internen Notizen im Außenbrief.
5. Freigabe verlangen, wenn rote Schwellen berührt sind.

## Ausgabe

- QA-Protokoll
- Korrekturliste
- Freigabevermerk
- Rest-Risiko-Liste

## Qualitätsgates

- Rote Schwellen stoppen den Automatismus.
- Jede Zahl muss aus Quelle oder Rechnung herleitbar sein.
- Außenkommunikation und interne Bewertung bleiben getrennt.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.
