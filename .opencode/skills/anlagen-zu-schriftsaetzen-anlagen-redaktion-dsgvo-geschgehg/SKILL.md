---
name: anlagen-zu-schriftsaetzen-anlagen-redaktion-dsgvo-geschgehg
description: "Prüft Anlagen vor Einreichung auf personenbezogene Daten, Geschäftsgeheimnisse, Drittmandate, Schwärzungsbedarf und Redaktionsprotokoll."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/anlagen-redaktion-dsgvo-geschgehg/SKILL.md`. Urspruenglicher Skill-Name: `anlagen-redaktion-dsgvo-geschgehg`.

# Redaktion, DSGVO und Geschäftsgeheimnisse

## Zweck

Dieser Skill verhindert, dass das Anlagenpaket prozessual richtig, aber berufsrechtlich oder datenschutzrechtlich gefährlich ist. Er arbeitet mit einer Redaktionslogik: notwendig, verhältnismäßig, dokumentiert, reversibel intern, sauber exportiert extern.

## Mindestinput

- Anlagenliste oder konkrete Dateien.
- Parteien und Dritte.
- Angabe, welche Informationen streitrelevant sind.
- Schwärzungsstand, falls vorhanden.

## Arbeitsablauf

1. Identifiziere personenbezogene Daten und Drittgeheimnisse.
2. Trenne streitrelevante von entbehrlichen Informationen.
3. Schlage Schwärzungen und Begründungen vor.
4. Prüfe, ob Schwärzung den Beweiswert zerstört.
5. Erstelle Redaktionsprotokoll.

## Ausgabe

- Schwärzungsmatrix.
- Redaktionsprotokoll.
- Warnliste für Kollisionen mit Beweiszweck.

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
