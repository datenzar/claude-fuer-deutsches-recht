# DFG-Förderantrag

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`dfg-foerderantrag`) | [`dfg-foerderantrag.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/dfg-foerderantrag.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

Plugin für die praktische Antragstellung bei der Deutschen Forschungsgemeinschaft: Sachbeihilfe, elan-Formalia, Projektbeschreibung, Finanzplan, Forschungsdaten, Ethik-/KI-Check, Reviewer-Perspektive, Wiedereinreichung und strategische Entscheidung zwischen kleinem schnellen Antrag und großem Prestigeprojekt.

Der Stil ist bewusst nicht bürokratisch. Das Plugin fragt zuerst: Was ist wissenschaftlich stark, was ist realistisch förderbar, was kann schneller entschieden werden und wo ist der große Antrag zwar verführerisch, aber prozessual zäher? Es arbeitet adaptiv: Anfänger bekommen eine geführte Mini-Roadmap; erfahrene Antragsteller bekommen direkt Red-Team, Kürzungsrisiko und Programmstrategie.

## Quellen-Gate

Vor jeder belastbaren Ausgabe aktuelle DFG-Seiten prüfen:

- DFG Sachbeihilfe: themenoffene Einzelförderung, Neuanträge jederzeit, Fortsetzungsanträge spätestens 6 Monate vor Mittelverbrauch.
- DFG Begutachtung: grundsätzlich zwei Gutachten; bei Anträgen bis 200.000 Euro kann ausnahmsweise ein aussagekräftiges externes Gutachten reichen.
- Reinhart-Koselleck-Projekte: 500.000 bis 1,25 Mio. Euro für fünf Jahre in Stufen von 250.000 Euro; nur für herausragende, besonders innovative oder risikobehaftete Projekte, die nicht in normale Verfahren passen.
- DFG-Merkblätter, elan-Vorlagen, fachzuständige Ansprechpersonen und aktuelle Vordruckstände immer live gegen `dfg.de` prüfen.

## Schnellstart

```text
/dfg-foerderantrag:allgemein
```

Der Allgemein-Skill führt in 60 Sekunden durch: Forschungsfrage, Förderprogramm, Summe, Tempo, Zielgruppe der Begutachtung, Vorarbeiten, Risiken, Daten-/Ethikthemen und gewünschtes Ergebnis.

Typische Startpunkte:

| Situation | Start |
| --- | --- |
| "Ich habe nur eine Forschungsidee" | `allgemein` → Mini-Roadmap und Minimalprojekt |
| "Sachbeihilfe oder größer?" | `dfg-foerderstrategie-schnell-oder-gross` |
| "Entwurf liegt vor" | `dfg-reviewer-red-team` → danach Text- und Finanzskills |
| "Ablehnung liegt vor" | `dfg-wiedereinreichung-nach-ablehnung` |

## Skill-Matrix

| Skill | Wofür? |
| --- | --- |
| `allgemein` | Einstieg, Triage, Programmroute und erster Arbeitsplan |
| `dfg-foerderstrategie-schnell-oder-gross` | Entscheidung: kleiner schneller Antrag, normale Sachbeihilfe, Koselleck oder anderes Programm |
| `dfg-sachbeihilfe-elan-formalia` | Sachbeihilfe, elan, Anlagen, Vordrucklogik, formales Gate |
| `dfg-bis-200k-begutachtung-light` | Kleine/mittlere Anträge so bauen, dass sie schnell, klar und begutachtbar sind |
| `dfg-koselleck-500k-125m` | Koselleck-Check: 500.000 bis 1,25 Mio. Euro, Risiko, Profil, Vertrauensvorschuss |
| `dfg-projektbeschreibung-arbeitsprogramm` | Forschungsfrage, Stand der Forschung, Ziele, Arbeitspakete, Meilensteine |
| `dfg-finanzplan-module-personal-geraete` | Personal, Geräte, Reisen, Workshops, Mercator Fellow, Chancengleichheit, Budgetbegründung |
| `dfg-reviewer-red-team` | Gutachterperspektive, Angriffsflächen, Kürzungsrisiken, Ablehnungsgründe |
| `dfg-wiedereinreichung-nach-ablehnung` | Ablehnung auswerten, Gutachten ernst nehmen, Neuaufstellung |
| `dfg-ki-ethik-forschungsdaten` | KI-Nutzung, Vertraulichkeit, Forschungsdatenmanagement, Ethik und Datenschutz |

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Adaptiver Einstieg, Schnelltriage und Workflow-Routing im DFG-Förderantrag-Plugin. Führt Anfänger mit maximal sechs Fragen, fordert Profis mit Go/No-Go und Reviewer-Risiken, klärt Forschungsfrage, Programmroute, Antragssumme, Tempo, Vora... |
| `dfg-bis-200k-begutachtung-light` | Kleine und mittlere DFG-Anträge bis 200.000 Euro begutachtungsfreundlich bauen: klare Kernfrage, schlanker Finanzplan, ein Gutachten möglich, schnelle Lesbarkeit, Fortsetzungsfähigkeit. |
| `dfg-eigenanteil-und-grundausstattung` | Eigenanteil und Grundausstattung der Hochschule sauber von DFG-Foerderung abgrenzen: Was muss die Hochschule stellen (Buero, Standardrechner, Sekretariat, Bibliothek), was darf die DFG finanzieren (projektspezifische Geraete, Personal ue... |
| `dfg-eigene-vorarbeiten-darstellen` | Eigene Vorarbeiten in DFG-Antrag richtig darstellen: bisher publizierte Ergebnisse, eigene Methodik-Beitraege, Pilotdaten. Reviewer-Perspektive: Anknuepfungsfaehigkeit pruefen, keine Selbstplagiat-Pruefung. Mustertext fuer 2-Seiten-Kapitel. |
| `dfg-erstantragsteller-besondere-checks` | Erstantragsteller-Spezialcheck: Promotion abgeschlossen, gute eigene Vorarbeit (Publikationen Erst- und Letztautor), Anbindung an erfahrene Person ohne Co-Antragstellung wenn moeglich, Lebenslauf mit Eltern- und Pflegezeiten transparent,... |
| `dfg-finanzplan-module-personal-geraete` | DFG-Finanzplan und Modulbegründung erstellen: Personal, Geräte, Verbrauchsmittel, Reisen, Workshops, Mercator Fellow, Chancengleichheit, Öffentlichkeitsarbeit, Kostenlogik und Kürzungsabwehr. |
| `dfg-foerderstrategie-schnell-oder-gross` | Strategischer DFG-Router: entscheidet zwischen kleiner schneller Sachbeihilfe, normalem Antrag über 200.000 Euro, Koselleck ab 500.000 Euro oder anderem DFG-Programm. Enthält Spatz-in-der-Hand-Logik, Kürzungsrisiko, Begutachtungsdichte u... |
| `dfg-grossgeraete-und-cluster-antrag` | Grossgeraete und Cluster-Geraete in DFG-Antrag: Geraete ab 50.000 Euro mit zusaetzlicher Wirtschaftlichkeit, Auslastungsplan, technische Anschlussbedingungen, Wartungsvertrag, Folgekosten. Eigene Geraetekommission der DFG. Pruefraster fu... |
| `dfg-grundsystem-foerderlinien` | Grundsystem der DFG-Foerderlinien einfuehrend erklaeren: Sachbeihilfe (Einzelantrag), Emmy Noether, Heisenberg, Reinhart Koselleck, SFB, GRK, Forschergruppen, Schwerpunktprogramme. Pro Linie: Zielgruppe, Hoehe, Dauer, Antragsweg, Begutac... |
| `dfg-internationale-kooperation-aufbau` | Internationale Kooperation in DFG-Antrag aufbauen: D-A-CH-Lead-Agency-Verfahren (DACH, SNF, FWF), Bilateral mit DFG-Partnerorganisationen (NSF, JSPS, ISF, NSFC). Kooperationszusagen, Mittelverteilung, Hauptantragsteller, Co-Antragsteller... |
| `dfg-ki-ethik-forschungsdaten` | DFG-Antrag auf KI-Nutzung, Ethik, Datenschutz, Forschungsdatenmanagement und gute wissenschaftliche Praxis prüfen. Behandelt Vertraulichkeit in Begutachtung, Datenmanagementplan, sensible Daten, Open Access und Nachnutzung. |
| `dfg-kollegen-review-organisieren` | Kollegen-Review eines DFG-Antrags strukturiert organisieren: 2 erfahrene Profs aus dem Fach plus 1 Methodik-Kollege, Briefing-Mail, Review-Raster (Originalitaet, Arbeitsprogramm, Finanzplan, Vorarbeiten), 1-Wochen-Frist. Output Vorlage B... |
| `dfg-koselleck-500k-125m` | Reinhart-Koselleck-Projekt prüfen und entwerfen: 500.000 Euro bis 1.250.000 Euro, 5 Jahre, Stufen von 250.000 Euro, außergewöhnliches Profil, positives Risiko, Vertrauensvorschuss, Abgrenzung zur Sachbeihilfe. |
| `dfg-praeregistrierung-replication-studies` | Praeregistrierung und Replikationsstudien im DFG-Antrag: Hypothesen ex ante festlegen, registered reports, OSF-Praeregistrierung, Replikationsplaene als eigenstaendiges Vorhaben. DFG-Statement to scientific integrity. Vorteile fuer Revie... |
| `dfg-projektbeschreibung-arbeitsprogramm` | DFG-Projektbeschreibung und Arbeitsprogramm ausarbeiten: Forschungslücke, Stand der Forschung, Ziele, Hypothesen, Methoden, Arbeitspakete, Meilensteine, Risiken, Forschungsdaten und verwertbare Antragssprache. |
| `dfg-publikationsstrategie-projekt` | Publikationsstrategie fuer das beantragte Projekt: realistische Zahl Publikationen, geplante Zeitschriften mit Impact und Open-Access-Status, DFG-Open-Access-Politik, Praeprints, Datenpublikation. Im Antrag muss Publikationsplan zu Arbei... |
| `dfg-replikationskrise-statistik-spezial` | Spezialfall Statistikabschnitt nach Replikationskrise: a-priori-Power-Analyse, Effektgroessenschaetzung, Vorab-Festlegung Hypothesen, Korrektur fuer multiple Testung, Sensitivitaetsanalysen. Pruefraster fuer Reviewer-Akzeptanz. |
| `dfg-reviewer-red-team` | DFG-Antrag aus Gutachterperspektive red-teamen: Originalität, Machbarkeit, Arbeitsprogramm, Qualifikation, Umfeld, Bias-Risiken, Kürzungsargumente, Ablehnungsrisiken und Verbesserungsplan. |
| `dfg-sachbeihilfe-elan-formalia` | DFG-Sachbeihilfe und elan-Formalia prüfen: Antragsberechtigung, Module, Vordrucke, Anlagen, Seitenlogik, Fachzuordnung, Fortsetzungsantrag, internationale Kooperation, formale Einreichungsreife. |
| `dfg-software-veroeffentlichung-spezial` | Spezialfall Software als Forschungsergebnis: DFG-Hinweise zur Open-Source-Veroeffentlichung, Lizenzwahl (MIT, BSD, Apache-2.0, GPL), Zenodo-DOI, Reproducibility. Pruefraster und Mustertext fuer Software-Sektion im Arbeitsprogramm. |
| `dfg-tieforschung-ethik-pflichten` | Tierversuchsethik-Pflichten in DFG-Antraegen: 3R-Prinzip (Replace, Reduce, Refine), TierSchG, TierSchVersV, Tierversuchsantrag bei der Behoerde parallel zur DFG. DFG-Senatskommission fuer tierexperimentelle Forschung. Ethik-Sektion im An... |
| `dfg-wiedereinreichung-nach-ablehnung` | DFG-Ablehnung, Gutachten und Entscheidung auswerten: tragende Kritik extrahieren, Verteidigungsreflex vermeiden, Wiedereinreichung planen, Antrag umbauen, Anschreiben und Änderungsmatrix erstellen. |
| `dfg-zeitplan-und-meilensteine` | Antragszeitplan vom ersten Skizzen-Entwurf bis zur Einreichung in elan strukturieren: 6 Monate vorher Themenfindung, 4 Monate vorher Literaturrecherche und Arbeitsprogramm, 3 Monate vorher Finanzplan, 6 Wochen vorher Kollegenreview, 2 Wo... |
| `dfg-zwischen-und-abschlussbericht` | Zwischen- und Abschlussbericht systematisch vorbereiten: Berichtsraster der DFG, Soll-Ist-Abgleich Arbeitsprogramm, Publikationen, Personal, Geraete, Mittelabfluss. Abschlussbericht ist gleichzeitig Bewertungsbasis fuer Folgeantrag. Typi... |
| `spezial-adaptive-dokumentenmatrix-und-lueckenliste` | Adaptive: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-anfaenger-risikoampel-und-gegenargumente` | Anfaenger: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-antraege-zahlen-schwellen-und-berechnung` | Antraege: Zahlen, Schwellenwerte und Berechnung im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-dfg-erstpruefung-und-mandatsziel` | DFG: Erstprüfung, Rollenklärung und Mandatsziel im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-elan-formular-portal-und-einreichung` | Elan: Formular, Portal und Einreichungslogik im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-ethik-abschlussprodukt-und-uebergabe` | Ethik: Abschlussprodukt und Übergabe im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-finanzplan-mandantenkommunikation-entscheidungsvorlage` | Finanzplan: Mandantenkommunikation und Entscheidungsvorlage im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-foerderantragssteller-tatbestand-beweis-und-belege` | Foerderantragssteller: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-formalia-red-team-und-qualitaetskontrolle` | Formalia: Red-Team und Qualitätskontrolle im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-forschungsdaten-fristennotiz-und-naechster-schritt` | Forschungsdaten: Fristennotiz und nächster Schritt im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-fuehrung-schriftsatz-brief-und-memo-bausteine` | Fuehrung: Schriftsatz-, Brief- und Memo-Bausteine im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-grosse-compliance-dokumentation-und-akte` | Grosse: Compliance-Dokumentation und Aktenvermerk im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-kleine-verhandlung-vergleich-und-eskalation` | Kleine: Verhandlung, Vergleich und Eskalation im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-koselleck-mehrparteien-konflikt-und-interessen` | Koselleck: Mehrparteienkonflikt und Interessenmatrix im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-profi-behoerden-gericht-und-registerweg` | Profi: Behörden-, Gerichts- oder Registerweg im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-reviewer-beweislast-und-darlegungslast` | Reviewer: Beweislast, Darlegungslast und Substantiierung im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-sachbeihilfe-fristen-form-und-zustaendigkeit` | Sachbeihilfe: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-schnelle-livequellen-und-rechtsprechungscheck` | Schnelle: Livequellen- und Rechtsprechungscheck im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-strategien-internationaler-bezug-und-schnittstellen` | Strategien: Internationaler Bezug und Schnittstellen im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-team-sonderfall-und-edge-case` | Team: Sonderfall und Edge-Case-Prüfung im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin dfg-foerderantrag: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin dfg-foerderantrag: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin dfg-foerderantrag: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin dfg-foerderantrag: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin dfg-foerderantrag: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin dfg-foerderantrag: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin dfg-foerderantrag: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin dfg-foerderantrag: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin dfg-foerderantrag: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin dfg-foerderantrag: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
