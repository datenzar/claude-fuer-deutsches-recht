# Handelsregister Praxis

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`handelsregister-praxis`) | [`handelsregister-praxis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/handelsregister-praxis.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Rabenhof Sensorik GmbH - Registergericht Charlottenburg, HRB 246810 B** (`handelsregister-registergericht-rabenhof-gmbh-2026`) | [Gesamt-PDF lesen](../testakten/handelsregister-registergericht-rabenhof-gmbh-2026/gesamt-pdf/handelsregister-registergericht-rabenhof-gmbh-2026_gesamt.pdf) | [`testakte-handelsregister-registergericht-rabenhof-gmbh-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-handelsregister-registergericht-rabenhof-gmbh-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein Registergerichts-Cockpit für Gesellschaftsrechtler, Notariate, Kanzleien und Rechtsabteilungen. Es ordnet, was eingetragen werden soll, welche Urkunden nötig sind, wer beim Registergericht entscheidet, wie man Beanstandungen beantwortet und wann Beschwerde oder Eilrechtsschutz Sinn ergeben.

## Wofür dieses Plugin da ist

Dieses Plugin ist ein Praxiswerkzeug. Es fragt zuerst die Lage ab, baut dann eine Dokumenten- und Vollzugsmatrix und erzeugt schließlich das konkrete Arbeitsprodukt: Nachreichung, Beanstandungsantwort, Beschwerdegerüst, Mandantenbrief, Checkliste, Fristenlog oder Vertrags-/Urkundenreview. Es ersetzt keine Berufsträgerentscheidung, aber es verhindert, dass ein formeller Nachweis, ein Rang, eine Abteilung-II-Belastung oder eine Registerfolge in der Hektik untergeht.

## Kaltstart

Starte mit dem allgemeinen Skill `handelsregister-allgemeiner-kaltstart`. Lade danach möglichst den aktuellen Register- oder Grundbuchauszug, das Gerichtsschreiben, die Anmeldung/Bewilligung, den Vertragsentwurf und vorhandene Anlagen hoch. Das Plugin sortiert erst, dann prüft es.

## Quellen- und Halluzinationsschutz

- Normen werden als Prüfanker verwendet, nicht als Schmuck.
- Rechtsprechung wird nur ausgegeben, wenn Gericht, Datum, Aktenzeichen und ein frei zugänglicher Fundlink geprüft sind.
- Unsichere Register-/Grundbuchstände werden nicht geraten; das Plugin fordert aktuelle Auszüge oder Nachweise an.

## Amtliche Startquellen

- [HGB §§ 8 ff., § 15](https://www.gesetze-im-internet.de/hgb/)
- [FamFG Registersachen und Beschwerde](https://www.gesetze-im-internet.de/famfg/)
- [GmbHG Anmeldung, Gesellschafterliste, Kapitalmaßnahmen](https://www.gesetze-im-internet.de/gmbhg/)
- [Registerportal der Länder](https://www.handelsregister.de/)
- [Unternehmensregister](https://www.unternehmensregister.de/)

## Typische Ergebnisse

- Prüfmatrix und Vollzugsfahrplan
- Entwurf für Nachreichung oder Antwort an das Gericht/Amt
- Mandantenbrief in normalem Deutsch
- Fristen- und Ranglog
- Beschwerde- oder Eilrechtsschutz-Skizze
- Liste fehlender Originale, Nachweise und Formmängel

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 72 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `amtsloeschung-familienloeschung-registerblatt` | Prüft Löschungsandrohung, Anhörung, Unrichtigkeit, Vermögenslosigkeit, Gegenwehr und Dokumentationsstrategie. |
| `auslandsurkunden-apostille-legalisation-uebersetzung` | Prüft Apostille, Legalisation, beglaubigte Übersetzung, Existenznachweis und Vertretungsnachweis. |
| `beanstandung-zwischenverfuegung-antwort` | Analysiert Registerbeanstandungen, trennt behebbare Formmängel von Rechtsstreit, formuliert Nachreichung, Bitte um Fristverlängerung oder Beschwerdevorbereitung. |
| `bekanntmachungen-monitoring` | Erstellt Monitoringplan für Bekanntmachungen, Friststart, Einspruchsfenster und Mandantenalerts. |
| `chronologischer-registerauszug` | Rekonstruiert Registergeschichte, kritische Umschlagpunkte und mögliche Inkonsistenzen. |
| `closing-handelregister-vollzug` | Prüft CP/CS, Eintragungsabhängigkeiten, Vollzugsreihenfolge, Escrow, Notarbestätigung und Bring-down. |
| `einstweiliger-rechtsschutz-registerstreit` | Plant Schutz gegen drohende Eintragung, Verzögerung, Registersperre, Gesellschafterlistenstreit und Vollzugsschäden. |
| `eintragung-prozessvergleich-registerfolge` | Übersetzt gerichtliche Vergleiche in Beschluss, Anmeldung, Liste, Löschung oder Berichtigung. |
| `erlaubnispflichtige-taetigkeit-register` | Prüft KWG, ZAG, GewO, Handwerk, Arbeitnehmerüberlassung und ob das Registergericht Nachweise verlangen kann. |
| `famfg-beschwerde-registersache` | Prüft Statthaftigkeit, Beschwer, Frist, Form, Abhilfe, Nichtabhilfe und Beschwerdebegründung gegen Registerentscheidungen. |
| `fehlerhafte-eintragung-berichtigung` | Prüft Schreibfehler, materiell falsche Eintragung, Amtskorrektur, Löschung, neue Anmeldung und Haftungsnotiz. |
| `firma-firmenbildung-und-irrefuehrung` | Prüft Firmenkern, Unterscheidbarkeit, Irreführung, Rechtsformzusatz, IHK-Stellungnahme und Abgrenzung zu Marke/Domain. |
| `formwechsel-registercheck` | Prüft Formwechselbericht, Beschlüsse, Satzung, neue Firma, Registerwechsel und Identitätskontinuität. |
| `frist-und-vollzugslog-register` | Baut ein Log für Beanstandungsfristen, Eintragungsdatum, Bekanntmachung, Closing-Abhängigkeit und Mandantenbericht. |
| `genossenschaft-registerschnittstelle` | Prüft Vorstand, Aufsichtsrat, Prüfung, Satzung und Eintragungslogik bei eG. |
| `gesellschafterlistenstreit-eilstrategie` | Ordnet Anspruch, einstweilige Verfügung, Registersperre, materiellen Streit und Kommunikation mit Registergericht/Notar. |
| `gmbh-co-kg-registerdoppelvollzug` | Koordiniert KG-Register, Komplementär-GmbH, Vertretung, Gesellschafterlisten und Firmenidentität. |
| `gmbh-geschaeftsfuehrerbestellung-abberufung` | Prüft Beschluss, Anmeldung, Versicherung, Vertretungsregel, Amtsannahme, Abberufung und Handelsregistervollzug. |
| `gmbh-gesellschafterliste-paragraph-40` | Prüft Liste, Prozentangaben, Veränderungsspalte, Notarzuständigkeit, Legitimationswirkung und Streit über Unrichtigkeit. |
| `gmbh-gruendung-erstanmeldung` | Checkt Stammkapital, Einzahlung, Geschäftsführer, Versicherung, Musterprotokoll, Gesellschaftsvertrag und Registereintragung. |
| `gmbh-kapitalerhoehung-bareinlage` | Prüft Satzungsänderung, Übernahme, Einzahlung, Anmeldung, Versicherung, Liste und Registervollzug. |
| `gmbh-kapitalerhoehung-sacheinlage` | Prüft Sacheinlagebericht, Werthaltigkeit, verdeckte Sacheinlage, Anmeldung und Beanstandungsrisiko. |
| `gmbh-kapitalherabsetzung-und-schutzjahr` | Prüft Gläubigerschutz, Sperrjahr, Bekanntmachungen, Versicherung und registerfeste Unterlagen. |
| `gmbh-liquidation-und-loeschung` | Führt durch Auflösung, Liquidatoren, Sperrjahr, Schlussbilanz, Löschung, Nachtragsliquidation und Registerkommunikation. |
| `gmbh-satzungsaenderung-und-neufassung` | Prüft Beschlussmehrheit, notarielle Beurkundung, vollständige Neufassung, Gegenstand, Firma, Sitz, Kapital und Anmeldung. |
| `handelsregister-allgemeiner-kaltstart` | Führt durch das erste Registerproblem: Wer meldet was an, welche Gesellschaft, welches Registerblatt, welches Ziel, welcher Fristdruck, welche Urkunden, welche Entscheidungsperson und welches Eskalationsniveau. |
| `handelsvollmacht-nicht-eintragungsfaehig` | Erklärt, was nicht ins Register gehört und wie interne Vollmachten dennoch sicher dokumentiert werden. |
| `hgb-publizitaet-paragraph-15` | Prüft negative und positive Publizität, Bekanntmachung, Gutgläubigkeit, Dritte und Risiko falscher Registerlage. |
| `insolvenzvermerk-und-registereintrag` | Prüft Eintragung von Eröffnung, Eigenverwaltung, Aufhebung, Insolvenzplan, Freigabe und Wirkungen für Vertretung. |
| `internationaler-registervergleich` | Vergleicht Companies House, irische/österreichische/schweizer Register und deutsche Nachweisanforderungen. |
| `kg-kommanditist-eintritt-austritt-haftsumme` | Prüft Einlage/Haftsumme, Sonderrechtsnachfolge, Austritt, Nachhaftung und Registerpublizität. |
| `ki-registerakte-halluzinationsschutz` | Zwingt zu Belegpfad, Registerauszug, Aktenzeichen, Normenanker und klarer Kennzeichnung nicht verifizierter Annahmen. |
| `nachlass-und-testamentsvollstrecker-register` | Prüft Erbschein, Europäisches Nachlasszeugnis, Testamentsvollstreckerzeugnis und Vertretungsmacht. |
| `notar-registergericht-kommunikation` | Erstellt klare Nachreichungslisten, Telefonnotizen, E-Mail-Entwürfe und Mandantenupdates ohne Schuldzuweisungschaos. |
| `ohg-kg-egbr-mopeg-statuswechsel` | Prüft kaufmännischen Betrieb, Statuswechsel, Anmeldung, Gesellschafter, Vertretung und MoPeG-Schnittstellen. |
| `online-abruf-registerportal-unternehmensregister` | Führt durch Handelsregister, Unternehmensregister, Bekanntmachungen, Chronologie, Ausdrucke, Screenshots und Beleglog. |
| `partg-partgmbb-register` | Prüft Partnerschaftsregister, Berufszulassung, Namensführung, Haftungsbeschränkung und Berufshaftpflichtnachweis. |
| `prokura-eintragung-und-widerruf` | Prüft Einzel-/Gesamtprokura, Filialprokura, Gesamtvertretung, Widerruf, Publizität und Unterschriftenmuster. |
| `rechtsprechung-register-live-verifizieren` | Legt fest, wie Entscheidungen in Registersachen nur mit Gericht, Datum, Aktenzeichen und freiem Fundlink ausgegeben werden. |
| `rechtsschein-und-innenstreit` | Trennt materielles Gesellschaftsrecht, Registerlage, Vertretungsmacht und Gutglaubensschutz. |
| `register-mandantenbrief` | Erstellt klare Mandantenupdates: Stand, Risiko, To-dos, Fristen, nächste Entscheidung. |
| `register-qualitaetsgate-vor-einreichung` | Checkliste vor dem Absenden: Urkunden, Beschlüsse, Listen, Unterschriften, Kapital, Namen, Daten, Registerblatt. |
| `registerakte-schnellscan-und-vollzugskarte` | Erstellt eine Vollzugskarte aus Satzung, Beschluss, Anmeldung, Liste, Notarvermerk, Gerichtsschreiben und Fristenlog. |
| `registerauszug-lesen` | Erklärt Abteilungen/Spalten, Historie, Vertretung, Kapital, Firma, Prokura, Insolvenz und Bekanntmachungen. |
| `registerbeweis-im-prozess` | Bereitet Registerauszüge, Bekanntmachungen und Nachweise prozesstauglich auf. |
| `registergericht-rollen-rechtspfleger-registerrichter` | Klärt Zuständigkeiten, Kommunikationsstil, Entscheidungswege und wann eine Sache richterlich, rechtspflegerisch oder rein vollzugstechnisch hängt. |
| `registergericht-und-datenschutz` | Klärt öffentliche Registerdaten, sensible Anlagen, Schwärzungen, Anschriften und Löschungswünsche. |
| `registerkosten-und-notarkosten` | Ordnet Register- und Notarkosten grob, vermeidet Doppelvollzug und erklärt Mandanten die Kostenlogik. |
| `registerrecht-aktiengesellschaft-vorstand-aufsichtsrat` | Prüft Bestellung, Vertretung, Satzungsänderungen, Kapitalmaßnahmen und Eintragung bei der AG. |
| `registerrecht-beschlussmaengel-und-registervollzug` | Prüft, ob das Registergericht bei Kapitalmaßnahme, Geschäftsführerbestellung oder Satzungsänderung Beschlussmängel beachten muss, wie weit die formelle Prüfung reicht und wann der materielle Streit auf Zivilprozess/Eilrechtsschutz verlag... |
| `registerrecht-digitalgruendung` | Prüft Online-Beurkundung/Beglaubigung, Identifizierung, digitale Einreichung und Medienbruch. |
| `registerrecht-fehlende-einzahlung` | Prüft Geschäftsführerversicherung, Kontoauszug, Hin- und Herzahlen, verdeckte Sacheinlage und Haftungsnotiz. |
| `registerrecht-fehlerhafte-geschaeftsfuehreradresse` | Prüft Anschriften, Geburtsdaten, Schutzinteressen, Schwärzungsmöglichkeiten und Auszugstypen. |
| `registerrecht-kapitalgesellschaft-co-kg-komplementaerwechsel` | Koordiniert Ausscheiden/Eintritt der Komplementär-GmbH, Haftung, Vertretung und Registerreihenfolge. |
| `registerrecht-mandatsannahme-notarferne` | Klärt Rolle der anwaltlichen Beratung neben Notar, Verantwortungsgrenzen und Mandantensteuerung. |
| `registerrecht-niederlassung-filiale` | Prüft eintragungsfähige Zweigniederlassung, unselbständige Betriebsstätte und Adress-/Vertretungsangaben. |
| `registerrecht-registergericht-telefonat-protokoll` | Erstellt kurze Telefonnotiz mit Name, Aktenzeichen, Beanstandung, Frist, Zusage und Folgeschritt. |
| `registerrecht-registerzeichen-und-aktenzeichen` | Erklärt HRB, HRA, PR, GnR, VR, Registernummer, Gericht und Aktenzeichenlogik. |
| `registerrecht-scheinloeschung-und-nachtragsliquidation` | Prüft Restvermögen, Prozessfähigkeit, Bestellung Nachtragsliquidator und Registereintragung. |
| `registerrecht-se-und-europaeische-gesellschaft` | Prüft SE-Firma, Sitz, monistisches/dualistisches System, Leitung, Verwaltungsrat und grenzüberschreitende Bezüge. |
| `registerrecht-umbenennung-rebranding` | Prüft Firmenänderung, Satzung, IHK, Marken-/Domainkonflikte, Bekanntmachung und Mandantenkommunikation. |
| `registersperre-und-closing-risiko` | Bewertet Sperrwirkung, einstweilige Verfügung, Gesellschafterlistenkonflikt und Alternativvollzug. |
| `sitz-inlandsanschrift-und-geschaeftsanschrift` | Prüft Satzungssitz, inländische Geschäftsanschrift, Empfangsbevollmächtigte, Briefkastenrisiken und Registereintragung. |
| `todesfall-gesellschafter-register` | Prüft Erbnachweis, Sonderrechtsnachfolge, Testamentsvollstrecker, Liste und Registerkommunikation. |
| `transparenzregister-schnittstelle` | Verbindet Handelsregisterdaten mit wirtschaftlich Berechtigten, GwG-Risiken und Meldepflichten. |
| `umwandlung-registervollzug` | Prüft Verschmelzung, Spaltung, Formwechsel, Registerreihenfolge, Schlussbilanz und Bekanntmachung. |
| `umzug-registerbezirk` | Prüft innerörtlich/anderer Bezirk, Satzungsänderung, Registerabgabe, Bekanntmachung und Adresslogik. |
| `unternehmensgegenstand-beanstandung` | Formuliert eintragungsfähige Gegenstände ohne Erlaubnis-/Aufsichtsrechtsfalle und ohne zu enge Zukunftsfessel. |
| `verein-registerschnittstelle` | Klärt, wann Vereinsregisterlogik statt Handelsregisterlogik greift und welche Beschlüsse/Protokolle gebraucht werden. |
| `verschmelzung-gmbh-registercheck` | Checkt Verschmelzungsvertrag, Zustimmungsbeschlüsse, Registeranmeldungen, Gläubigerschutz und Wirksamkeitszeitpunkt. |
| `vollmacht-und-anmeldung-oeffentliche-beglaubigung` | Prüft notarielle Beglaubigung, Vertreteranmeldung, Untervollmacht, Signatur und elektronische Einreichung. |
| `zweigniederlassung-auslaendische-gesellschaft` | Prüft Registerfähigkeit, Nachweise aus dem Herkunftsstaat, Übersetzung, Vertretungsmacht und deutsche Geschäftsanschrift. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
