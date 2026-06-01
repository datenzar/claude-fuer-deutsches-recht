---
name: workflow-anschluss-skills-router
description: "Anschluss-Skills Router im Plugin insolvenzrecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor."
---

# Anschluss-Skills Router

## Aufgabe
Dieser Workflow-Skill für `insolvenzrecht` Anschluss-Skills Router im Plugin insolvenzrecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Routing-Logik zu Plugin-Spezialskills
- **Mandant ist Schuldner / Geschäftsführer mit Antragsfrage:**
  - `spezial-insolvenzreife-antragspflicht-und-haftung` (§ 15a InsO, § 15b InsO).
  - `spezial-zahlungsunfaehigkeit-tatbestand-beweis-und-belege` (§ 17 InsO, 10-Prozent-/3-Wochen-Schwelle).
  - `spezial-ueberschuldung-fristen-form-und-zustaendigkeit` (§ 19 InsO, Fortbestehensprognose 12 Monate).
- **Verfahrensweg:**
  - `spezial-verfahrenstypen-livequellen-und-rechtsprechungscheck` (Regelinsolvenz vs. Eigenverwaltung § 270 InsO vs. Schutzschirm § 270d InsO).
  - `spezial-glaeubigerantrag-risikoampel-und-gegenargumente` (Gläubigerantrag § 14 InsO).
  - `spezial-verbraucherinsolvenz-mehrparteienkonflikt` (§§ 304 ff. InsO).
- **Operative Phase:**
  - `spezial-belegmatrix-formular-portal-und-einreichung` (Antragsunterlagen).
  - `spezial-tabelle-beweislast-und-darlegungslast` (Forderungstabelle).
  - `spezial-glaeubigerausschuss-fristennotiz-und-naechster-schritt` (§ 67 InsO).
- **Querschnitt:**
  - `spezial-inso-schriftsatz-brief-und-memo-bausteine` (Textbausteine).
  - `spezial-rechtsquellen-zahlen-schwellen-und-berechnung` (10-Prozent-/3-Wochen-Berechnung).
  - `spezial-triage-mandantenkommunikation-entscheidungsvorlage` (Mandantenbrief).
- **Grenzüberschreitend / besondere Lagen:**
  - `spezial-chronologie-internationaler-bezug-und-schnittstellen` (EuInsVO 2015/848).
  - `spezial-feststellung-sonderfall-und-edge-case`.

## Faustregel
- Immer zuerst Antragspflicht klären (§ 15a InsO), dann Verfahrenswahl, dann operative Skills.
