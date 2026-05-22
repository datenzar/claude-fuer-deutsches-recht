# Part 20: Cease & Desist to A&K Boulevard Boutique LLC (NYC)
def blatt_cd_letter_1():
    s = []
    s.append(WBFLetterhead(
        recipient="A&K Boulevard Boutique LLC\nAttn: Mr. Aaron Kalman, Managing Member\n"
                  "874 Madison Avenue\nNew York, NY 10075\n\nAlso via certified mail, RRR\n"
                  "and email: info@ak-boulevard.nyc",
        date="April 09, 2026",
        file_no="WBF-2026-KK-0014.07",
        re_line="DEMAND FOR IMMEDIATE CESSATION — Unauthorized Use of KLÔTZZKÈTTÉ Marks "
                "and Trade Dress; Counterfeit Silk Scarf Line"))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Dear Mr. Kalman:", S_NORMAL))
    s.append(Paragraph(
        "This firm represents <b>klôtzzkètté Inc.</b> (and its parent klôtzzkètté S.A. of "
        "Paris, France; collectively „klôtzzkètté“), the owner and exclusive licensee of "
        "certain federally protected trademark and trade dress rights in the United States, "
        "including but not limited to:", S_NORMAL))
    items = [
        "(i) The word mark <b>KLÔTZZKÈTTÉ</b>, the subject of U.S. App. Ser. No. 97/884.117 "
        "(filed Nov. 12, 2025) and U.S. common law rights extending continuously to 1958;",
        "(ii) The K°° crown design mark (App. 97/884.118);",
        "(iii) The position mark consisting of the gold thread insignia woven into the inner "
        "sole of each shoe (App. 97/884.119);",
        "(iv) The distinctive hexagonal flacon trade dress (App. 97/884.120);",
        "(v) The haptic/tactile mark covering the unique silk twill weave pattern of 18 momme "
        "with three intersecting rhombi (App. 97/884.121);",
        "(vi) The federally recorded CBP TMK-26-08812 covering all of the above.",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    s.append(Paragraph(
        "It has come to our client's attention through an investigation conducted by "
        "Spürnase-Couture GmbH (Munich) and confirmed by test purchases on April 02 and "
        "April 06, 2026, that A&amp;K Boulevard Boutique LLC is offering for sale, in its "
        "Madison Avenue boutique and through its e-commerce platform www.ak-boulevard.nyc, "
        "a line of silk scarves marketed under the descriptor „<i>Inspired-by-Klôtzzkètté "
        "Twill</i>“ at a retail price point of US$ 380 (vs. klôtzzkètté's own retail of "
        "US$ 695 for the genuine „K°° Touch Royal“ collection).", S_NORMAL))
    s.append(Paragraph(
        "Test-purchase Specimens A-1 and A-2 (held in attorney custody, available for "
        "inspection) bear: (a) the wholly unauthorized phrase „Klôtzzkètté“ in identical "
        "typeface; (b) a near-identical reproduction of the K°° crown logo with only the "
        "diacriticals shifted by 2°; and (c) the three-intersecting-rhombi weave pattern "
        "that is the subject of klôtzzkètté's pending haptic mark.", S_NORMAL))
    s.append(Paragraph("<b>I.  YOUR CONDUCT IS UNLAWFUL</b>", S_H3))
    s.append(Paragraph(
        "Your conduct constitutes, inter alia:", S_NORMAL))
    items = [
        "<b>(a) Trademark Infringement</b> under § 32(1) of the Lanham Act, 15 U.S.C. § "
        "1114(1), and at common law;",
        "<b>(b) False Designation of Origin / Unfair Competition</b> under § 43(a) of the "
        "Lanham Act, 15 U.S.C. § 1125(a);",
        "<b>(c) Trademark Dilution by Blurring and Tarnishment</b> under § 43(c), 15 U.S.C. "
        "§ 1125(c), the KLÔTZZKÈTTÉ mark being a famous mark within the meaning of the "
        "statute (see, e.g., <i>Tiffany (NJ) Inc. v. Costco Wholesale Corp.</i>, 971 F.3d "
        "74 (2d Cir. 2020));",
        "<b>(d) Counterfeiting</b> under 15 U.S.C. § 1116(d), exposing your company and you "
        "personally to enhanced statutory damages of up to US$ 2,000,000 per counterfeit "
        "mark per type of goods (15 U.S.C. § 1117(c)(2)) and to treble damages and "
        "attorneys' fees under § 1117(b);",
        "<b>(e) Violations of New York General Business Law §§ 349, 360-l (Anti-Dilution).</b>",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    return s

story += blatt_cd_letter_1()
story.append(PageBreak())

def blatt_cd_letter_2():
    s = []
    s.append(Paragraph("<b>II.  DEMANDS</b>", S_H3))
    s.append(Paragraph(
        "Within <b>ten (10) business days</b> of the date of this letter (i.e., by April 23, "
        "2026, 5:00 p.m. EDT), your client shall:", S_NORMAL))
    items = [
        "1. Immediately and permanently cease and desist from any and all use of the "
        "KLÔTZZKÈTTÉ marks, the K°° crown logo, the haptic twill pattern, and any "
        "colorable imitation thereof in commerce in the United States;",
        "2. Remove all infringing products from your physical premises, your e-commerce "
        "site, and any third-party marketplaces (including but not limited to Donauzon "
        "Marketplace, eBay, Etsy, Vestiaire Collective, The RealReal);",
        "3. Provide a complete inventory of all infringing units manufactured, imported, "
        "sold, given away, or otherwise distributed since January 1, 2025, together with "
        "the identity of every supplier, distributor, and customer to whom such items have "
        "been sold;",
        "4. Deliver up for destruction, under attorney supervision, all unsold infringing "
        "inventory, all promotional materials, all marketing collateral, all hangtags, all "
        "carrier bags, and all packaging bearing the infringing matter;",
        "5. Disgorge all profits derived from the infringing sales (preliminary estimate: "
        "US$ 1.4 million across 3,684 units);",
        "6. Reimburse our client's reasonable attorneys' fees and investigation costs "
        "incurred to date (currently US$ 47,890.00);",
        "7. Execute a Settlement Agreement and Consent Judgment substantially in the form "
        "enclosed (Annex C), including a permanent injunction;",
        "8. Provide written confirmation under oath, executed by an authorized officer, "
        "that the foregoing has been complied with in full.",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    s.append(Paragraph("<b>III.  CONSEQUENCES OF NON-COMPLIANCE</b>", S_H3))
    s.append(Paragraph(
        "Failure to comply with the foregoing demands within the time specified will leave "
        "klôtzzkètté no alternative but to commence litigation in the United States District "
        "Court for the Southern District of New York seeking, inter alia:", S_NORMAL))
    items = [
        "• A temporary restraining order and preliminary injunction pursuant to Fed. R. Civ. "
        "P. 65 and 15 U.S.C. § 1116;",
        "• An ex parte seizure order under § 1116(d) — note that your premises at 874 "
        "Madison Avenue have already been mapped for U.S. Marshal entry;",
        "• A permanent injunction;",
        "• An accounting and disgorgement of profits;",
        "• Actual damages plus treble damages (15 U.S.C. § 1117(b));",
        "• In the alternative, statutory damages of up to US$ 2,000,000 per counterfeit "
        "mark per type of goods;",
        "• Reasonable attorneys' fees (this is an exceptional case within the meaning of "
        "§ 1117(a) and § 1117(b));",
        "• Costs of suit;",
        "• Such other and further relief as the Court may deem just and proper.",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    s.append(Paragraph("<b>IV.  PRESERVATION OF EVIDENCE</b>", S_H3))
    s.append(Paragraph(
        "You are hereby placed on notice of a litigation hold. You are required to preserve, "
        "and to instruct your employees, officers, and agents to preserve, all documents, "
        "electronically stored information (including emails, text messages, chat logs, "
        "WhatsApp, Signal, and Slack communications), physical evidence, and metadata "
        "relating in any way to the infringing products. Spoliation of evidence may result "
        "in severe sanctions, including adverse inference instructions and dispositive "
        "sanctions under Fed. R. Civ. P. 37(e).", S_NORMAL))
    s.append(Paragraph("<b>V.  RIGHTS RESERVED</b>", S_H3))
    s.append(Paragraph(
        "This letter is sent without prejudice to any of klôtzzkètté's rights and remedies, "
        "all of which are expressly reserved. Nothing herein shall be construed as a waiver "
        "of any such rights. Any communication from your side should be directed exclusively "
        "to the undersigned.", S_NORMAL))
    s.append(Paragraph("Very truly yours,", S_NORMAL))
    s.append(Spacer(1, 0.5*cm))
    s.append(Paragraph("/J. Halston Whitman III/", S_NORMAL))
    s.append(Paragraph(
        "J. Halston Whitman III, Esq.<br/>"
        "cc:  Priscilla Forsythe-Vanderhof, Esq. (file)<br/>"
        "      Dr. Dr. A. Steinacker-von Tarsis (EU co-counsel, München)<br/>"
        "      Comtesse Béatrice de Klôtzzkètté-Visconti (Chair, klôtzzkètté Inc.)",
        S_SMALL))
    s.append(Spacer(1, 0.4*cm))
    s.append(HandNote(
        "Boulevard Boutique = 5. Sturm seit Januar.\n"
        "Wenn die nicht in 10 Tagen einknicken,\n"
        "Tiffany v. Costco-Pattern: SDNY TRO + Marshal Seizure.\n"
        "Halston meint, Aaron Kalman ist ein „repeat player“\n"
        "(zuvor Gucci-Klage 2019). Wird zahlen.\n"
        "— P. Forsythe-V., 4/9/26",
        font=FONT_HAND2, size=13.5, angle=0.8, w=15*cm))
    return s

story += blatt_cd_letter_2()
story.append(PageBreak())

print("[part20] done")
