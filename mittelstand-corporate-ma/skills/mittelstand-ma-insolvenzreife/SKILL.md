---
name: mittelstand-ma-insolvenzreife
description: "Freistehender Insolvenzreife- und StaRUG-Schwellencheck für M&A: prüft Zahlungsunfähigkeit, drohende Zahlungsunfähigkeit, Überschuldung, Antragspflichten und Deal-Auswirkungen intern."
---

# Freistehender Insolvenzreife- und StaRUG-Schwellencheck

## Zweck

Dieser Skill prüft in Corporate/M&A-Mandaten, ob Liquiditäts-, Fortbestehens-, Antragspflicht- oder StaRUG-Themen den Deal steuern. Er ersetzt keine finale insolvenzrechtliche Stellungnahme, zwingt aber die kritischen Fragen in eine belastbare Dokumentation.

## Prüfungsbereiche

- Zahlungsunfähigkeit nach § 17 InsO anhand Liquiditätsstatus und 3-Wochen-Vorschau.
- Drohende Zahlungsunfähigkeit nach § 18 InsO als Frühwarn- und StaRUG-Thema.
- Überschuldung nach § 19 InsO mit Fortbestehensprognose und Überschuldungsstatus.
- Antragspflichten und Organhaftung nach § 15a InsO.
- StaRUG-Frühwarnung und Restrukturierungsoptionen.
- Deal-Auswirkungen: MAC, Ordinary Course, Covenants, Finanzierung, Closing Conditions, W&I-Ausschlüsse.

## Arbeitsmodus

1. Erst Datenqualität prüfen: Bankstände, OPOS, Forecast, Bilanz, stille Lasten, Finanzierungslinien, Patronate, Rangrücktritte.
2. Liquiditätsstatus und Vorschau aus `mittelstand-ma-liquiditaetsvorschau` übernehmen oder neu aufbauen.
3. Fortbestehensannahmen getrennt nach operativ, finanziell, rechtlich und transaktionsbezogen dokumentieren.
4. Antragspflicht- und Geschäftsleiterfristen als rote Schwellen in den CP-Kalender eintragen.
5. Unsicherheit nicht glätten: Wenn Daten fehlen, `nicht beurteilbar` ausgeben und konkrete Nachforderung formulieren.

## Ausgabe

- Insolvenzreife-Matrix mit Status je Prüfung.
- StaRUG-Frühwarnmatrix.
- Fragenliste an Geschäftsleitung, CFO, Steuerberater, Finanzierungspartner und Insolvenzrechtsteam.
- Deal Impact Memo für SPA, Signing/Closing, W&I und Board Paper.
- Senior-Review-Gate mit Datum, Owner und offener Belegkette.

## Rote Schwellen

- Geschäftsleitung will trotz roter Liquiditätsampel signen oder closen.
- Fortbestehensprognose wird nur behauptet, aber nicht finanziell belegt.
- Zahlungsstockungen werden als „Timing“ etikettiert, ohne OPOS- und Bankabgleich.
- Rangrücktritt, Patronat oder Stundung sind rechtlich nicht dokumentiert.

## Vorlagen

- assets/templates/insolvenzreife-transaktionscheck.md
- assets/templates/starug-fruehwarnmatrix.md
- assets/templates/insolvenzplan-klassenmatrix.md
- assets/templates/liquiditaetsvorschau-3-wochen.md
