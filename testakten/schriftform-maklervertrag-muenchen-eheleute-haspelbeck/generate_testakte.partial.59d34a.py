#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testakte Maklervertrag München — Eheleute Haspelbeck-Türkenfeld ./. Bechtholdsmeier-Schongau e.K.
Az. LG München I 12 O 8842/23 → OLG München 13 U 412/24 → BGH I ZR 202/25

Generator-Script (ReportLab A4)
Sachverhalt angelehnt an BGH I ZR 202/25 vom 11. März 2026 (Maklervertrag § 656a BGB / Textform)
Alle Personen, Firmen, Adressen rein fiktiv — altfränkisch verschoben, Schauplatz München.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm, mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether, ListFlowable, ListItem
)
from reportlab.platypus.flowables import Flowable
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, Color
import datetime

# ─── Pfade ──────────────────────────────────────────────────────────────────
OUTPUT_DIR = "/home/user/workspace/claude-fuer-deutsches-recht/testakten/schriftform-maklervertrag-muenchen-eheleute-haspelbeck"
OUTPUT_PDF = os.path.join(OUTPUT_DIR, "Testakte_Maklervertrag_Muenchen_Haspelbeck.pdf")

# ─── Farben ──────────────────────────────────────────────────────────────────
DUNKELBLAU  = HexColor("#1B2A4A")
MITTELBLAU  = HexColor("#2C4A7C")
HELLGRAU    = HexColor("#F5F5F5")
RANDGRAU    = HexColor("#CCCCCC")
ROT         = HexColor("#CC0000")
NOTARROT    = HexColor("#AA0000")
GRUEN_WA    = HexColor("#DCF8C6")   # WhatsApp Sender
GRAU_WA     = HexColor("#ECECEC")   # WhatsApp Empfänger
TINTE_BLAU  = HexColor("#1A3C6E")
GOLD        = HexColor("#B8860B")
SIEGEL_ROT  = HexColor("#8B0000")

PAGE_W, PAGE_H = A4

# ─── Styles ──────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def make_style(name, parent='Normal', **kwargs):
    s = ParagraphStyle(name, parent=styles[parent], **kwargs)
    return s

NORMAL      = make_style('AkteNormal',      fontName='Helvetica',       fontSize=10, leading=14, spaceAfter=4,  alignment=TA_JUSTIFY)
NORMAL_L    = make_style('AkteNormalL',     fontName='Helvetica',       fontSize=10, leading=14, spaceAfter=4,  alignment=TA_LEFT)
BOLD        = make_style('AkteBold',        fontName='Helvetica-Bold',  fontSize=10, leading=14, spaceAfter=4,  alignment=TA_LEFT)
TITLE1      = make_style('AkteTitel1',      fontName='Helvetica-Bold',  fontSize=16, leading=20, spaceAfter=8,  alignment=TA_CENTER, textColor=DUNKELBLAU)
TITLE2      = make_style('AkteTitel2',      fontName='Helvetica-Bold',  fontSize=13, leading=17, spaceAfter=6,  alignment=TA_LEFT,   textColor=DUNKELBLAU)
TITLE3      = make_style('AkteTitel3',      fontName='Helvetica-Bold',  fontSize=11, leading=15, spaceAfter=4,  alignment=TA_LEFT)
RUBRUM      = make_style('AkteRubrum',      fontName='Helvetica',       fontSize=10, leading=14, spaceAfter=2,  alignment=TA_CENTER)
RUBRUM_B    = make_style('AkteRubrumB',     fontName='Helvetica-Bold',  fontSize=10, leading=14, spaceAfter=2,  alignment=TA_CENTER)
MONO        = make_style('AkteMono',        fontName='Courier',         fontSize=9,  leading=12, spaceAfter=2,  alignment=TA_LEFT)
MONO_SMALL  = make_style('AkteMonoS',       fontName='Courier',         fontSize=8,  leading=11, spaceAfter=2,  alignment=TA_LEFT)
ITALIC      = make_style('AkteItalic',      fontName='Helvetica-Oblique', fontSize=10, leading=14, spaceAfter=4, leftIndent=1.5*cm, textColor=HexColor("#3D2B1F"))
SMALL       = make_style('AkteSmall',       fontName='Helvetica',       fontSize=8,  leading=11, spaceAfter=2)
SMALL_C     = make_style('AkteSmallC',      fontName='Helvetica',       fontSize=8,  leading=11, spaceAfter=2,  alignment=TA_CENTER)
ROT_STIL    = make_style('AkteRot',         fontName='Helvetica-BoldOblique', fontSize=10, leading=14, spaceAfter=4, textColor=ROT)
FUSSNOTE    = make_style('AkteFuss',        fontName='Helvetica',       fontSize=8,  leading=11, spaceAfter=1, textColor=HexColor("#555555"))
FUSS_BOLD   = make_style('AkteFussB',       fontName='Helvetica-Bold',  fontSize=8,  leading=11, spaceAfter=1)
ZENTRAL     = make_style('AkteZentral',     fontName='Helvetica',       fontSize=10, leading=14, spaceAfter=4, alignment=TA_CENTER)
ZENTRAL_B   = make_style('AkteZentralB',    fontName='Helvetica-Bold',  fontSize=11, leading=15, spaceAfter=4, alignment=TA_CENTER)
INDENT      = make_style('AkteIndent',      fontName='Helvetica',       fontSize=10, leading=14, spaceAfter=4, leftIndent=1.0*cm, rightIndent=1.0*cm, alignment=TA_JUSTIFY)
NOTA_BENE   = make_style('AkteNB',         fontName='Helvetica-Bold',   fontSize=9,  leading=12, spaceAfter=2, textColor=MITTELBLAU)


# ─── Hilfsfunktionen ─────────────────────────────────────────────────────────

def p(text, style=NORMAL):
    return Paragraph(text, style)

def pb():
    return PageBreak()

def sp(h=0.3):
    return Spacer(1, h*cm)

def hr(color=RANDGRAU, thickness=0.5):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=4, spaceBefore=4)

def section_header(text, style=TITLE2):
    return KeepTogether([hr(MITTELBLAU, 1.5), p(text, style), hr(MITTELBLAU, 0.5), sp(0.2)])

def bestandteil_nr(n, titel):
    return KeepTogether([
        sp(0.2),
        p(f"<b>— Bestandteil {n} —</b>", make_style(f'Bst{n}', fontName='Helvetica-Bold', fontSize=9, textColor=HexColor("#888888"), alignment=TA_RIGHT)),
        p(titel, TITLE2),
        hr(MITTELBLAU, 1),
    ])

def notar_stempel():
    """ReportLab Flowable für Notar-Stempel-Simulation"""
    class NotarStempel(Flowable):
        def __init__(self, w=7*cm, h=2.5*cm):
            self.width = w
            self.height = h
        def draw(self):
            c = self.canv
            c.saveState()
            c.setStrokeColor(SIEGEL_ROT)
            c.setFillColor(HexColor("#FFF5F5"))
            c.setLineWidth(2.5)
            c.roundRect(0, 0, self.width, self.height, 8, fill=1, stroke=1)
            c.setFillColor(SIEGEL_ROT)
            c.setFont("Helvetica-Bold", 9)
            c.drawCentredString(self.width/2, self.height - 18, "NOTAR Dr. Ulfried Vorstetter")
            c.setFont("Helvetica", 8)
            c.drawCentredString(self.width/2, self.height - 30, "Maximilianstraße 22 · 80539 München")
            c.drawCentredString(self.width/2, self.height - 42, "UR-Nr. 1488/2023")
            c.setFont("Helvetica-Oblique", 7)
            c.drawCentredString(self.width/2, 8, "Beurkundungsdatum: 12. Mai 2023")
            c.restoreState()
    return NotarStempel()

def kanzlei_logo_ht():
    """ASCII-Logo Hagelbrand & Trotzenburg"""
    return p("""<font name="Courier" size="9"><b>
  ╔══════════════════════════════════╗
  ║  H / T  Rechtsanwälte           ║
  ║  Hagelbrand & Trotzenburg        ║
  ║  Promenadeplatz 9 · 80333 Mchn   ║
  ╚══════════════════════════════════╝</b></font>""", make_style('ASCIIHT', fontName='Courier', fontSize=9, alignment=TA_LEFT, leading=12))

def kanzlei_logo_km():
    """ASCII-Logo Korkenzieher Maibach"""
    return p("""<font name="Courier" size="9"><b>
  ╔══════════════════════════════════╗
  ║  K / M  Rechtsanwälte mbB        ║
  ║  Korkenzieher Maibach Partner    ║
  ║  Karlsplatz 4 · 80335 München    ║
  ╚══════════════════════════════════╝</b></font>""", make_style('ASCIIKM', fontName='Courier', fontSize=9, alignment=TA_LEFT, leading=12))

def email_block(von, an, datum, betreff, body_lines, cc=None):
    """E-Mail-Simulation mit Mono-Header"""
    elems = []
    header = f"""<font name="Courier" size="9"><b>Von:</b>    {von}
<b>An:</b>     {an}"""
    if cc:
        header += f"\n<b>CC:</b>     {cc}"
    header += f"""
<b>Datum:</b>  {datum}
<b>Betreff:</b> {betreff}</font>"""
    elems.append(Table(
        [[Paragraph(header, MONO)]],
        colWidths=[17*cm],
        style=TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), HexColor("#F0F4F8")),
            ('BOX', (0,0), (-1,-1), 0.5, HexColor("#A0B0C0")),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ])
    ))
    elems.append(sp(0.2))
    for line in body_lines:
        elems.append(p(line, MONO_SMALL))
    elems.append(sp(0.3))
    return elems

def wa_bubble(text, sender=True, time_str=""):
    """WhatsApp-Sprechblasen-Simulation"""
    bg = GRUEN_WA if sender else GRAU_WA
    align = TA_RIGHT if sender else TA_LEFT
    indent_l = 3*cm if sender else 0
    indent_r = 0 if sender else 3*cm
    bubble_style = ParagraphStyle('WAbubble', fontName='Helvetica', fontSize=9, leading=13,
                                   alignment=align, leftIndent=indent_l, rightIndent=indent_r,
                                   backColor=bg, borderRadius=10, borderPadding=(6, 10, 6, 10),
                                   spaceAfter=3)
    ts_style = ParagraphStyle('WAts', fontName='Helvetica', fontSize=7, leading=10,
                               textColor=HexColor("#888888"), alignment=align,
                               leftIndent=indent_l, rightIndent=indent_r, spaceAfter=6)
    elems = []
    elems.append(p(text, bubble_style))
    if time_str:
        elems.append(p(time_str, ts_style))
    return elems

def rubrum_table(klaeger, beklagte, az, gericht):
    data = [
        [Paragraph("<b>Kläger:</b>", BOLD), Paragraph(klaeger, NORMAL_L)],
        [Paragraph("", BOLD), Paragraph("", NORMAL_L)],
        [Paragraph("<b>Beklagte:</b>", BOLD), Paragraph(beklagte, NORMAL_L)],
        [Paragraph("", BOLD), Paragraph("", NORMAL_L)],
        [Paragraph("<b>Az.:</b>", BOLD), Paragraph(az, NORMAL_L)],
        [Paragraph("<b>Gericht:</b>", BOLD), Paragraph(gericht, NORMAL_L)],
    ]
    t = Table(data, colWidths=[3.5*cm, 13.5*cm])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    return t


# ─── Seitennummer-Canvas ──────────────────────────────────────────────────────

PAGE_NUMBER = [0]

def on_first_page(canv, doc):
    on_later_pages(canv, doc)

def on_later_pages(canv, doc):
    PAGE_NUMBER[0] = doc.page
    canv.saveState()
    canv.setFont("Helvetica", 7)
    canv.setFillColor(HexColor("#888888"))
    canv.drawString(2*cm, 1.2*cm, "Testakte Haspelbeck-Türkenfeld ./. Bechtholdsmeier-Schongau e.K. — Az. LG München I 12 O 8842/23 — FIKTIVE TESTAKTE")
    canv.drawRightString(PAGE_W - 2*cm, 1.2*cm, f"Seite {doc.page}")
    canv.setStrokeColor(RANDGRAU)
    canv.setLineWidth(0.3)
    canv.line(2*cm, 1.6*cm, PAGE_W - 2*cm, 1.6*cm)
    canv.restoreState()


# ═══════════════════════════════════════════════════════════════════════════════
# INHALT AUFBAU
# ═══════════════════════════════════════════════════════════════════════════════

def build_story():
    story = []

    # ─────────────────────────────────────────────────────────────────────────
    # 1. AKTENDECKEL
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        sp(1.5),
        p("FIKTIVE TESTAKTE — NUR ZU TRAININGSZWECKEN", make_style('warn', fontName='Helvetica-Bold', fontSize=8, alignment=TA_CENTER, textColor=HexColor("#BB0000"))),
        sp(0.5),
        p("""<font name="Courier" size="10"><b>
         ████████████████████████████████████████
         █                                      █
         █   M Ü N C H E N E R   S T A D T     █
         █   W A P P E N   ( A S C I I )        █
         █                                      █
         █          .---,                       █
         █         ( @ @ )                      █
         █     ___/  * *  \\___                  █
         █    /   [ MÜNCHEN ]  \\                █
         █    \\_______________/                 █
         █                                      █
         █   Mönch mit Buch — Stadtsiegel 1328  █
         █                                      █
         ████████████████████████████████████████
</b></font>""", make_style('ascii_wappen', fontName='Courier', fontSize=9, alignment=TA_CENTER, leading=13)),
        sp(1.0),
        p("A K T E", make_style('deckeltitel', fontName='Helvetica-Bold', fontSize=28, alignment=TA_CENTER, textColor=DUNKELBLAU, spaceAfter=6)),
        hr(DUNKELBLAU, 3),
        sp(0.3),
        p("Haspelbeck-Türkenfeld", make_style('deckeln', fontName='Helvetica-Bold', fontSize=18, alignment=TA_CENTER, textColor=DUNKELBLAU)),
        p("./.", make_style('deckelvs', fontName='Helvetica', fontSize=14, alignment=TA_CENTER)),
        p("Bechtholdsmeier-Schongau e.K.", make_style('deckelbek', fontName='Helvetica-Bold', fontSize=16, alignment=TA_CENTER, textColor=DUNKELBLAU)),
        sp(0.5),
        hr(DUNKELBLAU, 1),
        sp(0.3),
        p("Rückforderung Maklerprovision", make_style('deckelss', fontName='Helvetica-BoldOblique', fontSize=14, alignment=TA_CENTER, textColor=MITTELBLAU)),
        p("§§ 812 Abs. 1, 656a, 126b BGB", make_style('deckelpar', fontName='Helvetica', fontSize=11, alignment=TA_CENTER)),
        sp(0.5),
        p("<b>Aktenzeichen LG München I 12 O 8842/23</b>", make_style('deckelaz', fontName='Helvetica-Bold', fontSize=12, alignment=TA_CENTER, textColor=DUNKELBLAU)),
        p("OLG München 13 U 412/24", make_style('deckelaz2', fontName='Helvetica', fontSize=11, alignment=TA_CENTER)),
        p("BGH I ZR 202/25", make_style('deckelaz3', fontName='Helvetica-Bold', fontSize=11, alignment=TA_CENTER, textColor=MITTELBLAU)),
        sp(1.0),
        Table([
            [Paragraph("<b>Kläger:</b>", BOLD), Paragraph("Eheleute Korbinian und Walburga Haspelbeck-Türkenfeld, Mauerkircherstraße 47, 81679 München-Bogenhausen", NORMAL_L)],
            [Paragraph("<b>Beklagte:</b>", BOLD), Paragraph("Marlene Bechtholdsmeier-Schongau e.K., Schwere-Reiter-Straße 18, 80637 München (Maklerin)", NORMAL_L)],
            [Paragraph("<b>Streitwert:</b>", BOLD), Paragraph("EUR 8.810,76 nebst Zinsen 5 Prozentpunkte über Basiszinssatz ab 05. September 2023", NORMAL_L)],
            [Paragraph("<b>Angelegt:</b>", BOLD), Paragraph("22. Mai 2026", NORMAL_L)],
        ], colWidths=[3.5*cm, 13.5*cm], style=TableStyle([
            ('VALIGN',(0,0),(-1,-1),'TOP'), ('LEFTPADDING',(0,0),(-1,-1),4),
            ('TOPPADDING',(0,0),(-1,-1),3), ('BOTTOMPADDING',(0,0),(-1,-1),3),
            ('ROWBACKGROUNDS',(0,0),(-1,-1),[HexColor("#F0F4FA"), colors.white]),
            ('BOX',(0,0),(-1,-1),0.5,RANDGRAU),
        ])),
        sp(1.5),
        p("— FIKTIVE TESTAKTE — ALLE NAMEN/ADRESSEN ERFUNDEN — KEIN REALER RECHTSFALL —",
          make_style('disc', fontName='Helvetica-Oblique', fontSize=8, alignment=TA_CENTER, textColor=HexColor("#999999"))),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 2. INHALTSVERZEICHNIS
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(2, "Inhaltsverzeichnis"),
        sp(0.3),
        p("Hinweis: Das Inhaltsverzeichnis weist Querverweise auf Anlagen und Sonderbände auf, die in dieser Fassung der Testakte nicht vollständig abgebildet sind (vgl. Anlage K-MAK-7, K-MAK-13, K-MAK-21 — Sonderband II). Die Seitenangaben entsprechen der internen Aktennummerierung.", SMALL),
        sp(0.3),
    ]
    iv_data = [
        ["Nr.", "Bestandteil", "Az./Datum", "Ak.-Seite"],
        ["1", "Aktendeckel", "22.05.2026", "1"],
        ["2", "Inhaltsverzeichnis", "—", "2"],
        ["3", "Mandatsannahmebogen RA Hagelbrand-Wittlsbach", "Sept. 2023", "3"],
        ["4", "Klageschrift Haspelbeck-Türkenfeld", "14.09.2023", "4–11"],
        ["5", "Klageerwiderung Bechtholdsmeier-Schongau", "24.10.2023", "12–21"],
        ["6", "Replik Kläger", "17.11.2023", "22–27"],
        ["7", "E-Mail-Kette (Anlage K-MAK-1 ff.)", "30.03.–12.08.2023", "28–35"],
        ["8", "Notarieller Kaufvertrag-Auszug UR-Nr. 1488/2023", "12.05.2023", "36–41"],
        ["9", "Quittung Maklerprovision EUR 8.810,76", "15.05.2023", "42"],
        ["10", "Widerrufsbelehrung — Anlagenkonvolut", "Aug. 2022/2023", "43–44"],
        ["11", "Vergleichsprotokoll (gescheitert)", "12.06.2024", "45–46"],
        ["12", "Berufungsschriftsatz OLG München", "04.07.2024", "47–50"],
        ["13", "Berufungsbegründung (ausführlich)", "04.07.2024", "51–62"],
        ["14", "Berufungserwiderung Kläger", "22.08.2024", "63–68"],
        ["15", "Berufungsurteil OLG München 13 U 412/24", "17.02.2025", "69–72"],
        ["16", "Revisionsbegründung BGH I ZR 202/25", "15.05.2025", "73–81"],
        ["17", "Revisionserwiderung Kläger", "04.07.2025", "82–86"],
        ["18", "Stellungnahmen Verhandlungstermin BGH", "11.03.2026", "87–88"],
        ["19", "BGH-Urteil Tenor-Auszug I ZR 202/25", "11.03.2026", "89–91"],
        ["20", "Mandantenmemo Hagelbrand-Wittlsbach", "14.03.2026", "92–94"],
        ["21", "Handschriftliche Randnotizen Korbinian Haspelbeck", "lfd.", "verteilt"],
        ["22", "WhatsApp-Screenshot-Simulation", "12.05.2023", "95"],
        ["23", "Kanzleirechnung Hagelbrand & Trotzenburg (RVG)", "März 2026", "96–97"],
        ["24", "Aktenrand-Memo RAin Korkenzieher-Mariastein (rot)", "März 2026", "98"],
        ["25", "Anlagenverzeichnis K-MAK-1 bis K-MAK-29", "—", "99"],
        ["26", "Stundenaufstellung Hagelbrand & Trotzenburg", "Sept. 2023–März 2026", "100–102"],
        ["", "— Anlage K-MAK-7: nicht abgebildet (vgl. Sonderband II) —", "", "—"],
        ["", "— Anlage K-MAK-13: nicht abgebildet (vgl. Sonderband II) —", "", "—"],
        ["", "— Anlage K-MAK-21: nicht abgebildet (vgl. Sonderband II) —", "", "—"],
    ]
    iv_table = Table(iv_data, colWidths=[1*cm, 9.5*cm, 4*cm, 2.5*cm])
    iv_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DUNKELBLAU),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('LEADING', (0,0), (-1,-1), 12),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
        ('ALIGN', (3,0), (3,-1), 'RIGHT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, HexColor("#F5F8FF")]),
        ('GRID', (0,0), (-1,-1), 0.3, RANDGRAU),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('FONTNAME', (1,27), (1,29), 'Helvetica-Oblique'),
        ('TEXTCOLOR', (1,27), (1,29), HexColor("#888888")),
    ]))
    story.append(iv_table)
    story.append(pb())

    # ─────────────────────────────────────────────────────────────────────────
    # 3. MANDATSANNAHMEBOGEN
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(3, "Mandatsannahmebogen"),
        kanzlei_logo_ht(),
        sp(0.3),
        p("<b>Hagelbrand &amp; Trotzenburg Rechtsanwälte</b>", BOLD),
        p("Promenadeplatz 9 · 80333 München · Tel. 089/212 380 0 · Fax 089/212 380 99", SMALL),
        p("rechtsanwalt@hagelbrand-trotzenburg.de · USt-IdNr. DE 814 222 017", SMALL),
        sp(0.3), hr(), sp(0.2),
        p("<b>MANDATSANNAHMEBOGEN</b>", TITLE2),
        p("Aktenzeichen intern: HT/2023/0842/HWI", SMALL),
        sp(0.3),
    ]
    man_data = [
        ["Mandant(en):", "Korbinian Haspelbeck-Türkenfeld und Walburga Haspelbeck-Türkenfeld, geb. Brunnendorfer"],
        ["Anschrift:", "Mauerkircherstraße 47, 81679 München-Bogenhausen"],
        ["Telefon privat:", "089 / 98 34 12 07"],
        ["E-Mail:", "korbinian.haspelbeck@gmx.de"],
        ["Mandatsbeginn:", "04. September 2023"],
        ["Gegner:", "Marlene Bechtholdsmeier-Schongau e.K., Schwere-Reiter-Str. 18, 80637 München"],
        ["Streitgegenstand:", "Rückforderung Maklerprovision gem. § 812 Abs. 1 BGB i.V.m. § 656a, 126b BGB"],
        ["Streitwert:", "EUR 8.810,76 nebst Zinsen"],
        ["Stundensatz:", "EUR 380,00 netto zzgl. MwSt. (19 %)"],
        ["Kostendeckung:", "Rechtsschutzversicherung ARAG München, Vers.-Nr. 42-8818-K, Deckungszusage vom 12.09.2023"],
        ["Aktenführung:", "RA Dr. Knut Hagelbrand-Wittlsbach (Sachbearbeiter), RAin Margit Trotzenburg (Vertretung)"],
        ["Erstgespräch:", "04.09.2023, 14:00 Uhr, Dauer: 1,5 h (EUR 570,00 netto)"],
        ["Bemerkungen:", "Mandanten berichten von telefonischer Zusicherung der Maklerin, der Verkäufer-Maklervertrag sei 'formgerecht'. E-Mail-Austausch März/April 2023 liegt vor. Hinweis zur Provision in Signaturzeile fraglich bzgl. § 126b BGB. Anlage: K-MAK-1 bis K-MAK-6 im Erstgespräch vorgelegt."],
    ]
    mt = Table(man_data, colWidths=[4*cm, 13*cm])
    mt.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('LEADING', (0,0), (-1,-1), 13),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [HexColor("#F0F4FA"), colors.white]),
        ('GRID', (0,0), (-1,-1), 0.3, RANDGRAU),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(mt)
    story += [
        sp(0.5),
        p("Aufklärung und Vollmacht erteilt am 04.09.2023. Vollmacht liegt in Urschrift zur Akte.", SMALL),
        sp(0.3),
        Table([
            [Paragraph("München, den 04. September 2023", NORMAL_L), Paragraph("__________________________________", NORMAL_L)],
            [Paragraph("", NORMAL_L), Paragraph("RA Dr. Knut Hagelbrand-Wittlsbach", SMALL)],
        ], colWidths=[8.5*cm, 8.5*cm]),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 4. KLAGESCHRIFT (8 Seiten)
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(4, "Klageschrift"),
        kanzlei_logo_ht(),
        sp(0.3),
        p("Hagelbrand &amp; Trotzenburg Rechtsanwälte · Promenadeplatz 9 · 80333 München", SMALL),
        sp(0.3), hr(), sp(0.2),
        p("An das", NORMAL_L),
        p("<b>Landgericht München I</b>", BOLD),
        p("Prielmayerstraße 7", NORMAL_L),
        p("80335 München", NORMAL_L),
        sp(0.5),
        p("München, den 14. September 2023", NORMAL_L),
        sp(0.5),
        p("<b>K L A G E S C H R I F T</b>", make_style('kltkopf', fontName='Helvetica-Bold', fontSize=14, alignment=TA_CENTER, textColor=DUNKELBLAU)),
        sp(0.3),
        rubrum_table(
            "1. Korbinian Haspelbeck-Türkenfeld, Mauerkircherstraße 47, 81679 München\n2. Walburga Haspelbeck-Türkenfeld, geb. Brunnendorfer, gleiche Anschrift\n— gemeinsam und im Folgenden: „die Kläger" —\nAnwalt: RA Dr. Knut Hagelbrand-Wittlsbach, Hagelbrand & Trotzenburg, Promenadeplatz 9, 80333 München",
            "Marlene Bechtholdsmeier-Schongau e.K. (Maklerin)\nSchwere-Reiter-Straße 18, 80637 München\n— im Folgenden: „die Beklagte" —\nzugestellt an: RAin Dr. Adelheid Korkenzieher-Mariastein, Korkenzieher Maibach Partner mbB, Karlsplatz 4, 80335 München",
            "LG München I 12 O 8842/23",
            "Landgericht München I, Zivilkammer 12"
        ),
        sp(0.5),
        p("<b>Streitwert: EUR 8.810,76</b>", BOLD),
        sp(0.3),
        section_header("I. Klageantrag"),
        p("Die Kläger beantragen, die Beklagte zu verurteilen,", NORMAL),
        sp(0.2),
        p("1. an die Kläger <b>EUR 8.810,76</b> (in Worten: achttausendachthundertzehn Euro sechsundsiebzig Cent) nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz (§ 247 BGB) seit dem 05. September 2023 zu zahlen;", INDENT),
        sp(0.2),
        p("2. die Kläger von vorgerichtlichen Rechtsanwaltskosten in Höhe von EUR 729,23 (1,3-fache Geschäftsgebühr Nr. 2300 VV RVG aus Streitwert EUR 8.810,76 nebst Auslagenpauschale und Mehrwertsteuer) freizustellen.", INDENT),
        sp(0.3),
        section_header("II. Sachverhalt"),
        p("Die Kläger, die Eheleute Korbinian und Walburga Haspelbeck-Türkenfeld, sind Eigentümer des Einfamilienhauses Mauerkircherstraße 47, 81679 München-Bogenhausen (im Folgenden: „die streitgegenständliche Immobilie"). Im Frühjahr 2023 beabsichtigten die Kläger, diese Immobilie zu veräußern und gleichzeitig eine neue Wohnung im Münchner Umland zu erwerben.", NORMAL),
        sp(0.2),
        p("Die Beklagte, Frau Marlene Bechtholdsmeier-Schongau, betreibt unter der Bezeichnung „Immobilien-Vermittlung Marlene Bechtholdsmeier-Schongau e.K." ein Maklerbüro mit Geschäftslokal Schwere-Reiter-Straße 18, 80637 München. Die Beklagte war den Klägern bereits aus einem früheren Geschäftskontakt bekannt.", NORMAL),
        sp(0.2),
        p("<b>Käufer-Maklervertrag (unstreitig):</b> Zunächst vermittelte die Beklagte den Klägern als Käufern den Erwerb einer Wohnung in der Rosenheimer Straße 88, 81669 München. Der hierfür geschlossene Käufer-Maklervertrag wurde ausweislich Anlage K-MAK-2 ordnungsgemäß in Textform nach § 656a Abs. 1, § 126b BGB geschlossen. Die hieraus entstandene Maklerprovision in Höhe von EUR 6.180,00 brutto (inkl. 19 % USt.) wurde von den Klägern beglichen; dieser Betrag ist im vorliegenden Rechtsstreit nicht streitgegenständlich.", NORMAL),
        sp(0.2),
        p("<b>Verkäufer-Maklervertrag (streitig):</b> Gleichzeitig sollte die Beklagte auch den Verkauf der streitgegenständlichen Immobilie Mauerkircherstraße 47 übernehmen. Über diesen Verkäufer-Maklervertrag bestand zwischen den Parteien ein E-Mail-Austausch, der sich über den Zeitraum vom 30. März 2023 bis zum 14. April 2023 erstreckte (Anlage K-MAK-3). Der vollständige E-Mail-Austausch ist als Anlage K-MAK-3 beigefügt und auf Seite 28 ff. dieser Akte dokumentiert.", NORMAL),
        sp(0.2),
        p("Mit E-Mail vom 03. April 2023, 09:12 Uhr, übermittelte die Beklagte den Klägern eine E-Mail betreffend den Verhandlungsstand mit den Kaufinteressenten Bartholomäus und Hiltrud Höglmayr-Stockenfels. Unterhalb der Signatur der Beklagten befand sich folgender Hinweis (wörtlich):", NORMAL),
        sp(0.2),
        p("„Wir weisen darauf hin, dass bei Abschluss eines Kaufvertrages bei einem Einfamilienhaus eine vom Veräußerer und Erwerber zu zahlende Provision fällig wird. Diese beläuft sich maximal auf drei Komma sieben Prozent des Kaufpreises (inklusive gesetzlicher Mehrwertsteuer und je Partei), im Verkaufsfall der von Ihnen veräußerten Liegenschaft Mauerkircherstraße 47."", INDENT),
        sp(0.2),
        p("Die Kläger antworteten am 13. April 2023, 16:33 Uhr, mit der E-Mail: „Wie besprochen — bitte Notartermin vereinbaren." Daraufhin koordinierte die Beklagte mit Notar Dr. Ulfried Vorstetter einen Beurkundungstermin (UR-Nr. 1488/2023), der am 12. Mai 2023 stattfand. Im Kaufvertrag (Anlage K-MAK-5) enthält § 13 eine Maklerklausel.", NORMAL),
        sp(0.2),
        p("Die Beklagte stellte sodann am 15. Mai 2023 eine Rechnung über EUR 8.810,76 (1,2 Prozent inkl. 19 % USt. bezogen auf den Kaufpreis EUR 617.000,00) und buchte diesen Betrag am 30. Mai 2023 vom Treuhandkonto ab. Die Kläger bezahlten — wenn auch unter Vorbehalt des § 814 BGB, den sie nunmehr bestreiten — den genannten Betrag.", NORMAL),
        sp(0.2),
        p("Mit Schreiben vom 03. August 2023 (Anlage K-MAK-6) erklärten die Kläger durch ihren nunmehrigen Prozessbevollmächtigten gegenüber der Beklagten den Widerruf nach §§ 312g Abs. 1, 355 Abs. 1, 312b BGB und forderten zugleich die Rückzahlung des Betrages. Mit Schreiben vom 12. August 2023 wies die Bevollmächtigte der Beklagten, RAin Dr. Korkenzieher-Mariastein, den Widerruf zurück.", NORMAL),
        sp(0.2),
        p("Mangels außergerichtlicher Einigung erheben die Kläger Klage.", NORMAL),
        sp(0.3),
        section_header("III. Rechtliche Begründung"),
        p("Den Klägern steht gegen die Beklagte ein Anspruch auf Rückzahlung der geleisteten Maklerprovision aus § 812 Abs. 1 Satz 1 Alt. 1 BGB (Leistungskondiktion) zu, da ein wirksamer Verkäufer-Maklervertrag im Sinne von § 656a BGB nicht zustande gekommen ist.", NORMAL),
        sp(0.2),
        p("<b>1. Textform-Erfordernis nach § 656a Abs. 1 BGB:</b>", BOLD),
        p("Nach § 656a Abs. 1 BGB, eingefügt durch Art. 1 des Gesetzes über Fernabsatzverträge und andere Fragen des Verbraucherrechts vom 23. Juni 2021 (BGBl. I S. 2123), bedarf ein Maklervertrag, der den Nachweis oder die Vermittlung des Kaufs einer Wohnung oder eines Einfamilienhauses zum Gegenstand hat, der Textform nach § 126b BGB. Diese Formpflicht gilt für Maklerverträge, die — wie im vorliegenden Fall — nach dem 23. Dezember 2020 geschlossen wurden.", NORMAL),
        sp(0.2),
        p("<b>2. Inhaltliche Anforderungen des § 126b BGB:</b>", BOLD),
        p("Textform nach § 126b BGB erfordert eine lesbare Erklärung, in der die Person des Erklärenden genannt und der Abschluss der Erklärung durch Nachbildung der Namensunterschrift oder anderweitig erkennbar gemacht wird. Nach der Rechtsprechung des Bundesgerichtshofs (BGH, Urteil vom 20. April 2023, I ZR 197/22, NJW 2023, 2340 — „Maklervertrag-Textform I") müssen die wesentlichen Vertragsbestandteile — insbesondere der Provisionssatz und das Leistungsobjekt — hinreichend bestimmbar aus dem Textform-Dokument hervorgehen.", NORMAL),
        sp(0.2),
        p("Im vorliegenden Fall ist dies nicht gegeben: Der in der E-Mail-Signatur der Beklagten vom 03. April 2023 enthaltene Provisionshinweis genügt diesen Anforderungen nicht. Zwar nennt er einen Provisionssatz von „maximal drei Komma sieben Prozent"; er benennt aber nicht den tatsächlich vereinbarten Provisionssatz von 1,2 Prozent je Partei für das Einfamilienhaus Mauerkircherstraße 47. Eine Erklärung, die lediglich eine Maximalquote ankündigt, ohne den konkreten Vertragsgegenstand, die konkrete Provision und die gegenseitigen Leistungspflichten zu bestimmen, erfüllt das Textform-Erfordernis des § 656a BGB nicht (vgl. LG Stade, Urteil vom 18. September 2022, 1 O 200/22; LG München I, Hinweisbeschluss vom 14. November 2022, 7 O 14552/22).", NORMAL),
        sp(0.2),
        p("Darüber hinaus ist eine Signaturzeile einer geschäftlichen E-Mail kein eigenständiges, den Abschluss der Erklärung dokumentierendes Dokument im Sinne des § 126b BGB. Es fehlt an der für die Textform erforderlichen Abschlusserkennung, da der Signatur-Block bereits vor Abschluss des eigentlichen E-Mail-Textes platziert war und daher nicht als separate, die Erklärung abschließende Identifikationsmarkierung fungiert.", NORMAL),
        sp(0.2),
        p("<b>3. Fehlen eines wirksamen Maklervertragsschlusses:</b>", BOLD),
        p("Da der Textform genügende Verkäufer-Maklervertrag nicht zustande gekommen ist, fehlt es an einem Rechtsgrund im Sinne des § 812 Abs. 1 Satz 1 Alt. 1 BGB. Die von den Klägern geleistete Provision in Höhe von EUR 8.810,76 ist daher ohne rechtlichen Grund geleistet worden.", NORMAL),
        sp(0.2),
        p("<b>4. Kein Entreicherungseinwand (§ 818 Abs. 3 BGB):</b>", BOLD),
        p("Der Beklagten steht kein Entreicherungseinwand nach § 818 Abs. 3 BGB zu. Nach der gefestigten Rechtsprechung des Bundesgerichtshofs (BGH, Urteil vom 11. Januar 2007, III ZR 116/06, NJW 2007, 1128) ist die Berufung auf Entreicherung dann ausgeschlossen, wenn der Bereicherungsschuldner — wie hier die Beklagte — die gesetzlich vorgeschriebene Form nicht eingehalten hat und der Formvorschrift ein Schutzzweck zukommt, der auch den Bereicherungsausgleich einschließt. § 656a BGB dient dem Schutz der typischerweise wirtschaftlich unterlegenen Verbraucher-Auftraggeber; dieser Schutzzweck würde unterlaufen, wenn die Maklerin sich auf eine Entreicherung berufen könnte.", NORMAL),
        sp(0.2),
        p("<b>5. Hilfsweise: Widerruf nach § 312g BGB:</b>", BOLD),
        p("Hilfsweise stützen die Kläger ihren Anspruch auf den erklärten Widerruf des Verbraucherwiderrufsrechts nach § 312g Abs. 1 BGB. Der Maklervertrag wurde — soweit man ihn überhaupt als wirksam erachten würde — außerhalb von Geschäftsräumen angebahnt; eine ordnungsgemäße Widerrufsbelehrung für den Verkäufer-Maklervertrag wurde nicht erteilt. Die Beklagte hat lediglich für den Käufer-Maklervertrag (August 2022) eine Widerrufsbelehrung übermittelt. Damit läuft die Widerrufsfrist von 14 Tagen (§ 355 Abs. 2 BGB) nicht an, und der Widerruf vom 03. August 2023 ist fristgerecht erfolgt (§ 356 Abs. 3 BGB).", NORMAL),
        sp(0.3),
        section_header("IV. Beweisangebot"),
    ]
    bw_data = [
        ["Beweismittel", "Beweisthema"],
        ["Anlage K-MAK-1", "Käufer-Maklervertrag in Textform (unstreitig)"],
        ["Anlage K-MAK-2", "Widerrufsbelehrung Käufer-MV August 2022"],
        ["Anlage K-MAK-3", "Vollständige E-Mail-Kette März–August 2023"],
        ["Anlage K-MAK-4", "Rechnung Bechtholdsmeier-Schongau vom 15.05.2023"],
        ["Anlage K-MAK-5", "Kaufvertrag-Auszug UR-Nr. 1488/2023 mit § 13 Maklerklausel"],
        ["Anlage K-MAK-6", "Widerrufserklärung RA Hagelbrand-Wittlsbach vom 03.08.2023"],
        ["Zeuge: Notar Dr. Vorstetter", "Zu: Inhalt und Ablauf des Beurkundungstermins 12.05.2023, Inhalt § 13 Kaufvertrag"],
        ["Parteivernehmung Walburga Haspelbeck-Türkenfeld", "Zu: Mündliche Zusicherungen der Beklagten bzgl. Formwirksamkeit"],
        ["Parteivernehmung Korbinian Haspelbeck-Türkenfeld", "Zu: Zustandekommen des Vertrages, Zahlung unter Vorbehalt"],
    ]
    bwt = Table(bw_data, colWidths=[7*cm, 10*cm])
    bwt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DUNKELBLAU), ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'), ('FONTSIZE', (0,0), (-1,-1), 9),
        ('LEADING', (0,0), (-1,-1), 13), ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, HexColor("#F5F8FF")]),
        ('GRID', (0,0), (-1,-1), 0.3, RANDGRAU),
        ('LEFTPADDING', (0,0), (-1,-1), 5), ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(bwt)
    story += [
        sp(0.5),
        p("München, 14. September 2023", NORMAL_L),
        sp(0.3),
        p("RA Dr. Knut Hagelbrand-Wittlsbach", BOLD),
        p("Rechtsanwalt", NORMAL_L),
        p("(Vollmacht liegt in Urschrift bei)", SMALL),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 5. KLAGEERWIDERUNG (10 Seiten)
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(5, "Klageerwiderung"),
        kanzlei_logo_km(),
        sp(0.3),
        p("Korkenzieher Maibach Partner mbB · Karlsplatz 4 · 80335 München · Tel. 089/555 320 0", SMALL),
        sp(0.3), hr(), sp(0.2),
        p("An das", NORMAL_L),
        p("<b>Landgericht München I</b>", BOLD),
        p("Prielmayerstraße 7 · 80335 München", NORMAL_L),
        sp(0.5),
        p("München, den 24. Oktober 2023", NORMAL_L),
        sp(0.3),
        p("<b>KLAGEERWIDERUNG</b>", TITLE2),
        p("In dem Rechtsstreit", NORMAL_L),
        rubrum_table(
            "Korbinian und Walburga Haspelbeck-Türkenfeld (Kläger)",
            "Marlene Bechtholdsmeier-Schongau e.K. (Beklagte)",
            "LG München I 12 O 8842/23",
            "Landgericht München I"
        ),
        sp(0.3),
        p("nimmt die Beklagte zur Klageschrift vom 14. September 2023 wie folgt Stellung:", NORMAL),
        sp(0.3),
        section_header("I. Klageantrag"),
        p("Die Beklagte beantragt,", NORMAL_L),
        p("die Klage <b>abzuweisen</b>.", INDENT),
        sp(0.3),
        section_header("II. Vorbemerkung"),
        p("Die Kläger versuchen, sich ihrer vertraglichen Verpflichtung zur Zahlung der Maklerprovision durch einen formalistischen Angriff auf die Art des Vertragsschlusses zu entziehen. Die Beklagte hat die Kläger ordnungsgemäß beraten, ihnen den Kauf einer neuen Immobilie vermittelt und sodann ihren Wunsch nach Verkauf des Eigenheims Mauerkircherstraße 47 professionell umgesetzt. Der Kaufpreis von EUR 617.000,00 entspricht dem oberen Marktsegment für Bogenhausen und übersteigt die ursprüngliche Wertvorstellung der Kläger um nahezu EUR 40.000,00 — ein Ergebnis, das der Verhandlungsführung der Beklagten zu verdanken ist.", NORMAL),
        sp(0.3),
        section_header("III. Zur behaupteten Textform-Verletzung"),
        p("<b>1. E-Mail-Austausch wahrt die Textform nach § 126b BGB:</b>", BOLD),
        p("Die Kläger verkennen, dass die Textform nach § 126b BGB keine Schriftform (§ 126 BGB) voraussetzt. Eine dauerhaft lesbare Erklärung, die die Person des Erklärenden erkennen lässt und deren Abschluss kenntlich macht, genügt. Diese Voraussetzungen erfüllt die E-Mail-Kommunikation der Parteien.", NORMAL),
        sp(0.2),
        p("Die E-Mail der Beklagten vom 03. April 2023 enthält in der Signatur einen ausdrücklichen Hinweis auf die Provision für den Verkaufsfall der Liegenschaft Mauerkircherstraße 47. Die E-Mail war unterzeichnet mit „Marlene Bechtholdsmeier-Schongau" und trug die Geschäftsbezeichnung sowie sämtliche Kontaktdaten. Die Person der Erklärenden ist damit zweifelsfrei erkennbar. Der Abschluss der Erklärung ist durch die Signatur dokumentiert.", NORMAL),
        sp(0.2),
        p("Mit ihrer Antwort-E-Mail vom 13. April 2023 (16:33 Uhr) haben die Kläger — „wie besprochen" — ausdrücklich zugestimmt, dass die Beklagte einen Notartermin vereinbaren soll. In dieser Antwort liegt konkludent die Annahme des Verkäufer-Maklervertrages. Auf den konkreten Provisionssatz kommt es nicht an, da § 656a BGB nach seinem Wortlaut die Textform des Maklervertrages als solchen verlangt, nicht eine bestimmte Detailtiefe der Provisionsvereinbarung (a.A. LG Stade, das insoweit zu überhohen Anforderungen neigt).", NORMAL),
        sp(0.2),
        p("<b>2. Maklerklausel in § 13 des Kaufvertrages (Hilfsargument):</b>", BOLD),
        p("Hilfsweise hat die Beklagte jedenfalls durch die notarielle Maklerklausel in § 13 des Kaufvertrages UR-Nr. 1488/2023 (Anlage B-1) eine nochmalige, in notarieller Form bestätigte Bestätigung der Provisionsvereinbarung erhalten. Der Notar hat die Kläger ausweislich des Protokolls auf die Maklerprovision hingewiesen; die Kläger haben den Kaufvertrag einschließlich § 13 unterzeichnet, ohne Einwände zu erheben.", NORMAL),
        sp(0.2),
        p("<b>3. Hilfsweise: Wertersatz nach §§ 812, 818 Abs. 2 BGB:</b>", BOLD),
        p("Selbst wenn die Kläger einen kondiktionsrechtlichen Anspruch hätten, könnte die Beklagte — bei unterstellter Unwirksamkeit des Maklervertrages — Wertersatz nach § 818 Abs. 2 BGB für die tatsächlich erbrachte Maklerleistung verlangen. Der Verkaufspreis von EUR 617.000,00 wurde maßgeblich durch die Verhandlungsführung der Beklagten mit den Eheleuten Höglmayr-Stockenfels erzielt. Der Wert dieser Leistung entspricht zumindest der üblichen Maklercourtage.", NORMAL),
        sp(0.2),
        p("<b>4. Hilfsweise: Entreicherung (§ 818 Abs. 3 BGB):</b>", BOLD),
        p("Ferner ist zu berücksichtigen, dass die Beklagte den erhaltenen Betrag für Personal-, Büro- und Werbungskosten aufgewendet hat. Sie ist insoweit entreichert. Eine Verschärfung der Haftung nach § 818 Abs. 4 BGB setzt Bösgläubigkeit voraus, die nicht vorliegt.", NORMAL),
        sp(0.2),
        p("<b>5. Kein wirksamer Widerruf:</b>", BOLD),
        p("Der anwaltlich erklärte Widerruf vom 03. August 2023 ist verfristet und zudem rechtsmissbräuchlich. Maklerverträge für Immobilien, die sich auf Einfamilienhäuser beziehen, werden nicht zwingend als Fernabsatzverträge oder Verträge außerhalb von Geschäftsräumen geschlossen. Das erste Gespräch zwischen den Parteien fand in den Räumlichkeiten der Beklagten, Schwere-Reiter-Straße 18, statt; die Kläger haben das Büro der Beklagten aufgesucht. § 312b BGB setzt voraus, dass der Verbraucher bei einem außerhalb von Geschäftsräumen geschlossenen Vertrag tätig wird. Dies ist hier nicht der Fall.", NORMAL),
        sp(0.5),
        section_header("IV. Beweisangebot"),
        p("Zeugin: Kund. Höglmayr-Stockenfels (Hiltrud), zu: Kaufpreisverhandlung und Vermittlungsleistung der Beklagten", NORMAL),
        p("Urkunde: Kaufvertrag UR-Nr. 1488/2023 (Anlage B-1) mit § 13 Maklerklausel", NORMAL),
        p("Parteivernehmung Marlene Bechtholdsmeier-Schongau, zu: Ablauf und Inhalt der Gespräche mit den Klägern", NORMAL),
        sp(0.5),
        p("München, 24. Oktober 2023", NORMAL_L),
        sp(0.3),
        p("RAin Dr. Adelheid Korkenzieher-Mariastein", BOLD),
        p("Rechtsanwältin", NORMAL_L),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 6. REPLIK (6 Seiten)
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(6, "Replik der Kläger"),
        kanzlei_logo_ht(),
        sp(0.3),
        p("An das Landgericht München I · Prielmayerstraße 7 · 80335 München", SMALL),
        sp(0.3), hr(), sp(0.2),
        p("München, den 17. November 2023", NORMAL_L),
        sp(0.3),
        p("<b>R E P L I K</b>", TITLE2),
        rubrum_table(
            "Haspelbeck-Türkenfeld (Kl.)",
            "Bechtholdsmeier-Schongau e.K. (Bekl.)",
            "LG München I 12 O 8842/23",
            "LG München I, Zivilkammer 12"
        ),
        sp(0.3),
        section_header("I. Replik zur Klageerwiderung vom 24. Oktober 2023"),
        p("Die Kläger halten an ihrem Klageantrag vollumfänglich fest und erwidern auf die Klageerwiderung der Beklagten wie folgt:", NORMAL),
        sp(0.3),
        p("<b>1. Zur behaupteten Textform-Wahrung durch E-Mail-Signatur:</b>", BOLD),
        p("Die Beklagte verkennt die Anforderungen des § 126b BGB in Verbindung mit § 656a Abs. 1 BGB grundlegend. Die Textform dient dem Schutz des Verbrauchers; sie setzt voraus, dass der Verbraucher eine in Textform abgefasste Vertragserklärung erhält, die seine wesentlichen Rechte und Pflichten erkennbar macht. Ein Standardbaustein in der E-Mail-Signatur eines Maklers — zumal einer, die routinemäßig in sämtlichen ausgehenden E-Mails erscheint — kann nicht als individuelle, auf den konkreten Maklerauftrag zugeschnittene Vertragserklärung gewertet werden.", NORMAL),
        sp(0.2),
        p("Der Bundesgerichtshof hat in seiner Entscheidung vom 20. April 2023 (I ZR 197/22) ausgeführt, dass die Textform-Erklärung für den Maklervertrag nach § 656a BGB inhaltlich bestimmt genug sein muss, um eine rechtliche Bindungswirkung zu erzeugen. Einer Erklärung, die lediglich einen Maximalwert ankündigt (hier: „maximal drei Komma sieben Prozent"), fehlt die Bestimmtheit, den wesentlichen Provisionsanspruch zu begründen. Dies gilt vorliegend umso mehr, als die Beklagte sodann eine Provision von lediglich 1,2 Prozent abgerechnet hat — also einen erheblich anderen Prozentsatz als in der Signatur angekündigt.", NORMAL),
        sp(0.2),
        p("<b>2. Zur notariellen Maklerklausel:</b>", BOLD),
        p("Die Beklagte kann sich nicht auf § 13 des Kaufvertrages berufen. Der Bundesgerichtshof hat in ständiger Rechtsprechung (BGH, Urteil vom 03. Mai 2012, III ZR 62/11, NJW 2012, 2268; BGH, Urteil vom 17. April 2019, I ZR 11/18, NJW-RR 2019, 1136) klargestellt, dass eine notarielle Maklerklausel im Kaufvertrag einen eigenständigen Maklervertrag nur dann wirksam begründen kann, wenn auch der Kaufvertrag selbst in der für den Maklervertrag erforderlichen Form geschlossen wurde und wenn der Maklervertrag nicht schon durch die Leistung selbst präkludiert ist. Im vorliegenden Fall wurde die Maklerprovision bereits vor Beurkundung des Kaufvertrages fällig gestellt; die notarielle Klausel hat allenfalls deklaratorischen Charakter.", NORMAL),
        sp(0.2),
        p("<b>3. Zum Schutzzweck des § 656a BGB:</b>", BOLD),
        p("§ 656a BGB wurde durch das Gesetz über die Verteilung von Maklerkosten bei der Vermittlung von Kaufverträgen über Wohnungen und Einfamilienhäuser (BGBl. 2020 I S. 2425) eingeführt und ist am 23. Dezember 2020 in Kraft getreten. Gesetzgebungszweck war ausdrücklich der Schutz von Erwerbern und Veräußerern vor überrumpelnd abgeschlossenen Maklerverträgen sowie die Schaffung von Transparenz. Der Schutzzweck schließt nach dem Willen des Gesetzgebers den Bereicherungsausgleich ein: Der Formverstoß soll dazu führen, dass die Maklerprovision kondizierbar ist, ohne dass sich die Maklerin auf Entreicherung berufen kann.", NORMAL),
        sp(0.2),
        p("<b>4. Zur Widerrufsproblematik:</b>", BOLD),
        p("Die Beklagte behauptet, das erste Gespräch habe in ihren Geschäftsräumen stattgefunden. Dies bestreiten die Kläger. Das erste Gespräch zum Verkauf der Immobilie Mauerkircherstraße 47 fand nach Angaben der Kläger am 15. März 2023 in der Wohnung der Kläger, Mauerkircherstraße 47, statt. Die Beklagte besichtigte seinerzeit das zu verkaufende Objekt. Es liegt damit ein Vertrag außerhalb von Geschäftsräumen im Sinne des § 312b Abs. 1 Nr. 1 BGB vor.", NORMAL),
        sp(0.5),
        p("München, 17. November 2023", NORMAL_L),
        sp(0.3),
        p("RA Dr. Knut Hagelbrand-Wittlsbach", BOLD),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 7. E-MAIL-KETTE (8 Seiten)
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(7, "E-Mail-Kette (Anlage K-MAK-3) — Volltext"),
        p("Die nachfolgende E-Mail-Kette umfasst den gesamten elektronischen Schriftverkehr zwischen den Parteien im Zusammenhang mit dem Verkäufer-Maklervertrag (30. März bis 12. August 2023). Anlage K-MAK-3, vorgelegt von Klägerseite.", SMALL),
        sp(0.3),
    ]

    # E-Mail 1
    story.append(p("<b>E-Mail 1/8 — 30. März 2023, 14:47 Uhr</b>", NOTA_BENE))
    story += email_block(
        "k.haspelbeck@gmx.de (Korbinian Haspelbeck-Türkenfeld)",
        "m.bechtholdsmeier@immo-bms.de (Marlene Bechtholdsmeier-Schongau)",
        "Montag, 30. März 2023, 14:47:22 Uhr (MEZ)",
        "Unsere Immobilie Mauerkircherstr. 47 — Gegenangebot",
        [
            "Sehr geehrte Frau Bechtholdsmeier-Schongau,",
            "",
            "vielen Dank für das telefonische Gespräch von heute Vormittag. Wie",
            "besprochen möchten wir Ihnen als Verhandlungsausgangspunkt mitteilen,",
            "dass wir die Immobilie Mauerkircherstraße 47, 81679 München-Bogenhausen,",
            "zu einem Mindestverkaufspreis von EUR 595.000,00 veräußern möchten.",
            "",
            "Bitte nehmen Sie Kontakt mit den Interessenten Höglmayr auf und teilen Sie",
            "uns deren Reaktion zeitnah mit.",
            "",
            "Mit freundlichen Grüßen",
            "Korbinian Haspelbeck-Türkenfeld",
            "",
            "[Handnotiz KH: 'Walburga: hatten wir nicht EUR 600.000 gesagt? -- K.']",
        ]
    )
    story.append(p("<i>Anmerkung: Die Handnotiz am linken Rand ist eine Originalanmerkung von Korbinian Haspelbeck-Türkenfeld auf dem Papierausdruck; vgl. Bestandteil 21.</i>", ITALIC))

    # E-Mail 2
    story.append(p("<b>E-Mail 2/8 — 03. April 2023, 09:12 Uhr — STREITIGE E-MAIL (Provisionshinweis)</b>", make_style('em2h', fontName='Helvetica-Bold', fontSize=10, textColor=ROT)))
    story += email_block(
        "m.bechtholdsmeier@immo-bms.de (Marlene Bechtholdsmeier-Schongau)",
        "k.haspelbeck@gmx.de (Korbinian Haspelbeck-Türkenfeld)",
        "Montag, 3. April 2023, 09:12:08 Uhr (MEZ)",
        "AW: Unsere Immobilie Mauerkircherstr. 47 — Verhandlungsstand Höglmayr",
        [
            "Sehr geehrtes Ehepaar Haspelbeck-Türkenfeld,",
            "",
            "ich habe heute Morgen mit Herrn Bartholomäus Höglmayr-Stockenfels",
            "telefoniert. Die Familie zeigt ernsthaftes Interesse und möchte die",
            "Immobilie nochmals besichtigen (Terminvorschlag: 10. April, 11:00 Uhr).",
            "Ich gehe davon aus, dass wir bei einem Kaufpreis von EUR 617.000,00",
            "eine Einigung erzielen können.",
            "",
            "Bitte geben Sie mir Bescheid, ob Sie mit dem Besichtigungstermin",
            "einverstanden sind.",
            "",
            "Mit freundlichen Grüßen",
            "Marlene Bechtholdsmeier-Schongau",
            "Inhaberin",
            "",
            "-----------------------------------------------------------------------",
            "Immobilien-Vermittlung Marlene Bechtholdsmeier-Schongau e.K.",
            "Schwere-Reiter-Straße 18 | 80637 München",
            "Tel. 089 / 178 230 40 | Fax 089 / 178 230 49",
            "www.immo-bms.de | m.bechtholdsmeier@immo-bms.de",
            "HRA 112 934 — AG München",
            "-----------------------------------------------------------------------",
            "*** HINWEIS ZUR FÄLLIGKEIT DER PROVISION ***",
            "Wir weisen darauf hin, dass bei Abschluss eines Kaufvertrages bei",
            "einem Einfamilienhaus eine vom Veräußerer und Erwerber zu zahlende",
            "Provision fällig wird. Diese beläuft sich maximal auf drei Komma",
            "sieben Prozent des Kaufpreises (inklusive gesetzlicher Mehrwert-",
            "steuer und je Partei), im Verkaufsfall der von Ihnen veräußerten",
            "Liegenschaft Mauerkircherstraße 47.",
            "*** ENDE HINWEIS ***",
            "-----------------------------------------------------------------------",
        ]
    )
    story.append(p("<b>ANMERKUNG RA Dr. Hagelbrand-Wittlsbach (handschriftlich):</b> <i>Signatur-Hinweis erscheint NACH Absenderzeile, VOR E-Mail-Text-Ende. Kein eigenständiges Dokument iSv § 126b BGB — Abschluss der Erklärung nicht erkennbar gemacht! Vgl. BGH I ZR 197/22.</i>", ITALIC))
    story.append(sp(0.3))

    # E-Mail 3
    story.append(p("<b>E-Mail 3/8 — 13. April 2023, 16:33 Uhr — STREITIGE ANNAHME-E-MAIL</b>", make_style('em3h', fontName='Helvetica-Bold', fontSize=10, textColor=ROT)))
    story += email_block(
        "k.haspelbeck@gmx.de (Korbinian Haspelbeck-Türkenfeld)",
        "m.bechtholdsmeier@immo-bms.de (Marlene Bechtholdsmeier-Schongau)",
        "Donnerstag, 13. April 2023, 16:33:41 Uhr (MEZ)",
        "AW: AW: Unsere Immobilie Mauerkircherstr. 47 — Notartermin",
        [
            "Guten Tag,",
            "",
            "wie besprochen — bitte Notartermin vereinbaren. EUR 617.000 ok.",
            "",
            "Korbinian H.-T.",
            "",
            "Gesendet von iPhone",
        ]
    )
    story.append(p("<b>ANMERKUNG RA Dr. Hagelbrand-Wittlsbach:</b> <i>Dies ist die einzige Antwort-E-Mail. Kein Verweis auf Provisionsvereinbarung, kein Bezug auf konkrete Provisionshöhe, keine Bestätigung des Provisionssatzes. Nur allgemeines 'wie besprochen'. Nicht ausreichend iSv § 656a BGB als Annahme in Textform.</i>", ITALIC))

    # E-Mail 4
    story.append(p("<b>E-Mail 4/8 — 14. April 2023 — Terminanfrage an Notar</b>", NOTA_BENE))
    story += email_block(
        "m.bechtholdsmeier@immo-bms.de (Marlene Bechtholdsmeier-Schongau)",
        "notariat@vorstetter-notar.de (Notar Dr. Ulfried Vorstetter)",
        "Freitag, 14. April 2023, 10:05 Uhr (MEZ)",
        "Terminanfrage Beurkundung — EFH Mauerkircherstraße 47, München",
        [
            "Sehr geehrter Herr Dr. Vorstetter,",
            "",
            "ich bitte um einen Beurkundungstermin für folgenden Kaufvertrag:",
            "",
            "  Verkäufer: Eheleute Haspelbeck-Türkenfeld, Mauerkircherstraße 47",
            "  Käufer:    Eheleute Höglmayr-Stockenfels",
            "  Kaufpreis: EUR 617.000,00",
            "  Objekt:    EFH Mauerkircherstraße 47, 81679 München",
            "",
            "Entwurf des Kaufvertrages übermittle ich bis 18. April 2023.",
            "",
            "Mit freundlichen Grüßen",
            "M. Bechtholdsmeier-Schongau",
        ],
        cc="k.haspelbeck@gmx.de (in CC)"
    )

    # E-Mail 5 — Notartermin-Protokoll-Verweis
    story.append(p("<b>E-Mail 5/8 — 12. Mai 2023 — Notartermin (vgl. Bestandteil 8: Kaufvertrag-Auszug)</b>", NOTA_BENE))
    story.append(p("Beurkundungstermin vor Notar Dr. Ulfried Vorstetter, UR-Nr. 1488/2023, 12. Mai 2023, 14:00 Uhr, Notariat Maximilianstraße 22, 80539 München. Einzelheiten: vgl. Anlage K-MAK-5 (Kaufvertrag-Auszug), Bestandteil 8 dieser Akte.", INDENT))
    story.append(sp(0.3))

    # E-Mail 6 — Rechnung
    story.append(p("<b>E-Mail 6/8 — 15. Mai 2023 — Provision Rechnung</b>", NOTA_BENE))
    story += email_block(
        "m.bechtholdsmeier@immo-bms.de (Marlene Bechtholdsmeier-Schongau)",
        "k.haspelbeck@gmx.de (Korbinian Haspelbeck-Türkenfeld)",
        "Montag, 15. Mai 2023, 11:44 Uhr (MEZ)",
        "Rechnung Maklerprovision Verkauf Mauerkircherstraße 47 — Re. Nr. 2023/0514",
        [
            "Sehr geehrte Damen und Herren,",
            "",
            "anbei übermittle ich Ihnen unsere Rechnung für die Vermittlung des",
            "Kaufvertrages über das Einfamilienhaus Mauerkircherstraße 47,",
            "81679 München (Beurkundungsdatum: 12. Mai 2023).",
            "",
            "  Leistung: Maklerprovision Veräußerer-Seite",
            "  Kaufpreis: EUR 617.000,00",
            "  Provision: 1,0084 % netto = EUR 6.225,00 netto",
            "  zzgl. 19 % MwSt.: EUR 1.182,75",
            "  Zwischensumme: EUR 7.407,75",
            "  [Hinweis: Betrag korrigiert auf EUR 8.810,76 — vgl. Korrekturrechnung]",
            "",
            "  Rechnungsbetrag gesamt: EUR 8.810,76 (brutto)",
            "  Zahlungsziel: 14 Tage ab Rechnungsdatum",
            "",
            "Mit freundlichen Grüßen",
            "M. Bechtholdsmeier-Schongau",
            "",
            "[HANDNOTIZ W. Haspelbeck: 'Wieso jetzt 8.810? Hatte ich nicht',",
            "'6.180 erwartet? -- Walburga']",
        ]
    )

    # E-Mail 7 — Widerruf
    story.append(p("<b>E-Mail 7/8 — 03. August 2023 — Anwaltlicher Widerruf</b>", NOTA_BENE))
    story += email_block(
        "kanzlei@hagelbrand-trotzenburg.de (RA Dr. Hagelbrand-Wittlsbach)",
        "m.bechtholdsmeier@immo-bms.de (Marlene Bechtholdsmeier-Schongau)",
        "Donnerstag, 3. August 2023, 09:00 Uhr (MEZ)",
        "WIDERRUF Maklervertrag / Rückforderung Maklerprovision — Aktenzeichen HT/2023/0842/HWI",
        [
            "Sehr geehrte Frau Bechtholdsmeier-Schongau,",
            "",
            "in vorbezeichneter Sache vertreten wir die Eheleute Haspelbeck-Türkenfeld.",
            "Vollmacht fügen wir in Abschrift bei.",
            "",
            "Hiermit erklären wir namens und in Vollmacht unserer Mandanten:",
            "",
            "1. Den WIDERRUF des zwischen den Parteien angeblich begründeten",
            "   Verkäufer-Maklervertrages betreffend die Liegenschaft Mauerkircherstr. 47",
            "   nach §§ 312g Abs. 1, 355 Abs. 1 BGB (Verbraucherwiderrufsrecht).",
            "",
            "2. Ferner FORDERN WIR SIE AUF, die geleistete Maklerprovision in",
            "   Höhe von EUR 8.810,76 bis spätestens 04. September 2023 auf",
            "   folgendes Konto zu überweisen:",
            "   IBAN: DE12 7001 0080 0398 2244 11 (Haspelbeck-Türkenfeld)",
            "",
            "Begründung: Ein wirksamer Verkäufer-Maklervertrag in Textform nach § 656a",
            "BGB iVm § 126b BGB ist nicht zustande gekommen. Die Provisionsklausel in",
            "der E-Mail-Signatur vom 03.04.2023 genügt den gesetzlichen Anforderungen",
            "nicht. Die Zahlung erfolgte ohne Rechtsgrund. § 812 Abs. 1 Satz 1 BGB.",
            "",
            "Mit freundlichen Grüßen",
            "RA Dr. Knut Hagelbrand-Wittlsbach",
        ]
    )

    # E-Mail 8 — Zurückweisung
    story.append(p("<b>E-Mail 8/8 — 12. August 2023 — Zurückweisung Widerruf</b>", NOTA_BENE))
    story += email_block(
        "kanzlei@korkenzieher-maibach.de (RAin Dr. Korkenzieher-Mariastein)",
        "kanzlei@hagelbrand-trotzenburg.de (RA Dr. Hagelbrand-Wittlsbach)",
        "Samstag, 12. August 2023, 10:17 Uhr (MEZ)",
        "AW: WIDERRUF Maklervertrag — Zurückweisung",
        [
            "Sehr geehrter Herr Dr. Hagelbrand-Wittlsbach,",
            "",
            "wir vertreten Frau Bechtholdsmeier-Schongau. Vollmacht anliegend.",
            "",
            "Der erklärte Widerruf ist UNWIRKSAM. Wir weisen ihn zurück.",
            "",
            "1. Ein formwirksamer Maklervertrag liegt vor.",
            "2. Ein Widerrufsrecht nach § 312g BGB besteht nicht (kein Vertragsschluss",
            "   außerhalb von Geschäftsräumen, § 312b BGB nicht einschlägig).",
            "3. Die Provision ist verdient und fällig.",
            "",
            "Wir fordern Sie auf, von weiteren unbegründeten Ansprüchen Abstand zu",
            "nehmen. Andernfalls behalten wir uns vor, Ersatz der anwaltlichen",
            "Abwehrkosten zu verlangen.",
            "",
            "Mit freundlichen Grüßen",
            "RAin Dr. Adelheid Korkenzieher-Mariastein",
            "Korkenzieher Maibach Partner mbB",
        ]
    )
    story.append(pb())

    # ─────────────────────────────────────────────────────────────────────────
    # 8. NOTARIELLER KAUFVERTRAG-AUSZUG
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(8, "Notarieller Kaufvertrag-Auszug UR-Nr. 1488/2023"),
        p("Auszug aus dem notariell beurkundeten Kaufvertrag vom 12. Mai 2023.", SMALL),
        sp(0.2),
    ]
    story.append(notar_stempel())
    story += [
        sp(0.4),
        p("<b>KAUFVERTRAG</b>", TITLE2),
        p("Urkundenrolle Nr. 1488/2023", BOLD),
        sp(0.2),
        p("Verhandelt zu München am 12. Mai 2023 vor dem unterzeichneten Notar <b>Dr. Ulfried Vorstetter</b>, Notariat Maximilianstraße 22, 80539 München.", NORMAL),
        sp(0.3),
        p("<b>Erschienen sind:</b>", BOLD),
        p("1. <b>Korbinian Haspelbeck-Türkenfeld</b>, geb. 14. Februar 1974, wohnhaft Mauerkircherstraße 47, 81679 München, ausgewiesen durch Personalausweis Nr. L3Q8K4F22, ausgestellt 10. März 2019 durch Landeshauptstadt München, Kreisverwaltungsreferat,", NORMAL),
        p("2. <b>Walburga Haspelbeck-Türkenfeld</b>, geb. Brunnendorfer, geb. 29. August 1976, gleiche Anschrift, ausgewiesen durch Personalausweis Nr. T8W3M7P11, ausgestellt 05. Mai 2021 durch Landeshauptstadt München,", NORMAL),
        p("3. <b>Bartholomäus Höglmayr-Stockenfels</b>, geb. 07. November 1969, wohnhaft Grünwalder Straße 112, 81547 München, ausgewiesen durch Personalausweis Nr. M2F9K5R33, ausgestellt 20. Januar 2020 durch Landeshauptstadt München,", NORMAL),
        p("4. <b>Hiltrud Höglmayr-Stockenfels</b>, geb. Steinrieder, geb. 22. März 1972, gleiche Anschrift, ausgewiesen durch Personalausweis Nr. K4N1W8L55, ausgestellt 14. August 2022 durch Landeshauptstadt München.", NORMAL),
        sp(0.3),
        p("Der Notar hat die Erschienenen über die Bedeutung der Beurkundung belehrt. Die Erschienenen haben ihre Identität in der vorstehenden Weise nachgewiesen.", NORMAL),
        sp(0.3),
        p("[...] (Auszug: §§ 1–12 des Kaufvertrages nicht abgedruckt — vgl. Anlage K-MAK-5 vollständig)", ITALIC),
        sp(0.3),
        section_header("§ 13 Maklerklausel (Volltext)"),
        p("Die Erschienenen zu 1. und 2. (Verkäufer) bestätigen, dass die Vermittlung des vorliegenden Kaufvertrages durch die Immobilien-Vermittlung Marlene Bechtholdsmeier-Schongau e.K., Schwere-Reiter-Straße 18, 80637 München (im Folgenden: „Maklerin"), erfolgt ist.", NORMAL),
        sp(0.2),
        p("Die Erschienenen zu 1. und 2. schulden der Maklerin eine Provision in Höhe von <b>1,2 Prozent des beurkundeten Kaufpreises (inkl. 19 % Mehrwertsteuer, d.h. 1,0084 % netto), mithin EUR 8.810,76</b>, fällig mit Abschluss dieses Kaufvertrages.", NORMAL),
        sp(0.2),
        p("Die Erschienenen zu 3. und 4. (Käufer) schulden der Maklerin ebenfalls eine Provision in gleicher Höhe (EUR 8.810,76), fällig mit Abschluss dieses Kaufvertrages.", NORMAL),
        sp(0.2),
        p("Der Notar hat die Erschienenen darauf hingewiesen, dass diese notarielle Klausel keine eigenständige Grundlage für den Maklervertrag schafft, sofern ein wirksamer Maklervertrag nicht bereits anderweitig zustande gekommen ist; er empfiehlt den Erschienenen, etwaige Formfragen vorab mit der Maklerin zu klären.", ITALIC),
        sp(0.2),
        p("<b>Anmerkung des Notars (handschriftlich eingetragen):</b> <i>„Auf § 656a BGB habe ich die Erschienenen zu 1. und 2. ausdrücklich hingewiesen. Formwirksamkeit des vorgelagerten Maklervertrages ist Sache der Vertragsparteien."</i>", ITALIC),
        sp(0.3),
        p("[...] (weitere Klauseln §§ 14–22 nicht abgedruckt)", ITALIC),
        sp(0.3),
        p("Vorgelesen, genehmigt und unterzeichnet:", NORMAL_L),
        sp(0.2),
        Table([
            [Paragraph("Korbinian Haspelbeck-Türkenfeld", SMALL), Paragraph("Walburga Haspelbeck-Türkenfeld", SMALL)],
            [Paragraph("_____________________________", SMALL), Paragraph("_____________________________", SMALL)],
            [Paragraph("Bartholomäus Höglmayr-Stockenfels", SMALL), Paragraph("Hiltrud Höglmayr-Stockenfels", SMALL)],
            [Paragraph("_____________________________", SMALL), Paragraph("_____________________________", SMALL)],
        ], colWidths=[8.5*cm, 8.5*cm]),
        sp(0.3),
        notar_stempel(),
        sp(0.2),
        p("Urkundlich: <b>Dr. Ulfried Vorstetter, Notar</b>", BOLD),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 9. QUITTUNG
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(9, "Quittung — Maklerprovision EUR 8.810,76"),
        sp(0.5),
        Table([[
            Paragraph("""<b>Immobilien-Vermittlung<br/>Marlene Bechtholdsmeier-Schongau e.K.</b><br/>Schwere-Reiter-Straße 18 · 80637 München<br/>Tel. 089/178 230 40 · HRA 112 934 — AG München""", SMALL),
        ]], colWidths=[17*cm], style=TableStyle([
            ('BOX', (0,0), (-1,-1), 1, DUNKELBLAU), ('LEFTPADDING', (0,0), (-1,-1), 10),
            ('TOPPADDING', (0,0), (-1,-1), 8), ('BOTTOMPADDING', (0,0), (-1,-1), 8),
            ('BACKGROUND', (0,0), (-1,-1), HexColor("#F0F4FA")),
        ])),
        sp(0.5),
        p("<b>Q U I T T U N G</b>", make_style('quitttitel', fontName='Helvetica-Bold', fontSize=16, alignment=TA_CENTER, textColor=DUNKELBLAU)),
        p("Quittungs-Nr. Q/2023/0048", ZENTRAL),
        sp(0.3),
        Table([
            ["Empfängerin:", "Marlene Bechtholdsmeier-Schongau e.K."],
            ["Schuldner:", "Korbinian und Walburga Haspelbeck-Türkenfeld, Mauerkircherstraße 47, 81679 München"],
            ["Datum Eingang:", "30. Mai 2023"],
            ["Betrag:", "EUR 8.810,76 (in Worten: achttausendachthundertzehn Euro sechsundsiebzig Cent)"],
            ["Buchungsreferenz:", "Überw. IBAN DE12 7001 0080 0398 2244 11 v. 28.05.2023"],
            ["Verwendungszweck:", "Maklerprovision Verkauf EFH Mauerkircherstraße 47, Re.Nr. 2023/0514"],
            ["Rechtsgrundlage:", "Maklervertrag i.V.m. § 652 BGB / § 656a BGB (Streitgegenstand im vorliegenden Rechtsstreit)"],
        ], colWidths=[3.5*cm, 13.5*cm], style=TableStyle([
            ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'), ('FONTSIZE', (0,0), (-1,-1), 9.5),
            ('LEADING', (0,0), (-1,-1), 14), ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.white, HexColor("#F5F8FF")]),
            ('GRID', (0,0), (-1,-1), 0.3, RANDGRAU),
            ('LEFTPADDING', (0,0), (-1,-1), 5), ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ])),
        sp(0.5),
        p("Der Eingang des vorstehend bezeichneten Betrages wird hiermit quittiert.", NORMAL),
        sp(0.3),
        Table([
            [Paragraph("München, 30. Mai 2023", NORMAL_L), Paragraph("M. Bechtholdsmeier-Schongau", BOLD)],
            [Paragraph("", NORMAL_L), Paragraph("(Unterschrift / Stempel)", SMALL)],
        ], colWidths=[8.5*cm, 8.5*cm]),
        sp(0.3),
        p("<b>STEMPEL:</b>", SMALL),
        Table([[Paragraph("BEZAHLT\n30.05.2023\nBechtholdsmeier-Schongau e.K.", make_style('stempel', fontName='Helvetica-Bold', fontSize=10, alignment=TA_CENTER, textColor=SIEGEL_ROT))]], colWidths=[4*cm], style=TableStyle([
            ('BOX', (0,0), (-1,-1), 2, SIEGEL_ROT), ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ])),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 10. WIDERRUFSBELEHRUNG
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(10, "Widerrufsbelehrung — Hinweis und Anlagenkonvolut"),
        p("Volltext der Mail-Signatur-Widerrufsbelehrung und Anlagennotizen zum Käufer-Maklervertrag. Anlage K-MAK-2.", SMALL),
        sp(0.3),
        p("<b>A. Widerrufsbelehrung Käufer-Maklervertrag (August 2022)</b>", TITLE3),
        p("Folgende Widerrufsbelehrung wurde den Klägern im August 2022 im Zusammenhang mit dem Käufer-Maklervertrag übermittelt (vgl. Anlage K-MAK-2). Die Echtheit und den Zugang der Widerrufsbelehrung für den Käufer-Maklervertrag bestreitet die Beklagte nicht.", NORMAL),
        sp(0.2),
        Table([[Paragraph("""<b>WIDERRUFSBELEHRUNG (Käufer-Maklervertrag)</b>

<b>Widerrufsrecht</b>
Sie haben das Recht, binnen vierzehn Tagen ohne Angabe von Gründen diesen Vertrag zu widerrufen.

<b>Widerrufsfrist</b>
Die Widerrufsfrist beträgt vierzehn Tage ab dem Tag des Vertragsschlusses. Um Ihr Widerrufsrecht auszuüben, müssen Sie uns (Immobilien-Vermittlung Marlene Bechtholdsmeier-Schongau e.K., Schwere-Reiter-Straße 18, 80637 München, Tel. 089/178 230 40, m.bechtholdsmeier@immo-bms.de) mittels einer eindeutigen Erklärung (z.B. ein mit der Post versandter Brief, Telefax oder E-Mail) über Ihren Entschluss, diesen Vertrag zu widerrufen, informieren.

<b>Folgen des Widerrufs</b>
Wenn Sie diesen Vertrag widerrufen, haben wir Ihnen alle Zahlungen, die wir von Ihnen erhalten haben, unverzüglich und spätestens binnen vierzehn Tagen ab dem Tag zurückzuzahlen, an dem die Mitteilung über Ihren Widerruf dieses Vertrages bei uns eingegangen ist.

<b>Muster-Widerrufsformular (Anlage)</b>
(Beizufügen — gesondert übermittelt)

Immobilien-Vermittlung Marlene Bechtholdsmeier-Schongau e.K., München, August 2022""", MONO_SMALL)]],
            colWidths=[17*cm], style=TableStyle([
                ('BOX', (0,0), (-1,-1), 0.5, RANDGRAU), ('BACKGROUND', (0,0), (-1,-1), HexColor("#FFFEF0")),
                ('LEFTPADDING', (0,0), (-1,-1), 10), ('RIGHTPADDING', (0,0), (-1,-1), 10),
                ('TOPPADDING', (0,0), (-1,-1), 8), ('BOTTOMPADDING', (0,0), (-1,-1), 8),
            ])
        ]],),
        sp(0.3),
        p("<b>B. Fehlende Widerrufsbelehrung für Verkäufer-Maklervertrag</b>", TITLE3),
        p("Für den behaupteten Verkäufer-Maklervertrag existiert keine Widerrufsbelehrung. Die Beklagte hat eine solche zu keinem Zeitpunkt übermittelt.", NORMAL),
        sp(0.2),
        p("<i>Handschriftliche Notiz RA Dr. Hagelbrand-Wittlsbach am Aktenrand: „beim Käufer-MV ja, aber Verkäufer-MV?! — Widerrufsfrist läuft nie an, §356 Abs.3 BGB — Trumpf!"</i>", ITALIC),
        sp(0.2),
        p("<i>Randnotiz Korbinian Haspelbeck-Türkenfeld (Tintenschrift): „Walburga: hatte ich nicht GENAU GEFRAGT?! Bechtholdsmeier hatte gesagt es sei alles in Ordnung."</i>", ITALIC),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 11. VERGLEICHSPROTOKOLL
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(11, "Vergleichsverhandlung — Protokoll (gescheitert)"),
        p("Landgericht München I — Zivilkammer 12 — Güte- und Vergleichstermin", BOLD),
        p("Az. LG München I 12 O 8842/23 · Termin: 12. Juni 2024 · Beginn: 10:30 Uhr", NORMAL_L),
        sp(0.3),
        p("<b>Anwesend:</b>", BOLD),
        Table([
            ["Kläger:", "Korbinian und Walburga Haspelbeck-Türkenfeld (persönlich erschienen)"],
            ["Kläger-Anwalt:", "RA Dr. Knut Hagelbrand-Wittlsbach"],
            ["Beklagte:", "Marlene Bechtholdsmeier-Schongau (persönlich erschienen)"],
            ["Beklagte-Anwältin:", "RAin Dr. Adelheid Korkenzieher-Mariastein"],
            ["Vorsitzender:", "RiLG Dr. Wendelin Pruckner-Altötting"],
        ], colWidths=[3.5*cm, 13.5*cm], style=TableStyle([
            ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'), ('FONTSIZE', (0,0), (-1,-1), 9.5),
            ('LEADING', (0,0), (-1,-1), 14), ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('GRID', (0,0), (-1,-1), 0.3, RANDGRAU), ('LEFTPADDING', (0,0), (-1,-1), 5),
            ('ROWBACKGROUNDS', (0,0), (-1,-1), [HexColor("#F0F4FA"), colors.white]),
            ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ])),
        sp(0.3),
        p("<b>Verlauf der Vergleichsverhandlung:</b>", BOLD),
        p("Der Vorsitzende RiLG Dr. Pruckner-Altötting eröffnete den Termin um 10:30 Uhr und wies die Parteien auf die vorläufige Rechtsauffassung der Kammer hin:", NORMAL),
        sp(0.2),
        p("„Die Kammer neigt nach derzeitigem Stand der Rechtsprechung dazu, in der E-Mail-Signatur keine hinreichend bestimmte Textform-Erklärung im Sinne des § 656a Abs. 1 BGB zu erblicken. Der Hinweis auf einen Maximalbetrag ohne konkrete Vereinbarung der Provisionshöhe sowie das Fehlen einer auf den Vertragsgegenstand spezifisch zugeschnittenen Erklärung dürften den Anforderungen des § 126b BGB nicht genügen. Die Kammer weist auf BGH I ZR 197/22 hin."", INDENT),
        sp(0.2),
        p("RAin Dr. Korkenzieher-Mariastein: „Die Beklagte bietet vergleichsweise die Zahlung von <b>EUR 4.405,38</b> (50 Prozent) an, zahlbar binnen vier Wochen. Die Beklagte besteht auf einer Abgeltungsklausel."", NORMAL),
        sp(0.2),
        p("RA Dr. Hagelbrand-Wittlsbach: „Die Kläger lehnen den Vergleich ab. Der Sachverhalt ist rechtlich eindeutig; wir erwarten ein Vollurteil über EUR 8.810,76."", NORMAL),
        sp(0.2),
        p("<i>Randnotiz K. Haspelbeck: „Walburga sagt nein. Ich auch. Sollen zahlen was sie schulden."</i>", ITALIC),
        sp(0.2),
        p("<b>Ergebnis:</b> Vergleichsverhandlung gescheitert. Termin zur mündlichen Verhandlung bestimmt auf 18. September 2024. Protokoll gefertigt durch Urkundsbeamtin der Geschäftsstelle Anni Scheichengruber.", BOLD),
        sp(0.3),
        p("gez. Dr. Pruckner-Altötting, RiLG", NORMAL_L),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 12. BERUFUNGSSCHRIFTSATZ OLG München
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(12, "Berufungsschriftsatz — OLG München 13 U 412/24"),
        kanzlei_logo_km(),
        sp(0.3),
        p("An das", NORMAL_L),
        p("<b>Oberlandesgericht München</b>", BOLD),
        p("Prielmayerstraße 5 · 80335 München", NORMAL_L),
        sp(0.3),
        p("München, den 04. Juli 2024", NORMAL_L),
        sp(0.3),
        p("<b>BERUFUNGSSCHRIFT</b>", TITLE2),
        p("In dem Rechtsstreit", NORMAL_L),
        rubrum_table(
            "Haspelbeck-Türkenfeld (Kl./Ber.Beklagte)",
            "Bechtholdsmeier-Schongau e.K. (Bekl./Ber.Klägerin)",
            "OLG München 13 U 412/24 (LG München I 12 O 8842/23)",
            "Oberlandesgericht München, Senat 13"
        ),
        sp(0.3),
        p("legt die Beklagte gegen das Urteil des LG München I vom 19. Juni 2024 (Az. 12 O 8842/23) <b>Berufung</b> ein.", NORMAL),
        sp(0.3),
        p("<b>Tenor des angefochtenen Urteils (LG München I):</b>", BOLD),
        p("Die Beklagte wird verurteilt, an die Kläger EUR 8.810,76 nebst Zinsen in Höhe von fünf Prozentpunkten über dem Basiszinssatz seit dem 05. September 2023 zu zahlen. Die Beklagte trägt die Kosten des Rechtsstreits. Das Urteil ist vorläufig vollstreckbar gegen Sicherheitsleistung in Höhe von 110 Prozent des jeweils zu vollstreckenden Betrages.", INDENT),
        sp(0.3),
        p("<b>Berufungsantrag:</b>", BOLD),
        p("1. Das Urteil des Landgerichts München I vom 19. Juni 2024 (Az. 12 O 8842/23) wird aufgehoben.", INDENT),
        p("2. Die Klage wird abgewiesen.", INDENT),
        p("3. Die Kläger tragen die Kosten des Rechtsstreits einschließlich der Kosten der Berufung.", INDENT),
        sp(0.3),
        p("München, 04. Juli 2024", NORMAL_L),
        sp(0.2),
        p("RAin Dr. Adelheid Korkenzieher-Mariastein", BOLD),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 13. BERUFUNGSBEGRÜNDUNG (12 Seiten)
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(13, "Berufungsbegründung — OLG München 13 U 412/24"),
        kanzlei_logo_km(),
        sp(0.3),
        p("An das Oberlandesgericht München · Prielmayerstraße 5 · 80335 München", SMALL),
        sp(0.3), hr(), sp(0.2),
        p("München, den 04. September 2024", NORMAL_L),
        sp(0.3),
        p("<b>BERUFUNGSBEGRÜNDUNG</b>", TITLE2),
        rubrum_table(
            "Bechtholdsmeier-Schongau e.K. (Ber.Klägerin)",
            "Haspelbeck-Türkenfeld (Ber.Beklagte)",
            "OLG München 13 U 412/24",
            "OLG München, 13. Zivilsenat"
        ),
        sp(0.3),
        section_header("A. Zusammenfassung des angefochtenen Urteils"),
        p("Das LG München I hat mit Urteil vom 19. Juni 2024 den Klageanspruch in vollem Umfang für begründet gehalten. Das Gericht hat festgestellt, dass kein wirksamer Verkäufer-Maklervertrag in Textform nach § 656a Abs. 1 BGB iVm § 126b BGB zwischen den Parteien zustande gekommen sei, da der Hinweistext in der E-Mail-Signatur vom 03. April 2023 die wesentlichen Vertragsbestandteile — insbesondere die konkrete Provisionshöhe — nicht mit hinreichender Bestimmtheit bezeichne.", NORMAL),
        sp(0.2),
        p("Das LG hat ferner festgestellt, dass auch eine konkludente Bestätigung des Vertrages durch den E-Mail-Wechsel nicht möglich sei, weil § 656a BGB eine konstitutive Formvorschrift enthalte, die durch konkludentes Verhalten nicht ersetzt werden könne.", NORMAL),
        sp(0.2),
        p("Schließlich hat das Gericht die Entreicherungseinrede nach § 818 Abs. 3 BGB nicht gelten lassen, weil der Formzweck des § 656a BGB dem entgegenstehe.", NORMAL),
        sp(0.3),
        section_header("B. Berufungsangriffe"),
        p("<b>I. Fehlerhafte Subsumtion unter § 126b BGB:</b>", BOLD),
        p("Das Landgericht hat die Anforderungen des § 126b BGB überspannt. Die Norm verlangt eine „lesbare Erklärung, in der die Person des Erklärenden genannt ist und die den Abschluss der Erklärung durch Nachbildung der Namensunterschrift oder anderweitig erkennbar macht." Diese Anforderungen sind erfüllt:", NORMAL),
        sp(0.2),
        p("a) Die E-Mail vom 03. April 2023 ist eine dauerhafte, lesbare Erklärung — sie ist in elektronischer Form gespeichert und jederzeit abrufbar.", NORMAL),
        p("b) Die Person der Erklärenden ist zweifelsfrei erkennbar: Name, Funktion, Kontaktdaten der Beklagten sind vollständig angegeben.", NORMAL),
        p("c) Der Abschluss der Erklärung wird durch die Signaturzeile kenntlich gemacht; diese funktioniert erkennbar als Abschluss des E-Mail-Textes.", NORMAL),
        sp(0.2),
        p("Das Landgericht hat zu Unrecht gefordert, dass auch die konkrete Provisionshöhe (nicht nur der Maximalwert) im Textform-Dokument enthalten sein müsse. § 656a BGB verlangt Textform für den Maklervertrag, nicht für eine spezifizierte Provisionsvereinbarung. Die Provisionsvereinbarung ist Nebenpflicht, keine essentiale negotii im Sinne des § 126b BGB.", NORMAL),
        sp(0.3),
        p("<b>II. Keine hinreichende Berücksichtigung der notariellen Bestätigung (§ 13 KV):</b>", BOLD),
        p("Das Landgericht hat die notarielle Maklerklausel in § 13 des Kaufvertrages UR-Nr. 1488/2023 zu Unrecht als lediglich deklaratorisch bewertet. Die Klausel enthält eine vollständige Provisionsvereinbarung mit exakter Bezifferung (EUR 8.810,76) und ist vor einem Notar erklärt worden, der die Vertragsparteien ausdrücklich belehrt hat. Damit sind — spätestens mit Beurkundung — alle Formerfordernisse des § 656a BGB erfüllt.", NORMAL),
        sp(0.2),
        p("Der BGH hat in seiner Entscheidung I ZR 11/18 (NJW-RR 2019, 1136) nicht ausgeschlossen, dass ein notarieller Kaufvertrag die Textform eines zuvor unzureichend geschlossenen Maklervertrages konvalidieren kann, wenn der Notar den Parteien die Reichweite der Verpflichtung erläutert hat.", NORMAL),
        sp(0.3),
        p("<b>III. Entreicherungseinwand zu Unrecht verneint:</b>", BOLD),
        p("Das Landgericht hat die Entreicherungseinrede nach § 818 Abs. 3 BGB mit der pauschalen Begründung zurückgewiesen, der Schutzzweck des § 656a BGB schließe sie aus. Dies ist nicht haltbar. Der BGH hat einen automatischen Ausschluss der Entreicherungseinrede bei Formverstößen nur in bestimmten, eng begrenzten Konstellationen angenommen (insb. bei arglistiger Täuschung oder planmäßiger Formumgehung). Eine solche Konstellation liegt hier nicht vor. Die Beklagte hat in gutem Glauben gehandelt.", NORMAL),
        sp(0.3),
        p("<b>IV. Subsidiär: Hilfsantrag Wertersatz:</b>", BOLD),
        p("Selbst wenn der Kondiktionsanspruch dem Grunde nach bestehen würde, wäre der Anspruch durch einen Gegenanspruch auf Wertersatz nach § 818 Abs. 2 BGB zu neutralisieren. Der Verkauf des Einfamilienhauses Mauerkircherstraße 47 zu EUR 617.000,00 wurde durch die professionelle Verhandlungsführung der Beklagten erreicht. Der Marktpreis für vergleichbare Maklerleistungen in München entspricht 1,2 bis 2,5 Prozent des Kaufpreises; der abgerechnete Betrag ist marktüblich.", NORMAL),
        sp(0.3),
        section_header("C. Beweisangebot im Berufungsverfahren"),
        p("Sachverständigengutachten (Immobilienwirtschaft München): Zu dem für den Verkauf des EFH Mauerkircherstraße 47 marktüblichen Maklerhonorar.", NORMAL),
        p("Zeuge: RAin Dr. Korkenzieher-Mariastein zur Frage: Wurde das erste Gespräch in den Büroräumen der Beklagten geführt? (Zur Widerrufsproblematik § 312b BGB)", NORMAL),
        sp(0.5),
        p("München, 04. September 2024", NORMAL_L),
        sp(0.2),
        p("RAin Dr. Adelheid Korkenzieher-Mariastein", BOLD),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 14. BERUFUNGSERWIDERUNG KLÄGER
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(14, "Berufungserwiderung der Kläger — OLG München 13 U 412/24"),
        kanzlei_logo_ht(),
        sp(0.3),
        p("An das Oberlandesgericht München · Prielmayerstraße 5 · 80335 München", SMALL),
        sp(0.3), hr(), sp(0.2),
        p("München, den 22. Oktober 2024", NORMAL_L),
        sp(0.3),
        p("<b>BERUFUNGSERWIDERUNG</b>", TITLE2),
        rubrum_table(
            "Haspelbeck-Türkenfeld (Ber.Beklagte/Kl.)",
            "Bechtholdsmeier-Schongau e.K. (Ber.Klägerin/Bekl.)",
            "OLG München 13 U 412/24",
            "OLG München, 13. Zivilsenat"
        ),
        sp(0.3),
        p("<b>Die Berufungsbeklagten beantragen:</b>", BOLD),
        p("Die Berufung der Berufungsklägerin wird zurückgewiesen.", INDENT),
        sp(0.3),
        section_header("Zur Berufungsbegründung"),
        p("Das LG München I hat das Recht richtig angewendet. Die Berufungsbegründung enthält keine durchgreifenden Angriffe gegen das angefochtene Urteil.", NORMAL),
        sp(0.2),
        p("<b>Zu I (Subsumtion § 126b BGB):</b> Die Berufungsklägerin verkennt, dass § 656a BGB in Verbindung mit § 126b BGB konstitutiv wirkt. Die Schutzzweckerwägungen des Gesetzgebers schließen eine großzügige Auslegung aus. Die Gesetzesbegründung (BT-Drucks. 19/15827, S. 22) weist ausdrücklich darauf hin, dass die Formvorschrift sicherstellen soll, dass der Verbraucher über die wesentlichen Bedingungen des Maklervertrages — einschließlich der Provision — in einer dauerhaften und nachprüfbaren Weise informiert wird. Eine Signaturzeile, die routinemäßig in allen E-Mails erscheint und lediglich einen Maximalwert angibt, erfüllt diesen Zweck nicht.", NORMAL),
        sp(0.2),
        p("<b>Zu II (Notarielle Bestätigung):</b> Selbst wenn man der Auffassung der Berufungsklägerin folgen wollte, fehlt es an der Möglichkeit einer nachträglichen Konvalidierung des formunwirksamen Maklervertrages. § 656a BGB enthält nach seinem Wortlaut keine Heilungsvorschrift. Analog § 311b Abs. 1 Satz 2 BGB — der für Grundstückskaufverträge eine Heilung durch notarielle Beurkundung vorsieht — gibt es für Maklerverträge keine vergleichbare Regelung.", NORMAL),
        sp(0.2),
        p("<b>Zu III (Entreicherungseinwand):</b> Der BGH hat in NJW 2007, 1128 den Entreicherungseinwand bei Formverstößen abgelehnt, wenn die Formvorschrift Verbraucherschutzcharakter hat. § 656a BGB dient ausdrücklich dem Schutz der Erwerber und Veräußerer; der Bereicherungsausgleich ist Teil dieses Schutzsystems. Andernfalls würde die Sanktionierung des Formverstoßes durch das Kondiktionsrecht ins Leere laufen.", NORMAL),
        sp(0.5),
        p("München, 22. Oktober 2024", NORMAL_L),
        sp(0.2),
        p("RA Dr. Knut Hagelbrand-Wittlsbach", BOLD),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 15. BERUFUNGSURTEIL OLG MÜNCHEN
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(15, "Berufungsurteil OLG München — 13 U 412/24"),
        sp(0.2),
        Table([[Paragraph("OBERLANDESGERICHT MÜNCHEN\n13. Zivilsenat\nPrielmayerstraße 5 · 80335 München\nTelefon: 089 / 5597 - 0", make_style('olggericht', fontName='Helvetica-Bold', fontSize=11, alignment=TA_CENTER, leading=16))]],
            colWidths=[17*cm], style=TableStyle([
                ('BOX', (0,0), (-1,-1), 1.5, DUNKELBLAU), ('BACKGROUND', (0,0), (-1,-1), HexColor("#EEF2FA")),
                ('TOPPADDING', (0,0), (-1,-1), 10), ('BOTTOMPADDING', (0,0), (-1,-1), 10),
            ])),
        sp(0.4),
        p("<b>URTEIL</b>", make_style('urttek', fontName='Helvetica-Bold', fontSize=16, alignment=TA_CENTER, textColor=DUNKELBLAU)),
        p("Im Namen des Volkes", make_style('inv', fontName='Helvetica-Oblique', fontSize=12, alignment=TA_CENTER)),
        sp(0.3),
        rubrum_table(
            "Korbinian und Walburga Haspelbeck-Türkenfeld, Mauerkircherstraße 47, 81679 München (Berufungsbeklagte/Kläger)",
            "Marlene Bechtholdsmeier-Schongau e.K., Schwere-Reiter-Straße 18, 80637 München (Berufungsklägerin/Beklagte)",
            "OLG München 13 U 412/24 (Vorinstanz: LG München I 12 O 8842/23)",
            "Oberlandesgericht München, 13. Zivilsenat"
        ),
        sp(0.3),
        p("<b>Verkündet am: 17. Februar 2025</b>", BOLD),
        p("Vorsitzende Richterin am OLG: Dr. Konstanze Freiherr-Pfisterrath", NORMAL_L),
        p("Richter am OLG: Dr. Irmfried Zulehner-Neumarkt, Dr. Benedikt Holzgartner-Regensburg", NORMAL_L),
        sp(0.3),
        section_header("Tenor"),
        p("1. Die Berufung der Beklagten gegen das Urteil des Landgerichts München I vom 19. Juni 2024 wird <b>zurückgewiesen</b>.", NORMAL),
        p("2. Die Beklagte trägt die Kosten der Berufung.", NORMAL),
        p("3. Das Urteil ist vorläufig vollstreckbar.", NORMAL),
        p("4. <b>Die Revision wird zugelassen.</b>", BOLD),
        sp(0.3),
        section_header("Gründe (Kurzfassung)"),
        p("Das Landgericht hat die Klage zu Recht für begründet erklärt. Die Berufung bleibt ohne Erfolg.", NORMAL),
        sp(0.2),
        p("Das Berufungsgericht teilt die Einschätzung des Landgerichts, dass die E-Mail-Signatur der Beklagten vom 03. April 2023 den Anforderungen des § 656a Abs. 1 BGB iVm § 126b BGB nicht genügt. Es fehlt an der hinreichenden Bestimmtheit der wesentlichen Vertragsbestandteile. Insbesondere ist die Angabe „maximal drei Komma sieben Prozent" bei tatsächlicher Abrechnung von 1,2 Prozent nicht geeignet, einen bestimmbaren Provisionsanspruch zu begründen.", NORMAL),
        sp(0.2),
        p("Die notarielle Maklerklausel in § 13 des Kaufvertrages vermag den Formverstoß nicht zu heilen. Eine Heilungsvorschrift fehlt im Gesetz; eine Analogie zu § 311b Abs. 1 Satz 2 BGB scheidet aus, da die Interessenlage unterschiedlich ist.", NORMAL),
        sp(0.2),
        p("Die Revision wird zugelassen, weil die Frage, welche inhaltlichen Anforderungen an eine Textform-Erklärung im Sinne des § 656a BGB zu stellen sind, von grundsätzlicher Bedeutung ist (§ 543 Abs. 2 Satz 1 Nr. 1 ZPO) und über den Einzelfall hinausgeht.", NORMAL),
        sp(0.5),
        p("gez. Dr. Freiherr-Pfisterrath · Dr. Zulehner-Neumarkt · Dr. Holzgartner-Regensburg", SMALL_C),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 16. REVISIONSBEGRÜNDUNG BGH
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(16, "Revisionsbegründung — BGH I ZR 202/25"),
        kanzlei_logo_km(),
        sp(0.3),
        p("An den", NORMAL_L),
        p("<b>Bundesgerichtshof</b>", BOLD),
        p("Herrenstraße 45a · 76133 Karlsruhe", NORMAL_L),
        sp(0.3),
        p("München, den 15. Mai 2025", NORMAL_L),
        sp(0.3),
        p("<b>REVISIONSBEGRÜNDUNG</b>", TITLE2),
        rubrum_table(
            "Marlene Bechtholdsmeier-Schongau e.K. (Revisionsklägerin/Beklagte)",
            "Korbinian und Walburga Haspelbeck-Türkenfeld (Revisionsbeklagte/Kläger)",
            "BGH I ZR 202/25 (OLG München 13 U 412/24 / LG München I 12 O 8842/23)",
            "Bundesgerichtshof, I. Zivilsenat"
        ),
        sp(0.3),
        section_header("A. Revisionsantrag"),
        p("Die Revisionsklägerin beantragt:", NORMAL_L),
        p("1. Das Urteil des Oberlandesgerichts München vom 17. Februar 2025 (Az. 13 U 412/24) wird aufgehoben.", INDENT),
        p("2. Die Klage wird abgewiesen.", INDENT),
        p("3. Die Revisionsbeklagten tragen die Kosten des Rechtsstreits in allen Instanzen.", INDENT),
        sp(0.3),
        section_header("B. Statthaftigkeit und Zulässigkeit der Revision"),
        p("Die Revision ist zugelassen (OLG München, Urt. vom 17. Februar 2025, 13 U 412/24). Das Berufungsgericht hat die Revision nach § 543 Abs. 2 Satz 1 Nr. 1 ZPO wegen grundsätzlicher Bedeutung der Rechtsfrage zur inhaltlichen Anforderung an Textform-Erklärungen nach § 656a BGB zugelassen.", NORMAL),
        sp(0.3),
        section_header("C. Revisionsgründe"),
        p("<b>I. Verletzung materiellen Rechts (§ 546 ZPO):</b>", BOLD),
        p("Das Berufungsgericht hat § 126b BGB und § 656a BGB in revisionsrechtlich zu beanstandender Weise angewendet.", NORMAL),
        sp(0.2),
        p("1. <b>Anforderungen an Textform nach § 126b BGB:</b> Das Berufungsgericht hat die gesetzlichen Anforderungen an die Textform überspannt. § 126b BGB stellt drei Anforderungen: (a) lesbare Erklärung, (b) Nennung der erklärenden Person, (c) Erkennbarmachung des Abschlusses der Erklärung. Das Berufungsgericht hat eine vierte, im Gesetz nicht vorgesehene Anforderung formuliert: die „hinreichende Bestimmtheit der wesentlichen Vertragsbestandteile" als inhärente Voraussetzung des § 126b BGB. Diese Anforderung ist — wie die Revisionsklägerin zeigen wird — dem Gesetz fremd.", NORMAL),
        sp(0.2),
        p("2. <b>Verhältnis von § 656a BGB zu § 126b BGB:</b> § 656a BGB ordnet die Geltung der Textform für den Maklervertrag an. Er schreibt aber nicht vor, dass alle wesentlichen Vertragsbestandteile im Textform-Dokument enthalten sein müssen. Die Vertragsparteien können die essentialia negotii — insbesondere die Provisionsvereinbarung — in anderen Formen (mündlich, konkludent) treffen; für den Maklervertrag als solchen genügt Textform. Das Berufungsgericht vermengt die Formanforderungen für den Maklervertrag mit inhaltlichen Bestimmtheitserfordernissen für die Provisionsvereinbarung.", NORMAL),
        sp(0.2),
        p("3. <b>BGH I ZR 197/22 nicht einschlägig:</b> Das von den Vorinstanzen herangezogene Urteil I ZR 197/22 betrifft eine andere Sachverhaltsgestaltung (dort: kein objektbezogener Hinweis auf die Provision). Im vorliegenden Fall benennt die E-Mail-Signatur ausdrücklich die streitgegenständliche Liegenschaft Mauerkircherstraße 47. Dies unterscheidet den vorliegenden Fall von dem in I ZR 197/22 entschiedenen.", NORMAL),
        sp(0.2),
        p("4. <b>Notarielle Klausel:</b> Das Berufungsgericht hat die notarielle Maklerklausel fehlerhaft gewürdigt. Die Parteien haben spätestens bei Beurkundung in notarieller Form (die die Textform übersteigt) eine verbindliche Vereinbarung über die Provision getroffen. Eine Heilungsvorschrift bedarf es nicht, wenn von vornherein davon auszugehen ist, dass ein Maklervertrag in höherer Form auch die Textform wahrt.", NORMAL),
        sp(0.3),
        p("<b>II. Verfahrensrüge (§ 547 ZPO):</b>", BOLD),
        p("Das Berufungsgericht hat das Beweisangebot der Revisionsklägerin (Sachverständigengutachten zum Marktwert der Maklerleistung) übergangen. Ein Sachverständigengutachten war zum Beweis des Wertersatzanspruchs nach § 818 Abs. 2 BGB angeboten worden. Die Ablehnung dieses Beweisangebots verletzt § 286 ZPO.", NORMAL),
        sp(0.5),
        p("München, 15. Mai 2025", NORMAL_L),
        sp(0.2),
        p("RAin Dr. Adelheid Korkenzieher-Mariastein", BOLD),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 17. REVISIONSERWIDERUNG
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(17, "Revisionserwiderung — BGH I ZR 202/25"),
        kanzlei_logo_ht(),
        sp(0.3),
        p("An den Bundesgerichtshof · Herrenstraße 45a · 76133 Karlsruhe", SMALL),
        sp(0.3), hr(), sp(0.2),
        p("München, den 04. Juli 2025", NORMAL_L),
        sp(0.3),
        p("<b>REVISIONSERWIDERUNG</b>", TITLE2),
        rubrum_table(
            "Haspelbeck-Türkenfeld (Revisionsbeklagte/Kl.)",
            "Bechtholdsmeier-Schongau e.K. (Revisionsklägerin/Bekl.)",
            "BGH I ZR 202/25",
            "Bundesgerichtshof, I. Zivilsenat"
        ),
        sp(0.3),
        p("<b>Die Revisionsbeklagten beantragen:</b>", BOLD),
        p("Die Revision der Revisionsklägerin wird als unbegründet zurückgewiesen.", INDENT),
        sp(0.3),
        section_header("Zur Revisionsbegründung"),
        p("Die Revision ist unzulässig, soweit die Revisionsklägerin eine Verfahrensrüge erhebt (keine ordnungsgemäße Bezeichnung des Verfahrensfehlers, § 551 Abs. 3 Nr. 2 ZPO). Im Übrigen ist die Revision unbegründet.", NORMAL),
        sp(0.2),
        p("Die Vorinstanzen haben § 656a BGB und § 126b BGB zutreffend angewendet. Der Schutzzweck der Norm, der auf Verbraucherschutz und Transparenz ausgerichtet ist, gebietet eine strenge Auslegung. Die inhaltliche Unbestimmtheit des Provisionshinweises (Maximalbetrag statt konkrete Vereinbarung) schließt eine Textform-Wirkung aus.", NORMAL),
        sp(0.2),
        p("Die Revisionsklägerin verkennt, dass § 656a BGB nicht nur die formale Hülle (Textform), sondern auch den Inhalt der Erklärung betrifft: Eine Erklärung, aus der der Verbraucher nicht erkennen kann, zu welcher konkreten Leistung er sich verpflichtet, erfüllt den Schutzzweck nicht. Der BGH hat in I ZR 197/22 (NJW 2023, 2340) klargestellt, dass die Textform-Erklärung dem Verbraucher eine informierte Entscheidung ermöglichen muss.", NORMAL),
        sp(0.2),
        p("Zum Entreicherungseinwand: Der BGH hat in seiner Entscheidung III ZR 116/06 (NJW 2007, 1128) den Entreicherungseinwand bei Formverstößen mit Verbraucherschutzzweck bereits abgelehnt; an dieser Rechtsprechung ist festzuhalten.", NORMAL),
        sp(0.5),
        p("München, 04. Juli 2025", NORMAL_L),
        sp(0.2),
        p("RA Dr. Knut Hagelbrand-Wittlsbach", BOLD),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 18. STELLUNGNAHMEN BGH-TERMIN
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(18, "Stellungnahmen zum Verhandlungstermin BGH — 11. März 2026"),
        p("<b>Verhandlungstermin: BGH I ZR 202/25 — 11. März 2026, 10:00 Uhr</b>", TITLE3),
        p("Bundesgerichtshof, Herrenstraße 45a, 76133 Karlsruhe, Sitzungssaal 13", NORMAL_L),
        sp(0.3),
        p("<b>Telefonnotiz RA Dr. Hagelbrand-Wittlsbach (12. März 2026, 08:15 Uhr):</b>", BOLD),
        p("„Termin läuft. BGH-Senat I ZR — Vorsitzender: VRiBGH Dr. Klaus-Peter Mandelkern-Ingolstadt, Richter: RiBGH Dorothea Streit-Waldenfels, RiBGH Benedikt Nymphenburg-Rauch. Revisionsklägerin-Anwältin erschienen: RAin Dr. Korkenzieher-Mariastein. Sitzungsvertreter auf Revisionsbeklagten-Seite: ich selbst. Senat hat gleich zu Beginn signalisiert: Revision dürfte keinen Erfolg haben. Insbes. zur Frage der Bestimmtheit der Textform-Erklärung teilt Senat die Auffassung der Vorinstanzen. Beratungspause 30 Minuten. Dann Verkündung Tenor. — Volltext-Urteil kommt in ca. 4 Wochen."", ITALIC),
        sp(0.3),
        p("<b>Kurzmitteilung RAin Dr. Korkenzieher-Mariastein an Mandantin Bechtholdsmeier-Schongau (per E-Mail, 11. März 2026, 14:22 Uhr):</b>", BOLD),
        p("„Sehr geehrte Frau Bechtholdsmeier-Schongau, leider hat der BGH heute die Revision zurückgewiesen. Der Tenor ist gesprochen. Begründung folgt. Ich empfehle, die Zahlung vorzubereiten und die E-Mail-Templates aller Maklerverträge dringend anzupassen. Ich melde mich nach Eingang des vollständigen Urteils. Mit freundlichen Grüßen, Dr. Korkenzieher-Mariastein"", ITALIC),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 19. BGH-URTEIL TENOR-AUSZUG
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(19, "BGH-Urteil Tenor-Auszug — I ZR 202/25 (11. März 2026)"),
        sp(0.2),
        Table([[Paragraph("BUNDESGERICHTSHOF\nI. Zivilsenat\nHerrenstraße 45a · 76133 Karlsruhe", make_style('bghkopf', fontName='Helvetica-Bold', fontSize=12, alignment=TA_CENTER, leading=17))]],
            colWidths=[17*cm], style=TableStyle([
                ('BOX', (0,0), (-1,-1), 2, DUNKELBLAU), ('BACKGROUND', (0,0), (-1,-1), HexColor("#E8EEF8")),
                ('TOPPADDING', (0,0), (-1,-1), 12), ('BOTTOMPADDING', (0,0), (-1,-1), 12),
            ])),
        sp(0.4),
        p("<b>URTEIL</b>", make_style('bghurt', fontName='Helvetica-Bold', fontSize=18, alignment=TA_CENTER, textColor=DUNKELBLAU)),
        p("Im Namen des Volkes", make_style('bghiv', fontName='Helvetica-Oblique', fontSize=13, alignment=TA_CENTER)),
        sp(0.3),
        rubrum_table(
            "Marlene Bechtholdsmeier-Schongau e.K., Schwere-Reiter-Straße 18, 80637 München (Revisionsklägerin)",
            "Korbinian und Walburga Haspelbeck-Türkenfeld, Mauerkircherstraße 47, 81679 München (Revisionsbeklagte)",
            "I ZR 202/25",
            "Bundesgerichtshof, I. Zivilsenat"
        ),
        sp(0.3),
        p("<b>Verkündet am: 11. März 2026</b>", BOLD),
        sp(0.3),
        section_header("Tenor"),
        p("1. Die Revision der Klägerin [Anm.: Revisionsklägerin = Beklagte] gegen das Urteil des Oberlandesgerichts München vom 17. Februar 2025 — 13 U 412/24 — wird <b>zurückgewiesen</b>.", NORMAL),
        p("2. Die Revisionsklägerin hat die Kosten des Revisionsverfahrens zu tragen.", NORMAL),
        sp(0.4),
        section_header("Leitsätze (sinngemäß — Auszug)"),
        p("1. Eine in der Signaturzeile einer allgemeinen Geschäfts-E-Mail enthaltene Provisionshinweisklausel genügt den Anforderungen des § 656a Abs. 1 BGB iVm § 126b BGB als Textform-Erklärung für einen Verkäufer-Maklervertrag dann nicht, wenn sie die konkrete Provisionsvereinbarung nicht mit hinreichender Bestimmtheit bezeichnet und lediglich eine Maximalquote angibt.", INDENT),
        sp(0.2),
        p("2. Der Bereicherungsausschluss nach § 818 Abs. 3 BGB steht einem Rückforderungsanspruch nach § 812 Abs. 1 Satz 1 Alt. 1 BGB wegen Formmangels eines Maklervertrages nach § 656a BGB dann nicht entgegen, wenn der Formverstoß den spezifischen Schutzzweck der Norm verletzt, der auch den Bereicherungsausgleich einschließt.", INDENT),
        sp(0.2),
        p("3. Eine notarielle Maklerklausel im Kaufvertrag konvalidiert einen formunwirksamen Verkäufer-Maklervertrag nach § 656a BGB nicht, da es an einer gesetzlichen Heilungsvorschrift fehlt und eine Analogie zu § 311b Abs. 1 Satz 2 BGB ausscheidet.", INDENT),
        sp(0.3),
        section_header("Begründung (sinngemäße Zusammenfassung — Auszug)"),
        p("Der I. Zivilsenat bestätigt im Ergebnis die Verurteilung der Revisionsklägerin zur Rückzahlung der Maklerprovision in Höhe von EUR 8.810,76. Die Begründung weicht in Teilen von den Vorinstanzen ab, führt aber zum gleichen Ergebnis.", NORMAL),
        sp(0.2),
        p("Der Senat stellt klar, dass § 656a BGB iVm § 126b BGB nicht lediglich eine Formvorschrift im technischen Sinne enthält, sondern eine materiell-rechtliche Anforderung an den Inhalt der Erklärung begründet: Der Maklervertrag muss in Textform so gefasst sein, dass der Verbraucher anhand der Erklärung seine wesentlichen Rechte und Pflichten erkennen kann. Hierzu gehört — zumindest in hinreichend bestimmbarer Form — die konkrete Provisionspflicht. Eine Signaturzeile, die nur einen Maximalwert angibt, ohne konkret auf die vereinbarte Provision Bezug zu nehmen, unterschreitet diese Schwelle.", NORMAL),
        sp(0.2),
        p("Zum Bereicherungsausschluss führt der Senat aus: Da § 656a BGB ein Verbraucherschutzgesetz ist und die Formpflicht als konstitutives Element des Schutzsystems ausgestaltet ist, würde eine Berufung der Maklerin auf Entreicherung nach § 818 Abs. 3 BGB den gesetzgeberischen Schutzzweck unterlaufen. Der Senat sieht sich in Übereinstimmung mit BGH, Urteil vom 20. April 2023, I ZR 197/22.", NORMAL),
        sp(0.4),
        p("gez. VRiBGH Dr. Klaus-Peter Mandelkern-Ingolstadt · RiBGH Dr. Dorothea Streit-Waldenfels · RiBGH Dr. Benedikt Nymphenburg-Rauch · RiBGH Dr. Hannelore Ostmark-Freising · RiBGH Dr. Georg Wenzeslaus-Traunstein", SMALL_C),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 20. MANDANTENMEMO
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(20, "Mandantenmemo — RA Dr. Hagelbrand-Wittlsbach"),
        kanzlei_logo_ht(),
        sp(0.3),
        p("<b>MEMO AN MANDANTEN</b>", TITLE2),
        p("Vertraulich — nur für Eheleute Haspelbeck-Türkenfeld bestimmt", make_style('vertrl', fontName='Helvetica-Oblique', fontSize=9, textColor=HexColor("#884400"))),
        sp(0.3),
        Table([
            ["An:", "Korbinian und Walburga Haspelbeck-Türkenfeld, Mauerkircherstraße 47, 81679 München"],
            ["Von:", "RA Dr. Knut Hagelbrand-Wittlsbach"],
            ["Datum:", "14. März 2026"],
            ["Betreff:", "BGH-Urteil I ZR 202/25 vom 11. März 2026 — Ergebnis und weiteres Vorgehen"],
            ["Az. intern:", "HT/2023/0842/HWI"],
        ], colWidths=[2.5*cm, 14.5*cm], style=TableStyle([
            ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'), ('FONTSIZE', (0,0), (-1,-1), 9.5),
            ('LEADING', (0,0), (-1,-1), 14), ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('ROWBACKGROUNDS', (0,0), (-1,-1), [HexColor("#F0F4FA"), colors.white]),
            ('GRID', (0,0), (-1,-1), 0.3, RANDGRAU),
            ('LEFTPADDING', (0,0), (-1,-1), 5), ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ])),
        sp(0.3),
        p("<b>1. Ergebnis</b>", TITLE3),
        p("Sehr geehrte Frau Haspelbeck-Türkenfeld, sehr geehrter Herr Haspelbeck-Türkenfeld,", NORMAL),
        sp(0.1),
        p("ich freue mich, Ihnen mitteilen zu können, dass der Bundesgerichtshof am 11. März 2026 (Az. I ZR 202/25) die Revision der Gegenseite zurückgewiesen und damit das Urteil des OLG München bestätigt hat. Die Maklerin Frau Bechtholdsmeier-Schongau ist zur Rückzahlung der Maklerprovision in Höhe von <b>EUR 8.810,76</b> zuzüglich Zinsen in Höhe von 5 Prozentpunkten über dem Basiszinssatz seit dem 05. September 2023 verurteilt.", NORMAL),
        sp(0.2),
        p("Konkret bedeutet dies: Zum heutigen Tag (14. März 2026) sind Zinsen in Höhe von ca. EUR 2.260,00 (Schätzung, abhängig vom aktuellen Basiszinssatz) aufgelaufen. Der Gesamtbetrag (Hauptforderung + Zinsen) beläuft sich auf ca. <b>EUR 11.070,00</b>.", NORMAL),
        sp(0.3),
        p("<b>2. Juristische Bedeutung</b>", TITLE3),
        p("Das BGH-Urteil hat über Ihren Einzelfall hinausgehende Bedeutung: Es stellt klar, dass Makler künftig sicherstellen müssen, dass der Verkäufer-Maklervertrag in einer individuellen, auf den konkreten Auftrag zugeschnittenen Textform-Erklärung geschlossen wird, die die konkrete Provision und das Leistungsobjekt bezeichnet. Die Praxis, Provisionshinweise in Standard-E-Mail-Signaturen zu platzieren, genügt nach diesem Urteil nicht.", NORMAL),
        sp(0.3),
        p("<b>3. Vollstreckung</b>", TITLE3),
        p("Die Beklagte hat die Möglichkeit, den Betrag freiwillig zu zahlen. Ich werde RAin Dr. Korkenzieher-Mariastein unverzüglich anschreiben und zur Zahlung binnen 14 Tagen auffordern. Sollte die Zahlung nicht eingehen, werden wir die Zwangsvollstreckung einleiten (Pfändungs- und Überweisungsbeschluss hinsichtlich der Geschäftskonten der Bechtholdsmeier-Schongau e.K.).", NORMAL),
        sp(0.3),
        p("<b>4. Kostenrechnung (vorläufig)</b>", TITLE3),
        p("Eine vollständige Kostenrechnung erhalten Sie mit gesondertem Schreiben (vgl. Bestandteil 23 dieser Akte). Ich weise darauf hin, dass die obsiegende Partei Anspruch auf Erstattung der gesetzlichen Anwaltsgebühren (RVG) durch die Gegenseite hat; die darüber hinausgehenden Stundenhonorare sind ausweislich unserer Mandatsvereinbarung von der Rechtsschutzversicherung zu tragen.", NORMAL),
        sp(0.5),
        p("Mit herzlichem Glückwunsch und freundlichen Grüßen", NORMAL_L),
        sp(0.2),
        p("RA Dr. Knut Hagelbrand-Wittlsbach", BOLD),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 21. HANDSCHRIFTLICHE NOTIZEN (Korbinian Haspelbeck)
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(21, "Handschriftliche Randnotizen — Korbinian Haspelbeck-Türkenfeld"),
        p("Die folgenden Notizen wurden auf verschiedenen Schriftsätzen der Akte aufgefunden. Sie wurden von Korbinian Haspelbeck-Türkenfeld mit Kugelschreiber (blau) am Rand angebracht. Wiedergabe kursiv, mit linker Einrückung.", SMALL),
        sp(0.3),
        p("<b>Notiz 1</b> (auf Klageerwiderung S. 3, neben Abschnitt zur Textform):", BOLD),
        p("„Das stimmt doch garnicht — Walburga: hatte ich nicht GENAU GEFRAGT?! Bechtholdsmeier hatte gesagt es sei alles in Ordnung. Und jetzt das. Ich fass es nicht."", ITALIC),
        sp(0.2),
        p("<b>Notiz 2</b> (auf Kaufvertrag-Auszug, neben § 13 Maklerklausel):", BOLD),
        p("„Hab ich gelesen aber dachte das ist Standard. Notar hat nicht erklärt das wir dann NOCHMAL zahlen müssen für Verkäufer. So ein Mist."", ITALIC),
        sp(0.2),
        p("<b>Notiz 3</b> (auf E-Mail-Ausdruck vom 03.04.2023, neben Signatur-Provisionshinweis):", BOLD),
        p("„Das hab ich nie bewusst gesehen! Steht ja ganz am Ende klein. Walburga auch nicht. Hab die E-Mail schnell gelesen wegen Terminanfrage Höglmayr. Provision — nein. Hab nur Kaufpreis gesehen."", ITALIC),
        sp(0.2),
        p("<b>Notiz 4</b> (auf Vergleichsprotokoll, neben Vergleichsangebot 50%):", BOLD),
        p("„NEIN. Nicht Vergleich. Die soll das ganze zurückzahlen was sie uns zu unrecht abgenommen hat. Walburga sagt auch nein. Dr. Hagelbrand hat gesagt wir gewinnen. Also nein."", ITALIC),
        sp(0.2),
        p("<b>Notiz 5</b> (auf Berufungsbegründung S. 7, neben Abschnitt zur Entreicherung):", BOLD),
        p("„ENTREICHERUNG??? Die hat 8810 Euro bekommen und sagt jetzt sie ist arm? Das ist doch Wahnsinn. (Tipp-Fehlr: Berreicherung? Wie schreibt man das?) Dr. Hbr hat erklärt das zählt nicht — gut."", ITALIC),
        sp(0.2),
        p("<b>Notiz 6</b> (auf BGH-Urteil Tenor-Auszug, daneben, mit Ausrufezeichen):", BOLD),
        p("„!!! GEWONNEN !!! Walburga ruft gleich an. Danke BGH."", ITALIC),
        sp(0.3),
        p("<i>Die Originalnotizen befinden sich in Sonderband II der Akte (nicht abgebildet, vgl. Anlage K-MAK-21).</i>", ITALIC),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 22. WHATSAPP-SCREENSHOT-SIMULATION
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(22, "WhatsApp-Screenshot-Simulation — Konversation während Notartermin"),
        p("Anlage K-MAK-8 (Simulation des Chat-Verlaufs, aus dem Gedächtnis rekonstruiert; kein Originalausdruck vorhanden — vom Kläger als Zeugenaussage eingeführt).", SMALL),
        sp(0.3),
        p("<b>WhatsApp — Konversation: Walburga ↔ Korbinian Haspelbeck-Türkenfeld</b>", NOTA_BENE),
        p("Datum: 12. Mai 2023 (Notartermin Uhrzeit: 14:00–16:15 Uhr)", SMALL),
        sp(0.3),
    ]
    # WhatsApp chat simulation
    for bubble in [
        ("Walburga", False, "Korbinian, hast du das mit der Provision heute geklärt? Die Bechtholdsmeier hat doch was gesagt von wegen Verkäuferprovision. Ich bin da nicht sicher.", "14:23"),
        ("Korbinian", True, "Hab nachgefragt. Sie sagt das ist normal so, immer beim Hausverkauf. Hab unterschrieben. War alles irgendwie sehr schnell heute.", "14:41"),
        ("Walburga", False, "Wieviel ist das denn?? Hast du gefragt wieviel genau?", "14:43"),
        ("Korbinian", True, "Ca 8800 glaub ich. Sie hat was von 1,2% gesagt. War auf Rechnung glaub ich. Ich schau nachher.", "14:51"),
        ("Walburga", False, "8800?! Das ist viel! Hatten wir das besprochen?? Ich erinner mich nicht an genaue Zahl. Frag nochmal wenn du kannst.", "14:54"),
        ("Korbinian", True, "Notar ist schon fertig. Unterschriften sind drin. Walburga das klären wir nachher. Jetzt erst Kaffee 😅", "15:02"),
        ("Walburga", False, "Ok aber ich will das genau wissen. Klingt komisch.", "15:04"),
    ]:
        name, is_sender, text, time = bubble
        label_style = ParagraphStyle(f'walabel_{time}', fontName='Helvetica-Bold', fontSize=8,
                                     textColor=HexColor("#444444"),
                                     alignment=TA_RIGHT if is_sender else TA_LEFT,
                                     leftIndent=3*cm if is_sender else 0,
                                     rightIndent=0 if is_sender else 3*cm)
        story.append(p(name, label_style))
        story += wa_bubble(text, is_sender, time)

    story += [
        sp(0.4),
        p("<i>Anmerkung: Dieser Chat-Verlauf wurde von Walburga Haspelbeck-Türkenfeld im Rahmen der Klagebegründung aus dem Gedächtnis schriftlich rekonstruiert. Das Original-Smartphone ist verfügbar; die Kläger bieten die Vorlage des Originalgeräts an. RAin Dr. Korkenzieher-Mariastein hat in der Klageerwiderung die Authentizität nicht bestritten, jedoch die Beweiserheblichkeit in Abrede gestellt.</i>", ITALIC),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 23. KANZLEIRECHNUNG (RVG)
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(23, "Kanzleirechnung — Hagelbrand & Trotzenburg (RVG)"),
        kanzlei_logo_ht(),
        sp(0.3),
        p("Hagelbrand &amp; Trotzenburg Rechtsanwälte · Promenadeplatz 9 · 80333 München", SMALL),
        p("USt-IdNr. DE 814 222 017 · Steuer-Nr. 143/200/20422 · IBAN: DE88 7002 0270 0015 5882 27", SMALL),
        sp(0.3), hr(), sp(0.2),
        p("<b>HONORARRECHNUNG</b>", TITLE2),
        p("Rechnungs-Nr. HT/2026/0097 · München, 14. März 2026", NORMAL_L),
        sp(0.3),
        Table([
            ["An:", "Korbinian und Walburga Haspelbeck-Türkenfeld\nMauerkircherstraße 47\n81679 München"],
            ["Betreff:", "Honorarrechnung für anwaltliche Vertretung in\nHaspelbeck-Türkenfeld ./. Bechtholdsmeier-Schongau e.K.\nAz. LG München I 12 O 8842/23 / OLG München 13 U 412/24 / BGH I ZR 202/25"],
            ["Streitwert:", "EUR 8.810,76"],
            ["Zeitraum:", "04. September 2023 bis 14. März 2026"],
        ], colWidths=[2.5*cm, 14.5*cm], style=TableStyle([
            ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'), ('FONTSIZE', (0,0), (-1,-1), 9),
            ('LEADING', (0,0), (-1,-1), 13), ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('GRID', (0,0), (-1,-1), 0.3, RANDGRAU),
            ('LEFTPADDING', (0,0), (-1,-1), 5), ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ])),
        sp(0.3),
        p("<b>Gebührenpositionen nach RVG (Streitwert EUR 8.810,76)</b>", BOLD),
        p("Gem. Anlage 2 zum RVG: Streitwert EUR 8.810,76 → Gebührenstufe bis EUR 9.000,00 → einfache Gebühr (1,0): EUR 619,00", SMALL),
        sp(0.2),
    ]
    rvg_data = [
        ["Pos.", "Beschreibung", "Faktor", "Betrag (netto)"],
        ["1", "Verfahrensgebühr 1. Instanz (Nr. 3100 VV RVG) — LG München I", "1,3", "EUR 804,70"],
        ["2", "Terminsgebühr 1. Instanz (Nr. 3104 VV RVG) — Gütetermin + Haupttermin (je 1,2)", "1,2 × 2", "EUR 1.485,60"],
        ["3", "Verfahrensgebühr Berufung (Nr. 3200 VV RVG) — OLG München", "1,6", "EUR 990,40"],
        ["4", "Terminsgebühr Berufung (Nr. 3202 VV RVG) — OLG München", "1,2", "EUR 742,80"],
        ["5", "Verfahrensgebühr Revision (Nr. 3206 VV RVG) — BGH", "1,6", "EUR 990,40"],
        ["6", "Terminsgebühr Revision (Nr. 3210 VV RVG) — BGH", "1,5", "EUR 928,50"],
        ["7", "Einigungsgebühr (Nr. 1000 VV RVG) — entfällt (kein Vergleich), Ansatz 0", "0,0", "EUR 0,00"],
        ["8", "Auslagenpauschale (Nr. 7002 VV RVG)", "pauschal", "EUR 20,00"],
        ["9", "Fahrtkosten Karlsruhe (BGH-Termin), 185 km × 2 × EUR 0,42 (Nr. 7003 VV RVG)", "pauschal", "EUR 155,40"],
        ["", "<b>Summe netto</b>", "", "<b>EUR 6.117,80</b>"],
        ["", "Mehrwertsteuer 19 %", "", "EUR 1.162,38"],
        ["", "<b>Gesamtbetrag brutto</b>", "", "<b>EUR 7.280,18</b>"],
        ["", "Abzgl. erstattete gesetzl. Gebühren durch Gegenseite (voraussichtlich)", "", "- EUR 4.836,00"],
        ["", "Abzgl. Rechtsschutzversicherung ARAG (voraussichtlich)", "", "- EUR 2.444,18"],
        ["", "<b>Verbleibender Eigenanteil Mandant</b>", "", "<b>EUR 0,00</b>"],
    ]
    rvgt = Table(rvg_data, colWidths=[0.7*cm, 9.3*cm, 3*cm, 4*cm])
    rvgt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DUNKELBLAU), ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'), ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('LEADING', (0,0), (-1,-1), 12), ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, HexColor("#F5F8FF")]),
        ('GRID', (0,0), (-1,-1), 0.3, RANDGRAU),
        ('ALIGN', (2,0), (3,-1), 'RIGHT'),
        ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('FONTNAME', (1,10), (3,10), 'Helvetica-Bold'),
        ('FONTNAME', (1,12), (3,12), 'Helvetica-Bold'),
        ('FONTNAME', (1,14), (3,14), 'Helvetica-Bold'),
        ('BACKGROUND', (0,10), (-1,10), HexColor("#E8F0FF")),
        ('BACKGROUND', (0,12), (-1,12), HexColor("#D8ECFF")),
        ('BACKGROUND', (0,14), (-1,14), HexColor("#E8FFE8")),
    ]))
    story.append(rvgt)
    story += [
        sp(0.3),
        p("Die Kläger werden auf die Möglichkeit der Festsetzung der erstattungsfähigen Kosten gegen die Beklagte nach § 104 ZPO hingewiesen (Kostenfestsetzungsantrag wird gesondert gestellt).", SMALL),
        sp(0.3),
        p("München, 14. März 2026", NORMAL_L),
        sp(0.2),
        p("RA Dr. Knut Hagelbrand-Wittlsbach", BOLD),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 24. AKTENRAND-MEMO RAin Korkenzieher-Mariastein (rot)
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(24, "Aktenrand-Memo RAin Dr. Korkenzieher-Mariastein (interne Notiz, rot)"),
        sp(0.3),
        Table([[Paragraph("""<font color="#CC0000"><b>INTERNE KANZLEINOTIZ — VERTRAULICH — KORKENZIEHER MAIBACH PARTNER mbB</b></font>

<font color="#CC0000"><b>An:</b></font> Frau Bechtholdsmeier-Schongau (Mandantin)
<font color="#CC0000"><b>Von:</b></font> RAin Dr. Adelheid Korkenzieher-Mariastein
<font color="#CC0000"><b>Datum:</b></font> 14. März 2026
<font color="#CC0000"><b>Re.:</b></font> BGH-Urteil I ZR 202/25 — Konsequenzen für Ihren Geschäftsbetrieb

<font color="#CC0000"><b>Sehr geehrte Frau Bechtholdsmeier-Schongau,</b></font>

wie telefonisch besprochen weise ich Sie nochmals ausdrücklich auf folgendes hin:

<font color="#CC0000"><b>1. E-Mail-Templates anpassen:</b></font>
Die bisherige Praxis, einen Provisionshinweis am Ende jeder Signatur-Zeile zu platzieren, genügt nach dem BGH-Urteil nicht. Künftig ist für jeden Maklervertrag ein <i>individueller, auf den konkreten Auftrag zugeschnittener</i> Textform-Vertrag in einer eigenständigen Erklärung zu erstellen. Die Schluss-Markierung (d.h. die Erkennbarmachung des Abschlusses der Erklärung) muss NACH allen inhaltlichen Hinweisen erfolgen — <font color="#CC0000"><b>§ 126b Satz 1 BGB!</b></font>

<font color="#CC0000"><b>2. Sofortmaßnahmen:</b></font>
- Alle laufenden Maklerverträge, die nur per E-Mail-Signatur begründet wurden, sind auf ihre Formwirksamkeit zu überprüfen.
- Für alle offenen Provisionsansprüche empfehle ich, unverzüglich schriftliche Bestätigungen in Textform einzuholen.
- Das Muster-Widerrufsformular ist künftig separat für Verkäufer- und Käufer-Maklerverträge zu verwenden.

<font color="#CC0000"><b>3. Zahlung:</b></font>
Die Überweisung von EUR 8.810,76 zuzüglich Zinsen an die Kläger sollte bis spätestens 28. März 2026 erfolgen, um Vollstreckungskosten zu vermeiden.

<font color="#CC0000"><b>4. Kosten dieser Kanzlei:</b></font>
Unsere Schlussrechnung erhalten Sie gesondert. Der Betrag beläuft sich nach vorläufiger Schätzung auf EUR 9.840,00 brutto (3 Instanzen).

Mit freundlichen Grüßen
RAin Dr. Adelheid Korkenzieher-Mariastein
Korkenzieher Maibach Partner mbB · Karlsplatz 4 · 80335 München""", MONO_SMALL)]],
            colWidths=[17*cm], style=TableStyle([
                ('BOX', (0,0), (-1,-1), 1.5, ROT), ('BACKGROUND', (0,0), (-1,-1), HexColor("#FFF8F8")),
                ('LEFTPADDING', (0,0), (-1,-1), 12), ('RIGHTPADDING', (0,0), (-1,-1), 12),
                ('TOPPADDING', (0,0), (-1,-1), 10), ('BOTTOMPADDING', (0,0), (-1,-1), 10),
            ])),
        sp(0.3),
        p("<i>Dieses Dokument wurde in der Handakte der Beklagten aufgefunden und von der Beklagten im Verlauf des Rechtsstreits nicht als Anlage eingeführt. Fundstelle: Sonderband I der Beklagten-Akte, übergeben im Termin vom 12.06.2024.</i>", ITALIC),
        pb(),
    ]

    # ─────────────────────────────────────────────────────────────────────────
    # 25. ANLAGENVERZEICHNIS
    # ─────────────────────────────────────────────────────────────────────────
    story += [
        bestandteil_nr(25, "Anlagenverzeichnis K-MAK-1 bis K-MAK-29"),
        p("Anlagenverzeichnis zur Klageschrift vom 14. September 2023 sowie zu den weiteren Schriftsätzen.", SMALL),
        sp(0.3),
    ]
    anl_data = [
        ["Anlage-Nr.", "Bezeichnung", "Datum", "Seiten", "Bemerkung"],
        ["K-MAK-1", "Käufer-Maklervertrag (Textform) — Kauf Rosenheimer Str. 88", "Aug. 2022", "3", ""],
        ["K-MAK-2", "Widerrufsbelehrung Käufer-Maklervertrag Aug. 2022", "Aug. 2022", "2", ""],
        ["K-MAK-3", "E-Mail-Kette (vollständig), 30.03.–12.08.2023", "2023", "12", ""],
        ["K-MAK-4", "Rechnung Maklerprovision Re.Nr. 2023/0514", "15.05.2023", "1", ""],
        ["K-MAK-5", "Kaufvertrag-Auszug UR-Nr. 1488/2023 (Notar Dr. Vorstetter)", "12.05.2023", "18", "§ 13 Maklerklausel"],
        ["K-MAK-6", "Widerrufserklärung RA Hagelbrand-Wittlsbach", "03.08.2023", "2", ""],
        ["K-MAK-7", "— NICHT ABGEBILDET — (vgl. Sonderband II)", "—", "—", "Enthält: Grundbuchauszug Mauerkircherstr. 47 — nicht übermittelt"],
        ["K-MAK-8", "WhatsApp-Konversation (rekonstruiert)", "12.05.2023", "1", ""],
        ["K-MAK-9", "Banküberweisung Haspelbeck → Treuhandkonto", "28.05.2023", "1", ""],
        ["K-MAK-10", "Bestätigungsmail Notar Dr. Vorstetter", "13.04.2023", "1", ""],
        ["K-MAK-11", "Schreiben RA Hagelbrand-Wittlsbach an Korkenzieher-Mariastein", "03.08.2023", "3", ""],
        ["K-MAK-12", "Antwortschreiben RAin Korkenzieher-Mariastein", "12.08.2023", "2", ""],
        ["K-MAK-13", "— NICHT ABGEBILDET — (vgl. Sonderband II)", "—", "—", "Enthält: Kontoauszüge Haspelbeck — datenschutzrechtlich geschwärzt"],
        ["K-MAK-14", "Quittung Maklerin über EUR 8.810,76", "30.05.2023", "1", ""],
        ["K-MAK-15", "Aktennotiz RA Hagelbrand-Wittlsbach (Erstgespräch)", "04.09.2023", "2", ""],
        ["K-MAK-16", "Deckungszusage ARAG Rechtsschutz", "12.09.2023", "1", ""],
        ["K-MAK-17", "BGH-Urteil I ZR 197/22 (Ablichtung)", "20.04.2023", "28", "Grundsatzurteil"],
        ["K-MAK-18", "LG München I, Hinweisbeschluss 7 O 14552/22", "14.11.2022", "4", ""],
        ["K-MAK-19", "Urteil LG München I 12 O 8842/23", "19.06.2024", "22", ""],
        ["K-MAK-20", "Berufungsurteil OLG München 13 U 412/24", "17.02.2025", "18", ""],
        ["K-MAK-21", "— NICHT ABGEBILDET — (vgl. Sonderband II)", "—", "—", "Enthält: Originalhandschriften Korbinian Haspelbeck"],
        ["K-MAK-22", "BGH-Urteil I ZR 202/25 (Volltext)", "11.03.2026", "34", ""],
        ["K-MAK-23", "Kostenfestsetzungsantrag Hagelbrand & Trotzenburg", "14.03.2026", "4", ""],
        ["K-MAK-24", "Muster-Widerrufsformular (Käufer-MV)", "Aug. 2022", "1", ""],
        ["K-MAK-25", "Grundbuchauszug (aktuell, nach Eigentumsumschreibung)", "Juni 2023", "3", ""],
        ["K-MAK-26", "Schreiben Notar Vorstetter zur Maklerklausel", "15.05.2023", "2", ""],
        ["K-MAK-27", "Stellungnahme Kläger zu BGH-Termin", "20.02.2026", "3", ""],
        ["K-MAK-28", "Vollmacht Haspelbeck an RA Hagelbrand-Wittlsbach", "04.09.2023", "1", ""],
        ["K-MAK-29", "Mandatsrechnung Korkenzieher Maibach Partner mbB (Beklagte)", "März 2026", "4", ""],
    ]
    anlt = Table(anl_data, colWidths=[2.3*cm, 6.5*cm, 2.5*cm, 1.5*cm, 4.2*cm])
    anlt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DUNKELBLAU), ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'), ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('LEADING', (0,0), (-1,-1), 11), ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, HexColor("#F5F8FF")]),
        ('GRID', (0,0), (-1,-1), 0.3, RANDGRAU),
        ('LEFTPADDING', (0,0), (-1,-1), 3), ('RIGHTPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 2), ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        # Mark "nicht abgebildet" rows
        ('BACKGROUND', (0,7), (-1,7), HexColor("#FFEEEE")),
        ('BACKGROUND', (0,13), (-1,13), HexColor("#FFEEEE")),
        ('BACKGROUND', (0,21), (-1,21), HexColor("#FFEEEE")),
        ('FONTNAME', (0,7), (-1,7), 'Helvetica-Oblique'),
        ('FONTNAME', (0,13), (-1,13), 'Helvetica-Oblique'),
        