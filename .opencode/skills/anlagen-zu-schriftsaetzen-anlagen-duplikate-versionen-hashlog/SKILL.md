---
name: anlagen-zu-schriftsaetzen-anlagen-duplikate-versionen-hashlog
description: "Erkennt doppelte Dateien, verschiedene Fassungen desselben Dokuments, OCR-Kopien, E-Mail-Anhänge und manipulativ wirkende Metadatenbrüche; erzeugt ein Hash- und Versionenprotokoll."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/anlagen-duplikate-versionen-hashlog/SKILL.md`. Urspruenglicher Skill-Name: `anlagen-duplikate-versionen-hashlog`.

# Duplikate, Fassungen und Hashlog

## Zweck

Dieser Skill macht die stille technische Kontrolle hinter dem Anlagenverzeichnis. Er entscheidet nicht materiell-rechtlich, aber er zeigt, ob die Anlagenbasis stabil genug ist, um gerichtsfest verwendet zu werden.

## Mindestinput

- Dateiliste mit Größe, Datum, Quelle und optional Hash.
- Hinweis, welche Fassungen bereits im Schriftsatz zitiert sind.
- Optional: E-Mail-Header oder DMS-Export.

## Arbeitsablauf

1. Gruppiere identische, ähnliche und wahrscheinlich zusammengehörige Dateien.
2. Trenne Original, Arbeitskopie, OCR, Scan, Vorschau, Screenshot und E-Mail-Anhang.
3. Markiere widersprüchliche Datums-/Versionssignale.
4. Bestimme die gerichtliche Fassung pro Dokumentfamilie.
5. Erzeuge Hashlog und Änderungsnotiz.

## Ausgabe

- Hash-/Duplikatlog als CSV/Markdown-Tabelle.
- Fassungsentscheidung pro Dokumentfamilie.
- Warnliste für Metadaten-/Authentizitätsrisiken.
- Vorschlag, welche Dateien nicht eingereicht werden.

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
