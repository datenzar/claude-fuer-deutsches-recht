---
name: anlagen-zu-schriftsaetzen-original-abschrift-kopie-und-2077d014
description: "Klären, wann Original, beglaubigte Abschrift, einfache Kopie, Scan, elektronisches Dokument oder Ausdruck als Anlage sinnvoll oder erforderlich ist."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/original-abschrift-kopie-und-elektronische-fassung/SKILL.md`. Urspruenglicher Skill-Name: `original-abschrift-kopie-und-elektronische-fassung`.

# Original, Abschrift, Kopie und elektronische Fassung

## Zweck

Dieser Skill verhindert Formverwechslungen: Eine Anlage ist oft nur Beleg, manchmal aber gerade Urkunde, Original, Vollmacht, Ausfertigung oder beglaubigte Abschrift.

## Mindestinput

- Dokumentart.
- Verfahrensart und Gericht.
- Ob Original vorhanden ist.
- Streit über Echtheit ja/nein.

## Arbeitsablauf

1. Ordne Dokumentqualität ein.
2. Prüfe, ob Originalvorlage, Kopie oder Scan genügt.
3. Markiere Echtheits- und Bestreitensrisiken.
4. Formuliere Vorlage-/Nachreichungsvorschlag.

## Ausgabe

- Dokumentqualitätsvermerk.
- Vorlageempfehlung.
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
