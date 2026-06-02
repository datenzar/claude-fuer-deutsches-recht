---
name: anlagen-zu-schriftsaetzen-spezial-pruefmodus-fristennot-cc382ce5
description: "Validiert ein vorhandenes Anlagenpaket und gibt eine kurze Fristennotiz plus nächste Handlung aus."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/spezial-pruefmodus-fristennotiz-und-naechster-schritt/SKILL.md`. Urspruenglicher Skill-Name: `spezial-pruefmodus-fristennotiz-und-naechster-schritt`.

# Prüfmodus, Fristennotiz und nächster Schritt

## Zweck

Dieser Skill ist für fertige, aber verdächtige Pakete: einmal streng prüfen, dann sagen, was sofort zu tun ist.

## Mindestinput

- Fertiges Anlagenpaket.
- Schriftsatz.
- Frist.

## Arbeitsablauf

1. Vergleiche Zitate und Dateien.
2. Prüfe Nummern, Lesbarkeit, Schwärzung.
3. Formuliere Fristennotiz.

## Ausgabe

- Prüfbericht.
- Stop-Liste.
- Nächster Schritt.

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
