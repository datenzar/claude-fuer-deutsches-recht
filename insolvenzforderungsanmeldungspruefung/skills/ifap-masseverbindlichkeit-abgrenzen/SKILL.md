---
name: ifap-masseverbindlichkeit-abgrenzen
description: "Grenzt Insolvenzforderungen von Masseverbindlichkeiten, Neumasse, Altmasse und falsch angemeldeten Forderungen ab."
---

# Masseverbindlichkeit abgrenzen

## Aufgabe

Erkennt Forderungen, die nicht oder nur teilweise zur Insolvenztabelle gehören.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Leistung nach Eröffnung
- Verwalterbestellung oder Zustimmungsvorbehalt relevant
- Gläubiger meldet Masseforderung zur Tabelle an

## Workflow

1. Leistungszeitraum und Entstehungsgrund vor, nach oder während vorläufiger Verwaltung einordnen.
2. Prüfen, ob die Forderung überhaupt Insolvenzforderung ist oder als Masseverbindlichkeit außerhalb der Tabelle zu behandeln ist.
3. Bei gemischten Zeiträumen Teilbeträge bilden.
4. Verwalterhandlung, Betriebsfortführung, Dauerschuldverhältnis und Steuer-/SV-Bezug markieren.
5. Ausgabe zwischen Tabellenbestreiten, Weiterleitung an Massebearbeitung und Rückfrage unterscheiden.

## Ausgabe

- Abgrenzungsvermerk
- Teilbetragsaufteilung
- Rückfrage an Massebearbeitung
- Tabellenentscheidung

## Qualitätsgates

- Masseverbindlichkeit wird nicht zur Quote festgestellt.
- Gemischte Zeiträume werden nicht pauschal behandelt.
- Unsicherheit wird als Eskalationspunkt markiert.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.
