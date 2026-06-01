---
name: spezial-tabellenimport-zahlen-schwellen-und-berechnung
description: "Tabellenimport: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output."
---

# Tabellenimport: Zahlen, Schwellenwerte und Berechnung

## Aufgabe
Dieser Skill ist ein konkreter Fachbaustein für `insolvenzforderungsanmeldungspruefung`. Ausgangspunkt ist: Freistehendes Plugin für die Insolvenzforderungsanmeldungsprüfung: Intake, § 174 InsO, Belege, Grund, Betrag, Rang, vbuH, Nachforderungen, Tabellenimport, Prüfungstermin, Bestreiten, Feststellung, Tabellenauszug und Verteilung.

Er führt durch **Zahlen, Schwellenwerte und Berechnung** im Themenfeld **Tabellenimport**. Ziel ist nicht ein abstrakter Lexikontext, sondern ein belastbares Arbeitsprodukt für die nächste anwaltliche, behördliche, gerichtliche, organisatorische oder mandantenbezogene Entscheidung.

## Kaltstart
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Tabellenimport** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Tabellenimport — Datenstruktur und Berechnung
- **Stammdaten:** Gläubiger-Nr., Name, Anschrift, Bankverbindung, Vertreter, Vollmacht.
- **Forderungsdaten:** Hauptforderung netto/brutto, Zinsen aufgegliedert (Zeitraum, Zinssatz, Basiswert), Mahnkosten, Vorgerichtliche Anwaltskosten, Gerichtskosten, Vollstreckungskosten.
- **Verzugszinsen:** Bei B2B § 288 Abs. 2 BGB Basiszins +9 Prozentpunkte; bei Verbraucher § 288 Abs. 1 BGB Basiszins +5 Prozentpunkte; Verzugsbeginn nach § 286 BGB.
- **Rangangabe:** § 38 InsO (einfach), § 39 Abs. 1 Nr. 1–5 InsO (nachrangig), § 47 InsO (Aussonderung), §§ 49–51 InsO (Absonderung mit Ausfallbetrag § 52 InsO).
- **vbuH-Flag § 302 Nr. 1 InsO:** Ausdrücklich anmelden, sonst keine Restschuldbefreiungs-Ausnahme.
- **Quote-Berechnung:** Anteil je Forderung an Gruppensumme; je niedriger der Rang, desto geringer die Quote (nachrangige Forderungen § 39 InsO erhalten regelmäßig 0 %).
- **Tabellensoftware:** Insolvenzverwalter verwenden idR spezialisierte Software (winsolvenz, LEXolution); Anmeldungen über Standardisierte Formulare oder Schnittstellen sind effizienter.
- **Praxis:** Prüfung Mathematik (Zinsen, Kosten) vor Anmeldung — Bestreiten wegen Rechenfehler kostet Glaubwürdigkeit und führt regelmäßig zur Kürzung.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
