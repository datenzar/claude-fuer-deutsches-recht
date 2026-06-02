---
name: grosskanzlei-corporate-ma-grosskanzlei-corporate-ma-dat-c31e2215
description: "KI-Qualitaetskontrolle und Halluzinations-Absicherung in M&A-Transaktionen: Anwendungsfall KI-generierte DD-Berichte, Klauseln oder Recherchen sollen auf Datenqualitaet, Bias und Black-Box-Risiken geprüft werden. Art. 22 DSGVO automatisierte Entscheidungen, KI-VO Risikoklassen. Prüfraster Halluzinations-Erkennung, Quellenverifikation, Bias-Analyse, Plausibilitaetsprüfung, Human-in-the-Loop-Dokumentation. Output Qualitaetsprotokoll mit Risikoampel, Prüfvermerken und Freigabebestätigung. Abgrenzung zu KI-Governance-Berufsrecht und zu Datenraum-Aufbau."
---

> Opencode-Port von `grosskanzlei-corporate-ma/skills/grosskanzlei-corporate-ma-datenqualitaet-xai-qualitaetskontrolle/SKILL.md`. Urspruenglicher Skill-Name: `grosskanzlei-corporate-ma-datenqualitaet-xai-qualitaetskontrolle`.

<!-- anthropic-depth-boost-v1 -->
# Datenqualität und XAI-Qualitätskontrolle

## Zweck
Dieser Skill führt ein Big-Law Corporate/M&A-Mandat durch den Arbeitsbereich **Datenraum, Legal Due Diligence und Information-Request-Steuerung**. Er übersetzt die vorhandenen Unterlagen in einen verwertbaren Deal-Befund, trennt gesicherte Tatsachen von Annahmen und zwingt zu einem senior-review-fähigen nächsten Schritt. Adressaten sind Partner, Counsel, Associates, Legal-Operations-Team und Inhouse-Counsel in großvolumigen Transaktionen.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Datenqualität und XAI-Qualitätskontrolle und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für ein M&A-Mandat aus Sicht von Buy-side, Sell-side oder Target."
- "Mach daraus eine Partner-/Mandantenunterlage mit Risiken, Annahmen und offenen Punkten."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-kommandocenter` oder `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-deal-intake`. Wenn der Nutzer ausdrücklich nur eine kurze Sprachfassung, Übersetzung oder E-Mail will, arbeite knapp und route nicht in einen Deep-Dive.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/grosskanzlei-corporate-ma/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Rolle der Kanzlei, Deal-Typ, Zielgesellschaft, Käufer/Verkäufer, Jurisdiktionen, Signing-/Closing-Zeitplan, Vertraulichkeitsstufe und gewünschtes Output-Format.

Benötigte Unterlagen:
- Datenraumindex, Q&A-Tracker, IRL und Disclosure-Log.
- NDA, Clean-Room-Protokoll, MAR-Insiderliste falls Public-M&A-Bezug.
- Registerauszüge, wesentliche Verträge, Litigation-Liste, IP/IT- und HR-Unterlagen.

Arbeite mit diesen Variablen: `deal_name`, `rolle`, `deal_phase`, `target`, `gegenpartei`, `jurisdiktionen`, `frist_oder_closing`, `materiality_threshold`, `owner`, `source_tag`.

## Workflow
1. **Deal-Kontext fixieren.** Bestimme Rolle, Phase, Transaktionsstruktur, Zielgesellschaft und Entscheidungsempfänger. Wenn Rolle oder Phase fehlen, frage genau eine Rückfrage; bei Fristdruck arbeite mit `[Annahme - prüfen]` weiter.
2. **Quellen inventarisieren.** Liste alle Dokumente mit Datum, Version, Quelle, Datenraum-ID und Vertraulichkeitsstufe. Markiere Uploads als `[Mandant]`, öffentliche Register als `[Register]`, Gerichts-/Behördenquellen als `[Primärquelle]` und Modellwissen als `[Modellwissen - prüfen]`.
3. **Rechts- und Workstream-Schnittstellen trennen.** Ordne Punkte in Corporate, Commercial, Tax, Regulatory, Finance, IP/IT, HR, Litigation, Real Estate, ESG und PMO. Vermische DD-Finding, Vertragsfolge und Closing-Aufgabe nicht in einem Satz.
4. **Materiality-Schwelle setzen.** Übernimm Schwellen aus LOI, SPA, DD-Scope oder Kanzlei-Playbook. Fehlt sie, schlage eine vorläufige qualitative Ampel vor: Dealbreaker, Price/Indemnity, Signing/Closing Condition, Disclosure-only, Housekeeping.
5. **Normenprüfung durchführen.** Prüfe die unten genannten Normgruppen nicht abstrakt, sondern bezogen auf den konkreten Deal-Schritt: Wirksamkeit, Zustimmung, Vollzugshindernis, Haftung, Offenlegung, Frist, Beweisquelle.
6. **Belegkette bauen.** Jede wesentliche Aussage braucht Quelle, Dokument, Fundstelle und Unsicherheitsmarker. Keine Fundstelle erfinden. Wenn ein Registerauszug, eine BGH-/EuGH-Entscheidung oder Behördenpraxis nicht abrufbar ist, steht ausdrücklich `[zu verifizieren]`.
7. **Risikomatrix erstellen.** Gib pro Punkt aus: Sachverhalt, Rechtsfrage, Norm, Subsumtion, Risikoampel, wirtschaftliche Auswirkung, empfohlene Aktion, Owner, Deadline und Folge-Skill.
8. **Draft oder Review-Gate wählen.** Wenn die Tatsachen reichen, liefere den gewünschten Output. Wenn nicht, liefere eine Information-Request-Liste oder ein Senior-Review-Memo mit genau den offenen Entscheidungen.
9. **Hand-off vorbereiten.** Überführe Findings in Datenraum-Q&A, SPA-Markup, CP-Tracker, Board Paper, Mandantenmail oder Closing Bible. Verweise auf den konkreten Anschluss-Skill unten.
10. **Abschlusskontrolle.** Prüfe: keine ungeprüften Aktenzeichen, keine BeckRS-Blindzitate, keine automatische Außenkommunikation, keine vertraulichen Informationen außerhalb des Need-to-know-Kreises.

## Pruefraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Deal-Schritt rechtlich tragfähig, praktisch vollziehbar und für die gewählte Mandatsseite taktisch sinnvoll ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird. Maßgeblich sind Mandatsvereinbarung, Konfliktprüfung und Vertraulichkeitsrahmen. Ist die Rolle unklar, darf kein parteilicher Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Wirksamkeit und Corporate Authority.** Bei Anteils- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Form und Registerlage zu prüfen. Relevanter Kern:
- BGB §§ 311 Abs. 2, 241 Abs. 2 und 280 für vorvertragliche Aufklärungspflichten.
- GeschGehG §§ 2, 4, 6 und 17 für Geschäftsgeheimnisse im Datenraum.
- GWB §§ 35 ff. und § 41 sowie Art. 7 FKVO für Gun-Jumping und Clean-Room-Fragen.
- MAR Art. 7, 17 und 18 für Insiderinformationen, Ad-hoc-Prüfung und Insiderlisten.

**3. Organpflichten und Business Judgment.** Bei Geschäftsleitungs- oder Aufsichtsratsentscheidungen ist zu fragen, ob die Entscheidung auf angemessener Informationsgrundlage, ohne sachfremde Interessen und zum Wohl der Gesellschaft vorbereitet ist. Für die Pflicht zur eigenverantwortlichen Prüfung von Ansprüchen und Organverantwortung ist BGH, 21.04.1997 - II ZR 175/95, ARAG/Garmenbeck, als Leitentscheidung zu markieren: https://dejure.org/1997,161 `[dejure.org]`.

**4. Register- und Gesellschafterlistenlogik.** Bei GmbH-Anteilen, Einziehung, Vollmachtskette oder Closing-Fähigkeit ist § 16 GmbHG gesondert zu prüfen. Zur Legitimationswirkung der Gesellschafterliste: BGH, 20.11.2018 - II ZR 12/17, abrufbar über BGH-Datenbank und dejure: https://dejure.org/2018,47817 `[BGH-Datenbank/dejure.org]`.

**5. Regulatory und Vollzugshindernisse.** Wenn Fusionskontrolle, AWV/FDI, MAR, GwG, Sanktionen oder branchenspezifische Genehmigungen berührt sind, lautet der Zwischensatz nicht nur „Risiko“, sondern: Anmeldung erforderlich? Vollzugsverbot? Closing Condition? Long-Stop-Date gefährdet? Bußgeld- oder Nichtigkeitsfolge?

**6. Subsumtion.** Subsumtion erfolgt dokumentennah: Jede rechtliche Annahme bekommt eine Tatsachenquelle. Beispiel: `§ 15 GmbHG notarielle Form erfüllt?` nur bejahen, wenn Entwurf/Urkunde/Notarbestätigung vorliegt. `§ 41 GWB Vollzug gesperrt?` nur bejahen, wenn Zusammenschluss, Schwellen und fehlende Freigabe geprüft sind.

**Zwischenergebnis:** Das Ergebnis ist als Ampel zu formulieren: grün mit Beleg, gelb mit offener Information, rot mit Handlungssperre. Rot bedeutet in M&A regelmäßig: nicht signen, nicht closen, nicht offenlegen oder nicht extern versenden, bevor Partner/Spezialist freigegeben hat.

## Output-Module
- **Deal-Vermerk:** Executive Summary, Sachverhalt, Normen, Subsumtion, Risikoampel, Empfehlung.
- **Issue List:** Tabelle mit Finding, Quelle, Risiko, Vertragsfolge, Preis-/Indemnity-Folge, Owner, Deadline.
- **Information Request:** präzise Fragen an Mandant, Gegenseite oder Datenraum-Team, jeweils mit Grund und Priorität.
- **Drafting-Anschluss:** Klauselvorschlag, Markup-Kommentar, Disclosure-Punkt, CP-Formulierung oder Board-Paper-Abschnitt.
- **Matter-Update:** kurzer Eintrag für `history.md` und ggf. Frist-/Owner-Eintrag für `fristen.yaml`.

## Quellen und Zitierregel
Nutze nur frei prüfbare Quellen oder vom Nutzer bereitgestellte/lizenzierte Quellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und Link auf `dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu` oder `eur-lex.europa.eu`. Keine BeckRS-Alleinzitate, keine anwalt24-Belege, keine erfundenen Randnummern. Quellen-Tags: `[Mandant]`, `[Register]`, `[BGH-Datenbank]`, `[dejure.org]`, `[EUR-Lex]`, `[Web-Recherche - prüfen]`, `[Modellwissen - prüfen]`.

## Hand-Off zu anderen Skills
Nach diesem Skill weiter mit:
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-datenraum-aufbau` - wenn Dokumente, Datenraumlücken oder Clean-Room-Fragen der nächste Engpass sind.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-datenraum-gap-clean-room` - wenn Dokumente, Datenraumlücken oder Clean-Room-Fragen der nächste Engpass sind.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-due-diligence-legal` - wenn aus Unterlagen ein Legal-DD-Befund oder DD-Report gebaut werden soll.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-qa-information-requests` - wenn Findings in Information Requests und Seller-Q&A übersetzt werden müssen.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-due-diligence-reporting` - wenn aus Unterlagen ein Legal-DD-Befund oder DD-Report gebaut werden soll.

## Was dieser Skill nicht macht
- Er ersetzt keine Partnerentscheidung über Deal-Taktik, Signing-Freigabe oder Closing-Freigabe.
- Er führt keine automatische Außenkommunikation an Gegenseite, Behörde, Notar, Datenraumteilnehmer oder Mandant aus.
- Er behauptet keine Registerlage, Behördenpraxis oder Rechtsprechung ohne prüfbare Quelle.
- Er vermischt nicht DD-Finding, Vertragsrisiko und wirtschaftliche Bewertung; diese Ebenen bleiben getrennt.
- Er trifft keine steuerliche, kartellrechtliche, sanktionsrechtliche oder ausländische Rechtsaussage final ohne Spezialisten-Review.
- Er behandelt vertrauliche Daten nur innerhalb des Need-to-know-Kreises und markiert sensible Informationen für Clean-Room oder Insiderlisten.

## Berufsrechtliche Hinweise
Vor Mandatsarbeit sind Interessenkonflikte nach § 43a BRAO und § 3 BORA, Verschwiegenheit nach § 43a Abs. 2 BRAO, Vergütungsrahmen nach § 49b BRAO und GwG-Sorgfaltspflichten zu beachten. Bei personenbezogenen Daten gelten DSGVO Art. 5, 6, 25 und 32. Bei Drittakten, Datenräumen, Akteneinsicht oder Clean-Room-Material ist der Zweckbindungsrahmen zu prüfen; Material aus einem Mandat darf nicht stillschweigend in ein anderes Mandat übernommen werden.

## Bisheriger Skill-Kern, integriert und weiterzuverwenden

# Datenqualität und XAI-Qualitätskontrolle

## Zweck

Sichert KI-gestützte M&A-Arbeit gegen Halluzination, Bias, Black-Box-Probleme und schlechte Datenqualität ab.

## Arbeitsmodus

- Datenqualität, Quellenstatus, Stichprobe und Plausibilisierung festhalten.
- Explainability-Anforderungen für jedes Ergebnis markieren.
- Human-in-the-loop und Senior Review dokumentieren.
- Fehler, Annahmen und nicht geprüfte Bereiche offenlegen.

## Rote Schwellen

- Keine Belegkette.
- Nicht erklärbares Ergebnis bei hohem Risiko.
- Bias oder Datenlücke wird nicht benannt.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/data-quality-gate.md
- assets/templates/xai-quality-control-log.md

## Triage

1. Welche Datenquellen wurden fuer die M&A-Analyse genutzt — Datenraum, Handelsregister, Pressemitteilungen, Expert Calls?
2. Welche Ergebnisse basieren auf automatisierter Verarbeitung — DD-Analyse, Vertragsmarkup, Risikobewertung?
3. Gibt es Bereiche, die nicht geprueft wurden — fehlende Daten, eingeschraenkter Datenraum, nicht zugaengliche Unterlagen?
4. Welche Ergebnisse haben hohes Risiko und erfordern Senior Review?

## Zentrale Rechtsgrundlagen

- Art. 22 DSGVO — automatisierte Einzelentscheidungen: bei rechtlich bedeutsamen Entscheidungen darf keine vollautomatische Entscheidung ohne menschliche Ueberpruefung getroffen werden
- Art. 13, 14 EU-KI-Verordnung (in Kraft ab 2024/2025) — KI-Systeme mit hohem Risiko muessen transparent, pruefbar und erklaerbar sein; Dokumentationspflichten
- §§ 675, 280 BGB — Beraterhaftung: Ergebnisse, die auf unzuverlaessigen Daten basieren, koennen Schadensersatz ausloesen; Anwalt muss Datenbasis offenlegen
- § 43a BRAO — Unabhaengigkeit: Anwalt darf sich nicht auf Ergebnisse verlassen, die er nicht nachpruefen kann

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow

1. **Datenquellen dokumentieren:** alle verwendeten Quellen mit Datum, Version, Zugaenglichkeit; Luecken explizit benennen
2. **Stichprobe und Plausibilisierung:** 10-20 % der Ergebnisse manuell querprufen
3. **Explainability-Flag setzen:** je Ergebnis mit hohem Risiko: Human muss Ergebnis nachvollziehen koennen
4. **Halluzinations-Check:** Leitsatz-Zitate, Normen, Aktenzeichen — alle Faktenangaben verifizieren
5. **Human-in-the-loop-Protokoll:** wer hat geprueft, wann, Ergebnis der Pruefung

## Rote Schwellen

- Keine Belegkette fuer wesentliche Ergebnisse: Haftungsrisiko
- Nicht erklaerbares Ergebnis bei hohem Risiko: sofortige Senior Review; kein Versand
- Bias oder Datenlücke nicht benannt: moeglicherweise fehlerhafte Mandatsberatung
