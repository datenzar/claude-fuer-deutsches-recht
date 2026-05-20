---
name: mittelstand-corporate-ma-billing-narratives
description: "Mittelstandsmandat Billing Narratives: erstellt deal-taugliche Time Narratives, Phasenbudgets, Workstream-Rechnungen, Cap/Success-Fee-Hinweise und Matter-Controlling."
---

# Mittelstandsmandat Billing Narratives

## Zweck

Erstellt deal-taugliche Time Narratives, Phasenbudgets, Workstream-Rechnungen, Cap/Success-Fee-Hinweise und Matter-Controlling. Für GoBD, XRechnung und ZUGFeRD liegt der freistehende interne Workflow `mittelstand-ma-erechnung-gobd` im selben Plugin.

## Arbeitsmodus

- Tätigkeiten nach Phase, Workstream und Deliverable erfassen.
- Narratives knapp, mandantentauglich und prüfbar formulieren.
- Budgetabweichungen und Scope Creep markieren.
- WIP, Cap, Success Fee, Auslagen, Rabatte und Steuerlogik als eigene Prüfpunkte führen.
- Bei Rechnungsreife an `mittelstand-ma-erechnung-gobd` übergeben.

## Rote Schwellen

- Narrative enthält Mandatsgeheimnis unnötig detailliert.
- Budgetwarnung fehlt.
- Leistung ohne Akte/Workstream.
- Rechnungsnummer, Umsatzsteuerlogik oder E-Rechnungsformat unklar.

## Standardausgabe

- Billing Narrative Ledger.
- Budgetstatus nach Workstream.
- Rechnungsreife-Ampel.
- Übergabe an E-Rechnung/GoBD mit Belegkette.

## Vorlagen

- assets/templates/billing-narrative-ledger.md
- assets/templates/erechnung-gobd-billing.md
