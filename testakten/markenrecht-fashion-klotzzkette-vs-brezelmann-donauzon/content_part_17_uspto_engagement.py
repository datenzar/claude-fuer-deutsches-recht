# Part 17: USPTO Engagement Letter Whitman Brennan Forsythe LLP + Power of Attorney
def blatt_wbf_engagement_letter():
    s = []
    s.append(WBFLetterhead(
        recipient="klôtzzkètté Inc.\n712 Fifth Avenue, 36th Floor\nNew York, NY 10019\n\nAttention: Corporate Counsel",
        date="March 14, 2026",
        file_no="WBF-2026-KK-0014",
        re_line="Engagement Letter / Retainer Agreement — Trademark Portfolio Matters"))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Dear Sir or Madam:", S_NORMAL))
    s.append(Paragraph(
        "On behalf of <b>Whitman Brennan Forsythe LLP</b> (the „Firm“), I am pleased to confirm "
        "the engagement of this Firm by <b>klôtzzkètté Inc.</b> (the „Client“) in connection with "
        "the matters described herein. This Engagement Letter, together with the Standard Terms "
        "of Engagement (Annex A) attached hereto, constitutes the entire agreement between us.",
        S_NORMAL))
    s.append(Paragraph("<b>1. Scope of Engagement</b>", S_H3))
    s.append(Paragraph(
        "The Firm shall represent the Client in connection with the following intellectual "
        "property matters before the United States Patent and Trademark Office („USPTO“), the "
        "Trademark Trial and Appeal Board („TTAB“), the U.S. Customs and Border Protection "
        "(„CBP“), and — as may become necessary — before the United States District Courts "
        "(initially the Southern District of New York):", S_NORMAL))
    items = [
        "(a) Filing and prosecution of U.S. trademark applications for the KLÔTZZKÈTTÉ word mark, "
        "the K°° crown design mark, the position mark (gold thread insignia, sole position), "
        "the trade dress of the hexagonal flacon, and a haptic/tactile mark for the silk twill "
        "weave pattern (collectively, the „Marks“) — all on a TEAS Plus / TEAS Standard basis "
        "as applicable;",
        "(b) Recordation of the Marks with the U.S. Customs and Border Protection through the "
        "e-Recordation portal (estimated CBP Reg. No. TMK-26-08812);",
        "(c) Prosecution of Opposition No. 91/289.412 before the TTAB against the application "
        "of Klotzkettie LLC (Wilmington, DE), and ancillary discovery matters;",
        "(d) Coordination with the European Union counsel (Steinacker Lichtenberg &amp; Partners "
        "IP Boutique, Munich) regarding Madrid Protocol designations into the United States and "
        "related international portfolio harmonization;",
        "(e) Pre-litigation enforcement matters, including the issuance of cease-and-desist "
        "letters to identified U.S. infringers (initially: A&amp;K Boulevard Boutique LLC, "
        "New York, regarding „inspired-by-klôtzzkètté“ scarves);",
        "(f) Such further matters as the Client may from time to time direct in writing.",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18, firstLineIndent=-18)))
    s.append(Paragraph("<b>2. Hourly Rates and Retainer</b>", S_H3))
    s.append(Paragraph(
        "Fees will be billed at the following standard hourly rates (subject to annual "
        "adjustment): J. Halston Whitman III (Managing Partner) — US$ 1,450/hour; "
        "Priscilla Forsythe-Vanderhof, Esq. (Senior Associate) — US$ 695/hour; "
        "Paralegal (e.g., M. Pruitt-Calhoun) — US$ 285/hour. An initial retainer in the amount "
        "of <b>US$ 75,000.00</b> shall be wire-transferred to the Firm's Trust Account (J.P. "
        "Morgan, ABA 021-000-021, A/c 802-114-771-K) within ten (10) business days of the "
        "execution of this letter, to be drawn down against invoices issued monthly.", S_NORMAL))
    s.append(Paragraph("<b>3. Confidentiality and Privilege</b>", S_H3))
    s.append(Paragraph(
        "All communications between the Firm and the Client shall be protected by the attorney-"
        "client privilege under New York State and federal law (DR 4-101; ABA Model Rule 1.6); "
        "such privilege shall be maintained also as against the Client's European counsel under "
        "common-interest doctrine. Both Firms shall execute a Common Interest Agreement (Exhibit "
        "B), dated as of even date herewith.", S_NORMAL))
    s.append(Paragraph("<b>4. Governing Law and Dispute Resolution</b>", S_H3))
    s.append(Paragraph(
        "This Engagement Letter shall be governed by the laws of the State of New York, without "
        "regard to choice-of-law principles. Any dispute arising hereunder shall be resolved "
        "by binding arbitration before the American Arbitration Association in New York, NY, "
        "under the Commercial Arbitration Rules.", S_NORMAL))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Very truly yours,", S_NORMAL))
    s.append(Spacer(1, 0.6*cm))
    s.append(Paragraph("__________________________________", S_NORMAL_LEFT))
    s.append(Paragraph("<b>J. Halston Whitman III</b>", S_NORMAL_LEFT))
    s.append(Paragraph(
        "Managing Partner · Whitman Brennan Forsythe LLP<br/>"
        "Member, New York / New Jersey / D.C. Bars; Reg. U.S. Patent Atty. (Reg. No. 48,772)",
        S_SMALL))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("AGREED AND ACCEPTED on behalf of klôtzzkètté Inc.:", S_NORMAL))
    s.append(Spacer(1, 0.6*cm))
    s.append(Paragraph("By: __________________________________  Date: ____________", S_NORMAL_LEFT))
    s.append(Paragraph("Name: Comtesse Béatrice de Klôtzzkètté-Visconti (Chair, klôtzzkètté Inc.)",
                        S_SMALL))
    return s

story += blatt_wbf_engagement_letter()
story.append(PageBreak())

# Power of Attorney
def blatt_power_of_attorney():
    s = []
    s.append(Paragraph("<b>POWER OF ATTORNEY</b>", S_CENTER))
    s.append(Paragraph("Form Adapted from PTO/AIA/82 — For Use with USPTO Trademark Applications",
                        S_CENTER))
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph(
        "I, <b>Comtesse Béatrice de Klôtzzkètté-Visconti</b>, in my capacity as Chair of the "
        "Board of Directors of klôtzzkètté Inc. (a Delaware Corporation; principal place of "
        "business: 712 Fifth Avenue, 36th Floor, New York, NY 10019), hereby appoint and "
        "constitute as the attorneys of record before the United States Patent and Trademark "
        "Office the following individuals, with full authority to prosecute, transact business, "
        "and act for and on behalf of klôtzzkètté Inc. in any and all trademark applications "
        "and registrations now or hereafter owned by klôtzzkètté Inc., including without "
        "limitation the applications enumerated in Schedule A hereto:", S_NORMAL))
    rows = [
        ["Practitioner", "USPTO Reg. No.", "Bar Memberships", "Status"],
        ["J. Halston Whitman III", "48,772", "NY, NJ, D.C.", "Managing Partner — Primary"],
        ["Priscilla Forsythe-Vanderhof", "62,114", "NY, MA", "Senior Associate — Secondary"],
        ["Reginald A. Brennan IV", "44,309", "NY, CT, FL", "Of Counsel — Backup"],
        ["Hadrian M. Pruitt-Calhoun", "—", "Paralegal", "Document filings only"],
    ]
    t = Table(rows, colWidths=[5.0*cm, 2.6*cm, 3.0*cm, 5.4*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#3a2c1a")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888888")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f5f1e6")]),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "This Power of Attorney revokes any prior power of attorney filed in connection with "
        "the trademark applications and registrations of klôtzzkètté Inc. and supersedes the "
        "same in its entirety. The correspondence address for all applications listed in "
        "Schedule A shall be: <b>Whitman Brennan Forsythe LLP, 1290 Avenue of the Americas, "
        "41st Floor, New York, NY 10104, Attention: J. H. Whitman III, Esq.</b>", S_NORMAL))
    s.append(Paragraph("<b>Schedule A — Trademark Applications (current)</b>", S_H3))
    sched = [
        ["Serial No.", "Mark / Subject", "Class(es)", "Filing Basis"],
        ["97/884.117", "KLÔTZZKÈTTÉ (word mark)", "25 (clothing)", "ITU — § 1(b)"],
        ["97/884.117a", "KLÔTZZKÈTTÉ (word mark — Cl. 14)", "14 (jewelry)", "ITU — § 1(b)"],
        ["97/884.117b", "KLÔTZZKÈTTÉ (word mark — Cl. 3)", "3 (perfume)", "ITU — § 1(b)"],
        ["97/884.117c", "KLÔTZZKÈTTÉ (word mark — Cl. 18)", "18 (leather)", "ITU — § 1(b)"],
        ["97/884.118", "K°° crown design (logo)", "25", "1(a) — Use in commerce"],
        ["97/884.119", "Gold thread insignia (position mark, insole)", "25", "1(a)"],
        ["97/884.120", "Hexagonal flacon trade dress", "3", "1(a)"],
        ["97/884.121", "Haptic/tactile mark — silk twill weave", "24, 25", "ITU — § 1(b)"],
        ["IR 1.488.220", "Madrid Protocol Designation (basing on EU)", "3, 14, 18, 25, 35", "§ 66(a)"],
    ]
    t = Table(sched, colWidths=[2.8*cm, 6.5*cm, 3.0*cm, 3.7*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 8.5),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1c2e4a")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888888")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f5f1e6")]),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Executed this 14th day of March, 2026.", S_NORMAL))
    s.append(Spacer(1, 0.6*cm))
    s.append(Paragraph("___________________________________________", S_NORMAL_LEFT))
    s.append(Paragraph(
        "Comtesse Béatrice de Klôtzzkètté-Visconti<br/>"
        "Chair of the Board · klôtzzkètté Inc.", S_SMALL))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph(
        "<b>State of New York · County of New York · ss.:</b><br/>"
        "On this 14th day of March, 2026, before me personally appeared Comtesse Béatrice de "
        "Klôtzzkètté-Visconti, to me known and known to me to be the individual described in "
        "and who executed the foregoing instrument, and she acknowledged to me that she "
        "executed the same in her capacity stated.", S_SMALL))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("____________________________________  (NOTARY SEAL)", S_NORMAL_LEFT))
    s.append(Paragraph("Marlon Whittaker-Smythe — Notary Public, State of New York<br/>"
                        "Commission Expires April 30, 2028 · No. 01WH6044712", S_SMALL))
    return s

story += blatt_power_of_attorney()
story.append(PageBreak())

print("[part17] done")
