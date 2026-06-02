---
name: patentrecht-stand-der-technik-recherche-workflow
description: "Plant eine Stand-der-Technik-Recherche: Suchbegriffe, CPC/IPC-Klassen, Datenbanken, Suchstrings, Trefferbewertung und Übergabe an das Patentrecherche-Plugin."
---

> Opencode-Port von `patentrecht/skills/stand-der-technik-recherche-workflow/SKILL.md`. Urspruenglicher Skill-Name: `stand-der-technik-recherche-workflow`.

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
