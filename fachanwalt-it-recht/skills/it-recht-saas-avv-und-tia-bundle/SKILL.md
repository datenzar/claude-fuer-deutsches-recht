---
name: it-recht-saas-avv-und-tia-bundle
description: "SaaS-Vertrag mit AVV nach Art. 28 DSGVO und Transfer Impact Assessment als Bundle. Sieben-Fragen-Diagnose: Anbietersitz Datenstandort Datenkategorien Konzernverflechtung Subprozessoren US-Bezug DPF-Zertifizierung. Schritt-fuer-Schritt fuer Bundle-Erstellung. EuGH C-311/18 Schrems II EU-SCC 2021/914 Modul 2 oder 3 EU-US Data Privacy Framework Durchfuehrungsbeschluss 2023/1795 vom 10.07.2023. EDSA Empfehlungen 01/2020 Version 2.0. Mustertexte fuer Bundle-Anlage und TIA-Skeleton. Abgrenzung: keine reine AVV-Pruefung (avv-art-28-mindestinhalte-checkliste) keine Cloud-Due-Diligence (it-recht-cloud-vertrag-datenschutz-due-diligence)."
---

# IT-Recht — SaaS mit AVV und TIA als Bundle

## Zweck

Dieser Skill liefert ein vollstaendiges Vertragsbundle fuer SaaS-Beschaffung mit Drittlandsbezug: SaaS-Hauptvertrag, AVV nach Art. 28 DSGVO, EU-SCC 2021/914 (Modul je nach Rolle), Transfer Impact Assessment (TIA). Das Bundle ist als kanzleitaugliches Paket gestaltet, das die Aufsicht im Pruefungsfall ohne Nachfragen versteht.

## Wann brauchen Sie diesen Skill / Kaltstart-Fragen

Sie brauchen den Skill, wenn ein Mandant einen SaaS-Anbieter mit Drittlandsbezug einsetzt — typischerweise US-Anbieter (Salesforce, Slack, Microsoft 365, Google Workspace, Zoom, HubSpot) oder andere Drittland-Anbieter (Indien, Israel, UK).

Sieben-Fragen-Diagnose:

1. **Anbietersitz:** Wo ist der Vertragspartner ansaessig? Welche Konzernmutter?
2. **Datenstandort:** Welche Region waehlbar? Standardregion?
3. **Datenkategorien:** Welche Daten gehen in den Dienst — Mitarbeiter, Kunden, Endkunden? Art. 9 oder 10 Daten?
4. **Konzernverflechtung:** Gibt es US-Mutter mit Zugriff (CLOUD Act)?
5. **Subprozessoren:** Welche, in welchen Laendern?
6. **US-Bezug:** Faellt der Anbieter unter US-Ueberwachungsgesetze (FISA 702, EO 12333)?
7. **DPF-Zertifizierung:** Ist der Anbieter EU-US Data Privacy Framework zertifiziert? Welche Listung beim US Department of Commerce?

## Rechtlicher Rahmen

- **Art. 28 DSGVO** AVV.
- **Art. 32 DSGVO** TOM.
- **Art. 44 DSGVO** Allgemeines Prinzip Drittlandstransfer.
- **Art. 45 DSGVO** Angemessenheitsbeschluss; EU-US Data Privacy Framework Durchfuehrungsbeschluss (EU) 2023/1795 vom 10.07.2023.
- **Art. 46 DSGVO** SCC 2021/914.
- **EuGH C-311/18 Schrems II** (Urteil 16.07.2020): SCC nur ausreichend mit zusaetzlichen Massnahmen, wenn Drittlandrecht keinen vergleichbaren Schutz bietet.
- **EDSA Empfehlungen 01/2020** Version 2.0 (angenommen 18.06.2021): Sechs-Schritte-Methodik fuer TIA.
- **EDSA Empfehlungen 02/2020** (Version 2.0 angenommen 18.06.2021): Europaeische wesentliche Garantien.
- **FISA 702 USA** (50 USC 1881a) und Executive Order 12333.
- **Executive Order 14086 USA** (07.10.2022) als Basis EU-US DPF.

## Mandantenfuehrung Schritt-fuer-Schritt

1. **Zuerst: Mapping.** Welche SaaS-Dienste mit welchen Datenkategorien laufen?
2. **Als zweites: DPF-Pruefung.** Auf dataprivacyframework.gov pruefen, ob der konkrete Anbieter zertifiziert ist. Wenn ja: Angemessenheitsbeschluss reicht; SCC als Backup empfohlen.
3. **Als drittes: AVV pruefen.** Mindestinhalte Art. 28 III.
4. **Als viertes: SCC abschliessen.** Auch wenn DPF zertifiziert, als Backup im Bundle Modul 2 (Verantwortlicher zu Auftragsverarbeiter) oder Modul 3 (Auftragsverarbeiter zu Auftragsverarbeiter) — je nach Rolle.
5. **Als fuenftes: TIA durchfuehren.** Sechs Schritte EDSA: (1) Datenfluss kennen, (2) Tool wahlen, (3) Drittlandsrecht pruefen, (4) Zusatzmassnahmen pruefen, (5) Verfahrensschritte, (6) Re-Evaluierung.
6. **Als sechstes: Zusatzmassnahmen.** Verschluesselung Customer Managed Key, Pseudonymisierung, vertragliche Garantien.
7. **NICHT** ausschliesslich auf DPF vertrauen — Schrems III ist anhaengig (EuGH C-589/22 Latombe). Backup SCC empfohlen.

## Trade-off-Matrix

| Konstellation | Bundle-Minimum |
|---|---|
| EU-Anbieter, kein US-Bezug | AVV Art. 28 |
| EU-Anbieter mit US-Mutter | AVV + SCC + TIA (CLOUD Act Risiko) |
| US-Anbieter DPF-zertifiziert | AVV + DPF-Hinweis + SCC Backup + TIA leicht |
| US-Anbieter ohne DPF | AVV + SCC + TIA komplett + Zusatzmassnahmen |
| Anderes Drittland ohne Angemessenheit | AVV + SCC + TIA komplett |

## Mustertexte

### Bundle-Anlage Datenschutz (Cover Sheet)

```
SaaS-Vertrag: [Anbieter, Vertragsdatum]
Anlage 1: Auftragsverarbeitungsvertrag nach Art. 28 DSGVO
Anlage 2: Technisch-organisatorische Massnahmen Art. 32 DSGVO (TOM)
Anlage 3: Standardvertragsklauseln 2021/914 Modul [2 oder 3]
Anlage 4: Transfer Impact Assessment Stand [Datum]
Anlage 5: Subprozessorliste Stand [Datum]
Anlage 6: Zertifizierungen (DPF-Listung, ISO 27001, SOC 2)
```

### TIA-Skeleton (Kerntext)

> Transfer Impact Assessment fuer [Anbieter]
> Erstellt am [Datum] vom Verantwortlichen [Mandant]
>
> Schritt 1 — Datenfluss
> - Datenkategorien: [konkret]
> - Datensubjekte: [konkret]
> - Drittland: [USA / Indien / UK]
> - Zweck der Verarbeitung: [konkret]
>
> Schritt 2 — Transfertool
> - Mechanismus: [SCC 2021/914 Modul X / DPF / Andere]
>
> Schritt 3 — Drittlandrecht
> - Einschlaegige Ueberwachungsgesetze: [FISA 702 / EO 12333 / nationales Sicherheitsrecht]
> - Anbieter konkret betroffen: [Pruefung]
> - EDSA Empfehlungen 02/2020 europaeische wesentliche Garantien erfuellt: [ja / nein / teilweise]
>
> Schritt 4 — Zusatzmassnahmen
> - Technisch: [Verschluesselung, Customer Managed Key, Pseudonymisierung]
> - Organisatorisch: [Schulung, Zugriffsbeschraenkung]
> - Vertraglich: [Transparenzklausel, Benachrichtigung bei Behoerdenanfrage]
>
> Schritt 5 — Verfahrensschritte
> - Implementierung: [Datum]
> - Verantwortlicher: [Person]
>
> Schritt 6 — Re-Evaluierung
> - Naechste Pruefung: [Datum, mindestens jaehrlich]
> - Trigger fuer Sofortpruefung: [neue EuGH-Entscheidung, neuer DPF-Status, Anbieterwechsel]

### Klausel "DPF und SCC kombiniert"

> Soweit die Verarbeitung in den Vereinigten Staaten erfolgt, stuetzt sich der Transfer primaer auf den Durchfuehrungsbeschluss der Europaeischen Kommission (EU) 2023/1795 vom 10.07.2023 (EU-US Data Privacy Framework), sofern und solange der Auftragnehmer entsprechend zertifiziert ist. Die Standardvertragsklauseln 2021/914 (Modul [2 oder 3]) sind als alternativer Transfermechanismus zwingend mit abgeschlossen und greifen automatisch, falls die DPF-Zertifizierung entfaellt oder der Durchfuehrungsbeschluss aufgehoben wird.

## Typische Fehler

- DPF-Zertifizierung des Anbieters nicht auf dataprivacyframework.gov verifiziert.
- SCC ohne TIA — Schrems II nicht eingehalten.
- TIA nur Anbieter-Generaltext, kein konkreter Datenfluss.
- SCC-Modul falsch (Modul 2 statt 3 oder umgekehrt).
- Re-Evaluierungsdatum fehlt.

**Was triggert die Aufsicht?** Verweis "Anbieter ist DPF-konform", aber keine Listung; SCC fehlt; TIA leerformelig; Anbieter-AVV ungeprueft.

## Querverweise

- `it-recht-cloud-vertrag-datenschutz-due-diligence`
- `it-recht-datenschutz-im-it-vertrag`
- `avv-eu-kommission-musterklauseln-2021-915`
- `avv-eu-us-data-privacy-framework-bezug`
- `us-transfer-tia-dokumentation`
- `drittlandstransfer-pruefung`

## Quellen Stand 06/2026

- DSGVO Art. 28, 32, 44 ff.
- EU-SCC 2021/914, Durchfuehrungsbeschluss 04.06.2021.
- EU-US DPF, Durchfuehrungsbeschluss (EU) 2023/1795 vom 10.07.2023.
- EuGH C-311/18 Schrems II, Urteil 16.07.2020.
- EuGH C-589/22 Latombe (anhaengig, Stand 2025).
- EDSA, Empfehlungen 01/2020 zu Drittlandstransfers, Version 2.0, angenommen 18.06.2021.
- EDSA, Empfehlungen 02/2020 zu europaeischen wesentlichen Garantien, Version 2.0, angenommen 18.06.2021.
- Executive Order 14086 (USA), 07.10.2022.
- Keine Aufsatzfundstellen aus Modellwissen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
