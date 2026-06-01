---
name: workflow-dokumentenintake
description: "Dokumentenintake im Plugin produktrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte."
---

# Dokumentenintake

## Aufgabe
Dieser Workflow-Skill liest Konformitätserklärungen, technische Dokumentationen, CE-Unterlagen, Marktüberwachungsbescheide, Rückrufmitteilungen, Schadensmeldungen und Lieferverträge in das Plugin `produktrecht` ein und ordnet sie ProdSG/ProdHaftG und einschlägigen EU-Verordnungen zu.

## Dokumentenarten
- **EU-Konformitätserklärung (DoC):** Hersteller, Produkt, anwendbare Richtlinien/VO, harmonisierte Normen, benannte Stelle.
- **Technische Dokumentation:** Risikoanalyse, Konstruktionsunterlagen, Prüfberichte, Betriebsanleitung, Beipackzettel.
- **Marktüberwachungsbescheid (§ 26 ProdSG):** Anordnung, Frist, Begründung; ggf. Rückrufanordnung (§ 26 Abs. 4 ProdSG).
- **Schadensmeldung Mandant / Endkunde:** Verletzte, Sachschaden, Produktidentifikation, Chronologie.
- **Lieferverträge / B2B-AGB:** Haftungsregeln, Freistellung, Versicherung, Audit.

## Erste Triage
- **Produktkategorie und Regulatorik:** Maschinenverordnung (EU) 2023/1230, Niederspannungs-RL 2014/35/EU, EMV-RL 2014/30/EU, Spielzeug-RL 2009/48/EG, MedizinprodukteVO (EU) 2017/745 (MDR), GPSR (EU) 2023/988, Bauprodukten-VO (EU) 305/2011, BatterieVO (EU) 2023/1542.
- **Rolle:** Hersteller, Bevollmächtigter, Importeur, Händler, Fulfillment-Dienstleister (Art. 4 (EU) 2019/1020).
- **Verschuldensunabhängige Haftung:** § 1 ProdHaftG (i. V. m. Produkthaftungs-RL 85/374/EWG; ab 2026 abgelöst durch RL (EU) 2024/2853).
- **Fristen:** Meldepflicht bei ernster Gefahr nach Art. 19 GPSR (24h); RAPEX/Safety Gate.

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
