---
name: costs-court-fees-risk-budget
description: "Erstellt Kosten- und Risikobudget: Gerichtskosten, Anwaltskosten, Übersetzung, Transcript, Sachverständige, Security, Settlement und Enforcement."
---

# Costs and Budget

## Aufgabe

Dieser Skill unterstützt Verfahren vor deutschen Commercial Courts oder Commercial Chambers mit internationalem Wirtschaftsbezug. Er liefert eine prozessuale Arbeitsstruktur und, wenn gewünscht, englischen Output. Deutsches Prozessrecht bleibt der Rahmen; englische Sprache bedeutet nicht Common-Law-Verfahren.

## Kaltstart

Stelle höchstens fünf Fragen, sofern die Akte sie nicht beantwortet:

1. Soll der Output auf Deutsch, Englisch oder zweisprachig sein?
2. Welches Gericht/Forum ist vorgesehen oder vereinbart?
3. Welche Klausel, welcher Streitwert und welche Parteien liegen vor?
4. Welche Frist oder Verfahrenshandlung steht als nächstes an?
5. Welche Unterlagen sind schon da: contract, correspondence, notices, expert report, exhibits, prior pleadings?

## Arbeitsworkflow

### Kosten-Modell deutsches Verfahren (auch Commercial Court)

| Kostenart | Norm | Berechnungsgrundlage |
| --- | --- | --- |
| Gerichtskosten | GKG (Gerichtskostengesetz), insbesondere Anlage 1 KV | Streitwert-degressiv; 3,0-Gebühr bei LG-Klage erste Instanz, ermäßigt auf 1,0 bei frühem Vergleich |
| Anwaltskosten Inland | RVG, insbesondere VV 3100 (Verfahrens-1,3), 3104 (Termins-1,2), 3200 (Berufung) | Streitwertabhängige Gebühren oder Vergütungsvereinbarung § 3a RVG |
| Vergütungsvereinbarung | § 3a RVG | Stundensätze grosskanzlei-typisch 350-700 EUR; Mandatsbedarf bei internationalen Streitigkeiten |
| Übersetzungen | JVEG | 1,55 EUR pro angefangene 55 Zeichen Standardtext; bei Anlagen oft erhebliche Posten |
| Wortprotokoll § 613 ZPO Justizstandort-Stärkungsgesetz | JVEG | Stenografie/Tonprotokoll kostenpflichtig, vorher Antrag |
| Sachverständige | § 8 ff. JVEG | nach Honorargruppen; bei IT/Finanz oft hoch (Honorargruppe M3) |
| Sicherheitsleistung Ausländer | § 110 ZPO Prozesskostensicherheit | Kläger ohne Wohnsitz/Sitz in EU/EWR |
| Streitwert Zwischenfeststellung | § 256 ZPO | für Sicherungsverfahren oft niedriger als Hauptsacheverfahren |
| Vollstreckungskosten | GvKostG, § 788 ZPO | trägt Schuldner |

### Schwellen-Beispiele Streitwert/Gerichtsgebühren (orientativ; live aktuelle KV-Werte prüfen)

| Streitwert | Verfahrensgebühr 3,0 (KV 1210) | Berufungsgebühr 4,0 (KV 1220) |
| --- | --- | --- |
| 100.000 EUR | ca. 3.273 EUR | ca. 4.364 EUR |
| 500.000 EUR | ca. 10.041 EUR | ca. 13.388 EUR |
| 5.000.000 EUR | ca. 49.143 EUR (Höchstsatz erreichbar) | dito |

(Stand vor letzter GKG-Novelle, vor Verwendung im Mandat aktuelle Gebührentabelle bestätigen.)

### Trade-off Kostenmodell

- **Streitwertdeckelung GKG:** ab ca. 30 Mio. EUR Streitwert Höchstgebühr; bei Mega-Mandaten Gericht "billig" gegenüber Schiedsgericht.
- **Erstattungsfähigkeit:** Vergütungsvereinbarung übersteigt RVG nicht erstattbar gegenüber Gegner (§ 3a Abs. 1 RVG, § 91 ZPO Grenzen). Bei W&I-Verfahren regelmäßiger Streitpunkt.
- **Cost Cap mit Mandant:** §§ 49b BRAO, § 4 RVG: keine Erfolgshonorare grundsätzlich (Ausnahmen § 4a RVG nur bei wirtschaftlicher Notwendigkeit).

1. **Forum sichern:** Commercial Court, Commercial Chamber, ordentliches Gericht, Schiedsgericht oder Ausland trennen.
2. **Sprache sichern:** wirksame Englischwahl, notwendige Übersetzungen und deutsch bleibende Verfahrensschritte prüfen.
3. **Prozesshandlung bauen:** Antrag, Schriftsatz, Evidence Map, Timetable, Hearing Script oder Mandantenmemo erstellen.
4. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären.
5. **Nächsten Schritt festlegen:** Frist, Verantwortliche, Unterlagen, gerichtliche Kommunikation und Mandantenfreigabe.

## Output-Standard

- **Executive Snapshot:** forum, language, next deadline, procedural risk.
- **Procedural Action:** konkreter nächster Antrag/Schriftsatz/Briefing in der gewünschten Sprache.
- **Evidence and Exhibits:** welche Anlagen tragen welchen Punkt, welche Übersetzung fehlt.
- **Risk Flags:** Zuständigkeit, Sprache, Frist, Geheimnis, Kosten, Rechtsmittel.
- **Follow-up Skills:** passende Skills aus diesem Plugin vorschlagen.

## Red Flags

- Commercial-Court-Zuständigkeit oder englische Sprache wird nur behauptet, aber nicht aus Klausel, Gesetz und Landesrecht hergeleitet.
- Englischer Schriftsatz klingt wie US-Litigation und enthält keine ZPO-tauglichen Beweisangebote.
- Anlagen sind englisch/deutsch gemischt, aber Übersetzungs- und Zitierlogik fehlt.
- Geheimhaltungsinteressen werden erst in der mündlichen Verhandlung entdeckt.
- Das Wortprotokoll wird gewünscht, aber nicht rechtzeitig prozessual vorbereitet.

## Quellenregel

Vor echter Verwendung aktuelle Primärquellen prüfen: GVG, ZPO, einschlägige Landesverordnungen und die Gerichtsseite des zuständigen Landes. Keine erfundenen Gerichtslisten, keine erfundenen Formularpflichten, keine Paywall-Fundstellen. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
