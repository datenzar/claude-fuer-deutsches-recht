---
name: liquiditaet-12-monate
description: Erstellt die rollierende Zwoelf-Monats-Liquiditaetsvorschau auf Basis der plausibilisierten Annahmen. Pro Woche oder pro Monat Aufstellung der Einzahlungen und Auszahlungen Anfangsbestand Endbestand Linieverbleib. Pruefung ob in jedem Zeitabschnitt mehr als die geschuldeten Verbindlichkeiten zur Verfuegung stehen. Bezuege zur Zahlungsfaehigkeit nach § 17 InsO (Zehn-Prozent-Schwelle Drei-Wochen-Frist nach BGH IX ZR 123/04). Falls Plugin liquiditaetsplanung installiert — dort die detaillierte Wochenplanung; dieses Plugin uebernimmt die Monatsaggregate.
---

# Zwoelf-Monats-Liquiditaet

## Zweck

Die Fortbestehensprognose erfordert dass das Unternehmen ueber den **Prognosehorizont von zwoelf Monaten** zahlungsfaehig bleibt. Das bedeutet: in jedem Monat muessen die liquiden Mittel plus Kreditlinien plus Zufluesse die faelligen Verbindlichkeiten decken.

## Drei Schichten

### Schicht 1 — Monatliche Liquiditaetsplanung

Aus den Annahmen aus `annahmen-sammeln-fortfuehrung` plus Plausibilisierung:

```yaml
liquiditaet:
  startbestand-2026-05-20: 18000
  kreditlinie-verfuegbar: 12000  # Linie 150000 minus 138000 ausgenutzt
  
  monatsdaten:
    - monat: 2026-06
      einzahlungen:
        forderungen-laul: 185000
        gesellschafter-darlehen: 0
        sonstige: 0
        summe: 185000
      auszahlungen:
        lieferanten: 130000
        loehne-gehaelter: 78000
        sozialabgaben: 24000
        steuern: 14000
        bank-tilgung: 8000
        miete: 6000
        energie: 9000
        sonstige: 5000
        summe: 274000
      saldo-monat: -89000
      monatsendbestand: -71000  # negativ — Linie reicht nicht
      bemerkung: Liquiditaetsluecke
```

### Schicht 2 — Detaillierte Wochenplanung

Bei kritischen Phasen (Monaten mit knapp positivem Saldo oder negativem Endbestand) muss die Wochenplanung herangezogen werden:

- Drei-Wochen-Schwelle § 17 InsO BGHZ 163, 134 — bei Luecke groesser als zehn Prozent ueber laenger als drei Wochen liegt Zahlungsunfaehigkeit vor.
- Plugin `liquiditaetsplanung` enthaelt die wochenbasierten Vorlagen.

### Schicht 3 — Sensitivitaetsszenarien

Drei Szenarien aus `annahmen-belastbarkeit-plausibilisieren` werden in der Liquiditaet durchgerechnet:

- **Basis-Szenario** — Plan
- **Negativ-Szenario** — ambitionierte Annahmen reduziert
- **Stress-Szenario** — Top-Kunde weg

Bei jedem Szenario die monatlichen Salden ueber die zwoelf Monate.

## Pruefkriterien

### Pro Monat

- **Monatsendbestand mindestens null** (besser kein voll ausgenutzter Kontokorrent).
- **Keine roten Monate** im Plan.

### Ueber den Horizont

- **Steigender Trend** oder Stabilisierung der Liquiditaet.
- **Wesentliche Risikoposten** identifiziert.
- **Massnahmenoptionen** bei Risiko-Eintritt vorhanden.

### Bei Sensitivitaet

- **Negativ-Szenario** Liquiditaet auch positiv? Wenn nein: dann ist die Prognose **nur** im Basis-Szenario tragfaehig. Das ist **nicht** ausreichend fuer eine positive Fortbestehensprognose.
- **Stress-Szenario** soll mit den Massnahmen abgefedert werden koennen — gegebenenfalls Patronatserklaerungen Comfortletter Gesellschafterdarlehen.

## Konsolidierung mit dem Plugin `liquiditaetsplanung`

Wenn das Plugin `liquiditaetsplanung` installiert ist:

- Die detaillierte Wochenplanung erfolgt dort (Skill `liquiditaetsvorschau-3-6-12-monate`).
- Hier importieren wir die Monatsaggregate.
- Die Drei-Wochen-Schwelle § 17 InsO wird in `liquiditaetsplanung` separat geprueft.

Wenn nicht installiert: einfache Tabelle hier; bei Bedarf nachinstallieren.

## Beispielergebnis

```
Liquiditaetspruefung Zwoelf Monate
Basis-Szenario: positiv (Endbestand jeweils ueber null)
Negativ-Szenario: kritisch (Monat 11 unter null)
Stress-Szenario: negativ ab Monat 4

Bewertung: ohne Sanierungsmassnahmen ist die Liquiditaet im Stress-Szenario
ueberschritten. Mit Massnahmen aus Skill sanierungsbausteine-vorschlagen
ist die Liquiditaet ueber den Horizont zu sichern.
```

## 90-Prozent-Deckung ist der operative Massstab

Die „ueberwiegende Wahrscheinlichkeit" nach § 19 Abs. 2 InsO ist nicht abstrakt zu pruefen, sondern operativ ueber den Liquiditaetsplan. Das Unternehmen ist „ueberwiegend wahrscheinlich fortfuehrbar" wenn ueber den gesamten Zwoelf-Monats-Horizont mit hoher Wahrscheinlichkeit **keine Zahlungsunfaehigkeit nach § 17 InsO eintritt**. Damit gilt durchgehend der BGH-Massstab aus BGHZ 163, 134 (BGH IX ZR 123/04):

- **In jedem Zeitabschnitt** muss die Deckung der faelligen Verbindlichkeiten mindestens **90 Prozent** betragen (Liquiditaetsluecke unter zehn Prozent).
- **Eine voruebergehende Luecke** ueber zehn Prozent darf hoechstens **drei Wochen** andauern. Wer laenger als drei Wochen unter 90 Prozent Deckung liegt ist nach BGH zahlungsunfaehig — und das ist gerade nicht „fortfuehrbar".
- **Ueber den vollen Zwoelf-Monats-Horizont** muss diese Schwelle eingehalten werden — andernfalls ist die Fortbestehensprognose **negativ**.

Die „mehr als 50 Prozent Wahrscheinlichkeit" der Prognose bezieht sich darauf dass dieses Szenario (Einhaltung der BGH-Schwelle ueber zwoelf Monate) eintritt — also nicht ein abstrakter Erfolgswert sondern die methodische Wahrscheinlichkeit dass das Unternehmen die 90-Prozent-Deckung bzw. die Drei-Wochen-Karenz **ueber den gesamten Horizont durchhaelt**.

**Konsequenz fuer die Liquiditaetsprognose:**

- Pro Monat (besser pro Woche in kritischen Phasen): Liquiditaetsbestand plus Linie / faellige Verbindlichkeiten = Deckungsquote.
- Deckungsquote in jedem Zeitabschnitt mindestens **90 Prozent**.
- Bei Unterschreitung max. drei Wochen — danach muss die Quote zwingend ueber 90 Prozent zurueckkehren.
- Im Negativ- und Stress-Szenario diese Pruefung **wiederholen**. Wenn auch das Negativ-Szenario die Schwelle einhaelt: starke Prognose. Wenn nur das Basis-Szenario einhaelt aber das Negativ-Szenario reisst: knappe Prognose — nur mit zusaetzlichen verbindlichen Massnahmen positiv.

## Ausgabe

- `liquiditaet-12-monate.xlsx` mit monatlichen Werten je Szenario.
- `liquiditaet-monatssalden.md` als menschenlesbare Uebersicht.
- Hinweis auf Pruefer-Flag bei roten Monaten.
- Empfehlung auf naechsten Skill `fortbestehensprognose-zusammenfuehren`.
