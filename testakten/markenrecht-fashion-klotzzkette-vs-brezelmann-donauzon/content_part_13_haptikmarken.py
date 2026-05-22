# Part 13: Haptikmarken-Anmeldung DPMA / EUIPO / USPTO (Schal + Flakon)
def blatt_haptik_memo():
    s = []
    s.append(Paragraph("<b>INTERNES MEMO — Haptikmarken-Strategie</b>", S_CENTER))
    s.append(HLine())
    s.append(Paragraph(
        "Verfasser: Dr. Dr. A. Steinacker-von Tarsis (ASt)<br/>"
        "Co-Bearb.: M. v. Brenkenhoff (MvB)<br/>"
        "Datum: 18.02.2026<br/>"
        "Anlass: Anfrage der Comtesse vom 12.02.2026 — Haptikmarken für Schal-Kollektion "
        "„K°° Touch Royal“ und für Parfumflakon-Oberfläche; parallel DPMA / EUIPO / USPTO.",
        S_NORMAL))
    s.append(Paragraph("<b>I. Sachverhalt</b>", S_H3))
    s.append(Paragraph(
        "Die Mandantin betreibt seit 2024 die Premium-Schalskollektion „K°° Touch Royal“. "
        "Verwendet wird ein Seiden-Twill mit 18 momme Stoffgewicht. Charakteristisch ist eine "
        "spezifische Web-Struktur, die — beim Streichen mit den Fingerspitzen über die Oberfläche "
        "in Diagonalrichtung — ein eindeutig ertastbares Muster aus <b>drei sich kreuzenden "
        "Rauten</b> aufweist. Diese Haptik ist nach unseren Untersuchungen (1) <b>distinkt</b> "
        "gegenüber marktüblichen Twill-Webungen, (2) <b>reproduzierbar</b> und (3) für den "
        "Premium-Konsumenten als Herkunftshinweis erkennbar (Verbraucherbefragung Allensbach "
        "IfD 2025, n=2.412, Zuordnungsgrad 68 %).", S_NORMAL))
    s.append(Paragraph(
        "Ferner soll die <b>geschliffene Bergkristall-Oberfläche</b> des Parfumflakons "
        "„K°° pour Femme“, mit fühlbaren Krönchen-Reliefs an drei Stellen (Schulter, Bauch, "
        "Boden), als Haptikmarke geschützt werden.", S_NORMAL))
    s.append(Paragraph("<b>II. Rechtliche Würdigung</b>", S_H3))
    s.append(Paragraph(
        "1. Die <b>haptische Marke</b> (Tastmarke) ist nach geltendem Markenrecht zwar nicht "
        "explizit benannt, jedoch nach <i>EuGH, 12.12.2002, C-273/00 — Sieckmann</i> sowie "
        "<i>EuGH, 27.11.2003, C-283/01 — Shield Mark/Kist</i> grundsätzlich als „sonstige "
        "Aufmachung“ markenfähig — sofern die Anforderungen an klare und eindeutige "
        "Darstellbarkeit erfüllt sind. Die VO (EU) 2017/1001 (Reform der UMV) hat das Erfordernis "
        "der grafischen Darstellung gelockert; ein digitales Modell mit Reliefkartierung "
        "(Höhenprofil in mm-Auflösung) genügt aus unserer Sicht.", S_NORMAL))
    s.append(Paragraph(
        "2. Die <b>Unterscheidungskraft</b> ist nach <i>EuGH, 12.06.2018, C-163/16 — "
        "Louboutin/van Haren</i>, GRUR 2018, 802, zu prüfen. Bei Louboutin (rote Schuhsohle) "
        "wurde die Position der Farbe als markentauglich anerkannt; übertragen auf eine "
        "Tastmarke bedeutet dies: Die haptische Empfindung kann unabhängig von der visuellen "
        "Erscheinung Herkunftshinweis sein.", S_NORMAL))
    s.append(Paragraph(
        "3. <b>Erwartete Beanstandungen</b>: (a) mangelnde abstrakte Unterscheidungskraft "
        "(§ 3 Abs. 1 MarkenG / Art. 4 UMV); (b) Sieckmann-Kriterien nicht erfüllt; "
        "(c) Klassen-Konkretisierungs-Beanstandung.", S_NORMAL))
    s.append(Paragraph("<b>III. Vorgehen</b>", S_H3))
    s.append(Paragraph(
        "(1) Parallelanmeldung DPMA (30 2026 102 887 — Schal; 30 2026 102 888 — Flakon); "
        "(2) Parallelanmeldung EUIPO (in Vorbereitung); "
        "(3) USPTO-Anmeldung 97/884.121 über die NY-Kanzlei Whitman Brennan Forsythe LLP "
        "(parallele Lanham-Act-Argumentation, Wal-Mart v. Samara Bros. + Louboutin-Logik); "
        "(4) Sachverständigengutachten <b>Prof. Dr. Hieronymus Tastenberger</b>, TU Darmstadt, "
        "Lehrstuhl für Textilhaptik, in Auftrag — Honorar pauschal EUR 18.000 zzgl. Reisekosten;"
        " (5) Beweismittel: haptisches Musterstück 10×10 cm Schal-Twill (Anlage K-HAP-1), "
        "Flakon-Schnittzeichnung mit Reliefhöhen in mm (Anlage K-HAP-2).", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(HandNote(
        "Comtesse hat das Musterstück (10×10 cm) persönlich aus Paris\nmitgebracht — bewahre es im Tresor des Büros auf.\nReliefhöhen Flakon: 0,8 mm Schulter / 1,2 mm Bauch / 0,4 mm Boden.\n→ siehe Anlage K-HAP-2 (Schnittzeichnung von Atelier Cremieux Paris)\n— ASt 18.02.",
        font=FONT_HAND, size=14, color=colors.HexColor("#1e3a6e"), w=15*cm, angle=-0.5))
    return s

story += blatt_haptik_memo()
story.append(PageBreak())

# DPMA Anmeldung Haptikmarke Schal
def blatt_haptik_anmeldung_schal():
    s = []
    s.append(Briefkopf(
        KANZLEI_ADDR,
        "Deutsches Patent- und Markenamt\nMarkenstelle - Haptische Marken\nZweibrückenstraße 12\n80331 München",
        "21.02.2026", "Sch-Lich 26-0211 / DPMA Anm. 30 2026 102 887"))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<b>Anmeldung einer Haptikmarke (Tastmarke) gem. § 3 i.V.m. § 8 Abs. 1 MarkenG</b>",
        S_H3))
    s.append(Paragraph(
        "Sehr geehrte Damen und Herren,", S_NORMAL))
    s.append(Paragraph(
        "namens und in Vollmacht der Anmelderin <b>klôtzzkètté S.A.</b> beantragen wir hiermit "
        "die Eintragung folgender Marke:", S_NORMAL))
    rows = [
        ["Markenform:", "Haptische Marke / Tastmarke (haptische Markenform sui generis)"],
        ["Bezeichnung:", "K°° TOUCH ROYAL — Drei-Rauten-Webstruktur"],
        ["Substrat:", "Seiden-Twill mit Stoffgewicht 18 momme (54 g/m²)"],
        ["Haptische Definition:", "Beim Streichen mit der Fingerspitze über die Oberfläche "
                                  "in Diagonalrichtung (45° zur Webrichtung) ergibt sich ein "
                                  "ertastbares Muster aus drei sich gleichseitig kreuzenden "
                                  "Rauten, jeweils mit Kantenlänge ca. 14 mm, Tiefenamplitude "
                                  "ca. 0,12 mm."],
        ["Klassen (Nizza 12. Ed.):", "24 (Webstoffe und Textilwaren), 25 (Bekleidung)"],
        ["Beweismittel:", "Anlage K-HAP-1: haptisches Musterstück 10×10 cm (in Probedöschen "
                          "Borosilikatglas, versiegelt)"],
        ["", "Anlage K-HAP-3: 3D-Profilkarte aus Konfokal-Mikroskopie "
              "(Auflösung 5 µm × 5 µm × 0,1 µm)"],
        ["", "Anlage K-HAP-4: Sachverständigengutachten Prof. Dr. H. Tastenberger "
              "(TU Darmstadt, Lehrstuhl Textilhaptik) — folgt"],
        ["Anmelderin:", "klôtzzkètté S.A., 12 rue du Faubourg Saint-Honoré, 75008 Paris (FR)"],
    ]
    t = Table(rows, colWidths=[4.4*cm, 12.0*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9),
        ("FONTNAME", (0,0), (0,-1), "Times-Bold"),
        ("BOX", (0,0), (-1,-1), 0.3, colors.HexColor("#777777")),
        ("INNERGRID", (0,0), (-1,-1), 0.15, colors.HexColor("#bbbbbb")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>Begründung der Markenfähigkeit</b>", S_H3))
    s.append(Paragraph(
        "Die haptische Marke erfüllt die Markenfähigkeitsvoraussetzungen des § 3 MarkenG. Sie "
        "ist (a) <b>geeignet</b>, Waren eines Unternehmens von denen anderer zu unterscheiden, "
        "wie die als Anlage beigefügten Verbraucherbefragungen (Allensbach IfD 2025) belegen "
        "(Zuordnungsgrad 68 %); (b) <b>klar und eindeutig darstellbar</b> durch die Kombination "
        "aus (i) Wortbeschreibung, (ii) Konfokal-Mikroskopie-Profilkarte mit metrischen "
        "Tiefenangaben, (iii) hinterlegter Probe in inertem Glas — was die Sieckmann-Kriterien "
        "(EuGH C-273/00) <i>mutatis mutandis</i> erfüllt; (c) <b>schutzfähig</b>, da die "
        "Webstruktur weder technisch bedingt (§ 3 Abs. 2 Nr. 2 MarkenG) noch der Ware ihren "
        "wesentlichen Wert verleiht (§ 3 Abs. 2 Nr. 3 MarkenG) ist — sondern lediglich ein "
        "Herkunftshinweis ist.", S_NORMAL))
    s.append(Paragraph(
        "Auf <i>EuGH, 12.06.2018, C-163/16 — Louboutin/van Haren</i>, GRUR 2018, 802, wird "
        "Bezug genommen: Auch bei Tastmarken ist allein zu prüfen, ob das gekennzeichnete Element "
        "vom Verkehr als Herkunftshinweis verstanden wird. Eine bloße ästhetische oder "
        "funktionelle Ausgestaltung steht nicht entgegen.", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("München, 21.02.2026 — gez. ASt &amp; MvB", S_NORMAL_LEFT))
    return s

story += blatt_haptik_anmeldung_schal()
story.append(PageBreak())

# Haptikmarke Flakon - Anmeldung + Reliefkarte
def blatt_haptik_anmeldung_flakon():
    s = []
    s.append(Briefkopf(
        KANZLEI_ADDR,
        "Deutsches Patent- und Markenamt\nMarkenstelle - Haptische Marken\nZweibrückenstraße 12\n80331 München",
        "21.02.2026", "Sch-Lich 26-0212 / DPMA Anm. 30 2026 102 888"))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<b>Anmeldung einer Haptikmarke (Tastmarke) — Parfumflakon K°° pour Femme</b>", S_H3))
    s.append(Paragraph(
        "Sehr geehrte Damen und Herren,", S_NORMAL))
    s.append(Paragraph(
        "namens und in Vollmacht der Anmelderin <b>klôtzzkètté S.A.</b> melden wir hiermit "
        "die folgende Haptikmarke zur Eintragung an:", S_NORMAL))
    s.append(Paragraph("<b>Beschreibung der haptischen Erscheinung</b>", S_H3))
    s.append(Paragraph(
        "Der Parfumflakon „K°° pour Femme“ (3D-Formmarke EU 008 776 015) weist auf seiner "
        "äußeren Oberfläche drei fühlbare Krönchen-Reliefs auf, jeweils nach Methode des "
        "<i>geschliffenen Bergkristalls</i> aus dem Glas geschliffen, durchschnittliche "
        "Reliefhöhe in mm wie folgt:", S_NORMAL))
    rows = [
        ["Position", "Reliefhöhe", "Durchmesser", "Tiefenstruktur"],
        ["Schulter (oberes Drittel)", "0,80 mm ± 0,05", "12 mm", "konkav-konvexer Wechsel"],
        ["Bauch (mittleres Drittel)", "1,20 mm ± 0,05", "18 mm", "konvex, dominantes Krönchen"],
        ["Boden (unteres Drittel)", "0,40 mm ± 0,05", "8 mm", "graviert, mit „K°°“-Kürzel"],
    ]
    t = Table(rows, colWidths=[4.5*cm, 3.0*cm, 3.0*cm, 5.5*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1c2e4a")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888888")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f5f1e6")]),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    # ASCII Reliefkarte
    relief = (
"   Flakon-Schnittzeichnung mit Reliefhöhen in mm:                    \n"
"                                                                      \n"
"                  ___________                                         \n"
"                 /           \\                                        \n"
"                |   K°° K°°   | <- Schulter, Reliefhöhe 0,80 mm       \n"
"                |     0,8mm   |                                       \n"
"                +-------------+                                       \n"
"               /               \\                                      \n"
"              |   K°°   K°°    | <- Bauch, Reliefhöhe 1,20 mm         \n"
"              |     1,2 mm     |    (dominantes Krönchen-Relief)      \n"
"              |                |                                      \n"
"               \\______________/                                       \n"
"                |   K°°  K°°  |  <- Boden, Reliefhöhe 0,40 mm         \n"
"                |    0,4 mm   |     (graviert, mit Kürzel)            \n"
"                +=============+                                       \n"
"                                                                      \n"
"   Gesamthöhe Flakon  : 137 mm                                        \n"
"   Maximale Breite   :  54 mm  (Hexagonalbauch)                       \n"
"   Schliff-Methode   : Naturkristall-Schliff, manuell, à la main       \n"
"   Atelier           : Cristallerie de Saint-Louis (FR)               \n"
    )
    s.append(ASCIIBox(relief, font="Courier", size=8, color=colors.HexColor("#220020"),
                      caption="Anlage K-HAP-2: Flakon-Schnittzeichnung mit Reliefhöhen"))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Die haptische Definition ist objektiv, klar und eindeutig: Bei tastender Berührung "
        "des Flakons werden die drei Krönchen-Reliefs an den genannten Positionen mit den "
        "genannten Reliefhöhen erfahren. Eine Verkehrsbefragung (Allensbach IfD 2025) ergab, "
        "dass 71 % der Premium-Konsumentinnen den Flakon allein anhand der Haptik (verbundene "
        "Augen-Tasttest) der Maison klôtzzkètté zuordnen.", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("München, 21.02.2026 — gez. ASt &amp; MvB", S_NORMAL_LEFT))
    return s

story += blatt_haptik_anmeldung_flakon()
story.append(PageBreak())

print("[part13] done")
