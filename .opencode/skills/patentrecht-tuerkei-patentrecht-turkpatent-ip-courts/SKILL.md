---
name: patentrecht-tuerkei-patentrecht-turkpatent-ip-courts
description: "Orientiert in türkischen Patentfragen: TURKPATENT-Register, nationale Phase/EP-Validierung, Opposition/Invalidity, Verletzung, einstweilige Maßnahmen, Zoll und lokale Counsel-Schnittstelle."
---

> Opencode-Port von `patentrecht/skills/tuerkei-patentrecht-turkpatent-ip-courts/SKILL.md`. Urspruenglicher Skill-Name: `tuerkei-patentrecht-turkpatent-ip-courts`.

# Türkei: TURKPATENT und IP-Gerichte

## Aufgabe

Türkische Patentstrategie mit Register-, Validierungs-, Verletzungs- und Grenzbeschlagnahmefragen.

## Kaltstart

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **TURKPATENT-/EP-Validierungsstatus prüfen lassen.**
2. **Fristen, Übersetzungen und Jahresgebühren abfragen.**
3. **Invalidity/Opposition und Verletzungsverfahren trennen.**
4. **PI, Zollmaßnahmen und Beweissicherung als Eiloptionen markieren.**
5. **Lokale Counsel-Anfrage mit Produkt- und Patentunterlagen bauen.**


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

- Turkey Patent Checklist.
- Customs/PI Option Note.
- Invalidity/Infringement Matrix.
- Counsel Questions.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.
