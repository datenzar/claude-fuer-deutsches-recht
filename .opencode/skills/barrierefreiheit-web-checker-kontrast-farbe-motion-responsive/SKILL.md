---
name: barrierefreiheit-web-checker-kontrast-farbe-motion-responsive
description: "Prüft Kontrast, Farbe ohne Farbcodierung, Zoom, Reflow, Textabstände, responsives Layout, Animationen, Motion-Reduction, Hover-Fallen und mobile Nutzung. Output: visuelle Barrierefreiheitsmatrix."
---

> Opencode-Port von `barrierefreiheit-web-checker/skills/kontrast-farbe-motion-responsive/SKILL.md`. Urspruenglicher Skill-Name: `kontrast-farbe-motion-responsive`.

# Kontrast, Farbe, Motion, Responsive

Nutze diesen Skill für visuelle und responsive Barrierefreiheit.

## Prüffelder

- Text- und Komponenten-Kontrast.
- Informationen nicht nur durch Farbe.
- Zoom bis 200 Prozent ohne Funktionsverlust.
- Reflow bei schmaler Ansicht.
- Textabstände und Zeilenhöhen.
- Animationen, Parallax, Autoplay, blinkende Inhalte.
- prefers-reduced-motion respektieren.
- Touch-Zielgrößen und mobile Bedienbarkeit.

## Matrix

| Komponente | Problem | Nutzerwirkung | Fix |
| --- | --- | --- | --- |
| Button | Kontrast zu niedrig | nicht erkennbar | Farbe/Border anpassen |
| Fehlermeldung | nur rot | Farbwahrnehmung | Icon + Text |
| Slider | Autoplay | Bewegung/Bedienung | Pause/Stop + Motion |

## Priorität

Kontrast und Reflow sind oft schnell zu beheben und stark nutzerwirksam. Animationsprobleme werden gern unterschätzt, weil sie nur manche Nutzerinnen und Nutzer hart treffen.

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
