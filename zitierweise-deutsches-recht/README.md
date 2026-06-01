# Zitierweise deutsches Recht (v4.0)

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`zitierweise-deutsches-recht`) | [`zitierweise-deutsches-recht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/zitierweise-deutsches-recht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Zitierweise-Pruefkorpus — Kanzlei Roosendaal Birkenhainer Partners mbB — Kanzleihandbuch v4 mit 100 Fundstellen und Pruefvermerken** (`zitierweise-pruefkorpus-roosendaal-kanzleihandbuch-mit-100-fundstellen-und-pruefvermerken`) | [Gesamt-PDF lesen](../testakten/zitierweise-pruefkorpus-roosendaal-kanzleihandbuch-mit-100-fundstellen-und-pruefvermerken/gesamt-pdf/zitierweise-pruefkorpus-roosendaal-kanzleihandbuch-mit-100-fundstellen-und-pruefvermerken_gesamt.pdf) | [`testakte-zitierweise-pruefkorpus-roosendaal-kanzleihandbuch-mit-100-fundstellen-und-pruefvermerken.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zitierweise-pruefkorpus-roosendaal-kanzleihandbuch-mit-100-fundstellen-und-pruefvermerken.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Zitierweise-Pruefkorpus — Kanzlei Roosendaal Birkenhainer Partners mbB — Kanzleihandbuch v4 mit 100 Fundstellen und Pruefvermerken** (`zitierweise-pruefkorpus-roosendaal-kanzleihandbuch-mit-100-fundstellen-und-pruefvermerken`) | [Gesamt-PDF lesen](../testakten/zitierweise-pruefkorpus-roosendaal-kanzleihandbuch-mit-100-fundstellen-und-pruefvermerken/gesamt-pdf/zitierweise-pruefkorpus-roosendaal-kanzleihandbuch-mit-100-fundstellen-und-pruefvermerken_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zitierweise-pruefkorpus-roosendaal-kanzleihandbuch-mit-100-fundstellen-und-pruefvermerken.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

Deutsche juristische Hauszitierweise als zuschaltbares Plugin. Fokus: belastbare, überprüfbare Quellen statt schöner, aber nicht verifizierbarer Fundstellen.

## Was ist neu in v4.0

1. **BeckRS-Sperre:** BeckRS-Fundstellen werden nicht mehr aus Modellwissen erzeugt. Sie dürfen nur übernommen werden, wenn der Nutzer sie liefert oder ein lizenzierter Live-Zugriff sie verifiziert.
2. **Literatur-Sperre:** Kommentare, Handbücher, Monographien und Aufsätze werden nicht blind zitiert. Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
3. **Rechtsprechungs-Mindeststandard:** Gericht, Entscheidungsform, Datum und Aktenzeichen sind Pflicht. Wo möglich kommt eine amtliche oder frei zugängliche Quelle dazu.
4. **Keine Palandt-/Pahlen-Aktualzitate:** Der frühere Palandt heißt seit 2022 Grüneberg; historische Altauflagen nur bei konkreter Nutzerquelle.
5. **Prüfvermerk statt Halluzination:** Unverifizierte Entscheidungen werden markiert oder weggelassen, nicht ausgeschmückt.

## Direkt-Download

| Datei | Direkt-Download |
| --- | --- |
| **Plugin-ZIP: Zitierweise deutsches Recht** | [zitierweise-deutsches-recht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/zitierweise-deutsches-recht.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Installation in Claude Code

1. ZIP herunterladen.
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/` und `references/` im ZIP-Root enthalten. Nicht das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Routing: klärt, ob ein Text Zitate erzeugen, glätten, prüfen oder sperren soll. |
| `zitierweise-anwenden` | Wendet die Quellenregel v4.0 an: Rechtsprechung nur mit Datum, Aktenzeichen und verifizierbarer Quelle; keine BeckRS-, Kommentar- oder Aufsatz-Blindzitate. |

## Kurzregel

Norm zuerst. Dann verifizierte Rechtsprechung. Literatur nur bei bereitgestellter oder live verifizierter Quelle. Keine BeckRS-, Kommentar- oder Aufsatz-Blindzitate.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Zitierweise Deutsches Recht-Plugin. Setzt v4.0 durch: Rechtsprechung nur mit Datum, Aktenzeichen und verifizierbarer Quelle; keine BeckRS-, Kommentar- oder Aufsatz-Blindzitate. Fragt Ziel,... |
| `zit-gesetzeszitierung-bauleiter` | Bauleiter Gesetzeszitierung in Schriftsatz und Memo: Norm, Absatz, Satz, Halbsatz, Nummer, Buchstabe. Pruefraster fuer einheitliche Schreibweise. |
| `zit-internationale-urteile-spezial` | Spezialfall Zitierung internationaler Urteile EuGH EGMR sowie Common-Law-Urteile: ECLI, Neutral Citation, Public Domain. Pruefraster fuer internationale Mandate. |
| `zit-kommentar-aufsatzzitierung-spezial` | Spezialfall Kommentar- und Aufsatzzitierung: Bearbeiter, Randnummer, Auflagenjahr, Zeitschrift, Heft, Seite. Pruefraster fuer wissenschaftliches Schreiben. |
| `zit-rechtsprechungszitierung-leitfaden` | Leitfaden Rechtsprechungszitierung BGH BVerfG EuGH: Gericht, Entscheidungsform, Datum, Aktenzeichen, frei pruefbarer Link dejure.org / openjur.de. Pruefraster fuer Memos. |
| `zitat-amtliche-sammlung-vs-zeitschrift` | Amtliche Sammlung vs. Zeitschrift: Reihenfolge der Fundstellen. Amtliche Sammlung (BGHZ, BVerfGE) hat Vorrang, dann Parallelfundstelle Zeitschrift (NJW, JZ, ZIP). Beispiel BGHZ 240 S. 1 = NJW 2024 S. 1832. |
| `zitat-archivierungspflicht` | Archivierungspflicht der zitierten Quelle: Screenshot mit Datum, PDF-Abruf, archive.org-Backup. Wichtig bei Schriftsaetzen, weil Online-Quellen veraendert werden. Empfehlung Kanzleiprozess. |
| `zitat-aufsatz-zeitschrift` | Aufsatz in juristischer Zeitschrift: Verfasser, Aufsatztitel, Zeitschrift Jahr, Heft (falls relevant), Seite. Beispiel Mueller, Die neue Haftung des GmbH-Geschaeftsfuehrers, NZG 2024 S. 567. Bei Online-Zeitschrift: zusaetzlich URL. |
| `zitat-bag-bfh-bsg-bag` | Fachgerichtsbarkeit zitieren: BAG, BFH, BSG, BVerwG, BGH. Format Senat, Datum, Aktenzeichen, amtliche Sammlung sowie Parallel-Fundstelle. Beispiel BAG, Urt. v. 12.09.2023 9 AZR 372 aus 22, BAGE 178 S. 199 = NZA 2023 S. 1521. |
| `zitat-bgh-entscheidung` | BGH-Entscheidung korrekt zitieren: Senat, Datum, Aktenzeichen, Fundstelle. Beispiel BGH, Urt. v. 11.04.2024 III ZR 168 aus 23, BGHZ 240 S. 1 = NJW 2024 S. 1832. Bei wichtiger Linie: Vor- und Folgeentscheidungen ergaenzen. |
| `zitat-bverfg-entscheidung` | BVerfG-Entscheidung zitieren: Senatsnummer, Datum, Aktenzeichen, BVerfGE, ggf. Kammerbeschluss. Beispiel BVerfG, Urt. v. 17.01.2024 1 BvR 1841 aus 23, BVerfGE 167 S. 1. Kammerentscheidung BVerfG (K), Beschl. v. ... mit Hinweis 'Nichtanna... |
| `zitat-eugh-rechtsprechung` | EuGH-Rechtsprechung zitieren: Urt./Beschl., Datum, Rs. C-Nummer, Parteinamen, ECLI. Beispiel EuGH, Urt. v. 04.07.2019 - C-377/17, Kommission/Deutschland, ECLI:EU:C:2019:562. Bei Generalanwalts-Schlussantraegen: GA-Anfang. |
| `zitat-gesetz-verordnung` | Gesetz/Verordnung zitieren: Norm-Bezeichnung, ggf. § und Absatz. Beispiel § 17 InsO, § 311 Abs. 2 BGB, Art. 26 DSGVO. Bei zeitlicher Bezugnahme: § X i. d. F. v. JJJJ. |
| `zitat-haus-zitierregel-anpassen` | Kanzlei-Hauszitierweise anpassen: Excel-Vorlage Beck/NJW vs. Hartung/Roemermann v4. Empfehlung: konsistente Regel pro Kanzlei, in den Schriftsatz-Templates verankern. Output: Hauszitierregel-Dokument. |
| `zitat-instanzgerichte-strategisch` | Instanzgerichts-Entscheidungen strategisch zitieren: OLG-Entscheidungen, LG-Entscheidungen. Wann sinnvoll: Tendenzen, Lokal-Linien, Fehlen BGH-Rechtsprechung. Vermeiden: AG-Entscheidungen ausser bei sehr engen Fragen. |
| `zitat-internationale-quellen` | Internationale Quellen: EuGH, EGMR, Common-Law-Faelle (in IPR-Kontext). Format mit ECLI bzw. Neutral Citation. Beispiel EGMR, Urt. v. 23.01.2024 - Nr. 12345/22, ECLI:CE:ECHR:2024:0123JUD001234522. |
| `zitat-internet-quellen` | Internet-Quellen zitieren: Stand, URL, Abrufdatum. Bevorzugt: dejure.org, openjur.de, bundesgerichtshof.de, bundesverfassungsgericht.de, eur-lex. Vermeiden: anwalt24.de, BeckRS allein als einzige Fundstelle. |
| `zitat-kommentar-randnummer` | Kommentar mit Bearbeiter und Randnummer zitieren: Palandt/Gruenberg, BGB, 84. Aufl. 2025, § 433 Rn. 12. Bei Loseblatt-Kommentar Stand-Datum. Beispiele MueKo, BeckOK, Erfurter Kommentar. |
| `zitat-leitsatzentscheidung` | Leitsatz-Entscheidung mit Leitsatz zitieren: BGH, Urt. ..., Leitsatz 1 lautet: ... Original-Leitsatz im Wortlaut, dann Begruendung mit Rn. Format fuer Schriftsatz und Memo. |
| `zitat-monografie-handbuch` | Monografie/Handbuch zitieren: Verfasser, Titel, Auflage Jahr, Seitenzahl. Bei Handbuch mit mehreren Bearbeitern: Bearbeiter in Hauptverfasser, Titel, Auflage Jahr, Kapitel/§, Rn. Beispiel: Schmitz, in: Beck'sches Handbuch GmbH, 6. Aufl.... |
| `zitat-rechtsprechung-ohne-fundstelle` | Rechtsprechung ohne offizielle Fundstelle: nur juris- oder BeckRS-Eintrag. Loesungen: dejure.org-Permalink, Gericht/Datum/Aktenzeichen + 'juris', alternativ BeckRS-Eintrag mit klarer Angabe. Vermeiden: 'BeckRS allein' fuer wichtige Argum... |
| `zitat-streitstand-darstellen` | Streitstand in Memo/Schriftsatz darstellen: h. M. (Rechtsprechung BGH + ueberwiegende Literatur), Gegenmeinung (Verfasser + Stellenangabe), eigene Loesung. Format mit klarer Position. |
| `zitat-verboten-anwalt24-beckrs` | Verbotene Zitate vermeiden: anwalt24.de (kein primaerer Rechtsstand), BeckRS allein (interne Beck-Online-ID), 'lawblog'-Eintraege. Speziell bei Schriftsaetzen: Gericht prueft Originalquelle. Empfehlung: immer dejure.org oder Originalents... |
| `zitierweise-anwenden` | Wende deutsche juristische Hauszitierweise v4.0 an. Rechtsprechung nur mit Gericht Entscheidungsform Datum Az. Aktenzeichen und verifizierbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate. Literatur nur bei Nutzerq... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
