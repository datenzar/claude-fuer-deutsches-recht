# Part 15: BPatG-Verhandlungsprotokoll-Auszug + BGH-Hinweisbeschluss Soundmarke
def blatt_bpatg_protokoll():
    s = []
    s.append(Paragraph("<b>BUNDESPATENTGERICHT</b>", S_CENTER))
    s.append(Paragraph("25. Senat — Markenbeschwerdesenat", S_CENTER))
    s.append(HLine())
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>Az. 25 W (pat) 88/26</b>", S_RIGHT))
    s.append(Paragraph("<b>VERHANDLUNGSPROTOKOLL — AUSZUG —</b>", S_CENTER))
    s.append(Paragraph("öffentliche Sitzung vom 16.04.2026", S_CENTER))
    s.append(Spacer(1, 0.2*cm))
    meta = [
        ["Sitzung:", "öffentlich, mündliche Verhandlung gem. § 69 MarkenG"],
        ["Vorsitzender:", "Vors. Richter am BPatG Dr. Knipperdolling"],
        ["Beisitzer:", "Richter am BPatG Heyderich; Richterin am BPatG Dr. Schmidt-Bösse"],
        ["Sachverständige Anhörung:", "Prof. Dr. Hieronymus Steinpfeil (Marken-Kommentator, München)"],
        ["Verfahrensgegenstand:", "Beschwerde der klôtzzkètté S.A. gegen Teilzurückweisung der "
                                   "Anmeldung DPMA 30 2024 442 188 („LE LUXE EST UN DROIT NATUREL“) "
                                   "wegen § 8 Abs. 2 Nr. 2 MarkenG (Freihaltebedürfnis)"],
        ["Anwesend:", "Anmelderin durch RAin Dr. Dr. Steinacker-von Tarsis"],
        ["", "Vertreter DPMA: Markenprüfer ORR Dr. Wieckenberg"],
    ]
    t = Table(meta, colWidths=[4.5*cm, 12.0*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("FONTNAME", (0,0), (0,-1), "Times-Bold"),
        ("BOX", (0,0), (-1,-1), 0.3, colors.HexColor("#777777")),
        ("INNERGRID", (0,0), (-1,-1), 0.15, colors.HexColor("#bbbbbb")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Der Vorsitzende eröffnet die Sitzung um 10:04 Uhr und stellt fest, dass die Beteiligten "
        "ordnungsgemäß geladen sind. Sodann gibt er den Sachverhalt vor:", S_NORMAL))
    proto = (
"  PROTOKOLL — wörtliche Wiedergabe der Diskussion\n"
"  ===============================================\n"
"\n"
"  Vors.RaBPatG Dr. Knipperdolling:\n"
"    \"Frau Dr. Dr. Steinacker, das DPMA hat den Slogan teilweise\n"
"    wegen § 8 Abs. 2 Nr. 2 MarkenG zurückgewiesen — Freihaltebedürfnis.\n"
"    Was sagen Sie zu der Argumentation, dass der Slogan rein\n"
"    beschreibend sei?\"\n"
"\n"
"  RAin Dr. Dr. Steinacker:\n"
"    \"Hohes Senat — der Slogan 'LE LUXE EST UN DROIT NATUREL'\n"
"    ist kein beschreibender Hinweis. Er ist ein philosophischer\n"
"    Anspruch, eine Wertaussage. Der Verkehr wird ihn als Aussage\n"
"    der Mandantin verstehen, nicht als Sachhinweis. Vergleichbar\n"
"    BGH I ZB 18/16 - 'Lambertz Werks Brote'.\"\n"
"\n"
"  Dr. Schmidt-Bösse:\n"
"    \"Aber das Wort 'luxe' selbst ist doch rein beschreibend für\n"
"    luxuriöse Waren in Klasse 25?\"\n"
"\n"
"  RAin Steinacker:\n"
"    \"Mit Verlaub — das Französische ist als Fremdsprache für den\n"
"    inländischen Durchschnittsverbraucher in der Klasse 25 nicht\n"
"    ohne weiteres verständlich. Verweise auf EuGH C-191/01 -\n"
"    'Doublemint' und BGH I ZB 19/13 - 'für eine bessere Welt'.\"\n"
"\n"
"  Prof. Steinpfeil (Sachverständiger):\n"
"    \"Aus markentheoretischer Sicht: Slogans sind nach moderner\n"
"    Verkehrsauffassung markenfähig, wenn sie über die rein\n"
"    beschreibende Bedeutung hinaus einen markenmäßigen Charakter\n"
"    aufweisen. 'LE LUXE EST UN DROIT NATUREL' enthält ein\n"
"    überraschendes konzeptionelles Moment — die Verbindung von\n"
"    'Luxus' und 'Naturrecht' ist nicht alltäglich.\"\n"
"\n"
"  Vors. Knipperdolling:\n"
"    \"Der Senat zieht sich zur Beratung zurück.\"\n"
"\n"
"  -- Pause 10:42 - 11:18 --\n"
"\n"
"  Vors. Knipperdolling [nach Beratung]:\n"
"    \"Der Senat ist der Auffassung, dass die Beschwerde\n"
"    überwiegend Erfolg haben dürfte. Wir geben die Sache zur\n"
"    erneuten Prüfung an das DPMA zurück. Termin zur Beschluss-\n"
"    verkündung am 28.05.2026, 10:00 Uhr.\"\n"
"\n"
"  Ende: 11:21 Uhr.\n"
"\n"
"  gez. Protokollführer: Just.OberSekr. Lemmerich (Steno)\n"
    )
    s.append(Preformatted(proto, S_MONO_SMALL))
    s.append(HandNote(
        "Wir haben gewonnen — Comtesse hat während des Verlesens\nzweimal Beifall geklatscht, Vors. musste mahnen.\nGut, dass keine Pressevertreter da waren.  — ASt 16.04.",
        font=FONT_HAND, size=14, color=colors.HexColor("#225522"), w=14*cm, angle=-0.4))
    return s

story += blatt_bpatg_protokoll()
story.append(PageBreak())

# BGH-Hinweisbeschluss zur Soundmarken-Rechtsbeschwerde
def blatt_bgh_hinweis():
    s = []
    s.append(Paragraph("<b>BUNDESGERICHTSHOF</b>", S_CENTER))
    s.append(Paragraph("I. Zivilsenat — Vorsitzender Richter VRiBGH Prof. Dr. Koch", S_CENTER))
    s.append(HLine())
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>I ZB 14/26</b>", S_RIGHT))
    s.append(Paragraph("<b>HINWEISBESCHLUSS</b>", S_CENTER))
    s.append(Paragraph("(im Verfahren der Rechtsbeschwerde — Soundmarke „K°°-Jingle“ EUIPO 018 502 311)",
                        S_CENTER))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "In der Rechtsbeschwerdesache der klôtzzkètté S.A. gegen den Beschluss des "
        "Bundespatentgerichts vom 04.12.2025 (Az. 25 W (pat) 122/25) — Sound-/Hörmarke — "
        "weist der Senat gem. § 89 Abs. 4 MarkenG i.V.m. § 552 a ZPO darauf hin, dass die "
        "Rechtsbeschwerde wegen folgender Erwägungen Erfolg haben könnte:", S_NORMAL))
    s.append(Paragraph(
        "1. Soweit das BPatG die Soundmarke „K°°-Jingle“ wegen mangelnder Unterscheidungskraft "
        "(§ 8 Abs. 2 Nr. 1 MarkenG) zurückgewiesen hat, könnte der Senat geneigt sein, dieser "
        "Beurteilung nicht zu folgen. Soundmarken sind nach EuGH-Rechtsprechung "
        "(C-283/01 — <i>Shield Mark</i>) grundsätzlich schutzfähig, sofern (a) hinreichend klar "
        "dargestellt — was hier durch MP3-Datei und Pluralton-Notation gegeben ist —, und "
        "(b) markenfähig im Sinne der Herkunftshinweisfunktion. Die 8-sekündige Komposition mit "
        "ihren vier distinkten Sound-Elementen (Champagnerstiel, Eiswürfel, Stimme, Reverb-Tail "
        "Palais Garnier) entfaltet markenmäßigen Eindruck.", S_NORMAL))
    s.append(Paragraph(
        "2. Insbesondere ist das Argument des BPatG, der reine „Lebensgeräusche-Charakter“ der "
        "ersten beiden Soundelemente (knackender Stiel, klirrende Eiswürfel) führe zu mangelnder "
        "Unterscheidungskraft, im Lichte von <i>BGH, 18.04.2002 — I ZB 30/00, „Werben mit der "
        "Stimme“</i> kritisch zu sehen. Auch alltägliche Geräusche können — wenn in einer "
        "spezifischen, ungewöhnlichen Kombination eingesetzt — Unterscheidungskraft entfalten "
        "(vgl. die Senatsentscheidung <i>BGH, 18.10.2017 — I ZB 22/20, „Quadratisch Praktisch "
        "Gut“</i>).", S_NORMAL))
    s.append(Paragraph(
        "3. Die Sache erscheint dem Senat indes — abweichend von der Auffassung der "
        "Rechtsbeschwerdeführerin — nicht <i>per se</i> geeignet zur Vorlage an den EuGH "
        "(Art. 267 AEUV), da die einschlägige Auslegung der Markenrichtlinie (RL 2015/2436) "
        "bereits hinreichend geklärt ist.", S_NORMAL))
    s.append(Paragraph(
        "<b>Es wird angeregt</b>, dass die Rechtsbeschwerdeführerin und das DPMA als "
        "Verfahrensbeteiligter binnen einer Frist von 4 Wochen zu diesem Hinweis Stellung "
        "nehmen.", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Karlsruhe, 02.04.2026", S_NORMAL_LEFT))
    s.append(Paragraph("gez. VRiBGH Prof. Dr. Koch — RinBGH Dr. Schaffert — RiBGH Feddersen",
                        S_NORMAL_LEFT))
    s.append(Spacer(1, 0.4*cm))
    s.append(StampBox("ausgef.\n02.04.2026\nBGH I. ZS\n— UrkBeamtin Hülk —",
                       angle=-7, color=colors.HexColor("#225522"), w=4.8*cm, h=2.2*cm))
    s.append(Spacer(1, 0.3*cm))
    s.append(HandNote(
        "Das ist DURCHBRUCH — wir bekommen die Soundmarke!\nComtesse anrufen sofort (NICHT vor 10:00 MEZ — aber jetzt 11:15 ok).\nMP3 wird LEGENDÄR — schon jetzt in 47 Kinospots verwendet.\nVfG-Strategie auf Geschäftsschluss BGH erweitern.",
        font=FONT_HAND, size=14, color=colors.HexColor("#7a1f1f"), w=15*cm, angle=0.8))
    return s

story += blatt_bgh_hinweis()
story.append(PageBreak())

print("[part15] done")
