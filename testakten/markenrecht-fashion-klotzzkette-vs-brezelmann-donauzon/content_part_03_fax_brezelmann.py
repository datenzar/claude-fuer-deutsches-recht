# Part 03: Fax Brezelmann (frech) + Aktenvermerk Reaktion + interne Mail
def blatt_fax_brezelmann():
    s = []
    s.append(FaxHeader(
        from_no="+49 7931 88 41 12",
        to_no="+49 89 21 03 96-99",
        date="04.02.2026  16:47 Uhr",
        pages="1 von 1",
        subject="IHR SCHREIBEN VOM 22.01.2026 - „KLOETZKETTE“",
        sender="Brezelmann Discount KG / Bad Mergentheim\nz.Hd. Hr. E. Brezelmann (Komplementaer)",
        recipient="Steinacker Lichtenberg & Partners IP\nz.Hd. Fr. RAin Dr. Dr. Steinacker-v. Tarsis"))
    s.append(Spacer(1, 0.4*cm))
    fax_body = (
"SEHR GEEHRTE FRAU DR. DR. STEINACKER,\n"
"\n"
"IHR SCHREIBEN VOM 22.01.2026 LIEGT UNS VOR. HIERMIT ERKLAERT\n"
"DIE BREZELMANN DISCOUNT KG AUSDRUECKLICH WIE FOLGT:\n"
"\n"
"1. EINE MARKENVERLETZUNG WIRD MIT NACHDRUCK BESTRITTEN. UNSERE\n"
"   WARE IST KEINE FAELSCHUNG SONDERN ORIGINALWARE WELCHE WIR UEBER\n"
"   EINEN GRAUMARKT-IMPORTEUR IN TURIN (IT) ERWORBEN HABEN. NAEHERES\n"
"   TEILEN WIR NICHT MIT. DIE BEZUGSRECHNUNGEN LIEGEN ORDNUNGSGEMAESS\n"
"   VOR. ERSCHOEPFUNG IM SINNE VON § 24 MARKENG IST GEGEBEN.\n"
"\n"
"2. UNSERE PREISGESTALTUNG (T-SHIRT EUR 9,99) HAT NICHTS MIT DER\n"
"   FRAGE DER MARKENRECHTLICHEN ZULAESSIGKEIT ZU TUN. IM UEBRIGEN\n"
"   BETRACHTEN WIR DIE PREISE IHRER MANDANTSCHAFT (T-SHIRT EUR 389,-)\n"
"   ALS UNVERSCHAEMT UND VERBRAUCHERFEINDLICH.\n"
"\n"
"3. EINE UNTERLASSUNGSERKLAERUNG WIRD NICHT ABGEGEBEN. FRIST WIRD\n"
"   AUSDRUECKLICH ABGELEHNT. KOSTENERSTATTUNG WIRD ZURUECKGEWIESEN.\n"
"\n"
"4. WIR REGEN AN, DASS IHRE MANDANTIN SICH ANSTELLE EINER\n"
"   RECHTLICHEN AUSEINANDERSETZUNG EINMAL DER FRAGE WIDMET WARUM\n"
"   IHRE PRODUKTE IM EINFACHEN VOLK NICHT MEHR ANKOMMEN.\n"
"\n"
"5. WIR BEHALTEN UNS NEGATIVE FESTSTELLUNGSKLAGE BEIM LG\n"
"   STUTTGART AUSDRUECKLICH VOR.\n"
"\n"
"MIT FREUNDLICHEN GRUESSEN\n"
"\n"
"EGON BREZELMANN\n"
"-- KOMPLEMENTAER -- \n"
"BREZELMANN DISCOUNT KG\n"
"\n"
"PS: HABEN SIE EIGENTLICH UEBERHAUPT JE EIN T-SHIRT FUER UNTER\n"
"    EUR 10,- GEKAUFT? ICH BEZWEIFLE DAS SEHR.\n"
)
    s.append(Preformatted(fax_body, S_FAX))
    s.append(Spacer(1, 0.3*cm))
    s.append(HandNote(
        "WAS FUER EIN FLEGEL.\nComtesse ist beleidigt — bitte sofort eV vorbereiten.\nForumshopping LG Stuttgart prüfen (RA Schmiedhuber).\n— ASt, 04.02.26 abends",
        font=FONT_HAND, size=14, color=colors.HexColor("#aa0e0e"), w=14*cm, angle=-1.4))
    return s

story += blatt_fax_brezelmann()
story.append(PageBreak())

# ------------------ Aktenvermerk Strategie ------------------
def blatt_strategie():
    s = []
    s.append(Paragraph("<b>AKTENVERMERK — STRATEGIE-MEMO</b>", S_CENTER))
    s.append(HLine())
    s.append(Paragraph("Verfasser: ASt &amp; MvB · Datum: 06.02.2026 · STRENG VERTRAULICH", S_RIGHT))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<b>1. Lageeinschätzung</b>", S_H3))
    s.append(Paragraph(
        "Nach Eingang des Fax-Schreibens der Brezelmann Discount KG vom 04.02.2026 (Bl. 6 dieser "
        "Akte, siehe auch Bl. 47 — irrtümlich dort einsortiert) ist von einer kooperativen Beilegung "
        "nicht mehr auszugehen. Der Hinweis auf eine angeblich beabsichtigte negative Feststellungs"
        "klage beim LG Stuttgart ist als <i>forum-shopping</i> zu werten; Gegenmaßnahme: "
        "<b>einstweilige Verfügung beim LG Frankfurt a.M.</b> (Konzentration, schnelle Kammer "
        "für Markensachen — Vors. RaG Hoffacker-Wendel; bekannt für markenrechtsfreundliche "
        "Linie).", S_NORMAL))
    s.append(Paragraph("<b>2. Maßnahmenkatalog (priorisiert)</b>", S_H3))
    measures = [
        ("a)", "Schutzschriftenregister Hessen — Recherche umgehend (heute, 06.02.); "
               "Ergebnis dokumentieren."),
        ("b)", "eV-Antrag an LG Frankfurt vorbereiten — Entwurf bis Mo 09.02.; "
               "Glaubhaftmachung durch eidesstattliche Versicherung der Detektivin "
               "Karla Kalt-Bandel (Spürnase-Couture GmbH); Foto-Dossier 14 Aufn."),
        ("c)", "Verfügungsgrund: Pitti Uomo Florenz (11.-15.03.2026) — Vertrieb auch "
               "auf Messen droht; Eilbedürftigkeit gegeben."),
        ("d)", "Parallel: Widerspruch EUIPO gegen UAB klotzkettie — Frist 14.04.2026; "
               "MvB ausarbeiten."),
        ("e)", "Donauzon Marketplace GmbH — DSA-Notice nach Art. 16 DSA versenden, "
               "Beschwerdefrist 7 Tage abwarten; bei Untätigkeit gesamtschuldnerische "
               "Haftung gem. EuGH C-682/18 (Peterson/YouTube) bzw. C-500/19 "
               "(Puma/CG SE) prüfen."),
        ("f)", "USPTO parallel: koordinieren mit J. Halston Whitman III, Whitman "
               "Brennan Forsythe LLP, NYC — Engagement Letter unterzeichnet."),
        ("g)", "Anti-KI-Authentizitätsmarke „pure human craft“ beim DPMA "
               "(30 2025 218 446) — Sachstand abfragen; bei Eintragung Pressemitteilung "
               "vorbereiten."),
        ("h)", "Haptik-Marken-Anmeldungen DPMA/EUIPO/USPTO vorbereiten (NEU) — "
               "siehe gesondertes Memo Bl. 41 ff."),
    ]
    for label, txt in measures:
        s.append(Paragraph(f"<b>{label}</b> {txt}",
                            ParagraphStyle("m", parent=S_NORMAL, leftIndent=20, firstLineIndent=-20)))
    s.append(Paragraph("<b>3. Streitwert-Schätzung</b>", S_H3))
    s.append(Paragraph(
        "Für die einstweilige Verfügung wird der Streitwert auf <b>EUR 1.200.000,00</b> geschätzt "
        "(8 Marken × EUR 150.000 — Grundsatz: getrennte Schutzrechtsverletzungen, vgl. BGH, "
        "13.10.2022 — I ZR 29/22, GRUR 2023, 90 — <i>Markenstreitwert</i>). Hauptsache: "
        "EUR 4.800.000,00 (entspricht durchschnittlichem Jahresumsatz der Mandantin im DE-Markt × 0,8).",
        S_NORMAL))
    s.append(Paragraph("<b>4. Kommunikation Mandantin</b>", S_H3))
    s.append(Paragraph(
        "Comtesse wird täglich (!) per verschlüsselter E-Mail (PGP-Key 0xC0FFEE42BA5E) und ab "
        "11.03.2026 zusätzlich telefonisch unterrichtet. Wegen ihrer Hochbetagtheit (84 J.) "
        "bitte stets erst nach 10:00 MEZ anrufen, vorher kein Ansprechpartner.", S_NORMAL))
    s.append(Spacer(1, 0.3*cm))
    s.append(HandNote(
        "Frau Hellweg, bitte:\n→ Schutzschrift-Register morgen 8:00 prüfen\n→ Beck-Online-Tagebuch zu Hoffacker-Wendel\n→ Kuchen für Mandantin bei nächstem Besuch (KEIN Marmor!)",
        font=FONT_HAND2, size=13, color=colors.HexColor("#345"), w=14*cm, angle=0.5))
    return s

story += blatt_strategie()
story.append(PageBreak())

print("[part03] done")
