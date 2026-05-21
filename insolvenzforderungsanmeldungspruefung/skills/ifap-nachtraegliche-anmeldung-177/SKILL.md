---
name: ifap-nachtraegliche-anmeldung-177
description: "Steuert verspätete, geänderte und nachträgliche Forderungsanmeldungen nach § 177 InsO mit Kosten-, Termin- und Schriftverfahrenslogik."
---

# Nachträgliche Anmeldung nach § 177 InsO

## Aufgabe

Ordnet späte und geänderte Anmeldungen in Prüfungstermin, Sondertermin oder schriftliches Verfahren ein.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Anmeldung kommt nach Fristablauf
- Anmeldung wird geändert
- Prüfungstermin ist vorbei

## Workflow

1. Zeitpunkt der Anmeldung gegenüber Anmeldefrist und Prüfungstermin feststellen.
2. Prüfen, ob Prüfung im bestehenden Termin möglich ist oder besonderer Termin/schriftliches Verfahren nötig wird.
3. Kostenfolge und Säumigenhinweis als organisatorischen Punkt markieren.
4. Änderung von neuer Forderung unterscheiden.
5. Nachträgliche Prüfung in Tabellenstand und Wiedervorlagen einbauen.

## Ausgabe

- Nachtragsvermerk
- Termin-/Schriftverfahrensvorschlag
- Kostenhinweis
- aktualisierter Tabellenstatus

## Qualitätsgates

- Nachtrag wird nicht als neue Dublette behandelt, wenn er dieselbe Forderung ergänzt.
- Fristlage wird mit konkretem Datum ausgegeben.
- Alte und neue Beträge bleiben nachvollziehbar.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.
