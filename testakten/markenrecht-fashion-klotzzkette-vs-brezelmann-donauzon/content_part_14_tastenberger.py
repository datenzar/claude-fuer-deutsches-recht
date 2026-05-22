# Part 14: Sachverständigengutachten Prof. Tastenberger (TU Darmstadt)
def blatt_tastenberger_1():
    s = []
    s.append(Paragraph("<b>SACHVERSTÄNDIGENGUTACHTEN — Textilhaptik</b>", S_CENTER))
    s.append(Paragraph(
        "Prof. Dr.-Ing. Hieronymus Tastenberger · Lehrstuhl für Textilhaptik · "
        "Technische Universität Darmstadt", S_CENTER))
    s.append(Paragraph("Karolinenplatz 5 · 64289 Darmstadt", S_CENTER))
    s.append(HLine())
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>I. Auftrag und Fragestellung</b>", S_H3))
    s.append(Paragraph(
        "Mit Schreiben der Kanzlei Steinacker Lichtenberg &amp; Partners IP vom 19.02.2026 wurde "
        "ich beauftragt, ein Sachverständigengutachten zu erstellen zur Frage, ob die "
        "Webstruktur der Schalskollektion „K°° Touch Royal“ der klôtzzkètté S.A. (drei sich "
        "kreuzende Rauten, Seiden-Twill 18 momme) eine haptisch <b>unterscheidungskräftige "
        "Markenform</b> i.S.d. § 3 MarkenG, Art. 4 UMV, darstellt, und ob diese unter "
        "Berücksichtigung der Sieckmann-Kriterien (EuGH C-273/00) <b>hinreichend klar und "
        "eindeutig dargestellt</b> werden kann.", S_NORMAL))
    s.append(Paragraph("<b>II. Untersuchungsobjekt</b>", S_H3))
    s.append(Paragraph(
        "Vorgelegt wurden: (a) 5 Schal-Quadrate à 20×20 cm aus laufender Produktion 2025/26 "
        "der klôtzzkètté S.A. (Charge K-TR-2025-04); (b) Bezugsschal des Premium-Konkurrenten "
        "<i>maison hermès</i> (für Vergleichsmessung); (c) eines aktuellen Imitationsproduktes "
        "der Brezelmann Discount KG (Modell BTM-WMN-118, beschlagnahmt 12.03.2026 Pitti Uomo).",
        S_NORMAL))
    s.append(Paragraph("<b>III. Methodik</b>", S_H3))
    s.append(Paragraph(
        "Die Untersuchung erfolgte mit den am Lehrstuhl etablierten Methoden:", S_NORMAL))
    methods = [
        ["#", "Methode", "Gerät / Standard"],
        ["1", "Konfokal-Mikroskopie (3D-Profilkarte)",
         "Olympus LEXT OLS5100, Auflösung 5 µm × 5 µm × 0,1 µm"],
        ["2", "Reibungskoeffizient (Kawabata KES-FB4)",
         "Kato Tech Co., µ-Bestimmung in Web- und Schussrichtung"],
        ["3", "Sensorisches Panel (haptische Diskriminierung)",
         "n = 28 Prüferinnen (textil-haptisch geschult), "
         "Doppelblindversuch nach DIN ISO 4121"],
        ["4", "REM (Rasterelektronenmikroskopie)",
         "Zeiss LEO 1530 VP, 200× — 5.000× Vergrößerung"],
        ["5", "Tribo-Akustik-Spektrum",
         "Eigenentwicklung TU Darmstadt 2022, „TouchSound“-System"],
    ]
    t = Table(methods, colWidths=[0.8*cm, 6.5*cm, 8.7*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 8.5),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1c2e4a")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888888")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f5f1e6")]),
    ]))
    s.append(t)
    s.append(Paragraph("<b>IV. Ergebnisse</b>", S_H3))
    s.append(Paragraph(
        "<b>1. Konfokal-Mikroskopie:</b> Die Webstruktur weist eine reproduzierbare 3-Rauten-"
        "Diagonalprägung mit Kantenlänge 14,3 ± 0,4 mm und mittlerer Reliefamplitude 0,118 mm "
        "± 0,015 mm auf. Die Standardabweichung zwischen den 5 Vergleichsmustern liegt unter "
        "12 % — also reproduzierbar und beständig.", S_NORMAL))
    s.append(Paragraph(
        "<b>2. KES-Reibungsmessung:</b> Reibungskoeffizient in Diagonalrichtung "
        "µ = 0,182 (in Webrichtung µ = 0,154; in Schussrichtung µ = 0,167). Die <i>Anisotropie</i> "
        "ist signifikant; insbesondere der „Stick-Slip“-Effekt beim Streichen in Diagonale ist "
        "klar tastbar (haptische Frequenz ca. 8 Hz, dem menschlichen Tastsinn zugänglich, "
        "vgl. Tastenberger/Federmann, Textilhaptik 2018, S. 247 ff.).", S_NORMAL))
    s.append(Paragraph(
        "<b>3. Sensorisches Panel:</b> 24 von 28 Prüferinnen (= 86 %) konnten den klôtzzkètté-"
        "Twill bei Blindverkostung („Tastverkostung“) richtig identifizieren — gegenüber 71 % "
        "beim Hermès-Bezugsschal und nur 11 % beim Brezelmann-Imitat (welches "
        "ohne ertastbare Rauten-Struktur kommt — die Rauten sind lediglich aufgedruckt, nicht "
        "eingewebt).", S_NORMAL))
    return s

story += blatt_tastenberger_1()
story.append(PageBreak())

def blatt_tastenberger_2():
    s = []
    s.append(Paragraph("<b>— Gutachten Tastenberger, Bl. 2/2 —</b>", S_RIGHT))
    # ASCII Profilkarte
    profile = (
"  3D-Konfokal-Profilkarte — Schal K°° Touch Royal — Diagonalansicht:    \n"
"                                                                         \n"
"  z [µm]                                                                 \n"
"   ^                                                                     \n"
"  120│           ╱╲          ╱╲          ╱╲                              \n"
"     │          ╱  ╲        ╱  ╲        ╱  ╲                             \n"
"   80│         ╱    ╲      ╱    ╲      ╱    ╲     Raute 1 / 2 / 3        \n"
"     │        ╱      ╲    ╱      ╲    ╱      ╲    (jeweils Kante 14,3mm) \n"
"   40│       ╱        ╲  ╱        ╲  ╱        ╲                          \n"
"     │      ╱          ╲╱          ╲╱          ╲                         \n"
"    0│_____╱______________________________________________╲____         \n"
"          0    7    14   21   28   35   42   49   56   63   x [mm]      \n"
"                                                                         \n"
"  µ = 0,182 (45° Diagonalrichtung, Stick-Slip 8 Hz)                      \n"
"  Stoffgewicht: 18 momme (54 g/m²)                                       \n"
"  Reproduzierbarkeit:  SD < 12 % (n = 5 Charge K-TR-2025-04)             \n"
    )
    s.append(ASCIIBox(profile, font="Courier", size=8, color=colors.HexColor("#221100"),
                      caption="3D-Konfokal-Profilkarte — Anlage K-HAP-3"))
    s.append(Paragraph("<b>V. Rechtliche Würdigung (im Lichte von § 3 MarkenG / Art. 4 UMV / EuGH)</b>", S_H3))
    s.append(Paragraph(
        "Aus textil-haptischer und materialwissenschaftlicher Sicht ist die Webstruktur "
        "<i>distinkt</i>, <i>reproduzierbar</i> und <i>für den Menschen tast-bar</i>. Die "
        "Kombination aus (a) verbaler Beschreibung der Drei-Rauten-Struktur, (b) Konfokal-3D-"
        "Profilkarte mit metrischen Toleranzen, (c) KES-Reibungsdaten, (d) sensorischem "
        "Panel-Befund (86 % Wiedererkennungsquote) sowie (e) hinterlegter Probe in inerter "
        "Polycarbonat-Schachtel erfüllt die Sieckmann-Kriterien (C-273/00) — soweit eine "
        "<i>Haptikmarke</i> als „sonstige Marke“ i.S.v. Art. 4 UMV grundsätzlich anerkannt wird.",
        S_NORMAL))
    s.append(Paragraph(
        "Im übrigen ist auf die Reform der UMV (VO 2017/1001) hinzuweisen, welche das Erfordernis "
        "der grafischen Darstellbarkeit gelockert hat — die heutige technologische Realität "
        "(Konfokal-Mikroskopie, KES-Mess-Suiten, digitale 3D-Profile) ermöglicht eine "
        "Darstellung, die zur Sieckmann-Zeit (2002) noch nicht denkbar war.", S_NORMAL))
    s.append(Paragraph("<b>VI. Schlussfolgerung</b>", S_H3))
    s.append(Paragraph(
        "Aus naturwissenschaftlicher Sicht ist die haptische Markenform „K°° Touch Royal“ "
        "(Drei-Rauten-Webstruktur) als <b>distinkt, reproduzierbar und klar darstellbar</b> "
        "zu beurteilen. Ich empfehle die Eintragung — die rechtliche Anerkennung obliegt "
        "selbstverständlich dem DPMA bzw. dem EUIPO.", S_NORMAL))
    s.append(Paragraph(
        "Ich erkläre hiermit gem. § 410 ZPO, dass ich das Gutachten nach bestem Wissen und "
        "Gewissen erstattet habe und in keiner persönlichen oder geschäftlichen Abhängigkeit "
        "zur Auftraggeberin stehe. <i>Venire contra factum proprium</i>: ich habe in 12 "
        "vergangenen Gutachten zugunsten von Wettbewerbern der klôtzzkètté S.A. votiert.",
        S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Darmstadt, 04.03.2026", S_NORMAL_LEFT))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("<i>Prof. Dr.-Ing. Hieronymus Tastenberger</i>", S_NORMAL_LEFT))
    s.append(Paragraph("Lehrstuhl für Textilhaptik · TU Darmstadt", S_SMALL))
    s.append(Spacer(1, 0.4*cm))
    s.append(HandNote(
        "Tastenberger hat sich gefreut — sein 88. Gutachten überhaupt.\nHonorar EUR 18.000 + Reise EUR 642,80 — abrechenbar.\nGutachten 100 % bestätigend, Comtesse wird VERZÜCKT sein.\n→ Replik DPMA vorbereiten — falls je Beanstandung kommt.",
        font=FONT_HAND, size=13, color=colors.HexColor("#1e3a6e"), w=14*cm, angle=-0.3))
    return s

story += blatt_tastenberger_2()
story.append(PageBreak())

print("[part14] done")
