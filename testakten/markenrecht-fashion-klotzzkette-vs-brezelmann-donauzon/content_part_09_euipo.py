# Part 09: EUIPO-Korrespondenz Widerspruch + Riechmarke-Beschwerde + Soundmarke
def blatt_euipo_widerspruchsschrift():
    s = []
    s.append(Paragraph("<b>EUROPEAN UNION INTELLECTUAL PROPERTY OFFICE</b>", S_CENTER))
    s.append(Paragraph("Avenida de Europa, 4 · E-03008 Alicante", S_CENTER))
    s.append(Paragraph("— Opposition Division —", S_CENTER))
    s.append(HLine())
    s.append(Paragraph("<b>Widerspruchsverfahren B 4 187 932</b>", S_CENTER))
    s.append(Paragraph("(klôtzzkètté S.A. ./. UAB klotzkettie)", S_CENTER))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>WIDERSPRUCHSSCHRIFT</b>", S_H2))
    s.append(Paragraph(
        "im Namen und Auftrag der Widersprechenden<br/>"
        "<b>klôtzzkètté S.A.</b>, 12 rue du Faubourg Saint-Honoré, 75008 Paris, Frankreich,<br/>"
        "vertreten durch <i>Steinacker Lichtenberg &amp; Partners IP Boutique</i>, München (DE), "
        "EUIPO-Vertreter-Nr. 88472,", S_NORMAL))
    s.append(Paragraph("<b>g e g e n</b>", S_CENTER))
    s.append(Paragraph(
        "die Markenanmeldung <b>EUTM 019 412 880</b> „<b>klotzkettie</b>“ der <b>UAB klotzkettie</b>, "
        "Vilniaus g. 47, LT-01402 Vilnius, Litauen, angemeldet am 09.01.2026, veröffentlicht im "
        "Unionsmarkenblatt am 13.01.2026, Nizza-Klassen 3, 14, 18, 25, 35.", S_NORMAL))
    s.append(Paragraph("<b>I. Widerspruchsgrund</b>", S_H3))
    s.append(Paragraph(
        "Der Widerspruch stützt sich auf <b>Art. 8 Abs. 1 lit. b</b> UMV (Verwechslungsgefahr) "
        "sowie hilfsweise <b>Art. 8 Abs. 5</b> UMV (Schutz bekannter Marken), gestützt auf die "
        "nachstehenden älteren Marken der Widersprechenden:", S_NORMAL))
    s.append(Paragraph(
        "(a) EU 005 412 880 „klôtzzkètté“ (Wortmarke, Prio. 14.05.2008);<br/>"
        "(b) EU 010 988 411 „klôtzzkètté + K°°-Monogramm“ (Wort-/Bildmarke, Prio. 04.06.2012);<br/>"
        "(c) DPMA 30 2014 077 312 (Bildmarke, Krönchen silber-emailliert, Prio. 22.10.2014);<br/>"
        "(d) EUIPO 015 887 442 (Positionsmarke, Prio. 17.08.2016).", S_NORMAL))
    s.append(Paragraph("<b>II. Argumentation</b>", S_H3))
    s.append(Paragraph(
        "1. <b>Zeichenähnlichkeit</b>. Die angegriffene Marke „klotzkettie“ ist mit der älteren "
        "Wortmarke „klôtzzkètté“ klanglich identisch (siehe phonetische Transkription "
        "[ˈklɔt͡skɛti] vs. [ˈklɔt͡skɛti]; identisch zu 100 %). Visuell: 9 von 11 Buchstaben "
        "identisch (82 %), Abweichung lediglich Doppel-Z vs. Einzel-Z und Akzentsetzung. "
        "Konzeptuell: bedeutungsleer für den Verkehr, daher konzeptuelle Neutralität "
        "(vgl. EuGH, 22.06.1999, C-342/97 — <i>Lloyd</i>, Rn. 25).", S_NORMAL))
    s.append(Paragraph(
        "2. <b>Warenidentität</b>. Beide Marken beanspruchen u.a. Klassen 3, 14, 18, 25, 35 mit "
        "identischen oder hochgradig ähnlichen Spezifikationen.", S_NORMAL))
    s.append(Paragraph(
        "3. <b>Erhöhte Kennzeichnungskraft</b>. Die Widersprechende ist Inhaberin einer "
        "100-jährigen Maison de Luxe; Verkehrsdurchsetzung der Marke „klôtzzkètté“ in EU-Inland "
        "ist nachgewiesen (Verkehrsbefragung Allensbach IfD 2024, Zuordnungsgrad 73 % im Premium"
        "konsumentensegment). Es liegt eine bekannte Marke i.S.d. Art. 8 Abs. 5 UMV vor.", S_NORMAL))
    s.append(Paragraph(
        "4. <b>Bösgläubigkeit</b>. Hilfsweise wird auf <b>Art. 59 Abs. 1 lit. b</b> UMV "
        "verwiesen; die Anmeldung der UAB klotzkettie erfolgt erkennbar in Anlehnung an die "
        "ältere Marke und in Kenntnis der bestehenden Schutzrechte. Ein paralleles Verfahren "
        "vor dem LG Frankfurt a.M. (Az. 2-03 O 412/26) richtet sich gegen den deutschen "
        "Abnehmer der UAB (Brezelmann Discount KG); die strukturelle Verbindung zwischen "
        "der UAB und der deutschen Brezelmann KG ist mithin <i>liquide</i>.", S_NORMAL))
    s.append(Paragraph("<b>III. Antrag</b>", S_H3))
    s.append(Paragraph(
        "Es wird beantragt, der Markenanmeldung EUTM 019 412 880 die Eintragung für sämtliche "
        "beanspruchten Klassen zu versagen und der Anmelderin die Verfahrenskosten aufzuerlegen "
        "(Art. 109 UMV).", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("München / Alicante, 03.04.2026", S_NORMAL_LEFT))
    s.append(Paragraph("gez. Dr. Dr. A. Steinacker-von Tarsis, LL.M. (Cantab.)", S_NORMAL_LEFT))
    s.append(Paragraph("EUIPO-Vertreter-Nr. 88472", S_SMALL))
    return s

story += blatt_euipo_widerspruchsschrift()
story.append(PageBreak())

# ---- EUIPO Beanstandungsschreiben Riechmarke
def blatt_euipo_riechmarke():
    s = []
    s.append(Paragraph("<b>EUROPEAN UNION INTELLECTUAL PROPERTY OFFICE</b>", S_CENTER))
    s.append(Paragraph("— Office Action / Examiner's Notice —", S_CENTER))
    s.append(HLine())
    s.append(Paragraph("<b>Ref.: 019 122 776 — Olfactory Mark — klôtzzkètté S.A.</b>", S_RIGHT))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Sehr geehrte Damen und Herren,", S_NORMAL))
    s.append(Paragraph(
        "die mit Anmeldung vom 14.07.2024 eingereichte <b>Geruchsmarke</b> der klôtzzkètté S.A., "
        "bezeichnet als „<i>Akkord aus Iris pallida, weißer Birne und feuchtem Wildleder</i>“, "
        "wird hiermit nach Vor-Prüfung gemäß Art. 7 UMV i.V.m. Art. 4 UMV (klare und eindeutige "
        "Darstellbarkeit) beanstandet.", S_NORMAL))
    s.append(Paragraph("<b>Beanstandungsgründe:</b>", S_H3))
    s.append(Paragraph(
        "1. Die eingereichte Beschreibung („<i>Akkord aus Iris pallida, weißer Birne und feuchtem "
        "Wildleder</i>“) genügt nicht den vom Gerichtshof in der Sache <b>EuGH, 12.12.2002, "
        "C-273/00 — Sieckmann/DPMA</b>, GRUR 2003, 145, aufgestellten Anforderungen an die "
        "<b>klare, eindeutige, in sich abgeschlossene, leicht zugängliche, verständliche, "
        "dauerhafte und objektive grafische Darstellung</b>. Die verbalen Umschreibungen sind "
        "weder klar (was ist „feuchtes“ Wildleder?), noch objektiv (Iris-pallida-Konzentration "
        "wird nicht angegeben), noch dauerhaft (Geruchsempfindung ist subjektiv).", S_NORMAL))
    s.append(Paragraph(
        "2. Die zusätzlich eingereichten <b>Gaschromatographie-Spektrogramme</b> "
        "(MS-Identifikation 7 Hauptpeaks: Methylionon 18 %, Damascone 12 %, …) sowie eine "
        "Probe in einem Glasflakon (Hinterlegung beim EUIPO-Magazin am 14.07.2024) erfüllen "
        "die Sieckmann-Kriterien ebenfalls nicht, da sie nicht <i>für jedermann ohne weiteres "
        "verständlich</i> sind.", S_NORMAL))
    s.append(Paragraph(
        "3. Auch die <b>nach VO (EU) 2017/1431 zulässigen elektronischen Formate</b> "
        "(MP4-Video der „Riech-Aufführung“, Sounddatei „Atemzug der Comtesse beim Riechen“) "
        "bringen aus oben genannten Gründen die olfaktorische Botschaft nicht klar zum "
        "Ausdruck.", S_NORMAL))
    s.append(Paragraph("<b>Frist zur Stellungnahme:</b> 2 Monate ab Zustellung.", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Alicante, 14.09.2025", S_NORMAL_LEFT))
    s.append(Paragraph("gez. Examiner Pedro García-Fernández, EUIPO Examination Division",
                        S_SMALL))
    s.append(Spacer(1, 0.4*cm))
    # Eingangsstempel
    s.append(StampBox("eingegangen\n22.09.2025\nSchriftsatz pflicht.\nWiedervorl. 13.11.\n— hk —",
                       angle=-9, color=colors.HexColor("#225522"), w=5.0*cm, h=2.4*cm))
    s.append(Spacer(1, 0.4*cm))
    s.append(HandNote(
        "Riechmarke ist NICHT zu retten ohne Sieckmann-Reform.\nBeschwerde zur BoA einlegen — Argument: neue VO 2017/1431,\nMP3+GC-MS-Diagramm ZUSAMMEN = klar bestimmt.\n→ Lit.: Hacker/Thiering, MarkenG, § 8 Rn. 102 ff.\nAhler in WRP 2024, 1488; Mlle Périgord-Gutachten bestellen!",
        font=FONT_HAND, size=13, color=colors.HexColor("#7a1f1f"), w=15*cm, angle=-1.4))
    return s

story += blatt_euipo_riechmarke()
story.append(PageBreak())

# Beschwerde an EUIPO BoA gegen Riechmarken-Zurückweisung
def blatt_euipo_beschwerde():
    s = []
    s.append(Briefkopf(
        KANZLEI_ADDR,
        "European Union Intellectual Property Office\nBoards of Appeal\nAvenida de Europa, 4\nE-03008 Alicante\nSpain",
        "13.11.2025", "Sch-Lich 25-1622 / EUIPO 019 122 776"))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<b>Beschwerde gegen die Zurückweisungsentscheidung der Prüfungsabteilung "
        "betr. die Geruchsmarke „Iris pallida — weiße Birne — feuchtes Wildleder“ "
        "(EUIPO Nr. 019 122 776) — Anmelderin: klôtzzkètté S.A.</b>", S_H3))
    s.append(Paragraph(
        "Ladies and Gentlemen of the Boards of Appeal,", S_NORMAL))
    s.append(Paragraph(
        "im Namen und Auftrag der Beschwerdeführerin <b>klôtzzkètté S.A.</b> legen wir hiermit "
        "form- und fristgerecht <b>Beschwerde</b> gegen die Zurückweisungsentscheidung der "
        "Prüfungsabteilung vom 14.09.2025 (zugestellt am 22.09.2025) ein und beantragen die "
        "Aufhebung der Entscheidung sowie die Eintragung der Marke unter Berücksichtigung der "
        "nachstehenden ergänzenden Beschreibung und Beweismittel.", S_NORMAL))
    s.append(Paragraph("<b>I. Argumentation</b>", S_H3))
    s.append(Paragraph(
        "1. Die Voraussetzungen der <b>Sieckmann-Entscheidung</b> (EuGH C-273/00) sind in der "
        "Sache fortgeschrieben durch das Gerichtsurteil <b>EuGH, 27.11.2003, C-283/01 — "
        "Shield Mark/Kist</b> (Hörmarken-Notenschrift) sowie durch die Reformverordnung "
        "<b>VO (EU) 2017/1001 i.V.m. der Durchführungsverordnung (EU) 2018/626</b>, welche das "
        "Erfordernis der grafischen Darstellung aufgehoben und durch das Erfordernis einer "
        "<i>klaren, präzisen, leicht zugänglichen, in sich abgeschlossenen, beständigen und "
        "objektiven Darstellung in jeder geeigneten Form unter Anwendung allgemein zugänglicher "
        "Technologie</i> ersetzt hat (Art. 3 Abs. 1 DV).", S_NORMAL))
    s.append(Paragraph(
        "2. Die Kombination aus (a) verbaler Beschreibung des Duftakkords, (b) Gaschromatographie-"
        "Massenspektrogramm (vorgelegt als Anlage B 1 — vgl. Anlage K-OLF-1 dieser Akte), "
        "(c) Probekarte aus inertem Material (Anlage B 2) sowie (d) Sachverständigengutachten "
        "Mlle Hortense Périgord, Olfaktorik-Sachverständige Grasse, vom 02.11.2025 (Anlage B 3) "
        "erfüllt diese Anforderungen mutatis mutandis. <i>Mutatis mutandis</i> deshalb, weil "
        "die technologische Realität (GC-MS-Analyse, digitale Sensorik) heute Lösungen "
        "ermöglicht, die zur Sieckmann-Zeit (2002) noch nicht bestanden.", S_NORMAL))
    s.append(Paragraph(
        "3. Hilfsweise: Sollte die BoA die Sieckmann-Kriterien weiterhin als unerfüllt erachten, "
        "regen wir die <b>Vorlage zur Vorabentscheidung an den EuGH</b> nach Art. 267 AEUV an, "
        "ob die VO (EU) 2017/1001 die Sieckmann-Rechtsprechung wirksam überholt hat (vgl. "
        "Schlussanträge GA Pikamäe in Rs. C-371/19 zu sensorischen Marken — die Frage ist offen).",
        S_NORMAL))
    s.append(Paragraph(
        "<b>Antrag:</b> Aufhebung der Entscheidung der Prüfungsabteilung vom 14.09.2025; "
        "Eintragung der Marke EUIPO 019 122 776; hilfsweise Vorlage an EuGH.", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("München, 13.11.2025", S_NORMAL_LEFT))
    s.append(Paragraph("gez. Dr. Dr. A. Steinacker-von Tarsis", S_NORMAL_LEFT))
    return s

story += blatt_euipo_beschwerde()
story.append(PageBreak())

print("[part09] done")
