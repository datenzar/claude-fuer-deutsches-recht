---
name: ifap-formalpruefung-174
description: "Prüft die Mindestangaben der Forderungsanmeldung nach § 174 InsO einschließlich Grund, Betrag, Urkunden, Nachrang und elektronischer Einreichung."
---

# Formalprüfung nach § 174 InsO

## Aufgabe

Prüft, ob eine Forderungsanmeldung formal tabellenfähig ist oder gezielte Ergänzung braucht.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Anmeldung soll in die Tabelle
- Grund oder Betrag fehlen
- vbuH oder Nachrang ist angekreuzt

## Workflow

1. Prüfen, ob eine Anmeldung beim Verwalter vorliegt und welcher Gläubiger sie trägt.
2. Grund und Betrag isoliert erfassen, nicht aus Anlagen erraten, wenn die Anmeldung selbst leer bleibt.
3. Urkundenstatus prüfen: beigefügt, elektronisch, nachzureichen, unlesbar, nicht passend.
4. Nachranghinweis und Rangstelle prüfen, wenn nachrangige Forderung angemeldet ist.
5. vbuH, Unterhalt oder Steuerstraftat nur mit konkreten Tatsachen erfassen.
6. Mangelkategorie vergeben: heilbar, substanziell unklar, offensichtlich falscher Weg, Nachforderung erforderlich.

## Ausgabe

- § 174-Checkliste
- Mängelliste
- Nachforderungsvorschlag
- Status für Tabellenimport

## Qualitätsgates

- Grund und Betrag sind Pflichtachsen.
- Urkundenmangel wird nicht mit materiellem Bestreiten verwechselt.
- Elektronische Rechnung kann Urkunde sein, muss aber lesbar zuordenbar bleiben.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.
