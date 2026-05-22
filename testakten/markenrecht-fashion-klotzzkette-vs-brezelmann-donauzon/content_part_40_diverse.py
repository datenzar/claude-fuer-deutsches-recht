# -*- coding: utf-8 -*-
# Part 40: Diverse Akteneinlagen — Sieckmann-Hinterlegung, Tastenberger-Gutachten Auszug,
# handschriftliche Mlle-Périgord-Notiz, ASCII Logo Final

def blatt_sieckmann_duftmarke():
    s = []
    s.append(Paragraph("DEUTSCHES PATENT- UND MARKENAMT — DPMA", S_H2))
    s.append(Paragraph("Anlage zur Markenanmeldung 30 2026 102 887 (Geruchsmarke)", S_CENTER))
    s.append(Paragraph("»K°° pour Femme« — Duftmarke gem. Sieckmann-Kriterien "
                       "(EuGH C-273/00)", S_CENTER))
    s.append(HLine())
    s.append(Paragraph("<b>I. SCHRIFTLICHE BESCHREIBUNG DES DUFTES</b>", S_H3))
    s.append(Paragraph(
        "Die Duftmarke besteht aus einem komplexen, mehrschichtigen Riechstoffgemisch der "
        "folgenden olfaktorischen Architektur (vermittelt von Mlle. Hortense Périgord, "
        "Parfumeure indépendante, 17 rue Frédéric-Mistral, F-06130 Grasse):",
        S_NORMAL_LEFT))
    s.append(Spacer(1, 2*mm))
    s.append(Paragraph("<b>Kopfnote</b> (0–15 min): Bergamotte calabrese (12 %), "
                       "rosa Pfeffer Madagaskar (4 %), Aldehyd C-12 MNA (1,5 %), "
                       "Petitgrain Paraguay (3 %)", S_NORMAL))
    s.append(Paragraph("<b>Herznote</b> (15 min – 2 h): Damaszener Rose (Türkei, 11 %), "
                       "Iris pallida (Toskana, 9 %), Jasminum sambac absolue (Indien, 4,5 %), "
                       "Heliotropin (2 %)", S_NORMAL))
    s.append(Paragraph("<b>Basisnote</b> (2 – 12 h): Bourbon-Vetiver (Réunion, 7 %), "
                       "Patchouli Sulawesi gealtert 7 Jahre (5,5 %), Ambroxan (3 %), "
                       "Sandelholz Mysore reconstitué (4 %), Moschus Galaxolide (2,5 %)", S_NORMAL))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("<b>II. CHEMISCHE FORMEL (Auszug der 17 Hauptkomponenten)</b>", S_H3))
    s.append(ASCIIBox(r"""
   Komponente                 CAS-Nr.        Anteil (%)    Charakteristik
   ----------------------------------------------------------------------
   Linalylacetat              115-95-7         8,4         frisch-blumig
   Citral (Geranial+Neral)    5392-40-5        3,1         zitrisch-grasig
   Damascenone alpha          23696-85-7       0,8         rosig-tabakig
   beta-Ionone                14901-07-6       2,2         iris-veilchen
   Hedione (Methyldihydrojasm.)24851-98-7      6,7         jasmin-luftig
   Cis-3-Hexenol              928-96-1         0,3         grün-blattig
   Iso-E-Super                54464-57-2       4,9         holzig-samtig
   Galaxolide                 1222-05-5        2,5         moschus-pudrig
   Ambroxan                   3738-00-9        3,0         ambriert-warm
   ... (8 weitere Komponenten, vgl. Anlage 2 z. Anmeldung)
"""))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("<b>III. HINTERLEGUNG EINER GERUCHSPROBE</b>", S_H3))
    s.append(Paragraph(
        "Hinterlegt wurde beim DPMA — zu Händen der Markenstelle 3.4 — am 14.03.2026 "
        "eine Glasflakon-Probe à 30 ml, versiegelt mit Wachssiegel der Maison klôtzzkètté, "
        "Charge KK-FEM-2026-001-A, gelagert unter 18–22 °C, Lichtschutzgrad III. Eine "
        "Rückstellprobe befindet sich beim Institut français du Parfum, 16 rue Berthelot, "
        "F-06130 Grasse, hinterlegt am 09.03.2026 (Dépôt n° IFP-2026-DG-0044).",
        S_NORMAL_LEFT))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("<b>IV. RECHTLICHE ARGUMENTATION</b>", S_H3))
    s.append(Paragraph(
        "Die Anmelderin ist sich bewusst, dass die EuGH-Entscheidung Sieckmann (C-273/00) "
        "an die graphische Darstellbarkeit von Geruchsmarken hohe Anforderungen stellt: "
        "<i>klar, eindeutig, in sich abgeschlossen, leicht zugänglich, verständlich, "
        "dauerhaft, objektiv</i>. Die vorliegende Anmeldung trägt diesen Anforderungen wie "
        "folgt Rechnung: (1) verbale Beschreibung mit klassisch parfumeurischer Pyramide; "
        "(2) chemische Formel der 17 Hauptkomponenten mit Mengenangaben und CAS-Nummern; "
        "(3) physische Hinterlegung einer Probe gemäß Madrider Vereinbarung; (4) "
        "Rückstellprobe bei einer unabhängigen wissenschaftlichen Institution; (5) "
        "Stabilitätsgutachten Prof. Dr. F. Le Conte (Université de Strasbourg) vom 12.03.2026 "
        "über 36-monatige Geruchsstabilität bei sachgerechter Lagerung.",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "<i>Argumentum a maiore ad minus</i>: wenn schon eine schlichte Formel (Sieckmann: "
        "C<sub>6</sub>H<sub>5</sub>-CH=CHCOOCH<sub>3</sub>, Methylzimtsäureester) als ungenügend "
        "verworfen wurde, dann muss <i>a fortiori</i> die hier vorgelegte fünffache "
        "Mehrfachdokumentation als ausreichend gelten. Die Anmelderin regt höflich an, dem "
        "EuGH die Frage im Wege des Vorabentscheidungsverfahrens vorzulegen, sollte die "
        "Markenstelle anderer Auffassung sein.",
        S_NORMAL_LEFT))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("München / Grasse / Strasbourg, den 14.03.2026", S_RIGHT))
    s.append(Paragraph("Dr. Dr. A. Steinacker-von Tarsis<br/>"
                       "(unter Mitwirkung von Mlle. H. Périgord und Prof. Dr. F. Le Conte)", S_RIGHT))
    return s


def blatt_tastenberger_haptik():
    s = []
    s.append(Paragraph("Prof. Dr.-Ing. Hieronymus TASTENBERGER", S_H2))
    s.append(Paragraph("Technische Universität Darmstadt · Institut für Werkstoffkunde und "
                       "Haptik-Engineering · Karolinenplatz 5, 64289 Darmstadt", S_CENTER))
    s.append(HLine())
    s.append(Paragraph("<b>GUTACHTERLICHE STELLUNGNAHME</b> (Kurzfassung)", S_H3))
    s.append(Paragraph("zur tatsächlichen Unterscheidbarkeit der Haptikmarken "
                       "»K°° Touch Royal« (Schal) und »K°° pour Femme« (Flakon) "
                       "von marktüblichen Vergleichsprodukten", S_ITAL))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("Aktenzeichen: TUD-IH-2026-0117 · Auftraggeber: klôtzzkètté S.A. via "
                       "Steinacker LLP", S_NORMAL))
    s.append(Paragraph("Methodik: Tastenberger-24-Punkte-Haptikskala (T24, ISO/TR 9241-940), "
                       "Probandenzahl n = 84 (43 weiblich, 41 männlich), Doppelblindversuch, "
                       "Kruskal-Wallis-Test, α = 0,05.", S_NORMAL))
    s.append(Spacer(1, 3*mm))
    data = [
        ["Eigenschaft (T24-Dimension)", "K°° Schal", "Marktüblich Premium", "Δ T24", "p-Wert"],
        ["1. Glätte-Index (1–24)", "21,4", "16,8", "+4,6", "< 0,001"],
        ["2. Geschmeidigkeit (drape coef.)", "0,38", "0,52", "+0,14", "< 0,001"],
        ["3. Kühle beim Erstkontakt (J/cm²·s^0.5)", "0,247", "0,189", "+0,058", "< 0,01"],
        ["4. Wärmeretention 60s (°C)", "31,8", "29,2", "+2,6", "< 0,01"],
        ["5. Federspeichervermögen", "19,7", "13,4", "+6,3", "< 0,001"],
        ["6. Faltenrückbildung (%/min)", "94,1", "71,8", "+22,3", "< 0,001"],
        ["7. Kantenfühlbarkeit (subj. Score)", "22,1", "15,9", "+6,2", "< 0,001"],
        ["8. Schwingungsdämpfung @ 30 Hz", "0,84", "0,67", "+0,17", "< 0,05"],
        ["", "", "", "", ""],
        ["Eigenschaft (Flakon)", "K°° pour Femme", "Vergleichsflakon", "Δ", "p-Wert"],
        ["9. Griffrundung-Index (mm Krümmung)", "47,5", "61,2", "-13,7", "< 0,001"],
        ["10. Oberflächenrauheit Ra (μm)", "0,12", "0,34", "-0,22", "< 0,001"],
        ["11. Verschluss-Klick (dB @ 0,3 m)", "62,4", "54,8", "+7,6", "< 0,01"],
        ["12. Stand-Stabilität (Kipp-Winkel °)", "18,7", "14,2", "+4,5", "< 0,05"],
    ]
    t = Table(data, colWidths=[58*mm, 26*mm, 32*mm, 18*mm, 18*mm], repeatRows=1)
    t.setStyle(TableStyle([
        ('FONT', (0,0), (-1,0), "Times-Bold", 8),
        ('FONT', (0,1), (-1,-1), "Times-Roman", 7.5),
        ('FONT', (0,9), (-1,9), "Times-Bold", 7.5),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('BACKGROUND', (0,9), (-1,9), colors.lightgrey),
        ('GRID', (0,0), (-1,-1), 0.25, colors.grey),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ]))
    s.append(t)
    s.append(Spacer(1, 4*mm))
    s.append(Paragraph(
        "<b>FAZIT:</b> Sämtliche zwölf untersuchten Haptik-Dimensionen weisen statistisch "
        "signifikante Unterschiede (p < 0,05) gegenüber marktüblichen Premium-Vergleichs"
        "produkten auf, davon zehn Dimensionen mit p < 0,01. Die Haptik der streit"
        "gegenständlichen Produkte ist somit objektiv reproduzierbar, intersubjektiv "
        "wahrnehmbar und damit grundsätzlich geeignet, die Herkunftsfunktion einer Marke "
        "zu erfüllen. Auf die Rechtsprechung des EuGH zur Haptikmarke "
        "(insb. die Coty-Doktrin C-230/16 in entsprechender Anwendung) wird hingewiesen.",
        S_NORMAL_LEFT))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("Darmstadt, den 14. April 2026", S_RIGHT))
    s.append(Paragraph("Prof. Dr.-Ing. H. Tastenberger<br/>(Sachverständiger TU Darmstadt)", S_RIGHT))
    return s


def blatt_perigord_handnotiz():
    s = []
    s.append(Paragraph("Note manuscrite · Mlle Hortense Périgord (Grasse, mai 2026)", S_H3))
    s.append(Paragraph("(Auf einem zerknitterten Bogen Briefpapier »Maison Périgord — Parfumeure depuis 1934«)", S_TINY))
    s.append(HLine())
    s.append(Spacer(1, 4*mm))
    s.append(Paragraph("Mes chers amis de Munich,", S_HAND))
    s.append(Spacer(1, 2*mm))
    s.append(Paragraph(
        "j'ai senti — oui, senti, avec mon nez, pas avec la machine du Professeur Tastenberger "
        "qui est très allemand, très précis, très <i>quantifiable</i> — les huit échantillons "
        "que vous m'avez envoyés depuis Vilnius. Voici mon verdict, sans détour:",
        S_HAND))
    s.append(Spacer(1, 1*mm))
    s.append(Paragraph(
        "1) Échantillon V-001 (»KK pour Femme — Originale!«): c'est une catastrophe. "
        "Une catastrophe! Quelqu'un a essayé de copier notre Iris pallida avec un "
        "iso-E-super bon marché et a oublié l'âme. Pire — il y a une note résiduelle de "
        "<i>solvant industriel</i> (acétate d'éthyle? hexane?) qui me donne mal à la tête "
        "depuis trois jours.",
        S_HAND))
    s.append(Paragraph(
        "2) Échantillon V-002: même chose, en pire. Au lieu du jasmin sambac indien — du "
        "synthétique chinois bas de gamme. Honte.",
        S_HAND))
    s.append(Paragraph(
        "3) Échantillons V-003 à V-008: variations sur le même thème lamentable. "
        "Je refuse de continuer à les sentir, c'est mauvais pour ma vocation.",
        S_HAND))
    s.append(Spacer(1, 2*mm))
    s.append(Paragraph(
        "Conclusion: ce sont sans doute des contrefaçons grossières, produites avec mépris "
        "du métier. Tribunal? Oui, et vite. Le nez ne ment jamais — il est plus précis "
        "qu'aucune machine.",
        S_HAND))
    s.append(Spacer(1, 2*mm))
    s.append(Paragraph("Embrassez la Comtesse pour moi.", S_HAND))
    s.append(Paragraph("Hortense", S_HAND))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("[Am Rand, andere Handschrift, blauer Kuli:] <i>"
                       "→ als Anlage K-114 zur Berufungsschrift OLG FFM nehmen. "
                       "Übersetzen lassen (Frau Schmidt-Ronchetti, 22.05.2026 / Brenkenhoff)"
                       "</i>", S_HAND2))
    return s


def blatt_ascii_logo_final():
    s = []
    s.append(Paragraph("ANLAGE — Original-Kronen-Logo der Maison klôtzzkètté "
                       "(seit 1923, mit Modernisierung 1987)", S_H3))
    s.append(HLine())
    s.append(ASCIIBox(r"""

                            .  *  .  .  *  .
                          *                 *
                        *    .             .    *
                       .     /\           /\     .
                       *    /  \ /\ /\ /\/  \    *
                        .  /    *  *  *    \   .
                         \/                \/
                          \________________/
                           \              /
                            \    K°°    /
                             \  EST.   /
                              \  1923 /
                               \____/
                                 ||
                       ___________||___________
                      / klôtzzkètté            \
                     /   PARIS · NEW YORK       \
                    /     MILANO · GENÈVE        \
                   /_____________________________\

                   « tradition, élégance, discrétion »
                          ~ depuis 1923 ~
"""))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph(
        "<i>Reproduktion mit freundlicher Genehmigung der Maison klôtzzkètté S.A., Paris. "
        "Sämtliche Rechte vorbehalten. EUTM 017 224 119 (Bildmarke), DE 30 224 117 (Wort-/Bildmarke), "
        "US Reg. 4,887,553, IR 1.488.220.</i>",
        S_FOOT))
    s.append(Spacer(1, 6*mm))
    s.append(Paragraph("— Ende der Akte (vorläufige Bändigung Bd. I) —", S_CENTER))
    s.append(Paragraph("<i>Bändigung in Halbleder, mit Goldprägung »KKK ./. BD« — gefertigt "
                       "durch Buchbinderei Wendelin Lutzhöft, Schwabing, Auftragsnr. 2026-1147</i>",
                       S_TINY))
    return s


story += blatt_sieckmann_duftmarke()
story.append(PageBreak())
story += blatt_tastenberger_haptik()
story.append(PageBreak())
story += blatt_perigord_handnotiz()
story.append(PageBreak())
story += blatt_ascii_logo_final()
story.append(PageBreak())
print("[part40] done")
