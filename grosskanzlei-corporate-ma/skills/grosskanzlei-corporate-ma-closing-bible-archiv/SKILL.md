---
name: grosskanzlei-corporate-ma-closing-bible-archiv
description: "Closing Bible und Archiv: Erstellt Closing Bible, Versionierung, Signaturketten, Registerbelege und Deal-Archiv."
---

# Closing Bible und Archiv

## Zweck

Erstellt Closing Bible, Versionierung, Signaturketten, Registerbelege und Deal-Archiv.

## Arbeitsmodus

- Finale Dokumente, Anlagen, Signaturseiten und Nachweise sammeln.
- Index, Version, Datum, Parteien und Quelle erfassen.
- Fehlende Deliverables als Offenliste ausgeben.
- Archiv- und Zugriffskonzept dokumentieren.

## Rote Schwellen

- Unvollständige Signaturkette.
- Registerbeleg fehlt.
- Nicht finale Version im Closing Set.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/closing-bible-index.md
- assets/templates/closing-deliverables-register.md
