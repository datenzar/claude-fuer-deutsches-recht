# Wahlkampfrecht Praxis

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`wahlkampfrecht-praxis`) | [`wahlkampfrecht-praxis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/wahlkampfrecht-praxis.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Wahlkampfakte Morgenstadt 2026 - Landesliste, Plakatierung und digitale Lage** (`wahlkampfrecht-landtagswahl-morgenstadt-2026`) | [Gesamt-PDF lesen](../testakten/wahlkampfrecht-landtagswahl-morgenstadt-2026/gesamt-pdf/wahlkampfrecht-landtagswahl-morgenstadt-2026_gesamt.pdf) | [`testakte-wahlkampfrecht-landtagswahl-morgenstadt-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-wahlkampfrecht-landtagswahl-morgenstadt-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein großes Arbeitsplugin für demokratische Wahlkampfteams, Parteien, Kandidierende, Wahlkampfmanagerinnen, Kreisverbände, Landesgeschäftsstellen, Bundeswahlkampfstäbe, Kampagnenagenturen und anwaltliche Berater. Es verbindet Recht, Strategie und tägliche Durchführung: Plakatierung, Infostände, Veranstaltungen, Social Media, Daten, Spenden, Kandidatentraining, Krisenkommunikation, Desinformation, Wahltag und Nachbereitung.

Das Plugin soll Kampagnen handlungsfähiger machen, ohne sie zu verrohen. Es hilft bei klarer Message, schneller Lagearbeit und robustem Ground Game. Gleichzeitig zieht es rote Linien: keine Plakat-Sabotage, keine verdeckte Finanzierung, keine rechtswidrige Datennutzung, keine Desinformation, keine fingierten Accounts, keine Irreführung über Wahlverfahren und keine Nutzung staatlicher Ressourcen für Parteizwecke.

## Kaltstart

Starte mit `wahlkampf-allgemeiner-kaltstart` oder `wahlkampf-ebenen-und-wahlart-router`. Das Plugin fragt zuerst:

1. Welche Wahl: Bundestag, Europawahl, Landtag, Kommunalwahl, Bürgermeister-/Landratswahl, innerparteiliche Vorwahl oder Sonderfall?
2. Welche Rolle: Bundesstrategie, Landeswahlkampf, Kreisverband, Kandidatenteam, Agentur, Rechtsabteilung, Schatzmeisterei, Social-Media-Team oder Ehrenamtliche vor Ort?
3. Was ist der Druck: Plakatgenehmigung, Podium, Social-Media-Krise, Spende, Datenschutz, Desinformation, Schulveranstaltung, Wahltag, Behördenbrief oder Strategieplan?
4. Welche Rechtsordnung: Bund, Land, Kommune, Plattform, Datenschutz, Parteienfinanzierung, Strafrecht, Medienrecht, Versammlungsrecht?
5. Welcher Output: Schlachtplan, Freigabecheck, Behördenbrief, Briefing, Risikoampel, Presse-Q&A, Volunteer-Skript, Fristenkalender oder Incident-Log?

## Leitgedanken

- **Demokratisch kampfstark:** klare Strategie, aber keine Manipulation des Wahlverfahrens und keine organisierte Unwahrheit.
- **Recht und Taktik zusammen:** Ein Plakatstandort ist zugleich Sondernutzung, Verkehrssicherheit, Sichtbarkeit, Ehrenamtslogistik und Konfliktrisiko.
- **Resilienz vor Empörung:** Desinformation wird dokumentiert, priorisiert, entkräftet und bei Plattformen/Behörden sauber eskaliert.
- **Authentische Kandidierende:** Nicht alle Menschen sind Medienprofis. Das Plugin trainiert Verhalten unter Kamera, ohne Persönlichkeiten glattzubügeln.
- **Keine falsche Neutralität:** Amtsträger, öffentliche Einrichtungen, Schulen, Verwaltungen und Wahlorgane werden rechtlich sauber getrennt.

## Typische Workflows

| Lage | Einstiegsskills | Ergebnis |
| --- | --- | --- |
| Bundes- oder Landeswahlkampf planen | `wahlkampf-bundesstrategie-architektur`, `wahlkampf-landeswahlkampf-lagekarte`, `wahlkampf-schlachtenplan-ethik-und-taktik` | Strategiepapier, Phasenplan, Risiko-Board |
| Kreisverband muss Plakate hängen | `wahlkampf-plakatierung-genehmigung`, `wahlkampf-plakatstandorte-matrix`, `wahlkampf-fremdplakate-nicht-anruehren` | Standortliste, Teambriefing, Ordnungsamtsmail |
| Social-Media-Krise | `wahlkampf-rapid-response-room`, `wahlkampf-viraler-clip-notfall`, `wahlkampf-faktencheck-gegenrede` | Krisenlog, Q&A, Antwortleiter |
| Politische Online-Werbung | `wahlkampf-eu-2024-900-politische-werbung`, `wahlkampf-targeting-dsgvo`, `wahlkampf-ad-library-transparenz` | Transparenznotiz, Freigabevermerk, Targeting-Ampel |
| Podium mit problematischem Gegner | `wahlkampf-podium-teilnahmeentscheidung`, `wahlkampf-keine-buehne-aber-nicht-fehlen`, `wahlkampf-kandidatenbriefing-kamera` | Teilnahmevermerk, Sprechzettel, Schutzplan |
| Schulen, Jugend, öffentliche Einrichtungen | `wahlkampf-schulen-und-jugendformate`, `wahlkampf-staatliche-neutralitaet`, `wahlkampf-amtstraeger-ressourcen` | Einladungsschreiben, Neutralitätsprüfung, Rollenabgrenzung |
| Wahltag und Wahlraum | `wahlkampf-wahlraum-propagandaverbot`, `wahlkampf-wahlbeobachtung-und-wahltag`, `wahlkampf-briefwahlkommunikation` | Wahltagskarte, Beobachterbriefing, Eskalationspfad |

## Amtliche und frei prüfbare Startquellen

- [Grundgesetz](https://www.gesetze-im-internet.de/gg/) - insbesondere Art. 5, Art. 21 und Wahlrechtsgrundsätze.
- [Bundeswahlgesetz](https://www.gesetze-im-internet.de/bwahlg/) und [Bundeswahlordnung](https://www.gesetze-im-internet.de/bwo_1985/) für Bundestagswahlen.
- [Europawahlgesetz](https://www.gesetze-im-internet.de/euwg/) und [Europawahlordnung](https://www.gesetze-im-internet.de/euwo_1988/) für Europawahlen.
- [Parteiengesetz](https://www.gesetze-im-internet.de/partg/) für Parteienfinanzierung, Spenden, Rechenschaft und Parteiorganisation.
- [Strafgesetzbuch](https://www.gesetze-im-internet.de/stgb/) zu Wahlstraftaten, Nötigung, Beleidigung, Sachbeschädigung und Urkundenthemen.
- [Wahlprüfungsgesetz](https://www.gesetze-im-internet.de/wahlprg/) für Wahlprüfung nach Bundestagswahlen.
- [Bundeswahlleiterin: Wahlwerbung](https://www.bundeswahlleiterin.de/service/glossar/w/wahlwerbung.html), [unzulässige Wahlpropaganda](https://www.bundeswahlleiterin.de/service/glossar/w/wahlpropaganda-unzulaessige.html) und [Fakten gegen Desinformation](https://www.bundeswahlleiterin.de/bundestagswahlen/2025/fakten-desinformation.html).
- [Deutscher Bundestag: Parteienfinanzierung](https://www.bundestag.de/parlament/praesidium/parteienfinanzierung) und [Parteispenden über 35.000 EUR](https://www.bundestag.de/parteispenden).
- [EU-Kommission: Transparency and targeting of political advertising](https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/democracy-eu-citizenship-anti-corruption/democracy-and-electoral-rights/transparency-and-targeting-political-advertising_en) zur Verordnung (EU) 2024/900, die seit 10. Oktober 2025 voll gilt.
- [DSGVO](https://eur-lex.europa.eu/eli/reg/2016/679/oj) und [BDSG](https://www.gesetze-im-internet.de/bdsg_2018/) für Datenverarbeitung im Wahlkampf.
- Lokale Plakatierungs-, Sondernutzungs- und Veranstaltungsregeln der jeweiligen Gemeinde; diese müssen immer aktuell am konkreten Ort geprüft werden.

## Quellenhygiene

Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugänglicher Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen. Bei Landeswahlrecht, Plakatierungsfristen, Sondernutzung, Schulen und Kommunalrecht zwingend die konkrete Gemeinde und das Bundesland live prüfen.

## Datenschutz und Kampagnensicherheit

Keine echten Wählerdaten, Mitgliederdaten, Spenderlisten, Social-Media-Profile, Gesundheitsdaten, politische Meinungsdaten oder internen Kampagnengeheimnisse in ungeprüfte Systeme laden. Das Plugin ist ein Arbeits- und Demonstrationsrahmen; produktiver Einsatz braucht Datenschutz-, Berufsrechts-, Parteienfinanzierungs- und IT-Sicherheitsprüfung.

## Lizenz

Apache-2.0 OR MIT. Siehe Repository-Stammverzeichnis.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 118 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `wahlkampf-72-stunden-sprint` | Wahlkampfrecht Praxis: die letzten 72 Stunden vor Wahl, Debatte oder Krise planen. |
| `wahlkampf-ad-library-transparenz` | Wahlkampfrecht Praxis: Anzeigenbibliothek- und Transparenznotizen erstellen. |
| `wahlkampf-agenturvertrag-compliance` | Wahlkampfrecht Praxis: Agentur-, Media- und Beratungsvertraege im Wahlkampf pruefen. |
| `wahlkampf-aktenplan-und-beweisarchiv` | Wahlkampfrecht Praxis: Kampagnenakte so strukturieren, dass sie später prüfbar bleibt. |
| `wahlkampf-allgemeiner-kaltstart` | Wahlkampfrecht Praxis: Kaltstart fuer jede Wahlkampflage mit Routing zu Recht, Strategie, Digital, Plakatierung, Finanzen oder Krise. |
| `wahlkampf-amtstraeger-ressourcen` | Wahlkampfrecht Praxis: Auftritte von Regierungsmitgliedern, Buergermeistern und Abgeordneten pruefen. |
| `wahlkampf-angriff-auf-wahlleitung-vermeiden` | Wahlkampfrecht Praxis: Kritik an Wahlorganisation ohne Vertrauenszerstoerung formulieren. |
| `wahlkampf-arbeitsrecht-kampagnenteam` | Wahlkampfrecht Praxis: Beschaeftigung, Minijobs, Freelancer und Ehrenamt im Wahlkampf pruefen. |
| `wahlkampf-archivierung-screenshots` | Wahlkampfrecht Praxis: digitale Beweise fuer schnelle Praxis sichern. |
| `wahlkampf-asymmetrische-demobilisierung` | Wahlkampfrecht Praxis: Demobilisierungsstrategien analysieren. |
| `wahlkampf-barrierefreie-und-mehrsprachige-information` | Wahlkampfrecht Praxis: mehrsprachige und barrierefreie Kampagneninformationen rechtssicher planen. |
| `wahlkampf-barrierefreiheit-und-inklusion` | Wahlkampfrecht Praxis: barrierearme Wahlkampfkommunikation und Veranstaltungen planen. |
| `wahlkampf-bots-und-inauthentisches-verhalten` | Wahlkampfrecht Praxis: koordinierte inauthentische Kommunikation erkennen und vermeiden. |
| `wahlkampf-briefkasten-flyer` | Wahlkampfrecht Praxis: Flyer- und Briefkastenaktionen pruefen. |
| `wahlkampf-briefwahlkommunikation` | Wahlkampfrecht Praxis: Kommunikation ueber Briefwahl ohne Irrefuehrung pruefen. |
| `wahlkampf-buergerdialog-schwierige-fragen` | Wahlkampfrecht Praxis: Buergerdialoge mit unangenehmen, aber legitimen Fragen vorbereiten. |
| `wahlkampf-bundesstrategie-architektur` | Wahlkampfrecht Praxis: Bundeswahlkampf als rechtlich sauberes Operating Model bauen. |
| `wahlkampf-community-management` | Wahlkampfrecht Praxis: Community Manager fuer Kommentare, Beleidigungen und Fragen briefen. |
| `wahlkampf-compliance-schulung-vorstand` | Wahlkampfrecht Praxis: kurze Compliance-Schulung fuer Vorstand und Kampagnenteam erstellen. |
| `wahlkampf-cybersicherheit-kampagne` | Wahlkampfrecht Praxis: Kampagnen-IT gegen Accountuebernahmen und Leaks sichern. |
| `wahlkampf-datenschutz-folgenabschaetzung-politische-daten` | Wahlkampfrecht Praxis: pruefen, ob politische Datenverarbeitung eine DSFA braucht. |
| `wahlkampf-debattenvorbereitung` | Wahlkampfrecht Praxis: Kandidierende auf Debatte, Townhall oder TV-Runde vorbereiten. |
| `wahlkampf-deepfake-und-ki-kennzeichnung` | Wahlkampfrecht Praxis: KI-generierte Inhalte, Deepfakes und synthetische Stimmen pruefen. |
| `wahlkampf-desinformation-monitoring` | Wahlkampfrecht Praxis: Desinformation und Manipulationsnarrative monitoren. |
| `wahlkampf-ebenen-und-wahlart-router` | Wahlkampfrecht Praxis: Bundestag, Europa, Landtag, Kommunalwahl, Buergermeisterwahl und Sonderlagen sauber unterscheiden. |
| `wahlkampf-ehrenamtliche-schulen` | Wahlkampfrecht Praxis: Ehrenamtliche schnell und verstaendlich kampagnentauglich machen. |
| `wahlkampf-eu-2024-900-politische-werbung` | Wahlkampfrecht Praxis: politische Werbung nach EU-Verordnung 2024/900 pruefen. |
| `wahlkampf-faktencheck-gegenrede` | Wahlkampfrecht Praxis: sachliche Gegenrede gegen falsche Wahlkampfnarrative erstellen. |
| `wahlkampf-flooding-gegenrede-statt-muell` | Wahlkampfrecht Praxis: auf Informationsflutung reagieren, ohne selbst Muell zu produzieren. |
| `wahlkampf-foreign-interference-lage` | Wahlkampfrecht Praxis: Anzeichen auslaendischer Einflussnahme bewerten. |
| `wahlkampf-foto-im-wahlraum-und-stimmzettel` | Wahlkampfrecht Praxis: Selfies, Stimmzettelfotos und Wahlgeheimnisrisiken pruefen. |
| `wahlkampf-fraktion-partei-trennung` | Wahlkampfrecht Praxis: Fraktions-, Amts- und Parteimittel sauber trennen. |
| `wahlkampf-freiwillige-und-aufwandsersatz` | Wahlkampfrecht Praxis: Aufwandsersatz, Reisekosten und geldwerte Vorteile fuer Helfer pruefen. |
| `wahlkampf-fremdplakate-nicht-anruehren` | Wahlkampfrecht Praxis: Teams briefen, fremde Plakate weder abzuhaengen noch zu ueberkleben. |
| `wahlkampf-gegnerkritik-meinungsfreiheit` | Wahlkampfrecht Praxis: scharfe Kritik an Gegnern ohne Beleidigungs- oder Falschtatsachenrisiko pruefen. |
| `wahlkampf-gewerkschaften-verbaende-kirchen` | Wahlkampfrecht Praxis: Zusammenarbeit mit Verbaenden, Gewerkschaften, Kirchen und Initiativen pruefen. |
| `wahlkampf-giveaways-waehlerbestechung` | Wahlkampfrecht Praxis: Geschenke, Gewinnspiele, Essen, Getraenke und Rabatte im Wahlkampf pruefen. |
| `wahlkampf-grossspenden-sofortmeldung` | Wahlkampfrecht Praxis: Grossspenden ueber der aktuellen Sofortmeldeschwelle pruefen. |
| `wahlkampf-hausrecht-privatraeume` | Wahlkampfrecht Praxis: Wahlkampftermine in privaten Hallen, Vereinen und Betrieben pruefen. |
| `wahlkampf-haustuerwahlkampf` | Wahlkampfrecht Praxis: Haustuerwahlkampf rechtlich und praktisch sauber machen. |
| `wahlkampf-influencer-und-unterstuetzer` | Wahlkampfrecht Praxis: Influencer-, Unterstuetzer- und Testimonialkampagnen pruefen. |
| `wahlkampf-infostand-sondernutzung` | Wahlkampfrecht Praxis: Infostaende auf oeffentlichen Flaechen planen. |
| `wahlkampf-interne-chatdisziplin` | Wahlkampfrecht Praxis: interne Chats so briefen, dass sie nicht zur Brandquelle werden. |
| `wahlkampf-kandidaten-altposts-screening` | Wahlkampfrecht Praxis: Altposts und digitale Spuren von Kandidierenden screenen. |
| `wahlkampf-kandidatenbriefing-kamera` | Wahlkampfrecht Praxis: Kandidierende fuer Kamera, Smartphone-Clips und spontane Fragen trainieren. |
| `wahlkampf-kandidatenteam-intake` | Wahlkampfrecht Praxis: Kandidatenteam aufnehmen und biografische, digitale und organisatorische Schwachstellen erkennen. |
| `wahlkampf-kandidierenden-fuersorge` | Wahlkampfrecht Praxis: Belastung, Angriffe und Burnout in Kandidatenteams ernst nehmen. |
| `wahlkampf-kassenpruefung-kreisverband` | Wahlkampfrecht Praxis: Kreisverbaenden bei sauberer Kasse waehrend intensiver Kampagnen helfen. |
| `wahlkampf-keine-buehne-aber-nicht-fehlen` | Wahlkampfrecht Praxis: Alternativen entwickeln, wenn ein Podium nicht besucht werden soll. |
| `wahlkampf-koalitionssignale-und-rote-linien` | Wahlkampfrecht Praxis: Koalitionssignale im Wahlkampf strategisch und rechtlich sauber formulieren. |
| `wahlkampf-kommunalwahlkampf-groundgame` | Wahlkampfrecht Praxis: Kommunalwahlkampf in Infostaende, Haustuer, Plakate, lokale Termine und Wahlvorschlaege uebersetzen. |
| `wahlkampf-kostenversprechen-und-finanzierbarkeit` | Wahlkampfrecht Praxis: Kosten- und Finanzierungsversprechen kommunikativ und rechtlich absichern. |
| `wahlkampf-krisenstatement-fehler-eigener-leute` | Wahlkampfrecht Praxis: auf Fehltritte eigener Kandidierender oder Helfer reagieren. |
| `wahlkampf-lagebild-medienresonanz` | Wahlkampfrecht Praxis: Medien-, Social- und Vor-Ort-Lage ohne Panikmetriken verdichten. |
| `wahlkampf-landeslisten-und-direktkandidaten` | Wahlkampfrecht Praxis: Landeslisten, Kreiswahlvorschlaege und Direktkandidaturen ordnen. |
| `wahlkampf-landesrecht-plakatierung-livecheck` | Wahlkampfrecht Praxis: Livecheck von Landes- und Kommunalrecht bei Plakatierung erzwingen. |
| `wahlkampf-landeswahlkampf-lagekarte` | Wahlkampfrecht Praxis: Landtagswahlkampf mit Landesrecht, Kreisverbaenden und lokalen Behoerden strukturieren. |
| `wahlkampf-lautsprecher-fahrzeug` | Wahlkampfrecht Praxis: Lautsprecherwagen und mobile Wahlwerbung pruefen. |
| `wahlkampf-leak-und-hack-notfall` | Wahlkampfrecht Praxis: auf Leaks, Hacks und veroeffentlichte interne Dokumente reagieren. |
| `wahlkampf-lokale-buendnisse-und-listen` | Wahlkampfrecht Praxis: lokale Buendnisse, Listenverbindungen und Unterstuetzungserklaerungen pruefen. |
| `wahlkampf-marken-und-fremdlogos` | Wahlkampfrecht Praxis: fremde Marken, Unternehmenslogos und Behoerdenanmutung pruefen. |
| `wahlkampf-memes-satire-risiko` | Wahlkampfrecht Praxis: Memes, Satire und Bildmontagen pruefen. |
| `wahlkampf-message-house-authentizitaet` | Wahlkampfrecht Praxis: Message House entwickeln, das Kandidierende nicht kuenstlich verbiegt. |
| `wahlkampf-minderjaehrige-und-fotos` | Wahlkampfrecht Praxis: Bilder, Schulformate und Daten Minderjaehriger pruefen. |
| `wahlkampf-nachwahl-evaluation` | Wahlkampfrecht Praxis: Nachwahl-Evaluation ohne Selbstbetrug erstellen. |
| `wahlkampf-negative-campaigning-grenzen` | Wahlkampfrecht Praxis: Negative Campaigning auf Wahrheit, Fairness und Wirkung pruefen. |
| `wahlkampf-newsletter-messenger-sms` | Wahlkampfrecht Praxis: Newsletter, WhatsApp, Telegram, Signal und SMS-Wahlkampf pruefen. |
| `wahlkampf-oeffentliche-einrichtungen-nutzung` | Wahlkampfrecht Praxis: Nutzung öffentlicher Einrichtungen für Wahlkampf prüfen. |
| `wahlkampf-opposition-research-compliance` | Wahlkampfrecht Praxis: Opposition Research rechtlich und ethisch begrenzen. |
| `wahlkampf-ordner-und-sicherheit` | Wahlkampfrecht Praxis: Ordner, Security und Deeskalation bei Wahlkampfterminen organisieren. |
| `wahlkampf-parteieigenschaft-bundeswahlausschuss` | Wahlkampfrecht Praxis: Parteieigenschaft und Beteiligungsanzeige vorbereiten. |
| `wahlkampf-plakat-vandalismus-beweissicherung` | Wahlkampfrecht Praxis: Beweissicherung bei beschaedigten Wahlplakaten organisieren. |
| `wahlkampf-plakatierung-genehmigung` | Wahlkampfrecht Praxis: kommunale Plakatierung und Sondernutzung rechtlich praktisch begleiten. |
| `wahlkampf-plakatstandorte-matrix` | Wahlkampfrecht Praxis: Standortmatrix fuer Plakate mit Sichtbarkeit und Rechtssicherheit erstellen. |
| `wahlkampf-plattformmeldung-dsa` | Wahlkampfrecht Praxis: Plattformmeldewege und DSA-Mechanismen bei rechtswidrigen Inhalten nutzen. |
| `wahlkampf-podium-teilnahmeentscheidung` | Wahlkampfrecht Praxis: Teilnahme an Podien mit problematischen Mitbewerbern entscheiden. |
| `wahlkampf-polizei-und-ordnungsamt-kommunikation` | Wahlkampfrecht Praxis: robuste und freundliche Behoerdenkommunikation formulieren. |
| `wahlkampf-presseanfrage-antwortleiter` | Wahlkampfrecht Praxis: Presseanfragen in Sofortantwort, Hintergrund, Kein-Kommentar und Rechtspruefung sortieren. |
| `wahlkampf-presserecht-richtigstellung` | Wahlkampfrecht Praxis: Richtigstellung, Gegendarstellung und Unterlassung im Wahlkampf einordnen. |
| `wahlkampf-rapid-response-room` | Wahlkampfrecht Praxis: akute Wahlkampfkrisen in Social Media, Presse und vor Ort in einen handlungsfähigen Rapid-Response-Prozess übersetzen. |
| `wahlkampf-rechenschaftsbericht-vorbereitung` | Wahlkampfrecht Praxis: Wahlkampfbelege fuer den Rechenschaftsbericht aufbereiten. |
| `wahlkampf-rechtsfreigabe-gate` | Wahlkampfrecht Praxis: schnellen Freigabeprozess fuer Plakate, Posts, Ads, Veranstaltungen und Spenden bauen. |
| `wahlkampf-risiko-register` | Wahlkampfrecht Praxis: lebendes Risiko-Register fuer Wahlkampfleitung und Rechtsberatung fuehren. |
| `wahlkampf-rumor-control-center` | Wahlkampfrecht Praxis: Geruechtekontrolle fuer Teams und Kandidierende einrichten. |
| `wahlkampf-satellitenkampagne-durch-verein` | Wahlkampfrecht Praxis: Satellitenkampagne eines Vereins oder Dritten auf Zurechnung und Spendenrecht prüfen. |
| `wahlkampf-schlachtenplan-ethik-und-taktik` | Wahlkampfrecht Praxis: harten, aber demokratisch sauberen Kampagnenplan entwickeln. |
| `wahlkampf-schulen-und-jugendformate` | Wahlkampfrecht Praxis: Wahlkampfauftritte an Schulen, Jugendforen und Bildungseinrichtungen pruefen. |
| `wahlkampf-sicherheitslage-kandidierende` | Wahlkampfrecht Praxis: Schutzkonzept fuer Kandidierende und Wahlkampfteams erstellen. |
| `wahlkampf-social-media-redaktionsplan` | Wahlkampfrecht Praxis: rechtssicheren Redaktionsplan fuer Social Media bauen. |
| `wahlkampf-spendenannahme-pruefung` | Wahlkampfrecht Praxis: Parteispenden und Sachleistungen vor Annahme pruefen. |
| `wahlkampf-sponsoring-parteienrecht` | Wahlkampfrecht Praxis: Sponsoring, Anzeigen, Messestaende und geldwerte Vorteile pruefen. |
| `wahlkampf-sprachregelung-schnellkarte` | Wahlkampfrecht Praxis: Sprachregelungen fuer Kandidierende, Presse und Ehrenamt erstellen. |
| `wahlkampf-staatliche-neutralitaet` | Wahlkampfrecht Praxis: staatliche Neutralität bei Schulen, Rathäusern, Amtsinhabern, Behördenkanälen und öffentlichen Einrichtungen prüfen. |
| `wahlkampf-taegliches-briefing` | Wahlkampfrecht Praxis: taegliches Lagebriefing fuer Spitze, Stab und Kreisverbaende erstellen. |
| `wahlkampf-targeting-dsgvo` | Wahlkampfrecht Praxis: Targeting und Zustellung politischer Werbung datenschutzrechtlich pruefen. |
| `wahlkampf-tracking-pixel-cookies` | Wahlkampfrecht Praxis: Kampagnenwebsite, Pixel, Conversiontracking und Cookies pruefen. |
| `wahlkampf-ueberkleben-sachbeschaedigung` | Wahlkampfrecht Praxis: Ueberkleben, Beschmieren oder Entfernen fremder Plakate pruefen. |
| `wahlkampf-umfragen-und-prognosen` | Wahlkampfrecht Praxis: Umfragen, Projektionen und interne Trackings richtig verwenden. |
| `wahlkampf-umgang-mit-provokateuren` | Wahlkampfrecht Praxis: Umgang mit Provokateuren bei Veranstaltungen und Strassenwahlkampf planen. |
| `wahlkampf-unterstuetzungsunterschriften` | Wahlkampfrecht Praxis: Sammlung von Unterstuetzungsunterschriften pruefen. |
| `wahlkampf-urheberrecht-musik-bilder-clips` | Wahlkampfrecht Praxis: Musik, Fotos, Stockbilder, Clips und Logos in Wahlwerbung pruefen. |
| `wahlkampf-veranstaltungslogistik` | Wahlkampfrecht Praxis: Kundgebung, Saalveranstaltung oder Marktplatztermin planen. |
| `wahlkampf-vereine-unterstuetzer-dritte` | Wahlkampfrecht Praxis: Unterstuetzung durch Vereine, Initiativen und Drittkampagnen pruefen. |
| `wahlkampf-versammlungsrecht-schnittstelle` | Wahlkampfrecht Praxis: politische Kundgebungen ins Versammlungsrecht routen. |
| `wahlkampf-viraler-clip-notfall` | Wahlkampfrecht Praxis: auf unguenstigen viralen Clip ohne Panik reagieren. |
| `wahlkampf-waehlerdaten-und-listen` | Wahlkampfrecht Praxis: Waehler-, Mitglieder-, Interessenten- und Volunteerlisten pruefen. |
| `wahlkampf-wahl-o-mat-und-thesen` | Wahlkampfrecht Praxis: Antworten auf Wahl-O-Mat- oder Kandidatencheck-Thesen koordinieren. |
| `wahlkampf-wahlbeobachtung-und-wahltag` | Wahlkampfrecht Praxis: Wahlbeobachtung ohne Eingriff in Wahlhandlung briefen. |
| `wahlkampf-wahlkampf-in-vereinen-und-betrieben` | Wahlkampfrecht Praxis: Wahlkampf in Vereinen, Betrieben und halböffentlichen Räumen prüfen. |
| `wahlkampf-wahlkampfkosten-budget` | Wahlkampfrecht Praxis: Budget, Kostenstellen und Rechenschaftslogik bauen. |
| `wahlkampf-wahlprogramm-und-faktencheck` | Wahlkampfrecht Praxis: Wahlprogramm und Kurzforderungen auf belegbare Tatsachenbasis pruefen. |
| `wahlkampf-wahlpruefung-nachwahl` | Wahlkampfrecht Praxis: Wahlpruefung und Einspruch nach Wahlfehlern vorbereiten. |
| `wahlkampf-wahlraum-propagandaverbot` | Wahlkampfrecht Praxis: Wahlwerbung am Wahltag im und am Wahlgebaeude pruefen. |
| `wahlkampf-wahlstraftaten-stgb` | Wahlkampfrecht Praxis: Wahlstraftaten und strafrechtliche Nebenrisiken routen. |
| `wahlkampf-wahltag-krisenkarte` | Wahlkampfrecht Praxis: Krisenkarte fuer Wahlsonntag erstellen. |
| `wahlkampf-wahlverfahren-falschinfo` | Wahlkampfrecht Praxis: Falschinformationen ueber Wahltermin, Briefwahl, Stimmzettel oder Wahlraeume beantworten. |
| `wahlkampf-wahlvorschlaege-fristen` | Wahlkampfrecht Praxis: Wahlvorschlaege, Beteiligungsanzeige und Fristen pruefen. |
| `wahlkampf-war-room-betriebsmodell` | Wahlkampfrecht Praxis: Wahlkampfzentrale mit Entscheidungswegen, Freigaben und Eskalation aufsetzen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
