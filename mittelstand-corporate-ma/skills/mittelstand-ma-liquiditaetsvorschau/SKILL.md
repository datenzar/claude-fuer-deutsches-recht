---
name: mittelstand-ma-liquiditaetsvorschau
description: "Freistehende Liquiditätsvorschau für Corporate/M&A und Distressed M&A: prüft 3-Wochen-Liquidität, 13-Wochen-Cash-Bridge, Runway, OPOS, Bankdaten und Insolvenzschwellen intern."
---

# Freistehende Liquiditätsvorschau

## Zweck

Dieser Skill liefert die Liquiditätsvorschau direkt im Corporate/M&A-Plugin. Er ist für normale Buy-side/Sell-side-DD, Distressed M&A, StaRUG, Insolvenzplan, Board Papers und Signing-to-Closing-Monitoring gedacht. Er arbeitet mit Bankdaten, OPOS, Zahlungsplänen, Kaufpreislogik, Working-Capital-Mechanik und Management Forecasts.

## Prüfungsmodi

- 3-Wochen-Vorschau für Zahlungsfähigkeit im Krisenfall.
- 13-Wochen-Cash-Bridge für Distressed M&A, Bridge Financing und CP-Monitoring.
- 26-/52-Wochen-Runway für Board Paper, Business Judgment und Going-Concern-Fragen.
- SPA-nahe Liquidität: Locked Box, Completion Accounts, Leakage, Debt-like Items, Cash-like Items, Net Debt, Working Capital.
- Simulation: Base Case, Downside Case, No-Funding Case, Closing Delay, Customer Churn, Supplier Stop.

## Rechenregeln

1. Startliquidität nur aus belegten Bankständen, Cash Pools oder Treuhandkonten übernehmen.
2. Fällige Verbindlichkeiten getrennt aus OPOS Kreditoren, Steuern, Sozialversicherung, Löhnen, Mieten, Debt Service und Litigation erfassen.
3. Passiva II gesondert sichtbar machen, wenn rechtlich oder wirtschaftlich einzubeziehen.
4. Einzahlungen nur ansetzen, wenn Betrag, Schuldner, Fälligkeit und Realisierungswahrscheinlichkeit plausibel sind.
5. Jede Woche mit Anfangsbestand, Einzahlungen, Auszahlungen, Endbestand, Deckungslücke und Ampel ausgeben.
6. Keine Scheingenauigkeit: unklare Werte als Bandbreite oder TODO markieren.

## Ausgabe

- Liquiditätsampel mit Status `grün`, `gelb`, `rot`, `nicht beurteilbar`.
- 3-Wochen-Tabelle, 13-Wochen-Cash-Bridge und Runway-Kommentar.
- Quellenlog und Annahmenbuch.
- Kritische Nachfragen an Management, CFO, Steuerberater, Banken und Insolvenzrechtsteam.
- Übergabe an `mittelstand-ma-insolvenzreife`, `mittelstand-corporate-ma-distressed-ma`, `mittelstand-ma-fristen-cp-kalender` und Board Paper.

## Rote Schwellen

- Deckungslücke innerhalb von drei Wochen.
- Fällige Steuern, Sozialversicherung oder Löhne ungeklärt.
- Bank-Covenant, MAC, Default, Zahlungsstopp oder Rücklastschrift.
- Management Forecast widerspricht Bankdaten oder OPOS.

## Vorlagen

- assets/templates/liquiditaetsvorschau-3-wochen.md
- assets/templates/cash-bridge-13-wochen.md
- assets/templates/distressed-ma-liquiditaetsampel.md
- assets/templates/data-quality-gate.md
