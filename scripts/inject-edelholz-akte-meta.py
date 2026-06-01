#!/usr/bin/env python3
"""Schreibt AKTE-META-Bloecke in MD-Stuecke und Sidecars fuer Beilagen
der Edelholz-Manufaktur-Berlin-Akte.

Charakter der Akte:
- Steuerberater-Mandantenakte (Falkenrieth & Partner StB)
- Vorbereitung Liquiditaetskrise, Insolvenzantragspflicht
- Fast keine Behoerdenkommunikation, dafuer interne StB-Analysen
- Bankauszuege als 'original_eingehend' (Bank an Mandantin)
- OPOS-Listen, BWA, SuSa als 'interner_vermerk' (StB-Arbeitspapiere)
"""
from pathlib import Path
import re
import sys

AKTE = Path(__file__).resolve().parent.parent / "testakten" / "beispielakte-edelholz-berlin"

STB = "Falkenrieth & Partner StB-Gesellschaft mbB; StB Dipl.-Kffr. Andrea Falkenrieth; Friedrichstrasse 142; 10117 Berlin-Mitte"
MANDANTIN = "Edelholz Manufaktur Berlin GmbH; Geschaeftsfuehrung Friedrich Korbach / Anouk Liesen; Koepenicker Strasse 187; 10997 Berlin"
SPARKASSE = "Berliner Sparkasse; Niederlassung Mitte; Alexanderplatz 2; 10178 Berlin"
COMMERZBANK = "Commerzbank AG; Filiale Berlin-Friedrichshain; Frankfurter Allee 32; 10247 Berlin"
FA = "Finanzamt Berlin-Friedrichshain-Kreuzberg; Schoenstedtstrasse 5; 12043 Berlin"

# === MD-Stuecke ===
MD_META = {
    "01_stammdaten/firmenstammblatt.md": {
        "typ": "interner_vermerk",
        "absender": STB,
        "adressat": "Mandantenakte intern (Falkenrieth & Partner StB)",
        "datum": "Stand: 30. April 2026",
        "az": "Edelholz/2026/Stammdaten",
        "betreff": "Firmenstammblatt - Edelholz Manufaktur Berlin GmbH",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "01_stammdaten/personalliste.md": {
        "typ": "interner_vermerk",
        "absender": STB,
        "adressat": "Mandantenakte intern (Falkenrieth & Partner StB)",
        "datum": "Stand: 30. April 2026",
        "az": "Edelholz/2026/Personal",
        "betreff": "Personalliste - Edelholz Manufaktur Berlin GmbH",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE / PERSONALDATEN",
    },
    "02_bwa/bwa_jan-apr_2026.md": {
        "typ": "interner_vermerk",
        "absender": STB,
        "adressat": "Mandantenakte intern (Falkenrieth & Partner StB)",
        "datum": "12. Mai 2026",
        "az": "Edelholz/2026/BWA-04",
        "betreff": "Betriebswirtschaftliche Auswertung Januar bis April 2026 - Vorschau",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "02_bwa/bwa_kommentar_april2026.md": {
        "typ": "mandantenkorrespondenz",
        "absender": STB,
        "adressat": MANDANTIN,
        "datum": "12. Mai 2026",
        "az": "Edelholz/2026/BWA-Kommentar-04",
        "betreff": "Kommentar zur BWA Januar bis April 2026 - Mandanteninformation",
        "vertraulichkeit": "VERTRAULICH - MANDANTENINFORMATION",
    },
    "03_susa/susa_30042026.md": {
        "typ": "interner_vermerk",
        "absender": STB,
        "adressat": "Mandantenakte intern (Falkenrieth & Partner StB)",
        "datum": "Stand: 30. April 2026",
        "az": "Edelholz/2026/SuSa-04",
        "betreff": "Summen- und Saldenliste per 30. April 2026 - Vorschau",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "05_bank/bankauszuege_q1_2026_auszug.md": {
        "typ": "original_eingehend",
        "absender": SPARKASSE + " // " + COMMERZBANK,
        "adressat": MANDANTIN,
        "datum": "Auszuege Februar bis April 2026",
        "az": "Edelholz/2026/Bank-Q1",
        "betreff": "Bankauszuege - Auszug Februar bis April 2026 (beide Konten)",
        "eingangsstempel": "Eingang StB Falkenrieth: laufend Q1/Q2 2026",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "06_steuern_sv/steuern_sv_lage.md": {
        "typ": "interner_vermerk",
        "absender": STB,
        "adressat": "Mandantenakte intern (Falkenrieth & Partner StB)",
        "datum": "Stand: 30. April 2026",
        "az": "Edelholz/2026/Steuern-SV-Lage",
        "betreff": "Steuern und Sozialversicherung - Statusbericht 30. April 2026",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE / STEUERGEHEIMNIS",
    },
    "07_auftraege/auftragsbestand.md": {
        "typ": "interner_vermerk",
        "absender": STB,
        "adressat": "Mandantenakte intern (Falkenrieth & Partner StB)",
        "datum": "Stand: 30. April 2026",
        "az": "Edelholz/2026/Auftragsbestand",
        "betreff": "Auftragsbestand und offene Rechnungen - Stand 30. April 2026",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "08_vertraege/vertraege_uebersicht.md": {
        "typ": "interner_vermerk",
        "absender": STB,
        "adressat": "Mandantenakte intern (Falkenrieth & Partner StB)",
        "datum": "Stand: 30. April 2026",
        "az": "Edelholz/2026/Vertraege",
        "betreff": "Vertraege und Daueraufstellungen - Uebersicht",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "liquiditaetsplan_edelholz.md": {
        "typ": "interner_vermerk",
        "absender": STB,
        "adressat": MANDANTIN,
        "datum": "18. Mai 2026",
        "az": "Edelholz/2026/LiqPlan-13W",
        "betreff": "Liquiditaetsplan 13 Wochen (Vorschau) - Stand 18. Mai 2026",
        "vertraulichkeit": "VERTRAULICH - MANDANTENINFORMATION",
    },
}

# === Sidecars fuer Beilagen ===
SIDECARS = {
    "02_bwa/bwa_jan-apr_2026.xlsx": {
        "typ": "interner_vermerk",
        "absender": STB,
        "adressat": "Mandantenakte intern (Falkenrieth & Partner StB)",
        "datum": "12. Mai 2026",
        "az": "Edelholz/2026/BWA-04",
        "betreff": "Betriebswirtschaftliche Auswertung Januar bis April 2026 - Originaldatei",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "03_susa/susa_30042026.xlsx": {
        "typ": "interner_vermerk",
        "absender": STB,
        "adressat": "Mandantenakte intern (Falkenrieth & Partner StB)",
        "datum": "Stand: 30. April 2026",
        "az": "Edelholz/2026/SuSa-04",
        "betreff": "Summen- und Saldenliste per 30. April 2026 - Originaldatei",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "04_offene_posten/opos_debitoren_30042026.csv": {
        "typ": "interner_vermerk",
        "absender": STB,
        "adressat": "Mandantenakte intern (Falkenrieth & Partner StB)",
        "datum": "Stand: 30. April 2026",
        "az": "Edelholz/2026/OPOS-Debitoren",
        "betreff": "Offene Posten Debitoren - Auszug 30. April 2026",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "04_offene_posten/opos_kreditoren_30042026.csv": {
        "typ": "interner_vermerk",
        "absender": STB,
        "adressat": "Mandantenakte intern (Falkenrieth & Partner StB)",
        "datum": "Stand: 30. April 2026",
        "az": "Edelholz/2026/OPOS-Kreditoren",
        "betreff": "Offene Posten Kreditoren - Auszug 30. April 2026",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "liquiditaetsplan_edelholz.xlsx": {
        "typ": "interner_vermerk",
        "absender": STB,
        "adressat": MANDANTIN,
        "datum": "18. Mai 2026",
        "az": "Edelholz/2026/LiqPlan-13W",
        "betreff": "Liquiditaetsplan 13 Wochen - Originaldatei",
        "vertraulichkeit": "VERTRAULICH - MANDANTENINFORMATION",
    },
}


def render_meta_block(meta: dict) -> str:
    keys_ordered = ["typ", "absender", "adressat", "datum", "az", "ihr_zeichen",
                    "betreff", "eingangsstempel", "vertraulichkeit"]
    lines = ["<!-- AKTE-META"]
    for k in keys_ordered:
        if k in meta:
            lines.append(f"{k}: {meta[k]}")
    lines.append("-->")
    return "\n".join(lines) + "\n\n"


def render_sidecar(meta: dict) -> str:
    keys_ordered = ["typ", "absender", "adressat", "datum", "az", "ihr_zeichen",
                    "betreff", "eingangsstempel", "vertraulichkeit"]
    lines = []
    for k in keys_ordered:
        if k in meta:
            lines.append(f"{k}: {meta[k]}")
    return "\n".join(lines) + "\n"


AKTE_META_RE = re.compile(r"<!--\s*AKTE-META.*?-->\s*\n?", re.DOTALL)


def main():
    md_written = 0
    sc_written = 0
    for rel, meta in MD_META.items():
        target = AKTE / rel
        if not target.exists():
            print(f"WARN fehlt: {target}", file=sys.stderr); continue
        body = target.read_text(encoding="utf-8")
        # Falls schon AKTE-META vorhanden, ersetze, sonst voranstellen
        if AKTE_META_RE.search(body):
            new = AKTE_META_RE.sub(render_meta_block(meta), body, count=1)
        else:
            new = render_meta_block(meta) + body
        target.write_text(new, encoding="utf-8")
        print(f"MD  {rel}  ({meta['typ']})")
        md_written += 1

    for rel, meta in SIDECARS.items():
        target = AKTE / rel
        if not target.exists():
            print(f"WARN fehlt: {target}", file=sys.stderr); continue
        sidecar = target.with_suffix(target.suffix + ".meta")
        sidecar.write_text(render_sidecar(meta), encoding="utf-8")
        print(f"SC  {sidecar.relative_to(AKTE)}  ({meta['typ']})")
        sc_written += 1

    print(f"\n=> {md_written} MD-Bloecke, {sc_written} Sidecars")


if __name__ == "__main__":
    main()
