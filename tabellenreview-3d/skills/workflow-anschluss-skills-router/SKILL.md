---
name: workflow-anschluss-skills-router
description: "Anschluss-Skills Router im Plugin tabellenreview-3d: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor."
---

# Anschluss-Skills Router

## Aufgabe
Dieser Workflow-Skill leitet nach Sichtung in den passenden Tabellen-Review-Spezialskill: Spaltenintegrität, Zeilenkohärenz, Querbezüge, Insolvenztabellenanalyse, Cap-Table-Audit, Anlagenmatrix.

## Routing nach Tabellentyp
- **Insolvenztabelle (§ 174 ff. InsO):** Anmeldung, Bestreiten, Feststellung, Rang; Verweis auf Insolvenzplan-Skill (`insolvenzplan-starug-planwerkstatt`).
- **Cap Table:** Anteilsklassen, Vesting, Pre-Money/Post-Money, Verwässerung, Liquidation Preferences; Verweis auf `wandeldarlehen-lebenszyklus`, `gesellschaftsrecht`.
- **Forderungsaufstellung / Mahnbescheidsantrag:** Hauptforderung, Zinsen (§ 288 BGB), Verzugsschaden, Kosten (RVG).
- **Schadens-/Bilanztabelle:** Schadensposten, Beleg, Beweismittel; Querverweis auf Schadensberechnungs-Skill.
- **Anlagentabelle Schriftsatz (K1, K2 / B1, B2):** Reihenfolge wie zitiert; Anlagen-Konvolut nummerieren.
- **JVEG-Stundenaufstellung:** Spalten Tag, Tätigkeit, Stundenzahl, Honorargruppe, Betrag, USt; Verweis auf `jveg-kostenpruefer`.

## Anti-Muster
- Tabellen ohne Spalte "Quelle/Beleg" -- nicht auditfähig.
- Summen ohne Cross-Check; Rundungsfehler.
- Mehrere Versionen ohne Versionsspalte / Stand.

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
