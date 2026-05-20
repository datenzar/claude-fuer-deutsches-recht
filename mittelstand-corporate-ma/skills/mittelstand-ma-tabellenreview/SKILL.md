---
name: mittelstand-ma-tabellenreview
description: "Freistehender Tabellenreview für Corporate/M&A: prüft Dokumente, Datenpunkte, Tabellen, Formeln und Perspektiven als interne Review-Matrix mit vollständig interner Review-Logik."
---

# Freistehender Tabellenreview

## Zweck

Dieser Skill bildet den Tabellenreview vollständig im Corporate/M&A-Plugin ab. Alle Prüfraster, Spaltenprompts und Qualitätsregeln liegen hier. Er arbeitet mit CSV, Excel, Markdown-Tabellen oder Datenraumlisten und baut daraus einen Review-Würfel: Dokumente als Zeilen, Prüfungsfragen als Spalten, Perspektiven als Blätter.

## Review-Würfel

- Zeilen: Dokumente, Vertragscluster, Gesellschaften, Assets, Kunden, Lieferanten, Lizenzen, Immobilien, Forderungen, Mitarbeitende oder CPs.
- Spalten: Datenpunkte, Klauseln, Zahlenfelder, Risiken, Materiality, Belegstellen, Owner, Follow-up, SPA-Relevanz.
- Blätter: Legal, Tax, Finance, Commercial, ESG/Compliance, Employment, IP/IT, Regulatory, Restructuring, PMI.
- Querprüfungen: Summen, Laufzeiten, Kündigungsfristen, Change-of-Control, Garantien, Cap Table, Debt, Working Capital, Cash Bridge.

## Arbeitsmodus

1. Eingabedateien erkennen und als Dateninventar ausgeben.
2. Spaltenprompts aus Dealtyp, DD-Scope und Materiality ableiten.
3. Zeilenprompts pro Dokumententyp erzeugen.
4. Jede Zelle mit Status `leer`, `belegt`, `widersprüchlich`, `prüfen`, `nicht anwendbar` versehen.
5. Kreuzblatt-Widersprüche markieren, etwa Umsatz in Finance vs. Kundenverträge in Commercial.
6. Ergebnisse in DD-Findings, Q&A, Disclosure Schedules, SPA Issues und PMI-Aufgaben überführen.

## Rechenlogik

- Zahlenfelder nie frei erfinden; unklare Werte als `nicht belegt` markieren.
- Summen nur aus sichtbaren Quellen berechnen und Rechenweg angeben.
- Prozentwerte mit Nenner und Stichtag ausweisen.
- Bei CSV/Excel-Import Datentypen prüfen: Datum, Betrag, Währung, Ja/Nein, Text, Referenz.
- Jede aggregierte Aussage braucht mindestens eine Belegstelle oder einen offenen TODO.

## Ausgabe

- Review Setup mit Zeilen-, Spalten- und Blattdefinition.
- Review Grid als Markdown-Tabelle oder CSV-kompatible Struktur.
- Fehlerliste: Dubletten, Lücken, widersprüchliche Zahlen, fehlende Anlagen, unplausible Formeln.
- Übergabe an interne Skills: DD Reporting, Q&A, Disclosure Schedules, Liquiditätsvorschau, CP-Kalender.

## Vorlagen

- assets/templates/tabellenreview-workbook.md
- assets/templates/tabellenreview-column-prompts.md
- assets/templates/tabellenreview-row-prompts.md
- assets/templates/tabellenreview-3d-ma-setup.md
- assets/templates/data-quality-gate.md
