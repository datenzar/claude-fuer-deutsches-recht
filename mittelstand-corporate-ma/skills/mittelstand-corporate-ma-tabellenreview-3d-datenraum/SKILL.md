---
name: mittelstand-corporate-ma-tabellenreview-3d-datenraum
description: "3D-Tabellenreview im Datenraum: verbindet M&A-Datenraumprüfung mit interner Review-Matrix für Dokumente, Datenpunkte und Perspektiven Recht/Steuer/Wirtschaft."
---

# 3D-Tabellenreview im Datenraum

## Zweck

Dieser Skill bleibt als M&A-Datenraum-Variante erhalten und nutzt ausschließlich interne Vorlagen dieses Plugins. Für den generischen freistehenden Review-Würfel steht zusätzlich `mittelstand-ma-tabellenreview` bereit.

## Arbeitsmodus

- Spaltenprompts für Datenpunkte formulieren.
- Zeilen als Dokumente oder Vertragscluster definieren.
- Blätter für Legal, Tax, Finance, ESG, Regulatory und PMI anlegen.
- Kreuzblatt-Widersprüche, fehlende Anlagen und Belegketten ausgeben.
- Ergebnisse in Q&A, Red-Flag-Report, Disclosure Schedules und SPA Issues überführen.

## Rote Schwellen

- Keine Belegkette.
- Formel- oder CSV-Export nicht nachvollziehbar.
- Materiality-Schwellen uneinheitlich.
- Clean-Room-Daten werden mit offenem Datenraum vermischt.

## Standardausgabe

- Review-Setup mit Zeilen, Spalten, Blättern und Materiality.
- Review Grid mit Belegstelle, Risiko, Owner und Follow-up.
- Liste der Widersprüche und fehlenden Dokumente.
- Übergabe an `mittelstand-ma-tabellenreview` bei großen Tabellenläufen.

## Vorlagen

- assets/templates/tabellenreview-3d-ma-setup.md
- assets/templates/tabellenreview-workbook.md
- assets/templates/tabellenreview-column-prompts.md
- assets/templates/tabellenreview-row-prompts.md
- assets/templates/data-quality-gate.md
