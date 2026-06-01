---
name: workflow-redteam-qualitygate
description: "Red-Team Qualitygate im Plugin insolvenzrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton."
---

# Red-Team Qualitygate

## Aufgabe
Dieser Workflow-Skill für `insolvenzrecht` Red-Team Qualitygate im Plugin insolvenzrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Insolvenzrecht-Red-Team-Checks
- **Fristen:** § 15a InsO (3 Wochen bei ZU, 6 Wochen bei Überschuldung) korrekt berechnet ab Eintritt der materiellen Insolvenz (nicht ab Erkenntnis)?
- **Eröffnungsgrund-Schwellen:**
  - § 17 InsO Zahlungsunfähigkeit: 10-Prozent-Schwelle und 3-Wochen-Liquiditätslücke (BGH-Linie) explizit geprüft?
  - § 19 InsO Überschuldung: zweistufige Prüfung (rechnerische Überschuldung + negative Fortbestehensprognose) sauber getrennt?
  - § 18 InsO drohende Zahlungsunfähigkeit: Prognosezeitraum 24 Monate (seit SanInsFoG 2021) genannt?
- **Verwechslungsgefahr:**
  - Überschuldung ≠ bilanzielle Unterdeckung — Fortbestehensprognose entscheidet.
  - Zahlungsstockung ≠ Zahlungsunfähigkeit — Drei-Wochen-Grenze.
- **Anfechtung:** Bei § 133 InsO 4-Jahres-Zeitraum (seit Reform 2017 für kongruente Deckungen), bei §§ 130, 131 InsO 3 Monate, bei § 134 InsO 4 Jahre.
- **Strafbarkeit erkannt?** § 15a Abs. 4 InsO, §§ 283 ff. StGB, § 266a StGB Sozialversicherungsbeiträge.
- **EU-Bezug:** COMI-Prüfung (Art. 3 EuInsVO) erfolgt bei grenzüberschreitendem Sachverhalt?

## Halluzinations-Stopps
- Keine erfundenen Az. Falls unsicher: "BGH zu § X InsO, Az. zu verifizieren".
- Keine erfundenen IDW-Standard-Nummern (S6, S11, EPS 11 sind real; höhere Zahlen prüfen).
- Keine Verwechslung von § 64 GmbHG a.F. (vor 2021) und § 15b InsO (seit SanInsFoG).
