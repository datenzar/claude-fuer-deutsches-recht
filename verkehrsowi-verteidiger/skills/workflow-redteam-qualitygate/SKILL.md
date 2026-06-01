---
name: workflow-redteam-qualitygate
description: "Red-Team Qualitygate im Plugin verkehrsowi-verteidiger: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton."
---

# Red-Team Qualitygate

## Aufgabe
Dieser Workflow-Skill für `verkehrsowi-verteidiger` Red-Team Qualitygate im Plugin verkehrsowi-verteidiger: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## OWi-Red-Team-Checks
- **Frist-Re-Check:** Einspruch § 67 OWiG 2 Wochen ab Zustellung; Rechtsbeschwerde §§ 79, 80 OWiG 1 Woche / 1 Monat; Verjaehrung § 26 III StVG 3 Monate (bis Bescheid) / 6 Monate (bis 1. Instanz Urteil); Unterbrechung § 33 OWiG.
- **BKatV-Re-Check:** Aktuelle Anlage zur StVO und § 26a StVG; Regelbusse, Punkte, Fahrverbote stets gegen Tatzeit pruefen; bei Aenderungen lex mitior § 4 III OWiG.
- **Messverfahren-Check:**
  - **Eichschein** im Tatzeitraum gueltig?
  - **Bedienerschein** Messbeamter?
  - **Standardisiertes Messverfahren** (BGH-Linie zur Beweiskraft)?
  - **Toleranzwerte** zugunsten Betroffener abgezogen?
  - **Lichtbild Identifizierung** Fahrer?
- **Beweisanforderungs-Check Akteneinsicht § 49 OWiG i.V.m. § 147 StPO:** Vollstaendigkeit Akte; Messprotokoll; Lebensakte Geraet; Rohdaten (BVerfG-Linie zur fair-trial-Garantie); Schulungs-/Sachkundenachweis Bediener.
- **Toleranzwerte:**
  - Geschwindigkeit < 100 km/h: 3 km/h, ab 100 km/h: 3 %.
  - Abstand: 10 % der Standard-Messung.
  - Atemalkohol: 0,1 mg/l Toleranz.
- **Konsequenzen-Re-Check:** Punkte FAER 1-3? Fahrverbot 1-3 Monate? 8-Punkte-Grenze (§ 4 V StVG = Fahrerlaubnisentzug)? Wiederholungstaeter § 4 II StVG?
- **Berufliche Relevanz** angesprochen? Berufskraftfahrer, Aerzte, Anwaelte, Beamte - existenzielles Risiko Fahrverbot.
- **Halluzinations-Check:** Keine erfundenen OLG-Az; "OLG-Linie" / "staendige Rspr." statt erfundener Fundstellen.
