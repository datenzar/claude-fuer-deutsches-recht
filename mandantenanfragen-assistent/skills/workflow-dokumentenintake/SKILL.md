---
name: workflow-dokumentenintake
description: "Dokumentenintake im Plugin mandantenanfragen-assistent: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte."
---

# Dokumentenintake

## Aufgabe
Dieser Workflow-Skill liest eingehende Mandantenanfragen (E-Mail, Kontaktformular, Telefonat-Notiz, hochgeladene Anlagen) und bereitet Erstberatungs-Triage vor. Mandantengeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB) ist Grundlage; AVV nach Art. 28 DSGVO Pflicht für jeden externen Verarbeiter.

## Dokumentenarten erkennen
- **Mandantenmail mit Frist:** typisch "Bis zum ...", "Vorladung am ..."; sofort Fristenkontrolle und vorläufige Mandatsannahme.
- **Bescheid / Klage / Schriftsatz Gegenseite:** Eingangsdatum, Zustellungsnachweis, Rechtsmittelfrist eintragen.
- **Vertrag / AGB / Korrespondenz:** Sachverhaltsbasis für Mandantengespräch.
- **Anlagenkonvolut ohne Erklärung:** Mandant strukturiert oft chronologisch -- Belegmatrix vor inhaltlicher Bewertung erstellen.

## Erste Triage
- Rolle: Bestandsmandat oder Neumandat? Konflikt mit anderem Mandat (§ 3 BORA)?
- Zuständigkeit der Kanzlei (Rechtsgebiet, Fachanwalt)?
- Frist binnen 7 Tagen, 14 Tagen, länger? -- Eilstufe markieren.
- Mandant Verbraucher oder Unternehmer? Pflichtbelehrung bei Fernabsatz und Beratungsvertrag (§§ 312 ff. BGB).
- Vergütung: gesetzliches RVG, Honorarvereinbarung (Textform genügt nach § 3a RVG), Beratungshilfe (BerHG)?

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
