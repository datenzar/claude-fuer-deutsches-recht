# Part 01: Rubrum / Aktenvermerk Erstkontakt / Markenportfolio
# =====================================================================
# AKTENRUBRUM / Vorderblatt
# =====================================================================
def blatt_rubrum():
    s = []
    s.append(Spacer(1, 1.0*cm))
    s.append(Paragraph("STEINACKER  LICHTENBERG  &amp;  PARTNERS", S_CENTER))
    s.append(Paragraph("<i>— Intellectual Property Boutique —</i>", S_CENTER))
    s.append(Spacer(1, 1.4*cm))
    s.append(HLine(thickness=1.2))
    s.append(Spacer(1, 0.4*cm))
    big = ParagraphStyle("big", parent=S_CENTER, fontName="Times-Bold", fontSize=22, leading=26)
    s.append(Paragraph("HANDAKTE", big))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("<font size=14><b>Bd. I / IV</b></font>", S_CENTER))
    s.append(Spacer(1, 0.6*cm))
    s.append(HLine(thickness=0.6))
    s.append(Spacer(1, 0.7*cm))
    s.append(Paragraph("<b>klôtzzkètté S.A.</b>, Paris/Milano", S_CENTER))
    s.append(Paragraph("— Antragstellerin / Klägerin / Widersprechende —", S_CENTER))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<i>./.</i>", S_CENTER))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>Brezelmann Discount KG</b>, Bad Mergentheim", S_CENTER))
    s.append(Paragraph("<b>Donauzon Marketplace GmbH</b>, München / Luxembourg", S_CENTER))
    s.append(Paragraph("<b>UAB „klotzkettie“</b>, Vilnius", S_CENTER))
    s.append(Paragraph("<b>Klotzkettie LLC</b>, Wilmington, DE", S_CENTER))
    s.append(Paragraph("— Antragsgegnerinnen / Beklagte / Widerspruchsgegnerinnen —", S_CENTER))
    s.append(Spacer(1, 1.0*cm))
    sw = [
        ["Streitwert DE (LG Frankfurt 2-03 O 412/26)", "EUR 4.800.000,00"],
        ["EUIPO Widerspruch B 4 187 932", "EUR 80.000,00 (Verfahrenswert)"],
        ["BPatG 25 W (pat) 88/26", "EUR 50.000,00"],
        ["TTAB Opp. No. 91/289.412 (USPTO)", "USD 1.250.000,00 (Verfahrenswert)"],
        ["US District Court SDNY (in Vorbereitung)", "USD 8.700.000,00 + Treble Damages"],
        ["Gesamtstreitwert geschätzt (Equivalent EUR)", "≈ EUR 12.900.000,00"],
    ]
    t = Table(sw, colWidths=[10.5*cm, 5.5*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#888888")),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#f4ecd8")),
        ("BACKGROUND", (0,-1), (-1,-1), colors.HexColor("#e6d7b0")),
        ("FONTNAME", (0,-1), (-1,-1), "Times-Bold"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.8*cm))
    s.append(Paragraph("<b>Aktenzeichen-Verzeichnis (Stand 22.05.2026):</b>", S_NORMAL_LEFT))
    azlist = [
        "• LG Frankfurt a.M., 2-03 O 412/26 (Hauptsache + eV)",
        "• OLG Frankfurt a.M., 6 W 47/26 (Berufung Verfügung — anhängig)",
        "• EUIPO Alicante, Widerspruch B 4 187 932",
        "• EUIPO BoA, R 0 882/2025-5 (Beschwerde Riechmarke)",
        "• DPMA München, 30 2025 218 446 (Anmeldung „pure human craft“)",
        "• DPMA München, 30 2026 102 887 (Anmeldung Haptik Schal K°° Touch Royal)",
        "• DPMA München, 30 2026 102 888 (Anmeldung Haptik Flakon)",
        "• BPatG, 25 W (pat) 88/26",
        "• BGH, I ZB 14/26 (Rechtsbeschwerde Soundmarke — anhängig)",
        "• USPTO Serial No. 97/884.117 (KLÔTZZKÈTTÉ word mark, Class 25)",
        "• USPTO Serial No. 97/884.118 (K°° crown design)",
        "• USPTO Serial No. 97/884.119 (Position mark gold thread insignia)",
        "• USPTO Serial No. 97/884.120 (Trade dress hexagonal flacon)",
        "• USPTO Serial No. 97/884.121 (Haptic/tactile mark — silk twill weave)",
        "• TTAB Opposition No. 91/289.412 (vs. Klotzkettie LLC)",
        "• CBP e-Recordation TMK-26-08812",
        "• Tribunale di Firenze, R.G. 2026/4471 (Pitti-Uomo-Vollstreckung)",
    ]
    for line in azlist:
        s.append(Paragraph(line, S_SMALL))
    s.append(Spacer(1, 0.6*cm))
    s.append(HandNote(
        "angelegt 18.01.2026 — A.St.\nBd. I: Schriftsätze DE  /  Bd. II: EUIPO+DPMA\nBd. III: USPTO+TTAB+CBP  /  Bd. IV: Anlagen+Beweismittel\n*VORSICHT* Mandantin höchst sensibel — alles über mich!",
        font=FONT_HAND, size=14, color=colors.HexColor("#7a1f1f"), w=15*cm, angle=-1.2))
    return s

story += blatt_rubrum()
story.append(PageBreak())

# =====================================================================
# Aktenvermerk Erstkontakt
# =====================================================================
def blatt_aktenvermerk_erstkontakt():
    s = []
    s.append(Paragraph("<b>AKTENVERMERK</b>", S_CENTER))
    s.append(HLine())
    s.append(Spacer(1, 0.3*cm))
    meta = [
        ["Mandat:", "klôtzzkètté S.A. (Paris/Milano)"],
        ["Anlass:", "Erstkontakt — Telefonat 12.01.2026, 10:42 MEZ"],
        ["Verfasst von:", "Dr. Dr. A. Steinacker-von Tarsis (— ASt —)"],
        ["Akten-Nr.:", "WBF-2026-KK-0014 (intern) / Sch-Lich 26-0188"],
        ["Vertraulichkeit:", "STRENG VERTRAULICH — only-for-eyes-of"],
    ]
    t = Table(meta, colWidths=[3.6*cm, 12.4*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 10),
        ("FONTNAME", (0,0), (0,-1), "Times-Bold"),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("BOX", (0,0), (-1,-1), 0.3, colors.HexColor("#aaaaaa")),
        ("INNERGRID", (0,0), (-1,-1), 0.2, colors.HexColor("#cccccc")),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
        ("RIGHTPADDING", (0,0), (-1,-1), 5),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph(
        "Comtesse Béatrice de Klôtzzkètté-Visconti (im Folgenden: <i>die Mandantin</i>) "
        "kontaktierte die Unterzeichnete am 12.01.2026, 10:42 Uhr MEZ, telefonisch über das "
        "Direktwahlsekretariat (durchgestellt von Frau Hellweg). Die Mandantin schilderte zunächst "
        "in französischer Sprache, später teils auf Deutsch, teils Italienisch (sartoriale, lusso, "
        "<i>maison</i>, <i>atelier</i>) den nachstehenden Sachverhalt:", S_NORMAL))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph(
        "(1) Die Mandantin habe seit Spätherbst 2025 wiederholte Hinweise erhalten, dass in den "
        "Filialen der Brezelmann Discount KG (97980 Bad Mergentheim sowie Filialen in Crailsheim und "
        "Tauberbischofsheim) sowie über den Online-Marktplatz der Donauzon Marketplace GmbH Waren "
        "vertrieben würden, die in nahezu identischer Form das Krönchen-Monogramm „K°°“ der Mandantin "
        "trügen. Es handele sich um T-Shirts, Halstücher, Handtaschen-Imitate und (ganz besonders "
        "<i>infâme</i>) Parfumflakons mit asymmetrischem Stopfen. Die Mandantin habe von einem Bekannten "
        "(„Onkel Cosimo aus Florenz“) Fotos zugesandt bekommen.", S_NORMAL))
    s.append(Paragraph(
        "(2) Zudem sei am 09.01.2026 eine EU-Markenanmeldung der UAB „klotzkettie“ (Vilnius) für "
        "praktisch identische Klassen (3, 14, 18, 25) bekannt geworden. Die Anmeldung trage das "
        "Aktenzeichen EUTM 019 412 880. Auf Recherche der Unterzeichneten beim EUIPO sei eine "
        "Widerspruchsfrist bis 14.04.2026 zu beachten.", S_NORMAL))
    s.append(Paragraph(
        "(3) Die Mandantin wünsche <i>« une réponse foudroyante »</i> — also blitzartige Reaktion. "
        "Kostenrahmen sei zunächst <b>nicht limitiert</b>; die Mandantin verwies auf eine "
        "„Kriegskasse“ in Höhe von ca. EUR 2 Mio., die für Markenstreitigkeiten reserviert sei. "
        "Im Verlauf des Gesprächs erwähnte die Mandantin mehrfach « mes ancêtres » und die Gründung "
        "der Maison durch Antoine-Louis Klôtzzkètté im Jahre 1923.", S_NORMAL))
    s.append(Paragraph(
        "(4) Hinweis der Unterzeichneten auf Pitti-Uomo-Sichtungen (Florenz, Messe ab 11.03.2026, "
        "Halle 7, Stand B-44) — Mandantin sei bereits unterrichtet, eine Detektei in Frankfurt "
        "(Spürnase-Couture GmbH, Frau Kalt-Bandel) sei bereits mandatiert.", S_NORMAL))
    s.append(Paragraph(
        "(5) Mandatsannahme zugesagt. Mandatsvertrag und Vollmacht werden am 13.01.2026 per Kurier "
        "an Avenue du Faubourg Saint-Honoré 12 versandt. RVG bzw. Stundenvergütung "
        "(EUR 690/h Partnerin, EUR 420/h Associate) — Mandantin wählt Stundenvergütung.", S_NORMAL))
    s.append(Paragraph(
        "(6) Weiterer Hinweis: <i>parallel</i> sei das US-Vorgehen über die Tochter klôtzzkètté Inc. "
        "(Delaware) zu prüfen — Mandantin hat US-Kanzlei Whitman Brennan Forsythe LLP (NYC) bereits "
        "informiert; Erstkontakt zwischen den Häusern wird durch die Unterzeichnete koordiniert.",
        S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("München, 12.01.2026", S_NORMAL_LEFT))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("gez. ASt", S_NORMAL_LEFT))
    s.append(Spacer(1, 0.6*cm))
    s.append(HandNote(
        "N.B.: Mandantin hat während des Telefonats zweimal\nden Hörer hingeworfen (« quelle horreur! »),\neinmal sich entschuldigt (« pardonnez-moi, je suis émue »).\nBin gespannt — ASt",
        font=FONT_HAND, size=15, color=colors.HexColor("#1e3a6e"),
        w=14*cm, angle=-0.8))
    return s

story += blatt_aktenvermerk_erstkontakt()
story.append(PageBreak())

# =====================================================================
# Markenportfolio-Übersicht
# =====================================================================
def blatt_markenportfolio():
    s = []
    s.append(Paragraph("<b>MARKENPORTFOLIO klôtzzkètté S.A.</b>", S_H1))
    s.append(Paragraph("— Stand 22.05.2026, intern, vertraulich —", S_ITAL))
    s.append(HLine())
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph(
        "Die nachfolgende Übersicht erfasst sämtliche aktiven, angemeldeten und zurückgewiesenen "
        "Schutzrechte der Mandantin (DE/EU/INTL/US), die für das Verfahren ./. Brezelmann Discount KG "
        "und Donauzon Marketplace GmbH sowie das Parallelverfahren vor dem TTAB streitgegenständlich "
        "oder hilfsweise heranzuziehen sind. Sortierung nach Markentyp.", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))

    rows = [
        ["Nr.", "Typ", "Marke / Zeichen", "Amt / Reg.-Nr.", "Klassen", "Status"],
        ["1", "Wortmarke", "klôtzzkètté", "DPMA 30 2008 044 117 / EU 005 412 880",
         "3, 14, 18, 25, 35", "eingetragen"],
        ["2", "Wort-/Bildm.", "klôtzzkètté + K°°-Monogramm", "EU 010 988 411",
         "3, 14, 18, 25, 35", "eingetragen"],
        ["3", "Bildmarke", "Krönchen-Logo silber-emailliert", "DPMA 30 2014 077 312",
         "14, 25", "eingetragen"],
        ["4", "Positionsmarke", "Goldfaden-Krönchen Innensohle Pos. 1 cm", "EUIPO 015 887 442",
         "25", "eingetragen (str.)"],
        ["5", "Slogan-Marke", "LE LUXE EST UN DROIT NATUREL", "EU 018 412 776",
         "25, 35", "eingetragen"],
        ["6", "Soundmarke", "8-Sek. Jingle (Sektstiel/Eis/Stimme)", "EUIPO 018 502 311",
         "3, 25, 35, 41", "eingetragen"],
        ["7", "3D-Formmarke", "Flakon K°° Hexagonal asymm. Stopfen", "EU 008 776 015",
         "3", "eingetragen"],
        ["8", "Zertifik.-/Garantiem.", "klôtzzkètté pure human craft", "DPMA 30 2025 218 446",
         "9, 25, 35, 42", "in Anmeldung"],
        ["9", "Duftmarke", "Iris pallida / weiße Birne / Wildleder", "EUIPO (zurückgewiesen)",
         "3", "zurückgew. — Beschw."],
        ["10", "Haptikmarke", "Schal K°° Touch Royal (3 Rauten Webstr.)", "DPMA 30 2026 102 887",
         "24, 25", "in Anmeldung"],
        ["11", "Haptikmarke", "Flakonoberfläche Bergkristall-Reliefs", "DPMA 30 2026 102 888",
         "3, 21", "in Anmeldung"],
        ["12", "Haptic Mark US", "Silk twill weave 18 momme", "USPTO 97/884.121",
         "24, 25 (US Int.Cl.)", "filed — pending exam."],
        ["13", "US Word Mark", "KLÔTZZKÈTTÉ", "USPTO 97/884.117",
         "25 (US)", "TEAS Plus, ITU"],
        ["14", "US Word Mark", "KLÔTZZKÈTTÉ", "USPTO 97/884.117a",
         "14 (US)", "TEAS Plus, ITU"],
        ["15", "US Design Mark", "K°° crown logo", "USPTO 97/884.118",
         "25 (US)", "filed"],
        ["16", "US Position Mark", "Gold thread insignia insole", "USPTO 97/884.119",
         "25 (US)", "filed (Louboutin-style)"],
        ["17", "US Trade Dress", "Hexagonal flacon K°° pour Femme", "USPTO 97/884.120",
         "3 (US)", "filed (Wal-Mart v. Samara)"],
        ["18", "IR-Designation (MM2)", "klôtzzkètté Madrid Protocol", "WIPO Int. Reg. 1.488.220",
         "3, 14, 18, 25, 35", "designated: US, CH, JP, CN, KR, AU, CA"],
    ]
    t = Table(rows, colWidths=[0.8*cm, 2.1*cm, 4.6*cm, 4.0*cm, 2.6*cm, 2.4*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 7.6),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1c2e4a")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888888")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f5f1e6")]),
        ("LEFTPADDING", (0,0), (-1,-1), 3),
        ("RIGHTPADDING", (0,0), (-1,-1), 3),
        ("TOPPADDING", (0,0), (-1,-1), 2.5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2.5),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<i>Anmerkung:</i> Die Positionsmarke EUIPO 015 887 442 wurde durch die HUUMAN-Footwear B.V. "
        "(Eindhoven) am 04.11.2025 mit einem Löschungsantrag wegen fehlender Unterscheidungskraft "
        "(Art. 7 Abs. 1 lit. b UMV) angegriffen; das Verfahren ist unter EUIPO Az. C 058 412 anhängig. "
        "Die Mandantin hat insoweit den Schriftsatz vom 02.02.2026 vorgelegt; siehe Blatt 47 dieser "
        "Akte sowie ergänzend Blatt 91 (Replik).", S_SMALL))
    s.append(Spacer(1, 0.3*cm))
    s.append(HandNote(
        "WICHTIG: Marke Nr. 6 (Soundmarke) ist die Lieblingsmarke der Comtesse —\nbeim Auftakt vor der Großen Kammer 2025 hat sie den Jingle\nvom iPhone abspielen lassen, halber Saal hat applaudiert.\n→ unbedingt im Plädoyer einbauen!  — ASt",
        font=FONT_HAND, size=14, color=colors.HexColor("#7a1f1f"), w=15*cm, angle=0.6))
    return s

story += blatt_markenportfolio()
story.append(PageBreak())

print("[part01] done")
