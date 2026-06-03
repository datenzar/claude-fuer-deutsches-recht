---
name: europarecht-emrk-grch
description: "Ordnet Art 10 EMRK und Art 11 GRCh in die Äußerungsprüfung ein. Prüft scharfe Äußerungen, Reputationsschutz, Plattformen, Suchmaschinen, Datenschutz, Verhältnismäßigkeit und unionsrechtliche Bezüge."
---

# Europarecht: EMRK und Grundrechtecharta

## Leitplanken

Art. 10 EMRK schützt Freiheit der Meinungsäußerung; Einschränkungen müssen gesetzlich vorgesehen, legitim und in einer demokratischen Gesellschaft notwendig sein. Art. 11 GRCh schützt Freiheit der Meinungsäußerung und Informationsfreiheit im Unionsrecht.

Die europäische Ebene ist keine Dekoration. Sie soll prüfen, ob die deutsche Lösung konventions- und unionsrechtsfreundlich ist:

- EGMR: demokratische Notwendigkeit, Werturteil/Tatsachengrundlage, Art.-8-/Art.-10-Abwägung, Sanktion und chilling effect.
- EuGH/GRCh: Plattformen, Suchmaschinen, Datenschutz, DSA, Uploadfilter, journalistische Zwecke, Art. 7, 8, 11 und 16 GRCh.

## Wann relevant?

- Plattformregulierung, DSA, unionsrechtlicher Kontext.
- Presse, Journalismus, öffentliche Debatte.
- Staatliche Sanktion oder gerichtliche Unterlassung mit europarechtlichem Bezug.
- Grundrechtsfreundliche Auslegung im Lichte der EMRK.
- Suchmaschinen-De-Referenzierung oder Löschung angeblich falscher Inhalte.
- Veröffentlichung personenbezogener Daten, Video, Screenshot oder Namensnennung.

## Prüfpunkte

1. Schutzbereich und Kommunikationswert.
2. Eingriff oder private Plattformmaßnahme mit rechtlichem Rahmen.
3. gesetzliche Grundlage oder unionsrechtlicher Anker.
4. legitimer Zweck: Rechte anderer, Reputation, Privatleben, Datenschutz, Ordnung, Sicherheit.
5. Notwendigkeit und Verhältnismäßigkeit.
6. Rolle der betroffenen Person und Beitrag zu öffentlicher Debatte.
7. Tatsachengrundlage bei Werturteilen.
8. Reichweite der Sanktion: Verurteilung, Unterlassung, Löschung, De-Referenzierung, Label, Sperre.

## Spezialrouting

| Befund | Nächster Skill |
|---|---|
| EGMR-Art.-10-Rechtsprechung wird tragend | `egmr-art-10-rechtsprechung` |
| Plattform, Suchmaschine, DSGVO, DSA oder Uploadfilter | `eugh-grch-art-11-rechtsprechung` |
| Deutsche Instanzpraxis, Verbotstenor oder Eilverfahren | `olg-kg-praxis-rechtsprechung` |
| Internationaler Vergleich mit USA | `rechtsvergleich-usa-supreme-court` |

## Output

- EMRK-/GRCh-Relevanz:
- Schutzintensität:
- Einschränkungsgrund:
- Verhältnismäßigkeitsargument:
- Integration in deutsche Art.-5-GG-Abwägung:
- Zu ladende Spezialskills:


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
