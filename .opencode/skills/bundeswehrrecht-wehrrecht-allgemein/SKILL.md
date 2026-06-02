---
name: bundeswehrrecht-wehrrecht-allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Bundeswehrrecht und Wehrrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, erkennt stumme Uploads und schlägt passende Spezial-Skills aus diesem Plugin vor."
---

> Opencode-Port von `bundeswehrrecht-wehrrecht/skills/allgemein/SKILL.md`. Urspruenglicher Skill-Name: `allgemein`.

<!-- konvers-stil-v1 -->

# Bundeswehrrecht und Wehrrecht — Allgemein

## Sofortstart
Dieses Allgemein-Skill ist der Empfangstresen und Projektleiter des Plugins **Bundeswehrrecht und Wehrrecht**. Es soll den Nutzer nicht belehren, sondern schnell arbeitsfähig machen: erst die Lage erfassen, dann den passenden Pfad wählen, dann direkt einen verwertbaren Output erzeugen.

**Plugin-Fokus:** Bundeswehrrecht mit Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung, Wehrpflichtgesetz, Reservistenrecht, Soldatenversorgung, Befehlsrecht, Fürsorge und Rechtsschutz.

## Bei stummem Upload
Wenn der Nutzer nur ein Dokument, Bild, PDF, Vertrag, Bescheid, Tabellenwerk, E-Mail, Registerauszug oder Aktenkonvolut hochlädt, behandle das als Auftrag.

1. **Erkannt:** Dokumentart, Absender, Datum, Aktenzeichen, Beteiligte und Lebenssachverhalt nennen.
2. **Frist zuerst:** Zustellung, Rechtsbehelf, Behördenfrist, Zahlungsziel, Ausschlussfrist oder Verjährungsrisiko markieren.
3. **Einordnung:** Rechtsgebiet, Normengruppe, Behörde/Gericht und Arbeitstyp bestimmen.
4. **Primärer Pfad:** den wahrscheinlich passenden Spezial-Skill aus diesem Plugin nennen und bei eindeutigem Treffer direkt anwenden.
5. **Nur eine Rückfrage:** nur wenn ohne die Antwort ein falscher nächster Schritt droht.

## Intake in 60 Sekunden
- Wer fragt: Anwalt, Rechtsabteilung, Unternehmen, Patient, Apotheke, Krankenhaus, Verbraucher, Behörde, Soldat, Familie oder Verband?
- Was soll entstehen: Kurzprüfung, Memo, Schriftsatz, Antrag, Anzeige, Stellungnahme, Checkliste, Berechnung, Vertragsklausel, Behördenbrief oder Mandantenübersetzung?
- Was eilt: Frist, Termin, Zustellung, Anhörung, Ausschlussfrist, Verjährung, Bußgeld, Widerruf, Gebührenrisiko oder Verfahrensschritt?
- Welche Unterlagen liegen vor: Verträge, Bescheide, Rechnungen, Tabellen, Registerauszüge, Leitlinien, Formulare, E-Mails, Fotos, Chatverläufe?
- Was ist unsicher: Tatsachen, Zahlen, Zuständigkeit, Rechtslage, technische Daten, Marktdefinition, medizinischer Sachverhalt oder Familien-/Versorgungsverlauf?

## Arbeitsmodus
- **Schnelltriage:** Frist, Risiko, nächster Schritt.
- **Aktenmodus:** Dokumente sortieren, Timeline, Belegmatrix und Lückenliste.
- **Prüfmodus:** Tatbestand, Rechtsfolge, Gegenargumente, Risikoampel.
- **Entwurfsmodus:** Antrag, Schriftsatz, Vertragsklausel, Behördenbrief, Mandantenmail, Vorstandsvorlage.
- **Red-Team:** Ergebnis auf Halluzinationen, Quellen, Fristen, Zuständigkeit, Zahlen und Ton prüfen.

## Passende Einstiegsrouten
| Skill | Wann? |
| --- | --- |
| `soldatengesetz-rechtsstellung-grundpflichten` | Soldatengesetz Rechtsstellung Grundpflichten |
| `pflicht-zum-treuen-dienen-7-sg` | Pflicht zum treuen Dienen § 7 SG |
| `gehorsam-befehl-und-rechtswidriger-befehl` | Gehorsam Befehl und rechtswidriger Befehl |
| `kameradschaft-achtungs-und-vertrauenspflicht` | Kameradschaft Achtungs- und Vertrauenspflicht |
| `politische-betaetigung-maessigung-neutralitaet` | Politische Betätigung Mäßigung Neutralität |
| `nebentaetigkeit-geschenkannahme-compliance` | Nebentätigkeit Geschenkannahme Compliance |
| `dienstzeit-soldat-auf-zeit-berufssoldat-fwdl` | Dienstzeit Soldat auf Zeit Berufssoldat FWDL |
| `ernennung-dienstgrad-laufbahnrecht` | Ernennung Dienstgrad Laufbahnrecht |
| `versetzung-kommandierung-abordnung` | Versetzung Kommandierung Abordnung |
| `beurteilung-konkurrentenstreit-auswahlentscheidung` | Beurteilung Konkurrentenstreit Auswahlentscheidung |
| `wehrbeschwerdeordnung-beschwerde-frist-form` | Wehrbeschwerdeordnung Beschwerde Frist Form |
| `weitere-beschwerde-und-gerichtlicher-antrag-wehrdienstgericht` | Weitere Beschwerde und gerichtlicher Antrag Wehrdienstgericht |
| `truppendienstgericht-zustaendigkeit-verfahren` | Truppendienstgericht Zuständigkeit Verfahren |
| `wehrdisziplinarordnung-einfache-disziplinarmassnahme` | Wehrdisziplinarordnung einfache Disziplinarmaßnahme |
| `gerichtliches-disziplinarverfahren-soldat` | Gerichtliches Disziplinarverfahren Soldat |
| `vorlaeufige-dienstenthebung-einbehaltung-bezuege` | Vorläufige Dienstenthebung Einbehaltung Bezüge |
| `befehl-verweigern-gewissensnot-rechtswidrigkeit` | Befehl verweigern Gewissensnot Rechtswidrigkeit |
| `wehrstrafrecht-fahnenflucht-gehorsamsverweigerung-schnittstelle` | Wehrstrafrecht Fahnenflucht Gehorsamsverweigerung Schnittstelle |
| `einsatzunfall-wehrdienstbeschaedigung` | Einsatzunfall Wehrdienstbeschädigung |
| `soldatenversorgungsgesetz-beschaedigtenversorgung` | Soldatenversorgungsgesetz Beschädigtenversorgung |
| `dienstunfaehigkeit-entlassung-zurruhesetzung` | Dienstunfähigkeit Entlassung Zurruhesetzung |
| `ptbs-einsatzfolge-beweisfuehrung` | PTBS Einsatzfolge Beweisführung |
| `gleichstellung-diskriminierung-soldatinnen-soldaten` | Gleichstellung Diskriminierung Soldatinnen Soldaten |
| `sexuelle-belaestigung-beschwerde-schutzpflicht` | Sexuelle Belästigung Beschwerde Schutzpflicht |
| `mobbing-fuersorgepflicht-bundeswehr` | Mobbing Fürsorgepflicht Bundeswehr |
| `personalakte-einsicht-datenschutz` | Personalakte Einsicht Datenschutz |
| `geheimschutz-sicherheitsueberpruefung-sueg` | Geheimschutz Sicherheitsüberprüfung SÜG |
| `reservistendienst-dienstleistungspflicht` | Reservistendienst Dienstleistungspflicht |
| `wehrpflichtgesetz-spannungs-und-verteidigungsfall` | Wehrpflichtgesetz Spannungs- und Verteidigungsfall |
| `kriegsdienstverweigerung-verfahren` | Kriegsdienstverweigerung Verfahren |
| `wehruebungen-heranziehungsbescheid` | Wehrübungen Heranziehungsbescheid |
| `unterhaltssicherung-reservisten` | Unterhaltssicherung Reservisten |
| `auslandseinsatz-mandat-einsatzregeln` | Auslandseinsatz Mandat Einsatzregeln |
| `statusrechte-im-einsatz-urlaub-betreuung` | Statusrechte im Einsatz Urlaub Betreuung |
| `schadenersatz-regress-dienstunfall-material` | Schadenersatz Regress Dienstunfall Material |

## Quellenregel
Vor tragenden Aussagen immer aktuelle Normtexte, amtliche Behördenseiten, EU-Texte oder frei zugängliche Entscheidungen prüfen. Keine BeckRS-/juris-/Kommentarzitate aus Modellwissen. Wenn eine Quelle nicht verifizierbar ist, deutlich sagen und nicht als Beleg verwenden.

<!-- BEGIN ACTUAL-SKILL-ROUTING -->

## Aktuelle Anschluss-Skills

Diese Tabelle wird aus dem tatsächlichen Skillbestand des Plugins gebildet. Wenn ein Nutzer nach dem Einstieg weitergeleitet werden soll, nimm bevorzugt diese Namen.

| Skill | Wann einsetzen? |
| --- | --- |
| `aerztliche-begutachtung-dienstfaehigkeit` | Ärztliche Begutachtung Dienstfähigkeit: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinaro... |
| `akteneinsicht-wbo-wdo` | Akteneinsicht WBO WDO: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehr... |
| `arbeitsrecht-zivile-bundeswehrbeschaeftigte` | Arbeitsrecht zivile Bundeswehrbeschäftigte: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszipli... |
| `ausbildung-studium-bundeswehr-rueckforderung-ausbildungskosten` | Ausbildung Studium Bundeswehr Rückforderung Ausbildungskosten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeor... |
| `auslandseinsatz-mandat-einsatzregeln` | Auslandseinsatz Mandat Einsatzregeln: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarord... |
| `beamtenrecht-bundeswehrverwaltung-abgrenzung` | Beamtenrecht Bundeswehrverwaltung Abgrenzung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszip... |
| `befehl-verweigern-gewissensnot-rechtswidrigkeit` | Befehl verweigern Gewissensnot Rechtswidrigkeit: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdis... |
| `beschwerde-fristen-sofortcheck` | Workflow zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Beschwerde Fristen Sofortcheck. |
| `beschwerde-gegen-beurteilung-und-laufbahnentscheidung` | Beschwerde gegen Beurteilung und Laufbahnentscheidung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, W... |
| `besoldung-zulagen-auslandsverwendungszuschlag` | Besoldung Zulagen Auslandsverwendungszuschlag: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszi... |
| `beurteilung-konkurrentenstreit-auswahlentscheidung` | Beurteilung Konkurrentenstreit Auswahlentscheidung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehr... |
| `bundesverwaltungsgericht-wehrdienstsenate` | Bundesverwaltungsgericht Wehrdienstsenate: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplin... |
| `dienstunfaehigkeit-entlassung-zurruhesetzung` | Dienstunfähigkeit Entlassung Zurruhesetzung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszipl... |
| `dienstzeit-soldat-auf-zeit-berufssoldat-fwdl` | Dienstzeit Soldat auf Zeit Berufssoldat FWDL: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszip... |
| `disziplinarverfahren-intake` | Workflow zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Disziplinarverfahren Intake. |
| `eilverfahren-konkurrentenstreit-wehrdienstsenat` | Eilverfahren Konkurrentenstreit Wehrdienstsenat: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdis... |
| `einsatz-unfall-versorgung-dokumentenplan` | Workflow zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Einsatz Unfall Versorgung Dokumentenplan. |
| `einsatzunfall-wehrdienstbeschaedigung` | Einsatzunfall Wehrdienstbeschädigung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarord... |
| `entlassung-auf-eigenen-antrag` | Entlassung auf eigenen Antrag: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 20... |
| `ernennung-dienstgrad-laufbahnrecht` | Ernennung Dienstgrad Laufbahnrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnu... |
| `extremismus-verdachtsfall-sicherheitsrecht` | Extremismus Verdachtsfall Sicherheitsrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszipli... |
| `fristenkalender-bundeswehrrecht` | Fristenkalender Bundeswehrrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung... |
| `geheimschutz-sicherheitsueberpruefung-sueg` | Geheimschutz Sicherheitsüberprüfung SÜG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinar... |
| `gehorsam-befehl-und-rechtswidriger-befehl` | Gehorsam Befehl und rechtswidriger Befehl: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplin... |
| `gerichtliches-disziplinarverfahren-soldat` | Gerichtliches Disziplinarverfahren Soldat: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplin... |
| `gleichstellung-diskriminierung-soldatinnen-soldaten` | Gleichstellung Diskriminierung Soldatinnen Soldaten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Weh... |
| `impfpflicht-tauglichkeit-musterung` | Impfpflicht Tauglichkeit Musterung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnu... |
| `kaltstart-bundeswehrrecht` | Workflow zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Kaltstart Bundeswehrrecht. |
| `kameradschaft-achtungs-und-vertrauenspflicht` | Kameradschaft Achtungs- und Vertrauenspflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszi... |
| `kriegsdienstverweigerung-verfahren` | Kriegsdienstverweigerung Verfahren: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnu... |
| `livecheck-sg-wbo-wdo-wpflg-svg` | Workflow zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Livecheck SG WBO WDO WPflG SVG. |
| `mandantenbrief-soldat-verstaendlich` | Mandantenbrief Soldat verständlich: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnu... |
| `mobbing-fuersorgepflicht-bundeswehr` | Mobbing Fürsorgepflicht Bundeswehr: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnu... |
| `nebentaetigkeit-geschenkannahme-compliance` | Nebentätigkeit Geschenkannahme Compliance: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplin... |
| `output-beschwerde-antrag-stellungnahme` | Workflow zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Output Beschwerde Antrag Stellungnahme. |
| `personalakte-einsicht-datenschutz` | Personalakte Einsicht Datenschutz: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnun... |
| `personalvertretung-zivile-beschaeftigte-schnittstelle` | Personalvertretung zivile Beschäftigte Schnittstelle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, We... |
| `pflicht-zum-treuen-dienen-7-sg` | Pflicht zum treuen Dienen § 7 SG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung... |
| `politische-betaetigung-maessigung-neutralitaet` | Politische Betätigung Mäßigung Neutralität: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszipli... |
| `presseaeusserung-meinungsfreiheit-soldat` | Presseäußerung Meinungsfreiheit Soldat: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinaro... |
| `ptbs-einsatzfolge-beweisfuehrung` | PTBS Einsatzfolge Beweisführung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung... |
| `rechtsbeistand-im-disziplinarverfahren` | Rechtsbeistand im Disziplinarverfahren: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinaro... |
| `red-team-bundeswehr-beschwerde` | Red-Team Bundeswehr-Beschwerde: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2... |
| `reservistendienst-dienstleistungspflicht` | Reservistendienst Dienstleistungspflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplina... |
| `sanitaetsdienst-heilfuersorge` | Sanitätsdienst Heilfürsorge: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025... |
| `schadenersatz-regress-dienstunfall-material` | Schadenersatz Regress Dienstunfall Material: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszipl... |
| `sexuelle-belaestigung-beschwerde-schutzpflicht` | Sexuelle Belästigung Beschwerde Schutzpflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszi... |
| `social-media-soldat-dienstpflichten` | Social Media Soldat Dienstpflichten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordn... |
| `soldatenbeteiligung-vertrauensperson-sbg` | Soldatenbeteiligung Vertrauensperson SBG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplina... |
| `soldatengesetz-rechtsstellung-grundpflichten` | Soldatengesetz Rechtsstellung Grundpflichten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszip... |
| `soldatenversorgungsgesetz-beschaedigtenversorgung` | Soldatenversorgungsgesetz Beschädigtenversorgung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdi... |
| `status-soldat-beamter-zivilbeschaeftigter-klaeren` | Workflow zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Status Soldat Beamter Zivilbeschäftigter klären. |
| `statusrechte-im-einsatz-urlaub-betreuung` | Statusrechte im Einsatz Urlaub Betreuung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplina... |
| `trennungsgeld-umzugskosten-reisekosten` | Trennungsgeld Umzugskosten Reisekosten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinaro... |
| `truppendienstgericht-zustaendigkeit-verfahren` | Truppendienstgericht Zuständigkeit Verfahren: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszip... |
| `unterhaltssicherung-reservisten` | Unterhaltssicherung Reservisten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung... |
| `versetzung-kommandierung-abordnung` | Versetzung Kommandierung Abordnung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnu... |
| `vorlaeufige-dienstenthebung-einbehaltung-bezuege` | Vorläufige Dienstenthebung Einbehaltung Bezüge: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisz... |
| `wehrbeschwerdeordnung-beschwerde-frist-form` | Wehrbeschwerdeordnung Beschwerde Frist Form: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdiszipl... |
| `wehrdisziplinarordnung-einfache-disziplinarmassnahme` | Wehrdisziplinarordnung einfache Disziplinarmaßnahme: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Weh... |
| `wehrpflicht-wehrdienst-reservist-routing` | Workflow zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Wehrpflicht Wehrdienst Reservist Routing. |
| `wehrpflichtgesetz-spannungs-und-verteidigungsfall` | Wehrpflichtgesetz Spannungs- und Verteidigungsfall: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehr... |
| `wehrstrafrecht-fahnenflucht-gehorsamsverweigerung-schnittstelle` | Wehrstrafrecht Fahnenflucht Gehorsamsverweigerung Schnittstelle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerde... |
| `wehruebungen-heranziehungsbescheid` | Wehrübungen Heranziehungsbescheid: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnun... |
| `weitere-beschwerde-und-gerichtlicher-antrag-wehrdienstgericht` | Weitere Beschwerde und gerichtlicher Antrag Wehrdienstgericht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeor... |
| `widerruf-ernennung-arglistige-taeuschung` | Widerruf Ernennung arglistige Täuschung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinar... |

<!-- END ACTUAL-SKILL-ROUTING -->
