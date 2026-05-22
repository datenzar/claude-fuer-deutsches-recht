# Part 06: Gerichtsvollzieher-Protokoll Pitti Uomo (mehrere Seiten)
def blatt_gv_protokoll():
    s = []
    s.append(Paragraph("<b>PROTOKOLLO DI ESECUZIONE FORZATA  ·  PROTOKOLL ÜBER DIE VOLLZIEHUNG</b>", S_CENTER))
    s.append(Paragraph("<i>einer einstweiligen Verfügung des LG Frankfurt a.M., Az. 2-03 O 412/26</i>", S_CENTER))
    s.append(Paragraph("— im Wege der Amtshilfe gem. EuVTVO; Rogatorische Übertragung an das Tribunale di Firenze —",
                        S_CENTER))
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.3*cm))
    meta = [
        ["Vollziehungsort:", "Messe Pitti Uomo, Fortezza da Basso, Florenz"],
        ["", "Halle 7 („Padiglione delle Ghiaie“), Stand B-44"],
        ["Datum / Zeit Beginn:", "12.03.2026, 09:14 Uhr (CET)"],
        ["Datum / Zeit Ende:", "12.03.2026, 14:47 Uhr (CET)"],
        ["Beteiligter Schuldner:", "Brezelmann Discount KG, vertreten durch Hr. Egon Brezelmann"],
        ["Gläubigerin (Antragsteller):", "klôtzzkètté S.A., Paris"],
        ["Vollziehender Gerichtsv.:", "Niccolò Sartori, Ufficiale Giudiziario, Tribunale di Firenze"],
        ["Sequester:", "RA Dr. Lorenzo Maletti, Mailand (anwesend ab 11:03 Uhr)"],
        ["Beistand des Schuldners:", "Avv. Federico Bombelli, Studio Bombelli &amp; Trevisani, Florenz"],
        ["Beistand der Gläubigerin:", "RA Maximilian Frhr. von Brenkenhoff, Steinacker Lichtenberg (München)"],
        ["Zeugen:", "(1) Maria-Elena Forli (Messemitarb., Pitti Immagine);"],
        ["", "(2) Antonio Vespucci (Messemitarb., Aufsicht Halle 7);"],
        ["", "(3) Carabiniere Cap. M. Garibaldi, NAS Florenz, Matr. 8842-K"],
    ]
    t = Table(meta, colWidths=[4.4*cm, 12.0*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("FONTNAME", (0,0), (0,-1), "Times-Bold"),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("BOX", (0,0), (-1,-1), 0.3, colors.HexColor("#777777")),
        ("INNERGRID", (0,0), (-1,-1), 0.15, colors.HexColor("#bbbbbb")),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Auf rogatorisches Ersuchen des Landgerichts Frankfurt am Main (Beschluss vom 11.03.2026, "
        "Az. 2-03 O 412/26) i.V.m. Art. 39 EuGVVO (Brüssel Ia) wurde durch den "
        "Unterzeichneten die Vollziehung des vorgenannten Beschlusses am Stand B-44 der Brezelmann "
        "Discount KG auf der Messe Pitti Uomo durchgeführt. Der Stand war zum Vollzugszeitpunkt "
        "geöffnet; die Antragsgegnerin zu 1) vertreten durch ihren Komplementär Herrn Egon "
        "Brezelmann.", S_NORMAL))
    s.append(Paragraph(
        "<b>Vorgehen:</b> Nach Vorlage der Ausfertigung des Beschlusses (mit beglaubigter "
        "Übersetzung in die italienische Sprache, beglaubigt durch die Ermächtigte Übersetzerin "
        "Dott.ssa Sofia Innocenti, Florenz, am 11.03.2026, 22:30 Uhr) und förmlicher Zustellung "
        "an den Komplementär persönlich (09:18 Uhr) wurden die nachfolgend aufgelisteten Waren "
        "beschlagnahmt und an den vom LG Frankfurt bestellten Sequester (RA Dr. Maletti) "
        "herausgegeben. Die Wegnahme erfolgte unter Mitwirkung des Carabiniere-Hauptmanns "
        "Garibaldi nach dessen kurzer Diskussion mit dem Komplementär, in deren Verlauf der "
        "Schuldner mehrfach den Satz <i>« questa è una vergogna! »</i> äußerte.", S_NORMAL))
    s.append(Paragraph("<b>I N V E N T A R   D E R   B E S C H L A G N A H M T E N   W A R E N</b>", S_H3))
    inv = [
        ["Pos.", "Bezeichnung", "Modell-Nr.", "Stk.", "Einzel-VK €", "Summe €"],
        ["1", "T-Shirt Herren weiß m. K°°-Druck", "BTM-MEN-022", "312", "9,99", "3.116,88"],
        ["2", "Halstuch Damen seidenähnl. (Polyester) m. Krönchen-Bordüre", "BTM-WMN-118", "204", "12,99", "2.649,96"],
        ["3", "Handtasche PU-Leder schwarz m. K°°-Prägung", "BTM-BAG-K044", "88", "24,99", "2.199,12"],
        ["4", "Parfumflakon hexagonal asymm. Stopfen „K-Royal“ 50 ml", "BTM-PARF-K01", "14", "14,99", "209,86"],
        ["5", "Poster A0 „Brezelmann Luxe Outlet — feat. K°° Krönchen“", "BTM-POSTER-A0", "2", "—", "—"],
        ["6", "Werbedisplay Roll-Up mit Krönchen-Motiv", "BTM-ROLL-K", "1", "—", "—"],
        ["7", "Restposten unsortiert in Karton, vermutl. Versch.", "—", "ca. 47", "—", "—"],
        ["", "", "<b>Summe wertmäßig erfasst:</b>", "<b>668</b>", "", "<b>8.175,82</b>"],
    ]
    t2 = Table(inv, colWidths=[1.0*cm, 5.5*cm, 3.2*cm, 1.2*cm, 1.9*cm, 1.9*cm], repeatRows=1)
    t2.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 8.5),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#333333")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#888888")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0,1), (-1,-2), [colors.white, colors.HexColor("#f5f1e6")]),
        ("BACKGROUND", (0,-1), (-1,-1), colors.HexColor("#e6d7b0")),
        ("ALIGN", (3,1), (5,-1), "RIGHT"),
    ]))
    s.append(t2)
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph(
        "Sämtliche Waren wurden in <b>17 Versandkartons</b> verpackt (Inv-Nr. SEQ-2026/0312/01 — "
        "SEQ-2026/0312/17) und durch den Sequester gegen Quittung übernommen. Verbringung zum "
        "Lagerraum der Studio Maletti, Via Manzoni 14, Mailand, durch die Spedition "
        "<b>Trasporti Veloci s.r.l.</b> (Frachtbrief CMR-Nr. IT-2026-04471).", S_NORMAL))
    s.append(Paragraph(
        "<b>Anmerkung des Vollziehers:</b> Der Komplementär hat die Wegnahme zunächst durch "
        "körperliches Versperren des Standzugangs zu vereiteln versucht (09:34 — 09:41 Uhr) und "
        "ist erst nach Androhung der Verhaftung durch Cap. Garibaldi zurückgewichen. Wörtlich: "
        "<i>« Andate via, voi siete dei pirati! »</i> (Übers.: „Geht weg, ihr seid Piraten!“). "
        "Eine Protokollunterzeichnung durch den Komplementär ist verweigert worden (§ 762 ZPO "
        "entspr.).", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Florenz, 12.03.2026, 14:47 Uhr", S_NORMAL_LEFT))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("Niccolò <b>Sartori</b>", S_NORMAL_LEFT))
    s.append(Paragraph("Ufficiale Giudiziario, Tribunale di Firenze", S_SMALL))
    s.append(Paragraph("Matr.-Nr. 4471-FI", S_SMALL))
    return s

story += blatt_gv_protokoll()
story.append(PageBreak())

# Inventarliste handschriftlich / Rückseite Protokoll
def blatt_gv_handschrift():
    s = []
    s.append(Paragraph("<b>ANLAGE zum Protokoll Sartori 12.03.2026 — handschriftl. Notiz Hr. v. Brenkenhoff</b>",
                        S_CENTER))
    s.append(HLine())
    s.append(Spacer(1, 0.4*cm))
    s.append(HandNote(
        "Pitti-Vollziehung Bericht / Hr. v. B. an ASt:\n"
        "\n"
        "09:14  Eintreffen am Stand B-44, Halle 7 (südl. Eingang)\n"
        "09:18  Zustellung Beschluss durch Sartori — Brezelmann zuerst sprachlos\n"
        "09:22  Brezelmann ruft seine Anwältin in Würzburg an (45 Min. erfolglos)\n"
        "09:34  Versuch der Versperrung — Sartori hält stand\n"
        "09:41  Cap. Garibaldi spricht Klartext — Brezelmann gibt nach\n"
        "10:03  Beginn Inventur — 668 Stück Ware erfasst\n"
        "11:03  Maletti trifft ein (war im Stau auf A1 von Mailand)\n"
        "13:12  Foto-Dokumentation 47 Aufnahmen — siehe USB-Stick Anlage A\n"
        "14:47  Verladung abgeschlossen, Carabiniere bleibt vor Ort\n"
        "\n"
        "Brezelmann hat zwischendurch versucht 3 Parfumflakons in seine\n"
        "Aktentasche zu schmuggeln — Sartori hat es bemerkt und ihn\n"
        "konfrontiert. Sehr unangenehmer Moment für alle.\n"
        "\n"
        "Comtesse hat um 15:30 angerufen und gelacht (« je suis ravie »).\n"
        "Frühflug morgen FRA — bis Montag im Büro.\n"
        "MvB",
        font=FONT_HAND, size=13, color=colors.HexColor("#1e3a6e"),
        w=16*cm, angle=-0.3, ruled=True))
    return s

story += blatt_gv_handschrift()
story.append(PageBreak())

print("[part06] done")
