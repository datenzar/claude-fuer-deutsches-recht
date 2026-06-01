---
name: spezial-konformitaetsbewertung-red-team-und-qualitaetskontrolle
description: "Konformitaetsbewertung: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output."
---

# Konformitaetsbewertung: Red-Team und Qualitätskontrolle

## Aufgabe
Dieser Skill ist ein konkreter Fachbaustein für `ki-governance`. Ausgangspunkt ist: EU-KI-VO + DSGVO – Use-Case-Triage, KI-Inventar, AIA/DPIA, Vendor-Review, Drift-Monitoring der KI-Richtlinie.

Er führt durch **Red-Team und Qualitätskontrolle** im Themenfeld **Konformitaetsbewertung**. Ziel ist nicht ein abstrakter Lexikontext, sondern ein belastbares Arbeitsprodukt für die nächste anwaltliche, behördliche, gerichtliche, organisatorische oder mandantenbezogene Entscheidung.

## Kaltstart
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Konformitätsbewertung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Konformitätsbewertungsverfahren KI-VO (Art. 43)
- **Anhang VI — Interne Kontrolle**: Standardverfahren für die meisten Hochrisiko-KI-Systeme nach Anhang III, sofern harmonisierte Normen vollständig angewendet werden.
- **Anhang VII — Bewertung mit benannter Stelle**: für biometrische Identifikationssysteme nach Anhang III Nr. 1 lit. a, wenn keine harmonisierten Normen vollständig angewendet werden — oder freiwillig.
- **Konformitätsbewertung im Zuge anderer Unionsrechtsakte**: Wenn das KI-System Sicherheitsbauteil eines Produkts nach Anhang I ist (Medizinprodukt MDR, Maschine MaschinenVO etc.), wird die KI-VO-Bewertung in die bestehende Konformitätsbewertung integriert (Art. 43 Abs. 3).

## Pflichtdokumentation
- **Technische Dokumentation** Art. 11 i. V. m. Anhang IV: Systembeschreibung, Designspezifikationen, Trainingsdatenbeschreibung, Risikomanagement, Monitoring, Cybersicherheit.
- **Logging-Architektur** Art. 12: Aufzeichnungen über Lebenszyklus, Zweck-Erreichung, Identifikation problematischer Verhaltensweisen.
- **EU-Konformitätserklärung** Art. 47 i. V. m. Anhang V: 10 Jahre Aufbewahrung, Inhalt vorgeschrieben.
- **CE-Kennzeichnung** Art. 48 und **EU-Datenbankregistrierung** Art. 49 / 71 (Anhang VIII).

## Red-Team-Prüfungen
- **Robustheit**: adversariale Beispiele, Eingabestörungen, Edge Cases.
- **Bias / Fairness**: Tests über Untergruppen (Geschlecht, Alter, ethnische Herkunft, Region), Disparate-Impact-Analyse.
- **Cybersicherheit**: Prompt-Injection (bei LLM-basierten Systemen), Model Inversion, Membership Inference.
- **Datenleckage**: Aus Antworten rekonstruierbare Trainingsdaten (insb. bei Foundation Models).

## Qualitätskontrolle
- **Pre-Deployment**: vollständiger Konformitätsbewertungsbericht, abgenommen durch Compliance.
- **Pilotphase**: vorgesehene Stichprobe mit verstärktem Logging und Human Override.
- **Produktion**: Monitoring nach Art. 72 KI-VO (Marktbeobachtung durch Anbieter), Vorfallsmeldung nach Art. 73.
- **Substantielle Änderung**: bei Modellaktualisierung mit Performance-Verschiebung neue Bewertung nach Art. 43 Abs. 4.

## Trade-off
Interne Kontrolle (Anhang VI) ist günstiger und schneller, scheitert aber bei nicht-harmonisierten Aspekten. Beauftragung benannter Stelle (Anhang VII) gibt Rechtssicherheit, kostet Zeit (Wartezeit, Auditdurchläufe) und Geld; ist für Markteintritt sensibler Systeme aber empfehlenswert. Hybride Strategie: Anhang VI mit zusätzlichem freiwilligem externem Audit zur Vertrauensbildung.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
