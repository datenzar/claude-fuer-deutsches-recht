# Kriegsdienstverweigerung und Wehrdienst

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`kriegsdienstverweigerung-wehrdienst`) | [`kriegsdienstverweigerung-wehrdienst.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kriegsdienstverweigerung-wehrdienst.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **KDV-Verfahren Malte Eberhard Rabenow / Berlin-Köln 2026** (`kriegsdienstverweigerung-gewissensantrag-berlin-2026`) | [Gesamt-PDF lesen](../testakten/kriegsdienstverweigerung-gewissensantrag-berlin-2026/gesamt-pdf/kriegsdienstverweigerung-gewissensantrag-berlin-2026_gesamt.pdf) | [`testakte-kriegsdienstverweigerung-gewissensantrag-berlin-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kriegsdienstverweigerung-gewissensantrag-berlin-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Praxisplugin für Kriegsdienstverweigerung aus Gewissensgründen nach Art. 4 Abs. 3 GG und KDVG. Es ist ausdrücklich kein Plugin für Totalverweigerung, Dienstflucht, Befehlsboykott oder politische Leistungsverweigerung. Es behandelt die verfassungsrechtlich loyale Inanspruchnahme eines Grundrechts: Wer nicht gegen sein Gewissen Kriegsdienst mit der Waffe leisten kann, stellt sich nicht außerhalb der Ordnung, sondern beruft sich auf eine ihrer zentralen Gewissensgarantien.

Das Plugin führt von der ersten inneren Klärung über den Antrag beim Bundesamt für das Personalmanagement der Bundeswehr bis zur BAFzA-Entscheidung, Anhörung, Nachreichung, Anerkennung, Ablehnung, Widerspruch, Untätigkeitsklage und Eilrechtsschutz. Es berücksichtigt den Stand 2026 nach dem Wehrdienstmodernisierungsgesetz, insbesondere § 13 KDVG n. F. für ungediente Wehrpflichtige, die vor dem 01.01.2010 geboren wurden.

## Kaltstart

1. **Status klären:** ungedient, wehrpflichtig, vor/nach 01.01.2010 geboren, gemustert, einberufen, Reservist, FWDL, Soldat auf Zeit, Berufssoldat, Soldatin, frühere Soldatin/früherer Soldat?
2. **Ziel klären:** Antrag stellen, Begründung ordnen, Unterlagen vervollständigen, Sachstand erzwingen, Anhörung vorbereiten, Ablehnung angreifen, laufenden Dienstkonflikt entschärfen?
3. **Gewissen klären:** Geht es wirklich um Kriegsdienst mit der Waffe als solcher oder nur um einen bestimmten Krieg, eine politische Lage, Angst, Karriere, Gesundheit oder Totalverweigerung?
4. **Verfahren klären:** Antrag läuft über BAPersBw; BAFzA entscheidet inhaltlich nach Zuleitung. Direkte Übersendung an das BAFzA ist nicht der gesetzliche Standardweg.
5. **Rechtsschutz klären:** Sachstand, Nachreichung, Widerspruch, § 75 VwGO, § 80 VwGO oder § 123 VwGO nur nach Lage und Frist.

## Leitgedanke

Das Plugin soll nicht fertige Gewissensformeln produzieren. Es hilft, eine echte persönliche Entscheidung so zu strukturieren, dass sie rechtlich verständlich wird: Lebensweg, innere Entwicklung, Auslöser, Stabilität, Konsequenzen, Abgrenzung zu bloßer Politik und Plausibilität. Allgemeine Mustersätze sind gefährlich; eine persönliche, wahrhaftige und prüffähige Darstellung ist stärker.

## Typische Outputs

| Situation | Skills | Ergebnis |
| --- | --- | --- |
| Erster Antrag | `allgemein`, `status-routing`, `antrag-bapersbw-form`, `gewissensbegruendung-werkstatt` | Antragspaket mit Lebenslauf- und Begründungsplan |
| Antrag liegt, nichts passiert | `eingang-und-pk-nachweis`, `sachstandsanfrage-und-frist`, `untaetigkeitsklage-vwgo-75` | Sachstandsschreiben, Fristenmatrix, Eskalationsplan |
| Soldat oder Soldatin im Dienst | `aktive-soldaten-prioritaet`, `entlassung-berufssoldat-sg-46`, `entlassung-saz-sg-55`, `dienstpflichten-waehrend-verfahren` | Statusstrategie ohne unnötiges Disziplinarrisiko |
| Anhörung oder Zweifel | `schriftliche-anhoerung-kdvg-6`, `muendliche-anhoerung-vorbereitung`, `zweifel-ausraeumen-gesamtvorbringen` | Antwortentwurf, Anhörungsleitfaden, Belegliste |
| Ablehnung | `ablehnungsbescheid-analyse`, `widerspruch-kdvg-9`, `verwaltungsgericht-kdvg-10` | Rechtsbehelfsplan und Klagegerüst |
| 2026-Sonderfall | `wdmodg-2026-uebergang`, `kdvg-13-neun-monate`, `ungedient-vor-2010` | Prüfung der neuen Sonderregeln |

## Keine Totalverweigerung

Dieses Plugin erklärt bei Bedarf die Abgrenzung, unterstützt aber nicht beim bewussten Bruch mit allen Dienst- und Ersatzdienstpflichten. Der Fokus liegt auf der rechtmäßigen, offenen und dokumentierten Berufung auf das Gewissen gegen den Kriegsdienst mit der Waffe.

## Quellenstrategie

- **Amtlich zuerst:** GG, KDVG, WPflG, SG, VwGO, BAFzA-Hinweise, BAPersBw/Bundeswehr-Hinweise.
- **Rechtsprechung verifiziert:** BVerwG und BVerfG nur mit Datum, Aktenzeichen und freiem Link.
- **Aktualität 2026:** Vor Ausgabe immer prüfen, ob Wehrdienstmodernisierung, Bedarfswehrpflicht oder Verwaltungspraxis geändert wurden.
- **Keine Blindzitate:** keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.

## Datenschutz und Sicherheit

Gewissensbegründungen, Gesundheitsdaten, Personalakten, Musterungsunterlagen und Soldatenakten sind hochsensibel. In produktiven Verfahren nur in einem dafür freigegebenen, datenschutz- und berufsrechtskonformen System arbeiten.

## Lizenz

Apache-2.0 OR MIT. Siehe Repository-Stammverzeichnis.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 136 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ablehnungsbescheid-analyse` | Analysiert Tenor, Begründung, Rechtsbehelfsbelehrung und Fehler eines Ablehnungsbescheids. |
| `ablehnungsgruende-kdvg-7` | Zerlegt Ablehnungen wegen Musterungsverweigerung, Unvollständigkeit, ungeeigneter Gründe oder Zweifel. |
| `adressat-und-versandwege` | Prüft Post, Fax, E-Mail, Unterschrift und Zugangsnachweis. |
| `akte-fuer-gericht-aufbauen` | Ordnet Tatsachen, Gewissen, Belege und Verfahrensfehler gerichtsfest. |
| `akteneinsicht-kdv` | Routet Akteneinsicht bei BAFzA, BAPersBw und Gericht. |
| `aktenvernichtung-kdvg-12` | Erklärt Aufbewahrung und Löschung von KDV-Akten. |
| `aktive-soldaten-prioritaet` | Nutzt § 4 KDVG für vorrangige Entscheidung bei laufendem Dienst. |
| `aktuelle-lage-2026` | Prüft keine aktive Einberufung, fortbestehendes KDV-Recht und WDModG-Änderungen. |
| `allgemein` | Kaltstart für Kriegsdienstverweigerung aus Gewissensgründen: Status, Verfahrenslage, Gewissenskern, Antragspfad, Fristen, Rechtsschutz und passende Spezialskills auswählen. |
| `anerkennung-und-dienstfolgen` | Ordnet Folgen der Anerkennung für Wehrpflichtige, Soldaten und Reservisten. |
| `anerkennung-voraussetzungen-kdvg-5` | Prüft Vollständigkeit, geeignete Beweggründe und fehlende Wahrheitszweifel. |
| `anerkennungsbescheid-gueltigkeit` | Erklärt Fortgeltung alter Anerkennungsbescheide und Nachweisstrategien. |
| `angst-karriere-gesundheit-abgrenzen` | Unterscheidet Gewissensgründe von Angst, Karriere, Familienlage und Tauglichkeitsfragen. |
| `anhoerungsprotokoll-und-korrektur` | Prüft Protokoll der Anhörung auf Missverständnisse und Ergänzungsbedarf. |
| `anlagenverzeichnis-kdv` | Erstellt ein nachvollziehbares Anlagenverzeichnis für den KDV-Antrag. |
| `anschreiben-kurz-und-wuerdig` | Erstellt ein kurzes Anschreiben mit Art.-4-Berufung und Anlagenliste. |
| `antrag-bapersbw-form` | Führt durch Adresse, Form, Unterschrift, Lebenslauf und persönliche Begründung. |
| `antrag-zur-niederschrift` | Erklärt Antragstellung zur Niederschrift beim BAPersBw. |
| `anwaltlicher-brief-bafza` | Formuliert Schreiben im inhaltlichen Anerkennungsverfahren. |
| `anwaltlicher-brief-bapersbw` | Formuliert Schreiben zu Eingang, Weiterleitung, Musterung und §13. |
| `arbeitgeber-und-fehlzeit` | Kommuniziert Anhörungstermine datensparsam gegenüber Arbeitgebern. |
| `argumente-die-nicht-tragen` | Markiert KDV-schwache Argumente und passende Alternativwege. |
| `aufschiebende-wirkung-kdvg-3` | Erklärt § 3 KDVG, § 11 KDVG und die Sonderwirkung des § 13 Abs. 3. |
| `ausbildungskosten-rueckforderung` | Prüft mögliche Rückforderungen und Härteargumente nach KDV-bezogenem Ausscheiden. |
| `auslaendischer-wehrdienst-und-asyl` | Trennt deutsche KDV von Asyl-, Auslieferungs- und ausländischem Wehrrecht. |
| `ausland-aufenthalt-wehrpflicht` | Prüft Ruhen der Wehrpflicht und Genehmigungspflichten bei Auslandsaufenthalten. |
| `bafza-entscheidungspfad` | Trennt Registrierung/Zuleitung durch BAPersBw von der inhaltlichen Entscheidung des BAFzA. |
| `bedarfswehrpflicht-wpflg-2a` | Hält das Plugin anschlussfähig an aktivierte Bedarfswehrpflicht. |
| `befehl-und-gewissenskonflikt` | Routet akute Befehlsgewissenskonflikte neben dem KDV-Verfahren. |
| `begruendung-fuer-aktive-soldaten` | Spezialwerkstatt für aktive Soldaten mit früherer Dienstbereitschaft. |
| `begruendung-fuer-ehemalige-anerkannte` | Prüft Widerspruch zwischen alter Anerkennung und späterer Bundeswehrnähe. |
| `begruendung-fuer-reservisten` | Spezialwerkstatt für Reservisten mit früherem Dienst und aktueller Heranziehungsnähe. |
| `begruendung-fuer-ungediente` | Spezialwerkstatt für ungediente Antragsteller ohne Umkehrproblem. |
| `begruendung-redaktion-ohne-schablone` | Überarbeitet persönliche Begründung sprachlich, ohne sie zu standardisieren. |
| `beistand-kirchen-beratung` | Ordnet Beistand, kirchliche Beauftragte und anwaltliche Vertretung. |
| `berufliche-folgen-zivil` | Prüft Arbeitgeber, Ausbildung, Studium und Nachweise außerhalb der Bundeswehr. |
| `berufssoldaten-kdv` | Prüft KDV-Antrag, Entlassungsfolge und Statusrisiken bei Berufssoldaten. |
| `bescheid-archivieren` | Erstellt Nachweis- und Archivstrategie für Anerkennungsbescheide. |
| `beweislast-und-ueberzeugungsbildung` | Erklärt hohe Wahrscheinlichkeit und gerichtliche Überzeugungsbildung. |
| `bverwg-2005-pfaff-befehl` | Ordnet BVerwG 2 WD 12.04 als konkreten Gewissenskonflikt ein. |
| `bverwg-2012-sanitaetsdienst` | Wendet BVerwG 22.02.2012 - 6 C 31.11/6 C 11.11 an. |
| `bverwg-2018-innere-umkehr` | Wendet BVerwG 03.08.2018 - 6 B 124.18 auf Gediente an. |
| `bverwg-2021-parteivernehmung` | Bereitet persönliche gerichtliche Befragung nach BVerwG 31.03.2021 vor. |
| `checkliste-nach-antrag` | Ordnet Eingangsnachweis, Aktenlog, Sachstand und Fristen nach Antragstellung. |
| `checkliste-vor-antrag` | Letztes Qualitätsgate vor Absendung des KDV-Antrags. |
| `datenschutz-gewissensakte` | Schützt Gewissensbegründung, Gesundheitsdaten und Personalakten. |
| `dienstpflichten-waehrend-verfahren` | Minimiert Disziplinarrisiken während laufendem KDV-Antrag. |
| `dienststelle-kommunikation` | Formuliert sachliche Dienststellenkommunikation ohne Provokation. |
| `disziplinarrisiken-soldaten` | Warnt vor Disziplinar- und Strafrisiken bei eigenmächtigem Verhalten. |
| `disziplinarvorgesetzter-stellungnahme` | Erklärt Stellungnahme der Disziplinarvorgesetzten bei Berufs- und Zeitsoldaten. |
| `doppelte-staatsangehoerigkeit` | Routet deutsche KDV und ausländische Wehrpflichten ohne falsche Auslandsversprechen. |
| `eidesstattliche-versicherung` | Prüft, ob eidesstattliche Versicherungen zulässig oder sinnvoll sind. |
| `eilrechtsschutz-drohende-einberufung` | Prüft § 80 oder § 123 VwGO bei drohendem Dienst an der Waffe. |
| `einberufung-nach-antrag` | Prüft, ob Einberufung trotz KDV-Antrag zulässig sein kann. |
| `eingang-und-pk-nachweis` | Sichert Zugang, Aktenzeichen und Fristbeginn für spätere Rechtsschutzschritte. |
| `einstweilige-anordnung-vwgo-123` | Prüft vorläufige Regelung ohne passenden §80-Fall. |
| `europa-menschenrechte-kdv` | Ergänzt EMRK/EU-Grundrechte bei internationalen Bezügen vorsichtig. |
| `familie-partnerschaft-gesellschaftsdruck` | Trennt externe Erwartungen von der eigenen Gewissensentscheidung. |
| `fehlende-rechtsschutzbelehrung` | Prüft Bescheide auf richtige Rechtsbehelfsbelehrung und Fristfolgen. |
| `formularmythen-social-media` | Entlarvt falsche Tipps zu Adresse, Mustern, Fristen und angeblichen Automatismen. |
| `frist-bei-nachforderung-ein-monat` | Prüft Monatsfrist zur Vervollständigung nach § 7 KDVG. |
| `fristenkalender-kdv` | Erstellt Fristenkalender für Antrag, Nachreichung, Anhörung, Widerspruch, § 75 und § 13. |
| `fruehere-soldaten-und-erneute-heranziehung` | Prüft Rechtsschutzinteresse früherer Soldaten wegen möglicher erneuter Heranziehung. |
| `frueherer-abgelehnter-antrag` | Prüft Folgen früherer Ablehnung oder Rücknahme für Schutzwirkung und Glaubhaftigkeit. |
| `fuehrungszeugnis-zweifel` | Erklärt begrenzte Anforderung eines Führungszeugnisses bei Zweifeln. |
| `fwdl-probezeit-und-kdv` | Unterscheidet KDV von einfacher Beendigung des freiwilligen Wehrdienstes. |
| `gesetzliche-vertreter-rechtsbehelfe` | Erklärt Rechte gesetzlicher Vertreter im Widerspruchs- und Gerichtsverfahren. |
| `gewissensbegruendung-werkstatt` | Strukturiert Lebensweg, Auslöser, Wandel und heutige Unbedingtheit ohne fremde Mustersätze. |
| `gewissensentscheidung-massstab` | Prüft schwere Gewissensnot, unbedingte Bindung und Entscheidung gegen Töten im Krieg. |
| `glossar-kdv` | Erklärt Wehrpflicht, Musterung, Anerkennung, Ersatzdienst, BAPersBw und BAFzA. |
| `grundrecht-art-4-abs-3` | Rahmt KDV als staatstreue Grundrechtsausübung statt Staatsablehnung. |
| `humanistische-pazifistische-gruende` | Formt säkulare Ethik in eine persönliche KDV-Begründung. |
| `innere-umkehr-gediente` | Erarbeitet bei Gedienten den grundlegenden Wandel seit früherer Dienstbereitschaft. |
| `karrierecenter-und-bapersbw` | Erklärt Behördennamen, Wehrersatzbehörde und frühere Kreiswehrersatzamt-Begriffe. |
| `kdvg-13-neun-monate` | Nutzt § 13 Abs. 2 KDVG als Argument gegen unbegrenztes Liegenlassen. |
| `kein-totalverweigerungs-tool` | Grenzt KDV vom bewussten Bruch mit jeder Dienst- oder Ersatzdienstpflicht ab. |
| `ki-nutzung-gewissensbegruendung` | Setzt Grenzen für KI-Hilfe: strukturieren ja, fremde Begründung nein. |
| `klage-ohne-berufung` | Erklärt § 10 KDVG und warum erstinstanzliche Sorgfalt besonders wichtig ist. |
| `kommunikation-mit-familie` | Erklärt KDV ruhig gegenüber Familie und Umfeld ohne private Überoffenbarung. |
| `kosten-und-auslagen-anhoerung` | Prüft Auslagen, Entgeltfortzahlung und notwendige Aufwendungen bei Anhörung. |
| `lebensfuehrung-und-plausibilitaet` | Prüft, welche Lebensstationen die Gewissensentscheidung stützen oder erklären. |
| `lebenslauf-luecken-und-widersprueche` | Bearbeitet frühere Waffenaffinität, Bundeswehrbewerbung oder Lebenslauflücken ehrlich. |
| `mehrsprachige-orientierung` | Hilft Nicht-Muttersprachlern mit deutschen KDV-Begriffen ohne falsche Übersetzungssicherheit. |
| `minderjaehrige-antragstellung` | Prüft Antrag sechs Monate vor 18 oder vor 17 unter Sondervoraussetzungen. |
| `muendliche-anhoerung-vorbereitung` | Bereitet nichtöffentliche mündliche Anhörung ohne auswendig gelernte Musterantworten vor. |
| `musterung-verweigert-ablehnung` | Erklärt Ablehnungsrisiko bei Musterungsverweigerung. |
| `musterungen-und-eignung` | Erklärt, warum KDV-Antrag Musterung grundsätzlich nicht ersetzt und wie § 13 wirkt. |
| `musterungsbescheid-bestandskraft` | Prüft Bedeutung des Musterungsbescheids für Zuleitung und Entscheidung. |
| `nachreichung-fehlender-unterlagen` | Formuliert fristwahrende Nachreichungen nach behördlicher Aufforderung. |
| `notfallplan-vor-dienstantritt` | Erstellt 24/48-Stunden-Plan bei kurzfristiger Musterung, Übung oder Dienstantritt. |
| `parteivernehmung-vorbereiten` | Bereitet persönliche gerichtliche Befragung ehrlich und konsistent vor. |
| `personalakte-und-datenschutz-soldaten` | Prüft Personalaktenzuleitung und Datenschutz bei Soldaten-KDV. |
| `personenkennziffer-und-grundakte` | Erklärt Registrierung, PK, Grundakte und Zuleitung im BAPersBw-Verfahren. |
| `politische-motive-abgrenzen` | Trennt allgemeine Gewissensentscheidung von Kritik an einem bestimmten Krieg oder Staat. |
| `presseanfragen-und-kdv` | Hilft bei öffentlicher Kommunikation ohne Verfahrensschaden. |
| `psychische-belastung-und-beratung` | Routet Belastungen durch Gewissenskonflikt zu Hilfe ohne Pathologisierung. |
| `qualitaetsgate-vor-ausgabe` | Erzwingt Normstand, Behördenstand, Statusprüfung, Quellenhygiene und Abgrenzung zur Totalverweigerung. |
| `recht-auf-entscheidung-mein-gewissen-schlaeft-nicht` | Formuliert grundrechtsbewusst, warum eine ernste Gewissensentscheidung nicht beliebig liegen bleiben darf. |
| `rechtsanwaltliche-vollmacht` | Erstellt Vollmacht, Akteneinsicht und Zustellungsbitte. |
| `rechtsprechung-livecheck` | Prüft KDV-Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und Link. |
| `rechtsschutzbeduerfnis-pruefen` | Prüft Sachbescheidungsinteresse bei ausgesetzter Wehrpflicht und Soldatenstatus. |
| `religioese-weltanschauliche-gruende` | Ordnet religiöse, humanistische und weltanschauliche Gründe ohne Bekenntniszwang. |
| `reservisten-heranziehung` | Prüft KDV bei Beorderung, Heranziehungsbescheid und Übungen. |
| `ruecknahme-oder-verzicht` | Erklärt Rücknahme eines Antrags oder Verzicht auf Anerkennung. |
| `sachstandsanfrage-und-frist` | Formuliert gezielte Sachstandsanfragen vor Eskalation in § 75 VwGO. |
| `sanitaetsdienst-und-waffenloser-dienst` | Setzt BVerwG 2012 zu Sanitätsdienst und waffenlosem Dienst um. |
| `schluesselerlebnis-oder-wandel` | Unterscheidet einzelne Schlüsselerlebnisse und längere innere Wandelungsprozesse. |
| `schriftliche-anhoerung-kdvg-6` | Beantwortet Zweifel des BAFzA konkret, wahrhaftig und belegbar. |
| `sicherheitsueberpruefung-und-extremismus` | Trennt Gewissensentscheidung von Loyalitäts- oder Extremismusvorwürfen. |
| `social-media-und-oeffentlichkeit` | Prüft Posts, öffentliche Kampagnen und Dienstgeheimnisse im KDV-Kontext. |
| `sofortvollzug-und-anordnung` | Prüft Sofortvollzug und aufschiebende Wirkung im KDV-Kontext. |
| `soldat-auf-zeit-kdv` | Prüft KDV, § 55 SG und Nebenfolgen bei Soldaten auf Zeit. |
| `soldatinnen-und-kdv` | Stellt KDV-Rechte von Frauen dar, die dienen oder früher gedient haben. |
| `spannungs-verteidigungsfall` | Prüft Sonderregeln im Spannungs-, Verteidigungs- und Bereitschaftsdienstfall. |
| `sprache-der-loyalitaet` | Formuliert staatstreu und grundgesetznah ohne Unterwürfigkeit. |
| `sprachlich-einfache-erklaerung` | Erklärt KDV in einfacher Sprache für Menschen ohne Juristensprache. |
| `status-routing` | Bestimmt, ob jemand ungedient, wehrpflichtig, Soldat, Reservist, frühere Soldatin oder Sonderfall ist. |
| `stellungnahmen-dritter` | Prüft, wann Wahrnehmungen Dritter nach § 2 Abs. 3 KDVG helfen. |
| `ungedient-ab-2010` | Prüft jüngere ungediente Personen, Antragstermin und fehlendes aktuelles Bescheidungsinteresse. |
| `ungedient-vor-2010` | Wendet § 13 KDVG n. F. auf vor 2010 geborene ungediente Wehrpflichtige an. |
| `untaetigkeitsklage-vwgo-75` | Prüft Rechtsschutz bei Nichtbescheidung und grenzt diffuse Untätigkeitsbeschwerde ab. |
| `unterlagenmappe-kdv` | Strukturiert Antrag, Lebenslauf, Begründung, Belege, Nachweise und Bescheide. |
| `verwaltungsakt-oder-informelles-schreiben` | Unterscheidet Bescheid, Aufforderung, Sachstand und informelle E-Mail. |
| `verwaltungsgericht-kdvg-10` | Routet Klage und gerichtliche Besonderheiten in KDV-Sachen. |
| `vollstaendiger-lebenslauf` | Erstellt einen vollständigen, datensparsamen Lebenslauf mit gewissensrelevanten Stationen. |
| `vollstaendigkeit-kdvg-2` | Prüft Anschreiben, Art.-4-Berufung, Lebenslauf und persönliche Begründung. |
| `waffenbesitz-jagd-schuetzenverein` | Unterscheidet zivilen Waffenbezug von Kriegsdienst mit der Waffe. |
| `wahrheitspflicht-und-authentizitaet` | Entfernt austauschbare KI-/Musterprosa und stärkt eigene Sprache. |
| `wehrpflicht-ruht-ausland` | Prüft Ruhen der Wehrpflicht bei ständiger Lebensgrundlage im Ausland. |
| `widerspruch-fristen-sonderlagen` | Prüft normale und verkürzte Widerspruchsfristen, insbesondere § 11 KDVG. |
| `widerspruch-kdvg-9` | Erstellt Widerspruch gegen Ablehnung oder verfahrensrelevante Entscheidung. |
| `zeugenauswahl-und-aussage` | Prüft geeignete Zeugen für persönliche Entwicklung und Lebensführung. |
| `zivildienst-altfaelle` | Prüft Dienstzeit- oder Anerkennungsbescheinigungen aus früherem Zivildienst. |
| `ziviler-ersatzdienst-art-12a` | Erklärt Ersatzdienst nach Art. 12a GG und § 1 Abs. 2 KDVG. |
| `zweifel-ausraeumen-gesamtvorbringen` | Bearbeitet Zweifel aus Gesamtvorbringen und bekannten Tatsachen. |
| `zweitbescheid-bescheinigung` | Formuliert Antrag auf Bestätigung oder Zweitausfertigung einer früheren Anerkennung. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
