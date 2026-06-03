---
name: rechtsstand-register-und-fristen
description: "Prüft Patentregister und Fristen: DPMAregister, EPO Register, nationale Validierungen, Einheitspatent, Jahresgebühren, Priorität, Veröffentlichung, Erteilung, Einspruch, Beschränkung, Nichtigkeit und Verlängerungen."
---

# Rechtsstand, Register und Fristen

## Registerquellen

- DPMAregister für deutsche Schutzrechte.
- EPO Register für EP-Anmeldungen und EP-Patente.
- nationale Register für validierte EP-Teile.
- UPC/EPA/DPMA-Informationen, soweit Verfahrensstand betroffen ist.

## Fristenliste

| Frist | Startpunkt | Was prüfen? |
| --- | --- | --- |
| Prioritätsjahr | erste Anmeldung | Nachanmeldung/EP/PCT möglich? |
| Prüfungsbescheid | Zustellung/Amtsmitteilung | Antwortfrist, Verlängerung, Gebühren |
| Jahresgebühren | Anmeldetag/Jahr | gezahlt, Nachfrist, Erlöschen |
| Einspruch EP | Bekanntmachung der Erteilung | Fristende, Gebühr, Einspruchsgründe |
| Nichtigkeit | prozessuale Lage | Zulässigkeit, Parallelverfahren |
| Abmahnung | Zugang | Unterlassung/EV-Risiko |

## Output

- Registerauszug-Zusammenfassung mit Abrufdatum.
- Fristenkalender.
- Statusampel.
- offene Registerlücken.

## Regel

Nie allein aus einer Patentnummer schließen, dass ein Patent in Kraft ist. Immer Rechtsstand, Territory und geltende Anspruchsfassung prüfen.

## Konkrete Fristen

- **Prioritätsjahr Art. 87 EPÜ / § 41 PatG:** 12 Monate ab erster Hinterlegung; PCT-Frist ebenfalls 12 Monate.
- **PCT-Nationalisierung:** regelmäßig 30 oder 31 Monate ab Prioritätstag (Land-spezifisch; DE und EP: 31 Monate).
- **Recherchengebühr EPA:** mit Anmeldung; Prüfungsantrag binnen 6 Monaten nach Veröffentlichung des Recherchenberichts (Art. 94 (1) EPÜ).
- **Antwort auf Prüfungsbescheid EPA:** regelmäßig 4 Monate, verlängerbar.
- **DPMA-Prüfungsantrag (§ 44 PatG):** binnen 7 Jahren nach Anmeldetag.
- **Einspruch EPA:** **9 Monate** ab Veröffentlichung des Erteilungshinweises (Art. 99 EPÜ).
- **Beschränkungs-/Widerrufsantrag (Art. 105a EPÜ):** jederzeit.
- **Jahresgebühren EPA:** ab dem 3. Anmeldejahr; ab Erteilung an nationale Ämter.
- **Jahresgebühren DPMA (§ 17 PatG):** ab dem 3. Anmeldejahr; bei Nichtzahlung Erlöschen (§ 20 PatG); Wiedereinsetzungsfrist § 123 PatG.
- **Nichtigkeitsklage BPatG (§ 81 PatG):** keine starre Frist, aber nur gegen erteiltes Patent.
- **UPC Opt-out (Übergangszeit):** prüfen Sie aktuell unifiedpatentcourt.org -- Übergangszeitraum 7 Jahre ab Inkrafttreten UPCA (mit Verlängerungsoption auf 14 Jahre).

## Quellen live
- `register.dpma.de`, `register.epo.org`, `worldwide.espacenet.com`, `unifiedpatentcourt.org`, `wipo.int/portal/en/index.html` (PatentScope für PCT).


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
