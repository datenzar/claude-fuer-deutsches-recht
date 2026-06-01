---
name: workflow-dokumentenintake
description: "Dokumentenintake im Plugin verlagsredaktion: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte."
---

# Dokumentenintake

## Aufgabe
Dieser Workflow-Skill liest Manuskripte, Aufsätze, Festschriftsbeiträge, Buchprojekte, Lektoratsnoten und Druckfahnen ein und sortiert sie für die Verlagsredaktion juristischer Fachliteratur.

## Dokumentenarten
- **Manuskript Aufsatz (NJW, JuS, JZ, ZIP, BB, NZG etc.):** Titel, Verfasser mit Funktion, Abstract, Gliederung, Fußnoten.
- **Manuskript Festschriftsbeitrag:** Widmung, längere Form, oft historisch-systematische Linie.
- **Lehrbuchmanuskript:** Inhaltsverzeichnis, Stichwortverzeichnis, Schemata, Übungsfälle.
- **Kommentarauszug:** Bearbeiter, Norm, Randnummern, Streitstand-Darstellung.
- **Druckfahne:** Setzungsfehler, Trennungen, Verweise (vgl. ..., siehe oben Rn. ...).
- **Korrespondenz Autor / Verlag:** Korrekturwünsche, Stilfragen, Zitiernachweise.

## Erste Triage
- **Werktyp:** Aufsatz, Anmerkung, Festschriftsbeitrag, Lehrbuch, Kommentar, Praxishandbuch.
- **Zitierstandard:** Verlagsvorgaben (z. B. NJW-Manuskriptrichtlinien) oder Repository-Standard `references/zitierweise.md`.
- **Aktualitätsstand:** Fassungsstand der Norm, Stand der Rspr., Stand der Lit.
- **Rechte:** Verlagsvertrag, Open Access, Nutzungsrechte an Abbildungen.

## Kaltstart
Wenn Material vorliegt, arbeite zuerst mit dem Material. Stelle nur Rückfragen, die für die nächste Weiche nötig sind:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.
