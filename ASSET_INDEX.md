# Release-Asset-Index

Übersicht aller Dateien, die der Release-Workflow (`.github/workflows/release-plugin-zips.yml`) pro Tag-Release `vX.Y.Z` an den GitHub-Release anhängt.

**Stand:** v2.0.4

## Asset-Typen

Jedes Asset hat einen klar definierten Typ. Der Typ steuert, wie es zu verwenden ist.

| Typ          | Erkennungsmerkmal             | Verwendung                                                                                  |
| ------------ | ----------------------------- | ------------------------------------------------------------------------------------------- |
| **plugin**   | `<plugin-name>.zip`           | Über „Customize Plugins → Install from .zip" in Claude Code/Cowork hochladen.               |
| **fallakte** | `testakte-<aktenname>.zip`    | **Kein Plugin.** Mandatsunterlagen für Testzwecke. In den Chat ziehen, nicht zum Plugin-Upload geben. |
| **manifest** | `marketplace.json`            | **Kein Plugin.** Marketplace-Manifest. Für `/plugin marketplace add` via Filesystem oder zur manuellen Inspektion. |

## Plugin-Assets (52 Stück)

Alphabetisch wie in `marketplace.json`. URL-Schema:
`https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/<name>.zip`

| Plugin                                       | Kurzbeschreibung                                                                       |
| -------------------------------------------- | -------------------------------------------------------------------------------------- |
| `aktenaufbereiter-strafrecht`                | Strukturierung großer Strafakten                                                       |
| `anlagen-zu-schriftsaetzen`                  | Anlagen-Sortierung für gerichtliche Schriftsätze                                       |
| `arbeitsrecht`                               | Kündigung, KSchG-Klage, Aufhebungsvertrag, Abmahnung, BR-Anhörung                       |
| `berufsrecht-ki-vertragspruefung`            | Berufsrechtliche Vorprüfung von Verträgen mit Legal-Tech-Anbietern                     |
| `betreuungsrecht`                            | Berufsbetreuer-Skills nach BtOG, §§ 1814 ff. BGB                                       |
| `datenschutzrecht`                           | DSGVO/BDSG/TTDSG, DPIA, AVV-Review, Datenpannenmeldung                                 |
| `fachanwalt-agrarrecht`                      | Light-Touch: HöfeO, Anerbenrecht, Pachtrecht                                           |
| `fachanwalt-bank-kapitalmarktrecht`          | Light-Touch: KWG, ZAG, WpHG, Bankvertragsrecht                                         |
| `fachanwalt-bau-architektenrecht`            | Light-Touch: BGB Werkvertrag, VOB/B, HOAI                                              |
| `fachanwalt-erbrecht`                        | Light-Touch: BGB Erbrecht §§ 1922 ff.                                                   |
| `fachanwalt-familienrecht`                   | Light-Touch: BGB Familienrecht, FamFG                                                  |
| `fachanwalt-internationales-wirtschaftsrecht`| Light-Touch: IPR, IZVR, Schiedsrecht                                                   |
| `fachanwalt-it-recht`                        | Light-Touch: Softwarerecht, IT-Vertragsrecht, Cloud                                    |
| `fachanwalt-medizinrecht`                    | Light-Touch: Arzthaftung §§ 630a ff. BGB                                               |
| `fachanwalt-migrationsrecht`                 | Light-Touch: AufenthG, AsylG, FreizügG/EU                                              |
| `fachanwalt-sportrecht`                      | Light-Touch: Verbandsrecht                                                             |
| `fachanwalt-strafrecht`                      | Light-Touch: StGB, StPO, Notfristen                                                    |
| `fachanwalt-transport-speditionsrecht`       | Light-Touch: HGB Transport, CMR                                                        |
| `fachanwalt-urheber-medienrecht`             | Light-Touch: UrhG, Verlagsrecht, Filmrecht                                             |
| `fachanwalt-vergaberecht`                    | Light-Touch: GWB §§ 97 ff., VgV                                                        |
| `fachanwalt-verkehrsrecht`                   | Light-Touch: StVG, StVO, PflVG                                                         |
| `fachanwalt-versicherungsrecht`              | Light-Touch: VVG, VAG                                                                  |
| `fachanwalt-verwaltungsrecht`                | Light-Touch: VwGO, VwVfG                                                               |
| `fluggastrechte`                             | VO (EG) 261/2004 plus EuGH-Rspr., Ticketprüfung, Pauschalklage                          |
| `forderungsmanagement-klagewerkstatt`        | Generalisierter Klage-Assistent mit eigenem Plugin-Pattern                             |
| `fortbestehensprognose`                      | Fortbestehensprognose § 19 II InsO als GF-Selbstdokumentation                          |
| `gesellschaftsrecht`                         | M&A-DD, Gesellschafterbeschlüsse, HRB-Anmeldung                                        |
| `gewerblicher-rechtsschutz`                  | DPMA/EUIPO, FTO, UWG-Abmahnung, Urheberrecht                                           |
| `immobilienrechtspraxis`                     | Vertragserstellung, Bauträger, WEG, Maklerrecht                                        |
| `insolvenzrecht`                             | §§ 17, 19 InsO, § 15a InsO, BGH-Volltexte                                              |
| `jurastudium`                                | Karteikarten, Gutachten-Coaching, Examensvorbereitung                                  |
| `kanzlei-builder-hub`                        | Community-Skills finden, prüfen, installieren                                          |
| `kanzlei-cowork`                             | Fristenbuch, Timesheet, Rechnung, Mandantenakte                                        |
| `ki-governance`                              | EU-KI-VO + DSGVO, KI-Inventar, Vendor-Review                                           |
| `liquiditaetsplanung`                        | 3-Wochen-Vorschau, 13/26/52-Wochen-Planung, BGH-Schema Passiva II                      |
| `memorandums-ersteller`                      | Mandantenunterlagen → juristisches Memorandum                                          |
| `methodenlehre-deutsches-recht`              | Gutachten- vor Urteilsstil                                                             |
| `mietrecht`                                  | Mietspiegel-Quellen, Mieterhöhung, Eigenbedarf                                         |
| `nda-abgleich`                               | NDA-Review aus Empfängersicht                                                          |
| `patentrecherche`                            | Espacenet, Google Patents, DPMAregister                                                |
| `produktrecht`                               | Launch-Review, Impressum, PAngV, Marketing-Claims                                      |
| `prozessrecht`                               | Mahnbescheid, einstweilige Verfügung, Schutzschrift, Zwangsvollstreckung               |
| `rechtsberatungsstelle`                      | Pro-Bono/RDG-konform, Intake, Fristen                                                  |
| `regulatorisches-recht`                      | KWG, ZAG, WpHG, GwG, EnWG, TKG                                                         |
| `sozialrecht-kanzlei`                        | Bescheidanalyse, Widerspruch, Klage SGB                                                |
| `steuerberater-werkzeuge`                    | BWA-/SuSa-/Bilanzprüfung, Krisenfrüherkennung                                          |
| `steuerrecht-kanzlei`                        | Bescheidanalyse, Einspruch, Klage FG/BFH                                               |
| `tabellenreview-3d`                          | 3D-Tabellenreview-Würfel                                                               |
| `verfassungsrecht`                           | Verfassungsbeschwerde, GG-Auslegung, BVerfG-Verfahren                                  |
| `verlagsredaktion`                           | Redaktioneller Assistent für juristische Publikationen                                 |
| `vertragsrecht`                              | NDA, AGB, SaaS, Lieferantenverträge                                                    |
| `verwaltete-agentenrezepte`                  | Kuratierte Workflow-Rezepte zum Wiederverwenden                                        |
| `zitierweise-deutsches-recht`                | Deutsche Hauszitierweise                                                               |

## Fallakten-Assets (5 Stück)

URL-Schema: `https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/<asset>.zip`

**Wichtig:** Diese ZIPs sind **keine Plugins**. Sie enthalten Mandatsunterlagen für Testzwecke und gehören in den Chat (als Anhang/Drag-and-drop), nicht in den Plugin-Upload-Dialog.

| Asset                                                      | Passt zu Plugin                                                                            |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `testakte-beispielakte-edelholz-berlin.zip`                | `liquiditaetsplanung` + `insolvenzrecht` + `steuerberater-werkzeuge` + `fortbestehensprognose` |
| `testakte-betreuung-hildegard-sauer.zip`                   | `betreuungsrecht`                                                                          |
| `testakte-fluggastrechte-familie-braeutigam.zip`           | `fluggastrechte`                                                                           |
| `testakte-fortbestehensprognose-paragrafix-gmbh.zip`       | `fortbestehensprognose` + `insolvenzrecht`                                                 |
| `testakte-sozialrecht-rollstuhl-tannenberg.zip`            | `sozialrecht-kanzlei`                                                                      |

## Manifest-Asset (1 Stück)

| Asset              | Verwendung                                                                                                                                                |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `marketplace.json` | Marketplace-Manifest mit Plugin-Liste + Beschreibungen. **Kein Plugin.** Für `curl`-Download durch Skripte und zur manuellen Inspektion der Plugin-Liste. |

## Asset-Anzahl pro Release

| Typ          | Anzahl | Summe |
| ------------ | ------ | ----- |
| plugin       | 52     |       |
| fallakte     | 5      |       |
| manifest     | 1      |       |
| **gesamt**   |        | **58** |

## Verifikation eines Release

```bash
curl -s "https://api.github.com/repos/Klotzkette/claude-fuer-deutsches-recht/releases/latest" \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print('Tag:', d['tag_name']); print('Assets:', len(d['assets'])); [print(' -', a['name']) for a in d['assets']]"
```

Erwartet: 58 Assets, davon 52 Plugin-ZIPs, 5 Fallakten-ZIPs mit `testakte-`-Prefix, eine `marketplace.json`.
