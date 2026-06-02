---
name: patentrecht-us-patent-law-pto-ptab
description: "Orientiert deutsche Teams im US-Patentrecht: Patentability, claim drafting, IDS, office action, continuation, reissue, reexamination, IPR/PGR vor PTAB und Local-Counsel-Briefing."
---

> Opencode-Port von `patentrecht/skills/us-patent-law-pto-ptab/SKILL.md`. Urspruenglicher Skill-Name: `us-patent-law-pto-ptab`.

# US-Patentrecht: USPTO und PTAB

## Aufgabe

US-spezifische Patentamts- und PTAB-Themen ohne deutschen Automatismus.

## Kaltstart

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **US-Ziel klären: Prosecution, FTO, PTAB-Angriff oder Litigation Support.**
2. **Claims auf US-Eligibility, novelty, non-obviousness und written description/external support sensibel prüfen.**
3. **IDS-/Prior-Art- und Family-Consistency-Fragen sammeln.**
4. **Office-Action-Response oder PTAB-Petition als Arbeitsauftrag strukturieren.**
5. **US Counsel Fragen, Deadlines und Dokumente vorbereiten.**


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

- US Patent Issue List.
- Office Action Response Outline.
- PTAB Briefing Sheet.
- DE/EN Client Note.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.
