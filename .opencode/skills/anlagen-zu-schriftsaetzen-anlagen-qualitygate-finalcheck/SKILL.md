---
name: anlagen-zu-schriftsaetzen-anlagen-qualitygate-finalcheck
description: "Finaler Red-Team-Check vor Einreichung: Nummern, Schriftsatzverweise, Dateien, Stempel, OCR, Schwärzung, Dateinamen, beA-Paket, Lücken und Begleitvermerk."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/anlagen-qualitygate-finalcheck/SKILL.md`. Urspruenglicher Skill-Name: `anlagen-qualitygate-finalcheck`.

# Anlagen-Qualitygate vor Versand

## Zweck

Dieser Skill ist die letzte Tür vor Versand. Er soll schnell, streng und praktisch sein: Was kann heute noch peinlich, haftungsträchtig oder prozessual schädlich werden?

## Mindestinput

- Finaler Schriftsatz.
- Finales Anlagenverzeichnis.
- Dateiliste/Ordner.
- Frist und Versandweg.

## Arbeitsablauf

1. Vergleiche alle Anlagenzitate mit Dateien.
2. Prüfe Nummernlücken, Doppelte und Überhänge.
3. Prüfe Lesbarkeit/OCR, Stempel, Dateinamen, Schwärzung und Paketgröße.
4. Erstelle Ampel: Stop, vor Versand beheben, nach Versand kontrollieren.
5. Formuliere Freigabevermerk.

## Ausgabe

- Stop-Liste.
- Korrekturen vor Versand.
- Freigabevermerk.
- Versandbegleitnotiz.

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
