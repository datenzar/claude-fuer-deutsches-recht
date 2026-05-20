# Fortbestehensprognose

Fortbestehensprognose nach § 19 Abs. 2 InsO als Geschaeftsfuehrer-Selbstdokumentation. Pruefablauf Bilanzstatus Annahmen Plausibilisierung 12-Monats-Liquiditaet. Sanierungsbausteine harte Patronatserklaerung Comfortletter Gesellschafterdarlehen Rangruecktritt Stundung Forderungsverzicht. IDW S 11 S 6 StaRUG. Funktioniert allein; empfohlene Begleitplugins liquiditaetsplanung (wochenbasierte Liquiditaet) und insolvenzrecht (§ 17 § 18 InsO Antragspflicht).

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Fortbestehensprognose (`fortbestehensprognose`, dieses Plugin) | [fortbestehensprognose.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fortbestehensprognose.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus „Code → Download ZIP“ verwenden.

## Zum Ausprobieren: Beispielakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

[testakte-fortbestehensprognose-paragrafix-gmbh.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fortbestehensprognose-paragrafix-gmbh.zip)

Fiktive Akte einer mittelständischen GmbH (Paragrafix GmbH) zur Erstellung einer Fortbestehensprognose nach § 19 II InsO: BWA, SuSa, Bilanz, Planungsrechnung, Markt-Annahmen.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `annahmen-belastbarkeit-plausibilisieren` | Plausibilisiert die in `annahmen-sammeln-fortfuehrung` gesammelten Annahmen. Pruefraster Konsistenz mit Vergangenheit (BWA SuSa Jahresabschluss) Marktentwicklung (Branche makroekonomisch) Konsistenz untereinander (Ums… |
| `annahmen-sammeln-fortfuehrung` | Sammelt die Annahmen die der Geschaeftsfuehrer der Fortbestehensprognose zu Grunde legt. Umsatzentwicklung Kostenentwicklung Personalkostenentwicklung Investitionen Working-Capital Saisonalitaet Auftragsbestand Kunden… |
| `ausloesendes-ereignis-erfassen` | Erfasst den Anlass der Fortbestehensprognose. Typische Ausloeser sind Hinweis des Steuerberaters nach § 102 StaRUG Hinweis des Wirtschaftspruefers Bekanntwerden negativen Eigenkapitals Bilanzaufstellung mit negativem … |
| `bilanzieller-status-aufnehmen` | Nimmt die bilanzielle Ausgangslage auf — Aktiva Passiva Eigenkapital nach HGB-Stichtagsbilanz. Pruefraster bilanzielle Ueberschuldung (Aktiva kleiner als Passiva). Erfasst stille Reserven und stille Lasten Sonderposte… |
| `comfortletter-weich-erzeugen` | Erzeugt einen Comfortletter — eine weiche Erklaerung des Patrons oder Mutterunternehmens das Tochterunternehmen zu unterstuetzen. Im Gegensatz zur harten externen Patronatserklaerung ist der Comfortletter nicht rechts… |
| `forderungsverzicht-besserungsschein` | Erzeugt eine Forderungsverzichtsvereinbarung mit Besserungsschein. Glaeubiger verzichtet auf Forderung — bei Wiedererstarken der Zahlungsfaehigkeit der Schuldnerin lebt die Forderung wieder auf. Effekt im insolvenzrec… |
| `fortbestehensprognose-zusammenfuehren` | Fuehrt alle Bausteine zusammen — bilanzieller Status Annahmen Plausibilisierung 12-Monats-Liquiditaet Sensitivitaetsszenarien — und bewertet ob die Fortbestehensprognose nach § 19 Abs. 2 InsO positiv ist. Massstab ueb… |
| `gesellschafterdarlehen-rangruecktritt` | Erzeugt eine Erklaerung zum qualifizierten Rangruecktritt fuer Gesellschafterdarlehen nach § 19 Abs. 2 S. 2 InsO. BGH-konforme Formulierung BGH II ZR 18/19 — der Rangruecktritt muss sich erstrecken auf Insolvenz Glaeu… |
| `fortbestehensprognose-kaltstart-interview` | Kaltstart-Interview fuer das Fortbestehensprognose-Plugin. Stellt fest wer das Plugin nutzt (Geschaeftsfuehrer / Vorstand / Gesellschafter mit Eigenverantwortung / Finanzleiter mit Mandat) wer der Anwaltliche und steu… |
| `liquiditaet-12-monate` | Erstellt die rollierende Zwoelf-Monats-Liquiditaetsvorschau auf Basis der plausibilisierten Annahmen. Pro Woche oder pro Monat Aufstellung der Einzahlungen und Auszahlungen Anfangsbestand Endbestand Linieverbleib. Pru… |
| `patronatserklaerung-extern-hart-erzeugen` | Erzeugt eine harte externe Patronatserklaerung des Gesellschafters (oder eines Dritten) zugunsten der Gesellschaft. Erfasst Patron Begueneten Hoehe Bedingungen Laufzeit Insolvenzfeste Klausel. Zur Beruecksichtigung im… |
| `prognose-dokumentation-stichtag` | Abschliessende Selbstdokumentation der Fortbestehensprognose zum konkreten Stichtag. Enthaelt Ausgangslage Annahmen Plausibilisierung Liquiditaet Szenarien Sanierungsbausteine mit Belegen Gesamtergebnis. Dient als Bel… |
| `sanierungsbausteine-vorschlagen` | Wenn die Fortbestehensprognose ohne Massnahmen negativ oder knapp positiv ist schlaegt dieser Skill konkrete Sanierungsbausteine vor. Auswahl Patronatserklaerung hart Comfortletter Gesellschafterdarlehen mit Rangrueck… |
| `stundungsanfrage-glaeubiger` | Erzeugt Stundungsanfragen an Glaeubiger (Lieferanten Bank Vermieter Steueramt Sozialversicherungstraeger). Erfasst pro Glaeubiger Forderungshoehe Faelligkeit Stundungswunsch (neue Faelligkeit Ratenzahlung Tilgungspaus… |
| `wenn-prognose-negativ-naechste-schritte` | Wenn die Fortbestehensprognose negativ ausfaellt — Eskalations- und Pflichtenkatalog fuer den Geschaeftsleiter. Antragspflicht § 15a InsO sechs Wochen bei Ueberschuldung drei Wochen bei Zahlungsunfaehigkeit. Zahlungsv… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Alle Aussagen beruhen auf der im Plugin hinterlegten Rechtsprechung und genannter Kommentarliteratur. Die Skills ersetzen keine eigene anwaltliche, steuerberatende oder berufsbetreuerische Prüfung im Einzelfall.
