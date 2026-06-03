---
name: abrechnung-ist-plan-mieterschnittstelle
description: "Prüft Jahresabrechnung, Wirtschaftsplan, Ist-Kosten, Planansätze und Mieterschnittstelle. Erkennt Verteilerschlüssel, umlagefähige Betriebskosten, Gewerbeanteile, Nachzahlungen, Belegeinsicht und Vermieterkommunikation. Output: Prüfmatrix."
---

# Abrechnung, Ist/Plan und Mieterschnittstelle

Nutze diesen Skill, wenn Jahresabrechnung, Wirtschaftsplan, Betriebskostenabrechnung für Mieter und Eigentümerabrechnung zusammenstoßen.

## Kerntrennung

- **WEG-Jahresabrechnung:** Verhältnis Gemeinschaft/Eigentümer, Nachschüsse und Anpassung der Vorschüsse.
- **Wirtschaftsplan:** Zukunftsbudget und Vorschüsse.
- **Betriebskostenabrechnung:** Verhältnis Vermieter/Mieter, nur umlagefähige Kosten nach Mietvertrag und BetrKV.
- **Gewerbe:** Restaurant/Laden kann Kosten verursachen, die nicht ohne Weiteres gleichmäßig verteilt werden dürfen.

## Prüfraster

| Position | Ist 2025 | Plan 2026 | Umlagefähig Mieter? | Schlüssel | Risiko |
| --- | --- | --- | --- | --- | --- |
| Heizung | [...] | [...] | [...] | [...] | [...] |
| Wasser | [...] | [...] | [...] | [...] | [...] |
| Hausmeister | [...] | [...] | [...] | [...] | [...] |
| Versicherung | [...] | [...] | [...] | [...] | [...] |
| Instandhaltung | [...] | [...] | regelmäßig nein | [...] | [...] |
| Gewerbe-Sonderkosten | [...] | [...] | prüfen | [...] | [...] |

## Mieterschnittstelle

Vermietende Eigentümer brauchen oft zwei Auswertungen:

1. **WEG-Prüfung:** Ist die Abrechnung gegenüber dem Eigentümer korrekt?
2. **Mieterprüfung:** Welche Positionen dürfen in die Betriebskostenabrechnung?
3. **Fristprüfung:** Abrechnungsfrist und Einwendungsfrist im Mietverhältnis.
4. **Belegpaket:** Rechnungen, Verträge, Verteilerschlüssel, Heizkostenabrechnung.

## Red Flags

- Erhaltungskosten in Betriebskostenabrechnung.
- Gewerbekosten auf alle Wohnungen verteilt ohne Schlüsselprüfung.
- CO2-Kosten falsch oder gar nicht verteilt.
- Ist-Kosten weichen stark vom Plan ab, ohne Erläuterung.
- Vermögensbericht fehlt oder ist mit Abrechnung vermischt.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
