---
name: workflow-redteam-qualitygate
description: "Red-Team Qualitygate im Plugin schriftform-und-textform-bgb: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton."
---

# Red-Team Qualitygate

## Aufgabe
Dieser Workflow-Skill stresst formrechtliche Ergebnisse gegen typische Fehler: Verwechslung Schrift-/Text-/elektronische Form, falsche Bewertung qualifizierter Signaturen, Übersehen von Heilungstatbeständen.

## Formenkanon prüfen
- **Schriftform (§ 126 BGB):** eigenhändige Namensunterschrift unter der Urkunde; gewillkürte Schriftform (§ 127 BGB) lässt Telekommunikationsformen zu, soweit nicht anders bestimmt.
- **Elektronische Form (§ 126a BGB):** ersetzt Schriftform nur mit qualifizierter elektronischer Signatur (QES) nach Art. 3 Nr. 12, Art. 25 Abs. 2 eIDAS-VO (EU) 910/2014.
- **Textform (§ 126b BGB):** lesbare Erklärung, dauerhafter Datenträger, Person des Erklärenden genannt -- E-Mail genügt regelmäßig; Fax ebenfalls.
- **Notarielle Beurkundung (§ 128 BGB):** für § 311b BGB (Grundstück), § 2247 BGB (Testament alternativ Eigenhändigkeit), § 1410 BGB (Ehevertrag), § 2348 BGB (Erbverzicht).
- **Öffentliche Beglaubigung (§ 129 BGB):** Notar bestätigt Echtheit der Unterschrift -- nicht den Inhalt.

## Red-Team-Punkte
- Schriftform durch eingescannte Unterschrift? -- Nein, allenfalls Textform.
- AGB-mäßige doppelte Schriftformklausel im Arbeitsverhältnis? -- BAG hat solche Klauseln vielfach für unwirksam gehalten (siehe ständige Rspr. des BAG zu § 305c, § 307 BGB; konkrete Az. live prüfen).
- DocuSign / Adobe Sign mit einfacher oder fortgeschrittener Signatur erfüllt **keine** Schriftform; nur QES.
- Heilung beachten: § 311b Abs. 1 S. 2 BGB (Grundstück: Heilung durch Auflassung und Eintragung), § 766 S. 3 BGB (Bürgschaft Vollkaufmanns, § 350 HGB), § 550 BGB (langjährige Mietverträge: Folge ordentliche Kündbarkeit, nicht Nichtigkeit).
- Frist Mietrecht § 550 BGB: nur Verträge mit Laufzeit > 1 Jahr.
- Falle: Bei zustimmungspflichtigem Geschäft Form des Hauptgeschäfts auch für Vollmacht? § 167 Abs. 2 BGB -- Sondertatbestände (Bürgschaft, Grundstück) beachten.

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
