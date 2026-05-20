---
name: mittelstand-corporate-ma-disclosure-schedules
description: "Disclosure Schedules: Leitet Disclosure Schedules aus Datenraum, DD-Findings, Q&A und SPA-Garantien ab."
---

# Disclosure Schedules

## Zweck

Leitet Disclosure Schedules aus Datenraum, DD-Findings, Q&A und SPA-Garantien ab.

## Arbeitsmodus

- Garantien in Offenlegungskategorien übersetzen.
- Datenraumbelege und Q&A-Antworten verknuepfen.
- Fair-Disclosure-Risiko markieren.
- Versionierung und Freigabe je Schedule führen.

## Rote Schwellen

- Offenlegung nicht auffindbar.
- Zu allgemeine Disclosure ohne Deal-Bezug.
- Schedule widerspricht SPA-Garantie.

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

- assets/templates/disclosure-schedules-matrix.md
- assets/templates/fair-disclosure-check.md
