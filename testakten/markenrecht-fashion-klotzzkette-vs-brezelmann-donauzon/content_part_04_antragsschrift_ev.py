# Part 04: Antragsschrift einstweilige Verfügung LG Frankfurt
def blatt_antragsschrift_ev():
    s = []
    s.append(Briefkopf(KANZLEI_ADDR, LG_FFM_ADDR, "11.03.2026",
                        "Sch-Lich 26-0188 / 2-03 O ___/26"))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>ANTRAGSSCHRIFT</b>", S_CENTER))
    s.append(Paragraph("<b>auf Erlass einer einstweiligen Verfügung</b>", S_CENTER))
    s.append(Paragraph("— ohne mündliche Verhandlung gemäß § 937 Abs. 2 ZPO —", S_CENTER))
    s.append(Spacer(1, 0.3*cm))
    s.append(HLine())
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("<b>In der einstweiligen Verfügungssache</b>", S_NORMAL))
    s.append(Paragraph(
        "<b>klôtzzkètté S.A.</b>, 12 rue du Faubourg Saint-Honoré, 75008 Paris, Frankreich, "
        "RCS Paris 552 094 471, vertreten durch die Hauptgesellschafterin Comtesse Béatrice de "
        "Klôtzzkètté-Visconti, ebenda,", S_NORMAL))
    s.append(Paragraph("— Antragstellerin —", S_RIGHT))
    s.append(Paragraph(
        "Prozessbevollmächtigte: Steinacker Lichtenberg &amp; Partners IP Boutique, "
        "Maximiliansplatz 19, 80333 München (federführend: Dr. Dr. Annabella Steinacker-von "
        "Tarsis, LL.M.; Mitbearb.: RA Maximilian Freiherr von Brenkenhoff)", S_SMALL))
    s.append(Paragraph("<b>g e g e n</b>", S_CENTER))
    s.append(Paragraph(
        "1. <b>Brezelmann Discount KG</b>, Wurstgasse 4, 97980 Bad Mergentheim, vertreten "
        "durch den Komplementär Herrn Dipl.-Kfm. Egon Brezelmann, ebenda;", S_NORMAL))
    s.append(Paragraph(
        "2. <b>Donauzon Marketplace GmbH</b>, Tour Trintignant, 2540 Luxembourg, "
        "Niederlassung Deutschland: Erdbeerallee 88, 80807 München, vertreten durch die "
        "Geschäftsführung;", S_NORMAL))
    s.append(Paragraph("— Antragsgegnerinnen —", S_RIGHT))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph(
        "<b>wegen:</b> Unterlassung der Verletzung von Marken der Antragstellerin "
        "(EU 005 412 880, EU 010 988 411, DPMA 30 2014 077 312, EUIPO 015 887 442, "
        "EU 008 776 015, EUIPO 018 502 311 — kumulativ)", S_NORMAL))
    s.append(Paragraph(
        "<b>Verfahrenswert:</b> vorläufig EUR 1.200.000,00 (1/4 des Hauptsachewertes von "
        "EUR 4.800.000,00)", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>A N T R Ä G E</b>", S_CENTER))
    s.append(Spacer(1, 0.1*cm))
    s.append(Paragraph(
        "Wir beantragen, das Gericht möge — wegen besonderer Dringlichkeit ohne mündliche "
        "Verhandlung, § 937 Abs. 2 ZPO — wie folgt erkennen:", S_NORMAL))
    s.append(Paragraph(
        "<b>I.</b> Den Antragsgegnerinnen wird bei Meidung eines vom Gericht für jeden Fall der "
        "Zuwiderhandlung festzusetzenden Ordnungsgeldes bis zu EUR 250.000,00 — ersatzweise "
        "Ordnungshaft bis zu sechs Monaten —, oder Ordnungshaft bis zu sechs Monaten, im Falle "
        "wiederholter Zuwiderhandlung bis zu insgesamt zwei Jahren, zu vollziehen an dem "
        "jeweiligen Geschäftsführer bzw. dem Komplementär persönlich (§ 890 Abs. 1 und 2 ZPO), "
        "untersagt, im geschäftlichen Verkehr im Gebiet der Bundesrepublik Deutschland",
        S_NORMAL))
    s.append(Paragraph(
        "(1) Bekleidungsstücke, insbesondere T-Shirts, Halstücher, Schals; (2) Lederwaren, "
        "insbesondere Handtaschen, Geldbörsen; (3) Schuhe; (4) Parfümerieartikel, insbesondere "
        "Eaux de Parfum und deren Flakons — anzubieten, zu vertreiben, einzuführen, auszuführen, "
        "zu bewerben oder bewerben zu lassen, die mit dem Zeichen „K°°“, dem Schriftzug "
        "„klôtzzkètté“ oder einem damit verwechslungsfähigen Zeichen (insbesondere "
        "„klotzkette“, „klotzkettie“, „klötzkette“, „klotzkettiee“, „kloetzkette“) versehen "
        "sind und/oder im Falle der Parfumflakons die hexagonale Form mit asymmetrischem Stopfen "
        "gemäß 3D-Formmarke EU 008 776 015 aufweisen.", S_NORMAL))
    s.append(Paragraph(
        "<b>II.</b> Den Antragsgegnerinnen wird aufgegeben, sämtliche in ihrem Besitz oder "
        "Eigentum befindlichen, unter Ziff. I bezeichneten Waren innerhalb von 48 Stunden ab "
        "Zustellung dieses Beschlusses an einen vom Gericht zu bestellenden Sequester "
        "herauszugeben.", S_NORMAL))
    s.append(Paragraph(
        "<b>III.</b> Die Antragsgegnerinnen tragen gesamtschuldnerisch die Kosten des Verfahrens.",
        S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>B E G R Ü N D U N G</b>", S_CENTER))
    s.append(Paragraph("<b>I. Sachverhalt</b>", S_H3))
    s.append(Paragraph(
        "1. Die Antragstellerin ist die im Jahr 1923 von Antoine-Louis Klôtzzkètté gegründete "
        "französische Maison de Luxe mit Stammsitz in Paris und Filialatelier Via Montenapoleone "
        "27 in Mailand. Sie ist Inhaberin der streitgegenständlichen Marken; im Einzelnen wird "
        "auf die Portfolio-Übersicht (Anlage AS 1) Bezug genommen.", S_NORMAL))
    s.append(Paragraph(
        "2. Die Antragsgegnerin zu 1) ist ein in Süddeutschland operierender Discountfachhandel "
        "mit 47 Filialen. Sie vertreibt seit dem Herbst 2025 nachweislich Waren, die das "
        "Krönchen-Monogramm und/oder den Schriftzug der Antragstellerin tragen, zu Preisen "
        "zwischen EUR 9,99 und EUR 24,99 (Einzelpreis), während die Originalprodukte der "
        "Antragstellerin im Premium-Preissegment (EUR 389 — 2.890) liegen. Auf das vorgerichtliche "
        "Abmahnschreiben vom 22.01.2026 (Anlage AS 4) hat sich die Antragsgegnerin zu 1) mit "
        "Fax-Schreiben vom 04.02.2026 (Anlage AS 5) ausdrücklich geweigert, eine "
        "Unterlassungserklärung abzugeben.", S_NORMAL))
    s.append(Paragraph(
        "3. Die Antragsgegnerin zu 2) betreibt einen der größten Online-Marktplätze für "
        "Drittanbieter im DACH-Raum. Eine systematische Recherche der Antragstellerin "
        "(Anlage AS 6 — 187 Screenshots) hat ergeben, dass zwischen dem 12.01.2026 und dem "
        "07.03.2026 insgesamt <b>2.342 Angebote</b> mit dem Krönchen-Monogramm der Antragstellerin "
        "über den Marktplatz der Antragsgegnerin zu 2) abrufbar waren; davon waren 1.918 zum "
        "Erhebungszeitpunkt noch aktiv. Die Antragstellerin hat die Antragsgegnerin zu 2) am "
        "29.01.2026 und am 12.02.2026 förmlich nach Art. 16 DSA in Kenntnis gesetzt (Anlage AS 7); "
        "die beanstandeten Angebote wurden nur teilweise entfernt (Quote: 23 %).", S_NORMAL))
    s.append(Paragraph(
        "4. Am 09.03.2026 wurde der Antragstellerin durch die Detektivin Karla Kalt-Bandel "
        "(Spürnase-Couture GmbH, Frankfurt) mitgeteilt, dass die Antragsgegnerin zu 1) "
        "vorbereitende Handlungen für einen Auftritt auf der Messe Pitti Uomo (Florenz, "
        "11.03. — 15.03.2026), Halle 7, Stand B-44, unter dem Eigennamen „Brezelmann Luxe Outlet“ "
        "ankündigt — namentlich seien dort Waren der oben bezeichneten Art zum Verkauf vorgesehen. "
        "Eidesstattliche Versicherung der Detektivin Karla Kalt-Bandel vom 10.03.2026 als "
        "<b>Anlage AS 8</b> beigefügt.", S_NORMAL))
    return s

story += blatt_antragsschrift_ev()
story.append(PageBreak())

# Antragsschrift Teil 2 (Rechtliche Würdigung)
def blatt_antragsschrift_ev_2():
    s = []
    s.append(Paragraph("<b>— Antragsschrift Bl. 2/4 —</b>", S_RIGHT))
    s.append(Paragraph("<b>II. Verfügungsanspruch</b>", S_H3))
    s.append(Paragraph(
        "1. Der Verfügungsanspruch ergibt sich aus § 14 Abs. 5 i.V.m. Abs. 2 Nr. 1, 2 und 3 "
        "MarkenG bzw. — vorrangig hinsichtlich der Unionsmarken — Art. 130 i.V.m. Art. 9 Abs. 2 "
        "lit. a, b und c UMV.", S_NORMAL))
    s.append(Paragraph(
        "2. Hinsichtlich der Wortmarke <b>EU 005 412 880</b> „klôtzzkètté“ und der "
        "Wort-/Bildmarke <b>EU 010 988 411</b> liegt eine Doppelidentität gem. Art. 9 Abs. 2 "
        "lit. a UMV vor, soweit die Antragsgegnerin zu 1) Produkte unter dem Schriftzug "
        "„klötzkette“ feilbietet. Eine solche Marken-Doppelidentität führt zum absoluten "
        "Schutz; auf eine Verwechslungsgefahr kommt es nicht an (vgl. EuGH, 22.09.2011, "
        "C-323/09 — <i>Interflora</i>, Rn. 38).", S_NORMAL))
    s.append(Paragraph(
        "3. Hinsichtlich der Wort-/Bildmarke und der Bildmarke (DPMA 30 2014 077 312) sowie "
        "der Positionsmarke (EUIPO 015 887 442) liegt jedenfalls hochgradige Verwechslungsgefahr "
        "(Art. 9 Abs. 2 lit. b UMV) vor. Die Gesamtbeurteilung (vgl. EuGH, 11.11.1997, C-251/95 — "
        "<i>Sabel/Puma</i>) ergibt:", S_NORMAL))
    s.append(Paragraph(
        "(aa) <b>Zeichenähnlichkeit:</b> Das Krönchen-Monogramm „K°°“ wird in den "
        "Verletzungsformen unverändert übernommen — visuelle Ähnlichkeit nahe 100 %, klanglich "
        "ohnehin identisch.<br/>"
        "(bb) <b>Warenidentität:</b> Bekleidung (Kl. 25), Lederwaren (Kl. 18), Parfum (Kl. 3) "
        "— durchgehend Identität.<br/>"
        "(cc) <b>Kennzeichnungskraft:</b> Die Antragstellerin gilt nach Verkehrsbefragung "
        "(Allensbach IfD 2024, 73 % Zuordnungsgrad) im Premium-Segment als überdurchschnittlich "
        "kennzeichnungskräftig, im Bereich der Krönchen-Marke als bekannt i.S.v. Art. 9 Abs. 2 "
        "lit. c UMV.<br/>"
        "(dd) <b>Maßgeblicher Verkehr:</b> auch der durchschnittlich aufmerksame und informierte "
        "Verbraucher (vgl. EuGH, 22.06.1999, C-342/97 — <i>Lloyd Schuhfabrik Meyer</i>) wird die "
        "Zeichen verwechseln; erst recht der Premium-Konsument, dem die feinen Unterschiede "
        "nicht hinreichend deutlich werden.", S_NORMAL))
    s.append(Paragraph(
        "4. Hinsichtlich der <b>3D-Formmarke EU 008 776 015</b> (hexagonaler Flakon mit "
        "asymmetrischem Stopfen) liegt eine identische Übernahme vor. Die Schutzfähigkeit "
        "ist nach Art. 7 Abs. 1 lit. e UMV bestandskräftig — eine technische Bedingtheit der "
        "Form ist nicht gegeben (vgl. EuGH, 14.09.2010, C-48/09 P — <i>Lego</i>, sowie BGH, "
        "18.10.2017 — I ZB 22/20, <i>Quadratisch Praktisch Gut</i>).", S_NORMAL))
    s.append(Paragraph(
        "5. Eine Erschöpfung der Markenrechte (Art. 15 UMV / § 24 MarkenG) — von der Antrags"
        "gegnerin zu 1) im Fax vom 04.02.2026 vage behauptet („Graumarkt-Import Turin“) — "
        "scheidet aus. Die Antragstellerin unterhält ein selektives Vertriebssystem (vgl. EuGH, "
        "06.12.2017, C-230/16 — <i>Coty Germany/Akzente</i>, GRUR 2018, 211), das den Vertrieb "
        "ausschließlich an autorisierte Boutiquen vorsieht. Die Antragsgegnerinnen sind nicht "
        "autorisiert. Ferner liegen <b>berechtigte Gründe</b> i.S.d. Art. 15 Abs. 2 UMV vor: "
        "Der Vertrieb über Discount-Filialen zerstört das Premium-Image und stellt eine "
        "Schädigung der Markenwertschätzung dar (vgl. EuGH, 23.04.2009, C-59/08 — "
        "<i>Copad/Dior</i>, Rn. 35 ff.).", S_NORMAL))
    s.append(Paragraph(
        "6. Hinsichtlich der Antragsgegnerin zu 2) (Donauzon Marketplace GmbH) folgt die "
        "Haftung als <i>Täterin</i> (jedenfalls aber als <i>Mittäterin/Gehilfin</i>) aus den "
        "Grundsätzen des EuGH, Urt. v. 22.12.2022, C-148/21 und C-184/21 — "
        "<i>Louboutin/Amazon</i>, GRUR 2023, 264, Rn. 50 ff., dahin, dass Marktplatzbetreiber "
        "dann selbst markenmäßige Benutzungshandlungen begehen, wenn sie eigene Logistik-, "
        "Werbe- und Versandinfrastruktur einbinden und Dritte hierdurch unmittelbar in der "
        "Verbreitung verletzender Waren unterstützen. Die Antragsgegnerin zu 2) erfüllt diese "
        "Kriterien (Fulfillment-by-Donauzon, „Empfohlen für Dich“-Algorithmus, Donauzon-"
        "Markenpräsentationssystem mit „K°°-Krönchen“-Filter — siehe Screenshot AS 9). "
        "Die Inanspruchnahme des Haftungsprivilegs Art. 6 ff. DSA setzt jedenfalls "
        "Untätigkeit nach Notice voraus, woran es hier fehlt (nur 23 % Take-Down-Quote).", S_NORMAL))
    s.append(Paragraph("<b>III. Verfügungsgrund</b>", S_H3))
    s.append(Paragraph(
        "1. Der Verfügungsgrund (Dringlichkeit) ist im Bereich der Markenrechtsverletzungen "
        "nach ständiger Rechtsprechung der hessischen Markenrechtskammern dringlichkeits"
        "vermutend zu beurteilen, solange nicht mehr als vier Wochen seit Kenntnis vergangen "
        "sind. Die Antragstellerin hat von dem aktuellen Verletzungsumfang erst am 09.03.2026 "
        "(Mitteilung Detektei) erfahren; der Antrag ist am 11.03.2026, also <i>am Tag des "
        "Messebeginns</i> Pitti Uomo, eingereicht. Dringlichkeit ist mithin gegeben.", S_NORMAL))
    s.append(Paragraph(
        "2. Bei einem Aufschub droht der Antragstellerin endgültiger, nicht wiedergutzu"
        "machender Schaden: Eine Sichtung gefälschter klôtzzkètté-Produkte auf der "
        "internationalen Leitmesse Pitti Uomo (Besucherzahl 2025: 32.000 Fach- und 8.000 "
        "Premium-Endkunden) hat ungleich höheren Markenimage-Schaden als jeder denkbare "
        "Verletzergewinn der Antragsgegnerinnen. <i>Periculum in mora</i> (vgl. <i>lite "
        "pendente</i>-Doktrin sinngemäß).", S_NORMAL))
    s.append(Paragraph("<b>IV. Glaubhaftmachung</b>", S_H3))
    s.append(Paragraph(
        "Der Antrag wird glaubhaft gemacht durch:<br/>"
        "• Anlage AS 1: Markenportfolio-Auszüge (Registerauszüge DPMA/EUIPO);<br/>"
        "• Anlage AS 2: Verkehrsbefragung Allensbach IfD 2024;<br/>"
        "• Anlage AS 3: Eidesstattliche Versicherung der Comtesse de Klôtzzkètté-Visconti "
        "vom 10.03.2026;<br/>"
        "• Anlage AS 4: Abmahnschreiben vom 22.01.2026;<br/>"
        "• Anlage AS 5: Fax-Antwort Brezelmann vom 04.02.2026;<br/>"
        "• Anlage AS 6: 187 Screenshots Donauzon-Marktplatz;<br/>"
        "• Anlage AS 7: DSA-Notices vom 29.01. und 12.02.2026;<br/>"
        "• Anlage AS 8: Eidesstattliche Versicherung Karla Kalt-Bandel vom 10.03.2026 "
        "nebst Foto-Dossier (Aufn. 1-14);<br/>"
        "• Anlage AS 9: Screenshot „K°°-Krönchen“-Filter Donauzon vom 07.03.2026.", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("München, 11.03.2026", S_NORMAL_LEFT))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("gez. <b>Dr. Dr. Annabella Steinacker-von Tarsis</b>, LL.M. (Cantab.)", S_NORMAL_LEFT))
    s.append(Paragraph("Rechtsanwältin", S_SMALL))
    s.append(Paragraph("gez. <b>Maximilian Freiherr von Brenkenhoff</b>", S_NORMAL_LEFT))
    s.append(Paragraph("Rechtsanwalt", S_SMALL))
    s.append(Spacer(1, 0.3*cm))
    s.append(HandNote(
        "Übergabe an Wachtmeisterei 11.03.26 — 06:48 Uhr Frühflug MUC-FRA\nVors. RaG Hoffacker-Wendel persönlich übergeben — Beschluss noch am selben Tag!\nZustellung Florenz: Carabiniere via Tribunale di Firenze\n→ Sequester: RA Dr. Maletti (Mailand) bereits informiert.",
        font=FONT_HAND, size=14, color=colors.HexColor("#1e3a6e"), w=15*cm, angle=-0.6))
    return s

story += blatt_antragsschrift_ev_2()
story.append(PageBreak())

print("[part04] done")
