---
name: anlagen-zu-schriftsaetzen-spezial-baut-beweislast-und-d-e6bafbbb
description: "Prüft, ob die Anlage eine konkrete Darlegung trägt oder nur einen pauschalen Anlagenverweis kaschiert; trennt Tatsachenvortrag, Beweisangebot und bloße Hintergrundunterlage."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/spezial-baut-beweislast-und-darlegungslast/SKILL.md`. Urspruenglicher Skill-Name: `spezial-baut-beweislast-und-darlegungslast`.

# Beweislast, Darlegungslast und Anlagen

## Zweck

Dieser Skill macht die prozessuale Strenge sichtbar: Der Schriftsatz muss die erhebliche Tatsache enthalten. Die Anlage darf den Vortrag belegen, aber nicht ersetzen.

## Mindestinput

- Schriftsatzstelle.
- Anlagenzitat.
- Streitige Tatsache.

## Arbeitsablauf

1. Formuliere die behauptete Tatsache.
2. Prüfe, ob sie im Schriftsatz selbst steht.
3. Ordne die Anlage als Beleg, Erläuterung oder ungeeigneten Anlagenfriedhof ein.
4. Schlage eine bessere Schriftsatzformulierung vor.

## Ausgabe

- Substantiierungscheck.
- Korrekturbaustein.
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
