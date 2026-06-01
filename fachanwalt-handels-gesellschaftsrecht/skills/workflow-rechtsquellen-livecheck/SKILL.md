---
name: workflow-rechtsquellen-livecheck
description: "Rechtsquellen-Livecheck im Plugin fachanwalt-handels-gesellschaftsrecht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen."
---

# Rechtsquellen-Livecheck

## Aufgabe
Dieser Workflow-Skill für `fachanwalt-handels-gesellschaftsrecht` Rechtsquellen-Livecheck im Plugin fachanwalt-handels-gesellschaftsrecht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Pflicht-Quellenregister Handels-/Gesellschaftsrecht

| Quellenart | Wo prüfen | Hinweis |
| --- | --- | --- |
| HGB, GmbHG, AktG, UmwG, PartGG, MoPeG | gesetze-im-internet.de | aktuelle Fassung mit Änderungsstand |
| BGB | gesetze-im-internet.de | inkl. § 705 ff. nach MoPeG (seit 01.01.2024) |
| Handelsregister | handelsregister.de (Bundeszentralregister) | Auszug, Gesellschafterliste, Satzung, Jahresabschluss |
| Unternehmensregister | unternehmensregister.de | Konzernabschlüsse, Verschmelzungsdaten |
| Transparenzregister | transparenzregister.de | wirtschaftlich Berechtigte |
| Rechtsprechung BGH | bundesgerichtshof.de Datenbank | Volltextzugriff |
| Rechtsprechung OLG/LG | freie Sammlungen openjur.de, dejure.org | nur frei verifizierbare Aktenzeichen |
| EU-Recht | eur-lex.europa.eu | EuGH-Urteile, Richtlinien (UmwandlungsRL 2019/2121, Gesellschaftsrechts-RL 2017/1132) |
| BaFin-Verlautbarungen | bafin.de | Mar, MaRisk, Sanktionen |
| FinanzAmt-Erlasse | bundesfinanzministerium.de | BMF-Schreiben (UmwStG, KStG) |
| GWB / Bundeskartellamt | bundeskartellamt.de | Fusionskontrolle |
| AWV / BMWK | bmwk.de | Investitionsprüfung Sektorale/Sektorenübergreifende Anzeige |

## Workflow-Schritte für Live-Quellencheck

1. **Norm identifizieren:** Welche Vorschrift ist tragend für die Aussage?
2. **Gesetzesstand prüfen:** Aktuelle Fassung mit Inkrafttretensdatum (gesetze-im-internet.de zeigt Stand).
3. **Verordnungen / Begleitrecht:** zusätzliche Rechtsverordnungen, Anlagen (z.B. KV bei GKG).
4. **Rechtsprechung verifizieren:** mindestens einen verifizierten Volltext oder offizielle Pressemitteilung mit Aktenzeichen, Datum, Gericht.
5. **EU-Bezug prüfen:** Welche EuGH-Urteile zur unionsrechtskonformen Auslegung?
6. **Datum dokumentieren:** Stand der Recherche im Output ("Stand: TT.MM.JJJJ").
7. **Unsicherheiten markieren:** Wenn live nicht prüfbar, klar als "(noch zu verifizieren)" markieren.

## Typische Aktualitäts-Fallen

- **MoPeG (Modernisierung Personengesellschaftsrecht):** seit 01.01.2024 völlig neue GbR-Regelungen, eGbR im Gesellschaftsregister; alte Kommentar-Stellen veraltet.
- **DiRUG (Digitalisierungsrichtlinie):** seit 01.08.2022 Online-Gründung GmbH § 2 Abs. 3 GmbHG; Schritt-für-Schritt-Anleitung BNotK.
- **UmwG-Novelle 2023:** Umsetzung Richtlinie 2019/2121, Grenzüberschreitende Umwandlung neu in §§ 305 ff. UmwG.
- **Transparenzregister:** seit 01.08.2021 Vollregister statt Auffangregister; jährliche Meldepflichten.
- **Justizstandort-Stärkungsgesetz:** Schwellen § 23 GVG (2026 bis 10.000 EUR), § 511 ZPO (1.000 EUR), § 495a ZPO (1.000 EUR), § 119b GVG Commercial Court.

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
