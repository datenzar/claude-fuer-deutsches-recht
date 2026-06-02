---
name: patentrecht-japan-patentrecht-jpo-ip-high-court
description: "Strukturiert japanische Patentfragen: J-PlatPat, JPO-Prüfung, Opposition/Invalidation Trial, Korrektur, IP High Court, Übersetzung und lokale Vertretung."
---

> Opencode-Port von `patentrecht/skills/japan-patentrecht-jpo-ip-high-court/SKILL.md`. Urspruenglicher Skill-Name: `japan-patentrecht-jpo-ip-high-court`.

# Japan: JPO und IP High Court

## Aufgabe

Japan-spezifische Prosecution- und Rechtsbestandsroute mit Übersetzungs- und Vertreterbedarf.

## Kaltstart

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **J-PlatPat/JPO-Daten mit Patentfamilie abgleichen.**
2. **Anspruchs- und Übersetzungsrisiken markieren.**
3. **Opposition, Invalidation Trial und Correction Trial trennen.**
4. **IP High Court/Verletzungsgericht nur als lokale Counsel Route behandeln.**
5. **Japanisches Claim Chart für Counsel vorbereiten.**


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

- Japan Patent Status Note.
- JPO Trial Decision Tree.
- Translation Risk List.
- Local Counsel Bundle.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.
