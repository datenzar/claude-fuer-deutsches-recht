---
name: fortbestehensprognose-zusammenfuehren
description: Fuehrt alle Bausteine zusammen — bilanzieller Status Annahmen Plausibilisierung 12-Monats-Liquiditaet Sensitivitaetsszenarien — und bewertet ob die Fortbestehensprognose nach § 19 Abs. 2 InsO positiv ist. Massstab ueberwiegende Wahrscheinlichkeit dass das Unternehmen im Prognosezeitraum zahlungsfaehig bleibt (mehr als 50 Prozent). IDW S 11 Massstab. Schaltet bei Bedarf den Skill `sanierungsbausteine-vorschlagen` aus oder eskaliert ueber `wenn-prognose-negativ-naechste-schritte` zum Insolvenzanwalt.
---

# Fortbestehensprognose zusammenfuehren

## Massstab

§ 19 Abs. 2 InsO seit SanInsFoG 2021: "Die Fortfuehrung des Unternehmens ist nach den Umstaenden ueberwiegend wahrscheinlich" — Prognosezeitraum **zwoelf Monate**.

**Ueberwiegend wahrscheinlich** bedeutet **mehr als 50 Prozent** Wahrscheinlichkeit (klassische BGH-Rspr. zur Vorhersage; bestaetigt durch IDW S 11).

### Operativ — was bedeutet das?

Die abstrakte Wahrscheinlichkeitsformel ist methodisch durch die **Zahlungsfaehigkeitsprognose** zu fuellen. Die Fortbestehensprognose ist genau dann positiv wenn das Unternehmen ueber den Zwoelf-Monats-Horizont mit ueberwiegender Wahrscheinlichkeit **nicht in die Zahlungsunfaehigkeit nach § 17 InsO geraet**. Das bedeutet konkret:

- In jedem Zeitabschnitt der zwoelf Monate muessen **mindestens 90 Prozent** der dann faelligen Verbindlichkeiten aus den verfuegbaren Mitteln (Liquiditaetsbestand plus Kreditlinie plus rechtzeitig erzielbare Zufluesse) gedeckt werden koennen.
- **Voruebergehende Unterdeckungen** ueber zehn Prozent duerfen hoechstens **drei Wochen** dauern und muessen mit ueberwiegender Wahrscheinlichkeit binnen dieser Frist wieder geschlossen werden (BGH IX ZR 123/04, BGHZ 163, 134).

Wenn die Liquiditaetsplanung in jedem Zeitabschnitt diese Schwelle einhaelt — auch im plausibilisierten Negativ-Szenario — ist die Fortbestehensprognose **positiv**. Wenn die Schwelle in einem oder mehreren Zeitabschnitten oder ueber laengere Phasen reisst und auch durch Sanierungsbausteine nicht verbindlich geschlossen werden kann ist die Prognose **negativ**.

Die „mehr als 50 Prozent Wahrscheinlichkeit" der Prognose ist also nicht abstrakt zu vermuten sondern aus dem Liquiditaetsplan und seiner Sensitivitaet abzuleiten: ueber das Basis-Szenario hinaus muss auch das **plausible Negativ-Szenario** die Schwelle einhalten — andernfalls reicht die Wahrscheinlichkeit nicht aus.

## Pruefablauf

### Schritt 1 — Bilanzielle Ueberschuldung gegeben?

Aus Skill `bilanzieller-status-aufnehmen`:

- Bilanzielle Ueberschuldung gegeben? Wenn nein: § 19 InsO nicht erfuellt — Fortbestehensprognose **nicht erforderlich** (aber haeufig sinnvoll als Krisendokumentation).
- Wenn ja: weiter zu Schritt 2.

### Schritt 2 — Annahmen plausibilisiert?

Aus Skill `annahmen-belastbarkeit-plausibilisieren`:

- Annahmen ueberwiegend **realistisch** oder **konservativ**?
- Maximal eine oder zwei **ambitionierte** Annahmen die nicht tragend sind?
- **Nicht-belastbare** Annahmen ausgeschlossen?

Wenn die Annahmen die das Ergebnis tragen ambitioniert oder nicht-belastbar sind: Prognose **nicht positiv**.

### Schritt 3 — Liquiditaet ueber 12 Monate positiv

Aus Skill `liquiditaet-12-monate`:

- **Basis-Szenario** positiv ueber alle zwoelf Monate?
- **Negativ-Szenario** mit zumutbaren Massnahmen abdeckbar?
- **Stress-Szenario** zumindest mit zusaetzlichen Massnahmen (Patronatserklaerung Gesellschafterdarlehen) abdeckbar?

### Schritt 4 — Gesamtbewertung

Drei moegliche Ergebnisse:

#### A. Prognose positiv

- Bilanzbild trotz Ueberschuldung positiv (stille Reserven Rangruecktritt).
- Liquiditaet ueber zwoelf Monate positiv im Basis-Szenario und im Negativ-Szenario.
- Annahmen plausibel und ueberwiegend belegt.
- Sanierungsmassnahmen falls noch erforderlich umgesetzt oder vertraglich gesichert.

**Folge**: Keine insolvenzrechtliche Ueberschuldung nach § 19 Abs. 2 InsO. Antragspflicht entfaellt insoweit. **Aber**: Zahlungsfaehigkeit § 17 InsO und drohende Zahlungsunfaehigkeit § 18 InsO bleiben **eigene** Pruefungspunkte — siehe Plugin `insolvenzrecht`.

#### B. Prognose positiv mit Sanierungsmassnahmen

- Ohne Massnahmen waere die Prognose negativ.
- Mit konkreten umsetzbaren Massnahmen ist die Prognose positiv.

**Folge**: Massnahmen muessen tatsaechlich umgesetzt werden. Skill `sanierungsbausteine-vorschlagen` mit konkreten Vorschlaegen.

**Wichtig**: Massnahmen muessen **rechtzeitig** umgesetzt und **verbindlich** sein:

- Patronatserklaerung **schriftlich unterzeichnet** und vom Patron einsehbar.
- Gesellschafterdarlehen **mit qualifiziertem Rangruecktritt** notariell.
- Stundungsvereinbarungen **schriftlich** mit Glaeubigern.
- Forderungsverzichte **schriftlich** ggf. mit Besserungsschein.

#### C. Prognose negativ

- Liquiditaet ueber zwoelf Monate **nicht sicherstellbar**.
- Sanierungsmassnahmen reichen nicht.
- Keine ausreichende Patronage- / Gesellschafterstuetzung.

**Folge**: 
- **Insolvenzrechtliche Ueberschuldung gegeben** (§ 19 InsO).
- **Antragspflicht** sechs Wochen nach Eintritt § 15a Abs. 1 S. 2 InsO.
- **Sofort Insolvenzanwalt** einschalten — Skill `wenn-prognose-negativ-naechste-schritte`.
- Pruefung **drohende Zahlungsunfaehigkeit** § 18 InsO mit StaRUG-Option (Prognosezeitraum 24 Monate).

## Stichtag und Dokumentation

Die Prognose ist immer auf den **Stichtag des Tages** zu beziehen an dem sie erstellt wird. Das Verhaeltnis Stichtag → 12 Monate ist rollierend.

```yaml
prognose-zusammenfassung:
  prognose-id: FP-2026-0001
  stichtag: 2026-05-20
  geschaeftsleiter: Mueller, Hans (GF GmbH XYZ)
  prognose-horizont: 2026-06 bis 2027-05
  
  bilanzbild:
    bilanzielle-ueberschuldung: ja (Hoehe 82000 EUR)
    insolvenzrechtliche-bilanzbasis: positiv (133000 EUR)
    rangruecktritt: Gesellschafterdarlehen 120000 EUR
    stille-reserven: 175000 EUR
    
  liquiditaet:
    basis-szenario: positiv
    negativ-szenario: positiv knapp (Endbestand Monat 11 bei 8000 EUR)
    stress-szenario: negativ ohne Patronatserklaerung positiv mit
    
  annahmen-belastbarkeit:
    realistisch: 7
    konservativ: 2
    ambitioniert: 1 (Kostensenkung Standortschliessung)
    nicht-belastbar: 0
    
  sanierungsmassnahmen-erforderlich: ja
  konkret-belegt:
    - Patronatserklaerung Hauptgesellschafter 200000 EUR (unterzeichnet)
    - Gesellschafterdarlehen 120000 EUR mit Rangruecktritt (notariell)
    - Stundungsvereinbarungen Lieferanten (schriftlich von 5 Lieferanten)
  noch-offen:
    - Stundung Bank Tilgung (in Verhandlung — noch nicht schriftlich)
    
  ergebnis: positiv-mit-massnahmen
  bewertung-wahrscheinlichkeit: ueberwiegend (mehr als 50 Prozent)
  
  pflicht-ueberpruefung: vierteljaehrlich oder bei wesentlicher Aenderung
```

## Sonderfall — der konkrete Tag der Erstellung zaehlt

- Die Prognose ist **stichtagsbezogen**.
- Bei einer wesentlichen Aenderung der Annahmen (Wegfall Hauptkunde Verlust Kreditlinie) muss die Prognose **neu erstellt** werden.
- Bei vierteljaehrlicher Routinepruefung — Dokumentation der laufenden Pruefung als Beweis fuer aktive Pflichterfuellung des Geschaeftsleiters.

## Ausgabe

- `prognose-zusammenfassung.md` mit Stichtag Bewertung Beleg-Status.
- Weiterleitung an:
  - `sanierungsbausteine-vorschlagen` wenn Massnahmen erforderlich.
  - `wenn-prognose-negativ-naechste-schritte` wenn Ergebnis negativ.
  - `prognose-dokumentation-stichtag` zur abschliessenden Dokumentation.
