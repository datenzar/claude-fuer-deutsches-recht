---
name: workflow-dokumentenintake
description: "Dokumentenintake im Plugin zitierweise-deutsches-recht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte."
---

# Dokumentenintake

## Aufgabe
Dieser Workflow-Skill liest fertige oder im Entwurf befindliche juristische Texte (Memos, Gutachten, Schriftsätze, Aufsätze, Hausarbeiten) ein und prüft Zitate gegen den Repository-Standard `references/zitierweise.md`.

## Dokumentenarten
- **Memo / Gutachten:** Fließtext mit Fußnoten oder eingeschobenen Verweisen ("BGH, Urt. v. TT.MM.JJJJ - Az. ..., freie/amtliche Quelle Rn. 14").
- **Schriftsatz:** im Fließtext eingebettete Zitate; eher knappe Zitate.
- **Aufsatz:** klassische Fußnoten mit Volltextzitierung.
- **Hausarbeit:** Pflichtteil Zitate (Lit. und Rspr.); Plagiatsrisiko bei fehlenden Belegen.
- **Kommentarbeitrag:** strenger Stil nach Verlagsmaßgabe.

## Erste Triage
- **Zitatklassen erkennen:**
  - Norm: § X Y Gesetz (mit Absatz/Satz/Nummer); ggf. Fassungsdatum bei Reform-Norm.
  - Rspr.: Gericht, Datum, Aktenzeichen, Fundstelle (z. B. NJW), Randnummer.
  - Kommentar: Bearbeiter, "in:" Werk, Auflage, Jahr, Norm, Rn.
  - Aufsatz: Autor, Zeitschrift, Jahrgang, Anfangsseite, ggf. konkrete Seite.
  - Buch: Autor, Werk, Auflage, Jahr, ggf. Seite/Rn.
  - EuGH/EuG: Datum, Rechtssache (C-/T-Nummer), ECLI.
- **Stilkonsistenz:** ein Stil im Text durchgängig, nicht "BGHZ 100, 200" neben "BGH NJW 1987, 1234" gemischt ohne System.

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
