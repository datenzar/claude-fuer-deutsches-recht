---
name: patentrecht-israel-patentrecht-ilpo-opposition-revocation
description: "Prüft israelische Patentfragen: ILPO-Register, Examination, Opposition vor Erteilung, Revocation/Cancellation, Verletzung, einstweilige Maßnahmen und technologiebezogene Counsel-Fragen."
---

> Opencode-Port von `patentrecht/skills/israel-patentrecht-ilpo-opposition-revocation/SKILL.md`. Urspruenglicher Skill-Name: `israel-patentrecht-ilpo-opposition-revocation`.

# Israel: ILPO, Opposition und Revocation

## Aufgabe

Israelisches Patentrecht mit starker High-Tech-/MedTech-Relevanz und Register-/Opposition-Fokus.

## Kaltstart

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **ILPO-Status, Priorität und Patentfamilie prüfen.**
2. **Pre-grant opposition und post-grant revocation/cancellation unterscheiden.**
3. **Verletzungs- und Eilrechtsschutzroute über lokale Counsel vorbereiten.**
4. **Technische Belege, Produktvergleich und Geschäftsgeheimnisse sichern.**
5. **DE/EN Counsel Brief und Mandantenampel erstellen.**


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

- Israel Patent Status Note.
- Opposition/Revocation Matrix.
- Infringement Evidence List.
- Local Counsel Brief.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.
