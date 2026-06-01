---
name: spezial-rechtsformwahl-behoerden-gericht-und-registerweg
description: "Rechtsformwahl: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output."
---

# Rechtsformwahl: Behörden-, Gerichts- oder Registerweg

## Aufgabe
Dieser Skill ist ein konkreter Fachbaustein für `gesellschaftsgruender`. Ausgangspunkt ist: Gründungsassistent deutsche Gesellschaften (GmbH UG GbR OHG KG GmbH und Co KG PartG mbB gGmbH). Von Rechtsformwahl über Gesellschaftsvertrag und Geschäftsführervertrag bis Notar Handelsregister Gewerbeamt Finanzamt Transparenzregister. MoPeG DiRUG GwG. Kein Ersatz für Anwaltsberatung.

Er führt durch **Behörden-, Gerichts- oder Registerweg** im Themenfeld **Rechtsformwahl**. Ziel ist nicht ein abstrakter Lexikontext, sondern ein belastbares Arbeitsprodukt für die nächste anwaltliche, behördliche, gerichtliche, organisatorische oder mandantenbezogene Entscheidung.

## Kaltstart
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Rechtsformmatrix (Kurzüberblick)

| Form | Kapital | Notar | Haftung | Register |
| --- | --- | --- | --- | --- |
| GmbH | 25.000 EUR (§ 5 GmbHG), mind. 12.500 EUR eingezahlt (§ 7 GmbHG) | Gesellschaftsvertrag + Anmeldung | beschränkt | HRB |
| UG (haftungsbeschränkt) | 1 EUR (§ 5a GmbHG), Thesaurierung 25 % bis 25.000 EUR | Gesellschaftsvertrag + Anmeldung | beschränkt | HRB |
| AG | 50.000 EUR (§ 7 AktG) | notariell § 23 AktG | beschränkt | HRB |
| OHG / KG | – | nur Anmeldung beglaubigt § 12 HGB | unbeschränkt (Komplementär) / beschränkt (Kommanditist) | HRA |
| GmbH&Co.KG | + GmbH-Stammkapital | ja (GmbH-Teil) | KG-Komplementär ist haftungsbeschränkte GmbH | HRA + HRB |
| PartG mbB | – | nur Anmeldung beglaubigt § 4 PartGG | berufsspezifisch beschränkt § 8 Abs. 4 PartGG | Partnerschaftsregister |
| GbR / eGbR | – | eGbR-Eintragung freiwillig § 707 BGB n.F. seit MoPeG 1.1.2024 | unbeschränkt | Gesellschaftsregister |
| gGmbH | wie GmbH | wie GmbH | wie GmbH | HRB + Gemeinnützigkeit FA |

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsformwahl prüfen:** Haftungsbedarf (beschränkt vs. unbeschränkt), Kapitalverfügbarkeit, Steuerstruktur (Körperschaft- vs. Einkommensteuer-Transparenz), Mitarbeiterzahl/Mitbestimmung, Investorenrunden, Exit-Optionen.
3. **Registerweg planen:** GmbH/AG: Notar → HRB-Anmeldung Amtsgericht; UG: Musterprotokoll § 2 Abs. 1a GmbHG möglich, beschleunigt aber begrenzt; OHG/KG: HRA; GbR: seit MoPeG eGbR möglich (Voraussetzung für GbR-Erwerb von Grundstücken/GmbH-Anteilen § 707a BGB n.F.).
4. **Begleitende Behörden:** Gewerbeanmeldung Gewerbeamt (§ 14 GewO), Finanzamt (Steuernummer, USt-ID, Anmeldung Körperschaft-/Gewerbesteuer), Transparenzregister (§ 19 GwG, Eintragung wirtschaftlich Berechtigte), IHK/HwK-Pflichtmitgliedschaft.
5. **Anschluss:** Anschluss-Skill `spezial-gmbh-fristen-form-und-zustaendigkeit` (GmbH-spezifisch), `gesellschaftsgruender-kg-und-gmbhcokg` (Personengesellschaft), `gesellschaftsgruender-transparenzregister` (GwG-Eintragung).

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
