# Part 11: Olfaktorik-Gutachten Mlle Périgord (3 Seiten)
def blatt_olfaktorik_1():
    s = []
    s.append(Paragraph("<b>SACHVERSTÄNDIGENGUTACHTEN</b>", S_CENTER))
    s.append(Paragraph("<i>betreffend die Geruchsmarke EUIPO 019 122 776</i>", S_CENTER))
    s.append(Paragraph("Antragstellerin: klôtzzkètté S.A., Paris", S_CENTER))
    s.append(HLine())
    s.append(Paragraph("<i>Mlle Hortense Périgord — Olfaktorik-Sachverständige —</i>", S_RIGHT))
    s.append(Paragraph("Atelier des Senteurs · 14 Avenue Maximin Isnard · F-06130 Grasse", S_RIGHT))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>I. Gegenstand des Auftrags</b>", S_H3))
    s.append(Paragraph(
        "Mit Schreiben vom 02.10.2025 hat mich die Kanzlei Steinacker Lichtenberg &amp; Partners "
        "IP (München) im Auftrag der klôtzzkètté S.A. (Paris) beauftragt, eine sachverständige "
        "Stellungnahme zur Möglichkeit der klaren, präzisen, in sich abgeschlossenen, leicht "
        "zugänglichen, verständlichen, dauerhaften und objektiven Darstellung des "
        "Duftakkords „Iris pallida — weiße Birne — feuchtes Wildleder“ im Sinne der "
        "Rechtsprechung des EuGH (C-273/00 — <i>Sieckmann</i>) abzugeben, "
        "ferner zur sachgerechten Charakterisierung mittels moderner chromatographischer und "
        "spektroskopischer Verfahren.", S_NORMAL))
    s.append(Paragraph("<b>II. Untersuchungsmaterial</b>", S_H3))
    s.append(Paragraph(
        "Bereitgestellt wurden: (a) ein 25-ml-Glasflakon mit der streitgegenständlichen "
        "Duftkomposition; (b) Datenblatt der Komponenten (Iris-pallida-Extrakt 18 %, "
        "Pyrus-communis-Acetatfraktion 12 %, Suède-Mousse-Accord 24 %, Träger Triäthyl-Citrat "
        "46 %); (c) Gaschromatographie-Massenspektrogramme (GC-MS) der Analytik-Werkstatt "
        "Lemonniex (Cannes) vom 18.10.2025.", S_NORMAL))
    s.append(Paragraph("<b>III. Methodik</b>", S_H3))
    s.append(Paragraph(
        "Zur Untersuchung kamen folgende Verfahren zum Einsatz: (1) klassische sensorische "
        "Analyse durch ein 7-köpfiges Expertenpanel (École de Parfumerie Grasse, Diplom 2018+); "
        "(2) GC-MS-Analyse (Agilent 7890B / 5977A; Säule HP-5MS UI, 30 m × 0,25 mm × 0,25 µm; "
        "Temperaturprogramm 60 °C — 280 °C, 10 °C/min); (3) elektronische Nase (Heracles Neo, "
        "Alpha M.O.S., Toulouse) — Kreuzkorrelation mit Datenbank Sycomore-3.", S_NORMAL))
    s.append(Paragraph("<b>IV. Sensorischer Befund</b>", S_H3))
    s.append(Paragraph(
        "Die sensorische Beschreibung des Duftakkords lautet (Konsens des Panels, "
        "Übereinstimmung 6/7 in der Hauptcharakteristik): „Iris-pallida-Aufschlag (Kopfnote, "
        "0—15 min) mit subtiler, leicht puddingartiger Süße der weißen Birne (Kopf-bis-"
        "Herznote, 5—45 min); im Abklang öffnet sich eine warme, feuchte Wildleder-Note "
        "(Suède mouillé), die an mit Regen benetzte Hirschledersohlen erinnert (Basisnote, "
        "30 min—4 h).“ Die Komposition ist olfaktorisch <i>distinkt</i> und in keinem mir "
        "bekannten Vergleichsstoff wiederzufinden.", S_NORMAL))
    s.append(Paragraph("<b>V. GC-MS-Befund</b>", S_H3))
    s.append(Paragraph(
        "Die GC-MS-Analyse identifiziert 7 dominante Peaks (relative Anteile in Klammern):",
        S_NORMAL))
    peaks = [
        ["Peak", "Retentionszeit [min]", "Substanz (Identifikation NIST 2020)", "Rel. Anteil"],
        ["1", "8.42", "α-Methyl-Ionon", "18,4 %"],
        ["2", "10.17", "α-Damascon (Suède-Akkord, Schlüsselsubstanz)", "11,9 %"],
        ["3", "11.84", "Hexyl-Phenyl-Acetat (weiße Birne, Acetatfraktion)", "9,1 %"],
        ["4", "13.22", "γ-Heptalacton (Birnen-Cremigkeit)", "5,7 %"],
        ["5", "15.66", "Iso-E Super (Holzakkord, Träger)", "14,2 %"],
        ["6", "18.04", "Cetonal (Wildleder-Sublimat)", "6,3 %"],
        ["7", "22.18", "Castoréum-Equivalent (synth., Suède-Boden)", "4,8 %"],
    ]
    t = Table(peaks, colWidths=[1.2*cm, 3.0*cm, 8.6*cm, 2.5*cm], repeatRows=1)
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
    return s

story += blatt_olfaktorik_1()
story.append(PageBreak())

def blatt_olfaktorik_2():
    s = []
    s.append(Paragraph("<b>— Gutachten Périgord, Bl. 2/3 —</b>", S_RIGHT))
    # ASCII spectrogram
    spectro = (
"  GC-MS Total Ion Chromatogram (TIC) — klôtzzkètté EU 019 122 776     \n"
"                                                                       \n"
"  Intensität                                                           \n"
"     ^                                                                 \n"
"   100│              ⬢                                                 \n"
"     │              ⬢⬢                                                \n"
"    80│             ⬢⬢⬢                ⬢                              \n"
"     │           ⬢ ⬢⬢⬢⬢              ⬢⬢                              \n"
"    60│          ⬢⬢ ⬢⬢⬢⬢          ⬢ ⬢⬢⬢            ⬢                \n"
"     │         ⬢⬢⬢ ⬢⬢⬢⬢⬢       ⬢⬢ ⬢⬢⬢⬢          ⬢⬢                \n"
"    40│        ⬢⬢⬢⬢ ⬢⬢⬢⬢⬢      ⬢⬢⬢⬢⬢⬢⬢ ⬢        ⬢⬢⬢   ⬢⬢          \n"
"     │       ⬢⬢⬢⬢⬢ ⬢⬢⬢⬢⬢⬢ ⬢ ⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢      ⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢          \n"
"    20│   ⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢⬢          \n"
"     │___|____|____|____|____|____|____|____|____|____|____|____|____|\n"
"        5   8   10  12  14  16  18  20  22  24  26  28  30   t [min]  \n"
"                                                                       \n"
"   Peaks identifiziert (NIST 2020, Match ≥ 86):                        \n"
"   #1  α-Methyl-Ionon              #5  Iso-E Super                     \n"
"   #2  α-Damascon                  #6  Cetonal                         \n"
"   #3  Hexyl-Phenyl-Acetat         #7  Castoréum-Equivalent            \n"
"   #4  γ-Heptalacton                                                   \n"
    )
    s.append(ASCIIBox(spectro, font="Courier", size=7.5,
                      color=colors.HexColor("#220020"),
                      caption="Total Ion Chromatogram — Anlage K-OLF-2"))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>VI. Rechtliche Bewertung der Darstellbarkeit (im Lichte von Sieckmann)</b>",
                        S_H3))
    s.append(Paragraph(
        "Aus olfaktorischer Sicht erfüllt die vorgelegte Komposition die im EuGH-Urteil "
        "<i>Sieckmann</i> (C-273/00) entwickelten sieben Kriterien — sofern die kombinierte "
        "Darstellung aus (1) verbaler Beschreibung, (2) quantitativer Zusammensetzung in "
        "Gewichtsprozent, (3) GC-MS-Spektrogramm mit Substanzidentifizierung gemäß NIST-Datenbank, "
        "(4) E-Nase-Referenz im Sycomore-3-System und (5) physischer Hinterlegungsprobe in inertem "
        "Borosilikatglas zugrunde gelegt wird. Die <i>klare und präzise</i> Darstellung ist "
        "gegeben (Tab. V); die <i>Beständigkeit</i> wird durch GC-MS-Wiederholungsmessung im "
        "Abstand von 6 Monaten (Differenz Hauptpeaks &lt; 3,2 %) belegt; die <i>objektive "
        "Zugänglichkeit</i> ist durch jede zugelassene Analytik-Werkstatt nachprüfbar.", S_NORMAL))
    s.append(Paragraph(
        "Das EuGH-Urteil <i>Sieckmann</i> stammt aus dem Jahre 2002 und ist in seinem rein "
        "<b>technischen Verständnis von „grafischer Darstellbarkeit“</b> heute überholt; das "
        "Erfordernis ist in der Reformverordnung VO (EU) 2017/1001 i.V.m. DV (EU) 2018/626 "
        "ersetzt durch das Erfordernis einer <i>angemessenen Darstellungsform unter Verwendung "
        "allgemein zugänglicher Technologie</i> (Art. 3 Abs. 1 DV). Es spricht — aus "
        "naturwissenschaftlicher Sicht — alles dafür, dass die heute verfügbare Analytik die "
        "Sieckmann-Hürde überwindet.", S_NORMAL))
    s.append(Paragraph("<b>VII. Schlussfolgerung</b>", S_H3))
    s.append(Paragraph(
        "Die Komposition „Iris pallida — weiße Birne — feuchtes Wildleder“ ist olfaktorisch "
        "<i>distinkt</i>, technisch <i>vollständig charakterisierbar</i> und naturwissenschaftlich "
        "geeignet, im Markenregister geführt zu werden — die rechtliche Anerkennung als "
        "schutzfähige Marke obliegt selbstverständlich dem EUIPO bzw. der BoA.", S_NORMAL))
    return s

story += blatt_olfaktorik_2()
story.append(PageBreak())

def blatt_olfaktorik_3():
    s = []
    s.append(Paragraph("<b>— Gutachten Périgord, Bl. 3/3 —</b>", S_RIGHT))
    s.append(Paragraph("<b>VIII. Honorar und Beweismittel-Verzeichnis</b>", S_H3))
    s.append(Paragraph(
        "Honorar: 24 Std. à EUR 380,00 = EUR 9.120,00 zzgl. Reisekosten Grasse — München "
        "(EUR 1.180,40) und Laborkosten Lemonniex (EUR 4.450,00), Gesamtsumme EUR 14.750,40 "
        "(netto, zzgl. französischer TVA 20 %; Rechnung folgt gesondert).", S_NORMAL))
    bv = [
        ["Lfd. Nr.", "Beweismittel"],
        ["K-OLF-1", "GC-MS Spektrogramm 18.10.2025 (Lemonniex, Cannes)"],
        ["K-OLF-2", "Total Ion Chromatogram (vorstehende Abb.)"],
        ["K-OLF-3", "GC-MS Referenzmessung 18.04.2025 (Wiederholungstest, Beständigkeit)"],
        ["K-OLF-4", "Sensorisches Panel-Protokoll Grasse 21.10.2025 (7 Prüferinnen)"],
        ["K-OLF-5", "Heracles Neo E-Nase-Ausdruck mit Sycomore-3-Match"],
        ["K-OLF-6", "Hinterlegungsprobe Borosilikatglas (versiegelt, EUIPO-Magazin)"],
        ["K-OLF-7", "Komponenten-Sicherheitsdatenblatt (Iris-Extrakt, Pyrus-Acetat etc.)"],
        ["K-OLF-8", "Foto der Probe (Glas, Etikett, Siegel)"],
    ]
    t = Table(bv, colWidths=[2.2*cm, 13.8*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#3a2c1a")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888888")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f5f1e6")]),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Ich erkläre hiermit gemäß Art. 78 UMV i.V.m. § 410 ZPO, dass ich das vorliegende "
        "Gutachten nach bestem Wissen und Gewissen, unparteiisch und unter Berücksichtigung "
        "des aktuellen wissenschaftlichen Standes erstattet habe. Ich bin von der "
        "Antragstellerin in keiner Weise — weder finanziell, persönlich noch beruflich — "
        "abhängig.", S_NORMAL))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph("Grasse, 02.11.2025", S_NORMAL_LEFT))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<i>Hortense Périgord</i>", S_NORMAL_LEFT))
    s.append(Paragraph("Olfaktorik-Sachverständige · Mitglied de la Société Française des Parfumeurs",
                        S_SMALL))
    s.append(Spacer(1, 0.5*cm))
    s.append(HandNote(
        "Mlle Périgord war 3 Tage in München — sehr beeindruckend.\nComtesse hat sie zum Abendessen ins Käfer eingeladen.\nNebenbei: P. hält das Castoréum-Equivalent (Peak 7) für »banal« —\nempfiehlt für die Neuanmeldung 2027 echte Birken-Knospenharzfraktion.\n→ MvB notieren!",
        font=FONT_HAND, size=13, color=colors.HexColor("#1e3a6e"), w=15*cm, angle=-0.6))
    return s

story += blatt_olfaktorik_3()
story.append(PageBreak())

print("[part11] done")
