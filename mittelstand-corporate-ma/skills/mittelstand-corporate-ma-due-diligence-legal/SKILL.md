---
name: mittelstand-corporate-ma-due-diligence-legal
description: "Legal Due Diligence: Führt standardisierte Legal Due Diligence mit Findings, Materiality, Quellenbelegen, Human-in-the-loop und Red-Flag-Report."
---

# Legal Due Diligence

## Zweck

Führt standardisierte Legal Due Diligence mit Findings, Materiality, Quellenbelegen, Human-in-the-loop und Red-Flag-Report.

## Arbeitsmodus

- Scope und Materiality festlegen.
- Dokumente nach Workstream prüfen.
- Findings immer mit Quelle, Risiko, wirtschaftlicher Relevanz, SPA-Auswirkung und nächster Frage ausgeben.
- Stichproben und Senior Review markieren.

## Rote Schwellen

- Finding ohne Belegstelle.
- Rechtsquelle oder Registerstatus nicht verifiziert.
- KI-Ergebnis ohne Plausibilisierung als finaler DD-Bericht.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `mittelstand-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/dd-scope-materiality.md
- assets/templates/dd-finding-card.md
- assets/templates/red-flag-report.md
