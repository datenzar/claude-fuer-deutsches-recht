---
name: patentrecht-patentprozess-negative-feststellungsklage
description: "Prüft negative Feststellungsklagen, Nichtverletzungserklärungen, Forum-Risiken, Abmahnreaktionen und grenzüberschreitende Koordination bei Patentstreitigkeiten."
---

> Opencode-Port von `patentrecht/skills/patentprozess-negative-feststellungsklage/SKILL.md`. Urspruenglicher Skill-Name: `patentprozess-negative-feststellungsklage`.

# Patentprozess: Negative Feststellung und Torpedo-Risiken

## Aufgabe

Aktive Verteidigung und Forum-Strategie bei drohender Patentklage.

## Kaltstart

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Rechtschutzbedürfnis und Drohlage erfassen.**
2. **Forum, Zuständigkeit und Territorialität prüfen.**
3. **Nichtverletzungsargumente in claim construction übersetzen.**
4. **Parallel zu Revocation/FTO/Schutzschrift planen.**
5. **Kommunikationsrisiken gegenüber Gegner und Kunden steuern.**


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

- DNI Strategy Memo.
- Forum Risk Map.
- Non-Infringement Chart.
- Client Communication Draft.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.
