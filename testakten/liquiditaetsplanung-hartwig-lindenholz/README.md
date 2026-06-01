# Testakte: Liquiditaetsplanung Bauschreinerei Hartwig Lindenholz GmbH

## Zweck

Schlanke Trainings-Testakte fuer das Plugin `liquiditaetsplanung/`.
Kontrastiert bewusst zu den beiden vorhandenen Liquiditaets-Akten:

- **Edelholz Berlin**: Klasse A, Insolvenznaehe (Eroeffnungsantrag steht im Raum)
- **Paragrafix GmbH**: Klasse A, Fortbestehensprognose / StaRUG-Schwelle
- **Hartwig Lindenholz GmbH** (diese Akte): Klasse B, **keine Insolvenzschwelle**,
  klassischer Saison-Cashflow-Engpass im Q1 mit rollierender 13-Wochen-Planung
  und Hausbank-Gespraech (Kontokorrent-Ausweitung).

## Mandant

- **Firma**: Bauschreinerei Hartwig Lindenholz GmbH
- **Sitz**: Bad Driburg (Nordrhein-Westfalen)
- **Branche**: Bauelemente, Innenausbau, Treppenbau (Saison-Geschaeft)
- **Geschaeftsfuehrer**: Hartwig Lindenholz, geb. 1968
- **Beschaeftigte**: 14 (inkl. zwei Auszubildende)
- **Umsatz 2025**: ca. 2,4 Mio EUR
- **Hausbank**: Volksbank Hoexter eG (Kontokorrent 150.000 EUR)

## Steuerberatung

- **Kanzlei**: Brockhausen Steuerberatung
- **StB**: Margarethe Brockhausen
- **Sitz**: Bad Driburg, Lange Strasse 22

## Trainingsfrage

Soll die Mandantin den Liquiditaetsengpass im Q1 mit einer Kontokorrent-Ausweitung
ueberbruecken, oder ist eine strukturelle Massnahme (Working-Capital-Programm,
Saison-Tilgungsplan) sinnvoller?

**Erwartete Antwort**: Kontokorrent-Ausweitung ist nur Symptombekaempfung; die
13-Wochen-Planung zeigt einen wiederkehrenden Saison-Effekt, der durch eine
saisonale Tilgungsstruktur und Vorauszahlungs-Klauseln in Werkvertraegen
strukturell adressiert werden sollte. KEINE Insolvenznaehe.

## Briefkopf-Banner

Diese Akte ist Teil des Briefkopf-Patterns (siehe `scripts/build-testakte-gesamt-pdf.py`).
Jeder MD-Stueck-Block traegt `<!-- AKTE-META ... -->`-Header. Beilagen in `originale/`
haben `.meta`-Sidecars.
