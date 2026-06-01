---
name: workflow-dokumentenintake
description: "Dokumentenintake im Plugin tabellenreview-3d: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte."
---

# Dokumentenintake

## Aufgabe
Dieser Workflow-Skill liest tabellenartige Werke (Excel, CSV, Word-Tabellen, PDF-Tabellen) in das Plugin `tabellenreview-3d` ein. Er bereitet sie für die dreidimensionale Prüfung vor: (1) Spaltenstimmigkeit, (2) Zeilenkohärenz, (3) Cross-Bezüge (Querverweise, Verlinkungen, Summen).

## Dokumentenarten
- **Excel / XLSX:** Tabellenblätter (Sheets), benannte Bereiche, Formeln, bedingte Formatierungen, Pivot-Tabellen, Datenmodelle.
- **CSV:** Trennzeichen identifizieren (Komma, Semikolon, Tab); Encoding (UTF-8 vs. CP1252); Spaltenheader.
- **Word-/PDF-Tabellen:** Layout-Tabellen vs. Datentabellen; verbundene Zellen, Mehrzeiler in Zellen.
- **Cap Table:** Anteilseigner, Anteilsklassen, Vesting-Status, Verwässerung -- Querverweise zu Gesellschaftsvertrag.
- **Forderungstabelle Insolvenz:** Insolvenzforderung, Sicherungsrechte, Rang, Anmeldung, Prüfung; Querverweis zu InsO und Insolvenzplan.

## Erste Triage
- Welche Datentypen je Spalte (Zahl, Text, Datum, Boolean, Verweis)?
- Welche Spaltennamen sind verbindlich definiert (Datenmodell, Vorgabe Mandant/Aufsicht)?
- Welche Cross-Bezüge existieren (Summen in Footer, Verweise auf andere Sheets, externe Verlinkungen)?
- Welche Validierungsregeln (Datenprüfung in Excel, Pflichtfelder, Wertelisten)?

## Kaltstart
Wenn Material vorliegt, arbeite zuerst mit dem Material. Stelle nur Rückfragen, die für die nächste Weiche nötig sind:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.
