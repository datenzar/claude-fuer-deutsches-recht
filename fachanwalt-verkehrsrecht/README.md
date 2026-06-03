# Fachanwalt Verkehrsrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fachanwalt-verkehrsrecht`) | [`fachanwalt-verkehrsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-verkehrsrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **StVO-Akte Schulstraße/Lieferzone** (`strassenverkehrsrecht-stvo-schulstrasse-lieferzone`) | [Gesamt-PDF lesen](../testakten/strassenverkehrsrecht-stvo-schulstrasse-lieferzone/gesamt-pdf/strassenverkehrsrecht-stvo-schulstrasse-lieferzone_gesamt.pdf) | [`testakte-strassenverkehrsrecht-stvo-schulstrasse-lieferzone.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strassenverkehrsrecht-stvo-schulstrasse-lieferzone.zip) |
| **Verkehrsunfall Tannenbruck — A45 Quotenstreit, OWi, Fahrerlaubnis-Entzug, MPU** (`verkehrsunfall-quotenstreit-tannenbruck-a45`) | [Gesamt-PDF lesen](../testakten/verkehrsunfall-quotenstreit-tannenbruck-a45/gesamt-pdf/verkehrsunfall-quotenstreit-tannenbruck-a45_gesamt.pdf) | [`testakte-verkehrsunfall-quotenstreit-tannenbruck-a45.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehrsunfall-quotenstreit-tannenbruck-a45.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Plugin Fachanwalt für Verkehrsrecht. Orientierung StVG StVO PflVG VVG-Bezüge. Verkehrsunfall Personenschaden Sachschaden Bußgeld Fahrerlaubnis OWi-Verfahren Verkehrsstrafrecht (§§ 315c 316 StGB). Schnittstellen zu Versicherungs- und Strafrecht.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `fachanwalt-verkehrsrecht-orientierung` | Orientierung im Verkehrsrecht — FAO Voraussetzungen Normen typische Mandate Fristen Quellenprüfung. Verkehrsunfall mit Personen- und Sachschaden Schadensregulierung Versicherung Haftpflicht Kasko Bußgeld Fahrerlau… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Fachanwalt Verkehrsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeit... |
| `bussgeld-einspruch-pruefen` | Workflow-Skill zu bussgeld einspruch pruefen. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht): Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen. |
| `fachanwalt-verkehr-autonom-1d-stvg` | Unfall mit autonomem Fahrzeug oder Frage zur Haftung bei automatisiertem Fahren. § 1d StVG autonomes Fahren Level 4. Prüfraster: Haftungsverteilung Halter § 7 StVG Fahrer § 18 StVG Hersteller § 1 ProdHaftG Datensaetze Black-Box § 1g StVG... |
| `fachanwalt-verkehrsrecht-bussgeldbescheid-pruefen` | Mandant hat OWi-Bußgeldbescheid erhalten und Anwalt prüft ob Einspruch sinnvoll ist. OWiG §§ 65 ff. StVG § 26 Abs. 3 Verjährung. Prüfraster: Form- und Verfahrensfehler Verjährung 3 Monate ab Tat unterbrochen § 33 OWiG Messverfahren stand... |
| `fachanwalt-verkehrsrecht-fahrerlaubnis-entzug` | Mandant hat Führerschein entzogen bekommen oder befuerchtet Entziehung und fragt nach Möglichkeiten. § 69 StGB strafgerichtlich § 3 StVG verwaltungsrechtlich. Prüfraster: Sperrfrist § 69a StGB vorlaeufige Entziehung § 111a StPO Wiederert... |
| `fachanwalt-verkehrsrecht-mpu-vorbereitung` | Mandant muss MPU ablegen und fragt wie er sich vorbereiten soll. MPU Medizinisch-Psychologische Untersuchung Fahrerlaubnisrecht. Prüfraster: Anlass Alkohol Drogen Punkte Aggression zugelassene Begutachtungsstellen § 66 FeV Vorbereitungsk... |
| `fachanwalt-verkehrsrecht-orientierung` | Einstieg in den Skill-Verbund Verkehrsrecht. Orientierung im Verkehrsrecht FAO Voraussetzungen §§ 14g bis 14i FAO Verkehrsrecht. Typische Mandate Verkehrsunfall Schadensregulierung OWi-Bußgeld Fahrerlaubnis MPU Verkehrsstrafrecht §§ 315c... |
| `fachanwalt-verkehrsrecht-regulierungsanforderung` | Mandant hat Verkehrsunfall und fordert Schadensersatz vom Haftpflichtversicherer des Unfallverursachers. § 115 VVG Direktanspruch §§ 7 17 StVG § 823 BGB. Prüfraster: Direktanspruch Reparatur vs. fiktive Abrechnung Wiederbeschaffungswert... |
| `fachanwalt-verkehrsrecht-tempo-messung-beweis` | Mandant bestreitet korrekte Geschwindigkeitsmessung in Bußgeldbescheid. Tempo-Messung Beweisanfechtung OWiG. Prüfraster: Standardmessgeräte PoliScan Speed Es 3.0 LeivTec XV-3 Multanova PTB-Zulassung Eichschein Messdokumentation Messverfa... |
| `fachanwalt-verkehrsrecht-unfallregulierung-quoten` | Mandant hat Unfall mit Mitverschulden und fragt welche Schadensposten zu welcher Quote durchsetzbar sind. § 254 BGB Mitverschulden Quoten-Modelle. Prüfraster: Schadenstabellen Reparatur Mietwagen Wertminderung Nutzungsausfall Schmerzensg... |
| `fachanwalt-verkehrsrecht-versicherer-quotenverhandlung-vergleich` | Versicherer hat Regulierung angeboten und Anwalt verhandelt Quotenerhöhung oder Vergleich. Versicherer-Verhandlung Unfallregulierung. Prüfraster: Mitverschuldensquote § 254 BGB vorgerichtliche Korrespondenz Schmerzensgeld-Tabellen gerich... |
| `mandat-triage-verkehrsrecht` | Neues Verkehrsrechtsmandat kommt rein und Anwalt muss Sachgebiet klaeren und Fristen prüfen. Eingangs-Triage Verkehrsrecht. Prüfraster: Verfahrensart (Zivilrecht Schadensregulierung OWi Strafrecht Fahrerlaubnis) Unfallart Fristen (Einspr... |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Klage Verkehrsunfall, Einspruch OWi-Bußgeldbescheid, Klage KFZ-Versicherung: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau. |
| `spezial-315c-internationaler-bezug-und-schnittstellen` | 315C: Internationaler Bezug und Schnittstellen im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-autonom-abschlussprodukt-und-uebergabe` | Autonom: Abschlussprodukt und Übergabe im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-bezuege-behoerden-gericht-und-registerweg` | Bezuege: Behörden-, Gerichts- oder Registerweg im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-bussgeld-zahlen-schwellen-und-berechnung` | Bussgeld: Zahlen, Schwellenwerte und Berechnung im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-fachanwalt-erstpruefung-und-mandatsziel` | Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-fahrerlaubnis-compliance-dokumentation-und-akte` | Fahrerlaubnis: Compliance-Dokumentation und Aktenvermerk im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-kanzlei-mandantenkommunikation-entscheidungsvorlage` | Kanzlei: Mandantenkommunikation und Entscheidungsvorlage im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-personen-verhandlung-vergleich-und-eskalation` | Personen: Verhandlung, Vergleich und Eskalation im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-pflvg-risikoampel-und-gegenargumente` | Pflvg: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-quoten-sonderfall-und-edge-case` | Quoten: Sonderfall und Edge-Case-Prüfung im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-sachschaden-livequellen-und-rechtsprechungscheck` | Sachschaden: Livequellen- und Rechtsprechungscheck im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-schnittstelle-red-team-und-qualitaetskontrolle` | Schnittstelle: Red-Team und Qualitätskontrolle im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-stgb-formular-portal-und-einreichung` | Stgb: Formular, Portal und Einreichungslogik im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-stvg-fristen-form-und-zustaendigkeit` | Stvg: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-stvo-dokumentenmatrix-und-lueckenliste` | Stvo: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-unfallregulierung-beweislast-und-darlegungslast` | Unfallregulierung: Beweislast, Darlegungslast und Substantiierung im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-verkehr-fristennotiz-und-naechster-schritt` | Verkehr: Fristennotiz und nächster Schritt im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-verkehrsrecht-tatbestand-beweis-und-belege` | Verkehrsrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-verkehrsstrafrecht-mehrparteien-konflikt-und-interessen` | Verkehrsstrafrecht: Mehrparteienkonflikt und Interessenmatrix im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-verkehrsunfall-schriftsatz-brief-und-memo-bausteine` | Verkehrsunfall: Schriftsatz-, Brief- und Memo-Bausteine im Plugin fachanwalt verkehrsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `unfall-haftungsquote-berechnen` | Mandant hatte Verkehrsunfall und fragt: Wer haftet wie viel und welche Schadensposten koennen geltend gemacht werden? §§ 7 17 18 StVG iVm § 254 BGB Haftungsquote. Prüfraster: Betriebsgefahr beidseitig Anscheinsbeweis Auffahrunfall Spurwe... |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlungs-Strategie für Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht): ZOPA, BATNA, Verhandlungsfenster, Druckmittel, Settlement-Skript, Vergleichsentwurf und prozessuale Absicherung (Protokoll-/Anwaltsvergleich). |
| `verk-fahrerlaubnisrecht-leitfaden` | Leitfaden Fahrerlaubnisrecht: Entziehung, MPU, Sperrfrist, vorzeitige Wiedererteilung. Pruefraster FeV-Begutachtung und Klage gegen Fahrerlaubnisbehoerde. |
| `verk-fahrtenbuch-anordnung-spezial` | Spezialfall Fahrtenbuchanordnung § 31a StVZO: Voraussetzungen, Ermessen, Mitwirkung, Verhaeltnismaessigkeit. Pruefraster fuer Widerspruch und Klage. |
| `verk-trunkenheit-drogenfahrt-spezial` | Spezialfall Trunkenheits- und Drogenfahrt: § 24a StVG OWi, § 316 StGB, relative und absolute Fahruntuechtigkeit, BAK-Werte, Cannabis-Grenzwert Reform 2024. Pruefraster fuer Verteidiger. |
| `verk-unfallregulierung-workflow` | Workflow Unfallregulierung: Anspruchsgrundlagen § 7 StVG / § 18 StVG / § 823 BGB / § 115 VVG, Quote, Schadenspositionen Wiederbeschaffungswert, Wertminderung, Nutzungsausfall. Pruefraster fuer Geschaedigtenanwalt. |
| `vkr-blitzer-messverfahren-spezial` | Spezialfall Blitzer- und Messverfahren: standardisiertes Messverfahren, Rohmessdaten-Recht des Verteidigers (BVerfG 2 BvR 1167/20), Verwertbarkeit, Beweisantrag Sachverstaendigengutachten. Pruefraster und Schriftsatzbausteine. |
| `vkr-bussgeldverfahren-grundzuege` | Bussgeldverfahren Grundzuege: Anhoerungsbogen, Einspruch innerhalb 2 Wochen, Hauptverhandlung Amtsgericht, Rechtsbeschwerde OLG nach §§ 79 ff. OWiG. Strategien Verteidigung, Punkterabatt bei Punkteabbau-Seminar. Pruefraster. |
| `vkr-einfuehrung-rechtsfelder` | Verkehrsrecht einfuehrend: Verkehrsstrafrecht (Trunkenheit § 316 StGB, Gefaehrdung § 315c StGB, Unfallflucht § 142 StGB), OWi (Bussgeldverfahren), Haftpflicht, Kasko, Fuehrerscheinrecht, FeV, MPU. Entscheidungstabelle. |
| `vkr-totalschaden-fiktiv-spezial` | Spezialfall fiktive Abrechnung beim Totalschaden: Wiederbeschaffungswert minus Restwert, 130-Prozent-Grenze BGH, Verweisung auf guenstigere Reparaturen (BGH-Verweisrechtsprechung). Pruefraster fuer Mandantenberatung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin fachanwalt-verkehrsrecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin fachanwalt-verkehrsrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin fachanwalt-verkehrsrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin fachanwalt-verkehrsrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin fachanwalt-verkehrsrecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin fachanwalt-verkehrsrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin fachanwalt-verkehrsrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin fachanwalt-verkehrsrecht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin fachanwalt-verkehrsrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin fachanwalt-verkehrsrecht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
