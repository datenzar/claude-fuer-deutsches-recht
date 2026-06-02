---
name: anlagen-zu-schriftsaetzen-anlagenmatrix-csv-xlsx-aufbau
description: "Entwirft eine robuste Anlagenmatrix für große Verfahren mit Dok-ID, Nummernkreisen, Schriftsatzstelle, Beweiszweck, Quelle, Hash, Status, Datenschutz und Nachreichung."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/anlagenmatrix-csv-xlsx-aufbau/SKILL.md`. Urspruenglicher Skill-Name: `anlagenmatrix-csv-xlsx-aufbau`.

# Anlagenmatrix CSV/XLSX Aufbau

## Zweck

Dieser Skill ist für Akten, die nicht mehr mit einem einfachen Word-Anlagenverzeichnis beherrscht werden. Er baut die Tabelle, mit der Kanzlei, Mandant und Gerichtsfassung auseinandergehalten werden.

## Mindestinput

- Dateiliste oder vorhandene Matrix.
- Verfahrensstränge und Nummernkreise.
- Gewünschte Spalten/Tiefe.

## Arbeitsablauf

1. Lege stabile Kanzlei-Dok-ID fest.
2. Definiere Spalten für alle Nummernkreise.
3. Ergänze Beweiszweck, Schriftsatzstelle, Quelle, Hash, Status, Schwärzung, Versandpaket.
4. Erzeuge Pflege- und Änderungsregeln.

## Ausgabe

- Matrixschema.
- Beispielzeilen.
- Pflegeanweisung.

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
