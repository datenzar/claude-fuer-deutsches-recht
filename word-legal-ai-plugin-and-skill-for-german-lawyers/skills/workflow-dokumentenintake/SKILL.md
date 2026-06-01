---
name: workflow-dokumentenintake
description: "Dokumentenintake im Plugin word-legal-ai-plugin-and-skill-for-german-lawyers: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte."
---

# Dokumentenintake

## Aufgabe
Dieser Workflow-Skill liest Microsoft-Word-Dokumente (.docx) in die juristische Arbeitsumgebung ein und bereitet sie für strukturierten Eingriff vor: Formatvorlagen, Querverweise, Inhaltsverzeichnis, Track Changes, Kommentare, Felder, Schnellbausteine.

## Dokumentenarten
- **Schriftsatzentwurf:** Formatvorlagen "Überschrift 1/2/3" prüfen; Anrede, Rubrum, Antrag, Begründung, Beweise.
- **Vertragsentwurf:** mit Definitionen-Glossar, Querverweisen ("§ 5 Abs. 2"), Anlagenverzeichnis, Schlussbestimmungen.
- **Memo:** mit Inhaltsverzeichnis, Fußnoten, Quellenverzeichnis.
- **Redline-Vorlage (Markup):** Annahme/Ablehnung von Änderungen, Kommentarflut.
- **Mustertext aus Schnellbausteinen:** unternehmensweite Vorlagen (Briefkopf, Honorarvereinbarung, Vollmacht).

## Erste Triage
- Welche **Word-Version** (Microsoft 365, 2021, 2019, Mac vs. Win)? Funktionsumfang unterschiedlich.
- Welche Formatvorlagen aktiv? "Format > Formatvorlagen anzeigen" - sind sie konsistent oder direkte Formatierungen drüber?
- Track Changes aktiv? "Überprüfen > Änderungen nachverfolgen". Pre-existing Annahme/Ablehnung nötig?
- Querverweise & Felder: "Einfügen > Querverweis"; auf Feldnamen achten (REF, NUMPAGES, SEQ).
- Vertraulichkeit: Mandantengeheimnis bei Cloud-Synchronisation (OneDrive); AVV nach Art. 28 DSGVO klären.

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
