---
name: anlagen-zu-schriftsaetzen-anlagen-aus-datenraum-und-sharepoint
description: "Überführt Datenraum-/SharePoint-/DMS-Exporte in Anlagenlogik: Pfade, Versionen, Berechtigungen, Exportzeitpunkt, Index und gerichtliche Fassung."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/anlagen-aus-datenraum-und-sharepoint/SKILL.md`. Urspruenglicher Skill-Name: `anlagen-aus-datenraum-und-sharepoint`.

# Datenraum und SharePoint als Anlagenquelle

## Zweck

Dieser Skill ist für moderne Akten, in denen der Beweis nicht aus einem Ordner, sondern aus Datenraum-Exports, SharePoint-Links und DMS-Versionen kommt.

## Mindestinput

- Exportliste oder Ordnerstruktur.
- Zeitpunkt des Exports.
- Berechtigungen/Quelle.
- Ziel-Schriftsatz.

## Arbeitsablauf

1. Sichere Exportzeitpunkt und Quelle.
2. Ordne Pfade in Dokumentfamilien.
3. Entscheide, welche Links durch echte Dateien ersetzt werden müssen.
4. Erzeuge Exportvermerk und Anlagenindex.

## Ausgabe

- Datenraum-Exportvermerk.
- Pfad-zu-Anlage-Mapping.
- Nachforderungsliste für fehlende Originaldateien.

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
