---
name: workflow-rechtsquellen-livecheck
description: "Rechtsquellen-Livecheck im Plugin mandantenanfragen-assistent: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen."
---

# Rechtsquellen-Livecheck

## Aufgabe
Dieser Workflow-Skill erzwingt, dass jede gegenüber dem Mandanten ausgesprochene Rechtsauskunft mit aktuellen, frei prüfbaren Quellen belegt ist. Mandantengeheimnis bleibt gewahrt; bei externer Recherche keine personenbezogenen Mandantendaten in nicht-AVV-fähige Tools.

## Pflichtquellen Mandantenkommunikation
- **Berufsrecht:** BRAO, BORA, RVG, FAO -- `brak.de`, `gesetze-im-internet.de`.
- **Materielles Recht:** `gesetze-im-internet.de`, `dejure.org` (mit Verlinkung zu Rspr.).
- **Rechtsprechung:** `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, Landesarbeitsgerichte über `lareda.hessenrecht.hessen.de` u. ä.; OLG-Datenbanken länderspezifisch.
- **EU-Recht und EuGH:** `eur-lex.europa.eu`, `curia.europa.eu`.
- **Formulare und Behördenseiten:** `service.bund.de`, Online-Justiz der Länder, FormularServer.

## Anti-Halluzinations-Regeln
- Niemals BGH-Az. erfinden. Bei Unsicherheit "ständige Rspr. des BGH (vgl. z. B. ...)" und Az. live nachprüfen.
- Keine Kommentar-, Aufsatz-, BeckRS-Fundstellen aus Modellwissen. Nur, wenn Mandant oder externe Recherche die Stelle bestätigt.
- Norm-Stand markieren: Bei ständig geänderten Gesetzen (StGB nach Reformen, ZPO nach Beschleunigungsnovellen, EnWG, GwG, GEG) Fassungsdatum nennen.

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
