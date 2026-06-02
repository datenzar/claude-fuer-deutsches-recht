---
name: anlagen-zu-schriftsaetzen-anlagen-uebergabe-an-assisten-c65d25b8
description: "Erzeugt klare Arbeitsanweisungen für Kanzleiteam, Assistenz, Legal Tech oder externen Dienstleister: was umbenennen, scannen, stempeln, schwärzen, prüfen."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/anlagen-uebergabe-an-assistenz-und-legal-tech/SKILL.md`. Urspruenglicher Skill-Name: `anlagen-uebergabe-an-assistenz-und-legal-tech`.

# Übergabe an Assistenz und Legal Tech

## Zweck

Dieser Skill verwandelt anwaltliche Logik in ausführbare Arbeitsschritte. Er ist für den Moment, in dem die Anwältin die Entscheidung trifft und das Team das Paket bauen muss.

## Mindestinput

- Entscheidungsliste oder Anlagenmatrix.
- Teamrollen und Frist.
- Technische Vorgaben.

## Arbeitsablauf

1. Übersetze rechtliche Entscheidungen in einzelne Aufgaben.
2. Lege Reihenfolge und Verantwortliche fest.
3. Definiere Kontrollpunkte und Rückfragen.
4. Formuliere Übergabemail oder Ticketliste.

## Ausgabe

- Arbeitsanweisung.
- Ticket-/Aufgabenliste.
- Freigabecheck.

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
