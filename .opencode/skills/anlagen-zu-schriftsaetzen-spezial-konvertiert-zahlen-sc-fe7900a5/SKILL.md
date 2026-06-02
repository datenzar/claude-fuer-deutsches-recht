---
name: anlagen-zu-schriftsaetzen-spezial-konvertiert-zahlen-sc-fe7900a5
description: "Prüft PDF-Konvertierung, Dateigrößen, Seitenzahlen, OCR und technische Schwellen vor Versand."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/spezial-konvertiert-zahlen-schwellen-und-berechnung/SKILL.md`. Urspruenglicher Skill-Name: `spezial-konvertiert-zahlen-schwellen-und-berechnung`.

# Konvertierung, Zahlen und technische Schwellen

## Zweck

Dieser Skill ist der technische Vorfilter zwischen Kanzleiordner und gerichtlichem Anlagenpaket.

## Mindestinput

- Dateiliste.
- Zielsystem.
- Frist.

## Arbeitsablauf

1. Prüfe Formate und Größen.
2. Markiere riskante Dateien.
3. Plane Konvertierung/OCR/Splitting.

## Ausgabe

- Konvertierungsplan.
- Dateigrößenampel.
- Versandpakete.

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
