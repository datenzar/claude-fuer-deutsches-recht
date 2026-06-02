---
name: anlagen-zu-schriftsaetzen-berufung-beschwerde-und-neue-anlagen
description: "Prüft Anlagen in Rechtsmittelverfahren: Übernahme alter Nummern, neue Anlagen, § 531 ZPO-Risiken, Verweis auf Vorinstanz und Synchronisation."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/berufung-beschwerde-und-neue-anlagen/SKILL.md`. Urspruenglicher Skill-Name: `berufung-beschwerde-und-neue-anlagen`.

# Berufung, Beschwerde und neue Anlagen

## Zweck

Dieser Skill hilft, wenn die Akte in die zweite Instanz wandert und alte K-Nummern, neue BB-/BK-Nummern und vorinstanzliche Anlagen gleichzeitig im Spiel sind.

## Mindestinput

- Vorinstanzliches Anlagenverzeichnis.
- Rechtsmittelschriftsatz.
- Neue oder geänderte Anlagen.
- Angabe, ob neues Vorbringen betroffen ist.

## Arbeitsablauf

1. Erstelle Korrespondenztabelle alt/neu.
2. Trenne Bezugnahme auf vorhandene Akte von neuer Anlage.
3. Markiere Zulassungs-/Präklusionsrisiken.
4. Schlage Nummernkreis für Rechtsmittelinstanz vor.

## Ausgabe

- Synchronisationsmatrix.
- Rechtsmittel-Anlagenverzeichnis.
- Warnliste neues Vorbringen.

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
