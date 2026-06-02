---
name: anlagen-zu-schriftsaetzen-spezial-schriftsaetzen-dokume-1366115c
description: "Baut aus Schriftsatz und Dateiliste eine Matrix mit Tatsachen, Belegen, fehlenden Anlagen und Nachforderungen."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/spezial-schriftsaetzen-dokumentenmatrix-und-lueckenliste/SKILL.md`. Urspruenglicher Skill-Name: `spezial-schriftsaetzen-dokumentenmatrix-und-lueckenliste`.

# Dokumentenmatrix und Lückenliste

## Zweck

Dieser Skill ersetzt pauschales „bitte alle Unterlagen schicken“ durch präzise Nachforderungen.

## Mindestinput

- Schriftsatz.
- Dateiliste.
- Streitpunkte.

## Arbeitsablauf

1. Extrahiere Beweisanker.
2. Ordne Dateien zu.
3. Markiere fehlende oder überschüssige Anlagen.

## Ausgabe

- Dokumentenmatrix.
- Nachforderungsliste.
- Korrekturplan.

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
