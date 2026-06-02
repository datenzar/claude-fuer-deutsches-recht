---
name: kuendigungsbutton-312k-bgb
description: "Kündigungsbutton § 312k BGB: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: BGB §§ 312 ff., 355 und 327 ff., 434 ff.; EGBGB Informationspflichten; PAngV; UWG; DDG; DSA; DSGVO; BFSG; GPSR; ElektroG/VerpackG/BattG."
---

# Kündigungsbutton § 312k BGB

## Worum geht es konkret

§ 312k BGB verpflichtet Unternehmer, die im elektronischen Geschäftsverkehr Verbraucherverträge über entgeltliche Leistungen in Form eines Dauerschuldverhältnisses anbieten, einen Kündigungsbutton bereitzustellen. Gilt seit 1. Juli 2022. Bei Verstoß: keine wirksame Bindung an die Mindestvertragslaufzeit, jederzeitige Kündigungsmöglichkeit und Unterlassungsanspruch nach UWG und UKlaG. Der Skill ordnet Anwendungsbereich, technische Anforderungen, Risiken und Mustertexte.

## Wann brauchen Sie diesen Skill / Kaltstart-Fragen

- Welcher Vertragstyp (Streaming-Abo, Datingplattform, Fitnessstudio-Online, Telekommunikation)?
- Ist der Vertragsschluss elektronisch möglich? Wenn ja: Kündigung auch?
- Wer ist Vertragspartner – Verbraucher oder Unternehmer (B2B)?
- Aktuelle Buttongestaltung: vorhanden, sichtbar, beschriftet?
- Bestätigungsseite vorhanden, mit unmittelbarer Bestätigungsmail?
- Schon Abmahnung erhalten? Welcher Verband?

## Rechtlicher Rahmen

- § 312k I BGB: Pflicht zur Bereitstellung eines Kündigungsbuttons bei online geschlossenen Verbraucherverträgen über entgeltliche Dauerschuldverhältnisse.
- § 312k II BGB: Gestaltungsanforderungen – Schaltfläche "Verträge hier kündigen" oder gleichwertig, gut lesbar.
- § 312k III BGB: Bestätigungsseite – Identitätsangabe, Vertragsangabe, Kündigungsart (ordentlich/außerordentlich), Datum/Uhrzeit, Bestätigungs-Button.
- § 312k IV BGB: Sofortige elektronische Bestätigung mit Inhalt, Zugangszeitpunkt.
- § 312k V BGB: Rechtsfolge bei Verstoß – Verbraucher kann jederzeit und ohne Einhaltung der Kündigungsfrist kündigen.
- § 312k VI BGB: Ausnahmen (Verträge die nur schriftlich gekündigt werden können nach gesetzlicher Sonderregelung).
- UWG § 5a, § 3a: Marktverhaltensregel – Verstoß als unlautere geschäftliche Handlung.
- UKlaG: Unterlassungsklage Verbraucherverbände.
- EU-Schnittstellen: Verbraucherrechte-RL 2011/83 (Art. 8 Klarheit Bestellprozess) – nicht deckungsgleich, aber Hintergrund.

## Workflow / Schritt für Schritt

1. **Anwendungsbereich prüfen.** Verbraucher? Online-Abschluss möglich? Entgeltliche Dauerschuldverhältnis?
2. **Buttontext prüfen.** "Verträge hier kündigen" oder gleichwertig, gut lesbar, ohne weitere Login-Hürde direkt nach Klick erreichbar.
3. **Bestätigungsseite prüfen.** Vollständige Angaben: Identifizierung des Vertrags, Art der Kündigung, Datum/Uhrzeit, eindeutiger Bestätigungs-Button.
4. **Bestätigung per E-Mail.** Unmittelbar nach Klick, mit Zeitstempel.
5. **Bestandskunden.** Pflicht gilt auch für Altverträge, soweit Vertrag online abgeschlossen wurde.
6. **Login-Hürde unzulässig.** OLG Düsseldorf und andere haben Login-Pflicht zwischen Button und Bestätigung als unzulässig eingestuft.
7. **Beweissicherung.** Screenshots, Versionierung der Seite, Log-Files.
8. **Abmahnung.** Modifizierte Unterlassungserklärung mit Vertragsstrafenklausel.

## Trade-off-Matrix

| Konstellation | Strategie |
| --- | --- |
| Kein Button vorhanden | Sofortige Implementierung; Risiko Abmahnung |
| Button mit Login-Pflicht | Login entfernen; nur Identifikationsdaten abfragen |
| B2B-Abo | § 312k nicht anwendbar |
| Hybrid B2C/B2B | Pflicht für B2C-Bereich; Schaltflächentexte differenzieren |
| Bestätigungsmail fehlt | sofort einrichten |

## Praxistipps

- Buttontext muss eindeutig sein. "Vertrag kündigen" reicht; "Abomanagement" reicht nicht.
- Bestätigungsseite darf weitere Angaben verlangen – aber nur soweit zur Identifizierung erforderlich (Name, Kundennummer, E-Mail).
- Aufgabenverteilung zwischen Frontend und Backend: Sofortige Bestätigungsmail muss auch bei Systemstörungen funktionieren – Monitoring.
- Bestandskunden: § 312k findet auch auf Altverträge Anwendung, wenn sie online geschlossen wurden – kein Bestandsschutz.
- Abmahnungen erfolgen häufig durch Verbraucherzentralen (NRW, Bundesverband VZBV).

## Mustertexte

**Kompletter Buttontext:**
"Verträge hier kündigen" – einzeilig, gut lesbar, ständig auf der Website verfügbar.

**Bestätigungsseite (Pflichtfelder):**
- Identifizierung: Name, Anschrift oder Kundennummer, E-Mail.
- Vertragsbezeichnung und -nummer.
- Kündigungsart: ordentlich zum [Datum] / außerordentlich zum [Datum].
- Kündigungsgrund (bei außerordentlich).
- Datum/Uhrzeit der Abgabe.
- Bestätigungs-Button: "Jetzt kündigen".

**Bestätigungsmail (Inhalt):**
"Ihre Kündigung ist bei uns am [Datum, Uhrzeit] eingegangen. Vertrag: [...]. Wirksamkeit: [Datum]. Sie erhalten diese E-Mail zur Bestätigung des Eingangs nach § 312k IV BGB."

**Modifizierte Unterlassungserklärung Eingangsformat:**
"Wir verpflichten uns, es zu unterlassen, im geschäftlichen Verkehr im elektronischen Vertragsschluss mit Verbrauchern Dauerschuldverhältnisse anzubieten, ohne den nach § 312k BGB vorgeschriebenen Kündigungsbutton bereitzustellen. Vertragsstrafe für jeden Fall der Zuwiderhandlung: [Betrag] EUR, deren Höhe in das billige Ermessen des Gläubigers gestellt wird, im Streitfall vom zuständigen Gericht zu überprüfen."

## Typische Fehler

- Login-Pflicht zwischen Button und Bestätigung.
- Buttontext irreführend ("Abo verwalten" statt "Vertrag kündigen").
- Bestätigungsmail erst Stunden später.
- Bestandskunden ausgeschlossen.
- Mobile-Ansicht: Button nicht sichtbar.

## Querverweise

- digitale-inhalte-abo-kuendigungsbutton
- widerrufsrecht-verbraucher-355-312g-bgb
- button-loesung-312j-bgb
- abmahnung-uwg-unterlassungserklaerung
- shop-check-checkout-widerruf-impressum
- rechtstexte-versionierung-deployment

## Quellen Stand 06/2026

- § 312k BGB – Volltext gesetze-im-internet.de.
- Gesetzesbegründung BT-Drs. 19/26915 – publik bei dipbt.bundestag.de.
- OLG Düsseldorf zur Login-Pflicht – Rechtsprechung verifizieren (Az. in OLG-Datenbank).
- UWG §§ 3a, 5a; UKlaG – Volltexte gesetze-im-internet.de.
- Verbraucherzentrale Bundesverband (VZBV) – Abmahnpraxis und Musterklagen.
- Verbraucherrechte-RL 2011/83/EU – EUR-Lex.
