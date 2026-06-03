---
name: substitution-rabattvertrag-aut-idem
description: "Substitution Rabattvertrag Aut-idem: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht."
---

# Substitution Rabattvertrag Aut-idem

## Worum geht es konkret

Beim Abgabevorgang an GKV-Versicherte ist die Apotheke verpflichtet, ein wirkstoffgleiches Arzneimittel ("aut idem") des Rabattpartners der Krankenkasse abzugeben, sofern der Arzt das nicht ausgeschlossen hat (Aut-idem-Kreuz). Bei Abweichungen drohen Retax bis zur Vollabsetzung ("Null-Retax"). Pharmazeutische Bedenken erlauben eine Ausnahme; sie müssen jedoch im Einzelfall, schriftlich und nachvollziehbar dokumentiert werden.

## Wann brauchen Sie diesen Skill / Kaltstart-Fragen

- Substitution kollidiert mit Patientenwunsch oder Verträglichkeit.
- Krankenkasse retaxiert wegen abweichender Abgabe.
- Patient verlangt Markenprodukt trotz Rabattvertrag.
- Aut-idem-Kreuz fehlt, aber Patient ist auf bestimmtes Präparat eingestellt.
- Abgabe von Originalpräparat trotz Generikum-Rabattvertrag — Dokumentation für Aufsicht.

Eingaben:
- Rezept / E-Rezept-Token.
- Aktueller Aut-idem-Status, Rabattvertragsliste der Krankenkasse.
- Patientenanamnese (Allergie, Unverträglichkeit, Compliance-Risiko).
- Vorherige Substitutionen, Beratungsprotokolle.

## Rechtlicher Rahmen

- **§ 129 SGB V:** Rahmenvertrag, Aut-idem-Substitution, Rabattvertragsregeln.
- **Anlage 1 Rahmenvertrag § 129 SGB V** (vom Anwender zu verifizieren — Vereinbarung GKV-Spitzenverband / DAV): Substitutionsausschlussliste.
- **§ 73 Abs. 5 SGB V:** Wirtschaftlichkeitsgebot.
- **§ 17 Abs. 5 ApBetrO:** Abgabe nach pharmazeutischer Sorgfalt.
- **§ 12 ApBetrO:** Beratungspflicht.
- BSG und LSG, staend. Rspr. zu Retaxation und Pharmazeutische Bedenken.
- BGH, staend. Rspr. zur Substitution.

## Workflow / Schritt für Schritt

1. **Aut-idem-Kreuz prüfen:** Wenn gesetzt — keine Substitution (Apotheker:in darf nicht abweichen).
2. **Wirkstoff, Stärke, Packungsgrösse, Indikationsbereich, Galenik** identifizieren.
3. **Rabattvertrag prüfen:** Welches Präparat hat die Krankenkasse mit welchem Hersteller? Datenstand aktuell?
4. **Substitutionsausschlussliste:** Bestimmte Wirkstoffe sind grundsätzlich nicht austauschbar (Liste vom Anwender zu prüfen — Anlage 1 Rahmenvertrag).
5. **Pharmazeutische Bedenken:** Liegt eine Indikation gegen Substitution vor (z. B. Allergie auf Hilfsstoff, fehlende Anwendererfahrung, Compliance-Risiko bei älteren Patienten)? Dann Bedenken schriftlich dokumentieren.
6. **Beratung:** Patient über Substitution informieren, Aufklärung über gleiche Wirkstoffe.
7. **Abgabe:** Bei dokumentierten Bedenken Originalpräparat abgeben; Kennzeichnung auf Rezept "Pharmazeutische Bedenken".
8. **Krankenkasse-Kommunikation:** Bei Retax sofort Widerspruch einlegen, Bedenken-Dokumentation beifügen.

## Trade-off-Matrix

| Situation | Pflicht | Ausnahme | Risiko |
|---|---|---|---|
| Aut-idem Kreuz gesetzt | keine Substitution | — | gering |
| Rabattvertrag, Patient akzeptiert | substituieren | — | gering |
| Rabattvertrag, Patient lehnt ab | substituieren, sofern keine Bedenken | Pharmazeutische Bedenken | Retax bei mangelnder Dokumentation |
| Wirkstoff auf Ausschlussliste | nicht austauschen | — | bei Verstoss Retax |
| Patient älter, neu auf Substitut | Substitut, aber Aufklärung | bei begründeter Compliance-Sorge: Bedenken | Vollabsetzung möglich |
| Allergie gegen Hilfsstoff im Substitut | Originalpräparat | Bedenken-Dokumentation | gering bei guter Doku |

## Praxistipps

- Pharmazeutische Bedenken müssen einzelfallbezogen sein — Pauschalformeln wie "Patient ist alt" reichen nicht. Indikation, Hilfsstoff-Allergie, Compliance-Risiko, Galenik-Unterschied (z. B. Inhalator-Typ) — alles konkret.
- Substitutionsausschlussliste stets aktuell halten — DAV-Mitgliedsapotheken erhalten regelmässig Updates.
- Substitution-Software (SaaS) prüft tagesaktuell Rabattverträge; manuelle Kontrolle nur zur Validierung.
- Patient bewusst zu Substitution erziehen — schriftliche Patienteninformation in Wartebereich.
- Bei Null-Retax: Frist Widerspruch (vier Wochen, vom Anwender zu verifizieren) einhalten; sonst entgangener Erlös endgültig.

## Mustertexte

### Pharmazeutische Bedenken-Vermerk (Auszug)
"Patient:in [Initialen, Geb.-Datum], Rezept vom [Datum] für [Wirkstoff, Stärke]. Rabattvertrag mit Krankenkasse [Name] sieht [Generikum X] vor. Bedenken: [a) Patient ist seit [Zeit] auf [Originalpräparat] eingestellt; b) bekannte Hilfsstoff-Unverträglichkeit gegen [Hilfsstoff]; c) Galenik-Wechsel würde Compliance gefährden, vgl. § 17 Abs. 5 ApBetrO]. Beratung am [Datum] durchgeführt. Abgabe: [Originalpräparat]. Aufkleber 'Pharmazeutische Bedenken' auf Rezept angebracht."

### Widerspruch gegen Retax (Auszug)
"Mit Schreiben vom [Datum] retaxieren Sie die Abgabe vom [Datum] in Höhe von [Betrag]. Hiergegen legen wir frist- und formgerecht Widerspruch ein. Die Abgabe erfolgte abweichend vom Rabattvertrag aufgrund pharmazeutischer Bedenken (Hilfsstoff-Unverträglichkeit, dokumentiert in Anlage [Nr.]). § 17 Abs. 5 ApBetrO und § 129 Abs. 1a SGB V berechtigen zur Abweichung. Wir bitten um Stornierung der Retax."

## Typische Fehler

- Substitution ohne Aut-idem-Prüfung — sofortige Retax.
- Pauschale Pharmazeutische Bedenken ("Patient will Original") — wird als nicht ausreichend abgelehnt.
- Substitutionsausschlussliste ignoriert; Substitution eines nicht austauschbaren Wirkstoffs — Vollabsetzung.
- Bedenken nicht auf Rezept gekennzeichnet — Krankenkasse erkennt nicht, dass Apotheke begründet abweicht.
- Widerspruchsfrist versäumt — entgangener Erlös wird endgültig.

## Querverweise

- `arzneimittelabgabe-verschreibungspflicht` (allgemeiner Abgabevorgang)
- `retaxationsabwehr-nullretax-risiko` (Retax-Abwehr)
- `lieferengpaesse-austausch-dokumentation` (Austausch bei Lieferengpass)
- `rechnung-retaxation-krankenkasse` (Krankenkassen-Rechnung)
- `e-rezept-ti-gematik-apothekenprozess` (E-Rezept-Substitution)
- `schiedsstellen-krankenkassen-apotheke` (Streitschlichtung)

## Quellen Stand 06/2026

- SGB V §§ 129, 73; ApBetrO § 17.
- Rahmenvertrag § 129 SGB V mit Anlagen (vom Anwender zu verifizieren — Anlage 1 Substitutionsausschlussliste).
- BSG, staend. Rspr. zu pharmazeutischen Bedenken und Retaxation.
- DAV-Mitgliederinformationen / aktuelle Rabattvertragslisten (vom Anwender zu verifizieren).
- ABDA-Leitlinien zur Substitution.
