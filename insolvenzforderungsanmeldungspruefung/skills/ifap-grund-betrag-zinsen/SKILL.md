---
name: ifap-grund-betrag-zinsen
description: "Prüft Anspruchsgrund, Hauptforderung, Teilzahlungen, Gutschriften, Zinsen, Kosten und rechnerische Konsistenz der Anmeldung."
---

# Grund, Betrag und Zinsen

## Aufgabe

Zerlegt die angemeldete Forderung in prüfbare Teilpositionen und macht Rechenfehler sichtbar.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Betrag passt nicht zu Belegen
- Zinsen sind angemeldet
- Teilzahlungen oder Gutschriften stehen im Raum

## Workflow

1. Anspruchsgrund konkretisieren: Vertrag, Lieferung, Dienstleistung, Darlehen, Steuer, Lohn, Schaden, Kosten, Titel.
2. Hauptforderung aus Anmeldung und Belegen in Teilpositionen zerlegen.
3. Teilzahlungen, Gutschriften, Aufrechnungen, Skonto, Storno und Sicherheiten abziehen oder als ungeklärt markieren.
4. Zinsen prüfen: Beginn, Zinssatz, Zeitraum bis Eröffnung, Rechtsgrund, Verzugsnachweis, titulierte Zinsen.
5. Kosten prüfen: Mahnkosten, Rechtsverfolgungskosten, Gerichtskosten, Inkasso, tituliert oder nicht tituliert.
6. Feststellbarer und zu bestreitender Betrag getrennt ausgeben.

## Ausgabe

- Betragsrechnung
- Zinsrechnung
- Teilbestreitensvorschlag
- Rechenprotokoll

## Qualitätsgates

- Zinsen nach Verfahrenseröffnung werden nicht blind als Insolvenzforderung übernommen.
- Teilzahlungen werden quellenbezogen dokumentiert.
- Rundungs- und Währungsfragen werden offengelegt.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.
