---
name: workflow-rechtsquellen-livecheck
description: "Rechtsquellen-Livecheck im Plugin zitierweise-deutsches-recht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen."
---

# Rechtsquellen-Livecheck

## Aufgabe
Dieser Workflow-Skill verlangt vor jeder Zitatfreigabe einen Live-Check in einer frei zugänglichen oder lizenzierten Quelle. Er bündelt die Pflichtquellen je Zitatklasse.

## Live-Checkpunkte je Zitatklasse
- **Norm:** `gesetze-im-internet.de`, Landesrechts-Portale (z. B. `landesrecht-bw.de`, `recht.nrw.de`). Fassungsdatum / letzte Änderung prüfen, BGBl.-Bekanntmachung markieren.
- **BGH / BVerfG / BVerwG / BAG / BSG / BFH:** Pressemitteilungen und Volltext direkt auf der jeweiligen Bundesgerichts-Seite; Az. exakt; Randnummer der zitierten Stelle.
- **OLG:** länderspezifische Datenbanken; oft auch `dejure.org`, `openjur.de` als Aggregator (Volltext frei).
- **EuGH / EuG:** `curia.europa.eu` (Rechtssache C-/T-Nummer, ECLI als Permalink).
- **Verwaltungsbehörden (BaFin, BKartA, BfDI):** offizielle Verlautbarungen mit Datum und Aktenzeichen.
- **Zeitschriften (NJW, NZG, GRUR, ZIP, BB):** Heft, Anfangsseite, ggf. Verlagsdatenbank (Beck-Online, juris) -- nur als Volltext über lizenzierten Zugriff zitierbar.
- **Kommentare (MüKo, Staudinger, Palandt/Grüneberg, Schönke/Schröder):** Bearbeiter, Werk, Auflage, Jahr, Norm, Rn. -- nur mit lizenziertem Zugriff oder vom Mandanten gelieferter Quelle.
- **Aufsätze:** Anfangsseite + konkrete Seite "(549)" und Autor + Zeitschrift.

## Verifizierungsregeln
- Az. nie aus Modellwissen ergänzen.
- Bei Hinweis auf "ständige Rspr." mindestens eine Leitentscheidung mit echtem Az. nennen.
- Bei nicht-amtlichen Quellen (Beck-Online, juris) Hinweis auf Paywall und Verlagsdatenbank.

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
