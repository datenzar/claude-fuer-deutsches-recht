---
name: anlagen-zu-schriftsaetzen-emails-chats-screenshots-als-anlagen
description: "Macht aus EML/MSG, Chatverläufen und Screenshots gerichtstaugliche Anlagen mit Headern, Kontext, Exportlogik, Vollständigkeitswarnung und Beweiszweck."
---

> Opencode-Port von `anlagen-zu-schriftsaetzen/skills/emails-chats-screenshots-als-anlagen/SKILL.md`. Urspruenglicher Skill-Name: `emails-chats-screenshots-als-anlagen`.

# E-Mails, Chats und Screenshots als Anlagen

## Zweck

Dieser Skill behandelt digitale Kommunikation nicht als hübschen Screenshot, sondern als Beweisproblem: Was ist der vollständige Verlauf, wer ist Absender, woher stammt der Export, fehlen Anhänge, und wie wird Kontext sichtbar?

## Mindestinput

- EML/MSG, Screenshot, Chat-Export oder Beschreibung.
- Beteiligte und Zeitraum.
- Beweiszweck.

## Arbeitsablauf

1. Prüfe, ob Originaldatei, Export und Screenshot auseinanderfallen.
2. Sichere Header-/Metadatenhinweise.
3. Ordne Anhänge der Nachricht zu.
4. Entscheide Einzelanlage oder Kommunikationskonvolut.
5. Formuliere Schriftsatzanker ohne Überbehauptung.

## Ausgabe

- Kommunikations-Anlagenkonzept.
- Header-/Kontextvermerk.
- Konvolutdeckblatt für Chat/E-Mail-Kette.

## Typische Fehler, die du aktiv suchst

- Unklare Anlagenfunktion: Die Datei existiert, aber niemand sagt, welche Tatsache sie beweist.
- Nummerierung folgt dem Ordner, nicht dem Schriftsatz.
- Der Schriftsatz versteckt entscheidenden Vortrag in der Anlage.
- Dateiname, Stempel oder Anlagenverzeichnis widersprechen einander.

## Anschluss-Skills

- `anlagen-zu-schriftsaetzen` für den Hauptworkflow.
- `anlagen-qualitygate-finalcheck` vor Versand.
- `schriftsatz-anlagen-mapping` für Belegmatrix und Lückenliste.

## Quellen- und Vorsichtsregel

Bei tragenden Aussagen zu Form, elektronischer Einreichung oder prozessualer Verwertbarkeit aktuelle amtliche Quellen prüfen: ZPO, BRAO, ERVV, ERVB und gerichtliche Hinweise. Keine BeckRS-/juris-/Literatur-Blindzitate. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle nennen.
