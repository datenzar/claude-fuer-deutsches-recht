---
name: workflow-dokumentenintake
description: "Dokumentenintake im Plugin fachanwalt-strafrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen, erkennt U-Haft-, Akteneinsichts-, Rechtsmittel- und Hauptverhandlungsrisiken und baut eine knappe Arbeitsakte mit Anschluss-Skills."
---

# Dokumentenintake

## Aufgabe
Dieser Workflow-Skill für `fachanwalt-strafrecht` Dokumentenintake im Plugin fachanwalt-strafrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Strafrecht-Intake-Bausteine
- **Dokumentarten identifizieren:** Beschluss (Haftbefehl § 114 StPO, Durchsuchungsbeschluss § 105 StPO, Eroeffnungsbeschluss § 207 StPO, Strafbefehl § 408 StPO), Anklageschrift § 200 StPO, Bussgeldbescheid, Urteil, Strafvollstreckungsentscheidung, Vernehmungsprotokoll, Gutachten, Asservatenverzeichnis.
- **Fristen extrahieren - rot markieren:** Berufung § 314 StPO 1 Woche, Revision § 341 StPO 1 Woche plus Revisionsbegründung § 345 StPO gesondert berechnen, Strafbefehl-Einspruch § 410 StPO 2 Wochen, Beschwerde § 311 StPO 1 Woche (sofortige) bzw. einfache Beschwerde § 304 StPO ohne diese Wochenfrist, Wiedereinsetzung § 44 StPO 1 Woche.
- **Verteidigung/Vollmacht** §§ 137 ff. StPO checken: Wahlverteidigung, notwendige Verteidigung, Pflichtverteidigerantrag, Datum, Mandantenunterschrift; besondere Vertretungsvollmacht fuer Hauptverhandlung im Strafbefehlsverfahren § 411 Abs. 2 StPO und Abwesenheitskonstellationen gesondert markieren.
- **Bei U-Haft Sofortpruefung:** Haftbefehl-Bestandsaufnahme; Haftprüfung § 117 StPO; mündliche Verhandlung §§ 118, 118a StPO; Aussetzungsantrag § 116 StPO; Haftbeschwerde nach § 304 StPO; Akteneinsicht auf haftrelevante Informationen nach § 147 Abs. 2 S. 2 StPO.
- **Zustellungspruefung** § 37 StPO / §§ 166 ff. ZPO: Postzustellungsurkunde, Ersatzzustellung, ggf. Heilung § 189 ZPO.
- **Beweismittelverzeichnis** § 200 II StPO bei Anklage sichten; vermisste Beweismittel reklamieren.
- **Anschluss:** `strafprozess-aktenlog-fristen-und-wiedervorlagen`, `strafprozess-akteneinsicht-nachlieferungen-und-sonderbaende`, `strafprozess-rechtsmittel-und-notfristencockpit`, danach Chronologie / Belegmatrix / Akteneinsicht beantragen § 147 StPO.
