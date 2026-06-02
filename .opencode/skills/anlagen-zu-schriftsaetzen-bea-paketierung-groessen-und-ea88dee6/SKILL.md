---
name: anlagen-zu-schriftsaetzen-bea-paketierung-groessen-und-ea88dee6
description: "Plant elektronische Anlagenpakete für beA/ERV: Dateinamen, Reihenfolge, Paketgrößen, PDF/OCR, Nachsendungen, Begleitvermerk und finaler Versandcheck."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/bea-paketierung-groessen-und-versandplan/SKILL.md`. Urspruenglicher Skill-Name: `bea-paketierung-groessen-und-versandplan`.

# beA-Paketierung und Versandplan

## Zweck

Dieser Skill übersetzt die schöne Anlagenlogik in einen realen elektronischen Versand. Er denkt an Dateigrößen, technische Grenzen, klare Paketnamen, Begleitvermerk und Wiederauffindbarkeit in der Gerichtsakte.

## Mindestinput

- Nummernkreis und endgültiges Anlagenverzeichnis.
- Dateiliste mit Dateigrößen und Format.
- Frist und Empfängergericht.
- Angabe, ob ein Paket oder mehrere Teilpakete versandt werden sollen.

## Arbeitsablauf

1. Prüfe zulässige Formate und aktuelle ERVV/ERVB-Anforderungen.
2. Sortiere Dateien in logische Teilpakete, ohne den Vortrag zu zerreißen.
3. Benenne jedes Paket und jede Datei stabil.
4. Erstelle Versandcheck mit Prüfsummen, Seitenzahlen, OCR und Stempelstatus.
5. Formuliere Begleitvermerk für mehrere Teilpakete oder Nachreichung.

## Ausgabe

- beA-Versandplan.
- Teilpaket-Tabelle mit Inhalt und Größe.
- Begleitvermerk.
- Finale Vor-Versand-Checkliste.

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
