---
name: workflow-dokumentenintake
description: "Dokumentenintake im Plugin urteilsbauer-relationsmacher: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte."
---

# Dokumentenintake

## Aufgabe
Dieser Workflow-Skill liest die vollständige Akte (Klage, Klageerwiderung, Schriftsätze, Beweisangebote, Sitzungsprotokolle) ein und bereitet sie für die Relationstechnik vor: Klägerstation -> Schlüssigkeit -> Beklagtenstation -> Erheblichkeit -> Beweisstation.

## Dokumentenarten
- **Klageschrift (§ 253 ZPO):** bestimmter Antrag, Klagegrund, Beweisangebote.
- **Klageerwiderung / Schriftsätze Beklagtenseite:** Bestreiten (§ 138 Abs. 2-4 ZPO), Einreden, Gegenangriffe.
- **Replik / Duplik:** Vertiefung; auch hier auf Substantiierung achten.
- **Beweisangebote:** Zeuge, Urkunde, Augenschein, Sachverständige, Parteivernehmung.
- **Protokolle:** Erklärungen zu Protokoll, Beweisaufnahme, Geständnisse (§ 288 ZPO).

## Erste Triage Relationstechnik
- **Klägerstation (Schlüssigkeit):** Ergibt sich aus dem Klägervortrag, alle Tatsachen als wahr unterstellt, der Klageantrag?
- **Beklagtenstation (Erheblichkeit):** Stehen dem Klägervortrag erhebliche Einwendungen entgegen? Substanziierung (§ 138 ZPO)?
- **Beweisstation:** Welche streitigen Tatsachen sind beweisbedürftig? Welche Beweismittel sind angeboten? Verteilung der Beweislast?
- **Subsumtion und Tenor:** Begründetheit prüfen; konkrete Tenor-Formulierung (Hauptsache, Zinsen, Kosten, Vollstreckbarkeit).

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
