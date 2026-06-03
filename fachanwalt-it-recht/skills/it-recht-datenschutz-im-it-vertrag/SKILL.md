---
name: it-recht-datenschutz-im-it-vertrag
description: "Datenschutzklauseln im IT-Vertrag pruefen und gestalten. Schnittstelle IT-Recht und Datenschutzrecht. Sieben-Fragen-Diagnose: Vertragstyp Werkvertrag Dienstvertrag SaaS Lizenz personenbezogene Daten Rolle Verantwortlicher Auftragsverarbeiter gemeinsam Verantwortlicher Subverarbeiter Datenstandort. AVV Art. 28 DSGVO Joint Controllership Art. 26 DSGVO Drittlandstransfer Art. 44 ff DSGVO. Schritt-fuer-Schritt fuer Vertragspruefung. Mustertexte fuer Klauseln. Abgrenzung: kein reiner AVV (avv-pruefung) keine SaaS-Spezialklauseln (it-recht-saas-avv-und-tia-bundle)."
---

# IT-Recht — Datenschutz im IT-Vertrag

## Zweck

Dieser Skill liegt an der Schnittstelle des IT-Vertragsrechts und des Datenschutzrechts. Er hilft beim Pruefen und Gestalten von IT-Vertraegen mit datenschutzrechtlicher Komponente: Softwareentwicklung, IT-Outsourcing, Hosting, Wartung, Cloud, SaaS, Lizenz mit Telemetrie. Ziel ist, dass der IT-Vertrag und die datenschutzrechtliche Konstruktion (AVV oder Joint Controllership) konsistent sind.

## Wann brauchen Sie diesen Skill / Kaltstart-Fragen

Sie brauchen den Skill, sobald ein IT-Vertrag personenbezogene Daten beruehrt — was praktisch immer der Fall ist, wenn IT betrieben wird.

Sieben-Fragen-Diagnose:

1. **Welcher Vertragstyp?** Kaufvertrag Software, Werkvertrag Individualentwicklung, Dienstvertrag Wartung, SaaS-Mietvertrag, Lizenzvertrag, Outsourcing-Rahmenvertrag?
2. **Werden personenbezogene Daten verarbeitet?** Mitarbeiter-, Kunden-, Endkundendaten? Welche Datenkategorien Art. 9, 10?
3. **Rolle des IT-Dienstleisters:** Verantwortlicher (Art. 4 Nr. 7), Auftragsverarbeiter (Art. 4 Nr. 8 i.V.m. Art. 28) oder gemeinsam Verantwortlicher (Art. 26)?
4. **Subverarbeiter:** Wer nutzt Subdienstleister? Welche Genehmigungsklausel?
5. **Datenstandort:** EU/EWR oder Drittland? Bei Drittland: welcher Transfermechanismus Art. 44 ff DSGVO?
6. **Vertragslaufzeit und Datenrueckgabe:** Was passiert nach Vertragsende? Art. 28 III g.
7. **Audit und Kontrolle:** Welche Pruefrechte des Verantwortlichen Art. 28 III h?

## Rechtlicher Rahmen

- **Art. 4 DSGVO** Begriffe.
- **Art. 5 DSGVO** Grundsaetze.
- **Art. 6 DSGVO** Rechtmaessigkeit.
- **Art. 24 DSGVO** Verantwortlichkeit.
- **Art. 25 DSGVO** Privacy by Design und Default.
- **Art. 26 DSGVO** Joint Controller.
- **Art. 28 DSGVO** Auftragsverarbeitung mit Mindestinhalten Art. 28 III lit a-h.
- **Art. 32 DSGVO** TOM.
- **Art. 44 ff DSGVO** Drittlandstransfer.
- **EU-SCC 2021/914** Standardvertragsklauseln Modul 1 bis 4.
- **EuGH C-311/18 Schrems II** (Urteil 16.07.2020).
- **§§ 280, 311 BGB** vertragliche Haftung.
- **§§ 631 ff BGB** Werkvertrag.
- **§§ 535 ff BGB** Mietvertrag (haeufig SaaS).
- **EDSA Leitlinien 07/2020** zu Begriffen Verantwortlicher und Auftragsverarbeiter (Version 2.0, 07.07.2021).

## Mandantenfuehrung Schritt-fuer-Schritt

1. **Zuerst: Rollenpruefung.** Ist der IT-Dienstleister Auftragsverarbeiter oder Verantwortlicher? Sehr haeufig nicht durch Vertragsbezeichnung, sondern durch faktische Zwecksetzung bestimmt. Wer entscheidet ueber Zweck und Mittel?
2. **Als zweites: AVV oder Joint Controller Vereinbarung?** Vertraege ohne Datenschutzanhang gibt es im IT-Bereich praktisch nie rechtmaessig.
3. **Als drittes: Mindestinhalte Art. 28 III pruefen** (Gegenstand, Dauer, Art, Zweck, Datenkategorien, Betroffenenkategorien, Rechte und Pflichten Verantwortlicher).
4. **Als viertes: Drittlandstransfer pruefen.** Standort Server? Subdienstleister in USA, Indien? Schrems II Anforderungen TIA.
5. **Als fuenftes: Subverarbeiter-Klausel.** Generelle Genehmigung mit Widerspruchsrecht (Art. 28 II Satz 2).
6. **Als sechstes: Loeschung Rueckgabe.** Was passiert mit Daten nach Vertragsende?
7. **NICHT** AVV einfach vom IT-Dienstleister einseitig akzeptieren ohne Vergleich mit Mandantenanforderungen.

## Trade-off-Matrix

| Konstellation | Empfohlene Vertragsform | Begruendung |
|---|---|---|
| Cloud-Storage, kein Zweckbezug | AVV Art. 28 | reine Speicherung |
| Wartung mit Zugriff Mandantendaten | AVV Art. 28 | weisungsgebunden |
| Newsletter-Versand mit eigenem Tracking | Joint Controller Art. 26 | gemeinsame Zwecke |
| Cloud mit eigener Auswertung Telemetrie | Joint Controller oder zwei Verantwortliche | KI-Modell vom Anbieter trainiert |
| Bezahlsoftware mit Telemetrie ohne Auswertung | AVV moeglich | Telemetrie nur fuer Funktion |
| US-Anbieter direkt | EU-SCC + TIA + ggf. DPF | Schrems II Compliance |

## Mustertexte

### Klausel "Datenschutzrechtliche Rolle"

> Die Parteien gehen davon aus, dass der Auftragnehmer in Bezug auf [bezeichnete Verarbeitungen] Auftragsverarbeiter im Sinne von Art. 4 Nr. 8 in Verbindung mit Art. 28 DSGVO ist. Soweit der Auftragnehmer Zweck und Mittel weitergehender Verarbeitungen (z. B. Anonymisierung zur Produktverbesserung) festlegt, ist er insoweit eigenstaendig Verantwortlicher; die Parteien werden hierfuer eine separate Vereinbarung schliessen.

### Klausel "Subverarbeiter"

> Der Auftragnehmer kann Subverarbeiter mit allgemeiner Genehmigung des Auftraggebers einsetzen. Eine aktuelle Liste der Subverarbeiter wird unter [URL] gefuehrt. Der Auftragnehmer informiert den Auftraggeber ueber beabsichtigte Aenderungen mit einer Frist von [30 Tagen]. Der Auftraggeber kann der Aenderung mit datenschutzrechtlicher Begruendung widersprechen; in diesem Fall sind die Parteien zur Verhandlung verpflichtet, und der Auftraggeber kann den Vertrag bei Nichteinigung mit angemessener Frist aus wichtigem Grund kuendigen.

### Klausel "Drittlandstransfer"

> Personenbezogene Daten werden grundsaetzlich in der Europaeischen Union verarbeitet. Soweit eine Verarbeitung in einem Drittland erforderlich ist, schliessen die Parteien zusaetzlich die Standardvertragsklauseln 2021/914 (Modul [2 oder 3] je nach Rolle) ab. Eine Transfer Impact Assessment liegt vor und wird mindestens jaehrlich aktualisiert.

### Klausel "Datenrueckgabe und Loeschung"

> Nach Ende des Vertragsverhaeltnisses gibt der Auftragnehmer auf Wahl des Auftraggebers saemtliche personenbezogenen Daten in einem strukturierten gaengigen maschinenlesbaren Format zurueck oder loescht sie. Die Loeschung wird in einem Loeschprotokoll dokumentiert. Aufbewahrungspflichten nach Art. 28 Abs. 3 lit. g DSGVO bleiben unberuehrt; der Auftragnehmer benennt diese.

## Typische Fehler

- AVV vergessen, weil Vertrag als reiner Werkvertrag oder Lizenzvertrag formuliert.
- Rolle "Auftragsverarbeiter" angegeben, faktisch Verantwortlicher (z. B. eigene Tracking-Auswertung).
- Subverarbeiter nicht genehmigt.
- Drittlandstransfer nicht adressiert.
- Loeschklausel fehlt oder widerspricht Aufbewahrungspflicht.

**Was triggert Aufsicht / Vertragsverhandlung?** Keine AVV-Anlage, leere Floskel zu TOM, Verweis auf "branchenuebliche Standards" ohne Konkretisierung, keine SCC bei US-Anbieter.

## Querverweise

- `avv-art-28-dsgvo-grundtatbestand`
- `avv-art-28-mindestinhalte-checkliste`
- `it-recht-saas-avv-und-tia-bundle`
- `it-recht-cloud-vertrag-datenschutz-due-diligence`
- `datenschutz-erstgespraech-mandantenmatrix-7-fragen`

## Quellen Stand 06/2026

- DSGVO Art. 4, 5, 24, 25, 26, 28, 32, 44 ff.
- BGB §§ 280, 311, 535 ff., 631 ff.
- EU-SCC 2021/914, Durchfuehrungsbeschluss 04.06.2021.
- EuGH C-311/18 Schrems II, Urteil 16.07.2020.
- EDSA, Leitlinien 07/2020 zu den Begriffen Verantwortlicher und Auftragsverarbeiter, Version 2.0, angenommen 07.07.2021.
- Keine Aufsatzfundstellen aus Modellwissen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
