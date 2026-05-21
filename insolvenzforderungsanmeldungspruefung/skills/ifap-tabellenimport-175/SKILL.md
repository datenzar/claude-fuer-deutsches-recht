---
name: ifap-tabellenimport-175
description: "Erstellt Tabellenimport und Tabellenarbeitsstand nach § 175 InsO mit Grund, Betrag, Rang, vbuH, Widerspruch und Prüfstatus."
---

# Tabellenimport nach § 175 InsO

## Aufgabe

Überführt geprüfte Forderungen in eine saubere Tabellenstruktur.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Tabelle soll angelegt werden
- CSV-Import wird gebraucht
- gerichtlicher Arbeitsstand ist zu liefern

## Workflow

1. Pflichtspalten aus Verfahrenspraxis definieren: laufende Nummer, Gläubiger, Vertreter, Grund, Betrag, Rang, Status.
2. § 174-Angaben in Tabellenlogik übertragen, ohne Begründungen zu verlieren.
3. vbuH, Unterhalt, Steuerstraftat und Schuldnerhinweis gesondert kennzeichnen.
4. Bestreiten von Verwalter, Schuldner oder Gläubiger getrennt abbilden.
5. Exportformat als CSV und menschenlesbare Prüfliste ausgeben.

## Ausgabe

- Tabellenimport.csv
- Tabellenarbeitsstand
- Fehlerliste
- Importnotiz

## Qualitätsgates

- Keine Tabellenzeile ohne Prüfnummer.
- Widerspruchsperson wird getrennt vom Forderungsstatus erfasst.
- Sonderzeichen und Dezimalformate werden vor Import kontrolliert.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.
