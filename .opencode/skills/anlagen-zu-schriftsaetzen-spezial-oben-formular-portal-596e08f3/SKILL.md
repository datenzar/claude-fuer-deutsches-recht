---
name: anlagen-zu-schriftsaetzen-spezial-oben-formular-portal-596e08f3
description: "Prüft, wie Anlagen technisch eingereicht werden: beA, ERV, Portal, Datenträger, mehrere Teilpakete, Begleitvermerk und Eingangsprüfung."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/spezial-oben-formular-portal-und-einreichung/SKILL.md`. Urspruenglicher Skill-Name: `spezial-oben-formular-portal-und-einreichung`.

# Portal, beA und Einreichungslogik

## Zweck

Dieser Skill ersetzt die alte unklare Portal-Füllung durch einen echten Einreichungsworkflow.

## Mindestinput

- Gericht/Portal.
- Dateiliste mit Größen.
- Frist.

## Arbeitsablauf

1. Prüfe aktuelle Formatanforderungen.
2. Plane Paketierung und Reihenfolge.
3. Erzeuge Begleitvermerk.
4. Erstelle Eingangskontrollliste.

## Ausgabe

- Einreichungsplan.
- Begleitvermerk.
- Eingangskontrolle.

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
