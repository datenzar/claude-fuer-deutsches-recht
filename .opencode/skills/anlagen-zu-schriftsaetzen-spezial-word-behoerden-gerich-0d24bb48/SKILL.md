---
name: anlagen-zu-schriftsaetzen-spezial-word-behoerden-gerich-0d24bb48
description: "Bereitet Word-, PDF- und Scan-Anlagen für Gerichts- oder Behördenwege vor: Konvertierung, Lesezeichen, PDF/A, Dateiname, Deckblatt."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/spezial-word-behoerden-gericht-und-registerweg/SKILL.md`. Urspruenglicher Skill-Name: `spezial-word-behoerden-gericht-und-registerweg`.

# Word/PDF-Umwandlung für Gericht und Behörden

## Zweck

Dieser Skill räumt die Schnittstelle zwischen Office-Dateien und verfahrensfester PDF-Fassung auf.

## Mindestinput

- DOCX/PDF/Scan.
- Zielweg.
- Nummernkreis.

## Arbeitsablauf

1. Entscheide Zielformat.
2. Prüfe Umwandlungsrisiken.
3. Erzeuge Dateiname und Deckblatt.

## Ausgabe

- Konvertierungsanweisung.
- Kontrollvermerk.
- Dateinamensliste.

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
