---
name: ifap-intake-kanalcheck
description: "Erfasst Forderungsanmeldungen aus Post, E-Mail, Portal, Tabellenexport und Nachtrag mit Eingangsbuch, Metadaten und Dublettenverdacht."
---

# Intake und Kanalcheck

## Aufgabe

Erfasst eingehende Forderungsanmeldungen kanalneutral und bildet ein belastbares Eingangsbuch.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Posteingang liegt vor
- Portalexport oder CSV liegt vor
- Gläubiger sendet Nachtrag
- mehrere Kanäle enthalten dieselbe Forderung

## Workflow

1. Eingangskanal, Eingangsdatum, Dateiname, Absender, Vertreter und Gläubiger-ID erfassen.
2. Anmeldung von Begleitschreiben, Anlagen, Rechnungspaketen, Titeln und Zahlungsnachweisen trennen.
3. Fristlage prüfen: rechtzeitig, verspätet, geändert oder offensichtlich nur Ergänzung.
4. Dublettenindizien markieren: gleicher Gläubiger, gleiche Rechnung, gleicher Betrag, gleicher Zeitraum, gleicher Titel.
5. Eingangsbuch und Prüfnummer vergeben, ohne materiell zu entscheiden.

## Ausgabe

- Intake-Register
- Dublettenhinweise
- fehlende Mindestdaten
- Zuordnung zu bestehender Prüfnummer

## Qualitätsgates

- Nachträge werden an die ursprüngliche Anmeldung geklebt.
- E-Mail-Text und Anlagen werden getrennt ausgewertet.
- Unlesbare Dateien werden nicht stillschweigend ignoriert.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.
