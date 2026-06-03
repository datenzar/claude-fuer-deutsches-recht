---
name: risikomatrix-ampel
description: "Erzeugt eine verständliche Risikoampel für Äußerungen mit Strafrecht, Zivilrecht, Plattformrisiko, arbeits- oder schulbezogenem Risiko, Beleglage, Verteidigungslinie und empfohlenem nächsten Schritt."
---

# Risikomatrix Ampel

## Zweck

Dieser Skill verdichtet die Vollprüfung in ein schnelles Entscheidungsdokument.

## Matrix

| Bereich | Ampel | Grund | Was senkt Risiko? |
|---|---|---|---|
| Strafrecht |  |  |  |
| Zivilrecht |  |  |  |
| Plattform |  |  |  |
| Arbeitsplatz/Schule |  |  |  |
| Reputationsrisiko |  |  |  |

## Ampelmaßstab

- **Grün:** gute Verteidigungslinie, Belege tragfähig, Sachbezug stark.
- **Gelb:** kontextabhängig, Formulierungsrisiko, Belege lückenhaft.
- **Rot:** schwerer unbelegter Tatsachenvorwurf, Prangerwirkung, bewusste Unwahrheit, reine Herabsetzung.

## Output

Gib zusätzlich:

- Top-3-Risiken.
- Top-3-Verteidigungsargumente.
- beste nächste Handlung.
- sichere Alternativfassung.
- Hinweise auf passende Skills.

## Schneller Arbeitsmodus

- Starte mit Wortlaut, Medium, Adressat, Anlass, Vor- und Nachgeschichte, Reichweite, Betroffenem und vorhandenen Belegen.
- Trenne strikt: Tatsachenbehauptung, Werturteil, gemischte Aeusserung, Satire/Spott, Schmähungs- oder Prangerkontext.
- Gewichte meinungsfreiheitsfreundlich, aber nicht blind: Sachbezug, Machtkritik, Beleglage, Formalbeleidigung, Privatbereich und Eskalationsrisiko getrennt ausweisen.
- Keine erfundene Rechtsprechung. Entscheidungen nur mit Gericht, Datum, Aktenzeichen und verifizierbarer Quelle nennen; sonst Recherchebedarf markieren.

## Ausgabeformat

- Ampel mit einem Satz Begruendung.
- Beste Verteidigungslinie.
- Gefaehrlichster Gegeneinwand.
- Sichere Alternativformulierung.
- Naechste Handlung: nichts tun, belegen, loeschen, klarstellen, antworten, verteidigen oder anwaltlich eskalieren.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
