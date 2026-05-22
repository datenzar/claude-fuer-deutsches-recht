# Part 30: ASCII-Art Logo-Skizzen, Verletzungsform-Vergleich, interne Memos, Verkehrsbefragung
def blatt_ascii_logo_compare():
    s = []
    s.append(Paragraph("<b>LOGO- UND VERLETZUNGSFORM-VERGLEICH</b>", S_H1))
    s.append(Paragraph("Anlage zur Berufung 6 W 47/26 — Blatt 47 / B-2 (Aktualisierung)",
                        S_SMALL))
    s.append(HLine())
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("<b>I.  Originalmarke K°° (eingetragen EUTM 017 224 119)</b>", S_H3))
    s.append(ASCIIBox(
        "        .-^^^^^^^^^^^^^^^^^^-.\n"
        "      .'      ___           '.\n"
        "     /     .-'   '-.            \\\n"
        "    /     /   /^\\   \\            \\\n"
        "   |     |   |   |   |            |\n"
        "    \\     \\   \\_/   /            /\n"
        "     \\     '-...-'             /\n"
        "      '.       K°°          .'\n"
        "        '-..__________..-'\n"
        "             |||||||  \n"
        "         _ __|_____|__ _ \n"
        "        / KLÔTZZKÈTTÉ \\\n"
        "       /__1923 · PARIS_\\",
        caption="Fig. 1 — Original K°°-Krone (Schutzgegenstand; Marke nicht maßstabsgetreu)"))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>II.  Verletzungsform „klotzkettiee“ (Brezelmann/UAB klotzkettie)</b>",
                        S_H3))
    s.append(ASCIIBox(
        "       .-~~~~~~~~~~~~~~~~~~~~-.\n"
        "     .'      ___                '.\n"
        "    /     .-'   '-.                \\\n"
        "   /     /   /-\\   \\                \\\n"
        "  |     |   | x |   |                |\n"
        "   \\     \\   \\_/   /                /\n"
        "    \\     '-...-'                 /\n"
        "     '.       Ko o            .'\n"
        "       '-..______________..-'\n"
        "            |||||||||  \n"
        "        _ __|_______|__ _ \n"
        "       / klotzkettiee  \\\n"
        "      /__limited edition_\\",
        caption="Fig. 2 — Verletzungsform; Zweck der Imitation evident (Krone, Schriftzug, Layout)"))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>III.  Verletzungsform „klotzkettie“ (UAB / EUTM-Anmeldung)</b>",
                        S_H3))
    s.append(ASCIIBox(
        "      _________________________\n"
        "     | KLOTZKETTIE             |\n"
        "     |       (no diacritics)   |\n"
        "     |    ___________          |\n"
        "     |   /  XX  XX  /\\         |\n"
        "     |  /          /  \\        |\n"
        "     | / [ Ko o ] /    \\       |\n"
        "     |/__________/      \\      |\n"
        "     |__________________\\______|",
        caption="Fig. 3 — Variante Vilnius; Krone schematisiert ohne Diakritik"))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>IV.  Maße der Krone (Original Antoine-Louis Klôtzzkètté 1923-Skizze, "
                        "reproduziert nach Hausarchiv Paris)</b>", S_H3))
    s.append(ASCIIBox(
        "         <--- 4.20 cm --->\n"
        "        ^   .---^---.       \n"
        "        |  /  /^\\  \\       \n"
        " 2.80   | /  /   \\  \\       \n"
        "  cm    ||  |  K  |  ||      \n"
        "        | \\  \\   /  /       \n"
        "        |  \\__\\_/_/         \n"
        "        v   |     |          \n"
        "            |_____|          \n"
        "        <--- 3.10 cm --->",
        caption="Fig. 4 — Maßzeichnung mit eingetragenen Proportionen; "
                "Höhen-Breiten-Verhältnis 2:3 (golden ratio-nah)"))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph(
        "Die kombinierte Gegenüberstellung der Figuren 1–4 zeigt unmittelbar: Die "
        "Verletzungsformen sind nicht zufällig ähnlich, sondern bewusst übernommen. "
        "Insbesondere die <i>Position</i> des Schriftzugs unter dem Kronenmotiv und die "
        "<i>Bandbreite</i> der dreischichtigen Zackenung sind 1:1 reproduziert. "
        "Querverweis: Sachverständigengutachten Prof. Dr. H. Steinpfeil, Bl. 89 ff.",
        S_NORMAL))
    return s

story += blatt_ascii_logo_compare()
story.append(PageBreak())

def blatt_haptik_ascii():
    s = []
    s.append(Paragraph("<b>HAPTIK-MARKEN-DARSTELLUNG — ANLAGE ZU DPMA 30 2026 102 887/888</b>",
                        S_H1))
    s.append(Paragraph("Erfahrungsschema des Tastreliefs für Schaltuch &amp; Flakon "
                        "(reproduziert nach Tastenberger 22.04.2026)", S_SMALL))
    s.append(HLine())
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph(
        "<b>1.  „K°° Touch Royal“ — Seiden-Twill 18 momme — Rautenkreuz-Schema</b>",
        S_H3))
    s.append(ASCIIBox(
        "    /\\    /\\    /\\    /\\    /\\\n"
        "   /  \\  /  \\  /  \\  /  \\  /  \\\n"
        "  /    \\/    \\/    \\/    \\/    \\\n"
        "  \\    /\\    /\\    /\\    /\\    /\n"
        "   \\  /  \\  /  \\  /  \\  /  \\  /\n"
        "    \\/    \\/    \\/    \\/    \\/\n"
        "    /\\    /\\    /\\    /\\    /\\\n"
        "   /  \\  /  \\  /  \\  /  \\  /  \\\n"
        "  / R1 \\/ R2 \\/ R3 \\/ R1 \\/ R2 \\\n"
        "  \\    /\\    /\\    /\\    /\\    /\n"
        "   \\  /  \\  /  \\  /  \\  /  \\  /\n"
        "    \\/    \\/    \\/    \\/    \\/\n"
        "    R1 = Hauptraute  (4.0 mm × 4.0 mm × 18 momme)\n"
        "    R2 = Verstärkungsraute (3.0 × 3.0, leicht gehoben)\n"
        "    R3 = Tertiärraute (2.0 × 2.0, eingelassen)\n"
        "    Periodizität: 9.4 mm in beide Richtungen",
        caption="Schema 1 — Drei kreuzende Rauten R1, R2, R3 — Haptik-Marker · DPMA 102 887"))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<b>2.  „K°° pour Femme“-Flakon — Bergkristall-Effekt — Reliefskizze</b>", S_H3))
    s.append(ASCIIBox(
        "             _____\n"
        "            /     \\        ← Cabochon-Kappe (matt-frostiert)\n"
        "           |   Â   |        ← Erhabenes „K°°“ in 1.2 mm-Relief\n"
        "           |       |\n"
        "         __|_______|__\n"
        "        /             \\\n"
        "       /  /\\  /\\  /\\   \\\n"
        "      |  /  \\/  \\/  \\   |   ← Facettierte Bergkristall-Reliefs\n"
        "      | /  / K \\  / K \\ |     (52 Facetten total, je 1.8 mm)\n"
        "      |/__/____\\/_____\\|\n"
        "      |              ___ |\n"
        "      |  K°°  pour  Femme|   ← Eingravierter Schriftzug 0.4 mm\n"
        "      |________________ |\n"
        "       \\______________/\n"
        "          Bodenring (poliert, glatt)",
        caption="Schema 2 — Hexagonaler Bergkristall-Flakon · DPMA 102 888 / USPTO 97/884.120"))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>3.  Test-Apparatur — Tastenberger TU Darmstadt</b>", S_H3))
    s.append(ASCIIBox(
        "    +----------------------------------------+\n"
        "    |    TU DARMSTADT — Lehrstuhl Textilhaptik|\n"
        "    |       Tribometer-Setup TKT-04          |\n"
        "    +----------------------------------------+\n"
        "          ___                  ___\n"
        "    [ load cell ]======[ stylus tip ]\n"
        "         ||                     ||\n"
        "    -----||----[ silk twill specimen ]----\n"
        "         ||                     ||\n"
        "      probe        sample       probe\n"
        "    Friction coefficient measured @ 0.5 N normal load",
        caption="Schema 3 — Tribometer-Anordnung Tastenberger; Friktionskoeffizient "
                "0.21–0.24 (Original) vs. 0.42 (Imitation)"))
    s.append(Paragraph(
        "Querverweis: Tastenberger-Gutachten Bl. 91–93, Ergänzungsgutachten Bl. 122. "
        "Friktionsdifferenz von Faktor 2 ist sensorisch <i>unmittelbar</i> wahrnehmbar.",
        S_SMALL))
    return s

story += blatt_haptik_ascii()
story.append(PageBreak())

def blatt_verkehrsbefragung():
    s = []
    s.append(Paragraph("<b>VERKEHRSBEFRAGUNG — IPSOS-MORI DE/AT/CH</b>", S_H1))
    s.append(Paragraph("Anlage B-45 zur Berufung OLG; Anlage S-1 zur EUIPO BoA-Antwort",
                        S_SMALL))
    s.append(HLine())
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph(
        "Im Auftrag der Kanzlei Steinacker Lichtenberg &amp; Partners hat IPSOS-MORI "
        "Deutschland in der Zeit vom 12.04. bis 28.04.2026 eine repräsentative Erhebung "
        "zur Bekanntheit der Marke KLÔTZZKÈTTÉ und ihrer Bildkomponenten durchgeführt. "
        "Stichprobenumfang: n = 2.014 (DE), n = 612 (AT), n = 488 (CH); Methodik: "
        "CAWI + telefonische Vertiefungs-Interviews (CATI) bei 380 Premium-Konsumenten.",
        S_NORMAL))
    rows = [
        ["Frage / Item", "DE", "AT", "CH", "Gewichtet"],
        ["Ungestützte Markenbekanntheit (Top-of-Mind „Luxus-Mode“)", "8,4 %", "11,2 %",
         "18,7 %", "9,8 %"],
        ["Gestützte Markenbekanntheit (KLÔTZZKÈTTÉ?)", "41,2 %", "46,8 %",
         "63,4 %", "44,8 %"],
        ["Markeneinschätzung „luxuriös“ (Top-Box)", "84,1 %", "82,5 %",
         "89,2 %", "84,7 %"],
        ["Markeneinschätzung „Pariser Herkunft“ korrekt", "76,8 %", "78,4 %",
         "81,1 %", "77,5 %"],
        ["Erkennung K°°-Logo (Pflichtwahl)", "52,1 %", "55,3 %", "67,4 %",
         "54,2 %"],
        ["Erkennung K°°-Logo (mit gleichzeitig „klotzkettiee“-Logo)", "61,3 %",
         "60,2 %", "70,8 %", "62,1 %"],
        ["Verwechslung KLÔTZZKÈTTÉ ↔ klotzkettiee (Top-Box: „gleiche Marke“)",
         "44,2 %", "41,8 %", "39,4 %", "43,1 %"],
        ["Verwechslung KLÔTZZKÈTTÉ ↔ klotzkettie (Top-Box)", "47,7 %", "45,1 %",
         "42,8 %", "46,5 %"],
        ["Spontane Assoziation „Brezelmann“ ↔ KLÔTZZKÈTTÉ", "0,4 %", "0,2 %",
         "0,1 %", "0,3 %"],
        ["Käuferinnen-Profil: HH-Netto &gt; 8.000 €/Mon (Premium-Segment)", "6,2 %",
         "7,1 %", "12,4 %", "7,4 %"],
        ["Anteil Käuferinnen, die ein Imitations-Schaltuch akzeptabel finden",
         "11,8 %", "9,4 %", "7,2 %", "10,4 %"],
    ]
    t = Table(rows, colWidths=[7.5*cm, 2.0*cm, 2.0*cm, 2.0*cm, 2.3*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 8.5),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1c2e4a")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888")),
        ("ALIGN", (1,1), (-1,-1), "CENTER"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f5f1e6")]),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<b>Wesentliche Ergebnisse zur prozessrelevanten Beurteilung:</b>", S_H3))
    items = [
        "(a) Gestützte Bekanntheit der Marke KLÔTZZKÈTTÉ in DE: 41,2 % — übersteigt die "
        "vom BGH (I ZR 21/01 — POST) für „bekannte Marke“ akzeptierte Schwelle von 40 %;",
        "(b) Verwechslungsquote 43–47 % zwischen KLÔTZZKÈTTÉ und klotzkettiee/klotzkettie "
        "im DACH-Raum belegt unmittelbare Verwechslungsgefahr;",
        "(c) Premium-Segment-Käuferinnen (HH-Netto &gt; 8.000 €) erkennen die Marke "
        "korrekt in 84,7 % der Fälle — die einschlägige Verkehrsauffassung;",
        "(d) Die unter (c) genannten Probandinnen lehnen Imitate zu 89,6 % ab "
        "(„nicht acceptable“) — was den Imageschaden der Mandantin durch die "
        "Marktdiffusion belegt.",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Diese Befunde stützen sowohl die Erhöhung des Schadens-Quotienten nach der "
        "Lizenzanalogie als auch die Bejahung des Ruf-Schutzes nach § 14 Abs. 2 Nr. 3 "
        "MarkenG bzw. Art. 8(5) EUTMR.", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(HandNote(
        "44 %! Comtesse wird das lieben.\n"
        "Aber: 11 % der Käuferinnen akzeptieren Imitate.\n"
        "→ daraus folgt: Brezelmann-Klientel überschneidet sich\n"
        "  mit klôtzzkètté-Markt in messbarem Umfang.\n"
        "→ Schadensschätzung nach Marktanteil-Modell justifiziert.\n"
        "— A.St., 06.05.26",
        font=FONT_HAND, size=14, angle=0.3, w=15*cm))
    return s

story += blatt_verkehrsbefragung()
story.append(PageBreak())

print("[part30] done")
