---
name: patentrecht-patentprozess-claim-construction-de-en
description: "Übersetzt Patentansprüche prozessfest zwischen Deutsch und Englisch: Merkmalsgliederung, claim construction, Äquivalenz, Prosecution History, technische Begriffe und gerichtstaugliche Argumentation."
---

> Opencode-Port von `patentrecht/skills/patentprozess-claim-construction-de-en/SKILL.md`. Urspruenglicher Skill-Name: `patentprozess-claim-construction-de-en`.

# Patentprozess: Claim Construction DE/EN

## Aufgabe

Bilinguale Anspruchsauslegung für deutsche, UPC- und Common-Law-nahe Verfahren.

## Kaltstart

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Anspruch in technische Merkmale zerlegen.**
2. **Begriffspaare DE/EN mit Definition und Fundstelle erfassen.**
3. **Beschreibung, Figuren und Prosecution History zuordnen.**
4. **Wortsinngemäß/Äquivalenz/Nichtverletzung getrennt argumentieren.**
5. **Gerichts- und Mandantenfassung erstellen.**


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

- Bilingual Claim Construction Table.
- Merkmalsgliederung.
- Hearing Vocabulary Sheet.
- Argument Skeleton.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.
