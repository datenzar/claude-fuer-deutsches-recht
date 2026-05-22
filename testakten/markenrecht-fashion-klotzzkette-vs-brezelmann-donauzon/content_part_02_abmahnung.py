# Part 02: Abmahnung Brezelmann + Unterlassungserklärung
# =====================================================================
def blatt_abmahnung_brezelmann():
    s = []
    s.append(Briefkopf(
        KANZLEI_ADDR,
        "Brezelmann Discount KG\nz.Hd. Herrn Dipl.-Kfm. Egon Brezelmann\nWurstgasse 4\n97980 Bad Mergentheim\n\n— Vorab per Telefax: 07931 / 88 41 12 —\n— sowie per Einschreiben mit Rückschein —",
        "22.01.2026", "Sch-Lich 26-0188 (StI/hk)"))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("<b>Markenverletzung — Abmahnung mit Aufforderung zur Abgabe einer strafbewehrten Unterlassungs- und Verpflichtungserklärung</b>", S_H3))
    s.append(Paragraph(
        "<b>Mandantin:</b> klôtzzkètté S.A., 12 rue du Faubourg Saint-Honoré, 75008 Paris (RCS Paris "
        "552 094 471), vertreten durch ihre Hauptgesellschafterin und alleinvertretungsberechtigte "
        "Geschäftsführerin Comtesse Béatrice de Klôtzzkètté-Visconti.", S_NORMAL))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("Sehr geehrter Herr Brezelmann,", S_NORMAL_LEFT))
    s.append(Spacer(1, 0.15*cm))
    s.append(Paragraph(
        "namens und in Vollmacht (Vollmachtsurkunde beigefügt, Anlage K 1) der oben benannten "
        "Mandantin, der klôtzzkètté S.A. (im Folgenden: <i>die Mandantin</i>), zeigen wir die "
        "Mandatierung an und nehmen wie folgt Stellung:", S_NORMAL))
    s.append(Paragraph("<b>I. Sachverhalt</b>", S_H3))
    s.append(Paragraph(
        "1. Unsere Mandantin ist Inhaberin einer Vielzahl prioritätsälterer Marken, insbesondere "
        "der Unionswortmarke „klôtzzkètté“ (EU 005 412 880, eingetragen am 14.05.2008 für die "
        "Klassen 3, 14, 18, 25 und 35), der Unionswort-/Bildmarke „klôtzzkètté“ mit Krönchen-Monogramm "
        "„K°°“ (EU 010 988 411), der nationalen Bildmarke des silbern-emaillierten Krönchen-Logos "
        "(DPMA 30 2014 077 312) sowie der Positionsmarke „goldenes Krönchen-Insignium auf linker "
        "Schuh-Innensohle Pos. 1 cm vom Fersenrand“ (EUIPO 015 887 442). Wegen weiterer Einzelheiten "
        "verweisen wir auf die als <b>Anlage K 2</b> beigefügte Portfolio-Übersicht (siehe auch "
        "Blatt 3 dieser Akte).", S_NORMAL))
    s.append(Paragraph(
        "2. Am 11.01.2026, 13.01.2026 und 14.01.2026 wurden in den Filialen Ihrer Gesellschaft "
        "in Bad Mergentheim (Wurstgasse 4), Crailsheim (Hauptstraße 17) sowie Tauberbischofsheim "
        "(Marktplatz 4) Waren feilgeboten und verkauft, die das oben bezeichnete Krönchen-Monogramm "
        "„K°°“ unserer Mandantin tragen, namentlich:", S_NORMAL))
    bullet_items = [
        "a) T-Shirts (Modellbezeichnung intern „BTM-MEN-022“) mit aufgedrucktem Krönchen, "
        "Verkaufspreis EUR 9,99;",
        "b) Halstücher mit gewebter Krönchen-Bordüre (Modellbezeichnung „BTM-WMN-118“), "
        "Verkaufspreis EUR 12,99;",
        "c) Handtaschen-Imitate (LeatherLook PU) mit eingeprägtem K°°-Monogramm "
        "(Modellbezeichnung „BTM-BAG-K044“), Verkaufspreis EUR 24,99;",
        "d) <i>besonders gravierend:</i> Parfumflakons in hexagonaler Form mit asymmetrischem "
        "Stopfen, die unverkennbar die 3D-Formmarke EU 008 776 015 unserer Mandantin nachahmen, "
        "Bezeichnung „K-Royal Eau de Parfum“, Verkaufspreis EUR 14,99.",
    ]
    for bi in bullet_items:
        s.append(Paragraph(bi, ParagraphStyle("b", parent=S_NORMAL, leftIndent=14)))
    s.append(Paragraph(
        "3. Sämtliche vorgenannten Waren stammen ausweislich der Etiketten aus Lieferungen "
        "der Firma <i>Brezelmann Trading Lithuania, UAB</i> (Vilnius) — gegen die parallel "
        "vor dem EUIPO Widerspruch eingelegt wurde (Az. B 4 187 932).", S_NORMAL))
    s.append(Paragraph("<b>II. Rechtliche Würdigung</b>", S_H3))
    s.append(Paragraph(
        "1. Die festgestellten Handlungen stellen sich als Markenverletzungen i.S.v. § 14 Abs. 2 "
        "Nr. 1, Nr. 2 und Nr. 3 MarkenG bzw. Art. 9 Abs. 2 lit. a, b und c UMV dar. Hinsichtlich "
        "der unter Ziff. I.2 lit. a) bis c) bezeichneten Waren liegt zumindest hochgradige Verwechslungs"
        "gefahr (§ 14 Abs. 2 Nr. 2 MarkenG; Art. 9 Abs. 2 lit. b UMV) vor; die Zeichenähnlichkeit "
        "beträgt nach von uns durchgeführter visueller Analyse mindestens 87 % (Krönchen-Monogramm "
        "K°°). Die Warenidentität ist gegeben.", S_NORMAL))
    s.append(Paragraph(
        "2. Hinsichtlich der Flakons (Ziff. I.2 lit. d) liegt eine Verletzung der 3D-Formmarke "
        "EU 008 776 015 vor; jedenfalls aber besteht eine Rufausbeutung der bekannten Marke "
        "i.S.v. § 14 Abs. 2 Nr. 3 MarkenG. Die unterscheidungskräftige Stellung des asymmetrischen "
        "Stopfens — die nach dem Ergebnis von Verkehrsbefragungen (vgl. <i>Allensbach IfD 2024</i>: "
        "73 % Zuordnungsgrad bei Premiumkonsumenten) — wird offenkundig ausgebeutet.", S_NORMAL))
    s.append(Paragraph(
        "3. Die Verteidigungsmöglichkeit der Erschöpfung (§ 24 MarkenG; Art. 15 UMV) scheidet "
        "aus. Unsere Mandantin unterhält ein selektives Vertriebssystem (vgl. EuGH, 06.12.2017, "
        "C-230/16 — <i>Coty Germany/Akzente</i>; sowie EuGH, 13.10.2011, C-439/09 — "
        "<i>Pierre Fabre Dermo-Cosmétique</i>), das ausschließlich an autorisierte Boutiquen "
        "vertreibt. Die Brezelmann Discount KG ist nicht autorisierter Vertriebspartner. Eine "
        "Inverkehrbringung im EWR mit Zustimmung der Mandantin (§ 24 Abs. 1 MarkenG) wird "
        "ausdrücklich bestritten.", S_NORMAL))
    s.append(Paragraph(
        "4. Hilfsweise berufen wir uns auf § 14 Abs. 2 Nr. 3 MarkenG (Bekanntheitsschutz). Die "
        "Mandantin gilt nach unanfechtbarer Verkehrsdurchsetzung (vgl. BGH, 27.03.2013 — I ZB 56/12, "
        "<i>Test</i>) als bekannte Marke im EU-Inland. Es liegt eine unlautere Ausnutzung der "
        "Wertschätzung vor.", S_NORMAL))
    s.append(Paragraph("<b>III. Aufforderung</b>", S_H3))
    s.append(Paragraph(
        "Wir fordern Sie hiermit auf, bis spätestens "
        "<b>Freitag, 06.02.2026, 12:00 Uhr</b>", S_NORMAL))
    s.append(Paragraph(
        "die anliegende <b>strafbewehrte Unterlassungs- und Verpflichtungserklärung</b> "
        "(Anlage K 3 — siehe Folgeblatt) ohne jede Änderung rechtsverbindlich unterzeichnet "
        "zurückzusenden, ferner Auskunft über Bezugsquellen, Liefermengen und Abnehmer zu "
        "erteilen sowie unsere bisherigen Kosten in Höhe einer 2,5-fachen Geschäftsgebühr nach "
        "RVG aus einem Gegenstandswert von <b>EUR 1.200.000,00</b> zzgl. Auslagenpauschale und "
        "Umsatzsteuer, mithin <b>EUR 12.471,40</b>, zu erstatten.", S_NORMAL))
    s.append(Paragraph(
        "Für den Fall fruchtlosen Fristablaufs behalten wir uns die unverzügliche gerichtliche "
        "Geltendmachung (einstweilige Verfügung beim Landgericht Frankfurt am Main, hilfsweise "
        "Hauptsacheklage) — sowie strafrechtliche Anzeige nach § 143 MarkenG — ausdrücklich vor.", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Mit vorzüglicher Hochachtung", S_NORMAL))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("gez. <b>Dr. Dr. Annabella Steinacker-von Tarsis</b>, LL.M. (Cantab.)", S_NORMAL_LEFT))
    s.append(Paragraph("Rechtsanwältin · Fachanwältin für gewerblichen Rechtsschutz", S_SMALL))
    return s

story += blatt_abmahnung_brezelmann()
story.append(PageBreak())

# Unterlassungserklärung (Anlage K 3)
def blatt_unterlassungserklaerung():
    s = []
    s.append(Paragraph("<b>ANLAGE K 3</b> — Strafbewehrte Unterlassungs- und Verpflichtungserklärung", S_H2))
    s.append(HLine())
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Hiermit verpflichtet sich die <b>Brezelmann Discount KG</b>, Wurstgasse 4, 97980 Bad "
        "Mergentheim, vertreten durch ihren Komplementär Herrn Dipl.-Kfm. Egon Brezelmann, "
        "gegenüber der <b>klôtzzkètté S.A.</b>, Paris (im Folgenden: <i>die Gläubigerin</i>), "
        "es bei Meidung einer für jeden Fall der Zuwiderhandlung fällig werdenden, in das Ermessen "
        "der Gläubigerin gestellten und im Streitfall durch das zuständige Gericht zu überprüfenden "
        "Vertragsstrafe (vgl. BGH, 24.10.2019 — <b>I ZR 35/19</b>, GRUR 2020, 401 — "
        "<i>Vertragsstrafenklausel</i>) zu unterlassen,", S_NORMAL))
    s.append(Paragraph(
        "1. im geschäftlichen Verkehr ohne Zustimmung der Gläubigerin Bekleidungsstücke, "
        "Halstücher, Taschen, Schuhe, Parfumflakons und Parfümerieartikel anzubieten, in "
        "den Verkehr zu bringen, einzuführen, auszuführen oder zu bewerben, die mit dem "
        "Zeichen „K°°“ (silbern, golden oder farblos) und/oder dem Schriftzug „klôtzzkètté“, "
        "„klotzkette“, „klotzkettie“, „klötzkette“ oder einem anderen mit den vorgenannten "
        "Zeichen verwechslungsfähigen Zeichen versehen sind;", S_NORMAL))
    s.append(Paragraph(
        "2. insbesondere die in Anlage K 3.1 abgebildeten Produkte (T-Shirts BTM-MEN-022, "
        "Halstücher BTM-WMN-118, Handtaschen BTM-BAG-K044, Parfumflakons „K-Royal“) anzubieten, "
        "zu vertreiben oder bewerben zu lassen;", S_NORMAL))
    s.append(Paragraph(
        "3. der Gläubigerin innerhalb von zehn (10) Werktagen nach Annahme dieser Erklärung "
        "Auskunft zu erteilen über (a) Bezugsquellen und Lieferanten, (b) Lagerbestände, "
        "(c) Liefermengen, Lieferzeiten und -preise, (d) Abnehmer, (e) Werbeaufwendungen, "
        "(f) erzielten Umsatz und Gewinn (gestaffelt nach Modellbezeichnung) — jeweils belegt "
        "durch Rechnungskopien;", S_NORMAL))
    s.append(Paragraph(
        "4. der Gläubigerin Schadensersatz nach Wahl der Gläubigerin nach den Grundsätzen "
        "der dreifachen Schadensberechnung (entgangener Gewinn / Lizenzanalogie / "
        "Verletzergewinn) — Höhe nach abgeschlossener Auskunft — zu leisten;", S_NORMAL))
    s.append(Paragraph(
        "5. die Anwaltskosten der Gläubigerin in Höhe von EUR 12.471,40 (2,5-fache "
        "Geschäftsgebühr nach RVG, Streitwert EUR 1.200.000,00 zzgl. Auslagenpauschale und "
        "Umsatzsteuer) zu erstatten.", S_NORMAL))
    s.append(Spacer(1, 0.5*cm))
    s.append(Paragraph("Bad Mergentheim, den ____________________", S_NORMAL_LEFT))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("________________________________________", S_NORMAL_LEFT))
    s.append(Paragraph("Brezelmann Discount KG, vertreten durch Egon Brezelmann (Komplementär)", S_SMALL))
    s.append(Spacer(1, 0.5*cm))
    # Eingangsstempel - imitiert
    s.append(StampBox("zur Akte gen.\nReg-Nr 26-0188\nfrist 06.02.2026\nWiedervorl. 09.02.\n— hk —",
                       angle=-7, color=colors.HexColor("#225522"), w=5.4*cm, h=2.6*cm))
    s.append(Spacer(1, 0.3*cm))
    s.append(HandNote(
        "Brezelmann hat NICHT unterschrieben — also EINSTW. VFG.\nFax-Antwort siehe Bl. 12 — frech und gewerblich gefärbt.\n→ Pitti Uomo abwarten, dann zuschlagen!  ASt",
        font=FONT_HAND, size=14, color=colors.HexColor("#7a1f1f"), w=14*cm, angle=-0.4))
    return s

story += blatt_unterlassungserklaerung()
story.append(PageBreak())

print("[part02] done")
