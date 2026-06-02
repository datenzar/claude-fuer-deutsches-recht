---
name: barrierefreiheit-web-checker-remediation-roadmap-dokumentation
description: "Erstellt Maßnahmenplan für Barrierefreiheits-Fixes: Priorisierung, Nutzerimpact, Rechtsrisiko, Aufwand, Owner, Tickets, Re-Test, Nachweisakte und Management-Reporting. Output: Roadmap und Dokumentation."
---

> Opencode-Port von `barrierefreiheit-web-checker/skills/remediation-roadmap-dokumentation/SKILL.md`. Urspruenglicher Skill-Name: `remediation-roadmap-dokumentation`.

# Remediation-Roadmap und Dokumentation

Nutze diesen Skill nach Audit oder Beschwerde. Ziel ist ein Plan, der Entwickler, Management, Rechtsabteilung und Nutzerkontakt zusammenbringt.

## Priorisierung

1. Blocker in Kernprozessen: Login, Checkout, Antrag, Zahlung, Terminbuchung.
2. Tastaturfallen und Fokusverlust.
3. Fehlende Labels und Fehlermeldungen.
4. Kontrast/Reflow.
5. Dokumente mit rechtlich wesentlichen Informationen.
6. Kosmetische oder seltene Barrieren.

## Roadmap

| Ticket | Problem | Nutzerimpact | Rechtsrisiko | Owner | Frist | Re-Test |
| --- | --- | --- | --- | --- | --- | --- |

## Nachweisakte

- Auditdatum
- Maßstab
- Stichprobe
- Toolversionen
- manuelle Prüfprotokolle
- Tickets
- Re-Test
- offene Restbarrieren mit Begründung
- Kommunikationsnachweise

## Merksatz

Ein Maßnahmenplan ist kein Ausredenpapier. Er muss zeigen, was wann behoben wird, wer verantwortlich ist und wie der Fix geprüft wird.

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
