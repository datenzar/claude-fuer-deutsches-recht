---
name: workflow-output-waehlen
description: "Output wählen im Plugin zitierweise-deutsches-recht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung."
---

# Output wählen

## Aufgabe
Dieser Workflow-Skill bestimmt das Format der Zitierprüfung: Korrektur-Markup (Track Changes), Fundstellenliste, Quellenverzeichnis, Plagiats-Risikoreport, Stil-Memo.

## Outputtypen
- **Korrektur-Markup im Word-/PDF-Dokument:** Zitat-für-Zitat-Annotation; falsche Zitate ergänzen, doppelte streichen.
- **Fundstellenliste (Tabelle):** Spalten Zitat im Text, Norm/Rspr./Lit., Quelle/Beleg, Status (verifiziert / unklar / falsch), Empfehlung.
- **Quellenverzeichnis am Memo-/Hausarbeitsende:** vollständige Auflistung Rspr. und Lit., alphabetisch nach Autor, chronologisch nach Datum.
- **Plagiats-Risikoreport:** Passagen ohne Beleg, abgeschriebene Formulierungen, fehlende eigene Würdigung.
- **Stil-Memo:** Hinweise zu Verlagsstil (NJW vs. JuS vs. JZ vs. Festschrift), Hausstil der Kanzlei, Hausarbeitsstil der Lehrstühle.

## Referenz und Standard
- Bindender Hausstandard: `references/zitierweise.md`.
- Pflichtfelder Rspr.: Gericht, Datum, Aktenzeichen, Fundstelle, Randnummer.
- Pflichtfelder Lit.: Autor, Werk/Zeitschrift, Auflage/Jahrgang, Anfangsseite (konkrete Seite), ggf. Norm und Rn.
- Reihenfolge: Rspr. vor Lit.; neueste zuerst.

## Anti-Muster
- "vgl. nur" als Tarnung für ungeprüfte Sammelzitate.
- Kommentar-/Aufsatz-Fundstellen aus Modellwissen ohne Verifizierung.

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
