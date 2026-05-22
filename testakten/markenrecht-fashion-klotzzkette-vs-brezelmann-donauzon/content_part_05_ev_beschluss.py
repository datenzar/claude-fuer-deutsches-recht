# Part 05: einstweilige Verfügung Beschluss LG Frankfurt
def blatt_ev_beschluss():
    s = []
    s.append(Paragraph("<b>LANDGERICHT FRANKFURT AM MAIN</b>", S_CENTER))
    s.append(Paragraph("Kammer für Markensachen — 2. Zivilkammer", S_CENTER))
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("<b>Aktenzeichen: 2-03 O 412/26</b>", S_CENTER))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("<b>B E S C H L U S S</b>", S_CENTER))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("In dem einstweiligen Verfügungsverfahren", S_NORMAL))
    s.append(Paragraph(
        "<b>klôtzzkètté S.A.</b>, 12 rue du Faubourg Saint-Honoré, 75008 Paris, "
        "Antragstellerin,", S_NORMAL))
    s.append(Paragraph("Verfahrensbevollmächtigte: RAe Steinacker Lichtenberg &amp; Partners IP, München", S_SMALL))
    s.append(Paragraph("g e g e n", S_CENTER))
    s.append(Paragraph(
        "1. <b>Brezelmann Discount KG</b>, Wurstgasse 4, 97980 Bad Mergentheim;<br/>"
        "2. <b>Donauzon Marketplace GmbH</b>, Niederlassung Deutschland: Erdbeerallee 88, "
        "80807 München, — Antragsgegnerinnen —", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "wegen Unterlassung der Verletzung mehrerer Marken (EU 005 412 880; "
        "EU 010 988 411; DPMA 30 2014 077 312; EUIPO 015 887 442; EU 008 776 015; "
        "EUIPO 018 502 311),", S_NORMAL))
    s.append(Paragraph(
        "hat das Landgericht Frankfurt am Main — Kammer für Markensachen — am 11.03.2026 "
        "durch den Vorsitzenden Richter am Landgericht <b>Dr. Hoffacker-Wendel</b> sowie die "
        "Richterin am Landgericht <b>Dr. Lindemann</b> und den Richter am Landgericht "
        "<b>Karwacki</b> ohne mündliche Verhandlung beschlossen:", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<b>I.</b> Den Antragsgegnerinnen wird bei Meidung eines vom Gericht für jeden Fall "
        "der Zuwiderhandlung festzusetzenden Ordnungsgeldes bis zu <b>EUR 250.000,00</b> "
        "— ersatzweise Ordnungshaft —, oder Ordnungshaft bis zu sechs Monaten, im Falle "
        "wiederholter Zuwiderhandlung bis zu insgesamt zwei Jahren, zu vollziehen am jeweiligen "
        "Komplementär bzw. Geschäftsführer, untersagt, im geschäftlichen Verkehr im Gebiet der "
        "Bundesrepublik Deutschland Bekleidungsstücke, Lederwaren, Schuhe und Parfümerieartikel "
        "anzubieten, zu vertreiben, einzuführen, auszuführen, zu bewerben oder bewerben zu "
        "lassen, die mit dem Zeichen „K°°“, dem Schriftzug „klôtzzkètté“ oder einem damit "
        "verwechslungsfähigen Zeichen versehen sind und/oder im Falle von Parfumflakons die "
        "hexagonale Form mit asymmetrischem Stopfen gemäß 3D-Formmarke EU 008 776 015 "
        "aufweisen.", S_NORMAL))
    s.append(Paragraph(
        "<b>II.</b> Den Antragsgegnerinnen wird aufgegeben, die in ihrem Besitz oder Eigentum "
        "befindlichen, unter Ziff. I bezeichneten Waren innerhalb von 48 Stunden ab Zustellung "
        "an den hiermit zum Sequester bestellten <b>Rechtsanwalt Dr. Lorenzo Maletti</b>, "
        "Studio Legale Maletti &amp; Pieri, Via Manzoni 14, 20121 Milano, sowie hilfsweise an "
        "den <b>Obergerichtsvollzieher Niccolò Sartori</b>, beigeordnet dem Tribunale di "
        "Firenze, herauszugeben.", S_NORMAL))
    s.append(Paragraph(
        "<b>III.</b> Die Antragsgegnerinnen tragen gesamtschuldnerisch die Kosten des Verfahrens. "
        "Der Verfahrenswert wird auf <b>EUR 1.200.000,00</b> festgesetzt.", S_NORMAL))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("<b>Gründe</b>", S_H2))
    s.append(Paragraph(
        "Der Antrag auf Erlass einer einstweiligen Verfügung ist zulässig und begründet. Die "
        "örtliche und sachliche Zuständigkeit der erkennenden Kammer folgt aus §§ 32 ZPO, 140, "
        "141 MarkenG i.V.m. der Konzentrationsverordnung Hessen. Die Antragstellerin hat sowohl "
        "Verfügungsanspruch als auch Verfügungsgrund glaubhaft gemacht; auf die Antragsschrift "
        "vom 11.03.2026 wird in vollem Umfang Bezug genommen. Eine mündliche Verhandlung war "
        "wegen der besonderen Dringlichkeit im Hinblick auf den am 11.03.2026 beginnenden "
        "Messetermin Pitti Uomo (Florenz) nicht durchzuführen, § 937 Abs. 2 ZPO.", S_NORMAL))
    s.append(Paragraph(
        "<b>Rechtsbehelfsbelehrung:</b> Gegen diesen Beschluss ist Widerspruch (§ 924 ZPO) "
        "statthaft. Über den Widerspruch entscheidet das Gericht durch Endurteil aufgrund "
        "mündlicher Verhandlung.", S_NORMAL))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Frankfurt am Main, 11.03.2026", S_NORMAL))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("gez. Dr. Hoffacker-Wendel", S_NORMAL_LEFT))
    s.append(Paragraph("Vorsitzender Richter am Landgericht", S_SMALL))
    s.append(Spacer(1, 0.3*cm))
    s.append(StampBox("Ausgefertigt\n11.03.2026\nLG Frankfurt a.M.\nUrkundsbeamtin\n— Schramm —",
                       angle=-6, color=colors.HexColor("#225522"), w=5.4*cm, h=2.6*cm))
    return s

story += blatt_ev_beschluss()
story.append(PageBreak())

# =====================================================================
# Schutzschriftenkontrolle (Aktenvermerk)
# =====================================================================
def blatt_schutzschriften():
    s = []
    s.append(Paragraph("<b>AKTENVERMERK · Schutzschriftenkontrolle</b>", S_CENTER))
    s.append(HLine())
    s.append(Paragraph("Datum: 09.03.2026 · 14:22 Uhr · Bearb.: MvB", S_RIGHT))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Recherche im <b>Zentralen Schutzschriftenregister Hessen (ZSSR-Hessen)</b> sowie im "
        "<b>Beck-Online Schutzschriftenregister</b>:", S_NORMAL))
    rows = [
        ["Register", "Suchstring", "Treffer", "Relevanz"],
        ["ZSSR Hessen", "klötzkette OR klotzkette OR brezelmann", "0", "—"],
        ["ZSSR Hessen", "K°° OR krönchen", "2", "irrelevant (Hotelkette)"],
        ["Beck-Online SSR", "klotzkette", "0", "—"],
        ["Beck-Online SSR", "donauzon AND marken", "1", "irrelevant (Buchhandel)"],
        ["Beck-Online SSR", "brezelmann", "0", "—"],
    ]
    t = Table(rows, colWidths=[4.5*cm, 6.5*cm, 1.8*cm, 4.0*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1c2e4a")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#888888")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f5f1e6")]),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<b>Ergebnis:</b> Keine relevante Schutzschrift hinterlegt. Antrag auf Erlass einer "
        "einstweiligen Verfügung ohne mündliche Verhandlung gem. § 937 Abs. 2 ZPO kann gestellt "
        "werden.", S_NORMAL))
    s.append(Paragraph(
        "<b>Ergänzend</b> wurde am 10.03.2026, 08:15 Uhr, eine erneute Abfrage durchgeführt — "
        "weiterhin keine relevanten Treffer.", S_NORMAL))
    s.append(Spacer(1, 0.5*cm))
    s.append(Paragraph("gez. MvB", S_NORMAL_LEFT))
    s.append(Spacer(1, 0.5*cm))
    s.append(HandNote(
        "ASt: Bitte gegenzeichnen — Antragsschrift kann raus.\nMvB",
        font=FONT_HAND, size=15, color=colors.HexColor("#345"), w=13*cm, angle=0.4))
    return s

story += blatt_schutzschriften()
story.append(PageBreak())

print("[part05] done")
