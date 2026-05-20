---
name: mittelstand-corporate-ma-handelsregisterabruf
description: "Handelsregister- und Registerabruf: Führt offizielle Registerabrufe für Zielgesellschaft, Verkäufer, Erwerber, Beteiligungsketten, KG und Organstellung."
---

# Handelsregister- und Registerabruf

## Zweck

Führt offizielle Registerabrufe für Zielgesellschaft, Verkäufer, Erwerber, Beteiligungsketten, KG und Organstellung.

## Arbeitsmodus

- Registerportal, Bundesanzeiger, Unternehmensregister und Transparenzregister als Quellenstatus trennen.
- HRB/HRA, Vertretung, Satzung, Liste, UBO und Historie erfassen.
- Screenshots oder Abrufnachweise als Anlage planen.
- Abgleich mit Datenraum und SPA.

## Rote Schwellen

- Registerstand veraltet.
- Vertretungsmacht unklar.
- UBO-Kette nicht nachvollziehbar.

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

- assets/templates/handelsregisterabruf-protokoll.md
- assets/templates/handelsregister-corporate-housekeeping.md
