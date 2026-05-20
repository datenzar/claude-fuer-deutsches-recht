---
name: mittelstand-ma-erechnung-gobd
description: "Freistehender Billing-, GoBD- und E-Rechnungsworkflow für M&A-Mandate: erzeugt Narratives, Workstream-Abrechnung, XRechnung-XML, ZUGFeRD-Prüfpaket und revisionssicheren Buchungsnachweis."
---

# Freistehender Billing-, GoBD- und E-Rechnungsworkflow

## Zweck

Dieser Skill macht aus Deal-Arbeit abrechenbare, prüfbare und mandantentaugliche Abrechnung. Er verbindet Mittelstandsmandat-Narratives, Phasenbudget, WIP, Caps, Success Fees, Auslagen, Umsatzsteuer, DATEV-nahe Buchungslogik, XRechnung und ZUGFeRD-Prüfpaket. Alle Billing-, E-Rechnungs- und GoBD-Bausteine liegen in diesem Workflow.

## Arbeitsmodus

1. Tätigkeiten aus Zeiteinträgen, Dokumenten, Calls, Markups und Deliverables erfassen.
2. Narrative kurz, konkret und ohne unnötige Mandatsgeheimnisse formulieren.
3. Jede Leistung Phase, Workstream, Fee Earner, Datum, Dauer, Rate, Rabatt, Budget und Deliverable zuordnen.
4. Rechnungsposten mit Umsatzsteuerlogik, Reverse-Charge-Hinweis, Auslagen und Vorschüssen prüfen.
5. XRechnung-XML als strukturierte Datensatz-Skizze ausgeben; ZUGFeRD als Hybrid-Prüfpaket mit PDF/A-3-Hinweis vorbereiten.
6. GoBD-Protokoll führen: Änderungslog, Rechnungsnummer, Storno, Korrekturrechnung, Belegkette, Exportstatus.

## Ausgabe

- Billing Narrative Ledger.
- Workstream-Rechnungsentwurf mit Budgetabweichungen.
- XRechnung-Datenblock und ZUGFeRD-Checkliste.
- DATEV/FiBu-Exportvorschlag als CSV-kompatible Tabelle.
- GoBD-Prüfprotokoll mit Unveränderbarkeitshinweis und Korrekturpfad.

## Rote Schwellen

- Rechnungsnummer fehlt oder wurde doppelt vergeben.
- Rechnung soll rückdatiert oder ohne Leistungsbezug erzeugt werden.
- Umsatzsteuer, Reverse Charge oder Leistungsort unklar.
- Narrative offenbart unnötig vertrauliche Deal-Informationen.
- E-Rechnung wird als technisch versandfertig behauptet, obwohl XML/PDF/A-3 nicht validiert wurde.

## Vorlagen

- assets/templates/erechnung-gobd-billing.md
- assets/templates/billing-narrative-ledger.md
- assets/templates/ai-use-disclosure-log.md
