---
name: workflow-dokumentenintake
description: "Dokumentenintake im Plugin patentrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte."
---

# Dokumentenintake

## Aufgabe
Dieser Workflow-Skill liest Patentanmeldungen, Bescheide DPMA/EPA, Recherche-Reports, Verletzungsabmahnungen, Lizenzverträge und FTO-Analysen (Freedom to Operate) ein und ordnet sie für die patentrechtliche Bewertung nach PatG (§§ 1, 3, 4, 9, 14, 16 PatG) und EPÜ.

## Dokumentenarten
- **Patentanmeldung / Patent:** Anspruchssatz (Hauptanspruch + Unteransprüche), Beschreibung, Zeichnungen, Zusammenfassung. Schutzbereich ergibt sich aus den Ansprüchen, Beschreibung erläutert (§ 14 PatG, Art. 69 EPÜ).
- **Recherchen-/Prüfungsbescheid DPMA bzw. EPA:** Stand der Technik (D1, D2, ...), Einwände Neuheit (§ 3 PatG / Art. 54 EPÜ) und erfinderische Tätigkeit (§ 4 PatG / Art. 56 EPÜ).
- **Verletzungsanalyse / Abmahnung:** geltend gemachte Ansprüche (Unterlassung § 139, Auskunft § 140b, Vernichtung § 140a, Schadensersatz § 139 PatG); behauptete Patentverletzung.
- **FTO-Bericht:** Drittpatente, ggf. Lizenzbedarf, Inhibierung von Produktrollouts.
- **Lizenzvertrag:** Lizenzart (einfach/ausschließlich), Gebiete, Felder, Sublizenzen, Lizenzgebühren, Best-Mode-Pflichten.

## Erste Triage
- **Status:** Anmeldung, Prüfung, erteilt, Einspruch (EPA: 9-Monats-Frist), Beschwerde, Nichtigkeitsklage (BPatG)?
- **Schutzbereich:** Hauptanspruch lesen, Merkmale gliedern.
- **Fristen:** Prioritätsfrist 12 Monate (§ 41 PatG, Art. 87 EPÜ), Einspruch EPA 9 Monate, Beschwerdefristen.
- **Beneficial owner:** Erfinderbenennung (§ 37 PatG); Diensterfindung (§ 6 ArbnErfG)?

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
