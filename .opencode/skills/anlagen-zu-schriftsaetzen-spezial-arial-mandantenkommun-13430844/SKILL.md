---
name: anlagen-zu-schriftsaetzen-spezial-arial-mandantenkommun-13430844
description: "Entscheidet Stempelbild, Deckblatt, Anlagenverzeichnis und Mandantenfreigabe so, dass die Anlage optisch und logisch eindeutig ist."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/spezial-arial-mandantenkommunikation-entscheidungsvorlage/SKILL.md`. Urspruenglicher Skill-Name: `spezial-arial-mandantenkommunikation-entscheidungsvorlage`.

# Stempelbild und Entscheidungsvorlage

## Zweck

Der Skill fokussiert die scheinbar kleinen Dinge: Arial-12-Stempel, Position, Deckblatt und die Frage, was der Mandant vor Einreichung freigeben muss.

## Mindestinput

- Musteranlage.
- Nummernkreis.
- Freigabebedarf.

## Arbeitsablauf

1. Definiere Stempel und Deckblatt.
2. Prüfe Lesbarkeit nach Stempel.
3. Formuliere Mandantenfreigabe mit Risiken.

## Ausgabe

- Stempelspezifikation.
- Freigabevermerk.
- Korrekturliste.

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
