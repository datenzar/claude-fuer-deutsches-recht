---
name: workflow-mandantenkommunikation
description: "Mandantenkommunikation im Plugin kanzlei-builder-hub: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten."
---

# Mandantenkommunikation

## Aufgabe
Dieser Workflow-Skill kommuniziert Builder-Ergebnisse an die Auftraggeber-Seite (Kanzleipartner, IT-Verantwortliche, Wissensmanagement, externe Mandanten der Builder-Kanzlei) -- knapp, technisch korrekt, mit Hinweis auf Validator-Status.

## Kommunikations-Struktur
- **Was wurde gebaut:** Plugin-Name, Skill-Name(n), Version (semantisch).
- **Validator-Status:** `validate-yaml-frontmatter.py` und `validate-plugin-structure.mjs` -- OK / Fehler.
- **Was ist NICHT enthalten:** Skill-Grenzen klar benennen (kein Live-Quellencheck, kein Mandantengeheimnis-Hosting, kein KI-Output ohne Verifizierung).
- **Nächste Schritte:** Testlauf vorgesehen, Rollout-Termin, Schulungsbedarf.
- **Risiken / offene Punkte:** Halluzinationsrisiken, Mandantenakte-Konformität, BORA-Pflichten der Kanzlei beim Einsatz.

## Adressatengerecht
- **Kanzleipartner:** Geschäftsnutzen, Risikohinweise, Lizenz/Datenschutz, Schulungsaufwand.
- **IT/Admin:** Installations-/Update-Pfad, Validator-Pipeline, Abhängigkeiten.
- **Wissensmanagement:** Pflege, Zitationsstandard, Update-Zyklus für Rechtsprechungs- und Norm-Änderungen.

## Anti-Muster
- Versprechen "rechtssichere KI" -- KI ist nie ohne Verifizierung rechtssicher (Verschwiegenheit § 43a Abs. 2 BRAO, § 203 StGB, Halluzinationsrisiken).
- "Wir ersetzen den Anwalt" -- Skill ist Werkzeug, kein Mandatsverhältnis.

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
