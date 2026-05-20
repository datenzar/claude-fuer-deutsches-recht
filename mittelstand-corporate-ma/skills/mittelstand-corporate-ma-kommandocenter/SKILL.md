---
name: mittelstand-corporate-ma-kommandocenter
description: "Deal-Kommandocenter: Schnellstart für Corporate/M&A-Mandate. Erkennt aus einem Satz, Datenraum, Term Sheet oder Markup den passenden Deal-Workflow und erzeugt Deal-Karte, Ampel, Rollen und nächste Aktion."
---

# Deal-Kommandocenter

## Zweck

Schnellstart für Corporate/M&A-Mandate. Der Skill erkennt aus einem Satz, Datenraum, Term Sheet, Markup, Screenshot oder Registerauszug die Deal-Phase und führt in den passenden internen Workflow. Das Plugin ist freistehend: Aktenanlage, Tabellenreview, Liquiditätsvorschau, CP-Kalender, Billing und Restrukturierung liegen im selben Plugin.

## Arbeitsmodus

- Dealtyp und Parteiperspektive erkennen: Buy-side, Sell-side, Management, W&I-Versicherer, Public M&A oder Restrukturierung.
- Maximal drei Rückfragen stellen, danach mit vorsichtigen Annahmen und TODOs arbeiten.
- Deal-Phase bestimmen: Origination, Vorbereitung, Datenraum, Due Diligence, Vertrag, Signing/Closing, Integration oder Streit/Restrukturierung.
- Den passenden internen Spezialskill routen und rote Schwellen sichtbar machen.
- Anfängerfreundlich bleiben: fehlende Begriffe erklären, aber den Arbeitsfluss nicht aufhalten.

## Interne Routing-Karte

| Signal | Interner Skill |
| --- | --- |
| Neue Anfrage, Aktenzeichen, Datenraum-Einladung | `mittelstand-ma-aktenanlage` |
| Datenraumliste, CSV, Excel, Review Grid | `mittelstand-ma-tabellenreview` |
| Cash, OPOS, Bank, Runway, Distressed | `mittelstand-ma-liquiditaetsvorschau` |
| Zahlungsunfähigkeit, Überschuldung, StaRUG | `mittelstand-ma-insolvenzreife` |
| Signing, Closing, CP, Long Stop Date | `mittelstand-ma-fristen-cp-kalender` |
| Rechnung, Narrative, XRechnung, ZUGFeRD | `mittelstand-ma-erechnung-gobd` |
| Textentwurf, Report, SPA, Board Paper | `mittelstand-ma-schreibcanvas` |
| Register, HRB/HRA, Gesellschafterliste | `mittelstand-corporate-ma-handelsregisterabruf` |
| Rechtsprechung und amtliche Quellen | `mittelstand-corporate-ma-rechtsprechungsrecherche` |

## Rote Schwellen

- Frist, Signing oder Closing unklar.
- Mandatsgeheimnis, Clean Room oder Insiderinformation betroffen.
- KI-Ergebnis soll ungeprüft als Rechtsrat, DD-Finding oder Board-Grundlage verwendet werden.
- Liquiditätslücke, Insolvenzantragspflicht, Sanktionstreffer oder GwG-Risiko sichtbar.

## Standardausgabe

- Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Senior-Review-Hinweis bei hohen Risiken.

## Vorlagen

- assets/templates/workflow-deal-kommandocenter.md
- assets/templates/cowork-ma-dashboard.md
- assets/templates/workflow-freigabeampel.md
