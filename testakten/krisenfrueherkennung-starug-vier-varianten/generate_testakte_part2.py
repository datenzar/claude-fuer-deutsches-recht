
# ═══════════════════════════════════════════════════════════════════════════════
# COMPLETION OF build_variante_d + VORLAGEN-ANNEX + FOLIENSATZ + STUNDENAUFSTELLUNG + main()
# This file is appended to generate_testakte_part1.py
# ═══════════════════════════════════════════════════════════════════════════════

# NOTE: This file continues from inside build_variante_d() which was cut off.
# The cut-off point was inside skizze_data definition. We close it here.

_VARIANTE_D_COMPLETION = """
            ParagraphStyle('handskizze', fontName='Times-Italic', fontSize=10,
                           leading=16, textColor=colors.HexColor('#1A1A80'),
                           leftIndent=10)
        )
    ]]
    skizze_tbl = Table(skizze_data, colWidths=[16*cm])
    skizze_tbl.setStyle(TableStyle([
        ('BOX', (0,0),(0,0), 2, colors.HexColor('#1A1A80')),
        ('BACKGROUND', (0,0),(0,0), colors.HexColor('#FAFAEE')),
        ('PADDING', (0,0),(0,0), 12),
        ('VALIGN', (0,0),(-1,-1), 'TOP'),
    ]))
    story.append(skizze_tbl)
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "<i>Anmerkung RAin Wandelmoser: Handschrift des Mandanten, Inhalt plausibel, "
        "Reichweite 11 Tage bestätigt eigene Einschätzung ZU-Risiko. "
        "Original zu den Handakten.</i>",
        S['small']))
    story.append(PageBreak())

    # E-Mail-Kette Tarek-Yusuf
    story.append(Paragraph("D.7 E-Mail-Kette Tarek-Yusuf Celebi-Drebenstedt an RAin Wandelmoser", S['h1']))
    story.append(hr(FARBE_D))
    story.append(Spacer(1, 0.2*cm))

    emails_d = [
        ("Von", "tarek.celebi@salaltbar.de"),
        ("An", "wandelmoser@kanzlei-wandelmoser.de"),
        ("Datum", "25. April 2026, 23:47 Uhr"),
        ("Betreff", "hilfe ich weiss nicht mehr weiter"),
    ]
    for label, val in emails_d:
        row_data = [[
            Paragraph(f"<b>{label}:</b>", S['small']),
            Paragraph(val, S['small'])
        ]]
        row_tbl = Table(row_data, colWidths=[2.5*cm, 14*cm])
        row_tbl.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
        story.append(row_tbl)

    story.append(Spacer(1, 0.15*cm))
    mail1_text = (
        "hallo frau wandelmoser\\n\\n"
        "ich war heute beim steuerberater und der hat mir gesagt ich soll unbedingt zu einem anwalt gehen "
        "wegen meiner firma. ich hab drei filialen salat-bar in neukölln und die zahlen sich kaum noch. "
        "die miete bei der sonnenallee hat sich erhöht und ich weiß gar nicht wie ich das zahlen soll. "
        "der lieferant schickt auch keine ware mehr wenn ich nicht zahle. "
        "ich hab auch irgendwas unterschrieben das ich als geschäftsführer haften muss???\\n\\n"
        "bitte ich brauch hilfe!! bitte bitte bitte. "
        "ich hab auch kinder und meine frau weiss von nichts. "
        "was soll ich jetzt tun??\\n\\n"
        "danke\\nTarek\\n\\n"
        "PS: mein steuerberater hat das hier hingelegt, weiss nicht was das bedeutet: §102 StaRUG ??"
    )
    fax_lines_mail1 = ["=== E-MAIL (eingehend) ==="] + mail1_text.split("\\n")
    story.append(fax_block(fax_lines_mail1))
    story.append(Spacer(1, 0.3*cm))

    # Second email
    emails_d2 = [
        ("Von", "tarek.celebi@salaltbar.de"),
        ("An", "wandelmoser@kanzlei-wandelmoser.de"),
        ("Datum", "26. April 2026, 08:12 Uhr"),
        ("Betreff", "Re: hilfe ich weiss nicht mehr weiter"),
    ]
    for label, val in emails_d2:
        row_data = [[
            Paragraph(f"<b>{label}:</b>", S['small']),
            Paragraph(val, S['small'])
        ]]
        row_tbl = Table(row_data, colWidths=[2.5*cm, 14*cm])
        row_tbl.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
        story.append(row_tbl)
    story.append(Spacer(1, 0.15*cm))
    mail2_text = (
        "frau wandelmoser nochmal ich\\n\\n"
        "entschuldigung dass ich so viele mails schicke aber ich hab heute früh einen brief vom vermieter "
        "gekriegt. er kündigt fristlos! sagt ich hab 3 monate mite nicht gezahlt. "
        "das stimmt gar nicht weil ich hab im januar gezahlt, aber februar und märz... stimmt, "
        "da hab ich irgendwie vergessen oder kein geld gehabt, ich weiss nicht mehr genau.\\n\\n"
        "der brief sagt ich muss raus bis 15. mai 2026. das ist in 3 wochen!!!! "
        "was mache ich jetzt mit den mitarbeitern? die filiale läuft mittwochs immer gut wenn markt ist.\\n\\n"
        "tarek\\n\\nPS: sry für rechtschreibung schreibe vom handy"
    )
    fax_lines_mail2 = ["=== E-MAIL (eingehend) ==="] + mail2_text.split("\\n")
    story.append(fax_block(fax_lines_mail2))
    story.append(PageBreak())

    # Filial-Übersicht-Tabelle
    story.append(Paragraph("D.8 Filial-Uebersicht (Umsaetze, Miete, Wareneinsatz)", S['h1']))
    story.append(hr(FARBE_D))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "Stand: April 2026 (geschaetzte Werte lt. Mandantenangaben, nicht testiert)",
        S['small']))
    story.append(Spacer(1, 0.2*cm))

    filial_data = [
        ['Kennzahl', 'F1: Hermannplatz', 'F2: Boddinstrasse', 'F3: Sonnenallee', 'GESAMT'],
        ['Eroffnet', 'Marz 2023', 'Oktober 2023', 'April 2024', '—'],
        ['Sitzplatze', '28', '18', '22', '68'],
        ['Mitarbeiter (FTE)', '5,5', '3,0', '4,0', '12,5 (+1 GF)'],
        ['Umsatz Apr 2026 (EUR)', '18.400', '11.200', '8.600', '38.200'],
        ['Umsatz Ø/Monat 2025 (EUR)', '20.100', '12.400', '10.200', '42.700'],
        ['Miete kalt (EUR/Mon)', '3.800', '2.400', '5.200', '11.400'],
        ['Wareneinsatz (EUR/Mon)', '7.200', '4.800', '4.100', '16.100'],
        ['Personal (EUR/Mon)', '5.800', '3.200', '4.200', '13.200'],
        ['Sonstige Kosten (EUR/Mon)', '1.200', '900', '1.100', '3.200'],
        ['Summe Kosten (EUR/Mon)', '18.000', '11.300', '14.600', '43.900'],
        ['EBITDA (EUR/Mon)', '+400', '-100', '-6.000', '-5.700'],
        ['Miete-Rückstand (EUR)', '0', '0', '18.400 (3 Mon)', '18.400'],
        ['Vertragslaufzeit Mietvertrag', '31.12.2027', '31.03.2026 (monatl.)', '31.12.2026', '—'],
        ['Kündigungsrisiko', 'GERING', 'MITTEL (monatl.)', 'HOCH (fristlos!)', '—'],
    ]
    filial_tbl = Table(filial_data, colWidths=[4.2*cm, 2.9*cm, 2.9*cm, 2.9*cm, 2.6*cm])
    filial_style = tbl_style_standard()
    filial_style.add('BACKGROUND', (4,0),(4,-1), colors.HexColor('#EEF4FF'))
    filial_style.add('BACKGROUND', (3,1),(3,-1), colors.HexColor('#FFF0F0'))
    filial_style.add('FONTNAME', (0,0),(-1,0), 'Helvetica-Bold')
    filial_style.add('FONTNAME', (0,0),(0,-1), 'Helvetica-Bold')
    for i in [11]:
        filial_style.add('TEXTCOLOR', (1,i),(3,i), ROT)
        filial_style.add('FONTNAME', (1,i),(3,i), 'Helvetica-Bold')
    filial_tbl.setStyle(filial_style)
    story.append(filial_tbl)
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "<b>Schlussfolgerung:</b> F3 Sonnenallee vernichtet EUR 6.000/Monat. "
        "Sofortige Schliessungsprüfung (Kündigungsrecht bereits vorhanden) "
        "könnte monatliches Defizit von EUR 5.700 auf EUR 300 reduzieren. "
        "Gleichzeitig: Verlust von 4 Arbeitsplätzen, Abfindungsrisiko EUR 12.000-18.000.",
        S['body']))
    story.append(PageBreak())

    # Interner Vermerk Wandelmoser
    story.append(Paragraph("D.9 Interner Vermerk RAin Wandelmoser", S['h1']))
    story.append(hr(FARBE_D))
    story.append(Spacer(1, 0.2*cm))

    vermerk_data = [[
        Paragraph(
            "KANZLEI CHARLOTTE WANDELMOSER — INTERNER VERMERK\\n"
            "VERTRAULICH — NUR FUR KANZLEIAKTEN\\n\\n"
            "Mandat: Salaltbar UG (haftungsbeschränkt) / GF Celebi-Drebenstedt\\n"
            "Datum: 28. April 2026\\n"
            "Bearbeiter: RAin C. Wandelmoser\\n\\n"
            "GEBUEHREN / HONORAR:\\n"
            "Erstgespräch (60 min, 28.04.2026): EUR 280,00 netto + MwSt.\\n"
            "Folgemandat: Stundensatz EUR 280,00 netto.\\n\\n"
            "Frage Pro Bono: NEIN. Begründung: Kein soziales Notfall-Mandat im\\n"
            "engeren Sinne; GF hat drei Jahre lang Unternehmen betrieben und Risiken\\n"
            "ignoriert. Zudem: Regressrisiko wenn Insolvenzverwalter später rückwirkend\\n"
            "Beratungsfehler prüft. RATENZAHLUNG anbieten: EUR 500 sofort, dann\\n"
            "EUR 280/Monat bis Abschluss. Mandatsübernahme-Vereinbarung heute unterschreiben.\\n\\n"
            "WEITERVERWEISUNG: Falls StaRUG-Plan oder größere Restrukturierung nötig\\n"
            "(unwahrscheinlich bei dieser Größe): Verweis an Reher Wennstedt Restrukturierung\\n"
            "Partnerschaft mbB, Hamburg (Dr. Tjark Reher-Bornholmsen). Haben Erfahrung\\n"
            "auch mit Kleinstmandanten wenn Grundsatzfragen.\\n\\n"
            "NÄCHSTE SCHRITTE:\\n"
            "1. Mandatsannahme-Schreiben + Vollmacht heute oder 29.04.\\n"
            "2. § 102 StaRUG-Schreiben an GF (als förmliche Warnung, Aktennotiz).\\n"
            "3. Drei-Wochen-Frist § 15a InsO: endet 19.05.2026 (wenn ZU am 28.04. eingetreten).\\n"
            "4. Bis 02.05.: Entscheidung des Mandanten über Schließung F3 Sonnenallee.\\n"
            "5. Bei Entscheidung Weitermachen: 13-Wochen-Liquiditätsplan erstellen (vereinfacht).\\n\\n"
            "RISIKOFAKTOREN MANDAT:\\n"
            "- Mandant kfm. überfordert, Kommunikation über WhatsApp/E-Mail nachts\\n"
            "- Ehefrau von Krise unwissend — Haftungsrisiko wenn gemeinsam Vermögen\\n"
            "- Steuerrückstände könnten zu persönl. Haftung GF nach § 69 AO führen\\n"
            "- Lieferstopp Frische-Kontor: Betriebsunterbrechung F1+F2 sofort möglich\\n\\n"
            "DOKUMENTATION: Alle E-Mails ausdrucken + zu den Akten.",
            ParagraphStyle('vermerk_int', fontName='Courier', fontSize=8,
                           leading=12, textColor=TEXT_SCHWARZ, leftIndent=5)
        )
    ]]
    verm_tbl = Table(vermerk_data, colWidths=[16.5*cm])
    verm_tbl.setStyle(TableStyle([
        ('BOX',(0,0),(0,0),1.5,GRAU_DUNKEL),
        ('BACKGROUND',(0,0),(0,0),colors.HexColor('#FFFEF0')),
        ('PADDING',(0,0),(0,0),10),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
    ]))
    story.append(verm_tbl)
    story.append(Spacer(1, 0.3*cm))

    # Frühwarnsystem-Light für UGs
    story.append(PageBreak())
    story.append(Paragraph("D.10 Fruehwarnsystem-Light-Vorlage fuer UGs (vereinfachtes 24-Monats-Sheet)", S['h1']))
    story.append(hr(FARBE_D))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Diese Vorlage richtet sich an Geschaeftsfuehrer kleiner UGs und GmbHs "
        "ohne kaufmaennische Ausbildung. Sie ist kein Ersatz fuer professionelle Beratung, "
        "hilft aber, Krisenfrühsignale zu erkennen und § 1 StaRUG-Pflicht zu erfüllen.",
        S['body']))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("SCHRITT 1: Kassensturz (monatlich, 1. des Monats)", S['h2']))
    kasse_data = [
        ['Position', 'Betrag (EUR)', 'Kommentar'],
        ['Kontostand(e) alle Geschaeftskonten', '________', 'Alle Konten addieren'],
        ['Bargeld (alle Kassen)', '________', 'Zahlen, nicht schaetzen!'],
        ['Forderungen faellig < 14 Tage', '________', 'Nur wenn sicher eingehend'],
        ['SUMME VERFUEGBAR', '________', 'A + B + C'],
        ['Miete(n) nächster Monat', '________', 'Alle Filialen'],
        ['Personalkosten nächster Monat', '________', 'Brutto + SV-Arbeitgeberanteil'],
        ['Wareneinkauf nächste 4 Wochen', '________', 'lt. Bestellplan'],
        ['Fällige Lieferantenrechnungen', '________', 'Überfällig zählt doppelt!'],
        ['Steuern/SV fällig nächste 4 Wochen', '________', 'USt, LSt, SV'],
        ['SUMME PFLICHTZAHLUNGEN', '________', 'E + F + G + H + I'],
        ['NETTO-LIQUIDITAT (A-E)', '________', 'Wenn negativ: SOFORT Anwalt!'],
        ['REICHWEITE (Tage)', '________', 'Verfuegbar / (Pflichtzahlungen/30)'],
    ]
    kasse_tbl = Table(kasse_data, colWidths=[7.5*cm, 3.5*cm, 5.5*cm])
    kasse_style = tbl_style_standard()
    kasse_style.add('BACKGROUND', (0,11),(2,12), colors.HexColor('#FFE8E8'))
    kasse_style.add('FONTNAME', (0,11),(0,12), 'Helvetica-Bold')
    kasse_tbl.setStyle(kasse_style)
    story.append(kasse_tbl)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("SCHRITT 2: Ampel-Check — Wann muss ich handeln?", S['h2']))
    ampel_data = [
        ['Ampel', 'Kriterium', 'Was tun?'],
        ['GRUEN', 'Reichweite > 60 Tage, keine Rückstände', 'Weiter monatlich prüfen'],
        ['GELB', 'Reichweite 30-60 Tage ODER ein Rückstand', 'Steuerberater informieren, Kosten senken'],
        ['ROT', 'Reichweite < 30 Tage ODER mehrere Rückstände', 'SOFORT Rechtsanwalt! § 15a InsO prüfen!'],
        ['SCHWARZ', 'Kein Geld für Löhne ODER Insolvenzantragspflicht', 'Insolvenzantrag innerhalb 3 Wochen!'],
    ]
    ampel_tbl = Table(ampel_data, colWidths=[2.2*cm, 8*cm, 6.3*cm])
    ampel_style = tbl_style_standard()
    ampel_style.add('BACKGROUND', (0,1),(0,1), colors.HexColor('#90EE90'))
    ampel_style.add('BACKGROUND', (0,2),(0,2), colors.HexColor('#FFD700'))
    ampel_style.add('BACKGROUND', (0,3),(0,3), colors.HexColor('#FF6B6B'))
    ampel_style.add('BACKGROUND', (0,4),(0,4), colors.HexColor('#333333'))
    ampel_style.add('TEXTCOLOR', (0,4),(0,4), colors.white)
    ampel_style.add('FONTNAME', (0,1),(-1,4), 'Helvetica-Bold')
    ampel_tbl.setStyle(ampel_style)
    story.append(ampel_tbl)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("SCHRITT 3: 24-Monats-Vorausschau (vereinfacht)", S['h2']))
    story.append(Paragraph(
        "Tragen Sie fuer jeden der naechsten 24 Monate ein: "
        "erwartete Einnahmen, geplante Ausgaben, Differenz. "
        "Wenn in einem der 24 Monate die Differenz dauerhaft negativ ist, "
        "liegt 'drohende Zahlungsunfaehigkeit' im Sinne des § 18 InsO vor — "
        "und Sie duerfen (nicht müssen) bereits jetzt einen StaRUG-Plan einleiten.",
        S['body']))

    monate_headers = ['Monat', 'Einnahmen (EUR)', 'Ausgaben (EUR)', 'Saldo (EUR)', 'Ampel']
    monate_rows = [monate_headers]
    for i in range(1, 25):
        monate_rows.append([f'M+{i:02d}', '________', '________', '________', '○'])
    monate_tbl = Table(monate_rows, colWidths=[2.0*cm, 3.5*cm, 3.5*cm, 3.5*cm, 2.0*cm])
    monate_style = tbl_style_standard()
    monate_style.add('FONTSIZE', (0,0),(-1,-1), 8)
    monate_style.add('LEADING', (0,0),(-1,-1), 10)
    monate_tbl.setStyle(monate_style)
    story.append(monate_tbl)
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "<i>Hinweis: Dieses vereinfachte Sheet ersetzt KEINE Fortbestehensprognose "
        "nach IDW S 11. Es dient der eigenen Ersteinschätzung. "
        "Lassen Sie die Prognose von einem Steuerberater oder Rechtsanwalt prüfen.</i>",
        S['small']))
    story.append(PageBreak())


def build_vorlagen_annex(story):
    """Vorlagen-Annex — gemeinsam für alle Varianten (~15 Seiten)"""
    story.append(Paragraph("VORLAGEN-ANNEX", S['h_kapitel']))
    story.append(Paragraph("Gemeinsame Vorlagen für alle vier Varianten", S['subtitle_cap']))
    story.append(hr(DUNKELBLAU, thickness=2))
    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph(
        "Die nachfolgenden Vorlagen sind praxiserprobte Muster für die Krisenfrüherkennung "
        "und das Krisenmanagement nach § 1 StaRUG. Sie sind nicht mandantenbezogen "
        "und können nach Anpassung auf den Einzelfall verwendet werden.",
        S['body']))
    story.append(PageBreak())

    # ─── A.1 § 102 StaRUG-Standardwarnschreiben ──────────────────────────────
    story.append(Paragraph("Anlage V-1: § 102 StaRUG-Standardwarnschreiben (Volltext)", S['h1']))
    story.append(hr(DUNKELBLAU))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Dieses Muster richtet sich an Berater (Rechtsanwaelte, Steuerberater, Wirtschaftsprüfer), "
        "die im Rahmen ihrer Beratung Krisenzeichen feststellen und nach § 102 StaRUG zur "
        "unverzüglichen Information des Geschäftsleitungsorgans verpflichtet sind.",
        S['body']))
    story.append(Spacer(1, 0.3*cm))

    story.append(kanzlei_kopf_rw())
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("[Kanzlei-Briefkopf]", S['center']))
    story.append(Spacer(1, 0.2*cm))

    az_block = [
        ["An:", "[Unternehmen], vertreten durch die Geschäftsführung"],
        ["", "[Anschrift]"],
        ["Von:", "[Beraterkanzlei / Steuerberaterbüro / WP-Kanzlei]"],
        ["Datum:", "[Datum]"],
        ["Betreff:", "Gesetzliche Warnanzeige gemäß § 102 StaRUG — VERTRAULICH"],
        ["Aktenzeichen:", "[Kanzlei-AZ]"],
    ]
    for row in az_block:
        az_tbl = Table([row], colWidths=[3*cm, 13.5*cm])
        az_tbl.setStyle(TableStyle([
            ('FONTNAME',(0,0),(0,0),'Helvetica-Bold'),
            ('FONTNAME',(1,0),(1,0),'Helvetica'),
            ('FONTSIZE',(0,0),(-1,-1),9),
            ('BOTTOMPADDING',(0,0),(-1,-1),2),
            ('TOPPADDING',(0,0),(-1,-1),2),
        ]))
        story.append(az_tbl)
    story.append(Spacer(1, 0.3*cm))
    story.append(HRFlowable(width='100%', thickness=0.5, color=GRAU_MID))
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("Sehr geehrte Damen und Herren,", S['body_left']))
    story.append(Spacer(1, 0.1*cm))

    warn_paragraphen = [
        ("I. Rechtsgrundlage und Anlass", (
            "Im Rahmen unserer Beratungstätigkeit für Ihr Unternehmen haben wir Kenntnis von "
            "Tatsachen erlangt, die nach unserer Einschätzung auf bestandsgefährdende "
            "Entwicklungen im Sinne des § 1 Abs. 1 Satz 3 des Gesetzes über den "
            "Stabilisierungs- und Restrukturierungsrahmen für Unternehmen (StaRUG) hindeuten. "
            "Wir sind daher verpflichtet, Sie gemäß § 102 Abs. 1 StaRUG unverzüglich und "
            "schriftlich zu informieren."
        )),
        ("II. Festgestellte Risikoindikatoren", (
            "Im Einzelnen haben wir folgende Risikofaktoren festgestellt, die im Zusammenhang "
            "mit der Pflicht zur Krisenfrüherkennung und zum Krisenmanagement nach § 1 StaRUG "
            "relevant sind: [HIER: konkrete Risikofaktoren eintragen — z.B. negative "
            "Liquiditätsentwicklung, Covenant-Bruch, Verlustanzeige § 92 AktG / § 49 Abs. 3 GmbHG, "
            "drohende Zahlungsunfähigkeit § 18 InsO, unzureichender 24-Monats-Planungshorizont etc.]"
        )),
        ("III. Ihre Pflichten nach § 1 StaRUG", (
            "Als Mitglied der Geschäftsleitung sind Sie nach § 1 Abs. 1 StaRUG verpflichtet, "
            "fortlaufend über Entwicklungen zu wachen, welche den Fortbestand des Unternehmens "
            "gefährden können. Dies umfasst insbesondere: (1) die Einrichtung eines angemessenen "
            "Risikofrüherkennungssystems, (2) die Aufstellung und laufende Aktualisierung eines "
            "Liquiditätsplans für einen Zeitraum von mindestens 24 Monaten, (3) die Einleitung "
            "geeigneter Gegenmaßnahmen bei Feststellung bestandsgefährdender Entwicklungen sowie "
            "(4) die frühzeitige Einbeziehung von Sanierungsberatern, Gläubigern und ggf. des "
            "Aufsichtsrats. Ein Verstoß gegen § 1 StaRUG kann zu einer Haftung nach § 43 Abs. 2 "
            "GmbHG bzw. § 93 AktG führen."
        )),
        ("IV. Erforderliche Maßnahmen", (
            "Wir empfehlen dringend, folgende Maßnahmen unverzüglich einzuleiten: "
            "[HIER: konkrete Handlungsempfehlungen eintragen — z.B. Erstellung 13-Wochen-Plan, "
            "Bankenrunde einberufen, StaRUG-Berater mandatieren, Sanierungsgutachten beauftragen, "
            "Anzeige Restrukturierungssache § 31 StaRUG etc.]. "
            "Wir stehen Ihnen für die Umsetzung dieser Maßnahmen zur Verfügung."
        )),
        ("V. Haftungshinweis und Vertraulichkeit", (
            "Dieses Schreiben erfolgt im Rahmen unserer gesetzlichen Pflicht nach § 102 Abs. 1 StaRUG. "
            "Es entbindet Sie nicht von eigenen Handlungspflichten. Bitte bestätigen Sie den Erhalt "
            "dieses Schreibens schriftlich. Dieses Schreiben ist vertraulich und ausschließlich für "
            "die Mitglieder der Geschäftsleitung und ggf. des Aufsichtsrats bestimmt."
        )),
    ]
    for titel, text in warn_paragraphen:
        story.append(Paragraph(f"<b>{titel}</b>", S['h3']))
        story.append(Paragraph(text, S['body']))
        story.append(Spacer(1, 0.2*cm))

    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph("[Ort], [Datum]", S['right']))
    story.append(Spacer(1, 0.6*cm))
    story.append(Paragraph(
        "[Unterschrift Berater / Kanzleistempel]",
        ParagraphStyle('sig_template', fontName='Times-Italic', fontSize=11,
                       alignment=TA_RIGHT, textColor=DUNKELBLAU)
    ))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph(
        "<b>Empfangsbestatigung:</b><br/>"
        "Ich/Wir bestätigen den Empfang dieses Schreibens am __________________ .<br/><br/>"
        "Unterschrift Geschaeftsfuehrung: ___________________________________<br/><br/>"
        "Name in Druckbuchstaben: ___________________________________________",
        ParagraphStyle('empfangsbestaetigung', fontName='Helvetica', fontSize=9,
                       leading=16, borderPad=8, borderWidth=1, borderColor=GRAU_MID,
                       borderRadius=3, backColor=GRAU_HELL)
    ))
    story.append(PageBreak())

    # ─── A.2 24-Monats-Liquiplan-Master-Template ──────────────────────────────
    story.append(Paragraph("Anlage V-2: 24-Monats-Liquiditaetsplan — Master-Template", S['h1']))
    story.append(hr(DUNKELBLAU))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Dieses Template entspricht dem Standard nach § 1 StaRUG / IDW S 11 / IDW S 19. "
        "Es ist als Grundgerüst zu verstehen und muss auf den Einzelfall angepasst werden. "
        "Die erste Zeile entspricht dem Startmonat (M+0 = Aufstellungsdatum).",
        S['body']))
    story.append(Spacer(1, 0.2*cm))

    # Wochenbasis W1-W13
    story.append(Paragraph("<b>Teil A: Wochenbasis (W1-W13)</b>", S['h3']))
    wochen_cols = ['Position', 'W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W08', 'W09', 'W10', 'W11', 'W12', 'W13']
    wochen_rows_data = [
        ['EINZAHLUNGEN', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['Umsatzerlöse', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['Forderungseinzüge', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['Sonstige Einzahlungen', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['SUMME EINZAHLUNGEN (A)', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['AUSZAHLUNGEN', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['Lohn/Gehalt + SV-AG', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['Miete / Nebenkosten', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['Wareneinsatz', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['Energie/Versorgung', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['Zinsen/Tilgung Darlehen', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['Steuern + SV-AN', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['Investitionen/Capex', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['Sonstige Auszahlungen', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['SUMME AUSZAHLUNGEN (B)', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['NETTO CASHFLOW (A-B)', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['KASSENBESTAND ANFANG', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['KASSENBESTAND ENDE', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['MINDESTLIQUIDITAET', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['AMPEL', '○', '○', '○', '○', '○', '○', '○', '○', '○', '○', '○', '○', '○'],
    ]
    col_w = [3.8*cm] + [0.9*cm]*13
    w_tbl = Table([wochen_cols] + wochen_rows_data, colWidths=col_w)
    w_style = tbl_style_zahlen()
    w_style.add('FONTNAME', (0,0),(-1,0), 'Helvetica-Bold')
    w_style.add('FONTSIZE', (0,0),(-1,-1), 7)
    w_style.add('BACKGROUND', (0,0),(0,0), DUNKELBLAU)
    w_style.add('TEXTCOLOR', (0,0),(0,0), colors.white)
    for i in [1,6]:
        w_style.add('BACKGROUND', (0,i),(13,i), colors.HexColor('#E8EFF8'))
        w_style.add('FONTNAME', (0,i),(0,i), 'Helvetica-Bold')
    for i in [5,11,16,17,19]:
        w_style.add('FONTNAME', (0,i),(0,i), 'Helvetica-Bold')
    w_tbl.setStyle(w_style)
    story.append(w_tbl)
    story.append(Spacer(1, 0.4*cm))

    # Monatsbasis M4-M24
    story.append(Paragraph("<b>Teil B: Monatsbasis (M4-M24)</b>", S['h3']))
    mon_cols = ['Position', 'M04', 'M05', 'M06', 'M07', 'M08', 'M09', 'M10', 'M11', 'M12']
    mon_rows_data = [
        ['EINZAHLUNGEN', '', '', '', '', '', '', '', '', ''],
        ['Umsatzerlöse', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['Forderungseinzüge', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['Sonstige', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['SUMME EIN (A)', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['AUSZAHLUNGEN', '', '', '', '', '', '', '', '', ''],
        ['Personal + SV', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['Miete', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['Wareneinsatz', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['Energie', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['Schuldenservice', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['Steuern/SV', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['Sonstige', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['SUMME AUS (B)', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['NETTO CF (A-B)', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['KASSENBESTAND', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['SZENARIO', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ]
    col_w2 = [3.0*cm] + [1.15*cm]*9
    m_tbl = Table([mon_cols] + mon_rows_data, colWidths=col_w2)
    m_style = tbl_style_zahlen()
    m_style.add('FONTSIZE', (0,0),(-1,-1), 8)
    m_tbl.setStyle(m_style)
    story.append(m_tbl)
    story.append(Spacer(1, 0.2*cm))

    mon_cols2 = ['Position', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24']
    mon_rows2 = [
        ['SUMME EIN (A)', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['SUMME AUS (B)', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['NETTO CF (A-B)', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['KASSENBESTAND', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['SZENARIO', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ]
    col_w3 = [3.0*cm] + [1.0*cm]*12
    m2_tbl = Table([mon_cols2] + mon_rows2, colWidths=col_w3)
    m2_style = tbl_style_zahlen()
    m2_style.add('FONTSIZE', (0,0),(-1,-1), 8)
    m2_tbl.setStyle(m2_style)
    story.append(m2_tbl)
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Szenario-Codes: B = Base Case | S = Stress (z.B. -20% Umsatz) | SS = Severe Stress (z.B. -40%) | "
        "Mindestliquiditaet: branchenüblich 2-4 Wochen Fixkosten als Reserve",
        S['small']))
    story.append(PageBreak())

    # ─── A.3 Geschäftsführer-Krisenprotokoll ──────────────────────────────────
    story.append(Paragraph("Anlage V-3: Geschaeftsfuehrer-Krisenprotokoll (Vorlage)", S['h1']))
    story.append(hr(DUNKELBLAU))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Das Krisenprotokoll dokumentiert, wann der Geschaeftsfuehrer von bestandsgefährdenden "
        "Entwicklungen Kenntnis erlangt hat und welche Massnahmen er eingeleitet hat. "
        "Es dient dem Nachweis pflichtgemaeßen Handelns (§ 1 StaRUG, § 43 GmbHG, § 93 AktG) "
        "und sollte monatlich oder bei wesentlichen Veraenderungen ausgefüllt werden.",
        S['body']))
    story.append(Spacer(1, 0.2*cm))

    krisen_proto = [
        ['Eintrag Nr.', '[fortlaufend]'],
        ['Datum / Uhrzeit', '______________________'],
        ['Verfasser (GF/Vorstand)', '______________________'],
        ['Anwesende', '______________________'],
        ['Auslösendes Ereignis', '______________________'],
        ['Beschreibung der Risikolage', '[detaillierte Beschreibung, quantifiziert]'],
        ['Liquiditätsreserve Stand heute', 'EUR __________ (Reichweite __ Tage)'],
        ['Eingeleitete Massnahmen', '[Liste der Maßnahmen mit Verantwortlichen und Fristen]'],
        ['Externe Berater informiert', '□ RA  □ StB  □ WP  □ Sanierungsberater  □ Banken'],
        ['Nächster Review-Termin', '______________________'],
        ['Unterschrift GF', '______________________'],
        ['Unterschrift weiterer GF (falls vorhanden)', '______________________'],
    ]
    krisen_tbl = Table(krisen_proto, colWidths=[5*cm, 11.5*cm])
    krisen_style = tbl_style_standard()
    krisen_style.add('FONTNAME', (0,0),(0,-1), 'Helvetica-Bold')
    krisen_tbl.setStyle(krisen_style)
    story.append(krisen_tbl)
    story.append(PageBreak())

    # ─── A.4 Frühwarn-KPI-Schwellen-Tabelle ──────────────────────────────────
    story.append(Paragraph("Anlage V-4: Fruehwarn-KPI-Schwellen-Tabelle", S['h1']))
    story.append(hr(DUNKELBLAU))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Die nachstehende Tabelle gibt Richtwerte für Fruehwarnindikatoren an. "
        "Die Schwellenwerte sind Orientierungswerte — massgeblich ist stets die Gesamtschau. "
        "Einzel-KPIs sind kein Automatismus für eine Insolvenzantragspflicht.",
        S['body']))
    story.append(Spacer(1, 0.2*cm))

    kpi_data = [
        ['KPI', 'Einheit', 'Gruen\n(kein akuter Bedarf)', 'Gelb\n(Monitoring)', 'Rot\n(Handlungsbedarf)', 'Schwarz\n(Insolvenz)'],
        ['Liquiditaetsreichweite', 'Tage', '> 60', '30-60', '14-30', '< 14'],
        ['13-Wochen-Cash-Coverage', 'Ratio', '> 1,3', '1,0-1,3', '0,8-1,0', '< 0,8'],
        ['Eigenkapitalquote', '% Bilanzsumme', '> 20%', '10-20%', '5-10%', '< 5% / negativ'],
        ['EBITDA-Marge', '% Umsatz', '> 8%', '3-8%', '0-3%', 'negativ'],
        ['Schuldendienstdeckung (DSCR)', 'Ratio', '> 1,5', '1,2-1,5', '1,0-1,2', '< 1,0'],
        ['Nettoverschuldung / EBITDA', 'x EBITDA', '< 3x', '3-5x', '5-7x', '> 7x'],
        ['Verbindlichkeiten ü. 90 Tage fällig', '% Gesamt-VB', '< 5%', '5-15%', '15-30%', '> 30%'],
        ['Umsatzrückgang gg. Vorjahr', '% p.a.', '< 5%', '5-15%', '15-30%', '> 30%'],
        ['Covenant-Abstand (Leverage)', 'Headroom gg. Test', '> 30%', '15-30%', '5-15%', '< 5% / verletzt'],
        ['Anlagendeckungsgrad I', 'EK / AV', '> 100%', '80-100%', '60-80%', '< 60%'],
        ['Working Capital Ratio', 'UV / kurzfr. VB', '> 1,5', '1,2-1,5', '1,0-1,2', '< 1,0'],
        ['Banken-Ampel (intern)', 'Rating-Klasse', 'Normal', 'Watch List', 'Intensiv-/Sanierung', 'Abbau / Workout'],
        ['Lieferantenrückstände', 'EUR o. Tage', '0 / 0', 'gering / < 30T', 'erheblich / 30-60T', 'Lieferstopp'],
        ['Personalfluktuation Mgmt.', '% p.a.', '< 10%', '10-20%', '20-30%', '> 30%'],
    ]
    kpi_tbl = Table(kpi_data, colWidths=[4.5*cm, 1.8*cm, 2.4*cm, 2.4*cm, 2.4*cm, 2.4*cm])
    kpi_style = tbl_style_standard()
    kpi_style.add('FONTSIZE', (0,0),(-1,-1), 8)
    kpi_style.add('LEADING', (0,0),(-1,-1), 10)
    kpi_style.add('BACKGROUND', (2,1),(2,-1), colors.HexColor('#CCFFCC'))
    kpi_style.add('BACKGROUND', (3,1),(3,-1), colors.HexColor('#FFFFAA'))
    kpi_style.add('BACKGROUND', (4,1),(4,-1), colors.HexColor('#FFCCCC'))
    kpi_style.add('BACKGROUND', (5,1),(5,-1), colors.HexColor('#FF8888'))
    kpi_style.add('FONTNAME', (0,0),(-1,0), 'Helvetica-Bold')
    kpi_style.add('FONTNAME', (0,0),(0,-1), 'Helvetica-Bold')
    kpi_tbl.setStyle(kpi_style)
    story.append(kpi_tbl)
    story.append(PageBreak())

    # ─── A.5 Restrukturierungsplan-Inhaltsverzeichnis-Master ─────────────────
    story.append(Paragraph("Anlage V-5: Restrukturierungsplan — Inhaltsverzeichnis-Master", S['h1']))
    story.append(hr(DUNKELBLAU))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Mustergliederung nach §§ 5 ff. StaRUG. Der Restrukturierungsplan besteht zwingend "
        "aus einem darstellenden Teil (§ 6 StaRUG) und einem gestaltenden Teil (§ 7 StaRUG). "
        "Die Reihenfolge ist nicht zwingend; die Nummerierung dient der Übersicht.",
        S['body']))
    story.append(Spacer(1, 0.2*cm))

    itv_data = [
        ['Nr.', 'Gliederungspunkt', 'Rechtsgrundlage', 'Hinweise'],
        ['I.', 'DARSTELLENDER TEIL', '§ 6 StaRUG', ''],
        ['1.', 'Unternehmensbeschreibung und Geschäftsmodell', '§ 6 Abs. 1 Nr. 1', 'Rechtsform, Organe, Standorte, Produkte'],
        ['2.', 'Krisenursachen und Krisendiagnose', '§ 6 Abs. 1 Nr. 1', 'Abgrenzung Struktur-/Rentabilitäts-/Liquiditätskrise'],
        ['3.', 'Finanzielle und wirtschaftliche Lage', '§ 6 Abs. 1 Nr. 1', 'Bilanzen, GuV, Cashflow, Verbindlichkeiten'],
        ['4.', 'Fortbestehensprognose (24 Monate)', '§ 6 Abs. 1 Nr. 1; IDW S 11', 'Zahlungsfähigkeit im Planungszeitraum'],
        ['5.', 'Gläubigergruppen und Klassenbildung', '§§ 9 f. StaRUG', 'Mindestens gleich- + bestvorrangige Gruppe'],
        ['6.', 'Vergleichsrechnung / Liquidationswert', '§ 6 Abs. 2 StaRUG', 'Verbesserung ggü. Insolvenz nachweisen'],
        ['7.', 'Restrukturierungsmaßnahmen im Überblick', '§ 6 Abs. 1 Nr. 2', 'Operative + finanzielle Sanierungsbausteine'],
        ['8.', 'Planumsetzungsrisiken', '§ 6 Abs. 1 Nr. 3', 'Risikomatrix, Sensitivitätsanalyse'],
        ['II.', 'GESTALTENDER TEIL', '§ 7 StaRUG', ''],
        ['9.', 'Forderungseingriffe je Gruppe', '§ 7 Abs. 1 StaRUG', 'Stundung, Teilerlass, Umtausch, Sicherheitenregelung'],
        ['10.', 'Gruppenbildung und Stimmrechte', '§§ 9, 24 StaRUG', 'Gleichartige Rechtsstellung, keine Willkür'],
        ['11.', 'Cross-Class-Cram-Down (falls geplant)', '§ 26 StaRUG', 'Mehrheitlicher Anforderungstest, Schlechterstellungsverbot'],
        ['12.', 'Kapitalmaßnahmen (falls geplant)', '§ 7 Abs. 4 StaRUG', 'Kapitalherabsetzung/-erhöhung, Debt-to-Equity'],
        ['13.', 'Bedingungen der Planwirksamkeit', '§ 67 StaRUG', 'Vollzugsbedingungen, Long-Stop-Date'],
        ['III.', 'ANLAGEN', '', ''],
        ['14.', 'Sanierungsgutachten (IDW S 6)', '', 'Kurzgutachten oder Vollgutachten'],
        ['15.', 'Liquiditaetsplan 24 Monate', '', 'Base + Stress-Szenarien'],
        ['16.', 'Vertragsänderungen / Term Sheets', '', 'Bankvereinbarungen, Anleiheänderungen'],
        ['17.', 'Stimmrechtssimulation', '', 'Je Gruppe: Ja/Nein/Enthaltung'],
        ['18.', 'Zertifikat des Restrukturierungsbeauftragten', '§ 76 Abs. 4 StaRUG', 'Falls bestellt'],
    ]
    itv_tbl = Table(itv_data, colWidths=[1.0*cm, 6.5*cm, 4.5*cm, 4.5*cm])
    itv_style = tbl_style_standard()
    itv_style.add('FONTSIZE', (0,0),(-1,-1), 8)
    itv_style.add('FONTNAME', (0,0),(-1,0), 'Helvetica-Bold')
    for i in [1,10,13]:
        itv_style.add('BACKGROUND', (0,i),(-1,i), colors.HexColor('#D6E4F0'))
        itv_style.add('FONTNAME', (0,i),(-1,i), 'Helvetica-Bold')
    itv_tbl.setStyle(itv_style)
    story.append(itv_tbl)
    story.append(PageBreak())


def build_foliensatz(story):
    """Foliensatz 'Restructuring Lounge Impulsvortrag' — 8 Folien"""

    def folie(story, nr, titel, inhalt_func):
        """Rendert eine einzelne Folie als hochformatige Seite mit dickem Rahmen."""
        story.append(Spacer(1, 0.3*cm))
        # Rahmen via Tabelle
        content_parts = []
        # Folien-Header
        header_data = [[
            Paragraph(
                f"RESTRUCTURING LOUNGE HAMBURG — WAYES — 28. Mai 2026",
                ParagraphStyle('folie_header_top', fontName='Helvetica', fontSize=7,
                               textColor=colors.HexColor('#888888'), alignment=TA_LEFT)
            ),
            Paragraph(
                f"Folie {nr}/8",
                ParagraphStyle('folie_nr', fontName='Helvetica-Bold', fontSize=8,
                               textColor=DUNKELBLAU, alignment=TA_RIGHT)
            )
        ]]
        hdr_tbl = Table(header_data, colWidths=[10*cm, 6*cm])
        hdr_tbl.setStyle(TableStyle([
            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
            ('BOTTOMPADDING',(0,0),(-1,-1),4),
        ]))
        content_parts.append(hdr_tbl)
        content_parts.append(HRFlowable(width='100%', thickness=2, color=DUNKELBLAU, spaceAfter=8))
        content_parts.append(Paragraph(titel, ParagraphStyle(
            'folie_titel', fontName='Helvetica-Bold', fontSize=16,
            textColor=DUNKELBLAU, leading=20, spaceAfter=12, alignment=TA_LEFT
        )))
        content_parts.append(HRFlowable(width='100%', thickness=0.5, color=GRAU_MID, spaceAfter=10))
        inhalt_func(content_parts)
        content_parts.append(Spacer(1, 0.3*cm))
        content_parts.append(HRFlowable(width='100%', thickness=1, color=DUNKELBLAU, spaceBefore=6))
        content_parts.append(Paragraph(
            "Dr. Tjark Reher-Bornholmsen  |  Reher Wennstedt Restrukturierung Partnerschaft mbB  |  Hamburg",
            ParagraphStyle('folie_footer', fontName='Helvetica', fontSize=7,
                           textColor=GRAU_DUNKEL, alignment=TA_CENTER, spaceBefore=4)
        ))

        outer_data = [[content_parts]]
        outer_tbl = Table(outer_data, colWidths=[16.5*cm])
        outer_tbl.setStyle(TableStyle([
            ('BOX', (0,0),(0,0), 3, DUNKELBLAU),
            ('PADDING', (0,0),(0,0), 14),
            ('VALIGN', (0,0),(0,0), 'TOP'),
            ('BACKGROUND', (0,0),(0,0), colors.white),
        ]))
        story.append(outer_tbl)
        story.append(PageBreak())

    S_folie_body = ParagraphStyle('fbody', fontName='Helvetica', fontSize=11,
                                   leading=17, textColor=TEXT_SCHWARZ, spaceAfter=6)
    S_folie_bullet = ParagraphStyle('fbullet', fontName='Helvetica', fontSize=11,
                                    leading=17, textColor=TEXT_SCHWARZ, leftIndent=20, spaceAfter=4)
    S_folie_bold = ParagraphStyle('fbold', fontName='Helvetica-Bold', fontSize=12,
                                   leading=18, textColor=DUNKELBLAU, spaceAfter=8)
    S_folie_big = ParagraphStyle('fbig', fontName='Helvetica-Bold', fontSize=22,
                                  leading=28, textColor=ROT, alignment=TA_CENTER, spaceAfter=10)
    S_folie_zitat = ParagraphStyle('fzitat', fontName='Times-Italic', fontSize=13,
                                    leading=20, textColor=DUNKELBLAU, alignment=TA_CENTER,
                                    spaceAfter=10, spaceBefore=10)

    # Folie 1 — Hook
    def f1(parts):
        parts.append(Paragraph(
            '"Ich dachte, § 1 StaRUG gilt nur für große Konzerne."',
            S_folie_zitat))
        parts.append(Paragraph(
            "— Tarek-Yusuf Çelebi-Drebenstedt, Geschäftsführer Salaltbar UG (haftungsbeschränkt), "
            "Berlin-Neukölln, 14 Mitarbeiter, Stammkapital EUR 1,00 — Drei-Wochen-Frist läuft.",
            ParagraphStyle('fq2', fontName='Helvetica', fontSize=9, textColor=GRAU_DUNKEL,
                           alignment=TA_CENTER, spaceAfter=12)))
        parts.append(HRFlowable(width='100%', thickness=0.5, color=GRAU_MID))
        parts.append(Spacer(1, 0.3*cm))
        parts.append(Paragraph("<b>§ 1 StaRUG gilt für JEDEN Geschäftsführer.</b>", S_folie_bold))
        parts.append(Paragraph(
            "Unabhaengig von: Unternehmensgröße | Rechtsform | Börsennotierung | "
            "Anzahl Mitarbeiter | Umsatzhöhe | Eigenkapitalausstattung",
            S_folie_body))
        parts.append(Spacer(1, 0.2*cm))
        parts.append(Paragraph(
            "Heute: Vier Faelle — ein Gesetz — vier Lehren.",
            S_folie_big))

    folie(story, 1, "Hook: § 1 StaRUG — Das Gesetz, das alle vergessen", f1)

    # Folie 2 — 24-Monats-These
    def f2(parts):
        parts.append(Paragraph(
            "Der neue Standard: 24 Monate Planungshorizont",
            S_folie_bold))
        items_f2 = [
            "FRÜHER: Quartalsbericht + Jahresabschluss = ausreichend",
            "HEUTE (seit StaRUG 2021): 24-Monats-Liquiditätsplan ist Pflicht (§ 1 Abs. 1 StaRUG)",
            "12 Monate: nur noch für Fortbestehensprognose (IDW S 11) — NICHT ausreichend für § 1 StaRUG",
            "24-Monats-Plan muss: rollierend / mindestens quartalsweise aktualisiert / plausibilisiert sein",
            "Wer keinen 24-Monats-Plan hat: verletzt bereits JETZT § 1 StaRUG",
        ]
        for i, itm in enumerate(items_f2, 1):
            parts.append(Paragraph(f"{i}.  {itm}", S_folie_bullet))
        parts.append(Spacer(1, 0.3*cm))
        tbl_f2_data = [
            ['Zeitraum', 'Standard', 'Instrument'],
            ['W01-W13 (wochenweise)', 'Minimum bei Krise', '13-Wochen-Liquiditaetsplan'],
            ['M01-M12', 'Fortbestehensprognose', 'IDW S 11 (kurzfristig)'],
            ['M01-M24', 'StaRUG-Standard (§ 1)', '24-Monats-Liquiditaetsplan'],
            ['M01-M60', 'Strategische Planung', 'Businessplan / LRP'],
        ]
        tbl_f2 = Table(tbl_f2_data, colWidths=[4*cm, 5*cm, 7*cm])
        tbl_f2.setStyle(tbl_style_standard())
        parts.append(tbl_f2)

    folie(story, 2, "These: 24 Monate sind der neue Standard", f2)

    # Folie 3 — § 102-Warnpflicht
    def f3(parts):
        parts.append(Paragraph(
            "§ 102 StaRUG: Die stille Revolution im Beraterrecht",
            S_folie_bold))
        parts.append(Paragraph(
            "<b>§ 102 Abs. 1 StaRUG:</b> Berater (Rechtsanwälte, Steuerberater, Wirtschaftsprüfer), "
            "die im Rahmen ihrer Tätigkeit Kenntnis von bestandsgefährdenden Entwicklungen erlangen, "
            "haben die Geschäftsleitung unverzüglich zu informieren.",
            S_folie_body))
        parts.append(Spacer(1, 0.2*cm))
        items_f3 = [
            "PFLICHT — keine Option, kein Ermessen",
            "Unverzüglich = ohne schuldhaftes Zögern (i.d.R. innerhalb weniger Tage)",
            "Schriftlich empfohlen (Beweissicherung!)",
            "Keine Ausnahme für langjährige Mandatsbeziehung",
            "Haftungsrisiko des Beraters bei Verstoß (§ 280 BGB / berufsrechtlich)",
            "PRAXIS: § 102-Schreiben in jede Krisenberatung einbauen — IMMER",
        ]
        for i, itm in enumerate(items_f3, 1):
            parts.append(Paragraph(f"→  {itm}", S_folie_bullet))
        parts.append(Spacer(1, 0.3*cm))
        warn_box_data = [[Paragraph(
            "<b>PRAXIS-TIPP Reher Wennstedt:</b> § 102-Schreiben raus, Empfangsbestaetigung einholen, "
            "zu den Handakten. Wer das nicht macht, haftet neben dem Mandanten.",
            ParagraphStyle('warn_folie', fontName='Helvetica', fontSize=10, textColor=ROT,
                           leading=14))]]
        warn_box = Table(warn_box_data, colWidths=[14*cm])
        warn_box.setStyle(TableStyle([
            ('BOX',(0,0),(0,0),2,ROT),
            ('BACKGROUND',(0,0),(0,0),colors.HexColor('#FFF0F0')),
            ('PADDING',(0,0),(0,0),8),
        ]))
        parts.append(warn_box)

    folie(story, 3, "§ 102 StaRUG: Warnpflicht des Beraters — unterschaetzt und gefaehrlich", f3)

    # Folie 4 — Fallvignette A
    def f4(parts):
        parts.append(Paragraph(
            "Fall A: VEYRA AI Foundation gGmbH — KI-gGmbH in der Spendenkrise",
            S_folie_bold))
        vigA = [
            ['Rechtsform', 'gGmbH (gemeinnützig)'],
            ['Problem', 'EU-Förderauszahlung 9 Monate verzögert / Spenden -40%'],
            ['Aktenzeichen', 'AG Frankfurt 810 RES 14/26'],
            ['StaRUG-Instrument', 'Anzeige Restrukturierungssache § 31; Stundungsplan'],
            ['Lektion', '§ 1 StaRUG gilt auch für gGmbH-Geschaeftsfuehrerinnen!'],
            ['Zitat GF', '"Brauche STAB-Anordnung VOR Q3-Foerderbescheid"'],
        ]
        vig_tbl = Table(vigA, colWidths=[4.5*cm, 11.5*cm])
        vig_tbl.setStyle(tbl_style_standard())
        parts.append(vig_tbl)
        parts.append(Spacer(1, 0.2*cm))
        parts.append(Paragraph(
            "Takeaway: Kein Umsatz, kein Gewinn, keine Aktionäre schützt nicht vor § 1 StaRUG. "
            "Drohende Zahlungsunfähigkeit in Monat 17 verpflichtet zur Krisenfrüherkennung ab Tag 1.",
            S_folie_body))

    folie(story, 4, "Fall A: KI-gGmbH — Common Sense trifft Krisenrecht", f4)

    # Folie 5 — Fallvignette B
    def f5(parts):
        parts.append(Paragraph(
            "Fall B: HERRENBLUSE & ZWIRN HARTMANNSCHMIDT AG — Anleihe-Deadline",
            S_folie_bold))
        vigB = [
            ['Rechtsform', 'AG (börsennotiert, Open Market)'],
            ['Problem', 'EUR 65 Mio. Anleihe in 18 Monaten fällig, Covenant-Bruch'],
            ['Aktenzeichen', 'AG Bamberg 53 RES 7/26'],
            ['StaRUG-Instrument', 'Cross-Class-Cram-Down § 26 StaRUG (Anleihe-Restrukturierung)'],
            ['Lektion', 'IDW S 6 + IDW S 11 zusammen: zwei verschiedene Standards!'],
            ['Stolperstein', 'Familien-Anker + Schlechterstellungsverbot §§ 64, 27 StaRUG'],
        ]
        vig_tbl = Table(vigB, colWidths=[4.5*cm, 11.5*cm])
        vig_tbl.setStyle(tbl_style_standard())
        parts.append(vig_tbl)
        parts.append(Spacer(1, 0.2*cm))
        parts.append(Paragraph(
            "Takeaway: 18 Monate klingt lang. In der Anleihe-Restrukturierung ist es knapp — "
            "IDW S 6, Bankenrunde, Cross-Class-Cram-Down brauchen 9-12 Monate Vorlauf.",
            S_folie_body))

    folie(story, 5, "Fall B: Familienunternehmen AG — Anleihe-Countdown", f5)

    # Folie 6 — Fallvignette C
    def f6(parts):
        parts.append(Paragraph(
            "Fall C: NORDFELS POWER CELLS SE — Aktivist trifft Stabilisierungsanordnung",
            S_folie_bold))
        vigC = [
            ['Rechtsform', 'SE (börsennotiert)'],
            ['Problem', 'EUR 550 Mio. Finanzschulden, Großkunde weg, Aktivist-HF 11%'],
            ['Aktenzeichen', 'AG Stuttgart 14 RES 22/26 + Stabilisierungsanordnung'],
            ['StaRUG-Instrument', 'Stabilisierungsanordnung §§ 49-59 + CRO + CramDown + KE'],
            ['Lektion', 'Aktivisten-Brief auf Englisch ist Eskalation — sofort rechtlich reagieren!'],
            ['Lektion 2', 'Kapitalherabsetzung/-erhöhung gegen Streubesitz braucht §§ 7 Abs. 4, 26 StaRUG'],
        ]
        vig_tbl = Table(vigC, colWidths=[4.5*cm, 11.5*cm])
        vig_tbl.setStyle(tbl_style_standard())
        parts.append(vig_tbl)
        parts.append(Spacer(1, 0.2*cm))
        parts.append(Paragraph(
            "Takeaway: Stabilisierungsanordnung ist das staerkste StaRUG-Werkzeug — "
            "aber sie hat eine kurze Laufzeit. Restrukturierungsplan muss danach sofort stehen.",
            S_folie_body))

    folie(story, 6, "Fall C: SE mit Aktivist — Wenn der Hedgefonds droht", f6)

    # Folie 7 — Fallvignette D
    def f7(parts):
        parts.append(Paragraph(
            "Fall D: SALALTBAR UG — Der Klassiker, der alle Annahmen bricht",
            S_folie_bold))
        vigD = [
            ['Rechtsform', 'UG (haftungsbeschränkt), Stammkapital EUR 1,00'],
            ['Problem', 'Reichweite 11 Tage, Lieferstopp, fristlose Mietkündigung'],
            ['Aktenzeichen', 'AG Charlottenburg 36 IN 412/26 (Insolvenzantrag droht)'],
            ['StaRUG-Instrument', 'Keines — zu spät. § 15a InsO bereits relevant.'],
            ['Lektion', '§ 1 StaRUG gilt AUCH für UG-GF — Unwissen schützt nicht'],
            ['Lektion 2', 'Berater-Pflicht: RAin Wandelmoser § 102-Schreiben trotz kleinem Mandat!'],
        ]
        vig_tbl = Table(vigD, colWidths=[4.5*cm, 11.5*cm])
        vig_tbl.setStyle(tbl_style_standard())
        parts.append(vig_tbl)
        parts.append(Spacer(1, 0.2*cm))
        parts.append(Paragraph(
            "Takeaway: Das Gesetz unterscheidet nicht zwischen EUR 1 und EUR 100.000 Stammkapital. "
            "Wer als GF keinen Liquiditaetsplan hat, verletzt § 1 StaRUG — und haftet persönlich.",
            S_folie_body))

    folie(story, 7, "Fall D: UG mit EUR 1 — Das Gesetz kennt keine Groessenschwelle", f7)

    # Folie 8 — Call-to-Action
    def f8(parts):
        parts.append(Paragraph("Die drei Takeaways des Abends:", S_folie_bold))
        takeaways = [
            ("1", "§ 1 StaRUG ist Pflicht — nicht Option.",
             "Jeder GF / Vorstand / Geschäftsleiter muss heute einen 24-Monats-Plan haben. "
             "Kein Plan = Pflichtverletzung = Haftung."),
            ("2", "§ 102 StaRUG: Berater, warnt Eure Mandanten schriftlich.",
             "Das Schreiben ist Euer Schutz und der des Mandanten. "
             "Ohne Schreiben: volle Haftung im Regressfall."),
            ("3", "Wer das Heft des Handelns verliert, verliert StaRUG.",
             "Der Stabilisierungsrahmen existiert nur, solange Handlungsfähigkeit besteht. "
             "Wer wartet bis zur akuten ZU, ist zu spät."),
        ]
        for nr, bold_txt, body_txt in takeaways:
            ta_data = [[
                Paragraph(nr, ParagraphStyle('ta_nr', fontName='Helvetica-Bold', fontSize=24,
                                              textColor=colors.white, alignment=TA_CENTER)),
                [Paragraph(bold_txt, ParagraphStyle('ta_bold', fontName='Helvetica-Bold', fontSize=12,
                                                     textColor=DUNKELBLAU, spaceAfter=4)),
                 Paragraph(body_txt, S_folie_body)]
            ]]
            ta_tbl = Table(ta_data, colWidths=[1.2*cm, 14.3*cm])
            ta_tbl.setStyle(TableStyle([
                ('BACKGROUND',(0,0),(0,0), DUNKELBLAU),
                ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                ('PADDING',(0,0),(0,0),8),
                ('PADDING',(1,0),(1,0),6),
                ('BOX',(0,0),(-1,-1),1,GRAU_MID),
            ]))
            parts.append(ta_tbl)
            parts.append(Spacer(1, 0.2*cm))
        parts.append(Spacer(1, 0.3*cm))
        parts.append(Paragraph(
            "Kontakt: Reher Wennstedt Restrukturierung Partnerschaft mbB  |  "
            "Hohe Bleichen 12  |  20354 Hamburg  |  www.reher-wennstedt.de (fiktiv)",
            ParagraphStyle('cta_contact', fontName='Helvetica', fontSize=9,
                           textColor=GRAU_DUNKEL, alignment=TA_CENTER)))

    folie(story, 8, "Call-to-Action: Was muessen Sie MORGEN tun?", f8)


def build_stundenaufstellung(story):
    """Stundenaufstellung Reher Wennstedt — 2 Seiten"""
    story.append(Paragraph("KOSTENUBERSICHT", S['h_kapitel']))
    story.append(Paragraph("Reher Wennstedt Restrukturierung Partnerschaft mbB", S['subtitle_cap']))
    story.append(hr(DUNKELBLAU, thickness=2))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Die nachstehende Stundenaufstellung illustriert den typischen Beratungsaufwand "
        "für eine Krisenfrüherkennungsberatung nach § 1 StaRUG. "
        "Die Angaben sind Richtwerte auf Basis fiktiver Mandate der vier Varianten.",
        S['body']))
    story.append(Spacer(1, 0.3*cm))

    story.append(kanzlei_kopf_rw())
    story.append(Spacer(1, 0.3*cm))

    meta_data = [
        ['Kanzlei:', 'Reher Wennstedt Restrukturierung Partnerschaft mbB'],
        ['Adresse:', 'Hohe Bleichen 12, 20354 Hamburg'],
        ['Telefon:', '+49 (0)40 / 44 00 00-0 (fiktiv)'],
        ['Erstellungsdatum:', '22. Mai 2026'],
        ['Berichtszeitraum:', '1. Januar 2026 — 22. Mai 2026'],
        ['Rechnungsgrundlage:', 'Stundenhonorar gemäß Mandatsvereinbarungen'],
    ]
    for row in meta_data:
        m_tbl = Table([row], colWidths=[3.5*cm, 13*cm])
        m_tbl.setStyle(TableStyle([
            ('FONTNAME',(0,0),(0,0),'Helvetica-Bold'),
            ('FONTSIZE',(0,0),(-1,-1),9),
            ('BOTTOMPADDING',(0,0),(-1,-1),2),
        ]))
        story.append(m_tbl)
    story.append(Spacer(1, 0.3*cm))
    story.append(HRFlowable(width='100%', thickness=0.5, color=GRAU_MID))
    story.append(Spacer(1, 0.3*cm))

    # Variante A
    story.append(Paragraph("Mandat A: VEYRA AI Foundation gGmbH — AZ AG Frankfurt 810 RES 14/26", S['h2']))
    std_a = [
        ['Datum', 'Tätigkeit', 'Bearbeiter', 'Std', 'Satz (EUR/h)', 'Betrag (EUR)'],
        ['05.01.2026', 'Erstgespräch Dr. Hellinghaus-Karpov, Sachverhaltsaufnahme', 'Dr. Reher-Bornholmsen', '2,0', '450', '900,00'],
        ['12.01.2026', 'Prüfung Vereinssatzung, Fördervertrag EU-Horizont', 'Dr. Reher-Bornholmsen', '3,5', '450', '1.575,00'],
        ['19.01.2026', 'Erstellung § 102-StaRUG-Warnschreiben, Abstimmung GF', 'Dr. Reher-Bornholmsen', '1,5', '450', '675,00'],
        ['26.01.2026', 'Ausarbeitung 24-Monats-Liquiditätsplan (Basis)', 'Ass. M. Tolksdorf', '8,0', '280', '2.240,00'],
        ['02.02.2026', 'Stress-Szenario-Analyse (Spendeneinbruch / Förder-Delay)', 'Ass. M. Tolksdorf', '4,0', '280', '1.120,00'],
        ['10.02.2026', 'Aufsichtsratssitzung Veyra AI: Präsentation Krisenanalyse', 'Dr. Reher-Bornholmsen', '3,0', '450', '1.350,00'],
        ['17.02.2026', 'Entwurf Stundungsvereinbarung Nordlicht Cloud GmbH', 'Dr. Reher-Bornholmsen', '2,5', '450', '1.125,00'],
        ['24.02.2026', 'Verhandlung Nordlicht Cloud GmbH (telefonisch)', 'Dr. Reher-Bornholmsen', '1,5', '450', '675,00'],
        ['03.03.2026', 'Vorbereitung Anzeige Restrukturierungssache § 31 StaRUG', 'Dr. Reher-Bornholmsen', '2,0', '450', '900,00'],
        ['10.03.2026', 'Einreichung AG Frankfurt, Abstimmung Gericht', 'Dr. Reher-Bornholmsen', '1,0', '450', '450,00'],
        ['', 'ZWISCHENSUMME MANDAT A', '', '29,0', '', '11.010,00'],
    ]
    std_a_tbl = Table(std_a, colWidths=[2.2*cm, 6.5*cm, 3.0*cm, 1.0*cm, 1.8*cm, 2.0*cm])
    std_a_style = tbl_style_zahlen()
    std_a_style.add('FONTNAME', (0,-1),(-1,-1), 'Helvetica-Bold')
    std_a_style.add('BACKGROUND', (0,-1),(-1,-1), colors.HexColor('#E8EFF8'))
    std_a_tbl.setStyle(std_a_style)
    story.append(std_a_tbl)
    story.append(Spacer(1, 0.4*cm))

    # Variante B
    story.append(Paragraph("Mandat B: HERRENBLUSE & ZWIRN HARTMANNSCHMIDT AG — AZ AG Bamberg 53 RES 7/26", S['h2']))
    std_b = [
        ['Datum', 'Tätigkeit', 'Bearbeiter', 'Std', 'Satz (EUR/h)', 'Betrag (EUR)'],
        ['08.01.2026', 'Erstgespräch Vorstand (Hartmannschmidt + Lüttke-Berens)', 'Dr. Reher-Bornholmsen', '3,0', '450', '1.350,00'],
        ['15.01.2026', 'Anleihebedingungen-Prüfung + Covenant-Analyse', 'Dr. Vellmer-Lutz', '5,0', '380', '1.900,00'],
        ['22.01.2026', 'Bankenrunde Vorbereitung (NorddeutscheLandesbank-Avis)', 'Dr. Reher-Bornholmsen', '2,5', '450', '1.125,00'],
        ['29.01.2026', 'Bankenrunde (Protokollierung)', 'Dr. Vellmer-Lutz', '4,0', '380', '1.520,00'],
        ['05.02.2026', 'Cross-Class-Cram-Down-Memo (Erstfassung)', 'Dr. Vellmer-Lutz', '6,0', '380', '2.280,00'],
        ['12.02.2026', 'HV-Vorbereitung Familien-Anker Hartmannschmidt Holding', 'Dr. Reher-Bornholmsen', '3,0', '450', '1.350,00'],
        ['19.02.2026', 'Abstimmung Sanierungsgutachten Hartwig Aktuar', 'Dr. Reher-Bornholmsen', '2,0', '450', '900,00'],
        ['26.02.2026', 'Anzeige AG Bamberg § 31 StaRUG, Korrespondenz Gericht', 'Dr. Vellmer-Lutz', '2,0', '380', '760,00'],
        ['', 'ZWISCHENSUMME MANDAT B', '', '27,5', '', '11.185,00'],
    ]
    std_b_tbl = Table(std_b, colWidths=[2.2*cm, 6.5*cm, 3.0*cm, 1.0*cm, 1.8*cm, 2.0*cm])
    std_b_style = tbl_style_zahlen()
    std_b_style.add('FONTNAME', (0,-1),(-1,-1), 'Helvetica-Bold')
    std_b_style.add('BACKGROUND', (0,-1),(-1,-1), colors.HexColor('#E8EFF8'))
    std_b_tbl.setStyle(std_b_style)
    story.append(std_b_tbl)
    story.append(PageBreak())

    # Variante C
    story.append(Paragraph("Mandat C: NORDFELS POWER CELLS SE — AZ AG Stuttgart 14 RES 22/26", S['h2']))
    std_c = [
        ['Datum', 'Tätigkeit', 'Bearbeiter', 'Std', 'Satz (EUR/h)', 'Betrag (EUR)'],
        ['02.01.2026', 'Krisenanalyse Vorstand (Vossbergen/Tannert-Brescia/Bietendüvel)', 'Dr. Reher-Bornholmsen', '4,0', '450', '1.800,00'],
        ['09.01.2026', 'Aktionärsstrukturanalyse + Aktivisten-Letter-Strategie', 'Prof. Dr. Hartfeld-Marwede', '6,0', '520', '3.120,00'],
        ['16.01.2026', 'Restrukturierungsbeauftragten-Auswahl (Greve-Tornquist)', 'Dr. Reher-Bornholmsen', '2,0', '450', '900,00'],
        ['23.01.2026', 'Stabilisierungsanordnungs-Antrag §§ 49-59 StaRUG (Volltext)', 'Prof. Dr. Hartfeld-Marwede', '10,0', '520', '5.200,00'],
        ['30.01.2026', 'Abstimmung AG Stuttgart (Richter, Geschäftsstelle)', 'Dr. Reher-Bornholmsen', '3,0', '450', '1.350,00'],
        ['06.02.2026', 'Schlechterstellungsverbots-Gutachten (Erstfassung)', 'Prof. Dr. Hartfeld-Marwede', '8,0', '520', '4.160,00'],
        ['13.02.2026', 'Westshore Catalyst Investor-Letter-Response (englisch)', 'Dr. Reher-Bornholmsen', '3,0', '450', '1.350,00'],
        ['20.02.2026', '24-Monats-Liquiditätsplan drei Szenarien (Ass. Zuarbeit)', 'Ass. P. Rademann', '12,0', '280', '3.360,00'],
        ['27.02.2026', 'Restrukturierungsplan-Entwurf (Basis), gestaltender Teil', 'Prof. Dr. Hartfeld-Marwede', '14,0', '520', '7.280,00'],
        ['', 'ZWISCHENSUMME MANDAT C', '', '62,0', '', '28.520,00'],
    ]
    std_c_tbl = Table(std_c, colWidths=[2.2*cm, 6.5*cm, 3.0*cm, 1.0*cm, 1.8*cm, 2.0*cm])
    std_c_style = tbl_style_zahlen()
    std_c_style.add('FONTNAME', (0,-1),(-1,-1), 'Helvetica-Bold')
    std_c_style.add('BACKGROUND', (0,-1),(-1,-1), colors.HexColor('#E8EFF8'))
    std_c_tbl.setStyle(std_c_style)
    story.append(std_c_tbl)
    story.append(Spacer(1, 0.4*cm))

    # Variante D
    story.append(Paragraph("Beratungs-Kosten Variante D: SALALTBAR UG — Vergleichsperspektive", S['h2']))
    story.append(Paragraph(
        "HINWEIS: Variante D wird von RAin Charlotte Wandelmoser (Berlin) bearbeitet. "
        "Reher Wennstedt wird ggf. für StaRUG-Tiefenberatung hinzugezogen. "
        "Stundenhonorar RAin Wandelmoser: EUR 280,00 netto/h.",
        S['body']))
    std_d = [
        ['Datum', 'Tätigkeit', 'Bearbeiter', 'Std', 'Satz (EUR/h)', 'Betrag (EUR)'],
        ['28.04.2026', 'Erstgespräch Çelebi-Drebenstedt (60 min)', 'RAin Wandelmoser', '1,0', '280', '280,00'],
        ['29.04.2026', '§ 102-StaRUG-Schreiben verfassen + versenden', 'RAin Wandelmoser', '1,5', '280', '420,00'],
        ['30.04.2026', 'Filialanalyse + Cash-Flow-Skizze auswerten', 'RAin Wandelmoser', '1,5', '280', '420,00'],
        ['02.05.2026', 'Folgegespräch (E-Mail + Tel.), § 15a InsO-Memo', 'RAin Wandelmoser', '1,0', '280', '280,00'],
        ['05.05.2026', 'Schließungsberatung Sonnenallee + Mietrechtl. Optionen', 'RAin Wandelmoser', '2,0', '280', '560,00'],
        ['', 'ZWISCHENSUMME RAin Wandelmoser', '', '7,0', '', '1.960,00'],
    ]
    std_d_tbl = Table(std_d, colWidths=[2.2*cm, 6.5*cm, 3.0*cm, 1.0*cm, 1.8*cm, 2.0*cm])
    std_d_style = tbl_style_zahlen()
    std_d_style.add('FONTNAME', (0,-1),(-1,-1), 'Helvetica-Bold')
    std_d_style.add('BACKGROUND', (0,-1),(-1,-1), colors.HexColor('#E8EFF8'))
    std_d_tbl.setStyle(std_d_style)
    story.append(std_d_tbl)
    story.append(Spacer(1, 0.4*cm))

    # Gesamtüberblick
    gesamt_data = [
        ['Mandat', 'Kanzlei', 'Stunden', 'Betrag (EUR netto)', 'zzgl. 19% MwSt.', 'Gesamt (EUR brutto)'],
        ['A: VEYRA AI Foundation', 'Reher Wennstedt', '29,0', '11.010,00', '2.091,90', '13.101,90'],
        ['B: HARTMANNSCHMIDT AG', 'Reher Wennstedt', '27,5', '11.185,00', '2.125,15', '13.310,15'],
        ['C: NORDFELS SE', 'Reher Wennstedt', '62,0', '28.520,00', '5.418,80', '33.938,80'],
        ['D: SALALTBAR UG', 'RAin Wandelmoser', '7,0', '1.960,00', '372,40', '2.332,40'],
        ['GESAMT', '', '125,5', '52.675,00', '10.008,25', '62.683,25'],
    ]
    gesamt_tbl = Table(gesamt_data, colWidths=[3.8*cm, 3.0*cm, 1.5*cm, 3.2*cm, 2.5*cm, 3.0*cm])
    gesamt_style = tbl_style_zahlen()
    gesamt_style.add('FONTNAME', (0,-1),(-1,-1), 'Helvetica-Bold')
    gesamt_style.add('BACKGROUND', (0,-1),(-1,-1), DUNKELBLAU)
    gesamt_style.add('TEXTCOLOR', (0,-1),(-1,-1), colors.white)
    gesamt_tbl.setStyle(gesamt_style)
    story.append(gesamt_tbl)
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "<i>Lehrperspektive: Die vier Fälle illustrieren das Kostenspektrum der StaRUG-Beratung — "
        "von EUR 2.332 (Kleinstmandat UG) bis EUR 33.938 (komplexe SE mit Aktivist und Cross-Class-Cram-Down). "
        "Frühzeitige Beratung ist stets günstiger als das Krisenmanagement in der Insolvenz.</i>",
        S['small']))
    story.append(PageBreak())


def main():
    """Hauptfunktion: Erzeugt das komplette Konvolut-PDF."""
    story = []

    # 1. Konvolut-Aktendeckel
    build_konvolut_deckel(story)

    # 2. Vorbemerkung
    build_vorbemerkung(story)

    # 3. Vergleichstabelle
    build_vergleichstabelle(story)

    # 4. Variante A
    build_trennblatt(story, "A",
                     "VEYRA AI Foundation gGmbH",
                     "KI-Forschungs-gGmbH | Frankfurt am Main",
                     "AG Frankfurt 810 RES 14/26", FARBE_A)
    build_variante_a(story)

    # 5. Variante B
    build_trennblatt(story, "B",
                     "HERRENBLUSE & ZWIRN HARTMANNSCHMIDT AG",
                     "Hemdenmanufaktur | Bamberg",
                     "AG Bamberg 53 RES 7/26", FARBE_B)
    build_variante_b(story)

    # 6. Variante C
    build_trennblatt(story, "C",
                     "NORDFELS POWER CELLS SE",
                     "Batteriehersteller | Ellwangen",
                     "AG Stuttgart 14 RES 22/26", FARBE_C)
    build_variante_c(story)

    # 7. Variante D
    build_trennblatt(story, "D",
                     "SALALTBAR UG (haftungsbeschraenkt)",
                     "Vegane Salat-Bar-Kette | Berlin-Neukoelln",
                     "AG Charlottenburg 36 IN 412/26", FARBE_D)
    build_variante_d(story)

    # 8. Vorlagen-Annex
    story.append(PageBreak())
    story.append(Paragraph("─" * 60, ParagraphStyle('trenn', fontName='Helvetica', fontSize=8,
                                                      alignment=TA_CENTER, textColor=GRAU_MID)))
    story.append(PageBreak())
    build_vorlagen_annex(story)

    # 9. Foliensatz
    story.append(PageBreak())
    story.append(Paragraph("FOLIENSATZ — IMPULSVORTRAG", S['h_kapitel']))
    story.append(Paragraph(
        "Restructuring Lounge Hamburg — WAYES — 28. Mai 2026",
        S['subtitle_cap']))
    story.append(hr(DUNKELBLAU, thickness=2))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "Die nachfolgenden acht Folien entsprechen der Präsentation des Impulsvortrags "
        "von Dr. Tjark Reher-Bornholmsen auf der WAYES Restructuring Lounge Hamburg "
        "am 28. Mai 2026 zum Thema 'Krisenfrüherkennung nach § 1 StaRUG — Pflicht, nicht Option'. "
        "Jede Folie ist als eigenständige Seite mit Folienrahmen dargestellt.",
        S['body']))
    story.append(PageBreak())
    build_foliensatz(story)

    # 10. Stundenaufstellung
    build_stundenaufstellung(story)

    # ─── PDF erzeugen ────────────────────────────────────────────────────────────
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        rightMargin=2.0*cm,
        leftMargin=2.0*cm,
        topMargin=2.5*cm,
        bottomMargin=2.0*cm,
        title="Testakte Krisenfrueherkennung StaRUG — Vier Varianten",
        author="Reher Wennstedt Restrukturierung Partnerschaft mbB (fiktiv)",
        subject="§ 1 StaRUG Krisenfrüherkennung — Lehrakte",
        creator="generate_testakte.py"
    )

    def on_page(canvas_obj, doc_obj):
        page_standard(canvas_obj, doc_obj,
                      aktenzeichen="Konvolut: AG Frankfurt/Bamberg/Stuttgart/Charlottenburg",
                      betreff="Krisenfrüherkennung § 1 StaRUG — Vier Varianten")

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF erzeugt: {OUTPUT}")

    # Validierung
    from reportlab.lib.pagesizes import A4 as _A4
    import struct
    with open(OUTPUT, 'rb') as f:
        content = f.read()
    page_count = content.count(b'/Type /Page\n') + content.count(b'/Type/Page\n')
    # Alternativer Zähler
    import re
    pages_found = len(re.findall(b'/Type\\s*/Page[^s]', content))
    print(f"Geschaetzte Seitenanzahl: {pages_found}")
    print("Validierung:")
    print(f"  - Dateipfad: {OUTPUT}")
    print(f"  - Dateigrösse: {len(content):,} Bytes")
    print(f"  - Variante A: VEYRA AI Foundation gGmbH | AG Frankfurt 810 RES 14/26")
    print(f"  - Variante B: HERRENBLUSE & ZWIRN HARTMANNSCHMIDT AG | AG Bamberg 53 RES 7/26")
    print(f"  - Variante C: NORDFELS POWER CELLS SE | AG Stuttgart 14 RES 22/26")
    print(f"  - Variante D: SALALTBAR UG | AG Charlottenburg 36 IN 412/26")


if __name__ == "__main__":
    main()
