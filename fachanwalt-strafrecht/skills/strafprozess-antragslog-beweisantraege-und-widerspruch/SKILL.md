---
name: strafprozess-antragslog-beweisantraege-und-widerspruch
description: "Antragslog für die Hauptverhandlung: verwaltet Beweisanträge, Beweisermittlungsanträge, Widersprüche, § 257-StPO-Erklärungen, Ablehnungsbeschlüsse, Wiederholungsbedarf, Revisionssicherung und taktische Priorität."
---

# Antragslog, Beweisanträge und Widerspruch

## Zweck

In langen Hauptverhandlungen geht der Überblick über Anträge schnell verloren. Dieser Skill führt ein präzises Register: Was wurde gestellt, warum, wie hat das Gericht entschieden, was folgt daraus?

## Antragsregister

```text
Antragslog

Nr.:
Datum/Sitzungstag:
Art: Beweisantrag / Beweisermittlungsantrag / Widerspruch / Erklärung / Befangenheit / Aussetzung
Beweistatsache:
Beweismittel:
Konnex:
Ziel:
Beschluss/Entscheidung:
Reaktion:
Revisionsrelevanz:
Wiedervorlage:
```

## Beweisantrag-Qualität

Prüfe vor Einreichung:

- konkrete Tatsachenbehauptung,
- konkretes Beweismittel,
- Konnex zwischen Beweismittel und Beweistatsache,
- Erheblichkeit für Schuld, Rechtsfolge oder Verfahrensfrage,
- keine unnötige Breite,
- Reihenfolge im Verteidigungsnarrativ.

## Widerspruch/Beanstandung

Bei Verwertungsfragen und Verfahrensfehlern:

- Zeitpunkt festhalten,
- genaue Maßnahme benennen,
- Rechtsgrund oder Verfahrensfehler knapp angeben,
- Entscheidung des Gerichts verlangen,
- Protokollierung kontrollieren.

## Revisionssicherung

Nicht alles ist später heilbar. Deshalb am Sitzungstag prüfen:

- Wurde ein Antrag förmlich gestellt?
- Wurde er beschieden?
- Ist die Begründung dokumentiert?
- Muss eine Erklärung oder Beanstandung folgen?
- Muss der Antrag nach neuer Lage wiederholt oder angepasst werden?

## Output

- `Antragslog`
- `Beweisantrag-Entwurf`
- `Widerspruchsnotiz`
- `Revisionssicherungscheck`
- `Nächster Antrag`
