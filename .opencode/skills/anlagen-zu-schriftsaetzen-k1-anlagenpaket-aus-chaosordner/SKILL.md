---
name: anlagen-zu-schriftsaetzen-k1-anlagenpaket-aus-chaosordner
description: "Aus einem Mandantenordner mit beliebigen Dateinamen die erste Anlagenstaffel K1 bis K20 bilden: priorisieren, umbenennen, Lücken markieren, Rückfragen ausgeben."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/k1-anlagenpaket-aus-chaosordner/SKILL.md`. Urspruenglicher Skill-Name: `k1-anlagenpaket-aus-chaosordner`.

# K1 aus Chaosordner bauen

## Zweck

Dieser Skill ist für den Moment gedacht, in dem ein Mandant einen ZIP-Ordner mit „final_final_neu.pdf“, Screenshots, Tabellen und E-Mail-Anhängen sendet und in 90 Minuten eine brauchbare Anlagenstaffel entstehen muss.

## Mindestinput

- Ordnerliste oder Dateiexport.
- Schriftsatzentwurf oder wenigstens Anspruchs-/Verteidigungslinie.
- Nummernkreis und gewünschte Tiefe der Staffel.

## Arbeitsablauf

1. Dateien grob clustern: Vertrag, Leistung, Abnahme, Rechnung, Mahnung, Mangel, Korrespondenz, Zahlung.
2. Doppelte und bloße technische Kopien aussondern.
3. Für jede potentielle K-Anlage Beweiszweck und Schriftsatzstelle bestimmen.
4. K1 bis K20 als erste arbeitsfähige Staffel vorschlagen.
5. Nicht zuordenbare Dateien in Nachforderungs-/Klärliste schieben.

## Ausgabe

- K1-K20-Vorschlagsliste.
- Dateinamensvorschläge.
- Nicht verwendete Dateien mit Grund.
- Eine einzige priorisierte Rückfrage, wenn nötig.

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
