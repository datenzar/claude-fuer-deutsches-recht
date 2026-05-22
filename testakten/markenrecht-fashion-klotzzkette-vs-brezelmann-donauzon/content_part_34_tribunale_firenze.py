# Part 34: Tribunale Firenze IT-Verfahren + Übersetzung
def blatt_tribunale_decreto():
    s = []
    s.append(Paragraph("<b>TRIBUNALE DI FIRENZE</b>", S_CENTER))
    s.append(Paragraph("— SEZIONE SPECIALIZZATA IN MATERIA DI IMPRESA —", S_CENTER))
    s.append(Paragraph("Viale Guidoni, 61 · 50127 Firenze · Italia", S_CENTER))
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.3*cm))
    rows = [
        ["R.G. n.:", "2026/4471"],
        ["Procedimento:", "Cautelare ante causam ex art. 700 c.p.c."],
        ["Ricorrente:", "klôtzzkètté S.A., con sede in Parigi"],
        ["Resistente:", "UAB klotzkettie con sede in Vilnius (Lituania) — non costituita"],
        ["Giudice designato:", "Dott. Giambattista DOLCETTI-PROCACCINI"],
        ["Data udienza:", "27 febbraio 2026 — udienza camerale ex art. 669-sexies c.p.c."],
    ]
    t = Table(rows, colWidths=[4*cm, 12.5*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("FONTNAME", (0,0), (0,-1), "Times-Bold"),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888")),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>DECRETO INAUDITA ALTERA PARTE</b>", S_CENTER))
    s.append(Paragraph(
        "Il Giudice Dott. Dolcetti-Procaccini, letto il ricorso depositato in data "
        "23/02/2026 e i relativi allegati (1–28), ritenuto che ricorrano i presupposti "
        "del <i>fumus boni iuris</i> e del <i>periculum in mora</i>, considerato in "
        "particolare:", S_NORMAL))
    items = [
        "(a) la titolarità da parte della ricorrente del marchio italiano "
        "<b>IT 302.025.000.118.547</b> (KLÔTZZKÈTTÉ, denominativo, classe 25), "
        "registrato sin dal 1962, di indubbia rinomanza ai sensi dell'art. 12, comma 1, "
        "lett. e), C.P.I.;",
        "(b) la documentazione fotografica e i verbali di acquisto-prova allegati "
        "(documenti 14–22), che dimostrano l'allestimento da parte della resistente, "
        "presso lo stand n. 47-A del Pitti Uomo di Firenze (19–22 gennaio 2026), di una "
        "collezione di sciarpe contrassegnate dal segno „klotzkettie“, in tutto e per "
        "tutto idoneo a generare confusione con il marchio della ricorrente;",
        "(c) il <i>periculum in mora</i>, atteso che la fiera in oggetto si svolge nei "
        "prossimi tre giorni e che l'esposizione delle merci infrange i diritti della "
        "ricorrente in maniera continuata e potenzialmente irreversibile;",
        "(d) i precedenti giurisprudenziali in materia di marchi di lusso e fiere "
        "settoriali (Cass., sez. I, n. 9921/2017; Trib. Milano, ord. 12/06/2019); "
        "(e) la circostanza che la resistente, regolarmente convocata in via informale "
        "in data 25/02/2026 mediante posta certificata, non ha fornito riscontro alcuno.",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    s.append(Paragraph("<b>P.Q.M.</b>", S_H3))
    s.append(Paragraph(
        "ordina:", S_NORMAL))
    s.append(Paragraph(
        "<b>I.</b> il sequestro giudiziario di tutti gli articoli contrassegnati dal "
        "segno „klotzkettie“ o segni similari, esposti, custoditi o detenuti presso lo "
        "stand n. 47-A del Pitti Uomo di Firenze, sito presso la Fortezza da Basso;",
        S_NORMAL))
    s.append(Paragraph(
        "<b>II.</b> incarica l'<b>Ufficiale Giudiziario del Tribunale di Firenze</b> di "
        "eseguire il sequestro in data 27/02/2026, con l'assistenza di un consulente "
        "tecnico nominato dalla ricorrente e di un notaio, redigendo apposito verbale, "
        "con facoltà di accedere allo stand anche in orario non di apertura della fiera;",
        S_NORMAL))
    s.append(Paragraph(
        "<b>III.</b> fissa la cauzione a carico della ricorrente in <b>EUR 50.000,00</b>, "
        "da prestare a mezzo polizza fidejussoria di compagnia di primaria importanza, "
        "entro le 18:00 del 26/02/2026;",
        S_NORMAL))
    s.append(Paragraph(
        "<b>IV.</b> fissa l'udienza di comparizione delle parti per la conferma o "
        "modifica del presente provvedimento al <b>14 marzo 2026</b>, ore 10:00, "
        "Aula n. 14;",
        S_NORMAL))
    s.append(Paragraph(
        "<b>V.</b> dichiara il provvedimento immediatamente esecutivo.",
        S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Firenze, lì 26 febbraio 2026", S_NORMAL))
    s.append(Paragraph("Il Giudice", S_RIGHT))
    s.append(Paragraph("Dott. Giambattista Dolcetti-Procaccini", S_RIGHT))
    return s

story += blatt_tribunale_decreto()
story.append(PageBreak())

def blatt_tribunale_uebersetzung():
    s = []
    s.append(Paragraph("<b>BEGLAUBIGTE ÜBERSETZUNG AUS DEM ITALIENISCHEN</b>", S_CENTER))
    s.append(Paragraph(
        "Übersetzerin: Dr. Carlotta SCHATZBERG-SAVELLI, allgemein beeidigt für die "
        "Sprache Italienisch beim OLG Frankfurt", S_SMALL))
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph(
        "<b>(Übersetzung des Decreto inaudita altera parte vom 26.02.2026)</b>", S_H3))
    s.append(Paragraph(
        "<b>TRIBUNAL VON FLORENZ — SPEZIALSEKTION FÜR UNTERNEHMENSRECHT</b>", S_CENTER))
    s.append(Paragraph(
        "Geschäftsnummer 2026/4471 — Eilverfahren ante causam gemäß Art. 700 italZPO.",
        S_SMALL))
    s.append(Paragraph(
        "Antragstellerin: klôtzzkètté S.A. mit Sitz in Paris.<br/>"
        "Antragsgegnerin: UAB klotzkettie mit Sitz in Vilnius (Litauen) — säumig.<br/>"
        "Verfahrensrichter: Dr. Giambattista Dolcetti-Procaccini.<br/>"
        "Termin: 27. Februar 2026 — Kammerverhandlung gemäß Art. 669-sexies italZPO.",
        S_NORMAL))
    s.append(Paragraph("<b>BESCHLUSS OHNE ANHÖRUNG DER GEGENSEITE</b>", S_CENTER))
    s.append(Paragraph(
        "Der Verfahrensrichter, nach Einsicht in den am 23.02.2026 hinterlegten Antrag "
        "und die zugehörigen Anlagen (1–28), in der Annahme, dass die Voraussetzungen "
        "des <i>fumus boni iuris</i> (Glaubhaftmachung des Rechts) und des <i>periculum "
        "in mora</i> (Eilbedürftigkeit) gegeben sind, im Hinblick insbesondere auf:",
        S_NORMAL))
    items = [
        "(a) die Inhaberschaft der Antragstellerin an der italienischen Marke "
        "<b>IT 302.025.000.118.547</b> (KLÔTZZKÈTTÉ, Wortmarke, Klasse 25), die seit "
        "1962 eingetragen ist und zweifelsfrei Ruf im Sinne von Art. 12 Abs. 1 lit. e) "
        "des italienischen Markenrechtsgesetzbuches genießt;",
        "(b) die fotografische Dokumentation und die Test-Kaufprotokolle in der Anlage "
        "(Dokumente 14–22), aus denen sich ergibt, dass die Antragsgegnerin am Stand "
        "Nr. 47-A der Pitti-Uomo-Messe in Florenz (19. bis 22. Januar 2026) eine "
        "Schalkollektion mit dem Zeichen „klotzkettie“ ausgestellt hat, das in jeder "
        "Hinsicht geeignet ist, Verwechslungsgefahr mit der Marke der Antragstellerin "
        "hervorzurufen;",
        "(c) die Eilbedürftigkeit angesichts der bevorstehenden Folgemesse und der "
        "kontinuierlichen, potenziell irreversiblen Rechtsverletzung;",
        "(d) die einschlägige Rechtsprechung im Bereich Luxusmarken und Fachmessen "
        "(it. Kassationshof, 1. Senat, Nr. 9921/2017; Tribunal Mailand, "
        "Beschluss vom 12.06.2019);",
        "(e) den Umstand, dass die Antragsgegnerin, obwohl sie am 25.02.2026 informell "
        "über Posta-certificata benachrichtigt wurde, keinerlei Stellungnahme abgegeben hat.",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    s.append(Paragraph("<b>aus diesen Gründen</b>", S_H3))
    s.append(Paragraph(
        "ordnet er an:", S_NORMAL))
    s.append(Paragraph(
        "<b>I.</b> die richterliche Beschlagnahme aller mit dem Zeichen „klotzkettie“ "
        "oder ähnlichen Zeichen versehenen Artikel, die am Stand Nr. 47-A der "
        "Pitti-Uomo-Messe in Florenz, gelegen in der Fortezza da Basso, ausgestellt, "
        "verwahrt oder in Besitz gehalten werden;", S_NORMAL))
    s.append(Paragraph(
        "<b>II.</b> beauftragt den <b>Gerichtsvollzieher des Tribunals Florenz</b> mit "
        "der Vollziehung der Beschlagnahme am 27.02.2026 unter Beizug eines von der "
        "Antragstellerin benannten technischen Beraters und eines Notars; ein "
        "entsprechendes Protokoll ist zu fertigen; der Zutritt zum Stand kann auch "
        "außerhalb der Messeöffnungszeiten erfolgen;", S_NORMAL))
    s.append(Paragraph(
        "<b>III.</b> setzt die Sicherheitsleistung der Antragstellerin auf "
        "<b>EUR 50.000,00</b> fest, zu erbringen durch Bankbürgschaft einer Bank von "
        "Primärrating bis spätestens 18:00 Uhr am 26.02.2026;", S_NORMAL))
    s.append(Paragraph(
        "<b>IV.</b> setzt den Termin zur Anhörung der Parteien zur Bestätigung oder "
        "Änderung dieses Beschlusses auf den <b>14. März 2026</b>, 10:00 Uhr, "
        "Saal Nr. 14, fest;", S_NORMAL))
    s.append(Paragraph(
        "<b>V.</b> erklärt diesen Beschluss für sofort vollstreckbar.", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Florenz, den 26. Februar 2026", S_NORMAL))
    s.append(Paragraph("Der Verfahrensrichter", S_RIGHT))
    s.append(Paragraph("Dr. Giambattista Dolcetti-Procaccini", S_RIGHT))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<i>Beglaubigungsvermerk:</i> Hiermit bestätige ich, dass die vorstehende "
        "Übersetzung mit dem mir vorgelegten italienischen Original wortgetreu "
        "übereinstimmt. Frankfurt am Main, den 04.03.2026.<br/>"
        "<b>Dr. Carlotta Schatzberg-Savelli</b> — Beeidigte Übersetzerin", S_SMALL))
    s.append(StampBox("ÜBERSETZER-\nKAMMER FFM\n04.03.2026", angle=8, w=4.8*cm, h=1.8*cm))
    s.append(HandNote(
        "Tribunale war schnell und konsequent.\n"
        "Italiener verstehen sartoriale Eigentumsrechte.\n"
        "Dolcetti-Procaccini soll am 12.05.2026 als Sachverständiger\n"
        "(per Skype) im OLG-Termin gehört werden — Idee Brenkenhoff.\n"
        "Honorar Schatzberg-Savelli: 2.114,90 EUR (siehe Kostennote A).\n"
        "— A.St., 05.03.",
        font=FONT_HAND, size=13, angle=-0.5, w=15.5*cm))
    return s

story += blatt_tribunale_uebersetzung()
story.append(PageBreak())

print("[part34] done")
