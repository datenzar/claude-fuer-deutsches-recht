---
name: patentrecht-patentprozess-experten-und-sachverstaendige
description: "Plant technische Expertenarbeit in Patentverfahren: Privatgutachten, gerichtliche Sachverständige, Parteigutachten, Experimente, Reproduzierbarkeit, Befragung und Schwachstellenanalyse."
---

> Opencode-Port von `patentrecht/skills/patentprozess-experten-und-sachverstaendige/SKILL.md`. Urspruenglicher Skill-Name: `patentprozess-experten-und-sachverstaendige`.

# Patentprozess: Experten und Sachverständige

## Aufgabe

Technische Evidenz gerichts- und verhandlungsfest machen.

## Kaltstart

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Beweisfrage in technische Testhypothese übersetzen.**
2. **Geeignete Expertise und Unabhängigkeit prüfen.**
3. **Testdesign, Dokumentation und Reproduzierbarkeit sichern.**
4. **Gegenexperten- und Cross-Examination-Fragen vorbereiten.**
5. **Ergebnis in Claim Chart und Schriftsatzlogik übertragen.**


## Prüfmatrix

| Ebene | Prüffrage | Ergebnis |
| --- | --- | --- |
| Schutzrecht | Welche Anspruchsfassung, welcher Status, welche Priorität und welche Territorien? | Register live prüfen; Annahmen markieren. |
| Technik | Welche Merkmale, Varianten, Ausführungsformen und Belege sind wirklich tragend? | Merkmalsgliederung/Claim Chart. |
| Verfahren | Welches Forum, welche Frist, welche Sprache, welche Verfahrensart? | Forum- und Fristenampel. |
| Rechtsbestand | Welche Angriffe tragen realistisch und welche Belege fehlen? | Invalidity-/Opposition-Map. |
| Strategie | Was ist wirtschaftlich sinnvoll: Angriff, Verteidigung, Design-around, Lizenz, Vergleich? | Handlungsempfehlung. |

## Output

Erzeuge je nach Auftrag:

- Expert Brief.
- Test Protocol.
- Weakness Questions.
- Hearing Prep Sheet.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.
