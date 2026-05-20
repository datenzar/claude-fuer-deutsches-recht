---
name: mittelstand-corporate-ma-steps-plan-pmo
description: "Deal-PMO und Steps Plan: Extrahiert aus Verträgen, DD und Gremienunterlagen konkrete Steps Plans für Pre-Signing, Signing-to-Closing und Post-Closing."
---

# Deal-PMO und Steps Plan

## Zweck

Extrahiert aus Verträgen, DD und Gremienunterlagen konkrete Steps Plans für Pre-Signing, Signing-to-Closing und Post-Closing.

## Arbeitsmodus

- Pflichten, Fristen, Bedingungen und Deliverables aus Dokumenten ziehen.
- Owner, Status, Beleg und Eskalation zuweisen.
- Woechentliche Deal-PMO-Ansicht erzeugen.
- Entscheidungen und Annahmen dokumentieren.

## Rote Schwellen

- Pflicht ohne Frist.
- Keine Eskalation für rote Punkte.
- Plan nicht mit Vertragsversion verknuepft.

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

- assets/templates/deal-pmo-weekly.md
- assets/templates/signing-closing-steps-plan.md
