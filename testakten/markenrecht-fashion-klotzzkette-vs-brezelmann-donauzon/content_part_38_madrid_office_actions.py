# -*- coding: utf-8 -*-
# Part 38: Madrid Office Actions multi-country + Strategy Memo + ASCII Map

def blatt_madrid_oa_us():
    s = []
    s.append(Paragraph("UNITED STATES PATENT AND TRADEMARK OFFICE", S_H2))
    s.append(Paragraph("OFFICE ACTION (Examiner's Amendment Required)", S_CENTER))
    s.append(HLine())
    s.append(Paragraph("U.S. Application Serial No. 79/342.118 "
                       "(Madrid IR 1.488.220 — designation United States)", S_NORMAL))
    s.append(Paragraph("Mark: <b>KLÔTZZKÈTTÉ</b> (with diacritics)", S_NORMAL))
    s.append(Paragraph("Applicant: klôtzzkètté S.A. (France)", S_NORMAL))
    s.append(Paragraph("Examining Attorney: <b>Tracy R. Albertson</b>, Law Office 117", S_NORMAL))
    s.append(Paragraph("Issued: April 21, 2026 &nbsp;&nbsp;|&nbsp;&nbsp; Response deadline: October 21, 2026", S_NORMAL))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("<b>SUMMARY OF ISSUES:</b>", S_NORMAL))
    s.append(Paragraph(
        "<b>1. Identification of Goods/Services — Indefinite (37 C.F.R. § 2.32(a)(6); TMEP §§ 1402.01, 1402.03):</b> "
        "The wording in International Classes 14, 18, 25, 26, and 35 is, in part, indefinite and "
        "must be clarified because it does not make clear what the goods/services are and where "
        "they are properly classified. Specifically, in Class 14 the wording &quot;bijouterie de "
        "luxe&quot; is in French and must be translated; in Class 25 the wording &quot;ensembles "
        "de prêt-à-porter haute couture&quot; is partially in French; in Class 35 the wording "
        "&quot;services de boutique de luxe avec service personnalisé en cabines privées&quot; "
        "must be redrafted in standard English from the USPTO ID Manual.",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "<b>2. Translation Statement Required (TMEP § 809.01(b)):</b> Applicant must submit "
        "the English translation of all non-English wording in the mark. The diacritical marks "
        "(ô, è, é) appear over the letters O, E, E respectively. The Examining Attorney requires "
        "a statement of the form: &quot;The wording KLÔTZZKÈTTÉ has no meaning in a foreign "
        "language.&quot; If, however, the wording has a meaning in French or in any other "
        "language, applicant must so state and provide the English translation.",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "<b>3. § 2(d) Refusal — Likelihood of Confusion (15 U.S.C. § 1052(d)):</b> "
        "<i>Withdrawn</i> upon further consideration in view of applicant's letter of protest of "
        "March 14, 2026 (LP-2026-3331), the prior registration U.S. Reg. No. 4,887,221 "
        "(KLOTZ KETTLE COOKWARE) having been amicably amended pursuant to a co-existence "
        "agreement filed concurrently herewith. <i>See</i> the corresponding § 2(d) office action "
        "issued April 02, 2026.",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "<b>4. Specimen of Use (Sections 1 and 71) — Premature:</b> Since this is a § 66(a) "
        "application based on Madrid Protocol, no specimen is presently required. Applicant is "
        "reminded that affidavits or declarations of use under Section 71 will be due between "
        "the 5th and 6th anniversary of the U.S. registration.",
        S_NORMAL_LEFT))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("If applicant has any questions, please contact the assigned examining attorney.", S_NORMAL))
    s.append(Paragraph("/Tracy R. Albertson/<br/>Tracy R. Albertson, Examining Attorney<br/>"
                       "Law Office 117 &nbsp;|&nbsp; (571) 272-4xxx &nbsp;|&nbsp; tracy.albertson@uspto.gov", S_NORMAL))
    return s


def blatt_madrid_oa_china_jp_kr():
    s = []
    s.append(Paragraph("PROVISIONAL REFUSALS — Madrid IR 1.488.220 — Overview Table", S_H2))
    s.append(Paragraph("(Excerpt from monitoring docket maintained by Steinacker LLP, "
                       "internal ref. KK-MAD-MON, updated 18.05.2026)", S_TINY))
    s.append(HLine())
    data = [
        ["Office", "Designation", "Status", "Issue", "Deadline", "Local Counsel"],
        ["CNIPA (CN)", "China", "Provisional refusal (full)",
         "Cl. 14, 25 — similar prior mark 克娄兹凯特 (Reg. 19.887.221)",
         "12.09.2026", "Wang &amp; Yuan IP, Beijing"],
        ["JPO (JP)", "Japan", "Provisional refusal (partial)",
         "Cl. 3 — descriptive in katakana transliteration クロッツケッテ",
         "08.10.2026", "Sonderhoff &amp; Einsel, Tokyo"],
        ["KIPO (KR)", "Korea", "Granted — registration 27.04.2026",
         "—", "—", "Kim &amp; Chang IP, Seoul"],
        ["IP Australia", "Australia", "Granted — 03.05.2026", "—", "—", "Spruson &amp; Ferguson, Sydney"],
        ["INPI (BR)", "Brazil", "Provisional refusal (full)",
         "Cl. 25 — prior mark CLOTHES KETTE Mfg. Ltda (Reg. 928.224.117)",
         "21.10.2026", "Dannemann Siemsen, Rio"],
        ["IMPI (MX)", "Mexico", "Granted — 11.05.2026", "—", "—", "Olivares, CDMX"],
        ["UKIPO (GB)", "United Kingdom", "Granted — 02.04.2026", "—", "—", "Carpmaels &amp; Ransford, London"],
        ["IPOS (SG)", "Singapore", "Provisional refusal (partial)",
         "Cl. 35 — service description too broad", "19.09.2026", "Drew &amp; Napier, Singapore"],
        ["ROSPATENT (RU)", "Russia", "<i>Sanctions hold — no prosecution</i>",
         "Compliance: EU VO 833/2014 Art. 5n", "n/a", "n/a"],
        ["IPI (CH)", "Switzerland", "Granted — 19.04.2026", "—", "—", "Pestalozzi, Zurich"],
        ["UAE-MOE", "UAE", "Pending examination", "—", "≈ 11/2026", "Al Tamimi &amp; Co., Dubai"],
        ["IP India", "India", "Provisional refusal (partial)",
         "Cl. 3 — Cosmetics: descriptive; Cl. 25 OK", "07.11.2026", "Anand &amp; Anand, New Delhi"],
        ["DPMA (DE)", "Germany (basic)", "(Heimatamt — siehe gesondert)", "—", "—", "Steinacker LLP, München"],
        ["EUIPO (EU)", "EU (parallel)", "(siehe Blatt 89 ff. EUIPO B 4 187 932)", "—", "—", "Steinacker LLP"],
        ["INPI (FR)", "France", "Granted — 14.04.2026", "—", "—", "Cabinet Bouchara, Paris"],
        ["DKPTO (DK)", "Denmark", "Granted — 07.05.2026", "—", "—", "Plesner, Copenhagen"],
    ]
    t = Table(data, colWidths=[24*mm, 22*mm, 36*mm, 50*mm, 18*mm, 28*mm], repeatRows=1)
    t.setStyle(TableStyle([
        ('FONT', (0,0), (-1,0), "Times-Bold", 7.5),
        ('FONT', (0,1), (-1,-1), "Times-Roman", 7),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('GRID', (0,0), (-1,-1), 0.25, colors.grey),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 2.5),
        ('RIGHTPADDING', (0,0), (-1,-1), 2.5),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    s.append(t)
    s.append(Spacer(1, 4*mm))
    s.append(Paragraph(
        "<i>Hinweis:</i> Gesamtkostenrahmen für die Erwiderung sämtlicher Office Actions wird "
        "auf EUR 187.500 (zzgl. amtlicher Gebühren ca. EUR 42.800) geschätzt. Vgl. "
        "Mandatsbestätigung WBF-2026-KK-0014.MAD vom 11.05.2026 (Bl. 224 d. A.).",
        S_NORMAL))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("<i>Querverweis:</i> Auf das parallele Brasilien-Risiko hatte Mlle. "
                       "Périgord bereits in ihrer fragmentarischen Randnotiz vom 09.04.2026 "
                       "hingewiesen (»attention au Brésil — la marque CLOTHES KETTE me semble "
                       "drôlement proche, n'est-ce pas?«, vgl. Bl. 67 d. A. — dort jedoch ohne "
                       "Datum). Vermerk Steinacker: <i>venire contra factum proprium nemini "
                       "licet</i> — wir müssen koexistieren oder kaufen.",
                       S_NORMAL))
    return s


def blatt_strategy_memo():
    s = []
    s.append(Paragraph("STEINACKER LICHTENBERG &amp; PARTNERS IP BOUTIQUE", S_H2))
    s.append(Paragraph("INTERNES STRATEGIEMEMO — STRENG VERTRAULICH / NICHT ZUR AKTE", S_H3))
    s.append(Paragraph("(versehentlich abgeheftet — siehe handschriftliche Anmerkung)", S_TINY))
    s.append(HLine())
    s.append(Paragraph("Von: &nbsp;&nbsp;Dr. Dr. A. Steinacker-von Tarsis", S_NORMAL))
    s.append(Paragraph("An: &nbsp;&nbsp;&nbsp;RA M. Freiherr v. Brenkenhoff; Ref. Dr. Mecklenburg-Pries", S_NORMAL))
    s.append(Paragraph("Datum: 19.05.2026, 23:48 Uhr (Maximiliansplatz, Büro)", S_NORMAL))
    s.append(Paragraph("Betreff: klôtzzkètté ./. Brezelmann u.a. — Gesamtstrategie Q3/Q4 2026", S_NORMAL))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph(
        "Liebe Kollegen, ein paar Gedanken zur Nacht — bitte morgen früh besprechen, bevor "
        "die Mandantin um 10:30 telefoniert (Comtesse + Whitman gemeinsam, kombiniertes Update).",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "<b>1. WO STEHEN WIR.</b> Wir haben in den vergangenen sechs Wochen einen ungeheuren "
        "Apparat ausgerollt: LG FFM (einstweilige Verfügung 11.06., Versäumnis-Teilurteil vs. "
        "Brezelmann), Tribunale Firenze (decreto inaudita altera parte), OLG-Berufung 6 W 47/26, "
        "EUIPO BoA R 0 882/2025-5, BPatG-Beschwerden zu allen fünf neuen Markenformen, BGH-"
        "Rechtsbeschwerde I ZB 14/26, SDNY-Complaint (in Bearbeitung), TTAB Opp. 91/289.412, "
        "CBP TMK-26-08812, Madrid IR 1.488.220 mit zur Zeit 6 offenen Office Actions, "
        "Strafanzeige Vilnius + parallel Luxemburg + Strafanzeige in München (folgt). "
        "<i>Lite pendente</i> in mindestens fünf Jurisdiktionen.",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "<b>2. KOSTEN.</b> Aktueller Stand laut Budgetforecast: EUR 2,55 Mio (DE+EU), "
        "USD 1,87 Mio (US). Comtesse hat bei letztem Telefonat (15.05.) signalisiert, dass "
        "EUR 3,5 Mio das absolute Maximum sind, danach Familienrat in Cap d'Antibes. <i>Cave!</i>",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "<b>3. RISIKEN.</b> (a) Donauzon-Vergleichsangebot EUR 1,25 Mio + Sortimentsfilterung — "
        "verlockend, aber wirtschaftlich unzureichend (Schaden p.a. allein DE ca. EUR 4,2 Mio "
        "laut Steinpfeil); (b) BPatG-Zurückweisung Soundmarke wurde durch BGH gekippt — Risiko "
        "in Brasilien (CLOTHES KETTE!) deutlich größer; (c) USPTO TTAB Verfahren kann sich "
        "über 24-36 Monate ziehen, Whitman-Stundensatz USD 1.450 → strategisch begrenzt halten; "
        "(d) Whistleblower Pétard ist <b>unberechenbar</b> — entweder Goldgrube oder Bumerang; "
        "(e) DSGVO-Risiko bei den Spürnase-Testkäufen, wenn Donauzon das aufgreift.",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "<b>4. EMPFEHLUNG.</b> Wir verfolgen weiterhin <i>multi-front pressure</i>, mit klarer "
        "Priorisierung: (1) Brezelmann zermürben bis zum Anerkenntnisurteil (Wahrscheinlichkeit "
        "85 %, wir haben das Versäumnis-Teilurteil), (2) Donauzon-Vergleich auf min. EUR 2,3 Mio "
        "+ Sortimentsfilterung + Auskunftspflicht hochverhandeln, (3) US-Verfahren mit Whitman "
        "als <i>Hebel</i> halten, nicht als Hauptkampf, (4) Vilnius / Luxemburg / München "
        "strafrechtlich konsequent durchziehen — die Verurteilung von Brezelmanas in Litauen "
        "wäre das mediale Highlight.",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "<b>5. EXIT-SZENARIO.</b> Gesamtvergleich EUR 4,5 Mio + Marktfreigabe in 27 Ländern + "
        "öffentliche Entschuldigung Brezelmann auf Donauzon-Startseite + Übernahme der "
        "UAB klotzkettie für symbolischen EUR 1,— + RICO-Vorbehalt für US-Anteil. "
        "Realisierbar ab Q1 2027, schätze ich.",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "Gute Nacht. — A.",
        S_NORMAL))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("[Handschriftlich am Rand, blauer Kuli:] <i>BRENKENHOFF: Wer hat das in "
                       "die Hauptakte abgeheftet?? Das gehört IMMER in die Strategiehängemappe!! "
                       "→ Sekretariat 20.05. Vermerk: Dr. M.-P., Asche aufs Haupt.</i>",
                       S_HAND2))
    return s


def blatt_ascii_map():
    s = []
    s.append(Paragraph("ASCII-VERFAHRENSLANDKARTE (interne Übersichtsskizze)", S_H2))
    s.append(Paragraph("Stand: 19.05.2026 — gez. Ref. Dr. Mecklenburg-Pries (Korrekturen Brenkenhoff)", S_TINY))
    s.append(HLine())
    art = r"""
                                  +------------------------+
                                  |   klôtzzkètté S.A.     |
                                  |   Paris  ·  fr. 1923   |
                                  |   Comtesse B. d. K-V.  |
                                  +-----------+------------+
                                              |
              +-----------------+--------------+---------------+---------------+
              |                 |              |               |               |
        [Steinacker]      [Whitman BFP]   [klôtzzkètté    [Spürnase-       [Pinkerton
         München DE        New York NY     Inc., NY DE]    Couture München]  Jericho NY]
              |                 |              |               |
   ===========+=================+==============+===============+================
   |  ZIVIL & ADMIN.  |  STRAFE  |  ZOLL  |  US-FRONT  |  MADRID/INT'L  |
   ===========+=================+==============+===============+================
              |                 |              |               |
   +----------+----------+      |      +-------+--------+      |
   |                     |      |      |                |      |
[LG FFM 2-03 O 412/26]   |      |      [SDNY 26-CV-xxxx]      |
   ↓                     |      |      [TTAB Opp 91/289.412]  |
[OLG FFM 6 W 47/26]      |      |      [USPTO Madrid 79/342118|
   ↓                     |      |       6 OAs offen]          |
[BGH I ZR ??/26]         |      |      [CBP TMK-26-08812]     |
                         |      |      [LAX 26-LAX-002-887]   |
[EUIPO Opp B 4 187 932]  |      |                             |
   ↓                     |      |     +-----------------------+
[EUIPO BoA R 0 882/25-5] |      |     | DPMA · BPatG · BGH    |
   ↓                     |      |     | 5 neue Markenformen   |
[EuG T-???/26?]          |      |     | (Sound/Scent/Haptik   |
                         |      |     |  Schal/Flakon/Position)|
[Tribunale FI 2026/4471] |      |     +-----------------------+
                         |      |
                  +------+------+------+
                  |             |      |
            [StA Vilnius]  [StA Lux] [StA München]
            ICCS-2026-08827  (folgt)   (folgt)
                  |
            UAB klotzkettie ← Brezelmanas (vermutet = Brezelmann)
            (Vilniaus g. 47)

   Gegner:                            Begleitstörer:
   ========                           ===============
   • Brezelmann Discount KG           • A&K Boulevard Boutique LLC (NYC)
   • Donauzon Marketplace GmbH        • Klotzkettie LLC (Wilmington DE)
   • UAB klotzkettie (Vilnius)        • KK Trading SARL (Luxembourg)

   Whistleblower:  S. Pétard (Lugano CH) — UNGEKLÄRT VERTRAUEN
"""
    s.append(ASCIIBox(art))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("<i>Mutatis mutandis</i>: die Skizze ist nicht maßstabsgetreu, sondern "
                       "soll dem geneigten Leser die Mehrebenenstruktur des Verfahrens "
                       "vergegenwärtigen. Querverweise auf Blatt 22, 47, 89, 134, 178, 199 "
                       "(z. T. nicht in dieser Akte).", S_TINY))
    return s


story += blatt_madrid_oa_us()
story.append(PageBreak())
story += blatt_madrid_oa_china_jp_kr()
story.append(PageBreak())
story += blatt_strategy_memo()
story.append(PageBreak())
story += blatt_ascii_map()
story.append(PageBreak())
print("[part38] done")
