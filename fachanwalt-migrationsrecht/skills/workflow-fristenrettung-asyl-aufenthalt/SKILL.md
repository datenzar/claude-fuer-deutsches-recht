---
name: workflow-fristenrettung-asyl-aufenthalt
description: "Fristenrettung Asyl/Aufenthalt: Workflow-Skill für Migrationsrecht; priorisiert Klage, Eilantrag, Dublin, Fiktion, Ablauf Titel und Abschiebung; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output."
---

# Fristenrettung Asyl/Aufenthalt

## Aufgabe
Workflow-Skill im Plugin `fachanwalt-migrationsrecht`. Schwerpunkt: priorisiert Klage, Eilantrag, Dublin, Fiktion, Ablauf Titel und Abschiebung.

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

## Frist-Knockout-Tabelle Migration

- **1 Woche — § 36 Abs. 3 AsylG:** Klage und Eilantrag § 80 Abs. 5 VwGO bei offensichtlich unbegründetem Asylantrag (§ 30 AsylG).
- **1 Woche — § 34a Abs. 2 AsylG:** Eilantrag gegen Dublin-Bescheid (Drittstaaten-/Wiederaufnahmebescheid).
- **2 Wochen — § 74 AsylG:** Klage gegen sonstige BAMF-Ablehnungsbescheide.
- **1 Monat — § 74 VwGO:** Klage gegen Ausländerbehördenbescheide (Versagung/Widerruf Aufenthaltstitel, Ausweisung); Widerspruch wo landesrechtlich vorgesehen.
- **6 Monate Dublin-Übernahme (Art. 29 VO 604/2013):** Bei Versäumnis Zuständigkeit DE; bei Untertauchen 18 Monate.
- **Fiktionsbescheinigung (§ 81 Abs. 4 AufenthG):** Rechtzeitig vor Ablauf des Titels Verlängerungsantrag stellen — Fiktion erlischt sonst.
- **Wiedereinsetzung (§ 60 VwGO; § 32 VwVfG):** 2 Wochen ab Wegfall des Hindernisses, max. 1 Jahr.
- **Praxis-Tipp:** Bei Postanstaltszustellung gilt der Tag der Postaushändigung, nicht der Bescheiddatum — Briefumschlag mit Eingangsstempel aufbewahren. Bei Bevollmächtigtem: Zustellung an Anwalt mit Vollmacht maßgeblich.

## Spanisch bei Bedarf
Erkläre zusätzlich auf Spanisch: `Situación`, `Plazo`, `Riesgo`, `Documentos necesarios`, `Próximo paso`. Normen bleiben deutsch mit kurzer Erklärung.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.
