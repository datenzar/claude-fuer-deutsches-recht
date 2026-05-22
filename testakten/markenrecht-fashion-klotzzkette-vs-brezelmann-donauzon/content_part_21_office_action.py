# Part 21: USPTO Office Action § 2(d) Refusal + Response
def blatt_office_action():
    s = []
    s.append(Paragraph("<b>UNITED STATES PATENT AND TRADEMARK OFFICE</b>", S_CENTER))
    s.append(Paragraph("Office Action — Trademark Examining Operation", S_CENTER))
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.3*cm))
    rows = [
        ["Serial No.:", "97/884.117 — KLÔTZZKÈTTÉ"],
        ["Mark:", "KLÔTZZKÈTTÉ (standard character)"],
        ["Applicant:", "klôtzzkètté Inc."],
        ["Correspondent:", "Whitman Brennan Forsythe LLP / J. H. Whitman III, Esq."],
        ["Examining Attorney:", "Tracy R. Albertson — Law Office 116"],
        ["Issued:", "April 22, 2026 — Response deadline: October 22, 2026"],
    ]
    t = Table(rows, colWidths=[4.5*cm, 12*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("FONTNAME", (0,0), (0,-1), "Times-Bold"),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Examining Attorney's Action issued pursuant to 37 C.F.R. § 2.61.", S_SMALL))
    s.append(Paragraph(
        "Registration of the applied-for mark is <b>refused</b> on the following grounds:",
        S_NORMAL))
    s.append(Paragraph("<b>§ 2(d) Refusal — Likelihood of Confusion</b>", S_H3))
    s.append(Paragraph(
        "Registration of the applied-for mark is refused because of a likelihood of "
        "confusion with the mark in U.S. Registration No. 6,221,883: "
        "<b>KLOTZ KETTLE COOKWARE</b>, registered December 14, 2021 for „cast-iron cooking "
        "pots, dutch ovens, frying pans; non-electric kettles“ in International Class 21, "
        "owned by Heinrich-Klotz Hauswaren GmbH, Solingen, Germany.", S_NORMAL))
    s.append(Paragraph(
        "Trademark Act § 2(d), 15 U.S.C. § 1052(d); TMEP §§ 1207.01 et seq. The Examining "
        "Attorney notes that:", S_NORMAL))
    items = [
        "(i) The marks share the dominant element „KLOTZ K—“;",
        "(ii) Both marks evoke a Germanic origin and trade impression;",
        "(iii) Class 21 (cookware) and Class 25 (clothing) may co-exist in modern lifestyle "
        "department stores, expanding the likelihood of consumer association.",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    s.append(Paragraph(
        "Although applicant's mark is in International Class 25 and the cited registration "
        "is in International Class 21, the Examining Attorney is of the opinion, citing "
        "<i>In re Iolo Techs., LLC</i>, 95 USPQ2d 1498 (TTAB 2010), that consumers exposed "
        "to both marks would presume a common source.", S_NORMAL))
    s.append(Paragraph("<b>Specimen Refusal (§ 1(a) Basis Only)</b>", S_H3))
    s.append(Paragraph(
        "Should applicant elect to convert to § 1(a) use-in-commerce basis, the current "
        "specimen of record (a digital lookbook PDF dated „Spring/Summer 2026“) is "
        "<b>unacceptable</b> as it does not show the mark in use as a trademark in commerce. "
        "TMEP §§ 904.03(i), 904.07.", S_NORMAL))
    s.append(Paragraph("<b>Identification of Goods — Indefinite</b>", S_H3))
    s.append(Paragraph(
        "The identification of goods „clothing of all kinds, including but not limited to "
        "everything one might wear“ is indefinite and overly broad. Applicant must amend to "
        "specify particular items by their common commercial name (TMEP § 1402.03).",
        S_NORMAL))
    s.append(Paragraph(
        "<b>Suggested amended identification:</b> „Suits, dresses, blouses, skirts, trousers, "
        "scarves, ties, gloves, hats, coats, jackets, lingerie; all of the foregoing being "
        "luxury items“ in Class 25.", S_NORMAL))
    s.append(Paragraph(
        "Applicant has six (6) months from the issue date of this Office Action to file a "
        "complete response.", S_NORMAL))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("/Tracy R. Albertson/", S_NORMAL))
    s.append(Paragraph("Tracy R. Albertson — Trademark Examining Attorney<br/>"
                        "Law Office 116 · (571) 272-8847 · tracy.albertson@uspto.gov",
                        S_SMALL))
    return s

story += blatt_office_action()
story.append(PageBreak())

def blatt_office_action_response():
    s = []
    s.append(WBFLetterhead(
        recipient="Trademark Examining Attorney Tracy R. Albertson\nLaw Office 116\n"
                  "United States Patent and Trademark Office\nP.O. Box 1451\n"
                  "Alexandria, VA 22313-1451",
        date="June 17, 2026",
        file_no="WBF-2026-KK-0014.OA1",
        re_line="App. Ser. No. 97/884.117 — KLÔTZZKÈTTÉ — Response to Office Action of "
                "April 22, 2026"))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Dear Examining Attorney Albertson:", S_NORMAL))
    s.append(Paragraph(
        "Applicant respectfully submits this Response and traverses the Section 2(d) "
        "refusal on the grounds set forth below.", S_NORMAL))
    s.append(Paragraph("<b>I.  No Likelihood of Confusion</b>", S_H3))
    s.append(Paragraph(
        "The cited registration KLOTZ KETTLE COOKWARE and the applied-for mark KLÔTZZKÈTTÉ "
        "are dissimilar in commercial impression. The cited mark is, in essence, a "
        "descriptive composite: the personal name „Klotz“, the noun „kettle“, and the "
        "generic „cookware“. The applied-for mark is a single fanciful, multi-syllabic "
        "term of French derivation, written with diacritical marks (Ô, È, É) and with a "
        "doubled letter (ZZ). The phonetic, visual, and connotative impressions are "
        "fundamentally different.", S_NORMAL))
    s.append(Paragraph(
        "<b>(1) The marks differ in sight.</b> KLÔTZZKÈTTÉ contains three diacritics, "
        "double-Z, and an acute É terminus. KLOTZ KETTLE COOKWARE contains spaces, no "
        "diacritics, and a verbose three-word structure. The visual impressions are utterly "
        "distinct.", S_NORMAL))
    s.append(Paragraph(
        "<b>(2) The marks differ in sound.</b> KLÔTZZKÈTTÉ is pronounced /klɔts.kɛˈte/ "
        "(French) or /klɒts.kɛˈtei/ (American). The cited mark is pronounced /klɒts ˈkɛt.l̩ "
        "ˈkʊk.weər/ — three distinct trochaic words.", S_NORMAL))
    s.append(Paragraph(
        "<b>(3) The marks differ in meaning.</b> KLÔTZZKÈTTÉ is a fanciful term derived "
        "from the surname of Antoine-Louis Klôtzzkètté (1898–1971), the founder of "
        "Applicant's storied luxury house. The cited mark plainly references cooking "
        "kettles. There is no overlap in semantic field.", S_NORMAL))
    s.append(Paragraph(
        "<b>(4) The goods are fundamentally dissimilar.</b> Class 25 (luxury apparel) and "
        "Class 21 (cookware) do not move in the same channels of trade. Applicant's goods "
        "are sold in dedicated luxury boutiques (Madison Avenue, Rodeo Drive, Worth Avenue) "
        "and through approximately 38 specialty department-store accounts. The cited "
        "registrant's goods are sold through hardware stores, mass-market kitchen retailers "
        "(Williams Sonoma, Bed Bath &amp; Beyond), and Donauzon. See <i>Recot, Inc. v. "
        "Becton</i>, 214 F.3d 1322 (Fed. Cir. 2000) (consumers do not assume single source "
        "across unrelated product categories).", S_NORMAL))
    s.append(Paragraph(
        "<b>(5) The price points differ by an order of magnitude.</b> Applicant's silk "
        "scarves retail at US$ 695. Registrant's cast-iron skillets retail at US$ 89. "
        "Consumers of luxury silk are sophisticated and exercise the highest degree of care.",
        S_NORMAL))
    s.append(Paragraph("<b>II.  Amendment to Identification of Goods</b>", S_H3))
    s.append(Paragraph(
        "Applicant accepts the Examining Attorney's suggested amendment and substitutes the "
        "following identification: „Suits, dresses, blouses, skirts, trousers, scarves, ties, "
        "gloves, hats, coats, jackets, lingerie; all of the foregoing being luxury items“ in "
        "International Class 25.", S_NORMAL))
    s.append(Paragraph("<b>III.  Maintenance of § 1(b) Basis</b>", S_H3))
    s.append(Paragraph(
        "Applicant maintains its filing basis under § 1(b) Intent-to-Use and will file a "
        "Statement of Use in due course. The Examining Attorney's comments regarding "
        "specimen sufficiency are therefore not presently at issue.", S_NORMAL))
    s.append(Paragraph(
        "For the foregoing reasons, Applicant respectfully requests that the § 2(d) refusal "
        "be <b>withdrawn</b> and the application be passed to publication.", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Respectfully submitted,", S_NORMAL))
    s.append(Paragraph("/Priscilla Forsythe-Vanderhof/", S_NORMAL))
    s.append(Paragraph("Priscilla Forsythe-Vanderhof, Esq. — USPTO Reg. 62,114", S_SMALL))
    s.append(Spacer(1, 0.4*cm))
    s.append(HandNote(
        "Halston: „Albertson examiniert seit 28 Jahren —\n"
        "der wittert Schwäche. Hartes Traversal, kein Compromise.“\n"
        "Wenn er trotzdem auf 2(d) beharrt: Phase 2 = Cons. of Use mit\n"
        "Solingen-Hauswaren. Komme zu Steinacker zurück\n"
        "für „klotz“-etymology Affidavit.\n"
        "— P.F.-V., 06/17",
        font=FONT_HAND, size=13, angle=-1.5, w=15*cm))
    return s

story += blatt_office_action_response()
story.append(PageBreak())

print("[part21] done")
