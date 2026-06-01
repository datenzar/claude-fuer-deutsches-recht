---
name: workflow-dokumentenintake
description: "Dokumentenintake im Plugin schriftform-und-textform-bgb: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte."
---

# Dokumentenintake

## Aufgabe
Dieser Workflow-Skill liest streitige Erklärungen, Kündigungen, Verträge, Vollmachten, E-Mails, PDFs und Unterschriftsbilder ein und ordnet sie den Form-Tatbeständen des BGB zu (§§ 125-127, 126-126b BGB).

## Dokumentenarten
- **Vertragsurkunde:** Wer hat unterschrieben? Originalunterschrift oder Faksimile? Doppelt unterzeichnet?
- **Kündigungsschreiben:** wessen Unterschrift, in welcher Form (Schrift, Text, qualifiziert elektronisch)? Zugang nachgewiesen (§ 130 BGB)?
- **Vollmacht:** Form richtet sich nach Hauptgeschäft (§ 167 Abs. 2 BGB) -- Sondertatbestände beachten (§ 766 BGB Bürgschaft, § 311b BGB Grundstück: Notarform).
- **E-Mail / Messenger-Nachricht:** regelmäßig Textform (§ 126b BGB), nicht Schriftform.
- **PDF mit eingescannter Unterschrift:** keine Schriftform i. S. d. § 126 BGB, allenfalls Textform; ggf. nach AGB als ausreichend qualifiziert.
- **DocuSign / Adobe Sign:** je nach Verfahren einfache (EES), fortgeschrittene (FES) oder qualifizierte elektronische Signatur (QES); nur QES erfüllt Schriftform (§ 126a BGB i. V. m. Art. 25 Abs. 2 eIDAS-VO (EU) 910/2014).

## Erste Triage
- Welche Formanforderung ist gesetzlich verlangt (z. B. § 766 BGB, § 311b BGB, § 623 BGB, § 550 BGB, § 484 BGB, § 4 NachwG, § 14 BetrVG, § 1410 BGB)?
- Vertragliche / AGB-bedingte Formvereinbarung (§ 127 BGB)? Einfache oder qualifizierte Schriftformklausel? Doppelte Schriftformklausel kann nach AGB-Recht unwirksam sein (BAG, ständige Rspr.).
- Folge bei Nichteinhaltung: § 125 BGB Nichtigkeit, sofern keine Heilung.

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
