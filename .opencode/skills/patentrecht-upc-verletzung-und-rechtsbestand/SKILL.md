---
name: patentrecht-upc-verletzung-und-rechtsbestand
description: "Prüft Einheitliches Patentgericht UPC: Verletzungsklage, Zentral-/Lokal-/Regionalkammer, Widerklage auf Nichtigerklärung, Opt-out, Einheitspatent und klassische europäische Patente."
---

> Opencode-Port von `patentrecht/skills/upc-verletzung-und-rechtsbestand/SKILL.md`. Urspruenglicher Skill-Name: `upc-verletzung-und-rechtsbestand`.

# UPC: Verletzung, Rechtsbestand und Zuständigkeit

## Aufgabe

UPC-Route für europäische Patentstreitigkeiten mit Zuständigkeit, Opt-out-Status, Verletzungs- und Rechtsbestandsangriffen.

## Kaltstart

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Patentart klären: Einheitspatent oder EP-Bündelpatent.**
2. **Opt-out und Übergangsregime live im UPC/EPO-Kontext prüfen.**
3. **Kammerwahl nach Sitz, Verletzungsort, Beklagtem und Patentklassifikation vorbereiten.**
4. **Verletzungsangriff, Revocation-Counterclaim und Bifurcation-Risiko abbilden.**
5. **Verfahrenssprache, CMS-Anforderungen und Beweismittelpaket planen.**


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

- UPC-Routenmemo.
- Claim/Invalidity Matrix.
- CMS-Aktionsliste.
- Mandantenampel.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.
