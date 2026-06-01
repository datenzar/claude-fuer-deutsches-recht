#!/usr/bin/env python3
"""
Schreibt Sidecar-Meta-Files (.meta) neben die 13 Beilagen der Thalvenia-Testakte.
Format: key: value Zeilen (kein HTML-Kommentar-Wrapper, weil eigenständige Datei).
"""
from pathlib import Path
import sys

AKTE = Path(__file__).resolve().parent.parent / "testakten" / "bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart"

# Wiederverwendbare Adressbloecke (semikolon-separiert, wie im Builder erwartet)
BAFIN_VBS4 = "Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin); Referat VBS 4 - Kreditinstitutsaufsicht Spezialinstitute; Graurheindorfer Str. 108; 53117 Bonn"
THALVENIA_VORSTAND = "Thalvenia Bank AG; Vorstand; Koenigstrasse 87; 70173 Stuttgart"
THALVENIA_RECHT = "Thalvenia Bank AG; Leiterin Rechtsabteilung Dr. Marit Hoffrath-Seel; Koenigstrasse 87; 70173 Stuttgart"
THALVENIA_CCO = "Thalvenia Bank AG; Chief Compliance Officer Anneke Birkenhainer; Koenigstrasse 87; 70173 Stuttgart"
KANZLEI = "Schwertbeck Roosendaal mbB Rechtsanwaelte; Prof. Dr. Heinrich Schwertbeck; Mainzer Landstrasse 172; 60327 Frankfurt am Main"
FIU = "Generalzolldirektion - Financial Intelligence Unit (FIU); Zentralstelle fuer Finanztransaktionsuntersuchungen; Carusufer 3-5; 01099 Dresden"
BNETZA = "Bundesnetzagentur; Referat 704 - Informationssicherheit kritischer Infrastrukturen; Tulpenfeld 4; 53113 Bonn"

# Liste aller Sidecars: (Pfad, Meta-Dict)
SIDECARS = [
    # ===== EMAILS =====
    ("emails/email-bafin-pruefungsmitteilung.eml", {
        "typ": "original_eingehend",
        "absender": BAFIN_VBS4,
        "adressat": THALVENIA_VORSTAND,
        "datum": "18. Maerz 2026, 09:22 Uhr",
        "az": "VBS 4 1 7-K-22-188/2026",
        "betreff": "Sonderpruefung gem. § 44 KWG - Pruefungsmitteilung",
        "eingangsstempel": "18.03.2026 09:47 Uhr (Eingang E-Mail, Geschaeftsstelle Vorstand)",
        "vertraulichkeit": "VERTRAULICH",
    }),
    ("emails/email-bnetza-cybersicherheits-zustaendigkeit.eml", {
        "typ": "original_eingehend",
        "absender": BNETZA,
        "adressat": THALVENIA_RECHT,
        "datum": "03. April 2026, 10:15 Uhr",
        "az": "BNetzA 7-K-2026-1847",
        "betreff": "Einstufung als KRITIS-Betreiber gem. BSI-KritisV - Auskunftsersuchen",
        "eingangsstempel": "03.04.2026 10:18 Uhr (Eingang E-Mail, Rechtsabteilung)",
        "vertraulichkeit": "VERTRAULICH",
    }),
    ("emails/email-cybersicherheits-vorfall-meldung-bait.eml", {
        "typ": "interner_vermerk",
        "absender": "Thalvenia Bank AG; Magnus Thorvaldsson (CISO); Koenigstrasse 87; 70173 Stuttgart",
        "adressat": "Thalvenia Bank AG; Vorstand / CRO / CCO / Leiterin Rechtsabteilung; Koenigstrasse 87; 70173 Stuttgart",
        "datum": "09. Januar 2026, 08:35 Uhr",
        "az": "CISO-2026-IT-NOTFALL-001",
        "betreff": "NOTFALL - IT-Sicherheitsvorfall Stufe 2 - Ransomware 09.01.2026",
        "vertraulichkeit": "STRENG VERTRAULICH - INTERN",
    }),
    ("emails/email-fiu-anfrage-stra.eml", {
        "typ": "original_eingehend",
        "absender": FIU,
        "adressat": THALVENIA_VORSTAND,
        "datum": "22. Februar 2026, 14:05 Uhr",
        "az": "2026-FIU-7711-TN",
        "betreff": "Auskunftsersuchen gem. § 30 GwG",
        "eingangsstempel": "22.02.2026 14:09 Uhr (Eingang E-Mail, Geschaeftsstelle Vorstand)",
        "vertraulichkeit": "VERTRAULICH - § 30 GwG",
    }),
    ("emails/email-vorstand-thalvenia-an-kanzlei.eml", {
        "typ": "mandantenkorrespondenz",
        "absender": "Thalvenia Bank AG; Dr. Cornelius Thalheim-Lattermann (Vorstandsvorsitzender); Koenigstrasse 87; 70173 Stuttgart",
        "adressat": KANZLEI,
        "datum": "18. Maerz 2026, 17:44 Uhr",
        "az": "CTL-2026-MANDAT-001",
        "betreff": "DRINGEND - BaFin Sonderpruefung - Mandatsanfrage",
        "vertraulichkeit": "ANWALTLICH PRIVILEGIERT",
    }),

    # ===== DOCX =====
    ("docx/compliance-handbuch-thalvenia-v3-3.docx", {
        "typ": "internes_dokument",
        "absender": "Thalvenia Bank AG; Compliance-Abteilung (CCO); Koenigstrasse 87; 70173 Stuttgart",
        "adressat": "Thalvenia Bank AG; Alle Mitarbeiterinnen und Mitarbeiter; Koenigstrasse 87; 70173 Stuttgart",
        "datum": "Stand: Oktober 2025 (Version 3.3)",
        "az": "Compliance-Handbuch Thalvenia v3.3",
        "betreff": "Compliance-Handbuch Thalvenia Bank AG - Vollversion",
        "vertraulichkeit": "VERTRAULICH - Nur fuer interne Verwendung",
    }),
    ("docx/pressemitteilung-entwurf.docx", {
        "typ": "entwurf",
        "absender": "Thalvenia Bank AG; Unternehmenskommunikation (i.A. Vorstand); Koenigstrasse 87; 70173 Stuttgart",
        "adressat": "Entwurfsfassung - Adressatenkreis Presse (offen)",
        "datum": "Entwurf, Datum offen (nach BaFin-Entscheid)",
        "az": "Thalvenia-PR-2026-BaFin-Entwurf",
        "betreff": "Pressemitteilung Entwurf - Massnahmen zur Compliance-Staerkung",
        "vertraulichkeit": "ENTWURF - NICHT ZUR VEROEFFENTLICHUNG",
    }),
    ("docx/stellungnahme-vorstand-thalvenia-bafin-pruefung.docx", {
        "typ": "original_ausgehend",
        "absender": KANZLEI + "; i.A. Thalvenia Bank AG",
        "adressat": BAFIN_VBS4 + "; z.Hd. Dr. Hannelore Koesters",
        "datum": "28. Juli 2026",
        "az": "SR-2026-FIN-0612",
        "ihr_zeichen": "VBS 4 1 7-K-22-188/2026",
        "betreff": "Stellungnahme des Vorstands zur BaFin-Anhoerung vom 14. Juli 2026 (Arbeitsfassung)",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH",
    }),

    # ===== XLSX =====
    ("xlsx/gwg-pflichten-katalog.xlsx", {
        "typ": "interner_vermerk",
        "absender": "Thalvenia Bank AG; Compliance-Abteilung (CCO Anneke Birkenhainer); Koenigstrasse 87; 70173 Stuttgart",
        "adressat": "Mandantenakte intern (Kanzlei Schwertbeck Roosendaal mbB)",
        "datum": "Stand: 15. Juli 2026",
        "az": "Compliance-GwG-Katalog-2026",
        "betreff": "Katalog der GwG-Pflichten und Erfuellungsstatus - Arbeitspapier Anhoerung",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH PRIVILEGIERT",
    }),
    ("xlsx/kundenidentifikation-kyc-mangelpruefung.xlsx", {
        "typ": "interner_vermerk",
        "absender": "Thalvenia Bank AG; Compliance-Abteilung / AML-Team; Koenigstrasse 87; 70173 Stuttgart",
        "adressat": "Mandantenakte intern (Kanzlei Schwertbeck Roosendaal mbB)",
        "datum": "Stand: 20. Juli 2026",
        "az": "KYC-Mangelpruefung-2026",
        "betreff": "Kundenidentifikation KYC - Mangelpruefung Stichprobe BaFin-Anhoerung",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH PRIVILEGIERT",
    }),

    # ===== PDFs =====
    ("pdfs/compliance-handbuch-thalvenia-auszug.pdf", {
        "typ": "internes_dokument",
        "absender": "Thalvenia Bank AG; Compliance-Abteilung (CCO); Koenigstrasse 87; 70173 Stuttgart",
        "adressat": "Thalvenia Bank AG; Alle Mitarbeiterinnen und Mitarbeiter; Koenigstrasse 87; 70173 Stuttgart",
        "datum": "Stand: Oktober 2025 (Version 3.3)",
        "az": "Compliance-Handbuch Thalvenia v3.3 - Auszug",
        "betreff": "Compliance-Handbuch Auszug Kap. 2 (AML/GwG) und Kap. 3 (BAIT)",
        "vertraulichkeit": "VERTRAULICH - Nur fuer interne Verwendung",
    }),
    ("pdfs/stellungnahme-bafin-final.pdf", {
        "typ": "original_ausgehend",
        "absender": KANZLEI + "; i.A. Thalvenia Bank AG",
        "adressat": BAFIN_VBS4 + "; z.Hd. Dr. Hannelore Koesters",
        "datum": "28. Juli 2026",
        "az": "SR-2026-FIN-0612",
        "ihr_zeichen": "VBS 4 1 7-K-22-188/2026",
        "betreff": "Stellungnahme Thalvenia Bank AG zur BaFin-Anhoerung - Endfassung",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH",
    }),

    # ===== JPG =====
    ("jpg/bafin-bonn-frankfurt-gebaeude.jpg", {
        "typ": "bild_dokumentation",
        "absender": "Thalvenia Bank AG; Rechtsabteilung (Bildmaterial Mandantenakte); Koenigstrasse 87; 70173 Stuttgart",
        "adressat": "Mandantenakte intern",
        "datum": "Aufgenommen: Maerz 2026",
        "az": "Bild-Doku Thalvenia BaFin-Verfahren Nr. 01",
        "betreff": "Foto: BaFin-Dienstsitz (Aussenansicht) - Hintergrundinformation Mandat",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH",
    }),
    ("jpg/compliance-dashboard-screenshot.jpg", {
        "typ": "bild_dokumentation",
        "absender": "Thalvenia Bank AG; Compliance-Abteilung (Screenshot interne Systeme); Koenigstrasse 87; 70173 Stuttgart",
        "adressat": "Mandantenakte intern (Kanzlei Schwertbeck Roosendaal mbB)",
        "datum": "Aufgenommen: 12. Juli 2026",
        "az": "Bild-Doku Compliance-Dashboard Nr. 02",
        "betreff": "Screenshot: Compliance-Dashboard SymphonyAI Sensa - Beleg Tier-2-Aktivierung",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH PRIVILEGIERT",
    }),
    ("jpg/thalvenia-hauptsitz-stuttgart.jpg", {
        "typ": "bild_dokumentation",
        "absender": "Thalvenia Bank AG; Unternehmenskommunikation; Koenigstrasse 87; 70173 Stuttgart",
        "adressat": "Mandantenakte intern",
        "datum": "Aufgenommen: 2025 (Bestandsbild)",
        "az": "Bild-Doku Thalvenia Hauptsitz Nr. 03",
        "betreff": "Foto: Thalvenia Bank AG Hauptsitz Stuttgart Koenigstrasse 87",
        "vertraulichkeit": "VERTRAULICH",
    }),
]


def render_sidecar(meta: dict) -> str:
    """Rendert ein Sidecar-File (key: value Zeilen)."""
    keys_ordered = ["typ", "absender", "adressat", "datum", "az", "ihr_zeichen",
                    "betreff", "eingangsstempel", "vertraulichkeit"]
    lines = []
    for k in keys_ordered:
        if k in meta:
            lines.append(f"{k}: {meta[k]}")
    return "\n".join(lines) + "\n"


def main():
    written = 0
    for rel_path, meta in SIDECARS:
        target = AKTE / rel_path
        if not target.exists():
            print(f"WARN: Beilage fehlt: {target}", file=sys.stderr)
            continue
        sidecar = target.with_suffix(target.suffix + ".meta")
        sidecar.write_text(render_sidecar(meta), encoding="utf-8")
        print(f"OK  {sidecar.relative_to(AKTE)}  ({meta['typ']})")
        written += 1
    print(f"\n=> {written}/{len(SIDECARS)} Sidecars geschrieben")


if __name__ == "__main__":
    main()
