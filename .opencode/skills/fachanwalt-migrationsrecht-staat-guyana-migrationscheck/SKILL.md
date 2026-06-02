---
name: fachanwalt-migrationsrecht-staat-guyana-migrationscheck
description: "Staaten- und Gebietscheck Guyana: migrationsrechtlicher Workflow für Herkunfts-, Transit-, Dokumenten-, Visum-, Schutz-, Passbeschaffungs-, Rückführungs- und Aufenthaltstitelfragen mit Live-Quellencheck und optionaler spanischer Erklärung."
---

> Opencode-Port von `fachanwalt-migrationsrecht/skills/staat-guyana-migrationscheck/SKILL.md`. Urspruenglicher Skill-Name: `staat-guyana-migrationscheck`.

# Staaten-/Gebietscheck: Guyana

## Aufgabe
Dieser Skill prüft migrationsrechtliche Fälle mit Bezug zu **Guyana**. Er ist kein Länderlexikon, sondern ein Arbeitsworkflow für Herkunfts-, Transit-, Dokumenten-, Visum-, Schutz- und Rückführungsfragen.

## Kaltstart
1. Welche Beziehung besteht zu Guyana: Staatsangehörigkeit, Geburt, Wohnsitz, Transit, Fluchtgrund, Urkunde, Pass, Familie, Arbeitgeber oder Zielstaat?
2. Wo befindet sich die Person jetzt und mit welchem Aufenthaltsstatus?
3. Geht es um Aufenthaltstitel, Blaue Karte EU, Visum, Familiennachzug, Asyl, Dublin/GEAS, Einbürgerung, Passbeschaffung, Abschiebungsabwehr oder Rückkehr?
4. Welche Dokumente aus Guyana liegen vor und wie wurden sie beschafft/übersetzt/legalisiert?
5. Welche aktuelle Länder-, Behörden- oder Sicherheitsquelle trägt das Ergebnis?

## Prüfraster
1. **Identität und Dokumente:** Pass, ID, Geburts-/Heiratsurkunden, Register, Übersetzung, Legalisation/Apostille, Echtheit, Zumutbarkeit der Beschaffung.
2. **Aufenthaltsrecht Deutschland:** Passpflicht, Visumverfahren, Titelvoraussetzungen, Lebensunterhalt, Beschäftigung, Familie, Fiktionswirkung.
3. **Schutzrecht:** Individuelle Verfolgung, Gruppen-/Regionenrisiko, innerstaatliche Fluchtalternative, Art. 3 EMRK, Krankheit, Vulnerabilität.
4. **EU/Europarat:** Dublin/GEAS, sichere Herkunft/Drittstaaten, EMRK/HUDOC, EUAA/UNHCR-Quellen; nur anwenden, wenn aktuell und einschlägig.
5. **Rückführung/Pass:** Botschaftspraxis, Heimreisedokument, Mitwirkung, Zumutbarkeit, Vollstreckungshindernisse.
6. **Strategie:** Antrag, Nachreichung, Eilantrag, Länderquellenvermerk, Mandantenhinweis, spanische/einfache Erklärung bei Bedarf.

## Output
- Kurzlage: `Guyana`, Status, Ziel, Frist, Hauptrisiko.
- Quellenvermerk mit Datum des Live-Checks.
- Dokumenten- und Beweisliste.
- Textbaustein für Behörde/Gericht/Mandant.
- Anschluss-Skills: Aufenthaltsstatus, Asyl, Dublin/GEAS, Familiennachzug, Einbürgerung, Passbeschaffung oder Abschiebungsabwehr.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.
