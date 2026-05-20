---
name: grosskanzlei-corporate-ma-matter-file
description: "Deal-Akte: Legt die Transaktionsakte als Matter Workspace an: Struktur, Workstreams, Datenraumspiegel, Register, Q&A, SPA, Signing, Closing und PMI."
---

# Deal-Akte

## Zweck

Legt die Transaktionsakte als Matter Workspace an: Struktur, Workstreams, Datenraumspiegel, Register, Q&A, SPA, Signing, Closing und PMI.

## Arbeitsmodus

- Ordnerstruktur für 00_Admin bis 90_Archive erzeugen.
- Deal-Codes, Gegenparteien, Gerichte/Register, Notar, Steuerberater, W&I und Banken verknuepfen.
- Aktenzeichen der Kanzlei mit HRB/HRA, LEI, ISIN, Deal-Codenamen und Parteien verknuepfen.
- Ablage- und Benennungsregeln ausgeben.

## Rote Schwellen

- Unklare Vertraulichkeitsstufe.
- Keine Rollen/Owner.
- Kein Archiv- und Closing-Bible-Plan.

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

- assets/templates/matter-opening-checklist.md
- assets/templates/closing-bible-index.md
