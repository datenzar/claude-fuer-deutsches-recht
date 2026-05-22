# Part 28: EUIPO Board of Appeal — Antwort der Beschwerdegegnerin + Spürnase II Bericht
def blatt_euipo_boa_response_1():
    s = []
    s.append(Paragraph("<b>EUIPO — BOARDS OF APPEAL — FIFTH BOARD</b>", S_CENTER))
    s.append(Paragraph("Case R 0 882/2025-5 — Appeal Number — RESPONSE OF THE APPELLEE",
                        S_CENTER))
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.3*cm))
    rows = [
        ["Appellant:", "UAB klotzkettie (Vilnius, LT)"],
        ["Appellee / Opponent:", "klôtzzkètté S.A. (Paris, FR) — represented by "
                                  "Steinacker Lichtenberg &amp; Partners"],
        ["Underlying case:", "EUIPO Opposition Division Interim Decision of 08/05/2026, "
                              "B 4 187 932"],
        ["Decision under appeal:", "Refusal of EUTM App. 018 998 712 in Cl. 18, 25, 35 "
                                    "(Cl. 3 also)"],
        ["Date of appeal:", "07/06/2026"],
        ["Response deadline:", "07/08/2026"],
    ]
    t = Table(rows, colWidths=[4.5*cm, 12*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("FONTNAME", (0,0), (0,-1), "Times-Bold"),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888")),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>RESPONSE OF THE APPELLEE</b>", S_CENTER))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("Honourable Members of the Fifth Board of Appeal,", S_NORMAL))
    s.append(Paragraph(
        "klôtzzkètté S.A. (the „Appellee“ and Opponent in the underlying proceeding) "
        "respectfully submits the following observations in response to the Notice of "
        "Appeal filed by UAB klotzkettie (the „Appellant“) on 07 June 2026, and requests "
        "that the appeal be dismissed in its entirety, with costs.", S_NORMAL))
    s.append(Paragraph("<b>I. PROCEDURAL HISTORY</b>", S_H3))
    s.append(Paragraph(
        "1. The Opposition Division of 08/05/2026 (B 4 187 932) provisionally upheld the "
        "opposition with respect to Classes 18, 25, 35 (Article 8(1)(b) and 8(5) EUTMR) "
        "and Class 3 (Article 8(1)(b) on the basis of the pending EUIPO scent mark "
        "019 002 118), and ordered the Appellee to submit additional reputation evidence "
        "for Germany and the Baltic States by 10/07/2026. Said evidence was timely "
        "submitted on 02/07/2026 (1,488 pages, including: Nielsen DE 2025 brand-tracker "
        "data; LRT-TV broadcast affidavits Latvia/Lithuania/Estonia 2022-2025; "
        "BrandFinance 2024-2025 rankings; depositions of three boutique managers from "
        "Munich, Berlin, Hamburg).", S_NORMAL))
    s.append(Paragraph("<b>II. APPELLANT'S GROUNDS OF APPEAL — ANALYSIS</b>", S_H3))
    s.append(Paragraph(
        "2. The Appellant raises four grounds of appeal. None of them, with respect, "
        "have merit.", S_NORMAL))
    s.append(Paragraph("<b>A. „No Likelihood of Confusion“ — rejected</b>", S_H3))
    s.append(Paragraph(
        "3. The Appellant argues that the marks differ in the doubled-Z and the "
        "diacriticals. As the Opposition Division correctly held, these are visual "
        "minutiae which the average consumer of luxury fashion goods does not "
        "consistently retain (cf. <i>Lloyd Schuhfabrik Meyer</i>, C-342/97; <i>SABEL</i>, "
        "C-251/95). The Appellant's mark is, phonetically and conceptually, a virtually "
        "identical copy of the Opponent's mark, and the goods are identical or closely "
        "related.", S_NORMAL))
    s.append(Paragraph(
        "4. The Appellant's reliance on <i>Lévi-Strauss/Procter &amp; Gamble</i> "
        "(C-145/05) is misplaced; that decision concerned three-dimensional shape marks "
        "and is inapposite here.", S_NORMAL))
    s.append(Paragraph("<b>B. „No Reputation in DE/Baltikum“ — rejected</b>", S_H3))
    s.append(Paragraph(
        "5. The Appellant's argument was rendered moot by the supplementary evidence "
        "filed on 02/07/2026. The Opposition Division's preliminary conclusion (interim "
        "decision § 23) that the reputation in FR/IT/BNL is established remains "
        "uncontested. The new evidence raises the German aided-awareness figure to "
        "43.8 % (Nielsen Q1/2025) — above the threshold accepted by the Board in "
        "<i>R 1/2014-G</i>.", S_NORMAL))
    s.append(Paragraph("<b>C. „Bad Faith Allegation Unproven“ — wrong standard</b>", S_H3))
    s.append(Paragraph(
        "6. The Appellant argues that the Opposition Division accepted an unproven "
        "Article 59(1)(b) EUTMR claim. This is doubly wrong. <i>First</i>, bad faith "
        "is a ground for invalidity, not opposition; the Opposition Division did not "
        "rely on it. <i>Second</i>, the dossier nevertheless contains overwhelming "
        "circumstantial evidence — including the Brezelmann e-mail of 21.01.2026 "
        "(Annex B-6, file leaf 33) offering to „assign the mark for EUR 290,000“ — "
        "that the Appellant is a corporate appendage of an obstructive German "
        "discount retailer.", S_NORMAL))
    s.append(Paragraph("<b>D. „Coexistence in LT-market“ — irrelevant</b>", S_H3))
    s.append(Paragraph(
        "7. The Appellant submits affidavits from three Lithuanian retailers alleging "
        "„coexistence“ since 2019. Even were these affidavits accurate (which is "
        "disputed), Article 8(1)(b) EUTMR is an absolute Union-wide standard; "
        "national coexistence does not bar an opposition based on Union-wide rights "
        "(<i>Anheuser-Busch ./. Budějovický Budvar</i>, C-482/09).", S_NORMAL))
    return s

story += blatt_euipo_boa_response_1()
story.append(PageBreak())

def blatt_euipo_boa_response_2():
    s = []
    s.append(Paragraph("<b>III. ADDITIONAL OBSERVATIONS</b>", S_H3))
    s.append(Paragraph(
        "8. The Appellee respectfully draws the Board's attention to a parallel "
        "proceeding before the German Federal Patent Court (BPatG, 25 W (pat) 88/26) "
        "concerning the related sound mark <b>EUTM 019 002 117</b> (the K°° auftakt-"
        "motiv). The BPatG, by its decision of 04/05/2026, has signalled the "
        "registrability of the sound mark, citing the Opposition Division's interim "
        "decision approvingly. This cross-border consistency confirms the Appellee's "
        "right to the integrated „K°°“ multi-sensory brand identity.", S_NORMAL))
    s.append(Paragraph(
        "9. Furthermore, the Appellee has, since the date of the interim decision, "
        "filed three further haptic mark applications (DE 30 2026 102 887 — silk twill "
        "weave; DE 30 2026 102 888 — bergkristall flacon relief; pending US Serial "
        "97/884.121). The CJEU's <i>Sieckmann</i> jurisprudence (C-273/00) — which the "
        "Appellant invokes against the scent mark — does not apply to haptic marks, "
        "which are inherently capable of clear graphic representation (cf. expert "
        "opinion of Prof. Dr.-Ing. H. Tastenberger, TU Darmstadt, 22.04.2026, file "
        "leaf 91 ff.).", S_NORMAL))
    s.append(Paragraph("<b>IV. PRAYER FOR RELIEF</b>", S_H3))
    s.append(Paragraph(
        "10. The Appellee respectfully requests that the Board of Appeal:", S_NORMAL))
    items = [
        "(a) dismiss the appeal in its entirety;",
        "(b) confirm the Opposition Division's decision of 08/05/2026 in its entirety, "
        "including with respect to Class 3;",
        "(c) refuse EUTM application 018 998 712 in all classes (3, 18, 25, 35);",
        "(d) award costs of the appeal to the Appellee in the maximum permitted amount "
        "under Article 109 EUTMR and Article 18 EUTMIR;",
        "(e) such further or other relief as the Board may deem appropriate.",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Respectfully submitted,", S_NORMAL))
    s.append(Paragraph(
        "Steinacker Lichtenberg &amp; Partners IP Boutique<br/>"
        "Dr. Dr. A. Steinacker-von Tarsis, LL.M. (Cantab.) · M. Freiherr v. Brenkenhoff",
        S_NORMAL))
    s.append(Paragraph("Munich, 22 July 2026", S_RIGHT))
    s.append(Spacer(1, 0.4*cm))
    s.append(HLine())
    s.append(Paragraph("<b>SPÜRNASE-COUTURE GMBH — SUPPLEMENTARY INVESTIGATION REPORT II</b>",
                        S_H3))
    s.append(Paragraph("(Annex B-44 to the Berufung OLG; Annex S-2 to the EUIPO BoA response)",
                        S_SMALL))
    s.append(Spacer(1, 0.2*cm))
    rows = [
        ["Operative:", "Karla Kalt-Bandel (Lead) · Bastian Spürmüller-Fürst (Sub-Op.)"],
        ["Period:", "May 14 – June 22, 2026"],
        ["Brief:", "Document continued offer of „inspired-by“-klotzkettiee items by "
                    "Brezelmann Discount KG and Donauzon-Marketplace listings"],
        ["Methodology:", "Mystery-shopping (4 venues), online test-purchase (8 listings), "
                          "informant interview Vilnius (1 sitting, 02:15 h)"],
        ["Status:", "CONFIDENTIAL — Attorney's Eyes Only — Bates SC-2026-2-001 to -087"],
    ]
    t = Table(rows, colWidths=[3.5*cm, 13*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9),
        ("FONTNAME", (0,0), (0,-1), "Times-Bold"),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("<b>Befundzusammenfassung</b>", S_H3))
    s.append(Paragraph(
        "<b>1. Brezelmann Discount KG — Filialnetz.</b> In den Filialen Bad Mergentheim, "
        "Würzburg, Heilbronn und Stuttgart-Vaihingen wurden zwischen dem 14. und 28. Mai "
        "2026 weiterhin Schaltücher mit der Aufschrift „klotzkettiee — limited edition“ "
        "zum Verkaufspreis von EUR 12,99 angeboten. Bonbeleg-Kopien S-2-014 bis S-2-031. "
        "Die Ware wird nach Auskunft der Filialleiterin Frau M. Steigerwald (Bad "
        "Mergentheim) „direkt aus Vilnius über Donauzon-Logistics“ bezogen — wörtlich.",
        S_NORMAL))
    s.append(Paragraph(
        "<b>2. Donauzon Marketplace DE.</b> 38 aktive Listings wurden am 02.06.2026 "
        "dokumentiert. Trotz angeblicher Notice-and-Take-Down-Verpflichtung nach dem "
        "Urteil 27.07.2026 sind 19 dieser Listings am 22.06.2026 noch online. "
        "Screenshots S-2-032 bis S-2-061. ASIN-Liste anbei.", S_NORMAL))
    s.append(Paragraph(
        "<b>3. Informant Vilnius — „Q“.</b> Anonymer Informant bestätigte am 16.06.2026 "
        "in Café Forto Dvaras, Vilnius: UAB klotzkettie ist eine Briefkastenfirma mit "
        "EINEM einzigen Mitarbeiter („Egonas“ — vermutlich Brezelmann, deutscher Akzent, "
        "spricht kein Litauisch). Containerumschlag-Volumen Q1/2026: 3 Container á "
        "40-foot — geschätzte 28.000 Stück Ware. Bestimmungsorte: 80 % Donauzon FBA-"
        "Lager Werne (DE), 20 % über Donauzon Logistics nach LA/Long Beach.", S_NORMAL))
    s.append(Paragraph(
        "<b>4. Gesamtumsatz-Schätzung Brezelmann + UAB klotzkettie 2025-Q2/2026:</b> "
        "EUR 1.840.000 brutto (Spürnase-Modell, ±18 %).", S_NORMAL))
    s.append(Spacer(1, 0.2*cm))
    s.append(HandNote(
        "„Egonas“ = Egon. Der Akzent verrät ihn.\n"
        "Q hat Foto. Wenn nötig liefern wir das im Berufungstermin.\n"
        "Spürmüller-Fürst war beeindruckt von Q's Espresso-Kenntnis.\n"
        "Honorar 14.500 EUR netto, Rechnung folgt.\n"
        "— Karla K.-B., 23.06.2026",
        font=FONT_HAND2, size=13, angle=-0.5, w=15*cm))
    return s

story += blatt_euipo_boa_response_2()
story.append(PageBreak())

print("[part28] done")
