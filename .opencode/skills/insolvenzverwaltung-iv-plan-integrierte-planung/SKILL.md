---
name: insolvenzverwaltung-iv-plan-integrierte-planung
description: "Integrierte Planrechnung aus GuV, Liquidität und Bilanz für Insolvenzplan, StaRUG oder Sanierungskonzept erstellen. §§ 220 229 InsO Finanzplanung § 14 StaRUG. Prüfraster: Ist-Zahlen, Planannahmen, Maßnahmenwirkung, Base Case, Downside, Stressszenarien, Working Capital, Steuer-/Zinseffekte, Brückenrechnung und Annahmenregister. Output: Planungsmodell, Szenariovergleich, Maßnahmen-Brücke, Lückenliste. Abgrenzung: nicht für Vergleichsrechnung (iv-plan-vergleichsrechnung) oder Konzepttext."
---

> Opencode-Port von `insolvenzverwaltung/skills/iv-plan-integrierte-planung/SKILL.md`. Urspruenglicher Skill-Name: `iv-plan-integrierte-planung`.

# Integrierte Planrechnung für Plan und Sanierungskonzept

## Aufgabe

Zahlen konsistent, nachvollziehbar und gerichtsfähig machen. Der Skill verbindet Liquiditätsplanung, GuV-Planung und Planbilanz zu einem Modell, das Sanierungsmaßnahmen, Insolvenzplan, StaRUG-Plan und Fortbestehensprognose tragen kann.

Wenn Unterlagen fehlen, fragt er gezielt nach, bildet eine klar markierte Annahme oder bietet einen Simulationsstand an. Er darf eine Liquiditätsvorschau nie als vollständige Sanierungsplanung ausgeben, solange GuV- und Bilanzbrücken fehlen.

## Startet bei

- neuem Planmandat oder Sanierungsprojekt
- unvollständiger Datenlage
- Vorbereitung von Insolvenzplan, Eigenverwaltung, Schutzschirm oder StaRUG
- Prüfung eines vorhandenen Planentwurfs

## Geführter Workflow

1. Ist-Zahlen importieren und auf Stichtage normalisieren.
2. Planannahmen für Umsatz, Rohertrag, Personal, Fixkosten, Working Capital, Investitionen und Finanzierung erfassen.
3. Maßnahmen mit GuV-, Bilanz- und Liquiditätseffekt einzeln modellieren.
4. Base Case, Plan Case, Fortführung ohne Plan, Liquidation und Stress Case anlegen.
5. Bilanzielle und liquiditätsseitige Brücken erklären, statt nur Tabellen zu liefern.
6. Planversion, Datenstand, Annahmen und Belege dokumentieren.

## Ausgabe

- Planungsmodell als CSV-Struktur
- Annahmenregister
- Szenariovergleich
- Sensitivitätenliste
- Maßnahmen-Brücke
- Plausibilitäts- und Lückenliste

## Mindestmodell

| Ebene | Muss enthalten | Prüffrage |
|---|---|---|
| GuV | Umsatz, Rohertrag, Personal, sonstige Kosten, Zinsen, Steuern, Ergebnis | Erklärt das Modell, wie das Unternehmen wieder Ergebnis erwirtschaftet? |
| Bilanz | Anlagevermögen, Working Capital, Rückstellungen, Finanzschulden, Eigenkapital, Liquidität | Schließt die Bilanz rechnerisch und zeigt sie die Kapitalstruktur nach Sanierung? |
| Liquidität | Anfangsbestand, Einzahlungen, Auszahlungen, Linien, Tilgung, Mindestliquidität | Bleibt Zahlungsfähigkeit im Plan- und Downside-Fall erhalten? |
| Maßnahmen | Kosten, Wirkung, Timing, Status, Verantwortlicher, Nachweis | Ist jede Planveränderung auf eine reale Maßnahme oder belegte Annahme zurückgeführt? |

Für akute Krisen muss die Liquidität kurzfristig engmaschig sein. Für das laufende und folgende Planjahr ist regelmäßig eine monatliche Darstellung sinnvoll. Spätere Planjahre können zusammengefasst werden, wenn die rechnerischen Brücken transparent bleiben.

## Maßnahmen-Brücke

Jede Maßnahme erhält einen eigenen Datensatz:

- **Auslöser/Krisenursache:** Welche Ursache wird behoben oder entschärft?
- **GuV-Effekt:** Umsatz, Marge, Kosten, Abschreibung, Zins, Steuer.
- **Liquiditätseffekt:** Einmalzahlung, laufender Effekt, Vorfinanzierungsbedarf, Fälligkeit.
- **Bilanz-Effekt:** Forderungen, Vorräte, Verbindlichkeiten, Eigenkapital, Rückstellungen.
- **Status:** verbindlich, verhandelt, plausibel, ungeklärt, nicht tragfähig.
- **Nachweis:** Vertrag, Beschluss, Bankzusage, Bestellung, Kündigung, Kalkulation, Kontoauszug.

Keine Maßnahme doppelt zählen. Wenn eine Maßnahme in der GuV ergebniswirksam ist, muss der daraus folgende Cash- und Bilanz-Effekt konsistent abgeleitet werden.

## Sensitivitäten

Mindestens prüfen:

- Forderungseinzug später oder nur teilweise.
- Umsatz oder Auftragseingang niedriger als geplant.
- Rohmarge sinkt.
- Personal- oder Energiekosten steigen.
- Maßnahmen starten später oder wirken nur teilweise.
- Finanzierung wird nur unter zusätzlichen Bedingungen verlängert.
- Steuer-/SV-Rückstände werden nicht wie geplant gestundet.

Ergebnis immer als `trägt`, `trägt nur bei Nachweis`, `trägt nicht` ausgeben.

## Qualitätsgates

- Keine Rechtswirkung ohne genaue Betroffenengruppe, Betrag, Zeitpunkt und Beleg.
- Vergleichsrechnung, Planrechnung und Sanierungskonzept müssen zueinander passen.
- Annahmen, Schätzungen und fehlende Quellen werden sichtbar markiert.
- Berufsgeheimnis, Datenschutz, Geschäftsgeheimnisse und gerichtliche Fristen bleiben vorrangig.
- Liquiditätsplan, GuV und Planbilanz müssen rechnerisch geschlossen sein.
- Working-Capital-Effekte müssen erläutert werden; Wachstum ohne Liquiditätsbindung ist verdächtig.
- Steuer-, Zins- und Sozialversicherungseffekte dürfen nicht als Restgröße verschwinden.
- Kleinere Unternehmen dürfen schlanker geplant werden, aber nicht ohne Ergebnis-/Bilanz-/Liquiditätsverknüpfung.

## Rückfragen

Wenn Angaben fehlen, stelle höchstens acht konkrete Fragen und gruppiere sie nach Zahlen, Recht, Stakeholdern und Verfahren. Bei Eilfällen liefere zuerst eine Minimalroute mit Stoppern.

## Arbeitsstil

Freundlich, ruhig, präzise und planarchitektonisch. Der Skill erklärt, warum eine Information wichtig ist, und macht aus unsortiertem Material einen belastbaren nächsten Arbeitsschritt.

## IV-Einordnung

Diese integrierte Fassung ist für Insolvenzverwalter, Sachwalter und vorläufige Verwaltung zugeschnitten. Sie priorisiert Masseinteresse, Berichtsfähigkeit gegenüber Gericht und Gläubigerausschuss, Rollenreinheit, Dokumentation von Belegen und spätere Planvollzugsfähigkeit.

## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette (IV-Insolvenzplan)

§ 217 InsO (Plan-Option) → § 218 InsO (Vorlage durch IV) → §§ 220-221 InsO (Plan-Inhalte) → § 222 InsO (Gruppenbildung) → §§ 235-244 InsO (Abstimmung) → § 245 InsO (Obstruktionsverbot) → § 248 InsO (Bestaetigung) → § 254 InsO (Wirkung) → §§ 49-51 InsO (Absonderungsrechte in Plan)

## Triage — IV-Plan

Bevor losgelegt wird, klaere:
1. **Plan sinnvoller als Liquidation?** Vergleichsrechnung: Plan-Quote vs. Liquidationsquote.
2. **Gruppenbildung konsistent?** § 222 InsO: gesicherte, nicht gesicherte, Kleinglaeubieger, Arbeitnehmer.
3. **Mehrheiten realistisch?** Simulation Kopf- + Summenmehrheit je Gruppe.
4. **Cramdown-Szenario?** § 245 InsO: ablehnende Gruppe ueberstimmbar wenn Best-Interest-Test bestanden.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## IV-Einordnung

Diese integrierte Fassung ist fuer Insolvenzverwalter, Sachwalter und voraeufige Verwaltung zugeschnitten. Sie priorisiert Masseinteresse, Berichtsfaehigkeit gegenueber Gericht und Glaeubigerausschuss sowie Planvollzugsfaehigkeit.
