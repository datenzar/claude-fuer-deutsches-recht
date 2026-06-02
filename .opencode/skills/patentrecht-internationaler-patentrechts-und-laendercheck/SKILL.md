---
name: patentrecht-internationaler-patentrechts-und-laendercheck
description: "Routet grenzüberschreitende Patentmandate nach DE, EP, UPC, PCT, USA, Kanada, Japan, Schweiz, UK, Türkei und Israel; trennt Recherche, Anmeldung, Rechtsstand, Verletzung, Rechtsbestand und lokale Counsel-Fragen."
---

> Opencode-Port von `patentrecht/skills/internationaler-patentrechts-und-laendercheck/SKILL.md`. Urspruenglicher Skill-Name: `internationaler-patentrechts-und-laendercheck`.

# Internationaler Patent- und Ländercheck

## Aufgabe

Master-Routing für internationale Patentfragen: Territorien, Patentfamilie, Priorität, PCT/Nationalphasen, Validierungen, Einheitspatent, UPC-Opt-out, nationale Verletzungs- und Nichtigkeitsrisiken.

## Kaltstart

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Territorien und wirtschaftliche Märkte priorisieren.**
2. **Patentfamilie, Prioritäten, Anmelder- und Inhaberkette erfassen.**
3. **Pro Land trennen: Schutzfähigkeit, Rechtsstand, Verletzung, Rechtsbestand, Durchsetzung, Kosten.**
4. **Live-Register definieren: DPMA, EPO Register, Espacenet, WIPO PATENTSCOPE, USPTO, CIPO, J-PlatPat, Swissreg, UKIPO, TURKPATENT, ILPO.**
5. **Lokale Counsel-Fragen und Übersetzungsbedarf ausgeben.**


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

- Ländermatrix.
- Register-Rechercheplan.
- Local-Counsel-Fragenkatalog.
- Risikomemo DE/EN.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.
