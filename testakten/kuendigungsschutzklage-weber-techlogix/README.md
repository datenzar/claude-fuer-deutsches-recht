# Testakte: Kündigungsschutzklage Weber ./. TechLogix GmbH

**Fiktiver Beispielfall** zur Demonstration der `kueschk-*`-Skills im Plugin `arbeitsrecht`.

## Parteien

| Rolle | Partei |
|---|---|
| Arbeitnehmer (Kläger) | Marcus Weber, Berliner Str. 42, 10243 Berlin |
| Arbeitgeberin (Beklagte) | TechLogix GmbH, Tempelhofer Damm 18, 12099 Berlin, HRB 198432 B, AG Charlottenburg |
| Geschäftsführerin AG | Anja Kreutzfeldt |
| Betriebsrat | Vorhanden (5 Mitglieder, Vorsitz: Torsten Hähnel) |

## Arbeitsverhältnis

| Parameter | Wert |
|---|---|
| Beginn | 01.03.2018 |
| Funktion | Senior IT-Administrator |
| Vollzeit | 40 Std./Woche |
| Bruttogehalt | EUR 4.850,00/Monat |
| Kündigungsfrist | 4 Monate zum Monatsende (§ 622 Abs. 2 Nr. 4 BGB) |
| Betriebsgröße | 23 Arbeitnehmer (inkl. Teilzeit anteilig: 19,5 Köpfe nach § 23 KSchG) |

## Kündigung

| Parameter | Wert |
|---|---|
| Art | Ordentliche betriebsbedingte Kündigung |
| Ausstellungsdatum Schreiben | 28.04.2026 |
| Zugang beim Arbeitnehmer | 30.04.2026 (Einwurf 16:42 Uhr, Zeuge: Nachbarin Frau Koslowski) |
| Beendigungsdatum laut Kündigung | 31.08.2026 |
| Kündigungsgrund laut Schreiben | „Umstrukturierung des IT-Bereichs, Wegfall der Stelle durch Auslagerung an externen Dienstleister" |

**3-Wochen-Frist § 4 KSchG:** Läuft ab **20.05.2026** (Mittwoch).

> ⚠️ Die Frist ist im Zeitpunkt der Akte bereits kritisch nah — typische Testsituation für den Frist-Skill.

## Sachverhalt / Mandantennotiz (unstrukturiert)

```
Erstgespräch 06.05.2026, 14:30 Uhr, Besprechungsraum 2

Marcus Weber, 44 J., verheiratet, 2 Kinder (9 und 13), Ehefrau Teilzeit-Erzieherin.
Keine Schwerbehinderung. Kein BR-Mitglied.

Zum Sachverhalt lt. Mandant: Ende März Gespräch mit GF Kreutzfeldt – kurz, kalt.
Sinngemäß: „Wir lagern den IT-Betrieb an DataFlow Solutions aus. Ihre Stelle fällt weg."
Kein Protokoll, kein Zeuge. Weber hat Notiz gemacht (liegt vor).
Kündigung kam dann als Brief per Bote 30.04., Frau Koslowski aus dem 1. OG war dabei.

Betriebsrat: Weber weiß, dass Torsten Hähnel (BR-Vorsitz) das Anhörungsschreiben nach eigenen
Angaben „zu spät" bekommen haben will. Laut Hähnel kein Widerspruch eingelegt. Zeitplan unklar.

Sozialauswahl: 2 weitere IT-Admins im Betrieb — Felix Grunewald (32, ledig, 2 J. BZ)
und Petra Sonnleitner (51, 1 Kind, 8 J. BZ, GdB 30 – kein Ausweis beantragt).
Warum Weber und nicht Grunewald oder Sonnleitner? Keine Erklärung von AG-Seite.

DataFlow: Auftrag noch nicht unterschrieben lt. Weber. „Die verhandeln noch."

Mandant wünscht: Weiterbeschäftigung, hilfsweise gute Abfindung.
Kostenbelehrung § 12a ArbGG erteilt, Notiz in Akte.
PKH geprüft: Einkommen knapp über Grenze, keine PKH.
Vollmacht unterschrieben. Passfoto gemacht für Akte.
```

## Anlagen in dieser Akte

| Datei | Inhalt |
|---|---|
| `kuendigungsschreiben_techlogix_30-04-2026.txt` | Kündigungsschreiben (Abschrift, Original beim Mandanten) |
| `arbeitsvertrag_weber_2018_auszug.txt` | Auszug Arbeitsvertrag (relevante Klauseln, inkl. Befristungs- und Kündigungsklausel) |
| `mandantennotiz_erstgespraech_06-05-2026.txt` | Handschriftliche Notiz des Anwalts (Abschrift), Erstgespräch |
| `notiz_weber_gespraech_maerz_2026.txt` | Eigene Notiz des Mandanten vom Gespräch mit Kreutzfeldt |
| `betriebsrat_anhoerung_entwurf_roh.txt` | Unvollständiges BR-Anhörungsschreiben der AG (von Weber eingescannt, teils unleserlich) |
| `sozialauswahl_vergleichstabelle_roh.md` | Rohtabelle Vergleich Weber / Grunewald / Sonnleitner (vom Anwalt erstellt) |
| `vollmacht_weber.txt` | Unterschriebene Vollmacht (Abschrift) |

## Rechtliche Knackpunkte dieser Akte

1. **Frist § 4 KSchG** — 20.05.2026 als Ablaufdatum → Soforthandlungsbedarf
2. **Betriebsratsanhörung § 102 BetrVG** — Zeitplan und Vollständigkeit unklar, möglicher Formfehler
3. **Sozialauswahl § 1 Abs. 3 KSchG** — Sonnleitner (GdB 30, 8 J. BZ, 1 Kind) vs. Weber (8,2 J. BZ, 2 Kinder); Grunewald (nur 2 J. BZ) wäre klar schutzbedürftiger
4. **Unternehmerische Entscheidung** — Auftrag DataFlow noch nicht unterschrieben, Wegfall des Beschäftigungsbedarfs nicht nachgewiesen
5. **Sonderkündigungsschutz** — nicht einschlägig, aber abzuprüfen
6. **Weiterbeschäftigungsantrag** — großer Senat BAG, GS-1/84

## Skills zum Durchspielen

| Skill | Was er hier prüft |
|---|---|
| `kueschk-triage-laie-oder-anwalt` | Einstieg (Anwalt-Modus) |
| `kueschk-frist-und-zugang-pruefen` | Fristberechnung, Zugangsbeweis Koslowski |
| `kueschk-anwendbarkeit-kschg-pruefen` | § 23 KSchG: 19,5 berechnete Köpfe |
| `kueschk-formfehler-pruefen` | BR-Anhörung Zeitplan und Vollständigkeit |
| `kueschk-kuendigungsgrund-personen-verhalten-betrieb` | Betriebsbedingt, DataFlow-Auftrag |
| `kueschk-sonderkuendigungsschutz-checkliste` | GdB 30 Sonnleitner, Weber selbst kein Schutz |
| `kueschk-klageschrift-anwalt-baustein` | Klageschrift ArbG Berlin |
| `kueschk-weiterbeschaeftigungsantrag-grosser-senat` | Hilfsantrag Weiterbeschäftigung |
| `kueschk-abfindung-faustformel-und-spannweite` | 8,2 Jahre × 4.850 EUR |
| `kueschk-guetetermin-strategie-und-sprechzettel` | Gütertermin-Vorbereitung |

## Einstieg in die Akte

```
/arbeitsrecht:kueschk-triage-laie-oder-anwalt
```
Dann weiter mit `kueschk-frist-und-zugang-pruefen` — die Frist ist das erste Thema.

## Disclaimer

Alle Personen, Firmen, Adressen, Beträge und Aktenzeichen sind frei erfunden. Übereinstimmungen mit realen Personen oder Unternehmen wären rein zufällig. Die Akte dient ausschließlich dem Testen der Skills und ist keine Rechtsberatung.
