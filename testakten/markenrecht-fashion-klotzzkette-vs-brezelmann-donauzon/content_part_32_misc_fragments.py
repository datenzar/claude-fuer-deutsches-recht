# Part 32: Fax-Wechsel, weitere handschriftliche Notizen, Sachverständigenrechnungen,
# Telefonnotizen
def blatt_fax_donauzon():
    s = []
    s.append(FaxHeader(
        from_no="+352 26 11 88 22",
        to_no="+49 89 21 03 96-99",
        date="2026-04-14 16:48:11 +0200",
        pages="2 of 2",
        subject="Re: AZ 2-03 O 412/26 — Vorschlag zur außergerichtlichen Beilegung",
        sender="Donauzon Marketplace GmbH · Tour Trintignant · 2540 Luxembourg",
        recipient="Steinacker Lichtenberg & Partners IP Boutique · München"))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph(
        "Sehr geehrte Frau Dr. Dr. Steinacker-von Tarsis,", S_NORMAL))
    s.append(Paragraph(
        "im Anschluss an unsere Klageerwiderung vom 14.04.2026 erlauben wir uns, einen "
        "Vorschlag zur außergerichtlichen Beilegung des Verfahrens zu unterbreiten. "
        "Unsere Mandantin ist bereit, im Sinne einer kooperativen Lösung folgende "
        "Maßnahmen anzubieten:", S_NORMAL))
    items = [
        "(1) Einrichtung eines „Brand Registry“-Kontos für klôtzzkètté S.A. mit "
        "<i>Trusted-Flagger</i>-Status nach Art. 22 DSA (kostenfrei; sofortige "
        "Umsetzung; Implementierung 14 Tage);",
        "(2) Proaktive Entfernung sämtlicher Listings, die das Wortzeichen "
        "„klotzkettiee“ oder „klotzkettie“ enthalten, aus den DE/AT/CH/FR/IT-"
        "Marketplaces (binnen 21 Tagen ab Vergleich);",
        "(3) Sperrung des Verkäufer-Accounts der UAB klotzkettie sowie ggf. assoziierter "
        "Accounts;",
        "(4) Pauschale Aufwandsentschädigung an klôtzzkètté S.A. in Höhe von "
        "<b>EUR 35.000,00</b> für entstandene Rechtsverfolgungskosten;",
        "(5) Keinerlei Eingeständnis einer rechtlichen Haftung; lite pendente "
        "Kostenaufteilung 50/50.",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    s.append(Paragraph(
        "Wir bitten um Rückmeldung binnen <b>14 Tagen</b>. Sollte sich Ihre Mandantin "
        "nicht bis zum 28.04.2026 (Eingang bei uns) auf diesen Vorschlag einlassen, "
        "behalten wir uns vor, im Termin am 11.06.2026 ausführlicher zu erwidern.",
        S_NORMAL))
    s.append(Paragraph(
        "Mit kollegialen Grüßen", S_NORMAL))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph(
        "<i>i.A.</i> Roy „Roi“ Pelletier, Director Legal &amp; Trust EMEA<br/>"
        "Donauzon Marketplace GmbH · Tour Trintignant · 2540 Luxembourg<br/>"
        "Tel +352 26 11 88-0 · roy.pelletier@donauzon.com", S_SMALL))
    s.append(Spacer(1, 0.3*cm))
    s.append(HandNote(
        "Donauzon will EUR 35.000. Wir wollen EUR 4.8 Mio.\n"
        "Comtesse sagt: „Pas de pitié.“\n"
        "Ablehnung 25.04. mit Vorschlag EUR 2,1 Mio + Notice-and-Stay-Down\n"
        "+ Trusted Flagger + DSA Art. 23 (Counterfeit Reporter).\n"
        "Pelletier wird das nicht akzeptieren — aber wir bauen Druck auf.\n"
        "— Brenkenhoff, 16.04.",
        font=FONT_HAND, size=13.5, angle=-0.4, w=15*cm))
    return s

story += blatt_fax_donauzon()
story.append(PageBreak())

def blatt_steinpfeil_rechnung():
    s = []
    s.append(Paragraph("<b>PROF. DR. HIERONYMUS STEINPFEIL</b>", S_CENTER))
    s.append(Paragraph("<i>Sachverständigenbüro für Markenrecht &amp; Verkehrsauffassung</i>",
                        S_CENTER))
    s.append(Paragraph("Schellingstraße 144 · 80798 München · Tel +49 89 12 84 88-0",
                        S_CENTER))
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>HONORARRECHNUNG Nr. 26-G-0118</b>", S_RIGHT))
    s.append(Spacer(1, 0.2*cm))
    rows = [
        ["Empfängerin:", "Steinacker Lichtenberg & Partners IP Boutique"],
        ["Anschrift:", "Maximiliansplatz 19 · 80333 München"],
        ["Az.-Bezug:", "2-03 O 412/26 — klôtzzkètté ./. Brezelmann u. Donauzon"],
        ["Tätigkeitszeitraum:", "20.02. – 14.05.2026"],
        ["Rechnungsdatum:", "20. Mai 2026"],
        ["Fälligkeit:", "20. Juni 2026 (30 Tage netto)"],
    ]
    t = Table(rows, colWidths=[4*cm, 12.5*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("FONTNAME", (0,0), (0,-1), "Times-Bold"),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888")),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.2*cm))
    rows = [
        ["Pos.", "Leistung", "Std./Pos.", "Satz €/h", "Summe €"],
        ["1.", "Vorbesprechung und Akteneinsicht (Bl. 1–48)", "8,5", "385,00",
         "3.272,50"],
        ["2.", "Gutachten Verkehrsauffassung „Verwechslungsgefahr KLÔTZZKÈTTÉ ↔ "
              "klotzkettiee“ (88 Seiten, in vier Sprachen referenziert)",
         "62,0", "385,00", "23.870,00"],
        ["3.", "Vorbereitung Termin 11.06.2026 (vorgemerkt) und Korrespondenz",
         "6,0", "385,00", "2.310,00"],
        ["4.", "Reisekosten Pendelverkehr Schellingstraße ↔ Maximiliansplatz "
              "(13× zu Fuß)", "—", "—", "0,00"],
        ["5.", "Übersetzungs- und Schreibauslagen, Recherchen", "—", "—",
         "1.488,15"],
        ["6.", "Konsultation Kollege Dr. K.-H. Vogelstein-Mommsen (Universität Heidelberg) "
              "zur Frage Sieckmann-Anwendbarkeit", "4,5", "385,00", "1.732,50"],
        ["", "<b>Nettosumme</b>", "", "", "<b>32.673,15</b>"],
        ["", "USt 19 %", "", "", "6.207,90"],
        ["", "<b>Endsumme</b>", "", "", "<b>38.881,05</b>"],
    ]
    t = Table(rows, colWidths=[1.0*cm, 10.0*cm, 1.8*cm, 1.8*cm, 1.9*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 8.5),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1c2e4a")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888")),
        ("ALIGN", (2,1), (-1,-1), "RIGHT"),
        ("BACKGROUND", (0,-3), (-1,-1), colors.HexColor("#ede0c8")),
        ("FONTNAME", (1,-3), (-1,-1), "Times-Bold"),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Bankverbindung: Stadtsparkasse München · IBAN DE93 7015 0000 0123 4567 88 · "
        "BIC SSKMDEMM<br/>Bei Überweisung bitte Rechnungsnummer 26-G-0118 angeben. "
        "USt-IdNr. DE 188 217 042.", S_SMALL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Prof. Dr. Hieronymus Steinpfeil — Sachverständiger", S_NORMAL))
    s.append(Spacer(1, 0.4*cm))
    s.append(HLine())
    s.append(Paragraph("<b>Mlle Hortense PÉRIGORD — Olfactrice diplômée Grasse</b>", S_H3))
    s.append(Paragraph(
        "<b>Note d'honoraires N° 26/088</b> — pour la rédaction du complément au "
        "rapport olfactique relatif à la marque „K°° pour Femme“ (rapport II du "
        "25 juin 2026), comprenant l'analyse comparative GC-MS de 14 échantillons, "
        "la rédaction multilingue (FR-EN-DE) et la déposition orale prévue le "
        "12 octobre 2026 devant la BoA EUIPO Alicante.", S_NORMAL))
    rows = [
        ["Désignation", "Montant € HT"],
        ["Analyse GC-MS chromatographique (Laboratoire Robertet, Grasse) — 14 échant.",
         "8.450,00"],
        ["Rédaction rapport II (32 pages, trilingue)", "14.200,00"],
        ["Préparation et déplacement Alicante (vol + 2 nuits)", "1.880,00"],
        ["Honoraires de comparution (estimés, à confirmer)", "4.500,00"],
        ["Total HT", "29.030,00"],
        ["TVA 20 % (France)", "5.806,00"],
        ["<b>Total TTC</b>", "<b>34.836,00</b>"],
    ]
    t = Table(rows, colWidths=[12.5*cm, 4*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#3a2c1a")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888")),
        ("ALIGN", (1,1), (-1,-1), "RIGHT"),
        ("BACKGROUND", (0,-1), (-1,-1), colors.HexColor("#ede0c8")),
    ]))
    s.append(t)
    return s

story += blatt_steinpfeil_rechnung()
story.append(PageBreak())

def blatt_telefonnotiz():
    s = []
    s.append(Paragraph("<b>TELEFONNOTIZ</b>", S_H1))
    s.append(HLine())
    s.append(Spacer(1, 0.3*cm))
    rows = [
        ["Datum:", "23. Juni 2026, 11:14 – 11:47 MEZ"],
        ["Telefonierende:", "RA M. v. Brenkenhoff (München) ↔ J. H. Whitman III, Esq. (New York)"],
        ["Az.:", "2-03 O 412/26 · WBF-2026-KK-0014 · TTAB Opp. 91/289.412"],
        ["Notierende:", "Brenkenhoff (Diktat 13:08, abgetippt 14:22 durch RefRA Pia Lützow)"],
        ["Verteiler:", "Akte; Steinacker; Forsythe-Vanderhof; Brennan IV — NICHT Mandantin"],
    ]
    t = Table(rows, colWidths=[3.5*cm, 13*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("FONTNAME", (0,0), (0,-1), "Times-Bold"),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888")),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>Inhalt</b>", S_H3))
    s.append(Paragraph(
        "Whitman III berichtet, dass die TTAB-Discovery-Conference am 03.06.2026 "
        "stattgefunden hat. Klotzkettie LLC war NICHT vertreten („no-show“). Cheryl S. "
        "Goodman (Interlocutory Attorney) hat eine Show-Cause-Order angekündigt; bei "
        "weiterer Nichtteilnahme droht Default Judgment unter 37 C.F.R. § 2.132. "
        "Halston hält das für „extremely good news“.", S_NORMAL))
    s.append(Paragraph(
        "Brenkenhoff fragt nach der Strategie für den parallelen LG-Frankfurt-Termin "
        "(11.06.2026): Donauzon hat über Pelletier (Luxembourg) erneut "
        "Vergleichsfühler ausgestreckt, diesmal mit Angebot EUR 850.000 plus Trusted "
        "Flagger plus permanente Sperrung der UAB klotzkettie. Whitman III empfiehlt "
        "TAKTIK: Annahme im Grundsatz, aber Bedingung: KEIN Geheimhaltungs-Vergleich, "
        "weil sonst die US-SDNY-Klage geschwächt würde („ich brauche das DE-Urteil als "
        "Sword-and-Shield-Beweis für meine Lanham-Act-Counterfeiting-Beweisaufnahme“).",
        S_NORMAL))
    s.append(Paragraph(
        "Folgevereinbarung: Mittwoch-Strategie-Call 24.06.2026, 15:00 MEZ / 09:00 EDT. "
        "Brenkenhoff bereitet einen Side-by-Side-Vergleich der DE- und US-Strategien "
        "vor. Halston verspricht, am Dienstag eine erste Discovery-Protective-Order-"
        "Vorlage zu versenden.", S_NORMAL))
    s.append(Paragraph("<b>Action Items</b>", S_H3))
    items = [
        "[B] Side-by-Side DE/US-Strategie bis 24.06., 14:00 MEZ;",
        "[W] Protective Order Draft bis 23.06., EOB EDT;",
        "[F-V] TTAB-Default-Motion vorbereiten, falls Klotzkettie LLC am 03.07. erneut "
        "no-shows;",
        "[S] Comtesse-Briefing telefonisch 24.06., 22:00 MEZ — sprachlich behutsam, "
        "weil sie mittlerweile in Cannes auf der Festspiele-Yacht ist und keine "
        "Anrufe vor 23:00 MEZ erträgt.",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>Zitate (auf Wunsch wörtlich)</b>", S_H3))
    s.append(Paragraph(
        "Whitman III: <i>„This is the moment to keep the pressure on. Klotzkettie LLC is "
        "running out of cash for representation; the Brezelmann faction in Germany is "
        "running out of plausible-deniability. We close ranks now.“</i>", S_QUOTE))
    s.append(Paragraph(
        "Brenkenhoff: <i>„Einverstanden. Aber bei der Comtesse muss man behutsam sein — "
        "sie liebt das Wort ‚Sieg‘ nicht; sie liebt das Wort ‚Anerkennung‘.“</i>",
        S_QUOTE))
    s.append(Paragraph(
        "Whitman III: <i>„Then we shall talk to her about Anerkennung. With or without "
        "the umlaut.“</i>", S_QUOTE))
    s.append(Spacer(1, 0.4*cm))
    s.append(HandNote(
        "Halston ist ein guter Mann.\n"
        "Auch wenn er Anerkennung nicht aussprechen kann.\n"
        "Pia hat sich an seinem „Annerkennung“ verschluckt.\n"
        "(Wirklich — sie hat im Sekretariat losgelacht.)\n"
        "— Brenkenhoff",
        font=FONT_HAND3, size=11.5, angle=1.2, w=14*cm))
    return s

story += blatt_telefonnotiz()
story.append(PageBreak())

print("[part32] done")
