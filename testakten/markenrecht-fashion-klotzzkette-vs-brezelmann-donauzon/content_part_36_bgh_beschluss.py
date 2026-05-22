# -*- coding: utf-8 -*-
# Part 36: BGH-Beschwerdebeschluss Soundmarke + Anhang gutachterlicher Stellungnahme

def blatt_bgh_beschluss():
    s = []
    s.append(Paragraph("BUNDESGERICHTSHOF", S_H1))
    s.append(Paragraph("I. ZIVILSENAT", S_H2))
    s.append(Paragraph("BESCHLUSS", S_CENTER))
    s.append(Spacer(1, 4*mm))
    s.append(Paragraph("I ZB 14/26", S_RIGHT))
    s.append(Paragraph("verkündet am 28. April 2026", S_RIGHT))
    s.append(Paragraph("Krempelmann-Esch, Justizangestellte<br/>als Urkundsbeamtin der Geschäftsstelle", S_RIGHT))
    s.append(HLine())
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph(
        "In der Rechtsbeschwerdesache",
        S_NORMAL))
    s.append(Paragraph(
        "der <b>klôtzzkètté Société Anonyme</b>, 12 rue du Faubourg Saint-Honoré, F-75008 Paris, "
        "vertreten durch den Verwaltungsrat, dieser vertreten durch die Présidente du Conseil "
        "d'Administration, Comtesse Béatrice de Klôtzzkètté-Visconti,",
        S_NORMAL))
    s.append(Paragraph("— Rechtsbeschwerdeführerin und Anmelderin —", S_RIGHT))
    s.append(Paragraph(
        "Verfahrensbevollmächtigte: Rechtsanwälte Steinacker Lichtenberg & Partners "
        "IP Boutique, Maximiliansplatz 19, 80333 München",
        S_NORMAL))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("g e g e n", S_CENTER))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph(
        "den Beschluss des 25. Senats (Markenbeschwerdesenat) des Bundespatentgerichts vom "
        "17. Februar 2026 — Az. 25 W (pat) 88/26 —",
        S_NORMAL))
    s.append(Paragraph(
        "betreffend die Anmeldung Nr. 30 2025 218 446 (Hörmarke — sechstöniges Klangsignal "
        "im Modus B-Dur, sog. <i>klôtzzkètté-Boutique-Glockenspiel</i>, Notation: g'–c''–e''–g''–a''–g'')",
        S_NORMAL))
    s.append(Spacer(1, 4*mm))
    s.append(Paragraph(
        "hat der I. Zivilsenat des Bundesgerichtshofs auf die mündliche Verhandlung vom "
        "9. April 2026 durch den Vorsitzenden Richter Prof. Dr. Heribert Köstner, die Richter "
        "Dr. Ingelore Bachmeier-Lutz, Dr. Reiner Holzgreve und die Richterinnen Dr. Klothilde "
        "Pfeifer-Sembach sowie Dr. Annegret Strehlke-Wißmann",
        S_NORMAL))
    s.append(Paragraph("b e s c h l o s s e n :", S_CENTER))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph(
        "<b>I.</b> Auf die Rechtsbeschwerde der Anmelderin wird der Beschluss des "
        "Bundespatentgerichts vom 17. Februar 2026 aufgehoben.",
        S_NORMAL))
    s.append(Paragraph(
        "<b>II.</b> Die Sache wird zur erneuten Verhandlung und Entscheidung — auch über die "
        "Kosten des Rechtsbeschwerdeverfahrens — an das Bundespatentgericht zurückverwiesen.",
        S_NORMAL))
    s.append(Paragraph(
        "<b>III.</b> Der Streitwert für das Rechtsbeschwerdeverfahren wird auf "
        "EUR 50.000,— festgesetzt.",
        S_NORMAL))
    s.append(PageBreak())

    # Gründe
    s.append(Paragraph("G r ü n d e :", S_H2))
    s.append(Paragraph(
        "<b>A.</b> Die Anmelderin meldete am 14. November 2025 beim Deutschen Patent- und "
        "Markenamt das im Tenor näher bezeichnete sechstönige Klangsignal als Hörmarke für "
        "Waren und Dienstleistungen der Klassen 14, 18, 25 und 35 (insbesondere Türklingelton, "
        "POS-Audio, Werbespots, Boutique-Ambiente) an. Das DPMA wies die Anmeldung mit Beschluss "
        "vom 8. Januar 2026 zurück. Auf die Erinnerung der Anmelderin änderte die Markenstelle "
        "ihre Auffassung nicht. Die Beschwerde zum Bundespatentgericht blieb erfolglos.",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "Das Bundespatentgericht hat ausgeführt, dem angemeldeten Zeichen fehle die "
        "Unterscheidungskraft (§ 8 Abs. 2 Nr. 1 MarkenG); die Tonfolge sei zu kurz, zu banal "
        "und werde vom Verkehr als bloßes Gestaltungselement, nicht als betrieblicher "
        "Herkunftshinweis aufgefasst. Die Anmelderin habe auch nicht ausreichend dargelegt, "
        "dass sich das Zeichen im Verkehr durchgesetzt habe (§ 8 Abs. 3 MarkenG).",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "Mit der vom Bundespatentgericht zugelassenen Rechtsbeschwerde verfolgt die Anmelderin "
        "ihren Eintragungsantrag weiter.",
        S_NORMAL_LEFT))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph(
        "<b>B.</b> Die zulässige Rechtsbeschwerde ist begründet. Sie führt zur Aufhebung des "
        "angegriffenen Beschlusses und zur Zurückverweisung der Sache an das Bundespatentgericht.",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "<b>I.</b> Das Bundespatentgericht hat einen unzutreffenden Maßstab an die "
        "Unterscheidungskraft kurzer Hörmarken angelegt.",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "1. Nach ständiger Senatsrechtsprechung (vgl. BGH, Beschluss vom 18. April 2024 — "
        "I ZB 35/22 — <i>Telekom-Jingle II</i>, GRUR 2024, 988 Rn. 14 ff.; BGH, GRUR 2008, 1093 "
        "Rn. 15 — <i>Marlene-Dietrich-Bildnis I</i>) sind an die Unterscheidungskraft von "
        "Hörmarken keine strengeren Anforderungen zu stellen als an andere Markenformen. Dies "
        "folgt auch aus der Rechtsprechung des Gerichtshofs der Europäischen Union "
        "(EuGH, Urteil vom 27. November 2003 — C-283/01 — <i>Shield Mark/Kist</i>, "
        "Slg. 2003, I-14313 Rn. 36 ff.).",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "2. Das Bundespatentgericht hat verkannt, dass eine sechstönige, in sich melodisch "
        "geschlossene Tonfolge nicht von vornherein als zu kurz oder zu banal angesehen werden "
        "darf. Maßgeblich ist vielmehr, ob die konkrete Tonfolge — unter Berücksichtigung der "
        "beanspruchten Waren und Dienstleistungen — vom angesprochenen Verkehr als "
        "betrieblicher Herkunftshinweis aufgefasst werden kann.",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "3. Die Anmelderin hat substantiiert vorgetragen, dass die hier in Rede stehende "
        "Tonfolge seit 1962 durchgehend als akustische Türklingel in sämtlichen klôtzzkètté-"
        "Boutiquen weltweit eingesetzt wird und in einer von der IPSOS-MORI Deutschland GmbH "
        "im Juli 2025 durchgeführten Verkehrsbefragung von 41,3 % der angesprochenen Käuferinnen "
        "der Luxusmode-Zielgruppe spontan und von weiteren 22,8 % nach Hörprobe der Anmelderin "
        "zugeordnet werden konnte. Diesem Vortrag hätte das Bundespatentgericht im Rahmen der "
        "Prüfung nach § 8 Abs. 3 MarkenG nachgehen müssen.",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "<b>II.</b> Da die tatsächlichen Feststellungen für eine abschließende Entscheidung "
        "nicht ausreichen, ist die Sache an das Bundespatentgericht zurückzuverweisen.",
        S_NORMAL_LEFT))
    s.append(PageBreak())

    # Anhang - gutachterliche Stellungnahme
    s.append(Paragraph("ANHANG — gutachterliche Stellungnahme (Auszug)", S_H2))
    s.append(Paragraph(
        "<b>Prof. Dr. phil. habil. Wendelin Tongeber, Hochschule für Musik und Tanz Köln, "
        "Institut für Musikwissenschaft und Werbeforschung</b>",
        S_NORMAL))
    s.append(Paragraph("— Stellungnahme zur akustischen Unterscheidungskraft der Tonfolge "
        "<i>g'–c''–e''–g''–a''–g''</i> (klôtzzkètté-Glockenspiel, 1962/2025) —", S_ITAL))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("<b>1. Musikwissenschaftlicher Befund.</b> Die zu untersuchende Tonfolge stellt "
        "in struktureller Hinsicht eine sog. <i>melodische Geste mit terzaufwärts-quartabwärts-"
        "Schluss</i> dar (g'–c''–e''–g''–a''–g''), die ungeachtet ihrer Kürze über drei "
        "musikalisch signifikante Eigenschaften verfügt: (a) tonale Eindeutigkeit in C-Dur mit "
        "leittöniger Spannung über das h''; (b) rhythmische Asymmetrie 3+3+2 in der Sechzehntel-"
        "Notation; (c) charakteristisches obertonreiches Klangbild durch die Verwendung "
        "messingener Glocken mit ø 7,4 cm bzw. 5,1 cm.",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "<b>2. Werbewissenschaftliche Einordnung.</b> Die Tonfolge erfüllt nach der Typologie "
        "von Kellaris/Cox (1989) und der erweiterten Kategorisierung Tongeber/Steinhart (2021) "
        "sämtliche Merkmale eines sog. <i>Sonic Logos</i>: Kürze (< 3 sek), tonale Geschlossenheit, "
        "Wiedererkennbarkeit nach einmaliger Exposition, emotionale Konnotation (in der "
        "vorgenannten IPSOS-Studie: 67,2 % »elegant/diskret«, 41,9 % »französisch«, "
        "29,8 % »teuer«).",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "<b>3. Vergleich mit anderen geschützten Hörmarken.</b> Mit lediglich sechs Tönen "
        "liegt die hier streitgegenständliche Tonfolge zwischen dem Deutschen-Telekom-Jingle "
        "(5 Töne, EU-Marke 000 173 642, eingetragen 1999) und dem Nokia-Klingelton (13 Töne, "
        "<i>Gran Vals</i>-Auszug). Eine generelle Untauglichkeit von Tonfolgen zwischen 5 und 8 "
        "Tönen zur Vermittlung betrieblicher Herkunftshinweise ist musik- und werbewissenschaftlich "
        "nicht haltbar.",
        S_NORMAL_LEFT))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("Köln, den 14. März 2026", S_RIGHT))
    s.append(Paragraph("Prof. Dr. phil. habil. W. Tongeber<br/>(Sachverständiger)", S_RIGHT))
    return s

story += blatt_bgh_beschluss()
story.append(PageBreak())
print("[part36] done")
