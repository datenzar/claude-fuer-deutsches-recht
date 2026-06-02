---
name: anlagen-zu-schriftsaetzen-anlagen-fuer-glaubhaftmachung
description: "Spezialworkflow für Eilverfahren: Anlagen, eidesstattliche Versicherung, Screenshots, E-Mails, Fotos und Glaubhaftmachungsdichte nach § 294 ZPO ordnen."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/anlagen-fuer-glaubhaftmachung/SKILL.md`. Urspruenglicher Skill-Name: `anlagen-fuer-glaubhaftmachung`.

# Anlagen für Glaubhaftmachung

## Zweck

Dieser Skill ist für einstweilige Verfügung, Arrest, einstweilige Anordnung und sonstige Eilsachen. Er fragt: Was muss heute glaubhaft gemacht werden, mit welchem Mittel, und was ist nur schmückendes Beiwerk?

## Mindestinput

- Eilantrag oder Sachverhalt.
- Dringlichkeitsfrist.
- Vorhandene Belege.
- Eidesstattliche Versicherung vorhanden ja/nein.

## Arbeitsablauf

1. Bestimme glaubhaft zu machende Tatsachen.
2. Ordne jede Tatsache einem Beleg oder einer Versicherung zu.
3. Prüfe Aktualität und Dringlichkeit.
4. Erstelle Eilanlagenverzeichnis und Lückenliste.

## Ausgabe

- Glaubhaftmachungsmatrix.
- Eilanlagenverzeichnis.
- Textbaustein für Beweis-/Glaubhaftmachungsangebot.

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
