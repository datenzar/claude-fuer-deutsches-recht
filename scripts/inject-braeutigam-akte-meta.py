#!/usr/bin/env python3
"""AKTE-META-Bloecke und Sidecars fuer Bräutigam-Fluggastrechte-Akte (Klasse C, Verbraucher).

Charakter:
- Verbraucherakte (FluggastrechteVO EG 261/2004)
- Mandantin: Familie Bräutigam-Zaytuna, Hamburg
- Gegnerin: Pacific Sky Airways GmbH
- Mischung aus Originalbelegen (Buchung, Quittungen Hotel/Taxi/Essen),
  ausgehender Korrespondenz (Mail an PSA), bildhafter Dokumentation (Bordkarten,
  handschriftlicher Notizzettel, WhatsApp-Screenshot),
  Vollmacht (Mandant -> Kanzlei), interne Mitschrift Anwaltsgespraech.
"""
from pathlib import Path
import re
import sys

AKTE = Path(__file__).resolve().parent.parent / "testakten" / "fluggastrechte-familie-braeutigam"

KANZLEI = "Kanzlei Mandantenakte intern; Sachgebiet Reise- und Fluggastrechte; Hamburg"
MANDANT = "Familie Dr. Sebastian Braeutigam und Yasmin Zaytuna-Braeutigam; Verbraucher; Hamburg"
MANDANT_SB = "Dr. Sebastian Braeutigam; Privatperson; Hamburg"
PSA = "Pacific Sky Airways GmbH; Kundenservice / Beschwerdemanagement; Flughafenstrasse 1-3; 60549 Frankfurt am Main"
HOTEL_BKK = "Moevenpick Hotel Suvarnabhumi Bangkok; Front Desk; 999 Bangna-Trad Km. 15; 10540 Samut Prakan, Thailand"

MD_META = {
    "Aufstellung_Auslagen.md": {
        "typ": "interner_vermerk", "absender": KANZLEI, "adressat": "Mandantenakte intern",
        "datum": "20. Mai 2026", "az": "Braeutigam-Zaytuna/EG261/Auslagen",
        "betreff": "Auslagenaufstellung Bangkok 11.-13.04.2026 - Vorschau",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "Bildbeschreibung_IMG_2451_Notizzettel_Bangkok.md": {
        "typ": "bild_dokumentation",
        "absender": MANDANT_SB,
        "adressat": "Mandantenakte intern (Kanzlei)",
        "datum": "11. April 2026, 22:47 Uhr Ortszeit Bangkok",
        "az": "Braeutigam/IMG-2451",
        "betreff": "Bildbeschreibung handschriftlicher Notizzettel Bangkok Suvarnabhumi Airport Gate D5",
        "vertraulichkeit": "VERTRAULICH",
    },
    "Chatverlauf_Yasmin_Leila_Bangkok.md": {
        "typ": "bild_dokumentation",
        "absender": "Yasmin Zaytuna-Braeutigam; Privatperson; Hamburg",
        "adressat": "Mandantenakte intern (Kanzlei)",
        "datum": "12. April 2026, 03:22 Uhr Ortszeit Bangkok",
        "az": "Braeutigam/Chat-Yasmin-Leila",
        "betreff": "WhatsApp-Screenshot Yasmin/Leila Bangkok - Beweismittel Stresssituation",
        "vertraulichkeit": "VERTRAULICH",
    },
    "Vollmacht_handschriftlich_Sebastian_Bräutigam.md": {
        "typ": "mandantenkorrespondenz",
        "absender": MANDANT_SB,
        "adressat": KANZLEI,
        "datum": "20. Mai 2026",
        "az": "Vollmacht-Braeutigam-20052026",
        "betreff": "Handschriftliche Vollmacht zur Geltendmachung Fluggastrechte EG 261",
        "vertraulichkeit": "VERTRAULICH - MANDATSGRUNDLAGE",
    },
}

SIDECARS = {
    "Aufstellung_Auslagen.xlsx": {
        "typ": "interner_vermerk", "absender": KANZLEI, "adressat": "Mandantenakte intern",
        "datum": "20. Mai 2026", "az": "Braeutigam-Zaytuna/EG261/Auslagen",
        "betreff": "Auslagenaufstellung Bangkok - Originaldatei",
        "vertraulichkeit": "VERTRAULICH - MANDANTENAKTE",
    },
    "Buchungsbestaetigung_PSA_4471.pdf": {
        "typ": "original_eingehend", "absender": PSA, "adressat": MANDANT,
        "datum": "14. November 2025", "az": "PSA-XK4LB7",
        "betreff": "Buchungsbestaetigung Pacific Sky Airways - Hin- und Rueckflug Bangkok",
        "eingangsstempel": "14.11.2025 (Eingang E-Mail, sebastian.braeutigam@archi-sb.de)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "Hotel_Bangkok_Quittung.pdf": {
        "typ": "original_eingehend", "absender": HOTEL_BKK, "adressat": MANDANT,
        "datum": "12. April 2026 (Aufenthalt 11.-12.04.2026)",
        "az": "BKK-MVK-2026-04-08847",
        "betreff": "Hotelrechnung Moevenpick Bangkok - Family Deluxe Room (1 Nacht)",
        "eingangsstempel": "12.04.2026 (Eingang an Rezeption, Beleg in Mandantenakte)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "Quittung_Essen_Bangkok.pdf": {
        "typ": "original_eingehend",
        "absender": "Restaurant Mango Tree; Soi Tantawan; 10500 Bangkok, Thailand",
        "adressat": MANDANT,
        "datum": "12. April 2026",
        "az": "MGT-2026-04-12-2284",
        "betreff": "Restaurantquittung Bangkok - Familienverpflegung Notaufenthalt",
        "eingangsstempel": "12.04.2026 (Beleg in Mandantenakte)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "Taxi_Flughafen_2x.pdf": {
        "typ": "original_eingehend",
        "absender": "Bangkok Airport Taxi Service; Suvarnabhumi Public Taxi; 10540 Samut Prakan, Thailand",
        "adressat": MANDANT,
        "datum": "11. und 13. April 2026",
        "az": "BKK-Taxi-2026-04",
        "betreff": "Taxi-Quittungen Flughafen Bangkok (Hin und Rueck zum Hotel)",
        "eingangsstempel": "11./13.04.2026 (Belege in Mandantenakte)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "Notiz_Sebastian.txt": {
        "typ": "interner_vermerk", "absender": KANZLEI, "adressat": "Mandantenakte intern",
        "datum": "20. Mai 2026, 10:30 Uhr (Telefonat)",
        "az": "Braeutigam/Mandantengespraech-20052026",
        "betreff": "Mitschrift Mandantengespraech Dr. Sebastian Braeutigam - Sachverhaltsschilderung",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH PRIVILEGIERT",
    },
    "Vollmacht_handschriftlich_Sebastian_Bräutigam.docx": {
        "typ": "mandantenkorrespondenz",
        "absender": MANDANT_SB, "adressat": KANZLEI,
        "datum": "20. Mai 2026", "az": "Vollmacht-Braeutigam-20052026",
        "betreff": "Vollmacht - Originaldatei DOCX (handschriftlich unterzeichnete Vorlage)",
        "vertraulichkeit": "VERTRAULICH - MANDATSGRUNDLAGE",
    },
    "bordkarten_hinflug_alle.pdf": {
        "typ": "bild_dokumentation",
        "absender": MANDANT,
        "adressat": "Mandantenakte intern (Kanzlei)",
        "datum": "Hinflug: 28. Maerz 2026",
        "az": "Braeutigam/Bordkarten-Hinflug",
        "betreff": "Bordkarten Hinflug Frankfurt-Bangkok (alle vier Familienmitglieder, gestempelt)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "bordkarten_rueckflug_nicht_gestempelt.pdf": {
        "typ": "bild_dokumentation",
        "absender": MANDANT,
        "adressat": "Mandantenakte intern (Kanzlei)",
        "datum": "Geplanter Rueckflug: 11. April 2026 (annulliert)",
        "az": "Braeutigam/Bordkarten-Rueckflug-annulliert",
        "betreff": "Bordkarten geplanter Rueckflug PSA 4472 - NICHT gestempelt (Annullierung)",
        "vertraulichkeit": "VERTRAULICH - BEWEISMITTEL",
    },
    "mailverlauf-mit-PSA.pdf": {
        "typ": "mandantenkorrespondenz",
        "absender": MANDANT_SB,
        "adressat": PSA,
        "datum": "12. April 2026 ff.",
        "az": "PSA-Buchung XK4LB7 / Annullierung PSA 4472",
        "betreff": "E-Mail-Korrespondenz Dr. Braeutigam gegen Pacific Sky Airways - Annullierung 11.04.2026",
        "vertraulichkeit": "VERTRAULICH",
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
