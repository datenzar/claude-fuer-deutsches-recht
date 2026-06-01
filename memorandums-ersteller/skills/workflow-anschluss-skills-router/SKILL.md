---
name: workflow-anschluss-skills-router
description: "Anschluss-Skills Router im Plugin memorandums-ersteller: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor."
---

# Anschluss-Skills Router

## Aufgabe
Dieser Workflow-Skill leitet die Memo-Aufgabe an die passenden Spezial-Skills weiter: Strukturentwurf, Subsumtionsabschnitt, Quellenarbeit, Risiko-Matrix, Executive-Summary-Generator, Vertraulichkeits-/Privilege-Check.

## Routing nach Memo-Phase
- **Strukturentwurf:** Skills für Memo-Skelett und Gliederung; Standardstruktur nach CLAUDE.md.
- **Sachverhaltsdarstellung:** Faktenmatrix, Belegmatrix, Chronologie -- verweise auf `workflow-chronologie-und-belegmatrix`.
- **Subsumtion / rechtliche Bewertung:** Gutachtenstil-Skill, Streitstand bei tragenden Merkmalen.
- **Quellen:** Verweis auf `workflow-rechtsquellen-livecheck` und `references/zitierweise.md` (Pflicht).
- **Kurzantwort / Executive Summary:** komprimierende Skills; eine Aussage je Frage.
- **Risiko-Matrix:** Bewertung der Restrisiken (rechtlich, faktisch, prozessual, reputativ).
- **Vertraulichkeit:** Privileged & confidential, Reichweite des Anwaltsprivilegs (EU vs. US, Konzernreichweite).

## Anti-Muster
- Memo ohne Kurzantwort am Anfang -- Adressat findet das Ergebnis nicht.
- Fußnoten ohne Verifizierung (Halluzinationsrisiko bei Aufsatz- und Kommentarfundstellen).

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
