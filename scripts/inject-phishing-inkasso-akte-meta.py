#!/usr/bin/env python3
"""AKTE-META-Bloecke und Sidecars fuer Phishing- und Inkasso-Testakten.

Phishing-Akte (Mayer ./. Sparkasse Berlin):
- Originalbriefe (Sparkasse, Anwalt Brezelmann, Ombudsmann/DSGV)
- Interne Vermerke (Aktennotiz, Kontovertrag-Auszug, Internes Rechtsgutachten)
- Bewertungs-MDs (Erstbewertung 675u/v, Ampel, Bankpflichten, Klagepfad)
- Beweismittel (Screenshots, Strafanzeige, eV, Zeugenaussage, Kontoauszuege)

Inkasso-Akte (ModeFuchs ./. von Altenhausen):
- Kette Rechnung -> Mahnungen -> Abtretung -> Inkasso -> Anwalt -> Mahnbescheid -> Klage
- 28 PDFs, 4 MDs, 2 CSVs
"""
from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parent.parent
PHISH = REPO / "testakten" / "phishing-vorfall-mayer-sparkasse-berlin"
INKASSO = REPO / "testakten" / "inkasso-zahlungsklage-modefuchs"

# === Adressbloecke Phishing ===
SPK = "Sparkasse Berlin; Abteilung Zahlungsverkehr / Schadensbearbeitung; Alexanderplatz 2; 10178 Berlin"
SPK_RECHT = "Sparkasse Berlin; Abteilung Recht und Compliance - Direktor Dr. jur. Friedrich Steinberg; Alexanderplatz 2; 10178 Berlin"
MAYER = "Peter Mayer; Privatperson; Lietzenburger Strasse 74; 10719 Berlin"
KANZLEI_BB = "Kanzlei Brezelmann & Partner Rechtsanwaelte; Fachanwaelte fuer Bank- und Kapitalmarktrecht; Kurfuerstendamm 195; 10707 Berlin"
DSGV = "Kundenbeschwerdestelle beim Deutschen Sparkassen- und Giroverband e.V.; Schlichter Dr. h.c. Wolfgang Reiter; Charlottenstrasse 47; 10117 Berlin"
LG_BERLIN = "Landgericht Berlin; 4. Zivilkammer; Tegeler Weg 17-21; 10589 Berlin"
STA_BERLIN = "Staatsanwaltschaft Berlin; Abteilung Cybercrime; Turmstrasse 91; 10559 Berlin"
KANZLEI_INTERN = KANZLEI_BB + " (intern, Mandantenakte 2025-B-0478)"

PHISH_MD = {
    "00_aktenuebersicht.md": {
        "typ": "interner_vermerk", "absender": KANZLEI_BB,
        "adressat": "Mandantenakte intern (Kanzlei Brezelmann & Partner)",
        "datum": "Stand: laufend (Akte 2025-B-0478)", "az": "2025-B-0478 / LG Berlin 4 O 218/25",
        "betreff": "Aktenuebersicht Mayer ./. Sparkasse Berlin - Stammdaten und Originalunterlagen",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH PRIVILEGIERT",
    },
    "04_erstbewertung_675u_675v.md": {
        "typ": "interner_vermerk", "absender": KANZLEI_BB,
        "adressat": "Mandantenakte intern (Kanzlei Brezelmann & Partner)",
        "datum": "Erstbewertung Juni 2025", "az": "2025-B-0478/Erstbewertung",
        "betreff": "Erstbewertung Anspruchsgrundlagen § 675u BGB und Einwand § 675v BGB",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH PRIVILEGIERT",
    },
    "05_grobe_fahrlaessigkeit_ampel.md": {
        "typ": "interner_vermerk", "absender": KANZLEI_BB,
        "adressat": "Mandantenakte intern (Kanzlei Brezelmann & Partner)",
        "datum": "Juni 2025", "az": "2025-B-0478/Ampel-grobe-Fahrlaessigkeit",
        "betreff": "Bewertungsampel grobe Fahrlaessigkeit gem. § 675v Abs. 3 BGB",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH PRIVILEGIERT",
    },
    "06_bankpflichten_und_tech_logs.md": {
        "typ": "interner_vermerk", "absender": KANZLEI_BB,
        "adressat": "Mandantenakte intern (Kanzlei Brezelmann & Partner)",
        "datum": "Juni/Juli 2025", "az": "2025-B-0478/Bankpflichten",
        "betreff": "Bankpflichten und Auswertung technischer Logs (Art. 97 PSD2, pushTAN)",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH PRIVILEGIERT",
    },
    "07_ombudsmann_und_klagepfad.md": {
        "typ": "interner_vermerk", "absender": KANZLEI_BB,
        "adressat": "Mandantenakte intern (Kanzlei Brezelmann & Partner)",
        "datum": "Juli/August 2025", "az": "2025-B-0478/Klagepfad",
        "betreff": "Ombudsmann-Verfahren und Strategiepfad zur Klage LG Berlin",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH PRIVILEGIERT",
    },
}

PHISH_SIDECARS = {
    "02_transaktionsmatrix.csv": {
        "typ": "interner_vermerk", "absender": KANZLEI_BB,
        "adressat": "Mandantenakte intern", "datum": "Stand: 2025",
        "az": "2025-B-0478/Transaktionsmatrix",
        "betreff": "Transaktionsmatrix Phishing-Vorfall 28.05.2025",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH PRIVILEGIERT",
    },
    "03_beweis_und_log_matrix.csv": {
        "typ": "interner_vermerk", "absender": KANZLEI_BB,
        "adressat": "Mandantenakte intern", "datum": "Stand: 2025",
        "az": "2025-B-0478/Beweis-Log",
        "betreff": "Beweis- und Log-Matrix - Zuordnung Belege zu Sachverhaltspunkten",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH PRIVILEGIERT",
    },
    "originale/01_Aktendeckblatt.pdf": {
        "typ": "internes_dokument", "absender": KANZLEI_BB,
        "adressat": "Mandantenakte intern", "datum": "Anlage Mandat 2025",
        "az": "2025-B-0478/Aktendeckblatt",
        "betreff": "Aktendeckblatt Mayer ./. Sparkasse Berlin",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/02_Vollmacht_und_Mandatsvertrag.pdf": {
        "typ": "mandantenkorrespondenz", "absender": MAYER, "adressat": KANZLEI_BB,
        "datum": "Mai/Juni 2025", "az": "2025-B-0478/Vollmacht",
        "betreff": "Vollmacht und Mandatsvertrag - Peter Mayer an Kanzlei Brezelmann & Partner",
        "vertraulichkeit": "VERTRAULICH - MANDATSGRUNDLAGE",
    },
    "originale/03_Kontovertrag_und_AGB.pdf": {
        "typ": "internes_dokument", "absender": SPK, "adressat": MAYER,
        "datum": "Vertragsbestand 2025", "az": "Kundennummer 478-239-561",
        "betreff": "Kontovertrag und AGB Sparkasse Berlin - Auszug Mandantenakte",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/04_Sonderbedingungen_pushTAN.pdf": {
        "typ": "internes_dokument", "absender": SPK, "adressat": MAYER,
        "datum": "Vertragsbestand 2025", "az": "Kundennummer 478-239-561 / pushTAN",
        "betreff": "Sonderbedingungen pushTAN-Verfahren - Pflichten und Regeln",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/05_Aktennotiz_Erstkontakt.pdf": {
        "typ": "interner_vermerk", "absender": KANZLEI_BB,
        "adressat": "Mandantenakte intern", "datum": "Mai/Juni 2025",
        "az": "2025-B-0478/Erstkontakt",
        "betreff": "Aktennotiz Erstkontakt Mandant - Sachverhaltsschilderung Phishing",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH PRIVILEGIERT",
    },
    "originale/06_Email_Mayer_an_Sparkasse_280525.pdf": {
        "typ": "original_ausgehend", "absender": MAYER, "adressat": SPK,
        "datum": "28. Mai 2025", "az": "Schadensmeldung Mayer 28.05.2025",
        "betreff": "Erste Reklamation / Schadensmeldung nicht autorisierter Zahlungsvorgaenge",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/07_Ablehnungsschreiben_Sparkasse_020625.pdf": {
        "typ": "original_eingehend", "absender": SPK + " - Assessor jur. Thomas Krueger", "adressat": MAYER,
        "datum": "02. Juni 2025", "az": "SB-2025/KR-44782", "ihr_zeichen": "E-Mail vom 28.05.2025",
        "betreff": "Ihre Schadensmeldung vom 28.05.2025 - Ablehnung der Erstattungsansprueche",
        "eingangsstempel": "Anfang Juni 2025 (Eingang Mandant, an Kanzlei weitergeleitet)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/08_Email_Mayer_an_Sparkasse_030625.pdf": {
        "typ": "original_ausgehend", "absender": MAYER, "adressat": SPK,
        "datum": "03. Juni 2025", "az": "Gegendarstellung Mayer 03.06.2025",
        "ihr_zeichen": "SB-2025/KR-44782",
        "betreff": "Gegendarstellung zur Ablehnung vom 02.06.2025",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/09_Zweites_Ablehnungsschreiben_Sparkasse_050625.pdf": {
        "typ": "original_eingehend", "absender": SPK, "adressat": MAYER,
        "datum": "05. Juni 2025", "az": "SB-2025/KR-44782-2",
        "ihr_zeichen": "Ihre E-Mail vom 03.06.2025",
        "betreff": "Endgueltige Ablehnung der Erstattungsansprueche - Schadensmeldung 28.05.2025",
        "eingangsstempel": "Anfang Juni 2025 (Eingang Mandant, an Kanzlei)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/10_Email_Mayer_an_Freund_290525.pdf": {
        "typ": "mandantenkorrespondenz",
        "absender": MAYER,
        "adressat": "Privatperson (Freund); kein Geschaeftsverkehr",
        "datum": "29. Mai 2025",
        "az": "Beweismittel - zeitnaher Sachverhaltsbericht",
        "betreff": "E-Mail Peter Mayer an Freund - zeitnaher Bericht zum Phishing-Vorfall",
        "vertraulichkeit": "VERTRAULICH - BEWEISMITTEL",
    },
    "originale/11_Screenshots_Phishing.pdf": {
        "typ": "bild_dokumentation", "absender": MAYER, "adressat": "Mandantenakte intern (Kanzlei)",
        "datum": "Mai 2025", "az": "2025-B-0478/Screenshots",
        "betreff": "Screenshots und Anrufanzeige Phishing-Vorfall 28.05.2025",
        "vertraulichkeit": "VERTRAULICH - BEWEISMITTEL",
    },
    "originale/12_Internes_Rechtsgutachten_Sparkasse.pdf": {
        "typ": "interner_vermerk", "absender": SPK_RECHT,
        "adressat": "Sparkasse Berlin intern (Abteilung Recht und Compliance)",
        "datum": "Juni 2025", "az": "SB-2025/Rechtsgutachten-44782",
        "betreff": "Internes Rechtsgutachten Sparkasse Berlin - Bankposition Mayer-Fall",
        "vertraulichkeit": "VERTRAULICH - INTERN SPARKASSE (Akteneinsicht)",
    },
    "originale/13_Anwaltsschreiben_an_Sparkasse_100625.pdf": {
        "typ": "original_ausgehend",
        "absender": KANZLEI_BB + " - RA Dr. Marcus Brezelmann",
        "adressat": SPK,
        "datum": "10. Juni 2025", "az": "2025-B-0478", "ihr_zeichen": "SB-2025/KR-44782",
        "betreff": "Aufforderung zur Erstattung gem. § 675u BGB - Mayer ./. Sparkasse Berlin",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH",
    },
    "originale/14_Antwort_Sparkasse_auf_Anwalt_200625.pdf": {
        "typ": "original_eingehend", "absender": SPK_RECHT, "adressat": KANZLEI_BB,
        "datum": "20. Juni 2025", "az": "SB-2025/ST-44782-2", "ihr_zeichen": "2025-B-0478",
        "betreff": "Zurueckweisung der Erstattungsforderung - Schadensfall Peter Mayer",
        "eingangsstempel": "ca. 23.06.2025 (Eingang Kanzlei Brezelmann & Partner)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/15_Antrag_Ombudsmann_010725.pdf": {
        "typ": "original_ausgehend",
        "absender": KANZLEI_BB + " - RA Dr. Marcus Brezelmann i.A. Peter Mayer",
        "adressat": DSGV,
        "datum": "01. Juli 2025", "az": "2025-B-0478",
        "betreff": "Schlichtungsantrag Mayer ./. Sparkasse Berlin gem. § 14 UKlaG",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/16_Schlichtungsvorschlag_Ombudsmann_150825.pdf": {
        "typ": "original_eingehend", "absender": DSGV, "adressat": KANZLEI_BB + " // " + SPK,
        "datum": "15. August 2025", "az": "S-2025/07-0891",
        "ihr_zeichen": "2025-B-0478 (Beschwerdefuehrer) / SB-2025/ST-44782-2 (Bank)",
        "betreff": "Schlichtungsvorschlag (70/30) gem. § 10 Verfahrensordnung DSGV-Kundenbeschwerdestelle",
        "eingangsstempel": "ca. 18.08.2025 (Eingang Kanzlei und Sparkasse)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/17_Kontoauszuege.pdf": {
        "typ": "original_eingehend", "absender": SPK, "adressat": MAYER,
        "datum": "Mai/Juni 2025", "az": "DE89 1005 0000 0478 2395 42",
        "betreff": "Kontoauszuege Mayer Mai/Juni 2025 - Belegung Schadenspositionen",
        "eingangsstempel": "laufend (elektronisch)",
        "vertraulichkeit": "VERTRAULICH - BANKDATEN",
    },
    "originale/18_Strafanzeige_Bescheinigung.pdf": {
        "typ": "original_eingehend", "absender": STA_BERLIN, "adressat": MAYER,
        "datum": "29. Mai 2025", "az": "STA Berlin Az. 234 Js 1788/25",
        "betreff": "Bescheinigung Strafanzeige Phishing - Aktenzeichen Eingang",
        "eingangsstempel": "29.05.2025 (Bestaetigung am Tage der Anzeige)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/19_Eidesstattliche_Versicherung_Mayer.pdf": {
        "typ": "mandantenkorrespondenz", "absender": MAYER,
        "adressat": LG_BERLIN + " (via Kanzlei Brezelmann & Partner)",
        "datum": "September 2025", "az": "2025-B-0478/eV-Mayer",
        "betreff": "Eidesstattliche Versicherung Peter Mayer - Phishing-Vorfall 28.05.2025",
        "vertraulichkeit": "VERTRAULICH - BEWEISMITTEL",
    },
    "originale/20_Zeugenaussage_Kollegin.pdf": {
        "typ": "mandantenkorrespondenz",
        "absender": "Zeugin Frau Kollegin (Klarname in Akte); persoenliche Stellungnahme",
        "adressat": KANZLEI_BB,
        "datum": "Juni 2025", "az": "2025-B-0478/Zeugin",
        "betreff": "Schriftliche Zeugenaussage - Beobachtung der Drucksituation am 28.05.2025",
        "vertraulichkeit": "VERTRAULICH - BEWEISMITTEL",
    },
    "originale/21_Klageschrift_mit_Anlagen.pdf": {
        "typ": "original_ausgehend",
        "absender": KANZLEI_BB + " - RA Dr. Marcus Brezelmann i.A. Peter Mayer",
        "adressat": LG_BERLIN,
        "datum": "15. September 2025", "az": "2025-B-0478",
        "betreff": "Klageschrift Mayer ./. Sparkasse Berlin - Erstattung nicht autorisierter Zahlungsvorgaenge",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH",
    },
    "originale/22_Klageerwiderung_Sparkasse.pdf": {
        "typ": "original_eingehend",
        "absender": "Sparkasse Berlin; Justitiariat; Alexanderplatz 2; 10178 Berlin",
        "adressat": LG_BERLIN + " // " + KANZLEI_BB,
        "datum": "Oktober 2025", "az": "LG Berlin 4 O 218/25",
        "ihr_zeichen": "2025-B-0478",
        "betreff": "Klageerwiderung Sparkasse Berlin im Verfahren Mayer ./. Sparkasse Berlin",
        "eingangsstempel": "ca. November 2025 (Eingang Kanzlei via Gericht)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/23_Sicherheitshinweis_Sparkasse_150125.pdf": {
        "typ": "original_eingehend", "absender": SPK, "adressat": MAYER,
        "datum": "15. Januar 2025", "az": "SB-Sicherheitshinweis-2025-01",
        "betreff": "Sicherheitshinweis Sparkasse Berlin - Phishing- und Spoofing-Warnung (vor Vorfall)",
        "eingangsstempel": "Januar 2025 (Eingang Mandant)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/24_Technisches_Protokoll_TAN.pdf": {
        "typ": "internes_dokument", "absender": SPK + " - IT-Forensik",
        "adressat": "Akte LG Berlin 4 O 218/25 (via Sparkasse Justitiariat)",
        "datum": "Mai 2025 (Auswertung)", "az": "SB-IT-Forensik-TAN-44782",
        "betreff": "Technisches Protokoll TAN/IP/Device zur streitgegenstaendlichen Transaktion",
        "vertraulichkeit": "VERTRAULICH - BANK-INTERN (Akteneinsicht)",
    },
}

# === Adressbloecke Inkasso ===
MODEFUCHS = "ModeFuchs GmbH; Geschaeftsfuehrer Friedrich-Heinrich von Streithofen; Kaiserplatz 12; 10002 Musterstadt"
INKASSO_GMBH = "InkassoZentrale GmbH; Geschaeftsfuehrer Dr. Marvin Rueter / Constanze Lehnhardt; Friedrich-Krause-Ufer 42; 13353 Berlin"
ALTENHAUSEN_ALT = "Gottlieb von Altenhausen; Privatperson; Kaiserstrasse 47; 90403 Nuernberg"
ALTENHAUSEN_NEU = "Gottlieb von Altenhausen; Privatperson; Lorenzer Strasse 3; 90402 Nuernberg"
KANZLEI_BC = "Kanzlei Brezelmann & Collegen Rechtsanwaelte; Fachanwalt fuer Zivilrecht RA Dr. Hubertus Brezelmann; Maximilianstrasse 28; 90402 Nuernberg"
AG_WEDDING = "Amtsgericht Berlin-Wedding; Mahngericht; Brunnenplatz 1; 13357 Berlin"
AG_NUERNBERG = "Amtsgericht Nuernberg; Zivilabteilung; Fuerther Strasse 110; 90429 Nuernberg"

INKASSO_MD = {
    "00_aktenuebersicht.md": {
        "typ": "interner_vermerk", "absender": KANZLEI_BC,
        "adressat": "Mandantenakte intern (Kanzlei Brezelmann & Collegen)",
        "datum": "Stand: laufend (Akte BRZ-2025-447-MF)", "az": "BRZ-2025-447-MF",
        "betreff": "Aktenuebersicht ModeFuchs ./. von Altenhausen - Beteiligte, Forderung, Zeitstrahl",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH PRIVILEGIERT",
    },
    "04_klagefreigabe.md": {
        "typ": "interner_vermerk", "absender": KANZLEI_BC,
        "adressat": "Mandantenakte intern", "datum": "Sommer 2025", "az": "BRZ-2025-447-MF/Klagefreigabe",
        "betreff": "Klagefreigabe und Bewertung Erfolgsaussichten Verteidigung",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH PRIVILEGIERT",
    },
    "05_gerichtsort_pruefung.md": {
        "typ": "interner_vermerk", "absender": KANZLEI_BC,
        "adressat": "Mandantenakte intern", "datum": "Sommer 2025", "az": "BRZ-2025-447-MF/Gerichtsort",
        "betreff": "Pruefung oertliche Zustaendigkeit (Verbraucher, §§ 12, 13 ZPO, § 29c ZPO)",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH PRIVILEGIERT",
    },
    "06_korrigierter_klageauftrag.md": {
        "typ": "interner_vermerk", "absender": KANZLEI_BC,
        "adressat": "Mandantenakte intern", "datum": "Sommer 2025",
        "az": "BRZ-2025-447-MF/Klageauftrag-korrigiert",
        "betreff": "Korrigierter Klageauftrag - korrigierte Verteidigungsstrategie",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH PRIVILEGIERT",
    },
    "07_fehleranalyse_vorhandene_klage.md": {
        "typ": "interner_vermerk", "absender": KANZLEI_BC,
        "adressat": "Mandantenakte intern", "datum": "August 2025",
        "az": "BRZ-2025-447-MF/Fehleranalyse",
        "betreff": "Fehleranalyse der vorhandenen Klageschrift der InkassoZentrale",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH PRIVILEGIERT",
    },
}

INKASSO_SIDECARS = {
    "02_mahnlauf_modefuchs.csv": {
        "typ": "interner_vermerk", "absender": KANZLEI_BC,
        "adressat": "Mandantenakte intern", "datum": "Stand: 2025",
        "az": "BRZ-2025-447-MF/Mahnlauf",
        "betreff": "Mahnlauf ModeFuchs - tabellarische Aufstellung",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH PRIVILEGIERT",
    },
    "03_anspruchsmatrix_modefuchs.csv": {
        "typ": "interner_vermerk", "absender": KANZLEI_BC,
        "adressat": "Mandantenakte intern", "datum": "Stand: 2025",
        "az": "BRZ-2025-447-MF/Anspruchsmatrix",
        "betreff": "Anspruchsmatrix - Pruefung Haupt- und Nebenforderungen",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH PRIVILEGIERT",
    },
    "originale/00_Aktenverzeichnis_ModeFuchs.pdf": {
        "typ": "internes_dokument", "absender": KANZLEI_BC, "adressat": "Mandantenakte intern",
        "datum": "Stand: 2025", "az": "BRZ-2025-447-MF/Aktenverzeichnis",
        "betreff": "Aktenverzeichnis ModeFuchs-Akte (Anlage 0)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/01_Bestellbestaetigung_03-04-2025.pdf": {
        "typ": "original_eingehend", "absender": MODEFUCHS, "adressat": ALTENHAUSEN_ALT,
        "datum": "03. April 2025", "az": "ModeFuchs-Bestellung-2025-04-03",
        "betreff": "Bestellbestaetigung Cashmere-Mantel Aurelia / Lederhandtasche Noa",
        "eingangsstempel": "03.04.2025 (Eingang E-Mail beim Kunden)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/02_Versandbestaetigung_06-04-2025.pdf": {
        "typ": "original_eingehend", "absender": MODEFUCHS, "adressat": ALTENHAUSEN_ALT,
        "datum": "06. April 2025", "az": "ModeFuchs-Versand-2025-04-06",
        "betreff": "Versandbestaetigung Bestellung 2025-04-03",
        "eingangsstempel": "06.04.2025 (Eingang E-Mail beim Kunden)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/03_Zustellbestaetigung_08-04-2025.pdf": {
        "typ": "original_eingehend",
        "absender": "DHL Deutsche Post AG; Paketzustellung; Charles-de-Gaulle-Strasse 20; 53113 Bonn",
        "adressat": ALTENHAUSEN_ALT,
        "datum": "08. April 2025", "az": "DHL-Tracking 2025-04-08",
        "betreff": "Zustellbestaetigung Paketsendung ModeFuchs",
        "eingangsstempel": "08.04.2025 (Empfangsbestaetigung Kunde)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/04_Rechnung_R-20250406-3098.pdf": {
        "typ": "original_eingehend", "absender": MODEFUCHS, "adressat": ALTENHAUSEN_ALT,
        "datum": "06. April 2025", "az": "R-20250406-3098",
        "betreff": "Rechnung Bestellung Cashmere-Mantel Aurelia und Lederhandtasche Noa (698,00 EUR)",
        "eingangsstempel": "ca. 08.04.2025 (Eingang Kunde, Faelligkeit 17.04.2025)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/05_Erste_Zahlungserinnerung_20-04-2025.pdf": {
        "typ": "original_eingehend", "absender": MODEFUCHS, "adressat": ALTENHAUSEN_ALT,
        "datum": "20. April 2025", "az": "ModeFuchs-Erinnerung-1-2025-04-20",
        "ihr_zeichen": "R-20250406-3098",
        "betreff": "Erste Zahlungserinnerung - Rechnung R-20250406-3098",
        "eingangsstempel": "ca. 22.04.2025 (Eingang Kunde)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/06_Zweite_Mahnung_E-Mail_04-05-2025.pdf": {
        "typ": "original_eingehend", "absender": MODEFUCHS, "adressat": ALTENHAUSEN_ALT,
        "datum": "04. Mai 2025", "az": "ModeFuchs-Mahnung-2-Email-2025-05-04",
        "ihr_zeichen": "R-20250406-3098",
        "betreff": "Zweite Mahnung per E-Mail - Rechnung R-20250406-3098",
        "eingangsstempel": "04.05.2025 (Eingang E-Mail Kunde)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/07_Erste_Mahnung_Post_05-05-2025.pdf": {
        "typ": "original_eingehend", "absender": MODEFUCHS, "adressat": ALTENHAUSEN_ALT,
        "datum": "05. Mai 2025", "az": "ModeFuchs-Mahnung-1-Post-2025-05-05",
        "ihr_zeichen": "R-20250406-3098",
        "betreff": "Erste Mahnung per Post - Rechnung R-20250406-3098",
        "eingangsstempel": "ca. 07.05.2025 (Eingang Postzustellung Kunde)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/08_Zweite_Mahnung_Post_22-05-2025.pdf": {
        "typ": "original_eingehend", "absender": MODEFUCHS, "adressat": ALTENHAUSEN_ALT,
        "datum": "22. Mai 2025", "az": "ModeFuchs-Mahnung-2-Post-2025-05-22",
        "ihr_zeichen": "R-20250406-3098",
        "betreff": "Zweite/letzte Mahnung vor Inkasso - Rechnung R-20250406-3098",
        "eingangsstempel": "ca. 24.05.2025 (Eingang Postzustellung Kunde)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/09_Abtretungserklaerung_08-06-2025.pdf": {
        "typ": "internes_dokument", "absender": MODEFUCHS, "adressat": INKASSO_GMBH,
        "datum": "08. Juni 2025", "az": "Abtretung MF-IZ-2025-06-08",
        "betreff": "Abtretungserklaerung Forderung gegen Altenhausen aus R-20250406-3098",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/10_Inkassoschreiben_10-06-2025.pdf": {
        "typ": "original_eingehend", "absender": INKASSO_GMBH, "adressat": ALTENHAUSEN_ALT,
        "datum": "10. Juni 2025", "az": "IZ-MF-2025-1749",
        "ihr_zeichen": "R-20250406-3098",
        "betreff": "Aussergerichtliche Zahlungsaufforderung - Forderung der ModeFuchs GmbH",
        "eingangsstempel": "ca. 12.06.2025 (Eingang Postzustellung Kunde)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/11_Letzte_Inkassoaufforderung_25-06-2025.pdf": {
        "typ": "original_eingehend", "absender": INKASSO_GMBH, "adressat": ALTENHAUSEN_ALT,
        "datum": "25. Juni 2025", "az": "IZ-MF-2025-1749",
        "betreff": "Letzte Inkassoaufforderung vor gerichtlicher Geltendmachung",
        "eingangsstempel": "ca. 27.06.2025 (Eingang Postzustellung Kunde)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/12_Gebuehrenrechnung_Inkasso_10-06-2025.pdf": {
        "typ": "original_eingehend", "absender": INKASSO_GMBH, "adressat": ALTENHAUSEN_ALT,
        "datum": "10. Juni 2025", "az": "IZ-MF-2025-1749-Gebuehr",
        "betreff": "Gebuehrenrechnung Inkasso - Kostennote nach RDG/RVG",
        "eingangsstempel": "ca. 12.06.2025 (Eingang Kunde)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/13_Interner_Eingangsvermerk_Inkasso_08-06-2025.pdf": {
        "typ": "interner_vermerk", "absender": INKASSO_GMBH,
        "adressat": "InkassoZentrale GmbH intern", "datum": "08. Juni 2025",
        "az": "IZ-MF-2025-1749/Eingang",
        "betreff": "Interner Eingangsvermerk InkassoZentrale - Aktenanlage 08.06.2025",
        "vertraulichkeit": "VERTRAULICH - INTERN INKASSO (Akteneinsicht)",
    },
    "originale/14_Sachstandsvermerk_Inkasso_18-06-2025.pdf": {
        "typ": "interner_vermerk", "absender": INKASSO_GMBH,
        "adressat": "InkassoZentrale GmbH intern", "datum": "18. Juni 2025",
        "az": "IZ-MF-2025-1749/Sachstand-18062025",
        "betreff": "Sachstandsvermerk InkassoZentrale - 18.06.2025",
        "vertraulichkeit": "VERTRAULICH - INTERN INKASSO (Akteneinsicht)",
    },
    "originale/15_Zahlungsnotiz_Inkasso_01-07-2025.pdf": {
        "typ": "interner_vermerk", "absender": INKASSO_GMBH,
        "adressat": "InkassoZentrale GmbH intern", "datum": "01. Juli 2025",
        "az": "IZ-MF-2025-1749/Zahlungsnotiz",
        "betreff": "Zahlungsnotiz InkassoZentrale - Erhalt der Hauptforderung am 26.06.2025 (direkt ModeFuchs)",
        "vertraulichkeit": "VERTRAULICH - INTERN INKASSO (Akteneinsicht)",
    },
    "originale/16_Aktenvermerk_RA_Brezelmann_27-06-2025.pdf": {
        "typ": "interner_vermerk", "absender": KANZLEI_BC,
        "adressat": "Mandantenakte intern", "datum": "27. Juni 2025",
        "az": "BRZ-2025-447-MF/Aktenvermerk-27062025",
        "betreff": "Aktenvermerk RA Brezelmann - Mandatsuebernahme und Erstberatung",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH PRIVILEGIERT",
    },
    "originale/17_Mandatsblatt_BRZ-2025-447-MF.pdf": {
        "typ": "internes_dokument", "absender": KANZLEI_BC,
        "adressat": "Mandantenakte intern", "datum": "Juni 2025",
        "az": "BRZ-2025-447-MF/Mandatsblatt",
        "betreff": "Mandatsblatt Kanzlei Brezelmann & Collegen - Akte BRZ-2025-447-MF",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/18_E-Mail_Altenhausen_an_RA_Brezelmann_27-06-2025.pdf": {
        "typ": "mandantenkorrespondenz", "absender": ALTENHAUSEN_NEU, "adressat": KANZLEI_BC,
        "datum": "27. Juni 2025", "az": "BRZ-2025-447-MF/Mandatsanfrage",
        "betreff": "Mandatsanfrage Altenhausen - Verteidigung gegen Inkassoforderung",
        "vertraulichkeit": "VERTRAULICH - MANDATSGRUNDLAGE",
    },
    "originale/19_Kontoauszug_Altenhausen_26-06-2025.pdf": {
        "typ": "original_eingehend",
        "absender": "Sparkasse Nuernberg; Kontoauszug-Service; Lorenzer Platz 6; 90402 Nuernberg",
        "adressat": ALTENHAUSEN_NEU,
        "datum": "26. Juni 2025", "az": "Kontoauszug Altenhausen 26.06.2025",
        "betreff": "Kontoauszug - Beleg der Zahlung 698,00 EUR an ModeFuchs am 26.06.2025",
        "eingangsstempel": "26.06.2025 (elektronisch)",
        "vertraulichkeit": "VERTRAULICH - BANKDATEN",
    },
    "originale/20_Anwaltsschreiben_RA_Brezelmann_an_InkassoZentrale_30-06-2025.pdf": {
        "typ": "original_ausgehend", "absender": KANZLEI_BC, "adressat": INKASSO_GMBH,
        "datum": "30. Juni 2025", "az": "BRZ-2025-447-MF", "ihr_zeichen": "IZ-MF-2025-1749",
        "betreff": "Forderung ModeFuchs ./. Altenhausen - Hauptforderung gezahlt, Zurueckweisung Nebenforderungen",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH",
    },
    "originale/21_Mahnbescheid_Antrag_InkassoZentrale_05-07-2025.pdf": {
        "typ": "original_ausgehend", "absender": INKASSO_GMBH, "adressat": AG_WEDDING,
        "datum": "05. Juli 2025", "az": "IZ-MF-2025-1749",
        "betreff": "Antrag auf Erlass eines Mahnbescheids gegen Altenhausen",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/22_Widerspruch_Mahnbescheid_RA_Brezelmann_18-07-2025.pdf": {
        "typ": "original_ausgehend", "absender": KANZLEI_BC, "adressat": AG_WEDDING,
        "datum": "18. Juli 2025", "az": "BRZ-2025-447-MF",
        "ihr_zeichen": "Mahnbescheid AG Berlin-Wedding (Antrag InkassoZentrale 05.07.2025)",
        "betreff": "Widerspruch gegen Mahnbescheid - Altenhausen ./. InkassoZentrale GmbH",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH",
    },
    "originale/23_Klageschrift_InkassoZentrale_25-07-2025.pdf": {
        "typ": "original_eingehend",
        "absender": "Kanzlei InkassoZentrale (Justitiariat); Friedrich-Krause-Ufer 42; 13353 Berlin",
        "adressat": AG_NUERNBERG,
        "datum": "25. Juli 2025", "az": "IZ-MF-2025-1749",
        "betreff": "Klageschrift InkassoZentrale ./. Altenhausen - Restforderung 99,84 EUR plus Kosten",
        "eingangsstempel": "ca. 29.07.2025 (Zustellung an Kanzlei Brezelmann & Collegen)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/24_Klageerwiderung_RA_Brezelmann_15-08-2025.pdf": {
        "typ": "original_ausgehend", "absender": KANZLEI_BC, "adressat": AG_NUERNBERG,
        "datum": "15. August 2025", "az": "BRZ-2025-447-MF",
        "ihr_zeichen": "IZ-MF-2025-1749",
        "betreff": "Klageerwiderung Altenhausen - Hauptforderung erloschen, Nebenforderungen unbegruendet",
        "vertraulichkeit": "VERTRAULICH - ANWALTLICH",
    },
    "originale/25_E-Mail_Zahlungserinnerung_ModeFuchs_20-04-2025.pdf": {
        "typ": "original_eingehend", "absender": MODEFUCHS, "adressat": ALTENHAUSEN_ALT,
        "datum": "20. April 2025", "az": "ModeFuchs-Erinnerung-Email-2025-04-20",
        "betreff": "E-Mail-Zahlungserinnerung ModeFuchs (Duplikat zu Postversand)",
        "eingangsstempel": "20.04.2025 (Eingang E-Mail)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/26_E-Mail_Zweite_Mahnung_ModeFuchs_04-05-2025.pdf": {
        "typ": "original_eingehend", "absender": MODEFUCHS, "adressat": ALTENHAUSEN_ALT,
        "datum": "04. Mai 2025", "az": "ModeFuchs-Mahnung-2-Email-04052025",
        "betreff": "E-Mail-Mahnung ModeFuchs (zweite Stufe)",
        "eingangsstempel": "04.05.2025 (Eingang E-Mail)",
        "vertraulichkeit": "VERTRAULICH",
    },
    "originale/27_Zahlungsbestaetigung_ModeFuchs_30-06-2025.pdf": {
        "typ": "original_eingehend", "absender": MODEFUCHS, "adressat": ALTENHAUSEN_NEU,
        "datum": "30. Juni 2025", "az": "ModeFuchs-Zahlungsbestaetigung-2025-06-30",
        "betreff": "Zahlungsbestaetigung ModeFuchs - Hauptforderung 698,00 EUR ausgeglichen",
        "eingangsstempel": "ca. 02.07.2025 (Eingang Kanzlei via Mandant)",
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


def process(akte: Path, md_map: dict, sc_map: dict) -> tuple[int, int]:
    md_n = sc_n = 0
    for rel, meta in md_map.items():
        target = akte / rel
        if not target.exists():
            print(f"WARN fehlt: {target}", file=sys.stderr); continue
        body = target.read_text(encoding="utf-8")
        if AKTE_META_RE.search(body):
            new = AKTE_META_RE.sub(render_meta_block(meta), body, count=1)
        else:
            new = render_meta_block(meta) + body
        target.write_text(new, encoding="utf-8")
        print(f"  MD  {rel}  ({meta['typ']})"); md_n += 1
    for rel, meta in sc_map.items():
        target = akte / rel
        if not target.exists():
            print(f"WARN fehlt: {target}", file=sys.stderr); continue
        sidecar = target.with_suffix(target.suffix + ".meta")
        sidecar.write_text(render_sidecar(meta), encoding="utf-8")
        print(f"  SC  {sidecar.relative_to(akte)}  ({meta['typ']})"); sc_n += 1
    return md_n, sc_n


def main():
    print("=== Phishing (Mayer ./. Sparkasse Berlin) ===")
    pm, ps = process(PHISH, PHISH_MD, PHISH_SIDECARS)
    print(f"  => {pm} MD, {ps} Sidecars\n")
    print("=== Inkasso (ModeFuchs ./. von Altenhausen) ===")
    im, isc = process(INKASSO, INKASSO_MD, INKASSO_SIDECARS)
    print(f"  => {im} MD, {isc} Sidecars\n")
    print(f"GESAMT: {pm + im} MD, {ps + isc} Sidecars")


if __name__ == "__main__":
    main()
