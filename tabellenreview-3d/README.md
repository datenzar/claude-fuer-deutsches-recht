# Tabellenreview 3D

3D-Tabellenreview als Wuerfel: Spaltenprompts pro Datenpunkt x Zeilenprompts pro Dokument x Arbeitsblatt-Perspektiven (Recht / Steuer / Wirtschaft) gestapelt. Massenpruefung Vertragsstapel M&A-DD Immobilien Vendor-Onboarding mit Excel-Mehrblatt Kreuzblatt-Konsistenz Audit-Trail Belegkette.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Tabellenreview 3D (`tabellenreview-3d`, dieses Plugin) | [tabellenreview-3d.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/tabellenreview-3d.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus „Code → Download ZIP“ verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `arbeitsblatt-perspektiven-definieren` | Definiert die dritte Wuerfel-Achse — Arbeitsblaetter als Perspektiven die ueber denselben Dokumentenstapel laufen aber jeweils eine andere Brille aufsetzen. Typische Perspektiven: Recht (Anwalt) Steuer (Steuerberater)… |
| `audit-trail-protokoll` | Fuehrt das Audit-Trail-Protokoll des Wuerfels — jeder Reviewlauf jede Prompt-Aenderung jede Pruefer-Abnahme jeder Cache-Treffer jede Hash-Pruefung wird unveraenderlich protokolliert. Spalten pro Eintrag: Zeitstempel A… |
| `belegkette-rueckverfolgung` | Sichert die Belegkette jeder Zelle des Wuerfels — von der Antwort ueber das woertliche Zitat bis zur Originalstelle im Quelldokument mit Seite Absatz und Datei-Hash. Erkennt Belegkette-Brueche (Datei-Hash weicht ab / … |
| `caching-und-teil-rerun` | Caching der Wuerfelzellen und gezielter Teil-Rerun bei Aenderungen — vermeidet die voll Neuberechnung von tausenden Zellen wenn nur ein Spaltenprompt eine Zeile oder ein Arbeitsblatt geaendert wurde. Cache-Key pro Zel… |
| `dokumentstapel-aufnehmen` | Nimmt einen Dokumentenstapel als Zeilenachse des Wuerfels auf. Quellen: VDR-Export (Datasite Intralinks Box) lokaler Ordner SharePoint-Bibliothek E-Mail-Anhang-Sammlung gescannte PDF mit OCR-Pipeline. Erzeugt pro Doku… |
| `excel-multi-sheet-export` | Exportiert den dreidimensionalen Wuerfel in eine einzige Excel-Datei mit mehreren Tabellenblaettern — ein Reiter pro Arbeitsblatt-Perspektive (Recht / Steuer / Wirtschaft / Datenschutz / IT / Betrieb / Compliance). Je… |
| `tabellenreview-3d-kaltstart-interview` | Kaltstart-Interview fuer das tabellenreview-3d-Plugin. Erfragt typische Anwendungsfaelle (M&A-DD / Immobilienportfolio / Vendor-Onboarding / Arbeitsvertraege / Mietvertraege / Anlagedokumente / freie Eigenwuerfel), St… |
| `kreuzblatt-konsistenzpruefung` | Prueft die dritte Wuerfel-Dimension auf innere Konsistenz — laeuft NACH `review-durchfuehren` ueber alle Arbeitsblaetter und sucht Widersprueche zwischen Perspektiven (z. B. ein Vertrag rechtlich gruen aber datenschut… |
| `pdf-bericht-erzeugen` | Erstellt einen pruefbaren PDF-Bericht aus dem 3D-Wuerfel. Struktur: Deckblatt mit Projekt Mandant Stichtag Wuerfel-Ampel; Management-Summary mit Hotspots und blockierenden Roten; pro Arbeitsblatt-Perspektive ein Absch… |
| `prompt-versionierung` | Versioniert alle Spalten- und Zeilenprompts mit semantischer Versions-ID — patch fuer Wortlautfeinheiten minor fuer geaenderte Antworttypen oder Ampelregeln major fuer geaenderte Pruefdimension. Jede Zelle im Wuerfel … |
| `pruefer-uebergabe-paket` | Schnuert das vollstaendige Pruefer-Paket nach Abschluss eines Wuerfellaufs — Excel-Wuerfel-Datei aus Skill `excel-multi-sheet-export` PDF-Bericht aus `pdf-bericht-erzeugen` Belegketten-CSV aus `belegkette-rueckverfolg… |
| `review-durchfuehren` | Fuehrt den eigentlichen Reviewlauf ueber den Wuerfel durch — Anzahl Zellen = Spalten x Zeilen x Arbeitsblaetter. Pro Zelle: Spaltenprompt + Zeilenprompt + Arbeitsblatt-Perspektive zusammenfuehren, Antwort aus dem Doku… |
| `risikoampel-aggregation` | Konsolidiert die Ampel-Wertungen entlang aller drei Wuerfelachsen — pro Zelle (atomisch) pro Zeile (Dokument-Gesamtampel) pro Spalte (Datenpunkt-Hotspots) pro Arbeitsblatt (Perspektiven-Gesamtampel) und pro Gesamtwuer… |
| `spaltenprompts-definieren` | Definiert die Spaltenprompts der ersten Wuerfel-Achse — jede Spalte ist eine einzige praezise Frage die fuer ALLE Dokumente identisch gestellt wird damit Vergleichbarkeit ueber den Stapel entsteht. Enthaelt eine Bibli… |
| `vorlage-arbeitsvertrag-portfolio` | Wuerfelvorlage fuer Massenpruefung von Arbeitsvertraegen — 15 Spalten (Vertragsdatum Probezeit Befristung-mit-oder-ohne-Sachgrund Wochenarbeitszeit Kuendigungsfrist Tarifbindung Bruttogehalt Sonderzahlung Verschwiegen… |
| `vorlage-immobilien-portfolio` | Wuerfelvorlage fuer Immobilien-Portfolioanalyse — 16 Spalten (Gemarkung / Flur / Flurstueck / Wirtschaftsart / Groesse / Eigentuemerkette / Abteilung-II-Lasten / Abteilung-III-Grundpfandrechte / Rang / Loeschungserlei… |
| `vorlage-ma-due-diligence` | Fertige Wuerfelvorlage fuer M&A-Due-Diligence — 18 Spalten (Vertragsart Laufzeit Kuendigungsfrist Change-of-Control MAC-Klausel Abtretungsverbot Haftungsbegrenzung Garantien Vertragsstrafe SLA Datenschutz Geheimhaltun… |
| `vorlage-vendor-onboarding-3d` | Wuerfelvorlage fuer Vendor- und Lieferanten-Onboarding — 17 Spalten (Vendor-Stammdaten Branche AVV-Pflicht AVV-vorhanden SLA-Reaktionszeit SLA-Verfuegbarkeit Exit-Klausel Datenherausgabe Verschluesselung Subunternehme… |
| `wuerfel-aufbauen` | Baut die dreidimensionale Wuerfel-Struktur fuer ein neues Pruefprojekt auf — drei Achsen: Spalten (Datenpunkte als Spaltenprompts) Zeilen (Dokumente mit optionalen Zeilenprompts) Arbeitsblaetter (Perspektiven wie Rech… |
| `zeilenprompts-definieren` | Definiert die Zeilenprompts der zweiten Wuerfel-Achse — pro Dokument eine optionale Sonderanweisung die das Lesen genau dieses Dokuments steuert. Beispiele: 'Konzernvertrag — AktG Paragraph 311 zusaetzlich pruefen' / … |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.
