---
name: workflow-dokumentenintake
description: "Dokumentenintake im Plugin patentrecherche: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte."
---

# Dokumentenintake

## Aufgabe
Dieser Workflow-Skill liest Rechercheanforderungen, technische Beschreibungen, Erfindungsmeldungen, frühere Recherche-Reports und Norm-/Standarddokumente ein und bereitet sie zu einer durchsuchbaren Rechercheaufgabe (Stand der Technik, FTO, Family-Watch, Validity-Search).

## Dokumentenarten
- **Erfindungsmeldung / technische Beschreibung:** Merkmale, Wirkung, Aufgabe, Varianten -- Basis für Suchstrategie.
- **Schutzanspruch / Anspruchssatz:** für FTO und Validity-Suche maßgeblich (Wortlaut + Beschreibung).
- **Frühere Recherche:** Suchstrategien, gefundene Dokumente, Lücken; klassifizierende IPC-/CPC-Codes notieren.
- **Standard-/Normdokumente:** ETSI, IEEE, ISO, DIN -- relevant für SEP / FRAND.
- **Mandantenliste eigener und Wettbewerber-Patente:** für Family-Watch und Wettbewerbsanalyse.

## Erste Triage
- **Rechercheart:** Stand der Technik (state of the art), Patentierbarkeits-Recherche (Patentability), Freedom-to-Operate (FTO), Validity (Nichtigkeitsangriff), Family-Watch (Monitoring).
- **Suchsprache(n):** Englisch, Deutsch, Französisch, Japanisch, Chinesisch -- nach Marktgebiet und Schutzregion.
- **IPC/CPC-Klassen:** zentrale Klassifikationen identifizieren über `worldwide.espacenet.com`.
- **Zeitraum:** Stichtag = Prioritätstag / Anmeldetag (für Neuheit § 3 PatG, Art. 54 EPÜ).
- **Quellen:** Espacenet, DEPATISnet (DPMA), Google Patents, Patentscope (WIPO), USPTO, JPlatPat, CNIPA.

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
