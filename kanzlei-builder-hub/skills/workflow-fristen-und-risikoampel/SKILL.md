---
name: workflow-fristen-und-risikoampel
description: "Fristen- und Risikoampel im Plugin kanzlei-builder-hub: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen."
---

# Fristen- und Risikoampel

## Aufgabe
Dieser Workflow-Skill markiert beim Skill-/Plugin-Bau die typischen Risiken: Validator-Fehler, Versionsdrift, Halluzinations-Pfade, Mandantengeheimnis-Konformität, Update-Frist für Rechtsprechungs- und Norm-Änderungen.

## Risikoampel Builder-Hub
- **Rot:** `validate-yaml-frontmatter.py` oder `validate-plugin-structure.mjs` schlägt fehl -- darf nicht ausgeliefert werden.
- **Rot:** Komma-Zahl in `description` (Frontmatter) -- "1,5" statt "1.5"; Validator schlägt fehl.
- **Rot:** Skill-Description enthält Mandantendaten / Beispiele mit Klarnamen.
- **Rot:** Bezug auf erfundene BGH-/EuGH-Az. im Skill-Inhalt.
- **Gelb:** Skill verweist auf andere Skills, die umbenannt wurden -> broken link.
- **Gelb:** Plugin enthält Skill ohne Querverweise zum Anschluss-Skill.
- **Gelb:** Skill bezieht sich auf Norm-Fassung, ohne Fassungsdatum zu nennen (z. B. "ZPO" ohne Hinweis auf KostRMoG / Beschleunigungsnovelle).
- **Grün:** Validator ohne Fehler, Querverweise konsistent, Halluzinationssperre eingebaut, Sprache Deutsch.

## Update-Fristen
- **Quartalsweise:** Norm-Updates der zentralen Gesetzbücher (BGB, ZPO, StGB, AktG, UStG, EStG, ggf. spezielle Verfahrensordnungen).
- **Monatlich:** Rspr.-Updates für Highlight-Entscheidungen (BGH Pressemitteilungen, BVerfG, EuGH).
- **Ad-hoc:** bei tagesaktuellen Gesetzes-/Verordnungsänderungen (z. B. GPSR, AI Act, eIDAS 2.0).

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
