---
name: spezial-messung-fahrverbot-punkte
description: "Messung, Punkte, Fahrverbot und Verteidigungsziel im Verkehrs-OWi: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output."
---

# Messung, Punkte, Fahrverbot und Verteidigungsziel im Verkehrs-OWi

## Aufgabe
Dieser Skill ersetzt einen zu groben Spezial-Slot durch einen konkreten Fachworkflow im Plugin `verkehrsowi-verteidiger`. Kontext des Plugins: Freistehendes VerkehrsOWi-Plugin für Bußgeldbescheid, Anhörung, Einspruch, Punkte, Fahrverbot, Rotlicht, Geschwindigkeit, Abstand, Handy, Alkohol, Drogen, Akteneinsicht, Messakte, Zeugenstrategie und Amtsgericht.

Er arbeitet nicht lexikalisch, sondern fallbezogen: Er trennt zuerst Rollen, Ziel, Fristen, Zuständigkeiten und Belege, prüft dann die fachlichen Weichen und liefert ein Ergebnis, mit dem weitergearbeitet werden kann.

## Kaltstart
Wenn Material vorliegt, nutze es zuerst. Frage nur nach, was für die nächste Entscheidung fehlt:

1. Wer handelt in welcher Rolle und gegen wen?
2. Welches praktische Ziel soll erreicht werden?
3. Welche Fristen, Termine, Zustellungen, Schwellenwerte oder Sanktionen stehen im Raum?
4. Welche Unterlagen, Daten, Registerauszüge, Bescheide, Verträge, Screenshots oder sonstigen Belege liegen vor?
5. Soll der Output intern, für Mandantschaft, Behörde, Gericht, Gegnerseite oder Gremium formuliert werden?

## Arbeitsworkflow
1. **Sortieren:** Sachverhalt, Dokumente und offene Punkte in eine knappe Fallmatrix bringen.
2. **Rechtsrahmen:** Einschlägige Normen, Zuständigkeiten, Verfahren, Fristen und formelle Anforderungen live prüfen, soweit Aktualität tragend ist.
3. **Materielle Weichen:** Die Kernfragen zu **Messung, Punkte, Fahrverbot und Verteidigungsziel im Verkehrs-OWi** mit Tatbestandsmerkmalen, Belegen, Gegenargumenten und typischen Praxisfehlern abarbeiten.
4. **Risikoampel:** Ergebnis in Grün/Gelb/Rot mit Begründung, Unsicherheiten und Beweisbedarf einordnen.
5. **Anschluss:** Passende weitere Skills desselben Plugins vorschlagen, wenn Spezialprüfung, Schriftsatz, Tabelle, Brief oder Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- Kurzbild in fünf Sätzen: Lage, Ziel, Frist, Risiko, nächster Schritt.
- Prüfmatrix mit Punkt, Norm/Quelle, Tatsachen, Beleg, Bewertung, To-do.
- Konkreter Textbaustein oder Arbeitsprodukt passend zur Lage: Memo, Mandantenbrief, Behörden-/Gerichtsschreiben, Checkliste, Tabelle oder Verhandlungsagenda.
- Keine Scheingenauigkeit: Annahmen, Lücken und Live-Check-Bedarf offen markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwenden, wenn die Nutzerin oder der Nutzer den Text selbst bereitstellt; dann nicht als frei verifizierte Quelle ausgeben.

## Messung / Punkte / Fahrverbot Bausteine
- **Punkte FAER § 4 StVG (seit Reform 2014):**
  - 1 Punkt: leichtere Verstoesse (z. B. Tempoueberschreitung 21-30 km/h innerorts).
  - 2 Punkte: schwerere Verstoesse mit Fahrverbot (z. B. ueber 30 km/h innerorts mit Fahrverbot).
  - 3 Punkte: Straftaten und besonders schwere OWi (z. B. § 316 StGB Trunkenheit, Unfallflucht).
  - **4-5 Punkte:** Ermahnung; **6-7 Punkte:** Verwarnung mit Aufbauseminar-Hinweis; **8 Punkte:** Entziehung Fahrerlaubnis (zwingend, § 4 V StVG).
  - **Punkteabbau:** freiwilliges Fahreignungsseminar bei 1-5 Punkten = 1 Punkt Reduktion (nur einmal in 5 Jahren).
- **Fahrverbot § 25 StVG:**
  - 1-3 Monate; Antritt regelmaessig nach Wahl binnen 4-Monatsfrist § 25 IIa StVG bei Ersttaeter; wiederholt sofort.
  - Bekannte Konstellationen: Geschwindigkeitsverstoss innerorts ab 31 km/h, ausserorts ab 41 km/h; Rotlicht qualifiziert (1+ Sek); Abstand unter 50% halber Tacho ab 80 km/h.
- **Wegfall Fahrverbot wegen unzumutbarer Haerte** (OLG-Linie restriktiv):
  - Berufskraftfahrer (Existenzgefahr).
  - Pflege Angehoeriger.
  - Wesentlicher Verlust soziale Bindungen.
  - **Kompensation moeglich:** Erhoehung Geldbusse um 50-100 % (BGH-Linie zur tatschuldangemessenen Kompensation).
- **Messung Standard-Pruefung:**
  - **Eichschein** Geraet im Tatzeitraum?
  - **Bedienerschein** mit Schulungsnachweis?
  - **Toleranzwerte abgezogen?** (Geschwindigkeit: 3 km/h bis 100 km/h, 3 % darueber; Abstand: 10 %).
  - **Standardisiertes Messverfahren** (BGH zur Beweiskraft)?
  - **Rohdaten** verfuegbar? (BVerfG-Linie zur fair-trial-Garantie zur Akteneinsicht).
- **Messverfahren-Spezialitaeten:**
  - PoliScan FM1: Photopositionierung-Diskussion.
  - Leivtec XV3: dokumentierte Verfahrensschwaechen einzelner OLG-Bezirke.
  - ES 8.0/3.0: Smear-Effekt; Photolinie.
  - TraffiStar S330: stationaerer Blitzer, Rohdaten-Diskussion.
- **Praxis-Tipp:** Bei Punktestand-Abfrage KBA Flensburg (kostenfrei); Punkteloesch-Tabelle § 29 StVG: 2,5 Jahre fuer 1-Punkt-OWi; 5 Jahre fuer 2-Punkt; 10 Jahre fuer 3-Punkt-Verstoesse.
