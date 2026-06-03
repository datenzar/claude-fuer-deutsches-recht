# Versammlungsrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`versammlungsrecht`) | [`versammlungsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/versammlungsrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Verfassungsbeschwerde Klimacamp Initiative Saarbruecken — Art. 8 GG / Versammlungsfreiheit / Bannmeile Landtag** (`verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg`) | [Gesamt-PDF lesen](../testakten/verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg/gesamt-pdf/verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg_gesamt.pdf) | [`testakte-verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Praxisplugin für Menschen, Organisationen und anwaltliche Teams, die eine Versammlung unter freiem Himmel, einen Aufzug, eine Mahnwache, ein Camp oder eine konfliktträchtige Kundgebung rechtlich sauber anzeigen, durchführen oder gegen Behördeneingriffe verteidigen wollen.

Das Plugin denkt Versammlungsrecht nicht als Bittgang zur Behörde. Es startet bei Art. 8 GG: friedlich, ohne Waffen, grundsätzlich ohne Erlaubnis. Zugleich nimmt es ernst, dass Versammlungen im öffentlichen Raum geplant werden müssen: richtige Behörde, richtige Frist, klare Leitung, Ordner, Route, Technik, Rettungswege, Kooperationsgespräch, Auflagenprüfung und Eilrechtsschutz, wenn die Behörde ausweicht oder überzieht.

## Kaltstart

1. **Wo?** Bundesland, Stadt, Route, Platz, Bannmeile, mehrere Behördenbezirke?
2. **Was?** Außenversammlung, Aufzug, Innenversammlung, private Runde, Mahnwache, Infostand, Camp, Gegenversammlung?
3. **Wann?** Termin, Bekanntgabezeitpunkt, Einladung, Social-Media-Post, Eil- oder Spontanversammlung?
4. **Wer?** Veranstalter, Leitung, Stellvertretung, Ordner, Organisation, Kontaktkanal?
5. **Wofür?** Anzeige erstellen, Behördenfragen beantworten, Auflagen prüfen, Verbot abwehren, Eilrechtsschutz, Tag-der-Versammlung-Plan?

## Leitgedanke

- **Anzeige statt Genehmigung:** Öffentliche Versammlungen unter freiem Himmel werden angezeigt; die Behörde soll planen und schützen, nicht politisch vorsortieren.
- **Landesrecht zuerst:** Viele Länder haben eigene Versammlungsgesetze. Das Plugin fragt deshalb immer nach Ort und Bundesland.
- **Kooperation ohne Selbstzensur:** Behördenbelange werden ernst genommen, aber Ort, Zeit, Thema und Ausdrucksform bleiben Teil der grundrechtlich geschützten Versammlung.
- **Konkrete Gefahr statt Behördenbauchgefühl:** Auflagen und Verbote müssen tatsachenbasiert und verhältnismäßig sein.
- **Schnelle Outputs:** Anzeige, Ordnerliste, Kooperationsagenda, Behördenbrief, Eilantrag, Notfallkarte und Nachbereitungsvermerk.

## Typische Outputs

| Situation | Passende Skills | Ergebnis |
| --- | --- | --- |
| Versammlung normal planen | `allgemein`, `landesrecht-und-behoerde-finden`, `anzeige-unter-freiem-himmel`, `muster-anzeige-generator` | Anzeige, Fristplan, Behördenkontakt |
| Einladung soll heute raus | `frist-48-stunden-bekanntgabe`, `bekanntgabe-social-media`, `qualitaetsgate-vor-bekanntgabe` | Kommunikationskalender und Go/No-Go |
| Spontane oder eilige Demo | `spontanversammlung`, `eilversammlung`, `behoerdenkommunikation` | Kurzmeldung, Aktenvermerk, Polizeisprechzettel |
| Behörde will verlegen oder verbieten | `auflagen-pruefen`, `falscher-tag-falscher-ort-einwand`, `verbot-und-beschraenkung-abwehren`, `muster-eilantrag` | Gegenbrief und Eilrechtsschutz-Gerüst |
| Ordner und Tag selbst | `ordner-auswahl`, `ordnerliste-und-mitteilung`, `polizei-vor-ort-deeskalation`, `notfallkarte-versammlungstag` | Briefing, Liste, Notfallkarte |
| Camp, Technik, Verkehr | `camp-dauerversammlung`, `technik-lautsprecher-musik`, `verkehr-rettungswege-oepnv` | Konzept und mildere Mittel |

## Quellenstrategie

- **Bundesrecht:** Art. 8 GG, Versammlungsgesetz, VwGO.
- **Landesrecht:** jeweiliges Landesversammlungsgesetz und Zuständigkeitsregel.
- **Behördenpraxis:** offizielle Onlineformulare und Hinweise der konkreten Versammlungsbehörde.
- **Rechtsprechung:** nur mit Gericht, Datum, Aktenzeichen und frei überprüfbarem Link.
- **Keine Blindzitate:** keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.

## Berufs- und Datenschutzhinweis

Bei echten Mandaten keine sensiblen personenbezogenen Daten, politischen Mitgliedschaften, Teilnehmerlisten oder Behördenakten in ungeprüfte Systeme laden. Ordnerlisten, Minderjährigendaten, Gesundheitsdaten und Polizeikommunikation sind datensensibel. Für produktiven Kanzleieinsatz ist das jeweils eigene Datenschutz-, Berufsrechts- und Hosting-Setup maßgeblich.

## Lizenz

Apache-2.0 OR MIT. Siehe Repository-Stammverzeichnis.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 55 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Allgemeiner Kaltstart im Versammlungsrecht: Land und Ort, Art der Versammlung, Frist, Behörde, Risiko und Ziel klären, dann passende Spezialskills und nächsten Output auswählen. |
| `anwaltlicher-brief-an-behoerde` | Entwirft einen anwaltlichen oder sehr sachlichen Laienbrief gegen problematische Behördenkommunikation. |
| `anzeige-unter-freiem-himmel` | Führt durch die Anzeige einer öffentlichen Versammlung unter freiem Himmel oder eines Aufzugs, ohne sie fälschlich als Genehmigungsantrag zu behandeln. |
| `auflagen-pruefen` | Prüft Beschränkungen, Auflagen und Nebenbestimmungen auf Rechtsgrundlage, Tatsachenbasis und Verhältnismäßigkeit. |
| `auflagenverstoss-und-owi` | Prüft Ordnungswidrigkeiten- und Strafrisiken bei nicht angezeigten Versammlungen, Auflagenverstößen und Auflösung. |
| `bannmeile-schutzbereiche` | Prüft befriedete Bezirke, Bannmeilen und Schutzbereiche um Bundestag, Bundesrat, Landtage und besondere Orte. |
| `barrierefreiheit-und-inklusion` | Plant barrierearme Versammlungen: Wege, Lautsprecher, Gebärdensprache, Ruhebereiche, Assistenz und sichere Kommunikation. |
| `behoerdenkommunikation` | Formuliert kluge Mails und Telefonnotizen an Versammlungsbehörde, Polizei, Ordnungsamt und Straßenverkehrsbehörde. |
| `bekanntgabe-social-media` | Prüft, wann Flyer, Website, Messenger, Pressemitteilung oder Social-Media-Post die Bekanntgabe oder Einladung auslösen. |
| `bescheid-lesen` | Analysiert versammlungsrechtliche Bescheide, Auflagenkataloge, Verbote, Telefonnotizen und E-Mails der Behörde. |
| `beweissicherung-am-versammlungstag` | Erstellt Beweissicherungsplan für Auflagen, Polizeihandeln, Störer, Wetter, Teilnehmerzahl und Ablauf. |
| `blockade-sitzblockade-friedlichkeit` | Prüft Blockaden, Sitzblockaden, Zufahrtsnähe und Friedlichkeitsgrenzen. |
| `bundeslaender-synopse` | Erstellt eine Arbeits-Synopse der Landesversammlungsgesetze und markiert, was vor Ausgabe live amtlich zu prüfen ist. |
| `camp-dauerversammlung` | Prüft Camps, Mahnwachen, Zelte, Schlafen, Infrastruktur und Dauerversammlungen unter Art. 8 GG. |
| `datenschutz-fotos-livestream` | Prüft Fotos, Livestreams, Drohnen, Teilnehmerdaten, Ordnerlisten und Polizeiaufnahmen. |
| `dritte-anwohner-laerm-geschaeft` | Bearbeitet Konflikte mit Anwohnern, Geschäften, Schulen, Kirchen, Kliniken, Botschaften oder sensiblen Orten. |
| `eilversammlung` | Prüft Eilversammlungen, bei denen ein Veranstalter existiert, der Zweck aber bei voller Fristeinhaltung vereitelt würde. |
| `eingangsbestaetigung-und-aktenzeichen` | Sichert Nachweis von Anzeige, Eingang, Aktenzeichen und behördlicher Zuständigkeit. |
| `falscher-tag-falscher-ort-einwand` | Reagiert auf Behördeneinwände wie falscher Tag, falscher Ort, sensible Nachbarschaft, parallele Veranstaltung oder politisch unpassender Anlass. |
| `frist-48-stunden-bekanntgabe` | Berechnet die versammlungsrechtliche 48-Stunden-Frist bis zur Bekanntgabe oder Einladung und markiert Landesabweichungen. |
| `gefahrenprognose-redteam` | Zerlegt die behördliche Gefahrenprognose und baut eine eigene, realistische Sicherheitslage auf. |
| `gegenveranstaltung-und-trennung` | Plant konkurrierende Versammlungen, Gegenprotest, Pufferzonen und gleichzeitige Grundrechtsausübung. |
| `infostand-mahnwache-kleinstversammlung` | Prüft Kleinstkundgebung, Mahnwache, Infostand mit politischem Meinungskern und Abgrenzung zur Sondernutzung. |
| `innenraum-versammlung-abgrenzen` | Grenzt öffentliche und private Versammlungen in geschlossenen Räumen von anzeigepflichtigen Versammlungen unter freiem Himmel ab. |
| `kooperationsgespraech` | Bereitet Kooperationsgespräche mit Versammlungsbehörde und Polizei vor und protokolliert sie. |
| `kosten-haftung-und-versicherung` | Prüft Kosten, Gebühren, Schäden, Haftung, Versicherung und Regress rund um Versammlungen. |
| `kundgebung-stationaer-platzwahl` | Prüft stationäre Kundgebungen, Mahnwachen, Infostände mit Meinungskern und symbolische Orte. |
| `landesrecht-und-behoerde-finden` | Findet das anwendbare Landesversammlungsgesetz und die konkrete zuständige Versammlungsbehörde oder Polizei anhand von Ort und Route. |
| `leiter-verantwortung` | Erklärt Rolle, Rechte und Pflichten der Versammlungsleitung vor, während und nach der Versammlung. |
| `mildere-mittel-matrix` | Erstellt eine Matrix milderer Mittel gegen Verbot, Verlegung oder zu breite Auflagen. |
| `muster-anzeige-generator` | Erstellt eine präzise Anzeige für Kundgebung, Mahnwache, Demonstrationszug, Fahrradaufzug oder Dauerversammlung. |
| `muster-eilantrag` | Erstellt ein Grundgerüst für verwaltungsgerichtlichen Eilrechtsschutz im Versammlungsrecht. |
| `nachbereitung-und-aktenvermerk` | Erstellt Nachbereitung nach Durchführung, Auflagenproblemen, Polizeikontakt, Presse und möglichem Folgeverfahren. |
| `notfallkarte-versammlungstag` | Erstellt eine kompakte Notfallkarte für Leitung, Stellvertretung, Ordner und Dokumentationsteam. |
| `offizielle-quellen-livecheck` | Erzwingt Live-Check von Gesetz, Behörde, Formular, Rechtsprechung und Landesrecht vor verbindlichem Output. |
| `ordner-auswahl` | Hilft bei Auswahl, Anzahl, Zuverlässigkeit und Briefing von Ordnerinnen und Ordnern. |
| `ordnerliste-und-mitteilung` | Erstellt datensparsame Ordnerliste oder Ordnerzahl-Mitteilung an die Behörde nach dem einschlägigen Recht. |
| `partei-gewerkschaft-verein-veranstalter` | Hilft Parteien, Gewerkschaften, Vereinen, Initiativen und losen Gruppen bei Veranstalterrolle und interner Verantwortlichkeit. |
| `polizei-vor-ort-deeskalation` | Gibt Leitfaden für Kommunikation mit Einsatzleitung, Störer, Auflösung, Durchsuchung und Platzverweise am Versammlungstag. |
| `polizeifilmerei-beweissicherung-kug-201-stgb` | Versammlungsrecht: Polizeieinsätze, Gegenaufnahmen, Beweissicherung, KUG/KunstUrhG, § 201 StGB, § 201a StGB, Presse- und Versammlungsfreiheit, Vor-Ort-Kommunikation und Nachbereitung. |
| `presse-und-oeffentlichkeitsarbeit` | Hilft bei Pressemitteilungen, Einladungstexten, Veranstalterangabe und Kommunikation ohne unnötige Rechtsrisiken. |
| `privat-oeffentlich-abgrenzen` | Prüft, ob eine Zusammenkunft öffentlich, privat, vereinsintern, parteiintern, betrieblich oder nur ein Gesprächskreis ist. |
| `qualitaetsgate-vor-bekanntgabe` | Letzter Check vor öffentlicher Einladung oder Versand der Anzeige. |
| `route-aufzug-und-streckenplanung` | Plant Aufzüge und Routen so, dass Versammlungszweck, Verkehr, Sicherheit und Behördeneinwände gut ausbalanciert sind. |
| `schule-universitaet-jugendliche` | Prüft Schüler-, Studierenden-, Hochschul- und Jugendversammlungen samt Aufsicht, Schulrecht und Hausrecht. |
| `schutz-vor-vorauseilendem-gehorsam` | Hilft, berechtigte Behördenbelange zu berücksichtigen, ohne die Versammlung aus Angst selbst zu entkernen. |
| `spontanversammlung` | Prüft echte Spontanversammlungen, bei denen Anlass und Bildung so unmittelbar zusammenfallen, dass vorherige Anzeige nicht möglich war. |
| `strafrecht-versg-risiken` | Routet Strafbarkeitsrisiken aus VersammlG, StGB, Waffenrecht, Vermummung, Schutzwaffen und Nötigung. |
| `technik-lautsprecher-musik` | Prüft Lautsprecher, Megaphon, Bühne, Strom, Fahrzeuge, Musik, Projektionen und Lärmschutz. |
| `untatigkeit-und-schweigen` | Reagiert, wenn Behörde auf Anzeige oder Rückfrage nicht antwortet und der Termin näher rückt. |
| `verbot-und-beschraenkung-abwehren` | Entwickelt Gegenstrategie gegen Verbot, faktische Verhinderung oder so einschneidende Beschränkung, dass der Zweck leerläuft. |
| `verkehr-rettungswege-oepnv` | Bearbeitet Verkehr, ÖPNV, Rettungswege, Baustellen, Umleitungen und Straßenverkehrsbehörden. |
| `versammlungskonzept` | Erstellt ein belastbares Versammlungskonzept als Anlage zur Anzeige oder als Antwort auf Behördenfragen. |
| `wahlkampf-und-politische-kundgebung` | Prüft Wahlkampfstände, Kandidatenauftritte, Parteiveranstaltungen, Gegendemonstrationen und kommunale Neutralitätsfragen. |
| `widerspruch-klage-eilrechtsschutz` | Routet Widerspruch, Anfechtungsklage, § 80 Abs. 5 VwGO und § 123 VwGO bei versammlungsrechtlichen Bescheiden. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
