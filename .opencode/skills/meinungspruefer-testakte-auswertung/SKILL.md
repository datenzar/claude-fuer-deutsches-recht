---
name: meinungspruefer-testakte-auswertung
description: "Wertet die Testakte meinungspruefer-grenzfaelle-alltag aus. Sortiert X, LinkedIn, Kantine, Schule, Arbeitgeber, Bürgermeister, Lackaffe, Pinocchio und Tatsachenbelege in getrennte Prüfstränge."
---

> Opencode-Port von `meinungspruefer/skills/testakte-auswertung/SKILL.md`. Urspruenglicher Skill-Name: `testakte-auswertung`.

# Testakte auswerten

## Ziel

Nutze diesen Skill, wenn die Arbeitsakte `meinungspruefer-grenzfaelle-alltag` hochgeladen oder genannt wird. Die Akte enthält mehrere kleine, unordentliche Äußerungsfälle. Sie soll nicht mit einer Erwartungshorizont erschlagen werden, sondern in Arbeitsstränge zerlegt werden.

## Vorgehen

1. Dateien inventarisieren.
2. Jede Äußerung als eigenes Äußerungsblatt erfassen.
3. Stränge bilden:
   - X-Post Bauprojekt.
   - LinkedIn Projektleitung.
   - Kantine/Arbeitgeber.
   - Schule/Elternchat.
   - Bürgermeister und "Lackaffe".
   - Pinocchio-Vergleich.
   - Tatsachenvorwurf mit Beleglücken.
4. Pro Strang passende Skills vorschlagen.
5. Eine Gesamtampel ausgeben.

## Output

- Akteninventar.
- Äußerungsliste.
- Risikocluster.
- Nächste Bearbeitungsschritte.
- Vorschlag für einen vollständigen Prüfvermerk.

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
