---
name: barrierefreiheit-web-checker-pdf-downloads-dokumente
description: "Prüft PDFs, Downloads, eingebettete Dokumente, Preislisten, AGB, Formulare und Bescheide auf Barrierefreiheit: Tags, Lesereihenfolge, Alternativtexte, Tabellen, Formularfelder und HTML-Alternative. Output: Dokumenten-Audit."
---

> Opencode-Port von `barrierefreiheit-web-checker/skills/pdf-downloads-dokumente/SKILL.md`. Urspruenglicher Skill-Name: `pdf-downloads-dokumente`.

# PDFs, Downloads und Dokumente

Nutze diesen Skill, wenn eine Website barrierefrei wirkt, aber wichtige Informationen in PDFs, Word-Dateien oder Formularen versteckt sind.

## Prüfpunkte

- Ist das Dokument überhaupt notwendig oder gibt es eine HTML-Alternative?
- PDF getaggt?
- Lesereihenfolge korrekt?
- Überschriften und Listen strukturiert?
- Tabellen mit Kopfzellen?
- Bilder mit Alternativtext?
- Formularfelder benannt?
- Sprache gesetzt?
- Scan-PDF mit OCR?

## Priorität

AGB, Preislisten, Produktinformationen, Formulare, Widerrufsbelehrung, Barrierefreiheitserklärung und behördliche Bescheide sind hoch zu priorisieren. Rein dekorative Broschüren können niedriger priorisiert werden, wenn die wesentlichen Informationen barrierefrei anderweitig vorliegen.

## Schneller Arbeitsmodus

- Lege den Scope fest: Website, App, PDF, Checkout, Formular, Intranet oder öffentliche Stelle; dazu Normrahmen BFSG/BITV/WAD/EN 301 549/WCAG.
- Beurteile nicht nur formal, sondern aus Nutzersicht: Tastatur, Screenreader, Zoom/Reflow, Kontrast, Fehlermeldungen, Zeitlimits und Dokumentzugang.
- Automatische Scanner sind nur Startpunkt. Markiere False Positives, manuelle Nachpruefung und reproduzierbare Testschritte.
- Formuliere Fixes als Entwickler-Tickets mit Komponente, Problem, Nutzerwirkung, Normbezug, Prioritaet und Re-Test.

## Ausgabeformat

- Befund.
- Nutzerwirkung.
- Norm-/Kriteriumsbezug.
- Konkreter Fix.
- Prioritaet und Nachweis fuer die Dokumentation.
