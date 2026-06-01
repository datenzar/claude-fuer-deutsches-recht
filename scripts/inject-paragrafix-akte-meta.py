#!/usr/bin/env python3
"""AKTE-META-Bloecke und Sidecars fuer Paragrafix-Fortbestehensprognose-Akte.

Charakter:
- Restrukturierungsakte einer SaaS-GmbH (Legal-AI, Berlin)
- Mehrere echte Schriftstuecke: Comfort Letter (Earlybird), StaRUG-Hinweis (KMK/Steiglitz),
  Mietvertrag-Auszug (Heidestrasse 78 GbR), Kontoauszug Commerzbank, Rechnungen OpenAI/AWS
- Interne Memos: Sanierungsbausteine, Notiz GF Carolin, Term Sheet
- StB-Arbeitspapiere: Bilanz, BWA, SuSa, Cashflow, 13-Wochen-Liq, Mitarbeiterliste
"""
from pathlib import Path
import re
import sys

AKTE = Path(__file__).resolve().parent.parent / "testakten" / "fortbestehensprognose-paragrafix-gmbh"

KMK = "KMK Steuerberatungsgesellschaft mbH; StBin Dipl.-Bw. Claudia Steiglitz - zertifizierte Restrukturierungsberaterin (DGRV); Kurfuerstendamm 217; 10719 Berlin-Wilmersdorf"
PARAGRAFIX = "Paragrafix GmbH; Geschaeftsfuehrung Dr. Carolin Vogt-Hesselbach; Heidestrasse 78; 10557 Berlin"
PARAGRAFIX_INTERN = "Paragrafix GmbH; Mandantenakte intern (HRB 247841 B AG Charlottenburg); Heidestrasse 78; 10557 Berlin"
EARLYBIRD = "Earlybird Venture Capital GmbH & Co. KG; General Partner Frederik Schoening; Ritterstrasse 12; 10969 Berlin-Kreuzberg"
COMMERZBANK = "Commerzbank AG; Firmenkundenbetreuung Berlin-Mitte; Kaiserplatz 1; 60311 Frankfurt am Main"
HEIDE_GBR = "Heidestrasse 78 GbR; vertreten durch Immobilienverwaltung Steinweg; Heidestrasse 78; 10557 Berlin"
OPENAI = "OpenAI, L.L.C.; Billing Department; 3180 18th Street; 94110 San Francisco, CA, USA"
AWS = "Amazon Web Services EMEA SARL; Billing; 38 Avenue John F. Kennedy; L-1855 Luxembourg"

MD_META = {
    "01_Bilanz_HGB_31-12-2025.md": {
        "typ": "interner_vermerk", "absender": KMK, "adressat": PARAGRAFIX_INTERN,
        "datum": "Stichtag: 31. Dezember 2025", "az": "Paragrafix/12847/Bilanz-2025",
        "betreff": "Bilanz HGB per 31. Dezember 2025 - Vorschau",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "03_SuSa_30-04-2026.md": {
        "typ": "interner_vermerk", "absender": KMK, "adressat": PARAGRAFIX_INTERN,
        "datum": "Stichtag: 30. April 2026", "az": "Paragrafix/12847/SuSa-04-2026",
        "betreff": "Summen- und Saldenliste 30. April 2026 - Vorschau",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "04_Cashflow_Modell_Rollierend.md": {
        "typ": "interner_vermerk", "absender": KMK, "adressat": PARAGRAFIX_INTERN,
        "datum": "02. Mai 2026", "az": "Paragrafix/12847/CF-Modell",
        "betreff": "Cashflow-Modell rollierend - Eingabeparameter und Szenarien",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "05_Term_Sheet_Series_A_Tranche_2.md": {
        "typ": "entwurf", "absender": EARLYBIRD,
        "adressat": PARAGRAFIX,
        "datum": "Stand: April 2026 (non-binding)",
        "az": "Earlybird-Paragrafix Series-A T2",
        "betreff": "Non-Binding Term Sheet - Series A Financing Tranche 2 Disbursement Conditions",
        "vertraulichkeit": "VERTRAULICH - VERHANDLUNGSGRUNDLAGE",
    },
    "12_Liquiditaetsplanung_13_Wochen_KW18-KW30.md": {
        "typ": "interner_vermerk", "absender": KMK, "adressat": PARAGRAFIX_INTERN,
        "datum": "02. Mai 2026", "az": "Paragrafix/12847/LiqPlan-13W",
        "betreff": "Liquiditaetsplanung 13 Wochen KW 18-30/2026 (§ 17 InsO 3-Wochen-Test)",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "13_Sanierungsbausteine_Memo.md": {
        "typ": "interner_vermerk",
        "absender": "Paragrafix GmbH; Geschaeftsfuehrung Dr. Carolin Vogt-Hesselbach; Heidestrasse 78; 10557 Berlin",
        "adressat": "Paragrafix GmbH; Beirat / Investor Earlybird VC (intern); Heidestrasse 78; 10557 Berlin",
        "datum": "Q2 2026", "az": "Paragrafix-Sanierungsbausteine-Q2-2026",
        "betreff": "Internes Memorandum Sanierungsbausteine Q2 2026 - Vorbereitung Fortbestehensprognose § 19 Abs. 2 InsO",
        "vertraulichkeit": "STRENG VERTRAULICH - INTERN",
    },
    "15_Mitarbeiterliste_Stand_30-04-2026.md": {
        "typ": "interner_vermerk",
        "absender": "Paragrafix GmbH; People & Operations; Heidestrasse 78; 10557 Berlin",
        "adressat": PARAGRAFIX_INTERN,
        "datum": "Stand: 30. April 2026", "az": "Paragrafix-Personal-30042026",
        "betreff": "Mitarbeiterliste Paragrafix GmbH - Stand 30. April 2026 (anonymisiert)",
        "vertraulichkeit": "VERTRAULICH - PERSONALDATEN / DSGVO",
    },
}

SIDECARS = {
    "01_Bilanz_HGB_31-12-2025.xlsx": {
        "typ": "interner_vermerk", "absender": KMK, "adressat": PARAGRAFIX_INTERN,
        "datum": "Stichtag: 31. Dezember 2025", "az": "Paragrafix/12847/Bilanz-2025",
        "betreff": "Bilanz HGB 31. Dezember 2025 - Originaldatei",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "02_BWA_April_2026.pdf": {
        "typ": "interner_vermerk", "absender": KMK, "adressat": PARAGRAFIX_INTERN,
        "datum": "Stand: April 2026 (Monat 4/2026)", "az": "Paragrafix/12847/BWA-04-2026",
        "betreff": "Betriebswirtschaftliche Auswertung April 2026 (DATEV-Standard)",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "03_SuSa_30-04-2026.xlsx": {
        "typ": "interner_vermerk", "absender": KMK, "adressat": PARAGRAFIX_INTERN,
        "datum": "Stichtag: 30. April 2026", "az": "Paragrafix/12847/SuSa-04-2026",
        "betreff": "Summen- und Saldenliste 30. April 2026 - Originaldatei",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "04_Cashflow_Modell_Rollierend.xlsx": {
        "typ": "interner_vermerk", "absender": KMK, "adressat": PARAGRAFIX_INTERN,
        "datum": "02. Mai 2026", "az": "Paragrafix/12847/CF-Modell",
        "betreff": "Cashflow-Modell rollierend - Originaldatei",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "05_Term_Sheet_Series_A_Tranche_2.docx": {
        "typ": "entwurf", "absender": EARLYBIRD, "adressat": PARAGRAFIX,
        "datum": "Stand: April 2026 (non-binding)",
        "az": "Earlybird-Paragrafix Series-A T2",
        "betreff": "Non-Binding Term Sheet Series A Tranche 2 - Verhandlungsentwurf",
        "vertraulichkeit": "VERTRAULICH - VERHANDLUNGSGRUNDLAGE",
    },
    "06_Comfortletter_Earlybird_17-04-2026.pdf": {
        "typ": "original_eingehend", "absender": EARLYBIRD, "adressat": PARAGRAFIX,
        "datum": "17. April 2026", "az": "Earlybird-Paragrafix Comfort Letter 17.04.2026",
        "betreff": "Comfort Letter - Continued Investor Support - Series A Tranche 2",
        "eingangsstempel": "17.04.2026 (Eingang Geschaeftsfuehrung Dr. Vogt-Hesselbach)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "07_Hinweisschreiben_StaRUG_Steiglitz.pdf": {
        "typ": "original_eingehend", "absender": KMK, "adressat": PARAGRAFIX,
        "datum": "06. Mai 2026", "az": "KMK-Paragrafix-StaRUG-102-06052026",
        "betreff": "Hinweispflicht gem. § 102 StaRUG - Moegliche Insolvenzreife / erforderliche Massnahmen",
        "eingangsstempel": "06.05.2026 (Eingang per Einschreiben Rueckschein, Geschaeftsfuehrung)",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH / STBV § 57",
    },
    "08_Kontoauszug_Commerzbank_April_2026.pdf": {
        "typ": "original_eingehend", "absender": COMMERZBANK, "adressat": PARAGRAFIX,
        "datum": "30. April 2026", "az": "Commerzbank DE84-2004-0040-0512-3470-00 / April 2026",
        "betreff": "Kontoauszug Geschaeftskonto April 2026",
        "eingangsstempel": "Anfang Mai 2026 (Eingang elektronisch)",
        "vertraulichkeit": "VERTRAULICH - BANKDATEN",
    },
    "09_Rechnungen_LLM_April_2026.pdf": {
        "typ": "original_eingehend", "absender": OPENAI, "adressat": PARAGRAFIX,
        "datum": "30. April 2026", "az": "INV-OAI-2026-04-129847",
        "betreff": "Rechnung LLM-Nutzung April 2026 (OpenAI API)",
        "eingangsstempel": "30.04.2026 (Eingang per E-Mail, billing@paragrafix.de)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "10_AWS_Rechnung_April_2026.pdf": {
        "typ": "original_eingehend", "absender": AWS, "adressat": PARAGRAFIX,
        "datum": "01. Mai 2026 (fuer April 2026)", "az": "AWE-EMEA-EU-DE-2026-04-28471920",
        "betreff": "AWS Invoice April 2026 - Cloud-Infrastruktur",
        "eingangsstempel": "01.05.2026 (Eingang per E-Mail, billing@paragrafix.de)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "11_Mietvertrag_Auszug_Heidestrasse.pdf": {
        "typ": "internes_dokument", "absender": HEIDE_GBR, "adressat": PARAGRAFIX,
        "datum": "Vertragsdatum: 15. August 2023", "az": "MV Heidestr. 78 - Paragrafix GmbH",
        "betreff": "Auszug Gewerbemietvertrag Heidestrasse 78, Berlin - relevante Bestimmungen Fortbestehensprognose",
        "vertraulichkeit": "VERTRAULICH",
    },
    "12_Liquiditaetsplanung_13_Wochen_KW18-KW30.xlsx": {
        "typ": "interner_vermerk", "absender": KMK, "adressat": PARAGRAFIX_INTERN,
        "datum": "02. Mai 2026", "az": "Paragrafix/12847/LiqPlan-13W",
        "betreff": "13-Wochen-Liquiditaetsplanung KW 18-30/2026 - Originaldatei",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "13_Sanierungsbausteine_Memo.docx": {
        "typ": "interner_vermerk",
        "absender": "Paragrafix GmbH; Geschaeftsfuehrung Dr. Carolin Vogt-Hesselbach; Heidestrasse 78; 10557 Berlin",
        "adressat": "Paragrafix GmbH; Beirat / Investor Earlybird VC (intern); Heidestrasse 78; 10557 Berlin",
        "datum": "Q2 2026", "az": "Paragrafix-Sanierungsbausteine-Q2-2026",
        "betreff": "Sanierungsbausteine Memo - Originaldatei DOCX",
        "vertraulichkeit": "STRENG VERTRAULICH - INTERN",
    },
    "14_Notiz_GF_Carolin.txt": {
        "typ": "interner_vermerk",
        "absender": "Paragrafix GmbH; Dr. Carolin Vogt-Hesselbach (Geschaeftsfuehrerin); Heidestrasse 78; 10557 Berlin",
        "adressat": "Persoenliche Akte / Beirat (intern)",
        "datum": "14. Mai 2026, 17:42 Uhr",
        "az": "GF-Notiz-Telko-Earlybird-14052026",
        "betreff": "Persoenliche Notiz - Telko Frederik Schoening (Earlybird VC) zur Tranche 2",
        "vertraulichkeit": "STRENG VERTRAULICH - PERSOENLICH",
    },
    "15_Mitarbeiterliste_Stand_30-04-2026.xlsx": {
        "typ": "interner_vermerk",
        "absender": "Paragrafix GmbH; People & Operations; Heidestrasse 78; 10557 Berlin",
        "adressat": PARAGRAFIX_INTERN,
        "datum": "Stand: 30. April 2026", "az": "Paragrafix-Personal-30042026",
        "betreff": "Mitarbeiterliste - Originaldatei (anonymisiert)",
        "vertraulichkeit": "VERTRAULICH - PERSONALDATEN / DSGVO",
    },
}


def render_meta_block(meta: dict) -> str:
    keys_ordered = ["typ", "absender", "adressat", "datum", "az", "ihr_zeichen",
                    "betreff", "eingangsstempel", "vertraulichkeit"]
    lines = ["<!-- AKTE-META"]
    for k in keys_ordered:
        if k in meta: lines.append(f"{k}: {meta[k]}")
    lines.append("-->")
    return "\n".join(lines) + "\n\n"


def render_sidecar(meta: dict) -> str:
    keys_ordered = ["typ", "absender", "adressat", "datum", "az", "ihr_zeichen",
                    "betreff", "eingangsstempel", "vertraulichkeit"]
    return "\n".join(f"{k}: {meta[k]}" for k in keys_ordered if k in meta) + "\n"


AKTE_META_RE = re.compile(r"<!--\s*AKTE-META.*?-->\s*\n?", re.DOTALL)


def main():
    md_n = sc_n = 0
    for rel, meta in MD_META.items():
        target = AKTE / rel
        if not target.exists():
            print(f"WARN fehlt: {target}", file=sys.stderr); continue
        body = target.read_text(encoding="utf-8")
        if AKTE_META_RE.search(body):
            new = AKTE_META_RE.sub(render_meta_block(meta), body, count=1)
        else:
            new = render_meta_block(meta) + body
        target.write_text(new, encoding="utf-8")
        print(f"MD  {rel}  ({meta['typ']})"); md_n += 1
    for rel, meta in SIDECARS.items():
        target = AKTE / rel
        if not target.exists():
            print(f"WARN fehlt: {target}", file=sys.stderr); continue
        sidecar = target.with_suffix(target.suffix + ".meta")
        sidecar.write_text(render_sidecar(meta), encoding="utf-8")
        print(f"SC  {sidecar.relative_to(AKTE)}  ({meta['typ']})"); sc_n += 1
    print(f"\n=> {md_n} MD-Bloecke, {sc_n} Sidecars")


if __name__ == "__main__":
    main()
