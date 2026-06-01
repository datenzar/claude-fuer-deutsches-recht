---
name: workflow-anschluss-skills-router
description: "Anschluss-Skills Router im Plugin methodenlehre-buergerliches-recht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor."
---

# Anschluss-Skills Router

## Aufgabe
Dieser Workflow-Skill leitet methodische Anliegen zu den passenden Spezialskills weiter: Auslegung, Analogie/teleologische Reduktion, Streitstandsdarstellung, Subsumtionsprüfung, Anspruchsgrundlagenprüfung in der Reihenfolge.

## Routing nach Methodenfrage
- **Auslegung eines TBM (Begriff):** Wortlaut + Systematik + Historie + Telos; ggf. verfassungs-/unionsrechtskonform. -> Auslegungs-Skill.
- **Anspruchsgrundlagenprüfung:** Vertrag, c.i.c., GoA, dinglich, Delikt, Bereicherung (vgl. `references/methodik-buergerliches-recht.md`).
- **Analogie:** planwidrige Regelungslücke + vergleichbare Interessenlage. -> Analogie-Skill; Strafrecht: Analogieverbot Art. 103 II GG beachten, im Zivilrecht zulässig.
- **Teleologische Reduktion:** Norm beschränken gegen Wortlaut auf den gewollten Anwendungsbereich; hohe Begründungslast.
- **Streitstand:** hM, Mindermeinung, Argumente, Stellungnahme. -> Streitstands-Skill.
- **Subsumtion eines Tatbestandsmerkmals:** -> Subsumtions-Skill (auch Plugin `subsumtions-pruefer`).
- **Vorlage Art. 100 GG / Art. 267 AEUV:** bei verfassungsrechtlichen / unionsrechtlichen Kollisionen prüfen.

## Anti-Muster
- Auslegung ohne Wortlautgrenze.
- Analogie ohne planwidrige Regelungslücke (positive Regelungsentscheidung des Gesetzgebers).
- "Argument aus dem Sinn der Norm" ohne historische und systematische Unterstützung.

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
