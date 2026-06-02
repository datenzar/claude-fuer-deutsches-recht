---
name: patentrecht-patentanmeldung-anspruchsentwurf
description: "Bereitet Patentansprüche vor: Anspruch 1, Unteransprüche, Alternativausführungen, Vorrichtung/Verfahren/System/Computerprogramm, Stütze in Beschreibung und Rückfragen zur Anspruchsbreite."
---

> Opencode-Port von `patentrecht/skills/patentanmeldung-anspruchsentwurf/SKILL.md`. Urspruenglicher Skill-Name: `patentanmeldung-anspruchsentwurf`.

# Patentanmeldung — Anspruchsentwurf

## Arbeitsmodus

Der Skill entwirft keine endgültige Patentanmeldung, sondern einen belastbaren Arbeitsentwurf für Patentanwältinnen und Patentabteilungen.

## Schritte

1. **Erfindungskern formulieren:** ein Satz mit technischer Aufgabe, Lösung und Wirkung.
2. **Anspruchskategorie wählen:** Vorrichtung, Verfahren, Verwendung, System, computerimplementiertes Verfahren, Datenträger, Produkt-by-Process nur vorsichtig.
3. **Merkmale sortieren:** zwingend, bevorzugt, optional, Ausführungsbeispiel, bloßer Vorteil.
4. **Breite prüfen:** Anspruch so breit wie vertretbar; keine unnötige Einengung durch konkrete Maße, Materialien oder Herstellerteile.
5. **Unteransprüche bauen:** Varianten, fallback positions, kommerzielle Kernfeatures, Schutz gegen Design-around.
6. **Beschreibung koppeln:** jedes Anspruchsmerkmal braucht Offenbarungsstütze.
7. **Recherchebedarf markieren:** unbekannte Merkmale und voraussichtlich kritischer Stand der Technik.

## Outputstruktur

```text
Anspruch 1 (Arbeitsentwurf)
[Kategorie] umfassend:
a) ...
b) ...
dadurch gekennzeichnet, dass ...

Unteransprüche
2. ...
3. ...

Offene Punkte
- [noch zu klären: ...]

Risiken der Anspruchsfassung
- zu eng: ...
- zu breit: ...
- fehlende Stütze: ...
```

## Red Flags

- Claim liest sich wie Produktwerbung statt technische Lehre.
- Vorteil steht im Anspruch, aber kein technisches Merkmal.
- Nur ein Ausführungsbeispiel vorhanden, aber sehr breiter Anspruch gewünscht.
- Software/AI-Feature ohne technischen Beitrag.
- Vorveröffentlichung oder Verkauf vor Anmeldung ungeklärt.
