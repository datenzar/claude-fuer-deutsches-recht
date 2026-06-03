# Grundbuchamt Praxis

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`grundbuchamt-praxis`) | [`grundbuchamt-praxis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/grundbuchamt-praxis.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Haus Altenau - verlorener Grundschuldbrief, Wegerecht und Kaufpreisfälligkeit** (`grundbuchamt-briefgrundschuld-wegerecht-altenau-2026`) | [Gesamt-PDF lesen](../testakten/grundbuchamt-briefgrundschuld-wegerecht-altenau-2026/gesamt-pdf/grundbuchamt-briefgrundschuld-wegerecht-altenau-2026_gesamt.pdf) | [`testakte-grundbuchamt-briefgrundschuld-wegerecht-altenau-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-grundbuchamt-briefgrundschuld-wegerecht-altenau-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein Grundbuch-Cockpit für alle, die Auszüge lesen, Urkunden grundbuchtauglich nachweisen, Zwischenverfügungen verstehen und Grundbuchvollzug sauber betreiben müssen. Schwerpunkt ist die praktische Leseführung durch Abteilung I, II und III, damit keine Dienstbarkeit, Vormerkung, Rangstelle oder Briefgrundschuld übersehen wird.

## Wofür dieses Plugin da ist

Dieses Plugin ist ein Praxiswerkzeug. Es fragt zuerst die Lage ab, baut dann eine Dokumenten- und Vollzugsmatrix und erzeugt schließlich das konkrete Arbeitsprodukt: Nachreichung, Beanstandungsantwort, Beschwerdegerüst, Mandantenbrief, Checkliste, Fristenlog oder Vertrags-/Urkundenreview. Es ersetzt keine Berufsträgerentscheidung, aber es verhindert, dass ein formeller Nachweis, ein Rang, eine Abteilung-II-Belastung oder eine Registerfolge in der Hektik untergeht.

## Kaltstart

Starte mit dem allgemeinen Skill `grundbuchamt-allgemeiner-kaltstart`. Lade danach möglichst den aktuellen Register- oder Grundbuchauszug, das Gerichtsschreiben, die Anmeldung/Bewilligung, den Vertragsentwurf und vorhandene Anlagen hoch. Das Plugin sortiert erst, dann prüft es.

## Quellen- und Halluzinationsschutz

- Normen werden als Prüfanker verwendet, nicht als Schmuck.
- Rechtsprechung wird nur ausgegeben, wenn Gericht, Datum, Aktenzeichen und ein frei zugänglicher Fundlink geprüft sind.
- Unsichere Register-/Grundbuchstände werden nicht geraten; das Plugin fordert aktuelle Auszüge oder Nachweise an.

## Amtliche Startquellen

- [GBO](https://www.gesetze-im-internet.de/gbo/)
- [GBV](https://www.gesetze-im-internet.de/gbvfg/)
- [FamFG Aufgebotsverfahren](https://www.gesetze-im-internet.de/famfg/)
- [BGB Grundstücksrechte](https://www.gesetze-im-internet.de/bgb/)
- [Justizportal des Bundes und der Länder](https://justiz.de/)

## Typische Ergebnisse

- Prüfmatrix und Vollzugsfahrplan
- Entwurf für Nachreichung oder Antwort an das Gericht/Amt
- Mandantenbrief in normalem Deutsch
- Fristen- und Ranglog
- Beschwerde- oder Eilrechtsschutz-Skizze
- Liste fehlender Originale, Nachweise und Formmängel

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 64 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abteilung-i-eigentum-und-erwerbsgrund` | Prüft Eigentümer, Erwerbsgrund, Erbengemeinschaft, Bruchteile, Gesamthand, eGbR und Voreintragung. |
| `abteilung-ii-dienstbarkeit-vormerkung-beschraenkung` | Analysiert Wegerecht, Leitungsrecht, Nießbrauch, Wohnungsrecht, Vormerkung, Sanierungsvermerk, Nacherbfolge und Verfügungsbeschränkung. |
| `abteilung-iii-grundschuld-hypothek-rang` | Prüft Grundschuld, Hypothek, Rentenschuld, Brief/Buch, Rang, Löschung, Abtretung und Sicherungszweck-Schnittstelle. |
| `amtshaftung-und-vollzugsfehler` | Ordnet Fehler von Notar, Grundbuchamt, Partei und Bank ohne vorschnelle Schuldzuweisung. |
| `aufgebotsverfahren-famfg` | Prüft Zuständigkeit, Antragsberechtigung, Glaubhaftmachung, Aufgebotsfrist, öffentliche Bekanntmachung und Beschlussverwertung. |
| `auflassung-und-eigentumsumschreibung` | Prüft Auflassung, Antrag, Voreintragung, Unbedenklichkeitsbescheinigung, Genehmigungen und Vollzug. |
| `auflassungsvormerkung-kaufvertrag` | Prüft Vormerkungszweck, Rang, Löschung, Sicherung gegen Zwischenverfügungen und Käufer-/Bankenschutz. |
| `auslandsurkunden-apostille-grundbuch` | Prüft Apostille, Legalisation, notarielle Bescheinigung, Übersetzung und Register-/Vertretungsnachweis. |
| `baulast-ist-nicht-grundbuch` | Erklärt, warum Baulasten nicht im Grundbuch stehen müssen und wie man Baulastenverzeichnis/Grundbuch zusammenliest. |
| `beschwerde-grundbuchsache` | Prüft Statthaftigkeit, Beschwer, Frist, Abhilfe, Nichtabhilfe und OLG-Vorlage in Grundbuchsachen. |
| `bestandsverzeichnis-flurstueck-und-zuschreibung` | Prüft Grundstück, Flurstück, Gemarkung, Wirtschaftsart, Zuschreibung, Bestandsteil und Katasterabgleich. |
| `briefrecht-abtretung-und-loeschung` | Prüft Besitz am Brief, Abtretungserklärung, Löschungsbewilligung, Briefvorlage und Ersatzwege. |
| `dienstbarkeit-wegerecht-pruefen` | Liest Inhalt, herrschendes/dienendes Grundstück, Ausübungsbereich, Baulast-Schnittstelle und Löschbarkeit. |
| `elektronischer-rechtsverkehr-grundbuch` | Prüft elektronische Einreichung, notarielle Signatur, Scans, Ausfertigungen und Medienbruchrisiken. |
| `familiengerichtliche-genehmigung-grundbuch` | Prüft Minderjährige, betreute Personen, Genehmigungsbedürftigkeit, Rechtskraft und Nachweisform. |
| `finanzierung-und-rangstelle` | Koordiniert Bankauflagen, Rangbescheinigung, Belastungsvollmacht, Zweckerklärung und Auszahlungsvoraussetzungen. |
| `gbo-antrag-bewilligung-eintragung` | Prüft GBO-Mechanik aus Antrag, Bewilligung, Eintragungsfähigkeit, Eintragungsreife und Vollzugshindernis. |
| `gbr-egbr-grundbuch` | Prüft Gesellschaftsregister, Voreintragung, Vertretung, Gesellschafterwechsel und MoPeG-Folgen. |
| `genehmigungen-landwirtschaft-verkehrswert` | Prüft Grundstücksverkehr, siedlungsrechtliche Genehmigungen, Vorkaufsrechte und Registervollzug. |
| `grundbuch-qualitygate-vor-vollzug` | Prüft Antrag, Bewilligung, Rang, Nachweise, Anlagen, Genehmigungen, Urkundenform und Zahlungslogik. |
| `grundbuch-vollzugslog` | Erstellt Fristen-, Rang- und Nachweisliste mit Verantwortlichen, Stand und nächstem Schritt. |
| `grundbuchamt-allgemeiner-kaltstart` | Führt durch Eigentum, Belastungen, Vollzugsziel, Grundbuchbezirk, Urkundentyp, Nachweise, Rang, Fristdruck und Kommunikationsweg mit dem Grundbuchamt. |
| `grundbuchamt-amtswiderspruch-und-richtigstellung` | Prüft offensichtliche Unrichtigkeit, Amtswiderspruch, Amtslöschung, Berichtigung und Rechtsschutz. |
| `grundbuchamt-brief-vs-buchrecht-erklaerung` | Erklärt Mandanten, warum der Briefkörper zählt und warum Kopien nicht reichen. |
| `grundbuchamt-eilfall-rangverlust` | Erarbeitet Sofortplan bei drohendem Rangverlust oder konkurrierendem Antrag. |
| `grundbuchamt-erbbaurecht-schnittstelle` | Verknüpft Grundstücksgrundbuch, Erbbaugrundbuch, Reallast, Zustimmung und Belastungen. |
| `grundbuchamt-flurbereinigung-und-umlegung` | Prüft neue Grundstücksbezeichnungen, Surrogation, Rangfortsetzung und Vollzugsnachweise. |
| `grundbuchamt-gesamtgrundschuld-und-mithaft` | Prüft Mithaft mehrerer Grundstücke, Pfandfreigabe, Rang und Bankauflagen. |
| `grundbuchamt-gesellschaftsrechtliche-vertretung` | Prüft Handelsregister, Gesellschafterliste, Geschäftsführer, Prokura, Liquidator und ausländische Vertreter. |
| `grundbuchamt-insolvenz-auslaendischer-trustee` | Prüft inzidente Anerkennung, Vertretungsmacht, Urkundenform, Übersetzung und Register-/Grundbuchfähigkeit. |
| `grundbuchamt-kommunikation` | Formuliert sachliche Anfragen, Nachreichungen, Fristbitten und Beschwerdeankündigungen ohne Vollzug zu gefährden. |
| `grundbuchamt-konkurrierende-antraege-rangkonflikt` | Prüft, was zu tun ist, wenn Vormerkung, Grundschuld, Pfändung, Insolvenz-/ZVG-Vermerk oder Dienstbarkeit konkurrierend eingehen und der Rang wirtschaftlich entscheidend wird. |
| `grundbuchamt-maengelmatrix` | Klassifiziert jedes Hindernis nach Form, Berechtigung, Genehmigung, Rang, Kosten, Steuer und Inhalt. |
| `grundbuchamt-nichtigkeitsrisiko-kaufvertrag` | Prüft, ob ein möglicher Form-, Genehmigungs-, Vertretungs- oder Verbotsgesetzmangel den Grundbuchvollzug blockiert und wie Zwischenverfügung, Nachgenehmigung oder Rückabwicklung vorbereitet werden. |
| `grundbuchamt-teilloesung-rangfreigabe` | Prüft Teilflächen, Freigabeerklärung, Rangwirkung, Bankbrief und Vollzug. |
| `grundbuchamt-verlorene-genehmigung-und-ersatznachweis` | Prüft, wie eine verlorene familiengerichtliche, betreuungsgerichtliche, sanierungsrechtliche oder behördliche Genehmigung grundbuchtauglich ersetzt oder erneut beschafft wird. |
| `grundbuchamt-verwalterzustimmung-weg` | Prüft Teilungserklärung, Verwalternachweis, Beschluss, Form und Nachreichung. |
| `grundbuchamt-vollstreckungsunterwerfung` | Prüft § 800 ZPO-Schnittstelle, dingliche Unterwerfung, Klausel und Zustellung. |
| `grundbuchauszug-fuer-due-diligence` | Baut eine DD-Tabelle aus Eigentum, Belastungen, Rang, Vollzugshindernissen, offenen Fragen und Deal-Relevanz. |
| `grundbuchauszug-lesen-abteilung-i-ii-iii` | Erklärt Bestandsverzeichnis, Abteilung I, II und III mit Warnsystem gegen übersehene Dienstbarkeiten, Vormerkungen, Verfügungsbeschränkungen und Rangfallen. |
| `grundbuchberichtigung-erbfall` | Prüft Erbschein, notarielle Verfügung von Todes wegen, Europäisches Nachlasszeugnis, Grundbuchberichtigung und Kostenfristen. |
| `grunderwerbsteuer-unbedenklichkeitsbescheinigung` | Prüft GrESt-Schnittstelle, Fälligkeitslogik, Ausnahmen und Vollzugshindernis. |
| `grundschuld-bestellung-buchgrundschuld` | Prüft Bewilligung, Rang, Betrag, Zinsen, Nebenleistung, Unterwerfung und Sicherungsabrede. |
| `grundschuldbrief-verlust-aufgebot` | Führt durch Feststellung des Verlusts, Aufgebotsantrag, Nachweise, Ausschließungsbeschluss, Ersatzbrief/Löschung und Bankkommunikation. |
| `insolvenzvermerk-zwangsversteigerung` | Prüft Verfügungsbeschränkung, Zwangsversteigerungsvermerk, Rang, Löschung und Erwerb aus Verfahren. |
| `kataster-liegenschaftskarte-abgleich` | Prüft Flurstücksidentität, Vermessung, Teilung, Vereinigung, Fortführung und Vollzugshindernisse. |
| `kaufvertrags-check-grundbuch` | Prüft Belastungen, Fälligkeit, Löschung, Vormerkung, Finanzierung, Besitzübergang und Risiken aus Abteilung II. |
| `leitungsrecht-und-energieanlagen` | Prüft Strom, Wasser, Fernwärme, Telekommunikation, dingliche Sicherung und Rangkonflikte. |
| `loeschungsbewilligung-bank` | Checkt Bankformular, Unterschriften, Vertretungsmacht, Briefvorlage, Teillöschung und Verwahrstelle. |
| `nacherbenvermerk-und-verfuegungsbeschraenkung` | Prüft Vermerk, Zustimmung, Befreiung, Löschung und Erwerberrisiko. |
| `niessbrauch-wohnungsrecht` | Prüft Berechtigte, Inhalt, Rang, Löschung, Tod, Heimunterbringung, Vermietung und Finanzierungskonflikt. |
| `notariat-vollzugsauftrag-grundbuch` | Steuert Notarvollzug, Treuhandauflagen, Fälligkeitsmitteilung, Bankunterlagen und Mandantenkommunikation. |
| `paragraph-29-gbo-formnachweis` | Prüft öffentliche oder öffentlich beglaubigte Urkunden, Registerauszüge, Erbnachweise, Vollmachten, Auslandsurkunden und Übersetzungen. |
| `prioritaetsmitteilung-und-rangbescheinigung` | Prüft, wann Rang gesichert ist und wie Notar/Bank/Grundbuchamt die Reihenfolge dokumentieren. |
| `rangprinzip-und-rangvorbehalt` | Ordnet Rangfolge, Rangrücktritt, Gleichrang, Rangvorbehalt und Prioritätsrisiken. |
| `reallast-und-erbbauzins` | Prüft Inhalt, Anpassung, Rang, Vollstreckbarkeit und Zusammenhang mit Erbbaurechten. |
| `rechtsprechung-grundbuch-live-verifizieren` | Verlangt bei jeder Entscheidung Gericht, Datum, Aktenzeichen und frei zugänglichen Link, sonst nur als Prüfbedarf ausgeben. |
| `sanierungsvermerk-und-vorkaufsrechte-kommune` | Prüft Genehmigung, Vorkaufsrecht, Löschung, Bescheinigung und Kaufvertragsvollzug. |
| `teilflaechenkauf-und-vermessung` | Plant Vormerkung, Messungsanerkennung, Fortführungsnachweis, Rang, Kaufpreisfälligkeit und Umschreibung. |
| `testamentsvollstrecker-grundbuch` | Prüft Verfügungsbefugnis, Zeugnis, Beschränkungen, Nachweisform und Verkaufsvollzug. |
| `vollmacht-vorsorgevollmacht-grundbuch` | Prüft notarielle Vollmacht, Ausfertigung, Betreuungs-/Vorsorgevollmacht, Widerruf, Auslandsbezug und Missbrauchsrisiko. |
| `vorkaufsrecht-wiederkaufsrecht` | Prüft dingliches Recht, Ausübungsfall, Frist, Löschung, Rang und Kaufvertragsgestaltung. |
| `weg-teilungsgrundbuch` | Prüft Teilungserklärung, Aufteilungsplan, Abgeschlossenheit, Sonder-/Gemeinschaftseigentum, Sondernutzungsrechte und Grundbuchblätter. |
| `zwischenverfuegung-paragraph-18-gbo` | Analysiert beanstandete Hindernisse, Behebbarkeit, Rangwahrung, Frist und Antwortstrategie. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
