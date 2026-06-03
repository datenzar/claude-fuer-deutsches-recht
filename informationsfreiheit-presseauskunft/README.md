# Informationsfreiheit und Presseauskunft

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`informationsfreiheit-presseauskunft`) | [`informationsfreiheit-presseauskunft.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/informationsfreiheit-presseauskunft.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **IFG-/Presseauskunftsakte Hafenstadt** (`informationsfreiheit-presseauskunft-klinikdaten-hafenstadt`) | [Gesamt-PDF lesen](../testakten/informationsfreiheit-presseauskunft-klinikdaten-hafenstadt/gesamt-pdf/informationsfreiheit-presseauskunft-klinikdaten-hafenstadt_gesamt.pdf) | [`testakte-informationsfreiheit-presseauskunft-klinikdaten-hafenstadt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-informationsfreiheit-presseauskunft-klinikdaten-hafenstadt.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin ist das Cockpit für Menschen, Journalistinnen, Kanzleien, NGOs und Unternehmen, die amtliche Informationen bekommen wollen, ohne an Zuständigkeitsnebel, Gebührenbescheiden oder Ausweichantworten hängen zu bleiben.

## Start

Beginne mit `allgemein`. Das Plugin fragt zuerst nach Rolle, Ziel, Frist, Behörde/Gericht/Register, vorhandenen Unterlagen und gewünschtem Output. Danach schlägt es die passenden Spezialskills aus diesem Plugin vor.

## Arbeitsweise

- Es arbeitet mit Akten- und Fristenlogik statt mit Bauchgefühl.
- Es trennt Rechtsgrundlage, Verfahren, Beweis, Kosten, Kommunikation und Eskalation.
- Es soll Nutzerinnen und Nutzer befähigen: verständliche Erklärung, präzise Rückfragen, dann belastbarer Entwurf.
- Rechtsprechung und Gesetzesstände werden nicht halluziniert, sondern als Live-Check über amtliche oder frei zugängliche Quellen markiert.

## Typische Outputs

- Kaltstart-Interview und Aktenlandkarte
- Behörden-, Gerichts- oder Gegneranschreiben
- Widerspruchs-/Klage-/Eilantragsbausteine
- Kosten-, Fristen- und Zuständigkeitsmatrix
- Dashboard/Tracker für laufende Vorgänge
- Kurzfassung für Mandant, Vorstand, Verband, Redaktion oder Bürgerin

## Quellenhygiene

Siehe [`references/QUELLEN.md`](./references/QUELLEN.md). Dieses Plugin gibt keine endgültige Rechtsberatung, sondern robuste Arbeitsfassungen, Prüfpfade und Dokumentationshilfen.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 100 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Informationsfreiheit und Presseauskunft: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Spezialskill-Routing und erste Ausgabe. |
| `ifg-001-kaltstart-informationsbegehren-sortier` | Informationsfreiheit und Presseauskunft: Kaltstart Informationsbegehren sortieren. Kaltstart Informationsbegehren sortieren im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und A... |
| `ifg-002-ifg-oder-presseauskunft-richtig-routen` | Informationsfreiheit und Presseauskunft: IFG oder Presseauskunft richtig routen. IFG oder Presseauskunft richtig routen im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausga... |
| `ifg-003-bundesbehoerde-oder-landesbehoerde-erk` | Informationsfreiheit und Presseauskunft: Bundesbehörde oder Landesbehörde erkennen. Bundesbehörde oder Landesbehörde erkennen im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und... |
| `ifg-004-kein-ifg-im-land-ersatzwege-finden` | Informationsfreiheit und Presseauskunft: Kein IFG im Land: Ersatzwege finden. Kein IFG im Land: Ersatzwege finden im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeform... |
| `ifg-005-kostenrisiko-und-gebuehrenankuendigung` | Informationsfreiheit und Presseauskunft: Kostenrisiko und Gebührenankündigung prüfen. Kostenrisiko und Gebührenankündigung prüfen im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik... |
| `ifg-006-fristenkalender-und-untaetigkeitstrack` | Informationsfreiheit und Presseauskunft: Fristenkalender und Untätigkeitstracker. Fristenkalender und Untätigkeitstracker im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Aus... |
| `ifg-007-drittbeteiligung-bei-betriebsgeheimnis` | Informationsfreiheit und Presseauskunft: Drittbeteiligung bei Betriebsgeheimnissen. Drittbeteiligung bei Betriebsgeheimnissen im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und... |
| `ifg-008-personenbezogene-daten-und-schwaerzung` | Informationsfreiheit und Presseauskunft: Personenbezogene Daten und Schwärzung. Personenbezogene Daten und Schwärzung im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabe... |
| `ifg-009-uig-und-umweltinformationen-abgrenzen` | Informationsfreiheit und Presseauskunft: UIG und Umweltinformationen abgrenzen. UIG und Umweltinformationen abgrenzen im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabe... |
| `ifg-010-vig-und-verbraucherinformationen-nutze` | Informationsfreiheit und Presseauskunft: VIG und Verbraucherinformationen nutzen. VIG und Verbraucherinformationen nutzen im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Aus... |
| `ifg-011-akteneinsicht-oder-auskunft-oder-kopie` | Informationsfreiheit und Presseauskunft: Akteneinsicht oder Auskunft oder Kopie. Akteneinsicht oder Auskunft oder Kopie im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausga... |
| `ifg-012-presseanfrage-schnell-und-knapp-formul` | Informationsfreiheit und Presseauskunft: Presseanfrage schnell und knapp formulieren. Presseanfrage schnell und knapp formulieren im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik... |
| `ifg-013-ablehnungsbescheid-in-angriffspunkte-z` | Informationsfreiheit und Presseauskunft: Ablehnungsbescheid in Angriffspunkte zerlegen. Ablehnungsbescheid in Angriffspunkte zerlegen im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenl... |
| `ifg-014-widerspruch-gegen-ifg-ablehnung` | Informationsfreiheit und Presseauskunft: Widerspruch gegen IFG-Ablehnung. Widerspruch gegen IFG-Ablehnung im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearb... |
| `ifg-015-verpflichtungsklage-und-eilrechtsschut` | Informationsfreiheit und Presseauskunft: Verpflichtungsklage und Eilrechtsschutz. Verpflichtungsklage und Eilrechtsschutz im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Aus... |
| `ifg-016-gebuehrenbescheid-angreifen` | Informationsfreiheit und Presseauskunft: Gebührenbescheid angreifen. Gebührenbescheid angreifen im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |
| `ifg-017-informationszugang-bei-beliehenen-priv` | Informationsfreiheit und Presseauskunft: Informationszugang bei beliehenen Privaten. Informationszugang bei beliehenen Privaten im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik u... |
| `ifg-018-parlaments-und-rechnungshofgrenzen` | Informationsfreiheit und Presseauskunft: Parlaments- und Rechnungshofgrenzen. Parlaments- und Rechnungshofgrenzen im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeform... |
| `ifg-019-sicherheitsinteressen-und-geheimschutz` | Informationsfreiheit und Presseauskunft: Sicherheitsinteressen und Geheimschutz. Sicherheitsinteressen und Geheimschutz im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausga... |
| `ifg-020-veroeffentlichung-erhaltene-dokumente` | Informationsfreiheit und Presseauskunft: Veröffentlichung erhaltene Dokumente prüfen. Veröffentlichung erhaltene Dokumente prüfen im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik... |
| `ifg-021-informationszugang-baden-wuerttemberg` | Informationsfreiheit und Presseauskunft: Informationszugang Baden-Württemberg Livecheck. Informationszugang Baden-Württemberg Livecheck im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumente... |
| `ifg-022-informationszugang-bayern-livecheck` | Informationsfreiheit und Presseauskunft: Informationszugang Bayern Livecheck. Informationszugang Bayern Livecheck im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeform... |
| `ifg-023-informationszugang-berlin-livecheck` | Informationsfreiheit und Presseauskunft: Informationszugang Berlin Livecheck. Informationszugang Berlin Livecheck im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeform... |
| `ifg-024-informationszugang-brandenburg-liveche` | Informationsfreiheit und Presseauskunft: Informationszugang Brandenburg Livecheck. Informationszugang Brandenburg Livecheck im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und A... |
| `ifg-025-informationszugang-bremen-livecheck` | Informationsfreiheit und Presseauskunft: Informationszugang Bremen Livecheck. Informationszugang Bremen Livecheck im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeform... |
| `ifg-026-informationszugang-hamburg-livecheck` | Informationsfreiheit und Presseauskunft: Informationszugang Hamburg Livecheck. Informationszugang Hamburg Livecheck im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabefo... |
| `ifg-027-informationszugang-hessen-livecheck` | Informationsfreiheit und Presseauskunft: Informationszugang Hessen Livecheck. Informationszugang Hessen Livecheck im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeform... |
| `ifg-028-informationszugang-mecklenburg-vorpomm` | Informationsfreiheit und Presseauskunft: Informationszugang Mecklenburg-Vorpommern Livecheck. Informationszugang Mecklenburg-Vorpommern Livecheck im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen,... |
| `ifg-029-informationszugang-niedersachsen-livec` | Informationsfreiheit und Presseauskunft: Informationszugang Niedersachsen Livecheck. Informationszugang Niedersachsen Livecheck im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik u... |
| `ifg-030-informationszugang-nordrhein-westfalen` | Informationsfreiheit und Presseauskunft: Informationszugang Nordrhein-Westfalen Livecheck. Informationszugang Nordrhein-Westfalen Livecheck im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokum... |
| `ifg-031-informationszugang-rheinland-pfalz-liv` | Informationsfreiheit und Presseauskunft: Informationszugang Rheinland-Pfalz Livecheck. Informationszugang Rheinland-Pfalz Livecheck im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlog... |
| `ifg-032-informationszugang-saarland-livecheck` | Informationsfreiheit und Presseauskunft: Informationszugang Saarland Livecheck. Informationszugang Saarland Livecheck im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabe... |
| `ifg-033-informationszugang-sachsen-livecheck` | Informationsfreiheit und Presseauskunft: Informationszugang Sachsen Livecheck. Informationszugang Sachsen Livecheck im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabefo... |
| `ifg-034-informationszugang-sachsen-anhalt-live` | Informationsfreiheit und Presseauskunft: Informationszugang Sachsen-Anhalt Livecheck. Informationszugang Sachsen-Anhalt Livecheck im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik... |
| `ifg-035-informationszugang-schleswig-holstein` | Informationsfreiheit und Presseauskunft: Informationszugang Schleswig-Holstein Livecheck. Informationszugang Schleswig-Holstein Livecheck im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumen... |
| `ifg-036-informationszugang-thueringen-livechec` | Informationsfreiheit und Presseauskunft: Informationszugang Thüringen Livecheck. Informationszugang Thüringen Livecheck im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausga... |
| `ifg-037-ifg-bund-antrag-formulieren` | Informationsfreiheit und Presseauskunft: IFG Bund: Antrag formulieren. Antrag formulieren für IFG Bund im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `ifg-038-ifg-bund-zustaendigkeit-pruefen` | Informationsfreiheit und Presseauskunft: IFG Bund: Zuständigkeit prüfen. Zuständigkeit prüfen für IFG Bund im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `ifg-039-ifg-bund-frist-setzen` | Informationsfreiheit und Presseauskunft: IFG Bund: Frist setzen. Frist setzen für IFG Bund im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `ifg-040-ifg-bund-kosten-deckeln` | Informationsfreiheit und Presseauskunft: IFG Bund: Kosten deckeln. Kosten deckeln für IFG Bund im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `ifg-041-ifg-bund-schwaerzung-angreifen` | Informationsfreiheit und Presseauskunft: IFG Bund: Schwärzung angreifen. Schwärzung angreifen für IFG Bund im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `ifg-042-ifg-bund-drittanhoerung-begleiten` | Informationsfreiheit und Presseauskunft: IFG Bund: Drittanhörung begleiten. Drittanhörung begleiten für IFG Bund im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt... |
| `ifg-043-ifg-bund-widerspruch-bauen` | Informationsfreiheit und Presseauskunft: IFG Bund: Widerspruch bauen. Widerspruch bauen für IFG Bund im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `ifg-044-ifg-bund-klage-vorbereiten` | Informationsfreiheit und Presseauskunft: IFG Bund: Klage vorbereiten. Klage vorbereiten für IFG Bund im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `ifg-045-ifg-bund-presseantwort-nachfassen` | Informationsfreiheit und Presseauskunft: IFG Bund: Presseantwort nachfassen. Presseantwort nachfassen für IFG Bund im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schri... |
| `ifg-046-ifg-bund-tracking-aktualisieren` | Informationsfreiheit und Presseauskunft: IFG Bund: Tracking aktualisieren. Tracking aktualisieren für IFG Bund im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt t... |
| `ifg-047-ifggebv-gebuehren-antrag-formulieren` | Informationsfreiheit und Presseauskunft: IFGGebV Gebühren: Antrag formulieren. Antrag formulieren für IFGGebV Gebühren im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten S... |
| `ifg-048-ifggebv-gebuehren-zustaendigkeit-pruef` | Informationsfreiheit und Presseauskunft: IFGGebV Gebühren: Zuständigkeit prüfen. Zuständigkeit prüfen für IFGGebV Gebühren im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächst... |
| `ifg-049-ifggebv-gebuehren-frist-setzen` | Informationsfreiheit und Presseauskunft: IFGGebV Gebühren: Frist setzen. Frist setzen für IFGGebV Gebühren im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |
| `ifg-050-ifggebv-gebuehren-kosten-deckeln` | Informationsfreiheit und Presseauskunft: IFGGebV Gebühren: Kosten deckeln. Kosten deckeln für IFGGebV Gebühren im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt t... |
| `ifg-051-ifggebv-gebuehren-schwaerzung-angreife` | Informationsfreiheit und Presseauskunft: IFGGebV Gebühren: Schwärzung angreifen. Schwärzung angreifen für IFGGebV Gebühren im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächst... |
| `ifg-052-ifggebv-gebuehren-drittanhoerung-begle` | Informationsfreiheit und Presseauskunft: IFGGebV Gebühren: Drittanhörung begleiten. Drittanhörung begleiten für IFGGebV Gebühren im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und... |
| `ifg-053-ifggebv-gebuehren-widerspruch-bauen` | Informationsfreiheit und Presseauskunft: IFGGebV Gebühren: Widerspruch bauen. Widerspruch bauen für IFGGebV Gebühren im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Sch... |
| `ifg-054-ifggebv-gebuehren-klage-vorbereiten` | Informationsfreiheit und Presseauskunft: IFGGebV Gebühren: Klage vorbereiten. Klage vorbereiten für IFGGebV Gebühren im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Sch... |
| `ifg-055-ifggebv-gebuehren-presseantwort-nachfa` | Informationsfreiheit und Presseauskunft: IFGGebV Gebühren: Presseantwort nachfassen. Presseantwort nachfassen für IFGGebV Gebühren im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko un... |
| `ifg-056-ifggebv-gebuehren-tracking-aktualisier` | Informationsfreiheit und Presseauskunft: IFGGebV Gebühren: Tracking aktualisieren. Tracking aktualisieren für IFGGebV Gebühren im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nä... |
| `ifg-057-uig-umweltinformation-antrag-formulier` | Informationsfreiheit und Presseauskunft: UIG Umweltinformation: Antrag formulieren. Antrag formulieren für UIG Umweltinformation im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und... |
| `ifg-058-uig-umweltinformation-zustaendigkeit-p` | Informationsfreiheit und Presseauskunft: UIG Umweltinformation: Zuständigkeit prüfen. Zuständigkeit prüfen für UIG Umweltinformation im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko... |
| `ifg-059-uig-umweltinformation-frist-setzen` | Informationsfreiheit und Presseauskunft: UIG Umweltinformation: Frist setzen. Frist setzen für UIG Umweltinformation im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Sch... |
| `ifg-060-uig-umweltinformation-kosten-deckeln` | Informationsfreiheit und Presseauskunft: UIG Umweltinformation: Kosten deckeln. Kosten deckeln für UIG Umweltinformation im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten... |
| `ifg-061-uig-umweltinformation-schwaerzung-angr` | Informationsfreiheit und Presseauskunft: UIG Umweltinformation: Schwärzung angreifen. Schwärzung angreifen für UIG Umweltinformation im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko... |
| `ifg-062-uig-umweltinformation-drittanhoerung-b` | Informationsfreiheit und Presseauskunft: UIG Umweltinformation: Drittanhörung begleiten. Drittanhörung begleiten für UIG Umweltinformation im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, R... |
| `ifg-063-uig-umweltinformation-widerspruch-baue` | Informationsfreiheit und Presseauskunft: UIG Umweltinformation: Widerspruch bauen. Widerspruch bauen für UIG Umweltinformation im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nä... |
| `ifg-064-uig-umweltinformation-klage-vorbereite` | Informationsfreiheit und Presseauskunft: UIG Umweltinformation: Klage vorbereiten. Klage vorbereiten für UIG Umweltinformation im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nä... |
| `ifg-065-uig-umweltinformation-presseantwort-na` | Informationsfreiheit und Presseauskunft: UIG Umweltinformation: Presseantwort nachfassen. Presseantwort nachfassen für UIG Umweltinformation im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege,... |
| `ifg-066-uig-umweltinformation-tracking-aktuali` | Informationsfreiheit und Presseauskunft: UIG Umweltinformation: Tracking aktualisieren. Tracking aktualisieren für UIG Umweltinformation im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Ris... |
| `ifg-067-vig-lebensmittel-und-produkte-antrag-f` | Informationsfreiheit und Presseauskunft: VIG Lebensmittel und Produkte: Antrag formulieren. Antrag formulieren für VIG Lebensmittel und Produkte im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Bel... |
| `ifg-068-vig-lebensmittel-und-produkte-zustaend` | Informationsfreiheit und Presseauskunft: VIG Lebensmittel und Produkte: Zuständigkeit prüfen. Zuständigkeit prüfen für VIG Lebensmittel und Produkte im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist,... |
| `ifg-069-vig-lebensmittel-und-produkte-frist-se` | Informationsfreiheit und Presseauskunft: VIG Lebensmittel und Produkte: Frist setzen. Frist setzen für VIG Lebensmittel und Produkte im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko... |
| `ifg-070-vig-lebensmittel-und-produkte-kosten-d` | Informationsfreiheit und Presseauskunft: VIG Lebensmittel und Produkte: Kosten deckeln. Kosten deckeln für VIG Lebensmittel und Produkte im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Ris... |
| `ifg-071-vig-lebensmittel-und-produkte-schwaerz` | Informationsfreiheit und Presseauskunft: VIG Lebensmittel und Produkte: Schwärzung angreifen. Schwärzung angreifen für VIG Lebensmittel und Produkte im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist,... |
| `ifg-072-vig-lebensmittel-und-produkte-drittanh` | Informationsfreiheit und Presseauskunft: VIG Lebensmittel und Produkte: Drittanhörung begleiten. Drittanhörung begleiten für VIG Lebensmittel und Produkte im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand,... |
| `ifg-073-vig-lebensmittel-und-produkte-widerspr` | Informationsfreiheit und Presseauskunft: VIG Lebensmittel und Produkte: Widerspruch bauen. Widerspruch bauen für VIG Lebensmittel und Produkte im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Beleg... |
| `ifg-074-vig-lebensmittel-und-produkte-klage-vo` | Informationsfreiheit und Presseauskunft: VIG Lebensmittel und Produkte: Klage vorbereiten. Klage vorbereiten für VIG Lebensmittel und Produkte im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Beleg... |
| `ifg-075-vig-lebensmittel-und-produkte-pressean` | Informationsfreiheit und Presseauskunft: VIG Lebensmittel und Produkte: Presseantwort nachfassen. Presseantwort nachfassen für VIG Lebensmittel und Produkte im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand... |
| `ifg-076-vig-lebensmittel-und-produkte-tracking` | Informationsfreiheit und Presseauskunft: VIG Lebensmittel und Produkte: Tracking aktualisieren. Tracking aktualisieren für VIG Lebensmittel und Produkte im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Fr... |
| `ifg-077-landespressegesetz-antrag-formulieren` | Informationsfreiheit und Presseauskunft: Landespressegesetz: Antrag formulieren. Antrag formulieren für Landespressegesetz im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächst... |
| `ifg-078-landespressegesetz-zustaendigkeit-prue` | Informationsfreiheit und Presseauskunft: Landespressegesetz: Zuständigkeit prüfen. Zuständigkeit prüfen für Landespressegesetz im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nä... |
| `ifg-079-landespressegesetz-frist-setzen` | Informationsfreiheit und Presseauskunft: Landespressegesetz: Frist setzen. Frist setzen für Landespressegesetz im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt t... |
| `ifg-080-landespressegesetz-kosten-deckeln` | Informationsfreiheit und Presseauskunft: Landespressegesetz: Kosten deckeln. Kosten deckeln für Landespressegesetz im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schri... |
| `ifg-081-landespressegesetz-schwaerzung-angreif` | Informationsfreiheit und Presseauskunft: Landespressegesetz: Schwärzung angreifen. Schwärzung angreifen für Landespressegesetz im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nä... |
| `ifg-082-landespressegesetz-drittanhoerung-begl` | Informationsfreiheit und Presseauskunft: Landespressegesetz: Drittanhörung begleiten. Drittanhörung begleiten für Landespressegesetz im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko... |
| `ifg-083-landespressegesetz-widerspruch-bauen` | Informationsfreiheit und Presseauskunft: Landespressegesetz: Widerspruch bauen. Widerspruch bauen für Landespressegesetz im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten... |
| `ifg-084-landespressegesetz-klage-vorbereiten` | Informationsfreiheit und Presseauskunft: Landespressegesetz: Klage vorbereiten. Klage vorbereiten für Landespressegesetz im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten... |
| `ifg-085-landespressegesetz-presseantwort-nachf` | Informationsfreiheit und Presseauskunft: Landespressegesetz: Presseantwort nachfassen. Presseantwort nachfassen für Landespressegesetz im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risik... |
| `ifg-086-landespressegesetz-tracking-aktualisie` | Informationsfreiheit und Presseauskunft: Landespressegesetz: Tracking aktualisieren. Tracking aktualisieren für Landespressegesetz im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko un... |
| `ifg-087-transparenzgesetz-antrag-formulieren` | Informationsfreiheit und Presseauskunft: Transparenzgesetz: Antrag formulieren. Antrag formulieren für Transparenzgesetz im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten... |
| `ifg-088-transparenzgesetz-zustaendigkeit-pruef` | Informationsfreiheit und Presseauskunft: Transparenzgesetz: Zuständigkeit prüfen. Zuständigkeit prüfen für Transparenzgesetz im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und näch... |
| `ifg-089-transparenzgesetz-frist-setzen` | Informationsfreiheit und Presseauskunft: Transparenzgesetz: Frist setzen. Frist setzen für Transparenzgesetz im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt tre... |
| `ifg-090-transparenzgesetz-kosten-deckeln` | Informationsfreiheit und Presseauskunft: Transparenzgesetz: Kosten deckeln. Kosten deckeln für Transparenzgesetz im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt... |
| `ifg-091-transparenzgesetz-schwaerzung-angreife` | Informationsfreiheit und Presseauskunft: Transparenzgesetz: Schwärzung angreifen. Schwärzung angreifen für Transparenzgesetz im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und näch... |
| `ifg-092-transparenzgesetz-drittanhoerung-begle` | Informationsfreiheit und Presseauskunft: Transparenzgesetz: Drittanhörung begleiten. Drittanhörung begleiten für Transparenzgesetz im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko un... |
| `ifg-093-transparenzgesetz-widerspruch-bauen` | Informationsfreiheit und Presseauskunft: Transparenzgesetz: Widerspruch bauen. Widerspruch bauen für Transparenzgesetz im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten S... |
| `ifg-094-transparenzgesetz-klage-vorbereiten` | Informationsfreiheit und Presseauskunft: Transparenzgesetz: Klage vorbereiten. Klage vorbereiten für Transparenzgesetz im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten S... |
| `ifg-095-transparenzgesetz-presseantwort-nachfa` | Informationsfreiheit und Presseauskunft: Transparenzgesetz: Presseantwort nachfassen. Presseantwort nachfassen für Transparenzgesetz im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko... |
| `ifg-096-transparenzgesetz-tracking-aktualisier` | Informationsfreiheit und Presseauskunft: Transparenzgesetz: Tracking aktualisieren. Tracking aktualisieren für Transparenzgesetz im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und... |
| `ifg-097-archivrecht-antrag-formulieren` | Informationsfreiheit und Presseauskunft: Archivrecht: Antrag formulieren. Antrag formulieren für Archivrecht im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt tre... |
| `ifg-098-archivrecht-zustaendigkeit-pruefen` | Informationsfreiheit und Presseauskunft: Archivrecht: Zuständigkeit prüfen. Zuständigkeit prüfen für Archivrecht im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt... |
| `ifg-099-archivrecht-frist-setzen` | Informationsfreiheit und Presseauskunft: Archivrecht: Frist setzen. Frist setzen für Archivrecht im Rahmen von Informationsfreiheit und Presseauskunft; Zuständigkeit, Tatbestand, Frist, Belege, Risiko und nächsten Schritt trennen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
