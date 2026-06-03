---
name: arzneimittelabgabe-verschreibungspflicht
description: "Arzneimittelabgabe Verschreibungspflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht."
---

# Arzneimittelabgabe Verschreibungspflicht

## Worum geht es konkret

Abgabe verschreibungspflichtiger Arzneimittel (Rx) durch öffentliche Apotheken. Geregelt sind: Verschreibungspflicht, formale Anforderungen an die ärztliche Verordnung (Papierrezept, Muster-16, E-Rezept), Identitätsprüfung, Plausibilitätsprüfung, Aushändigung, Beratung, Dokumentation. Abgrenzung zur OTC-Abgabe (apothekenpflichtig, nicht verschreibungspflichtig) und zur BtM-Abgabe (gesondertes Regime).

## Wann brauchen Sie diesen Skill / Kaltstart-Fragen

- Konflikt um eine zu Unrecht oder zu Recht durchgeführte Abgabe.
- Retax wegen Formalfehler auf dem Rezept.
- Strafrechtlicher Vorwurf: Abgabe ohne gültige Verschreibung (§ 96 Nr. 4, 13 AMG).
- Beanstandung durch Krankenkasse oder Aufsicht.

Eingaben:
- Rezept (Original oder E-Rezept-Token / Beleg).
- Abgabedokumentation (Zeit, abgebende Person, Charge).
- ggf. Vorgespräch, falls Patient nicht der Adressat war.
- Korrespondenz mit Arzt, Krankenkasse oder Behörde.

## Rechtlicher Rahmen

- **§ 48 AMG:** Verschreibungspflicht — definiert, wann ein Arzneimittel nur auf ärztliche Verordnung abgegeben werden darf.
- **AMVV (Arzneimittelverschreibungsverordnung):** Formerfordernisse, Geltungsdauer (drei Monate, BtM sieben Tage), Pflichtangaben.
- **§ 17 ApBetrO:** Abgabevorgang — Identitätskontrolle, Plausibilitätsprüfung, Beratung, Dokumentation.
- **§§ 12, 12a ApBetrO:** Beratungspflicht.
- **§ 21 AMG:** Zulassungspflicht.
- **§ 73 AMG:** Verbringungsverbot, Ausnahmen Einzelimport.
- **§ 96 AMG:** Strafvorschrift — Abgabe ohne ärztliche Verordnung.
- **§ 97 AMG:** Ordnungswidrigkeit.
- **SGB V § 360:** E-Rezept-Pflicht seit 01.01.2024.
- BGH/OLG, staend. Rspr. zu Heilmittelwerbung und Apothekenabgabe.

## Workflow / Schritt für Schritt

1. **Identität prüfen:** Bei E-Rezept Token/Code; bei Papierrezept Plausibilität der Verordnerangaben (Arzt, Praxis, BSNR/LANR).
2. **Formelle Prüfung:** Datum, Name Patient, Name Arzneimittel, Stärke, Menge, Dosierung, Unterschrift Arzt (bei Papier) / qualifizierte elektronische Signatur (E-Rezept).
3. **Geltungsdauer:** Drei Monate ab Ausstellung (§ 2 AMVV); GKV vier Wochen für Versorgung; BtM sieben Tage.
4. **Plausibilität:** Indikation, Dosierung, Interaktion, Kontraindikation. Bei Unklarheit Rücksprache Arzt.
5. **Substitutionsprüfung:** Aut-idem-Status, Rabattvertrag (siehe Skill `substitution-rabattvertrag-aut-idem`).
6. **Aushändigung mit Beratung:** Informationen zur Anwendung, Nebenwirkungen, Aufbewahrung.
7. **Dokumentation:** Im Apothekenwarenwirtschaftssystem; Rezept aufbewahren (drei Jahre, bei BtM zehn Jahre).
8. **Sonderfälle:** Notfallabgabe ohne Rezept (§ 4 AMVV) bei akutem Bedarf, max. kleinste Packung; Heimversorgung, Patientenstellvertretung.

## Trade-off-Matrix

| Situation | Sofortabgabe möglich? | Beleg | Risiko |
|---|---|---|---|
| Vollständiges E-Rezept | ja | Token + Quittung | gering |
| Papierrezept Muster-16 vollständig | ja | Original + Quittung | gering |
| Rezept ohne Unterschrift | nein | Rücksprache Arzt | hoch (Strafbarkeit) |
| Notfall ohne Rezept § 4 AMVV | ja, kleinste Packung | Notfallprotokoll | mittel, Dokumentation zwingend |
| Telefonische Verordnung | nein, aber Notfall-Regelung | schriftliche Bestätigung Arzt binnen einer Woche | mittel |
| Rezept abgelaufen | nein | Hinweis an Patient | gering |
| Faxrezept (BtM) | nein (Original zwingend) | — | hoch |

## Praxistipps

- Bei Plausibilitätszweifeln: nicht aus Eile abgeben, sondern Arzt anrufen — fehlerhafte Abgaben sind sowohl OWi/Strafbarkeitsrisiko als auch Patientenrisiko.
- Notfallabgabe immer mit schriftlicher Notiz: "Notfallabgabe nach § 4 AMVV, Indikation, Versorgungslücke, Folgerezept binnen [Frist] verlangt."
- E-Rezept: bei technischer Störung muss "Ersatzverfahren" (Papier oder Token-Print) genutzt werden — siehe Gematik-Vorgaben.
- Bei Substitution Aut-idem-Liste (§ 129 SGB V, Anlage) prüfen und Pharmazeutische Bedenken dokumentieren, falls trotz Rabattvertrag abgewichen wird.

## Mustertexte

### Dokumentation Notfallabgabe (Auszug)
"Notfallabgabe am [Datum, Uhrzeit] nach § 4 AMVV. Patient: [Name, Geb.-Datum]. Arzneimittel: [Name, Stärke, kleinste verfügbare Packung]. Indikation: [akut, z. B. Asthma-Anfall, Insulin]. Patient erklärt: [Rezept verloren / Arzt nicht erreichbar / Wochenende]. Folgerezept ist binnen sieben Tagen vorzulegen; entsprechende Aufforderung wurde übergeben (Anlage). Abgebender Apotheker: [Name]. Beratung: erfolgt."

### Hinweis an Patient bei abgelaufenem Rezept (Auszug)
"Sehr geehrte:r [Patient:in], das vorgelegte Rezept vom [Datum] ist nach § 2 AMVV abgelaufen (Geltungsdauer drei Monate). Wir können das Arzneimittel daher nicht zu Lasten der Krankenkasse oder als verschreibungspflichtige Abgabe abgeben. Bitte wenden Sie sich an die ausstellende Praxis für ein neues Rezept. Bei akutem Bedarf prüfen wir eine Notfallabgabe nach § 4 AMVV."

## Typische Fehler

- Abgabe trotz fehlender Unterschrift; eigene Anbringung der Unterschrift wäre Urkundenfälschung (§ 267 StGB).
- Notfallabgabe ohne Dokumentation des Notfallbezugs.
- Substitution gegen Patientenwunsch ohne Plausibilitätsdokumentation; Patient verklagt wegen Pharmazeutische Bedenken.
- E-Rezept-Token mehrfach eingelöst; Doppelabgabe wegen mangelhaftem Workflow.
- Faxrezept BtM angenommen — Original ist zwingend.

## Querverweise

- `btm-rezept-betaeubungsmittel-dokumentation` (BtM-Sonderrecht)
- `e-rezept-ti-gematik-apothekenprozess` (E-Rezept-Workflow)
- `substitution-rabattvertrag-aut-idem` (Austausch)
- `retaxationsabwehr-nullretax-risiko` (Formfehler-Folgen)
- `lieferengpaesse-austausch-dokumentation` (Austausch bei Nichtverfügbarkeit)
- `notfallkontrazeption-beratung` (Sonderfall OTC mit Beratungspflicht)

## Quellen Stand 06/2026

- AMG, AMVV — aktueller Stand zur Anwendung im Bundesgesetzblatt prüfen.
- ApBetrO §§ 17, 20.
- SGB V § 360 zur E-Rezept-Pflicht.
- BGH, staend. Rspr. zur Apothekenabgabe.
- Gematik-Vorgaben zum E-Rezept (vom Anwender zu verifizieren — Versionsstand).
