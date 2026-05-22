# Part 25: DPMA Löschungsantrag gegen kleinere Anmeldung "klotzkettiee" (Doppel-E)
def blatt_loeschungsantrag():
    s = []
    s.append(Briefkopf(
        kanzlei_block=("USt-IdNr.: DE 271 884 117\n"
                       "Steuer-Nr.: 143/261/00012\n"
                       "Kammer: München I\n"
                       "Mandatsnummer: 26-1014-KK"),
        recipient_block=("An das\nDeutsche Patent- und Markenamt\n"
                          "— Markenabteilung 3.4 —\n"
                          "Cincinnatistraße 64\n80686 München\n\n"
                          "vorab per DPMAdirektPro"),
        datum="22. Mai 2026",
        az="2-03 O 412/26 ./. DPMA 30 2026 100 217 (Löschungsverf.)"))
    s.append(Spacer(1, 0.5*cm))
    s.append(Paragraph(
        "<b>ANTRAG AUF ERKLÄRUNG DER NICHTIGKEIT WEGEN ABSOLUTER SCHUTZHINDERNISSE "
        "UND/ODER BÖSGLÄUBIGER ANMELDUNG</b>", S_CENTER))
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("<b>Antragstellerin:</b>", S_NORMAL))
    s.append(Paragraph(
        "<b>klôtzzkètté S.A.</b><br/>"
        "12 rue du Faubourg Saint-Honoré · 75008 Paris (Frankreich)<br/>"
        "RCS Paris 552 094 471<br/>"
        "vertreten durch ihre Präsidentin Comtesse Béatrice de Klôtzzkètté-Visconti<br/>"
        "— diese vertreten durch die unterzeichnenden Bevollmächtigten —", S_SMALL))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph("<b>Antragsgegnerin:</b>", S_NORMAL))
    s.append(Paragraph(
        "<b>Egon Brezelmann e.K. — Bad Mergentheim</b><br/>"
        "Wurstgasse 4 · 97980 Bad Mergentheim<br/>"
        "HR-Nr. HRA 1442 / AG Stuttgart<br/>"
        "vertreten durch sich selbst (kein Bevollmächtigter im Register)", S_SMALL))
    s.append(Spacer(1, 0.2*cm))
    s.append(Paragraph(
        "<b>angegriffene Marke:</b> DE 30 2026 100 217 — <b>klotzkettiee</b> (Wortmarke), "
        "angemeldet 12.01.2026, eingetragen 04.03.2026, Klassen 25, 30 (!) und 32 (!!).",
        S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "<b>In dem Markennichtigkeitsverfahren</b> stellen wir gemäß § 50 Abs. 1, § 8 Abs. "
        "2 Nr. 1, 2, 4 und 14 MarkenG sowie wegen Bösgläubigkeit nach § 8 Abs. 2 Nr. 14 "
        "MarkenG i.V.m. Art. 59 Abs. 1 lit. b EUTMR (analog) den", S_NORMAL))
    s.append(Paragraph(
        "<b>ANTRAG</b>", S_CENTER))
    s.append(Paragraph(
        "die Eintragung der oben bezeichneten deutschen Marke DE 30 2026 100 217 "
        "<b>vollständig zu löschen</b>, hilfsweise für die Klassen 30 und 32 zu löschen, "
        "höchst hilfsweise eine Beschränkung des Warenverzeichnisses anzuordnen.",
        S_NORMAL))
    s.append(Paragraph("<b>Begründung:</b>", S_H3))
    s.append(Paragraph("<b>I. Sachverhalt</b>", S_H3))
    s.append(Paragraph(
        "1. Die Antragstellerin ist Inhaberin einer Vielzahl international und europaweit "
        "geschützter Marken der Wort- und Bildmarke „klôtzzkètté“ (vgl. Markenportfolio "
        "Bl. 3–4). Die Antragstellerin ist im Übrigen die <i>unbestrittene</i> Mutter der "
        "klôtzzkètté-Familie.", S_NORMAL))
    s.append(Paragraph(
        "2. Die Antragsgegnerin, Egon Brezelmann e.K. aus Bad Mergentheim, ist als "
        "Discounter im Lebensmittelbereich tätig. Zum Geschäftsfeld gehören in keiner "
        "erkennbaren Weise Mode-, Luxus- oder Bekleidungswaren. Ausweislich des "
        "Handelsregisters umfasst der Geschäftsgegenstand „Vertrieb von Wurst- und "
        "Brezelwaren sowie ergänzenden Discounterartikeln“ (HRA 1442, AG Stuttgart).",
        S_NORMAL))
    s.append(Paragraph(
        "3. Bereits am 14.02.2026, also nur 33 Tage nach Anmeldung der streitgegenständlichen "
        "Marke, hat die Antragsgegnerin durch dasselbe Vertretungsorgan die — den Kollegen "
        "DPMA bereits vorgelegte — frühere Anmeldung „Klotz-Kette“ (DE 30 2025 218 552) "
        "im Wege einer Mehrfachanmeldungsstrategie auf ungewöhnliche Klassen ausgeweitet. "
        "Schon dies erweckt den Verdacht systematischer Spekulation.", S_NORMAL))
    s.append(Paragraph(
        "4. Die angegriffene Marke „klotzkettiee“ unterscheidet sich von dem Kennzeichen "
        "der Antragstellerin nur durch (a) das fehlende Diakritikon (ô, è, é) und (b) ein "
        "verdoppeltes „e“ am Ende. Beide Modifikationen sind kennzeichenrechtlich "
        "<i>de minimis</i>.", S_NORMAL))
    s.append(Paragraph("<b>II. Rechtliche Würdigung</b>", S_H3))
    s.append(Paragraph(
        "5. <b>§ 8 Abs. 2 Nr. 14 MarkenG (Bösgläubigkeit).</b> Die Anmeldung erfolgte "
        "in Behinderungs- bzw. Spekulationsabsicht. Der Anmelder kannte oder konnte die "
        "ältere Marke der Antragstellerin nicht ignorieren (vgl. Internationaler Ruf, "
        "Vogue, Harper's Bazaar, GQ, Süddeutsche Zeitung et al.). Bezeichnend ist, dass "
        "die Anmelderin die Marke auch für Klassen 30 (Brezeln, Brot, Backwaren) und 32 "
        "(Biere, Mineralwasser) anmeldete — ein offensichtlicher Versuch, durch breite "
        "Klassenstreuung die Anschlussverwertung zu sichern oder die Marke an die "
        "Antragstellerin teuer zu verkaufen.", S_NORMAL))
    s.append(Paragraph(
        "6. <b>§ 8 Abs. 2 Nr. 4 MarkenG (Täuschungseignung).</b> Die Marke ist geeignet, "
        "den Verkehr über die geographische Herkunft, Eigenschaft oder Reputation der "
        "Waren zu täuschen. Verbraucher würden bei „klotzkettiee“-Brezeln annehmen, dass "
        "eine Cobranding-Aktion mit dem französischen Luxushaus stattfindet — was nicht "
        "der Fall ist.", S_NORMAL))
    s.append(Paragraph(
        "7. <b>§ 9 Abs. 1 Nr. 2 und 3 MarkenG i.V.m. § 51 MarkenG (relative "
        "Schutzhindernisse).</b> Insoweit besteht <i>kollidierende</i> Verwechslungsgefahr "
        "mit den prioritätsälteren Marken der Antragstellerin in den identischen oder "
        "ähnlichen Klassen 25 und 14, sowie eine Beeinträchtigung des Rufes (bekannte "
        "Marke) auch im Hinblick auf Klassen 30 und 32 nach § 9 Abs. 1 Nr. 3 MarkenG "
        "(<i>vgl. BGH, I ZR 35/19 — „Pippi Langstrumpf“-ähnlicher Schutz für bekannte "
        "Modenamen</i>).", S_NORMAL))
    s.append(Paragraph(
        "8. <b>Beweismittel:</b>", S_NORMAL))
    items = [
        "B-1: Markenportfolio der Antragstellerin (Auszug, 12 Seiten);",
        "B-2: Ipsos-Mori Brand Awareness Survey 2024 (Deutschland; aided 41 %);",
        "B-3: Spürnase-Couture GmbH Detektivbericht 04.03.2026 (Bl. 24 ff.);",
        "B-4: Auszug Register klotzkettiee mit Klassen 25/30/32 — DPMA-Beleg;",
        "B-5: Parallele Anmeldung „Klotz-Kette“ DE 30 2025 218 552 — Spekulationsindiz;",
        "B-6: Email-Korrespondenz Brezelmann-Steinacker („wollen Sie sie kaufen?“ am "
        "21.01.2026, Bl. 33);",
        "B-7: Schreiben Antragsgegnerin an Mitkonkurrent „LumièreLuxe AG“ vom 03.02.2026 "
        "mit Angebot zur Ablösung der Marke gegen EUR 380.000 (Bl. 34).",
    ]
    for it in items:
        s.append(Paragraph(it, ParagraphStyle("li", parent=S_NORMAL, leftIndent=18,
                                               firstLineIndent=-18)))
    return s

story += blatt_loeschungsantrag()
story.append(PageBreak())

def blatt_loeschungsantrag_2():
    s = []
    s.append(Paragraph("<b>III. Antrag auf Sicherstellung des Verkehrsschutzes</b>", S_H3))
    s.append(Paragraph(
        "9. Hilfsweise wird angeregt, eine einstweilige Anordnung der Markenabteilung "
        "nach § 56 Abs. 1 i.V.m. § 50 Abs. 2 MarkenG zu erlassen, mit der die "
        "Eintragungswirkung der angegriffenen Marke bis zum Abschluss des "
        "Nichtigkeitsverfahrens ausgesetzt wird.", S_NORMAL))
    s.append(Paragraph("<b>IV. Kosten und Streitwert</b>", S_H3))
    s.append(Paragraph(
        "10. Es wird beantragt, der Antragsgegnerin die Kosten des Verfahrens nach § 63 "
        "Abs. 1 MarkenG aufzuerlegen.", S_NORMAL))
    s.append(Paragraph(
        "11. Der Gegenstandswert wird auf <b>EUR 250.000,00</b> festgesetzt "
        "(Streitwertfestsetzung gemäß § 23 RVG; vgl. zur Bemessung BPatG GRUR 2018, 1234).",
        S_NORMAL))
    s.append(Paragraph(
        "12. Verfahrensgebühr nach Nr. 401 RVG-VV: EUR 1.880,00 (1,3-fache). "
        "Inklusive Auslagenpauschale und USt: ca. EUR 2.295,00 — vorgemerkt.", S_NORMAL))
    s.append(Paragraph("<b>V. Zustellungsanschrift</b>", S_H3))
    s.append(Paragraph(
        "Zustellungen werden erbeten an die unterzeichnende Kanzlei, "
        "Steinacker Lichtenberg &amp; Partners IP Boutique, Maximiliansplatz 19, "
        "80333 München; vorzugsweise über das beA / DPMAdirektPro-Postfach 00-7711-22.",
        S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(
        "Vorsorglich rügen wir bereits hier vorsorglich die Verspätung etwaiger "
        "verspäteter Schriftsätze der Gegenseite und bitten um Beachtung von § 53 MarkenG.",
        S_NORMAL))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph(
        "<b>Dr. Dr. Annabella Steinacker-von Tarsis, LL.M. (Cantab.)</b><br/>"
        "Rechtsanwältin · Fachanwältin für gewerblichen Rechtsschutz<br/>"
        "Steinacker Lichtenberg &amp; Partners IP Boutique", S_SMALL))
    s.append(Spacer(1, 0.4*cm))
    s.append(HLine())
    s.append(Paragraph("<b>Anlage B-6 — Auszug E-Mail Brezelmann vom 21.01.2026</b>", S_H3))
    s.append(Paragraph(
        "(stilistische Wiedergabe; Originalrechtschreibung beibehalten)", S_SMALL))
    s.append(Spacer(1, 0.2*cm))
    monomails = [
        "From:    egon.brezelmann@bm-discount.de",
        "To:      kanzlei@steinacker-lichtenberg.de",
        "Date:    21.01.2026  17:32",
        "Subject: Re: Ihr schreiben wegen marken-anmeldung",
        "",
        "Hallo Frau Doktor Dr Steinacker,",
        "",
        "ja klar habe ich da was angemeldet. Klotzkettiee, mit doppel-e, das ist",
        "ja schliesslich was ganz anderes als bei Ihrer Mandantschaft mit dem",
        "französichen Strichlein-Krempel. Sie wollen also dass ich es loesche.",
        "Ich sage: wir können da reden. Für EUR 290.000,- gebe ich es ab. Plus",
        "Mehrwertsteuer natürlich. Wäre günstiger als Anwalt nicht?",
        "",
        "Mit freundlichen Gruessen",
        "Egon Brezelmann",
        "Brezelmann Discount KG, Wurstgasse 4, 97980 Bad Mergentheim",
        "T 07931 / 88-0  ·  F 07931 / 88-99",
        "",
        ">> -----Ursprüngliche Nachricht-----",
        ">> Von: kanzlei@steinacker-lichtenberg.de",
        ">> ...",
        ">> Die von Ihnen angemeldete Marke „klotzkettiee“ kollidiert mit den",
        ">> bestehenden Schutzrechten unserer Mandantschaft. Wir fordern Sie auf,",
        ">> die Anmeldung binnen 14 Tagen zurückzunehmen ...",
    ]
    for ln in monomails:
        s.append(Paragraph(ln.replace(' ', '&nbsp;'), S_MONO_SMALL))
    s.append(Spacer(1, 0.3*cm))
    s.append(HandNote(
        "EUR 290.000! Und „französischer Strichlein-Krempel“.\n"
        "Comtesse darf das nicht lesen.\n"
        "Hauptsache, die Mail liegt in der Akte —\n"
        "als Bösgläubigkeits-Beleg nicht zu schlagen.\n"
        "— A.St., 22.01.2026",
        font=FONT_HAND, size=14, angle=-0.8, w=15*cm))
    return s

story += blatt_loeschungsantrag_2()
story.append(PageBreak())

print("[part25] done")
