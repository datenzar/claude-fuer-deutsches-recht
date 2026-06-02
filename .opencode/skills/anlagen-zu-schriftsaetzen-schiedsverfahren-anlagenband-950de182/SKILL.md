---
name: anlagen-zu-schriftsaetzen-schiedsverfahren-anlagenband-950de182
description: "Plant Anlagenbände im Schiedsverfahren: mehrere Originale, USB-Sticks, PDF-Bundles, Index, Hashliste, Verfahrensanordnung und parallele elektronische Struktur."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/schiedsverfahren-anlagenband-und-datentraeger/SKILL.md`. Urspruenglicher Skill-Name: `schiedsverfahren-anlagenband-und-datentraeger`.

# Schiedsverfahren: Anlagenband und Datenträger

## Zweck

Schiedsverfahren sind oft logistischer als staatliche Verfahren. Dieser Skill baut eine Struktur, die für Tribunal, Parteien und Sekretariat gleichermaßen funktioniert.

## Mindestinput

- Verfahrensanordnung.
- Anzahl Parteien/Schiedsrichter.
- Anlagenliste und Dateigrößen.
- Vorgaben zu Datenträgern oder Uploadportal.

## Arbeitsablauf

1. Extrahiere formale Anforderungen aus der Verfahrensanordnung.
2. Plane Papier- und elektronische Fassung synchron.
3. Erzeuge Index, Hashliste und Datenträgerbeschriftung.
4. Markiere Übersetzungs-, Vertraulichkeits- und Seitenumfangsrisiken.

## Ausgabe

- Schieds-Anlagenplan.
- USB-/Upload-Index.
- Druck- und Bindelogistik.

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
