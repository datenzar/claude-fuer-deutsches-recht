---
name: anlagen-zu-schriftsaetzen-zeitleiste-und-belegkette
description: "Baut aus Anlagen eine Chronologie und zeigt zu jedem Ereignis, welcher Beleg trägt, welcher nur plausibilisiert und welcher fehlt."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/zeitleiste-und-belegkette/SKILL.md`. Urspruenglicher Skill-Name: `zeitleiste-und-belegkette`.

# Zeitleiste und Belegkette

## Zweck

Dieser Skill macht aus einem Anlagenhaufen eine Erzählung. Gerade bei Bau-, Handels-, Arbeits- oder Gesellschaftsverfahren müssen Ereignis, Datum, Dokument und Beweiszweck sauber zusammenkommen.

## Mindestinput

- Dokumentenliste oder Aktenauszug.
- Streitige Kernfragen.
- Datumsbereich.

## Arbeitsablauf

1. Extrahiere Ereignisse und Daten.
2. Ordne je Ereignis Belege und Gegenbelege zu.
3. Markiere unsichere Daten und Dokumentwidersprüche.
4. Leite daraus Anlagenreihenfolge oder Nachforderung ab.

## Ausgabe

- Chronologie.
- Belegkette pro Streitpunkt.
- Widerspruchs- und Lückenliste.

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
