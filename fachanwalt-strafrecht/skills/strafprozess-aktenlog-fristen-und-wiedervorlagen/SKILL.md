---
name: strafprozess-aktenlog-fristen-und-wiedervorlagen
description: "Aktenlog, Fristenbuch und Wiedervorlagen im Strafverfahren: erstellt aus Eingangspost, beA, EGVP, Verfügung, Ladung, Beschluss, Strafbefehl, Urteil und Aktennachlieferung eine robuste Fristen- und Aufgabensteuerung."
---

# Aktenlog, Fristen und Wiedervorlagen

## Zweck

Der Skill baut aus jeder Strafakte ein lebendes Register. Er ist besonders wichtig, wenn mehrere Verteidiger, Referendare, Sekretariat und Mandant parallel Informationen liefern.

## Eingang zuerst klassifizieren

| Eingang | Sofort prüfen |
| --- | --- |
| Strafbefehl | Einspruchsfrist § 410 StPO, Beschränkung möglich |
| Urteil | Berufung/Revision, Verkündung, Zustellung, Protokoll |
| Beschluss | einfache oder sofortige Beschwerde, Frist, Statthaftigkeit |
| Ladung | Anwesenheitspflicht, Entschuldigung, Vertretung, Terminskollision |
| Haftbefehl | dringender Tatverdacht, Haftgrund, Verhältnismäßigkeit, § 116 StPO |
| Aktennachlieferung | neue Beweise, neue Zeugen, neue Fristen, Reaktionsbedarf |
| Verfügung StA/Gericht | Stellungnahmefrist, Anhörung, Zuständigkeit |

## Fristen-Register

```text
Fristenregister

Fristart:
Norm:
Auslösendes Ereignis:
Zustellung/Verkündung:
Fristende:
Vorfrist:
Verantwortlich:
Erledigt:
Beleg:
```

## Wiedervorlagen

Lege mindestens an:

- Akteneinsicht nachhalten.
- Nachlieferungen prüfen.
- Mandantenrückmeldung.
- Staatsanwaltschaft/Gericht erinnern.
- Haftprüfung/Haftbeschwerde bewerten.
- HV-Vorbereitung starten.
- Rechtsmittelentscheidung nach Urteil.

## Fehlervermeidung

- Fristbeginn nicht raten: Zustellung, Verkündung, Bekanntgabe und Empfangsbekenntnis trennen.
- Nicht jedes Rechtsmittel ist sofortige Beschwerde; Statthaftigkeit prüfen.
- Revisionsbegründung nicht mit Revisionseinlegung verwechseln.
- Strafbefehl kann beschränkt angegriffen werden, aber Beschränkung muss strategisch sitzen.

## Output

- `Aktenlog`
- `Fristenregister`
- `Wiedervorlagenliste`
- `Rot-Liste heute`
- `Nächste Kanzleihandlung`
