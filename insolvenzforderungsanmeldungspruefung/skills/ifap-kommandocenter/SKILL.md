---
name: ifap-kommandocenter
description: "Startet die Insolvenzforderungsanmeldungsprüfung vom Eingang bis zur Tabelle, erkennt Verfahrensstand, Rolle, Fristen und nächste sichere Aktion."
---

# Kommandocenter für die Forderungsprüfung

## Aufgabe

Steuert den gesamten Prüfpfad von Eingangsstapel bis Tabellen- und Streitnachlauf.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- neuer Eingangsstapel
- unklare Forderungsanmeldung
- Prüfungstermin steht bevor
- Tabelle muss bereinigt werden

## Workflow

1. Verfahrensdaten aufnehmen: Gericht, Aktenzeichen, Eröffnungsdatum, Anmeldefrist, Prüfungstermin, schriftliches Verfahren.
2. Material sortieren: Eingangskanal, Gläubiger, Forderungsart, Betrag, Rang, Belege, Titel und Nachträge.
3. Arbeitsmodus wählen: Einzelprüfung, Batchprüfung, Nachforderung, Tabellenimport, Prüfungstermin oder Streitnachlauf.
4. Rote Schwellen markieren: vbuH, Titel, Nachrang, Absonderung, Masseforderung, Arbeitnehmerforderung, Steuer/SV, Dublette.
5. Konkrete nächste Ausgabe erzeugen: Prüfplan, Rückfragenliste, Tabellenzeilen oder Entscheidungsvermerk.

## Ausgabe

- Prüfpfad mit Prioritäten
- offene Rückfragen
- nächster Skill-Vorschlag
- Risikoampel je Forderung

## Qualitätsgates

- Keine Feststellung ohne Belegkette.
- Jede streitige Forderung erhält einen Nachlaufvermerk.
- Fristen und Prüfungstermin werden sichtbar gemacht.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.
