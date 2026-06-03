---
name: word-dokument-finish-und-layout
description: "Finalisiert juristische Word-Dokumente vor Versand. Prüft Formatvorlagen, Nummerierung, Inhaltsverzeichnis, Querverweise, Anlagen, Track Changes, Kommentare, Metadaten, PDF/beA-Tauglichkeit, Unterschriftenblock, Tabellen, Seitenumbrüche und optische Konsistenz. Liefert eine Versand-Checkliste und konkrete Reparaturanweisungen."
---

# Word-Dokument Finish und Layout

## Zweck

Dieser Skill ist die letzte Werkbank vor Versand. Er behandelt das Dokument als echtes Kanzlei-Artefakt: Es muss nicht nur rechtlich stimmen, sondern in Word sauber, stabil und versandfähig sein.

## Prüfblöcke

| Block | Prüffrage |
|---|---|
| Formatvorlagen | Sind Überschriften, Standardtext, Zitate, Definitionen und Anlagen über Styles gebaut? |
| Nummerierung | Läuft die Nummerierung stabil und ohne manuelle Brüche? |
| Querverweise | Sind Verweise als Felder oder wenigstens konsistent aktualisiert? |
| Inhaltsverzeichnis | Ist es vorhanden und aktualisiert, wenn das Dokument länger ist? |
| Track Changes | Ist klar, ob Markup sichtbar versendet wird oder eine Clean Version? |
| Kommentare | Sind interne Kommentare entfernt oder bewusst sichtbar? |
| Metadaten | Sind Autor, Pfade, Vorversionen und versteckte Inhalte geprüft? |
| Anlagen | Stimmen Anlagenbezeichnung, Anlagenverzeichnis und Textverweise überein? |
| Versandform | Word, PDF, PDF/A, beA, E-Mail oder Signing-Plattform? |

## Ablauf

1. Dokumenttyp und Versandweg bestimmen.
2. Word-Hygiene prüfen: Formatvorlagen, Nummerierung, Tabellen, Seitenumbrüche.
3. Juristische Versandhygiene prüfen: Anlagen, Vollmacht, Signaturblock, Fristen.
4. Markup-Status prüfen: Clean, Redline, Vergleichsdokument oder kommentierte Fassung.
5. Metadaten- und Vertraulichkeitscheck durchführen.
6. Versandfassung benennen.

## Dateinamenskonvention

Empfohlen:

```text
2026-05-30_Mandant_Gegner_Dokumenttyp_v03_clean.docx
2026-05-30_Mandant_Gegner_Dokumenttyp_v03_redline.docx
2026-05-30_Mandant_Gegner_Dokumenttyp_v03_signed.pdf
```

## Versand-Checkliste

- Felder aktualisiert.
- Inhaltsverzeichnis aktualisiert.
- Keine leeren Überschriften.
- Keine sichtbaren Platzhalter.
- Keine versehentlichen Kommentare.
- Markup-Status bewusst gewählt.
- Metadaten geprüft.
- Anlagen vollständig.
- Signaturblock korrekt.
- PDF geöffnet und visuell geprüft.

## Output

- Ampel pro Prüfblock.
- Reparaturliste in Reihenfolge der Dringlichkeit.
- Versand-Checkliste.
- Optional: kurze manuelle Reparaturanweisung für die Versandfassung.

## Querverweise

- `revisions-prozess-redlines-comparison`
- `finaler-writing-quality-gate`
- `verweis-und-querverweis-technik`


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
