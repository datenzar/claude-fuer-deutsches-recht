# Part 18: TTAB Notice of Opposition + Answer + Scheduling Order
def blatt_ttab_caption():
    s = []
    s.append(Paragraph("<b>IN THE UNITED STATES PATENT AND TRADEMARK OFFICE</b>", S_CENTER))
    s.append(Paragraph("<b>BEFORE THE TRADEMARK TRIAL AND APPEAL BOARD</b>", S_CENTER))
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.4*cm))
    cap = [
        ["klôtzzkètté Inc.,", "", ""],
        ["    Opposer,", "", "Opposition No. 91/289.412"],
        ["v.", "", ""],
        ["Klotzkettie LLC,", "", "App. Serial No. 97/901.448"],
        ["    Applicant.", "", "Mark: KLOTZKETTIE (Class 25)"],
    ]
    t = Table(cap, colWidths=[7*cm, 1*cm, 9*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 10),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEAFTER", (0,0), (0,-1), 1.0, colors.black),
    ]))
    s.append(t)
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("<b>NOTICE OF OPPOSITION</b>", S_CENTER))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "klôtzzkètté Inc., a corporation organized under the laws of the State of Delaware, "
        "having a principal place of business at 712 Fifth Avenue, 36th Floor, New York, NY "
        "10019 (hereinafter „Opposer“), believes that it will be damaged by the registration "
        "of the mark <b>KLOTZKETTIE</b> as set forth in application Serial No. 97/901.448, "
        "published in the Official Gazette of February 24, 2026, and hereby opposes the "
        "same pursuant to § 13 of the Lanham Act, 15 U.S.C. § 1063.", S_NORMAL))
    s.append(Paragraph(
        "As grounds for opposition, Opposer alleges as follows:", S_NORMAL))
    s.append(Paragraph("<b>I.  THE PARTIES</b>", S_H3))
    s.append(Paragraph(
        "1. Opposer is the owner of a substantial portfolio of trademark applications and "
        "registrations relating to the famous luxury fashion house klôtzzkètté, founded in "
        "Paris in 1923 by Antoine-Louis Klôtzzkètté, and continuously used in U.S. commerce "
        "since 1958.", S_NORMAL))
    s.append(Paragraph(
        "2. Upon information and belief, Applicant Klotzkettie LLC is a single-member limited "
        "liability company organized under the laws of the State of Delaware, with a "
        "registered agent address at 251 Little Falls Drive, Wilmington, DE 19808. Upon "
        "further information and belief, said agent address corresponds to over 285,000 "
        "Delaware shell entities and Applicant has no genuine commercial presence at said "
        "address or elsewhere in the United States.", S_NORMAL))
    s.append(Paragraph(
        "3. Upon information and belief, the sole member of Applicant is one „Egonas "
        "Brezelmanas“, a natural person residing at Vilniaus g. 47, LT-01402 Vilnius, "
        "Lithuania, who is in fact identical to or controlled by Egon Brezelmann of "
        "Bad Mergentheim, Federal Republic of Germany (cf. parallel German proceedings "
        "Landgericht Frankfurt am Main, Az. 2-03 O 412/26, see Bl. 14 of this file).",
        S_NORMAL))
    s.append(Paragraph("<b>II.  OPPOSER'S MARKS</b>", S_H3))
    s.append(Paragraph(
        "4. Opposer is the owner of the following pending U.S. applications, each of which "
        "predates the filing date of the opposed application (which was filed January 9, "
        "2026):", S_NORMAL))
    rows = [
        ["Serial No.", "Mark", "Class", "Filing Date"],
        ["97/884.117", "KLÔTZZKÈTTÉ", "25", "Nov. 12, 2025"],
        ["97/884.118", "K°° (crown design)", "25", "Nov. 12, 2025"],
        ["97/884.121", "Haptic — silk twill weave", "24, 25", "Jan. 06, 2026"],
    ]
    t = Table(rows, colWidths=[3*cm, 6*cm, 2.5*cm, 3.5*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1c2e4a")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.black),
    ]))
    s.append(t)
    s.append(Paragraph(
        "5. Opposer is further the owner of foreign trademark registrations in the European "
        "Union (EUTM 018 998 712), France (FR N° 19/4.554.117), Italy (IT 302.025.000.118.547), "
        "Switzerland (CH 783.117), and an International Registration under the Madrid Protocol "
        "(IR 1.488.220), designating, inter alia, the United States.", S_NORMAL))
    return s

story += blatt_ttab_caption()
story.append(PageBreak())

def blatt_ttab_grounds():
    s = []
    s.append(Paragraph("<b>III.  GROUNDS FOR OPPOSITION</b>", S_H3))
    s.append(Paragraph("<b>Count One — Likelihood of Confusion (§ 2(d))</b>", S_H3))
    s.append(Paragraph(
        "6. Applicant's mark KLOTZKETTIE so resembles Opposer's previously used and applied-"
        "for marks KLÔTZZKÈTTÉ as to be likely, when used on or in connection with the "
        "identified goods („T-shirts, polo shirts, hooded sweatshirts, jeans, baseball caps, "
        "socks“ in Class 25), to cause confusion, or to cause mistake, or to deceive, within "
        "the meaning of § 2(d) of the Lanham Act, 15 U.S.C. § 1052(d).", S_NORMAL))
    s.append(Paragraph(
        "7. The marks are virtually identical in commercial impression. Phonetically, "
        "KLOTZKETTIE is pronounced /klɒtsˈkɛti/, while KLÔTZZKÈTTÉ is pronounced "
        "/klɔtskɛˈte/ in the original French (or /klɒtsˈkɛti/ in American pronunciation). "
        "The double-Z and accents in Opposer's mark are commercially insubstantial under "
        "<i>In re Viterra Inc.</i>, 671 F.3d 1358 (Fed. Cir. 2012). The Examining Attorney's "
        "decision to publish the opposed application despite the existence of pending "
        "Application Serial No. 97/884.117 was, in Opposer's respectful submission, "
        "patently erroneous.", S_NORMAL))
    s.append(Paragraph(
        "8. The <i>DuPont</i> factors (<i>In re E.I. du Pont de Nemours &amp; Co.</i>, 476 F.2d "
        "1357 (CCPA 1973)) weigh decisively in Opposer's favor:", S_NORMAL))
    items = [
        "(i) Similarity of marks (sight, sound, meaning): virtually identical;",
        "(ii) Similarity of goods (Class 25 apparel): identical/closely related;",
        "(iii) Established trade channels: department stores, online retailers, boutiques — "
        "overlap is total;",
        "(iv) Conditions under which sales are made: although Opposer's items retail at "
        "considerably higher price points, Applicant's lower-priced items will be perceived "
        "as the „diffusion line“ of Opposer, exacerbating confusion (see <i>Mason Eng'g &amp; "
        "Design Corp. v. Mateson Chem. Corp.</i>, 225 USPQ 956);",
        "(v) Fame of Opposer's mark: substantial in luxury sector (cf. WWD, Vogue, Harper's "
        "Bazaar coverage 1958–2026; total worldwide media impressions exceeding 4.2 bn);",
        "(vi) Number and nature of similar marks on similar goods: minimal; ",
        "(vii) Nature and extent of any actual confusion: documented (see Exhibit 14 — "
        "consumer affidavits collected by Spürnase-Couture GmbH, Munich); ",
        "(viii) Length of time during and conditions under which there has been concurrent "
        "use without evidence of actual confusion: none — Applicant has not yet commenced use; ",
        "(ix) Variety of goods on which mark is or is not used: Opposer uses on the full "
        "luxury good range; Applicant intends only narrow Class 25 use; ",
        "(x) Market interface between Applicant and Opposer: none — Applicant is a Delaware "
        "strawman entity; ",
        "(xi)–(xiii) Remaining factors: neutral or favoring Opposer.",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18, firstLineIndent=-18)))
    s.append(Paragraph("<b>Count Two — Dilution by Blurring (§ 43(c))</b>", S_H3))
    s.append(Paragraph(
        "9. Opposer's KLÔTZZKÈTTÉ mark is famous within the meaning of § 43(c)(2)(A) of the "
        "Lanham Act, 15 U.S.C. § 1125(c)(2)(A). The mark has been used in U.S. commerce "
        "since 1958, has been the subject of unsolicited media coverage including dedicated "
        "feature articles in The New York Times (Sept. 14, 2019), Vogue (Mar. 2021), and "
        "The Wall Street Journal Magazine (Nov. 2024), and Opposer's annual U.S. advertising "
        "expenditures exceed US$ 12 million.", S_NORMAL))
    s.append(Paragraph(
        "10. Applicant's adoption of a virtually identical mark for low-priced goods is "
        "calculated to impair the distinctiveness of Opposer's famous mark and constitutes "
        "dilution by blurring within the meaning of § 43(c)(2)(B).", S_NORMAL))
    s.append(Paragraph("<b>Count Three — Bad Faith / No Bona Fide Intent</b>", S_H3))
    s.append(Paragraph(
        "11. Upon information and belief, Applicant lacks a bona fide intent to use the mark "
        "in commerce as required by § 1(b) of the Lanham Act. Discovery is expected to "
        "reveal that Applicant has no business plan, no products, no manufacturing capacity, "
        "no distribution agreements, no marketing materials, and no employees. See "
        "<i>M.Z. Berger &amp; Co. v. Swatch AG</i>, 787 F.3d 1368 (Fed. Cir. 2015).", S_NORMAL))
    s.append(Paragraph(
        "WHEREFORE, Opposer respectfully requests that this opposition be sustained and "
        "registration of Application Serial No. 97/901.448 be refused.", S_NORMAL))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Dated: April 03, 2026", S_NORMAL))
    s.append(Paragraph("Respectfully submitted,", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("WHITMAN BRENNAN FORSYTHE LLP", S_NORMAL))
    s.append(Paragraph("By: /J. Halston Whitman III/", S_NORMAL))
    s.append(Paragraph(
        "J. Halston Whitman III (USPTO Reg. 48,772)<br/>"
        "Priscilla Forsythe-Vanderhof (USPTO Reg. 62,114)<br/>"
        "1290 Avenue of the Americas, 41st Floor<br/>"
        "New York, NY 10104 · (212) 555-0188", S_SMALL))
    return s

story += blatt_ttab_grounds()
story.append(PageBreak())

def blatt_ttab_answer():
    s = []
    s.append(Paragraph("<b>APPLICANT'S ANSWER TO NOTICE OF OPPOSITION</b>", S_CENTER))
    s.append(Paragraph("Opposition No. 91/289.412", S_CENTER))
    s.append(HLine(thickness=0.8))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Applicant Klotzkettie LLC, by and through its undersigned pro se representative, "
        "hereby answers the Notice of Opposition as follows:", S_NORMAL))
    s.append(Paragraph(
        "1. <i>Admitted</i> that Applicant is a Delaware limited liability company.", S_NORMAL))
    s.append(Paragraph(
        "2. <i>Denied</i> as to all allegations regarding shell entity status; the "
        "Wilmington address is a duly registered commercial address.", S_NORMAL))
    s.append(Paragraph(
        "3. <i>Denied</i>. Applicant has no knowledge of any „Egon Brezelmann“ of Bad "
        "Mergentheim. Mr. Egonas Brezelmanas is a Lithuanian national and an independent "
        "businessman with no connection to any German entity.", S_NORMAL))
    s.append(Paragraph(
        "4–11. <i>Denied</i> as to all material allegations. Applicant specifically denies "
        "that the marks are confusingly similar. The mark KLOTZKETTIE is a fanciful term "
        "derived from the Lithuanian dialect words „klotz“ (block) and „kettie“ (small chain). "
        "Any phonetic similarity to Opposer's mark is coincidental.", S_NORMAL))
    s.append(Paragraph("<b>AFFIRMATIVE DEFENSES</b>", S_H3))
    s.append(Paragraph(
        "<b>First Affirmative Defense (Laches).</b> Opposer's claims are barred by the "
        "doctrine of laches. Opposer has been on notice of similar marks since at least "
        "2018 and has failed to enforce its rights.", S_NORMAL))
    s.append(Paragraph(
        "<b>Second Affirmative Defense (Unclean Hands).</b> Upon information and belief, "
        "Opposer itself has engaged in trademark bullying by issuing meritless cease-and-"
        "desist letters to small businesses.", S_NORMAL))
    s.append(Paragraph(
        "<b>Third Affirmative Defense (No Fame).</b> KLÔTZZKÈTTÉ is not famous within the "
        "meaning of § 43(c) — consumer awareness in the United States is below 4 %.", S_NORMAL))
    s.append(Paragraph(
        "WHEREFORE, Applicant respectfully requests that the opposition be dismissed in its "
        "entirety with prejudice and that the opposed application proceed to registration.",
        S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Dated: April 28, 2026", S_NORMAL))
    s.append(Paragraph("/s/ Egonas Brezelmanas", S_NORMAL))
    s.append(Paragraph("Egonas Brezelmanas, Member · Klotzkettie LLC<br/>251 Little Falls "
                       "Drive, Wilmington, DE 19808 · klotzkettie.llc@protonmail.com",
                       S_SMALL))
    s.append(Spacer(1, 0.4*cm))
    s.append(HandNote(
        "Pro se Antwort?? Lächerlich.\n"
        "Forsythe-Vanderhof meint:\n"
        "Default Judgment in 60 Tagen wenn\n"
        "er die Discovery Disclosures versemmelt.\n"
        "Strategie: Aggressiv Interrogatories raus.\n"
        "— A.St.",
        font=FONT_HAND, size=14, angle=-1.2, w=14*cm))
    return s

story += blatt_ttab_answer()
story.append(PageBreak())

def blatt_ttab_scheduling():
    s = []
    s.append(Paragraph("<b>TRADEMARK TRIAL AND APPEAL BOARD</b>", S_CENTER))
    s.append(Paragraph("Mailing Address: P.O. Box 1451 · Alexandria, VA 22313-1451",
                        S_CENTER))
    s.append(HLine(thickness=0.8))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("Opposition No. 91/289.412", S_RIGHT))
    s.append(Paragraph("Mailed: May 04, 2026", S_RIGHT))
    s.append(Paragraph("<b>INSTITUTION AND SCHEDULING ORDER</b>", S_CENTER))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "A Notice of Opposition having been timely filed by klôtzzkètté Inc. against "
        "Application Serial No. 97/901.448 (KLOTZKETTIE), and an Answer having been filed "
        "thereto, the proceeding is hereby instituted. The dates below shall govern this "
        "proceeding pursuant to Trademark Rule 2.120(a)(2):", S_NORMAL))
    rows = [
        ["Event", "Deadline"],
        ["Deadline for Discovery Conference", "June 03, 2026"],
        ["Discovery Opens", "June 03, 2026"],
        ["Initial Disclosures Due", "July 03, 2026"],
        ["Expert Disclosures Due", "October 31, 2026"],
        ["Discovery Closes", "November 30, 2026"],
        ["Plaintiff's Pretrial Disclosures", "January 14, 2027"],
        ["Plaintiff's 30-day Trial Period Ends", "February 28, 2027"],
        ["Defendant's Pretrial Disclosures", "March 14, 2027"],
        ["Defendant's 30-day Trial Period Ends", "April 28, 2027"],
        ["Plaintiff's Rebuttal Disclosures", "May 13, 2027"],
        ["Plaintiff's 15-day Trial Period Ends", "June 12, 2027"],
        ["Plaintiff's Opening Brief Due", "August 11, 2027"],
        ["Defendant's Brief Due", "September 10, 2027"],
        ["Plaintiff's Reply Brief Due", "September 25, 2027"],
        ["Request for Oral Hearing (Optional)", "October 25, 2027"],
    ]
    t = Table(rows, colWidths=[10.5*cm, 5*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1c2e4a")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.black),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f0eee4")]),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "The parties are reminded that pursuant to TBMP § 401 et seq., a discovery conference "
        "must be held within thirty days of the date hereof. Should the parties fail to "
        "conduct said conference, the Board may, upon motion or sua sponte, sanction the "
        "non-cooperating party.", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("By the Board:", S_NORMAL))
    s.append(Paragraph("/Cheryl S. Goodman/", S_NORMAL))
    s.append(Paragraph("Cheryl S. Goodman, Interlocutory Attorney<br/>"
                        "Trademark Trial and Appeal Board",
                        S_SMALL))
    s.append(Spacer(1, 0.3*cm))
    s.append(StampBox("FILED\nESTTA\n05/04/2026", angle=-6, w=4.5*cm, h=1.8*cm))
    return s

story += blatt_ttab_scheduling()
story.append(PageBreak())

print("[part18] done")
