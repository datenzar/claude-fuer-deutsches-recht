---
name: anlagen-zu-schriftsaetzen-excel-tabellen-und-zahlenbeweis
description: "Bereitet XLSX/CSV als Anlage auf: Ausdruck, Summenlogik, Formelrisiko, Quelldaten, Rechenweg, PDF-Fassung und Anlagenbezug im Schriftsatz."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/excel-tabellen-und-zahlenbeweis/SKILL.md`. Urspruenglicher Skill-Name: `excel-tabellen-und-zahlenbeweis`.

# Excel-Tabellen und Zahlenbeweis

## Zweck

Dieser Skill verhindert, dass eine Excel-Datei als Black Box eingereicht wird. Zahlen müssen nachvollziehbar sein: Quelle, Rechenweg, Version, Stichtag, Rundung, Formel und Zusammenfassung.

## Mindestinput

- XLSX/CSV oder Tabelleninhalt.
- Zahlenbehauptung im Schriftsatz.
- Angabe, ob Originaldatei oder PDF-Ausdruck eingereicht wird.

## Arbeitsablauf

1. Trenne Quelldaten, Berechnung, Ergebnis und anwaltliche Wertung.
2. Prüfe sichtbare Formeln, Filter, ausgeblendete Spalten und Rundungen.
3. Erstelle PDF-taugliche Tabellenansicht mit Stichtag.
4. Formuliere Erläuterung für Schriftsatz oder Anlagenverzeichnis.

## Ausgabe

- Tabellen-Beweisvermerk.
- PDF-Ausdrucksanweisung.
- Warnliste versteckte Formeln/Filter.

## Typische Fehler, die du aktiv suchst

- Unklare Anlagenfunktion: Die Datei existiert, aber niemand sagt, welche Tatsache sie beweist.
- Nummerierung folgt dem Ordner, nicht dem Schriftsatz.
- Der Schriftsatz versteckt entscheidenden Vortrag in der Anlage.
- Dateiname, Stempel oder Anlagenverzeichnis widersprechen einander.

## Anschluss-Skills

- `anlagen-zu-schriftsaetzen` für den Hauptworkflow.
- `anlagen-qualitygate-finalcheck` vor Versand.
- `schriftsatz-anlagen-mapping` für Belegmatrix und Lückenliste.

## Quellen- und Vorsichtsregel

Bei tragenden Aussagen zu Form, elektronischer Einreichung oder prozessualer Verwertbarkeit aktuelle amtliche Quellen prüfen: ZPO, BRAO, ERVV, ERVB und gerichtliche Hinweise. Keine BeckRS-/juris-/Literatur-Blindzitate. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle nennen.
