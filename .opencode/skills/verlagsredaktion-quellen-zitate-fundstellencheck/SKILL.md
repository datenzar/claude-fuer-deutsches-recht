---
name: verlagsredaktion-quellen-zitate-fundstellencheck
description: "Prueft Quellen, Zitate, Randnummern, Fundstellen, Rechtsprechung und Literaturstatus mit strenger Regel gegen erfundene oder paywallige Blindzitate."
---

> Opencode-Port von `verlagsredaktion/skills/quellen-zitate-fundstellencheck/SKILL.md`. Urspruenglicher Skill-Name: `quellen-zitate-fundstellencheck`.

# Quellen-, Zitate- und Fundstellencheck

## Quellenregel

Keine Kommentar-, Handbuch-, Aufsatz- oder Datenbankfundstellen aus Modellwissen. Literatur nur aus Nutzerquelle, frei zugänglicher Quelle oder lizenziertem Live-Zugriff. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle.

## Prüfung

1. Jede Fundstelle extrahieren.
2. Quelle klassifizieren.
3. Existenzstatus markieren.
4. Pinpoint prüfen.
5. Hausstil anwenden.
6. Unsichere Stellen nicht verbessern, sondern markieren.

## Output

- Fundstellenliste.
- Ampel.
- Korrekturvorschläge.
- `[Quelle zu prüfen]`-Liste.
- Rechtsprechungs-Rechercheaufträge.

## Schneller Arbeitsmodus

- Erst klaeren: Produktart, Adressat, Verwendungsort, Frist und Freigabeperson. Wenn Angaben fehlen, mit einer kurzen Arbeitsannahme starten und offene Punkte sichtbar markieren.
- Trenne belegte Angaben aus Manuskript/Metadaten von redaktionellen Vorschlaegen. Keine Autor:innenzitate, Verkaufszahlen, Rechte oder Vergleichstitel erfinden.
- Liefere zuerst eine nutzbare Arbeitsfassung, danach eine kurze Pruefliste fuer Herstellung, Marketing, Vertrieb, Justiziariat oder Autor:innen.

## Qualitaetsgate

- Ist der Text fuer den konkreten Kanal verwendbar?
- Sind Rechte, Quellen, Namen, Titel, Preis, Termine und Freigaben als belegt oder offen markiert?
- Gibt es genau die naechsten Schritte mit Owner, Frist und Eskalation?
