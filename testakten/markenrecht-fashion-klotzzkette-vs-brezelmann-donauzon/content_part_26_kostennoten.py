# Part 26: Drei Kostennoten / RVG-Aufstellungen (astronomisch)
def blatt_kostennote_1():
    s = []
    s.append(Briefkopf(
        kanzlei_block=("USt-IdNr.: DE 271 884 117\nKonto: Bayerische Vereinsbank\n"
                       "IBAN: DE07 7011 6678 0044 2117 12\nBIC: HYVEDEMMXXX"),
        recipient_block=("klôtzzkètté S.A.\nAttn: Comtesse Béatrice de Klôtzzkètté-Visconti\n"
                          "12 rue du Faubourg Saint-Honoré\n75008 Paris · France\n\n"
                          "Empfangsbestätigung erbeten"),
        datum="30. April 2026",
        az="2-03 O 412/26 — eV-Verfahren Brezelmann/Donauzon"))
    s.append(Spacer(1, 0.5*cm))
    s.append(Paragraph("<b>KOSTENNOTE Nr. 26-Q1-014/A</b>", S_CENTER))
    s.append(Paragraph("(Zwischenrechnung — Quartal I/2026, Phase eV LG Frankfurt)",
                        S_CENTER))
    s.append(HLine())
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph(
        "Sehr geehrte Frau Comtesse, sehr geehrte Damen und Herren,", S_NORMAL))
    s.append(Paragraph(
        "in der vorbezeichneten Sache erlauben wir uns, die nachstehende "
        "Zwischenkostennote für das I. Quartal 2026 zur Anweisung vorzulegen. "
        "Die Berechnung erfolgt nach dem Rechtsanwaltsvergütungsgesetz (RVG) auf "
        "Basis des gerichtlich festgesetzten Streitwertes von <b>EUR 4.800.000,00</b> "
        "(Beschluss LG Frankfurt vom 04.03.2026, Az. 2-03 O 412/26).", S_NORMAL))
    s.append(Spacer(1, 0.2*cm))
    rows = [
        ["Pos.", "Tatbestand · RVG-Nr.", "Faktor", "Betrag EUR"],
        ["1.", "Geschäftsgebühr (Nr. 2300 VV-RVG) — Vorabprüfung und Abmahnung "
              "Brezelmann/Donauzon", "1,8 *", "21.844,80"],
        ["2.", "Verfahrensgebühr eV (Nr. 3100 VV-RVG)", "1,3", "15.776,80"],
        ["3.", "Terminsgebühr (Nr. 3104 VV-RVG) — mündliche Verhandlung 11.06.2026 "
              "(vorgemerkt)", "1,2", "14.563,20"],
        ["4.", "Beweismittel-Recherche, Sachverständigen-Akquisition "
              "(Prof. Steinpfeil, Mlle Périgord, Spürnase-Couture)", "—", "8.480,00"],
        ["5.", "Auslagenpauschale (Nr. 7002 VV-RVG)", "—", "20,00"],
        ["6.", "Schreibauslagen, Telekom., DHL-Express Capri/Mailand", "—", "1.244,17"],
        ["7.", "Reisekosten Steinacker/Brenkenhoff "
              "(MUC↔FRA, 4 Termine; MUC↔FCO Mailand 1 Termin)", "—", "4.882,40"],
        ["8.", "Übersetzungen IT→DE (Tribunale Firenze)", "—", "2.114,90"],
        ["9.", "GV-Kosten (Pitti Uomo, Florenz) — Verauslagung", "—", "3.882,00"],
        ["10.", "Detektivkosten Spürnase-Couture (siehe Rechnung Bl. 31)", "—", "12.847,55"],
        ["", "<b>Nettosumme</b>", "", "<b>85.655,82</b>"],
        ["", "USt 19 %", "", "16.274,61"],
        ["", "<b>Bruttosumme · zu zahlen bis 30.05.2026</b>", "", "<b>101.930,43</b>"],
    ]
    t = Table(rows, colWidths=[1.0*cm, 10.0*cm, 1.8*cm, 3.7*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1c2e4a")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888")),
        ("ALIGN", (3,1), (3,-1), "RIGHT"),
        ("ALIGN", (2,1), (2,-1), "CENTER"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f5f1e6")]),
        ("BACKGROUND", (0,-3), (-1,-1), colors.HexColor("#ede0c8")),
        ("FONTNAME", (0,-3), (-1,-1), "Times-Bold"),
    ]))
    s.append(t)
    s.append(Paragraph(
        "* Erhöhter Faktor 1,8 wegen besonderer Bedeutung der Sache und "
        "internationaler Streuung (vgl. § 14 RVG).", S_SMALL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Die Bezahlung erbitten wir auf das oben genannte Konto unter Angabe "
        "der Rechnungsnummer 26-Q1-014/A. Bei Nichteinhaltung der Zahlungsfrist "
        "behalten wir uns vor, weitere Verfahrensschritte zurückzustellen "
        "(§ 9 BORA).", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Mit vorzüglicher Hochachtung", S_NORMAL))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph(
        "Dr. Dr. A. Steinacker-von Tarsis · M. Freiherr v. Brenkenhoff", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(HandNote(
        "Comtesse hat „No.“ geschrieben.\n"
        "Annabella: „No.“ heißt: zahlen, aber\n"
        "ohne Quittung an Buchhaltung.\n"
        "Verbucht 02.05. auf Banque Pictet.\n"
        "— Brenkenhoff",
        font=FONT_HAND3, size=11.5, angle=-1.4, w=11*cm))
    return s

story += blatt_kostennote_1()
story.append(PageBreak())

def blatt_kostennote_2():
    s = []
    s.append(WBFLetterhead(
        recipient="klôtzzkètté Inc.\nAttn: Treasurer / Comptroller\n"
                  "712 Fifth Avenue, 36th Floor\nNew York, NY 10019",
        date="May 02, 2026",
        file_no="WBF-2026-KK-0014",
        re_line="Invoice 26-04-1188 — Trademark Portfolio &amp; Enforcement Matters — April 2026"))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<b>INVOICE No. 26-04-1188 — FOR PROFESSIONAL SERVICES RENDERED</b>",
        S_CENTER))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph(
        "<b>Period:</b> April 01 – April 30, 2026<br/>"
        "<b>Matter:</b> WBF-2026-KK-0014 (all subfiles)<br/>"
        "<b>Bill-to Currency:</b> United States Dollars (USD)", S_NORMAL))
    s.append(Spacer(1, 0.2*cm))
    rows = [
        ["Date", "Timekeeper", "Description", "Hrs", "Rate", "Amount"],
        ["04/01", "JHW III", "Review CBP recordation acceptance; call w/ A. Steinacker re "
                              "container detention LA/LB", "1.4", "1,450", "2,030.00"],
        ["04/03", "PFV", "Draft &amp; finalize Notice of Opposition (TTAB 91/289.412); "
                          "ESTTA submission", "8.7", "695", "6,046.50"],
        ["04/03", "JHW III", "Final review &amp; sign-off Notice of Opposition", "0.8", "1,450",
         "1,160.00"],
        ["04/05", "RAB IV (Of Counsel)", "Delaware Chancery analysis re Klotzkettie LLC "
                                          "service of process", "2.1", "1,250", "2,625.00"],
        ["04/07", "PFV", "Investigation: A&amp;K Boulevard Boutique LLC; test purchase "
                          "review", "3.2", "695", "2,224.00"],
        ["04/09", "JHW III", "Draft &amp; issue C&amp;D letter to A&amp;K Boulevard Boutique LLC", "2.6",
         "1,450", "3,770.00"],
        ["04/09", "PFV", "C&amp;D letter review &amp; cite-check", "1.4", "695", "973.00"],
        ["04/12", "MPC (Para)", "Document production review re USPTO 97/884.117-121 file "
                                  "wrappers", "5.8", "285", "1,653.00"],
        ["04/15", "JHW III", "Telephonic conference w/ Comtesse de K-V re strategic "
                              "expansion (1.2 h) and follow-up memo", "2.4", "1,450",
         "3,480.00"],
        ["04/19", "JHW III", "CBP detention LA/LB — authentication response coordination",
         "1.8", "1,450", "2,610.00"],
        ["04/19", "PFV", "Drafting authentication affidavit for CBP", "3.6", "695",
         "2,502.00"],
        ["04/22", "PFV", "Office Action § 2(d) refusal — initial analysis &amp; "
                          "memo to file", "4.4", "695", "3,058.00"],
        ["04/26", "PFV", "Discovery Conference prep (TTAB) — outline; coordinate w/ "
                          "v. Brenkenhoff re GDPR", "2.8", "695", "1,946.00"],
        ["04/28", "JHW III", "Strategic conference w/ Steinacker re Mar. 21 Capri "
                              "instructions; carte-blanche scope review", "1.6", "1,450",
         "2,320.00"],
        ["04/30", "PFV", "Engagement memo 26-OPN-014 — declining Heinrich-Klotz "
                          "opposition (3-page opinion)", "5.2", "695", "3,614.00"],
        ["", "", "<b>Total Professional Fees (April 2026)</b>", "<b>47.8</b>", "",
         "<b>40,011.50</b>"],
        ["", "", "Disbursements: ESTTA filings, FedEx, CBP filing fees", "", "",
         "1,884.62"],
        ["", "", "Westlaw / TTABVUE research", "", "", "412.18"],
        ["", "", "<b>GRAND TOTAL — DUE WITHIN 30 DAYS</b>", "", "",
         "<b>USD 42,308.30</b>"],
    ]
    t = Table(rows, colWidths=[1.4*cm, 2.5*cm, 7.2*cm, 1.2*cm, 1.4*cm, 2.5*cm],
                repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 8.2),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#3a2c1a")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.2, colors.HexColor("#999")),
        ("ALIGN", (3,1), (-1,-1), "RIGHT"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f5f1e6")]),
        ("BACKGROUND", (0,-1), (-1,-1), colors.HexColor("#ede0c8")),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Payment shall be remitted by wire transfer to: J.P. Morgan Chase Bank N.A. — "
        "Whitman Brennan Forsythe LLP Trust Account — ABA 021-000-021 — "
        "A/c 802-114-771-K — Reference: WBF-26-04-1188.", S_SMALL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("/J. Halston Whitman III/", S_NORMAL))
    s.append(Paragraph("J. Halston Whitman III, Managing Partner", S_SMALL))
    return s

story += blatt_kostennote_2()
story.append(PageBreak())

def blatt_kostennote_3():
    s = []
    s.append(Paragraph("<b>BUDGET-PROGNOSE 2026/27 (intern)</b>", S_H1))
    s.append(Paragraph("<i>Erstellt durch v. Brenkenhoff, abgestimmt mit Forsythe-Vanderhof, "
                        "Stand 03.05.2026 — NICHT an Mandantin</i>", S_SMALL))
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.3*cm))
    rows = [
        ["Verfahren / Schauplatz", "Geschätzte Kosten gesamt (EUR-äquivalent)",
         "Verbucht Q1/Q2 2026", "Erwartet Q3/Q4 2026"],
        ["DE — eV LG FFM + Hauptsache OLG", "412.000", "138.000", "274.000"],
        ["DE — DPMA Anti-KI + Haptik (Schal/Flakon/Soie d'Aube)", "98.500", "47.200", "51.300"],
        ["DE — DPMA Löschung „klotzkettiee“", "32.000", "8.500", "23.500"],
        ["DE — BPatG + BGH Soundmarke", "144.000", "44.000", "100.000"],
        ["EU — EUIPO Widerspruch B 4 187 932 + BoA", "172.000", "88.000", "84.000"],
        ["EU — EUIPO Riechmarke (Sieckmann-Streit)", "68.500", "21.500", "47.000"],
        ["IT — Tribunale Firenze + GV Pitti Uomo", "55.000", "55.000", "—"],
        ["US — USPTO Anmeldungen (Word/Pos/Trade Dress/Haptik) ×5", "118.000", "62.000",
         "56.000"],
        ["US — TTAB Opposition 91/289.412", "284.000", "44.000", "240.000"],
        ["US — CBP TMK-26-08812 + Enforcement", "76.000", "28.000", "48.000"],
        ["US — C&amp;D Boulevard Boutique + ggf. SDNY-Klage", "342.000", "12.000", "330.000"],
        ["US — Office Action Response (Klotz Kettle Cookware)", "44.000", "12.000", "32.000"],
        ["US — Madrid Designation Begleitung", "21.000", "—", "21.000"],
        ["LT — Strafanzeige UAB klotzkettie (parallel)", "38.000", "—", "38.000"],
        ["Sachverständige (Steinpfeil, Périgord, Tastenberger, "
         "Soundeng. Aurelius)", "187.000", "92.000", "95.000"],
        ["Übersetzungen DE/EN/FR/IT/LT", "44.000", "18.000", "26.000"],
        ["Reisekosten (FFM, Alicante, NYC, Vilnius, Florenz, Capri)", "118.000", "44.000",
         "74.000"],
        ["Detektive Spürnase-Couture + US-Pendant Pinkerton NYC", "94.000", "32.000",
         "62.000"],
        ["Honorarpauschalen / Retainer-Aufstockungen (Reserve)", "200.000", "100.000",
         "100.000"],
        ["", "", "", ""],
        ["<b>SUMME (Schätzung)</b>", "<b>2.547.500</b>", "<b>846.200</b>",
         "<b>1.701.300</b>"],
    ]
    t = Table(rows, colWidths=[7.5*cm, 3.0*cm, 3.0*cm, 3.0*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 8.2),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1c2e4a")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888")),
        ("ALIGN", (1,1), (-1,-1), "RIGHT"),
        ("ROWBACKGROUNDS", (0,1), (-1,-2), [colors.white, colors.HexColor("#f5f1e6")]),
        ("BACKGROUND", (0,-1), (-1,-1), colors.HexColor("#ede0c8")),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<b>Beobachtungen:</b><br/>"
        "• EUR 2,55 Mio Schätzung über 24 Monate sind im Verhältnis zum kumulierten "
        "Streitwert (DE EUR 4,8 Mio + US USD 8,7 Mio = ca. EUR 12 Mio Gesamt) "
        "konservativ kalkuliert (≈ 21 % des Streitwertes; üblich 15–35 %).<br/>"
        "• Hauptrisiko: US-SDNY-Klage gegen Donauzon Marketplace USA LLC — bei "
        "Verteidigung &gt;60 Verhandlungstagen kann allein dieser Komplex auf "
        "USD 1,2 Mio anwachsen.<br/>"
        "• Comtesse muss in Q4/2026 schriftlich über Schwellenwert-Überschreitung "
        "informiert werden (Mandatsverpflichtung).<br/>"
        "• <i>De minimis non curat lex</i> — aber bei diesen Summen schon längst nicht "
        "mehr.", S_SMALL))
    s.append(Spacer(1, 0.3*cm))
    s.append(HandNote(
        "Halston meint: „This is a Picasso budget for a Mona-Lisa case.“\n"
        "Trotzdem realistisch. Comtesse wird zahlen.\n"
        "Comtesse zahlt immer.\n"
        "— A.St., 04.05.2026",
        font=FONT_HAND, size=14, angle=0.4, w=15*cm))
    return s

story += blatt_kostennote_3()
story.append(PageBreak())

print("[part26] done")
