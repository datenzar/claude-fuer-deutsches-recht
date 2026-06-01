---
name: workflow-redteam-qualitygate
description: "Red-Team Qualitygate im Plugin phishing-vorfall-pruefer: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton."
---

# Red-Team Qualitygate

## Aufgabe
Dieser Workflow-Skill für `phishing-vorfall-pruefer` Red-Team Qualitygate im Plugin phishing-vorfall-pruefer: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

## Kaltstart
Wenn Material vorliegt, arbeite zuerst mit dem Material. Stelle nur Rückfragen, die für die nächste Weiche nötig sind:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Red-Team-Prüfpunkte Phishing-Vorfall
1. **Autorisierung:** Wurde die Zahlung tatsächlich nicht autorisiert (§ 675u BGB) oder autorisiert unter Täuschung (§ 675j BGB)? Diese Unterscheidung ist Weichenstellung für die gesamte Rechtsfolgenkette.
2. **Beweislast:** Bank trägt Beweislast für Autorisierung und ordnungsgemäße Aufzeichnung nach § 675w BGB — wurde das im Schreiben adressiert?
3. **Mitverschulden:** Wurde § 675v BGB (insb. grobe Fahrlässigkeit Kunde) sauber abgegrenzt? PIN-Weitergabe, Click auf Phishing-Link allein begründet nach BGH keine pauschale grobe Fahrlässigkeit (BGH XI ZR 91/14).
4. **Frist § 676b Abs. 2 BGB:** 13-Monats-Frist gegenüber Bank, sonst Ausschluss — gewahrt?
5. **Starke Kundenauthentifizierung:** § 1 Abs. 24 ZAG geprüft? PSD2 Art. 97; bei Verstoß § 675v Abs. 4 BGB: Kunde haftet **nicht**.
6. **Strafanzeige:** §§ 263a, 269, 202c StGB richtig benannt, ggf. § 202a (Ausspähen Daten), § 269 (Fälschung beweiserheblicher Daten).
7. **Halluzinations-Check:** Keine erfundenen BGH-Az.; verbreitete Az. sorgfältig prüfen (z. B. BGH XI ZR 91/14 - Phishing).

## Praxis-Tipp
Die häufigste Fehlbewertung: pauschale Annahme, der Kunde habe wegen Klick auf Phishing-Link "grobe Fahrlässigkeit" begangen. BGH 26.01.2016, XI ZR 91/14 differenziert: das bloße Folgen eines vortäuschend echten Hinweises trägt nicht zwingend grobe Fahrlässigkeit — entscheidend sind die konkreten Sicherheitsvorkehrungen der Bank und die Erkennbarkeit der Täuschung im Einzelfall.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.
