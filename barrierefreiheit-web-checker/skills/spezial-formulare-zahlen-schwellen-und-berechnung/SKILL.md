---
name: spezial-formulare-zahlen-schwellen-und-berechnung
description: "Formulare: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output."
---

# Formulare: Zahlen, Schwellenwerte und Berechnung

## Aufgabe
Dieser Skill ist ein konkreter Fachbaustein für `barrierefreiheit-web-checker`. Ausgangspunkt ist: Web-Barrierefreiheits-Checker für BFSG, BFSGV, BITV 2.0, EN 301 549 und WCAG: Scope, Audit, Tastatur, Screenreader, Formulare, PDFs, Erklärung, Roadmap und Abnahme.

Er führt durch **Zahlen, Schwellenwerte und Berechnung** im Themenfeld **Formulare**. Ziel ist nicht ein abstrakter Lexikontext, sondern ein belastbares Arbeitsprodukt für die nächste anwaltliche, behördliche, gerichtliche, organisatorische oder mandantenbezogene Entscheidung.

## Kaltstart
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Barrierefreie Formulare** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Barrierefreie Formulare — Zahlen und Schwellen
- **WCAG 2.1 AA — relevante Erfolgskriterien für Formulare:**
  - **1.3.1 Info and Relationships (A):** Label semantisch verknüpft (`<label for>`).
  - **1.3.5 Identify Input Purpose (AA):** `autocomplete`-Attribut bei häufigen Feldern.
  - **2.4.6 Headings and Labels (AA):** beschreibend.
  - **3.3.1 Error Identification (A):** Fehler werden identifiziert und beschrieben.
  - **3.3.2 Labels or Instructions (A):** Hinweis bei Eingabefeldern.
  - **3.3.3 Error Suggestion (AA):** Vorschläge zur Korrektur.
  - **3.3.4 Error Prevention (Legal, Financial, Data) (AA):** Bestätigungsschritt, Korrekturmöglichkeit, Stornierung.
  - **4.1.3 Status Messages (AA):** dynamische Statusmeldungen für Screenreader.
- **Kontrast** (1.4.3): mindestens 4,5:1 für normalen Text, 3:1 für großen Text (>= 18pt oder 14pt fett).
- **Tastatur-Bedienbarkeit** (2.1.1): jede Funktion ohne Maus.
- **Captcha**: Audio-Alternative oder andere Modalität (4.1.2 i.V.m. 1.1.1).
- **Marktüberwachung BFSG:** Bußgeldrahmen bis 100.000 EUR (§ 37 BFSG).

## Praxis-Tipp
Bei Formularen ist die häufigste Barriere kein Tastatur-Mangel, sondern fehlende Verknüpfung Label–Input (1.3.1) und unklare Fehlermeldungen (3.3.1-3). Diese sind technisch trivial behebbar — aber im Audit-Bericht oft aufgeführt.

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
