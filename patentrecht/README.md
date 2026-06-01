# patentrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`patentrecht`) | [`patentrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/patentrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Patentrecht — Erfindungsakten Ravenstein & Moll** (`patentrecht-erfindungsakten-ravenstein-moll`) | [Gesamt-PDF lesen](../testakten/patentrecht-erfindungsakten-ravenstein-moll/gesamt-pdf/patentrecht-erfindungsakten-ravenstein-moll_gesamt.pdf) | [`testakte-patentrecht-erfindungsakten-ravenstein-moll.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-patentrecht-erfindungsakten-ravenstein-moll.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Patentrecht — Erfindungsakten Ravenstein & Moll** (`patentrecht-erfindungsakten-ravenstein-moll`) | [Gesamt-PDF lesen](../testakten/patentrecht-erfindungsakten-ravenstein-moll/gesamt-pdf/patentrecht-erfindungsakten-ravenstein-moll_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-patentrecht-erfindungsakten-ravenstein-moll.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

> Großes Arbeitsplugin für Patentanwältinnen, Rechtsanwälte, Patentabteilungen und technische Gründerteams. Es führt vom rohen Erfindungsgedanken über Anspruchsentwurf, Recherche, Anmeldung, Prüfung, Freedom-to-Operate, Abmahnung, Lizenzvertrag, Einspruch und Nichtigkeit bis zur belastbaren Mandantenkommunikation.

## Wofür dieses Plugin gedacht ist

Das Plugin ist nicht nur eine Recherchehilfe. Es ist der Mandatsarbeitsplatz für Patentrecht:

- **Erfindung aufnehmen:** technische Lehre, Problem, Lösung, Ausführungsformen, Offenbarungsrisiken und fehlende Zeichnungen sauber einsammeln.
- **Anmeldung vorbereiten:** Anspruch 1, Unteransprüche, Beschreibung, Bezugszeichenliste, Figurenlogik, Alternativausführungen und Rückfragen strukturieren.
- **Patentfähigkeit prüfen:** Neuheit und erfinderische Tätigkeit nach PatG und EPÜ mit Merkmalsgliederung, nächstliegendem Stand der Technik und Aufgaben-Lösungs-Ansatz.
- **Recherche steuern:** gezielte Übergabe an das Spezialplugin [`patentrecherche`](../patentrecherche) für Espacenet, DPMAregister, DEPATISnet, EPO Register, WIPO PATENTSCOPE und weitere Datenbanken.
- **Verletzung und FTO prüfen:** Schutzbereich, wortsinngemäße Verwirklichung, Äquivalenz, Registerstand, Territory, Rechtsbestand und Design-around.
- **Abmahnung verteidigen:** Fristen, Unterlassung, Auskunft, Rückruf, Schadensersatz, negative Feststellung, Schutzschrift, Vergleichsfenster.
- **Verträge prüfen:** Patentlizenz, Exclusivity, Territory, Field of Use, Sublicensing, Improvements, Know-how, Royalties, Audit, Termination und DE/EN-Klauselrisiken.
- **Bestand angreifen oder verteidigen:** EPA-Einspruch, deutsche Nichtigkeitsklage, Beschränkung, Hilfsanträge, Fristen und Beweismittel.

## Arbeitsstil

Der Einstiegsskill fragt nicht lehrbuchartig alles ab, sondern sortiert den Fall sofort nach Dringlichkeit, Materiallage und Ziel. Bei Dokumentenupload ohne Begleittext erkennt er Fristen, Aktenart und Primärpfad. Danach schlägt er die passenden Spezialskills vor oder arbeitet direkt weiter.

## Quellen- und Zitierhygiene

- Normen und Behördeninformationen werden bevorzugt aus offiziellen Quellen geprüft: Patentgesetz auf Gesetze-im-Internet, DPMA-Informationen, DPMAregister/DEPATISnet, EPO/EPA Legal Texts, EPO Register, Espacenet, WIPO PATENTSCOPE und amtliche Gerichtsquellen.
- Rechtsprechung wird nur ausgegeben, wenn Gericht, Entscheidungsdatum, Aktenzeichen und eine frei zugängliche oder amtliche Fundstelle verifiziert sind.
- Keine BeckRS-/juris-/Paywall-Fundstellen erfinden oder als eigene Quelle verwenden.
- Wenn eine Bewertung von aktueller Amts- oder Registerlage abhängt, muss live nachgesehen werden.

## Verhältnis zu anderen Plugins

- [`patentrecherche`](../patentrecherche): tiefe Datenbankrecherche, CPC/IPC, Patentfamilien, Registerstand, Recherchebericht.
- [`gewerblicher-rechtsschutz`](../gewerblicher-rechtsschutz) und [`fachanwalt-gewerblicher-rechtsschutz`](../fachanwalt-gewerblicher-rechtsschutz): Marken, Designs, UWG, Verletzungsprozess und IP-Kollisionslagen.
- [`zitierweise-deutsches-recht`](../zitierweise-deutsches-recht): saubere Nachweise und Rechtsprechungszitate.
- [`word-legal-ai-plugin-and-skill-for-german-lawyers`](../word-legal-ai-plugin-and-skill-for-german-lawyers): Schriftsatz-, Gutachten-, Vertrags- und Mandantenbriefstil.

## Kern-Workflow

1. **Material erfassen:** Upload, Fristen, Beteiligte, Schutzrechte, Produkt/Verfahren, Technikfeld, Zielterritorien.
2. **Primärfrage festlegen:** Anmeldung, Recherche, FTO, Verletzung, Lizenz, Prüfungsbescheid, Einspruch/Nichtigkeit.
3. **Technische Lehre zerlegen:** Merkmale, Varianten, Wirkungen, Problem, Lösung, Zeichnungen, Bezugszeichen.
4. **Rechts- und Registerlage sichern:** Anmeldetag, Priorität, Veröffentlichung, Erteilung, Einspruch, Jahresgebühren, Validierungen, Rechtsstand.
5. **Spezialskill starten:** passende Skills aus diesem Plugin und bei Recherchebedarf aus `patentrecherche`.
6. **Output bauen:** Claim Draft, Merkmalsgliederung, Rechercheauftrag, Claim Chart, Risikomemo, Antwortentwurf, Lizenz-Redline oder Fristenplan.
7. **Red Team:** offene Tatsachen, technische Unschärfen, Fristen, Quellen, Gegenargumente, Mandantenrückfragen.

## Skills

| Skill | Funktion |
| --- | --- |
| `allgemein` | Einstieg, Triage und Workflow-Routing für jedes Patentrechtsmandat |
| `patentrecht-kaltstart-interview` | kurzes Mandatsprofil und wiederverwendbare Fallarchitektur |
| `erfindungsmeldung-aufnahme-und-rueckfragen` | rohe Erfindung, Offenbarung, technische Lehre und Rückfragen erfassen |
| `patentanmeldung-anspruchsentwurf` | Anspruch 1, Unteransprüche und Varianten vorbereiten |
| `beschreibung-und-zeichnungen-pruefen` | Beschreibung, Figuren, Bezugszeichen und Offenbarungsstütze prüfen |
| `neuheit-und-erfinderische-taetigkeit` | Merkmalsanalyse, Einzeldokumentprüfung, Aufgaben-Lösungs-Ansatz |
| `stand-der-technik-recherche-workflow` | Rechercheauftrag und Übergabe an `patentrecherche` |
| `gebrauchsmuster-oder-patent-route` | Patent, Gebrauchsmuster, EP/PCT, Geheimhaltung oder defensive Veröffentlichung abwägen |
| `pruefungsbescheid-dpma-epa-erwiderung` | Beanstandungen zerlegen und Erwiderung vorbereiten |
| `freedom-to-operate-und-schutzbereich` | FTO, Schutzbereich, Rechtsstand und Design-around |
| `abmahnung-patentverletzung-verteidigung` | Abmahnung, Fristen, Unterlassung, Schutzschrift, Vergleich |
| `patentverletzung-claim-chart` | claim chart für Verletzung oder Nichtverletzung |
| `vorbenutzungsrecht-paragraph-12-patg` | Vorbenutzungsrecht, Beweisführung und Risikostrategie |
| `patentlizenzvertrag-review` | Lizenzvertragsprüfung, Red Flags und Verhandlungspositionen |
| `patentlizenzvertrag-de-en-drafting` | zweisprachige Lizenzklauseln und Term-Sheet-Umsetzung |
| `erfinderbenennung-und-arbeitnehmererfindung` | Erfinderstatus, Arbeitnehmererfindung und Vergütungsschnittstellen |
| `einspruch-epa-und-nichtigkeit-bpatg` | EPA-Einspruch und Nichtigkeitsklage strategisch vorbereiten |
| `rechtsstand-register-und-fristen` | Register, Fristen, Jahresgebühren, Validierung, Einspruchs- und Klagefenster |
| `patentportfolio-und-technikstrategie` | Portfolio, Schutzzaun, Wettbewerbsmonitoring und Produktroadmap |
| `patentrecht-redteam-qualitygate` | Qualitätskontrolle für alle patentrechtlichen Outputs |

## Pflicht-Disclaimer im Output

Jedes externe Ergebnis enthält knapp: KI-gestützte Vorprüfung; keine amtliche Recherche; Register- und Rechtsstand sind live zu verifizieren; technische Bewertung setzt vollständige Unterlagen voraus.

## Lizenz

Apache-2.0 OR MIT. Siehe Repository-Stammverzeichnis.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abmahnung-patentverletzung-verteidigung` | Verteidigt gegen Patentabmahnungen: Fristen, Unterlassungserklärung, Registerstand, Anspruchsfassung, Nichtverletzung, Rechtsbestand, Vorbenutzungsrecht, Schutzschrift, Vergleich und Mandantenkommunikation. |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Patentrecht-Plugin. Erkennt Patentanmeldung, Erfindungsmeldung, Recherche, FTO, Abmahnung, Lizenz, Einspruch, Nichtigkeit, Register- und Fristenfragen; schlägt passende Spezialskills aus di... |
| `beschreibung-und-zeichnungen-pruefen` | Prüft Beschreibung, Zeichnungen, Bezugszeichenliste und Ausführungsbeispiele einer Patentanmeldung auf Offenbarungsstütze, Verständlichkeit, Anspruchskonsistenz, Varianten und formale Lücken. |
| `einspruch-epa-und-nichtigkeit-bpatg` | Bereitet EPA-Einspruch und deutsche Nichtigkeitsklage vor: Fristen, Zuständigkeit, Angriffsmittel, Stand der Technik, unzulässige Erweiterung, Ausführbarkeit, Priorität, Hilfsanträge und Prozessstrategie. |
| `erfinderbenennung-und-arbeitnehmererfindung` | Prüft Erfinderbenennung, Rechtekette und Arbeitnehmererfindungs-Schnittstellen: wer ist Erfinder, wer ist Anmelder, Diensterfindung, freie Erfindung, Inanspruchnahme, Vergütung und Dokumentationsrisiken. |
| `erfindungsmeldung-aufnahme-und-rueckfragen` | Nimmt rohe Erfindungsideen, Skizzen, Mandantenmails und Prototypnotizen auf; trennt technische Lehre von bloßer Idee, erkennt Offenbarungsrisiken und erstellt Rückfragen für eine patentfähige Anmeldung. |
| `freedom-to-operate-und-schutzbereich` | Prüft Freedom-to-Operate und Schutzbereich: Zielprodukt, Territory, Registerstand, Anspruchsmerkmale, wortsinngemäße Verwirklichung, Äquivalenz, Design-around und Risikomemo. |
| `gebrauchsmuster-oder-patent-route` | Prüft strategisch Patent, Gebrauchsmuster, EP/PCT, Geheimhaltung, defensive Veröffentlichung oder keine Anmeldung; berücksichtigt Offenbarung, Geschwindigkeit, Kosten, Technikart und Zielmärkte. |
| `neuheit-und-erfinderische-taetigkeit` | Prüft Patentfähigkeit mit Merkmalsgliederung, Neuheit nach § 3 PatG/Art. 54 EPÜ und erfinderischer Tätigkeit nach § 4 PatG/Art. 56 EPÜ; nutzt Einzeldokumentprüfung und Aufgaben-Lösungs-Ansatz. |
| `patentanmeldung-anspruchsentwurf` | Bereitet Patentansprüche vor: Anspruch 1, Unteransprüche, Alternativausführungen, Vorrichtung/Verfahren/System/Computerprogramm, Stütze in Beschreibung und Rückfragen zur Anspruchsbreite. |
| `patentlizenzvertrag-de-en-drafting` | Setzt Patentlizenz-Term-Sheets in deutsch-englische Vertragsklauseln um; erklärt Legal-English-Begriffe im deutschen Rechtskontext und vermeidet unklare Transaktionssprache. |
| `patentlizenzvertrag-review` | Prüft Patentlizenzverträge: Schutzrechte, Territory, Field of Use, Exklusivität, Unterlizenzen, Royalties, Milestones, Improvements, Inhaberschaft, Gewährleistung, Durchsetzung, Kündigung und Insolvenzrisiken. |
| `patentportfolio-und-technikstrategie` | Unterstützt Patentportfolio- und Technikstrategie: Schutzzaun, Roadmap, Wettbewerbsmonitoring, defensive Veröffentlichungen, Anmeldepriorisierung, Länderstrategie und Budgetsteuerung. |
| `patentrecht-kaltstart-interview` | Kaltstart-Interview für Patentrechtsmandate. Erstellt ein kurzes Profil zu Mandant, Technik, Ziel, Territorien, Fristen, Dokumentenlage, Risiko und gewünschtem Output; speichert keine Geheimnisse, sondern strukturiert die nächsten Skills. |
| `patentrecht-redteam-qualitygate` | Red-Team- und Qualitätsgate für patentrechtliche Outputs: prüft Fristen, Registerstand, Anspruchsfassung, technische Annahmen, Quellen, Beweise, Zitierhygiene, offene Tatsachen und Mandantenrisiken. |
| `patentverletzung-claim-chart` | Erstellt Claim Charts für Patentverletzung oder Nichtverletzung: Anspruchsmerkmale, Produkt-/Verfahrensbelege, Fundstellen, Beweisqualität, Lücken, Äquivalenz und Ergebnisampel. |
| `patr2-anmeldeverfahren-bauleiter` | Bauleiter Patentanmeldeverfahren DPMA und EPA: Pruefverfahren, Einspruch, Beschwerde. Pruefraster fuer Erfinder und Patentanwalt. |
| `patr2-arbeitnehmererfindung-leitfaden` | Leitfaden Arbeitnehmererfindergesetz ArbnErfG: Meldepflicht, Inanspruchnahme, Verguetung, Schiedsstelle. Pruefraster fuer Arbeitgeber und Erfinder. |
| `patr2-patentverletzungsklage-spezial` | Spezialfall Patentverletzungsklage: aequivalente Verletzung, Unterlassung, Auskunft, Schadensersatz, Anspruchsberechnung Lizenzanalogie. Pruefraster fuer Klaeger und Beklagter. |
| `patr2-zwangslizenz-spezial` | Spezialfall Zwangslizenz § 24 PatG und FRAND-Verteidigung: Voraussetzungen, EuGH Huawei / ZTE, kartellrechtliche Aspekte. Pruefraster fuer SEP-Inhaber und Implementer. |
| `pruefungsbescheid-dpma-epa-erwiderung` | Bereitet Erwiderungen auf Prüfungsbescheide von DPMA oder EPA vor: Beanstandungen, Entgegenhaltungen, Anspruchsänderungen, Argumentation zu Neuheit/erfinderischer Tätigkeit und Mandantenrückfragen. |
| `rechtsstand-register-und-fristen` | Prüft Patentregister und Fristen: DPMAregister, EPO Register, nationale Validierungen, Einheitspatent, Jahresgebühren, Priorität, Veröffentlichung, Erteilung, Einspruch, Beschränkung, Nichtigkeit und Verlängerungen. |
| `stand-der-technik-recherche-workflow` | Plant eine Stand-der-Technik-Recherche: Suchbegriffe, CPC/IPC-Klassen, Datenbanken, Suchstrings, Trefferbewertung und Übergabe an das Patentrecherche-Plugin. |
| `vorbenutzungsrecht-paragraph-12-patg` | Prüft Vorbenutzungsrecht nach § 12 PatG: Besitzstand vor Anmeldung/Priorität, Benutzung oder ernsthafte Veranstaltungen, Inland, Redlichkeit, Umfang, Beweisführung und Prozessstrategie. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
