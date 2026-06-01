---
name: workflow-anschluss-skills-router
description: "Anschluss-Skills Router im Plugin jveg-kostenpruefer: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor."
---

# Anschluss-Skills Router

## Aufgabe
Dieser Workflow-Skill leitet die JVEG-Kostenprüfung zu den passenden Spezialskills weiter. Er unterscheidet die Aufgabentypen: Sachverständigenhonorar, Dolmetscher/Übersetzer, Sachverständigenauslagen, Erinnerung gegen Festsetzung.

## Routing nach Aufgabentyp
- **Honorargruppen-Prüfung (§ 9 JVEG i. V. m. Anlage 1):** -> Sachverständigen-Skill mit Honorargruppen-Check.
- **Stundenzahl/Zeitaufwand-Plausibilität:** Erforderlichkeit nach § 8 Abs. 2 JVEG.
- **Auslagen (§§ 5-8 JVEG):** Fahrtkosten (§ 5 JVEG: 0.42 EUR/km Pkw, Bahnkarte), Übernachtung, Tage-/Abwesenheitsgeld, Schreibauslagen (§ 7 JVEG).
- **Dolmetscher (§ 9 Abs. 3 JVEG):** simultan 85 EUR/h, konsekutiv 75 EUR/h (Stand: prüfen unter `gesetze-im-internet.de`).
- **Übersetzung (§ 11 JVEG):** Grundbetrag pro 55-Zeichen-Zeile, ggf. höher bei Schwierigkeit oder Eile.
- **Erinnerung / Beschwerde (§ 4 JVEG):** Frist sechs Monate ab Bekanntgabe; ohne Aufschiebende Wirkung.

## Anti-Muster
- Pauschale Anwendung "alter" Sätze, ohne aktuelle Fassung des JVEG zu prüfen (laufende Anpassungen, zuletzt KostRÄG).
- Vermengung von JVEG-Vergütung und RVG-Anwaltsvergütung.

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
