---
name: dsfa-bfdi-und-laender-blacklist
description: "Abgleich einer Verarbeitung mit der BfDI-Pflichtliste nach Art. 35 Abs. 4 DSGVO und mit den Listen der Landesdatenschutzbehoerden. Output: dokumentierter Listenabgleich mit Trefferanalyse und ggf. Verweis auf zwingende DSFA."
---

# BfDI- und Laender-Blacklist Abgleich

## Zweck

Dieser Skill fuehrt einen sauberen Abgleich einer konkreten Verarbeitungstaetigkeit mit der Pflichtliste der zustaendigen Aufsichtsbehoerde nach Art. 35 Abs. 4 DSGVO (Blacklist) und mit der Whitelist nach Art. 35 Abs. 5 DSGVO durch. Ergebnis ist ein dokumentierter Listenabgleich, der die Erforderlichkeit oder Entbehrlichkeit einer DSFA stuetzt.

## Wann brauchen Sie diesen Skill

- In der DSFA-Trigger-Pruefung (Schwellwertanalyse)
- Bei einer Aufsichtsanfrage zur Begruendung einer durchgefuehrten oder unterlassenen DSFA
- Bei wesentlichen Aenderungen der Verarbeitung
- Wenn unklar ist, welche Landesdatenschutzbehoerde zustaendig ist (Sitzland-Pruefung)

## Rechtlicher Rahmen

- Art. 35 Abs. 4 DSGVO: Aufsichtsbehoerden erstellen und veroeffentlichen Listen der Verarbeitungstaetigkeiten, fuer die eine DSFA durchzufuehren ist.
- Art. 35 Abs. 5 DSGVO: Aufsichtsbehoerden koennen Listen veroeffentlichen, fuer die keine DSFA erforderlich ist (Whitelist).
- Art. 35 Abs. 6 DSGVO: Listen werden dem Ausschuss EDSA uebermittelt, Koehaerenzverfahren bei grenzueberschreitenden Verarbeitungen.
- § 40 BDSG: Zustaendigkeit der Landesdatenschutzbehoerden fuer den nicht-oeffentlichen Bereich.
- § 67 BDSG verweist auf die Pflichtliste im oeffentlichen Bereich des Bundes.
- EDSA-Leitlinien WP 248 rev.01 als Auslegungshilfe.

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Welche Verarbeitung soll abgeglichen werden? Konkrete Bezeichnung, Branche, eingesetzte Technologie, Datenkategorien.
2. **Verhaeltnismaessigkeitspruefung.** Zustaendige Aufsichtsbehoerde ermitteln: Bund (BfDI) fuer oeffentliche Stellen des Bundes, Telekommunikation und Postwesen; Laender fuer den nicht-oeffentlichen Bereich, sortiert nach Sitzland des Verantwortlichen.
3. **Risikoanalyse Listenabgleich.** Aktuelle Blacklist der zustaendigen Behoerde live abrufen (bfdi.bund.de bzw. Landesbehoerde). Treffer dokumentieren mit konkretem Listenpunkt und Datum des Abrufs.
4. **Massnahmen.** Pruefen ob die Verarbeitung exakt unter einen Listenpunkt faellt oder nur partiell. Bei partieller Deckung: Begruendung warum trotzdem oder warum nicht DSFA-pflichtig.
5. **Restrisiko.** Falls Blacklist-Treffer: DSFA zwingend. Falls Whitelist-Treffer: DSFA entbehrlich, Dokumentation der Whitelist-Position. Falls weder noch: Pruefung nach Art. 35 Abs. 1 und Abs. 3 DSGVO erforderlich.
6. **Konsultation / Genehmigung.** Listenabgleich dem DSB vorlegen, gegenzeichnen lassen, in das Verarbeitungsverzeichnis nach Art. 30 verlinken.

## Mustertext / Template

```
LISTENABGLEICH NACH ART. 35 ABS. 4 / ABS. 5 DSGVO [DATUM]

Verarbeitung: [BEZEICHNUNG]
Verantwortlicher: [NAME, SITZLAND]
Zustaendige Aufsichtsbehoerde: [BfDI / LfDI BW / LDA Bayern / ...]

Quelle Blacklist (Stand): [URL, Abrufdatum]
Quelle Whitelist (Stand): [URL, Abrufdatum]

Pruefung Blacklist
- Listenpunkt 1: [Bezeichnung] — Treffer ja / nein — Begruendung
- Listenpunkt 2: [Bezeichnung] — Treffer ja / nein — Begruendung
- ...

Pruefung Whitelist
- Listenpunkt: [Bezeichnung] — Treffer ja / nein — Begruendung

Ergebnis
[ ] BLACKLIST-TREFFER — DSFA zwingend nach Art. 35 Abs. 4 DSGVO
[ ] WHITELIST-TREFFER — DSFA entbehrlich nach Art. 35 Abs. 5 DSGVO
[ ] KEIN LISTENTREFFER — Pruefung nach Art. 35 Abs. 1, 3 DSGVO fortsetzen

Naechster Schritt: [Vollstaendige DSFA / Dokumentation / Weiterleitung an Skill]

Unterschrift: ____________________
```

## Typische Fehler

- Nur BfDI geprueft, Landesbehoerde uebersehen — im nicht-oeffentlichen Bereich ist regelmaessig die Landesbehoerde des Sitzlandes zustaendig.
- Listenstand veraltet — Listen werden fortgeschrieben, immer aktuelles Datum dokumentieren.
- Partielle Deckung als Volltreffer behandelt — Listenpunkte sind typenoffen, aber konkret zu pruefen.
- Whitelist als Freibrief verstanden — Whitelist entlastet nur, wenn die Verarbeitung exakt zur Listenposition passt.
- Keine Dokumentation des Abrufdatums — Aufsicht kann den Stand nicht nachvollziehen.
- Grenzueberschreitende Verarbeitung: Federfuehrungsbehoerde nach Art. 56 DSGVO uebersehen.

## Querverweise

- `datenschutzrecht/skills/dsfa-art-35-dsgvo-trigger-und-anwendungsbereich/SKILL.md` — Trigger-Pruefung
- `datenschutzrecht/skills/dsfa-edpb-leitlinien-9-19-anwendung/SKILL.md` — Wenn kein Listentreffer
- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` — Bei Blacklist-Treffer
- `datenschutzrecht/skills/spezial-dpia-dokumentenmatrix-und-lueckenliste/SKILL.md` — Dokumentenmatrix
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- Art. 35 Abs. 4, 5, 6 DSGVO
- § 40, § 67 BDSG
- BfDI: bfdi.bund.de — Pflichtliste und Whitelist (live pruefen)
- LfDI Baden-Wuerttemberg, LDA Bayern, BlnBDI Berlin, HmbBfDI Hamburg, HBDI Hessen, LfDI Rheinland-Pfalz, LfD Niedersachsen, LDI NRW, ULD Schleswig-Holstein, LfDI Saarland, SaechsDSB, LfD Sachsen-Anhalt, TLfDI, LfD Mecklenburg-Vorpommern, LfDI Bremen, LfD Brandenburg — eigene Listen abrufen
- EDSA-Leitlinien WP 248 rev.01
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle
