# -*- coding: utf-8 -*-
# Part 37: Pinkerton NYC Surveillance Report + Spürnase-Couture III + handschriftliche Notizen

def blatt_pinkerton():
    s = []
    # Pinkerton fake letterhead
    s.append(Paragraph("PINKERTON CONSULTING &amp; INVESTIGATIONS, INC.", S_H1))
    s.append(Paragraph("a Securitas company &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; est. 1850", S_CENTER))
    s.append(Paragraph("Two Jericho Plaza, Suite 309, Jericho, NY 11753 &nbsp;&nbsp;|&nbsp;&nbsp; "
                       "NY State Lic. # 11000123456", S_TINY))
    s.append(HLine())
    s.append(Spacer(1, 2*mm))
    s.append(Paragraph("CONFIDENTIAL — ATTORNEY WORK PRODUCT", S_RIGHT))
    s.append(Paragraph("Privileged &amp; Confidential per Fed. R. Civ. P. 26(b)(3)", S_RIGHT))
    s.append(Spacer(1, 2*mm))
    s.append(Paragraph("<b>SURVEILLANCE REPORT</b>", S_H2))
    s.append(Paragraph("File No. PCI-NY-2026-08827-K", S_NORMAL))
    s.append(Paragraph("Matter: WBF-2026-KK-0014 (klôtzzkètté Inc. v. A&amp;K Boulevard Boutique LLC et al.)", S_NORMAL))
    s.append(Paragraph("Period covered: May 4 — May 17, 2026 (14 calendar days)", S_NORMAL))
    s.append(Paragraph("Operative(s): J. Caruso (lead, NY PI Lic. 11000098771), M. Iwaszko, D. Rosenbluth", S_NORMAL))
    s.append(Paragraph("Subject(s): Aaron G. KALMAN (DOB 03/17/1979); A&amp;K Boulevard Boutique LLC; "
                       "874 Madison Avenue, NY, NY 10021; storage facility Manhattan Mini Storage, "
                       "520 W 17th St; Hudson Yards UPS Customer Center 405 W 31st St", S_NORMAL))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("<b>1. SUMMARY OF FINDINGS</b>", S_H3))
    s.append(Paragraph(
        "During the surveillance period, Subject KALMAN was observed on six (6) separate occasions "
        "transporting unmarked corrugated cartons (estimated dimensions 60×40×40 cm; brown kraft) "
        "from a third-floor stockroom at 874 Madison Ave to a rented locker (Unit 7-G-22) at "
        "Manhattan Mini Storage, 520 W 17th St. On May 11 at approximately 14:37 EDT, operative "
        "M. Iwaszko (posing as prospective customer) entered the boutique and purchased one (1) "
        "silk scarf bearing the mark KLÔTZZKÈTTÉ (90×90 cm, predominantly cobalt blue with "
        "gold crown motif) for the price of USD 1,295.00 (cash, no receipt offered, receipt "
        "provided only upon request and showing &quot;ASCOT BLEU 90 — Italian silk scarf&quot; "
        "without the KLÔTZZKÈTTÉ mark on the receipt). The scarf has been forensically examined "
        "(see Annex C, separate cover) and is, in the opinion of our consulting expert Mme. "
        "Périgord, a counterfeit of inferior weave (24 momme vs. genuine 32 momme).",
        S_NORMAL_LEFT))
    s.append(Spacer(1, 2*mm))
    s.append(Paragraph("<b>2. CHRONOLOGY (selected entries)</b>", S_H3))
    obs = [
        ("Mon 05/04 09:12", "Subject opens boutique. Truck arrives 09:48 (NJ plate G27-HKT). "
                            "Three (3) cartons offloaded via service entrance. No customs paperwork visible."),
        ("Tue 05/05 11:30", "Subject meets unidentified male (Caucasian, ~55 y, dark coat) at "
                            "café Sant Ambroeus, 1000 Madison Ave. Conversation ~38 min. "
                            "Photographs obtained, see Annex B-2 through B-9."),
        ("Wed 05/06 16:14", "UPS pickup at boutique. Five (5) packages labeled to addresses in "
                            "Greenwich CT, Palm Beach FL, Aspen CO, Bal Harbour FL, Beverly Hills CA. "
                            "Tracking numbers logged."),
        ("Thu 05/07 21:08", "Subject departs to private residence 1083 Park Ave, Apt 14-B."),
        ("Sat 05/09 13:55", "Boutique visited by female client (~40 y, blonde, blue Hermès Birkin). "
                            "Purchase total approx. USD 6,400, four (4) items, cash."),
        ("Mon 05/11 14:37", "Pretext purchase by operative Iwaszko. See Summary §1 above."),
        ("Tue 05/12 10:02", "Subject and unidentified male (same as 05/05) enter storage locker "
                            "7-G-22. Departure 10:41 with two (2) cartons loaded into black Cadillac "
                            "Escalade NY plate KKE-1923 (registered to Klotzkettie LLC, Wilmington DE)."),
        ("Fri 05/15 17:25", "Boutique receives FedEx International Priority shipment, AWB "
                            "7787-2244-9911, declared origin <b>Vilnius, Lithuania</b>, declared "
                            "value USD 287, declared contents &quot;cotton textile samples&quot;. "
                            "Weight: 14.7 kg. Suspicious value-to-weight ratio noted."),
        ("Sat 05/16 02:14", "Night-time delivery van (no markings) at service entrance. Two persons, "
                            "approx. 12 min activity. Video footage Annex D."),
    ]
    data = [["Date / Time (EDT)", "Observation"]] + obs
    t = Table(data, colWidths=[36*mm, 130*mm], repeatRows=1)
    t.setStyle(TableStyle([
        ('FONT', (0,0), (-1,0), "Times-Bold", 8),
        ('FONT', (0,1), (-1,-1), "Times-Roman", 8),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('GRID', (0,0), (-1,-1), 0.3, colors.grey),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    s.append(t)
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("<b>3. OPERATIONAL ASSESSMENT</b>", S_H3))
    s.append(Paragraph(
        "The pattern of observations is consistent with a transshipment operation in which "
        "counterfeit goods of Lithuanian (UAB klotzkettie) and/or third-country origin are "
        "received under low-declared customs values, repackaged at 874 Madison and the W 17th "
        "St storage facility, and distributed to high-net-worth individuals at second-home "
        "addresses in resort markets, thereby substantially evading both detection by rights "
        "holders and the customs duty regime. The use of cash transactions for high-ticket "
        "items, the discrepancy between receipt descriptions and actual goods, and the night-time "
        "deliveries are all hallmarks of a sophisticated grey-market / counterfeit operation, "
        "in our experience.",
        S_NORMAL_LEFT))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("Submitted respectfully,", S_NORMAL))
    s.append(Paragraph("/s/ James A. Caruso", S_NORMAL))
    s.append(Paragraph("James A. Caruso, CFE, CPP — Director, Investigative Services (NY)", S_NORMAL))
    s.append(Paragraph("Pinkerton Consulting &amp; Investigations, Inc.", S_NORMAL))
    s.append(Paragraph("Annexes: A (photographs, 47 pp.) · B (subject portraits, 12 pp.) · "
                       "C (forensic textile report by Mme. Périgord, separate cover) · D (video, USB)", S_TINY))
    return s


def blatt_spuernase_iii():
    s = []
    s.append(Paragraph("SPÜRNASE-COUTURE GmbH", S_H1))
    s.append(Paragraph("Diskrete Ermittlungen in der gehobenen Modebranche · seit 1987", S_CENTER))
    s.append(Paragraph("Schwanthalerstraße 78 · 80336 München · Tel. 089 / 5577-4040", S_TINY))
    s.append(HLine())
    s.append(Paragraph("<b>ERMITTLUNGSBERICHT NR. III/2026</b>", S_H2))
    s.append(Paragraph("Aktenzeichen: SC-2026-0444-K (Mandat klôtzzkètté S.A. via Steinacker LLP)", S_NORMAL))
    s.append(Paragraph("Ermittlungszeitraum: 02.05.2026 — 18.05.2026", S_NORMAL))
    s.append(Paragraph("Ermittlerinnen: Karla KALT-BANDEL (Lead, BDD-Lizenz Nr. M-1184), "
                       "Bastian SPÜRMÜLLER-FÜRST (BDD M-2207), Nadya OSTRZECHOWSKI (BDD M-3041)", S_NORMAL))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("<b>I. AUFTRAGSGEGENSTAND.</b> Aufgrund mündlicher Beauftragung durch RA "
        "Dr. Dr. A. Steinacker-von Tarsis am 30.04.2026, 16:55 Uhr, telefonisch bestätigt am "
        "02.05.2026 per E-Mail, ergänzt durch schriftlichen Auftrag vom 03.05.2026: "
        "Ermittlung der Vertriebskette der unter den Bezeichnungen «klotzkettiee», «KLOTZ-KETTE» "
        "und «K°-Kette» auf den Plattformen Donauzon.de / .lu / .it / .fr seit März 2026 "
        "angebotenen Damen- und Herrenaccessoires (Schals, Krawatten, Schlüsselanhänger, "
        "Manschettenknöpfe, Parfüm-Probefläschchen).", S_NORMAL_LEFT))
    s.append(Paragraph("<b>II. TESTKÄUFE.</b> Im Berichtszeitraum wurden insgesamt 47 Testbestellungen "
        "über sieben anonymisierte Donauzon-Konten (vier deutsche, je ein luxemburgisches, "
        "italienisches, französisches) zu insgesamt EUR 11.847,32 abgewickelt. Sämtliche "
        "Lieferungen erfolgten in unauffälliger brauner Wellpappe ohne Markennennung, jedoch mit "
        "dreifach gefalteten Beipackzetteln in linguistisch auffälligem Deutsch "
        "(»Original Frankreich Luxus echt!«), die in 32 von 47 Fällen identische Druckfehler "
        "(insbesondere »Société Anonime« statt »Anonyme«; »Boutigue« statt »Boutique«) aufwiesen "
        "— ein deutliches Indiz für einen einzigen Druckdienstleister.", S_NORMAL_LEFT))
    s.append(Paragraph("<b>III. ABSENDER.</b> Die Sendungen wurden durchwegs aus zwei Postleitzahlbereichen "
        "verschickt: LT-01402 Vilnius (Vilniaus g. 47 — bekannte Anschrift der UAB klotzkettie) "
        "sowie aus L-1450 Luxembourg-Limpertsberg (16, rue Auguste Letellier — auf den Namen "
        "einer »KK Trading SARL« registriert, deren wirtschaftlich Berechtigter ausweislich "
        "des luxemburgischen Registre des bénéficiaires effectifs ein gewisser <b>Mindaugas "
        "BREZELMANAS</b>, geb. 14.07.1981 in Kaunas, ist — vermutete Identität mit Egonas "
        "Brezelmanas / Egon Brezelmann).", S_NORMAL_LEFT))
    s.append(Paragraph("<b>IV. WAREN.</b> Forensische Begutachtung durch Mlle. H. Périgord (Grasse) "
        "und Prof. Dr.-Ing. H. Tastenberger (TU Darmstadt) ergab: Sämtliche Schals weisen "
        "Seidengewicht ≤ 22 Momme (Original: 32 Momme); 12 von 14 Parfüm-Proben enthalten "
        "Spuren von Phthalat-Weichmachern (DEHP, DBP) in Konzentrationen oberhalb der "
        "EU-Kosmetikverordnung (VO 1223/2009 Anhang II Nr. 1404, 1405). Vier Schlüsselanhänger "
        "lösten beim Tastenberger-Haptik-Test (24-Punkte-Skala) lediglich 7 bis 9 Punkte aus, "
        "gegenüber 21-23 Punkten beim Original — die Haptik ist somit objektiv reproduzierbar "
        "abweichend.", S_NORMAL_LEFT))
    s.append(Paragraph("<b>V. EMPFEHLUNG.</b> Wir empfehlen dringend (a) unverzügliche "
        "Strafanzeige in Luxemburg gegen die Verantwortlichen der KK Trading SARL "
        "(parallel zur bereits am 14.05.2026 in Vilnius gestellten Anzeige); (b) Erweiterung "
        "des UWG-Antrags vor dem LG Frankfurt auf das luxemburgische Vertriebsnetz; "
        "(c) Hinweis an die luxemburgischen Zollbehörden (ALD) gemäß VO (EU) 608/2013.", S_NORMAL_LEFT))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("München, den 19. Mai 2026", S_RIGHT))
    s.append(Paragraph("Karla Kalt-Bandel<br/>(Geschäftsführerin · vereidigte Ermittlerin)", S_RIGHT))
    s.append(Paragraph("Honorarabrechnung gesondert (vgl. Bl. 217 d. A.).", S_TINY))
    return s


def blatt_handnotiz_visconti():
    s = []
    s.append(Paragraph("Handschriftliche Notiz · Comtesse Béatrice de Klôtzzkètté-Visconti", S_H3))
    s.append(Paragraph("(am Rand des Pinkerton-Berichts, mit grünem Filzstift)", S_TINY))
    s.append(HLine())
    s.append(Spacer(1, 5*mm))
    s.append(Paragraph("Mes très chers Maîtres,", S_HAND))
    s.append(Spacer(1, 2*mm))
    s.append(Paragraph(
        "j'ai lu ce rapport Pinkerton hier soir au Cipriani, avec un negroni — et j'ai failli "
        "renverser le verre! Cette histoire de cartons à 02h14 du matin sur Madison — c'est "
        "scandaleux, abominable, et — entre nous — formidablement utile pour notre dossier "
        "RICO. Demandez tout de suite à Maître Whitman s'il pense que nous avons les "
        "predicate acts suffisants. À mon humble avis: oui, trois fois oui.",
        S_HAND))
    s.append(Spacer(1, 2*mm))
    s.append(Paragraph(
        "P.-S.: Le chauffeur Gianluca me dit qu'il a vu la Escalade noire KKE-1923 garée "
        "devant le Carlyle samedi soir. Coïncidence? Je ne crois pas aux coïncidences depuis "
        "1987.",
        S_HAND))
    s.append(Spacer(1, 2*mm))
    s.append(Paragraph("Bien à vous,<br/>B. de Kl-V.", S_HAND))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("[unten in andere Handschrift, vermutlich Steinacker:] "
                       "→ Vermerk Whitman 22.05., 17:30 CET / 11:30 EST. RICO-Prüfung läuft. "
                       "Predicate acts: (i) 18 USC § 2320 trafficking, (ii) § 2314 ITSP, "
                       "(iii) § 1956 money laundering. Pattern ✓.", S_HAND2))
    return s


story += blatt_pinkerton()
story.append(PageBreak())
story += blatt_spuernase_iii()
story.append(PageBreak())
story += blatt_handnotiz_visconti()
story.append(PageBreak())
print("[part37] done")
