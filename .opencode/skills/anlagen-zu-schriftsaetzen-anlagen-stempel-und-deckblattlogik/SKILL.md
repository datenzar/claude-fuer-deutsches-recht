---
name: anlagen-zu-schriftsaetzen-anlagen-stempel-und-deckblattlogik
description: "Legt fest, wie Anlagenstempel, Konvolutdeckblätter, Unteranlagen und Seiten-/Dokumentbezeichnungen aussehen müssen, damit Gericht und Gegner nicht suchen müssen."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/anlagen-stempel-und-deckblattlogik/SKILL.md`. Urspruenglicher Skill-Name: `anlagen-stempel-und-deckblattlogik`.

# Stempel- und Deckblattlogik

## Zweck

Dieser Skill ist für die optische und logische Lesbarkeit des Anlagenpakets. Er sorgt dafür, dass `Anlage K12` nicht nur irgendwo im Dateinamen steht, sondern im Dokument, im Verzeichnis und im Schriftsatz gleich verstanden wird.

## Mindestinput

- Nummernkreis.
- Liste Einzelanlagen und Konvolute.
- Vorgaben zu Stempelposition, Schrift und Seitenstempel.

## Arbeitsablauf

1. Entscheide Stempel nur Seite 1 oder jede Seite.
2. Entwirf Deckblatt für jedes Konvolut.
3. Lege Unteranlagenlogik fest: `K12.1` oder `K12/1`.
4. Prüfe Konsistenz zwischen Deckblatt, Dateiname, Anlagenverzeichnis und Schriftsatz.
5. Erzeuge Korrekturanweisung für Assistenz oder Legal Tech.

## Ausgabe

- Stempel-/Deckblatt-Spezifikation.
- Konvolutdeckblatttext.
- Korrekturliste für abweichende Stempel.

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
