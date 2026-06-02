---
name: patentrecht-uk-patentrecht-patents-court-ipec-ukipo
description: "Routet UK-Patentfragen: UKIPO Register, Patents Court, IPEC, opinions service, revocation, declaration of non-infringement, quia timet injunction und Kostenrisiko."
---

> Opencode-Port von `patentrecht/skills/uk-patentrecht-patents-court-ipec-ukipo/SKILL.md`. Urspruenglicher Skill-Name: `uk-patentrecht-patents-court-ipec-ukipo`.

# UK: UKIPO, Patents Court und IPEC

## Aufgabe

UK-Patentrecht nach Brexit mit eigenem Register, Gerichts- und Kostenregime.

## Kaltstart

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **UK-Registerstand und EP(UK)-Status prüfen.**
2. **Patents Court vs IPEC nach Streitwert/Komplexität abwägen.**
3. **Infringement, validity, revocation und DNI trennen.**
4. **UK Opinions Service als Vorstufe prüfen.**
5. **Costs, disclosure und injunction risk in Mandantenampel bringen.**


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

- UK Forum Memo.
- IPEC/Patents Court Comparison.
- UKIPO Opinion Checklist.
- DE/EN Client Brief.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.
