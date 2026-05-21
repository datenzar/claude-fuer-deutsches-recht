---
name: ifap-beleg-und-urkundencheck
description: "Prüft Rechnungen, Verträge, Titel, Lieferscheine, Kontoauszüge und sonstige Urkunden auf Belegkette, Lesbarkeit und Zuordnung."
---

# Beleg- und Urkundencheck

## Aufgabe

Bildet die Belegkette der Anmeldung und trennt belastbare Nachweise von bloßem Vortrag.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Anlagenstapel ist unübersichtlich
- Rechnungen fehlen
- Titel wird behauptet
- Buchhaltung widerspricht

## Workflow

1. Alle Belege inventarisieren: Typ, Datum, Nummer, Parteien, Betrag, Zeitraum, Datei, Lesbarkeit.
2. Belege der konkreten Forderungsposition zuordnen und Fremdbelege aussortieren.
3. Titelstatus prüfen: vollstreckbarer Titel, Endurteil, Mahnbescheid, Vergleich, Kostenfestsetzung, bloße Rechnung.
4. Schuldnerbuchhaltung und OPOS abgleichen: gebucht, bestritten, bezahlt, storniert, Gegenforderung, Skonto.
5. Lücken markieren und konkrete Nachforderung formulieren.

## Ausgabe

- Belegkettenmatrix
- Titelvermerk
- OPOS-Abgleich
- fehlende Urkunden

## Qualitätsgates

- Ein Titel ersetzt nicht automatisch die Rangprüfung.
- Ein OPOS-Eintrag ersetzt nicht automatisch den Rechtsgrund.
- Unlesbare oder fremdsprachige Belege erhalten eigenen Prüfstatus.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.
