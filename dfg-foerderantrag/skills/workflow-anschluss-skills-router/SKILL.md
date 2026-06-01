---
name: workflow-anschluss-skills-router
description: "Anschluss-Skills Router im Plugin dfg-foerderantrag: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor."
---

# Anschluss-Skills Router

## Aufgabe
Dieser Workflow-Skill für `dfg-foerderantrag` Anschluss-Skills Router im Plugin dfg-foerderantrag: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Routing nach DFG-Antragsphase

| Frage | Folgeskill |
|---|---|
| Erstantrag, Forschungsperson neu? | spezial-dfg-erstpruefung-und-mandatsziel + spezial-anfaenger-risikoampel-und-gegenargumente |
| Sachbeihilfe-Standard | spezial-foerderantragssteller-tatbestand-beweis-und-belege |
| Koselleck-Reinhart-Programm (große Strategien) | spezial-koselleck-mehrparteien-konflikt-und-interessen |
| Finanzplan / Personalmittel / Sach- und Investitionsmittel | spezial-finanzplan-mandantenkommunikation-entscheidungsvorlage + spezial-antraege-zahlen-schwellen-und-berechnung |
| elan-Portal-Einreichung | spezial-elan-formular-portal-und-einreichung |
| Forschungsdaten / DMP | spezial-forschungsdaten-fristennotiz-und-naechster-schritt |
| Ethik / KI-Einsatz / IRB | spezial-ethik-abschlussprodukt-und-uebergabe |
| Reviewer-Reaktion / Wiedereinreichung | spezial-formalia-red-team-und-qualitaetskontrolle |

## Wichtige DFG-Quellen (vor Ausgabe live verifizieren)

- **dfg.de/formulare**: aktuelle Antragsformulare und Merkblätter.
- **dfg.de/foerderung/programme**: Sachbeihilfe, Emmy Noether, Heisenberg, Reinhart Koselleck, SFB, Graduiertenkollegs.
- **elan.dfg.de**: elektronisches Antragsportal.
- **dfg.de/leitfaden**: Verwendungsrichtlinien (Allg. Bedingungen für Sachbeihilfen "Verwendungsrichtlinien").
- **dfg.de/foerderung/grundlagen_rahmenbedingungen**: gute wissenschaftliche Praxis, Forschungsdaten, KI.

## Praktischer Tipp

- DFG-Anträge folgen keinem Frist-Stichtag (außer ausgeschriebene Programme); Sachbeihilfe ist ganzjährig einreichbar.
- Wer zum ersten Mal beantragt: zwingend "Erstantrag" markieren; das aktiviert die DFG-interne Mentor-Schiene.
