---
name: anlagen-zu-schriftsaetzen-fremdsprachige-anlagen-uebersetzung
description: "Prüft fremdsprachige Anlagen: Relevanz, Übersetzungsbedarf, beglaubigte oder Arbeitsübersetzung, Auszug statt Vollübersetzung, Kosten und Schriftsatzanker."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/fremdsprachige-anlagen-uebersetzung/SKILL.md`. Urspruenglicher Skill-Name: `fremdsprachige-anlagen-uebersetzung`.

# Fremdsprachige Anlagen und Übersetzung

## Zweck

Dieser Skill sorgt dafür, dass fremdsprachige Dokumente nicht blind als Anlage landen. Er trennt zentrale Urkunde, bloße Begleitunterlage und Massendokument.

## Mindestinput

- Sprache und Dokumentart.
- Beweiszweck.
- Gericht/Verfahrensart.
- Vorhandene Übersetzung oder nur Original.

## Arbeitsablauf

1. Bestimme, ob die fremdsprachige Passage entscheidungserheblich ist.
2. Entscheide Vollübersetzung, Auszugsübersetzung oder Erläuterung.
3. Markiere Kosten- und Fristrisiko.
4. Erzeuge Anlagenverzeichniszeile mit Sprachhinweis.

## Ausgabe

- Übersetzungsentscheidung.
- Nachforderung an Mandant/Übersetzer.
- Schriftsatzbaustein.

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
