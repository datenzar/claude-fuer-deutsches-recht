---
name: workflow-dokumentenintake
description: "Dokumentenintake im Plugin subsumtions-pruefer: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte."
---

# Dokumentenintake

## Aufgabe
Dieser Workflow-Skill liest Sachverhalte, Gutachten, Schriftsätze, Urteile und Vermerke ein und sortiert sie nach Subsumtions-Bausteinen: Obersatz (Norm), Definition des Tatbestandsmerkmals, Subsumtion (konkrete Tatsachen unter Definition), Schlussfolgerung.

## Dokumentenarten
- **Sachverhalt:** Tatsachenmaterial mit Subsumtionsbedarf.
- **Vorgutachten / Memo:** Ist die Subsumtion sauber? Ist die Definition mit Quelle belegt?
- **Klausurlösung:** Subsumtion vs. bloße Wiederholung der Definition prüfen.
- **Urteil:** Tatbestand (§ 313 ZPO) liefert Tatsachen, Entscheidungsgründe liefern juristische Würdigung mit Subsumtion.

## Erste Triage
- Welche Norm ist Obersatz? Ist sie geltendes Recht (Fassungsstand)?
- Welche Tatbestandsmerkmale sind streitig?
- Liegt eine **vollständige Subsumtion** vor (Obersatz → Definition → Tatsachen → Schluss)?
- Anti-Muster: "Definition wiederholen statt subsumieren"; "Tatsachen umformulieren statt unter Definition zu prüfen"; "Schluss ohne Definition" (sog. Sprung-Subsumtion).
- Sprache: Gutachtenstil (Konjunktiv im Obersatz, Indikativ in Subsumtion und Schluss).

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
