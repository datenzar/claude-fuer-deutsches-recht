---
name: patentrecht-epo-epue-einspruch-beschwerde-beschraenkung
description: "Vertieft EPA/EPO-Verfahren: Einspruch, Beschwerde, zentrale Beschränkung, Hilfsanträge, Verfahrenssprache, mündliche Verhandlung und Übergang zu UPC/nationaler Durchsetzung."
---

> Opencode-Port von `patentrecht/skills/epo-epue-einspruch-beschwerde-beschraenkung/SKILL.md`. Urspruenglicher Skill-Name: `epo-epue-einspruch-beschwerde-beschraenkung`.

# EPÜ: Einspruch, Beschwerde und Beschränkung

## Aufgabe

EPO-Post-Grant-Strategie zwischen Einspruch, Beschwerde, zentraler Beschränkung und nationaler/UPC-Durchsetzung.

## Kaltstart

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Frist und Beteiligtenstellung prüfen.**
2. **Grounds of opposition strukturiert erfassen.**
3. **Hilfsanträge nach Verteidigungsbreite ordnen.**
4. **Mündliche Verhandlung und technische Argumentationslinie vorbereiten.**
5. **Auswirkungen auf UPC/nationale Verfahren abgleichen.**


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

- Opposition/Appeal Roadmap.
- Auxiliary Request Tree.
- Oral Proceedings Script.
- Patent Family Impact Note.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.
