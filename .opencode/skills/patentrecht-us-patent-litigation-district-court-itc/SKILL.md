---
name: patentrecht-us-patent-litigation-district-court-itc
description: "Bereitet US-Patentlitigation aus deutscher Sicht vor: complaint, answer, claim construction, discovery, Markman, damages, injunction, ITC exclusion order und Settlement-Druck."
---

> Opencode-Port von `patentrecht/skills/us-patent-litigation-district-court-itc/SKILL.md`. Urspruenglicher Skill-Name: `us-patent-litigation-district-court-itc`.

# US-Patentprozess: District Court und ITC

## Aufgabe

US-Durchsetzung und Verteidigung mit Discovery-, Claim-Construction- und Kostenrealität.

## Kaltstart

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Forum klären: District Court, ITC oder PTAB-Kombination.**
2. **Accused products, asserted claims und prior art in Litigation Matrix bringen.**
3. **Discovery-Belastung, hold notices und privilege issues markieren.**
4. **Claim construction/Markman-Begriffe aus deutscher Akte übersetzen.**
5. **Damages, injunction und Settlement-Fenster modellieren.**


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

- US Litigation Readiness Memo.
- Markman Term List.
- Discovery Risk Map.
- ITC/District Court Comparison.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.
