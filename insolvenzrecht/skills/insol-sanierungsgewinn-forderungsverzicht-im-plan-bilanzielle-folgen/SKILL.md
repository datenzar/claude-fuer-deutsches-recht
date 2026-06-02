---
name: insol-sanierungsgewinn-forderungsverzicht-im-plan-bilanzielle-folgen
description: "Bilanzielle Erfassung des Forderungsverzichts im Insolvenzplan und StaRUG-Plan. Handelsrechtliche und steuerliche Behandlung. Werthaltigkeit der verzichteten Forderung. Verzicht mit und ohne Besserungsschein. Gesellschafterverzicht versus Drittglaeubigerverzicht. Buchungsbeispiele und Auswirkungen auf das Eigenkapital. Schnittstelle zur Modellrechnung Paragraph 3a Absatz 3 EStG."
---

# Sanierungsgewinn — Forderungsverzicht im Plan, bilanzielle Folgen

## Worum geht es

Der Forderungsverzicht ist die typische Sanierungsmassnahme im Insolvenzplan und im StaRUG-Plan. Bilanziell loest er einen **Ertrag** aus — den **Sanierungsertrag** —, dessen steuerliche Behandlung ueber Paragraph 3a EStG laeuft. Aber bilanziell, also handelsrechtlich und in der Steuerbilanz, ist die Erfassung nicht in jedem Fall trivial: Werthaltigkeit der Forderung, Verzicht mit oder ohne Besserungsabrede, Gesellschafterverzicht versus Drittglaeubigerverzicht — jede Variante hat eigene Buchungsfolgen.

Dieser Skill ordnet die Konstellationen und liefert konkrete Buchungs-Saetze.

## Wann brauchen Sie diesen Skill / Kaltstart-Fragen

- Plan steht vor Vollzug; Buchhaltung des Schuldners muss die Bilanzfolgen vorbereiten.
- StB muss die Steuerbilanz fuer das Sanierungsjahr aufstellen.
- IV oder Sachwalter muss dem Glaeubigerausschuss die wirtschaftlichen Folgen erklaeren.

Kaltstart-Fragen:

1. Wer verzichtet (Drittglaeubiger, Gesellschafter, Mischung)?
2. In welcher Hoehe wurde die Forderung in der Bilanz des Schuldners passiviert?
3. Ist der Verzicht endgueltig oder mit Besserungsabrede?
4. Sind die verzichteten Forderungen werthaltig (Bonitaet des Schuldners ohne Sanierung)?
5. Welcher Rechnungslegungsstandard greift (HGB, IFRS)?

## Rechtlicher Rahmen

- Paragraph 252 Absatz 1 Nr. 4 HGB — Vorsichtsprinzip.
- Paragraph 246 HGB — Vollstaendigkeit.
- Paragraph 266 HGB — Bilanzgliederung.
- Paragraph 397 BGB — Erlass.
- Paragraph 158 BGB — Bedingung (Besserungsschein).
- Paragraph 5 Absatz 1 EStG — Massgeblichkeit der Handelsbilanz.
- Paragraph 5 Absatz 2a EStG — Rangruecktritt und auflosbare Verbindlichkeit.
- Paragraph 3a EStG — steuerliche Begnadigung des Sanierungsertrags.
- BFH, Urteil vom 26.02.2003 — II R 19/01: Verbindlichkeiten bleiben zivilrechtlich ueber die Liquidation hinaus bestehen; blosse Vermoegenslosigkeit begruendet keine Ausbuchung der Verbindlichkeit — Abgrenzung zum Verzicht.

## Workflow / Schritt fuer Schritt

1. **Forderung und Bilanzposition zuordnen.** Welche Verbindlichkeit der Schuldnerin steht der verzichteten Forderung gegenueber?
2. **Verzichtsart klaeren.** Endgueltig oder unter Besserungsabrede? Drittglaeubiger oder Gesellschafter?
3. **Werthaltigkeit der Forderung pruefen** (Bonitaet ohne Sanierung): vollwerthaltig, teilwerthaltig, nicht werthaltig.
4. **Bilanzielle Buchung waehlen** (siehe Tabelle).
5. **Steuerliche Behandlung pruefen.** Sanierungsertrag versus Einlage versus auflosbare Verbindlichkeit.
6. **Schnittstelle zu Paragraph 3a Absatz 3 EStG** (Modellrechnung).

## Buchungslogik

**Standardfall: Drittglaeubiger verzichtet endgueltig auf werthaltige Forderung**

```
Soll: Verbindlichkeit gegenueber Drittglaeubiger    EUR 1.000.000
Haben: ausserordentlicher Ertrag (Sanierungsertrag) EUR 1.000.000
```

Steuerlich: Sanierungsertrag, Paragraph 3a EStG anwendbar.

**Variante: Gesellschafter verzichtet (gesellschaftsrechtlich veranlasst) auf werthaltige Forderung**

```
Soll: Verbindlichkeit gegenueber Gesellschafter     EUR 1.000.000
Haben: Kapitalruecklage Paragraph 272 Absatz 2 Nr. 4 HGB EUR 1.000.000
```

Steuerlich: verdeckte Einlage; **kein** Sanierungsertrag, sondern Erhoehung der Anschaffungskosten der Beteiligung beim Gesellschafter (BFH-Linie zur verdeckten Einlage).

**Variante: Gesellschafter verzichtet auf nicht werthaltige Forderung**

```
Soll: Verbindlichkeit gegenueber Gesellschafter     EUR 1.000.000
Haben: Kapitalruecklage (Werthaltigkeit Tag des Verzichts) EUR 200.000
Haben: ausserordentlicher Ertrag (Sanierungsertrag) EUR 800.000
```

Steuerlich: Mischfall; nur der werthaltige Teil ist Einlage, der nicht werthaltige Teil ist Sanierungsertrag. Werthaltigkeitspruefung zwingend (BFH-Linie).

**Variante: Verzicht mit Besserungsabrede (Besserungsschein) gegenueber Drittglaeubiger**

```
Tag des Verzichts:
Soll: Verbindlichkeit                               EUR 1.000.000
Haben: ausserordentlicher Ertrag (Sanierungsertrag) EUR 1.000.000

Tag des Eintritts des Besserungsfalls:
Soll: ausserordentlicher Aufwand                    EUR x
Haben: Verbindlichkeit                              EUR x
```

Steuerlich: Sanierungsertrag entsteht im Verzichtsjahr; spaeterer Wiederaufleben fuehrt zu Aufwand. Wenn der Besserungsfall vor Plan-Vollzug feststeht, ist der Verzicht aufschiebend bedingt und entsteht erst mit Bedingungseintritt — abhaengig von der Klauselgestaltung.

**Variante: nur teilweiser Verzicht (Plan-Quote)**

```
Soll: Verbindlichkeit (verzichteter Teil)           EUR 800.000
Haben: ausserordentlicher Ertrag                    EUR 800.000

Die verbleibenden 20 % bleiben passiviert und werden plangemaess bedient.
```

## Trade-off-Matrix

| Gestaltung | bilanzielle Wirkung | steuerliche Wirkung |
|---|---|---|
| Endgueltiger Verzicht Drittglaeubiger | sofortiger Ertrag | Sanierungsertrag Paragraph 3a EStG |
| Verzicht mit Besserungsschein | sofortiger Ertrag mit potenzieller Rueckbuchung | Sanierungsertrag im Verzichtsjahr; Rueckbuchung im Besserungsjahr Aufwand |
| Gesellschafter-Verzicht werthaltig | Erhoehung Kapitalruecklage | verdeckte Einlage, kein Sanierungsertrag |
| Gesellschafter-Verzicht nicht werthaltig | gemischt | werthaltiger Teil Einlage, Rest Sanierungsertrag |
| Rangruecktritt qualifiziert (Paragraph 5 Absatz 2a EStG) | Verbindlichkeit bleibt | erst bei spaeterer Aufloesung Ertrag |
| Schuldumwandlung (DES) | Verbindlichkeit wird Eigenkapital | siehe Skill DES |

## Praxistipps der alten Hasen

1. **Werthaltigkeitspruefung dokumentieren.** Beim Gesellschafterverzicht entscheidet die Werthaltigkeit der Forderung am Tag des Verzichts. Spaetere Sicht ist irrelevant.
2. **Besserungsabrede genau formulieren.** Eine missverstaendliche Klausel kann den gesamten Sanierungsertrag steuerlich nach hinten verschieben — oder umgekehrt vorziehen.
3. **HGB- und Steuerbilanz auseinander halten.** Massgeblichkeit nach Paragraph 5 Absatz 1 EStG, aber Sonderregeln greifen.
4. **Konzern-Verzichte sind heikel.** Verdeckte Einlage Mutter zugunsten Tochter laeuft anders als ueber Schwesterunternehmen.
5. **Achtung Ausbuchung mangels Schuldner.** Verbindlichkeiten bleiben nach BFH II R 19/01 ueber blosse Vermoegenslosigkeit hinaus bestehen — keine erleichterte Ausbuchung; Verzicht ist eigene Kategorie.

## Mustertexte / Berechnungsbeispiele

**Aktennotiz Werthaltigkeitspruefung Gesellschafter-Verzicht:**

```
AKTENNOTIZ WERTHALTIGKEITSPRUEFUNG
Schuldnerin: [Name]
Gesellschafter: [Name]
Forderung: EUR [Betrag]
Tag des Verzichts: [Datum]

1. Sachverhalt
Der Gesellschafter [Name] verzichtet im Rahmen des Insolvenzplans / StaRUG-
Plans auf seine Forderung in Hoehe von EUR [Betrag] gegen die Schuldnerin.

2. Werthaltigkeit am Tag des Verzichts
Zu pruefen ist, ob die Forderung am Tag des Verzichts werthaltig war.
- Vermoegenslage Schuldnerin laut Bilanz vom [Datum]: EUR [...]
- Forderungsbestand insgesamt: EUR [...]
- Hypothetische Liquidationsquote: [%]
- Forderung des Gesellschafters: EUR [Betrag]
- Hypothetisch realisierbarer Betrag: EUR [Betrag] x [%] = EUR [...]

3. Bewertung
Die Forderung war zu [%] werthaltig. Daher: verdeckte Einlage in Hoehe
EUR [...], Sanierungsertrag in Hoehe EUR [...].

4. Verbuchung
[wie oben Variante "nicht werthaltig"]
```

## Typische Fehler

1. Werthaltigkeitspruefung beim Gesellschafterverzicht uebergangen — Ertrag faelschlich als Sanierungsertrag verbucht.
2. Besserungsschein-Klausel als unmittelbaren Verzicht behandelt.
3. Konzern-Verzicht ueber Schwester ohne Beruecksichtigung der Dreiecksbeziehung verbucht.
4. HGB- und Steuerbilanz nicht abgestimmt.
5. Ausbuchung mangels Schuldner mit Verzicht verwechselt (BFH II R 19/01 nicht beachtet).
6. Bei nur teilweisem Verzicht (Plan-Quote) Buchung als Vollverzicht.

## Querverweise

Im Plugin `insolvenzrecht`:

- `insol-sanierungsgewinn-3a-estg-im-insolvenzplan` — materielle Voraussetzungen.
- `insol-sanierungsgewinn-verlustvortrag-und-3a-iii-estg-vorab-pruefen` — Verrechnung.
- `insol-sanierungsgewinn-rangruecktritt-und-5-abs-2a-estg-im-plan` — Rangruecktritt.
- `insol-sanierungsgewinn-debt-equity-swap-im-plan` — DES.
- `insol-sanierungsgewinn-massehaftungsbefreiung-und-bilanz` — Massehaftung-Bilanz-Effekte.

In anderen Plugins:

- `steuerrecht-anwalt-und-berater` — Bilanzsteuerrecht.
- `grosskanzlei-corporate-ma` — Distressed-Bilanz-Themen.

## Quellen Stand 06/2026

- Paragraphen 246, 252, 266, 272 HGB, `gesetze-im-internet.de/hgb/`.
- Paragraph 5 EStG, `gesetze-im-internet.de/estg/__5.html`.
- Paragraph 3a EStG, `gesetze-im-internet.de/estg/__3a.html`.
- Paragraphen 158, 397 BGB, `gesetze-im-internet.de/bgb/`.
- BFH, Urteil vom 26.02.2003 — II R 19/01.
- OFD Frankfurt a. M. zur Behandlung der Verbindlichkeiten in Liquidation — aktuelle Verlautbarung vom Anwender mit aktueller OFD-Veroeffentlichung zu pruefen.
- Zitierweise und Quellenpruefung siehe `references/zitierweise.md`.
