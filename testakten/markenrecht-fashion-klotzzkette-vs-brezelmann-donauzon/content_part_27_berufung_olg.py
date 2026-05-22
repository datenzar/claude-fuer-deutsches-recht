# Part 27: Berufungsschriftsatz OLG Frankfurt 6 W 47/26
def blatt_olg_berufung_1():
    s = []
    s.append(Briefkopf(
        kanzlei_block=("Mandatsnummer: 26-1014-KK\n"
                       "Sachbearbeiterin: Dr. Steinacker\n"
                       "Beweismittel: B-1 bis B-48\n"
                       "Streitwert: EUR 4.800.000,-"),
        recipient_block=("An das\nOberlandesgericht Frankfurt am Main\n"
                          "— 6. Zivilsenat —\nZeil 42\n60313 Frankfurt am Main\n\n"
                          "vorab per beA  ·  per Bote zur Niederschrift"),
        datum="04. August 2026",
        az="6 W 47/26  (vorgehend LG FFM 2-03 O 412/26)"))
    s.append(Spacer(1, 0.5*cm))
    s.append(Paragraph(
        "<b>BERUFUNG</b>", S_CENTER))
    s.append(Paragraph(
        "der Verfügungsklägerin <b>klôtzzkètté S.A.</b> — Berufungsklägerin —", S_CENTER))
    s.append(Paragraph("gegen", S_CENTER))
    s.append(Paragraph(
        "<b>Brezelmann Discount KG</b> — Berufungsbeklagte zu 1 —<br/>"
        "<b>Donauzon Marketplace GmbH</b> — Berufungsbeklagte zu 2 —", S_CENTER))
    s.append(HLine())
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "In der vorbezeichneten Markenstreitsache legen wir namens und in Vollmacht der "
        "Berufungsklägerin gegen das Urteil der 3. Zivilkammer des Landgerichts Frankfurt am "
        "Main vom <b>27. Juli 2026</b>, Az. 2-03 O 412/26, zugestellt am 04.08.2026, "
        "form- und fristgerecht", S_NORMAL))
    s.append(Paragraph(
        "<b>BERUFUNG</b><br/>"
        "gemäß §§ 511, 517 ZPO ein, soweit die Klage in Höhe der ersten Stufe "
        "(Auskunft) abgewiesen wurde. Im Übrigen bleibt das Urteil unangegriffen.",
        S_NORMAL))
    s.append(Paragraph("<b>I. Erstinstanzliches Urteil — Tenor (Auszug)</b>", S_H3))
    s.append(Paragraph(
        "Das Landgericht Frankfurt hat mit Urteil vom 27.07.2026 wie folgt erkannt:",
        S_NORMAL))
    s.append(Paragraph(
        "<i>1. Die Beklagten werden verurteilt, es bei Meidung der gesetzlichen "
        "Ordnungsmittel zu unterlassen, im geschäftlichen Verkehr Bekleidung, "
        "Accessoires und Lederwaren unter dem Kennzeichen „klotzkettiee“ oder "
        "ähnlichen Bezeichnungen ohne Zustimmung der Klägerin anzubieten, "
        "in den Verkehr zu bringen, einzuführen oder auszuführen.</i><br/>"
        "<i>2. Die Beklagte zu 2 (Donauzon) wird verurteilt, eine "
        "Notice-and-Take-Down-Routine entsprechend der DSA Art. 16 i.V.m. der "
        "EU-Verordnung 2022/2065 einzurichten und der Klägerin Zugang zu einem "
        "Trusted-Flagger-Status nach Art. 22 DSA zu gewähren.</i><br/>"
        "<i>3. Die Klage wird im Übrigen abgewiesen, insbesondere hinsichtlich des "
        "Auskunfts- und Schadensersatz-Antrages.</i><br/>"
        "<i>4. Die Kosten des Verfahrens werden zu 30 % der Klägerin, zu 60 % der "
        "Beklagten zu 1 und zu 10 % der Beklagten zu 2 auferlegt.</i>", S_QUOTE))
    s.append(Paragraph("<b>II. Berufungsanträge</b>", S_H3))
    s.append(Paragraph("Es wird beantragt, das Urteil teilweise abzuändern und",
                        S_NORMAL))
    s.append(Paragraph(
        "<b>1.</b> die Beklagten <i>als Gesamtschuldner</i> zu verurteilen, der Klägerin "
        "Auskunft zu erteilen über:", S_NORMAL))
    items = [
        "a) Namen und Anschriften aller Hersteller, Lieferanten, Großabnehmer und "
        "Einzelhändler, denen die rechtsverletzenden Waren angeboten, geliefert oder "
        "zugänglich gemacht wurden;",
        "b) die Mengen der hergestellten, ausgelieferten, erhaltenen oder bestellten "
        "rechtsverletzenden Waren sowie die hierfür entstandenen Preise;",
        "c) die Umsätze, die mit den rechtsverletzenden Waren erzielt wurden, "
        "aufgegliedert nach Kalenderquartalen seit dem 01.01.2024;",
        "d) Art und Umfang der durchgeführten Werbung, aufgegliedert nach Werbeträgern, "
        "deren Auflage und Verbreitungsgebiet sowie Werbungskosten;",
        "e) bei Donauzon insbesondere: vollständige Listings, ASINs/Artikel-IDs, "
        "Verkäuferprofile, Versandländer, Plattformgebühren-Einnahmen aus den "
        "rechtsverletzenden Angeboten;",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=26,
                                               firstLineIndent=-12)))
    s.append(Paragraph(
        "<b>2.</b> festzustellen, dass die Beklagten als Gesamtschuldner verpflichtet "
        "sind, der Klägerin allen Schaden zu ersetzen, der ihr aus den in Ziffer 1 "
        "des landgerichtlichen Urteils bezeichneten Handlungen entstanden ist und "
        "noch entstehen wird;", S_NORMAL))
    s.append(Paragraph(
        "<b>3.</b> die Kosten des Rechtsstreits insgesamt — auch hinsichtlich der ersten "
        "Instanz — den Beklagten als Gesamtschuldnern aufzuerlegen.", S_NORMAL))
    return s

story += blatt_olg_berufung_1()
story.append(PageBreak())

def blatt_olg_berufung_2():
    s = []
    s.append(Paragraph("<b>III. Berufungsbegründung</b>", S_H3))
    s.append(Paragraph("<b>A. Verletzung materiellen Rechts (§ 546 ZPO)</b>", S_H3))
    s.append(Paragraph(
        "1. Das Landgericht hat den geltend gemachten Auskunftsanspruch nach § 19 MarkenG "
        "rechtsfehlerhaft zurückgewiesen. Das Gericht stützt sich auf die — irrige — "
        "Annahme, dass der Auskunftsanspruch unverhältnismäßig sei, weil die Beklagte zu 2 "
        "(Donauzon) als reiner Plattformbetreiber »keine eigenen Verkaufsdaten "
        "hinsichtlich der Third-Party-Seller-Listings« speichere. Diese Annahme "
        "widerspricht der Realität moderner Marktplatzplattformen, die alle Transaktions-"
        "metadaten in Echtzeit erfassen, sowie der gefestigten Rechtsprechung des EuGH "
        "(<i>Coty Germany ./. Amazon</i>, C-567/18; <i>Christian Louboutin ./. Amazon</i>, "
        "C-148/21 verb. mit C-184/21).", S_NORMAL))
    s.append(Paragraph(
        "2. Der EuGH hat in <i>Coty/Amazon</i> klargestellt, dass auch der Lagerist "
        "passiv-mittelbar für gespeicherte Verletzerwaren haftet, wenn er ihre Existenz "
        "kennt oder kennen muss. Die in Rede stehende Donauzon-Logistics-USA-LLC-"
        "Detention vom 19.04.2026 (Bl. 64) beweist die positive Kenntnis der "
        "Donauzon-Gruppe. Die Auskunftsverweigerung ist daher rechtswidrig.", S_NORMAL))
    s.append(Paragraph(
        "3. Das Landgericht hat ferner zu Unrecht den DSA-Trusted-Flagger-Status nach "
        "Art. 22 DSA als gleichwertig zur urheberrechtlichen/markenrechtlichen "
        "Auskunftspflicht behandelt. Die DSA-Trusted-Flagger-Architektur ist eine "
        "ex-post-Notifikationsstruktur; sie ersetzt nicht den materiellen Auskunfts-"
        "anspruch nach § 19 Abs. 1 und 2 MarkenG, der eine umfassende und einmalige "
        "Vermögensauskunft bezweckt. <i>A maiore ad minus</i>: was die DSA als Minimum-"
        "Standard erfasst, kann die spezialgesetzliche Anspruchsgrundlage nicht "
        "ersetzen.", S_NORMAL))
    s.append(Paragraph(
        "4. Das Landgericht hat zudem eine Beweiswürdigung vorgenommen, die mit dem "
        "<i>Anscheinsbeweis</i> nach § 286 ZPO nicht in Einklang steht: Die im Detektiv-"
        "bericht der Spürnase-Couture GmbH (Anlage K-12, Bl. 31 ff.) dokumentierten "
        "9 Testkäufe vom 14.–28.02.2026, jeweils mit fotografischer und kassenbon-"
        "gestützter Beweissicherung, begründen einen Anscheinsbeweis für ein "
        "systematisches Verletzungsgeschehen, der hinreichende Konkretheit für den "
        "Auskunftsanspruch begründet (vgl. BGH I ZR 35/19, Rn. 24; ebenso BGH I ZB "
        "22/20).", S_NORMAL))
    s.append(Paragraph("<b>B. Verfahrensfehler (§ 538 ZPO)</b>", S_H3))
    s.append(Paragraph(
        "5. Das Landgericht hat den am 18.07.2026 von der Klägerin gestellten "
        "Hilfsantrag auf Vernehmung des Zeugen <i>Sebastien Pétard</i> (ehem. "
        "Donauzon-Compliance-Officer, jetzt Frühpensionär, wohnhaft Lugano, CH) "
        "ohne Begründung übergangen. Dies stellt einen Gehörsverstoß nach Art. 103 "
        "Abs. 1 GG dar.", S_NORMAL))
    s.append(Paragraph(
        "6. Ferner hat das Landgericht die als Anlage K-31 vorgelegte „Whistleblower"
        "-Dokumentation Donauzon-USA“ vom 11.05.2026 ohne Erörterung beiseite gelegt — "
        "eine offenkundige Sachfragenversäumnis (<i>iura novit curia</i>, doch die "
        "Sachverhaltsfragen muss das Gericht klären lassen).", S_NORMAL))
    s.append(Paragraph("<b>C. Streitwert und Beschwer</b>", S_H3))
    s.append(Paragraph(
        "7. Die Beschwer beträgt — bezogen auf den abgewiesenen Auskunftsanspruch — "
        "EUR 1.200.000,00 (vgl. Streitwertbeschluss erster Instanz). Die Berufungssumme "
        "nach § 511 Abs. 2 Nr. 1 ZPO ist erreicht und überschritten.", S_NORMAL))
    s.append(Paragraph("<b>IV. Beweismittel</b>", S_H3))
    s.append(Paragraph(
        "Bezugnahme auf die erstinstanzlichen Beweismittel B-1 bis B-37; zusätzlich:",
        S_NORMAL))
    items = [
        "B-38: CBP Detention Notice 26-LAX-002-887 vom 19.04.2026 (Bl. 64);",
        "B-39: Whistleblower-Dokumentation Donauzon-USA, 11.05.2026 (Übersetzung "
        "aus dem Englischen);",
        "B-40: Ergänzungsgutachten Prof. Tastenberger TU Darmstadt vom 12.06.2026 "
        "(Haptik-Erweiterung);",
        "B-41: Soundeng. R. Aurelius Spektrogramm „K°° Auftakt-Motiv“, 22.06.2026;",
        "B-42: TTAB Filing Receipt 91/289.412 vom 03.04.2026;",
        "B-43: EU-Repräsentations-Beschluss klôtzzkètté S.A. vom 04.05.2026;",
        "B-44: Auskunftstabellen Pinkerton NYC (Sub-Detektei zu Spürnase-Couture);",
        "B-45: Verkehrsbefragung Ipsos-Mori DE 2024 (Brand Awareness 41 %);",
        "B-46: Comtesse-Korrespondenz Capri 14.03.2026 (Bl. 71) — nur zur Strategiefrage;",
        "B-47: Mlle Hortense Périgord Ergänzungsgutachten 25.06.2026 (Olfaktorik II);",
        "B-48: Kostenfeststellungsantrag der Klägerin (vorab).",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Es wird angeregt, eine mündliche Verhandlung anzuberaumen und dabei den "
        "Zeugen Pétard zu vernehmen.", S_NORMAL))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph(
        "<b>Dr. Dr. A. Steinacker-von Tarsis, LL.M. (Cantab.)</b> · <b>M. Freiherr "
        "v. Brenkenhoff</b><br/>"
        "— Rechtsanwälte —", S_SMALL))
    return s

story += blatt_olg_berufung_2()
story.append(PageBreak())

print("[part27] done")
