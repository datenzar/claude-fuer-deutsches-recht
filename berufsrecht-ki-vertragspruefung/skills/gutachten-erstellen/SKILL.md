---
name: gutachten-erstellen
description: "Erstelle das zusammenfassende Forpruefungs-Gutachten zum KI-Anbietervertrag. Aufbau Eingangsdaten Norm-Adapter Pruefpunkte Erforderlichkeit Verschwiegenheit Belehrung Subunternehmer Strafprozess TOM Drittstaat Ampelbewertung Lueckenliste Handlungsempfehlung. Ausdruecklich keine Rechtsberatung sondern strukturierte Argumentationshilfe fuer das Anbietergespraech."
---

# Forprüfungs-Gutachten erstellen

## Disclaimer

**Diese Forprüfung ist keine Rechtsberatung.** Sie ist eine strukturierte Argumentationshilfe für das Anbietergespräch. Die abschließende berufsrechtliche und strafrechtliche Beurteilung im konkreten Einzelfall bleibt der inhabilen Kanzlei beziehungsweise einer beauftragten Spezialkanzlei vorbehalten.

## Zweck

Das Gutachten fasst alle Einzelprüfungen zu einem strukturierten Dokument zusammen. Es ist intern für die Kanzlei bestimmt, kann aber auszugsweise als Argumentationsgrundlage gegenüber dem Anbieter verwendet werden.

## Aufbau

### 1. Eingangsdaten

Aus `berufsrecht-ki-vertragspruefung-kaltstart-interview`. Beruf, Anbieter, Produkt, Datenarten, Vertragstyp, Anlagen.

### 2. Norm-Adapter

Aus `parallelnormen-andere-berufe`. Tabelle der einschlägigen Normen. Hinweis auf § 203 StGB als Klammer.

### 3. Maßstab

Goldstandard: DAV-Stellungnahme Nr. 32/2025. BRAK-Leitfaden Dezember 2024 wird kurz erwähnt — zurückhaltend.

### 4. Einzelne Prüfpunkte

Pro Skill ein Abschnitt:

- **Erforderlichkeit** (`erforderlichkeit-dokumentieren`)
- **Verschwiegenheitsklausel** (`verschwiegenheitsklausel-pruefen`)
- **Strafrechtliche Belehrung** (`strafrechtliche-belehrung-pruefen`)
- **Subunternehmer-Regelung** (`subunternehmer-regelung-pruefen`)
- **Strafprozessuale Regelung** (`strafprozessuale-regelung-pruefen`)
- **TOM und Zertifizierungen** (`tom-und-zertifizierungen-pruefen`)
- **Cloud Act und Drittstaat** (`cloud-act-und-drittstaat-pruefen`)
- **AVV-Grenzprüfung Datenschutz** (`avv-grenzpruefung-datenschutz`) — als Schnittstelle

Jeder Abschnitt enthält:

- die einschlägige Norm
- die DAV-Lesart
- die konkrete Bewertung am vorgelegten Vertrag (Ampel grün/gelb/rot)
- Lücken und offene Punkte

### 5. Gesamtampel

| Bereich | Ampel | Bemerkung |
|---|---|---|
| Erforderlichkeit | | |
| Verschwiegenheitsklausel | | |
| Strafrechtliche Belehrung | | |
| Subunternehmer | | |
| Strafprozessuale Absicherung | | |
| TOM und Zertifizierungen | | |
| Drittstaat | | |
| AVV (Schnittstelle) | | |

### 6. Handlungsempfehlung

Drei Stufen:

- **Annehmbar** (alles grün, gelbe Punkte dokumentieren) — Vertrag nutzbar nach Annahme
- **Nachverhandelbar** (überwiegend grün/gelb, klare rote Punkte) — Rückfragebrief und Klauselvorschläge versenden
- **Nicht annehmbar** (mehrere rote Punkte, strukturelle Probleme) — Anbieterwechsel oder grundlegende Vertragsneuverhandlung

### 7. Anlagen

- Tabellarische Bewertung pro Prüfpunkt
- Lückenliste (priorisiert)
- Verweise auf Rückfragebrief und Klauselvorschläge

## Schlussklausel im Gutachten

Am Ende jedes Gutachtens steht:

> Dieses Forprüfungs-Gutachten ist keine Rechtsberatung. Es ist eine strukturierte Argumentationshilfe für das Anbietergespräch. Die abschließende berufsrechtliche und strafrechtliche Beurteilung im konkreten Einzelfall bleibt der inhabilen Kanzlei beziehungsweise einer beauftragten Spezialkanzlei vorbehalten. Quellen: Memorandum zu § 43e BRAO und § 203 StGB; DAV-Initiativstellungnahme Nr. 32/2025; BT-Drs. 18/12940; einschlägige Gesetzestexte (BRAO StBerG WPO PAO BNotO StGB StPO DS-GVO).

## Stil

- Sachlich, kurz
- Tabellen wo möglich
- Keine Marketing-Sprache
- Disclaimer am Anfang und am Ende
- Bezeichne Anbieterversprechen klar als "Aussage Anbieter, noch nicht im Vertrag" oder "im Vertrag (Fundstelle)"

## Output-Format

Markdown, ca. 5 bis 10 Seiten. PDF-Export optional via Plugin `office`.
