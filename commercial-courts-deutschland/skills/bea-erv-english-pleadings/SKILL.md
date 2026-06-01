---
name: bea-erv-english-pleadings
description: "Prüft beA/ERV-Einreichung englischer Schriftsätze: Dateiformat, Signatur, Anlagen, Fristen, Empfangsbekenntnis und Kanzlei-Workflow."
---

# beA/ERV

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

### beA/ERV-Einreichung englischer Schriftsätze — Praxis-Checkliste

| Punkt | Anforderung | Norm |
| --- | --- | --- |
| Pflicht zur elektronischen Einreichung | seit 01.01.2022 für Rechtsanwälte zwingend (beA-Pflicht) | § 130d ZPO |
| Format der Datei | PDF (idealerweise PDF/A); ZIP für Anlagensammlungen | Verordnungsrecht ERVV |
| Dateigröße | je Nachricht max. 100 MB; bei größeren Schriftsätzen splitten | RAVPV / ERVV |
| Anzahl Anlagen | technische Grenzen beachten; bei vielen Anlagen Index erstellen | Bundle-Index-Skill |
| Qualifizierte elektronische Signatur | Anwalt signiert mit qeS oder per "sicheren Übermittlungsweg" beA-zu-EGVP | § 130a Abs. 3 ZPO |
| Empfangsbestätigung | automatisches Empfangsbekenntnis; Prüfprotokoll prüfen | Beweis der Einreichung |
| Fristwahrung | Eingang bis 24:00 Uhr beim Gericht; vorsorglich Pufferzeit | BGH ständige Rechtsprechung zu Fristbestimmung beA |
| Englische Schriftsätze | technisch behandelt wie deutsche; aber Sprache muss von Spruchkörper akzeptiert sein (§ 184a GVG-Beschluss) | bei rein deutschsprachigen Gerichten zurückweisen-Risiko |
| Anlagenübersetzungen | englische Anlagen technisch zulässig; bei Bedarf beglaubigte Übersetzung gesondert einreichen | JVEG |
| Strukturdaten (XML) | für Mahnverfahren standardisiert; für normale Schriftsätze keine Pflicht | RAVPV |
| beA-Karte und PIN | regelmäßiges Software-Update, Hardware-Token-Validität prüfen | BRAK technische Hinweise |
| Rückläufer / Fehlermeldungen | "Eingangsdokument nicht lesbar" als Risiko bei großen oder verschlüsselten PDFs | vorab Test-Einreichung |

### Trade-off und Praxistipp

- **PDF/A-Konformität:** zwingend für viele Gerichte; reguläres Microsoft-Word-PDF kann zurückgewiesen werden. Lieber Adobe-Acrobat-Export "Save as PDF/A".
- **Anlagen-Bündel:** alle Anlagen in einer ZIP versus einzelne PDF-Dateien — Praxis je Gericht unterschiedlich. Vorher beim Spruchkörper rückfragen.
- **Englische OCR:** englische Anlagen sollten OCR-durchsuchbar sein, damit Richter zitieren können.
- **Notfall-Plan bei beA-Ausfall:** § 130d Satz 2 ZPO ermöglicht ersatzweise Einreichung in Papier mit Glaubhaftmachung der Nichtnutzbarkeit; nur in echten Notfällen.

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
