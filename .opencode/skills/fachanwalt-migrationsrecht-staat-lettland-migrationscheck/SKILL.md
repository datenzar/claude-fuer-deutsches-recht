---
name: fachanwalt-migrationsrecht-staat-lettland-migrationscheck
description: "Staaten- und Gebietscheck Lettland: migrationsrechtlicher Workflow für Herkunfts-, Transit-, Dokumenten-, Visum-, Schutz-, Passbeschaffungs-, Rückführungs- und Aufenthaltstitelfragen mit Live-Quellencheck und optionaler spanischer Erklärung."
---

> Opencode-Port von `fachanwalt-migrationsrecht/skills/staat-lettland-migrationscheck/SKILL.md`. Urspruenglicher Skill-Name: `staat-lettland-migrationscheck`.

# Staaten-/Gebietscheck: Lettland

## Aufgabe
Dieser Skill prüft migrationsrechtliche Fälle mit Bezug zu **Lettland**. Er ist kein Länderlexikon, sondern ein Arbeitsworkflow für Herkunfts-, Transit-, Dokumenten-, Visum-, Schutz- und Rückführungsfragen.

## Kaltstart
1. Welche Beziehung besteht zu Lettland: Staatsangehörigkeit, Geburt, Wohnsitz, Transit, Fluchtgrund, Urkunde, Pass, Familie, Arbeitgeber oder Zielstaat?
2. Wo befindet sich die Person jetzt und mit welchem Aufenthaltsstatus?
3. Geht es um Aufenthaltstitel, Blaue Karte EU, Visum, Familiennachzug, Asyl, Dublin/GEAS, Einbürgerung, Passbeschaffung, Abschiebungsabwehr oder Rückkehr?
4. Welche Dokumente aus Lettland liegen vor und wie wurden sie beschafft/übersetzt/legalisiert?
5. Welche aktuelle Länder-, Behörden- oder Sicherheitsquelle trägt das Ergebnis?

## Prüfraster
1. **Identität und Dokumente:** Pass, ID, Geburts-/Heiratsurkunden, Register, Übersetzung, Legalisation/Apostille, Echtheit, Zumutbarkeit der Beschaffung.
2. **Aufenthaltsrecht Deutschland:** Passpflicht, Visumverfahren, Titelvoraussetzungen, Lebensunterhalt, Beschäftigung, Familie, Fiktionswirkung.
3. **Schutzrecht:** Individuelle Verfolgung, Gruppen-/Regionenrisiko, innerstaatliche Fluchtalternative, Art. 3 EMRK, Krankheit, Vulnerabilität.
4. **EU/Europarat:** Dublin/GEAS, sichere Herkunft/Drittstaaten, EMRK/HUDOC, EUAA/UNHCR-Quellen; nur anwenden, wenn aktuell und einschlägig.
5. **Rückführung/Pass:** Botschaftspraxis, Heimreisedokument, Mitwirkung, Zumutbarkeit, Vollstreckungshindernisse.
6. **Strategie:** Antrag, Nachreichung, Eilantrag, Länderquellenvermerk, Mandantenhinweis, spanische/einfache Erklärung bei Bedarf.

## Output
- Kurzlage: `Lettland`, Status, Ziel, Frist, Hauptrisiko.
- Quellenvermerk mit Datum des Live-Checks.
- Dokumenten- und Beweisliste.
- Textbaustein für Behörde/Gericht/Mandant.
- Anschluss-Skills: Aufenthaltsstatus, Asyl, Dublin/GEAS, Familiennachzug, Einbürgerung, Passbeschaffung oder Abschiebungsabwehr.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.
