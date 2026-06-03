---
name: kalender-reminder-und-fristenmanagement
description: "Kalender- und Reminder-Skill für Betreuungen: legt Berichtstermine, Vermögensverzeichnis, Rechnungslegung, Gerichtstermine, Bescheidfristen, Arzt-/Pflege-/Heimtermine, Genehmigungsentscheidungen und wiederkehrende Zahlungen als klare Erinnerungsliste an."
---

# Kalender, Reminder und Fristenmanagement

## Zweck

Dieser Skill sorgt dafür, dass der Betreuer nichts Wichtiges vergisst: nicht die gerichtlichen Berichte, nicht die Bescheidfristen, nicht den Heimvertrag, nicht die Pflegekasse, nicht die nächste Rücksprache mit der betreuten Person.

## Fristenquellen

Prüfe:

- Betreuungsbeschluss und gerichtliche Schreiben,
- Berichtspflicht nach § 1863 BGB,
- Vermögensverzeichnis nach § 1835 BGB,
- Rechnungslegung/Vermögensübersicht bei Vermögenssorge,
- sozialrechtliche Bescheide mit Widerspruchsfrist,
- Miet-/Heim-/Kündigungsfristen,
- Zahlungsziele und Mahnungen,
- gerichtliche Genehmigungsfristen und Anhörungstermine,
- Arzt-, Pflege-, Reha- und Entlassmanagement-Termine.

## Reminder-Logik

Erzeuge drei Ebenen:

| Ebene | Zweck | Beispiel |
| --- | --- | --- |
| Sofort | Frist droht oder Schaden wahrscheinlich | Widerspruch bis 14.06.2026 |
| Vorbereitung | Unterlagen müssen rechtzeitig gesammelt werden | Jahresbericht 6 Wochen vor Fälligkeit starten |
| Routine | Betreuung gut führen | monatlicher Konto- und Besuchscheck |

## Standard-Reminder

- Monatlich: Kontakt zur betreuten Person dokumentieren.
- Monatlich bei Vermögenssorge: Kontoauszüge prüfen und Belege sichern.
- Quartalsweise: Wohn-/Pflege-/Gesundheitslage prüfen.
- Halbjährlich: Aufgabenkreise noch erforderlich? Weniger Betreuung möglich?
- Jährlich: Jahresbericht vorbereiten; bei Vermögenssorge Vermögensübersicht/Rechnungslegung prüfen.
- Bei jedem neuen Bescheid: Rechtsbehelfsfrist sofort notieren.

## Ausgabeformat

```text
Fristen- und Erinnerungsliste

Rot:
- [Datum] [Aufgabe] [Folge bei Versäumnis] [zuständige Stelle]

Gelb:
- [Datum] [Vorbereitung] [fehlende Unterlagen]

Routine:
- [Rhythmus] [Aufgabe] [Beleg/Notiz]
```

## Arbeitsregel

Wenn ein echter Kalenderzugriff vorhanden ist, nur nach ausdrücklichem Auftrag Termine anlegen. Sonst eine exportierbare Liste im Klartext liefern.
