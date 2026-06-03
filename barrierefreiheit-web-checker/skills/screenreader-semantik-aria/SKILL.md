---
name: screenreader-semantik-aria
description: "Prüft Screenreader-Nutzbarkeit, HTML-Semantik, Landmarken, Überschriften, Labels, Alt-Texte, ARIA, Live-Regionen, Fehlermeldungen und dynamische Komponenten. Output: Screenreader-Prüfprotokoll."
---

# Screenreader, Semantik, ARIA

Nutze diesen Skill, wenn die Website optisch funktioniert, aber semantisch unklar ist.

## Prüfschritte

1. Seitentitel und Sprache.
2. Landmarken: header, nav, main, footer, aside.
3. Überschriftenstruktur.
4. Links und Buttons mit verständlichem Namen.
5. Formularlabels und Fehlermeldungen.
6. Bilder und Icons mit sinnvollen Alternativen oder dekorativer Ausblendung.
7. ARIA nur dort, wo native HTML-Semantik nicht reicht.
8. Live-Regionen für dynamische Statusmeldungen.

## Merksatz

Schlechtes HTML wird durch ARIA selten besser. Erst native Semantik, dann ARIA gezielt.

## Output

```text
Problem:
Betroffene Komponente:
Screenreader-Auswirkung:
Empfohlener Fix:
Prüfung nach Fix:
```

## Schneller Arbeitsmodus

- Lege den Scope fest: Website, App, PDF, Checkout, Formular, Intranet oder öffentliche Stelle; dazu Normrahmen BFSG/BITV/WAD/EN 301 549/WCAG.
- Beurteile nicht nur formal, sondern aus Nutzersicht: Tastatur, Screenreader, Zoom/Reflow, Kontrast, Fehlermeldungen, Zeitlimits und Dokumentzugang.
- Automatische Scanner sind nur Startpunkt. Markiere False Positives, manuelle Nachpruefung und reproduzierbare Testschritte.
- Formuliere Fixes als Entwickler-Tickets mit Komponente, Problem, Nutzerwirkung, Normbezug, Prioritaet und Re-Test.

## Ausgabeformat

- Befund.
- Nutzerwirkung.
- Norm-/Kriteriumsbezug.
- Konkreter Fix.
- Prioritaet und Nachweis fuer die Dokumentation.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
