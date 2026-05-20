---
name: mittelstand-ma-aktenanlage
description: "Freistehende M&A-Aktenanlage: eröffnet Deal-Akte, Aktenzeichen, Parteienregister, Ordnerstruktur, Datenraumspiegel, Vertraulichkeitsstufen und Closing-Bible-Grundgerüst mit vollständig interner Arbeitslogik."
---

# Freistehende M&A-Aktenanlage

## Zweck

Dieser Skill eröffnet eine Corporate/M&A-Transaktionsakte vollständig innerhalb dieses Plugins. Er ersetzt keine DMS- oder Kanzleisoftware, liefert aber sofort eine belastbare Deal-Akte mit Aktenzeichen, Beteiligten, Workstreams, Ordnerplan, Dokumentenlog, Datenraumspiegel, Q&A-Register, Signing-/Closing-Struktur und Archivlogik.

## Startsignale

- Neue Anfrage aus E-Mail, Teams, Screenshot, Teaser, NDA, Term Sheet, Handelsregisterauszug oder Datenraum-Einladung.
- Unklarer Deal-Code, mehrere Zielgesellschaften, mehrere Verkäufer, Fondsvehikel oder KG-Struktur.
- Der Nutzer fragt: „Lege eine Akte an“, „sortiere den Datenraum“, „mach daraus einen Matter Workspace“ oder „baue die Closing Bible vor“.

## Arbeitsmodus

1. Maximal drei Rückfragen: Mandant/Rolle, Zielgesellschaft/Deal-Code, Deadline/Vertraulichkeit.
2. Falls Angaben fehlen, mit vorsichtigen Platzhaltern arbeiten und TODOs markieren.
3. Aktenzeichen der Kanzlei mit Deal-Code, HRB/HRA, LEI, ISIN, Steuer-ID, Notar, Gegenseite, W&I-Broker und Banken verknüpfen.
4. Ordnerstruktur von `00_Admin` bis `90_Archive` anlegen und für jeden Ordner Zweck, Owner, Vertraulichkeit und Namensschema ausgeben.
5. Datenraumspiegel und Closing-Bible-Index sofort vorbereiten, auch wenn noch keine Dokumente vorliegen.
6. Für jedes Dokument eine Belegkette führen: Quelle, Upload-Datum, Version, Datenraum-ID, Prüfer, Review-Status.

## Ausgabe

- Matter Opening Card mit Deal-Code, Aktenzeichen, Parteien, Rollen, Vertraulichkeit und nächster Aktion.
- Ordnerplan mit Workstreams: Corporate, Commercial, Finance, Tax, Employment, IP/IT, Real Estate, Regulatory, Litigation, Restructuring, PMI.
- Beteiligten- und Registermatrix.
- Ablageregeln für eingehende und ausgehende Dokumente.
- Übergabe an interne Skills: `mittelstand-ma-tabellenreview`, `mittelstand-ma-liquiditaetsvorschau`, `mittelstand-ma-fristen-cp-kalender`, `mittelstand-corporate-ma-handelsregisterabruf`, `mittelstand-corporate-ma-closing-bible-archiv`.

## Rote Schwellen

- Kein Mandant oder keine Parteiperspektive geklärt.
- Clean-Room-Informationen liegen offen im normalen Datenraum.
- Insiderinformation, Sanktionstreffer, Geldwäscheverdacht oder Insolvenzreife wird sichtbar.
- Signing/Closing-Frist fehlt oder ist widersprüchlich.

## Vorlagen

- assets/templates/aktenanlage-matter-file.md
- assets/templates/deal-folder-structure.md
- assets/templates/matter-opening-checklist.md
- assets/templates/closing-bible-index.md
