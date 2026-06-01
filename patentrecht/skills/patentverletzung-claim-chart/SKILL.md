---
name: patentverletzung-claim-chart
description: "Erstellt Claim Charts für Patentverletzung oder Nichtverletzung: Anspruchsmerkmale, Produkt-/Verfahrensbelege, Fundstellen, Beweisqualität, Lücken, Äquivalenz und Ergebnisampel."
---

# Claim Chart

## Input

- geltender Patentanspruch.
- Produktdaten, Fotos, Handbuch, CAD, Stückliste, Prüfbericht, Quellcode, Prozessbeschreibung.
- Registerstand und Territory.
- Ziel: Angriff, Verteidigung, FTO oder Vergleich.

## Tabelle

| Merkmal | Anspruchswortlaut | Produkt-/Verfahrensbefund | Beleg | Bewertung |
| --- | --- | --- | --- | --- |

Bewertung: erfüllt, nicht erfüllt, unklar, nur äquivalent denkbar, Beleg fehlt.

## Zusatzprüfungen

- Anspruchsauslegung: Begriffe aus Beschreibung/Figuren verstehen.
- Äquivalenz: gleiche Wirkung, Auffindbarkeit, Gleichwertigkeit; Gegenargumente.
- Beweisqualität: Mandantenangabe, Foto, Test, reverse engineering, Zeuge, Sachverständiger.
- Geheimhaltungs-/GeschG-Risiko bei technischen Unterlagen beachten.

## Output

- vollständiger Claim Chart.
- Lückenliste.
- Beweisanforderungen.
- Kurzfazit für Mandant oder Schriftsatz.

## Auslegungs- und Äquivalenz-Pflichtkern

- **§ 14 PatG / Art. 69 EPÜ und Auslegungsprotokoll:** Schutzbereich bestimmt sich nach den Ansprüchen; Beschreibung und Zeichnungen zur Auslegung; Mittelweg zwischen Wortsinn und Inhaltsidee.
- **Wortsinngemäße Verletzung:** Jedes Merkmal muss vollständig im angegriffenen Produkt/Verfahren erfüllt sein. Lückenfreiheit zwingend; einzelnes fehlendes Merkmal verhindert Wortsinn-Verletzung.
- **Äquivalenz (BGH "Schneidmesser" GRUR 2002, 511 / BGH X ZR 168/00):** Drei Voraussetzungen kumulativ:
  1. **Gleiche Wirkung** des Austauschmittels.
  2. **Auffindbarkeit** für den Fachmann mit dem Anspruch als Vorbild.
  3. **Gleichwertigkeit aus dem Anspruch** — Auswahlpflicht.
- **Mittelbare Verletzung § 10 PatG:** Lieferung wesentlicher Erfindungsmittel; sowohl objektives Element (Bezug auf wesentliches Mittel) als auch subjektives Element (Wissen/Erkennbarkeit).
- **Einwendungen:** Vorbenutzungsrecht § 12 PatG, Erschöpfung § 9 S. 2 PatG, Lizenz, Versuchsprivileg § 11 Nr. 2 PatG, Bolar-Klausel.
- **Beweisqualität:** Mandantenangabe < Foto/Video < Demonstration vor Notar/Sachverständigen < Marktproduktprüfung im Labor < unabhängiger Sachverständiger.
- **Geheimnisschutz:** Bei Reverse Engineering § 23 GeschGehG beachten; In-camera-Verfahren UPC oder §§ 16-20 GeschGehG.
- Falle: Claim Chart ohne Anspruchsversion und Stand-Verifikation (DPMA/EPA-Register-Abrufdatum) — bei Einspruch/Beschränkung kann sich der maßgebliche Anspruchstext ändern.
