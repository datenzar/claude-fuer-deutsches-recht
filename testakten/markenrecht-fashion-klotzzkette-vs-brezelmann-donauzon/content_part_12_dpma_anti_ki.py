# Part 12: DPMA Anti-KI-Authentizitätsmarke Anmeldung + Monitur Klasse 9
def blatt_dpma_anti_ki_anmeldung():
    s = []
    s.append(Briefkopf(
        KANZLEI_ADDR,
        "Deutsches Patent- und Markenamt\nMarkenstelle für Klassen\nZweibrückenstraße 12\n80331 München",
        "07.10.2025", "Sch-Lich 25-1488 / DPMA 30 2025 218 446"))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<b>Anmeldung einer deutschen Garantie- bzw. Zertifizierungsmarke</b><br/>"
        "— „klôtzzkètté pure human craft“ —", S_H3))
    s.append(Paragraph(
        "Sehr geehrte Damen und Herren,", S_NORMAL))
    s.append(Paragraph(
        "namens und in Vollmacht der Anmelderin — <b>klôtzzkètté S.A.</b>, 12 rue du Faubourg "
        "Saint-Honoré, 75008 Paris (Frankreich) — beantragen wir hiermit die Eintragung "
        "folgender Marke:", S_NORMAL))
    rows = [
        ["Markenform:", "Wort-/Bildmarke kombiniert mit Zertifikatsstempel-Optik"],
        ["Wortbestandteil:", "klôtzzkètté pure human craft"],
        ["Bildbestandteil:",
         "Stilisierter Zertifikatsstempel mit Krönchen-Monogramm K°°, "
         "umgeben von der lateinischen Umschrift „MANU FACTA · NON MACHINA NATA“ "
         "(handgemacht, nicht maschinell geboren)"],
        ["Klassen (Nizza 12. Ed.):", "9, 25, 35, 42"],
        ["Schutzform:", "Garantiemarke gem. § 106a MarkenG (alt: § 97 MarkenG)"],
        ["Markenfähigkeit:", "begründet (Zertifizierungsfunktion: Identität als manuelle Fertigung)"],
        ["Anmelderin/Inhaberin:", "klôtzzkètté S.A. (vertretungsberechtigt: Comtesse B. de Klôtzzkètté-V.)"],
        ["Vertreter beim DPMA:", "Steinacker Lichtenberg & Partners IP — DPMA-Reg.-Nr. 78229"],
    ]
    t = Table(rows, colWidths=[4.2*cm, 12.2*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("FONTNAME", (0,0), (0,-1), "Times-Bold"),
        ("BOX", (0,0), (-1,-1), 0.3, colors.HexColor("#777777")),
        ("INNERGRID", (0,0), (-1,-1), 0.15, colors.HexColor("#bbbbbb")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>I. Gegenstand und Funktion der Garantiemarke</b>", S_H3))
    s.append(Paragraph(
        "Die Anmelderin möchte mit der vorliegenden Garantiemarke ihren Kunden, dem Handel und "
        "der breiteren Öffentlichkeit gegenüber bescheinigen, dass die unter der Marke "
        "gekennzeichneten Produkte ausschließlich durch <b>menschliche Hand</b> — unter Ausschluss "
        "von Künstlicher Intelligenz (KI) und insbesondere generativer Bild-, Stoff- und "
        "Musterautomaten — entworfen und gefertigt wurden. Hintergrund ist die starke Verbreitung "
        "von KI-generierten Designs (insb. Stable-Diffusion-XL, MidJourney v7.2, Imagen-4), "
        "die das Premium-Image traditioneller Modehäuser bedrohen.", S_NORMAL))
    s.append(Paragraph("<b>II. Markensatzung (§ 106d MarkenG)</b>", S_H3))
    s.append(Paragraph(
        "Die <b>Markensatzung</b> ist als Anlage K-GAR-1 beigefügt; sie enthält in §§ 1-12 "
        "Bestimmungen über die Voraussetzungen der Lizenzvergabe (Verzicht auf KI-Entwurf), "
        "die Auditierung durch unabhängige Zertifizierer (Hersh-Wagner Inspecta GmbH, Hannover) "
        "sowie die Sanktionierung bei Missbrauch (Lizenzentzug, Vertragsstrafe bis EUR 250.000 "
        "je Verstoß).", S_NORMAL))
    s.append(Paragraph("<b>III. Hinweis auf parallele EU-Anmeldung</b>", S_H3))
    s.append(Paragraph(
        "Eine parallele Anmeldung als Unionsgewährleistungsmarke ist beim EUIPO erfolgt "
        "(EUTM 019 488 220, Anmeldetag 03.10.2025). Im Falle eines positiven Abschlusses dort "
        "bitten wir vorab um Berücksichtigung im Rahmen des DPMA-Prüfungsverfahrens.", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("München, 07.10.2025", S_NORMAL_LEFT))
    s.append(Paragraph("gez. Dr. Dr. A. Steinacker-von Tarsis", S_NORMAL_LEFT))
    s.append(Paragraph("DPMA-Rep.-Nr. 78229", S_SMALL))
    return s

story += blatt_dpma_anti_ki_anmeldung()
story.append(PageBreak())

# DPMA Monitur Klasse 9
def blatt_dpma_monitur():
    s = []
    s.append(Paragraph("<b>DEUTSCHES PATENT- UND MARKENAMT</b>", S_CENTER))
    s.append(Paragraph("Markenstelle für Klassen, Markenabt. 3.4", S_CENTER))
    s.append(HLine())
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<b>Az. 30 2025 218 446</b> · Anmeldung „klôtzzkètté pure human craft“", S_RIGHT))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph(
        "An: Steinacker Lichtenberg &amp; Partners IP Boutique, Maximiliansplatz 19, 80333 München",
        S_NORMAL))
    s.append(Paragraph("<b>BEANSTANDUNGSSCHREIBEN (Monitur)</b>", S_H2))
    s.append(Paragraph(
        "Im Rahmen der Vorprüfung gem. § 36 MarkenG ergeben sich Beanstandungen hinsichtlich der "
        "beanspruchten Klasse 9 sowie hilfsweise hinsichtlich des absoluten Schutzhindernisses "
        "der mangelnden Unterscheidungskraft (§ 8 Abs. 2 Nr. 1 MarkenG).", S_NORMAL))
    s.append(Paragraph("<b>I. Klasse 9</b>", S_H3))
    s.append(Paragraph(
        "Die beanspruchten Waren der Klasse 9 — namentlich „<i>Software zur Authentifizierung "
        "manuell gefertigter Produkte; Apparate zur Markenechtheits-Prüfung; computerlesbare "
        "Datenträger mit Authentizitätssignaturen</i>“ — sind nicht hinreichend konkretisiert. "
        "Wir bitten um Klarstellung gem. Nizza-Klassifikation 12. Edition, Stand 01.01.2025.",
        S_NORMAL))
    s.append(Paragraph("<b>II. Unterscheidungskraft (§ 8 Abs. 2 Nr. 1 MarkenG)</b>", S_H3))
    s.append(Paragraph(
        "Der Wortbestandteil „pure human craft“ besteht aus rein beschreibenden Begriffen der "
        "englischen Sprache und wird vom inländischen Verkehr ohne weiteres als Sachhinweis auf "
        "die Herstellungsart („reine menschliche Handwerkskunst“) verstanden. Die Verbindung "
        "mit dem Bestandteil „klôtzzkètté“ verleiht zwar dem Gesamtzeichen Unterscheidungskraft; "
        "an einer originären Schutzfähigkeit des Wortteils „pure human craft“ allein bestehen "
        "indes Zweifel. Hinsichtlich der reinen Wortmarke wird angeregt, von einer separaten "
        "Anmeldung des Wortteils Abstand zu nehmen.", S_NORMAL))
    s.append(Paragraph("<b>III. Frist</b>", S_H3))
    s.append(Paragraph(
        "Wir bitten um Stellungnahme binnen <b>vier Monaten</b> nach Zustellung dieses "
        "Beanstandungsschreibens. Bei fruchtlosem Fristablauf droht teilweise Zurückweisung "
        "gem. § 36 Abs. 3 MarkenG.", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("München, 18.02.2026", S_NORMAL_LEFT))
    s.append(Paragraph("gez. Frau Markenprüferin Pelzig", S_NORMAL_LEFT))
    s.append(Paragraph("DPMA Markenabt. 3.4, Sachgebiet Garantiemarken", S_SMALL))
    s.append(Spacer(1, 0.3*cm))
    s.append(StampBox("eingeg.\n25.02.2026\nWiedervorl.\n14.04.\n— hk —",
                       angle=-7, color=colors.HexColor("#225522"), w=4.8*cm, h=2.4*cm))
    s.append(Spacer(1, 0.4*cm))
    s.append(HandNote(
        "Klasse 9 nachschärfen (Software-Hash-Authentifizierung — Blockchain-NFT-Ansatz)\nWortteil-Hinweis akzeptieren — kein Trennantrag.\n→ Frist 14.06.2026, gut beherrschbar.\nMvB übernimmt — ASt",
        font=FONT_HAND, size=13, color=colors.HexColor("#1e3a6e"), w=15*cm, angle=0.3))
    return s

story += blatt_dpma_monitur()
story.append(PageBreak())

# Antwort der Kanzlei auf Monitur
def blatt_dpma_antwort_monitur():
    s = []
    s.append(Briefkopf(
        KANZLEI_ADDR,
        "Deutsches Patent- und Markenamt\nMarkenabt. 3.4 z.Hd. Frau Pelzig\nZweibrückenstraße 12\n80331 München",
        "07.04.2026", "Sch-Lich 26-0188 / DPMA 30 2025 218 446"))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>Stellungnahme zur Monitur vom 18.02.2026</b>", S_H3))
    s.append(Paragraph(
        "Sehr geehrte Frau Pelzig,", S_NORMAL))
    s.append(Paragraph(
        "namens und im Auftrag der Anmelderin nehmen wir auf die Monitur vom 18.02.2026 (Eingang "
        "25.02.) Stellung wie folgt:", S_NORMAL))
    s.append(Paragraph("<b>I. Konkretisierung Klasse 9</b>", S_H3))
    s.append(Paragraph(
        "Die Klasse 9 wird wie folgt konkretisiert:<br/>"
        "<i>„Computer-Software zur kryptografischen Authentifizierung manuell gefertigter "
        "Modeprodukte mittels Hash-Algorithmen (SHA-3, BLAKE3) und nicht-fungibler "
        "Tokens (NFT) auf der Ethereum- und Polygon-Blockchain; Geräte und Apparate "
        "zur Auslesung der entsprechenden RFID-Authentifizierungs-Chips, in die Innenseite "
        "von Bekleidungsstücken eingearbeitet; herunterladbare mobile Apps zur Verifizierung "
        "der Echtheit unter dem Markenzeichen klôtzzkètté pure human craft.“</i>",
        S_NORMAL))
    s.append(Paragraph("<b>II. Unterscheidungskraft</b>", S_H3))
    s.append(Paragraph(
        "Der Beanstandung wird insoweit beigetreten, dass eine isolierte Anmeldung des Wortteils "
        "„pure human craft“ nicht beabsichtigt ist; das Zeichen wird ausschließlich in der "
        "<b>Wort-/Bildkombination</b> beansprucht. Die Unterscheidungskraft des Gesamtzeichens "
        "wird durch die individuelle Schriftgestaltung (Custom-Antiqua „Klotzz-Antiqua 1923“), "
        "die lateinische Umschrift „MANU FACTA · NON MACHINA NATA“ und das Krönchen-Insigne "
        "klar hervorgerufen. Vgl. <i>BGH, 17.10.2017 — I ZB 22/16, Quadratisch Praktisch Gut</i>; "
        "<i>BGH, 06.04.2017 — I ZB 39/16, Schokoladengoldhase</i>.", S_NORMAL))
    s.append(Paragraph("<b>III. Antrag</b>", S_H3))
    s.append(Paragraph(
        "Wir beantragen, die Anmeldung in der konkretisierten Form zur Eintragung zuzulassen.",
        S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("München, 07.04.2026 — gez. Dr. Dr. A. Steinacker-von Tarsis &amp; MvB",
                        S_NORMAL_LEFT))
    return s

story += blatt_dpma_antwort_monitur()
story.append(PageBreak())

print("[part12] done")
