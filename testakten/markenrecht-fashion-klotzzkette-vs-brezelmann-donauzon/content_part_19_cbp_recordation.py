# Part 19: CBP e-Recordation TMK-26-08812
def blatt_cbp_form():
    s = []
    s.append(Paragraph("<b>U.S. CUSTOMS AND BORDER PROTECTION</b>", S_CENTER))
    s.append(Paragraph("Intellectual Property Rights e-Recordation (IPRR) Application",
                        S_CENTER))
    s.append(Paragraph("Form CBP-1567 (Rev. 03/2025) — OMB Control No. 1651-0070",
                        S_CENTER))
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.3*cm))
    rows = [
        ["Section A — Identification of Right Holder", ""],
        ["Right Holder Name:", "klôtzzkètté Inc."],
        ["DUNS Number:", "07-554-6831"],
        ["EIN / Tax ID:", "88-3274119"],
        ["Address:", "712 Fifth Avenue, 36th Floor, New York, NY 10019"],
        ["Designated Officer:", "J. Halston Whitman III, Esq. (counsel)"],
        ["Telephone:", "(212) 555-0188"],
        ["Email:", "ip-enforce@whitman-brennan.com"],
    ]
    t = Table(rows, colWidths=[5.5*cm, 11*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("SPAN", (0,0), (1,0)),
        ("FONTNAME", (0,0), (1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (1,0), colors.HexColor("#1c2e4a")),
        ("TEXTCOLOR", (0,0), (1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.black),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.2*cm))
    rows = [
        ["Section B — Subject of Recordation (TMK-26-08812)", ""],
        ["Trademark / Trade Name:", "KLÔTZZKÈTTÉ"],
        ["USPTO Reg. No. / App. No.:", "App. Ser. No. 97/884.117 (pending; § 1(b))"],
        ["Goods / Services Covered:", "International Class 25 — Clothing (including but not "
                                       "limited to suits, dresses, blouses, scarves, ties, "
                                       "and accessories), Class 14, Class 18, Class 3"],
        ["Country of Manufacture:", "France (Paris); Italy (Florence); Switzerland (Lugano)"],
        ["Authorized Importers:", "klôtzzkètté Inc.; Bergdorf Goodman, Inc.; Neiman Marcus "
                                  "Group LLC; Saks &amp; Company; Net-A-Porter USA Inc."],
        ["Restrictions on Importation:", "Any importation not bearing affixed CBP Holographic "
                                          "Security Seal (model HG-K°°-2025) shall be presumed "
                                          "counterfeit"],
    ]
    t = Table(rows, colWidths=[5.5*cm, 11*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("SPAN", (0,0), (1,0)),
        ("FONTNAME", (0,0), (1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (1,0), colors.HexColor("#3a2c1a")),
        ("TEXTCOLOR", (0,0), (1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.black),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.2*cm))
    rows = [
        ["Section C — Recordation Fee Tendered", ""],
        ["Recordation Fee (per class):", "US$ 190.00"],
        ["Number of Classes:", "4 (Cl. 3, 14, 18, 25)"],
        ["Subtotal:", "US$ 760.00"],
        ["Expedited Processing Surcharge:", "US$ 100.00"],
        ["Total Remitted (pay.gov tracking):", "US$ 860.00 — Conf. 26-PG-771148-K"],
    ]
    t = Table(rows, colWidths=[7*cm, 9.5*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("SPAN", (0,0), (1,0)),
        ("FONTNAME", (0,0), (1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (1,0), colors.HexColor("#1c2e4a")),
        ("TEXTCOLOR", (0,0), (1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.black),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "I, the undersigned, hereby certify that the information provided in this application "
        "is true and correct to the best of my knowledge, and that I am authorized to file "
        "this application on behalf of the Right Holder under 19 C.F.R. § 133.2.", S_SMALL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("/J. Halston Whitman III/", S_NORMAL))
    s.append(Paragraph("J. Halston Whitman III, Esq. — Filed via IPRR portal, March 18, 2026, "
                        "14:22 EDT", S_SMALL))
    s.append(Spacer(1, 0.3*cm))
    s.append(StampBox("RECEIVED\nCBP/IPR Branch\n03/19/2026", angle=-7, w=4.8*cm, h=1.8*cm))
    return s

story += blatt_cbp_form()
story.append(PageBreak())

def blatt_cbp_acceptance():
    s = []
    s.append(Paragraph("<b>U.S. CUSTOMS AND BORDER PROTECTION</b>", S_CENTER))
    s.append(Paragraph("Office of Trade — Regulations &amp; Rulings, IPR Branch",
                        S_CENTER))
    s.append(Paragraph("1300 Pennsylvania Avenue, N.W., Washington, D.C. 20229",
                        S_CENTER))
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("March 27, 2026", S_RIGHT))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph(
        "Whitman Brennan Forsythe LLP<br/>"
        "Attn: J. H. Whitman III, Esq.<br/>"
        "1290 Avenue of the Americas, 41st Floor<br/>"
        "New York, NY 10104", S_SMALL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<b>Re: Acceptance of Recordation — TMK-26-08812 — KLÔTZZKÈTTÉ</b>", S_NORMAL))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("Dear Counsel:", S_NORMAL))
    s.append(Paragraph(
        "This letter confirms that the above-captioned application for recordation has been "
        "accepted and assigned CBP Recordation No. <b>TMK-26-08812</b>, effective March 27, "
        "2026. The recordation shall remain in effect for a period of twenty (20) years from "
        "this date, subject to the continued existence of the underlying trademark right.",
        S_NORMAL))
    s.append(Paragraph(
        "Pursuant to 19 C.F.R. § 133.21, all U.S. Ports of Entry have been notified through "
        "the Automated Commercial Environment (ACE) and will, upon detection of suspected "
        "infringing merchandise, detain such merchandise and notify the right holder within "
        "five (5) business days.", S_NORMAL))
    s.append(Paragraph(
        "The Right Holder may receive automated detention notices through the IPRR portal. "
        "We strongly recommend providing CBP's Centers of Excellence and Expertise (CEEs), "
        "in particular the Apparel, Footwear &amp; Textiles CEE in San Francisco, with a "
        "Product Identification Guide („PIG“) and authentication training materials to "
        "facilitate enforcement.", S_NORMAL))
    s.append(Paragraph("Sincerely,", S_NORMAL))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Charles W. Steeves, Branch Chief<br/>"
                        "Intellectual Property Rights Branch · CBP",
                        S_SMALL))
    s.append(Spacer(1, 0.4*cm))
    s.append(HLine())
    s.append(Paragraph("<b>CBP DETENTION NOTICE No. 26-LAX-002-887 (Excerpt — for file)</b>",
                        S_H3))
    s.append(Paragraph(
        "<b>Port of Entry:</b> Los Angeles/Long Beach Seaport (Code 2704)<br/>"
        "<b>Date of Detention:</b> April 19, 2026<br/>"
        "<b>Entry No.:</b> 304-9912771-0<br/>"
        "<b>Importer of Record:</b> Donauzon Logistics USA LLC (EIN 84-3771224)<br/>"
        "<b>Consignee:</b> Donauzon Marketplace USA LLC, 410 Terry Avenue N., Seattle, WA<br/>"
        "<b>Country of Origin (declared):</b> Lithuania<br/>"
        "<b>Merchandise:</b> 2,488 pieces — silk-look scarves bearing the mark "
        "„klôtzzkettíe“ (misspelling intentional) and an apparent reproduction of the K°° "
        "crown logo; HTSUS 6214.10.1000<br/>"
        "<b>Suspected Infringement:</b> TMK-26-08812 (KLÔTZZKÈTTÉ)<br/>"
        "<b>Status:</b> Detained pending right-holder authentication response (5-day clock).",
        S_SMALL))
    s.append(Spacer(1, 0.2*cm))
    s.append(HandNote(
        "BINGO. Donauzon-USA-Tochter beim ersten Container erwischt.\n"
        "Forsythe-V. soll SOFORT Authentifizierung schicken.\n"
        "+ Parallel: SDNY-Klage vorbereiten gegen Donauzon Marketplace USA LLC.\n"
        "Diversity Jurisdiction (28 U.S.C. § 1332) gegeben? Ja — DE vs WA, NY.\n"
        "— J.H.W. III, 4/19/2026, 23:14 EST",
        font=FONT_HAND, size=13, angle=-0.5, w=15*cm))
    return s

story += blatt_cbp_acceptance()
story.append(PageBreak())

print("[part19] done")
