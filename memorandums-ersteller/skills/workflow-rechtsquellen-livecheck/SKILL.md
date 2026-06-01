---
name: workflow-rechtsquellen-livecheck
description: "Rechtsquellen-Livecheck im Plugin memorandums-ersteller: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen."
---

# Rechtsquellen-Livecheck

## Aufgabe
Dieser Workflow-Skill erzwingt den Live-Check sämtlicher tragender Quellen im Memo (Norm, Rspr., Lit., Gesetzgebungsmaterialien). Ein Memo ist nur so belastbar wie seine Belege.

## Pflichtquellen Memo
- **Normen:** `gesetze-im-internet.de` mit Fassungsstand; Landesrechts-Portale; bei EU-Recht `eur-lex.europa.eu` (offizielles Amtsblatt).
- **Rechtsprechung:** BGH, BVerfG, BVerwG, BAG, BSG, BFH, EuGH -- jeweils offizielle Seiten mit ECLI/Az.
- **Gesetzgebungsmaterialien (für historische Auslegung):** `dipbt.bundestag.de` (BT-Drs.); Bundesrat-Drs.; ggf. Stellungnahmen der wissenschaftlichen Dienste.
- **EU-Materialien:** Erwägungsgründe der jeweiligen Richtlinie/Verordnung; Vorschläge der Kommission COM-Dokumente.
- **Verwaltungsverlautbarungen:** BMF-Schreiben, BaFin-Rundschreiben, BAFin-Merkblätter, BKartA-Bekanntmachungen -- direkt auf der Behördenseite.

## Zitierdisziplin (vgl. `references/zitierweise.md`)
- Rspr.: Gericht, Datum, Az., Fundstelle, Rn.
- Kommentar: Bearbeiter, "in:" Werk, Auflage, Jahr, Norm, Rn.
- Aufsatz: Autor, Zeitschrift, Jahrgang, Anfangsseite (konkrete Seite).
- Reihenfolge: Rspr. vor Lit.; neueste zuerst.

## Anti-Halluzinations-Regeln
- Aktenzeichen nicht ergänzen. "BGH ständige Rspr. (vgl. zuletzt ...)" mit echtem Az.
- Kommentar- und Aufsatzfundstellen nur mit gelieferter Quelle oder lizenziertem Live-Zugriff.

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
