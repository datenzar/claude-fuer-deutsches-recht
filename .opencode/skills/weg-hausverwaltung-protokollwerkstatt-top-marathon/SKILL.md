---
name: weg-hausverwaltung-protokollwerkstatt-top-marathon
description: "Erstellt und prüft Protokolle für lange Eigentümerversammlungen mit vielen Tagesordnungspunkten. Trennt Aussprache, Antrag, Beschlusswortlaut, Abstimmung, Verkündung, Anlagen und Nacharbeit. Output: protokollfähige TOP-Struktur."
---

> Opencode-Port von `weg-hausverwaltung/skills/protokollwerkstatt-top-marathon/SKILL.md`. Urspruenglicher Skill-Name: `protokollwerkstatt-top-marathon`.

# Protokollwerkstatt für TOP-Marathons

Nutze diesen Skill, wenn eine Eigentümerversammlung viele Tagesordnungspunkte hat und das Protokoll später anfechtungsfest, verständlich und verwaltbar sein muss.

## Pro TOP erfassen

1. TOP-Nummer und Überschrift
2. Beschlussgegenstand
3. wesentliche Aussprache nur knapp
4. finaler Beschlusswortlaut
5. Abstimmungsergebnis
6. Verkündung
7. Anlagen
8. Nacharbeit: Auftrag, Frist, Verantwortliche, Kostenrahmen

## Protokollschema

```text
TOP [...]
Gegenstand:
[...]

Aussprache:
[nur wesentliche Punkte, keine Wortprotokoll-Falle]

Beschluss:
Die Gemeinschaft beschließt [...]

Abstimmung:
Ja: [...] MEA / Nein: [...] MEA / Enthaltungen: [...] MEA
Der Beschluss wurde [verkündet/nicht verkündet].

Nacharbeit:
Verwaltung: [...]
Beirat: [...]
Frist: [...]
```

## Qualitätsgate

- Beschlusswortlaut steht im Protokoll selbst oder eindeutig in Anlage.
- Abstimmung und Verkündung sind dokumentiert.
- Keine unklaren Aufträge wie "Verwalter soll sich kümmern".
- Kostenrahmen und Finanzierung sind sichtbar.
- Bei abgelehnten Beschlüssen wird ebenfalls klar protokolliert, was abgelehnt wurde.

## Schneller Arbeitsmodus

- Starte mit Objekt, Beschlussgegenstand, Einladung/Tagesordnung, Kostenverteilung, Stimmen, Eigentümerrollen und Fristen.
- Trenne Verwaltungspraxis, Beschlusskompetenz, ordnungsmäßige Verwaltung, bauliche Veraenderung, Kostenfolge und Anfechtungsrisiko.
- Bei Protokollen: Beschlusswortlaut, Abstimmungsergebnis, Verkündung, Anlagen und abweichende Auffassungen so aufnehmen, dass ein Gericht den Vorgang nachvollziehen kann.

## Ausgabeformat

- TOP/Beschlusskern.
- Formelle Risiken.
- Materielle Risiken.
- Vollzugsschritte der Verwaltung.
- Anfechtungs- oder Heilungsoptionen.
