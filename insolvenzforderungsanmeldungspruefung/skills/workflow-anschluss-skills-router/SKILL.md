---
name: workflow-anschluss-skills-router
description: "Anschluss-Skills Router im Plugin insolvenzforderungsanmeldungspruefung: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor."
---

# Anschluss-Skills Router

## Aufgabe
Dieser Workflow-Skill für `insolvenzforderungsanmeldungspruefung` Anschluss-Skills Router im Plugin insolvenzforderungsanmeldungspruefung: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Routing Forderungsanmeldung
- **Triage und Erstprüfung:**
  - `spezial-insolvenzforderungsanmeldungspruefung-erstpruefung` (Rolle, Ziel, Fristen).
  - `spezial-intake-tatbestand-beweis-und-belege` (Forderungsgrund prüfen).
- **Forderungsgrund und Rang:**
  - `spezial-forderungsgrund-rang-und-belegpruefung` (§ 38, § 39 InsO).
  - `spezial-grund-risikoampel-und-gegenargumente` (typische Bestreitensgründe).
  - `spezial-rang-schriftsatz-brief-und-memo-bausteine` (Nachrang § 39 InsO, Gesellschafterdarlehen § 39 Abs. 1 Nr. 5 InsO).
  - `spezial-masseverbindlichkeit-sonderfall-und-edge-case` (§ 55 InsO Masseverbindlichkeiten — nicht Insolvenzforderung).
- **Anmeldung und Form:**
  - `spezial-tabellenauszug-formular-portal-und-einreichung` (Anmeldeformat).
  - `spezial-inso-fristen-form-und-zustaendigkeit` (Anmeldefrist, Sondertermin § 177 InsO).
  - `spezial-betrag-behoerden-gericht-und-registerweg` (Betrags-Substantiierung).
  - `spezial-belege-dokumentenmatrix-und-lueckenliste`.
- **Bestreiten und Feststellung:**
  - `spezial-bestreiten-mehrparteien-konflikt-und-interessen` (§ 178 InsO Bestreiten).
  - `spezial-feststellung-internationaler-bezug-und-schnittstellen` (§ 180 InsO Feststellungsklage).
  - `spezial-pruefungstermin-compliance-dokumentation-und-akte` (§ 176 InsO).
  - `spezial-kanalcheck-beweislast-und-darlegungslast` (Beweislast).
- **Verteilung und Nachgang:**
  - `spezial-verteilung-red-team-und-qualitaetskontrolle` (Verteilungsverzeichnis).
  - `spezial-tabellenimport-zahlen-schwellen-und-berechnung` (Quotenberechnung).
  - `spezial-nachforderungen-livequellen-und-rechtsprechungscheck` (Restschuldbefreiung § 302 InsO).
- **Mandantenkommunikation:**
  - `spezial-ifap-mandantenkommunikation-entscheidungsvorlage`.
  - `spezial-vbuh-verhandlung-vergleich-und-eskalation`.

## Faustregel
- Vor der Anmeldung: Rang klären — Aussonderung § 47, Absonderung §§ 49–51, einfache Forderung § 38, Nachrang § 39, Masseverbindlichkeit § 55.
