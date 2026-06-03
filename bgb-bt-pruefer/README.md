# BGB BT Prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`bgb-bt-pruefer`) | [`bgb-bt-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bgb-bt-pruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **BGB BT — Holzofen, Lieferkette, Bürgschaft, GoA und Brandschaden** (`bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt`) | [Gesamt-PDF lesen](../testakten/bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt/gesamt-pdf/bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt_gesamt.pdf) | [`testakte-bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt.zip) |
| **BGB BT — Smart-Kühlschrank, digitale Elemente und Reparaturblockade** (`bgb-bt-smart-kuehlschrank-digital-repair-koeln`) | [Gesamt-PDF lesen](../testakten/bgb-bt-smart-kuehlschrank-digital-repair-koeln/gesamt-pdf/bgb-bt-smart-kuehlschrank-digital-repair-koeln_gesamt.pdf) | [`testakte-bgb-bt-smart-kuehlschrank-digital-repair-koeln.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bgb-bt-smart-kuehlschrank-digital-repair-koeln.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Großer BGB-BT-Prüfer für Schuldrecht Besonderer Teil: Kauf, Verbrauchsgüterkauf, Waren mit digitalen Elementen, Updatepflichten, Right-to-Repair-Schnittstellen, Miete, Pacht, Leihe, Darlehen, Dienst, Werk, Bau, Reise, Makler, Auftrag, Geschäftsbesorgung, Bürgschaft, Schuldversprechen, GoA, Bereicherung, Delikt und Rückabwicklung.

Das Plugin ist der Gegenpart zum `bgb-at-pruefer`: Es beginnt bei der Anspruchsfrage und führt dann durch die Vertragstypen und gesetzlichen Schuldverhältnisse des BGB-BT. Es ist für Anfänger verständlich genug, aber hart genug für Kanzleivermerke, Klageentwürfe, Verteidigungslinien und Ausbildung.

## Kaltstart

1. **Wer will was von wem?** Leistung, Zahlung, Unterlassung, Rückzahlung, Schadensersatz oder Herausgabe.
2. **Welcher Lebensbereich?** Kauf, Miete, Werk, Dienst, Auftrag, Bürgschaft, GoA, Bereicherung, Delikt.
3. **Welche Störung?** Mangel, Verzug, Kündigung, Rücktritt, Anfechtung, Nichtigkeit, Aufrechnung, Verjährung, Beweisproblem.
4. **Welches Arbeitsprodukt?** Gutachten, Mandantenbrief, Klageskizze, Anspruchsmatrix, Vergleichsvorschlag, Beweis- und Fristenplan.

## Leitprinzip

Erst Anspruchsgrundlage, dann Tatbestand, dann Rechtsfolge, dann Einwendungen. Keine Sammelwörter wie „irgendwie vertragsähnlich“, wenn eine saubere Reihenfolge möglich ist. Schnittstellen zum BGB AT, AGB-Recht, Bereicherungs- und Anfechtungsrecht sowie Methodenlehre werden aktiv vorgeschlagen.

## Quellenanker

- BGB amtlich/frei: https://www.gesetze-im-internet.de/bgb/
- Kaufvertrag: §§ 433 ff. BGB
- Digitale Produkte und Waren mit digitalen Elementen: §§ 327 ff., 327a, 327e, 327f, 434, 475b, 475c, 475e, 476, 477 BGB
- Miete/Pacht/Leihe/Darlehen/Dienst/Werk: §§ 488 ff., 535 ff., 581 ff., 598 ff., 611 ff., 631 ff. BGB
- Auftrag/Geschäftsbesorgung/GoA/Bürgschaft/Delikt/Bereicherung: §§ 662 ff., 675 ff., 677 ff., 765 ff., 812 ff., 823 ff. BGB
- Right to Repair: Richtlinie (EU) 2024/1799, Umsetzungsstand live prüfen; nicht ungeprüft als bereits vollständig deutsches BGB-Recht behandeln.

## Testakte

Die Demonstrationsakte `bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt` verbindet Kauf, Werk, Bürgschaft, GoA, Bereicherung und Delikt in einem realistisch unordentlichen Mandat.

Die Akte `bgb-bt-smart-kuehlschrank-digital-repair-koeln` ergänzt den modernen Kaufrechtsstrang: vernetzter Kühlschrank, App/Cloud/Firmware, Updatepflicht, § 475b/§ 475c BGB, Beweislast, Verjährung, Reparaturblockade und Right-to-Repair-Schnittstelle.

## Keine Blindzitate

Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und überprüfbarer freier Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatzangaben aus Modellwissen.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 60 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Skill-Routing für BGB-BT-Fälle: Anspruchsziel, Vertragstyp, gesetzliches Schuldverhältnis, Störung, Beweise, Fristen und Output. |
| `arbeitsnaher-dienstvertrag-bgb` | Prüft zivilrechtliche Dienstleistungsverhältnisse mit Arbeitsrechtsnähe, Scheinselbstständigkeit und Vergütungsfragen. |
| `auftrag-und-unentgeltliche-taetigkeit` | Prüft Auftrag §§ 662 ff. BGB, Weisungen, Auskunft, Rechenschaft, Aufwendungsersatz, Herausgabe und Kündigung. |
| `bauvertrag-und-verbraucherbauvertrag` | Prüft Bauvertrag, Verbraucherbauvertrag, Änderungsanordnung, Vergütungsanpassung, Baubeschreibung und Widerruf. |
| `bereicherungsrecht-entreicherung-und-saldotheorie` | Prüft Wertersatz, Entreicherung, verschärfte Haftung, Saldotheorie und Minderjährigenschutz. |
| `bereicherungsrecht-leistungskondiktion` | Prüft Leistung, Etwas erlangt, ohne Rechtsgrund, Zweckverfehlung und Rückabwicklung. |
| `bereicherungsrecht-nichtleistungskondiktion` | Prüft Eingriffskondiktion, Verwendungskondiktion, Rückgriffskondiktion und Vorrang der Leistungskondiktion. |
| `buergschaft-einreden-und-akzessorietaet` | Prüft Einreden des Bürgen, Vorausklage, Erlöschen der Hauptschuld, Sicherungszweck und Höchstbetragsbürgschaft. |
| `buergschaft-form-und-verbraucherbuerge` | Prüft Schriftform, elektronische Formgrenzen, Verbraucherbürgen, krasse Überforderung, Sittenwidrigkeit und Angehörigenbürgschaft. |
| `buergschaft-grundschema-paragraph-765` | Prüft Bürgschaft: Hauptschuld, Bürgschaftserklärung, Schriftform, Akzessorietät, Einreden und Inanspruchnahme. |
| `darlehen-und-finanzierung` | Prüft Gelddarlehen, Verbraucherdarlehen, Kündigung, Widerruf, Zinsen, Sicherheiten und Rückzahlungsstörungen. |
| `deliktsrecht-haftung-fuer-verrichtungen-paragraph-831` | Prüft Verrichtungsgehilfe, Ausführung der Verrichtung, Exkulpation, Auswahl/Überwachung und Schaden. |
| `deliktsrecht-paragraph-823-1` | Prüft Rechtsgutsverletzung, Handlung, Kausalität, Rechtswidrigkeit, Verschulden und Schaden. |
| `deliktsrecht-paragraph-826-sittenwidrige-schaedigung` | Prüft sittenwidrige vorsätzliche Schädigung, Gesamtwürdigung, Schädigungsvorsatz und Schaden. |
| `deliktsrecht-schutzgesetz-paragraph-823-2` | Prüft Schutzgesetzqualität, persönlicher/sachlicher Schutzbereich, Verstoß, Verschulden und Schaden. |
| `deliktsrecht-sonstiges-recht` | Prüft Eigentum, Besitz, eingerichteter und ausgeübter Gewerbebetrieb, APR und sonstige Rechte. |
| `deliktsrecht-tierhalter-und-gebaeude` | Prüft Tierhalterhaftung, Gebäudeeinsturz, Grundstücks- und Verkehrssicherungspflichten. |
| `dienstvertrag-und-behandlungsvertrag` | Prüft Dienstvertrag, freie Dienste, Geschäftsbesorgung, Behandlungsvertrag, Dokumentation und Aufklärung. |
| `gesamtschuld-und-regress-bgb-bt` | Prüft Gesamtschuld, Innenausgleich, Bürgschaftsregress, GoA/Bereicherung/Delikt-Regress und Verjährung. |
| `geschaeftsbesorgung-und-zahlungsdienste` | Prüft entgeltliche Geschäftsbesorgung, Zahlungsdienste, Ausführung, Fehlbuchung und Schnittstellen zum Bankrecht. |
| `goa-entgegenstehender-wille-paragraphen-678-679` | Prüft entgegenstehenden Willen, öffentliches Interesse, Unterhaltspflichten und Schadensersatz bei aufgedrängter Hilfe. |
| `goa-grundschema-paragraph-677` | Prüft echte berechtigte GoA: fremdes Geschäft, Fremdgeschäftsführungswille, Interesse und wirklicher/mutmaßlicher Wille. |
| `kaufrecht-abweichungsvereinbarung-objektive-anforderungen-476` | Prüft, ob Händler oder Hersteller objektive Anforderungen, digitale Funktionen, Updateversprechen, Kompatibilität oder Interoperabilität wirksam abbedungen haben. |
| `kaufrecht-beweislast-verjaehrung-digitale-elemente` | Prüft Beweislastvermutung, Sonderverjährung und Hemmungs-/Ablaufregeln bei Mängeln an digitalen Elementen, Updatepflichten und Reparaturübergabe. |
| `kaufrecht-dauerhafte-bereitstellung-digitaler-elemente-475c` | Prüft Waren mit digitalen Elementen bei dauerhafter Bereitstellung, insbesondere Smart-Home, Fahrzeuge, Wearables, Maschinen, Apps, Cloudkonten und laufende Firmwaredienste. |
| `kaufrecht-gefahruebergang-und-versendung` | Prüft Gefahrübergang, Versendung, Annahmeverzug, Transportverlust und Verbrauchsgüter-Ausnahmen. |
| `kaufrecht-nacherfuellung-ruecktritt-minderung` | Prüft kaufrechtliche Mängelrechte, Fristsetzung, Unzumutbarkeit, Fehlschlagen, Rücktritt und Minderung. |
| `kaufrecht-rechtsmangel-paragraph-435` | Prüft Rechtsmängel: Eigentum, Belastungen, Rechte Dritter, IP-Rechte, öffentlich-rechtliche Beschränkungen und Registerlagen. |
| `kaufrecht-right-to-repair-und-nacherfuellung` | Verbindet kaufrechtliche Nacherfüllung mit dem EU-Right-to-Repair-Stand, Reparaturvorrang, Reparaturinformationen, Ersatzteilen, Software-Locks und reparaturfreundlicher Mandatsstrategie. |
| `kaufrecht-sachmangel-paragraph-434` | Prüft Sachmängel nach subjektiven, objektiven, Montage- und Installationsanforderungen einschließlich Funktionalität, Kompatibilität, Interoperabilität, Zubehör, Anleitung, Werbung, digitalen Bestandteilen und öffentlicher Äußerungen. |
| `kaufrecht-schadensersatz-aufwendungsersatz` | Prüft §§ 280 ff. BGB im Kaufrecht mit Mangelschaden, Mangelfolgeschaden, Verzögerung und nutzlosen Aufwendungen. |
| `kaufrecht-updates-sicherheitsupdates-327f-475b` | Prüft Aktualisierungspflichten bei digitalen Produkten und Waren mit digitalen Elementen, einschließlich Sicherheitsupdates, Informationspflichten, Installationsfehlern und Folgen unterlassener Updates. |
| `kaufrecht-ware-mit-digitalen-elementen-475b` | Prüft, ob eine Kaufsache wegen App, Cloud, Firmware, Konto, Schlüssel, Sensorik oder OTA-Update eine Ware mit digitalen Elementen ist, und ordnet Mangelrechte nach § 434, § 475b und § 327a BGB. |
| `kaufvertrag-grundschema-paragraph-433` | Prüft Primär- und Sekundäransprüche aus Kaufvertrag nach § 433 BGB und Schnittstellen zu BGB AT, Verbraucherschutz und AGB. |
| `maklervertrag-und-provision` | Prüft Maklerlohn, Nachweis/Vermittlung, Kausalität, Textform, Verbraucherfragen und Verflechtung. |
| `mietrecht-mangel-minderung` | Prüft Mietmangel, Anzeige, Minderung, Zurückbehaltung, Schadensersatz und Beweisfragen. |
| `mietvertrag-grundschema-paragraph-535` | Prüft Gebrauchsüberlassung, Miete, Mangel, Minderung, Kündigung und Rückgabe. |
| `pacht-leihe-und-verwahrung` | Prüft Pacht, Leihe und Verwahrung: Nutzung, Fruchtziehung, Rückgabe, Haftung, Kündigung und Aufwendungsersatz. |
| `produzentenhaftung-und-verkehrssicherung` | Prüft deliktische Produzentenhaftung, Konstruktions-, Fabrikations-, Instruktions- und Produktbeobachtungsfehler. |
| `reisevertrag-pauschalreise` | Prüft Pauschalreise, Reisemangel, Abhilfe, Minderung, Kündigung, Schadensersatz und Entschädigung. |
| `schadensrecht-paragraphen-249-253` | Berechnet Naturalrestitution, Geldersatz, Nutzungsausfall, Schmerzensgeld, Vorteilsausgleich und Mitverschulden. |
| `schnittstelle-bgb-at-methodenlehre-agb` | Erkennt, wann BGB-BT-Probleme eigentlich Form, Anfechtung, Stellvertretung, AGB, Auslegung oder Methodenfragen sind. |
| `schuldversprechen-schuldanerkenntnis` | Prüft abstraktes Schuldversprechen, deklaratorisches/konstitutives Schuldanerkenntnis und Beweisfunktion. |
| `tausch-und-schenkung` | Prüft Tausch und Schenkung einschließlich Form, Vollzug, Widerruf, grober Undank und Mängelhaftung. |
| `unechte-goa-paragraph-687` | Prüft irrtümliche Eigengeschäftsführung und angemaßte Eigengeschäftsführung mit Herausgabe-/Schadensersatzfolgen. |
| `verbrauchsgueterkauf-digitales` | Prüft Verbrauchsgüterkauf, digitale Produkte, Waren mit digitalen Elementen, Aktualisierungspflichten, Beweislast, Verjährung, Abweichungsvereinbarungen und Right-to-Repair-Schnittstellen nach aktuellem BGB und EU-Rechtsstand. |
| `vergleich-paragraph-779` | Prüft Vergleich, Streit/Ungewissheit, gegenseitiges Nachgeben, Irrtum über Vergleichsgrundlage und Vollstreckbarkeit. |
| `verjaehrung-bgb-bt-spezial` | Prüft besondere Verjährungsfristen in Kauf, Werk, Miete, Reise, Delikt und Bürgschaft. |
| `werkvertrag-abnahme-und-faelligkeit` | Prüft Abnahme, Abnahmefiktion, Verweigerung, Fälligkeit, Abschlagszahlungen und Sicherheiten. |
| `werkvertrag-grundschema-paragraph-631` | Prüft Herstellungserfolg, Vergütung, Abnahme, Mangel, Nacherfüllung, Rücktritt, Minderung und Selbstvornahme. |
| `werkvertrag-maengelrechte` | Prüft § 634 BGB: Nacherfüllung, Selbstvornahme, Rücktritt, Minderung, Schadensersatz. |
| `workflow-anfangercoach-schuldrecht-bt` | Erklärt BGB-BT-Fälle für Einsteiger ohne die juristische Präzision zu verlieren. |
| `workflow-anspruchslandkarte` | Baut aus einem BGB-BT-Fall eine Anspruchslandkarte mit Vertrag, gesetzlichem Schuldverhältnis, Rückabwicklung, Delikt, Bereicherung und Sicherheiten. |
| `workflow-beweislast-und-belegmatrix` | Ordnet Darlegungs- und Beweislast in BGB-BT-Fällen, markiert fehlende Belege und formuliert Nachforderungen. |
| `workflow-dokumentenintake` | Sortiert Verträge, Rechnungen, Chats, Fotos, Gutachten, Mahnungen und Kontoauszüge für BGB-BT-Prüfungen. |
| `workflow-fristen-ruecktritt-kuendigung` | Prüft Fristen, Erklärungen und Zugang bei Rücktritt, Kündigung, Minderung, Nacherfüllungsverlangen und Verjährung im BGB BT. |
| `workflow-livequellen-rechtsstand` | Zwingt vor tragenden Aussagen zum Abgleich mit amtlichen Normtexten und frei zugänglicher Rechtsprechung. |
| `workflow-output-gutachten-klage-brief` | Erstellt aus der Prüfung Gutachten, Klageskizze, Mandantenbrief, Vergleichsvorschlag, Anspruchstabelle oder Beweisplan. |
| `workflow-red-team-gegenseite` | Prüft die eigene Lösung aus Sicht der Gegenseite und findet schwache Anspruchsvoraussetzungen, Einwendungen und Beweisprobleme. |
| `workflow-vergleich-und-verhandlungsplan` | Macht aus BGB-BT-Risiken eine Verhandlungsstrategie mit Zahlungsbandbreite, Sachleistung, Fristen und Nebenabreden. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
