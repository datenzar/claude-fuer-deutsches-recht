#!/usr/bin/env python3
"""Setzt AKTE-META-Bloecke an den Anfang der 22 MD-Stuecke der
Thalvenia-Testakte. Idempotent: ueberspringt Files, die bereits ein
AKTE-META haben.

Pilot fuer das authentischere Testakten-Layout. Wenn das Ergebnis gut ist,
wird dieses Skript auf weitere Testakten erweitert.
"""

from pathlib import Path
import re

REPO = Path(__file__).resolve().parent.parent
AKTE = REPO / "testakten" / "bafin-verfahren-kryptoverwahrung-thalvenia-bank-aufsichtsverletzung-stuttgart"

# Adressbloecke wiederverwendet
BAFIN = (
    "Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin); "
    "Referat VBS 4 - Bankenaufsicht Spezialinstitute; "
    "Marie-Curie-Str. 24-28; "
    "60439 Frankfurt am Main"
)
THALVENIA = (
    "Thalvenia Bank AG; Vorstand; "
    "Koenigstrasse 87; "
    "70173 Stuttgart"
)
KANZLEI = (
    "Schwertbeck Roosendaal mbB Rechtsanwaelte; "
    "Prof. Dr. Heinrich Schwertbeck; "
    "Mainzer Landstrasse 172; "
    "60327 Frankfurt am Main"
)
FIU = (
    "Generalzolldirektion - Zentralstelle fuer Finanztransaktionsuntersuchungen (FIU); "
    "Am Propsthof 78a; "
    "53121 Bonn"
)
STA_STUTTGART = (
    "Staatsanwaltschaft Stuttgart; "
    "Abteilung Wirtschaftsstrafsachen; "
    "Olgastrasse 2; "
    "70182 Stuttgart"
)
AUFSICHTSRAT = (
    "Thalvenia Bank AG; Aufsichtsrat; "
    "z.Hd. Dr. Friedwart Loehndorff (Vorsitz); "
    "Koenigstrasse 87; 70173 Stuttgart"
)

# Klassifizierung pro Stueck-Nummer
META = {
    "01": dict(
        typ="interner_vermerk",
        absender=KANZLEI,
        adressat="Aktenleitung intern; Az. SR-2026-FIN-0612; Mandat Thalvenia Bank AG",
        datum="20. Maerz 2026",
        az="SR-2026-FIN-0612",
        betreff="Mandatsuebernahme - Thalvenia Bank AG; BaFin-Sonderpruefung; Konfliktpruefung",
        vertraulichkeit="ANWALTLICH PRIVILEGIERT",
    ),
    "02": dict(
        typ="interner_vermerk",
        absender=KANZLEI,
        adressat="Mandatsakte SR-2026-FIN-0612",
        datum="22. Maerz 2026",
        az="SR-2026-FIN-0612 / Memo 02",
        betreff="Historische Kryptoverwahrungslizenz 2020 - Sachverhalt und Reichweite",
        vertraulichkeit="ANWALTLICH PRIVILEGIERT",
    ),
    "03": dict(
        typ="interner_vermerk",
        absender=KANZLEI,
        adressat="Mandatsakte SR-2026-FIN-0612",
        datum="24. Maerz 2026",
        az="SR-2026-FIN-0612 / Memo 03",
        betreff="MiCAR-Uebergangsregime Art. 143 VO (EU) 2023/1114 - Rechtsanalyse",
        vertraulichkeit="ANWALTLICH PRIVILEGIERT",
    ),
    "04": dict(
        typ="original_eingehend",
        absender=BAFIN,
        adressat=THALVENIA,
        datum="18. Maerz 2026",
        az="VBS 4 1 7-K-22-188/2026",
        betreff="Anordnung einer Sonderpruefung gem. Paragraph 44 Abs. 1 KWG i.V.m. Paragraph 44c KWG - Az. 188-K-22-2026",
        eingangsstempel="18.03.2026 09:47 Uhr (Einschreiben mit Rueckschein)",
        vertraulichkeit="VERTRAULICH",
    ),
    "05": dict(
        typ="interner_vermerk",
        absender=KANZLEI,
        adressat="Mandatsakte SR-2026-FIN-0612",
        datum="26. Maerz 2026",
        az="SR-2026-FIN-0612 / Memo 05",
        betreff="BaFin-Pruefungsschwerpunkte - Auswertung und Risikomatrix AML/Cybersecurity",
        vertraulichkeit="ANWALTLICH PRIVILEGIERT",
    ),
    "06": dict(
        typ="original_ausgehend",
        absender=THALVENIA,
        adressat=BAFIN,
        datum="13. Januar 2026",
        az="Thalvenia/BAIT-Vorfall-2026-001",
        ihr_zeichen="BAIT Tz. 55 Meldung",
        betreff="Meldung eines wesentlichen IT-Sicherheitsvorfalls gem. BAIT Tz. 55 - Cybervorfall vom 09.01.2026",
        vertraulichkeit="VERTRAULICH",
    ),
    "07": dict(
        typ="interner_vermerk",
        absender=KANZLEI,
        adressat="Mandatsakte SR-2026-FIN-0612",
        datum="28. Maerz 2026",
        az="SR-2026-FIN-0612 / Memo 07",
        betreff="AML/GwG-Pflichtenkatalog Paragraphen 4-12 GwG - Pruefraster fuer interne Selbstpruefung",
        vertraulichkeit="ANWALTLICH PRIVILEGIERT",
    ),
    "08": dict(
        typ="interner_vermerk",
        absender=KANZLEI,
        adressat="Mandatsakte SR-2026-FIN-0612",
        datum="02. April 2026",
        az="SR-2026-FIN-0612 / Memo 08",
        betreff="KYC-Mangelpruefung - Befund Stichprobe Hochrisikokunden",
        vertraulichkeit="ANWALTLICH PRIVILEGIERT",
    ),
    "09": dict(
        typ="interner_vermerk",
        absender=KANZLEI,
        adressat="Mandatsakte SR-2026-FIN-0612",
        datum="05. April 2026",
        az="SR-2026-FIN-0612 / Memo 09",
        betreff="PEP-Screening - Befund Lueckenanalyse 24 Monate",
        vertraulichkeit="ANWALTLICH PRIVILEGIERT",
    ),
    "10": dict(
        typ="interner_vermerk",
        absender=KANZLEI,
        adressat="Mandatsakte SR-2026-FIN-0612",
        datum="08. April 2026",
        az="SR-2026-FIN-0612 / Memo 10",
        betreff="STR-Meldungen FIU - Auswertung der nicht gemeldeten Verdachtsfaelle Token TN",
        vertraulichkeit="ANWALTLICH PRIVILEGIERT",
    ),
    "11": dict(
        typ="interner_vermerk",
        absender=KANZLEI,
        adressat="Mandatsakte SR-2026-FIN-0612",
        datum="12. April 2026",
        az="SR-2026-FIN-0612 / Memo 11",
        betreff="MAR-Marktmissbrauchsverdacht Eigenhandel Token TN - Rechtliche Bewertung Art. 15 MAR",
        vertraulichkeit="ANWALTLICH PRIVILEGIERT",
    ),
    "12": dict(
        typ="original_eingehend",
        absender=BAFIN,
        adressat=THALVENIA,
        datum="14. Juli 2026",
        az="VBS 4 1 7-K-22-188/2026",
        betreff="Anhoerung gem. Paragraph 28 VwVfG zum vorlaeufigen Pruefbericht; Frist 28. Juli 2026",
        eingangsstempel="14.07.2026 11:12 Uhr (Einschreiben mit Rueckschein)",
        vertraulichkeit="VERTRAULICH",
    ),
    "13": dict(
        typ="original_ausgehend",
        absender=KANZLEI,
        adressat=BAFIN,
        datum="28. Juli 2026",
        az="SR-2026-FIN-0612",
        ihr_zeichen="VBS 4 1 7-K-22-188/2026",
        betreff="Stellungnahme der Thalvenia Bank AG zur Anhoerung gem. Paragraph 28 VwVfG vom 14. Juli 2026",
        vertraulichkeit="VERTRAULICH",
    ),
    "14": dict(
        typ="interner_vermerk",
        absender=KANZLEI,
        adressat="Mandatsakte SR-2026-FIN-0612",
        datum="15. April 2026",
        az="SR-2026-FIN-0612 / Memo 14",
        betreff="MaRisk BA 2024 AT 4.3 / BTO 1.1 - Pruefung der Organisationspflichten",
        vertraulichkeit="ANWALTLICH PRIVILEGIERT",
    ),
    "15": dict(
        typ="interner_vermerk",
        absender=KANZLEI,
        adressat="Mandatsakte SR-2026-FIN-0612",
        datum="18. April 2026",
        az="SR-2026-FIN-0612 / Memo 15",
        betreff="Behoerdliche Zustaendigkeitsabgrenzung BaFin / FIU / BNetzA - Parallelverfahrenslandkarte",
        vertraulichkeit="ANWALTLICH PRIVILEGIERT",
    ),
    "16": dict(
        typ="interner_vermerk",
        absender=KANZLEI,
        adressat="Mandatsakte SR-2026-FIN-0612 - Sonderakte Strafverteidigung",
        datum="22. April 2026",
        az="SR-2026-FIN-0612 / Strafverfahren 13 Js 4481/26",
        betreff="Strafverfahren Dr. Tannenfels - Paragraph 261 StGB; Verteidigungsstrategie und Interessenkonflikt",
        vertraulichkeit="ANWALTLICH PRIVILEGIERT",
    ),
    "17": dict(
        typ="interner_vermerk",
        absender=KANZLEI,
        adressat="Mandatsakte SR-2026-FIN-0612",
        datum="25. April 2026",
        az="SR-2026-FIN-0612 / Memo 17",
        betreff="Sanktionsrahmen BaFin - Paragraph 56 GwG; Paragraph 60b GwG; Paragraph 6 KWG; Untersagungsrisiko",
        vertraulichkeit="ANWALTLICH PRIVILEGIERT",
    ),
    "18": dict(
        typ="interner_vermerk",
        absender=KANZLEI,
        adressat="Mandatsakte SR-2026-FIN-0612 - Vertraulich Vorstandsebene",
        datum="02. Mai 2026",
        az="SR-2026-FIN-0612 / Strategie 18",
        betreff="Vergleichs- und Settlement-Strategie BaFin - Undertakings und Meldepflichten",
        vertraulichkeit="ANWALTLICH PRIVILEGIERT",
    ),
    "19": dict(
        typ="entwurf",
        absender=THALVENIA,
        adressat="Oeffentlichkeit / Finanzpresse",
        datum="Entwurf - geplante Freigabe nach BaFin-Abstimmung",
        az="Thalvenia/Kommunikation/2026-PRE-019",
        betreff="Pressemitteilung - Entwurf; abstimmungspflichtig mit BaFin und Kanzlei",
        vertraulichkeit="VERTRAULICH - ENTWURFSSTUFE",
    ),
    "20": dict(
        typ="original_ausgehend",
        absender=THALVENIA,
        adressat=AUFSICHTSRAT,
        datum="15. Mai 2026",
        az="Thalvenia/AR-Bericht/2026-Q2-04",
        betreff="Bericht des Vorstands an den Aufsichtsrat gem. Paragraph 90 AktG - BaFin-Sonderpruefung",
        vertraulichkeit="VERTRAULICH - AUFSICHTSRAT",
    ),
    "21": dict(
        typ="interner_vermerk",
        absender=KANZLEI,
        adressat="Mandatsakte SR-2026-FIN-0612 - Remediation-Steuerungskreis",
        datum="20. Mai 2026",
        az="SR-2026-FIN-0612 / Remediation 21",
        betreff="100-Tage-Remediation-Roadmap - KPI-Matrix; Eskalationspfad; BaFin-Reporting",
        vertraulichkeit="VERTRAULICH",
    ),
    "22": dict(
        typ="interner_vermerk",
        absender=KANZLEI,
        adressat="Mandatsakte SR-2026-FIN-0612 - Vorstand und Aufsichtsrat",
        datum="10. August 2026",
        az="SR-2026-FIN-0612 / Abschlussvermerk",
        betreff="Anwaltlicher Abschlussvermerk - Zwischenstand vor BaFin-Entscheid",
        vertraulichkeit="ANWALTLICH PRIVILEGIERT - HOECHSTVERTRAULICH",
    ),
}


def fmt_meta(m: dict) -> str:
    keys_order = ["typ", "absender", "adressat", "datum", "az", "ihr_zeichen",
                  "betreff", "eingangsstempel", "vertraulichkeit"]
    lines = ["<!-- AKTE-META"]
    for k in keys_order:
        if k in m and m[k]:
            lines.append(f"{k}: {m[k]}")
    lines.append("-->")
    return "\n".join(lines) + "\n\n"


def main():
    changed = 0
    skipped = 0
    for nr, meta in META.items():
        # Datei finden, die mit nr beginnt
        candidates = list(AKTE.glob(f"{nr}-*.md"))
        if not candidates:
            print(f"  ! Keine Datei fuer Nr. {nr} gefunden")
            continue
        path = candidates[0]
        text = path.read_text(encoding="utf-8")
        if "<!-- AKTE-META" in text:
            skipped += 1
            print(f"  - {path.name}: hat bereits AKTE-META, ueberspringe")
            continue
        new_text = fmt_meta(meta) + text
        path.write_text(new_text, encoding="utf-8")
        changed += 1
        print(f"  + {path.name}: AKTE-META eingefuegt ({meta['typ']})")
    print(f"\nFertig: {changed} geaendert, {skipped} uebersprungen")


if __name__ == "__main__":
    main()
