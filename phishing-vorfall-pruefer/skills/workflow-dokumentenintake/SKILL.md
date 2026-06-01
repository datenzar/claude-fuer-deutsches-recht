---
name: workflow-dokumentenintake
description: "Dokumentenintake im Plugin phishing-vorfall-pruefer: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte."
---

# Dokumentenintake

## Aufgabe
Dieser Workflow-Skill für `phishing-vorfall-pruefer` Dokumentenintake im Plugin phishing-vorfall-pruefer: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte.. Er ist dazu da, den Nutzer schneller und sicherer in die richtige Bearbeitung zu führen.

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

## Typische Dokumentenarten Phishing-Vorfall
- **Original-Phishing-Mail / SMS** als .eml-Datei (Header sichern!) bzw. Smishing-Screenshot mit Absenderkennung.
- **Kontoauszug / Umsatzaufstellung** mit konkretem Belastungsdatum und Betrag.
- **Online-Banking-Logging-Protokoll** (Login-IP, Device, Uhrzeit) — bei Bank anfordern.
- **Schriftverkehr mit Bank**: Rückbuchungsantrag, Bankantwort, AGB-Bezug.
- **Strafanzeige / Akteneinsicht-Aufnahmebestätigung** mit Aktenzeichen.
- **Versicherungsmeldung** (Cyber-Police, falls vorhanden).
- **DSGVO-Datenpanne-Meldung** bei BfDI / Landesbehörde, falls Daten Dritter betroffen.
- **TAN-Verfahrens-Doku** (push-TAN, smsTAN, App): bei Diskussion Sorgfaltsmaßstab § 675v BGB.

## Praxis-Tipp
Beim Eingang einer Phishing-Mail unbedingt die Originaldatei mit vollständigem Header sichern (in Outlook: Datei "speichern unter .msg" oder als .eml-Datei) — gerichtsfest nur mit Header. PDF-Druck der Mail genügt nicht: IP-Spur, DKIM-Signatur und Return-Path sind nur im Header lesbar.

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
