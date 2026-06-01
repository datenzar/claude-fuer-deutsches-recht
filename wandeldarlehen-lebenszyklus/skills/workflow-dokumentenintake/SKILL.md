---
name: workflow-dokumentenintake
description: "Dokumentenintake im Plugin wandeldarlehen-lebenszyklus: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte."
---

# Dokumentenintake

## Aufgabe
Dieser Workflow-Skill liest Wandeldarlehensverträge (Convertible Loan / SAFE-Logik), Term Sheets, Investment Agreements, Cap Tables, Beschlussvorlagen und Wandlungsmitteilungen in den Lebenszyklus-Workflow ein.

## Dokumentenarten
- **Term Sheet:** Investmentsumme, Bewertungs-Cap, Discount, Zinssatz, Wandlungstrigger, Maturity, Most-Favored-Nation-Klausel.
- **Wandeldarlehensvertrag (Convertible Loan Agreement):** Hauptpflichten Darlehensgeber, Wandlungsrecht/-pflicht, Vorzeitige Fälligkeit, Sicherheiten, Subordination.
- **SAFE (Simple Agreement for Future Equity):** US-Standard ohne klassische Darlehensstruktur; in Deutschland teilweise umstrittene Wandlung; oft auf Wandeldarlehen umgestellt.
- **Cap Table:** Anteilseigner, Anteilsklassen, Vesting, Verwässerung.
- **Beschlüsse der Gesellschafterversammlung:** Kapitalerhöhung (§ 55 GmbHG, § 182 AktG), Übernahme- und Wandelerklärungen.
- **Steuerliche Stellungnahme:** Bewertung des Wandeldarlehens (Behandlung als Fremd- vs. Eigenkapital), KapSt-Folgen.

## Erste Triage
- **Lebenszyklus-Phase:** Verhandlung, Closing, Laufzeit, Wandlung, Rückzahlung, Default?
- **Wandlungstrigger:** qualifizierte Finanzierungsrunde (Mindesthöhe + Lead-Investor), Exit, Endfälligkeit (Maturity), Insolvenzeintritt.
- **Wandlungspreis-Mechanik:** Cap (max. Pre-Money), Discount (z. B. 20 %), niedrigerer Wert gilt.
- **Steuerliche Konsequenz:** verdeckte Einlage, Kapitalertragsteuer auf Zinsen, Behandlung bei Wandlung (oft tauschsteuerfrei nach BMF, aber individuell prüfen).

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
