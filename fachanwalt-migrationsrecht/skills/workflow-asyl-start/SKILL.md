---
name: workflow-asyl-start
description: "Asyl-Start: Workflow-Skill für Migrationsrecht; klärt Schutzgrund, Verfolgungsakteur, Beweise, Anhörung, Dublin und Fristen; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output."
---

# Asyl-Start

## Aufgabe
Workflow-Skill im Plugin `fachanwalt-migrationsrecht`. Schwerpunkt: klärt Schutzgrund, Verfolgungsakteur, Beweise, Anhörung, Dublin und Fristen.

## Kaltstart
Wenn Unterlagen vorhanden sind, zuerst auswerten. Frage nur, was die nächste Weiche verändert:
1. Rolle, Ziel und gewünschte Sprache der Erklärung.
2. Staatsangehörigkeit, Herkunfts-/Transitstaaten, aktueller Aufenthaltsort und Status.
3. Frist, Zustellung, Termin, Ablaufdatum oder Abschiebungsrisiko.
4. Vorhandene Dokumente und fehlende Nachweise.
5. Gewünschter Output: einfache Erklärung, spanische Zusammenfassung, Antrag, Klage/Eilantrag, Behördenmail, Arbeitgebermemo oder Dokumentenliste.

## Arbeitsworkflow
1. **Statusmatrix:** Person, Staat/Gebiet, Dokumente, Aufenthaltsort, aktueller Status, Zielstatus.
2. **Frist sichern:** Klage/Eilantrag, Dublin/GEAS, Fiktionswirkung, Visumtermin, Ausreisefrist, Abschiebung.
3. **Rechtsgrundlage:** AufenthG, AsylG, StAG, FreizügG/EU, EU-Recht, GFK/EMRK und Verwaltungspraxis live prüfen.
4. **Staatenbezug:** Bei Herkunfts-, Transit- oder Zielstaat passenden `staat-...-migrationscheck` ergänzen.
5. **Belege:** Dokumente, Urkunden, Übersetzungen, Atteste, Arbeitsvertrag, Abschluss, Behördenpost in eine Lückenliste bringen.
6. **Output:** Risikoampel, nächste Schritte, Entwurf und Anschluss-Skills.

## Asylrechtliche Kernweichen

- **Schutzgrundpyramide:** Art. 16a GG (politische Verfolgung, eingeschränkt durch sichere Drittstaaten § 26a AsylG) — Flüchtlingsschutz § 3 AsylG (GFK) — subsidiärer Schutz § 4 AsylG (ernsthafter Schaden) — nationales Abschiebungsverbot § 60 Abs. 5 AufenthG (EMRK, insbes. Art. 3) / Abs. 7 (konkrete Gefahr).
- **Verfolgungsakteure:** Staatlich, quasi-staatlich, nicht-staatlich; letztere nur, wenn Staat keinen Schutz bieten kann/will (§ 3c, 3d AsylG).
- **Innerstaatliche Fluchtalternative (§ 3e AsylG):** Zumutbarkeit und tatsächliche Erreichbarkeit.
- **Frist-Knockout:** Klage 2 Wochen (§ 74 AsylG); bei offensichtlich unbegründet 1 Woche mit Eilantrag (§ 36 AsylG); Dublin-Bescheid 1 Woche (§ 34a Abs. 2 AsylG).
- **Dublin-III (VO 604/2013) Fristen:** Übernahme-/Wiederaufnahmeersuchen i. d. R. 2–3 Monate; Überstellung 6 Monate (Art. 29), bei Untertauchen 18 Monate.
- **GEAS-Reform 2024:** Grenzverfahren-VO, Asylverfahrens-VO, AMM-VO — Anwendungsstand kontinuierlich prüfen (BAMF, BMI, eur-lex).

## Spanisch bei Bedarf
Erkläre zusätzlich auf Spanisch: `Situación`, `Plazo`, `Riesgo`, `Documentos necesarios`, `Próximo paso`. Normen bleiben deutsch mit kurzer Erklärung.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.
