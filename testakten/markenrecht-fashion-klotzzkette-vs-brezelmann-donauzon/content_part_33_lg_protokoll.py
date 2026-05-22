# Part 33: LG Frankfurt Verhandlungsprotokoll 11.06.2026 + Urteil
def blatt_lg_protokoll():
    s = []
    s.append(Paragraph("<b>LANDGERICHT FRANKFURT AM MAIN</b>", S_CENTER))
    s.append(Paragraph("— 3. Zivilkammer — Kammer für Markensachen", S_CENTER))
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>PROTOKOLL DER ÖFFENTLICHEN SITZUNG</b>", S_CENTER))
    s.append(Spacer(1, 0.2*cm))
    rows = [
        ["Datum/Uhrzeit:", "Donnerstag, den 11. Juni 2026, 10:00 – 12:48 Uhr"],
        ["Ort:", "Sitzungssaal 3.07 · Gerichtsstraße 2 · 60313 Frankfurt am Main"],
        ["Az.:", "2-03 O 412/26"],
        ["Vorsitzende:", "VRiLG Dr. Eleonora Wendt-Pasterczyk"],
        ["Beisitzende Richter:", "RiLG Dr. F. Holzapfel-Schäffer, RiLG Dr. A. Knoblauch-Sturm"],
        ["Protokoll:", "Justizfachangestellte K. Brzezinski"],
    ]
    t = Table(rows, colWidths=[3.5*cm, 13*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("FONTNAME", (0,0), (0,-1), "Times-Bold"),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888")),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("In der Markenstreitsache", S_NORMAL))
    s.append(Paragraph(
        "<b>klôtzzkètté S.A.</b>, Paris — Klägerin —<br/>"
        "Verfahrensbevollmächtigte: Steinacker Lichtenberg &amp; Partners IP Boutique, "
        "München; erschienen: RAe Dr. Dr. Steinacker-von Tarsis und Freiherr v. "
        "Brenkenhoff", S_SMALL))
    s.append(Paragraph("g e g e n", S_CENTER))
    s.append(Paragraph(
        "<b>Brezelmann Discount KG</b>, Bad Mergentheim — Beklagte zu 1 —<br/>"
        "Verfahrensbevollmächtigt: <i>nicht erschienen, kein Bevollmächtigter im Register</i>",
        S_SMALL))
    s.append(Paragraph(
        "<b>Donauzon Marketplace GmbH</b>, Luxembourg/München — Beklagte zu 2 —<br/>"
        "Verfahrensbevollmächtigt: Lawclock Frankfurt LLP; erschienen: RAin Dr. F. "
        "Saalfeld-Wegener, RA Dr. M. Hagenstein", S_SMALL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>Verhandlungsverlauf</b>", S_H3))
    s.append(Paragraph(
        "10:00 — Die Vorsitzende eröffnet die Sitzung. Erscheinen werden festgestellt. "
        "Die Beklagte zu 1 (Brezelmann Discount KG) ist trotz ordnungsgemäßer Ladung "
        "(Empfangsbestätigung vom 04.05.2026) nicht erschienen. Auf entsprechenden Antrag "
        "der Klägerin wird festgestellt, dass die Beklagte zu 1 säumig ist; ein "
        "Versäumnis-Teilurteil im Sinne der Sitzung wird in Aussicht gestellt.", S_NORMAL))
    s.append(Paragraph(
        "10:08 — Die Vorsitzende erörtert die Sach- und Rechtslage. Sie weist auf die "
        "EuGH-Rechtsprechung Coty/Amazon (C-567/18) hin und fragt die Beklagte zu 2 nach "
        "deren Compliance-Architektur.", S_NORMAL))
    s.append(Paragraph(
        "10:14 — RAin Dr. Saalfeld-Wegener (für Donauzon) erläutert das DSA-konforme "
        "Notice-and-Action-Verfahren und überreicht ein »Trusted Flagger Onboarding "
        "Packet« (Anlage B 2-7, 28 Seiten). Die Vorsitzende erkennt die rechtliche "
        "Komplexität an, weist jedoch darauf hin, dass die <i>materielle</i> "
        "Markenverletzungshaftung von der prozessualen DSA-Compliance zu trennen sei.",
        S_NORMAL))
    s.append(Paragraph(
        "10:32 — Dr. Steinacker-von Tarsis (für Klägerin) verweist auf den "
        "Spürnase-Couture-Detektivbericht II (Anlage K 44) und unterstreicht, dass "
        "Donauzon trotz der eV vom 04.03.2026 noch am 02.06.2026 (also 90 Tage später) "
        "19 verletzende Listings online hatte.", S_NORMAL))
    s.append(Paragraph(
        "10:48 — Die Vorsitzende erklärt: »Das Gericht ist geneigt, eine "
        "Notice-and-Stay-Down-Pflicht im Tenor aufzunehmen, soweit der Antrag dies "
        "stützt. Die Frage des Auskunftsanspruchs (Stufe 1) erscheint dem Senat hingegen "
        "wegen der Donauzon-DSA-Architektur differenziert zu betrachten.«", S_NORMAL))
    s.append(Paragraph(
        "11:04 — Vernehmung des sachverständigen Zeugen Prof. Dr. Hieronymus Steinpfeil. "
        "Der Zeuge wird belehrt nach §§ 395 ff. ZPO. Aussage: Im wesentlichen wiederholt "
        "und vertieft der Zeuge sein schriftliches Gutachten vom 14.05.2026. Die "
        "Verwechslungsgefahr zwischen KLÔTZZKÈTTÉ und klotzkettiee sei »sehr hoch« "
        "(Probandinnen Top-Box 44 %)«. Der Zeuge schließt: »Wer das nicht erkennt, "
        "hat keine Augen für Strichlein.« Allgemeine Heiterkeit auf der Klägerseite.",
        S_NORMAL))
    s.append(Paragraph(
        "11:42 — Die Beklagte zu 2 stellt einen <b>Vergleichsvorschlag</b> nach § 278 "
        "Abs. 6 ZPO mit folgendem wesentlichem Inhalt:", S_NORMAL))
    items = [
        "(a) Notice-and-Stay-Down-Verpflichtung für alle Listings mit den Suchworten "
        "klotzkette*, klôtzz*, K°°, gold-thread-position-mark;",
        "(b) Trusted-Flagger-Status nach Art. 22 DSA für klôtzzkètté S.A. mit "
        "48-Stunden-Reaktionsgarantie;",
        "(c) Pauschale Aufwandsentschädigung in Höhe von <b>EUR 875.000,00</b>;",
        "(d) Kostenaufteilung 80/20 zu Lasten Donauzon;",
        "(e) <i>Kein</i> Geheimhaltungsschutz; Veröffentlichung erlaubt;",
        "(f) Verzicht auf Berufung gegen die so resultierende Beschlussfassung.",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    s.append(Paragraph(
        "12:00 — Die Klägerin erbittet eine Beratungspause von 30 Minuten. Die Vorsitzende "
        "unterbricht die Verhandlung.", S_NORMAL))
    return s

story += blatt_lg_protokoll()
story.append(PageBreak())

def blatt_lg_protokoll_2():
    s = []
    s.append(Paragraph(
        "12:30 — Wiederaufnahme. Dr. Steinacker-von Tarsis erklärt nach Rücksprache mit "
        "der Mandantin (telefonisch erreicht in Cannes; Comtesse de K-V): <b>Annahme "
        "des Vergleichs unter folgenden Modifikationen:</b>", S_NORMAL))
    items = [
        "(i) Aufwandsentschädigung: <b>EUR 1.250.000,00</b> (nicht 875.000);",
        "(ii) Die Notice-and-Stay-Down-Verpflichtung erstreckt sich ausdrücklich auch "
        "auf <i>klotzkett*</i> als Wildcard-Match;",
        "(iii) Die in Annex B 2-7 beschriebene Trusted-Flagger-Architektur wird durch "
        "die Klägerin auditiert; Audit-Kosten trägt Donauzon;",
        "(iv) Zusätzliche Verpflichtung Donauzons, die Verkaufs- und Transaktionsdaten "
        "der UAB klotzkettie für die Periode 2025-Q1 bis 2026-Q2 ohne weiteres "
        "Verfahren herauszugeben (modifizierter Auskunftsanspruch nach § 19 MarkenG);",
        "(v) Verzicht auf die Berufung — angenommen.",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    s.append(Paragraph(
        "12:38 — RAin Dr. Saalfeld-Wegener teilt nach kurzer Beratung mit der "
        "Donauzon-Inhouse-Abteilung (per Telefon) mit, dass die Modifikationen (i), "
        "(ii) und (iii) akzeptiert werden, die Modifikation (iv) jedoch <b>abgelehnt</b> "
        "werde, weil sie die DSA-Privilegien überdehne und ein Präzedenz schaffe.",
        S_NORMAL))
    s.append(Paragraph(
        "12:44 — Die Vorsitzende stellt fest, dass eine vollständige Einigung im "
        "Termin nicht zustande kommt. Sie ordnet an, dass die Sache in das schriftliche "
        "Verfahren übergeleitet wird (§ 128 Abs. 2 ZPO) und kündigt eine "
        "Urteilsverkündung für den <b>27. Juli 2026, 11:00 Uhr</b> an.", S_NORMAL))
    s.append(Paragraph(
        "12:48 — Die Vorsitzende schließt die Sitzung.", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("vorgelesen und genehmigt", S_NORMAL))
    s.append(Paragraph("Brzezinski, JFA · Dr. Wendt-Pasterczyk, VRiLG", S_NORMAL))
    s.append(Spacer(1, 0.4*cm))
    s.append(HLine())
    s.append(Paragraph("<b>HANDSCHRIFTLICHER VERMERK AUF DEM PROTOKOLL-DECKEL</b>", S_H3))
    s.append(HandNote(
        "EUR 1.25 Mio + Audit + Wildcard waren auf dem Tisch.\n"
        "Donauzon will Auskunft nicht — verständlich,\n"
        "wir hätten ihre Marketplace-Konkurrenz ausspioniert.\n"
        "→ schriftliches Urteil 27.07. wird gemischt:\n"
        "   Tenor 1 + 2 unstreitig stattgegeben;\n"
        "   Tenor 3 (Auskunft) wahrscheinlich abgewiesen.\n"
        "→ daher Berufung 6 W 47/26. Genau wie geplant.\n"
        "Comtesse zufrieden trotz »nur 1,25 Mio«:\n"
        "Pelletier hat hier öffentlich gezogen.\n"
        "— Brenkenhoff, 11.06.2026, 14:22",
        font=FONT_HAND, size=14, angle=-0.3, w=15.5*cm))
    return s

story += blatt_lg_protokoll_2()
story.append(PageBreak())

def blatt_versaeumnis_teilurteil():
    s = []
    s.append(Paragraph("<b>LANDGERICHT FRANKFURT AM MAIN — VERSÄUMNIS-TEILURTEIL</b>",
                        S_CENTER))
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.2*cm))
    rows = [
        ["Az.:", "2-03 O 412/26"],
        ["Verkündet am:", "11. Juni 2026"],
        ["Klägerin:", "klôtzzkètté S.A., Paris"],
        ["Beklagte zu 1 (säumig):", "Brezelmann Discount KG, Bad Mergentheim"],
        ["Vorsitzende:", "VRiLG Dr. Wendt-Pasterczyk"],
    ]
    t = Table(rows, colWidths=[4*cm, 12.5*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("FONTNAME", (0,0), (0,-1), "Times-Bold"),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888")),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>Im Namen des Volkes</b>", S_CENTER))
    s.append(Paragraph(
        "Auf Antrag der Klägerin ergeht im schriftlichen Verfahren wegen Säumnis der "
        "Beklagten zu 1 folgendes Versäumnis-Teilurteil:", S_NORMAL))
    s.append(Paragraph("<b>Tenor</b>", S_H3))
    s.append(Paragraph(
        "<b>I.</b> Die Beklagte zu 1 wird verurteilt, es bei Meidung eines für jeden Fall "
        "der Zuwiderhandlung festzusetzenden Ordnungsgeldes bis zu EUR 250.000,00, "
        "ersatzweise Ordnungshaft, oder Ordnungshaft bis zu sechs Monaten — die "
        "Ordnungshaft zu vollziehen am Komplementär Egon Brezelmann persönlich — zu "
        "unterlassen, im geschäftlichen Verkehr in der Bundesrepublik Deutschland", S_NORMAL))
    s.append(Paragraph(
        "Bekleidung, Lederwaren, Accessoires und Parfümerieartikel unter der Bezeichnung "
        "»klotzkettiee« oder mit Bildelementen, die das Kronen-Logo der Klägerin "
        "wiedergeben, anzubieten, in den Verkehr zu bringen, zu bewerben, einzuführen, "
        "auszuführen oder zu diesen Zwecken zu besitzen.", S_QUOTE))
    s.append(Paragraph(
        "<b>II.</b> Die Beklagte zu 1 wird verurteilt, der Klägerin <i>Auskunft zu "
        "erteilen</i> über Herkunft, Vertriebsweg, Mengen und erzielten Preise der "
        "in Ziffer I beschriebenen rechtsverletzenden Waren seit dem 01.01.2024 sowie "
        "Rechnung zu legen über die hierdurch erzielten Umsätze und Gewinne.", S_NORMAL))
    s.append(Paragraph(
        "<b>III.</b> Es wird festgestellt, dass die Beklagte zu 1 verpflichtet ist, "
        "der Klägerin allen weiteren Schaden zu ersetzen, der ihr aus den in Ziffer I "
        "bezeichneten Handlungen entstanden ist und noch entstehen wird.", S_NORMAL))
    s.append(Paragraph(
        "<b>IV.</b> Die Beklagte zu 1 trägt die Kosten dieses Versäumnisteilurteils.",
        S_NORMAL))
    s.append(Paragraph(
        "<b>V.</b> Das Urteil ist gegen Sicherheitsleistung in Höhe von 110 % des "
        "jeweils zu vollstreckenden Betrages vorläufig vollstreckbar.", S_NORMAL))
    s.append(Paragraph("<b>Rechtsbehelfsbelehrung</b>", S_H3))
    s.append(Paragraph(
        "Gegen dieses Versäumnisurteil ist innerhalb von zwei Wochen nach Zustellung "
        "Einspruch beim Landgericht Frankfurt am Main einzulegen (§ 339 ZPO). Der "
        "Einspruch ist schriftlich oder zur Niederschrift der Geschäftsstelle einzureichen.",
        S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Dr. Wendt-Pasterczyk · Dr. Holzapfel-Schäffer · Dr. Knoblauch-Sturm",
                        S_CENTER))
    s.append(Spacer(1, 0.2*cm))
    s.append(StampBox("LG FRANKFURT\nVERKÜNDET\n11.06.2026", angle=-7, w=4.8*cm, h=2.0*cm))
    s.append(Spacer(1, 0.3*cm))
    s.append(HandNote(
        "Versäumnis-Teilurteil gegen Brezelmann.\n"
        "Auskunfts-Tenor ist GENAU das, was wir in der\n"
        "Hauptverhandlung gegen Donauzon vermissen.\n"
        "→ In der OLG-Berufung argumentieren wir mit\n"
        "diesem Brezelmann-Urteil per analogiam.\n"
        "— Steinacker, 12.06.",
        font=FONT_HAND2, size=13.5, angle=0.4, w=15*cm))
    return s

story += blatt_versaeumnis_teilurteil()
story.append(PageBreak())

print("[part33] done")
