---
name: anlagen-zu-schriftsaetzen-frist-und-eilversand-anlagenpaket
description: "Minimalpfad bei drohender Frist: welche Anlagen müssen jetzt mit, welche können nachgereicht, welche Risiken müssen im Schriftsatz offen gehalten werden."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/frist-und-eilversand-anlagenpaket/SKILL.md`. Urspruenglicher Skill-Name: `frist-und-eilversand-anlagenpaket`.

# Frist und Eilversand Anlagenpaket

## Zweck

Dieser Skill ist der nüchterne Notfallmodus. Er soll nicht alles perfekt machen, sondern die richtige Priorität setzen: fristwahrend, lesbar, nachvollziehbar, nachreichbar.

## Mindestinput

- Fristende.
- Schriftsatztyp.
- Vorhandene Kernanlagen.
- Was noch fehlt oder technisch kaputt ist.

## Arbeitsablauf

1. Bestimme Muss-Anlagen für Fristwahrung und Glaubhaftmachung.
2. Trenne Kür, Nachreichung und interne Kontrolle.
3. Formuliere Begleit-/Nachreichungshinweis.
4. Erstelle 30-Minuten- und 2-Stunden-Plan.

## Ausgabe

- Eilversandliste.
- Nachreichungsplan.
- Risikoampel.

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
