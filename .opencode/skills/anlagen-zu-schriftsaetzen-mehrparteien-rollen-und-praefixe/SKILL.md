---
name: anlagen-zu-schriftsaetzen-mehrparteien-rollen-und-praefixe
description: "Entwirft Nummernkreise bei Streitgenossen, Nebenintervention, Widerklage, Drittwiderklage, selbständigem Beweisverfahren und parallelen Verfahren."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/mehrparteien-rollen-und-praefixe/SKILL.md`. Urspruenglicher Skill-Name: `mehrparteien-rollen-und-praefixe`.

# Mehrparteien, Rollen und Präfixe

## Zweck

Dieser Skill verhindert Prefix-Chaos: K, B, WK, DWK, NI, SV, AST, AG, BK, BB, S-W. Er sorgt dafür, dass die Nummerierung der Prozessrolle folgt.

## Mindestinput

- Parteien-/Rollenübersicht.
- Verfahrensarten.
- Vorhandene Nummernkreise.

## Arbeitsablauf

1. Bestimme pro Rolle den klarsten Präfix.
2. Prüfe, ob alte Nummern beibehalten oder gespiegelt werden sollen.
3. Erzeuge Prefix-Legende für Schriftsatz und Anlagenverzeichnis.
4. Markiere Kollisionsrisiken.

## Ausgabe

- Präfixkonzept.
- Legendentext.
- Synchronisationsmatrix.

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
