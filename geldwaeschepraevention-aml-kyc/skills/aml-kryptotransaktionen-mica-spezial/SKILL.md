---
name: aml-kryptotransaktionen-mica-spezial
description: "Spezialfall Kryptotransaktionen und MiCA / Travel Rule: Identifizierung Kryptowallets, Reisedatenuebermittlung, schwellenfreie Pflichten. Pruefraster fuer CASP."
---

# AML: Krypto Travel Rule

## Aufgabe
Spezialfall Kryptotransaktionen und MiCA / Travel Rule: Identifizierung Kryptowallets, Reisedatenuebermittlung, schwellenfreie Pflichten.

## Normfokus und Praxis (Krypto-AML)
- Rechtsgrundlagen: VO (EU) 2023/1113 Transfer of Funds Regulation (TFR) anwendbar seit 30.12.2024 — Travel-Rule-Pflichten für Krypto-Transfers; MiCAR-VO (EU) 2023/1114 Art. 60-83 für CASP-Pflichten; § 1 Abs. 28 KWG (Kryptowerte), § 2 Abs. 1 Nr. 17 GwG (Kryptowerteverwahrer als Verpflichteter), §§ 10 ff. GwG (KYC).
- TFR-Pflichten ohne Schwelle: jeder CASP-zu-CASP-Transfer muss Begleitinformationen (Name Originator, Wallet-Adresse, Geburtsdatum oder Adresse oder Nationale ID/Steuer-ID/Verifizierungs-Code; Begünstigter analog). Bei selbst-gehosteten Wallets (Unhosted) ab 1 000 EUR pro Transfer zusätzlich Identifizierung des Wallet-Inhabers und Eigentumsnachweis (Signaturnachweis oder Verifikation Ownership).
- CASP-Zulassung MiCAR (Art. 59 ff.): Verwahrung, Tausch Krypto-Fiat, Tausch Krypto-Krypto, Plattformbetrieb, Beratung, Portfolio-Management, Ordervermittlung. Übergangsphase national bis 30.12.2024 bzw. spätestens 1.7.2026 für Bestandsanbieter.
- AML-Spezifika: § 15 GwG verstärkte Sorgfaltspflicht bei anonymisierten Adressen, Mixer-Transfers, Privacy Coins; FATF-Empfehlung 15 zu Virtual Assets; BaFin-Auslegungs- und Anwendungshinweise zum GwG (Sonderteil Krypto) und Travel-Rule-Hinweise.
- Praktiker-Tipp: Chain-Analytics-Integration (Chainalysis, Elliptic) für Risk-Score und Sanctions-Screening; Self-hosted-Wallet-Policy klar definieren (Whitelist-Ansatz, Pre-Funded mit Ownership-Proof); bei "missing information" (TFR Art. 7) Hold-Process binnen 5 Werktagen Klärung mit Counterparty-CASP, sonst Ablehnung; Verdachtsmeldung an FIU nach § 43 GwG bei substantiellem Verdacht (Mixer ≥ 5 %, Darknet, Ransomware-Treffer).

## Kaltstart
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Skill erwartet folgenden inhaltlichen Aufbau im Output:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieser Skill gehoert zum Plugin `geldwaeschepraevention-aml-kyc`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Skill nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
