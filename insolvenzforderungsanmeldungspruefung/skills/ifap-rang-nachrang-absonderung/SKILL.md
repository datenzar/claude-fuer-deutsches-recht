---
name: ifap-rang-nachrang-absonderung
description: "Prüft Rang, Nachrang, Sicherungsrechte, Absonderung, Aussonderung und Ausfallforderungen ohne Gläubigerangaben ungeprüft zu übernehmen."
---

# Rang, Nachrang und Sicherungsrechte

## Aufgabe

Prüft die insolvenzrechtliche Einordnung der Forderung und alle behaupteten Sonderrechte.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Nachrang ist angemeldet
- Sicherheit wird behauptet
- Ausfallforderung unklar
- Eigentumsvorbehalt steht im Raum

## Workflow

1. Regelrang nach § 38 InsO, Nachrang nach § 39 InsO und sonstige Rangangaben trennen.
2. Prüfen, ob Nachrang überhaupt zur Anmeldung aufgefordert wurde.
3. Absonderungsrechte erfassen: Sicherungsübereignung, Pfand, Grundpfandrecht, Forderungsabtretung, Eigentumsvorbehalt.
4. Ausfallforderung und Verwertungslage abfragen, wenn Sicherheit vorhanden ist.
5. Aussonderung von Forderungsanmeldung trennen, wenn Eigentum oder Herausgabe statt Quote gemeint ist.
6. Tabellenrang und Sonderrechtsvermerk getrennt formulieren.

## Ausgabe

- Rangmatrix
- Sicherheitenvermerk
- Ausfallstatus
- Rangkorrekturvorschlag

## Qualitätsgates

- Sicherungsrechte werden nicht allein aus Selbstauskunft festgestellt.
- Nachrang wird ausdrücklich bezeichnet.
- Aussonderung führt nicht automatisch zu einer Tabellenforderung.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.
