# Part 10: Soundmarke E-Mail-Kette atelier <-> Marketing + Hinterlegungsbestätigung + Logo-Skizzen
def blatt_soundmarke_emails():
    s = []
    s.append(Paragraph("<b>E-Mail-Verkehr betr. Soundmarke EUIPO 018 502 311</b>", S_CENTER))
    s.append(Paragraph("— interner Schriftverkehr atelier@klotzzkette.com / Marketing —", S_RIGHT))
    s.append(HLine())
    s.append(Spacer(1, 0.2*cm))
    body1 = """From:    Étienne Cabriol <e.cabriol@klotzzkette.com>  [Directeur Marketing & Image]
To:      atelier@klotzzkette.com
Cc:      Comtesse Béatrice <comtesse@klotzzkette.com>; legal@klotzzkette.com
Date:    11.05.2024  17:42  CET
Subject: Soundmarke "K°°-Jingle" — Aufnahmesession 14.05.2024

Chers tous,

la session d'enregistrement pour le K°°-Jingle aura lieu le 14.05.2024 à
14h00 au Studio Ferber (Paris XX). Composition finale (8 sec):

  [0:00 - 0:02]  un crack d'un stem de coupe de champagne (réelle, pas synth.)
  [0:02 - 0:04]  trois glaçons s'entrechoquent dans un verre en cristal
  [0:04 - 0:06]  voix féminine doux: "klôtzzkètté"
  [0:06 - 0:08]  réverbération longue (impulse response: Salle Pleyel)

Madame Édith Faleyras-Domnez (mezzo-soprano) prêtera sa voix.
Tous présent? L'enregistrement sera déposé auprès de l'EUIPO le 03.06.2024.

Cordialement,
Étienne Cabriol
Directeur Marketing & Image · klôtzzkètté S.A."""

    body2 = """From:    Comtesse Béatrice <comtesse@klotzzkette.com>
To:      Étienne Cabriol; atelier@klotzzkette.com
Date:    11.05.2024  21:55  CET
Subject: AW: Soundmarke "K°°-Jingle" — Aufnahmesession 14.05.2024

Étienne,

je suis ravie. Mais ATTENTION:
  • La voix doit être plus VELOUTÉE, je veux entendre la SOIE.
  • Le crack du champagne — ABSOLUMENT pas un mousseux! Krug ou Salon!
  • Les glaçons — du cristal Baccarat, pas un autre.
  • La réverbération — pas la Salle Pleyel (trop publique), mais le foyer
    de l'Opéra Garnier (mes ancêtres y ont assisté à la première de Faust).

Je serai présente à l'enregistrement.

Béatrice"""

    body3 = """From:    Étienne Cabriol <e.cabriol@klotzzkette.com>
To:      Comtesse Béatrice
Date:    12.05.2024  09:18  CET
Subject: AW: AW: Soundmarke ...

Madame la Comtesse,

bien noté. J'ai contacté Krug (livraison demain 13.05.) et obtenu une IR
licensing du foyer Opéra Garnier (€18.500 pour usage commercial sound mark).
La voix sera retenue de Mme Faleyras-Domnez (mezzo "veloutée", confirmé par
Studio Ferber).

Quant aux glaçons Baccarat: nous en commandons 24 (au cas où certains
fondraient avant le take final).

Cordialement,
ÉC"""

    body4 = """From:    Dr. Dr. A. Steinacker-von Tarsis <steinacker@steinacker-lichtenberg.de>
To:      Comtesse Béatrice; Étienne Cabriol
Cc:      legal@klotzzkette.com
Date:    03.06.2024  16:32  CET
Subject: Hinterlegung Soundmarke EUIPO — Bestätigung Eingang

Chers tous,

die Hinterlegung der Soundmarke beim EUIPO ist heute 14:30 Uhr CET erfolgt.
EUIPO-Hinterlegungsnummer: 018 502 311.
Anforderungen erfüllt:
  • Audiodatei MP3 (Bitrate 320 kbps, Sample 48 kHz, Stereo, 8.014 sec)
  • Dauer korrekt unter 60 Sek. (Art. 3 Abs. 6 DV)
  • Notenkonforme Beschreibung (8-taktiger Akkord, Pluralton-Notation)
    nach Shield Mark / Kist (C-283/01) — beigefügt als Annex II.
  • Verbale Beschreibung beigefügt (Annex I)

Eintragung wird in 4-7 Monaten erwartet.

Mit verbindlichen Grüßen
Annabella St-vT"""

    body5 = """From:    Comtesse Béatrice
To:      Annabella
Date:    03.06.2024  18:48  CET
Subject: AW: ...

JE SUIS AUX ANGES!!! Le jingle commence par le bruit du champagne, je vais
le faire diffuser dans tous les ateliers à 17h00 chaque jour. C'est notre
ADN sonore. 🥂

PS — Mme Faleyras-Domnez a fait un take où elle a chuchoté "klôtzzkètté"
encore plus doucement. C'est divin. Pouvez-vous demander à l'EUIPO si
on peut déposer une deuxième version chuchotée?"""

    for b in [body1, body2, body3, body4, body5]:
        s.append(Preformatted(b, S_MONO_SMALL))
        s.append(Spacer(1, 0.18*cm))
    return s

story += blatt_soundmarke_emails()
story.append(PageBreak())

# ---- Hinterlegungsbestätigung Soundmarke
def blatt_soundmarke_hinterlegung():
    s = []
    s.append(Paragraph("<b>EUROPEAN UNION INTELLECTUAL PROPERTY OFFICE</b>", S_CENTER))
    s.append(Paragraph("Notification of Receipt and Filing Date", S_CENTER))
    s.append(HLine())
    s.append(Spacer(1, 0.3*cm))
    rows = [
        ["Application No.:", "018 502 311"],
        ["Type:", "Sound Mark (Hörmarke)"],
        ["Format:", "Audio file MP3, 320 kbps, 48 kHz, stereo, 8.014 sec."],
        ["Applicant:", "klôtzzkètté S.A. · 12 rue du Faubourg Saint-Honoré · 75008 Paris (FR)"],
        ["Representative:", "Steinacker Lichtenberg & Partners IP — EUIPO Rep. 88472"],
        ["Filing date:", "03 June 2024"],
        ["Nice classes:", "3, 25, 35, 41"],
        ["Annex I:", "Verbal description (1 page)"],
        ["Annex II:", "Musical notation, pluralton (1 page)"],
        ["Annex III:", "MP3 file (deposited via TMview-XF)"],
        ["Mark description (Annex I):",
         "An 8-second audio composition. Sound element 1 (0.0-2.0 s): the cracking sound "
         "of the snapping stem of a champagne coupe (Baccarat crystal, broken at the rim). "
         "Sound element 2 (2.0-4.0 s): three ice cubes (Baccarat crystal) tinkling in a "
         "crystal glass. Sound element 3 (4.0-6.0 s): a female voice (mezzo-soprano, "
         "velvety quality) softly pronouncing the word „klôtzzkètté“. Sound element 4 "
         "(6.0-8.0 s): a long reverberation tail (impulse response taken in the foyer of "
         "the Palais Garnier opera house, Paris)."],
    ]
    t = Table(rows, colWidths=[4.5*cm, 12.0*cm])
    t.setStyle(TableStyle([
        ("FONT", (0,0), (-1,-1), "Times-Roman", 9.5),
        ("FONTNAME", (0,0), (0,-1), "Times-Bold"),
        ("BOX", (0,0), (-1,-1), 0.3, colors.HexColor("#777777")),
        ("INNERGRID", (0,0), (-1,-1), 0.15, colors.HexColor("#bbbbbb")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
        ("RIGHTPADDING", (0,0), (-1,-1), 5),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.3*cm))
    # Notation block (ASCII-art notation)
    notation = (
"  Annex II — Pluralton Notation                                       \n"
"                                                                       \n"
"   |°°  Crack Glass    Ice Cubes      Voice (mezzo)       Reverb tail  \n"
"   |    [stem snap]    *clink-clink   [klôtz-zkèt-té]    ~~~~~~~~~~~  \n"
"   |    ▌▌            ●  ●  ●          🎵 ♭6 ♮  ♭ ♮ ♯     ░░░░░░░░░  \n"
"   |____|________|________|________|________|________|________|_____  \n"
"        0s       2s       4s       5s       6s       7s       8s      \n"
"                                                                       \n"
"  Tempo: rubato. Dynamics: ppp → pp → p → pp.                          \n"
"  Reverb: Palais Garnier foyer IR, T60 = 2.8 s, mix 28 %.              \n"
"  Mastering: -16 LUFS integrated, -1 dBTP.                             \n"
    )
    s.append(ASCIIBox(notation, font="Courier", size=8, color=colors.HexColor("#220000"),
                      caption="Bestandteil der Anmeldung — Anlage II, Pluralton-Notation der Soundmarke"))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("Alicante, 04.06.2024 — gez. EUIPO Receipt Office", S_NORMAL_LEFT))
    s.append(HandNote(
        "Comtesse hat „chuchoté“-Version separat angemeldet (EU 018 502 312) —\nin Anmeldung, EUIPO hat ZURÜCKgewiesen wg. mangelnder Unterscheidung\nzwischen den beiden Versionen. → Beschwerde BoA noch zu prüfen.",
        font=FONT_HAND, size=13, color=colors.HexColor("#345"), w=15*cm, angle=-0.4))
    return s

story += blatt_soundmarke_hinterlegung()
story.append(PageBreak())

# Logo-Skizzen ASCII-Art K°°-Krönchen
def blatt_logo_skizzen():
    s = []
    s.append(Paragraph("<b>BLATT 47</b> — Skizzen K°°-Krönchen-Monogramm (Bauchskizzen ASt)", S_CENTER))
    s.append(HLine())
    s.append(Paragraph("(querverwiesen aus Bl. 3, Bl. 12, Bl. 21 — siehe auch Anlagen K-VAR-1 bis K-VAR-7)",
                        S_RIGHT))
    s.append(Spacer(1, 0.4*cm))

    skizze1 = (
"        Original K°°-Krönchen (DPMA 30 2014 077 312):                  \n"
"                                                                        \n"
"                    .-^^-.                                              \n"
"                   ( o  o )                                             \n"
"                    `-^^-' <-- 3 Spitzen, silber-emailliert            \n"
"                  K   °   °                                             \n"
"                 ===========                                            \n"
"                                                                        \n"
"        Verwendung: linke Schuh-Innensohle, Pos. 1 cm v. Fersenrand     \n"
"        (Positionsmarke EUIPO 015 887 442)                              \n"
    )
    s.append(ASCIIBox(skizze1, caption="Krönchen-Monogramm — Original (DPMA 30 2014 077 312)"))
    s.append(Spacer(1, 0.4*cm))

    skizze2 = (
"        Verletzungsform Brezelmann K°° (BTM-MEN-022):                  \n"
"                                                                        \n"
"                    .-‾‾-.                                              \n"
"                   ( O  O )    <-- 3 Spitzen, KUNSTSTOFF-aufdruck       \n"
"                    `-^^-'        deutlich dicker, Spitzen abgerundet  \n"
"                  K   °   °                                             \n"
"                 ===========                                            \n"
"                                                                        \n"
"        Verwendung: Brustaufdruck, Sublimationsdruck                    \n"
"        ähnlichkeit nach Verbraucher: 87 % (Verkehrsbefragung)          \n"
    )
    s.append(ASCIIBox(skizze2, caption="Verletzungsform — Brezelmann BTM-MEN-022 (Beschlagn. 12.03.2026)"))
    s.append(Spacer(1, 0.4*cm))

    skizze3 = (
"        Flakon-Kontur (Schnittzeichnung K°° pour Femme 50ml):          \n"
"                                                                        \n"
"               ___                                                      \n"
"              /   \\         <-- asymm. Stopfen (Glasguss, mattiert)     \n"
"             |  ●  |        <-- Krönchen-Relief (Bergkristall)         \n"
"             |     |                                                    \n"
"            /       \\       <-- Hexagonalbauch (60° Kantenwinkel)       \n"
"           |_________|                                                  \n"
"           |  K°°    |       <-- Bodenprägung                           \n"
"           |_________|                                                  \n"
"                                                                        \n"
"        Maße:  H = 137 mm  ·  Ø max = 54 mm  ·  Stopfen 18°-Versatz    \n"
"        3D-Formmarke EU 008 776 015 — Prio. 27.02.2009                  \n"
    )
    s.append(ASCIIBox(skizze3, caption="Flakon K°° pour Femme — Schnittzeichnung (3D-Formmarke)"))
    s.append(Spacer(1, 0.4*cm))
    s.append(HandNote(
        "Notiz vom 17.02.26 — ASt:\nDiese Skizzen GEHÖREN eigentlich zu Bl. 3 (Portfolio), siehe Querverweis.\nIrrtümlich vom Praktikanten als »Bl. 47« einsortiert — bitte nicht\nmehr umsortieren, sonst stimmt der Rest auch nicht mehr.\n→ Stand ist Stand!",
        font=FONT_HAND, size=14, color=colors.HexColor("#7a1f1f"), w=15*cm, angle=-0.8))
    return s

story += blatt_logo_skizzen()
story.append(PageBreak())

print("[part10] done")
