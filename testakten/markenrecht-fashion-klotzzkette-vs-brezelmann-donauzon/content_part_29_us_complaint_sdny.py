# Part 29: SDNY Complaint draft + Damages Model (US side major escalation)
def blatt_sdny_complaint_1():
    s = []
    s.append(Paragraph("<b>UNITED STATES DISTRICT COURT</b>", S_CENTER))
    s.append(Paragraph("<b>SOUTHERN DISTRICT OF NEW YORK</b>", S_CENTER))
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.2*cm))
    cap = [
        ["KLÔTZZKÈTTÉ INC.,", "", ""],
        ["    Plaintiff,", "", "Case No. 1:26-cv-_____ (___)"],
        ["v.", "", ""],
        ["DONAUZON MARKETPLACE USA LLC;", "", "COMPLAINT FOR"],
        ["DONAUZON LOGISTICS USA LLC;", "", " (1) TRADEMARK INFRINGEMENT"],
        ["A&K BOULEVARD BOUTIQUE LLC;", "", " (2) UNFAIR COMPETITION"],
        ["UAB KLOTZKETTIE; KLOTZKETTIE LLC;", "", " (3) TRADEMARK COUNTERFEITING"],
        ["BREZELMANN DISCOUNT KG;", "", " (4) DILUTION (§ 43(c))"],
        ["EGONAS BREZELMANAS, individually;", "", " (5) NY GBL §§ 349, 360-l"],
        ["EGON BREZELMANN, individually;", "", ""],
        ["and JOHN DOES 1–25,", "", "JURY TRIAL DEMANDED"],
        ["    Defendants.", "", ""],
    ]
    t = Table(cap, colWidths=[7.5*cm, 0.6*cm, 8.4*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LINEAFTER", (0,0), (0,-1), 1.0, colors.black),
    ]))
    s.append(t)
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>COMPLAINT</b>", S_CENTER))
    s.append(Paragraph(
        "Plaintiff klôtzzkètté Inc., by its undersigned attorneys Whitman Brennan Forsythe "
        "LLP, for its Complaint against the above-named defendants, alleges as follows:",
        S_NORMAL))
    s.append(Paragraph("<b>NATURE OF THE ACTION</b>", S_H3))
    s.append(Paragraph(
        "1. This is an action for trademark infringement, trademark counterfeiting, false "
        "designation of origin, unfair competition, and trademark dilution under the "
        "Lanham Act, 15 U.S.C. §§ 1051 <i>et seq.</i>, and related state-law claims. "
        "Plaintiff seeks injunctive relief, an accounting and disgorgement of profits, "
        "treble damages, statutory damages of up to US$ 2,000,000 per counterfeit mark "
        "per type of goods, and attorneys' fees.", S_NORMAL))
    s.append(Paragraph("<b>JURISDICTION AND VENUE</b>", S_H3))
    s.append(Paragraph(
        "2. This Court has subject-matter jurisdiction pursuant to 15 U.S.C. § 1121 and "
        "28 U.S.C. §§ 1331, 1338, and 1367. Supplemental jurisdiction over the state-"
        "law claims is proper under 28 U.S.C. § 1367(a).", S_NORMAL))
    s.append(Paragraph(
        "3. Personal jurisdiction over the Defendants is proper because each Defendant "
        "(i) is incorporated, registered, or domiciled within the United States; or "
        "(ii) has purposefully directed substantial commerce into the State of New York "
        "via its e-commerce platform and physical retail presence (in the case of "
        "A&amp;K Boulevard Boutique LLC, at 874 Madison Avenue, NY 10075); or (iii) "
        "owns and controls a wholly-owned U.S. subsidiary doing business in this "
        "District. <i>See Daimler AG v. Bauman</i>, 571 U.S. 117 (2014).", S_NORMAL))
    s.append(Paragraph(
        "4. Venue is proper in this District under 28 U.S.C. § 1391(b)(2) because a "
        "substantial part of the events giving rise to the claim occurred in this "
        "District, including infringing sales at A&amp;K Boulevard Boutique's Madison "
        "Avenue location.", S_NORMAL))
    s.append(Paragraph("<b>THE PARTIES</b>", S_H3))
    s.append(Paragraph(
        "5. Plaintiff <b>klôtzzkètté Inc.</b> is a Delaware corporation with its "
        "principal place of business at 712 Fifth Avenue, 36th Floor, New York, NY "
        "10019. It is the wholly-owned U.S. subsidiary of klôtzzkètté S.A. of Paris, "
        "France. Plaintiff holds the exclusive U.S. license to the KLÔTZZKÈTTÉ marks.",
        S_NORMAL))
    s.append(Paragraph(
        "6. Defendant <b>Donauzon Marketplace USA LLC</b> is a Delaware limited liability "
        "company with its principal place of business at 410 Terry Avenue North, Seattle, "
        "Washington 98109. It operates the e-commerce platform www.donauzon.com.",
        S_NORMAL))
    s.append(Paragraph(
        "7. Defendant <b>Donauzon Logistics USA LLC</b> is a Delaware limited liability "
        "company whose principal place of business is in San Bernardino, California; it "
        "served as importer of record for the merchandise detained at Los Angeles/Long "
        "Beach Seaport on April 19, 2026 (CBP Detention 26-LAX-002-887).", S_NORMAL))
    s.append(Paragraph(
        "8. Defendant <b>A&amp;K Boulevard Boutique LLC</b> is a New York limited liability "
        "company with its principal place of business at 874 Madison Avenue, New York, "
        "NY 10075.", S_NORMAL))
    s.append(Paragraph(
        "9. Defendant <b>UAB klotzkettie</b> is a Lithuanian uždaroji akcinė bendrovė "
        "with its registered office at Vilniaus g. 47, LT-01402 Vilnius. Upon information "
        "and belief, its sole director is Egonas Brezelmanas.", S_NORMAL))
    s.append(Paragraph(
        "10. Defendant <b>Klotzkettie LLC</b> is a Delaware shell entity with its "
        "registered agent at 251 Little Falls Drive, Wilmington, DE 19808. It is "
        "the named applicant in U.S. Trademark App. Ser. No. 97/901.448, against which "
        "Plaintiff has commenced TTAB Opposition No. 91/289.412.", S_NORMAL))
    return s

story += blatt_sdny_complaint_1()
story.append(PageBreak())

def blatt_sdny_complaint_2():
    s = []
    s.append(Paragraph("<b>FACTUAL ALLEGATIONS</b>", S_H3))
    s.append(Paragraph(
        "11. The KLÔTZZKÈTTÉ mark has been used continuously in U.S. commerce since 1958. "
        "Plaintiff and its predecessors-in-interest have invested in excess of US$ 240 "
        "million in advertising, marketing, and brand-building in the United States. The "
        "KLÔTZZKÈTTÉ mark is famous within the meaning of 15 U.S.C. § 1125(c)(2)(A).",
        S_NORMAL))
    s.append(Paragraph(
        "12. The Defendants have engaged in a coordinated, transnational scheme to "
        "manufacture, import, distribute, and sell counterfeit goods bearing the "
        "KLÔTZZKÈTTÉ marks and confusingly similar variants thereof. The scheme operates "
        "through the following identifiable nodes:", S_NORMAL))
    items = [
        "<b>(a) Manufacture / Stockholding:</b> UAB klotzkettie (Vilnius) maintains an "
        "approximately 28,000-piece annual inventory of counterfeit silk scarves and "
        "ready-to-wear items; per a Pinkerton-Spürnase-Couture intelligence report of "
        "June 22, 2026 (Annex S-2), the operation is staffed by a single employee "
        "with a discernible German (not Lithuanian) accent;",
        "<b>(b) Import:</b> Donauzon Logistics USA LLC serves as importer of record. "
        "The April 19, 2026 detention of 2,488 pieces at Los Angeles/Long Beach (CBP "
        "Notice 26-LAX-002-887) is documented in Annex CBP-1;",
        "<b>(c) Wholesale Distribution / Marketplace Facilitation:</b> Donauzon "
        "Marketplace USA LLC hosts at least 38 active listings as of June 22, 2026, "
        "notwithstanding actual notice (Annex S-2-032 to -061);",
        "<b>(d) Retail Sale:</b> A&amp;K Boulevard Boutique LLC offers the goods at its "
        "Madison Avenue boutique under the false „inspired-by“ descriptor at US$ 380 "
        "per piece;",
        "<b>(e) U.S. Trademark Squatting:</b> Klotzkettie LLC was incorporated in "
        "Delaware solely to obtain a U.S. trademark registration for an essentially "
        "identical mark, with no intent or capacity to use the mark in commerce — a "
        "violation of <i>M.Z. Berger &amp; Co. v. Swatch AG</i>, 787 F.3d 1368 (Fed. Cir. "
        "2015);",
        "<b>(f) German Coordination:</b> Brezelmann Discount KG and Egon Brezelmann, "
        "operating out of Bad Mergentheim, Germany, are the moving force, beneficial "
        "owner, and alter ego of the foregoing entities — supported by the e-mail of "
        "January 21, 2026 in which Egon Brezelmann admitted his offering price for "
        "the German klotzkettiee mark (EUR 290,000).",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    s.append(Paragraph("<b>FIRST CLAIM FOR RELIEF — Trademark Counterfeiting (§ 1114)</b>",
                        S_H3))
    s.append(Paragraph(
        "13–18. [Allegations incorporated; Plaintiff alleges willful counterfeiting and "
        "elects, in the alternative, statutory damages of up to US$ 2,000,000 per "
        "counterfeit mark per type of goods, 15 U.S.C. § 1117(c)(2).]", S_NORMAL))
    s.append(Paragraph("<b>SECOND CLAIM — Federal Trademark Infringement</b>", S_H3))
    s.append(Paragraph(
        "19–22. [Allegations incorporated.]", S_NORMAL))
    s.append(Paragraph("<b>THIRD CLAIM — False Designation of Origin (§ 43(a))</b>", S_H3))
    s.append(Paragraph("23–26. [Allegations incorporated.]", S_NORMAL))
    s.append(Paragraph("<b>FOURTH CLAIM — Trademark Dilution (§ 43(c))</b>", S_H3))
    s.append(Paragraph("27–30. [Allegations incorporated. Plaintiff alleges both blurring "
                        "and tarnishment.]", S_NORMAL))
    s.append(Paragraph("<b>FIFTH CLAIM — NY GBL §§ 349, 360-l</b>", S_H3))
    s.append(Paragraph("31–34. [Allegations incorporated.]", S_NORMAL))
    s.append(Paragraph("<b>PRAYER FOR RELIEF</b>", S_H3))
    s.append(Paragraph(
        "WHEREFORE, Plaintiff respectfully prays for judgment against Defendants, jointly "
        "and severally, as follows:", S_NORMAL))
    items = [
        "(a) A permanent injunction;",
        "(b) An accounting and disgorgement of profits;",
        "(c) Actual damages plus treble damages (15 U.S.C. § 1117(b));",
        "(d) In the alternative, statutory damages of up to US$ 2,000,000 per "
        "counterfeit mark per type of goods (§ 1117(c)(2));",
        "(e) Reasonable attorneys' fees and costs (this is an „exceptional case“);",
        "(f) Pre-judgment and post-judgment interest;",
        "(g) Such other and further relief as the Court may deem just and proper.",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Dated: New York, New York — August 18, 2026", S_NORMAL))
    s.append(Paragraph("Respectfully submitted,", S_NORMAL))
    s.append(Paragraph("/s/ J. Halston Whitman III", S_NORMAL))
    s.append(Paragraph(
        "J. Halston Whitman III (USPTO Reg. 48,772) · Priscilla Forsythe-Vanderhof "
        "(USPTO Reg. 62,114)<br/>"
        "WHITMAN BRENNAN FORSYTHE LLP · 1290 Avenue of the Americas, 41st Fl. · NY 10104",
        S_SMALL))
    return s

story += blatt_sdny_complaint_2()
story.append(PageBreak())

def blatt_damages_model():
    s = []
    s.append(Paragraph("<b>DAMAGES MODEL — U.S. PROCEEDINGS</b>", S_H1))
    s.append(Paragraph("Internal memorandum · WBF-2026-KK-0014.DM-01 · 04 Sept. 2026",
                        S_SMALL))
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Prepared by P. Forsythe-Vanderhof, Esq., with input from forensic accountant "
        "Marcus T. Hollander, CPA/CFF (Hollander Forensic Group LLC, NYC).", S_SMALL))
    s.append(Paragraph(
        "Per the Comtesse's 14 March 2026 instruction («pas de compromis»), and the "
        "Wednesday Strategy Call of 02/09/2026, this memo sets forth a quantitative "
        "model for the prayer-for-relief monetary amounts in the SDNY Complaint.",
        S_NORMAL))
    rows = [
        ["Damages Component", "Computation", "Amount (USD)"],
        ["Actual lost-profit damages (Plaintiff's lost sales)",
         "Estimated diverted U.S. silk-scarf unit sales: 4,800 units × USD 695 retail × "
         "62.8 % gross margin × 36 month period", "1,310,592"],
        ["Defendant's profits (disgorgement, § 1117(a))",
         "UAB klotzkettie estimated US-channel profit (Spürnase model): "
         "USD 1,840,000 brutto × 0.78 net margin (low-overhead operation)",
         "1,435,200"],
        ["Treble damages (§ 1117(b) — willful counterfeit)",
         "(actual + profits) × 3", "8,237,376"],
        ["Statutory damages — alternative election (§ 1117(c)(2))",
         "5 counterfeit marks (word, K°°, position, trade dress, haptic) × 4 types of "
         "goods × USD 400,000 average (within § 1117(c)(2) ceiling of USD 2 mio)",
         "8,000,000"],
        ["Pre-judgment interest (NY 9 % p.a. simple, 28 mos.)",
         "8,237,376 × 0.09 × 28/12", "1,729,849"],
        ["Statutory attorneys' fees + costs (estimated)",
         "Fee award based on lodestar of approx. 2,400 hrs blended at USD 870/h",
         "2,088,000"],
        ["Disgorgement of Donauzon Marketplace platform fees",
         "Estimated 8 % × USD 4.6 mio gross sales of infringing third-party listings",
         "368,000"],
        ["", "<b>Lower Bound (no treble; statutory + interest + fees)</b>",
         "<b>9,448,440</b>"],
        ["", "<b>Mid Estimate (treble + interest + fees, no statutory)</b>",
         "<b>12,055,225</b>"],
        ["", "<b>Upper Bound (treble + statutory <i>elected</i> + interest + fees)</b>",
         "<b>13,420,425</b>"],
    ]
    t = Table(rows, colWidths=[5.0*cm, 8.5*cm, 3.0*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 8.5),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#3a2c1a")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888")),
        ("ALIGN", (2,1), (2,-1), "RIGHT"),
        ("ROWBACKGROUNDS", (0,1), (-1,-4), [colors.white, colors.HexColor("#f5f1e6")]),
        ("BACKGROUND", (0,-3), (-1,-1), colors.HexColor("#ede0c8")),
        ("FONTNAME", (1,-3), (-1,-1), "Times-Bold"),
    ]))
    s.append(t)
    s.append(Paragraph(
        "<b>Note re. statutory election.</b> Plaintiff cannot recover both actual + "
        "treble damages and statutory damages; § 1117(c) is an alternative election. "
        "Strategy: plead in alternative; elect at trial based on discovery posture. "
        "If Defendant's books are opaque (likely), statutory damages route is "
        "advantageous.", S_SMALL))
    s.append(Paragraph(
        "<b>Settlement Posture.</b> Recommend opening demand of USD 12.0 million plus "
        "consent permanent injunction and CBP-perpetual recordation cooperation. Lowest "
        "acceptable: USD 8.7 million plus injunction. Per Comtesse instruction "
        "«pas de pitié» — no walk-away under USD 6.5 million absent dispositive "
        "discovery defects.", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(HandNote(
        "Halston: „13.4 ist Sticker-Preis.\n"
        "Realistisch verhandelbar 8.7-10.2.\n"
        "Aber Comtesse will den 13.4er erst aufrufen.\n"
        "Wenn sie hartnäckig sind: bench trial vor\n"
        "Judge Failla? Sie ist tough on counterfeiters.“\n"
        "— P.F.-V., 09/04/2026, 18:22 EST",
        font=FONT_HAND, size=13.5, angle=-0.2, w=15*cm))
    return s

story += blatt_damages_model()
story.append(PageBreak())

print("[part29] done")
