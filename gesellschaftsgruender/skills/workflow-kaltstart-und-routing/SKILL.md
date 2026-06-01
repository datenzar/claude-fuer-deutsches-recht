---
name: workflow-kaltstart-und-routing
description: "Kaltstart und Routing im Plugin gesellschaftsgruender: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills."
---

# Kaltstart und Routing

## Aufgabe
Dieser Workflow-Skill für `gesellschaftsgruender` Kaltstart und Routing im Plugin gesellschaftsgruender: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Routing-Cheatsheet Gesellschaftsgründung

| Stichwort | Anschluss-Skill | Erste Norm |
| --- | --- | --- |
| "Welche Rechtsform?" | `spezial-gruendungsassistent-erstpruefung-und-mandatsziel` + `spezial-rechtsformwahl-behoerden-gericht-und-registerweg` | Haftung, Kapital, Notar |
| "GmbH gründen" | `spezial-gmbh-fristen-form-und-zustaendigkeit` | § 5 GmbHG 25.000 EUR, § 2 GmbHG notariell |
| "UG (haftungsbeschränkt)" | `spezial-gmbh-fristen-form-und-zustaendigkeit` | § 5a GmbHG 1 EUR, 25 % Thesaurierung |
| "GmbH&Co.KG" | `gesellschaftsgruender-kg-und-gmbhcokg` | §§ 161 ff. HGB i.V.m. § 19 GmbHG |
| "PartG mbB" | `spezial-partg-dokumentenmatrix-und-lueckenliste` | § 8 Abs. 4 PartGG, Berufshaftpflicht |
| "Geschäftsführervertrag" | `spezial-geschaeftsfuehrervertrag-livequellen-check` | § 35 GmbHG i.V.m. Dienstvertrag |
| "gGmbH gemeinnützig" | `spezial-ggmbh-risikoampel-und-gegenargumente` | §§ 51 ff. AO, Mustersatzung |
| "Transparenzregister" | `gesellschaftsgruender-transparenzregister` | §§ 19 ff. GwG |
| "Online-Gründung DiRUG" | `spezial-gmbh-fristen-form-und-zustaendigkeit` | § 2 Abs. 3 GmbHG, Sacheinlagen ausgeschlossen |
| "GbR / eGbR MoPeG" | `spezial-partg-dokumentenmatrix-und-lueckenliste` + `gesellschaftsgruender-kg-und-gmbhcokg` | §§ 705 ff., 707 ff. BGB n.F. seit 1.1.2024 |

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
