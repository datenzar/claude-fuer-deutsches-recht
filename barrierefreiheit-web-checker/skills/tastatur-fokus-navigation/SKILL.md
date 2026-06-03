---
name: tastatur-fokus-navigation
description: "Prüft Tastaturbedienbarkeit, Fokusreihenfolge, sichtbaren Fokus, Skiplinks, Menüs, Modale, Cookie-Banner, Slider, Accordions und Tastaturfallen. Output: Tastaturprotokoll und Fix-Tickets."
---

# Tastatur, Fokus, Navigation

Nutze diesen Skill für die wichtigste manuelle Prüfung: Kann man die Website ohne Maus bedienen?

## Prüfpfad

1. Tab-Reihenfolge ab Startseite.
2. Skiplink oder direkter Sprung zum Hauptinhalt.
3. Sichtbarer Fokus in allen Zuständen.
4. Menüs, Submenüs, Filter, Slider, Accordions.
5. Modale, Cookie-Banner, Warenkorb, Login.
6. Fokus bleibt nicht gefangen und geht nach Schließen sinnvoll zurück.
7. Alle interaktiven Elemente sind erreichbar und auslösbar.

## Protokoll

| URL | Element | Problem | Reproduktion | Priorität | Fix |
| --- | --- | --- | --- | --- | --- |

## Red Flags

- Fokus unsichtbar.
- Cookie-Banner blockiert Tastatur.
- Menü öffnet per Hover, aber nicht per Tastatur.
- Modal lässt Fokus im Hintergrund weiterlaufen.
- Buttons sind als div gebaut.

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
