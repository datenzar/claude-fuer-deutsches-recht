---
name: anlagen-zu-schriftsaetzen-ocr-scan-lesbarkeit-und-beweiswert
description: "Prüft gescannte Anlagen auf Lesbarkeit, OCR-Durchsuchbarkeit, Seitenreihenfolge, abgeschnittene Ränder, schiefe Scans und Beweiswertprobleme."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/ocr-scan-lesbarkeit-und-beweiswert/SKILL.md`. Urspruenglicher Skill-Name: `ocr-scan-lesbarkeit-und-beweiswert`.

# OCR, Scanqualität und Lesbarkeit

## Zweck

Dieser Skill schaut wie eine strenge Geschäftsstelle auf das Paket: Kann man es lesen? Kann man es durchsuchen? Fehlt Seite 2? Ist die Unterschrift abgeschnitten? Sind Fotos zu dunkel?

## Mindestinput

- PDF-/Scanliste.
- Hinweis, ob Originale vorhanden sind.
- Frist und gewünschter Aufwand.

## Arbeitsablauf

1. Prüfe Sichtbarkeit, Vollständigkeit, Seitenreihenfolge und OCR.
2. Markiere Dokumente, die neu gescannt oder im Original vorgelegt werden sollten.
3. Entscheide, ob Vergrößerung/Ausschnitt zusätzlich sinnvoll ist.
4. Erzeuge klare Scan-Anweisung für Mandant oder Assistenz.

## Ausgabe

- Lesbarkeitsampel.
- Neuscan-Liste.
- OCR-/PDF/A-Prüfnotiz.
- Anweisung für bessere Reproduktion.

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
