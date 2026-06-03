---
name: workflow-anschluss-skills-router
description: "Anschluss-Skills Router im Plugin forschungszulage-antragstellung: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor."
---

# Anschluss-Skills Router

## Aufgabe
Dieser Workflow-Skill für `forschungszulage-antragstellung` Anschluss-Skills Router im Plugin forschungszulage-antragstellung: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Forschungszulage: das zweistufige Verfahren

| Stufe | Stelle | Inhalt |
|---|---|---|
| 1. BSFZ-Bescheinigung | Bescheinigungsstelle Forschungszulage (BSFZ) | inhaltliche Prüfung der FuE-Tätigkeit nach § 2 FZulG |
| 2. Festsetzung der Forschungszulage | zuständiges Finanzamt | Berechnung Bemessungsgrundlage, Festsetzung Forschungszulage nach § 10 FZulG |

Beide Stufen sind **getrennt** zu durchlaufen; die BSFZ-Bescheinigung ist Grundlagenbescheid für das Finanzamt.

## Routing nach FZulG-Themen

| Frage | Folgeskill |
|---|---|
| Ist mein Projekt FuE-fähig? | spezial-foerdercheck-risikoampel-und-gegenargumente |
| BSFZ-Portaltexte verfassen (Zeichenbudget!) | spezial-antragstellung-tatbestand-beweis-und-belege + spezial-bsfz-behoerden-gericht-und-registerweg |
| Plädoyer / überzeugende Begründung für BSFZ, Finanzamt, Einspruch oder Geschäftsführung | fz-plaedoyer-begruendung-und-verteidigung |
| Bemessungsgrundlage berechnen | spezial-antrag-zahlen-schwellen-und-berechnung + spezial-bemessungsgrundlage-mehrparteien-konflikt-und-interessen |
| Auftragsforschung / FuE durch Dritte | spezial-bemessungsgrundlage-mehrparteien-konflikt-und-interessen |
| Beihilfen-/De-minimis-Frage | spezial-beihilfen-beweislast-und-darlegungslast |
| Bescheid abgelehnt / Einspruch | spezial-einspruch-sonderfall-und-edge-case |
| Verlustlage / Konzern | spezial-abgrenzung-compliance-dokumentation-und-akte + Steuerberater einbeziehen |

## Wichtige Quellen (live verifizieren)

- **bescheinigung-forschungszulage.de** (BSFZ): Anträge, Merkblätter, FAQ.
- **bundesfinanzministerium.de**: BMF-Schreiben zum FZulG (vor Ausgabe Datum und AZ verifizieren).
- **bzst.de**: Bundeszentralamt für Steuern (Beihilfen / De-minimis-Schnittstelle).
- **gesetze-im-internet.de**: FZulG-Wortlaut.
