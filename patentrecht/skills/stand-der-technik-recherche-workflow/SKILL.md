---
name: stand-der-technik-recherche-workflow
description: "Plant eine Stand-der-Technik-Recherche: Suchbegriffe, CPC/IPC-Klassen, Datenbanken, Suchstrings, Trefferbewertung und Übergabe an das Patentrecherche-Plugin."
---

# Stand-der-Technik-Recherche — Workflow

## Wann nutzen?

- vor eigener Anmeldung.
- zur Prüfung eines Anspruchsentwurfs.
- nach Abmahnung oder Prüfungsbescheid.
- für Einspruch/Nichtigkeitsangriff.
- für Investor-/FTO-Vorrecherche.

## Rechercheauftrag erzeugen

1. Erfindung in Merkmale und technische Wirkung zerlegen.
2. Deutsche und englische Begriffe bilden.
3. Oberbegriffe, Synonyme, Herstellerjargon und Funktionsbegriffe ergänzen.
4. CPC/IPC-Kandidaten bestimmen.
5. Datenbanken und Länder auswählen.
6. Suchstrings dokumentieren.
7. Treffer in Clustern bewerten: hoch, mittel, niedrig, nur Kontext.

## Übergabe an `patentrecherche`

Wenn konkrete Datenbankrecherche nötig ist, schlage vor:

- `patentrecherche/klassifikation-cpc-ipc`
- `patentrecherche/agentische-datenbank-recherche`
- `patentrecherche/stand-der-technik-recherche`
- `patentrecherche/recherchebericht-erstellen`

## Output

- Suchprofil.
- Suchstrings.
- Datenbankplan.
- Trefferbewertungsschema.
- Dokumentationsvorlage für spätere Nachvollziehbarkeit.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
