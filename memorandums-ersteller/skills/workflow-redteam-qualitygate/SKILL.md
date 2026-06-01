---
name: workflow-redteam-qualitygate
description: "Red-Team Qualitygate im Plugin memorandums-ersteller: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton."
---

# Red-Team Qualitygate

## Aufgabe
Dieser Workflow-Skill prüft das fertige Memo vor Versand auf typische Schwächen: Halluzinationen, fehlende Gegenargumente, übersehene Sondernormen, schwache Subsumtion, unklare Empfehlung, fehlender Vertraulichkeitsvermerk.

## Red-Team-Punkte Memo
- **Halluzinations-Scan:** Jede zitierte Entscheidung mit echtem Az.? "Ständige Rspr." mit konkretem Az. belegt? Kommentar-/Aufsatzfundstellen mit Quelle?
- **Anspruchsgrundlagen vollständig?** Reihenfolge Vertrag, c.i.c., GoA, dinglich, Delikt, Bereicherung (vgl. CLAUDE.md / `references/methodik-buergerliches-recht.md`).
- **Subsumtion sauber?** Obersatz - Definition - Tatsachen - Schluss; keine Sprung-Subsumtion; keine Zirkelschlüsse.
- **Gegenargumente / Mindermeinung gewürdigt?** Wenn entscheidungserheblich.
- **Sondernormen geprüft?** AGB-Recht (§§ 305 ff. BGB), Verbraucherschutz (§§ 13, 14, 312 ff. BGB), DSGVO, Sektorengesetze (KWG, ZAG, GWG, etc.).
- **Auslegung erklärt?** Vier Auslegungsmethoden zzgl. verfassungs-/unionsrechtskonform.
- **Empfehlung klar?** Eine Linie, mit Begründung; Alternativen mit Trade-off.
- **Risikoanalyse?** Restrisiken benannt; "Cone of uncertainty".
- **Form:** Kurzantwort am Anfang, Quellenverzeichnis am Ende, Privileged & confidential.
- **Sprache:** Gutachtenstil bei Memo-Hauptteil; Cover-Letter mandantengerecht.
- Falle: Memo nur aus Mandantenperspektive -- bedenke immer auch die Sicht der Gegenseite / der Behörde / des Gerichts.

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
