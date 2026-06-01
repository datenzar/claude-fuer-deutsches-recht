---
name: workflow-output-waehlen
description: "Output wählen im Plugin insolvenzrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung."
---

# Output wählen

## Aufgabe
Dieser Workflow-Skill für `insolvenzrecht` Output wählen im Plugin insolvenzrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Output-Typen im Insolvenzrecht
- **Insolvenzantrag (§ 13 InsO Eigenantrag / § 14 InsO Gläubigerantrag):**
  - Vordrucke der Justiz-Portale verwenden; bei juristischen Personen verpflichtend mit Forderungsverzeichnis, Vermögensaufstellung, Gläubigerliste.
  - Bei Eigenantrag mit Eigenverwaltung § 270a InsO: Eigenverwaltungsplanung, IDW S2-Bescheinigung.
  - Bei Schutzschirm § 270d InsO: Bescheinigung Sachverständiger über drohende ZU oder Überschuldung.
- **Memo (Gutachtenstil) intern:**
  - Sachverhalt, Frage(n), Kurzantwort, rechtliche Bewertung, Gesamtergebnis, Risiken, Quellen — siehe CLAUDE.md.
  - Geeignet für: Insolvenzreife-Prüfung, Geschäftsführerhaftung, Anfechtungspotenzial.
- **Mandantenbrief:**
  - Anrede, Bezug, Sachstand, Empfehlung, nächste Schritte mit Frist, Kostenhinweis, Unterschrift.
  - Heikel: § 15a InsO Antragspflicht — schriftliche Belehrung, dokumentierte Übergabe.
- **Schriftsatz (Urteilsstil):**
  - Anfechtungsklage §§ 129 ff. InsO durch Verwalter.
  - Bestreitenswiderspruch § 178 InsO.
  - Feststellungsklage § 180 InsO durch Anmelder.
- **Tabelle / Matrix:**
  - Forderungstabelle (Anmeldung + Prüfung).
  - Anfechtungsmatrix (Rechtshandlung, Datum, Anfechtungsgrund §§ 130 ff. InsO, Erfolgsaussicht).
  - Liquiditätstabelle 13-Wochen.
- **Checkliste:**
  - Erstmaßnahmen Verwalter (§ 22 InsO).
  - Antragsunterlagen-Checkliste.
  - Berichtstermin-Vorbereitung § 156 InsO.
- **Beschluss-Entwurf (Verwalter):**
  - Erfüllungswahl § 103 InsO, Kündigung § 113 InsO, Sondervergütung § 4 InsVV.

## Output-Wahl je Mandanten-Rolle
- **Geschäftsführer:** Mandantenbrief + Memo zur Haftungsfrage.
- **Verwalter:** Tabelle, Schriftsatz, Berichtsmemo für Berichtstermin.
- **Gläubiger:** Forderungsanmeldung, ggf. Bestreitenswiderspruch, ggf. Feststellungsklage.
- **Investor / Erwerber:** Memo zur übertragenden Sanierung, Due-Diligence-Tabelle.
