---
name: insolvenzplan-starug-planwerkstatt-ips-sanierungskonzept
description: "Sanierungskonzept als wirtschaftliche Grundlage für Insolvenzplan oder StaRUG erstellen oder prüfen. §§ 220 229 InsO §§ 6 14 StaRUG Fortbestehensfähigkeit. Prüfraster: Ausgangslage, Krisenstadium, Krisenursachen, Leitbild, Maßnahmenpakete, Stakeholderbeiträge, integrierte GuV-/Bilanz-/Liquiditätsplanung, Szenarien und Dokumentation. Output: Sanierungskonzept-Gliederung, Maßnahmenplan, Plausibilitätsfragen, Lückenliste. Abgrenzung: nicht für integrierte Finanzplanung (ips-integrierte-planung)."
---

> Opencode-Port von `insolvenzplan-starug-planwerkstatt/skills/ips-sanierungskonzept/SKILL.md`. Urspruenglicher Skill-Name: `ips-sanierungskonzept`.

# Sanierungskonzept

## Aufgabe

Das wirtschaftliche Fundament des Plans herstellen. Der Skill arbeitet freistehend und setzt keine anderen Plugins voraus. Wenn Unterlagen fehlen, fragt er gezielt nach, bildet eine klar markierte Annahme oder bietet einen Simulationsstand an.

## Startet bei

- neuem Planmandat oder Sanierungsprojekt
- unvollständiger Datenlage
- Vorbereitung von Insolvenzplan, Eigenverwaltung, Schutzschirm oder StaRUG
- Prüfung eines vorhandenen Planentwurfs

## Geführter Workflow

1. Auftrag, Stichtag, Verfahrensroute und Adressat klären.
2. Unternehmenslage und Datenbasis erfassen: Recht, Wirtschaft, Steuern, Vermögen, Finanzierung, Ergebnis.
3. Krisenstadium, Ursachen und Managementmaßnahmen trennen.
4. Leitbild des sanierten Unternehmens, Marktannahmen, Ertragslogik, Organisation und Liquiditätslogik formulieren.
5. Maßnahmenpakete mit Verantwortlichen, Wirkung, Kosten, Timing, Abhängigkeiten und Belegstatus erfassen.
6. Plausibilitätsbrücken zur integrierten GuV-/Bilanz-/Liquiditätsplanung und Vergleichsrechnung herstellen.
7. Fortbestehensprognose und nachhaltige Sanierungsfähigkeit getrennt bewerten.

## Ausgabe

- Sanierungskonzept-Gliederung
- Maßnahmenplan
- Plausibilitätsfragen
- Management Summary
- Datenanforderung und Lückenliste
- Sanierungsfähigkeits-Ampel

## Kernbestandteile

Ein belastbares Sanierungskonzept braucht:

1. Auftrag, Stichtag, Verwendungszweck.
2. Unternehmensprofil und Ausgangslage.
3. Vermögens-, Finanz- und Ertragslage mit belegter Datenbasis.
4. Krisenstadium und Krisenursachen.
5. Leitbild des sanierten Unternehmens.
6. Maßnahmenprogramm mit Kosten, Timing, Wirkung, Verantwortlichen und Nachweisen.
7. Integrierte Planung aus GuV, Bilanz und Liquidität.
8. Szenarien und Sensitivitäten.
9. Ergebnis zur positiven Fortbestehensprognose und zur nachhaltigen Sanierungsfähigkeit.
10. Dokumentation von Quellen, Annahmen, Planversionen und offenen Punkten.

Bei kleineren Unternehmen darf die Darstellung schlanker sein. Die Kernbestandteile entfallen dadurch nicht; sie werden nur angemessen fokussiert.

## Qualitätsgates

- Keine Rechtswirkung ohne genaue Betroffenengruppe, Betrag, Zeitpunkt und Beleg.
- Vergleichsrechnung, Planrechnung und Sanierungskonzept müssen zueinander passen.
- Annahmen, Schätzungen und fehlende Quellen werden sichtbar markiert.
- Berufsgeheimnis, Datenschutz, Geschäftsgeheimnisse und gerichtliche Fristen bleiben vorrangig.
- Liquidität, GuV und Planbilanz müssen rechnerisch geschlossen sein.
- Eine positive Fortbestehensprognose ersetzt nicht die Prüfung nachhaltiger Sanierungsfähigkeit.
- Maßnahmen ohne Belegstatus, Verantwortlichen und Timing sind nicht tragend.

## Rückfragen

Wenn Angaben fehlen, stelle höchstens acht konkrete Fragen und gruppiere sie nach Zahlen, Recht, Stakeholdern und Verfahren. Bei Eilfällen liefere zuerst eine Minimalroute mit Stoppern.

## Arbeitsstil

Freundlich, ruhig, präzise und planarchitektonisch. Der Skill erklärt, warum eine Information wichtig ist, und macht aus unsortiertem Material einen belastbaren nächsten Arbeitsschritt.


## Rechtliche Grundlagen und Leitentscheidungen (Stand Mai 2026)

- IDW S 6 (Sanierungskonzept) und IDW S 11 (Insolvenzeröffnungsgründe) als methodische Mindeststandards.
- **BGH IX ZR 122/23 vom 05.12.2024** — Bei Bargeschäften im Sanierungskontext: Unlauterkeit (§ 142 Abs. 1 Hs. 2 InsO) muss konkret nachgewiesen werden; bloße Verlustsituation genügt nicht. Relevanz: Sanierungsbausteine ohne gezielte Gläubigerbenachteiligung sind anfechtungsfest. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.12.2024&Aktenzeichen=IX+ZR+122/23>
- **BGH IX ZR 129/22 vom 18.04.2024** — Sanierungsversuche entkräften Vorsatz iSd § 133 InsO bei konkretem belastbarem Sanierungskonzept. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129/22>

## Paragrafenkette (Insolvenzplan / StaRUG)

§ 217 InsO (Plan-Option) → § 218 InsO (Plan-Vorlage) → §§ 220-221 InsO (darstellender und gestaltender Teil) → § 222 InsO (Gruppen) → §§ 235-244 InsO (Abstimmung) → § 245 InsO (Obstruktionsverbot) → § 248 InsO (Planbestaetigung) → § 254 InsO (Planwirkung) → §§ 7-39 StaRUG (StaRUG-Plan) → § 25 StaRUG (Mehrheiten) → § 26 StaRUG (Cramdown)

## Triage — Plan-Vorarbeiten

Bevor losgelegt wird, klaere:
1. **Verfahrensart?** InsO-Plan (§§ 217 ff. InsO) oder StaRUG-Restrukturierungsplan (§§ 7-39 StaRUG)?
2. **Klassenbildung schluessig?** § 222 InsO / § 10 StaRUG — gleiche Rechte und Interessen je Gruppe.
3. **Mehrheits-Simulation?** Ist 75%-Schwelle (StaRUG) oder 50%+50% (InsO) realistisch?
4. **Vergleichsrechnung?** Liquidationswert als Referenz fuer Best-Interest-Test berechnen.
5. **Cramdown-Szenario?** Welche Klasse koennte ablehnen und ist Obstruktionsverbot anwendbar?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
