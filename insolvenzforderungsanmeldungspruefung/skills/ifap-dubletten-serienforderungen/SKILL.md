---
name: ifap-dubletten-serienforderungen
description: "Erkennt doppelte Forderungsanmeldungen, Serienrechnungen, Vertreterwechsel, Konzernforderungen und mehrfach eingereichte Titel."
---

# Dubletten und Serienforderungen

## Aufgabe

Findet Mehrfachanmeldungen und trennt echte Dubletten von ähnlichen Serienforderungen.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- gleiche Rechnung mehrfach
- Inkasso und Gläubiger melden parallel
- Konzernmeldungen überschneiden sich

## Workflow

1. Vergleichsschlüssel bilden: Gläubiger, Schuldnerkonto, Rechnungsnummer, Betrag, Zeitraum, Titel, Vertragsnummer.
2. Exakte Dubletten, wahrscheinliche Dubletten und bloß ähnliche Serienforderungen unterscheiden.
3. Vertreterwechsel und Inkasso-Zessionen prüfen: Forderungsinhaber, Vollmacht, Abtretung, Prozessstandschaft.
4. Bei Teilabtretungen und Konsortialforderungen Quoten und Teilbeträge trennen.
5. Entscheidung vorschlagen: zusammenführen, Nachweis verlangen, teilweise bestreiten, Doppelanmeldung bestreiten.

## Ausgabe

- Dublettenreport
- Zusammenführungsplan
- Zessions-/Vertretercheck
- Bestreitensvermerk

## Qualitätsgates

- Ähnliche Beträge sind nicht automatisch Dubletten.
- Inkassovertretung ist nicht Forderungsinhaberschaft.
- Zusammenführung bleibt im Audit-Trail nachvollziehbar.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.
