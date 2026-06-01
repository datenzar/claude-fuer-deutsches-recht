---
name: spezial-forderungsgrund-rang-und-belegpruefung
description: "Forderungsgrund, Rang und Belegprüfung zur Tabelle: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output."
---

# Forderungsgrund, Rang und Belegprüfung zur Tabelle

## Aufgabe
Dieser Skill ersetzt einen zu groben Spezial-Slot durch einen konkreten Fachworkflow im Plugin `insolvenzforderungsanmeldungspruefung`. Kontext des Plugins: Freistehendes Plugin für die Insolvenzforderungsanmeldungsprüfung: Intake, § 174 InsO, Belege, Grund, Betrag, Rang, vbuH, Nachforderungen, Tabellenimport, Prüfungstermin, Bestreiten, Feststellung, Tabellenauszug und Verteilung.

Er arbeitet nicht lexikalisch, sondern fallbezogen: Er trennt zuerst Rollen, Ziel, Fristen, Zuständigkeiten und Belege, prüft dann die fachlichen Weichen und liefert ein Ergebnis, mit dem weitergearbeitet werden kann.

## Kaltstart
Wenn Material vorliegt, nutze es zuerst. Frage nur nach, was für die nächste Entscheidung fehlt:

1. Wer handelt in welcher Rolle und gegen wen?
2. Welches praktische Ziel soll erreicht werden?
3. Welche Fristen, Termine, Zustellungen, Schwellenwerte oder Sanktionen stehen im Raum?
4. Welche Unterlagen, Daten, Registerauszüge, Bescheide, Verträge, Screenshots oder sonstigen Belege liegen vor?
5. Soll der Output intern, für Mandantschaft, Behörde, Gericht, Gegnerseite oder Gremium formuliert werden?

## Arbeitsworkflow
1. **Sortieren:** Sachverhalt, Dokumente und offene Punkte in eine knappe Fallmatrix bringen.
2. **Rechtsrahmen:** Einschlägige Normen, Zuständigkeiten, Verfahren, Fristen und formelle Anforderungen live prüfen, soweit Aktualität tragend ist.
3. **Materielle Weichen:** Die Kernfragen zu **Forderungsgrund, Rang und Belegprüfung zur Tabelle** mit Tatbestandsmerkmalen, Belegen, Gegenargumenten und typischen Praxisfehlern abarbeiten.
4. **Risikoampel:** Ergebnis in Grün/Gelb/Rot mit Begründung, Unsicherheiten und Beweisbedarf einordnen.
5. **Anschluss:** Passende weitere Skills desselben Plugins vorschlagen, wenn Spezialprüfung, Schriftsatz, Tabelle, Brief oder Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- Kurzbild in fünf Sätzen: Lage, Ziel, Frist, Risiko, nächster Schritt.
- Prüfmatrix mit Punkt, Norm/Quelle, Tatsachen, Beleg, Bewertung, To-do.
- Konkreter Textbaustein oder Arbeitsprodukt passend zur Lage: Memo, Mandantenbrief, Behörden-/Gerichtsschreiben, Checkliste, Tabelle oder Verhandlungsagenda.
- Keine Scheingenauigkeit: Annahmen, Lücken und Live-Check-Bedarf offen markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwenden, wenn die Nutzerin oder der Nutzer den Text selbst bereitstellt; dann nicht als frei verifizierte Quelle ausgeben.

## Forderungsgrund nach § 174 Abs. 2 InsO

- **Pflicht zur Substantiierung:** Forderungsgrund so darstellen, dass der Verwalter prüfen kann — Vertrag (Datum, Parteien, Inhalt), Lieferung/Leistung (Lieferschein, Stundenzettel), Rechnung (Datum, Nummer, Betrag), ggf. titulierter Anspruch (Urteil, Vollstreckungsbescheid).
- **Bei vorsätzlich unerlaubter Handlung** (§ 174 Abs. 2 InsO i.V.m. § 302 InsO): **gesondert** als „vbuH-Forderung" anmelden — sonst kein Schutz vor Restschuldbefreiung.
- **Bei Zinsen:** beziffern (Hauptforderung, Zinssatz, Startdatum) — bei nicht-bezifferten Zinsen separate Anmeldung erforderlich.

## Rangstufen — Differenzierung zwingend

- **Aussonderung § 47 InsO:**
  - Eigentum, Eigentumsvorbehalt (§ 449 BGB), Treuhand.
  - **Keine Anmeldung zur Tabelle**, aber Verwalter ist über das Aussonderungsrecht zu informieren — Herausgabeanspruch.
- **Absonderung §§ 49–52 InsO:**
  - Pfandrecht (§ 50 InsO), Sicherungsabtretung (§ 51 Nr. 1 InsO), Sicherungseigentum (§ 51 Nr. 1 InsO), Grundpfandrecht (§ 49 InsO).
  - Anmeldung **mit Hinweis auf Sicherung**; Ausfall (§ 52 InsO) wird **nachträglich** angemeldet, wenn Sicherheit nicht ausreicht.
- **Masseverbindlichkeit § 55 InsO:**
  - **Keine Anmeldung zur Tabelle** — direkter Anspruch gegen Verwalter aus der Masse.
  - Entstanden nach Verfahrenseröffnung durch Verwalter (§ 55 Abs. 1 Nr. 1 InsO) oder aus gegenseitigen Verträgen, deren Erfüllung der Verwalter wählt (§ 55 Abs. 1 Nr. 2 InsO).
- **Einfache Insolvenzforderung § 38 InsO:**
  - Quotale Befriedigung — Standardanmeldung.
- **Nachrangige Forderung § 39 InsO:**
  - § 39 Abs. 1 Nr. 1 Zinsen ab Eröffnung, Nr. 2 Kosten, Nr. 3 Geldstrafen/-bußen, Nr. 4 Schenkungen, Nr. 5 **Gesellschafterdarlehen** und gleichgestellte Forderungen.
  - Anmeldung **nur auf gesonderte Aufforderung** des Gerichts (§ 174 Abs. 3 InsO).

## Belegpflicht und typische Fehler

- **Beleg-Kopie reicht** — Original nicht erforderlich.
- **Buchhaltungsauszüge** zur Substantiierung des Saldos.
- **Bei Bürgschaft / Gesamtschuldnerschaft:** klar dokumentieren, sonst Doppelausschüttung droht (§ 43 InsO sperrt das).

## Risikoampel
- ROT: Anmeldung ohne Substantiierung — Verwalter wird bestreiten, Feststellungsklage erforderlich (§ 180 InsO).
- GELB: Rang unklar gesetzt (Vermischung von § 38 und § 39 InsO) — Korrekturzeit bis zum Prüfungstermin.
- GRÜN: Form, Substantiierung, Rangkennzeichnung, Beleg vollständig.
