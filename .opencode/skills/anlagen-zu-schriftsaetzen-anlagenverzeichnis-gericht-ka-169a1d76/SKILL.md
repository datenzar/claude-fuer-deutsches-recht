---
name: anlagen-zu-schriftsaetzen-anlagenverzeichnis-gericht-ka-169a1d76
description: "Erstellt getrennte Anlagenverzeichnisse: schlank für Gericht, ausführlicher für Kanzlei und technisch mit Dateipfad, Hash, Quelle und Bearbeitungsstatus."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/anlagenverzeichnis-gericht-kanzlei-und-intern/SKILL.md`. Urspruenglicher Skill-Name: `anlagenverzeichnis-gericht-kanzlei-und-intern`.

# Anlagenverzeichnis für Gericht, Kanzlei und intern

## Zweck

Ein gutes Anlagenverzeichnis ist nicht nur Inhaltsverzeichnis. Es ist die Brücke zwischen Schriftsatz, Gerichtspaket, Kanzleiakte und späterem Kosten-/Nachreichungsstreit.

## Mindestinput

- Nummerierte Anlagen oder Vorschlagsliste.
- Schriftsatzstellen oder Beweiszwecke.
- Optional: Dateipfade, Hashes, Quellen, Status.

## Arbeitsablauf

1. Erzeuge gerichtliches Kurzverzeichnis.
2. Erzeuge internes Langverzeichnis mit Quelle, Hash, Bearbeiter, Status.
3. Markiere Konvolute und Unteranlagen.
4. Füge Spalte „Tatsache/Schriftsatzstelle“ hinzu.
5. Prüfe Lücken und Doppelnummern.

## Ausgabe

- Gerichtsverzeichnis.
- Internes Kanzleiverzeichnis.
- Lücken- und Doppelungsbericht.

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
