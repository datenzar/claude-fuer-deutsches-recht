# NDA-Abgleich

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`nda-abgleich`) | [`nda-abgleich.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/nda-abgleich.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **NDA-Vertragsabgleich Windsysteme Norderhof AG / Eickmann Wirtschaftspartner Pte. Ltd. — Joint Venture, GeschGehG, Exportkontrolle** (`nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft`) | [Gesamt-PDF lesen](../testakten/nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft/gesamt-pdf/nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft_gesamt.pdf) | [`testakte-nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **NDA-Vertragsabgleich Windsysteme Norderhof AG / Eickmann Wirtschaftspartner Pte. Ltd. — Joint Venture, GeschGehG, Exportkontrolle** (`nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft`) | [Gesamt-PDF lesen](../testakten/nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft/gesamt-pdf/nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

NDA-Verhandlungshilfe für die empfangende Seite. Akzeptiert den Entwurf der Gegenseite und setzt den eigenen Standard chirurgisch durch. Ampelmatrix ROT/GELB/GRUEN. Ausgabe .docx mit echten Word-Tracked-Changes. Keine Absatzlöschungen, keine Klausel-Neufassungen.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| NDA-Abgleich (`nda-abgleich`, dieses Plugin) | [nda-abgleich.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/nda-abgleich.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `nda-abgleich` | NDA-Verhandlungshilfe für die empfangende Seite. Zwei Modi: (A) Standard-Destillation aus 1 bis n eigenen NDAs und frei beschreibbarer Erfahrung in einen konsolidierten Haltelinien-Standard mit Ampelmatrix ROT/GELB/G… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im NDA Abgleich-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei D... |
| `nda-abgleich` | Empfangende Seite soll NDA der Gegenseite prüfen und verhandeln oder Kanzlei will aus mehreren NDAs einen eigenen Standard destillieren. NDA-Verhandlungshilfe. Modus A Destillation: 1 bis n eigene NDAs in konsolidierten Haltelinien-Stand... |
| `nda-anwendbares-recht-gerichtsstand` | Anwendbares Recht und Gerichtsstand bei NDA: Empfehlung deutsches Recht + LG Sitz des Discloser; Schiedsklausel (DIS Regeln) ab hoeherer Bedeutung. Pruefraster: internationale NDAs vs. nationale, Verbraucherbeteiligung. |
| `nda-bei-arbeitnehmer-kuendigung` | Post-Termination-NDA bei Arbeitnehmer-Kuendigung: Wirksamkeit, Karenzentschaedigung § 74 HGB analog, Reichweite (keine generelle Wettbewerbssperre). Schnittstelle Arbeitsrecht. Empfehlung: nur ergaenzend zu nachvertraglichem Wettbewerbsv... |
| `nda-bei-bewerbungen-pitches` | NDA bei Bewerbungen/Pitches/Investorengespraechen: Investor-NDAs sind ungewoehnlich; ueblich nur enge Mutual-NDAs fuer fortgeschrittene Stage. Empfehlung: nicht beleidigt sein, wenn VC unterschreibt nicht; Verhandlungsstrategie. |
| `nda-bei-r-d-kooperation` | NDA bei F&E-Kooperation: Background-IP / Foreground-IP-Trennung, IP-Zuordnung bei gemeinsamer Erfindung, Foerderrechtshinweise (BMBF/EU). Empfehlung: NDA + Pre-LoI mit IP-Grundsaetzen. |
| `nda-definitionsklausel-abgleichen` | Definitionsklausel 'Vertrauliche Information' abgleichen: weiter Begriff (alle Informationen) vs. eng definiert (nur als vertraulich markiert). Empfehlung je nach Rolle: Discloser will weit, Recipient will eng. Wortlautempfehlungen. |
| `nda-grundstruktur-pruefen` | NDA-Grundstruktur pruefen: Parteien, Zweck der Offenlegung, Definition Vertrauliche Information, Pflichten, Laufzeit, Aufbewahrung/Rueckgabe, Vertragsstrafe, Geheimhaltungsdauer nach Vertragsende, Jurisdiction. Pruefraster gegen marktueb... |
| `nda-international-arbitration-spezial` | Spezialfall internationale NDAs und Schiedsklauseln: Rechtswahl, Schiedsort, einstweiliger Rechtsschutz, Common-Law-Begriffe Equity. Pruefraster fuer Cross-Border-Mandat. |
| `nda-it-saas-vendor` | NDA fuer SaaS-/IT-Vendor-Pitches: Cloud-Hosting, Datentrennung, Subprozessoren, Audit-Rechte, Penetration-Testing-Erlaubnis. Empfehlung: nicht-exklusive Lizenz fuer Test-Daten, klare Loeschpflicht nach Pitch. |
| `nda-laufzeit-und-survival` | Laufzeit und Survival der Geheimhaltungspflicht: Festlaufzeit, automatische Verlaengerung, Survival 2/3/5 Jahre nach Vertragsende. Bei Geschaeftsgeheimnissen i. S. GeschGehG ist Survival 'so lange die Information Geschaeftsgeheimnis ist'... |
| `nda-m-und-a-clean-team-spezial` | Spezialfall NDA fuer M-and-A und Clean-Team-Arrangements: Datenraum, Sondervertraulichkeit Wettbewerbsdaten, Kartellrecht. Pruefraster fuer Antitrust-Counsel. |
| `nda-mit-geschaeftsgeheimnis-geschgehg` | NDA als angemessene Geheimhaltungsmassnahme i. S. § 2 Nr. 1 b GeschGehG: NDA allein reicht nicht, technisch-organisatorische Massnahmen erforderlich (Zugangsschutz, Klassifizierung, Logging). Pruefraster. |
| `nda-mit-kartellsensitiven-daten` | NDA mit kartellsensitiven Daten (Preise, Mengen, Kunden): Clean Team Agreement, Aggregation, externe Berater zwischen den Parteien. Empfehlung: Vorabklaerung ob Daten ueberhaupt ausgetauscht werden duerfen. |
| `nda-mit-personenbezogenen-daten` | NDA mit personenbezogenen Daten: ggf. AV-Vertrag § 28 BDSG / Art. 28 DSGVO erforderlich, gemeinsame Verantwortlichkeit Art. 26 DSGVO pruefen. NDA ersetzt AV nicht. Empfehlung: separater AVV anlagengeb. |
| `nda-mitarbeiter-need-to-know` | Mitarbeiter und Need-to-Know: NDA verpflichtet Mitarbeiter ueber Arbeitsvertrag, externe Berater nur ueber separate NDA oder Backup-Klausel. Empfehlung: Liste freigegebener Personen, Bestaetigung Mitarbeiter-NDA, kein Datenraum-Zugriff o... |
| `nda-non-solicit-kartellrechtlich` | Non-Solicit in NDA kartellrechtlich pruefen: zeitlich begrenzt (12-24 Monate), sachlich begrenzt (nur fuer NDA-Zweck involvierte Mitarbeiter), keine generelle Bewerbungs-Sperre. Andernfalls Risiko § 1 GWB / Art. 101 AEUV. |
| `nda-permitted-disclosure` | Permitted Disclosure: Konzern, Beraterklausel, gesetzliche Offenlegungspflichten (Aufsicht, Strafverfolgung, Gericht). Standard-Wortlaut und typische Fallstricke (z. B. Konzernbegriff zu eng). |
| `nda-rueckgabe-vernichtung` | Rueckgabe und Vernichtung Vertraulicher Information: Pflicht, Bestaetigung, Backup-Ausnahme (technisch unmoeglich zu loeschende Backups). Bei Daten in Cloud: Loeschbestaetigung Vendor erforderlich. Wortlautempfehlungen. |
| `nda-standardklauseln-bauleiter` | Bauleiter NDA-Standardklauseln: Vertraulichkeitsumfang, Empfaengerkreis, Laufzeit, Rechtsfolgen, Schriftform. Pruefraster fuer mutual und one-way NDA. |
| `nda-typen-vergleich` | NDA-Typen vergleichen: einseitig (unilateral), gegenseitig (mutual), mehrparteiig. Empfehlung pro Situation: Verkaeufer in M&A unilateral; gemeinsame Entwicklung mutual; Konsortium mehrparteiig. Praxisanker fuer Templates. |
| `nda-vergleichsmatrix-leitfaden` | Leitfaden NDA-Vergleichsmatrix: relevante Klauseln vergleichen, Markup, Risikoampel, Wechselwirkungen mit Geschaeftsgeheimnisgesetz. Pruefraster fuer Reviewteam. |
| `nda-vertragsstrafe-pruefen` | Vertragsstrafe pruefen: Hoehe, AGB-Kontrolle §§ 305 ff. BGB, Bestimmtheitsgrundsatz, Schadensersatzkumulation oder Anrechnung. Bei Verbraucher-NDA strengere Grenzen. Bei B2B-Standard: ueblich 5000-25000 EUR pro Vorfall, Kumulation moeglich. |
| `nda-vor-m-a-data-room` | NDA vor M&A-Data-Room: enge Zweckbindung (Pruefung Transaktion), Standstill-Klausel, Non-Solicit, Verbot Reverse-Engineering. Empfehlung: separater Clean Team Agreement fuer Kartell-/Wettbewerbsdaten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
