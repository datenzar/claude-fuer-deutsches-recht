# Part 23: Comtesse handwritten note + facsimile cover + Internal memo response
def blatt_comtesse_handwritten():
    s = []
    s.append(Paragraph("<b>Anlage zu Bl. 71</b>", S_RIGHT))
    s.append(Paragraph("<i>Handschriftliche Mitteilung der Mandantin — eingegangen per Fax "
                        "Capri/München, 14.03.2026, 23:47 MEZ</i>", S_SMALL))
    s.append(HLine())
    s.append(Spacer(1, 0.3*cm))
    s.append(FaxHeader(
        from_no="+39 081 837 0011",
        to_no="+49 89 21 03 96-99",
        date="14.03.2026 23:47:18 CET",
        pages="1 of 1",
        subject="STRICTLY PERSONAL — pour Mme Dr. Steinacker",
        sender="Hotel Punta Tragara · Capri (IT) · Suite 414",
        recipient="Steinacker Lichtenberg & Partners · München (DE)"))
    s.append(Spacer(1, 0.4*cm))
    # Big handwritten note from Comtesse
    s.append(HandNote(
        "Annabella, mes chéris !\n"
        "\n"
        "Je vous écris depuis Capri, où la mer est\n"
        "violette comme jamais. Mais la situation\n"
        "à Munich, Francfort, Vilnius — et maintenant\n"
        "à New York ! — me tient éveillée.\n"
        "\n"
        "MES CHÉRIS, N'OUBLIEZ PAS NEW YORK !\n"
        "L'Amérique aussi doit s'agenouiller\n"
        "devant K°°.\n"
        "\n"
        "Pas de compromis. Pas de pitié.\n"
        "Pas de petite ronde de négotiation\n"
        "avec ces messieurs Brezelmann et\n"
        "Donauzon. Le grand-père Antoine-Louis\n"
        "n'aurait jamais toléré la moindre\n"
        "imitation. Ni moi.\n"
        "\n"
        "Le Halston Whitman III me semble\n"
        "un homme sérieux. Donnez-lui carte\n"
        "blanche. Le retainer sera augmenté\n"
        "autant que nécessaire. L'argent n'est\n"
        "pas le sujet ; la dignité de la maison l'est.\n"
        "\n"
        "Je rentre à Paris mardi. Téléphonez-moi\n"
        "ce soir-là à l'hôtel particulier (le numéro\n"
        "habituel) — pas avant 23h, je dîne avec\n"
        "Carla et l'ambassadeur.\n"
        "\n"
        "Bisous,\n"
        "Béatrice de K-V.",
        font=FONT_HAND, size=14, angle=-0.4, w=16*cm,
        paper=colors.HexColor("#faf6e8")))
    return s

story += blatt_comtesse_handwritten()
story.append(PageBreak())

def blatt_steinacker_memo_response():
    s = []
    s.append(Paragraph("<b>INTERNE NOTIZ — STRENG VERTRAULICH</b>", S_H1))
    s.append(HLine(thickness=1.2))
    s.append(Spacer(1, 0.2*cm))
    rows = [
        ["Verfasser:", "Dr. Dr. Annabella Steinacker-von Tarsis"],
        ["Verteiler:", "Maximilian Freiherr v. Brenkenhoff (intern); ausdrücklich NICHT an Mandantin"],
        ["Datum:", "15.03.2026, 07:32 MEZ"],
        ["Betreff:", "Mandantin-Telegrammartiges aus Capri vom 14.03.2026 — Strategiebewertung"],
        ["Az.:", "intern KLZK-INT-2026-014"],
    ]
    t = Table(rows, colWidths=[3.5*cm, 13*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("FONTNAME", (0,0), (0,-1), "Times-Bold"),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>I. Sachstand</b>", S_H3))
    s.append(Paragraph(
        "Die Mandantin hat gestern Abend (23:47 MEZ) per Fax aus dem Hotel Punta Tragara, "
        "Capri, eine handschriftliche Anweisung übermittelt (Anlage Bl. 71). Inhaltlich "
        "instruiert sie:", S_NORMAL))
    items = [
        "(a) Ausweitung der Verfolgung auf den US-amerikanischen Schauplatz "
        "(„l'Amérique aussi doit s'agenouiller devant K°°“);",
        "(b) Kategorischer Verzicht auf jegliche Vergleichsgespräche mit Brezelmann "
        "und Donauzon („pas de compromis, pas de pitié“);",
        "(c) Erweiterung des Mandats zugunsten der US-Kanzlei Whitman Brennan Forsythe LLP, "
        "mit unbeschränkter „carte blanche“-Vollmacht und Aufstockung des Retainers nach "
        "Bedarf.",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    s.append(Paragraph("<b>II. Bewertung</b>", S_H3))
    s.append(Paragraph(
        "Die Instruktion ist juristisch problematisch in zwei Hinsichten:", S_NORMAL))
    s.append(Paragraph(
        "<b>1. „Pas de compromis“:</b> Die kategorische Ablehnung jeder Vergleichsoption "
        "kollidiert mit der Pflicht des Anwalts, die wirtschaftlich vernünftigste Lösung "
        "zu suchen (§§ 43, 43a BRAO). Aus prozesstaktischer Sicht ist ein Vergleich mit "
        "Donauzon — als großem Marktteilnehmer mit ausgereifter Compliance-Infrastruktur — "
        "geradezu geboten: hier können wir innerhalb von 6 Monaten ein <i>Notice-and-"
        "Stay-Down</i>-Regime durchsetzen, was prozessual Jahre dauern würde. <i>Lite "
        "pendente nihil innovetur</i> — aber: <i>mutatis mutandis</i>, eine Mediation ist "
        "kein „Innovieren“ im pessimistischen Sinne.", S_NORMAL))
    s.append(Paragraph(
        "<b>2. „Carte blanche“ an WBF:</b> Eine unbeschränkte Vollmacht an die US-Kanzlei "
        "widerspricht dem Grundsatz der koordinierten Mandatsführung und kann zu "
        "transatlantischen Inkohärenzen führen. Empfehlung: Schriftliche Bestätigung mit "
        "Vorbehalt der Quartalsfreigaben durch München; gemeinsame Strategie-Calls "
        "mittwochs 15:00 MEZ / 10:00 EST.", S_NORMAL))
    s.append(Paragraph("<b>III. Empfehlung</b>", S_H3))
    s.append(Paragraph(
        "Ich werde die Mandantin am Dienstag Abend (17.03., 23:30 MEZ) in Paris anrufen "
        "und vorsichtig auf die Risiken der Maximalstrategie hinweisen. Insbesondere die "
        "<i>Heinrich-Klotz Hauswaren GmbH</i>-Front (vgl. USPTO-Office-Action 22.04.2026) "
        "darf NICHT aufgerissen werden, weil deren Eintragung uns als § 2(d)-Schutzschild "
        "dient. Diese Erläuterung wird voraussichtlich Widerstand hervorrufen — "
        "<i>venire contra factum proprium</i> der Mandantin gegen ihre eigene Instruktion "
        "ist möglich.", S_NORMAL))
    s.append(Paragraph(
        "Halston hat das US-Mandat angenommen; Retainer USD 75.000 plus EUR 250.000 "
        "Aufstockung sind im Trust. Die Strategie ist transatlantisch ausgerichtet, aber "
        "präzise — keine „carte blanche“, sondern „Wednesday Strategy Calls + quarterly "
        "freigabe“-Modell.", S_NORMAL))
    s.append(Paragraph("<b>IV. Aktenvermerk</b>", S_H3))
    s.append(Paragraph(
        "Diese Notiz verbleibt streng intern. Eine Kopie geht an v. Brenkenhoff. "
        "Mandantin erhält schriftliche Bestätigung der akzeptierten Strategie unter "
        "Auslassung der internen Bewertung. Aufbewahrungspflicht 10 Jahre (§ 50 BRAO).",
        S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Dr. Dr. A. Steinacker-von Tarsis, LL.M. (Cantab.)", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(HandNote(
        "Annabella —\n"
        "Bei „pas de pitié“ würde ich beifügen:\n"
        "„aber bitte mit Senf“ (Senf = Mandantin-Argot\n"
        "für Streitwerterhöhung).\n"
        "Comtesse will offensichtlich nicht recht\n"
        "haben, sondern gehört werden.\n"
        "— M.v.B.",
        font=FONT_HAND3, size=11.5, angle=2.5, w=12*cm))
    return s

story += blatt_steinacker_memo_response()
story.append(PageBreak())

print("[part23] done")
