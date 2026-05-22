# Part 31: Madrid Protocol Designation papers + WIPO IB Notification + Internal Memos
def blatt_madrid_designation():
    s = []
    s.append(Paragraph("<b>WORLD INTELLECTUAL PROPERTY ORGANIZATION</b>", S_CENTER))
    s.append(Paragraph("International Bureau · 34 chemin des Colombettes · CH-1211 Genève 20",
                        S_CENTER))
    s.append(Paragraph("MM2(E) — APPLICATION FOR INTERNATIONAL REGISTRATION GOVERNED "
                        "EXCLUSIVELY BY THE MADRID PROTOCOL", S_CENTER))
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.3*cm))
    rows = [
        ["1. Applicant's name and address:",
         "klôtzzkètté S.A.\n12 rue du Faubourg Saint-Honoré, 75008 Paris, France\n"
         "RCS Paris 552 094 471 · SIREN 552 094 471"],
        ["2. Connection to Contracting Party (Art. 2(1) Madrid Protocol):",
         "Establishment in France (Article 2(1)(ii))"],
        ["3. Entitlement (Art. 1(2) PMA):",
         "National (FR) and European Union (EUTM) registrations — see No. 5"],
        ["4. Representative:",
         "Steinacker Lichtenberg & Partners IP Boutique (DE)\n"
         "Maximiliansplatz 19, 80333 München, Germany\n"
         "WIPO ID: 30144-7711-K — Dr. Dr. A. Steinacker-von Tarsis"],
        ["5. Basic application / registration:",
         "EUTM 018 411 220 (registered 14/03/2018, Cl. 3, 9, 14, 18, 25, 35, 41, "
         "wordmark KLÔTZZKÈTTÉ)\nFR national 19/4.554.117 (registered 1958, all 45 classes)"],
        ["6. Designated Contracting Parties:",
         "AU, BR, CA, CH, CN, IN, JP, KR, MX, NO, RU, SG, TR, UA, US, VN"],
        ["7. Mark:",
         "KLÔTZZKÈTTÉ (standard characters, with diacriticals as shown)"],
        ["8. Indication of classes & list of goods/services (Nice 11th ed.):",
         "Cl. 3, 14, 18, 25, 35, 41 (see Annex MM2-1, 18 pages, full goods specification)"],
        ["9. Priority claim:",
         "EUTM 018 411 220 of 14/03/2018 — no further national priority claimed"],
        ["10. Description of the mark:",
         "The mark consists of the wording „KLÔTZZKÈTTÉ“ with three diacritical "
         "characters (circumflex on the first „O“, grave accent on the second „E“, "
         "acute accent on the third „E“) and a doubled „Z“ in the middle."],
        ["11. Translation / transliteration:",
         "No translation; family name of founder Antoine-Louis Klôtzzkètté (1898–1971)"],
        ["12. Fees:",
         "Basic fee CHF 653 + individual fees per designation = total CHF 14,872 "
         "(see Annex MM2-2, fee breakdown)"],
        ["13. Date:",
         "31 March 2026 — submitted via ePCT/eMadrid portal"],
    ]
    t = Table(rows, colWidths=[5.5*cm, 11*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 8.8),
        ("FONTNAME", (0,0), (0,-1), "Times-Bold"),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "I certify that the particulars given above are accurate. — Comtesse Béatrice de "
        "Klôtzzkètté-Visconti, Président · Paris, 31 March 2026", S_SMALL))
    s.append(Spacer(1, 0.3*cm))
    s.append(StampBox("WIPO · IB\nMADRID · MM2\n31-MAR-2026", angle=-7, w=4.8*cm,
                        h=2.0*cm))
    return s

story += blatt_madrid_designation()
story.append(PageBreak())

def blatt_wipo_acknowledgement():
    s = []
    s.append(Paragraph("<b>WORLD INTELLECTUAL PROPERTY ORGANIZATION</b>", S_CENTER))
    s.append(Paragraph("NOTIFICATION OF INTERNATIONAL REGISTRATION", S_CENTER))
    s.append(HLine())
    s.append(Spacer(1, 0.2*cm))
    rows = [
        ["International Registration No.:", "1.488.220"],
        ["Date of International Registration:", "31 March 2026"],
        ["Date of recording in International Register:", "12 May 2026"],
        ["Holder:", "klôtzzkètté S.A., Paris"],
        ["Mark:", "KLÔTZZKÈTTÉ"],
        ["Classes:", "3, 14, 18, 25, 35, 41"],
        ["Basic Registration:", "EUTM 018 411 220 of 14/03/2018"],
        ["Designated Contracting Parties:",
         "AU · BR · CA · CH · CN · IN · JP · KR · MX · NO · RU · SG · TR · UA · US · VN"],
        ["Status:", "Recorded; office actions/refusals due within 12–18 months of "
                    "designation (per Protocol Art. 5(2))"],
    ]
    t = Table(rows, colWidths=[5.5*cm, 11*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("FONTNAME", (0,0), (0,-1), "Times-Bold"),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888")),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<b>USPTO § 66(a) Notification — Subsequent.</b> The U.S. Patent and Trademark "
        "Office has been notified through ROMARIN of designation IR 1.488.220 (United "
        "States) on 14 May 2026. The USPTO assigned U.S. Serial No. 79/342.118 to the "
        "designation. USPTO Examiner Tracy R. Albertson, Law Office 116, will conduct "
        "the substantive examination in parallel to the direct national Application "
        "Serial No. 97/884.117. <i>Querverweis: Office Action vom 22.04.2026, Bl. 78.</i>",
        S_NORMAL))
    s.append(Paragraph(
        "<b>Russian Federation (RU) Note.</b> In view of geopolitical developments since "
        "February 2022 and the consequent suspension of cooperation by certain Western "
        "right-holders with Rospatent, the Russian designation is filed <i>pro forma</i>: "
        "klôtzzkètté has issued no licensing in RU since 27 February 2022 and does not "
        "intend to enforce in Russian courts. The designation is preserved solely to "
        "block bad-faith squatting (cf. parallel discussion EUIPO BoA submission "
        "22.07.2026).", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(StampBox("WIPO · IR\n1.488.220\n12-MAY-2026", angle=-7, w=4.8*cm, h=2.0*cm))
    s.append(Spacer(1, 0.4*cm))
    s.append(HLine())
    s.append(Paragraph("<b>INTERNES MEMO — Madrid-Strategie · Steinacker/Whitman, "
                        "15.05.2026</b>", S_H3))
    s.append(Paragraph(
        "Die Madrid-Designation IR 1.488.220 ist <i>gleichzeitig Schild und Schwert</i>: "
        "Schild gegen weitere Bad-Faith-Anmeldungen in den 16 designierten "
        "Vertragsstaaten; Schwert für die spätere Erweiterung der Enforcement-Front. "
        "Insbesondere die USPTO-Schiene wird damit doppelt geführt — National (97/884.117) "
        "und International (79/342.118) — sodass im Falle eines § 1(b)-Konversions-"
        "Engpasses bei der nationalen Anmeldung der § 66(a)-Pfad alternativ "
        "verfolgt werden kann. <i>Belt and suspenders</i>, wie Halston sagt.", S_NORMAL))
    s.append(Paragraph(
        "Kostenrahmen Madrid-Designation 2026: CHF 14.872 (Anmeldung) + estimated CHF "
        "62.500 (lokale Anwälte für mögliche Office Actions in 16 Staaten) + CHF 18.400 "
        "(Übersetzungen). Gesamt ca. CHF 95.000 = EUR 96.300.", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(HandNote(
        "Russia-Designation pro forma ist riskant.\n"
        "Wenn Putins Rospatent kreativ wird: lex specialis russica.\n"
        "Aber: Comtesse will alles eintragen lassen, was geht.\n"
        "Genau wie Großvater Antoine-Louis 1953:\n"
        "„Tout, partout, toujours.“\n"
        "— A.St., 16.05.",
        font=FONT_HAND2, size=13, angle=-0.6, w=15*cm))
    return s

story += blatt_wipo_acknowledgement()
story.append(PageBreak())

print("[part31] done")
