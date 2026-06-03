# Produkthaftung und Produktrecht (Plugin `produktrecht`)

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`produktrecht`) | [`produktrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/produktrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **BGB BT — Smart-Kühlschrank, digitale Elemente und Reparaturblockade** (`bgb-bt-smart-kuehlschrank-digital-repair-koeln`) | [Gesamt-PDF lesen](../testakten/bgb-bt-smart-kuehlschrank-digital-repair-koeln/gesamt-pdf/bgb-bt-smart-kuehlschrank-digital-repair-koeln_gesamt.pdf) | [`testakte-bgb-bt-smart-kuehlschrank-digital-repair-koeln.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bgb-bt-smart-kuehlschrank-digital-repair-koeln.zip) |
| **Projekt Isarlicht — Kernfusion und Transrapid am Starnberger See** (`kernfusion-transrapid-starnberger-see`) | [Gesamt-PDF lesen](../testakten/kernfusion-transrapid-starnberger-see/gesamt-pdf/kernfusion-transrapid-starnberger-see_gesamt.pdf) | [`testakte-kernfusion-transrapid-starnberger-see.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kernfusion-transrapid-starnberger-see.zip) |
| **Produkthaftung Frischwind Mobility GmbH — Akku-Brände E-Bike Wind-X7, Produktrückruf, Strafverfahren** (`produkthaftung-akku-brand-e-bike-frischwind-mobility-erfurt`) | [Gesamt-PDF lesen](../testakten/produkthaftung-akku-brand-e-bike-frischwind-mobility-erfurt/gesamt-pdf/produkthaftung-akku-brand-e-bike-frischwind-mobility-erfurt_gesamt.pdf) | [`testakte-produkthaftung-akku-brand-e-bike-frischwind-mobility-erfurt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-produkthaftung-akku-brand-e-bike-frischwind-mobility-erfurt.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Rechtliche Abläufe für Produktteams, Hersteller, Händler und Kanzleien: Produktsicherheit, Produkthaftung, Produktbeobachtung, Rückruf, Marktüberwachung, Software-/OTA-Updates, Right to Repair und Launch-Review. Der Ordner heißt weiter `produktrecht`, damit bestehende Links stabil bleiben; inhaltlich ist das Plugin jetzt ausdrücklich auch ein Produkthaftungs- und Produktlebenszyklus-Plugin.

Es trennt sauber zwischen Produktsicherheit/Behördenpflichten, verschuldensunabhängiger Produkthaftung, deliktischer Produzentenhaftung, vertraglicher Gewährleistung, digitalem Kaufrecht und künftigen Reparaturpflichten. Gerade bei vernetzten Waren wird nicht mehr gefragt “Hardware oder App?”, sondern: Welche Funktion hängt an Firmware, Cloud, Konto, Sensorik, Update oder Reparaturzugang?

**Alle Ausgaben sind Entwürfe zur anwaltlichen Prüfung – zitiert, markiert und abgesichert – keine rechtlichen Schlussfolgerungen.** Das Plugin erledigt die Arbeit: liest Dokumente, wendet Ihr Playbook an, findet Probleme, erstellt das Memo. Ein Anwalt prüft, verifiziert und entscheidet. Zitate sind nach Quelle gekennzeichnet. Berufsrechtliche Verschwiegenheitspflichten (§ 43a Abs. 2 BRAO, § 203 StGB) werden konservativ angewendet. Folgenreiche Maßnahmen – Abmahnungen, Einreichungen, Vertragsunterzeichnungen – sind durch explizite Bestätigung gesichert.

## Für wen ist dieses Plugin?

| Rolle | Hauptworkflows |
|---|---|
| **Produktjurist / Syndikusanwalt** | Launch-Review, Produktsicherheit, GPSR, Rückruf, Repair-/Update-Policy |
| **Produkthaftungsanwalt** | ProdHaftG, § 823 BGB, Produzentenhaftung, Beweisakte, Serienfehler, Regress |
| **Produktmanager / Engineering** | "Ist-das-ein-Problem?"-Triage, Software-/OTA-Änderungen, Repair-by-design |
| **Marketing / Brand** | Werbeaussagen-Prüfung vor Veröffentlichung |
| **GC / Leiter Rechtsabteilung** | Eskalierte Produktfälle, Marktüberwachung, Behördenkommunikation, Krisenstab |

## Erster Start: das Kaltstart-Interview

Verbindet sich mit Ihrem Launch-Tracker (Jira/Linear), liest zehn vergangene Launch-Reviews, lernt was Sie tatsächlich blockieren vs. durchwinken. Erstellt eine Risikokalibrierungstabelle, auf die jeder andere Skill zurückgreift.

Ihre Konfiguration wird unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/produktrecht/CLAUDE.md` gespeichert und überlebt Plugin-Updates.

```
/produktrecht:produktrecht-kaltstart-interview
```

## Befehle

| Befehl | Funktion |
|---|---|
| `/produktrecht:produktrecht-kaltstart-interview` | Kaltstart-Interview |
| `/produktrecht:launch-pruefung [PRD oder Ticket]` | Vollständiger Launch-Review gegen Ihr Framework |
| `/produktrecht:werbeaussagen-pruefung [Text]` | Werbeaussagen-Prüfung |
| `/produktrecht:ist-das-ein-problem [Frage]` | Schnelle "Ist-das-ein-Problem?"-Antwort |
| `/produktrecht:feature-risikobewertung [Feature]` | Tiefgehende Feature-Risikobewertung |
| `/produktrecht:impressum-pflicht` | Impressumspflichten prüfen (DDG, MStV) |
| `/produktrecht:preisangaben` | Preisangabenpflichten prüfen (PAngV) |
| `/produktrecht:produktrecht-mandat-arbeitsbereich` | Mandate verwalten (nur Multi-Mandanten-Praxis) |

## Skills

| Skill | Zweck |
|---|---|
| **kaltstart-interview** | Erstellt `~/.claude/plugins/config/claude-fuer-deutsches-recht/produktrecht/CLAUDE.md` aus Interview + vergangenen Launch-Reviews |
| **launch-pruefung** | Kategorie-für-Kategorie-Review, kalibriert auf Ihr Unternehmen (Sieben-Kategorien-Framework: Werberecht, Datenschutz, Produktsicherheit, AGB, Verbraucherrechte, Geistiges Eigentum, Aufsichtsrecht) |
| **werbeaussagen-pruefung** | Werbeaussagen-Taxonomie: Marktschreierische Anpreisung / Tatsachenbehauptung / Vergleich / implizierte Aussage / absolute Aussage; Prüfung nach §§ 5, 5a, 5b UWG und PAngV |
| **feature-risikobewertung** | Tiefgehende Analyse eines einzelnen Features (UWG, DSGVO, DSA, KI-VO, Verbraucherschutz BGB) |
| **ist-das-ein-problem** | Gleich-Minuten-Triage für die schnelle Slack-Frage |
| **impressum-pflicht** | Anbieterkennzeichnung §§ 5, 6 DDG (vormals TMG), § 18 MStV |
| **preisangaben** | PAngV-Prüfung: Gesamtpreis, Grundpreis, Streichpreise, Versandkosten |
| **mandat-arbeitsbereich** | Mandate anlegen, auflisten, wechseln und schließen für Multi-Mandanten-Praxis; isoliert Mandanten/Mandate so dass kein Kontext leckt |

## Interaktive Befehle vs. geplante Agenten

Die obigen Befehle laufen bei Aufruf – für laufende Arbeit an einem Mandat. Die Agenten unten laufen auf einem Zeitplan – für das, was sich bewegt während Sie nicht hinschauen:

| Agent | Was wird überwacht | Standard-Takt |
|---|---|---|
| **markteinführungs-monitor** | Launch-Tracker (Jira/Linear) auf bevorstehende Launches die wahrscheinlich rechtliche Prüfung benötigen; filtert Tickets mit Launch-Terminen in den nächsten 30 Tagen per Kalibrierungstabelle | Täglich |

## Integrationen

**Verbinden Sie zuerst ein Recherche-Tool – die Zitatschranken hängen davon ab.** Ohne eines wird jede Quellenangabe als `[prüfen]` markiert und der Prüfvermerk über jeder Ausgabe hält fest, dass Quellen nicht verifiziert wurden. Skills arbeiten beides; ein Recherche-Tool verschiebt Verifikationsarbeit von Ihrer Schulter.

Ausgeliefert mit in `.mcp.json` konfigurierten Konnektoren:

- **Slack** – Nachrichten suchen, Kanäle lesen, Diskussionen finden
- **Google Drive** – Dokumente suchen, lesen und abrufen
- **Linear** – Issue-Tracking und Projektmanagement
- **Atlassian** – Jira-Issues und Confluence-Seiten
- **Asana** – Aufgaben und Projekt-Tracking

Mit verbundenem Tracker: Kaltstart liest Launch-Historie, launch-pruefung liest Ticket-Kontext, markteinführungs-monitor-Agent überwacht den Kalender.

## Schnellstart

```
/produktrecht:produktrecht-kaltstart-interview
```

Dann:

```
/produktrecht:ist-das-ein-problem "Können wir den Preis auf der Preisseite A/B-testen?"
```

→ Antwort in einer Minute, kalibriert auf Ihre Risikotabelle.

```
/produktrecht:launch-pruefung PROJ-1234
```

→ Vollständiger Review, Kategorie für Kategorie, mit Aufgabenliste.

## Wie das Plugin lernt

Ihr Praxisprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/produktrecht/CLAUDE.md` ist nicht statisch – es verbessert sich durch Nutzung. Skills zeigen an, wenn eine Ausgabe eine Standard-Einstellung verwendet hat, die Sie anpassen sollten. Sie können das Setup erneut ausführen, die Datei direkt bearbeiten oder einem Skill mitteilen, eine neue Position zu erfassen.

## Wichtige Normen dieses Plugins

- **UWG** (§§ 3, 5, 5a, 5b, 7 – unlautere Werbung, Irreführung, Belästigung)
- **PAngV 2022** (Preisangabenpflichten, Grundpreis § 4, Streichpreise § 11)
- **BGB §§ 305 ff.** (AGB-Kontrolle, Einbeziehung, Inhaltskontrolle)
- **DDG** (vormals TMG – Impressumspflicht §§ 5, 6, Haftung §§ 7 ff.)
- **TDDDG** (Cookie-Einwilligung, § 25 TDDDG)
- **ProdHaftG / § 823 BGB** (verschuldensunabhängige Produkthaftung und deliktische Produzentenhaftung)
- **ProdSG / GPSR VO (EU) 2023/988** (Produktsicherheit, Marktüberwachung, Rückverfolgbarkeit, Safety Business Gateway)
- **BGB §§ 327 ff., 434, 475b, 475c, 475e, 476, 477** (digitale Produkte, Waren mit digitalen Elementen, Updatepflichten, Beweislast, Verjährung)
- **Richtlinie (EU) 2024/1799** (Recht auf Reparatur; Umsetzungsstand jeweils live prüfen)
- **Richtlinie (EU) 2024/2853** (neue Produkthaftungsrichtlinie; Umsetzung und zeitliche Anwendbarkeit live prüfen)
- **MarkenG** (Markenverletzung, Benutzungsmarken, Verwechslungsgefahr)
- **AGG** (Diskriminierungsverbot, Benachteiligung)
- **EU-Verordnungen:** DSA, DMA, KI-VO (AI Act, EU 2024/1689)

## Hinweise

- Die Kalibrierungstabelle ist das Herzstück. Wenn sie falsch ist, ist jeder Review falsch. Neu ausführen wenn sich Ihre Risikoposition ändert (neues Regulierungsumfeld, neuer GC, neue Bußgeld-Entscheidung).
- `ist-das-ein-problem` ist so konzipiert, dass PMs es eigenständig nutzen können. Es antwortet schnell und leitet zu einer echten Prüfung weiter, wenn nötig.
- Feature-Risikobewertung ist für die 10% der Launches, die Tiefe benötigen. Die meisten tun es nicht – keine unnötige Dokumentenpflege.
- GPSR ist VO (EU) 2023/988. Die BatterieVO ist VO (EU) 2023/1542 und nur bei Batterie-/Akkubezug einschlägig.
- Right to Repair und neue Produkthaftungsrichtlinie sind in Übergang und Umsetzung zu behandeln. Tragende Aussagen zum deutschen Umsetzungsstand immer live verifizieren.

## Voraussetzungen

Einige Features referenzieren externe Integrationen (Dokumentenmanagementsystem, Launch-Tracker, Fallmanagementsystem, Regulierungs-Feeds). Diese sind nicht mitgeliefert – wenn Sie einen MCP-Server dafür in Ihrer Umgebung haben, verwenden ihn die relevanten Features. Ohne einen fällt das Plugin auf Datei-Upload und manuelle Abläufe zurück. Führen Sie `/produktrecht:produktrecht-kaltstart-interview --check-integrations` aus um zu sehen, was in Ihrer Umgebung verfügbar ist.

## Konfiguration

Ihre Konfiguration wird unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/produktrecht/CLAUDE.md` gespeichert und überlebt Plugin-Updates – Sie führen das Setup nur einmal aus.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 60 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Produktrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei D... |
| `ce-kennzeichnung-routenplan` | CE-Kennzeichnung systematisch planen: Identifikation einschlaegiger Richtlinien (Maschinen, Niederspannung, EMV, RED, Medizinprodukte, Spielzeug, PSA), Konformitaetsbewertungsverfahren wie Modul A bis H, technische Dokumentation, EU-Konf... |
| `dual-use-produktrecht` | Dual-Use-Gueter (EG-Dual-Use-VO 2021 821): Produktrechtliche Pflichten und exportkontrollrechtliche Genehmigungspflichten, Anhang I, Catch-All, militaerische Endverwendung. Schnittstelle zu Aussenwirtschaftsgesetz AWG und AWV. Pruefraste... |
| `eu-produktsicherheitsverordnung-gpsr` | EU-Produktsicherheitsverordnung GPSR (VO (EU) 2023/988) in der Praxis: Geltung seit 13.12.2024, Pflichten fuer Hersteller, Importeure, Haendler und Online-Marktplaetze, Rueckverfolgbarkeit, Unfallmeldungen und Safety Business Gateway. |
| `feature-risikobewertung` | 'Tiefgehende Risikobewertung für ein einzelnes Feature oder einen Produktbereich wenn der Launch-Review etwas gefunden hat das mehr als eine Tabellenzeile braucht. Strukturierte Analyse: was könnte schiefgehen, wie wahrscheinlich, wie sc... |
| `impressum-pflicht` | Prüft die Impressumspflicht für Websites, Apps und Social-Media-Profile nach §§ 5 und 6 DDG und § 18 MStV, erstellt konforme Impressumstexte und identifiziert typische Abmahnrisiken nach UWG. Lädt bei Fragen zu Anbieterkennzeichnung, Imp... |
| `ist-das-ein-problem` | 'Schnelle "Ist-das-ein-Problem?"-Antwort für die schnelle Slack-Frage – muster-erkennt gegen Ihre Kalibrierung. Verwenden wenn der Nutzer sagt "ist das ein Problem", "kurze Frage", "können wir X machen", "brauche ich rechtliche Prüfung f... |
| `ki-act-produktintegration` | KI-Verordnung-Integration in Produkte: Hochrisiko-KI nach Anhang III, Konformitaetsbewertung mit CE-Kennzeichnung, Verzahnung mit Maschinen-VO und Medizinprodukten. Pruefraster fuer Produktverantwortliche, ab welchen KI-Bausteinen welche... |
| `launch-pruefung` | Produktmanager oder Rechtsabteilung will vor dem Launch prüfen, ob das Produkt oder Feature produktrechtlich freigegeben werden kann. Vollständige rechtliche Freigabeprüfung gegen konfiguriertes Prüfrahmenwerk und Risikokalibrierung. Nor... |
| `marktueberwachung-kommunikation` | Kommunikation mit Marktueberwachungsbehoerden (zentrale Stellen der Laender, BAuA, BfArM, BNetzA): Anfrage, Probenahme, Anordnung, Rueckruf. Antwortstrategie, Schweigerecht des Herstellers, Auskunftspflichten Art. 4 MarktueberwG. Mitwirk... |
| `nachhaltigkeitsklage-werbeaussagen` | Nachhaltigkeits- und Greenwashing-Klagen nach UWG sowie Empowering-Consumers-Richtlinie EU 2024 825: konkrete Anforderungen an Klimaneutralitaets-Claims, Recyclingangaben, Kompensationsangaben. Substanziierungspflicht, Lebenszyklus-Daten... |
| `preisangaben` | Prüft die Einhaltung der Preisangabenverordnung 2022 (PAngV) bei Gesamtpreisen, Grundpreisen, Streichpreisen und Versandkosten, insbesondere die 30-Tage-Niedrigstpreisregel bei Preisreduzierungen. Lädt bei Fragen zu Preisauszeichnung, Ra... |
| `prodr-gpsr-cra-fitness-spezial` | Spezialfall GPSR und CRA Fitness-Check digitale Produkte: Sicherheitsanforderungen, Konformitaetsbewertung, Marktueberwachung. Pruefraster fuer Hersteller IoT und Software. |
| `prodr-machinery-regulation-spezial` | Spezialfall Maschinenverordnung VO 2023 / 1230 Machinery Regulation: KI in Maschinen, Wesentliche Aenderung, Modernisierung Bestandsmaschinen. Pruefraster fuer Hersteller. |
| `prodr-produkthaftung-bauleiter` | Bauleiter Produkthaftung ProdHaftG und § 823 BGB Produktsicherheit: Fehlerbegriff, Hersteller-, Quasi-Hersteller- und Importeurshaftung. Pruefraster fuer Schadensregulierung. |
| `prodr-produktrueckruf-leitfaden` | Leitfaden Produktrueckruf: Pflicht zur Sicherheitsmassnahme nach ProdSG / GPSR, Meldung an Marktueberwachungsbehoerde, Kommunikation. Pruefraster fuer Hersteller. |
| `produktbeobachtung-feldueberwachung` | Produktbeobachtung und Feldueberwachung nach § 4 ProdSG und GPSR: aktive Beobachtung des Marktes nach Inverkehrbringen, Reklamationen, Schadensmeldungen, Reparaturdaten, Social-Media-Monitoring. Ableitung von Massnahmen (Information, Mod... |
| `produktbeobachtung-software-ota` | Prüft Produktbeobachtungspflichten für Software, Firmware, OTA-Updates, digitale Dienste, Sicherheitsupdates, End-of-Support, Reparaturdaten und Feldüberwachung nach BGB, Produktsicherheit, GPSR und neuer EU-Produkthaftung. |
| `produkthaftung-digital-software-pld-2024-2853` | Prüft die neue EU-Produkthaftungsrichtlinie 2024/2853 für Software, KI-Systeme, digitale Fertigungsdateien, relevante digitale Dienste, Updates, Beweiserleichterungen und erweiterte Anspruchsgegner. |
| `produkthaftung-grundlagen` | Grundlagen Produkthaftung: ProdHaftG und deliktische Produzentenhaftung, Fehlerbegriff, Anspruchsgegner, Beweislast, Haftungshöchstgrenzen, digitale Komponenten, Software, Updates, Reparatur und neue EU-Produkthaftungsrichtlinie 2024/2853. |
| `produkthaftung-produktsicherheit-gpsr-korrektur` | Korrigiert und prüft die Produktsicherheitsroute nach Verordnung (EU) 2023/988, Marktüberwachung, Safety Business Gateway, Rückruf, Warnung, Online-Marktplätze und Verhältnis zu Produkthaftung. |
| `produkthaftung-reparatur-update-und-lifecycle` | Prüft, wie Reparaturen, Refurbishment, Updates, End-of-Support und Produktbeobachtung die Haftungslage verändern, insbesondere bei nachträglichen Softwarefehlern und Sicherheitsupdates. |
| `produktrecht-anpassen` | 'Geführte Anpassung Ihres Produktrecht-Praxisprofils – eine Sache ändern ohne das gesamte Kaltstart-Interview erneut auszuführen. Risikokalibrierung, Eskalationskontakte, Launch-Review-Framework, Werbeaussagen-Haltung oder Mandate-Worksp... |
| `produktrecht-kaltstart-interview` | Produktrecht-Plugin erstmalig einrichten und Launch-Tracker verbinden sowie Risikokalibrierung der Rechtsabteilung erfassen. Verbindet Launch-Tracker liest vergangene Reviews lernt Risikokalibrierung. Normen ProdSG MarktueberwG CE-Kennze... |
| `produktrecht-mandat-arbeitsbereich` | Verwaltung von Produktmandats-Workspaces — Anlegen, Auflisten, Wechseln, Schließen oder Deaktivieren (auf Kanzleiebene). Lädt, wenn der Nutzer ein neues Mandat anlegen, zwischen Mandaten wechseln, ein Mandat abschließen oder den mandatsb... |
| `repair-by-design-software-locks-ersatzteile` | Prüft technische und vertragliche Reparaturhindernisse wie Pairing, Seriennummern-Locks, Diagnosezugang, Firmware-Sperren, Ersatzteilbindung, IP- und Cybersecurity-Rechtfertigungen. |
| `reparaturpflicht-hersteller-nach-gewaehrleistung` | Prüft, wann Hersteller auch außerhalb der kaufrechtlichen Gewährleistung Reparatur anbieten müssen oder sollten, einschließlich Kosten, angemessener Frist, Ersatzgerät, Reparaturformular und Produktgruppen mit EU-Reparierbarkeitsanforder... |
| `right-to-repair-produktrecht-2024-1799` | Prüft das EU-Recht auf Reparatur nach Richtlinie (EU) 2024/1799, Umsetzungsstand, Hersteller-/Repairerpflichten, Reparaturformular, Reparaturplattform, Ersatzteile und Grenzen software- oder hardwareseitiger Reparaturhindernisse. |
| `rueckruf-strategie-konzern` | Konzern-Rueckrufstrategie bei sicherheitsrelevanten Maengeln: Krisenstab, Information der Behoerde Safety Business Gateway, Pressemitteilung, Haendlerinformation, Kundenidentifizierung ueber Seriennummern, Kostenuebernahme, Versicherung.... |
| `spezial-belegmatrix-mandantenkommunikation-entscheidungsvorlage` | Belegmatrix: Mandantenkommunikation und Entscheidungsvorlage im Plugin produktrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-bewertungen-behoerden-gericht-und-registerweg` | Bewertungen: Behörden-, Gerichts- oder Registerweg im Plugin produktrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-chronologie-red-team-und-qualitaetskontrolle` | Chronologie: Red-Team und Qualitätskontrolle im Plugin produktrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-impressumspflicht-dokumentenmatrix-und-lueckenliste` | Impressumspflicht: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin produktrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-launch-tatbestand-beweis-und-belege` | Launch: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin produktrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-livecheck-formular-portal-und-einreichung` | Livecheck: Formular, Portal und Einreichungslogik im Plugin produktrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-machinery-compliance-dokumentation-und-akte` | Machinery: Compliance-Dokumentation und Aktenvermerk im Plugin produktrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-pangv-risikoampel-und-gegenargumente` | Pangv: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin produktrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-prodr-zahlen-schwellen-und-berechnung` | Prodr: Zahlen, Schwellenwerte und Berechnung im Plugin produktrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-produktbeobachtung-verhandlung-vergleich-und-eskalation` | Produktbeobachtung: Verhandlung, Vergleich und Eskalation im Plugin produktrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-produktlaunch-beweislast-und-darlegungslast` | Produktlaunch: Beweislast, Darlegungslast und Substantiierung im Plugin produktrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-produktlaunch-rechtscheck` | Produktlaunch-Rechtscheck von Impressum bis Marktüberwachung: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-produktnutzung-und-claimcheck` | Produktnutzung, Werbeclaim und Sicherheitsversprechen prüfen: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-produktrecht-schriftsatz-brief-und-memo-bausteine` | Produktrecht: Schriftsatz-, Brief- und Memo-Bausteine im Plugin produktrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-produktrechtliche-erstpruefung-und-mandatsziel` | Produktrechtliche: Erstprüfung, Rollenklärung und Mandatsziel im Plugin produktrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-rechtscheck-sonderfall-und-edge-case` | Rechtscheck: Sonderfall und Edge-Case-Prüfung im Plugin produktrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-rechtsquellen-internationaler-bezug-und-schnittstellen` | Rechtsquellen: Internationaler Bezug und Schnittstellen im Plugin produktrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-regulation-mehrparteien-konflikt-und-interessen` | Regulation: Mehrparteienkonflikt und Interessenmatrix im Plugin produktrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-review-fristen-form-und-zustaendigkeit` | Review: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin produktrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-software-livequellen-und-rechtsprechungscheck` | Software: Livequellen- und Rechtsprechungscheck im Plugin produktrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `werbeaussagen-pruefung` | 'Prüfung von Werbeaussagen auf Irreführungs- und Wettbewerbsrechtsrisiken nach deutschem und europäischem Recht. Lädt, wenn der Nutzer "Werbetext prüfen", "Marketingaussagen freigeben", "UWG-Prüfung", "Health Claims", "klimaneutral prüfe... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin produktrecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin produktrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin produktrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin produktrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin produktrecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin produktrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin produktrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin produktrecht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin produktrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin produktrecht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
