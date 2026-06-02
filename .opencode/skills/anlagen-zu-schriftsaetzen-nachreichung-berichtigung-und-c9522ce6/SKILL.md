---
name: anlagen-zu-schriftsaetzen-nachreichung-berichtigung-und-c9522ce6
description: "Plant die Reparatur eines Anlagenpakets nach gerichtlichem Hinweis, Rüge der Gegenseite, falscher Anlage, fehlender Datei oder versehentlicher Einreichung."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/nachreichung-berichtigung-und-gerichtshinweis/SKILL.md`. Urspruenglicher Skill-Name: `nachreichung-berichtigung-und-gerichtshinweis`.

# Nachreichung, Berichtigung und gerichtlicher Hinweis

## Zweck

Dieser Skill ist die Feuerwehr, wenn das Paket schon draußen ist. Er hält Nummern stabil, korrigiert transparent und vermeidet, dass aus einer kleinen Anlagenpanne ein prozessuales Glaubwürdigkeitsproblem wird.

## Mindestinput

- Hinweis/Rüge/Problem.
- Bisheriger Schriftsatz und Anlagenverzeichnis.
- Welche Datei falsch, fehlend oder unleserlich ist.
- Frist für Berichtigung/Nachreichung.

## Arbeitsablauf

1. Klassifiziere Problem: fehlt, falsch, doppelt, unleserlich, geheim, falsche Fassung.
2. Entscheide, ob Nummer beibehalten, ersetzt oder als Nachtrag ergänzt wird.
3. Formuliere Berichtigungs-/Nachreichungsvermerk.
4. Erstelle neue Kontrollliste und Versandplan.

## Ausgabe

- Reparaturplan.
- Berichtigungsschriftsatz-Baustein.
- Nachreichungsverzeichnis.

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
