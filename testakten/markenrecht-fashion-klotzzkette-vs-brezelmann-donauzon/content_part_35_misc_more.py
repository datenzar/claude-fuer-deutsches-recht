# Part 35: Misc — Strafanzeige Vilnius, Whistleblower-Doku, Mlle Périgord II, Compliance Memo
def blatt_strafanzeige_vilnius():
    s = []
    s.append(Briefkopf(
        kanzlei_block=("Az.: 26-1014-KK-LT\nLiteratur: Tarptautinis MGK 192 str.\n"
                       "Übersetzungsbüro: SIA Verba LT\nKollegen vor Ort: "
                       "Petrauskas & Daugėla"),
        recipient_block=("Generalinis prokuroras\nLietuvos Respublikos Generalinė "
                          "Prokuratūra\nRinktinės g. 5A\nLT-01515 Vilnius · "
                          "REPUBLIK LITAUEN\n\nzur Kenntnis: Vilniaus Apylinkės "
                          "Teismas"),
        datum="14. Juli 2026",
        az="—  (lit. Pendant zu 2-03 O 412/26)"))
    s.append(Spacer(1, 0.5*cm))
    s.append(Paragraph("<b>STRAFANZEIGE</b>", S_CENTER))
    s.append(Paragraph(
        "(deutsche Übersetzung; litauisches Original liegt bei)", S_SMALL))
    s.append(HLine())
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph(
        "<b>der Anzeigeerstatterin klôtzzkètté S.A.</b>, 12 rue du Faubourg "
        "Saint-Honoré, 75008 Paris, vertreten durch Steinacker Lichtenberg "
        "&amp; Partners (München) und in Vilnius mit Petrauskas &amp; Daugėla "
        "(Konstitucijos pr. 7, Vilnius)", S_NORMAL))
    s.append(Paragraph("<b>gegen</b>", S_CENTER))
    s.append(Paragraph(
        "<b>UAB klotzkettie</b>, Vilniaus g. 47, LT-01402 Vilnius, "
        "Reg.-Nr. 305.881.117, sowie deren faktischen Geschäftsführer "
        "<b>Egonas Brezelmanas</b>, geb. 14.07.1973 in Bad Mergentheim, "
        "Bundesrepublik Deutschland; vermutete tatsächliche Identität: "
        "Egon Brezelmann, geb. ebenda, Inhaber der Brezelmann Discount KG.",
        S_NORMAL))
    s.append(Paragraph("<b>wegen</b>", S_CENTER))
    s.append(Paragraph(
        "Vergehens nach <b>Art. 204 LR-StGB</b> (Verletzung eines fremden "
        "Warenzeichens — gewerbsmäßig), <b>Art. 205</b> (Inverkehrbringen "
        "gefälschter Waren), <b>Art. 192</b> (Urheberrechtsverletzung — "
        "soweit das Antoine-Louis-Klôtzzkètté-Krönchen-Design als angewandte "
        "Kunst geschützt ist) sowie <b>Art. 220</b> (Geldwäsche, weil Erlöse "
        "ggf. über die deutsche Brezelmann-KG verschleiert werden).",
        S_NORMAL))
    s.append(Paragraph("<b>I. Sachverhalt</b>", S_H3))
    s.append(Paragraph(
        "Die Anzeigeerstatterin ist Inhaberin der internationalen Marke "
        "IR 1.488.220 (KLÔTZZKÈTTÉ) mit Schutzwirkung u.a. in Litauen, "
        "sowie der EUTM 018 411 220. Die Anzeigegegnerin UAB klotzkettie "
        "betreibt einen Versandhandel von Schalen und Konfektionsware unter "
        "dem nahezu identischen Zeichen „klotzkettie“. Aus den "
        "Detektivermittlungen Spürnase-Couture vom 14.–28.05.2026 und der "
        "Quellenmeldung „Q“ vom 16.06.2026 (Café Forto Dvaras, Vilnius) ist "
        "bekannt:", S_NORMAL))
    items = [
        "(1) UAB klotzkettie ist eine reine Briefkastenfirma mit einem "
        "einzigen Mitarbeiter, der nach dem Befund von „Q“ Litauisch "
        "nicht spricht und einen deutschen Akzent hat;",
        "(2) Containerumschlag 2026: 3× 40-foot, geschätzte 28.000 Stück, "
        "80 % an die Donauzon-FBA-Lager in Werne (DE);",
        "(3) am 19.04.2026 wurden 2.488 Stück durch CBP am Hafen "
        "Los Angeles/Long Beach in den USA festgesetzt (Annex CBP-1);",
        "(4) die Anmeldung von „klotzkettiee“ beim DPMA und die Anmeldung "
        "von „klotzkettie“ als EUTM 018 998 712 sind koordiniert; aus dem "
        "E-Mail-Verkehr Brezelmann/Steinacker (21.01.2026) ergibt sich "
        "ein Angebot zur Ablösung der DE-Marke für EUR 290.000,00.",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    s.append(Paragraph(
        "Die geschätzten Erlöse 2025-Q1/2026 belaufen sich auf EUR 1,84 Mio. "
        "Die Tat wird gewerbsmäßig (Art. 204 § 2 lit. lett.) begangen.", S_NORMAL))
    s.append(Paragraph("<b>II. Antrag</b>", S_H3))
    s.append(Paragraph(
        "Die Anzeigeerstatterin <b>beantragt</b> die Aufnahme der "
        "Ermittlungen, die Anordnung der Durchsuchung der "
        "Geschäftsräume an der Vilniaus g. 47 sowie die Sicherstellung "
        "der dort vorgefundenen Waren und Geschäftsunterlagen.",
        S_NORMAL))
    s.append(Paragraph(
        "<b>III. Beweismittel.</b> Bezugnahme auf die der Anzeige "
        "beigefügten 47 Dokumente (B-1 bis B-47). Insbesondere die "
        "Detektivberichte und die CBP-Beschlagnahme-Notice sind als "
        "Anlagen 14 und 22 mit eingereicht.", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Mit Hochachtung,<br/>Petrauskas &amp; Daugėla, Vilnius "
        "(unterzeichnet: adv. Rūta Petrauskaitė)<br/>"
        "in Verbindung mit Steinacker Lichtenberg &amp; Partners, "
        "München", S_SMALL))
    s.append(Spacer(1, 0.4*cm))
    s.append(HandNote(
        "Vilnius-Strafanzeige ist ein Druckmittel.\n"
        "Real wird sie wenig liefern (LT-Behörden langsam).\n"
        "Aber: Brezelmanas/Brezelmann mit Strafverfahren\n"
        "in 3 Jurisdiktionen → verhandelt eher.\n"
        "Petrauskaitė ist eine Tigerin. Honorar EUR 18.500.\n"
        "— Steinacker, 15.07.",
        font=FONT_HAND, size=13.5, angle=-0.6, w=15*cm))
    return s

story += blatt_strafanzeige_vilnius()
story.append(PageBreak())

def blatt_whistleblower():
    s = []
    s.append(Paragraph("<b>WHISTLEBLOWER-DOKUMENTATION DONAUZON-USA</b>", S_H1))
    s.append(Paragraph(
        "Anlage K-31 zum LG FFM-Verfahren · Anlage B-39 zur OLG-Berufung · "
        "Anlage S-3 zur SDNY-Klage<br/>"
        "<i>Eingang 11.05.2026 · Quelle: Sebastien PÉTARD (ehem. Donauzon-Compliance-"
        "Officer)</i>", S_SMALL))
    s.append(HLine())
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("<b>Vorbemerkung — Annabella Steinacker, 12.05.2026:</b>", S_H3))
    s.append(Paragraph(
        "Am 11.05.2026, 14:32 MEZ, erreichte unsere Kanzlei eine USB-Stick-Sendung per "
        "DHL-Express (Sendungsverfolgungsnummer JD-014488-771-K) aus Lugano (Schweiz). "
        "Absender: nicht angegeben; ein der Sendung beiliegender Brief war handschriftlich "
        "(Caveat-Stil, vermutlich linkshändig) verfasst und enthielt nur den Satz: "
        "<i>„Vous trouverez ce qu'il vous faut. — S.“</i>. Der USB-Stick enthielt 14 "
        "PDF-Dokumente, drei Excel-Sheets und eine Liste mit 1.488 ASIN-Identifiern. "
        "Nach forensischer Echtheitsprüfung durch Dr. K.-H. Vogelstein-Mommsen "
        "(zertifizierter IT-Forensiker) ist die Authentizität der Daten zu 96 % gegeben.",
        S_NORMAL))
    s.append(Paragraph(
        "Unter den ASIN-Identifiern befinden sich mindestens 388, die zu Listings "
        "klôtzzkètté-imitierter Schaltücher führen, mit detaillierten Verkaufsdaten "
        "(Stückzahlen, Preise, Käuferanzahl, Versandländer). Donauzon hat in der "
        "Klageerwiderung vom 14.04.2026 noch behauptet, derartige Daten nicht zu "
        "besitzen.", S_NORMAL))
    s.append(Paragraph("<b>Auszug aus Sheet „2026-Q1-Sales-Detail.xlsx“ (anonymisiert)</b>",
                        S_H3))
    rows = [
        ["ASIN", "Listing Name", "Q1/26 Units", "ASP €", "GMV €", "Marketplace"],
        ["B084KLZ7TC", "klotzkettiee Twill Silk Scarf — Royal Blue", "412", "12.99",
         "5.351,88", "DE/AT"],
        ["B086KLZ8UU", "klotzkettiee Twill Silk Scarf — Ivory", "388", "12.99",
         "5.040,12", "DE/AT/CH"],
        ["B084KLZ8YQ", "K°°-Inspired Crown Necklace (gold-plated)", "227", "29.90",
         "6.787,30", "DE"],
        ["B084KLZ7ZX", "klotzkettie Position-Mark Leather Sneaker", "118", "89.00",
         "10.502,00", "DE/FR"],
        ["B084KLZ8AB", "klotzkettie Hexagonal Flacon Perfume EdT 50 ml", "344", "39.99",
         "13.756,56", "DE/IT"],
        ["B084KLZ8CD", "klotzkettiee Set (scarf + necklace + perfume) — Gift Box", "82",
         "79.99", "6.559,18", "DE"],
        ["B084KLZ8EF", "klotzkettie „Soie d'Aube“ Imitation Innenfutter", "29", "49.00",
         "1.421,00", "DE"],
        ["… (381 weitere ASINs ausgelassen)", "", "≈ 14.218", "", "≈ 198.244,00",
         "DE/AT/CH/FR/IT/ES/NL"],
        ["", "<b>Q1/2026 GMV total Donauzon-EU (geschätzt aus Sheet)</b>", "", "",
         "<b>247.662,04</b>", ""],
    ]
    t = Table(rows, colWidths=[2.5*cm, 6.0*cm, 2.0*cm, 1.6*cm, 2.4*cm, 2.0*cm],
                repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 8.2),
        ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1c2e4a")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#888")),
        ("ALIGN", (2,1), (-1,-1), "RIGHT"),
        ("ROWBACKGROUNDS", (0,1), (-1,-2), [colors.white, colors.HexColor("#f5f1e6")]),
        ("BACKGROUND", (0,-1), (-1,-1), colors.HexColor("#ede0c8")),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Diese Sheets sind sowohl rechtsbeweislich wertvoll (Schadensschätzung nach "
        "Lizenzanalogie) als auch — aus DSA-Sicht — Indizien für ein "
        "<i>schweres Compliance-Versagen</i> bei Donauzon-EU. Sie werden in den "
        "OLG-Berufungsschriftsatz und in den SDNY-Complaint aufgenommen. Quelle Pétard "
        "wird als Zeuge vernommen werden (Termin: OLG FFM, ggf. per Video aus Lugano).",
        S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>Verteilerverbot / Datenschutz</b>", S_H3))
    s.append(Paragraph(
        "Die Whistleblower-Dokumentation enthält möglicherweise personenbezogene Daten "
        "(Käufer-IDs in Original-Sheets). Vor jeglicher Verwendung im Prozess wird "
        "anonymisiert; vor jeglicher Verwendung in den USA wird der Discovery-Schutz "
        "nach Sedona Conference Principles eingehalten (vgl. PFV-Vorschlag Email "
        "19.03.2026).", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(HandNote(
        "„S.“ = Sebastien Pétard. Hat 14 Jahre für Donauzon-Luxembourg gearbeitet.\n"
        "Frühpensioniert nach internem Streit Q3 2025.\n"
        "Wohnt jetzt Lugano. Spricht 5 Sprachen, raucht Zigaretten ohne Filter.\n"
        "Sein Honorar als Zeuge: er WILL keins — er will nur „dass die\n"
        "Wahrheit auf den Tisch kommt“. Romantisch, aber verlässlich.\n"
        "→ Termin Lugano 23.07.2026, Ristorante Galleria Arté.\n"
        "— Brenkenhoff",
        font=FONT_HAND2, size=13, angle=0.6, w=15.5*cm))
    return s

story += blatt_whistleblower()
story.append(PageBreak())

def blatt_compliance_memo():
    s = []
    s.append(Paragraph("<b>INTERNES COMPLIANCE-MEMO — DSGVO/DSA-SYNTHESE</b>", S_H1))
    s.append(Paragraph("Verfasserin: Dr. Dr. A. Steinacker-von Tarsis · "
                        "11. Juli 2026 · STRENG VERTRAULICH", S_SMALL))
    s.append(HLine())
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph(
        "Zur Vorbereitung der OLG-Berufung 6 W 47/26 ist eine Synthese der "
        "verschiedenen datenschutz- und plattformrechtlichen Argumente notwendig. "
        "Folgende Konfliktlinien sind zu bewältigen:", S_NORMAL))
    s.append(Paragraph("<b>1. DSA Art. 16 (Notice and Action) vs. § 19 MarkenG "
                        "(Auskunftsanspruch)</b>", S_H3))
    s.append(Paragraph(
        "Das LG FFM hat im Urteil vom 27.07.2026 die DSA-Notice-and-Action-Architektur "
        "als „funktionsadäquaten Ersatz“ des Auskunftsanspruchs nach § 19 MarkenG "
        "behandelt. Dies ist unionsrechtlich problematisch: Erw.gr. 12 DSA ("
        "Verordnung 2022/2065) stellt klar, dass die Verordnung „spezifische "
        "Bestimmungen anderer Rechtsakte des Unionsrechts unberührt lässt“, "
        "insbesondere Richtlinie 2004/48/EG (Enforcement-Richtlinie). Art. 8 "
        "Enforcement-RL kodifiziert den Auskunftsanspruch — der § 19 MarkenG umsetzt. "
        "<i>A maiore ad minus</i>: was die Enforcement-RL <i>tatkräftig</i> regelt, "
        "kann die DSA <i>passiv-prozedural</i> nicht ersetzen.", S_NORMAL))
    s.append(Paragraph("<b>2. DS-GVO Art. 48 (Drittstaaten-Auskunft) vs. "
                        "TTAB-Discovery</b>", S_H3))
    s.append(Paragraph(
        "Bei der Antwort auf TTAB-Interrogatories besteht die Gefahr, dass durch "
        "Disclosure von Daten EU-ansässiger Zeuginnen (z.B. der Detektive "
        "Karla Kalt-Bandel und Bastian Spürmüller-Fürst) ein DS-GVO-Verstoß "
        "begangen wird. Lösung: Protective Order der TTAB mit ausdrücklicher "
        "GDPR-Klausel (Klausel 14(b), entworfen von Forsythe-Vanderhof). Status: "
        "akzeptiert von Klotzkettie LLC (keine Antwort = stillschweigend akzeptiert).",
        S_NORMAL))
    s.append(Paragraph("<b>3. Cross-Border Privilege: anwaltliche Verschwiegenheit</b>",
                        S_H3))
    s.append(Paragraph(
        "Common-Interest-Agreement zwischen Steinacker Lichtenberg und Whitman Brennan "
        "Forsythe LLP wurde am 14.03.2026 (Annex B zum Engagement Letter) unterzeichnet. "
        "Dies sichert die transatlantische anwaltliche Verschwiegenheit gegenüber "
        "US-Discovery-Anfragen (cf. <i>Upjohn Co. v. United States</i>, 449 U.S. 383). "
        "BORA § 2 in Verbindung mit ABA Model Rule 1.6 — keine Konflikte.", S_NORMAL))
    s.append(Paragraph("<b>4. TMEP § 1218 — USPTO-Examinator-Anfragen und Pariser Verband</b>",
                        S_H3))
    s.append(Paragraph(
        "Bei den USPTO-Office-Actions (z.B. § 2(d) Refusal Albertson 22.04.2026) ist zu "
        "berücksichtigen, dass die Beweisaufnahme durch USPTO-Examinator nach TMEP "
        "§ 710 anderen Beweisstandards folgt als die EUIPO-Examination. Dort, wo "
        "Pariser-Verbands-Konvention Art. 6quinquies-Berufung möglich ist, soll diese "
        "argumentativ geführt werden.", S_NORMAL))
    s.append(Paragraph("<b>5. Aufbewahrungspflichten der Akte</b>", S_H3))
    s.append(Paragraph(
        "Die Hauptakte umfasst per 22.05.2026 ca. 130 Blätter und wird voraussichtlich "
        "bis Q4 2027 auf ca. 220 Blätter anwachsen. Aufbewahrungsfrist gemäß § 50 BRAO: "
        "10 Jahre. Whistleblower-Original-USB-Stick wird im Tresor der Kanzlei "
        "(Fach 14-K) für 30 Jahre verwahrt (höchste Vertraulichkeitsstufe; "
        "Zugang nur Steinacker + Brenkenhoff).", S_NORMAL))
    return s

story += blatt_compliance_memo()
story.append(PageBreak())

print("[part35] done")
