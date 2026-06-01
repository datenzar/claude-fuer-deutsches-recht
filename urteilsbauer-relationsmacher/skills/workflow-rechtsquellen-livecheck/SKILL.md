---
name: workflow-rechtsquellen-livecheck
description: "Rechtsquellen-Livecheck im Plugin urteilsbauer-relationsmacher: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen."
---

# Rechtsquellen-Livecheck

## Aufgabe
Dieser Workflow-Skill verlangt vor jedem Urteilsentwurf den Live-Check der einschlägigen ZPO-Normen, Tatbestandsbausteine und Leitentscheidungen, damit der spätere Tenor und die Begründung tragen.

## Pflichtquellen Urteilsbau
- **ZPO:** `gesetze-im-internet.de/zpo`; insbesondere § 313 (Inhalt des Urteils), § 286 (freie Beweiswürdigung), § 287 (Schadensschätzung), § 92 ff. (Kostenentscheidung), § 708 ff. (vorläufige Vollstreckbarkeit), § 543 (Revisionszulassung), § 522 (Verwerfung Berufung als unbegründet).
- **GVG:** Geschäftsverteilungsplan, Einzelrichter / Kammer (§ 348 ZPO).
- **Materielles Recht:** BGB, HGB, ArbR, FamilienR, ErbR -- jeweils Fassung am Tag des Entscheids.
- **Rechtsprechung:** BGH (`bundesgerichtshof.de`) für Leitentscheidungen, OLG-Sammlungen länderspezifisch, BVerfG (`bverfg.de`) für verfassungsrechtliche Bezüge.
- **EuGH `curia.europa.eu`:** bei Unionsrechts-Bezug; Vorlagepflicht Art. 267 AEUV bei letztinstanzlichen Gerichten.

## Anti-Halluzinations-Regeln
- Tatbestand stets neutral, Wertungen in den Entscheidungsgründen.
- Az.-Konsistenz: Senatsbuchstabe BGH (VI, V, VII, VIII, IX, X, XI, XII) muss zum Rechtsgebiet passen.
- Zitiernachweise nach `references/zitierweise.md` (BGH, Datum, Az., Fundstelle, Rn.).
- Bei Verweis auf Sachverständigengutachten: Az., Datum, Sachverständiger, Tenor.

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
