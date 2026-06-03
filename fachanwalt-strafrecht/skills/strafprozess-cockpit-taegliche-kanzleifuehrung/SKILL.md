---
name: strafprozess-cockpit-taegliche-kanzleifuehrung
description: "Tägliches Strafprozess-Cockpit für Verteidiger: bündelt Verfahrensstand, Fristen, Haftlage, Akteneinsicht, offene Anträge, Mandantenkommunikation, Beweisfragen, Termine und nächste Schritte in einer laufend aktualisierbaren Verteidigungsübersicht."
---

# Strafprozess-Cockpit für die tägliche Verteidigung

## Zweck

Dieser Skill ist die Schaltzentrale einer Strafakte. Er soll verhindern, dass Fristen, Nachlieferungen, Haftfragen, Beweisanträge, Zusagen der Staatsanwaltschaft oder Mandantenaufträge in E-Mails und Notizen verschwinden.

## Kaltstart

Frage nur:

1. Verfahrensstand: Ermittlungsverfahren, Zwischenverfahren, Hauptverfahren, Rechtsmittel, Vollstreckung?
2. Rolle: Verteidigung, Pflichtverteidigung, Zeugenbeistand, Nebenklage, Adhäsion?
3. Gibt es Haft, Durchsuchung, Beschlagnahme, Vermögensarrest oder Führerscheinentzug?
4. Welche Frist oder welcher Termin steht als Nächstes?
5. Liegt Akteneinsicht vollständig vor?

## Cockpit-Felder

```text
Strafprozess-Cockpit

Mandant:
Az. Polizei/StA/Gericht:
Tatvorwurf:
Verfahrensstand:
Haft/Freiheit:
Pflichtverteidigung:
Nächster Termin:
Nächste Frist:
Akteneinsicht:
Offene Anträge:
Offene Beweise:
Mandantenauftrag:
Risikoampel:
Nächster Schritt:
```

## Ampellogik

- **Rot:** Haft, Rechtsmittelfrist, drohende Fristversäumung, HV morgen, unklare Zustellung, drohender Bewährungswiderruf, Durchsuchung/Arrest.
- **Gelb:** Akteneinsicht unvollständig, Nachlieferungen offen, Mandant nicht instruiert, Zeuge unklar, Beweisantrag nicht ausformuliert.
- **Grün:** Fristen notiert, Akte geordnet, Mandant instruiert, nächste Handlung terminiert.

## Täglicher Ablauf

1. Eingangspost scannen: Zustellung, Frist, Termin, Verfügung, Ladung, Beschluss.
2. Fristenbuch aktualisieren: Rechtsmittel, Wiedereinsetzung, Stellungnahmen, Haft, HV.
3. Aktenlog aktualisieren: neue Blätter, neue Sonderbände, digitale Beweise, Asservate.
4. Mandantenlog aktualisieren: letzte Information, offene Rückmeldung, Besuch/Telefonat.
5. Antragslog prüfen: gestellt, beschieden, wiederholen, zurücknehmen, ergänzen.
6. Tagesentscheidung treffen: heute handeln, diese Woche vorbereiten, beobachten.

## Output

Immer liefern:

- `Kurzstatus Akte`
- `Fristen/Wiedervorlagen`
- `Offene Entscheidungen`
- `Nächster anwaltlicher Schritt`
- `Mandanteninfo in 5 Sätzen`

## Quellenregel

StPO-Normen, Fristen und Formanforderungen live prüfen, wenn sie das Ergebnis tragen. Keine Rechtsprechung ohne Gericht, Datum, Aktenzeichen und frei prüfbare Quelle.
