---
name: barrierefreiheit-web-checker-automatisierter-audit-axe-43c9eaea
description: "Ordnet automatisierte Accessibility-Scans mit axe, Lighthouse, Pa11y oder ähnlichen Tools ein. Erklärt Treffer, False Positives, False Negatives, manuelle Nachprüfung und Entwickler-Tickets. Output: Scanner-Auswertung."
---

> Opencode-Port von `barrierefreiheit-web-checker/skills/automatisierter-audit-axe-lighthouse/SKILL.md`. Urspruenglicher Skill-Name: `automatisierter-audit-axe-lighthouse`.

# Automatisierter Audit

Automatische Scanner sind nützlich, aber nicht ausreichend. Sie finden technische Muster, nicht die vollständige Nutzbarkeit.

## Vorgehen

1. Tool, Version, Datum und URL dokumentieren.
2. Treffer gruppieren: kritisch, erheblich, gering, Hinweis.
3. Doppelte Treffer konsolidieren.
4. Manuelle Gegenprüfung markieren.
5. Entwickler-Ticket mit Reproduktion und erwarteter Lösung schreiben.
6. Re-Test nach Fix einplanen.

## Warnung

Ein grüner Lighthouse-Wert ist kein Compliance-Nachweis. Tastaturfallen, unverständliche Fehlertexte, schlechte Screenreader-Reihenfolge, PDF-Probleme und Prozessabbrüche bleiben oft unsichtbar.

## Ticketformat

```text
Titel:
URL/Komponente:
Problem:
Reproduktion:
Betroffene Nutzer:
Erwartetes Verhalten:
Prüfmaßstab:
Priorität:
Nachweis:
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
