---
name: mandat-triage-agrarrecht
description: Strukturierte Eingangs-Abfrage fuer agrarrechtliche Mandate. Klaert Sachgebiet (Landpacht Hoefeerbfolge Foerderrecht ELER GAP Tierhaltung Pflanzenschutz Duenge-VO Bio-Zertifizierung Direktvermarktung Hofnachfolge Genossenschaft Agrarstrukturrecht Jagdpacht Fischerei) Mandantenrolle (Landwirt Verpaechter Paechter Erbe weichender Erbe Genossenschaft Foerderbescheid-Adressat Verband Behoerde) Sofort-Fristen Sammelantrag-Termin Pachtvertragsanzeige § 2 LPachtVG Erbschaftsanzeige Hoefeerbschaft Verjaehrungen. Eskalation Telefon-Sofort bei Sammelantragsfrist Tierseuchen-Vorfall Behoerdliche Untersagung. Routing zu landpacht-und-hoferbfolge-pruefen.
---

# Mandat-Triage Agrarrecht

## Zweck

Agrarrecht-Mandate sind oft saisonal und förderrechtlich fristbeladen. Triage stellt sicher dass Sammelantrag und LPachtVG-Frist nicht verloren gehen.

## Ablauf — sieben Fragen

### Frage 1 — Mandantenrolle?

- Landwirt selbstbewirtschaftend
- Verpächter (Landwirt oder anderer Eigentümer)
- Pächter
- Hof-Erbe (Anerbe)
- Weichender Erbe
- Junglandwirt-Hofnachfolge
- Genossenschaft / Maschinenring
- Förderbescheid-Adressat
- Verband (Bauernverband)
- Behörde / Landwirtschaftsamt (selten)

### Frage 2 — Sachgebiet?

- Landpacht
- Höfeerbfolge / Hofübergabe
- ELER / GAP Sammelantrag
- Cross Compliance
- Tierhaltung Tiergesundheit
- Pflanzenschutz
- Düngeverordnung
- Wasserrecht im Außenbereich
- Naturschutz / FFH-Gebiet
- Bio-Zertifizierung
- Direktvermarktung Hofladen
- Genossenschaftsrecht
- Agrarstrukturrecht / Reichssiedlungsgesetz
- Jagdpacht / Jagdrecht
- Fischerei
- Bauplanungsrecht Außenbereich § 35 BauGB

### Frage 3 — Akute Eilbedürftigkeit?

- **Sammelantrag-Frist** 15. Mai (Vorlage) — verspätet bedeutet Förderverlust oder Kürzung
- **Tierseuche** ASP MKS Geflügelpest Anordnung Maßregelung
- **Behördliche Untersagung** Tierhaltung Düngung Direktvermarktung
- **Pacht-Kündigung** in laufendem Jahr
- **Cross Compliance Vor-Ort-Kontrolle** kritischer Befund
- **Rückforderung Fördermittel** mit Vollziehung
- **Eilantrag gegen Wolfsentnahme-Verbot**

### Frage 4 — Stand?

- Beratungsbedarf vor Antrag / Vertrag
- Antrag gestellt — wartet auf Bescheid
- Bescheid liegt vor — Frist offen
- Widerspruchs-/Klageverfahren
- Behördliche Anordnung sofortig vollziehbar
- Strafverfahren (z. B. Tierschutz § 17 TierSchG)
- Notarielle Abwicklung (Hofübergabe)

### Frage 5 — Bundesland?

- Höfeerbrecht je Bundesland verschieden
- Bayern: Bayerisches Höferecht
- BW: BWHöfeG
- NDS NRW SH: HöfeO
- HE RH-Pfalz: eigene HöfeO
- Sonstige: allg. Erbrecht
- Land-Recht Naturschutz Wasser

### Frage 6 — Frist?

- **Sammelantrag** 15. Mai (Vorlage länderspezifisch)
- **Pachtvertragsanzeige** § 2 LPachtVG ein Monat
- **Hofübergangs-Anzeige** Landwirtschaftsbehörde
- **Hofeserbschaft** Höferolle-Anpassung sechs Monate
- **Verjährungs-Standard** drei Jahre § 195 BGB
- **Widerspruchsfrist** ein Monat § 70 VwGO

### Frage 7 — Wirtschaftliche Verhältnisse?

- Betriebsgröße (Hektar Tiere Umsatz)
- Förderung-Volumen
- Versicherung Berufshaftpflicht Landwirt
- Erbschaftsteuer-Aspekt bei Hofübergabe

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Landpachtvertrag Hofeserbfolge | `landpacht-und-hoferbfolge-pruefen` |
| Förderbescheid Widerspruch / Klage | `landpacht-und-hoferbfolge-pruefen` ELER plus `mandat-triage-verwaltungsrecht` |
| Tierhaltungs-Streit Tierschutz | (Skill tierhaltung-tierschutz — perspektivisch) |
| Bio-Zertifizierung | (Skill bio-zertifizierung — perspektivisch) |
| Direktvermarktung | (Skill direktvermarktung-recht — perspektivisch) |
| Jagdpacht | (Skill jagdrecht — perspektivisch) |
| Genossenschaft | weiter an `gesellschaftsrecht`-Plugin |
| Strafverfahren TierSchG | weiter an `mandat-triage-strafrecht` |
| Hofübergabe steuerlich | weiter an `anw-mandat-triage-steuerrecht` plus ErbSt |

## Mandatsannahme

- **Konflikt-Check** — bei Höfeerbschaft kein Doppelmandat Anerbe / weichender Erbe
- **Streitwert** Hofeswert / Pachtwert / Förderhöhe
- **Versicherungs-Deckung** Berufshaftpflicht Landwirt prüfen
- **Notarbedarf** Hofübergabe

## Eskalation

- **Telefon-Sofort** Sammelantragsfrist Tierseuche Vor-Ort-Kontrolle Polizei
- **Binnen einer Stunde** Eilantrag VG gegen Anordnung
- **Heute** Pachtvertragsanzeige Sammelantrag-Vorbereitung
- **Diese Woche** Klage Erstentwurf Hofübergabe-Notarvorbereitung

## Ausgabe

- `triage-protokoll-agrarrecht.md`
- Aktenanlage
- Frist im Fristenbuch (Sammelantrag Pachtvertrag-Anzeige etc.)
- Mandatsvereinbarung mit Honorar
- Empfehlung Folge-Skill

## Quellen

- BGB §§ 585 ff. 1922 ff.
- HöfeO LPachtVG
- VO (EU) 2021/2115 GAP-Strategieplan
- TierSchG TierGesG
- BauGB § 35
- Düsing/Martinez Agrarrecht
