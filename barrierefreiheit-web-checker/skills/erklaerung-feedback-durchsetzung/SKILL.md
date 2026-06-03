---
name: erklaerung-feedback-durchsetzung
description: "Erstellt Barrierefreiheitserklärung, Feedbackmechanismus, Durchsetzungs- und Behördenreaktion. Trennt öffentliche Stellen, BFSG-relevante Dienste und freiwillige Erklärungen. Output: Erklärung, Antwortbrief oder Maßnahmenvermerk."
---

# Erklärung, Feedback, Durchsetzung

Nutze diesen Skill für Barrierefreiheitserklärungen, Feedbackwege, Beschwerden, Marktüberwachungs- oder Behördenanfragen.

## Inhalt einer guten Erklärung

- Geltungsbereich: Website/App/Dokumente.
- Maßstab: BITV/EN 301 549/WCAG oder freiwilliger Standard.
- Stand der Vereinbarkeit.
- Nicht barrierefreie Inhalte mit Begründung und Maßnahmenplan.
- Erstellungsmethode: Selbstbewertung, externer Audit, Datum.
- Feedbackkontakt.
- Durchsetzungs- oder Beschwerdestelle, falls einschlägig.

## Antwort auf Beschwerde

```text
Vielen Dank für den Hinweis. Wir haben die gemeldete Barriere unter der Vorgangsnummer [...] aufgenommen. Betroffen ist [...]. Wir prüfen den Fehler bis [...] und teilen Ihnen mit, welche Zwischenlösung oder Korrektur vorgesehen ist. Wenn Sie die Information sofort benötigen, stellen wir sie Ihnen in folgender barrierearmer Form bereit: [...].
```

## Red Flags

- Erklärung ist reine Werbeseite.
- "Wir sind WCAG-konform" ohne Auditdatum.
- Feedbackadresse geht ins Leere.
- Bekannte Barrieren werden verschwiegen.
- Keine Alternative für dringende Informationen.

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
