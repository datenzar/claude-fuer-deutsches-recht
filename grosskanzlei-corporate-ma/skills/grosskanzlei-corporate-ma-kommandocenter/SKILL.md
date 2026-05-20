---
name: grosskanzlei-corporate-ma-kommandocenter
description: "Deal-Kommandocenter: Schnellstart für Corporate/M&A-Mandate. Erkennt aus einem Satz, Datenraum, Term Sheet oder Markup den passenden Deal-Workflow und erzeugt eine Deal-Karte mit Ampel, Rollen, nächster Aktion und Freigabegrad."
---

# Deal-Kommandocenter

## Zweck

Schnellstart für Corporate/M&A-Mandate. Erkennt aus einem Satz, Datenraum, Term Sheet oder Markup den passenden Deal-Workflow und erzeugt eine Deal-Karte mit Ampel, Rollen, nächster Aktion und Freigabegrad.

## Arbeitsmodus

- Dealtyp und Parteiperspektive erkennen: Buy-side, Sell-side, Management, W&I-Versicherer oder Restrukturierung.
- Maximal drei Rückfragen stellen, danach mit Annahmen arbeiten.
- Deal-Phase bestimmen: Origination, Vorbereitung, Datenraum, Due Diligence, Vertrag, Signing/Closing, Integration oder Streit/Restrukturierung.
- An den passenden Spezialskill routen und die rote Schwelle sichtbar machen.

## Rote Schwellen

- Frist, Signing oder Closing unklar.
- Mandatsgeheimnis, Clean-Room oder Insiderinformation betroffen.
- KI-Ergebnis soll ungeprüft als Rechtsrat, DD-Finding oder Board-Grundlage verwendet werden.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/workflow-deal-kommandocenter.md
- assets/templates/cowork-ma-dashboard.md
- assets/templates/workflow-freigabeampel.md
