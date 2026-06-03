---
name: strafprozess-abschluss-urteil-bewaehrung-vollstreckung
description: "Abschlussworkflow nach Urteil, Einstellung oder Verständigung: sichert Rechtsmittelfristen, Bewährungsauflagen, Zahlungspflichten, Führungszeugnisfolgen, Vollstreckung, Mandantenbrief, Aktenabschluss und Wiedervorlagen."
---

# Abschluss: Urteil, Bewährung und Vollstreckung

## Zweck

Nach dem Urteil ist die Verteidigung nicht fertig. Dieser Skill sichert die Übergabe in Rechtsmittel, Bewährung, Vollstreckung oder Aktenabschluss.

## Sofort nach Entscheidung

- Entscheidungstenor notieren.
- Rechtsmittelbelehrung prüfen.
- Frist eintragen.
- Mandantenwillen abfragen.
- Nebenfolgen prüfen: Fahrverbot, Entziehung, Einziehung, Bewährung, Auflagen, Adhäsion, Kosten.
- Zahlungs- und Meldefristen notieren.

## Abschlussblatt

```text
Abschlussblatt

Entscheidung:
Datum:
Rechtskraft offen:
Rechtsmittel:
Frist:
Bewährung/Auflagen:
Einziehung/Kosten:
Führungszeugnis/BZR:
Vollstreckung:
Mandanteninfo:
Wiedervorlagen:
```

## Bewährung

Prüfe:

- Auflagen verständlich erklärt?
- Zahlungsfähigkeit realistisch?
- Bewährungshelferkontakt?
- Therapie-/Beratungsnachweise?
- Widerrufsrisiko?
- Folgekommunikation mit Mandant?

## Aktenabschluss

- Mandantenbrief mit Ergebnis und Pflichten.
- Fristenbuch prüfen.
- Kosten-/Honorarabschluss.
- Dokumente zurückgeben oder archivieren.
- Datenschutz und Löschung/Archivfristen beachten.

## Output

- `Mandantenbrief Abschluss`
- `Bewährungsplan`
- `Vollstreckungs-Wiedervorlagen`
- `Rechtsmittelentscheidung`
- `Aktenabschlussvermerk`
