# Part 24: EUIPO Zwischenentscheidung Widerspruchsabteilung B 4 187 932
def blatt_euipo_decision():
    s = []
    s.append(Paragraph("<b>EUROPEAN UNION INTELLECTUAL PROPERTY OFFICE</b>", S_CENTER))
    s.append(Paragraph("Avenida de Europa, 4 · E-03008 Alicante · Spain", S_CENTER))
    s.append(Paragraph("OPPOSITION DIVISION", S_CENTER))
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.3*cm))
    rows = [
        ["OPPOSITION No.:", "B 4 187 932"],
        ["Opponent:", "klôtzzkètté S.A., 12 rue du Faubourg Saint-Honoré, 75008 Paris (FR)"],
        ["Representative:", "Steinacker Lichtenberg & Partners IP Boutique (DE)"],
        ["Applicant:", "UAB klotzkettie, Vilniaus g. 47, LT-01402 Vilnius (LT)"],
        ["Representative:", "(none — direct filing)"],
        ["EUTM Application No.:", "018 998 712"],
        ["Mark:", "klotzkettie (word mark)"],
        ["Filed:", "07/11/2025"],
        ["Classes:", "3, 18, 25, 35"],
        ["Decision Date:", "08/05/2026"],
    ]
    t = Table(rows, colWidths=[4.5*cm, 12*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("FONTNAME", (0,0), (0,-1), "Times-Bold"),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888")),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<b>INTERIM DECISION OF THE OPPOSITION DIVISION OF 08/05/2026</b>", S_CENTER))
    s.append(HLine())
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("<b>I. FACTS</b>", S_H3))
    s.append(Paragraph(
        "On 11/02/2026, klôtzzkètté S.A. (the „Opponent“) filed a notice of opposition "
        "against EUTM Application No. 018 998 712 in the name of UAB klotzkettie (the "
        "„Applicant“), based on the following earlier rights:", S_NORMAL))
    rows = [
        ["Earlier Right", "Filing No.", "Status"],
        ["EUTM (word) — KLÔTZZKÈTTÉ", "EUTM 018 411 220", "Registered 14/03/2018"],
        ["EUTM (figurative) — K°° crown", "EUTM 017 224 119", "Registered 02/11/2017"],
        ["EUTM (position) — gold sole thread", "EUTM 018 712 884", "Registered 21/09/2022"],
        ["FR national — Klôtzzkètté", "FR 19/4.554.117", "Registered 1958, renewed 2018"],
        ["IT national — Klôtzzkètté", "IT 302.025.000.118.547", "Registered 1962"],
        ["EUIPO sound mark", "EUTM 019 002 117", "Pending — Bl. 47"],
        ["EUIPO scent mark", "EUTM 019 002 118", "Pending (Sieckmann obj.)"],
        ["DE haptic mark — silk twill", "DPMA 30 2026 102 887", "Pending"],
    ]
    t = Table(rows, colWidths=[6*cm, 5*cm, 5.5*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#003399")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888")),
    ]))
    s.append(t)
    s.append(Paragraph(
        "The opposition is based on Article 8(1)(b) and Article 8(5) EUTMR.", S_NORMAL))
    s.append(Paragraph("<b>II. RISK OF CONFUSION — Article 8(1)(b) EUTMR</b>", S_H3))
    s.append(Paragraph(
        "The Opposition Division finds, prima facie, that there exists a likelihood of "
        "confusion within the meaning of Article 8(1)(b) EUTMR with respect to all goods "
        "and services applied for in Classes 18, 25, and 35. The marks are aurally and "
        "conceptually highly similar; the only structural difference is the omission of "
        "the diacritics and the doubled Z in the contested sign — a difference which the "
        "average consumer of luxury goods will not consistently notice or recall (cf. "
        "<i>Lloyd Schuhfabrik</i>, C-342/97, paragraph 27).", S_NORMAL))
    s.append(Paragraph("<b>III. ENHANCED DISTINCTIVENESS / REPUTATION — Article 8(5)</b>", S_H3))
    s.append(Paragraph(
        "The Opponent claims that the earlier mark KLÔTZZKÈTTÉ enjoys an enhanced "
        "reputation acquired through use within the Union pursuant to Article 8(5) EUTMR. "
        "The evidence submitted (over 1,224 pages of catalogues, advertising spend "
        "documents, ranking reports, and consumer surveys) is substantial. The Division "
        "notes in particular:", S_NORMAL))
    items = [
        "(a) Worldwide annual advertising expenditure of EUR 34.8 million (2023);",
        "(b) Aided brand awareness of 78 % in France, 62 % in Italy, 41 % in Germany "
        "(Ipsos-Mori survey, 2024);",
        "(c) Inclusion in the BrandFinance „Luxury &amp; Premium 50“ (2024) at rank #24;",
        "(d) Continuous use since 1958 and EUTM registration since 2018.",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    s.append(Paragraph(
        "The Division accepts, on a provisional basis, the existence of an enhanced "
        "reputation in the territories of France, Italy, and the Benelux. The position "
        "with respect to Germany and the Baltic States requires further evidence.",
        S_NORMAL))
    return s

story += blatt_euipo_decision()
story.append(PageBreak())

def blatt_euipo_decision_2():
    s = []
    s.append(Paragraph("<b>IV. INTERIM ORDER</b>", S_H3))
    s.append(Paragraph(
        "The Opposition Division provisionally orders as follows:", S_NORMAL))
    s.append(Paragraph(
        "<b>(1)</b> The Opponent is invited to file additional evidence of reputation "
        "with respect to Germany and the Baltic States, within two (2) months of "
        "notification of this decision, i.e. by <b>10/07/2026</b>.", S_NORMAL))
    s.append(Paragraph(
        "<b>(2)</b> The Applicant is invited to submit observations on the merits of "
        "Article 8(1)(b) and 8(5) by the same date.", S_NORMAL))
    s.append(Paragraph(
        "<b>(3)</b> The cooling-off period having concluded on 14/04/2026 without "
        "settlement, the parties are reminded that further submissions shall be "
        "exchanged inter partes via the e-Comm portal.", S_NORMAL))
    s.append(Paragraph(
        "<b>(4)</b> The opposition with respect to Class 3 (perfumery) is provisionally "
        "<i>upheld</i> on the basis of EUTM 019 002 118 (scent mark), notwithstanding the "
        "Examiner's pending Sieckmann objection in the underlying registration "
        "procedure (cf. CJEU, C-273/00 <i>Sieckmann</i>).", S_NORMAL))
    s.append(Paragraph("<b>V. COSTS</b>", S_H3))
    s.append(Paragraph(
        "Costs shall be reserved to the final decision (Article 109(1) EUTMR).", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>The Opposition Division</b>", S_NORMAL))
    s.append(Paragraph("Marília RIBEIRO COSTA · Henrique VILELA-MATOS · Olga BORCZYK",
                        S_NORMAL))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph(
        "According to Article 67 EUTMR, an appeal against this interim decision is not "
        "admissible separately, but only together with the final decision.", S_SMALL))
    s.append(Spacer(1, 0.3*cm))
    s.append(StampBox("EUIPO\nE-COMM\n08/05/2026\nOpp. Div.", angle=-7, w=4.5*cm, h=2.2*cm))
    s.append(Spacer(1, 0.4*cm))
    s.append(HLine())
    s.append(Paragraph("<b>Aktenvermerk (intern) — Steinacker/Brenkenhoff, 09.05.2026, "
                        "11:14 MEZ</b>", S_H3))
    s.append(Paragraph(
        "Die <i>Zwischenentscheidung</i> ist im Wesentlichen ein Etappensieg: ", S_NORMAL))
    items = [
        "(a) Verwechslungsgefahr nach Art. 8(1)(b) EUTMR prima facie bejaht — exzellent.",
        "(b) Ruf nach Art. 8(5) für FR/IT/BNL akzeptiert; DE/Baltikum-Lücke ist Hausaufgabe — "
        "Mlle Périgord-Olfaktorik-Gutachten + Spürnase-Couture-Berichte werden zusätzlich "
        "verstärkt durch eine Nielsen-DE-Studie 2025 (Brand-Awareness 41 %, oben).",
        "(c) Klasse 3 vorläufig stattgegeben über die <i>pending</i> Riechmarke — "
        "bemerkenswert: das Amt ignoriert die eigene Sieckmann-Beanstandung. <i>De minimis "
        "lex non curat</i>; das werden wir nicht laut sagen, aber im Schriftsatz "
        "ausnutzen.",
        "(d) Klasse 35 (Einzelhandel/Online-Vertrieb) ist NICHT erwähnt — möglicherweise "
        "übersehen oder bewusst auf endgültige Entscheidung verlagert. Empfehlung: "
        "ausdrückliche Frage in den Folgeschriftsatz aufnehmen.",
        "(e) Frist 10.07.2026 — Mlle Périgord + Tastenberger werden Ergänzungsgutachten "
        "verfasst haben müssen bis 25.06.2026.",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    s.append(Paragraph(
        "<b>Querverweise:</b> Bl. 47 (Soundmarke), Bl. 71 (Comtesse-Anweisung), "
        "Bl. 88 ff. (Tastenberger-Gutachten), Bl. 102 (Mlle Périgord II — noch nicht "
        "erstellt).", S_SMALL))
    return s

story += blatt_euipo_decision_2()
story.append(PageBreak())

print("[part24] done")
