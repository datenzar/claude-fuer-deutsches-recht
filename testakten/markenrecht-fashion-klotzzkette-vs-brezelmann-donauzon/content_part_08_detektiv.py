# Part 08: Detektivbericht Spürnase-Couture GmbH + Foto-Liste + Rechnung
def blatt_detektiv_1():
    s = []
    # Briefkopf Detektei
    s.append(Paragraph("<font color='#2a1a0a'><b>SPÜRNASE-COUTURE GmbH</b></font>", S_CENTER))
    s.append(Paragraph("<i>— Wirtschafts- und Markenrechts-Detektei für die Modeindustrie —</i>", S_CENTER))
    s.append(Paragraph("Bahnhofsplatz 3 · 60329 Frankfurt am Main · T +49 69 24 28 17-0 · F -99",
                        S_CENTER))
    s.append(HLine(thickness=0.8))
    s.append(Spacer(1, 0.3*cm))
    meta = [
        ["Auftraggeber:", "Steinacker Lichtenberg &amp; Partners IP Boutique, München"],
        ["Endmandantin:", "klôtzzkètté S.A., Paris"],
        ["Auftragsdatum:", "14.01.2026"],
        ["Berichtszeitraum:", "17.01.2026 — 09.03.2026"],
        ["Auftragsnr.:", "SPC-2026-K-0044"],
        ["Bearbeitende Detektivin:", "Karla Kalt-Bandel (Operative Leitung)"],
        ["Unterstützung:", "Detektiv-Anwärter Bjarne Hossenfeld (1. Lehrjahr)"],
        ["Bericht-Nr.:", "SPC-2026-K-0044/Bericht-final"],
    ]
    t = Table(meta, colWidths=[4.2*cm, 12.0*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("FONTNAME", (0,0), (0,-1), "Times-Bold"),
        ("BOX", (0,0), (-1,-1), 0.3, colors.HexColor("#777777")),
        ("INNERGRID", (0,0), (-1,-1), 0.15, colors.HexColor("#bbbbbb")),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("<b>I. AUFTRAG</b>", S_H3))
    s.append(Paragraph(
        "Erhebung des Vertriebsumfangs der Brezelmann Discount KG hinsichtlich der mutmaßlich "
        "markenrechtsverletzenden Waren (T-Shirts, Halstücher, Handtaschen-Imitate, Parfumflakons "
        "— sämtlich mit Krönchen-Monogramm „K°°“ oder Schriftzug „klötzkette“). Beobachtungs"
        "objekte: drei Filialen in Bad Mergentheim, Crailsheim und Tauberbischofsheim sowie das "
        "Zentrallager der Brezelmann-Gruppe in Königshofen (Industriestraße 14).", S_NORMAL))
    s.append(Paragraph("<b>II. BEOBACHTUNGSLOGBUCH</b>", S_H3))
    log = [
        ["Datum", "Uhrzeit", "Ort", "Beobachtung"],
        ["17.01.2026", "10:42-13:18", "Filiale Bad Mergentheim",
         "Eingang: Pappkartons gestapelt (24 Stk), Etiketten erkennbar K°°-Monogramm. "
         "Verkaufsraum: 2 Verkaufsdisplays mit T-Shirts BTM-MEN-022. Aufn. 1, 2, 3."],
        ["17.01.2026", "14:30-15:48", "Filiale Bad Mergentheim",
         "Testkauf 1 (T-Shirt EUR 9,99 + Halstuch EUR 12,99) — Quittung Nr. K-44/2026-1188. "
         "Verkäuferin Fr. Wegner-Schramm bestätigt: „Wir kriegen das immer aus Italien.“"],
        ["18.01.2026", "09:15-11:32", "Filiale Crailsheim",
         "Schaufenster: Roll-Up-Display „Brezelmann Luxe — feat. K°°“. "
         "Aufn. 4, 5. Eingang: Lieferung wird gerade ausgeladen, "
         "8 Kartons mit kyrillischer und lateinischer Beschriftung „klotzkettie UAB Vilnius“."],
        ["18.01.2026", "12:00-12:45", "Filiale Crailsheim",
         "Testkauf 2 (Handtasche BTM-BAG-K044 + Parfumflakon BTM-PARF-K01) — "
         "Quittung Nr. K-72/2026-0322. Aufn. 6 (Parfumflakon im Verkaufsregal)."],
        ["19.01.2026", "08:00-10:18", "Filiale Tauberbischofsheim",
         "Schaufenster mit Poster „klötzkette für jedermann“ in Comic-Sans-Schriftart. "
         "Aufn. 7, 8."],
        ["19.01.2026", "11:00-12:30", "Filiale Tauberbischofsheim",
         "Beobachtung: Drei Damen aus Würzburg betreten die Filiale, fragen nach „echtem“ K°°. "
         "Verkäufer Herr Drechselmann: „Original wie aus Paris, nur viel günstiger.“ "
         "Bandaufnahme M-Track 22 (vgl. Anlage SPC-AUD-3)."],
        ["20.01.2026", "06:30-08:00", "Lager Königshofen",
         "Vor-Tor-Beobachtung. LKW „Brezelmann-Logistik“ liefert um 07:14 Uhr 4 Paletten "
         "an. Aufn. 9, 10. Auf den Lieferscheinen lesbar: „Absender: klotzkettie UAB, "
         "LT-01402 Vilnius“. Fahrer (Lt. Kennzeichen): LT-Kennzeichen ZGZ-887."],
        ["29.01.2026", "10:00-13:00", "Filiale Bad Mergentheim",
         "Nachkontrolle. Mengenschätzung Lager: ca. 1.200 T-Shirts, 400 Halstücher, "
         "200 Handtaschen, 80 Parfumflakons. Aufn. 11."],
        ["07.02.2026", "—", "Online-Recherche",
         "Donauzon Marketplace: 2.342 aktive Angebote mit Begriff „klötzkette“, "
         "„klotzkette“ oder „K°°“. Screenshot-Sammlung SPC-SCR-1 bis SPC-SCR-187 erstellt."],
        ["09.03.2026", "11:00-15:30", "Pitti-Vorbereitung",
         "Anruf einer Vertrauensperson („Onkel Cosimo“, Florenz): Pitti Uomo Halle 7 "
         "Stand B-44 ist von Brezelmann gebucht; Aufbau läuft seit 08.03.2026, 14:00 Uhr. "
         "Aufn. 12, 13, 14 (Standaufbau, Roll-Up, Kartonstapel)."],
    ]
    t = Table(log, colWidths=[2.0*cm, 2.0*cm, 3.5*cm, 8.5*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 8),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#3a2c1a")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888888")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f5f1e6")]),
        ("LEFTPADDING", (0,0), (-1,-1), 3),
        ("RIGHTPADDING", (0,0), (-1,-1), 3),
        ("TOPPADDING", (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
    ]))
    s.append(t)
    return s

story += blatt_detektiv_1()
story.append(PageBreak())

def blatt_detektiv_2():
    s = []
    s.append(Paragraph("<b>III. FOTO-DOKUMENTATION (textuelle Beschreibung der Aufnahmen)</b>", S_H3))
    photos = [
        ("Aufn. 1", "Eingangsbereich Filiale Brezelmann Bad Mergentheim, gestapelte Pappkartons "
                     "(24 Stk) mit Klôtzzkètté-Original-Etiketten — Detailaufn. eines Etiketts: "
                     "Schriftzug „klotzkettie UAB · Vilnius“ mit K°°-Logo."),
        ("Aufn. 2", "Verkaufsdisplay T-Shirts BTM-MEN-022, ca. 60 Stück gestapelt, Preisschild "
                     "EUR 9,99."),
        ("Aufn. 3", "Detail T-Shirt: Brustaufdruck Krönchen K°°, daneben Schriftzug „klötzkette“ "
                     "(mit Umlaut!) — Druckqualität minderwertig (vgl. Olfaktorik-Befund: leichter "
                     "Lösungsmittel-Geruch)."),
        ("Aufn. 4", "Schaufenster Crailsheim: Roll-Up „Brezelmann Luxe — feat. K°°“, im "
                     "Hintergrund Mannequin mit Imitations-Halstuch."),
        ("Aufn. 5", "Crailsheim: gleicher Roll-Up von schräg rechts."),
        ("Aufn. 6", "Crailsheim: Parfumflakon BTM-PARF-K01 im Verkaufsregal — hexagonaler "
                     "Korpus, asymmetrischer Stopfen (Original-Maße 13,7 cm × 5,4 cm; "
                     "Imitation: 13,5 cm × 5,3 cm — Identität bis ± 2 mm)."),
        ("Aufn. 7", "Tauberbischofsheim Schaufenster mit Comic-Sans-Poster „klötzkette für "
                     "jedermann“ (sic!) — Schriftart erkennbar nicht der hauseigene "
                     "Klôtzzkètté-Serifenduktus."),
        ("Aufn. 8", "Tauberbischofsheim Eingang von außen, Geschäftszeiten-Schild lesbar."),
        ("Aufn. 9", "Lager Königshofen: LKW Brezelmann-Logistik beim Entladen, vier Paletten "
                     "auf der Laderampe."),
        ("Aufn. 10", "Königshofen: Detailaufn. Lieferschein, Absender lesbar „klotzkettie UAB, "
                      "Vilniaus g. 47, LT-01402 Vilnius, Lithuania“ — Empfänger „Brezelmann "
                      "Discount KG / Wurstgasse 4 / 97980 Bad Mergentheim“. CMR-Nr. "
                      "LT-2026-01-0814."),
        ("Aufn. 11", "Bad Mergentheim Lager-Bereich (durch geöffnete Tür sichtbar): Schätzung "
                      "1.200 T-Shirts, 400 Halstücher, 200 Handtaschen, 80 Parfumflakons."),
        ("Aufn. 12", "Pitti Uomo Halle 7: Standaufbau B-44, 08.03.2026, 14:30 Uhr. "
                      "Roll-Ups bereits aufgebaut, Inventar wird gerade angeliefert."),
        ("Aufn. 13", "Detail Stand B-44: K°°-Krönchen-Monogramm bereits am Banner sichtbar."),
        ("Aufn. 14", "Eingang Stand: Onkel Cosimo (im Profil, mit Hut) vor dem Stand — Aufnahme "
                      "selfie-artig (Detail von Onkel Cosimo nicht erkennbar — Persönlichkeits"
                      "rechte gewahrt)."),
    ]
    rows = [["Aufn.", "Beschreibung"]] + photos
    t = Table(rows, colWidths=[1.6*cm, 14.4*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 8.5),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#3a2c1a")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888888")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f5f1e6")]),
        ("LEFTPADDING", (0,0), (-1,-1), 3),
        ("RIGHTPADDING", (0,0), (-1,-1), 3),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph(
        "<i>Hinweis:</i> Die Aufnahmen liegen physisch auf USB-Stick (Marke Kingston, 32 GB, "
        "Seriennr. KG-2026-44871) bei der Detektei vor und sind dem Empfänger auf Anforderung "
        "auszuhändigen. Backup im Tresor Filiale Frankfurt sowie verschlüsselt auf NAS "
        "Frankfurt-2 (AES-256, Schlüsselverwahrung Notar Dr. Lichtwesen).", S_SMALL))
    s.append(Paragraph("<b>IV. SCHLUSSBEWERTUNG</b>", S_H3))
    s.append(Paragraph(
        "Aus den Beobachtungen ergibt sich ein systematisches, planmäßiges und in großem Umfang "
        "durchgeführtes Vertriebskonzept der Brezelmann Discount KG für nachweislich aus Litauen "
        "(UAB klotzkettie) bezogene Produkte mit Marken der Mandantin. Die Behauptung des "
        "Komplementärs Brezelmann (Fax vom 04.02.2026), die Ware stamme aus „Graumarkt-Import "
        "Turin“, ist nach den vorliegenden Lieferscheinen falsch.", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Frankfurt am Main, 10.03.2026", S_NORMAL_LEFT))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("Karla <b>Kalt-Bandel</b>", S_NORMAL_LEFT))
    s.append(Paragraph("Detektivin · Operative Leitung Spürnase-Couture GmbH", S_SMALL))
    s.append(Spacer(1, 0.3*cm))
    s.append(HandNote(
        "Bjarne hat sich auf der Pitti-Voraufklärung selbst verraten — \nhat ein klôtzzkètté-Original-Halstuch gekauft, lol.\nNächstes Mal nicht mehr aus eigener Tasche!  k.k.b.",
        font=FONT_HAND, size=14, color=colors.HexColor("#345"), w=14*cm, angle=0.7))
    return s

story += blatt_detektiv_2()
story.append(PageBreak())

# ---- Rechnung Detektei
def blatt_detektiv_rechnung():
    s = []
    s.append(Paragraph("<b>SPÜRNASE-COUTURE GmbH · Bahnhofsplatz 3 · 60329 Frankfurt am Main</b>", S_CENTER))
    s.append(HLine())
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("<b>RECHNUNG R-2026-K-0044</b>", S_H2))
    s.append(Paragraph(
        "An: Steinacker Lichtenberg &amp; Partners IP Boutique<br/>"
        "Maximiliansplatz 19 · 80333 München<br/>"
        "z.Hd. Frau Dr. Dr. Steinacker-von Tarsis<br/><br/>"
        "Mandantenbezogen für: klôtzzkètté S.A. Paris<br/>"
        "Auftrag SPC-2026-K-0044", S_NORMAL))
    rows = [
        ["Pos.", "Leistung", "Einheit", "Anz.", "EP €", "Summe €"],
        ["1", "Vor-Ort-Observation 3 Filialen (BadMgm, Crailsh., Taubbi.)",
         "Stunde", "44", "120,00", "5.280,00"],
        ["2", "Testkäufe (3) inkl. Belegdokumentation", "pauschal", "1", "480,00", "480,00"],
        ["3", "Lager-Observation Königshofen (Frühschicht)", "Stunde", "22", "140,00", "3.080,00"],
        ["4", "Foto-Dokumentation (14 Aufn.) + Aufbereitung", "pauschal", "1", "1.200,00", "1.200,00"],
        ["5", "Online-Recherche Donauzon (Screenshots 187 Stk)", "Stunde", "18", "95,00", "1.710,00"],
        ["6", "Pitti-Voraufklärung Florenz (inkl. Reise Bjarne H.)",
         "pauschal", "1", "1.840,00", "1.840,00"],
        ["7", "Berichterstellung + EV-Erklärung Kalt-Bandel", "Stunde", "9", "140,00", "1.260,00"],
        ["8", "Spesen (Tank, Bahn, Übernachtung)", "Beleg", "1", "298,40", "298,40"],
        ["", "", "", "", "<b>Zwischensumme netto</b>", "<b>15.148,40</b>"],
        ["", "", "", "", "Abzug Selbstanzeige Bjarne (-)", "-268,40"],
        ["", "", "", "", "<b>Netto</b>", "<b>14.880,00</b>"],
        ["", "", "", "", "USt 19 %", "2.827,20"],
        ["", "", "", "", "<b>Rechnungsbetrag brutto</b>", "<b>17.707,20</b>"],
    ]
    t = Table(rows, colWidths=[1.0*cm, 7.8*cm, 1.6*cm, 1.2*cm, 2.4*cm, 2.0*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 8.5),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#3a2c1a")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888888")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0,1), (-1,-5), [colors.white, colors.HexColor("#f5f1e6")]),
        ("BACKGROUND", (0,-1), (-1,-1), colors.HexColor("#e6d7b0")),
        ("ALIGN", (3,1), (5,-1), "RIGHT"),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Zahlbar binnen 14 Tagen rein netto auf Konto Frankfurter Sparkasse, "
        "IBAN DE12 5005 0201 0000 4880 88, BIC HELADEF1822. Bitte stets unter "
        "Angabe der Rechnungsnummer R-2026-K-0044.", S_SMALL))
    s.append(Paragraph(
        "Frankfurt am Main, 10.03.2026 — gez. Kalt-Bandel (Geschäftsführerin Spürnase-Couture GmbH)",
        S_SMALL))
    return s

story += blatt_detektiv_rechnung()
story.append(PageBreak())

print("[part08] done")
