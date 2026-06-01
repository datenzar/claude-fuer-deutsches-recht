---
name: workflow-anschluss-skills-router
description: "Anschluss-Skills Router im Plugin insolvenzplan-starug-planwerkstatt: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor."
---

# Anschluss-Skills Router

## Aufgabe
Dieser Workflow-Skill für `insolvenzplan-starug-planwerkstatt` Anschluss-Skills Router im Plugin insolvenzplan-starug-planwerkstatt: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Plan-Routing zu Spezialskills
- **Triage und Planreife:**
  - `spezial-insolvenzplan-erstpruefung-und-mandatsziel` (Ziel, Beteiligte, Verfahrenswahl).
  - `spezial-starug-tatbestand-beweis-und-belege` (drohende ZU § 18 InsO als StaRUG-Voraussetzung).
  - `spezial-restrukturierungsplan-fristen-form-und-zustaendigkeit` (Restrukturierungsgericht, § 34 StaRUG).
- **Planstruktur:**
  - `spezial-darstellender-livequellen-und-rechtsprechungscheck` (darstellender Teil §§ 219, 220 InsO).
  - `spezial-gestaltender-zahlen-schwellen-und-berechnung` (gestaltender Teil §§ 221 ff. InsO).
  - `spezial-gruppen-schriftsatz-brief-und-memo-bausteine` (Gruppenbildung § 222 InsO, Klassen § 9 StaRUG).
- **Abstimmung und Cram-Down:**
  - `spezial-klassen-verhandlung-vergleich-und-eskalation` (Vor-Abstimmung, Lobby).
  - `spezial-cram-formular-portal-und-einreichung` (Cross-Class Cram-Down §§ 26–28 StaRUG, Obstruktionsverbot § 245 InsO).
  - `spezial-down-red-team-und-qualitaetskontrolle` (Minderheitenschutz § 251 InsO, Schlechterstellungstest § 64 StaRUG).
- **Sanierungskonzept und Anlagen:**
  - `spezial-sanierungskonzept-risikoampel-und-gegenargumente` (IDW S6).
  - `spezial-vergleichsrechnung-behoerden-gericht-und-registerweg` (Vergleichsrechnung gegen Regelinsolvenz).
  - `spezial-anlagen-mehrparteien-konflikt-und-interessen` (Anlagenpaket, Berater, Gutachter).
- **Querschnitt:**
  - `spezial-abstimmung-internationaler-bezug-und-schnittstellen` (EuInsVO, EU-Restrukturierungs-Richtlinie 2019/1023).
  - `spezial-teil-compliance-dokumentation-und-akte`.
  - `spezial-intake-dokumentenmatrix-und-lueckenliste`.

## Faustregel
- Insolvenzplan oder StaRUG-Plan entscheidet sich nach Eintritt der Zahlungsunfähigkeit (§ 17 InsO) — vorher StaRUG möglich, danach nur Insolvenzplan.
