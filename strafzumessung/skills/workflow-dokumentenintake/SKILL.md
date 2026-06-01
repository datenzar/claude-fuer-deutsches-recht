---
name: workflow-dokumentenintake
description: "Dokumentenintake im Plugin strafzumessung: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte."
---

# Dokumentenintake

## Aufgabe
Dieser Workflow-Skill für `strafzumessung` Dokumentenintake im Plugin strafzumessung: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Strafzumessung-Intake-Bausteine
- **Pflichtdokumente fuer Strafmasspruefung:**
  - **Anklageschrift / Strafbefehl** mit gesetzlichen Merkmalen, Strafrahmen.
  - **BZRG-Auszug** des Beschuldigten (Vorstrafen, Tilgungsfristen § 46 BZRG, Verwertungsverbot § 51 BZRG).
  - **Verteidigerakte / Beschuldigtenvernehmungen** (Aussageverhalten, ggf. Gestaendnis).
  - **Sachverstaendigengutachten** (Schuldfaehigkeit § 20 StGB, verminderte Schuldfaehigkeit § 21 StGB; bei Drogen / Sucht; bei psychischen Erkrankungen).
  - **Tatortprotokoll, Zeugenaussagen** (Beweislage / Tatschwere).
  - **Schadenshoehe-Belege** (Strafzumessungsfaktor § 46 II StGB).
- **Belege fuer Strafmilderung:**
  - **Tagessatz-Hoehe § 40 II StGB:** Lohnabrechnungen 3 Monate, Steuerbescheid, BAFOEG/Hartz-IV-Bescheid, Unterhaltsverpflichtungen.
  - **Schadenswiedergutmachung** (Quittungen, Vereinbarungen).
  - **TOA § 46a StGB** (Vermittlerprotokoll, Aussohnungsvereinbarung).
  - **Therapie-Bescheinigung** (Behandlungsbeginn, Verlauf, Prognose).
  - **Abstinenz-Nachweis** bei Drogen / Alkohol (Haaranalyse, ETG-Urintest mit chain-of-custody).
  - **Soziales Umfeld** (Arbeitgeber-Bescheinigung Anstellung, Mietvertrag, Familienstand).
- **Belege fuer Strafschaerfung kritisch lesen:** Vorstrafen (Datum, Aktualitaet, Einschlaegigkeit); Tatfolgen (Schaden, Personenschaden); Bewaehrungsbruch § 56f StGB.
- **Sondermaterialien JGG:** Jugendgerichtshilfe-Bericht; Pers. Verhaeltnisse; Erziehungsbedarf.
- **Anschluss:** Strafmilderung-Skill / Strafrahmen-Skill / Bewaehrungs-Skill / Verstaendigung-Skill.
