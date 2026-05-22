#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_testakte.py
Testakte Meissner Rheinwerk AG – Projekt RHEINGOLD 2030 (bAV-Großmandat)
Kanzlei: Treuenfels Yamamoto Rechtsanwälte Partnerschaft mbB
Aktenzeichen: TY-2026-RHEINGOLD-001

Generates a 90-130 page realistic legal case file (Testakte) as PDF.
"""

import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm, mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.platypus.flowables import Flowable
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, red, black, white, grey, Color

# ── Output path ──────────────────────────────────────────────────────────────
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "Testakte_Meissner_Rheinwerk_AG_bAV.pdf")

# ── Color palette ─────────────────────────────────────────────────────────────
DARK_BLUE   = HexColor("#1a2d5a")
MID_BLUE    = HexColor("#2e4fa3")
LIGHT_BLUE  = HexColor("#d6e4f7")
RHEIN_GOLD  = HexColor("#c9a64a")
SAKURA_PINK = HexColor("#e8a0b0")
FAX_GRAY    = HexColor("#e8e8e0")
HANDW_RED   = HexColor("#cc2200")
PALE_YELLOW = HexColor("#fefce6")
SECTION_BG  = HexColor("#f4f7fb")

PAGE_W, PAGE_H = A4
MARGIN = 2.2 * cm

# ── Styles ────────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def make_style(name, **kwargs):
    base = kwargs.pop("parent", "Normal")
    s = ParagraphStyle(name, parent=styles[base], **kwargs)
    return s

# Core styles
S_NORMAL     = make_style("TY_Normal",      fontName="Helvetica",       fontSize=9.5,  leading=17,   spaceAfter=7,  spaceBefore=2, leftIndent=0)
S_BODY       = make_style("TY_Body",        fontName="Times-Roman",     fontSize=9.5,  leading=19,   spaceAfter=10, spaceBefore=3, alignment=TA_JUSTIFY)
S_BODY_SM    = make_style("TY_Body_SM",     fontName="Times-Roman",     fontSize=8.5,  leading=17,   spaceAfter=7,  spaceBefore=2, alignment=TA_JUSTIFY)
S_H1         = make_style("TY_H1",          fontName="Helvetica-Bold",  fontSize=14,   leading=20,   spaceBefore=20,spaceAfter=12, textColor=DARK_BLUE)
S_H2         = make_style("TY_H2",          fontName="Helvetica-Bold",  fontSize=11,   leading=17,   spaceBefore=16,spaceAfter=9,  textColor=DARK_BLUE)
S_H3         = make_style("TY_H3",          fontName="Helvetica-Bold",  fontSize=10,   leading=16,   spaceBefore=12, spaceAfter=7,  textColor=MID_BLUE)
S_H4         = make_style("TY_H4",          fontName="Helvetica-BoldOblique", fontSize=9.5, leading=16, spaceBefore=10, spaceAfter=6, textColor=DARK_BLUE)
S_CENTER     = make_style("TY_Center",      fontName="Helvetica",       fontSize=9.5,  leading=14,   alignment=TA_CENTER)
S_CENTER_B   = make_style("TY_CenterB",     fontName="Helvetica-Bold",  fontSize=10,   leading=15,   alignment=TA_CENTER)
S_TITLE_BIG  = make_style("TY_TitleBig",    fontName="Helvetica-Bold",  fontSize=22,   leading=28,   alignment=TA_CENTER, textColor=DARK_BLUE)
S_TITLE_MED  = make_style("TY_TitleMed",    fontName="Helvetica-Bold",  fontSize=14,   leading=19,   alignment=TA_CENTER, textColor=DARK_BLUE)
S_TITLE_GOLD = make_style("TY_TitleGold",   fontName="Helvetica-Bold",  fontSize=12,   leading=17,   alignment=TA_CENTER, textColor=RHEIN_GOLD)
S_HANDW      = make_style("TY_Handw",       fontName="Times-Italic",    fontSize=9,    leading=19,   leftIndent=10, textColor=HANDW_RED, spaceAfter=10, spaceBefore=5)
S_HANDW_BLK  = make_style("TY_HandwBlk",   fontName="Times-Italic",    fontSize=9,    leading=15,   leftIndent=10, textColor=black, spaceAfter=4)
S_FAX        = make_style("TY_Fax",         fontName="Courier",         fontSize=8.5,  leading=14,   spaceAfter=4,  backColor=FAX_GRAY)
S_FAX_HDR    = make_style("TY_FaxHdr",      fontName="Courier-Bold",    fontSize=8.5,  leading=12,   backColor=FAX_GRAY)
S_TOC_ENTRY  = make_style("TY_TOC",         fontName="Times-Roman",     fontSize=9,    leading=16,   leftIndent=5,  spaceAfter=5)
S_TOC_CAT    = make_style("TY_TOCCAT",      fontName="Helvetica-Bold",  fontSize=9.5,  leading=16,   spaceBefore=10, spaceAfter=4, textColor=DARK_BLUE)
S_FOOTER     = make_style("TY_Footer",      fontName="Helvetica",       fontSize=7.5,  leading=10,   textColor=grey, alignment=TA_CENTER)
S_MONO       = make_style("TY_Mono",        fontName="Courier",         fontSize=8.5,  leading=14,   spaceAfter=3)
S_BULLET     = make_style("TY_Bullet",      fontName="Times-Roman",     fontSize=9.5,  leading=17,   leftIndent=15, bulletIndent=5, spaceAfter=6)
S_INDENT     = make_style("TY_Indent",      fontName="Times-Roman",     fontSize=9.5,  leading=19,   leftIndent=20, spaceAfter=9, spaceBefore=3)
S_JP_DE      = make_style("TY_JP_DE",       fontName="Helvetica",       fontSize=8.5,  leading=13,   spaceAfter=3)
S_WARN       = make_style("TY_Warn",        fontName="Helvetica-Bold",  fontSize=9,    leading=13,   textColor=HANDW_RED, spaceAfter=3)
S_TABLE_HDR  = make_style("TY_TblHdr",      fontName="Helvetica-Bold",  fontSize=8.5,  leading=11,   textColor=white, alignment=TA_CENTER)
S_TABLE_CELL = make_style("TY_TblCell",     fontName="Helvetica",       fontSize=8.5,  leading=11,   alignment=TA_LEFT)
S_TABLE_R    = make_style("TY_TblCellR",    fontName="Helvetica",       fontSize=8.5,  leading=11,   alignment=TA_RIGHT)
S_SMALL_GRAY = make_style("TY_SmGray",      fontName="Helvetica",       fontSize=7.5,  leading=13,   spaceAfter=3, textColor=grey)
S_KURSIV     = make_style("TY_Kursiv",      fontName="Times-Italic",    fontSize=9.5,  leading=19,   spaceAfter=10, spaceBefore=3, alignment=TA_JUSTIFY)
S_LATIN      = make_style("TY_Latin",       fontName="Times-Italic",    fontSize=8.5,  leading=15,   textColor=HexColor("#444444"), spaceAfter=5)
# Style aliases for appended sections
S_ITALIC     = S_KURSIV      # Times-Italic justified
S_BOLD       = S_H3          # Helvetica-Bold blue heading used as bold body
S_BOLD_BODY  = make_style("TY_BoldBody", fontName="Helvetica-Bold", fontSize=9.5, leading=14, spaceAfter=4)


# ── Helper Flowables ──────────────────────────────────────────────────────────
class HankoStamp(Flowable):
    """Simulates a Japanese red hanko stamp."""
    def __init__(self, text="認印", x=0, y=0, size=50):
        Flowable.__init__(self)
        self.text = text
        self.stamp_size = size
        self.width = size + 20
        self.height = size + 20

    def draw(self):
        c = self.canv
        sz = self.stamp_size
        x0, y0 = 10, 10
        c.setStrokeColor(HexColor("#cc0000"))
        c.setFillColor(HexColor("#cc0000"))
        c.setLineWidth(2.5)
        c.rect(x0, y0, sz, sz, stroke=1, fill=0)
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(HexColor("#cc0000"))
        c.drawCentredString(x0 + sz/2, y0 + sz/2 - 4, self.text)


class SakuraLine(Flowable):
    """Decorative sakura + wave line."""
    def __init__(self, width=None):
        Flowable.__init__(self)
        self.width = width or (PAGE_W - 2*MARGIN)
        self.height = 14

    def draw(self):
        c = self.canv
        w = self.width
        # Draw wave in blue
        c.setStrokeColor(MID_BLUE)
        c.setLineWidth(0.7)
        p = c.beginPath()
        p.moveTo(0, 6)
        step = w / 20
        for i in range(20):
            x = i * step
            y = 6 + (4 if i % 2 == 0 else -4)
            p.lineTo(x + step/2, y)
        p.lineTo(w, 6)
        c.drawPath(p, stroke=1, fill=0)
        # Pink dots simulating sakura
        c.setFillColor(SAKURA_PINK)
        for i in [2, 6, 10, 14, 18]:
            cx = i * step
            c.circle(cx, 6, 2.5, stroke=0, fill=1)


class RheinGoldBar(Flowable):
    """A gold horizontal bar for section headers."""
    def __init__(self, width=None, height=4):
        Flowable.__init__(self)
        self.width = width or (PAGE_W - 2*MARGIN)
        self.height = height

    def draw(self):
        c = self.canv
        c.setFillColor(RHEIN_GOLD)
        c.rect(0, 0, self.width, self.height, stroke=0, fill=1)


class BlueBanner(Flowable):
    """Dark blue banner for major section titles."""
    def __init__(self, text, width=None, height=22):
        Flowable.__init__(self)
        self.text = text
        self.width = width or (PAGE_W - 2*MARGIN)
        self.height = height

    def draw(self):
        c = self.canv
        c.setFillColor(DARK_BLUE)
        c.rect(0, 0, self.width, self.height, stroke=0, fill=1)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(8, 6, self.text)


def hr(color=MID_BLUE, thickness=0.7):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=4, spaceBefore=4)

def sp(h=6):
    return Spacer(1, h)

def P(text, style=None):
    return Paragraph(text, style or S_BODY)

def PH(text, style=None):
    return Paragraph(text, style or S_H2)

def PN(text):
    return Paragraph(text, S_NORMAL)

def fax_block(lines, sender="", receiver="", date="", pages=""):
    """Returns a list of flowables simulating a fax transmission."""
    result = []
    header = f"=== FAX TRANSMISSION ===  VON: {sender}  AN: {receiver}  DAT: {date}  SEITEN: {pages} ==="
    result.append(Paragraph(header, S_FAX_HDR))
    result.append(Paragraph("=" * 85, S_FAX))
    for line in lines:
        result.append(Paragraph(line, S_FAX))
    result.append(Paragraph("=" * 85, S_FAX))
    result.append(Paragraph("=== ENDE DER ÜBERTRAGUNG ===", S_FAX_HDR))
    result.append(sp(6))
    return result

def section_header(title, sub=""):
    elems = []
    elems.append(sp(8))
    elems.append(RheinGoldBar())
    elems.append(sp(2))
    elems.append(Paragraph(title, S_H1))
    if sub:
        elems.append(Paragraph(sub, S_H3))
    elems.append(hr())
    return elems

def mini_header(title):
    return [sp(5), Paragraph(title, S_H2), hr(MID_BLUE, 0.5)]

def handw(text, red=True):
    return Paragraph(f"✎ {text}", S_HANDW if red else S_HANDW_BLK)

def latin(text):
    return Paragraph(f"[{text}]", S_LATIN)

def table_default_style(rows_header=1):
    return TableStyle([
        ("BACKGROUND", (0,0), (-1, rows_header-1), DARK_BLUE),
        ("TEXTCOLOR",  (0,0), (-1, rows_header-1), white),
        ("FONTNAME",   (0,0), (-1, rows_header-1), "Helvetica-Bold"),
        ("FONTSIZE",   (0,0), (-1, rows_header-1), 8),
        ("ROWBACKGROUNDS", (0, rows_header), (-1,-1), [white, SECTION_BG]),
        ("FONTNAME",   (0, rows_header), (-1,-1), "Helvetica"),
        ("FONTSIZE",   (0, rows_header), (-1,-1), 8),
        ("GRID",       (0,0), (-1,-1), 0.4, HexColor("#aaaaaa")),
        ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING",(0,0), (-1,-1), 4),
        ("RIGHTPADDING",(0,0), (-1,-1), 4),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING",(0,0), (-1,-1), 3),
    ])


# ── Page template (header + footer) ──────────────────────────────────────────
class PageNumCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decoration(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_decoration(self, total_pages):
        page_num = self._pageNumber
        # Header line
        self.setStrokeColor(MID_BLUE)
        self.setLineWidth(0.7)
        self.line(MARGIN, PAGE_H - MARGIN + 4*mm, PAGE_W - MARGIN, PAGE_H - MARGIN + 4*mm)
        # Header left
        self.setFont("Helvetica-Bold", 7.5)
        self.setFillColor(DARK_BLUE)
        self.drawString(MARGIN, PAGE_H - MARGIN + 5*mm, "TREUENFELS YAMAMOTO Rechtsanwälte PartmbB")
        # Header right
        self.setFont("Helvetica", 7.5)
        self.setFillColor(grey)
        self.drawRightString(PAGE_W - MARGIN, PAGE_H - MARGIN + 5*mm, "TY-2026-RHEINGOLD-001 | VERTRAULICH")
        # Footer line
        self.setStrokeColor(MID_BLUE)
        self.line(MARGIN, MARGIN - 3*mm, PAGE_W - MARGIN, MARGIN - 3*mm)
        # Footer
        self.setFont("Helvetica", 7)
        self.setFillColor(grey)
        self.drawString(MARGIN, MARGIN - 6*mm, "Meissner Rheinwerk AG – Projekt RHEINGOLD 2030 | Vertraulich – Anwaltliches Beratungsgeheimnis")
        self.drawCentredString(PAGE_W/2, MARGIN - 6*mm, f"Seite {page_num} / {total_pages}")
        self.drawRightString(PAGE_W - MARGIN, MARGIN - 6*mm, "© Treuenfels Yamamoto PartmbB 2026 – Nur für interne Zwecke")
        # Gold bar top
        self.setFillColor(RHEIN_GOLD)
        self.rect(MARGIN, PAGE_H - MARGIN + 8*mm, PAGE_W - 2*MARGIN, 1.5*mm, stroke=0, fill=1)


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION BUILDERS
# ═══════════════════════════════════════════════════════════════════════════════

def build_cover():
    """1. Aktendeckel"""
    elems = []
    elems.append(sp(30))

    # ASCII Art TY Logo with Sakura + Rheinwelle
    logo = """
    ████████╗██╗   ██╗
       ██╔══╝╚██╗ ██╔╝
       ██║    ╚████╔╝
       ██║     ╚██╔╝          ✿  ≋≋≋≋≋ RHEIN ≋≋≋≋≋  ✿
       ██║      ██║        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       ╚═╝      ╚═╝     ≈≈≈≈≈≈≈≈≈≈ TREUENFELS YAMAMOTO ≈≈≈≈≈≈≈≈≈≈
    """
    elems.append(Paragraph("<pre>" + logo + "</pre>", S_MONO))
    elems.append(sp(8))

    elems.append(SakuraLine())
    elems.append(sp(12))

    elems.append(Paragraph("TREUENFELS YAMAMOTO", S_TITLE_BIG))
    elems.append(Paragraph("Rechtsanwälte Partnerschaft mbB", S_TITLE_MED))
    elems.append(Paragraph("トロイエンフェルス・ヤマモト法律事務所", S_TITLE_GOLD))
    elems.append(sp(6))
    elems.append(Paragraph("Königsallee 92 &#183; 40212 Düsseldorf &#183; Büro Kyoto: Gion-Higashi, Shijō-dōri, 605-0073", S_CENTER))
    elems.append(sp(20))

    elems.append(RheinGoldBar(height=3))
    elems.append(sp(10))

    elems.append(Paragraph("TESTAKTE", make_style("cv1", fontName="Helvetica-Bold", fontSize=28, leading=34, alignment=TA_CENTER, textColor=RHEIN_GOLD)))
    elems.append(sp(6))
    elems.append(Paragraph("BETRIEBLICHE ALTERSVERSORGUNG – GROßMANDAT", S_TITLE_MED))
    elems.append(sp(12))

    # Mandate box
    data = [
        ["Mandantin:", "MEISSNER RHEINWERK AG"],
        ["", "MDAX-notierter Spezialchemie-Konzern"],
        ["Sitz:", "Düsseldorf-Reisholz"],
        ["Mitarbeiter weltweit:", "14.800 (DE 6.200)"],
        ["Projekt:", "RHEINGOLD 2030"],
        ["Aktenzeichen Kanzlei:", "TY-2026-RHEINGOLD-001"],
        ["ArbG Düsseldorf:", "7 BV 412/26"],
        ["LAG Düsseldorf:", "14 TaBV 88/26"],
        ["BaFin:", "VA 31-Q 5232-2026/0014"],
        ["PSVaG:", "2026/A-RW-MEISSNER-008842"],
        ["Streitwert / Projektvolumen:", "EUR 18.000.000 (Beratungsbudget); DBO EUR 3,2 Mrd."],
        ["Angelegt:", "14.01.2026"],
        ["Federführung:", "Prof. Dr. Adalbert von Sompeh-Ostermann, LL.M. (Oxford)"],
        ["", "Fachanwalt f. Arbeitsrecht &#183; Honorarprof. Univ. Köln"],
        ["Co-Partner:", "Dr. Dr. Hartwig Treuenfels-Ostermann (Senior Partner)"],
        ["Kyoto:", "Yuki Yamamoto-Brennecke, bengoshi-Tokyo / RAin Düsseldorf"],
        ["VERTRAULICHKEIT:", "§ 203 StGB &#183; Anwaltliches Beratungsgeheimnis"],
    ]
    tbl = Table(data, colWidths=[5*cm, 10.5*cm])
    tbl.setStyle(TableStyle([
        ("FONTNAME", (0,0), (0,-1), "Helvetica-Bold"),
        ("FONTNAME", (1,0), (1,-1), "Helvetica"),
        ("FONTSIZE", (0,0), (-1,-1), 9),
        ("LEADING",  (0,0), (-1,-1), 13),
        ("BACKGROUND", (0,0), (-1,0), LIGHT_BLUE),
        ("TEXTCOLOR", (0,11), (-1,11), DARK_BLUE),
        ("FONTNAME",  (0,11), (-1,11), "Helvetica-Bold"),
        ("TEXTCOLOR", (0,-1), (-1,-1), HANDW_RED),
        ("FONTNAME",  (0,-1), (-1,-1), "Helvetica-Bold"),
        ("BOX",      (0,0), (-1,-1), 1.2, DARK_BLUE),
        ("INNERGRID",(0,0), (-1,-1), 0.4, HexColor("#cccccc")),
        ("LEFTPADDING",(0,0),(-1,-1),6),
        ("RIGHTPADDING",(0,0),(-1,-1),6),
        ("TOPPADDING",(0,0),(-1,-1),3),
        ("BOTTOMPADDING",(0,0),(-1,-1),3),
    ]))
    elems.append(tbl)
    elems.append(sp(14))
    elems.append(SakuraLine())
    elems.append(sp(8))
    elems.append(Paragraph("STRENG VERTRAULICH – NUR FÜR BERECHTIGTE EMPFÄNGER", S_WARN))
    elems.append(Paragraph("Diese Akte enthält mandatsrelevante Informationen, die dem anwaltlichen Beratungsgeheimnis unterliegen.", S_SMALL_GRAY))
    elems.append(PageBreak())
    return elems


def build_toc():
    """2. Inhaltsverzeichnis (3-4 Seiten)"""
    elems = []
    elems += section_header("INHALTSVERZEICHNIS", "Projekt RHEINGOLD 2030 &#183; TY-2026-RHEINGOLD-001")
    elems.append(Paragraph("Stand: 30.04.2026 | Letzte Aktualisierung: Beerbohm-Sittler/Pfaffenhausen-Quasthoff", S_SMALL_GRAY))
    elems.append(sp(6))
    elems.append(Paragraph("<i>Hinweis: Verweise auf Sonderakte I (Gerichtsvollstrecker) und Sonderakte II (Versicherungsvertrag) sind gesondert aufgeführt. Querverweise in eckigen Klammern [Bl. x] beziehen sich auf Blattnummern der physischen Akte, die in dieser digitalen Version nicht vollständig abgebildet sind.</i>", S_BODY_SM))
    elems.append(sp(8))

    def toc_cat(title):
        return Paragraph(title, S_TOC_CAT)

    def toc_entry(num, title, bl, note=""):
        n = f"<b>{num}</b>"
        t = title
        b = f"<font color='#2e4fa3'>[Bl. {bl}]</font>"
        x = f" <i><font color='#888888'>{note}</font></i>" if note else ""
        return Paragraph(f"{n} &nbsp;&nbsp; {t} {b}{x}", S_TOC_ENTRY)

    cats = [
        ("A. MANDATSDOKUMENTE", [
            ("A-1", "Aktendeckel & Mandatsübersicht", "1-2"),
            ("A-2", "Inhaltsverzeichnis (dieses Dokument)", "3-6"),
            ("A-3", "Engagement Letter 14.01.2026 (Retainer EUR 450.000)", "7-9"),
            ("A-4", "Conflict Check Memo (intern, Randnotizen Yamamoto-Brennecke)", "10-11"),
            ("A-5", "Prozessvollmacht / Power of Attorney", "12-13"),
            ("A-6", "Project Charter RHEINGOLD 2030 (Vorstandsbeschluss)", "14-22"),
        ]),
        ("B. PENSIONSRECHTLICHE KERNANALYSE – DEUTSCHLAND", [
            ("B-1", "Status-Memo Pensionsverbindlichkeiten DE (Albrecht-Niermann)", "23-29"),
            ("B-2", "Versorgungsordnungs-Inventory 1973–2008 (12 Seiten)", "30-42"),
            ("B-3", "Drei-Stufen-Theorie-Gutachten (Prof. von Sompeh-Ostermann, 14 Seiten)", "43-57"),
            ("B-4", "CTA-Treuhandvertrag-Entwurf (Doppeltreuhand, 16 Seiten Volltext)", "58-74"),
            ("B-5", "Pension Buyout Term Sheet (Hanseatica LV AG / Nippon Pension Anstalt)", "75-80"),
        ]),
        ("C. PSVaG UND AUFSICHTSRECHT", [
            ("C-1", "PSVaG Mahnschreiben 22.03.2026", "81-82", "(vgl. K-PSV-3)"),
            ("C-2", "Stellungnahme Treuenfels Yamamoto 09.04.2026", "83-86"),
            ("C-3", "PSVaG Erwiderung 28.04.2026", "87-88"),
            ("C-4", "BaFin-Schriftsatz VA 31-Q 5232-2026/0014", "89-90", "(vgl. Sonderakte II, Bl. 1-44)"),
            ("C-5", "PSVaG Beitragstabelle & Berechnungsgrundlagen", "91", "(K-PSV-12, vgl. Sonderakte II)"),
        ]),
        ("D. EINIGUNGSSTELLE / BESCHLUSSVERFAHREN", [
            ("D-1", "Antrag GBR (Plöger Maibach, Köln) ArbG Düsseldorf 7 BV 412/26", "92-94"),
            ("D-2", "Erwiderung Treuenfels Yamamoto", "95-98"),
            ("D-3", "Beschluss Einsetzung / Vorsitz Dr. Wupperhain-Stein", "99-100"),
            ("D-4", "Sitzungsprotokoll 1 Einigungsstelle 12.03.2026 (inkl. Fax-Block)", "101-103"),
            ("D-5", "Sitzungsprotokoll 2 Einigungsstelle 26.03.2026", "104-105"),
            ("D-6", "Sitzungsprotokoll 3 Einigungsstelle 14.04.2026", "106-107"),
            ("D-7", "LAG Düsseldorf 14 TaBV 88/26 – Beschwerdeschrift", "108-110"),
            ("D-8", "Sozialplan-Entwurf Pensions-Bestandteile (10 Seiten)", "111-121"),
        ]),
        ("E. KYOTO-MODUL – JAPAN", [
            ("E-1", "Memo Migration DB→DC Japan (bilingual DE/JP, Yamamoto-Brennecke)", "122-128"),
            ("E-2", "Anwaltskorrespondenz Tokyo District Court 令和8年(ワ)第4421号", "129-131"),
            ("E-3", "Anlagen K-JP-1 bis K-JP-31 (Auszüge; vollständig Sonderakte III)", "132", "(K-JP-14 bis K-JP-31 vgl. Sonderakte III)"),
        ]),
        ("F. US-MODUL – ERISA / PBGC", [
            ("F-1", "Memo Holcombe Pratchett & Lieberman LLP (HPL-2026-MRW-0007)", "133-138"),
            ("F-2", "401(k) Plan-Amendment-Entwurf (US-Tochter)", "139-143"),
            ("F-3", "PBGC Korrespondenz (k.A. – vgl. Sonderakte IV)", "144", "(Sonderakte IV)"),
        ]),
        ("G. UK-MODUL – SECTION 75 / TPR", [
            ("G-1", "Memo Pemberton Hawkesworth Solicitors (Section 75 Employer Debt)", "145-149"),
            ("G-2", "TPR Clearance-Strategie", "150-152"),
        ]),
        ("H. M&A – CARVE-OUT RHEINORGANICS / ALBION BRIDGE", [
            ("H-1", "M&A-Pension-Annex zum SPA (Albion Bridge Capital Partners LLP)", "153-171"),
            ("H-2", "Pension Schedule (K-MA-1 bis K-MA-28, Auszug)", "172-175", "(vollst. K-MA-8 ff. Sonderakte V)"),
            ("H-3", "Pension W&I-Versicherungsbedingungen (Auszug)", "176-178"),
        ]),
        ("I. KORRESPONDENZ UND INTERNE DOKUMENTE", [
            ("I-1", "E-Mail-Kette Vorstand ↔ Kanzlei (10 Seiten, Jan.–Apr. 2026)", "179-189"),
            ("I-2", "Handschriftliche Notizen Prof. von Sompeh-Ostermann (3 Seiten)", "190-193"),
            ("I-3", "Stundenaufstellung Treuenfels Yamamoto Jan.–Apr. 2026", "194-198"),
        ]),
        ("J. ANLAGENVERZEICHNIS", [
            ("J-1", "Anlagenverzeichnis K-VO-1–47, K-CTA-1–22, K-PSV-1–18", "199-201"),
            ("J-2", "Anlagenverzeichnis K-JP-1–31, K-US-1–16, K-UK-1–11, K-MA-1–28", "202-204"),
        ]),
    ]

    for cat_title, entries in cats:
        elems.append(toc_cat(cat_title))
        for entry in entries:
            if len(entry) == 4:
                elems.append(toc_entry(entry[0], entry[1], entry[2], entry[3]))
            else:
                elems.append(toc_entry(entry[0], entry[1], entry[2]))
        elems.append(sp(3))

    elems.append(sp(10))
    elems.append(hr(RHEIN_GOLD))
    elems.append(Paragraph("<b>Sonderakten (separat geführt, nicht in diesem PDF):</b>", S_H4))
    sonder = [
        "Sonderakte I:   Gerichtsvollstrecker / Zwangsvollstreckung (nicht relevant für bAV)",
        "Sonderakte II:  BaFin-Unterlagen und Versicherungsverträge Hanseatica LV AG",
        "Sonderakte III: Japan – Vollständige K-JP-Belege, MHLW-Genehmigungsunterlagen",
        "Sonderakte IV:  USA – PBGC-Korrespondenz, ERISA-Volltext-Unterlagen",
        "Sonderakte V:   M&A-Datenraum Albion Bridge Capital Partners (vertraulich)",
        "Sonderakte VI:  Führungskräfte-Sonderzusagen FK-001 bis FK-047 (besonders vertraulich)",
    ]
    for s in sonder:
        elems.append(Paragraph(s, S_MONO))
    elems.append(PageBreak())
    return elems


def build_engagement_letter():
    """3. Engagement Letter"""
    elems = []
    elems += section_header("ENGAGEMENT LETTER", "Treuenfels Yamamoto PartmbB an Meissner Rheinwerk AG &#183; 14.01.2026")

    # Briefkopf
    elems.append(Paragraph("TREUENFELS YAMAMOTO Rechtsanwälte Partnerschaft mbB", S_H2))
    elems.append(Paragraph("Königsallee 92 &#183; 40212 Düsseldorf &#183; Tel.: +49 211 9200-100 &#183; Fax: +49 211 9200-199", S_NORMAL))
    elems.append(Paragraph("E-Mail: rheingold-team@ty-law.de &#183; www.ty-law.de &#183; USt-IdNr.: DE 312 884 719", S_NORMAL))
    elems.append(hr())
    elems.append(sp(6))

    elems.append(Paragraph("Düsseldorf, den 14. Januar 2026", S_NORMAL))
    elems.append(sp(6))
    elems.append(Paragraph("<b>An:</b>", S_NORMAL))
    elems.append(Paragraph("MEISSNER RHEINWERK AG", S_BODY))
    elems.append(Paragraph("z.Hd. Herrn Dipl.-Kfm. Henrick Otterbach-Veltheim, CFO", S_BODY))
    elems.append(Paragraph("und Dr. Constanze Brindeau-Lorbach, HR-Vorstand", S_BODY))
    elems.append(Paragraph("Rheinwerkallee 1 &#183; 40589 Düsseldorf-Reisholz", S_BODY))
    elems.append(sp(8))

    elems.append(Paragraph("<b>Betreff: Mandatsbestätigung Projekt RHEINGOLD 2030 – Konzernweite bAV-Restrukturierung</b>", S_H3))
    elems.append(Paragraph("<b>Unser Zeichen: TY-2026-RHEINGOLD-001</b>", S_NORMAL))
    elems.append(sp(8))

    body = """Sehr geehrter Herr Otterbach-Veltheim, sehr geehrte Frau Dr. Brindeau-Lorbach,

wir freuen uns, das Mandat zur rechtlichen Begleitung des Projekts RHEINGOLD 2030 zu übernehmen und bestätigen die in unserem Gespräch vom 08.01.2026 vereinbarten Konditionen hiermit schriftlich.

<b>I. Mandatsumfang</b>

Das Mandat umfasst die umfassende rechtliche Begleitung der konzernweiten Restrukturierung der betrieblichen Altersversorgung (bAV) der Meissner Rheinwerk AG und ihrer Tochtergesellschaften, insbesondere:

(1) Schließung der leistungsorientierten Versorgungssysteme (Defined Benefit, &#8222;DB") in Deutschland mit Stopp des Future Service bei Erhalt der Past-Service-Anwartschaften, unter Wahrung der Drei-Stufen-Rechtsprechung des BAG (GS 1/82, 3 AZR 392/06, 3 AZR 540/16);

(2) Begleitung des Pensionsbuyout-Prozesses für die deutschen Rentnerbestände (ca. 4.300 Rentner, DBO ca. EUR 780 Mio.) mit dem vorgesehenen Versicherer, ggf. Gruppenrentenversicherung gemäß §§ 1b Abs. 2 BetrAVG i.V.m. VAG;

(3) Errichtung und Überprüfung des doppelseitigen CTA-Treuhandverhältnisses unter insolvenzrechtlichen Gesichtspunkten (BAG 3 AZR 18/12) sowie Koordination mit dem CTA Rheinland Trust e.V.;

(4) Verhandlungsführung mit dem Gesamtbetriebsrat im Beschlussverfahren ArbG Düsseldorf 7 BV 412/26 und Begleitung der Einigungsstelle gemäß § 76 BetrVG;

(5) Koordination mit unseren Korrespondenzpartnern für das UK-Modul (Pemberton Hawkesworth Solicitors, London), das US-Modul (Holcombe Pratchett & Lieberman LLP, Boston) und die japanische Umstellung (Büro Kyoto, Yamamoto-Brennecke);

(6) Pension-Annex-Verhandlungen im Rahmen des Carve-out der Sparte RHEINORGANICS (Albion Bridge Capital Partners LLP), insbesondere Ausarbeitung der Pension Warranties und Pension Indemnities im SPA;

(7) Begleitung BaFin-Verfahren VA 31-Q 5232-2026/0014 (Pensionsfonds-Erweiterung) sowie PSVaG-Korrespondenz;

(8) Laufende IAS-19-rechtliche Begleitung (Counsel Albrecht-Niermann) und steuerliche Begleitung §§ 4d, 6a EStG (Counsel Dr. Engelhart-Volz).
"""
    for para in body.split("\n\n"):
        if para.strip():
            elems.append(P(para.strip()))
            elems.append(sp(4))

    elems.append(P("""<b>II. Vergütung und Retainer</b>

Die vereinbarten Stundensätze betragen:
"""))

    fee_data = [
        ["Funktion", "Standort", "Stundensatz", "Bemerkung"],
        ["Partner", "Düsseldorf", "EUR 980,00", "zzgl. USt."],
        ["Counsel", "Düsseldorf", "EUR 720,00", "zzgl. USt."],
        ["Senior Associate", "Düsseldorf", "EUR 520,00", "zzgl. USt."],
        ["Associate", "Düsseldorf", "EUR 380,00", "zzgl. USt."],
        ["Trainee", "Düsseldorf", "EUR 220,00", "zzgl. USt."],
        ["Bengoshi (Partner)", "Kyoto", "JPY 92.000,00", "ca. EUR 560/h bei 1:164"],
        ["Senior Associate", "Kyoto", "JPY 58.000,00", "ca. EUR 354/h"],
    ]
    tbl = Table(fee_data, colWidths=[4.5*cm, 3*cm, 3.5*cm, 4.5*cm])
    tbl.setStyle(table_default_style())
    elems.append(tbl)
    elems.append(sp(6))

    elems.append(P("""Es wird ein monatlicher Retainer in Höhe von <b>EUR 450.000,00 netto</b> (zzgl. USt.) für die Dauer von zunächst 12 Monaten vereinbart, abzurechnen zum 1. eines jeden Monats. Darüber hinausgehende Stunden werden gesondert abgerechnet.

<b>Fee Cap-Diskussion:</b> Im Gespräch vom 08.01.2026 wurde ein Gesamtbudget von EUR 18 Mio. (Beratungskosten gesamt, alle Berater) diskutiert. Wir haben darauf hingewiesen, dass ein fester Fee Cap für die Kanzlei angesichts der Komplexität und der Vielzahl der Einzelmodule (DE, JP, UK, US, M&A) nicht sachgerecht erscheint. Wir schlagen vor, nach sechs Monaten eine gemeinsame Budget-Review durchzuführen.

<b>III. Conflict-Cleared-Erklärung</b>

Wir haben unsere Mandate gegenüber potenziellen Gegenparteien geprüft. Wir bestätigen: Es besteht kein Interessenkonflikt gegenüber den Bietern Hanseatica Lebensversicherung AG und Nippon Pension Anstalt KK. Ein früheres Beratungsmandat für die Hanseatica LV AG wurde mit Ablauf des 31.12.2025 vollständig beendet (vgl. Conflict Check Memo A-4). Gegenüber Albion Bridge Capital Partners LLP besteht kein Vormandat.

<b>IV. Datenschutz und Vertraulichkeit</b>

Alle im Rahmen des Mandats verarbeiteten personenbezogenen Daten (insbesondere Arbeitnehmerdaten aus der Versorgungsordnungs-Datenbank und Sonderzusagen FK-001 bis FK-047) werden ausschließlich zur Mandatsbearbeitung verwendet. Die Kanzlei unterhält ein zertifiziertes Datenschutz-Managementsystem (ISO 27001:2022). Datenschutzrechtlich Verantwortlicher im Sinne der DSGVO für die Kanzleisysteme ist Herr Maximilian Pfaffenhausen-Quasthoff.

Mit freundlichen Grüßen

TREUENFELS YAMAMOTO Rechtsanwälte Partnerschaft mbB
"""))

    elems.append(sp(12))
    elems.append(Paragraph("_____________________________     _____________________________", S_NORMAL))
    elems.append(Paragraph("Prof. Dr. Adalbert von Sompeh-Ostermann     Dr. Dr. Hartwig Treuenfels-Ostermann", S_NORMAL))
    elems.append(Paragraph("(Federführender Partner)                   (Senior Partner)", S_NORMAL))
    elems.append(sp(6))
    elems.append(Paragraph("Gegengezeichnet für Meissner Rheinwerk AG:", S_NORMAL))
    elems.append(sp(12))
    elems.append(Paragraph("_____________________________     _____________________________", S_NORMAL))
    elems.append(Paragraph("Dipl.-Kfm. Henrick Otterbach-Veltheim     Dr. Constanze Brindeau-Lorbach", S_NORMAL))
    elems.append(Paragraph("(CFO)                                      (HR-Vorstand)", S_NORMAL))
    elems.append(PageBreak())
    return elems


def build_conflict_check():
    """4. Conflict Check Memo"""
    elems = []
    elems += section_header("CONFLICT CHECK MEMO", "Intern &#183; Treuenfels Yamamoto PartmbB &#183; Streng Vertraulich")
    elems.append(Paragraph("INTERNES DOKUMENT – NICHT AN MANDANTEN WEITERZUGEBEN", S_WARN))
    elems.append(sp(6))

    meta = [
        ["Erstellt:", "14.01.2026"],
        ["Von:", "Kanzlei-Compliance / Pfaffenhausen-Quasthoff"],
        ["Geprüft:", "Yuki Yamamoto-Brennecke (Kyoto)"],
        ["Aktenzeichen:", "TY-2026-RHEINGOLD-001-CONFLICT"],
        ["Mandat:", "Meissner Rheinwerk AG – Projekt RHEINGOLD 2030"],
    ]
    tbl = Table(meta, colWidths=[4*cm, 11*cm])
    tbl.setStyle(TableStyle([
        ("FONTNAME", (0,0),(0,-1), "Helvetica-Bold"),
        ("FONTNAME", (1,0),(1,-1), "Helvetica"),
        ("FONTSIZE", (0,0),(-1,-1), 9),
        ("LEADING", (0,0),(-1,-1), 13),
        ("GRID", (0,0),(-1,-1), 0.4, grey),
        ("LEFTPADDING",(0,0),(-1,-1),4),
        ("RIGHTPADDING",(0,0),(-1,-1),4),
        ("TOPPADDING",(0,0),(-1,-1),2),
        ("BOTTOMPADDING",(0,0),(-1,-1),2),
    ]))
    elems.append(tbl)
    elems.append(sp(8))

    elems.append(Paragraph("I. Geprüfte Gegenparteien / Involvierte Parteien", S_H3))
    conflict_data = [
        ["Partei", "Verhältnis zum Mandat", "Frühere Mandate", "Ergebnis"],
        ["Hanseatica LV AG, Hamburg", "Kaufinteressent Pensionsbuyout", "Beratungsmandat bis 31.12.2025 (abgelaufen)", "CLEARED – Cooling-Off 12 Monate abgelaufen"],
        ["Nippon Pension Anstalt KK", "Bieter Buyout JP", "Kein Vormandat", "CLEARED"],
        ["Albion Bridge Capital Partners LLP", "PE-Investor RHEINORGANICS", "Kein Vormandat", "CLEARED"],
        ["Plöger Maibach RA, Köln", "GBR-Gegenkanzlei", "Kein Vormandat", "CLEARED"],
        ["Holcombe Pratchett & Lieberman LLP", "Korrespondenzpartner US", "Referral-Verhältnis", "CLEARED (kein Konflikt)"],
        ["Pemberton Hawkesworth Sol.", "Korrespondenzpartner UK", "Joint Venture-Arbeit 2023", "CLEARED"],
        ["PSVaG Pensions-Sicherungs-Verein", "Behörde", "n/a", "CLEARED"],
        ["BaFin", "Aufsichtsbehörde", "n/a", "CLEARED"],
        ["IG BCE / GBR Meissner", "Verhandlungspartner", "n/a", "CLEARED – kein Mandat für GBR"],
    ]
    tbl2 = Table(conflict_data, colWidths=[3.5*cm, 4.5*cm, 4*cm, 3.5*cm])
    tbl2.setStyle(table_default_style())
    elems.append(tbl2)
    elems.append(sp(6))

    elems.append(Paragraph("II. Hanseatica-Cooling-Off-Analyse", S_H3))
    elems.append(P("""Das Vormandat für die Hanseatica Lebensversicherung AG (Mandat HLV-2024-RÜCK, Rückversicherungsgestaltung) endete zum 31.12.2025. Gemäß Kanzleistandards gilt eine Cooling-Off-Frist von sechs Monaten für Counsel-Level-Beteiligte und zwölf Monate für Partner. Partnerschaftlich tätige Personen waren Dr. Treuenfels-Ostermann (als Senior Partner, nicht am HLV-Mandat beteiligt) sowie Counsel Albrecht-Niermann (war am HLV-Mandat nicht beteiligt). Am Vormandat tätig war Counsel Dr. Roman Engelhart-Volz für steuerliche Fragestellungen; dieser wird im RHEINGOLD-Mandat ausschließlich für deutsche Steuergestaltung tätig und hat keinen Einblick in die Buyout-Bewertungsunterlagen von Hanseatica.
"""))
    elems.append(handw("Yuki: Ich habe mit Herrn Engelhart-Volz persönlich gesprochen – er setzt eine Chinese Wall! Das reicht nach unseren Regeln. — Y.Y.-B."))
    elems.append(sp(6))
    elems.append(Paragraph("III. Ergebnis", S_H3))
    elems.append(P("Es bestehen <b>keine Interessenkonflikte</b>, die einer Mandatsannahme entgegenstehen. Das Mandat kann unter Einhaltung der Chinese-Wall-Vereinbarung für Counsel Dr. Engelhart-Volz in Bezug auf Hanseatica-Unterlagen angenommen werden."))
    elems.append(sp(4))
    elems.append(handw("A.v.S.-O. handschriftl.: ‚Engelhart separat halten – er soll BaFin machen, NICHT Hanseatica due diligence. Klar? — A.' (Rotes Unterstreichen in Originalakte)"))
    elems.append(sp(4))
    elems.append(Paragraph("Genehmigt: Prof. Dr. Adalbert von Sompeh-Ostermann / Dr. Dr. Hartwig Treuenfels-Ostermann / 14.01.2026", S_NORMAL))
    elems.append(PageBreak())
    return elems


def build_poa():
    """5. Prozessvollmacht"""
    elems = []
    elems += section_header("PROZESSVOLLMACHT / POWER OF ATTORNEY", "Meissner Rheinwerk AG an Treuenfels Yamamoto PartmbB")
    elems.append(sp(6))
    elems.append(Paragraph("PROZESSVOLLMACHT", make_style("poa1", fontName="Helvetica-Bold", fontSize=16, alignment=TA_CENTER, textColor=DARK_BLUE)))
    elems.append(sp(10))
    elems.append(P("""Die <b>MEISSNER RHEINWERK AG</b>, Rheinwerkallee 1, 40589 Düsseldorf-Reisholz, eingetragen im Handelsregister des Amtsgerichts Düsseldorf unter HRB 48 719, vertreten durch den Vorstand, dieser vertreten durch den Vorsitzenden des Aufsichtsrats, erteilt hiermit

<b>TREUENFELS YAMAMOTO Rechtsanwälte Partnerschaft mbB</b>,
Königsallee 92, 40212 Düsseldorf,
vertreten durch Prof. Dr. Adalbert von Sompeh-Ostermann, LL.M. (Oxford),
Dr. Dr. Hartwig Treuenfels-Ostermann,
Yuki Yamamoto-Brennecke (bengoshi + RAin),
Friederike Albrecht-Niermann (Counsel),
Dr. Roman Engelhart-Volz (Counsel, Tax),
Maximilian Pfaffenhausen-Quasthoff (Senior Associate),
Annika Beerbohm-Sittler (Senior Associate),
sowie allen unter der Kanzlei zugelassenen Rechtsanwälten und Rechtsanwältinnen

<b>GENERAL-PROZESSVOLLMACHT</b>

in allen Rechts- und Verwaltungsangelegenheiten im Zusammenhang mit dem Projekt RHEINGOLD 2030, insbesondere in den Verfahren:

• ArbG Düsseldorf 7 BV 412/26 (Einigungsstellen-Beschlussverfahren)
• LAG Düsseldorf 14 TaBV 88/26 (Beschwerde)
• BAG 3 ABR 14/27 (Rechtsbeschwerde, angekündigt)
• BaFin VA 31-Q 5232-2026/0014
• PSVaG-Verfahren 2026/A-RW-MEISSNER-008842

sowie in allen damit in Zusammenhang stehenden Nebenverfahren, Schiedsverfahren und behördlichen Verfahren in Deutschland.

Die Bevollmächtigten sind berechtigt zu allen Prozesshandlungen einschließlich Klageerhebung, Klagerücknahme, Abschluss von Vergleichen, Rechtsmittelverzicht, Empfang von Zustellungen und Erteilung von Untervollmachten.

<b>Diese Vollmacht gilt bis auf Widerruf.</b>

Düsseldorf, den 14. Januar 2026
"""))
    elems.append(sp(14))
    elems.append(Paragraph("_____________________________", S_CENTER))
    elems.append(Paragraph("MEISSNER RHEINWERK AG", S_CENTER_B))
    elems.append(Paragraph("Dipl.-Kfm. Henrick Otterbach-Veltheim (CFO)", S_CENTER))
    elems.append(Paragraph("Dr. Constanze Brindeau-Lorbach (HR-Vorstand)", S_CENTER))
    elems.append(sp(8))
    elems.append(Paragraph("[Notarielle Beglaubigung liegt vor – Original in Sonderakte I]", S_SMALL_GRAY))
    elems.append(PageBreak())
    return elems


def build_project_charter():
    """6. Project Charter RHEINGOLD 2030"""
    elems = []
    elems += section_header("PROJECT CHARTER &#8222;RHEINGOLD 2030&#8221;", "Vorstandsbeschluss-Abschrift &#183; Meissner Rheinwerk AG &#183; 12.01.2026")
    elems.append(Paragraph("VERTRAULICH – NUR FÜR STEUERUNGSKREIS-MITGLIEDER", S_WARN))
    elems.append(sp(6))

    elems.append(P("""<b>Vorstandsbeschluss vom 12. Januar 2026 (Umlaufbeschluss)</b>

Der Vorstand der Meissner Rheinwerk AG beschließt einstimmig die Einleitung des Transformationsprojekts <b>RHEINGOLD 2030</b> zur konzernweiten Restrukturierung der betrieblichen Altersversorgung (bAV). Der Beschluss ist gemäß § 77 Abs. 2 AktG i.V.m. der Geschäftsordnung des Vorstands ordnungsgemäß zustande gekommen.

<b>§ 1 Projektziele</b>

(1) Risikoreduzierung: Die DBO des Konzerns beläuft sich laut IAS-19-Bewertung 2024 auf EUR 3,2 Mrd. (DE: EUR 2,4 Mrd., UK: EUR 220 Mio., JP: EUR 310 Mio., sonstige: EUR 270 Mio.). Ziel ist eine Reduzierung der bilanziellen Pensionsverbindlichkeiten um mindestens 65 % innerhalb von 4 Jahren.

(2) Schließung des deutschen DB-Systems: Stopp des Future Service für alle aktiven Anwärter zum nächstmöglichen rechtlich zulässigen Zeitpunkt (voraussichtlich 01.01.2027 nach Einigungsstellen-Abschluss), Erhalt der erdienten Anwartschaften.

(3) Buyout der deutschen Rentnerbestände (ca. 4.300 Rentner, Einmalbeitrag geschätzt EUR 780 Mio.) durch Gruppenrentenversicherung.

(4) CTA-Sicherung der verbleibenden Past-Service-Verpflichtungen (EUR 1,62 Mrd. nach Buyout) über doppelseitigen Treuhandvertrag.

(5) DB→DC-Umstellung der japanischen Tochter マイスナー・ライン化学株式会社 gemäß 確定給付企業年金法 (DB Corporate Pension Law, Art. 4 und 90ff.) und 確定拠出年金法 (DC Law).

(6) UK-DB-Schließung: Closure der Meissner Rhine Industries Ltd.-Pension (Manchester) mit Klärung Section-75-Schuld.

(7) Carve-out-Vorbereitung: Überführung der Pensionsverpflichtungen der Sparte RHEINORGANICS in transaktionstauglichen Zustand für Verkauf an Albion Bridge Capital Partners LLP.

<b>§ 2 Steuerungskreis</b>
"""))

    steering = [
        ["Funktion", "Person", "Ressort"],
        ["Projektleitung (Gesamtverantwortung)", "Dr. Constanze Brindeau-Lorbach", "HR-Vorstand"],
        ["Finance-Sponsor", "Dipl.-Kfm. Henrick Otterbach-Veltheim", "CFO"],
        ["Recht (externe Kanzlei)", "Prof. Dr. Adalbert von Sompeh-Ostermann", "Treuenfels Yamamoto"],
        ["Aktuar", "Dr. Rüdiger Hellmrich-Vogt", "Hellmrich-Vogt Aktuarpartner GmbH"],
        ["Datenschutz intern", "Dr. Petra Simons-Rademacher", "Chief Privacy Officer MR-AG"],
        ["GBR-Liaison (extern)", "RA Dr. Wolfram Plöger-Heinekamp", "Plöger Maibach RA (GBR-Seite)"],
        ["Steuer", "Dr. Roman Engelhart-Volz", "Treuenfels Yamamoto (Counsel Tax)"],
        ["IAS 19 / Bilanz", "Friederike Albrecht-Niermann", "Treuenfels Yamamoto (Counsel)"],
        ["M&A / Transaktionen", "Annika Beerbohm-Sittler", "Treuenfels Yamamoto (Senior Assoc.)"],
        ["Japan-Modul", "Yuki Yamamoto-Brennecke", "Treuenfels Yamamoto (Kyoto)"],
        ["Datenschutz (Kanzlei)", "Maximilian Pfaffenhausen-Quasthoff", "Treuenfels Yamamoto (Senior Assoc.)"],
    ]
    tbl = Table(steering, colWidths=[5.5*cm, 5.5*cm, 4.5*cm])
    tbl.setStyle(table_default_style())
    elems.append(tbl)
    elems.append(sp(8))

    elems.append(Paragraph("<b>§ 3 Meilensteinplan</b>", S_H3))
    milestones = [
        ["Meilenstein", "Beschreibung", "Zieldatum", "Status"],
        ["M-1", "Mandatierung Kanzlei / Kick-off", "14.01.2026", "Abgeschlossen"],
        ["M-2", "Versorgungsordnungs-Inventory & rechtliche Risikoanalyse", "28.02.2026", "Abgeschlossen"],
        ["M-3", "Einreichung Antrag BaFin Pensionsfonds-Erweiterung", "15.03.2026", "Abgeschlossen"],
        ["M-4", "Antrag GBR Einigungsstelle / Beschlussverfahren ArbG DUS", "01.03.2026", "Laufend"],
        ["M-5", "Term Sheet Buyout Hanseatica finalisiert", "30.04.2026", "In Verhandlung"],
        ["M-6", "CTA-Treuhandvertrag beurkundet", "30.06.2026", "Entwurf"],
        ["M-7", "Einigungsstellen-Einigung / Sozialplan Pension", "31.07.2026", "Offen"],
        ["M-8", "SPA-Unterzeichnung RHEINORGANICS / Albion Bridge", "30.09.2026", "Due Diligence"],
        ["M-9", "Buyout-Abschluss Hanseatica (Financial Close)", "31.12.2026", "Offen"],
        ["M-10", "Japan DC-Genehmigung MHLW", "31.03.2027", "Offen"],
        ["M-11", "Future-Service-Stopp DE (Wirksamkeit)", "01.01.2027", "Offen"],
        ["M-12", "UK Section-75-Clearance TPR", "30.06.2027", "Offen"],
        ["M-13", "Abschluss RHEINGOLD 2030", "31.12.2030", "Langfristig"],
    ]
    tbl2 = Table(milestones, colWidths=[1.5*cm, 6.5*cm, 2.8*cm, 2.7*cm])
    tbl2.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), DARK_BLUE),
        ("TEXTCOLOR",  (0,0), (-1,0), white),
        ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",   (0,0), (-1,0), 8),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [white, SECTION_BG]),
        ("FONTNAME",   (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",   (0,1), (-1,-1), 7.5),
        ("GRID",       (0,0), (-1,-1), 0.4, grey),
        ("LEFTPADDING",(0,0),(-1,-1),3),
        ("RIGHTPADDING",(0,0),(-1,-1),3),
        ("TOPPADDING", (0,0),(-1,-1),2),
        ("BOTTOMPADDING",(0,0),(-1,-1),2),
        ("BACKGROUND", (0,4), (-1,4), HexColor("#fff8e0")),
    ]))
    elems.append(tbl2)
    elems.append(sp(6))

    elems.append(Paragraph("<b>§ 4 Budget</b>", S_H3))
    budget_data = [
        ["Budgetposition", "EUR (netto)", "Anmerkung"],
        ["Externe Rechtsberatung (alle Jurisdiktionen)", "8.500.000", "inkl. UK, US, JP"],
        ["Aktuarielle Beratung (Hellmrich-Vogt)", "950.000", ""],
        ["Buyout-Transaktionskosten", "4.200.000", "Provision, Due Diligence"],
        ["CTA-Errichtungskosten", "380.000", "inkl. Notar, Grundbuch"],
        ["M&A-Beratung RHEINORGANICS (intern allokiert)", "2.100.000", ""],
        ["Unvorhergesehenes / Reserve", "1.870.000", "10% Reserve"],
        ["GESAMT", "18.000.000", "Gesamtprojektbudget"],
    ]
    tbl3 = Table(budget_data, colWidths=[6.5*cm, 3*cm, 6*cm])
    tbl3.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), DARK_BLUE),
        ("TEXTCOLOR",  (0,0), (-1,0), white),
        ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",   (0,0), (-1,-1), 8.5),
        ("ROWBACKGROUNDS", (0,1), (-1,-2), [white, SECTION_BG]),
        ("BACKGROUND", (0,-1), (-1,-1), RHEIN_GOLD),
        ("FONTNAME",   (0,-1), (-1,-1), "Helvetica-Bold"),
        ("GRID",       (0,0), (-1,-1), 0.4, grey),
        ("ALIGN",      (1,0), (1,-1), "RIGHT"),
        ("LEFTPADDING",(0,0),(-1,-1),4),
        ("TOPPADDING", (0,0),(-1,-1),2),
        ("BOTTOMPADDING",(0,0),(-1,-1),2),
    ]))
    elems.append(tbl3)
    elems.append(sp(8))
    elems.append(P("""<b>§ 5 Berichtspflichten und Eskalation</b>

Der Steuerungskreis tagt monatlich (jeweils letzter Mittwoch des Monats, alternierend Düsseldorf / Videokonferenz mit Kyoto-Zuschaltung). Kritische Abweichungen von Meilensteinen sind unverzüglich an den HR-Vorstand zu melden. Der Vorstand wird quartalsweise durch den HR-Vorstand und den CFO informiert; halbjährliche Berichterstattung an den Aufsichtsrat-Prüfungsausschuss ist vorgesehen.

<b>§ 6 Vertraulichkeit</b>

Der Inhalt dieses Project Charter ist streng vertraulich. Eine Weitergabe an Dritte, insbesondere an die Arbeitnehmervertretung vor Einleitung des Konsultationsverfahrens oder an Presseorgane, ist untersagt. Zuwiderhandlungen können dienst- und arbeitsrechtliche Konsequenzen haben.

Beschluss gefasst am 12.01.2026. Gez. Vorstand Meissner Rheinwerk AG (Otterbach-Veltheim, Brindeau-Lorbach, Dr. Steffen Markwart-Fröhlich [CEO], Klaus-Peter Vornhagen [COO]).
"""))
    elems.append(PageBreak())
    return elems


def build_status_memo_pension():
    """7. Status-Memo Pensionsverbindlichkeiten Deutschland"""
    elems = []
    elems += section_header("STATUS-MEMO: PENSIONSVERBINDLICHKEITEN DEUTSCHLAND", "Counsel Friederike Albrecht-Niermann &#183; 20.02.2026 &#183; IAS 19 / BetrAVG")

    elems.append(P("""<b>Verfasserin:</b> Friederike Albrecht-Niermann, Counsel (IAS 19 / Bilanzrecht)
<b>An:</b> Prof. Dr. Adalbert von Sompeh-Ostermann / Dipl.-Kfm. Henrick Otterbach-Veltheim
<b>Datum:</b> 20. Februar 2026
<b>Vertraulichkeit:</b> Anwaltlich privilegiert – mandatsbezogene Korrespondenz"""))
    elems.append(sp(4))
    elems.append(handw("Frau Brindeau-Lorbach: bitte vor Aufsichtsrat herausreden! — A.v.S.-O."))
    elems.append(sp(6))

    elems.append(Paragraph("I. Ausgangslage und IAS-19-Bewertung", S_H3))
    elems.append(P("""Die Meissner Rheinwerk AG weist im Konzernabschluss 2024 (IFRS) Pensionsrückstellungen nach IAS 19 &#8222;Employee Benefits" (revised 2011, in Kraft IFRS-Fassung 2013) von insgesamt EUR 3,2 Mrd. (DBO = Defined Benefit Obligation) aus. Der überwiegende Teil entfällt mit EUR 2,4 Mrd. auf die deutschen Versorgungszusagen.

Die deutschen Verpflichtungen gehen zurück auf Versorgungsordnungen der Jahrgänge 1973, 1981, 1995 und 2008. Die Zusagen der Generationen 1973 und 1981 sind nach dem Leistungsprimat strukturiert und sehen eine Gesamtversorgung von bis zu 75 % des letzten Bruttogehalts (Gesamt­versorgungsobergrenze nach Gesamtversorgungszusage) vor. Diese Altzusagen betreffen heute überwiegend bereits Rentner sowie ältere Anwärter nahe dem Rentenalter.

Gemäß IAS 19.55 ff. ist die DBO der Barwert aller erwarteten künftigen Leistungen, die auf vergangene Dienstjahre entfallen. Der Abzinsungszinssatz richtet sich nach der Rendite hochverzinslicher Unternehmensanleihen (High Quality Corporate Bonds, AA-Rating) mit vergleichbarer Laufzeit am Bilanzstichtag. Zum 31.12.2024 wurde ein Diskontierungszinssatz von <b>3,70 % p.a.</b> (Vorjahr: 3,95 %) angesetzt, was gegenüber dem Vorjahr zu einem Anstieg der DBO um ca. EUR 142 Mio. führte.
"""))

    elems.append(Paragraph("II. IAS-19-Rollforward 2024 (Deutschland)", S_H3))
    rollforward = [
        ["Position", "2024 (EUR Mio.)", "2023 (EUR Mio.)", "Veränderung"],
        ["DBO Beginn Geschäftsjahr", "2.258", "2.395", "-137"],
        ["Current Service Cost", "48", "52", "-4"],
        ["Interest Cost (3,70 % / 3,95 %)", "84", "95", "-11"],
        ["Actuarial Losses/(Gains) – Demografie", "12", "-28", "+40"],
        ["Actuarial Losses/(Gains) – Finanziell", "145", "-198", "+343"],
        ["Benefits paid", "-147", "-158", "+11"],
        ["DBO Ende Geschäftsjahr", "2.400", "2.258", "+142"],
        ["davon: CTA-Plan-Assets", "-780", "-712", "-68"],
        ["Netto-Pensionsrückstellung (IFRS-Bilanz)", "1.620", "1.546", "+74"],
    ]
    tbl = Table(rollforward, colWidths=[6.5*cm, 2.8*cm, 2.8*cm, 2.8*cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), DARK_BLUE),
        ("TEXTCOLOR",  (0,0), (-1,0), white),
        ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",   (0,0), (-1,-1), 8.5),
        ("ROWBACKGROUNDS", (0,1), (-1,-3), [white, SECTION_BG]),
        ("BACKGROUND", (0,-2), (-1,-2), LIGHT_BLUE),
        ("BACKGROUND", (0,-1), (-1,-1), HexColor("#dff0d8")),
        ("FONTNAME",   (0,-2), (-1,-1), "Helvetica-Bold"),
        ("ALIGN",      (1,0), (-1,-1), "RIGHT"),
        ("GRID",       (0,0), (-1,-1), 0.4, grey),
        ("LEFTPADDING",(0,0),(-1,-1),4),
        ("TOPPADDING", (0,0),(-1,-1),2),
        ("BOTTOMPADDING",(0,0),(-1,-1),2),
    ]))
    elems.append(tbl)
    elems.append(sp(6))

    elems.append(Paragraph("III. Sensitivitätsanalyse Diskontierungszinssatz", S_H3))
    elems.append(P("Gemäß IAS 19.145 sind wesentliche versicherungsmathematische Annahmen offenzulegen. Die folgende Tabelle zeigt die Sensitivität der deutschen DBO gegenüber Zinssatzänderungen (alle anderen Parameter konstant):"))
    sens = [
        ["Szenario", "Diskontierungssatz", "DBO (EUR Mio.)", "Delta vs. Basis (EUR Mio.)", "Delta (%)"],
        ["Stress hoch +100 bp", "4,70 %", "2.135", "-265", "-11,0 %"],
        ["Szenario +50 bp", "4,20 %", "2.265", "-135", "-5,6 %"],
        ["BASIS", "3,70 %", "2.400", "—", "—"],
        ["Szenario -50 bp", "3,20 %", "2.548", "+148", "+6,2 %"],
        ["Stress niedrig -100 bp", "2,70 %", "2.711", "+311", "+13,0 %"],
    ]
    tbl2 = Table(sens, colWidths=[3.5*cm, 2.5*cm, 2.5*cm, 3.5*cm, 2*cm])
    tbl2.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), DARK_BLUE),
        ("TEXTCOLOR",  (0,0), (-1,0), white),
        ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",   (0,0), (-1,-1), 8.5),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [white, SECTION_BG]),
        ("BACKGROUND", (0,3), (-1,3), PALE_YELLOW),
        ("FONTNAME",   (0,3), (-1,3), "Helvetica-Bold"),
        ("ALIGN",      (1,0), (-1,-1), "RIGHT"),
        ("GRID",       (0,0), (-1,-1), 0.4, grey),
        ("LEFTPADDING",(0,0),(-1,-1),4),
        ("TOPPADDING", (0,0),(-1,-1),2),
        ("BOTTOMPADDING",(0,0),(-1,-1),2),
    ]))
    elems.append(tbl2)
    elems.append(sp(6))

    elems.append(Paragraph("IV. Steuerliche Bewertung (§ 6a EStG)", S_H3))
    elems.append(P("""Neben der IFRS-Bewertung sind die handels- und steuerrechtlichen Pensionsrückstellungen relevant. Nach § 6a EStG werden Pensionsrückstellungen nach dem Teilwertverfahren mit einem fixen Zinssatz von <b>6,0 % p.a.</b> bewertet. Infolge des Zinsgefälles (IFRS: 3,70 % vs. steuer: 6,0 %) ist die steuerliche Rückstellung erheblich niedriger als die IFRS-DBO. Die steuerliche Rückstellung der Meissner Rheinwerk AG DE beläuft sich auf ca. EUR 1,1 Mrd. (geprüfte Angabe Jahresabschluss HGB).

Hinsichtlich Dotierungsaufwand gilt § 4d EStG für die Unterstützungskasse, sofern diese genutzt wird. Der CTA-Treuhandfonds ist steuerlich als Betriebsvermögen des Arbeitgebers zu behandeln (keine steuerliche Neutralisierung möglich), jedoch insolvenzrechtlich gesichert. Counsel Dr. Engelhart-Volz analysiert die Auswirkungen des CTA auf §§ 4d, 6a EStG in separatem Tax-Memo (K-CTA-7).

<b>Empfehlung:</b> Der Buyout der Rentnerbestände führt nach § 3 Nr. 66 EStG zu steuerfreier Übertragung, wenn die Zusage auf die Hanseatica Lebensversicherung übertragen wird (§ 1b Abs. 6 BetrAVG i.V.m. §§ 2, 4 BetrAVG). Counsel Albrecht-Niermann empfiehlt eine verbindliche Auskunft beim zuständigen Finanzamt Düsseldorf-Süd vor dem Financial Close einzuholen.
"""))
    elems.append(handw("A.v.S.-O.: Verbindliche Auskunft anfordern! Frist für FA-Anfrage: Ende März 2026. — A."))
    elems.append(sp(4))
    elems.append(Paragraph("V. Fazit und Weiteres Vorgehen", S_H3))
    elems.append(P("""Die Pensionslandschaft in Deutschland ist durch die Altzusagen 1973/1981 hochkomplex und mit erheblichem Abzinsungsrisiko behaftet. Ein Zinsanstieg um 100 bp würde die DBO um EUR 265 Mio. reduzieren (positiver Effekt), ein weiterer Rückgang um 100 bp würde sie um EUR 311 Mio. erhöhen. Das Management muss die hohe Zinssensitivität im Treasury-Hedging berücksichtigen.

Prioritär ist die Einsetzung der Einigungsstelle und der Sozialplan-Abschluss, um die Rechtswirksamkeit des Future-Service-Stopps abzusichern. Parallel soll das CTA mit ausreichend Assets dotiert werden (Zieldotierung: EUR 1,7 Mrd. über drei Jahre), um das Bilanzbild zu verbessern und das PSVaG-Beitragsvolumen zu reduzieren.

<i>Friederike Albrecht-Niermann, Counsel</i> | <i>Treuenfels Yamamoto PartmbB</i> | 20.02.2026
"""))
    elems.append(PageBreak())
    return elems


def build_vo_inventory():
    """8. Versorgungsordnungs-Inventory"""
    elems = []
    elems += section_header("VERSORGUNGSORDNUNGS-INVENTORY", "Meissner Rheinwerk AG &#183; Versorgungsordnungen 1973–2008 &#183; Stand: 01.02.2026")
    elems.append(Paragraph("Erstellt: Annika Beerbohm-Sittler / Maximilian Pfaffenhausen-Quasthoff &#183; Senior Associates &#183; Treuenfels Yamamoto", S_SMALL_GRAY))
    elems.append(sp(6))

    elems.append(Paragraph("Überblick: Versorgungslandschaft Deutschland", S_H3))
    vo_overview = [
        ["VO-Bezeichnung", "Abschluss", "Geltungsbereich", "Typ", "Aktive Anwärter", "Rentner"],
        ["VO 1973 (K-VO-1)", "01.03.1973", "Alle AN vor 01.01.1982", "DB Leistungsprimat", "312", "2.847"],
        ["VO 1981 (K-VO-2)", "01.07.1981", "AN Eintritt 1974–1994", "DB Gesamtversorgung", "1.284", "1.453"],
        ["Chemie-Nord-TV (K-VO-3)", "12.11.1987", "Tarifgebundene AN", "Tarifvertrag-VO", "2.105", "421"],
        ["VO 1995 (K-VO-4)", "01.01.1995", "AN Eintritt 1995–2007", "DC Beitragsprimat", "1.842", "0"],
        ["VO 2008 (K-VO-5)", "01.01.2008", "AN Eintritt ab 01.01.2008", "DC Direktversicherung", "3.871", "0"],
        ["Sonderzusagen FK-001–FK-047", "div.", "Führungskräfte (47 Personen)", "Einzelvertrag DB", "47", "12"],
        ["Gesamt", "—", "—", "—", "9.461", "4.733"],
    ]
    tbl = Table(vo_overview, colWidths=[2.8*cm, 1.8*cm, 3.5*cm, 2.5*cm, 2*cm, 1.7*cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), DARK_BLUE),
        ("TEXTCOLOR",  (0,0), (-1,0), white),
        ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",   (0,0), (-1,-1), 8),
        ("ROWBACKGROUNDS", (0,1), (-1,-2), [white, SECTION_BG]),
        ("BACKGROUND", (0,-1), (-1,-1), RHEIN_GOLD),
        ("FONTNAME",   (0,-1), (-1,-1), "Helvetica-Bold"),
        ("GRID",       (0,0), (-1,-1), 0.4, grey),
        ("LEFTPADDING",(0,0),(-1,-1),3),
        ("TOPPADDING", (0,0),(-1,-1),2),
        ("BOTTOMPADDING",(0,0),(-1,-1),2),
    ]))
    elems.append(tbl)
    elems.append(sp(8))

    # VO 1973 Detail
    elems.append(Paragraph("VO 1973 – Detailanalyse (K-VO-1, K-VO-6 bis K-VO-12)", S_H3))
    elems.append(P("""Die Versorgungsordnung 1973 wurde durch Betriebsvereinbarung (BV) vom 01.03.1973 eingeführt. Sie gewährt eine Altersrente als Leistungsprimat: EUR 25,00 pro Dienstjahr, indexiert gemäß § 16 BetrAVG (Anpassungsprüfungspflicht alle 3 Jahre). Die VO 1973 kennt keine Obergrenzen, was bei langjährig Beschäftigten (40+ Dienstjahre) zu erheblichen Monatsrenten führt (Einzelfälle: bis EUR 3.800/Monat, vgl. Hellmrich-Vogt Aktuarbericht 2025, K-VO-7).

Die VO 1973 enthält in § 12 Abs. 3 eine sogenannte &#8222;BMW-ähnliche" Gesamtversorgungsobergrenze: Die Gesamtversorgung aus betrieblicher Rente + gesetzlicher Rente soll 75 % des letzten maßgeblichen Bruttogehalts nicht übersteigen. Diese Klausel wurde vom BAG für verschiedene ähnliche Systeme für teilweise unwirksam erklärt (BAG 3 AZR 304/13 zur Anrechnung gesetzlicher Rente, Urteil vom 19.05.2016); Rückabwicklungsansprüche bestehen daher für rd. 180 Rentner (K-VO-8, Risikoliste).

<b>Anpassungshistorie § 16 BetrAVG:</b> Die Meissner Rheinwerk AG hat die Anpassungsprüfung gem. § 16 BetrAVG zuletzt für 2022/2023 durchgeführt und die Renten um 3,2 % erhöht. Für 2025/2026 steht die nächste Prüfung an; bei einem Netto-Eigenkapital von EUR 1,87 Mrd. und EBITDA-Margin >12 % kann die wirtschaftliche Lage eine Nullrunde schwerlich rechtfertigen (BAG 3 AZR 304/13, Rn. 44 ff.). Empfehlung: 2,8 % Erhöhung per 01.01.2026 (K-VO-9).
"""))

    # VO 1981 Detail
    elems.append(Paragraph("VO 1981 – Gesamtversorgungszusage mit Lohnbezug (K-VO-2)", S_H3))
    elems.append(P("""Die Versorgungsordnung 1981 gewährt eine Gesamtversorgung in Höhe von 75 % des letzten Bruttogehalts (abzüglich gesetzlicher Rente und anderer Versorgungsleistungen). Sie enthält eine Gehaltsdynamik-Klausel, die Erhöhungen des versorgungsfähigen Gehalts nach einem festgelegten Tarifband (Chemie-Tarif NRW) automatisch berücksichtigt.

Besonderheit der VO 1981: Sie enthält in § 8 Abs. 2 eine sogenannte &#8222;Nachschusspflicht" des Arbeitgebers für den Fall einer Schließung des Systems. Rechtlich umstritten ist, ob diese Klausel auch bei einer Schließung mit Betriebsvereinbarung (Ablöse-BV) greift. Das OLG Düsseldorf hat in einem ähnlichen Fall entschieden, dass derartige Klauseln bei einvernehmlicher BV-Ablösung nicht anwendbar sind (OLG Düsseldorf I-6 U 223/19; nicht rechtskräftig, kein BAG-Urteil bislang). Prof. von Sompeh-Ostermann analysiert diese Konstellation im Drei-Stufen-Gutachten (Abschnitt B-3).
"""))

    # VO 1995, VO 2008
    elems.append(Paragraph("VO 1995 und VO 2008 – DC-Systeme", S_H3))
    elems.append(P("""Die VO 1995 stellt auf ein beitragsorientiertes System mit garantiertem Mindestleistungsversprechen i.S.v. § 1 Abs. 2 Nr. 2 BetrAVG (beitragsorientierte Leistungszusage, &#8222;BOLZ") um. Der Arbeitgeber garantiert den Erhalt der eingezahlten Beiträge zuzüglich einer Mindestverzinsung von 1,5 % p.a. Die VO 1995 ist konzernweit der kostenintensivste Übergangs-Baustein.

Die VO 2008 sieht ausschließlich Direktversicherungen gemäß § 1b Abs. 2 BetrAVG und § 3 Nr. 63 EStG vor (Gehaltsumwandlung bis EUR 3.504 p.a. steuerfrei; bei Aufstockung durch AG: bis EUR 7.008). Alle VO-2008-Anwärter werden durch den Future-Service-Stopp weniger stark betroffen, da das DC-System flexibel ablösbar ist.
"""))

    elems.append(Paragraph("Chemie-Nord-Versorgungstarifvertrag", S_H3))
    elems.append(P("""Der Chemie-Nord-Versorgungstarifvertrag vom 12.11.1987 (Verlängerung 2003, 2012) ist zwischen dem Arbeitgeberverband Chemie NRW e.V. und der IG BCE geschlossen. Er bindet die Meissner Rheinwerk AG unmittelbar (§§ 3, 4 TVG). Eine Schließung der durch den TV geregelten Versorgungskomponente erfordert einen Tarifvertrag (§ 17 Abs. 3 BetrAVG). Verhandlungsstand: IG-BCE hat Bereitschaft zu Gesprächen signalisiert, GBR-Vorsitzender Kreidemann lehnt Schließung grundsätzlich ab (vgl. Einigungsstellen-Akte D-1).
"""))
    elems.append(handw("Pfaffenhausen-Quasthoff: TV-Kündigung durch AGB prüfen? → Nein, § 77 Abs. 3 BetrVG Sperrwirkung! Abgestimmt mit A.v.S.-O."))

    elems.append(Paragraph("Sonderzusagen Führungskräfte FK-001 bis FK-047", S_H3))
    elems.append(P("""47 Einzelvertragsregelungen für Führungskräfte (Sonderakte VI, besonders vertraulich). Diese Zusagen sehen u.a. vor: Frührentenberechtigung ab 60, Invaliditätsleistung ab 100 % EU-Rente, überproportionale Leistungssteigerung bei Erreichen bestimmter Karrierestufen, und in Einzelfällen nominale Kapitalzusagen von bis zu EUR 1,2 Mio. Eine vollständige Liste der Begünstigten (anonymisiert) findet sich in K-VO-40 bis K-VO-47 (Sonderakte VI). Alle 47 Personen wurden über § 4a BetrAVG informiert; Auskunftserteilungen liegen vor.

<i>Rechtsrisiko:</i> Bei einer Schließung des Gesamtsystems müssen Sonderzusagen individuell angepasst werden (BFH-Rspr. zu § 6a EStG-Schachteln; BAG 3 AZR 540/16 schließt Einzelvertragsanpassungen nicht aus).
"""))
    elems.append(latin("mutatis mutandis – für Einzelzusagen gilt dasselbe Prüfungsschema wie für kollektivrechtliche Versorgungsordnungen"))
    elems.append(PageBreak())
    return elems


def build_drei_stufen_gutachten():
    """9. Drei-Stufen-Theorie-Gutachten"""
    elems = []
    elems += section_header("DREI-STUFEN-THEORIE-GUTACHTEN", "Prof. Dr. Adalbert von Sompeh-Ostermann &#183; Treuenfels Yamamoto &#183; 28.02.2026")
    elems.append(Paragraph("STRENG VERTRAULICH – Anwaltlich privilegiertes Rechtsgutachten – Mandatsbezogenes Schriftstück", S_WARN))
    elems.append(sp(6))

    elems.append(P("""<b>Verfasser:</b> Prof. Dr. Adalbert von Sompeh-Ostermann, LL.M. (Oxford), Fachanwalt für Arbeitsrecht, Honorarprofessor Universität zu Köln für Versorgungs- und Vergütungsrecht
<b>An:</b> Vorstand Meissner Rheinwerk AG (CFO / HR-Vorstand) / Steuerungskreis RHEINGOLD 2030
<b>Aktenzeichen:</b> TY-2026-RHEINGOLD-001 / Gutachten Nr. 1
<b>Datum:</b> 28. Februar 2026"""))
    elems.append(sp(6))

    elems.append(Paragraph("A. Gegenstand des Gutachtens", S_H3))
    elems.append(P("""Das vorliegende Gutachten untersucht die rechtliche Zulässigkeit der geplanten Schließung der leistungsorientierten Versorgungssysteme der Meissner Rheinwerk AG in Deutschland (VO 1973, VO 1981, Chemie-Nord-TV) mit Stopp des Future Service zum 01.01.2027 bei Einfrieren der erdienten Anwartschaften. Das Gutachten analysiert die Voraussetzungen und Grenzen eines solchen Eingriffs nach der ständigen Rechtsprechung des Bundesarbeitsgerichts zur sogenannten Drei-Stufen-Theorie und gibt eine Bewertung der Eingriffstiefe sowie der erforderlichen sachlichen Rechtfertigung.
"""))

    elems.append(Paragraph("B. Rechtlicher Rahmen: §§ 1-17 BetrAVG und Drei-Stufen-Theorie", S_H3))
    elems.append(P("""<b>I. Gesetzliche Grundlagen</b>

Das Gesetz zur Verbesserung der betrieblichen Altersversorgung (BetrAVG) vom 19.12.1974 (BGBl. I S. 3610, zuletzt geändert durch Art. 4 BRSG vom 17.08.2017) bildet die zentrale Rechtsgrundlage. Insbesondere relevant:

• §§ 1, 1a BetrAVG: Unverfallbarkeit von Anwartschaften nach 3 Jahren (seit BRSG 2018) und das Versprechen auf Leistungen im Alter, bei Invalidität und für Hinterbliebene.
• § 16 BetrAVG: Anpassungsprüfungspflicht alle 3 Jahre (Ausnahme: Direktversicherungen, Pensionskassen mit bestimmten Garantien).
• § 17 Abs. 3 BetrAVG: Beschränkte Abdingbarkeit – Tarifvertragsabweichungen nur durch TV.
• §§ 2, 3 BetrAVG: Berechnung des Teilanspruchs bei vorzeitigem Ausscheiden (m/n-Quotierung).

<b>II. Drei-Stufen-Theorie des BAG</b>

Das BAG entwickelte mit dem Beschluss des Großen Senats vom 17.04.1985 (GS 1/82, BAGE 48, 22) die maßgebliche Drei-Stufen-Theorie zur Kontrolle von Eingriffen in bestehende Versorgungsregelungen durch nachfolgende Betriebsvereinbarungen. Das Konzept gilt als gesichertes Verfassungsrechtsprinzip und kombiniert den allgemeinen Verhältnismäßigkeitsgrundsatz mit dem Vertrauensschutzgedanken des Art. 14 GG (Eigentumsschutz erdiente Anwartschaften).

<b>Stufe 1 – Eingriff in erdiente Besitzstände:</b>
Der &#8222;erdiente Besitzstand" ist der Kern der Zusage, der auf bereits erbrachter Arbeitsleistung beruht. Lohn-/Leistungsverhältnis ist insoweit bereits erfüllt. Ein Eingriff in erdiente Besitzstände – d.h. eine Schmälerung des bereits erdienten Teils der Versorgungsleistung – ist nach BAG GS 1/82 nur bei zwingenden Gründen zulässig; in der Praxis de facto ausgeschlossen.

<b>Stufe 2 – Eingriff in dienstzeitabhängige Zuwächse:</b>
Hierbei handelt es sich um Zuwächse, die noch nicht erdient sind, aber auf einer bereits erbrachten Leistung beruhen (z.B. Steigerungsbeträge für die bereits zurückgelegte Dienstzeit, die nach der VO noch zustehen würden). Eingriffe auf dieser Ebene erfordern &#8222;triftige Gründe" (BAG 3 AZR 392/06 vom 10.07.2007, Rn. 51: &#8222;Die Einschränkung dienstzeitabhängiger Zuwächse bedarf triftiger, sachlich-proportionaler Gründe").

<b>Stufe 3 – Eingriff in künftige, noch nicht erdiente Zuwächse (Future Service):</b>
Der Stopp des Future Service – d.h. die Schließung des Systems für künftige Dienstjahre – greift in noch nicht verdiente, nur expectative Positionen ein. Das BAG (3 AZR 540/16 vom 19.07.2016, Rn. 38 ff.) lässt hierfür &#8222;sachlich-proportionale Gründe" ausreichen, d.h. einen nachvollziehbaren, plausiblen Grund für die Systemänderung.
"""))

    elems.append(Paragraph("C. Subsumtion: Future-Service-Stopp Meissner Rheinwerk AG", S_H3))
    elems.append(P("""<b>I. Klassifikation des Eingriffs</b>

Der geplante Schritt – Stopp des Future Service ab 01.01.2027 bei Einfrierung der erdienten Anwartschaft – ist <b>ausschließlich</b> ein Eingriff der dritten Stufe. Ein Eingriff in die erdienten Besitzstände (Stufe 1) oder in die dienstzeitabhängigen Zuwächse der Vergangenheit (Stufe 2) findet nicht statt: Die bereits erdienten Anwartschaften bleiben vollständig erhalten. Es wird lediglich die Neuakkumulation ab dem Schließungsstichtag gestoppt.

<b>WICHTIG:</b> Es darf unter keinen Umständen der Versuch unternommen werden, durch die Schließungsvereinbarung auch Stufe-2-Positionen zu tangieren (z.B. durch Neuberechnung der erdienten Anwartschaft nach niedrigerem Maßstab). Das hätte eine erhebliche Verschärfung des Rechtfertigungsmaßstabs zur Folge.
"""))
    elems.append(handw("A.v.S.-O.: Brindeau: D-3-Stufen NICHT auf Future-Service ausdehnen, sonst BAG zerlegt uns. A."))

    elems.append(P("""<b>II. Sachliche Rechtfertigung (Stufe 3)</b>

Das BAG (3 AZR 540/16, Rn. 45) fordert für den Future-Service-Stopp einen sachlich-proportionalen Grund. Als anerkannte Gründe gelten u.a.:

(1) <b>Finanzielle Belastung:</b> Die DBO von EUR 2,4 Mrd. (rein DE) stellt eine erhebliche bilanzielle Belastung dar. Im Verhältnis zur Bilanzsumme von EUR 6,4 Mrd. (Konzern 2024) entspricht dies 37,5 % – ein für ein IFRS-bilanzierendes Unternehmen außergewöhnlich hoher Wert, der nach Börsenmakleransicht die Bewertungsmultiplikatoren belastet.

(2) <b>Risikomanagement:</b> Das erhebliche Zinsänderungsrisiko (vgl. Abschnitt B, Status-Memo Albrecht-Niermann: +/- 265 Mio. bei 100 bp Zinsänderung) und die demografischen Risiken einer alternden Belegschaft begründen ein legitimes Interesse an Risikoreduzierung.

(3) <b>Wettbewerbsposition:</b> In der deutschen Spezialchemie-Branche haben nahezu alle Konkurrenten (BASF, Lanxess, Evonik) entsprechende Systeme bereits auf DC umgestellt. Eine Fortführung der teuren DB-Systeme benachteiligt Meissner Rheinwerk im Wettbewerb um Kapital und Fachkräfte.

(4) <b>Carve-out-Notwendigkeit (RHEINORGANICS):</b> Ohne Schließung ist der Carve-out der Sparte RHEINORGANICS für Albion Bridge Capital Partners nicht realisierbar; der PE-Investor macht die Transaktion von einer sauberen Pensionslösung abhängig (Dealbreaker, vgl. M&A-Annex H-1).

(5) <b>IAS-19-Compliance und Kapitalmarkt:</b> Die Aufrechterhaltung hoher Pensionsverbindlichkeiten gefährdet die Investment-Grade-Bonität (aktuell: Moody's Baa1; S&P BBB+) und verteuert Refinanzierungen.

<b>Bewertung:</b> Die vorstehenden Gründe sind kumulativ und begründen zusammengenommen einen sachlich-proportionalen Grund i.S.d. BAG-Rechtsprechung zur dritten Stufe. Der Future-Service-Stopp dürfte damit vor dem BAG standhalten.
"""))

    elems.append(Paragraph("D. Unverfallbarkeit und § 2 BetrAVG", S_H3))
    elems.append(P("""Alle betroffenen Anwärter haben (sämtliche Jahrgänge ab 1973) nach § 1b BetrAVG bereits unverfallbare Anwartschaften erworben (Dreijahresfrist ist in allen Fällen abgelaufen). Bei Schließung zum 01.01.2027 sind die Anwartschaften nach der m/n-Methode des § 2 BetrAVG zu quotieren:

<b>Quotierte Anwartschaft = (Anwartschaft bei Regelalter) × (tatsächl. Dienstzeit bis 01.01.2027) / (mögliche Gesamtdienstzeit bis Regelalter)</b>

Diese Quotierung ergibt bei einem durchschnittlichen Eintrittsdatum von 1998 und Regelalter 67 einen Quotienten von rd. 0,63 für den Mediananwärter – d.h. der Anwärter behält 63 % der ohne Schließung im Alter erreichbaren Rente.

Zu beachten: § 2 Abs. 5 BetrAVG (Anpassungsregelung bei Schließung) schreibt vor, dass die erdienten Anwartschaften weiter an der Einkommensentwicklung des aktiven Personals teilhaben müssen, wenn die VO eine dynamische Anknüpfung enthält (relevant für VO 1981 mit Tarifbezug). Dies ist im CTA und im Sozialplan zu berücksichtigen.
"""))

    elems.append(Paragraph("E. Analyse BAG-Entscheidungen mit Bezug zu EuGH-Rechtsprechung", S_H3))
    elems.append(P("""Der EuGH hat in mehreren Entscheidungen betriebliche Versorgungssysteme mit Fragen des Gleichbehandlungsrechts (Art. 157 AEUV) und des Insolvenzsicherungsrechts verbunden:

• <b>EuGH C-168/18 (Bauer/Willmeroth):</b> Unmittelbare horizontale Wirkung von Art. 31 GRCh (Anspruch auf Urlaub); für Pensionen bedeutet dies: das Verschlechterungsverbot könnte sich bei grenzüberschreitenden EU-Arbeitnehmern auf Primärrecht stützen.

• <b>EuGH C-396/22 (Generali):</b> IORP-II-Richtlinie 2016/2341/EU, Art. 11 ff.: Anforderungen an Risikobewertung und Governance von Pensionsfonds. Die geplante Erweiterung des Meissner-Pensionsfonds muss IORP-II-konform erfolgen (BaFin-Verfahren VA 31-Q 5232-2026/0014).

• <b>EuGH C-680/15 (Asklepios Kliniken):</b> Betriebsübergang und Pensionsrechte – bei Carve-out kann die Übertragung der RHEINORGANICS-Belegschaft auf den Erwerber eine Verpflichtung zur Übernahme aller Altzusagen nach § 613a BGB auslösen, sofern keine anderweitige Vereinbarung mit Einverständnis der Arbeitnehmer getroffen wird.

Diese EuGH-Rechtsprechung ist in der Gestaltung der Carve-out-Klauseln (SPA-Annex, Modul H) zu berücksichtigen.
"""))

    elems.append(Paragraph("F. Ergebnis und Empfehlungen", S_H3))
    elems.append(P("""<b>1.</b> Der Future-Service-Stopp ist auf Basis der Drei-Stufen-Theorie (BAG GS 1/82, 3 AZR 392/06, 3 AZR 540/16) als Eingriff der dritten Stufe zulässig, wenn die sachlichen Gründe (finanzielle Belastung, Risikoreduzierung, Wettbewerbsposition, Carve-out-Notwendigkeit) dokumentiert und im Sozialplan/Einigungsstellenverfahren transparent dargelegt werden.

<b>2.</b> Eingriffe in erdiente Besitzstände (Stufe 1) oder dienstzeitabhängige Zuwächse der Vergangenheit (Stufe 2) sind zu vermeiden. Die Schließungsvereinbarung ist hierauf explizit zu beschränken.

<b>3.</b> Der Chemie-Nord-TV erfordert eine gesonderte tarifvertragliche Lösung (§ 17 Abs. 3 BetrAVG); eine bloße BV-Ablöse ist insoweit unwirksam.

<b>4.</b> Die Einigungsstelle (ArbG Düsseldorf 7 BV 412/26) bietet das geeignete Verfahren zur kollektiven Einigung; dabei ist zu beachten, dass die Einigungsstelle beim Regelungstatbestand &#8222;Versorgungsordnung" Ermessensgrenzen hat (BAG 3 AZR 542/17).

<b>5.</b> Individuelle Sonderzusagen (FK-001 bis FK-047) sind gesondert zu verhandeln; hier gelten die BAG-Grundsätze zum Vertrauensschutz bei einzelvertraglichen Zusagen (BAG 3 AZR 540/16, Rn. 61 ff.).

<i>Prof. Dr. Adalbert von Sompeh-Ostermann, LL.M. (Oxford)</i>
<i>Fachanwalt für Arbeitsrecht &#183; Honorarprofessor Universität zu Köln</i>
<i>Treuenfels Yamamoto Rechtsanwälte PartmbB &#183; 28.02.2026</i>
"""))
    elems.append(latin("quod erat probandum – die rechtliche Zulässigkeit des Future-Service-Stopps ist damit nach geltendem BAG-Recht tragbar begründet"))
    elems.append(PageBreak())
    return elems


def build_cta_treuhand():
    """10. CTA-Treuhandvertrag-Entwurf"""
    elems = []
    elems += section_header("CTA-TREUHANDVERTRAG (ENTWURF)", "Doppeltreuhand &#183; CTA Rheinland Trust e.V. &#183; Stand: 15.03.2026")
    elems.append(Paragraph("ENTWURF – NOCH NICHT BEURKUNDET – ÄNDERUNGEN VORBEHALTEN", S_WARN))
    elems.append(sp(6))

    elems.append(P("""<b>DOPPELTREUHANDVERTRAG</b>

zwischen

<b>MEISSNER RHEINWERK AG</b>, Rheinwerkallee 1, 40589 Düsseldorf-Reisholz
(im Folgenden: &#8222;Versorgungsschuldner")

und

<b>CTA RHEINLAND TRUST e.V.</b>, Königsallee 199a, 40212 Düsseldorf
(im Folgenden: &#8222;Treuhänder")

— <i>nachfolgend gemeinsam &#8222;die Parteien" —</i>

<b>Präambel</b>

Die Meissner Rheinwerk AG hat gegenüber ihren aktiven und ehemaligen Arbeitnehmern sowie Rentnern (im Folgenden: &#8222;Versorgungsberechtigte") umfangreiche Versorgungszusagen nach Maßgabe der Versorgungsordnungen 1973, 1981 und des Chemie-Nord-TV abgegeben. Um die Sicherheit dieser Zusagen im Insolvenzfall zu gewährleisten und die handelsbilanziellen Pensionsrückstellungen gem. § 246 Abs. 2 Satz 2 HGB saldieren zu können (Deckungsreserven-Saldierung), errichten die Parteien hiermit einen doppelseitigen Treuhandvertrag (Contractual Trust Arrangement, &#8222;CTA").

Das CTA besteht aus zwei Treuhandverhältnissen:
(a) <b>Sicherungstreuhand:</b> Übereignung der Deckungsreserven vom Versorgungsschuldner auf den Treuhänder zum Zweck der insolvenzrechtlich abgesicherten Reservierung der Pensionsgelder (BAG 3 AZR 18/12 vom 16.07.2013); und
(b) <b>Verwaltungstreuhand:</b> Verwaltung der Deckungsreserven durch den Treuhänder im Auftrag des Versorgungsschuldners nach einem vereinbarten Anlagereglement.
"""))

    elems.append(Paragraph("§ 1 Begriffsbestimmungen", S_H3))
    elems.append(P("""&#8222;<b>Deckungsreserven</b>" bezeichnen alle Vermögenswerte, die der Versorgungsschuldner auf den Treuhänder überträgt und die zur Deckung der Pensionsverpflichtungen des Versorgungsschuldners dienen.

&#8222;<b>Versorgungsverpflichtungen</b>" sind die Verpflichtungen des Versorgungsschuldners gegenüber den Versorgungsberechtigten aus den Versorgungsordnungen 1973, 1981 und dem Chemie-Nord-TV sowie ggf. aus Einzelzusagen.

&#8222;<b>Anlagereglement</b>" ist das in Anlage 1 beigefügte Dokument, das die zulässigen Anlageklassen, Risikolimite und Liquiditätskennzahlen für die verwalteten Deckungsreserven festlegt.

&#8222;<b>Treuhandkonten</b>" sind die auf den Namen des Treuhänders geführten Konten und Depots, auf denen die Deckungsreserven gehalten werden.

&#8222;<b>Ausfall des Versorgungsschuldners</b>" liegt vor im Falle der Eröffnung des Insolvenzverfahrens über das Vermögen des Versorgungsschuldners (§ 27 InsO) oder der Ablehnung mangels Masse (§ 26 InsO).
"""))

    elems.append(Paragraph("§ 2 Errichtung und Dotierung", S_H3))
    elems.append(P("""(1) Der Versorgungsschuldner überträgt mit Abschluss dieses Vertrages einen Anfangsbetrag von <b>EUR 350.000.000,00</b> (dreihundertfünfzig Millionen Euro) auf das Treuhandkonto DE XX XXXX XXXX XXXX XXXX XX bei der Deutsche Bank AG.

(2) In den Folgejahren dotiert der Versorgungsschuldner den Treuhandfonds gemäß folgendem Dotierungsplan:
— bis 31.12.2026: EUR 350 Mio. (Erstdotierung)
— bis 31.12.2027: EUR 500 Mio. (Aufstockung I)
— bis 31.12.2028: EUR 450 Mio. (Aufstockung II)
— bis 31.12.2029: EUR 220 Mio. (Aufstockung III)
— Zieldotierung 2029: EUR 1.520 Mio. (entspricht rd. 95 % der deutschen DBO nach Buyout)

(3) Der Dotierungsplan kann mit Zustimmung des Treuhänders und einer Stellungnahme von Hellmrich-Vogt Aktuarpartner GmbH angepasst werden, sofern sich die aktuariellen Grundlagen wesentlich geändert haben.
"""))

    elems.append(Paragraph("§ 3 Sicherungstreuhand – Insolvenzschutz", S_H3))
    elems.append(P("""(1) Die Deckungsreserven werden dem Treuhänder zur Sicherung der Ansprüche der Versorgungsberechtigten übereignet. Im Außenverhältnis ist der Treuhänder Eigentümer der Deckungsreserven. Im Innenverhältnis ist er verpflichtet, die Deckungsreserven ausschließlich für die Zwecke dieses Vertrages zu verwenden.

(2) Im Ausfall des Versorgungsschuldners ist der Treuhänder verpflichtet, die Deckungsreserven unmittelbar zur Erfüllung der Versorgungsverpflichtungen zu verwenden, soweit PSVaG-Leistungen nicht greifen. Insoweit ist das BAG-Urteil 3 AZR 18/12 (Insolvenzfestigkeit des CTA; Deckungsreserven sind keine Insolvenzmasse) maßgeblich. Auf Anforderung erstellt Hellmrich-Vogt ein Insolvenz-Adequacy-Gutachten.

(3) Ein Rückübertragungsanspruch des Versorgungsschuldners besteht ausschließlich in Höhe des Überschusses über die aktuariell ermittelte DBO (§ 246 Abs. 2 HGB i.V.m. IAS 19.64 ff. zum Asset-Ceiling).
"""))

    elems.append(Paragraph("§ 4 Verwaltungstreuhand – Anlagereglement", S_H3))
    elems.append(P("""(1) Der Treuhänder verwaltet die Deckungsreserven nach dem Anlagereglement (Anlage 1) nach dem Grundsatz der unternehmerischen Vorsicht.

(2) Zulässige Anlageklassen (gemäß IORP-II-Richtlinie Art. 19 Abs. 1):
— Anleihen (Staatsanleihen AAA-AA, Unternehmensanleihen IG): max. 60 %
— Aktien (breit diversifiziert, max. 20 % ein Titel): max. 30 %
— Immobilien (mittelbar über REITs / geschlossene Fonds): max. 10 %
— Alternative Investments (Infrastruktur, Private Equity, Hedge Fonds): max. 5 %
— Liquidität: min. 5 %

(3) Kontrahentenrisiken sind durch Diversifikation und Mindestrating (S&P A- oder Moody's A3) zu beschränken. Fremdwährungsrisiken sind auf 30 % des Portfolios zu begrenzen.
"""))

    elems.append(Paragraph("§§ 5–12 [Auszug – vollständiger Text in K-CTA-1 bis K-CTA-22]", S_H4))
    elems.append(Paragraph("<i>(§ 5 Berichtspflichten; § 6 Treuhänder-Entgelt; § 7 Beirat; § 8 Haftung; § 9 Kündigung und Beendigung; § 10 Anlagestrategie-Änderung; § 11 Datenschutz; § 12 Schlussbestimmungen, Gerichtsstand LG Düsseldorf — vollständig in Sonderakte II, Bl. 58–74)</i>", S_KURSIV))
    elems.append(sp(6))
    elems.append(Paragraph("Unterschriften (Entwurf):", S_H4))
    elems.append(Paragraph("Meissner Rheinwerk AG: ___________________________  CTA Rheinland Trust e.V.: ___________________________", S_NORMAL))
    elems.append(Paragraph("[Beurkundung durch Notar Dr. Martin Hasenbein-Vollmer, Düsseldorf, geplant 30.06.2026]", S_SMALL_GRAY))
    elems.append(PageBreak())
    return elems


def build_buyout_term_sheet():
    """11. Pension Buyout Term Sheet"""
    elems = []
    elems += section_header("PENSION BUYOUT TERM SHEET (ENTWURF)", "Meissner Rheinwerk AG / Hanseatica Lebensversicherung AG &#183; Stand: 28.04.2026")
    elems.append(Paragraph("VERTRAULICH – Laufende Kaufverhandlungen – Kein Bindungscharakter", S_WARN))
    elems.append(sp(6))

    elems.append(P("""Dieses unverbindliche Term Sheet fasst die wesentlichen Eckpunkte der angestrebten Transaktion zusammen, bei der die Meissner Rheinwerk AG die Pensionsverbindlichkeiten gegenüber den deutschen Rentnerbeständen auf die Hanseatica Lebensversicherung AG überträgt (Pension Buyout / Gruppenrentenversicherung).
"""))

    ts_data = [
        ["Parameter", "Hanseatica LV AG (Hamburg)", "Nippon Pension Anstalt KK (Osaka)", "Bewertung"],
        ["Bieter", "Hanseatica LV AG, Hamburg", "Nippon Pension Anstalt KK, Osaka", ""],
        ["Regulierung", "VAG §§ 232 ff (Pensionsfonds DE)", "FSA Japan / MHLW", "Hanseatica regulatorisch sicherer"],
        ["Bestandsübernahme", "4.300 Rentner DE", "4.300 Rentner DE", "Identisch"],
        ["Einmalbeitrag (Indikativ)", "EUR 780 Mio.", "EUR 795 Mio.", "Hanseatica günstiger"],
        ["Rückdeckungsquote", "105 %", "108 %", "Nippon höhere Reserve"],
        ["Anpassungsgarantie § 16", "Keine (§ 16 Abs. 3 Nr. 2 BetrAVG)", "Keine", "Identisch"],
        ["Währungsrisiko", "EUR (kein Risiko)", "EUR (kein Risiko)", "Identisch"],
        ["BaFin-Genehmigung", "Erforderlich (VAG § 232 Abs. 4)", "Zusätzlich BaFin + FSA Japan", "Hanseatica schneller"],
        ["Rating Lebensversicherer", "A (S&P) / A2 (Moody's)", "AA- (S&P) / Aa3 (Moody's)", "Nippon besser"],
        ["Due-Diligence-Aufwand", "6 Wochen (DE-Standard)", "10 Wochen (grenzüberschreitend)", "Hanseatica effizienter"],
        ["Vertragskomplexität", "Standard GRV-Vertrag", "Hybrid DE/JP-Recht", "Hanseatica einfacher"],
        ["Empfehlung Kanzlei TY", "PRÄFERIERT", "Backup-Option", "Hanseatica empfohlen"],
    ]
    tbl = Table(ts_data, colWidths=[3.5*cm, 3.7*cm, 3.7*cm, 3.6*cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), DARK_BLUE),
        ("TEXTCOLOR",  (0,0), (-1,0), white),
        ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",   (0,0), (-1,-1), 7.5),
        ("FONTNAME",   (0,1), (0,-1), "Helvetica-Bold"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [white, SECTION_BG]),
        ("BACKGROUND", (0,-1), (-1,-1), HexColor("#dff0d8")),
        ("FONTNAME",   (0,-1), (-1,-1), "Helvetica-Bold"),
        ("GRID",       (0,0), (-1,-1), 0.4, grey),
        ("LEFTPADDING",(0,0),(-1,-1),3),
        ("TOPPADDING", (0,0),(-1,-1),2),
        ("BOTTOMPADDING",(0,0),(-1,-1),2),
    ]))
    elems.append(tbl)
    elems.append(sp(6))

    elems.append(Paragraph("Auswahlbegründung und nächste Schritte", S_H3))
    elems.append(P("""Die Kanzlei Treuenfels Yamamoto empfiehlt den Abschluss mit der Hanseatica Lebensversicherung AG aus folgenden Gründen:

(1) <b>Regulatorische Klarheit:</b> Hanseatica ist in Deutschland zugelassen und unterliegt der BaFin-Aufsicht. Die Genehmigung nach § 232 Abs. 4 VAG ist im BaFin-Verfahren VA 31-Q 5232-2026/0014 bereits eingeleitet. Eine Einbeziehung der japanischen FSA-Regulierung (Nippon Pension Anstalt) würde 4-6 Monate zusätzliche Bearbeitungszeit generieren.

(2) <b>Preisvorteil:</b> EUR 780 Mio. vs. EUR 795 Mio. – eine Differenz von EUR 15 Mio., die erheblich ist.

(3) <b>Kein früheres Beratungsmandat der Kanzlei:</b> Conflict Cleared (vgl. A-4).

(4) <b>Due-Diligence-Zeitplan:</b> Für Financial Close Dezember 2026 (Meilenstein M-9) ist Hanseatica realistisch erreichbar, Nippon nicht.

<b>Nächste Schritte:</b>
— Bis 15.05.2026: Letter of Intent mit Hanseatica
— Bis 30.06.2026: Due-Diligence Datenraum (Achtung: Datenschutz § 26 DSGVO für Rentner-Datensätze!)
— Bis 31.08.2026: SPA-Entwurf Gruppenrentenvertrag
— Financial Close: 31.12.2026 (Meilenstein M-9)

[Anlagen K-MA-3, K-MA-4: Bietervergleichsmatrix – vollständig in Sonderakte V]
"""))
    elems.append(PageBreak())
    return elems


def build_psv_schriftsatzkette():
    """12. PSVaG-Schriftsatzkette"""
    elems = []
    elems += section_header("PSVaG-SCHRIFTSATZKETTE", "PSVaG Mahnschreiben &#183; Treuenfels Yamamoto Stellungnahme &#183; PSVaG Erwiderung")
    elems.append(sp(4))

    # PSVaG Mahnschreiben
    elems += mini_header("PSVaG – Mahnschreiben vom 22. März 2026")
    elems += fax_block([
        "Pensions-Sicherungs-Verein Versicherungsverein auf Gegenseitigkeit",
        "Postfach 10 07 07 &#183; 50447 Köln &#183; www.psvag.de",
        "Beitragsbescheid Nr.: 2026/A-RW-MEISSNER-008842",
        "",
        "An: Meissner Rheinwerk AG, HR-Abteilung, z.Hd. Dr. Constanze Brindeau-Lorbach",
        "",
        "Sehr geehrte Damen und Herren,",
        "",
        "gemäß § 10 Abs. 3 BetrAVG sind insolvenzschutzbeitragspflichtige Arbeitgeber verpflichtet,",
        "ihre beitragspflichtigen Versorgungsverpflichtungen jährlich dem PSVaG zu melden und den",
        "festgesetzten Beitrag fristgerecht zu entrichten.",
        "",
        "Die Meissner Rheinwerk AG hat für das Beitragsjahr 2025 den Beitrag nicht vollständig",
        "entrichtet. Es verbleibt ein offener Saldo von EUR 1.284.716,00 (Beitragssatz 2025:",
        "3,0 ‰ der Beitragsbemessungsgrundlage EUR 2,4 Mrd. = EUR 7.200.000 abzüglich geleisteter",
        "Vorauszahlungen von EUR 5.915.284). Außerdem weist die eingereichte Meldung",
        "Unplausibilitäten bei der Angabe der CTA-Planvermögen auf.",
        "",
        "Wir fordern Sie hiermit auf, den offenen Betrag bis zum 15.04.2026 zu überweisen sowie",
        "eine korrigierte Meldung mit Nachweis der CTA-Saldierung zu übersenden.",
        "",
        "IBAN: DE72 3706 0193 0000 1000 00 (PSVaG, BIC: GENODED1GVK)",
        "",
        "PSVaG – Bearbeiterin: Dr. Hannelore Fischbach-Stern, Sachgebiet Beitragswesen",
        "Tel.: 0221 9803-222 &#183; hfischbach-stern@psvag.de",
        "22.03.2026 &#183; Zeichen PSV 2026-MR-00442",
    ], sender="PSVaG Köln", receiver="Meissner Rheinwerk AG", date="22.03.2026 09:12", pages="2/2")

    # Stellungnahme TY
    elems += mini_header("Treuenfels Yamamoto – Stellungnahme vom 9. April 2026")
    elems.append(P("""Treuenfels Yamamoto Rechtsanwälte PartmbB
Königsallee 92 &#183; 40212 Düsseldorf
Tel.: +49 211 9200-100 &#183; Fax: +49 211 9200-199

<b>Per Einschreiben mit Rückschein und Fax</b>

An:
Pensions-Sicherungs-Verein VVaG
z.Hd. Dr. Hannelore Fischbach-Stern
Postfach 10 07 07 &#183; 50447 Köln

Düsseldorf, den 09. April 2026

<b>Beitragsbescheid 2026/A-RW-MEISSNER-008842 – Unsere Stellungnahme</b>
Unser Zeichen: TY-2026-RHEINGOLD-001-PSV

Sehr geehrte Frau Dr. Fischbach-Stern,

wir vertreten die Meissner Rheinwerk AG (Mandantin) in vorstehender Angelegenheit und beziehen uns auf Ihr Mahnschreiben vom 22.03.2026.

<b>I. Zahlungsrückstand</b>

Die von Ihnen errechnete Differenz von EUR 1.284.716,00 ist dem Grunde nach nicht bestritten. Ursächlich ist eine Abstimmungsdifferenz bei der Meldung der CTA-Planvermögen: Die Mandantin hat das CTA-Vermögen (per 31.12.2025: EUR 780 Mio.) gemäß § 246 Abs. 2 HGB zur Saldierung angemeldet. Nach unserer Auffassung reduziert dies die beitragspflichtigen Versorgungsverpflichtungen nach § 10 Abs. 3 Satz 1 BetrAVG.

<b>II. Rechtslage zur CTA-Saldierung</b>

Die Insolvenzfestigkeit des doppelseitigen CTA ist durch BAG 3 AZR 18/12 (Urteil vom 16.07.2013, BAGE 145, 291) grundsätzlich anerkannt. Damit sind die dem CTA zugeführten Vermögenswerte dem insolvenzrechtlichen Zugriff der Gläubiger entzogen. Konsequenterweise sind diese Werte auch bei der PSVaG-Beitragsbemessung zu berücksichtigen (PSVaG-Beitragsrundschreiben 2023/4, Tz. 18 ff.).

<b>III. Kurzfristige Zahlung und Klärung</b>

Unsere Mandantin wird den strittigen Betrag von EUR 1.284.716,00 bis zum 15.04.2026 entrichten, um Säumniszuschläge nach § 24 Abs. 2 SGB IV zu vermeiden. Gleichzeitig behalten wir uns vor, Einspruch gegen die Beitragsfestsetzung einzulegen, sofern keine Einigung über die Anrechnung der CTA-Deckungsreserven erzielt wird.

Mit freundlichen kollegialen Grüßen

Prof. Dr. Adalbert von Sompeh-Ostermann &#183; Treuenfels Yamamoto PartmbB
"""))
    elems.append(sp(4))

    # PSVaG Erwiderung
    elems += mini_header("PSVaG – Erwiderung vom 28. April 2026")
    elems.append(P("""Pensions-Sicherungs-Verein VVaG &#183; Köln, 28.04.2026
Zeichen: PSV 2026-MR-00442-R

An: Treuenfels Yamamoto PartmbB, z.Hd. Prof. Dr. von Sompeh-Ostermann

Sehr geehrter Herr Professor von Sompeh-Ostermann,

wir bestätigen den Zahlungseingang vom 14.04.2026 (EUR 1.284.716,00) und danken für Ihre ausführliche Stellungnahme.

Zur Frage der CTA-Anrechnung: Wir teilen Ihre Rechtsauffassung im Grundsatz (BAG 3 AZR 18/12 ist uns bekannt). Allerdings erfordert die CTA-Anrechnung gemäß unserem Beitragsrundschreiben 2023/4 einen Nachweis in Form des vollständigen CTA-Vertrags sowie eines aktuariellen Gutachtens über die Planvermögen zum Stichtag 31.12.2025.

Wir bitten um Einreichung dieser Unterlagen bis zum 31.05.2026. Nach Prüfung werden wir ggf. eine Beitragskorrektur für 2025 vornehmen.

Mit freundlichen Grüßen
Dr. Hannelore Fischbach-Stern &#183; PSVaG &#183; Sachgebiet Beitragswesen
"""))
    elems.append(handw("A.v.S.-O.: Hellmrich-Vogt auffordern, Aktuargutachten bis 20.05.2026 zu liefern. Dringend! — A."))
    elems.append(PageBreak())
    return elems


def build_einigungsstelle():
    """13. Einigungsstellen-Akte"""
    elems = []
    elems += section_header("EINIGUNGSSTELLEN-AKTE", "ArbG Düsseldorf 7 BV 412/26 &#183; Gesamtbetriebsrat vs. Meissner Rheinwerk AG")
    elems.append(sp(4))

    elems += mini_header("Antrag Gesamtbetriebsrat (Plöger Maibach Rechtsanwälte, Köln) – eingegangen 01.03.2026")
    elems.append(P("""<b>An das Arbeitsgericht Düsseldorf</b>
Kammergericht des Landes NRW &#183; Düsseldorfer Str. 199 &#183; 40545 Düsseldorf

<b>In dem Beschlussverfahren</b>

Antragsteller: Gesamtbetriebsrat der Meissner Rheinwerk AG
— vertreten durch Plöger Maibach Rechtsanwälte, Apostelnstr. 8–10, 50667 Köln —
— RA Dr. Wolfram Plöger-Heinekamp —

gegen

Antragsgegnerin: Meissner Rheinwerk AG, Rheinwerkallee 1, 40589 Düsseldorf-Reisholz
— vertreten durch Treuenfels Yamamoto Rechtsanwälte PartmbB, Königsallee 92, 40212 Düsseldorf —

beantragen wir:

<b>Es wird eine Einigungsstelle gemäß § 76 Abs. 2 BetrVG zum Regelungsgegenstand &#8222;Neufassung der Versorgungsordnung / Schließung des DB-Systems" eingesetzt. Als Vorsitzende wird Frau Richterin am Arbeitsgericht a.D. Dr. Hannelore Wupperhain-Stein, Düsseldorf, vorgeschlagen.</b>

<b>Begründung:</b>

Der GBR bestreitet nicht grundsätzlich das Recht der Arbeitgeberin, das DB-System zu schließen. Er fordert jedoch eine mitbestimmungsrechtlich ordnungsgemäße Durchführung nach § 87 Abs. 1 Nr. 8, 10 BetrVG. Die bisherigen Verhandlungen sind gescheitert, weil die Arbeitgeberin den Entwurf des Pensionsbuyout-Vertrages nicht offengelegt hat und die Auswirkungen auf die Versorgungsberechtigten nicht hinreichend dargestellt wurden.

GBR-Vorsitzender Lukas Kreidemann erklärt: &#8222;Die Betriebsräte werden keine Schließung unterschreiben, bevor nicht klar ist, was die Rente für jeden einzelnen Kollegen bedeutet."

RA Dr. Wolfram Plöger-Heinekamp &#183; Plöger Maibach Rechtsanwälte &#183; 01.03.2026
"""))
    elems.append(sp(4))

    elems += mini_header("Erwiderung Treuenfels Yamamoto – eingereicht 14.03.2026")
    elems.append(P("""Treuenfels Yamamoto Rechtsanwälte PartmbB &#183; Düsseldorf, 14.03.2026

An das Arbeitsgericht Düsseldorf – 7. Kammer – 7 BV 412/26

<b>Erwiderung der Arbeitgeberin</b>

Die Meissner Rheinwerk AG tritt dem Antrag des GBR nicht entgegen. Sie begrüßt die Einsetzung einer Einigungsstelle, da dies dem beschleunigten Projektfortschritt dienlich ist.

Hinsichtlich der Vorsitzenden: Die Arbeitgeberin stimmt dem Vorschlag Frau Dr. Wupperhain-Stein zu. Als Beisitzer benennt die Arbeitgeberin:
1. Dr. Günther Vossenkamp-Bleeke (Rechtsanwalt, Düsseldorf, Fachmann bAV)
2. Prof. Dr. Karin Stelzmüller-Frei (HS Bochum, Arbeitsrecht)
3. Hendrik Bruns-Meterding (RA, Düsseldorf)

Wir bitten darum, die erste Sitzung auf den 12.03.2026 anzusetzen [Anm.: der Antrag war bereits beschleunigt bearbeitet worden, Termin rückwirkend eingetragen].

Prof. Dr. Adalbert von Sompeh-Ostermann &#183; Treuenfels Yamamoto PartmbB
"""))
    elems.append(sp(4))

    elems += mini_header("Beschluss ArbG Düsseldorf – Einsetzung Einigungsstelle")
    elems.append(P("""<b>ARBEITSGERICHT DÜSSELDORF</b>
<b>Beschluss</b>
7 BV 412/26

Die Einigungsstelle für den Regelungsgegenstand &#8222;Schließung der leistungsorientierten Versorgungssysteme / Neuregelung bAV" wird eingesetzt. Den Vorsitz führt <b>Richterin am Arbeitsgericht a.D. Dr. Hannelore Wupperhain-Stein</b>. Jede Seite benennt drei Beisitzer. Die Einigungsstelle kann durch Beschluss mit Mehrheit der Stimmen entscheiden, sofern keine Einigung der Parteien erzielt wird.

Düsseldorf, den 05.03.2026
gez. Vors. Richter am ArbG Dr. Kempf-Lutzenberger
(7. Kammer)
"""))
    elems.append(sp(4))

    # Sitzungsprotokoll 1
    elems += mini_header("Sitzungsprotokoll Nr. 1 – Einigungsstelle – 12. März 2026")
    elems += fax_block([
        "EINIGUNGSSTELLE BEI DER MEISSNER RHEINWERK AG",
        "ArbG Düsseldorf 7 BV 412/26",
        "SITZUNGSPROTOKOLL Nr. 1  |  12.03.2026  |  10:00-16:45 Uhr",
        "Tagungsort: Konferenzraum Königsallee 92 (Treuenfels Yamamoto)",
        "",
        "ANWESEND:",
        "Vorsitz: Dr. Hannelore Wupperhain-Stein",
        "Beisitzer AG: Dr. Vossenkamp-Bleeke, Prof. Dr. Stelzmüller-Frei, Bruns-Meterding",
        "Beisitzer GBR: RA Dr. Plöger-Heinekamp, Lukas Kreidemann (GBR-Vors.), 2 weitere",
        "Protokoll: Stud.Jur. Tobias Wendelstein-Raber (Trainee TY)",
        "",
        "TOP 1: Verfahrensordnung – einstimmig beschlossen.",
        "TOP 2: Darstellung AG – Prof. von Sompeh-Ostermann stellt Projekt RHEINGOLD vor.",
        "  Wesentliche Punkte: DBO EUR 2,4 Mrd., Future-Service-Stopp 01.01.2027,",
        "  Buyout Rentner, CTA-Sicherung, Sozialplan-Entwurf liegt vor.",
        "TOP 3: GBR-Forderungskatalog (Dr. Plöger-Heinekamp):",
        "  (a) Vollständige Offenlegung IAS-19-Gutachten",
        "  (b) Alternativen zur Schließung (DC-Fortführung möglich?)",
        "  (c) Höhere Abfindung für Anwärter mit hohen Past-Service-Anwartschaften",
        "  (d) Einbeziehung der Sonderzusagen FK-001–FK-047 in Sozialplan",
        "",
        "ERGEBNIS: Keine Einigung in Sitzung 1. Fortsetzungssitzung: 26.03.2026.",
        "",
        "[Beisitzer Kreidemann per Fax zugeschaltet, da Zugverspätung ICE 792 Köln-DUS]",
        "FAX-EMPFANG: 10:23 Uhr, Gerät SHARP UX-350, OK",
    ], sender="Einigungsstelle TY", receiver="Alle Beisitzer", date="12.03.2026 18:00", pages="3/3")

    elems += mini_header("Sitzungsprotokoll Nr. 2 – 26. März 2026 (Auszug)")
    elems.append(P("""Sitzung 2 vom 26.03.2026 befasste sich schwerpunktmäßig mit:
— Verlesung des IAS-19-Gutachtens Hellmrich-Vogt (K-VO-7)
— Diskussion Drei-Stufen-Theorie (Prof. von Sompeh-Ostermann erläutert GS 1/82 und 3 AZR 392/06; Dr. Plöger-Heinekamp: &#8222;Wir bestreiten den sachlichen Grund nicht grundsätzlich, aber die Datenbasis ist unvollständig")
— GBR fordert Einsicht in SPA-Verhandlungen RHEINORGANICS / Albion Bridge
— AG lehnt ab: &#8222;Vertraulich, kein Mitbestimmungsrecht bei M&A nach § 106 BetrVG Abs. 3"
— Einigung zu TOP (a): IAS-19-Gutachten wird in geschwärzter Fassung offengelegt (K-VO-7-GBR)
Nächste Sitzung: 14.04.2026
"""))
    elems.append(handw("A.v.S.-O.: Plöger sucht Streit – ignorieren, Einigungsstelle wird's richten. — A."))

    elems += mini_header("Sitzungsprotokoll Nr. 3 – 14. April 2026 (Auszug)")
    elems.append(P("""Sitzung 3 vom 14.04.2026: Partieller Kompromiss erzielt:
— Sozialplan-Grundlagen vereinbart (Wahlmodell A/B/C, vgl. D-8)
— Schließungsdatum auf 01.04.2027 vorgezogen (statt 01.01.2027) nach GBR-Wunsch
— Offene Punkte: Sonderzusagen FK-Gruppe, Anpassung § 16 BetrAVG, Buyout-Garantien
— GBR kündigt Beschwerde LAG Düsseldorf an (14 TaBV 88/26) wegen Verfahrensfragen
— Nächste Sitzung: nach LAG-Termin
Vorsitz Dr. Wupperhain-Stein: &#8222;Ich sehe Einigungspotenzial bis Sommer 2026."
"""))
    elems.append(PageBreak())
    return elems


def build_sozialplan():
    """14. Sozialplan-Entwurf"""
    elems = []
    elems += section_header("SOZIALPLAN-ENTWURF (PENSION-BESTANDTEILE)", "Meissner Rheinwerk AG / Gesamtbetriebsrat &#183; Stand: 20.04.2026 (Verhandlungsstand)")
    elems.append(Paragraph("ENTWURF – NICHT UNTERZEICHNET – Verhandlungsstand nach Einigungsstelle Sitzung 3", S_WARN))
    elems.append(sp(6))

    elems.append(P("""<b>SOZIALPLAN</b>
gemäß §§ 111, 112 BetrVG
zwischen der Meissner Rheinwerk AG (Arbeitgeberin)
und dem Gesamtbetriebsrat der Meissner Rheinwerk AG (GBR)

<b>Vorbemerkung:</b> Dieser Sozialplan regelt ausschließlich die Bestandteile, die mit der Schließung der leistungsorientierten Versorgungssysteme (Defined Benefit, VO 1973, VO 1981, Chemie-Nord-TV) zum 01.04.2027 zusammenhängen. Soziale Absicherungsleistungen für Stellenabbau sind in einem separaten Interessenausgleich geregelt.

<b>§ 1 Geltungsbereich</b>

Dieser Sozialplan gilt für alle zum 01.04.2027 aktiven Anwärter der VO 1973 (312 Personen), VO 1981 (1.284 Personen) und des Chemie-Nord-TV (2.105 Personen), die im Zeitpunkt der Schließung ununterbrochen betriebszugehörig sind.
"""))

    elems.append(Paragraph("§ 2 Wahlmodelle (Optionen A/B/C)", S_H3))
    wahl_data = [
        ["Merkmal", "Option A: Standard", "Option B: Einmalzahlung", "Option C: Erhöhte Rente"],
        ["Beschreibung", "Einfrieren der PA auf Ist-Stand, Weiterführung als eingeschlafenes Anrecht", "Einmalige Abfindung = 40 % der DBO-Quote als Barwert", "Erhöhung der PA um 8 % Bonus, Verzicht auf Abfindung"],
        ["Voraussetzung", "Alle Berechtigten", "Mind. 5 J. Betriebszugehörigkeit", "Mind. 15 J. und Alter > 55"],
        ["PSVaG-Absicherung", "Ja (unverändert)", "Nein (nach Zahlung erloschen)", "Ja"],
        ["Steuerliche Behandlung", "§ 3 Nr. 9a EStG prüfen", "§ 3 Nr. 9a EStG (Freigrenze?)", "Keine Sonderbehandlung"],
        ["Wahlrecht bis", "30.06.2027", "30.06.2027", "30.06.2027"],
        ["Schätzvolumen", "— (kein Aufwand)", "EUR 35 Mio.", "EUR 18 Mio."],
    ]
    tbl = Table(wahl_data, colWidths=[2.5*cm, 3.7*cm, 3.7*cm, 3.6*cm])
    tbl.setStyle(table_default_style())
    elems.append(tbl)
    elems.append(sp(6))

    elems.append(P("""<b>§ 3 Übergangsregelung für rentennahe Jahrgänge</b>

Für Anwärter, die zum Schließungsdatum 01.04.2027 älter als 60 Jahre und noch nicht 65 Jahre alt sind (Übergangsjahrgänge 1962–1967), gilt folgendes:

Die erdiente Anwartschaft wird nicht nach dem m/n-Quotienten des § 2 BetrAVG berechnet, sondern nach der günstigeren Methode: Es wird der Betrag zugrunde gelegt, der sich ergibt, wenn der Anwärter zum Schließungsdatum aus dem Dienst ausgeschieden wäre. Das Ergebnis ist verglichen mit dem m/n-Quotienten und der höhere Betrag wird gewählt (sog. Besitzstandsklausel für rentennahe Jahrgänge).

<b>§ 4 Anpassungsverpflichtung nach § 16 BetrAVG</b>

Die eingefrorenen Anwartschaften nehmen weiterhin an der Anpassungsprüfung nach § 16 BetrAVG teil. Für Anwärter der VO 1981 mit dynamischer Lohnbindung: Die Anpassungspflicht orientiert sich nach der Schließung am Verbraucherpreisindex (nicht mehr am Tarifgehalt); eine hiervon abweichende Regelung bedarf einer Änderung des Chemie-Nord-TV (vgl. § 17 Abs. 3 BetrAVG).

<b>§ 5 Buyout-Absicherung</b>

Soweit die deutschen Rentnerbestände in die Hanseatica Lebensversicherung AG überführt werden, tritt die Hanseatica in alle Verpflichtungen des Versorgungsschuldners gegenüber den Rentnern ein (§ 1b Abs. 2 BetrAVG). Eine Zustimmung der Rentner ist nicht erforderlich (BAG 3 AZR 304/13, Rn. 25 ff. zur rechtsgeschäftlichen Schuldübernahme ohne Mitwirkung des Begünstigten).

<b>§ 6 Kommunikationspflichten</b>

Die Arbeitgeberin verpflichtet sich, jeden Anwärter schriftlich über seine einzufrierende Anwartschaft zu informieren (Auskunftspflicht § 4a BetrAVG). Die Mitteilung hat bis spätestens 01.02.2027 zu erfolgen und muss den einzufrierende Betrag nach jeder der drei Versorgungsordnungen sowie die Wahloptionen enthalten.

[ENTWURF – verbleibende offene Punkte: §§ 7–12, insbesondere Sonderzusagen FK, Datenschutz-Annex, Einigungsstellenvorbehalt bei Streitigkeiten]
"""))
    elems.append(PageBreak())
    return elems


def build_kyoto_module():
    """15. Kyoto-Modul"""
    elems = []
    elems += section_header("KYOTO-MODUL: MIGRATION JAPANISCHES DB-SYSTEM → DC", "Memo Yuki Yamamoto-Brennecke &#183; Treuenfels Yamamoto Kyoto &#183; 15.03.2026")

    # Kyoto letterhead
    elems.append(sp(4))
    logo_kyoto = """
    ┌─────────────────────────────────────────────────────────────────┐
    │   トロイエンフェルス・ヤマモト法律事務所                           │
    │   TREUENFELS YAMAMOTO HORITSU JIMUSHO                          │
    │   Gion-Higashi, Shijō-dōri-Ostseite &#183; 605-0073 Kyoto, Japan   │
    │   Tel.: +81-75-XXX-XXXX &#183; Fax: +81-75-XXX-XXXX               │
    │   yuki.yamamoto@ty-law.jp &#183; www.ty-law.de/kyoto               │
    └─────────────────────────────────────────────────────────────────┘
    """
    elems.append(Paragraph("<pre>" + logo_kyoto + "</pre>", S_MONO))
    elems.append(sp(6))

    # Hanko stamp simulation
    elems.append(HankoStamp(text="承認", size=50))
    elems.append(sp(4))
    elems.append(Paragraph("Offizielles Kyoto-Büro-Memo | Higashiyama-Stempel (承認 = Genehmigt)", S_SMALL_GRAY))
    elems.append(sp(8))

    # Bilingual memo header
    elems.append(Paragraph("<b>MEMO – BILINGUAL DEUTSCH / JAPANISCH (AUSZUG)</b>", S_CENTER_B))
    elems.append(Paragraph("<b>Migration 確定給付企業年金 (DB-System) → 確定拠出年金 (DC-System)</b>", S_CENTER_B))
    elems.append(sp(4))

    # Build two-column bilingual layout
    de_col = [
        "<b>An:</b> Prof. Dr. Adalbert von Sompeh-Ostermann,\nDr. Constanze Brindeau-Lorbach",
        "<b>Von:</b> Yuki Yamamoto-Brennecke",
        "<b>Datum:</b> 15. März 2026",
        "<b>Betrifft:</b> Migration japanisches DB-System der\nマイスナー・ライン化学株式会社 zum DC-System",
        "",
        "<b>I. Rechtliche Grundlage</b>",
        "Das DB-System der japanischen Tochtergesellschaft basiert auf der 確定給付企業年金法 (Kakutei Kyufu Kigyo Nenkin Ho, DB Corporate Pension Law, nachfolgend 'DB-Gesetz'). Die Migration zum DC-System erfordert gemäß Art. 4 und Art. 90 ff. des DB-Gesetzes die Genehmigung des Ministry of Health, Labour and Welfare (MHLW, 厚生労働省).",
        "",
        "<b>II. Genehmigungsverfahren MHLW</b>",
        "Das Genehmigungsverfahren (Art. 4 Kakutei Kyufu) wurde am 01.03.2026 eingeleitet. Das MHLW hat eine Bearbeitungsfrist von 6 Monaten angekündigt (Zieldatum: 01.09.2026). Ein erster Informationsaustausch mit dem Sachbearbeiter des MHLW (Büro Tokyo) fand am 10.03.2026 statt.",
        "",
        "<b>III. Tokyo District Court</b>",
        "Im Parallelverfahren 令和8年(ワ)第4421号 (Tokyo District Court) sind Ansprüche eines ehemaligen Vorstandsmitglieds der japanischen Tochter aus der DB-Zusage anhängig. Wir haben am 14.03.2026 eine Klageerwiderung eingereicht.",
        "",
        "<b>IV. Empfehlung</b>",
        "Wir empfehlen, das DC-System ab 01.04.2027 einzuführen (nach MHLW-Genehmigung), zunächst mit Arbeitgeberbeitrag 5 % des Grundgehalts, ohne Arbeitnehmerfinanzierung (Pflichtteil). Eine freiwillige AN-Komponente ist ab 2028 geplant.",
    ]
    jp_col = [
        "宛先：アダルベルト・フォン・ノイフェルト=ゾンペー教授\nコンスタンツェ・ブランドー=ローバッハ博士",
        "差出人：山本・ブレネッケ・ゆき",
        "日付：2026年3月15日",
        "件名：マイスナー・ライン化学株式会社の確定給付年金制度\nから確定拠出年金制度への移行について",
        "",
        "一. 法的根拠",
        "日本子会社の確定給付企業年金は、確定給付企業年金法（以下「DB法」）に基づいています。確定拠出年金制度への移行には、DB法第4条および第90条以下に基づき、厚生労働省の認可が必要です。",
        "",
        "二. 認可手続き（厚生労働省）",
        "認可申請は2026年3月1日に提出されました。厚生労働省は6ヶ月の審査期間を予告しており（目標日：2026年9月1日）、2026年3月10日に担当官との初回協議を行いました。",
        "",
        "三. 東京地方裁判所",
        "並行して、令和8年（ワ）第4421号として、日本子会社の元役員が確定給付年金に関する請求を提起しています。2026年3月14日に答弁書を提出しました。",
        "",
        "四. 推薦事項",
        "厚生労働省の認可取得後、2027年4月1日より確定拠出年金制度を導入することを推薦します。当初は会社拠出5%（基本給対比）とし、任意の従業員拠出は2028年より開始予定です。",
    ]

    # Create bilingual table
    rows = []
    max_rows = max(len(de_col), len(jp_col))
    for i in range(max_rows):
        de = de_col[i] if i < len(de_col) else ""
        jp = jp_col[i] if i < len(jp_col) else ""
        rows.append([Paragraph(de, S_JP_DE) if de else "", Paragraph(jp, S_JP_DE) if jp else ""])

    bi_tbl = Table(rows, colWidths=[7.5*cm, 7.5*cm])
    bi_tbl.setStyle(TableStyle([
        ("VALIGN",     (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",(0,0),(-1,-1), 6),
        ("RIGHTPADDING",(0,0),(-1,-1), 6),
        ("TOPPADDING", (0,0),(-1,-1), 4),
        ("BOTTOMPADDING",(0,0),(-1,-1), 4),
        ("INNERGRID",  (0,0), (-1,-1), 0.4, HexColor("#dddddd")),
        ("BOX",        (0,0), (-1,-1), 0.8, MID_BLUE),
        ("BACKGROUND", (0,0), (0,-1), HexColor("#f0f4fc")),
        ("BACKGROUND", (1,0), (1,-1), HexColor("#f9f5f0")),
    ]))
    elems.append(bi_tbl)
    elems.append(sp(8))

    # Handwritten Japanese note in Latin transcription
    elems.append(hr(SAKURA_PINK))
    elems.append(Paragraph("<b>Handschriftlich nachgereichte Notiz (Yuki Yamamoto-Brennecke, 16.03.2026, rote Tinte):</b>", S_H4))
    elems.append(Paragraph(
        '&#8222;Treuenfels-sensei e: kakutei-kyuufu-saraba, DC-koso michi nari. — Y. Yamamoto"',
        make_style("jp_note", fontName="Times-Italic", fontSize=11, leading=16, textColor=HANDW_RED, alignment=TA_CENTER)
    ))
    elems.append(Paragraph(
        "(Übersetzung: &#8222;An Herrn Treuenfels: Lebewohl der Leistungszusage – der DC-Weg ist der einzig richtige.&#8221;)",
        S_SMALL_GRAY
    ))
    elems.append(sp(4))

    # Anlagenverzeichnis JP
    elems.append(Paragraph("Anlagen (Auszug) – vollständig Sonderakte III:", S_H4))
    jp_anlagen = [
        "K-JP-1: Bestehende DB-Satzung マイスナー・ライン化学株式会社",
        "K-JP-2: DB-Gesetz (確定給付企業年金法) Art. 4, 90-95 (inoffizielle Übersetzung)",
        "K-JP-3: MHLW-Antragsunterlagen (Einreichung 01.03.2026)",
        "K-JP-4: Aktuargutachten japanischer Bestand (Hellmrich-Vogt / japanischer Koaktuar)",
        "K-JP-5 bis K-JP-13: Korrespondenz MHLW-Büro Tokyo",
        "K-JP-14: Klageschrift Tokyo District Court 令和8年(ワ)第4421号",
        "K-JP-15: Klageerwiderung Treuenfels Yamamoto Kyoto 14.03.2026",
        "K-JP-16 bis K-JP-31: Anlagen zur Klageerwiderung (vgl. Sonderakte III)",
    ]
    for a in jp_anlagen:
        elems.append(Paragraph(a, S_BULLET))
    elems.append(PageBreak())
    return elems


def build_us_module():
    """16. US-Modul"""
    elems = []
    elems += section_header("US-MODUL: ERISA / PBGC / 401(k)", "Holcombe Pratchett & Lieberman LLP (Boston) &#183; File No. HPL-2026-MRW-0007")
    elems.append(sp(4))

    # US letterhead
    us_header = """
    ╔══════════════════════════════════════════════════════════════════╗
    ║  HOLCOMBE PRATCHETT & LIEBERMAN LLP                             ║
    ║  Federal Street 200 &#183; Boston, MA 02110                         ║
    ║  Tel.: +1 (617) 555-0140  |  Fax: +1 (617) 555-0199           ║
    ║  Employee Benefits & ERISA Practice Group                      ║
    ║  File No.: HPL-2026-MRW-0007                                   ║
    ╚══════════════════════════════════════════════════════════════════╝
    """
    elems.append(Paragraph("<pre>" + us_header + "</pre>", S_MONO))
    elems.append(sp(6))

    elems.append(P("""<b>PRIVILEGED AND CONFIDENTIAL – ATTORNEY-CLIENT COMMUNICATION</b>
WORK PRODUCT DOCTRINE APPLIES

<b>MEMORANDUM</b>

TO:     Prof. Dr. Adalbert von Sompeh-Ostermann, Treuenfels Yamamoto (Lead Counsel)
        Henrick Otterbach-Veltheim, CFO, Meissner Rheinwerk AG
FROM:   Matthew B. Holcombe III, Partner (ERISA)
        Rebecca J. Lieberman-Strauss, Senior Associate (Benefits)
DATE:   March 22, 2026
RE:     ERISA Title IV / PBGC Implications of RHEINORGANICS Carve-Out and
        US DB Plan Status (Meissner Specialty Chemicals Inc., Wilmington DE / Houston TX)
"""))

    elems.append(Paragraph("I. Executive Summary", S_H3))
    elems.append(P("""The proposed carve-out of RHEINORGANICS to Albion Bridge Capital Partners LLP raises significant ERISA Title IV issues. Meissner Specialty Chemicals Inc. ("MSC-US") maintains a defined benefit plan subject to ERISA Title IV (the "MSC DB Plan") with approximately 820 participants (310 active, 510 retired/vested). The MSC DB Plan is insured by the Pension Benefit Guaranty Corporation ("PBGC") under 29 U.S.C. §§ 1301 et seq. (ERISA § 4001 et seq.).

Key risks:
(1) <b>PBGC Notice Requirements:</b> The carve-out transaction may constitute a "reportable event" under ERISA § 4043 and 29 C.F.R. Part 4043, triggering 30-day advance notice to the PBGC.
(2) <b>Controlled Group Liability:</b> Under ERISA § 4001(b)(1), all members of the controlled group are jointly and severally liable for unfunded vested benefits ("UVBs"). Post-carve-out, MSC-US exits the Meissner controlled group, potentially triggering a deemed termination under ERISA § 4062(e).
(3) <b>PBGC Variable Rate Premium:</b> The MSC DB Plan has UVBs of approximately USD 42 million (per most recent Form 5500, Plan Year 2024). The PBGC variable rate premium is $52 per $1,000 of UVBs (2026 rate), resulting in an annual premium of approximately USD 2.18 million.
(4) <b>Section 4062(e) Cessation of Operations:</b> If RHEINORGANICS operations are transferred to Albion Bridge, and MSC-US ceases operations at one or more facilities, ERISA § 4062(e) may impose liability. See Pension Benefit Guaranty Corp. v. Republic Industries Inc., 629 F.2d 645 (6th Cir. 1980).
"""))

    elems.append(Paragraph("II. ERISA Title IV Analysis – Controlled Group Liability", S_H3))
    elems.append(P("""<b>A. Controlled Group Composition</b>

Under ERISA § 4001(b)(1) and Treasury Regulation § 1.414(b)-1, the Meissner controlled group currently includes all entities in which Meissner Rheinwerk AG (German parent) directly or indirectly owns at least 80% of the voting power. This includes MSC-US (100% owned). Post-transaction, if Albion Bridge acquires RHEINORGANICS (which includes MSC-US), MSC-US would exit the controlled group.

<b>B. Deemed Termination Risk</b>

ERISA § 4062(e) applies when a plan sponsor ceases operations at a facility if this results in a significant reduction in plan participants. We do not currently believe § 4062(e) applies to the carve-out per se (because operations are transferred, not terminated), but this requires careful structuring. See PBGC Opinion Letter 2017-01.

<b>C. PBGC Clearance Procedure</b>

We strongly recommend initiating informal pre-clearance discussions with the PBGC's Corporate Finance and Restructuring Department (CFR) prior to transaction closing. This is consistent with PBGC's voluntary early warning program (29 C.F.R. § 4010; PBGC Technical Update 14-1).

Pursuant to 29 U.S.C. § 1303(e) (ERISA § 4003(e)), the PBGC has authority to seek termination if it determines that the plan's continuation poses an "unreasonable risk" of large losses. We do not currently believe this threshold is met given the plan's funded status (approx. 91% as of December 31, 2024, per actuarial valuation by Hellmrich-Vogt US partner Green & Sandoval LLC).
"""))

    elems.append(Paragraph("III. 401(k) Plan – Amendment for Carve-Out", S_H3))
    elems.append(P("""MSC-US also maintains a 401(k) plan (the "MSC 401(k) Plan") with approximately 1,980 participants (active). Under the proposed transaction structure, active MSC-US employees transferring to Albion Bridge affiliate will cease to be eligible for the MSC 401(k) Plan.

<b>Required Actions:</b>
1. Plan Amendment: Amend the MSC 401(k) Plan to exclude transferred employees effective as of the closing date. [Draft Amendment attached as Exhibit A]
2. QDRO Procedures: Update QDRO (Qualified Domestic Relations Order) procedures to address the transition period.
3. Blackout Period: Pursuant to ERISA § 101(i) and 29 C.F.R. § 2520.101-3, a "blackout period" notice must be provided no less than 30 days before the blackout begins.
4. Spin-off or Partial Termination: If more than 20% of plan participants are terminated within a 12-month period, this may constitute a "partial termination" under IRC § 411(d)(6), triggering full vesting for all affected participants.

The 401(k) plan amendment draft (Exhibit A) addresses items 1-3. We recommend that Green & Sandoval LLC review the actuarial determination of whether a partial termination occurs.
"""))

    elems.append(P("""<b>Footnotes (Bluebook):</b>

¹ Employee Retirement Income Security Act of 1974, Pub. L. No. 93-406, 88 Stat. 829 (codified as amended at 29 U.S.C. §§ 1001–1461).
² Pension Benefit Guaranty Corp. v. LTV Corp., 496 U.S. 633, 636 (1990) (describing PBGC's role as insurer of private defined benefit plans).
³ 29 C.F.R. § 4043.25 (reportable event: distribution to a substantial owner).
⁴ Rev. Rul. 2007-43, 2007-28 I.R.B. 45 (partial termination determination).
⁵ I.R.C. § 411(d)(6) (anti-cutback rule protecting accrued benefits).
⁶ 29 U.S.C. § 1054(b)(1)(G) (ERISA § 204(b)(1)(G), minimum accrual rules).
⁷ Akers v. Palmer, 71 F.3d 226, 229 (6th Cir. 1995) (controlled group ERISA liability).

<i>Matthew B. Holcombe III &#183; Rebecca J. Lieberman-Strauss</i>
<i>Holcombe Pratchett & Lieberman LLP &#183; Boston, MA &#183; March 22, 2026</i>
"""))
    elems.append(PageBreak())
    return elems


def build_uk_module():
    """17. UK-Modul"""
    elems = []
    elems += section_header("UK-MODUL: SECTION 75 / TPR CLEARANCE", "Pemberton Hawkesworth Solicitors (London) &#183; Meissner Rhine Industries Ltd.")
    elems.append(sp(4))

    uk_header = """
    ┌─────────────────────────────────────────────────────────────┐
    │  PEMBERTON HAWKESWORTH SOLICITORS                           │
    │  120 Aldersgate Street &#183; London EC1A 4JQ                   │
    │  Tel.: +44 20 7XXX XXXX &#183; DX 462 London/City              │
    │  Pensions & Employment Practice                            │
    │  Our ref.: PHW/2026/MRI/P-001                             │
    └─────────────────────────────────────────────────────────────┘
    """
    elems.append(Paragraph("<pre>" + uk_header + "</pre>", S_MONO))
    elems.append(sp(6))

    elems.append(P("""<b>PRIVILEGED AND CONFIDENTIAL</b>

<b>MEMORANDUM</b>

TO:     Prof. Dr. Adalbert von Sompeh-Ostermann, Treuenfels Yamamoto
FROM:   Rupert J. Hawkesworth-Crane, Partner (Pensions)
        Sophie Alcott-Pemberton, Senior Associate
DATE:   20 March 2026
RE:     Meissner Rhine Industries Ltd. UK DB Pension Scheme – Section 75 Employer Debt
        and TPR Clearance Strategy in connection with RHEINORGANICS Carve-Out
"""))

    elems.append(Paragraph("1. Background", S_H3))
    elems.append(P("""Meissner Rhine Industries Ltd. ("MRI"), incorporated in England and Wales (company no. 08847213), maintains the Meissner Rhine Industries Pension Scheme (the "Scheme"), a defined benefit occupational pension scheme. The Scheme was last valued as of 31 March 2024, showing a Technical Provisions deficit of GBP 47.2 million (assets: GBP 218.3m; liabilities: GBP 265.5m on a Technical Provisions basis).

The Scheme has approximately 1,100 members: 412 active members, 488 deferred members, and 200 pensioners.

MRI is the principal employer of the Scheme. Meissner Rheinwerk AG (Germany) is the ultimate parent but is not a "connected" or "associated" person under section 38 of the Pensions Act 2004 for Section 75 purposes (see below).
"""))

    elems.append(Paragraph("2. Section 75 Employer Debt", S_H3))
    elems.append(P("""Section 75 of the Pensions Act 1995 (as amended by the Pensions Act 2004 and the Occupational Pension Schemes (Employer Debt) Regulations 2005, SI 2005/678) provides that a debt ("Section 75 debt") becomes due from an employer to a defined benefit scheme on the occurrence of certain "employer debt trigger events".

The proposed carve-out of RHEINORGANICS, if it results in MRI ceasing to have any active members in the Scheme (i.e., all active members are either transferred to a Albion Bridge entity or made redundant), would constitute an <b>"insolvency event"</b> or <b>"withdrawal event"</b> trigger under SI 2005/678 Regulation 6.

The Section 75 debt is calculated on a "buy-out" basis (rather than the Technical Provisions basis), which assumes the Scheme liabilities are transferred to an insurance company. The buy-out deficit is estimated at <b>GBP 89.4 million</b> (per indicative quote from Standard Life Assurance Ltd., February 2026).

This Section 75 debt, if triggered, would be immediately due and payable by MRI, and potentially by any connected/associated entities (including the Meissner Rheinwerk AG parent) under section 75A of the 1995 Act.
"""))

    elems.append(Paragraph("3. TPR Clearance Strategy", S_H3))
    elems.append(P("""The Pensions Regulator ("TPR") has power under sections 38-51 of the Pensions Act 2004 to issue Contribution Notices ("CNs") and Financial Support Directions ("FSDs") where a transaction materially reduces the employer's ability to fund the Scheme.

We recommend a <b>Clearance Application</b> under section 42 of the Pensions Act 2004 and the Clearance Procedure Guidance (TPR, March 2014, updated January 2024). Clearance provides statutory comfort that TPR will not issue a CN or FSD in respect of a particular transaction.

<b>Key Steps:</b>
(1) Negotiate a <b>Pension Protection Package</b> ("PPP") with the Scheme Trustee, which may include:
    — A cash injection to reduce the buy-out deficit
    — A bank guarantee or parent company guarantee from Meissner Rheinwerk AG
    — A contingent asset arrangement (e.g., floating charge over MRI assets)
(2) Submit the Clearance Application to TPR with full details of the transaction, the PPP, and actuarial evidence of the scheme's funded position.
(3) TPR typically responds to Clearance Applications within 6–8 weeks (but can take longer for complex transactions).

<b>Indicative Pension Protection Package:</b>
— Minimum cash injection: GBP 25 million (to reduce buy-out deficit below GBP 64.4m)
— Parent guarantee (Meissner Rheinwerk AG): GBP 40 million for 7 years
— These are initial negotiating positions; the Scheme Trustee (St. James's Fiduciary Ltd.) has not yet been formally consulted.

<b>Timing Risk:</b> The transaction cannot close without TPR Clearance (or Albion Bridge accepting the risk, which is unlikely). We estimate the TPR process could take 4–6 months, which fits within the overall timeline if initiated by 01 June 2026.
"""))
    elems.append(Paragraph("Pemberton Hawkesworth Solicitors &#183; London, 20 March 2026", S_SMALL_GRAY))
    elems.append(PageBreak())
    return elems


def build_ma_annex():
    """18. M&A-Pension-Annex"""
    elems = []
    elems += section_header("M&A-PENSION-ANNEX ZUM SPA", "Carve-out RHEINORGANICS &#183; Albion Bridge Capital Partners LLP &#183; Stand: 15.04.2026")
    elems.append(Paragraph("STRENG VERTRAULICH – TRANSAKTIONSDOKUMENT – ENTWURF", S_WARN))
    elems.append(sp(6))

    elems.append(P("""<b>PENSION SCHEDULE</b>
(als Anlage zu Schedule 12 des Share Purchase Agreement zwischen der Meissner Rheinwerk AG als Verkäuferin und ABCP RHEINORGANICS BIDCO LTD. (Albion Bridge Capital Partners LLP-Tochter) als Käuferin)

<b>Hintergrund:</b>
Die Pension-Verpflichtungen der Sparte RHEINORGANICS sind integraler Bestandteil der SPA-Verhandlungen und wurden von Albion Bridge als potenzielle Dealbreaker identifiziert. Folgende Jurisdiktionen sind betroffen: DE, UK, US (MSC-US), JP.

<b>Section 12.1 – Definitionen</b>

&#8222;<b>Pension Liabilities</b>" bezeichnet alle Leistungsverpflichtungen (Defined Benefit und Defined Contribution) der Zielgruppe gegenüber aktiven und ehemaligen Mitarbeitern der Sparte RHEINORGANICS, soweit diese Verpflichtungen auf Dienstzeiten vor dem Closing beruhen.

&#8222;<b>Pre-Closing Pension Deficit</b>" ist der Unterschiedsbetrag zwischen der DBO der Pension Liabilities und dem Marktwert der zugeordneten Plan Assets, jeweils bezogen auf den Closing-Stichtag, berechnet nach IFRS IAS 19.

&#8222;<b>Carve-out Pension Adjustment</b>" ist eine preisanpassende Zahlung, die sich aus der Differenz zwischen dem vorläufigen Pre-Closing Pension Deficit (geschätzt EUR 84 Mio. für RHEINORGANICS) und dem tatsächlichen Pre-Closing Pension Deficit (gemäß Completion Accounts) ergibt.

<b>Section 12.2 – Pre-Closing Obligations (Verkäuferin)</b>

Die Verkäuferin verpflichtet sich, bis zum Closing:
(a) Die RHEINORGANICS-Anwärter aus dem deutschen DB-System (VO 1973, VO 1981) herauszulösen und in einen separaten Pensionsfonds zu überführen oder eine individual-vertragliche Übertragungsvereinbarung zu treffen;
(b) Den PSVaG über die Transaktion zu informieren (§ 14 Abs. 1 Nr. 9 BetrAVG, Pflichtmitteilung);
(c) Keine neuen DB-Zusagen an RHEINORGANICS-Mitarbeiter zu erteilen;
(d) Eine aktuarielle Bewertung des Pre-Closing Pension Deficit durch Hellmrich-Vogt (für DE/JP) und Green & Sandoval LLC (für US) spätestens 15 Tage vor Closing zu erstellen.
"""))

    elems.append(P("""<b>Section 12.3 – Pension Warranties der Verkäuferin</b>

Die Verkäuferin sichert zu und gewährleistet (jeweils bezogen auf Signing Date):

12.3.1 Sämtliche Versorgungsordnungen, -tarifverträge und Einzelzusagen der RHEINORGANICS-Entitäten sind vollständig und korrekt im Data Room offengelegt (K-MA-1 bis K-MA-12).

12.3.2 Die DBO der deutschen RHEINORGANICS-Bestände beträgt EUR 184.000.000 (einhundertvierundachtzig Millionen Euro) gemäß IAS-19-Bewertung Hellmrich-Vogt vom 31.12.2025 (K-MA-13).

12.3.3 Die Versorgungszusagen der RHEINORGANICS-Mitarbeiter sind nicht durch kollektivrechtliche Vereinbarungen gesperrt, die einer Übertragung auf die Käuferin entgegenstehen, mit Ausnahme der Einigungsstellen-Verfahrens ArbG Düsseldorf 7 BV 412/26 betreffend den GBR-Widerspruch zur DB-Schließung, über das vollständig informiert wurde.

12.3.4 Die CTA-Treuhandstruktur (CTA Rheinland Trust e.V.) erstreckt sich NICHT auf RHEINORGANICS-Bestände, die vor dem 01.01.2019 begründet wurden (Carve-out-Tranche A); für Bestände ab 2019 (Carve-out-Tranche B, EUR 22 Mio. DBO) besteht anteilige CTA-Sicherung.

12.3.5 Kein RHEINORGANICS-Mitarbeiter hat eine Einzelzusage erhalten, die über das Versorgungsniveau der VO 1995 hinausgeht (Ausnahme: FK-017, FK-023, FK-031 gem. Anhang 12-B, gesondert offengelegt).

<b>Section 12.4 – Pension Indemnity</b>

Die Verkäuferin stellt die Käuferin und alle Zielgesellschaften von sämtlichen Schäden, Kosten, Verfahren und Verbindlichkeiten frei, die aus folgenden Sachverhalten resultieren:

(a) Pre-Closing-Verbindlichkeiten im Rahmen des PSVaG-Insolvenzschutzes für RHEINORGANICS-Rentner, soweit diese auf Dienstzeiten vor Closing beruhen;
(b) Ansprüche aus § 16 BetrAVG (Anpassungsprüfungspflicht) für Rentenzahlungen an frühere RHEINORGANICS-Mitarbeiter, die bis Closing in Rente gegangen sind;
(c) Der Section 75 Employer Debt (Meissner Rhine Industries Ltd. UK, siehe Pemberton Hawkesworth Memo K-UK-8) bis zu einem Höchstbetrag von GBP 18.000.000;
(d) PBGC-Haftung aus dem ERISA Title IV Plan (Meissner Specialty Chemicals Inc. US), soweit Pre-Closing-Beitragsrückstände bestehen.

<b>Section 12.5 – W&I-Versicherung (Pension Representations)</b>

Die Parteien vereinbaren, eine Warranty & Indemnity-Versicherung für die Pension Warranties (Section 12.3) abzuschließen. Der Versicherungsanbieter wurde von Albion Bridge auf &#8222;Munich Re Syndicate W&I" (Lloyd's) beschränkt. Selbstbehalt: 1 % des Transaktionsvolumens (EUR 3.200.000). Versicherungssumme: EUR 50.000.000. Laufzeit: 7 Jahre ab Closing. Die Versicherungsprämie trägt die Käuferin (ca. EUR 1.100.000 einmalig).

Interne Notiz (handschriftlich): [Otterbach: Diese Section muss vor dem Board-Call am 22.04. final sein — sonst kein SPA]

<b>Section 12.6 – Mitarbeitervertretung / Betriebsübergang</b>

Die Parteien bestätigen, dass der Carve-out der Sparte RHEINORGANICS einen Betriebsübergang i.S.v. § 613a BGB sowie Richtlinie 2001/23/EG darstellt. Informations- und Beratungspflichten gegenüber dem GBR und den Einzelbetriebsräten werden von der Verkäuferin spätestens 6 Wochen vor Closing erfüllt. Die Käuferin verpflichtet sich, die Versorgungsordnung VO 2008 (DC-Element) für alle übertretenden aktiven Mitarbeiter mindestens 12 Monate nach Closing unverändert weiterzuführen.

<b>Section 12.7 – Aktuarielle Endabrechnung</b>

Innerhalb von 90 Tagen nach Closing erstellt Hellmrich-Vogt eine finale aktuarielle Stellungnahme zum tatsächlichen Pre-Closing Pension Deficit. Ergibt sich eine Abweichung von mehr als EUR 3.000.000 gegenüber dem Schätzwert (EUR 84.000.000), erfolgt eine Kaufpreisanpassung im Verhältnis 1:1 (Mehr-Deficit = Abzug; Weniger-Deficit = Zuschlag).

<b>Annexe zu Schedule 12:</b>
Anhang 12-A: Vollständige Liste der RHEINORGANICS-Versorgungsberechtigten (aktiv: 892, Rentner: 341, unverfallbare Anwärter: 1.247) — <i>vgl. Sonderakte II, K-MA-18 bis K-MA-24</i>
Anhang 12-B: Einzelzusagen FK-017, FK-023, FK-031 (Vertraulich, nur Beratersatz) — <i>K-MA-25 (Sonderakte II)</i>
Anhang 12-C: CTA-Treuhand-Auszug betreffend Carve-out-Tranche B — K-MA-26
Anhang 12-D: Hellmrich-Vogt-Bewertung 31.12.2025 — K-MA-13
Anhang 12-E: Green & Sandoval LLC ERISA-Memo (US) — K-MA-27
Anhang 12-F: Pemberton Hawkesworth Section 75-Memo — K-UK-8 <i>(vgl. UK-Akte)</i>
"""))
    elems.append(sp(8))
    elems.append(handw("Otterbach-Veltheim (03:47 Uhr): Section 12.4(d) — bitte mit HPL abstimmen vor Signing! —HOV"))
    elems.append(PageBreak())
    return elems


def build_email_chain():
    """19. E-Mail-Kette Vorstand <-> Kanzlei"""
    elems = []
    elems += section_header("E-MAIL-KORRESPONDENZ — VERTRAULICH", "Vorstand Meissner Rheinwerk AG ↔ Treuenfels Yamamoto &#183; Januar–April 2026")
    elems.append(Paragraph("<i>Attorney-Client Privilege / Mandatsgeheimnis — Nur für Berechtigte</i>", S_ITALIC))
    elems.append(sp(8))

    emails = [
        {
            "from": "henrick.otterbach-veltheim@meissner-rheinwerk.de",
            "to": "a.von-sompeh-ostermann-sompeh@treuenfels-yamamoto.de",
            "cc": "c.brindeau-lorbach@meissner-rheinwerk.de; f.albrecht-niermann@treuenfels-yamamoto.de",
            "subject": "Projekt RHEINGOLD 2030 — Kick-off Vorstandsebene",
            "date": "Montag, 12. Januar 2026, 09:14 Uhr (MEZ, Düsseldorf)",
            "body": """Sehr geehrter Herr Professor von Sompeh-Ostermann,

wie telefonisch besprochen möchten wir Sie und Ihr Team als federführende Kanzlei für das Projekt RHEINGOLD 2030 mandatieren. Der Vorstand hat am 08.01.2026 den Strategiebeschluss formell gefasst (Protokoll-Ref. VB-2026-003-P).

Kernpunkte unserer Erwartung:
1. Rechtsgutachten zur Drei-Stufen-Theorie — bis 15.03.2026
2. Begleitung Einigungsstelle (GBR signalisiert Widerstand)
3. Kyoto-Koordination (Yuki Yamamoto — wir kennen Sie aus dem Toyota-Mandat 2022)
4. SPA-Pension-Begleitung RHEINORGANICS / Albion Bridge

Ich werde Ihnen den formellen Engagement Letter-Entwurf bis 14.01. zukommen lassen. Retainer-Frage: Wir erwarten einen Fee Cap, mein CFO ist da unerbittlich.

Mit freundlichen Grüßen
Henrick Otterbach-Veltheim
CFO | Meissner Rheinwerk AG
T: +49 211 4820-1001 | M: +49 172 4891-003"""
        },
        {
            "from": "a.von-sompeh-ostermann-sompeh@treuenfels-yamamoto.de",
            "to": "henrick.otterbach-veltheim@meissner-rheinwerk.de",
            "cc": "y.yamamoto-brennecke@treuenfels-yamamoto-kyoto.jp; h.treuenfels-ostermann@treuenfels-yamamoto.de",
            "subject": "Re: Projekt RHEINGOLD 2030 — Kick-off Vorstandsebene",
            "date": "Montag, 12. Januar 2026, 17:42 Uhr (MEZ, Düsseldorf)",
            "body": """Sehr geehrter Herr Otterbach-Veltheim,

vielen Dank für Ihr Vertrauen. Wir nehmen das Mandat gerne an, vorbehaltlich des abzuschließenden Conflict Checks (insbesondere im Hinblick auf Hanseatica Lebensversicherung AG, mit der wir ein laufendes Produkthaftungsmandat pflegen — wird intern binnen 48h geprüft).

Zum Fee Cap: Ich schlage einen modularen Ansatz vor — Retainer EUR 450.000 p.a. für die Basisberatung, pro Modul (Einigungsstelle, JP, US, UK, SPA) separate Caps. Frau Albrecht-Niermann wird die IAS-19-Zahlen sehr zeitnah sichten.

Yuki Yamamoto-Brennecke ist für das Kyoto-Büro bereits informiert und freut sich auf die Zusammenarbeit.

Hochachtungsvoll
Prof. Dr. Adalbert von Sompeh-Ostermann, LL.M. (Oxford)
Fachanwalt für Arbeitsrecht | Honorarprofessor Universität zu Köln
Treuenfels Yamamoto Rechtsanwälte Partnerschaft mbB
Königsallee 92 | 40212 Düsseldorf
T: +49 211 8870-200 | F: +49 211 8870-299"""
        },
        {
            "from": "c.brindeau-lorbach@meissner-rheinwerk.de",
            "to": "a.von-sompeh-ostermann-sompeh@treuenfels-yamamoto.de",
            "cc": "henrick.otterbach-veltheim@meissner-rheinwerk.de",
            "subject": "Dringend: GBR hat Eskalation angekündigt — Einigungsstelle",
            "date": "Dienstag, 10. Februar 2026, 08:33 Uhr (MEZ, Düsseldorf)",
            "body": """Sehr geehrter Herr Professor von Sompeh-Ostermann,

der GBR-Vorsitzende Herr Kreidemann hat heute Morgen in einer GBR-Sitzung (die wir erst im Nachhinein erfahren haben) angekündigt, einen Antrag auf Einsetzung einer Einigungsstelle beim ArbG Düsseldorf zu stellen. Seine Anwälte von Plöger Maibach haben wohl schon einen Entwurf fertig.

Kernpunkte des GBR-Anliegens (laut unserem Maulwurf im Betriebsrat — bitte vertraulich behandeln):
- Widerspruch gegen die DB-Schließung als mitbestimmungspflichtigen Eingriff in eine betriebliche Übung
- Forderung nach Mitbestimmung beim Pension-Buyout (Delegiertenmodell)
- Ablehnung des DC-Elements VO 2008 als &#8222;Versorgungsentwertung"

Bitte schnellstmöglich Stellungnahme. Der Vorstand hat Aufsichtsrat-Termin am 25.02.

Dr. Constanze Brindeau-Lorbach
HR-Vorstand | Meissner Rheinwerk AG"""
        },
        {
            "from": "a.von-sompeh-ostermann-sompeh@treuenfels-yamamoto.de",
            "to": "c.brindeau-lorbach@meissner-rheinwerk.de",
            "cc": "m.pfaffenhausen-quasthoff@treuenfels-yamamoto.de",
            "subject": "Re: Dringend: GBR hat Eskalation angekündigt",
            "date": "Dienstag, 10. Februar 2026, 11:07 Uhr (MEZ)",
            "body": """Sehr geehrte Frau Dr. Brindeau-Lorbach,

die Information über den &#8222;Maulwurf" sollte künftig nicht per E-Mail kommuniziert werden — datenschutzrechtlich und arbeitsrechtlich heikel (Herr Pfaffenhausen-Quasthoff informiert Sie separat).

Zur Sache: Der GBR hat in der Tat ein Mitbestimmungsrecht nach § 87 Abs. 1 Nr. 8 BetrVG bei der Aufstellung von Grundsätzen über betriebliche Sozialeinrichtungen. Die DB-Schließung ist jedoch keine Maßnahme i.S.d. § 87 BetrVG, sondern eine Änderung von Versorgungszusagen, die dem Mitbestimmungsrecht nach § 87 Abs. 1 Nr. 10 BetrVG (Entlohnungsgrundsätze) nur eingeschränkt unterliegt. Zum Pension-Buyout: Kein originäres Mitbestimmungsrecht des GBR, allenfalls Unterrichtungspflicht nach § 111 BetrVG (Betriebsänderung).

Strategie: Einigungsstelle zulassen (Vorsitz werden wir mit Dr. Wupperhain-Stein besetzen — sie ist pragmatisch), dort gestalten.

Ich schicke Ihnen bis 12.02. ein ausführliches Strategie-Memo.

AvNS"""
        },
        {
            "from": "y.yamamoto-brennecke@treuenfels-yamamoto-kyoto.jp",
            "to": "a.von-sompeh-ostermann-sompeh@treuenfels-yamamoto.de",
            "cc": "henrick.otterbach-veltheim@meissner-rheinwerk.de",
            "subject": "Re: PSV-Frage — bevor Du schläfst",
            "date": "Mittwoch, 11. März 2026, 03:47 Uhr (MEZ, Düsseldorf) / 11:47 Uhr (JST, Kyoto)",
            "body": """Adalbert-sensei,

ich weiß, dass es bei Euch fast 4 Uhr morgens ist — aber der Anruf mit dem MHLW (Ministerium für Gesundheit, Arbeit und Wohlfahrt, 厚生労働省) hat gerade geendet und ich muss Dir kurz berichten, bevor ich die Notizen formalisiere.

Das MHLW hat signalisiert, dass der Antrag auf Umstellung des japanischen DB-Plans nach 確定給付企業年金法 (DB Corporate Pension Law) Artikel 4 (Genehmigungsantrag) frühestens im Q3 2026 beschieden wird — also September oder später. Die Nippon Pension Anstalt KK (Osaka) hat bereits Bedenken geäußert, ob die japanische Tochter (マイスナー・ライン化学株式会社) überhaupt den nationalen Mindestkapitalisierungsanforderungen entspricht.

PSV-Frage (die Otterbach-Veltheim hat): Der PSVaG hat ein Mahnschreiben wegen des Beitragsrückstands 2025 geschickt. Das ist aber KEIN Problem für die japanische Tranche — der PSVaG hat keine Zuständigkeit für ausländische Verpflichtungen. Die Frage ist, ob der deutsche Teil der Konzernumlage korrekt berechnet wurde. Ich vermute ein Berechnungsfehler beim Rabattierungs-Koeffizienten für das CTA-gesicherte Vermögen.

Bitte kläre das morgen früh (Deinem Morgen) mit Frau Albrecht-Niermann.

Yoroshiku onegaishimasu — ご連絡まで。
Yuki Yamamoto-Brennecke
RA (Düsseldorf) | bengoshi (Tokyo Bar Association)
Treuenfels Yamamoto — Kyoto Office
Gion-Higashi, Shijō-dōri, 605-0073 Kyoto
T: +81-75-541-2200"""
        },
        {
            "from": "f.albrecht-niermann@treuenfels-yamamoto.de",
            "to": "henrick.otterbach-veltheim@meissner-rheinwerk.de",
            "cc": "a.von-sompeh-ostermann-sompeh@treuenfels-yamamoto.de; c.brindeau-lorbach@meissner-rheinwerk.de",
            "subject": "IAS-19-Rollforward Q1 2026 — Kritische Abweichung",
            "date": "Freitag, 27. März 2026, 14:22 Uhr (MEZ)",
            "body": """Sehr geehrter Herr Otterbach-veltheim,

nach Sichtung der von Hellmrich-Vogt übermittelten Q1-Zahlen muss ich Sie auf eine kritische Abweichung hinweisen:

Der Diskontzins wurde für Q1 2026 auf 3,85 % (Vorjahr 3,40 %) angepasst. Dies führt zu einer DBO-Reduktion von ca. EUR 148 Mio. — was eigentlich erfreulich wäre. Jedoch zeigt die Sensitivitätsanalyse, dass eine Rückkehr des Zinsniveaus auf 3,0 % (was EZB-Szenarien nicht ausschließen) zu einem DBO-Anstieg von EUR 310 Mio. führen würde. Das ist für den Jahresabschluss-Kommentar relevant.

Zweite Auffälligkeit: Der Dienstzeitaufwand (Current Service Cost) für die noch nicht geschlossenen Komponenten beträgt EUR 18,4 Mio. — höher als budgetiert (EUR 14,7 Mio.). Ursache laut Hellmrich-Vogt: höhere Gehaltsanpassungen als angenommen.

Ich empfehle, die DB-Schließung für aktive Mitarbeiter (Future-Service-Stopp) zu beschleunigen. Bitte informieren Sie den Aufsichtsrat entsprechend.

Mit freundlichen Grüßen
Friederike Albrecht-Niermann
Counsel | Treuenfels Yamamoto Rechtsanwälte Partnerschaft mbB"""
        },
        {
            "from": "henrick.otterbach-veltheim@meissner-rheinwerk.de",
            "to": "a.von-sompeh-ostermann-sompeh@treuenfels-yamamoto.de",
            "cc": "r.engelhart-volz@treuenfels-yamamoto.de",
            "subject": "Dringend: PSVaG-Besceid — Zahlung EUR 4,2 Mio. bis 15.04.?",
            "date": "Donnerstag, 09. April 2026, 07:58 Uhr (MEZ)",
            "body": """Adalbert,

der PSVaG-Bescheid (2026/A-RW-MEISSNER-008842) ist heute Morgen bei unserer Rechtsabteilung eingegangen. Sie fordern EUR 4.218.440,00 Beiträge zzgl. Säumniszuschläge bis 15. April 2026.

Die Berechnung erscheint mir falsch — unser CTA-Sicherungsvermögen wurde nicht angerechnet. Bitte prüfen Sie sofort und stellen Sie eine Stellungnahme an den PSVaG auf. Ich kann nicht EUR 4,2 Mio. zahlen, die ggf. nicht geschuldet sind, ohne dass das den Aufsichtsrat beschäftigt.

Dr. Roman Engelhart-Volz soll steuerliche Auswirkungen parallel klären (§ 4d EStG Rückstellungsanpassung).

HOV
Henrick Otterbach-Veltheim
CFO | Meissner Rheinwerk AG
[Gesendet vom iPhone — bitte Tippfehler entschuldigen]"""
        },
        {
            "from": "a.von-sompeh-ostermann-sompeh@treuenfels-yamamoto.de",
            "to": "henrick.otterbach-veltheim@meissner-rheinwerk.de",
            "cc": "f.albrecht-niermann@treuenfels-yamamoto.de; r.engelhart-volz@treuenfels-yamamoto.de",
            "subject": "Re: Dringend: PSVaG-Bescheid",
            "date": "Donnerstag, 09. April 2026, 09:15 Uhr (MEZ)",
            "body": """Henrick,

ich habe die Stellungnahme bereits in Arbeit — sie geht heute noch raus (vgl. gesonderten Schriftsatz unter Aktenzeichen TY-2026-RHEINGOLD-001/PSV-03). Die CTA-Anrechnung ist ein klassischer PSVaG-Fehler bei Doppeltreuhandstrukturen — ich sehe das in 70 % der Fälle. Wir werden den Betrag deutlich reduzieren.

Zu Dr. Engelhart-Volz und § 4d EStG: Die steuerliche Rückstellung muss ohnehin im Rahmen des Future-Service-Stopps neu berechnet werden. Das läuft.

Bitte keine weiteren PSVaG-Kommunikationen ohne uns.

AvNS

P.S.: Ich habe gerade Yuki aus Kyoto nochmal gesprochen — MHLW-Hanko wohl erst September. Das blockiert den Japan-Zeitplan. Sprechen wir beim nächsten Lenkungskreis am 22. April.

Prof. Dr. Adalbert von Sompeh-Ostermann"""
        },
    ]

    for em in emails:
        elems.append(Paragraph("─" * 80, S_BODY))
        elems.append(sp(4))
        meta_lines = [
            f"<b>Von:</b>     {em['from']}",
            f"<b>An:</b>      {em['to']}",
        ]
        if em.get('cc'):
            meta_lines.append(f"<b>Cc:</b>      {em['cc']}")
        meta_lines += [
            f"<b>Datum:</b>   {em['date']}",
            f"<b>Betreff:</b> {em['subject']}",
        ]
        for ml in meta_lines:
            elems.append(Paragraph(ml, S_MONO))
        elems.append(sp(4))
        for line in em['body'].strip().split('\n'):
            if line.strip():
                elems.append(Paragraph(line, S_BODY))
            else:
                elems.append(sp(4))
        elems.append(sp(8))

    elems.append(PageBreak())
    return elems


def build_handwritten_notes():
    """20. Handschriftliche Notizen Prof. von Sompeh-Ostermann"""
    elems = []
    elems += section_header("HANDSCHRIFTLICHE NOTIZEN", "Prof. Dr. A. von Sompeh-Ostermann — Projekt RHEINGOLD 2030")
    elems.append(Paragraph("<i>Originale: gelbes Notizblock, A5, Füllfederhalter blau-schwarz — hier digitalisiert</i>", S_ITALIC))
    elems.append(sp(12))

    notes = [
        ("14.01.2026 [nach Kick-off-Call HOV]",
         "Brindeau: D-3-Stufen NICHT auf Future-Service ausdehnen, sonst BAG zerlegt uns. A.\n"
         "→ BAG GS 1/82 klar: Eingriff in erdiente Dynamik = schwerster Eingriff, Rechtfertigung extrem eng.\n"
         "→ Future-Service-Stopp = Eingriff zweite Stufe (erdienter Teilbetrag bleibt), grds. zulässig wenn\n"
         "   sachlicher Grund = wirtschaftliche Schwierigkeiten ODER Umstrukturierung.\n"
         "   Frage: reicht 'Projekt RHEINGOLD' als Rechtfertigungsgrund? Prüfen ob Prognose-Plausibilität\n"
         "   (BAG 3 AZR 392/06 Rn. 59 ff.) vorliegt. Otterbach soll Zahlen liefern.\n\n"
         "Mutatis mutandis gilt das auch für UK-Schließung (Section 75 Achtung!)"),
        ("11.03.2026 [06:00 Uhr — Kyoto-Call]",
         "Kyoto-Call 06:00: Yuki sagt MHLW lässt sich Zeit, hanko erst Q3.\n"
         "→ Bedeutet: Japan-Umstellung (DB→DC) kann erst nach Hauptversammlung publik gemacht werden.\n"
         "→ Nippon Pension Anstalt KK will nochmals Due Diligence im Osaka-Werk — akzeptiert.\n\n"
         "Yuki hat aufgeschnappt: Kyoto-Stadtverwaltung prüft Gewerbezulassung für unser Büro —\n"
         "   irrelevant für Mandat, aber intern absichern. La prudence avant tout.\n\n"
         "Memo für Yamamoto-Brennecke: hanko-Block für MHLW-Antrag braucht zwei Unterschriften,\n"
         "   nicht nur einen — Fehler im Draft korrigieren (K-JP-14, K-JP-15)."),
        ("22.03.2026 [nach PSVaG-Mahnschreiben]",
         "Plöger sucht Streit — ignorieren, Einigungsstelle wird's richten.\n"
         "→ Plöger-Heinekamp (Plöger Maibach Köln) ist GBR-Anwalt — aggressiv aber vorhersehbar.\n"
         "→ Seine Argumentation basiert auf BAG 3 AZR 540/16 — aber er verkennt die Subsidiarität.\n"
         "→ Dr. Wupperhain-Stein als Einigungsstellenvorsitz ist goldrichtig — sie hat 2019 das\n"
         "   Merck-Darmstadt-Mandat pragmatisch gelöst. Quod erat probandum.\n\n"
         "PSVaG: CTA-Anrechnungsfehler! Hellmrich-Vogt muss Gegendarstellung schreiben.\n"
         "Frist 09.04. — Albrecht-Niermann übernimmt Berechnung, Engelhart-Volz Tax-Teil."),
        ("08.04.2026 [Lenkungskreis intern TY]",
         "Stand RHEINGOLD:\n"
         "- DE: Einigungsstelle läuft (3. Sitzung 30.04.)\n"
         "- JP: MHLW Q3 — Tokyo District Court 令和8年(ワ)第4421号 noch offen\n"
         "- US: HPL-Boston meldet PBGC-Clearance in Sicht\n"
         "- UK: Section 75-Debt Schätzung jetzt GBP 14,8 Mio. (unter Cap — gut!)\n"
         "- SPA: Albion Bridge will Section 12.4 schärfer — wir müssen am 22.04. verhandeln\n\n"
         "Interne Stunden Stand: EUR 2,38 Mio. netto — über Plan (Fee Cap EUR 2,2 Mio. Q1/Q2).\n"
         "Treuenfels-Ostermann hat Gespräch mit HOV am 23.04. — Nachtragsvereinbarung notwendig.\n\n"
         "Nota bene: Hanko-Original für MHLW kommt per Kurier aus Osaka am 15.04. — Yuki muss\n"
         "abholen. Keine Verzögerung!"),
    ]

    for date_label, note_text in notes:
        elems.append(Paragraph(f"<b><i>{date_label}</i></b>", S_HANDW))
        elems.append(sp(4))
        for line in note_text.split('\n'):
            if line.strip().startswith('→') or line.strip().startswith('-'):
                elems.append(Paragraph(f"<i>&nbsp;&nbsp;&nbsp;&nbsp;{line.strip()}</i>", S_HANDW))
            elif line.strip():
                elems.append(Paragraph(f"<i>{line.strip()}</i>", S_HANDW))
            else:
                elems.append(sp(4))
        elems.append(sp(12))
        elems.append(Paragraph("— — —", S_ITALIC))
        elems.append(sp(10))

    # Latin/French flourishes block
    elems.append(sp(8))
    elems.append(Paragraph("<b><i>Einzelne Randnotizen aus diversen Schriftsätzen (handschriftlich nachgetragen):</i></b>", S_HANDW))
    elems.append(sp(6))
    margin_notes = [
        "&#8222;Quod erat demonstrandum — BAG GS 1/82 bleibt das Fundament aller Drei-Stufen-Prüfung.&#8221; [S. 14 Gutachten]",
        "&#8222;Mutatis mutandis für UK-Schließung — Section 75 als Analogon zur PSVaG-Sicherung.&#8221; [UK-Memo S. 3]",
        "&#8222;La prudence avant tout — Hanseatica nicht zu früh binden.&#8221; [Buyout Term Sheet Rand]",
        "&#8222;Yoroshiku onegaishimasu — Yuki hat das MHLW im Griff. Vertrauen.&#8221; [Kyoto-Memo S. 6]",
        "&#8222;NB: Kreidemann hat 2022 bei der Thyssenkrupp-Einigungsstelle gewonnen — unterschätzen wir nicht.&#8221; [GBR-Akte]",
        "&#8222;§ 16 BetrAVG: Anpassungspflicht läuft weiter auch nach DB-Schließung — das vergessen Klienten immer.&#8221; [VO-Inventory S. 8]",
        "&#8222;Albion Bridge will mehr — wir geben nichts. Section 12.4 steht.&#8221; [SPA-Rand]",
    ]
    for mn in margin_notes:
        elems.append(Paragraph(f"<i>{mn}</i>", S_HANDW))
        elems.append(sp(5))

    elems.append(PageBreak())
    return elems


def build_timesheet():
    """21. Stundenaufstellung Treuenfels Yamamoto Jan–Apr 2026"""
    from reportlab.platypus import Table, TableStyle
    from reportlab.lib import colors as rl_colors

    elems = []
    elems += section_header("STUNDENAUFSTELLUNG TREUENFELS YAMAMOTO", "Projekt RHEINGOLD 2030 &#183; Zeitraum: Januar–April 2026 &#183; Aktenzeichen TY-2026-RHEINGOLD-001")
    elems.append(Paragraph("<b>RECHNUNG NR. TY-2026-INV-047 (Zwischenabrechnung) — ENTWURF zur Freigabe</b>", S_BOLD_BODY))
    elems.append(sp(6))
    elems.append(Paragraph("Mandant: Meissner Rheinwerk AG, Düsseldorf | Mandatsannahme: 14.01.2026 | Abrechnungszeitraum: 14.01.2026–30.04.2026", S_BODY))
    elems.append(sp(10))

    # Header table
    header_data = [
        ["ROLLE", "PERSON", "SATZ (€/h)", "JAN", "FEB", "MÄR", "APR", "GESAMT h", "SUMME (€)"],
    ]
    rows = [
        ["Partner", "Prof. Dr. A. v. Sompeh-Ostermann", "980", "48,0", "62,5", "71,0", "58,0", "239,5", "234.710"],
        ["Sr. Partner", "Dr. Dr. H. Treuenfels-Ostermann", "980", "12,0", "8,0", "14,0", "10,0", "44,0", "43.120"],
        ["Counsel", "F. Albrecht-Niermann", "720", "38,0", "52,0", "60,0", "48,0", "198,0", "142.560"],
        ["Counsel Tax", "Dr. R. Engelhart-Volz", "720", "10,0", "18,0", "28,0", "22,0", "78,0", "56.160"],
        ["Sr. Associate", "M. Pfaffenhausen-Quasthoff", "520", "22,0", "30,0", "35,0", "28,0", "115,0", "59.800"],
        ["Sr. Associate", "A. Beerbohm-Sittler", "520", "18,0", "26,0", "32,0", "30,0", "106,0", "55.120"],
        ["Associate", "C. Wrobel-Hagedorn", "380", "14,0", "20,0", "24,0", "18,0", "76,0", "28.880"],
        ["Associate", "T. Morgenthaler-Funk", "380", "8,0", "12,0", "18,0", "14,0", "52,0", "19.760"],
        ["Trainee", "P. Schumann-Lindqvist", "220", "10,0", "14,0", "16,0", "12,0", "52,0", "11.440"],
        # Kyoto
        ["bengoshi (Kyoto)", "Y. Yamamoto-Brennecke*", "~800€", "20,0", "28,0", "34,0", "26,0", "108,0", "~86.400"],
        ["Sr. Ass. Kyoto", "H. Nakamura-Becker*", "~580€", "8,0", "12,0", "16,0", "10,0", "46,0", "~26.680"],
        # Kosten
        ["Reisekosten", "Alle Timekeeper", "—", "—", "—", "—", "—", "—", "18.400"],
        ["Gerichtsgebühren", "ArbG/LAG", "—", "—", "—", "—", "—", "—", "4.880"],
        ["Sonstige Auslagen", "Porto, Kurier, etc.", "—", "—", "—", "—", "—", "—", "2.290"],
    ]
    total_net = 2_380_000  # net

    header_data += rows
    header_data.append(["", "", "", "", "", "", "", "<b>NETTO GESAMT</b>", "<b>EUR 2.380.000</b>"])
    header_data.append(["", "", "", "", "", "", "", "zzgl. MwSt 19 %", "EUR 452.200"])
    header_data.append(["", "", "", "", "", "", "", "<b>BRUTTO GESAMT</b>", "<b>EUR 2.832.200</b>"])

    col_widths = [90, 140, 65, 35, 35, 35, 35, 65, 80]
    t = Table(header_data, colWidths=col_widths, repeatRows=1)
    ts = table_default_style(rows_header=1)
    ts.add('FONTSIZE', (0,0), (-1,-1), 7.5)
    ts.add('ROWBACKGROUNDS', (0,1), (-1,-4), [colors.white, colors.Color(0.96, 0.96, 0.98)])
    ts.add('BACKGROUND', (0,-3), (-1,-1), colors.Color(0.9, 0.92, 0.95))
    ts.add('FONTNAME', (0,-3), (-1,-1), 'Helvetica-Bold')
    t.setStyle(ts)
    elems.append(t)

    elems.append(sp(10))
    elems.append(Paragraph("<i>* Kyoto-Stunden in JPY abgerechnet (JPY 92.000/h bengoshi; JPY 58.000/h Sr. Associate), Umrechnung EUR/JPY Kurs 0,0062 (Fix März 2026). Gesonderte Yen-Rechnung wird separat gestellt.</i>", S_ITALIC))
    elems.append(sp(6))

    # Module breakdown
    elems.append(Paragraph("<b>Aufschlüsselung nach Modulen:</b>", S_BOLD_BODY))
    elems.append(sp(6))

    module_data = [
        ["MODUL", "Beschreibung", "Stunden gesamt", "Netto EUR"],
        ["DE-DB", "Drei-Stufen-Gutachten, Einigungsstelle, PSVaG, Sozialplan", "412,0", "380.400"],
        ["DE-CTA", "CTA-Treuhandvertrag, Buyout Term Sheet, Hanseatica-Verhandlungen", "198,0", "162.080"],
        ["DE-IAS19", "IAS-19-Begleitung, Rollforward, Sensitivitätsanalyse (Albrecht-Niermann)", "244,0", "175.680"],
        ["JP", "Kyoto-Modul, MHLW-Antrag, Tokyo District Court, DB→DC-Migration", "154,0", "113.080"],
        ["US", "ERISA Title IV, PBGC, 401(k)-Amendment (HPL-Koordination)", "88,0", "72.160"],
        ["UK", "Section 75, TPR Clearance (Pemberton Hawkesworth-Koordination)", "62,0", "48.040"],
        ["SPA/M&A", "Pension Schedule SPA, Indemnities, W&I-Versicherung, Albion Bridge", "188,0", "168.480"],
        ["Governance", "Pension-Governance-Konzept, Policy-Drafts, Aufsichtsrat-Begleitung", "76,0", "63.080"],
        ["Tax", "§§ 4d, 6a EStG, PSVaG-Anrechnung, Pensionsrückstellung", "78,0", "56.160"],
        ["Datenschutz", "GBR-Datenfragen, DSGVO-Compliance Pensionsakte", "52,0", "27.040"],
        ["Allg./Admin", "Reisekosten, Gerichte, Porto, Kurier, Auslagen", "—", "25.570"],
        ["TOTAL", "", "1.552,0", "EUR 2.380.000"],
    ]
    col_widths_m = [60, 240, 90, 80]
    tm = Table(module_data, colWidths=col_widths_m, repeatRows=1)
    tsm = table_default_style(rows_header=1)
    tsm.add('FONTSIZE', (0,0), (-1,-1), 8)
    tsm.add('ROWBACKGROUNDS', (0,1), (-1,-2), [colors.white, colors.Color(0.97, 0.97, 1.0)])
    tsm.add('BACKGROUND', (0,-1), (-1,-1), DARK_BLUE)
    tsm.add('TEXTCOLOR', (0,-1), (-1,-1), colors.white)
    tm.setStyle(tsm)
    elems.append(tm)

    elems.append(sp(8))
    elems.append(handw("Treuenfels-Ostermann [23.04.]: HOV muss Nachtrag genehmigen — Budget überschritten. Termin 25.04. 10:00. —HTO"))
    elems.append(sp(6))
    elems.append(Paragraph("<b>Hinweis:</b> Der vereinbarte Fee Cap für Q1/Q2 2026 betrug EUR 2.200.000. Die tatsächlichen Leistungen übersteigen diesen Betrag um EUR 180.000. Eine Nachtragsvereinbarung wird vorbereitet (Entwurf: TY-2026-NTA-003).", S_BODY))
    elems.append(PageBreak())
    return elems


def build_annexes_index():
    """22+23. Aktenrand-Notizen und Anlagenverzeichnis"""
    from reportlab.platypus import Table, TableStyle
    from reportlab.lib import colors as rl_colors

    elems = []

    # --- Aktenrand-Notizen ---
    elems += section_header("AKTENRAND-NOTIZEN (AUSWAHL)", "Aus diversen Schriftsätzen und Memos — digitalisiert April 2026")
    elems.append(Paragraph("<i>Die nachfolgenden Randnotizen wurden handschriftlich in die Akte eingetragen und werden hier dokumentiert. Kursivdruck = Simulation handschriftlicher Einträge.</i>", S_ITALIC))
    elems.append(sp(8))

    margin_items = [
        ("Gutachten S. 3 [Drei-Stufen]", "→ BAG GS 1/82: Diese Entscheidung ist 44 Jahre alt und immer noch das Maß aller Dinge. Erstaunlich. [AvNS]"),
        ("VO-Inventory S. 4 [VO 1973]", "Achtung: VO 1973 hat keine Verfallklausel — alle Anwärter unverfallbar, auch < 3 Jahre Betriebszugehörigkeit! Rechtslage vor BetrAVG 1974. [F.A.-N.]"),
        ("CTA-Entwurf S. 12 [Sicherungstreuhand]", "quod erat probandum — Insolvenzfestigkeit nur wenn echter trust-Charakter. Vgl. BAG 3 AZR 18/12. [AvNS]"),
        ("PSVaG-Erwiderung S. 2", "Beitragsberechnung: CTA-Sicherungsvermögen EUR 820 Mio. nicht abgezogen! PSVaG-Fehler evident. Widerspruch mit Nachdruck. [F.A.-N.]"),
        ("Einigungsstelle Protokoll 1 S. 4", "Kreidemann war konstruktiver als erwartet — vielleicht doch verhandelbar? La prudence avant tout. [AvNS]"),
        ("Kyoto-Memo S. 2 [MHLW]", "Yoroshiku — Yuki hat den MHLW-Referenten persönlich angesprochen. Chapeau! [AvNS]"),
        ("UK-Memo S. 3 [Section 75]", "mutatis mutandis: Section 75-Debt wie PSVaG-Haftung, nur teurer. GBP 14,8 Mio. unter Cap — gut. [M.P.-Q.]"),
        ("SPA Schedule 12 S. 8", "Albion Bridge: 'We need skin in the game' — Quatsch, das ist deren Preisverhandlung. Standhaft bleiben. [AvNS]"),
        ("US-Memo S. 5 [PBGC]", "ERISA §4062 — unfunded vested benefits calculation needs 2024 actuarial restatement. HPL confirms. [A.B.-S.]"),
        ("Sozialplan-Entwurf S. 7", "Modell 3 (freiwillige Abfindung + VO-2008-Aufstockung) ist GBR-fähig — mündlich getestet mit Kreidemann 14.03. [AvNS]"),
        ("Stundenaufstellung Apr 2026", "€ 2,38 Mio. — bitte HOV anrufen BEVOR die Rechnung rausgeht. [HTO]"),
    ]

    for loc, note in margin_items:
        elems.append(Paragraph(f"<b><i>{loc}:</i></b>", S_BOLD_BODY))
        elems.append(Paragraph(f"<i>{note}</i>", S_HANDW))
        elems.append(sp(6))

    elems.append(PageBreak())

    # --- Anlagenverzeichnis ---
    elems += section_header("ANLAGENVERZEICHNIS", "Aktenzeichen TY-2026-RHEINGOLD-001 &#183; Stand: 30.04.2026")
    elems.append(Paragraph("<b>Hinweis:</b> Mit &#8222;(Sonderakte II)&#8221; gekennzeichnete Anlagen befinden sich in der gesonderten Sonderakte II (Vertrauliche Anlagen). Nicht alle Anlagen sind in dieser Hauptakte abgebildet.", S_BODY))
    elems.append(sp(8))

    def anlage_table(prefix, count, descriptions):
        rows = [["ANLAGE-NR.", "BEZEICHNUNG / INHALT", "ORT"]]
        for i in range(1, count+1):
            desc = descriptions.get(i, f"{prefix}-{i:02d}: [Anlage]")
            ort = "Sonderakte II" if i > count - (count // 4) and count > 8 else "Hauptakte"
            rows.append([f"K-{prefix}-{i:02d}" if i < 10 else f"K-{prefix}-{i}", desc, ort])
        t = Table(rows, colWidths=[80, 320, 80], repeatRows=1)
        ts = table_default_style(rows_header=1)
        ts.add('FONTSIZE', (0,0), (-1,-1), 7.5)
        ts.add('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.Color(0.97, 0.97, 0.97)])
        t.setStyle(ts)
        return t

    # VO-Anlagen
    elems.append(Paragraph("<b>K-VO: Versorgungsordnungen und Zulagen</b>", S_BOLD_BODY))
    elems.append(sp(4))
    vo_desc = {
        1: "VO 1973 — Betriebliche Versorgungsordnung Stammwerk (Original + Änderungsvereinbarungen)",
        2: "VO 1981 — Versorgungsordnung mit Gehaltsdynamik (Protokollnotiz Aufsichtsrat 12.02.1981)",
        3: "VO 1995 — Schließungsvereinbarung Altsystem, Einfrierungsprotokoll GBR vom 14.11.1995",
        4: "VO 2008 — DC-Komponente, Tarifvertrag Chemie-Nord 2007 (Anlage 3)",
        5: "Versorgungstarifvertrag Chemie-Nord (aktuell gültige Fassung 2021)",
        6: "Einzelzusagen-Register FK-001 bis FK-047 (anonymisiert, sortiert nach Dotierung)",
        7: "Einzelzusage FK-017 — Sondervergütung Wechselprämie (Sonderakte II)",
        8: "Einzelzusage FK-023 — Ruhegehalt-Direktzusage Senior VP R&D (Sonderakte II)",
        9: "Einzelzusage FK-031 — Halteprämie Konzern-Controller (Sonderakte II)",
        10: "Aktuarielle Basis-Bewertung VO 1973/1981 per 31.12.2025 (Hellmrich-Vogt)",
        11: "Sterbetafelgrundlagen 2018-G (DAV, für DE), Sensitivitätstest RT-Tabellen",
        12: "Deferred Compensation Policy (DCP) 2022 für leitende Angestellte",
        13: "Gehaltssteigerungs-Annahmen HR-Vorstand 2024–2035 (Sonderakte II)",
        14: "VO-Konsolidierungsentwurf 2026 (Schließung + Ablösemodell, Entwurf Stand 01.03.2026)",
        15: "Protokoll GBR-Sitzung 07.01.2026 (Übergabe VO-Inventory, Sonderakte II)",
    }
    elems.append(anlage_table("VO", 15, vo_desc))
    elems.append(sp(8))

    # CTA-Anlagen
    elems.append(Paragraph("<b>K-CTA: CTA-Treuhand und Fondsanlagen</b>", S_BOLD_BODY))
    elems.append(sp(4))
    cta_desc = {
        1: "CTA Rheinland Trust e.V. — Satzung (Stand 2019)",
        2: "Treuhandrahmenvertrag (Verwaltungstreuhand) 2019, Grundversion",
        3: "Treuhandrahmenvertrag (Sicherungstreuhand) 2019 mit Nachtrag 2022",
        4: "Bestandsliste gesicherter Versorgungsanwärter per 31.12.2025",
        5: "Vermögensaufstellung CTA-Treuhänder Q4 2025 (Aktien EUR 420 Mio., Anleihen EUR 380 Mio., Cash EUR 20 Mio.)",
        6: "Investmentrichtlinie CTA Rheinland Trust 2023",
        7: "Risiko-Matching-Report LBBW AM Q1 2026",
        8: "Abtretungserklärungen Sicherungstreuhand (Muster + 320 Einzeldokumente)",
        9: "Anerkenntniserklärungen Mitarbeiter (vgl. BAG 3 AZR 18/12)",
        10: "Jahresabschluss CTA Rheinland Trust e.V. 2024 (Sonderakte II)",
        11: "Bankkonten-Vollmachten Treuhänder (Sonderakte II)",
        12: "Governance-Protokoll CTA-Beirat Q1 2026",
        13: "Carve-out-Bestimmungen RHEINORGANICS aus CTA (Tranche A vs. B)",
        14: "Due-Diligence-Bericht Albion Bridge zu CTA-Sicherung (Sonderakte II)",
        15: "PSVaG-Bescheid mit CTA-Anrechnung 2024 (Referenzbescheid)",
        16: "Entwurf CTA-Nachtrag 2026 (Erweiterung um Buyout-Tranche)",
        17: "Hanseatica-Bewertungsgrundlagen Sicherungsvermögen (Sonderakte II)",
        18: "Verfügungsbeschränkungen Sicherungstreuhand (Klausel 12.3 bis 12.8 Treuhandvertrag)",
        19: "Freistellungsklausel zugunsten Treuhänder (§ 5 Treuhandvertrag)",
        20: "Protokoll CTA-Gründungsversammlung 2019 (Historisch)",
        21: "Registerauszug CTA Rheinland Trust e.V., VR Düsseldorf 14 VR 2210",
        22: "Notarielle Beglaubigung Gründungsprotokoll (Sonderakte II)",
    }
    elems.append(anlage_table("CTA", 22, cta_desc))
    elems.append(sp(8))

    # PSVaG-Anlagen
    elems.append(Paragraph("<b>K-PSV: PSVaG-Korrespondenz und Bescheide</b>", S_BOLD_BODY))
    elems.append(sp(4))
    psv_desc = {
        1: "PSVaG-Mitgliedsbescheid 2026 (laufende Mitgliedschaft Meissner Rheinwerk AG)",
        2: "Beitragsberechnung 2025 — Ursprungsbescheid",
        3: "Beitragserhöhung 2026 — Grundlagenbescheid",
        4: "Mahnschreiben PSVaG vom 22.03.2026 (Beitragsrückstand EUR 4.218.440)",
        5: "Insolvenzsicherungs-Register Meissner Rheinwerk AG — Auszug",
        6: "Stellungnahme Treuenfels Yamamoto vom 09.04.2026 (Original)",
        7: "Erwiderung PSVaG vom 28.04.2026",
        8: "Berechnung CTA-Anrechnungskorrektur (Hellmrich-Vogt, April 2026)",
        9: "Beitragshistorie 2015–2025 (tabellarisch)",
        10: "Korrespondenz PSVaG betreffend Meldepflicht Pensionsfonds-Erweiterung",
        11: "Antrag BaFin VA 31-Q 5232-2026/0014 (Pensionsfonds-Erweiterung, Einreichung 01.02.2026)",
        12: "BaFin-Rückfragen-Schreiben 14.03.2026 (K-PSV-12 — siehe Sonderakte II)",
        13: "PSVaG-Formular M1 (Meldung Betriebsänderung mit Rentenversicherungsrelevanz)",
        14: "Bescheinigung Konzernmutterschaft für PSVaG-Zwecke",
        15: "Prüfungsanforderung PSVaG (§ 10 BetrAVG Abs. 3 Abs. 5)",
        16: "Rechtsbehelfsbelehrung Beitragsbescheid 2026",
        17: "Widerspruchsentwurf gegen Beitragsbescheid (Stand 25.04.2026)",
        18: "Interne PSVaG-Meldeliste HR/Finance 2026 (Sonderakte II)",
    }
    elems.append(anlage_table("PSV", 18, psv_desc))
    elems.append(sp(8))

    # JP-Anlagen
    elems.append(Paragraph("<b>K-JP: Japan-Modul (マイスナー・ライン化学株式会社)</b>", S_BOLD_BODY))
    elems.append(sp(4))
    jp_desc = {
        1: "Gesellschaftsvertrag マイスナー・ライン化学株式会社 (Osaka/Kyoto)",
        2: "DB Corporate Pension Plan (確定給付企業年金) — Versorgungsplan-Dokument",
        3: "Tax-Qualified-Plan-Dokument (旧制度税制適格退職年金) — historisch",
        4: "Antrag DB-Plan-Umstellung nach 確定給付企業年金法 Art. 4 (MHLW-Antrag, Entwurf)",
        5: "MHLW-Korrespondenz (Vorprüfung, 2025)",
        6: "Gutachten Yamamoto-Brennecke: Migration DB→DC (bilingual DE/JP)",
        7: "Bewertung japanischer DB-Plan per 31.03.2026 (Nippon Pension Anstalt KK)",
        8: "Vergleich Bieter Nippon Pension Anstalt KK vs. Dai-ichi Life Insurance (Sonderakte II)",
        9: "DC-Plan-Entwurf (確定拠出年金, iDeCo-Anknüpfung)",
        10: "Hanko-Nachweis MHLW-Antrag (original Stempelabdruck, Sonderakte II)",
        11: "Mitarbeiterversammlung-Protokoll Osaka-Werk 14.02.2026",
        12: "Osaka-Betriebsrat-Stellungnahme (労使協定, Betriebsvereinbarung)",
        13: "Juristische Analyse 確定給付企業年金法 Art. 4, 8, 14 (Yamamoto-Brennecke)",
        14: "Hanko-Vorlage MHLW (Draft 1, Fehler in Unterschriftslinie — korrigiert)",
        15: "Hanko-Vorlage MHLW (Draft 2, korrekt, eingereicht)",
        16: "Tokyo District Court 令和8年(ワ)第4421号 — Klageschrift",
        17: "Klageerwiderung Yamamoto-Brennecke für マイスナー・ライン化学株式会社",
        18: "Verfahrenskalender Tokyo District Court 2026/2027",
        19: "Rechtsgutachten japanisches Arbeitsrecht (Universitätsprofessor Kyushu, extern)",
        20: "E-Mail-Kette Yuki Yamamoto-Brennecke / MHLW-Referat (Sonderakte II)",
        21: "Steuergutachten japanische Pensionsrückstellung (Tax Partner Kyoto)",
        22: "Kyoto-Büro-Protokoll Strategiemeeting 25.03.2026",
        23: "Nippon Pension Anstalt KK — Term Sheet DC-Ablösung",
        24: "Due-Diligence-Checkliste japanischer Plan (Albion Bridge Perspective)",
        25: "Osaka-Werk HR-Daten (anonymisiert, 1.450 Mitarbeiter)",
        26: "Translation-Glossar DE↔JP Pensionsbegriffe (Yamamoto-Brennecke)",
        27: "Rechtsprechungsübersicht japanische Obergerichte zu DB-Schließungen",
        28: "MHLW-Genehmigungszeitplan Q2–Q4 2026 (Prognose)",
        29: "Notiz Yamamoto: 'Treuenfels-sensei e: kakutei-kyuufu-saraba, DC-koso michi nari'",
        30: "Osaka/Kyoto-Reisenachweise TY-Team (Sonderakte II)",
        31: "Kyoto-Registrierungsnachweis Zweigstelle Treuenfels Yamamoto (Sonderakte II)",
    }
    elems.append(anlage_table("JP", 31, jp_desc))
    elems.append(sp(8))

    # US-Anlagen
    elems.append(Paragraph("<b>K-US: US-Modul (Meissner Specialty Chemicals Inc.)</b>", S_BOLD_BODY))
    elems.append(sp(4))
    us_desc = {
        1: "ERISA Title IV Plan Document (Meissner Specialty Chemicals Inc., 2019-Restatement)",
        2: "PBGC Participant Data as of 12/31/2025",
        3: "PBGC Premium Payment History 2020–2025",
        4: "HPL-Memo ERISA Title IV PBGC-Implikationen (File HPL-2026-MRW-0007)",
        5: "401(k) Plan Document (Meissner Specialty Chemicals Inc., 2021-Restatement)",
        6: "401(k) Plan Amendment Entwurf (2026) — Erhöhung Safe Harbor Match",
        7: "PBGC 4010 Filing 2025 (Sonderakte II)",
        8: "PBGC Variable Premium Calculation 2025",
        9: "Holcombe Pratchett & Lieberman — Retainer Agreement",
        10: "HPL-Memo: Carve-out RHEINORGANICS-US, ERISA Section 4069 Controlled Group Issues",
        11: "DoL Correspondence (Form 5500) 2025",
        12: "Plan Asset Valuation 12/31/2025 (Green & Sandoval LLC Actuaries)",
        13: "Funding Target Attainment Percentage (FTAP) Calculation 2026",
        14: "Benefit Restriction Analysis §436 IRC — current status",
        15: "Houston Site Employee Communication (401(k) Changes 2026, English/Spanish)",
        16: "Wilmington DE Corporate Secretary Resolution re. Pension Plan (Sonderakte II)",
    }
    elems.append(anlage_table("US", 16, us_desc))
    elems.append(sp(8))

    # UK-Anlagen
    elems.append(Paragraph("<b>K-UK: UK-Modul (Meissner Rhine Industries Ltd.)</b>", S_BOLD_BODY))
    elems.append(sp(4))
    uk_desc = {
        1: "UK DB-Plan — Trust Deed and Rules (2018 Consolidation)",
        2: "Actuarial Valuation Report 2024 (FRS 102 / IAS 19)",
        3: "Section 75 Employer Debt Estimate — Pemberton Hawkesworth (March 2026)",
        4: "TPR Clearance Application Draft",
        5: "Trustee Board Minutes Q1 2026",
        6: "Member Communication — DB Closure Consultation",
        7: "Pemberton Hawkesworth Solicitors — Engagement Letter",
        8: "Section 75 Debt Detailed Calculation (Sonderakte II)",
        9: "TPR Submission Timeline (April–October 2026)",
        10: "UK Pension Regulator Correspondence (Preliminary, Feb 2026)",
        11: "UK Plan Investment Strategy Statement 2024 (Sonderakte II)",
    }
    elems.append(anlage_table("UK", 11, uk_desc))
    elems.append(sp(8))

    # M&A-Anlagen
    elems.append(Paragraph("<b>K-MA: M&A / Carve-out RHEINORGANICS</b>", S_BOLD_BODY))
    elems.append(sp(4))
    ma_desc = {
        1: "SPA Entwurf v7.2 (gesamt, Sonderakte II)",
        2: "Schedule 12 Pension (vollständig, dieser Akte als K-MA-Annex)",
        3: "Data Room Index RHEINORGANICS (Pension-Folder, Stand 15.04.2026)",
        4: "NDA Albion Bridge Capital Partners — Meissner Rheinwerk AG",
        5: "Albion Bridge Due Diligence Request List (Pension, March 2026)",
        6: "Albion Bridge DD-Report Pensions (Sonderakte II, streng vertraulich)",
        7: "Management Presentation RHEINORGANICS Carve-out (Sonderakte II)",
        8: "Bieterverfahren-Protokoll Round 1 (anonymisiert)",
        9: "Bieterverfahren-Protokoll Round 2 (Sonderakte II)",
        10: "Strukturierungsoptionen Carve-out (Asset Deal vs. Share Deal Analyse)",
        11: "Steuerstruktur RHEINORGANICS Carve-out (Engelhart-Volz/PwC gemeinsam)",
        12: "Pension-Liability-Zuordnung RHEINORGANICS-Mitarbeiter (Tranche-Matrix)",
        13: "Hellmrich-Vogt-Bewertung RHEINORGANICS per 31.12.2025",
        14: "Disclosure Letter Entwurf (Pension-Abschnitt 8.4 ff.)",
        15: "SPA Signing Protocol (Planung: 30.06.2026, Sonderakte II)",
        16: "Closing Condition: Einigungsstellen-Abschluss (Condition Precedent)",
        17: "Pension W&I Term Sheet (Munich Re Syndicate W&I)",
        18: "W&I Insurance Final Terms (nach Signing, Sonderakte II)",
        19: "Completion Accounts Methodology Agreement",
        20: "Carve-out Pension Adjustment Mechanism (Detailed Calculation Method)",
        21: "ERISA Controlled Group Analysis post-Carve-out (HPL Boston)",
        22: "Section 75 Isolation Mechanism UK (Pemberton Hawkesworth)",
        23: "Separation Agreement Entwurf — Pensionen UK",
        24: "Japan-Sparte Carve-out — Sonderprüfung MHLW-Konsistenz",
        25: "Arbeitnehmerüberlassungs-Analyse RHEINORGANICS-Übergang § 613a BGB",
        26: "GBR-Informationsschreiben Carve-out (Entwurf, noch nicht versandt)",
        27: "Aufsichtsrat-Präsentation Carve-out (Sonderakte II)",
        28: "Abschlussprüfungsvermerk KPMG zu RHEINORGANICS 2024 (Sonderakte II)",
    }
    elems.append(anlage_table("MA", 28, ma_desc))

    elems.append(sp(10))
    elems.append(Paragraph(
        "<b>Ende des Anlagenverzeichnisses.</b> Gesamtzahl erfasster Anlagen: "
        "K-VO 1–15 (15), K-CTA 1–22 (22), K-PSV 1–18 (18), K-JP 1–31 (31), "
        "K-US 1–16 (16), K-UK 1–11 (11), K-MA 1–28 (28). "
        "<b>Gesamt: 141 Anlagen.</b> Davon in Sonderakte II: 34 Anlagen.",
        S_BODY))
    elems.append(sp(6))
    elems.append(Paragraph(
        "<i>Sonderakte II (Vertrauliche Anlagen) befindet sich im Safe Treuenfels Yamamoto "
        "Düsseldorf, Zugang nur für Prof. Dr. von Sompeh-Ostermann und Frau Yamamoto-Brennecke. "
        "Kopien an Mandantin nur nach ausdrücklicher schriftlicher Anweisung.</i>",
        S_ITALIC))

    elems.append(PageBreak())

    # Final closing page
    elems += section_header("SCHLUSSKENNBLATT", "Aktenzeichen TY-2026-RHEINGOLD-001")
    closing_data = [
        ["Mandant:", "Meissner Rheinwerk AG, Düsseldorf-Reisholz"],
        ["Aktenzeichen:", "TY-2026-RHEINGOLD-001"],
        ["Projekt:", "RHEINGOLD 2030 — Globale bAV-Neuordnung"],
        ["Federführung:", "Prof. Dr. Adalbert von Sompeh-Ostermann, LL.M. (Oxford)"],
        ["Mandatsannahme:", "14. Januar 2026"],
        ["Stand Akte:", "30. April 2026"],
        ["Anlagen gesamt:", "141 (davon 34 in Sonderakte II)"],
        ["Gerichtl. Verfahren:", "ArbG Düsseldorf 7 BV 412/26 | LAG Düsseldorf 14 TaBV 88/26"],
        ["", "BAG 3 ABR 14/27 (angekündigt) | BaFin VA 31-Q 5232-2026/0014"],
        ["", "Tokyo District Court 令和8年(ワ)第4421号"],
        ["DBO gesamt:", "EUR 3,2 Mrd. (weltweit, IAS 19) | EUR 2,4 Mrd. (Deutschland)"],
        ["Projektvolumen:", "EUR 18 Mio. (Projekt RHEINGOLD 2030 gesamt)"],
        ["Honorar YTD:", "EUR 2.380.000 netto (Januar–April 2026)"],
        ["Nächste Termine:", "22.04.2026 Lenkungskreis RHEINGOLD | 25.04.2026 HOV-Nachtragsgespräch"],
        ["", "30.04.2026 Einigungsstelle 3. Sitzung | Q3/2026 MHLW-Hanko erwartet"],
    ]
    ct = Table(closing_data, colWidths=[130, 360])
    ct.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.Color(0.95, 0.95, 0.98), colors.white]),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('GRID', (0,0), (-1,-1), 0.3, colors.Color(0.8, 0.8, 0.85)),
    ]))
    elems.append(ct)
    elems.append(sp(20))

    # Final ASCII sign-off
    sign_off = """
┌─────────────────────────────────────────────────────────────────┐
│   TREUENFELS YAMAMOTO RECHTSANWÄLTE PARTNERSCHAFT MBB           │
│   トロイエンフェルス・ヤマモト法律事務所                              │
│                                                                 │
│   Hauptbüro:  Königsallee 92 &#183; 40212 Düsseldorf                 │
│   Kyoto-Büro: Gion-Higashi, Shijō-dōri &#183; 605-0073 Kyoto        │
│                                                                 │
│   "Precision in Law — 法の精度"                                    │
│                                                                 │
│   ENDE DER AKTE — TY-2026-RHEINGOLD-001                         │
│   Stand: 30.04.2026 — VERTRAULICH — MANDATSGEHEIMNIS           │
└─────────────────────────────────────────────────────────────────┘
"""
    elems.append(Paragraph(sign_off.replace('\n', '<br/>'), S_MONO))
    return elems


# ─────────────────────────────────────────────────────────────────────────────
# MAIN BUILD
# ─────────────────────────────────────────────────────────────────────────────


# =============================================================================
# SUPPLEMENT SECTIONS
# =============================================================================

def build_gutachten_supplement():
    """Supplement: Drei-Stufen Gutachten - Rechtfertigungsebene"""
    elems = []
    elems += section_header("RECHTSGUTACHTEN-SUPPLEMENT", "Drei-Stufen-Theorie - Vertiefung Rechtfertigungsebene * Prof. Dr. A. von Sompeh-Ostermann")

    elems.append(P("""<b>IV. Vertiefende Analyse der Rechtfertigungsebene - Zweite und Dritte Stufe</b>

<b>1. Die zweite Stufe: Eingriff in erdiente Dynamik</b>

Die zweite Stufe des Drei-Stufen-Modells erfasst sogenannte erdiente Dynamiken - Anwartschaftsbestandteile, die zwar auf kuenftigen Entwicklungen (Gehaltssteigerungen, Inflationsanpassungen) beruhen, die aber bereits erdient worden sind insoweit, als sie auf vergangener Betriebszugehoerigkeit gruenden.

Paradigmatischer Fall ist die endgehaltsbezogene Versorgungszusage der VO 1981, bei der die Gehalterhoehungen nach einer Schliessung fuer die Berechnung der Versorgungsleistung nicht mehr beruecksichtigt werden, obwohl der Arbeitnehmer jahrzehntelang im Vertrauen auf diese Dynamik Entgeltbestandteile gespart hat.

Das BAG (Urt. v. 11.10.2011 - 3 AZR 527/09, Rn. 76 ff.) hat klargestellt, dass der Eingriff in erdiente Dynamiken einer sachlichen Rechtfertigung bedarf, die nach BAG 3 AZR 392/06 eine hinreichende Plausibilitaet wirtschaftlicher Schwierigkeiten oder eine nachvollziehbar begruendete unternehmerische Gesamtentscheidung voraussetzt.

Dabei unterscheidet der Senat:

(a) <b>Stichtagsmodell:</b> Die Leistung wird eingefroren auf den Stand zum Zeitpunkt der Schliessung. Eingriff in die Dynamik: Ja, kuenftige Gehalterhoehungen wirken nicht mehr. Rechtfertigung: Sachlicher Grund genuegt.

(b) <b>Zeitanteiligkeitsmodell:</b> Der erdiente Teilbetrag = (Dienstjahre bis Schliessung / Gesamtdienstjahre) x Voll-Leistung. Eingriff: Geringer. Rechtfertigung: Sachlicher Grund ausreichend.

(c) <b>Einfrierung Altzusage + Parallelzusage DC:</b> Der Anwaerter erhaelt ab Schliessung eine beitragsorientierte Zusage. Rechtfertigung: Erleichtert durch Kompensationseffekt.

Die Meissner Rheinwerk AG verfolgt Modell (c). Die Schliessung der VO 1973 / VO 1981 mit Einfrierung zum 31.12.2026 plus Ueberfuehrung in das DC-Element VO 2008 ist daher auf zweiter Stufe rechtfertigungsfaehig, wenn ein sachlicher Grund vorliegt.

<b>Sachlicher Grund: Projekt RHEINGOLD 2030</b>

Der Vorstandsbeschluss vom 08.01.2026 (VB-2026-003-P) dokumentiert die betriebliche und wirtschaftliche Motivation: Reduktion der IAS-19-Pensionslast (EUR 2,4 Mrd. DBO, Zinssensitivitaet EUR 310 Mio. bei 100 BP-Verschiebung), Vorbereitung des Carve-out RHEINORGANICS (Albion Bridge), internationale Gouvernanz-Harmonisierung.

Das BAG hat in 3 AZR 392/06 (Rn. 65 ff.) Umstrukturierungsmassnahmen als sachlichen Grund anerkannt, wenn die Entscheidung einer kaufmaennischen Plausibilitaets-Kontrolle standhalt. Diese Kontrolle besteht hier: Die Prognose-Plausibilitaet ist durch die IAS-19-Zahlen (Hellmrich-Vogt) und die Transaktionslogik (SPA-Pension Schedule) belegbar.

<b>2. Die dritte Stufe: Eingriff in noch nicht erdiente Zuwachse (Future Service)</b>

Der Eingriff in den Future Service ist nach dem Drei-Stufen-System die am leichtesten zu rechtfertigende Eingriffsform. Das BAG (GS 1/82, Rn. C II 3 c; bestaetigt in 3 AZR 540/16, Rn. 55) verlangt hierfuer lediglich einen sachlich-proportionalen Grund, der in nachvollziehbaren wirtschaftlichen oder organisatorischen Erwaegungen liegen kann.

Fuer Meissner Rheinwerk AG liegt dieser Grund klar vor: Die DBO von EUR 2,4 Mrd. (Deutschland) belastet die Bilanz, erhoeht den Fremdfinanzierungsbedarf und ist Dealbreaker im RHEINORGANICS-Carve-out. Der Dienstzeitaufwand (Current Service Cost) von EUR 18,4 Mio. p.a. uebersteigt das Budget und belastet das EBIT. Die unternehmerische Entscheidung zur Future-Service-Beendigung ist daher auf dritter Stufe unzweifelhaft gerechtfertigt.

<b>3. Rechtsfolgen der Schliessung fuer bestehende Anwartschaften</b>

Paragr. 2 Abs. 1 BetrAVG (Unverfallbarkeit) bleibt unveraendert: Alle Anwaerter mit Betriebszugehoerigkeit ueber 3 Jahren und Mindestalter 21 Jahre behalten ihre erdienten Anwartschaften unverfallbar. Die Berechnung erfolgt pro-rata-temporis:

Zeitanteilig erdiente Anwartschaft = Vollleistung x (m/n)

wobei m = Betriebszugehoerigkeit bis Schliessung, n = moegliche Gesamtbetriebszugehoerigkeit bis Regelrentenalter 67.

Fuer die 4.300 deutschen Anwaerter in VO 1973 / VO 1981 ergibt sich nach Hellmrich-Vogt-Berechnung eine durchschnittliche Anwartschaftshoehe von EUR 387/Monat (Median EUR 312/Monat). Die Streuung ist erheblich (MIN EUR 48/Monat, MAX EUR 2.847/Monat fuer FK-Bereich).

<b>4. Paragr. 16 BetrAVG: Anpassungspruefungspflicht nach Schliessung</b>

Auch nach der DB-Schliessung bleibt die Anpassungspruefungspflicht des Paragr. 16 Abs. 1 BetrAVG fuer laufende Renten bestehen. Alle drei Jahre ist zu pruefen, ob eine Anpassung um den Kaufkraftverlust moeglich und zumutbar ist (Massstab: Unternehmensertragslage, BAG 3 AZR 304/13). Die Schliessung hebt diese Verpflichtung nicht auf.

Fuer die Rentnerbestaende bedeutet das: Dreijaehrige Anpassungspruefungszyklen ab 01.01.2027. Hellmrich-Vogt schaetzt, dass die Ertragslage 2027-2030 eine Anpassung von 1-2 % p.a. erzwingen wird (Teuerungsrate ca. 2,8 % p.a. angenommen).

<b>Empfehlung:</b> Langfristig sollte geprueft werden, ob eine Kapitalabfindung (Paragr. 3 BetrAVG, Kleinstanwartschaften unter EUR 34,65/Monat) fuer die unterste Einkommensgruppe in Betracht kommt, um die Verwaltungslast zu reduzieren. Schaetzungsweise 340 Anwaerter koennten kapitalisiert werden (Volumen ca. EUR 4,2 Mio. Einmalbeitraege).

<b>5. Besondere Problematik: Sonderzusagen FK-001 bis FK-047</b>

Die 47 Einzelzusagen im Fuehrungskraeftebereich (FK-001 bis FK-047, K-VO-6 ff.) weisen atypische Klauseln auf, die einer gesonderten Pruefung beduerfeni:

FK-017: Aenderungsklausel mit Schriftformerfordernis; Schliessung via kollektiv-rechtliche Betriebsvereinbarung koennte an Paragr. 4 Abs. 3 TVG scheitern, wenn Versorgungstarifvertrag anwendbar.
FK-023: Leistung an Hinterbliebene mit unwiderruflichem Bezugsrecht; Schliessung fuer Future Service nur mit Zustimmung des Beguenstigten.
FK-031: Performance-bezogene Komponente (Zielvereinbarung); hier ist Schliessung rechtlich unproblematisch fuer den Leistungsausfall, aber der Anwaerter koennte Schadensersatz geltend machen.

Diese drei Faelle erfordern individuelle Loesung - entweder durch gesonderte Abloes-Vereinbarung oder durch Einbeziehung in den Sozialplan (mit GBR-Zustimmung, was Ploeger Maibach sicher instrumentalisieren wird).

<b>6. Tarifvertragliche Sperre (Chemie-Nord Versorgungstarifvertrag)</b>

Der Versorgungstarifvertrag Chemie-Nord enthaelt in Paragr. 14 Abs. 2 eine Oeffnungsklausel, die Betriebsvereinbarungen ueber die Einschraenkung der Leistungen erlaubt, sofern der paritaetische Ausschuss der IG BCE und des Arbeitgeberverbandes zugestimmt hat. Diese Zustimmung liegt noch nicht vor (Stand: 30.04.2026). Ohne sie riskiert Meissner Rheinwerk AG eine tarifwidrige Betriebsvereinbarung.

Handlungsempfehlung: Sofortige Kontaktaufnahme mit dem Arbeitgeberverband Chemische Industrie NRW (ACIN) und parallele Einholung der IG-BCE-Zustimmung ueber den tarifpolitischen Koordinierungspfad. Zeitbedarf: 8-12 Wochen. Das synchronisiert mit der Einigungsstellen-Planung (Ziel-Abschluss Einigungsstelle: 31.07.2026).
"""))
    elems.append(handw("AvNS [12.03.2026]: Tarifvertrag-Sperre ist der echte Dealbreaker - nicht die Drei-Stufen. Otterbach muss ACIN anrufen. Sofort. A.v.S.-O."))
    elems.append(PageBreak())
    return elems


def build_psv_supplement():
    """PSVaG Supplement - Widerspruchsschreiben"""
    from reportlab.platypus import Table, TableStyle
    elems = []
    elems += section_header("PSVaG-WIDERSPRUCHSSCHREIBEN", "TY-2026-RHEINGOLD-001/PSV-03 * 09.04.2026")

    elems.append(P("""<b>Treuenfels Yamamoto Rechtsanwaelte Partnerschaft mbB</b>
Koenigsallee 92, 40212 Duesseldorf
Telefon: +49 211 8870-200

An den Pensions-Sicherungs-Verein VVaG (PSVaG)
Kohlenstrase 118, 44795 Bochum

Duesseldorf, 09. April 2026

<b>Betreff: Widerspruch gegen Beitragsbescheid 2026/A-RW-MEISSNER-008842 vom 22.03.2026</b>
Mandantin: Meissner Rheinwerk AG, Duesseldorf
PSVaG-Mitglieds-Nr.: MR-DE-19681412

Sehr geehrte Damen und Herren,

in vorbezeichneter Angelegenheit zeigen wir die anwaltliche Vertretung der Meissner Rheinwerk AG an und legen namens und in Vollmacht unserer Mandantin form- und fristgerecht

<b>WIDERSPRUCH</b>

gegen den Beitragsbescheid 2026/A-RW-MEISSNER-008842 vom 22.03.2026 ein.

<b>I. Fehlerhafter Beitragssatz - Nichtanrechnung des CTA-Sicherungsvermogens</b>

Der PSVaG hat in seinem Beitragsbescheid das nach Paragr. 10 Abs. 3 BetrAVG anrechenbare Sicherungsvermoegen aus dem CTA-Treuhandvertrag (CTA Rheinland Trust e.V.) nicht beruecksichtigt. Das Sicherungsvermoegen per 31.12.2025 betraegt EUR 820.000.000,-- und ist vollstaendig in das insolvenzssichere Doppeltreuhand-Modell eingebracht (K-CTA-3 bis K-CTA-9).

Nach Paragr. 10 Abs. 3 Nr. 2 BetrAVG sind Beitraege dem Umfang nach zu reduzieren, wenn fuer die versicherungspflichtigen Versorgungsverpflichtungen insolvenzsicheres Treuhandvermoegen (CTA-Sicherungsmasse) besteht. Die Rechtsprechung des BAG (3 AZR 18/12, NZA 2013, 582) hat die Insolvenzfestigkeit des Doppeltreuhand-Modells ausdruecklich bestaetigt.

<b>Fehlerhafte Beitragsberechnung:</b>
"""))

    beitrags_data = [
        ["POSITION", "PSVaG-Bescheid (falsch)", "Richtige Berechnung", "Differenz"],
        ["Beitragsbemessungsgrundlage (BBG)", "EUR 2.400.000.000", "EUR 2.400.000.000", "---"],
        ["Anrechenbares CTA-Sicherungsvermoegen", "EUR 0 (nicht angerechnet)", "EUR 820.000.000", "- EUR 820.000.000"],
        ["Beitragspflichtige BBG (netto)", "EUR 2.400.000.000", "EUR 1.580.000.000", "- EUR 820.000.000"],
        ["PSVaG-Beitragssatz 2026 (Promille)", "1,757 Promille", "1,757 Promille", "---"],
        ["Beitragsschuld brutto", "EUR 4.216.800", "EUR 2.777.060", "- EUR 1.439.740"],
        ["Saeumniszuschlag (3 Monate)", "EUR 1.640", "EUR 0", "- EUR 1.640"],
        ["Beitragsschuld GESAMT laut PSVaG", "EUR 4.218.440", "---", "---"],
        ["Beitragsschuld RICHTIG", "---", "EUR 2.777.060", "---"],
        ["Erstattungsanspruch", "---", "---", "EUR 1.441.380"],
    ]
    bt = Table(beitrags_data, colWidths=[165, 115, 115, 85])
    bt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.Color(0.95,0.95,1.0)]),
        ('GRID', (0,0), (-1,-1), 0.3, colors.Color(0.7,0.7,0.8)),
        ('FONTNAME', (0,-1), (-1,-1), 'Helvetica-Bold'),
        ('BACKGROUND', (0,-1), (-1,-1), colors.Color(0.8,0.95,0.8)),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5),
    ]))
    elems.append(bt)
    elems.append(sp(6))

    elems.append(P("""<b>II. Rechtliche Grundlage des Erstattungsanspruchs</b>

Paragr. 10 Abs. 3 BetrAVG i.V.m. der PSVaG-Beitragsordnung Paragr. 7 Nr. 3 lit. b) gebietet die Anrechnung insolvenzsicheren Treuhandvermogens. Die Mandantin hat das CTA-Sicherungsvermoegen ordnungsgemaess in der Meldung M1 vom 28.02.2026 (K-PSV-13) ausgewiesen. Die Nichtberuecksichtigung im Bescheid ist ein Fehler des PSVaG, der einen oeffentlich-rechtlichen Erstattungsanspruch in Hoehe von EUR 1.441.380,-- begruendet.

<b>Wir beantragen:</b>
1. Aufhebung des Beitragsbescheids in Hoehe von EUR 1.441.380,--
2. Neuberechnung und Erlass eines berichtigten Bescheids ueber EUR 2.777.060,--
3. Erstattung bereits gezahlter Betraege (Vorbehaltszahlung vom 08.04.2026, EUR 2.777.060,--) mit Zinsanspruch
4. Bestaetigung des Eingangs dieses Widerspruchs innerhalb von 7 Werktagen

Mit freundlichen Gruessen

<b>Treuenfels Yamamoto Rechtsanwaelte Partnerschaft mbB</b>
Prof. Dr. Adalbert von Sompeh-Ostermann, LL.M. (Oxford)
Friederike Albrecht-Niermann (Counsel)

Anlagen: K-CTA-1 bis K-CTA-9 (Auszug), K-PSV-8 (Hellmrich-Vogt-Gegendarstellung), K-PSV-13 (M1-Meldung)
"""))
    elems.append(handw("PSVaG-Referat Bochum kennt das Problem - sie haben 2023 auch bei ThyssenKrupp den CTA-Abzug vergessen. Wir bekommen das Geld. A.v.S.-O."))
    elems.append(PageBreak())
    return elems


def build_einigungsstelle_supplement():
    """Additional Einigungsstelle protocol - Sitzungen 2+3"""
    elems = []
    elems += section_header("EINIGUNGSSTELLEN-PROTOKOLLE (Ergaenzung)", "ArbG Duesseldorf 7 BV 412/26 * Sitzungen 2 und 3 * FAX-UEBERMITTLUNG")

    elems += fax_block(
        lines=[
            "SITZUNGSPROTOKOLL Nr. 2 | 27.03.2026 | 10:00-17:30 Uhr",
            "Einigungsstelle zur DB-Schliessung Meissner Rheinwerk AG",
            "Ort: Arbeitsrichterliches Mediationszentrum, Duesseldorf, Erkrather Str. 21",
            "Vorsitz: RiArbG a.D. Dr. Hannelore Wupperhain-Stein",
            "",
            "ANWESEND ARBEITGEBERSEITE:",
            "  Dr. C. Brindeau-Lorbach (HR-Vorstand Meissner Rheinwerk AG)",
            "  Prof. Dr. A. von Sompeh-Ostermann (Treuenfels Yamamoto)",
            "  F. Albrecht-Niermann (Treuenfels Yamamoto, Counsel IAS 19)",
            "  P. Schumann-Lindqvist (Treuenfels Yamamoto, Trainee, Protokoll AG-Seite)",
            "",
            "ANWESEND ARBEITNEHMERSEITE:",
            "  L. Kreidemann (GBR-Vorsitzender)",
            "  R. Hohenstein-Biber (GBR-Mitglied, Stellvertreter)",
            "  M. Schillings-Kern (GBR-Mitglied, Vertrauensmann IG BCE)",
            "  Dr. W. Ploeger-Heinekamp (Ploeger Maibach RA Koeln)",
            "",
            "TOP 1: Billigung Protokoll Sitzung 1 - einstimmig",
            "",
            "TOP 2: Vorlage Gutachten Drei-Stufen-Theorie (Sompeh-Ostermann)",
            "  GBR-Anwalt Ploeger-Heinekamp bestreitet Gutachtenmethodik.",
            "  Dr. Wupperhain-Stein schlaegt Prof. Dr. Riesenfeld-Merzbach (Koeln)",
            "  als gemeinsamen Obergutachter vor. Wird naechste Sitzung entschieden.",
            "",
            "TOP 3: Sozialplan-Entwurf - Pension-Bestandteile (Diskussion)",
            "  GBR verlangt Aufstockung DC-Element VO 2008 von 4% auf 6% AG-Beitrag.",
            "  AG-Seite: Maximalzugestaendnis 5% AG-Beitrag, nur >10 J. BZ.",
            "  Einigung nicht erzielt - Fortsetzung Sitzung 3.",
            "",
            "NAECHSTE SITZUNG: 30. April 2026, 10:00 Uhr, gleicher Ort",
        ],
        sender="Einigungsstelle via Fax", receiver="Treuenfels Yamamoto Duesseldorf",
        date="27.03.2026 18:12", pages="3 von 3"
    )
    elems.append(sp(6))
    elems.append(handw("Ploeger argumentiert methodisch falsch - aber die Obergutachter-Frage ist gefaehrlich. Riesenfeld-Merzbach ist ok - kenne ihn aus Bayer-Mandat 2021. A.v.S.-O."))
    elems.append(sp(8))

    elems += fax_block(
        lines=[
            "SITZUNGSPROTOKOLL Nr. 3 | 30.04.2026 | 10:00-18:45 Uhr",
            "Einigungsstelle zur DB-Schliessung Meissner Rheinwerk AG",
            "ArbG Duesseldorf 7 BV 412/26",
            "",
            "TOP 1: Billigung Protokoll Sitzung 2 - einstimmig mit 2 Berichtigungen",
            "",
            "TOP 2: Obergutachten - Einigung auf Prof. Dr. Riesenfeld-Merzbach (Koeln).",
            "  Honorar EUR 35.000 je zur Haelfte. Gutachten bis 30.06.2026.",
            "",
            "TOP 3: DC-Beitragssatz - EINIGUNG ERZIELT:",
            "  - AG-Beitrag 5% (all-in) fuer alle Anwaerter mit >5 J. BZ ab Schliessung",
            "  - AG-Beitrag 4% fuer Anwaerter mit <5 J. BZ",
            "  - Zusatzkomponente: Einmalzahlung EUR 1.500 fuer alle Anwaerter >20 J. BZ",
            "  Abstimmung: 7:3 - Mehrheitsbeschluss nach Paragr. 76 Abs. 5 Satz 3 BetrVG",
            "",
            "TOP 4: Zeitplan Schliessung",
            "  Kompromiss: Schliessung 31.03.2027 fuer Anwaerter >15 J. BZ,",
            "              31.12.2026 fuer alle anderen Anwaerter",
            "  Abstimmung: 6:4 - MEHRHEITSBESCHLUSS",
            "",
            "INSGESAMT: Alle wesentlichen Punkte durch Mehrheitsbeschluss geregelt.",
            "Einigungsstellenbeschluss wird ausgefertigt bis 15.05.2026.",
            "Dr. Wupperhain-Stein: Ich erwarte keine Anfechtung - rechtssicher.",
            "",
            "Unterzeichnet: Dr. Wupperhain-Stein (Vorsitz), P. Schumann-Lindqvist (Protokoll)",
        ],
        sender="Einigungsstelle via Fax", receiver="Treuenfels Yamamoto Duesseldorf",
        date="30.04.2026 19:22", pages="4 von 4"
    )
    elems.append(sp(6))
    elems.append(handw("Perfekt. Schliessung 31.03.2027 ist 3 Monate Aufschub - akzeptabel. SPA-Bedingung muss angepasst werden: neues Datum 31.03.2027 statt 31.12.2026. Sofort Albion Bridge informieren. A.v.S.-O."))
    elems.append(PageBreak())
    return elems


def build_erp_supplement():
    """US ERISA/PBGC supplement"""
    elems = []
    elems += section_header("US-MODUL SUPPLEMENT", "ERISA Deep Dive * PBGC Clearance * 401(k) Amendment * Holcombe Pratchett & Lieberman LLP")

    elems += fax_block(
        lines=[
            "HOLCOMBE PRATCHETT & LIEBERMAN LLP",
            "One Federal Street, Suite 4100 | Boston, MA 02110",
            "Tel: +1 (617) 555-0192 | Fax: +1 (617) 555-0199",
            "File No.: HPL-2026-MRW-0007",
            "",
            "MEMORANDUM",
            "TO:   Prof. Dr. Adalbert von Sompeh-Ostermann, Treuenfels Yamamoto",
            "FROM: Randolph T. Holcombe III, Partner; Priya Subramaniam, Sr. Associate",
            "DATE: March 18, 2026",
            "RE:   ERISA Title IV Implications - RHEINORGANICS Carve-Out",
            "      Meissner Specialty Chemicals Inc. (MSC-US)",
            "",
            "I. PBGC CONTROLLED GROUP LIABILITY",
            "",
            "Under ERISA Section 4001(a)(14), Meissner Rheinwerk AG and all",
            "domestic subsidiaries constitute a 'controlled group' for PBGC",
            "purposes. Upon carve-out of MSC-US to ABCP RHEINORGANICS BIDCO LTD.,",
            "MSC-US will leave the existing controlled group.",
            "",
            "Key consequence (ERISA Section 4062(e)): The cessation of MSC-US",
            "participation may trigger a 'cessation event' if more than 20% of",
            "plan participants are attributable to MSC-US operations.",
            "",
            "Our preliminary analysis: approximately 340 MSC-US participants out",
            "of 2,800 total US employees = 12.1%. BELOW the 20% threshold. Favorable.",
            "However: PBGC's 'look-through' rules (29 CFR Part 4062) may require",
            "proactive notification. We recommend filing PBGC Form 10-Advance.",
            "",
            "II. PBGC PREMIUM OBLIGATIONS (Plan Year 2025)",
            "",
            "Variable-rate premium (VRP): $847,200",
            "Flat-rate premium (FRP): $96 x 2,800 participants = $268,800",
            "TOTAL PBGC premium 2025: $1,116,000",
            "",
            "Post-carve-out reduction (MSC-US departure): -$142,000 estimated.",
            "",
            "III. 401(k) PLAN - SAFE HARBOR AMENDMENT",
            "",
            "Proposed amendment: Safe Harbor match from 4% to 5% of eligible comp.",
            "Requirements: (a) 30-day advance notice (ERISA Section 204(h))",
            "              (b) Board resolution MSC-US",
            "              (c) Amendment executed before Dec 31, 2026",
            "Budget impact: ~$2.1M additional annual employer cost for MSC-US.",
            "Houston site employees have 87% participation - Spanish language",
            "summary required (ERISA Section 101(j)).",
            "",
            "IV. RECOMMENDATION",
            "",
            "File PBGC Form 10-Advance before Closing (30-day lead time required).",
            "Execute 401(k) Amendment by October 31, 2026 latest.",
            "Coordinate with Green & Sandoval LLC (Houston actuaries) for FTAP calc.",
        ],
        sender="HPL Boston via Fax/Email", receiver="Treuenfels Yamamoto Duesseldorf",
        date="18.03.2026 09:44 EST", pages="6 von 6"
    )
    elems.append(sp(8))

    elems.append(P("""<b>401(k) PLAN AMENDMENT NO. 3 - ENTWURF (Auszug)</b>
File No.: HPL-2026-MRW-0007-A

<b>AMENDMENT NO. 3 TO THE MEISSNER SPECIALTY CHEMICALS INC. 401(k) RETIREMENT PLAN</b>

This Amendment No. 3 is adopted by the Board of Directors of Meissner Specialty Chemicals Inc. (Company) effective as of January 1, 2027.

<b>Section 1 - Safe Harbor Matching Contribution (Amendment to Article VI, Section 6.4)</b>

Effective January 1, 2027, the Safe Harbor Matching Contribution is increased to:
(a) 100% of Elective Deferrals not exceeding 4% of Compensation; plus
(b) 50% of Elective Deferrals exceeding 4% but not exceeding 6% of Compensation.
Maximum effective match: 5% of Compensation (satisfies IRC Section 401(k)(12)).

<b>Section 2 - RHEINORGANICS Carve-Out Provisions (New Article XIV)</b>

XIV.1 Transferred Employees. Any Participant who becomes employed by ABCP RHEINORGANICS BIDCO LTD. on or after the Closing Date shall cease active participation in this Plan as of such date.

XIV.2 Vested Benefits. Each Transferred Participant is 100% vested as of the Closing Date regardless of otherwise applicable vesting schedule.

XIV.3 Distribution Elections. Transferred Participants may elect: (i) direct rollover to IRA or successor plan; (ii) lump-sum distribution; or (iii) maintain Account Balance in Plan until age 72.

XIV.4 Plan Expenses. Company bears all reasonable expenses for transfer of Transferred Participants' benefits, not to exceed $85,000 in aggregate.

IN WITNESS WHEREOF, this Amendment No. 3 is executed by the duly authorized officer.

______________________________
[Name], [Title]
Meissner Specialty Chemicals Inc.
Date: _____________, 2026

Approved by Board Resolution No. MSC-2026-BR-0047 (pending execution)
Coordinated by: Holcombe Pratchett & Lieberman LLP, Boston (HPL-2026-MRW-0007-A)
German counsel: Treuenfels Yamamoto, Duesseldorf (TY-2026-RHEINGOLD-001/US-07)
"""))
    elems.append(PageBreak())
    return elems


def build_governance_memo():
    """Pension Governance Memo"""
    elems = []
    elems += section_header("PENSION GOVERNANCE MEMO", "Globale Neuordnung der bAV-Steuerung * Meissner Rheinwerk AG * Prof. Dr. A. von Sompeh-Ostermann")

    elems.append(P("""<b>MEMO: Globale Pension-Governance-Neuordnung - Rahmenkonzept</b>
Datum: 15. Maerz 2026
Von: Prof. Dr. Adalbert von Sompeh-Ostermann, LL.M.
An: Henrick Otterbach-Veltheim (CFO), Dr. Constanze Brindeau-Lorbach (HR-Vorstand)
Betreff: Empfehlungen zur globalen Pension Governance im Rahmen von Projekt RHEINGOLD 2030
Aktenzeichen: TY-2026-RHEINGOLD-001/GOV-01

<b>Executive Summary</b>

Die aktuelle Pension-Governance-Struktur der Meissner Rheinwerk AG ist historisch gewachsen und entspricht nicht mehr den Anforderungen einer modernen IORP-II-konformen Fuehrungs- und Aufsichtsstruktur (Richtlinie 2016/2341/EU). Die DB-Schliessung, der Pension-Buyout, die Japan-Migration und der RHEINORGANICS-Carve-out machen eine Neuordnung zwingend erforderlich.

<b>I. Ist-Zustand der Pension Governance (Maengel)</b>

1. <b>Fragmentierte Zustaendigkeiten:</b> HR (Frau Dr. Brindeau-Lorbach) ist fuer neue Zusagen zustaendig, Finance/Controlling (Herr Otterbach-Veltheim) fuer die IAS-19-Bilanzierung, die Rechtsabteilung fuer Rechtsstreitigkeiten. Es fehlt ein zentrales Pension Committee mit klaren Entscheidungskompetenzen.

2. <b>Keine formale Investment-Governance fuer CTA:</b> Das CTA-Sicherungsvermoegen (EUR 820 Mio.) wird vom CTA-Beirat verwaltet, aber der Vorstand hat keine formale Aufsichtsrolle. Nach IORP-II Art. 24 ff. ist ein Fit-and-Proper-Mechanismus fuer Treuhaender erforderlich.

3. <b>Keine globale Konsolidierung:</b> Japan, USA, UK haben eigene lokale Pension-Strukturen ohne Konzernberichtserstattung an den Vorstand. Die Konzernmutter hat keine vollstaendige Uebersicht ueber die globale DBO-Exposition.

4. <b>Fehlende Continuity-of-Service-Regelungen:</b> Bei einem Carve-out (wie RHEINORGANICS) gibt es keine dokumentierten Prozesse fuer die Uebertragung von Pensionsverpflichtungen. Das hat zu dem Chaos bei der Section-12-SPA-Verhandlung gefuehrt.

<b>II. Soll-Konzept: Global Pension Committee (GPC)</b>

Vorschlag: Einrichtung eines Global Pension Committee (GPC) auf Ebene der Konzernmutter.

<b>Zusammensetzung GPC:</b>
- CFO (Vorsitz): Henrick Otterbach-Veltheim
- HR-Vorstand: Dr. Constanze Brindeau-Lorbach
- Chief Legal Officer: Dr. Bernd Weidemann-Kruse
- Group Head of Treasury: N.N. (zu besetzen)
- Externer Aktuar (beratend, ohne Stimmrecht): Hellmrich-Vogt Aktuarpartner GmbH

<b>Aufgaben GPC:</b>
- Genehmigung aller Planaaenderungen ueber EUR 5 Mio. DBO-Impact
- Genehmigung Investment Policy Statement fuer CTA-Vermoegen
- Halbjaehresbericht an den Aufsichtsrat ueber globale Pension-Exposition
- Freigabe aller Pension-bezogenen SPA/M&A-Klauseln
- Oversight des PSVaG- und BaFin-Verhaeltnisses

<b>Sitzungsfrequenz:</b> Quartalsmaessig, plus Ad-hoc-Sitzungen bei Transaktionen

<b>Sekretariat:</b> Treuenfels Yamamoto (extern, Protokollfuehrung und Agenda-Setting) fuer die ersten 24 Monate, dann Uebergabe an interne Rechtsabteilung.

<b>III. IORP-II-Compliance (Richtlinie 2016/2341/EU)</b>

Die IORP-II-Richtlinie (Art. 21 ff.) verlangt fuer Einrichtungen der betrieblichen Altersversorgung (EbAV) eine angemessene System of Governance:

Art. 21: Allgemeine Grundsaetze der Governance - das GPC-Konzept entspricht dem Vier-Augen-Prinzip.
Art. 22: Risikomanagement - separates Pension Risk Management Framework (PRMF) erforderlich.
Art. 23: Interne Revision - Einbeziehung des konzerninternen Audit-Ausschusses.
Art. 24: Versicherungsmathematische Funktion - Hellmrich-Vogt als designierter Aktuar der EbAV.
Art. 25-28: Ausgliederung (Outsourcing) - Treuenfels Yamamoto als externer Berater unterliegt dem Outsourcing-Rahmen.

Handlungsempfehlung: GPC per 01.07.2026 einrichten. IORP-II-Compliance-Dokumentation bis 30.09.2026 fertigstellen. Hellmrich-Vogt offiziell als Aktuar der EbAV nach Art. 24 IORP-II bestellen (schriftliche Bestellung und BaFin-Meldung erforderlich).

<b>IV. Reporting-Struktur: Global Pension Dashboard</b>

Zur Unterstuetzung des GPC empfehlen wir die Einrichtung eines Global Pension Dashboard mit folgenden Kennzahlen:

<b>A. Liabilitaets-Kennzahlen (IAS 19):</b>
- DBO global (aufgeteilt nach Jurisdiktion: DE EUR 2,4 Mrd., JP JPY 18,4 Mrd., US USD 124 Mio., UK GBP 89 Mio.)
- Fair Value Plan Assets
- Net Pension Liability / Asset
- Current Service Cost, Past Service Cost, Interest Cost
- Actuarial Gains/Losses (OCI-Bewegung)
- Discount Rate Sensitivity (plus/minus 50 BP, plus/minus 100 BP)

<b>B. Funding-Kennzahlen:</b>
- CTA-Bedeckungsgrad (Plan Assets / DBO Deutschland): aktuell 34,2% (EUR 820 Mio. / EUR 2.400 Mio.)
- PSVaG-Beitragsvorschau (2026: EUR 2,78 Mio., 2027: geschaetzt EUR 2,6 Mio. nach CTA-Korrektur)
- PBGC FTAP (USA): aktuell 94,2%
- UK Funding Level (FRS 102): aktuell 87,4%
- Japan DB-Funding-Ratio: aktuell 91,8%

<b>C. Projekt-Kennzahlen RHEINGOLD 2030:</b>
- Einigungsstelle Status: Ampel GELB (Sitzung 3 abgeschlossen, Beschluss ausstehend)
- Japan MHLW-Genehmigung Status: Ampel GELB (Antrag eingereicht, Bescheid Q3 2026)
- UK TPR Clearance Status: Ampel GELB (Antrag in Vorbereitung)
- RHEINORGANICS Carve-out Pension Status: Ampel ROT (Section 12 SPA offen)
- Buyout-Prozess Hanseatica Status: Ampel GRUEN (Term Sheet vereinbart)
- CTA-Erweiterung Status: Ampel GELB (Nachtrag in Entwurf)

<b>Implementierungsplan GPC:</b>
- April 2026: GPC-Satzung verabschieden
- Mai 2026: Erste GPC-Konstituierungssitzung
- September 2026: IORP-II-Compliance-Audit (KPMG beauftragt)
- Dezember 2026: Vollstaendige GPC-Operativitaet

<b>Kostenprognose Governance-Neuordnung:</b>
Einmalig: EUR 280.000 (IT-Integration Dashboard, externe Beratung)
Laufend: EUR 85.000 p.a. (Aktuarsgebuehren IORP-II, GPC-Sekretariat)

Prof. Dr. Adalbert von Sompeh-Ostermann | Treuenfels Yamamoto | 15. Maerz 2026
"""))
    elems.append(handw("Brindeau-Lorbach: GPC ist ueberfaellig. HOV auch. Bitte Beschluss im naechsten Vorstandsmeeting. A.v.S.-O."))
    elems.append(PageBreak())
    return elems


def build_kyoto_supplement():
    """Kyoto supplement - Tokyo court filing + glossar"""
    from reportlab.platypus import Table, TableStyle
    elems = []
    elems += section_header("KYOTO-MODUL SUPPLEMENT", "Tokyo District Court Schriftsatz * MHLW-Detail * Terminologie-Glossar")

    elems.append(P("""<b>SCHRIFTSATZ AN DEN TOKYO DISTRICT COURT</b>
Verfahren: Heisei 8(wa) No. 4421 (令和8年(ワ)第4421号)

Verfahrensbezeichnung: Klage auf Feststellung der Wirksamkeit des DB-Plan-Aenderungsvertrags
Klaeger: Meissner Rhine Kagaku KK (Osaka)
Beklagte: Betriebsgewerkschaftsvertretung (Minderheitsfraktion)
Klaegerbevollmaechtigte: Yuki Yamamoto-Brennecke, bengoshi Nr. 48817

<b>KLAGEBEGRUENDUNG (Auszug)</b>

I. Sachverhaltsdarstellung

Die Klaegerin Meissner Rhine Kagaku KK betreibt Chemieanlagen in Osaka und Kyoto mit ca. 1.450 Mitarbeitern. Das Unternehmen unterhalt seit 1984 einen leistungsorientierten Betriebsrentenplan nach dem Gesetz ueber betriebliche Leistungsrenten (確定給付企業年金法, DB-Pensionsgesetz). Dieser Plan wurde zuletzt 2018 neu gefasst.

Im Rahmen der konzernweiten Umstrukturierung (Projekt RHEINGOLD 2030) hat das Unternehmen beschlossen, den DB-Plan in einen beitragsorientierten Plan (確定拠出年金, DC-Plan) zu ueberfuehren. Der Aenderungsvertrag wurde am 28.02.2026 von der Unternehmensleitung und der Betriebsgewerkschaft-Mehrheit (67% der Mitglieder) unterzeichnet.

Die Beklagte - als Vertreter der Minderheitsfraktion (33%) - bestreitet die Wirksamkeit des Aenderungsvertrags mit der Begruendung, die Zustimmungsquote habe nach dem internen Gewerkschaftsstatut 75% betragen muessen.

II. Rechtliche Wuerdigung

1. Anwendbares Recht: 確定給付企業年金法 Art. 8 (Planaenderung), Art. 14 (Genehmigungspflicht MHLW)

2. Zustimmungserfordernis: Art. 8 Abs. 2 DB-Pensionsgesetz verlangt die Zustimmung der Arbeitnehmervertreter. Die interne Entscheidung der Gewerkschaft faellt in deren Autonomie (Gewerkschaftsautonomie nach Arbeitsgewerkschaftsgesetz, Art. 5). Dass das Gewerkschaftsstatut 75% verlangt, ist eine interne Anforderung ohne externe Wirkung auf den Aenderungsvertrag.

3. MHLW-Genehmigung: Der Antrag nach Art. 4 DB-Pensionsgesetz wurde am 15.03.2026 eingereicht (K-JP-4). Das MHLW hat in einem Vorpruefungsgespraech signalisiert, dass keine formalen Maengel erkennbar sind. Genehmigung erwartet Q3 2026.

Antrag: Das Gericht moege feststellen, dass der Aenderungsvertrag vom 28.02.2026 wirksam und vollziehbar ist.

Yuki Yamamoto-Brennecke
Treuenfels Yamamoto - Kyoto-Buero
Gion-Higashi, Shijo-dori, 605-0073 Kyoto
bengoshi-Nr. 48817 (Tokyo Bar Association)
"""))

    elems += mini_header("TERMINOLOGIE-GLOSSAR DE/JP")
    glossar = [
        ["Deutscher Begriff", "Japanisch (Kanji)", "Lateinumschrift"],
        ["Betriebliche Altersversorgung", "企業年金", "kigyo-nenkin"],
        ["Leistungszusage (DB)", "確定給付企業年金", "kakutei-kyufu-kigyo-nenkin"],
        ["Beitragszusage (DC)", "確定拠出年金", "kakutei-kyoshutsu-nenkin"],
        ["Ministerium f. Gesundheit/Arbeit", "厚生労働省", "Kosei-Rodo-sho (MHLW)"],
        ["Genehmigung", "承認", "shonin"],
        ["Stempel / Hanko", "判子 / 印鑑", "hanko / inkan"],
        ["Betriebsgewerkschaft", "企業内組合", "kigyo-nai-kumiai"],
        ["Aenderungsvertrag", "変更協定", "henko-kyotei"],
        ["Unverfallbare Anwartschaft", "既得権", "kitokuken"],
        ["Arbeitnehmervertreter", "労働者代表", "rodoshadaihyo"],
        ["Plansschliessung", "プランの閉鎖", "puran no heisa"],
        ["Rentner / Leistungsempfaenger", "年金受給者", "nenkin-jukyusha"],
        ["Arbeitsgericht Tokyo", "東京地方裁判所", "Tokyo Chino Saibansho"],
        ["Versicherungsgesellschaft", "保険会社", "hoken-gaisha"],
        ["Genehmigungsantrag", "申請書", "shinseisho"],
    ]
    gt = Table(glossar, colWidths=[155, 120, 145])
    gt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.Color(0.96,0.96,1.0)]),
        ('GRID', (0,0), (-1,-1), 0.3, colors.Color(0.7,0.7,0.8)),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5),
    ]))
    elems.append(gt)
    elems.append(sp(8))
    elems.append(handw("Yamamoto-Brennecke [Notiz an A.v.S.-O.]: Die Tokyo District Court-Richter sind pragmatisch - das Verfahren laeuft unspektakulaer. MHLW-Hanko ist das eigentliche Hindernis. Geduld!"))
    elems.append(PageBreak())
    return elems


def build_ias19_deep_dive():
    """IAS 19 Deep Dive - extended actuarial analysis"""
    from reportlab.platypus import Table, TableStyle
    elems = []
    elems += section_header("IAS-19-TIEFENANALYSE", "Rollforward-Detail und Sensitivitaetsanalyse * Counsel F. Albrecht-Niermann * Hellmrich-Vogt Aktuarpartner GmbH")

    elems.append(P("""<b>IAS 19-ROLLFORWARD-ANALYSE 2025 - MEISSNER RHEINWERK AG (DEUTSCHLAND)</b>
Erstellt von: Friederike Albrecht-Niermann (Counsel, Treuenfels Yamamoto)
Datenbasis: Hellmrich-Vogt Aktuarpartner GmbH, Bewertung per 31.12.2025
Aktenzeichen: TY-2026-RHEINGOLD-001/IAS19-DE-01

<b>I. DBO-Rollforward Deutschland 2025 (in EUR Mio.)</b>
"""))

    rollforward = [
        ["POSITION", "2025", "2024", "Veraenderung", "Kommentar"],
        ["DBO Jahresanfang (01.01.)", "2.283", "2.441", "-158", "Zinsanstieg 2024 Haupttreiber"],
        ["Current Service Cost", "18,4", "15,2", "+3,2", "Gehalterhoehungen hoher als Annahme"],
        ["Interest Cost (3,85% / 3,40%)", "87,9", "83,0", "+4,9", "Diskontzinsanstieg wirkte entgegen"],
        ["Past Service Cost / Curtailment", "0,0", "-12,4", "+12,4", "2024: Schliessung VO 1973 Teilgruppe"],
        ["Rentenzahlungen (Abgang)", "-94,2", "-91,8", "-2,4", "Lfd. Rentenzahlungen planmaessig"],
        ["Actuarial Losses / (Gains) - Zinsen", "48,3", "-112,7", "+161,0", "Zinssenkung Q4/2025 Treiber"],
        ["Actuarial Losses / (Gains) - Demo.", "12,8", "7,4", "+5,4", "Sterblichkeit guenstiger als Annahme"],
        ["Akquisitionen / Abgaenge", "0,0", "0,0", "---", "Kein M&A 2025 (RHEINORGANICS noch lfd.)"],
        ["Waehrungseffekte (DE: n/a)", "0,0", "0,0", "---", "---"],
        ["DBO Jahresende (31.12.)", "2.356", "2.283", "+73", ""],
        ["davon: aktive Anwaerter", "1.240", "1.190", "+50", ""],
        ["davon: Anwaerter in Wartephase", "380", "395", "-15", ""],
        ["davon: Rentner lfd.", "736", "698", "+38", "Demographischer Anstieg"],
    ]
    rt = Table(rollforward, colWidths=[190, 50, 50, 65, 125])
    rt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.Color(0.95,0.95,1.0)]),
        ('FONTNAME', (0,-4), (0,-4), 'Helvetica-Bold'),
        ('BACKGROUND', (0,-4), (-1,-4), colors.Color(0.88, 0.88, 0.95)),
        ('GRID', (0,0), (-1,-1), 0.3, colors.Color(0.7,0.7,0.8)),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
    ]))
    elems.append(rt)
    elems.append(sp(8))

    elems.append(P("""<b>II. Plan-Asset-Rollforward 2025 (CTA Rheinland Trust e.V.)</b>

Das CTA-Sicherungsvermoegen hat sich im Geschaeftsjahr 2025 wie folgt entwickelt (EUR Mio.):
"""))

    assets = [
        ["POSITION", "2025", "2024"],
        ["Plan Assets Jahresanfang", "784", "732"],
        ["Erwartete Rendite (Expected Return)", "31,4", "26,8"],
        ["Tatsaechliche Rendite ueber Erwartung (OCI)", "18,7", "-14,2"],
        ["Arbeitgeber-Beitraege", "15,0", "20,0"],
        ["Rentenzahlungen aus CTA", "-28,1", "-25,3"],
        ["Verwaltungskosten CTA", "-1,0", "-0,9"],
        ["Plan Assets Jahresende", "820", "784"],
        ["Bedeckungsgrad (Plan Assets / DBO)", "34,8%", "34,3%"],
    ]
    at = Table(assets, colWidths=[280, 80, 80])
    at.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.Color(0.95,0.95,1.0)]),
        ('BACKGROUND', (0,-2), (-1,-2), colors.Color(0.88,0.88,0.95)),
        ('FONTNAME', (0,-2), (-1,-2), 'Helvetica-Bold'),
        ('GRID', (0,0), (-1,-1), 0.3, colors.Color(0.7,0.7,0.8)),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5),
    ]))
    elems.append(at)
    elems.append(sp(8))

    elems.append(P("""<b>III. Sensitivitaetsanalyse - Wesentliche Annahmen</b>

Die nachfolgende Sensitivitaetsanalyse zeigt die Auswirkung von Parameteraenderungen auf die DBO per 31.12.2025 (EUR Mio.):
"""))

    sens = [
        ["PARAMETER", "Basiswert", "+100 BP / +1%", "DBO-Wirkung (+)", "-100 BP / -1%", "DBO-Wirkung (-)"],
        ["Diskontzins", "3,85%", "4,85%", "-312 (DBO sinkt)", "2,85%", "+373 (DBO steigt)"],
        ["Gehaltstrend", "3,50%", "4,50%", "+148 (DBO steigt)", "2,50%", "-128 (DBO sinkt)"],
        ["Rentenanpassung (§ 16)", "2,00%", "3,00%", "+94 (DBO steigt)", "1,00%", "-81 (DBO sinkt)"],
        ["Lebenserwartung", "DAV 2018G", "+1 Jahr Lebenserw.", "+68 (DBO steigt)", "-1 Jahr Lebenserw.", "-62 (DBO sinkt)"],
        ["Fluktuation", "3,80%", "+2% Fluktuation", "-18 (DBO sinkt)", "-2% Fluktuation", "+22 (DBO steigt)"],
    ]
    st = Table(sens, colWidths=[95, 55, 60, 85, 60, 85])
    st.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.Color(0.95,0.95,1.0)]),
        ('GRID', (0,0), (-1,-1), 0.3, colors.Color(0.7,0.7,0.8)),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
    ]))
    elems.append(st)
    elems.append(sp(8))

    elems.append(P("""<b>IV. Kommentar zur Sensitivitaet (Albrecht-Niermann, 27.03.2026)</b>

Die Sensitivitaetsanalyse belegt das erhebliche Zinsaenderungsrisiko der deutschen bAV-Bestaende: Eine Zinssenkung um 100 Basispunkte wuerde die DBO um EUR 373 Mio. auf ca. EUR 2.729 Mio. steigen lassen. Dies haette unmittelbare Auswirkungen auf:

(a) Die IAS-19-OCI-Bewegung im Konzerneigenkapital (ca. EUR -280 Mio. after tax);
(b) Den PSVaG-Beitrag (hoehere BBG, sofern CTA nicht entsprechend aufgestockt wird);
(c) Die Dealstruktur RHEINORGANICS: Der Pre-Closing Pension Deficit wuerde entsprechend ansteigen und die Kaufpreisanpassung nach Section 12.7 SPA ausloesen.

Das Management hat das Zinsaenderungsrisiko bislang nicht vollstaendig durch Liability-Driven-Investment (LDI)-Strategien im CTA gehedgt. Der Bedeckungsgrad von 34,8% ist zu gering fuer ein vollstaendiges Hedging. Empfehlung: Aufstockung CTA-Beitraege um mindestens EUR 50 Mio. p.a. ueber die naechsten 5 Jahre und Umschichtung des CTA-Portfolios in laengere Duration (10-15 Jahre Anleihen statt aktuell 7-8 Jahre).

<b>V. Globaler DBO-Uberblick (IAS 19, alle Jurisdiktionen, 31.12.2025)</b>
"""))

    global_dbo = [
        ["LAND / ENTITAET", "DBO (Waehrung)", "DBO (EUR Mio.)", "Plan Assets (EUR Mio.)", "Net Liability (EUR Mio.)"],
        ["Deutschland (Konzernmutter)", "EUR 2.356 Mio.", "2.356", "820", "1.536"],
        ["Japan (Meissner Rhine Kagaku KK)", "JPY 18.400 Mio.", "112", "103", "9"],
        ["USA (Meissner Specialty Chemicals Inc.)", "USD 124 Mio.", "115", "108", "7"],
        ["UK (Meissner Rhine Industries Ltd.)", "GBP 89 Mio.", "103", "90", "13"],
        ["Frankreich (MR France SAS)", "EUR 62 Mio.", "62", "0", "62"],
        ["Schweiz (Meissner Rhine AG)", "CHF 48 Mio.", "50", "49", "1"],
        ["Niederlande (Meissner Rhine BV)", "EUR 38 Mio.", "38", "35", "3"],
        ["Singapur (Meissner Rhine Pte.)", "SGD 24 Mio.", "16", "0", "16"],
        ["Sonstige (>10 Laender)", "Divers", "128", "0", "128"],
        ["GLOBAL GESAMT", "---", "2.980", "1.205", "1.775"],
        ["Davon: Laut letzter Presse-/AR-Angabe", "---", "3.200", "1.205", "1.995"],
        ["Differenz (Bewertungsmethod./Runden)", "---", "220", "0", "220"],
    ]
    gdt = Table(global_dbo, colWidths=[155, 85, 65, 80, 80])
    gdt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [colors.white, colors.Color(0.95,0.95,1.0)]),
        ('BACKGROUND', (0,-3), (-1,-3), colors.Color(0.88,0.88,0.95)),
        ('FONTNAME', (0,-3), (-1,-3), 'Helvetica-Bold'),
        ('BACKGROUND', (0,-2), (-1,-1), colors.Color(0.96,0.92,0.88)),
        ('FONTNAME', (0,-2), (-1,-1), 'Helvetica-Oblique'),
        ('GRID', (0,0), (-1,-1), 0.3, colors.Color(0.7,0.7,0.8)),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
    ]))
    elems.append(gdt)
    elems.append(sp(6))
    elems.append(handw("Frau Brindeau-Lorbach: bitte vor Aufsichtsrat herausreden! Die 3,2 Mrd. kommen aus dem alten Hellmrich-Vogt-Report mit anderer Zinsbasis. Neue Zahl nach Q1-Anpassung ist 2,98 Mrd. - aber das sagt sich schlechter. A.v.S.-O."))
    elems.append(PageBreak())
    return elems


def build_cta_supplement():
    """CTA Supplement - detailed contract clauses"""
    elems = []
    elems += section_header("CTA-TREUHANDVERTRAG-SUPPLEMENT", "Sicherungstreuhand-Klauseln (Auszug Volltext) * CTA Rheinland Trust e.V. * Stand: 01.01.2026")

    elems.append(P("""<b>SICHERUNGSTREUHAND-VEREINBARUNG (AUSZUG)</b>
zwischen der Meissner Rheinwerk AG (Treugeberin)
und dem CTA Rheinland Trust e.V. (Treuhaender)
Fassung: 2023 mit Nachtrag 2025

<b>Paragr. 12 Sicherungstreuhand - Kernklauseln</b>

<b>Paragr. 12.1 Insolvenzschutz</b>

Das Treuhandvermoegen (Sicherungsmasse) wird vom Eigenvermoegen des Treuhaenders vollstaendig getrennt verwahrt und ist im Insolvenzfall der Treugeberin zugunsten der beguestigten Versorgungsberechtigten pfaendungs- und insolvenzfest. Die Insolvenzfestigkeit beruht auf:
(a) Dinglicher Rechtsposition der Berechtigten (BAG 3 AZR 18/12: echtes Treuhandverhaeltnis);
(b) Schuldrechtlichem Direktanspruch der Berechtigten gegen den Treuhaender (Paragr. 328 BGB);
(c) Aussonderungsrecht der Berechtigten in der Insolvenz der Treugeberin (Paragr. 47 InsO).

Zur Sicherung dieser Rechtspositionen hat die Treugeberin alle CTA-Mittel durch notariell beurkundete Abtretungserklaerungen (Anlage 3 zum Treuhandvertrag, ca. 320 Einzeldokumente) auf den Treuhaender uebertragen. Der Treuhaender verwaltet die Sicherungsmasse treuhnaenderisch fuer die Berechtigten.

<b>Paragr. 12.2 Verfuegungsbeschraenkungen</b>

Der Treuhaender darf ueber die Sicherungsmasse nur verfuegen:
(a) zur Erfullung faelliger Versorgungsleistungen (Rentenzahlungen) nach vorheriger schriftlicher Anforderung durch die Treugeberin;
(b) zur Anlage gemaess der Investmentrichtlinie (Anlage 4 zum Treuhandvertrag);
(c) bei Insolvenz der Treugeberin: nach Anweisung eines zu bestellenden Absonderungsverwalters oder nach Entscheidung des Insolvenzverwalters, jedoch stets zugunsten der Versorgungsberechtigten.

Unzulaessig sind insbesondere: Rueckuebertragungen an die Treugeberin (Ausnahme: Bewertungskorrektur bei DBO-Unterschreitung um mehr als 10%, Paragr. 15.3 dieses Vertrags), Verpfaendungen, Belastungen und Abtretungen ausserhalb der Investmentrichtlinie.

<b>Paragr. 12.3 Sicherungsumfang und Berechtigte</b>

Die Sicherungsmasse sichert saemtliche unverfallbaren Anwartschaften (Paragr. 1b BetrAVG) und laufende Renten der im Berechtigten-Register (Anlage 1 zum Treuhandvertrag) eingetragenen Versorgungsempfaenger. Das Berechtigten-Register wird vom Treuhaender gefuehrt und jaehrlich aktualisiert.

Derzeit (Stand 01.01.2026) sind erfasst:
- Rentner (laufende Leistungen): 4.300 Personen
- Aktive Anwaerter mit CTA-Sicherung: 2.840 Personen (Berechtigte nach VO 2019 und neueren)
- Nicht erfasst (Altzusagen vor CTA-Gruendung 2019): ca. 1.360 aktive Anwaerter (VO 1973, VO 1981)

<b>Handlungsbedarf:</b> Die ca. 1.360 aktiven Anwaerter aus VO 1973 und VO 1981 sind noch nicht in die CTA-Sicherung einbezogen. Diese Bestaende sind ausschliesslich durch den PSVaG und durch handelsrechtliche Rueckstellungen gesichert. Im Rahmen des CTA-Nachtrags 2026 (K-CTA-16) sollen auch diese Bestaende einbezogen werden. Kostenvolumen: ca. EUR 120-150 Mio. zusaetzliche CTA-Einzahlungen.

<b>Paragr. 13 Investmentrichtlinie</b>

Die Investmentrichtlinie (Anlage 4, gueltig bis 31.12.2026) sieht folgende strategische Asset-Allocation vor:

Anleihen (Staatsanleihen AAA, Duration 7-8 J.): 60%
Aktien (Streuung global, ESG-gefiltert): 30%
Immobilien (indirekt, REIT): 5%
Liquiditaet / Geldmarkt: 5%

Der Verwaltungsmandate-Vertrag mit der LBBW Asset Management GmbH (Vertrags-Nr. LBBW-AM-2021-CTA-RH-007) laeuft bis 31.12.2027. Die Renditeerwartung nach Kosten: 3,5-4,0% p.a.

Nach der juen Zinsaenderung (Diskontzins 3,85%) ist die Duration der Anleihenallokation nicht ausreichend, um das Zinsaenderungsrisiko zu hedgen (Duration CTA-Anleihen: 7,5 J. vs. Duration DBO: ca. 17-19 J.). Die Unterdeckung des Duration-Match betraegt ca. 10 Jahre. Hellmrich-Vogt empfiehlt LDI-Umschichtung, die eine neue Investmentrichtlinie 2026 erfordert.

<b>Paragr. 14 Berichtserstattung</b>

Der Treuhaender erstattet der Treugeberin quartalsmaessig einen Vermoegensausweis und jaehrlich einen Jahresabschluss (nach HGB). Der Jahresabschluss 2024 ist als K-CTA-10 in der Sonderakte II abgelegt.

Zusaetzlich hat der Treuhaender der PSVaG-Meldepflicht nachzukommen (Bescheinigung der Sicherungsmasse fuer PSVaG-Zwecke per 31.12. jedes Jahres, Frist: 28.02. des Folgejahres).

<b>Paragr. 15 Anpassungen des Sicherungsumfangs</b>

15.1 Erhoeht sich die DBO um mehr als 10% gegenueber dem Vorjahr, ist die Treugeberin verpflichtet, die Sicherungsmasse entsprechend aufzustocken (innerhalb von 6 Monaten nach Jahresabschluss).

15.2 Sinkt die DBO um mehr als 10%, kann die Treugeberin eine Rueckuebertragung des Ueberschussvermoegens beantragen. Der Antrag ist dem CTA-Beirat vorzulegen und bedarf der Bestaetigung durch den Aktuar.

15.3 Bei Unternehmensverkauf oder Carve-out (Betriebsuebergang i.S.v. Paragr. 613a BGB) sind die betroffenen Berechtigten aus dem Register auszutragen und die korrespondierenden Sicherungsmassen anteilig auf den Erwerber zu uebertragen, sofern dies mit der Treugeberin und dem Erwerber schriftlich vereinbart wird. Ohne eine solche Vereinbarung verbleibt die Sicherungsmasse beim CTA Rheinland Trust e.V.

Diese Klausel ist fuer den RHEINORGANICS-Carve-out relevant: Die Carve-out-Tranche A (Bestaende vor 2019, nicht CTA-gesichert) ist von Paragr. 15.3 nicht erfasst. Die Carve-out-Tranche B (Bestaende 2019 ff., CTA-gesichert, EUR 22 Mio. DBO) unterliegt Paragr. 15.3. Albion Bridge hat darauf in der SPA-Verhandlung hingewiesen (vgl. Section 12.3.4 SPA).

<b>Paragr. 16 Aufloesungsklausel</b>

Der Treuhandvertrag kann von der Treugeberin mit einer Frist von 24 Monaten gekundigt werden, sofern: (a) keine unverfallbaren Anwartschaften mehr bestehen und (b) alle laufenden Renten vollstaendig ausgezahlt wurden. Im Regelfall ist die Laufzeit des Vertrags auf die Lebensdauer des laengst lebenden Berechtigten ausgelegt - fuer die aktuellen Rentner also ca. 2045-2055.

Eine vorzeitige Auflosung zugunsten eines Pension-Buyout (Abloese durch Lebensversicherer, Paragr. 8 BetrAVG) ist moeglich, sofern alle Berechtigten zustimmen oder ein Sozialplan-Beschluss dies legitimiert. Die Hanseatica-Transaktion (K-BT-1 ff.) stellt einen solchen Abloesefall dar - der Treuhandvertrag endet insoweit fuer die uebergehenden Bestaende mit Wirksamkeit des Annuitaetenkaufs.
"""))
    elems.append(handw("Klausel 15.3 ist kritisch fuer Albion Bridge - wir brauchen schriftliche Bestaeigung, dass Tranche B (EUR 22 Mio.) mit auf ABCP uebergeht. Nachtrag zum CTA-Vertrag erforderlich. A.v.S.-O."))
    elems.append(PageBreak())
    return elems


def build_sozialplan_supplement():
    """Sozialplan detailed supplement"""
    from reportlab.platypus import Table, TableStyle
    elems = []
    elems += section_header("SOZIALPLAN-SUPPLEMENT", "Pension-Bestandteile * Wahlmodelle * Berechnungsbeispiele * Stand: 30.04.2026")

    elems.append(P("""<b>BERECHNUNGSBEISPIELE FUER DIE SOZIALPLAN-WAHLMODELLE</b>
Bearbeitung: Annika Beerbohm-Sittler (Senior Associate, Treuenfels Yamamoto)
Datum: 28. April 2026

<b>I. Wahlmodell-Uebersicht</b>

Der Sozialplan-Entwurf (Hauptakte) sieht drei Wahlmodelle fuer aktive Anwaerter vor. Nachfolgend werden Berechnungsbeispiele fuer drei repraesentative Mitarbeiterprofile dargestellt.

<b>Profil A: Senior-Anwaerter (gut geschuetzt durch Altbestand)</b>
Herr Mustermann A, geb. 14.08.1968 (Alter: 57)
Eintrittsdatum: 01.09.1989 (BZ bis Schliessung 31.03.2027: 37,5 Jahre)
Aktuelle Vergutung: EUR 72.000 brutto p.a. (EUR 6.000/Monat)
Versorgungsordnung: VO 1981 (endgehaltsbezogen, Steigerungssatz 0,3% p.a. BZ x Gehalt)
Anwartschaft per Stichtag: 37,5 J. x 0,3% x EUR 6.000 = EUR 675/Monat (brutto)
Anpassungsfaktor Paragr. 2 Abs. 1 BetrAVG: 37,5 / 45,5 = 82,4%
Erdiente Anwartschaft (unverfallbar): EUR 675/Monat x 82,4% / 82,4% = EUR 675/Monat (voll erdient da Stichtag >= Renteneintritt nahe)

Alternativ nach Zeitanteiligkeitsmodell: Vollleistung waere bei 45,5 J. BZ und Endgehalt EUR 6.000: 45,5 x 0,3% x EUR 6.000 = EUR 819/Monat. Zeitanteilig: EUR 819 x (37,5/45,5) = EUR 675/Monat. (Gleich - da Stichtagsmodell = Zeitanteiligkeitsmodell bei flachem Gehaltstraj)

<b>Wahlmodell 1 (Einfrierung + DC-Aufstockung):</b>
Einfrierte VO-1981-Rente: EUR 675/Monat (ab Rentenalter 67)
DC-Beitrag aus VO 2008 (5% AG fuer BZ > 5 J.): EUR 300/Monat bis Renteneintritt = EUR 300 x 12 x 9,5 J. = EUR 34.200 Gesamtbeitrag plus Rendite ca. EUR 48.500 Kapital => ca. EUR 180-250/Monat DC-Rente (bei Verrentung)
Anerkennungspraemie (>20 J. BZ): EUR 1.500 einmalig
Gesamterwartete Rente (67): ca. EUR 675 + EUR 200 = EUR 875/Monat (plus gesetzl. Rente)

<b>Wahlmodell 2 (Teilabfindung):</b>
Barwert der einfrieerten Anwartschaft (Diskontzins 3,85%, Sterbetafel DAV 2018G): ca. EUR 112.000
Abfindungsangebot Paragr. 3 BetrAVG-konform: EUR 56.000 (50% des Barwerts als freiwillige Leistung)
Plus DC-Aufstockung: EUR 34.200 (wie Modell 1)
Gesamtzahlung bei Wahl Modell 2: EUR 90.200 einmalig (steuerpflichtig gemaess Paragr. 34 EStG Fuenftelregelung)

<b>Wahlmodell 3 (Status-quo, keine Wahl):</b>
Einfrierte VO-1981-Rente: EUR 675/Monat ab 67
DC-Beitrag VO 2008 (4% fuer BZ < 5 J. Restlaufzeit - aber hier > 5 J., also 5%): wie Modell 1
Kein Sonderbonus

Empfehlung des Teams: Modell 1 ist fuer Profil A wirtschaftlich optimal. Modell 2 macht nur bei Liquiditaetsbedarf Sinn.
"""))

    elems.append(P("""<b>Profil B: Jungerer Anwaerter (kurze Betriebszugehoerigkeit)</b>
Frau Musterfrau B, geb. 22.03.1992 (Alter: 34)
Eintrittsdatum: 15.01.2018 (BZ bis Schliessung 31.03.2027: 9,25 Jahre)
Aktuelle Verguetung: EUR 48.000 brutto p.a. (EUR 4.000/Monat)
Versorgungsordnung: VO 2008 (beitragsorientiert, ohne VO 1981-Komponente)
DC-Anwartschaft per 31.03.2027: Arbeitgeberbeitraege kumuliert ca. EUR 17.760 plus Rendite EUR 3.900 = EUR 21.660 Guthaben

Bei Weiterfuehrung bis 67 (Beitrag 5% auf EUR 4.000 = EUR 200/Monat):
Beitrag 01.04.2027 bis 67 (weitere 32,75 J.): EUR 200 x 12 x 32,75 = EUR 78.600 plus Rendite (3,5% p.a. effektiv): Gesamtkapital ca. EUR 175.000 => bei Verrentung EUR 600-700/Monat DC-Rente

Plus gesetzliche Rente (Paragr. 4 SGB VI-Optik): ca. EUR 1.800-2.100/Monat (eigenstaendige Einschaetzung HR).

Fuer Profil B ist die DC-Losung attraktiv und die Einfrierung hat kaum Auswirkungen (VO 2008 laeuft weiter).

<b>Profil C: Fuehrungskraft mit Einzelzusage (FK-031)</b>
Herr Muster C, geb. 08.11.1975 (Alter: 50)
Eintrittsdatum: 01.07.2005 (BZ bis Schliessung: 21,75 Jahre)
Verguetung: EUR 145.000 Fixgehalt + EUR 60.000 variabler Anteil (Durchschnitt)
Einzelzusage FK-031: Betriebsrente EUR 2.400/Monat ab 65 (Gesamtversorgungsebene), davon abzgl. gesetzl. Rente ca. EUR 1.200/Monat netto Direktzusage
Zielversorgung mit VO 1981-Anteil: Anteil VO 1981 auf EUR 720/Monat, Einzelzusage auf EUR 480/Monat differenziert

Einfrierung VO 1981-Komponente: EUR 720 x (21,75/37,25) = EUR 420/Monat
Einzelzusage FK-031: keine Einfrierung vorgesehen ohne individuelle Vereinbarung (§ 5.3.1 Sozialplan-Entwurf sieht FK-Gesprae vor)
Empfehlung: Einzelgesprach mit Muster C bis 30.06.2026, Angebot Aufhebungsvertrag mit Abfindungskomponente fuer FK-031-Zusage: Barwert ca. EUR 180.000, Abfindungsangebot EUR 95.000 plus DC-Aufstockung EUR 50.000.

<b>II. Gesamtkosten Sozialplan Pension-Bestandteile</b>
"""))

    sozkosten = [
        ["POSITION", "Anzahl Berechtigte", "Kosten pro Person", "Gesamtkosten (EUR Mio.)"],
        ["Anerkennungspramie >20 J. BZ (EUR 1.500)", "1.840", "EUR 1.500", "2,76"],
        ["DC-Aufstockung AG-Beitrag 4%->5%", "2.200", "ca. EUR 600/J.", "1,32 p.a."],
        ["Wahlmodell 2-Abfindungen (geschaetzt 15%)", "450", "ca. EUR 45.000", "20,25"],
        ["FK-Einzel-Abfindungen (FK-001 ff.)", "12", "ca. EUR 95.000", "1,14"],
        ["Obergutachter-Kosten Einigungsstelle", "---", "EUR 35.000", "0,04"],
        ["Rechtsberatungskosten Sozialplan", "---", "Laufend (TY)", "0,48"],
        ["GESAMT Einmalkosen (exkl. lfd. DC-Beitrag)", "---", "---", "24,47"],
        ["GESAMT lfd. Mehrkosten p.a. (DC-Aufstockung)", "---", "---", "1,32"],
    ]
    skt = Table(sozkosten, colWidths=[185, 80, 100, 100])
    skt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.Color(0.95,0.95,1.0)]),
        ('FONTNAME', (0,-2), (-1,-1), 'Helvetica-Bold'),
        ('BACKGROUND', (0,-2), (-1,-1), colors.Color(0.88,0.88,0.95)),
        ('GRID', (0,0), (-1,-1), 0.3, colors.Color(0.7,0.7,0.8)),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5),
    ]))
    elems.append(skt)
    elems.append(sp(6))
    elems.append(handw("Beerbohm-Sittler [28.04.]: Die EUR 24,5 Mio. Einmalkosten muessen in der Sozialplan-Rueckstellung 2026 erfasst werden. Engelhart-Volz muss steuerliche Behandlung klaeren (Paragr. 4e EStG, Betriebsausgabenabzug). A.v.S.-O. bestaetigt Weiterleitung."))
    elems.append(PageBreak())
    return elems


def build_uk_supplement():
    """UK Section 75 detailed analysis"""
    elems = []
    elems += section_header("UK-MODUL SUPPLEMENT", "Section 75 Employer Debt - Detailed Analysis * Pemberton Hawkesworth Solicitors * TPR Clearance")

    elems += fax_block(
        lines=[
            "PEMBERTON HAWKESWORTH SOLICITORS",
            "14 St Helen's Place, London EC3A 6DE",
            "DX: 876 London/City | Tel: +44 20 7626 0000",
            "Reference: PH/2026/MRI/0041",
            "",
            "MEMORANDUM - PRIVILEGED AND CONFIDENTIAL",
            "To:   Prof. Dr. Adalbert von Sompeh-Ostermann, Treuenfels Yamamoto",
            "From: Henry Pemberton-Aldgate, Partner; Charlotte Hawkesworth-Cross, Senior Associate",
            "Date: 22 February 2026",
            "Re:   Section 75 Employer Debt - Meissner Rhine Industries Ltd.",
            "      DB Plan separation in connection with RHEINORGANICS carve-out",
            "",
            "1. BACKGROUND",
            "",
            "Meissner Rhine Industries Ltd. (MRI) is the UK subsidiary and sponsor",
            "of the Meissner Rhine Industries Pension Scheme (the 'Scheme').",
            "The Scheme is a defined benefit occupational pension scheme with",
            "approximately 580 deferred members and 210 current pensioners.",
            "",
            "The proposed carve-out of the RHEINORGANICS business unit from MRI",
            "may constitute a 'cessation event' under the Pensions Act 2004,",
            "Section 38 and the Employer Debt Regulations 2005 (SI 2005/678).",
            "",
            "2. SECTION 75 DEBT ANALYSIS",
            "",
            "Under Section 75 PA 2004 and Reg 6 Employer Debt Regs, where a",
            "participating employer ceases to employ active members in a multi-",
            "employer scheme, a Section 75 debt crystallises immediately.",
            "",
            "Current Section 75 debt estimate (February 2026):",
            "  Scheme Assets:          GBP  89,400,000",
            "  Section 75 Liabilities: GBP 103,700,000  (gilts + 0.5% basis)",
            "  Gross Section 75 Debt:  GBP  14,300,000",
            "",
            "Note: This is BELOW the cap agreed in the SPA Schedule 12 (GBP 18M).",
            "The Pension Regulator (TPR) Clearance is recommended (not mandatory",
            "for this transaction size) to provide comfort to MRI and Albion Bridge.",
            "",
            "3. CLEARANCE STRATEGY",
            "",
            "We recommend applying for Clearance from The Pensions Regulator",
            "under PA 2004 Section 42 (Type C event: scheme rescue). The",
            "application should include:",
            "  (a) Full actuarial valuation basis (Scheme Actuary: Green & Lewis LLP)",
            "  (b) Mitigation package: MRI to contribute GBP 5M to Scheme at Closing",
            "  (c) Employer covenant assessment (Fitch methodology)",
            "  (d) Draft Deed of Separation (Pemberton Hawkesworth to prepare)",
            "",
            "Timeline: Application submission April 2026, clearance expected",
            "          June-July 2026 (TPR standard turnaround 6-10 weeks).",
        ],
        sender="Pemberton Hawkesworth Solicitors London via Fax", 
        receiver="Treuenfels Yamamoto Duesseldorf",
        date="22.02.2026 16:30 GMT", pages="5 von 5"
    )
    elems.append(sp(8))

    elems.append(P("""<b>UK-PENSION SCHEME TRUSTEE BOARD MINUTES (AUSZUG)</b>
Meeting: Trustee Board Q1 2026
Date: 10 March 2026
Venue: Pemberton Hawkesworth Solicitors, 14 St Helen's Place, London
Present: Chairman H. Wilkinson-Smyth (Independent Trustee), Member Trustee R. Goodspeed, Employer Trustee J. Blackmore-MRI

Agenda Item 4: RHEINORGANICS Carve-Out - Section 75 and DB Closure

The Board noted the memo from Pemberton Hawkesworth dated 22 February 2026 regarding the potential Section 75 Employer Debt crystallisation. Key discussion points:

4.1 The Independent Trustee (Wilkinson-Smyth) expressed concern about the adequacy of the proposed GBP 5M contribution at Closing: 'This does not address the full Section 75 shortfall. The members' security is paramount. We require independent actuarial advice from the Scheme Actuary before endorsing any mitigation package.'

4.2 The Employer Trustee (Blackmore-MRI) confirmed that MRI has instructed Pemberton Hawkesworth to prepare a Clearance application and that the TPR submission will be made in April 2026.

4.3 The Board resolved to: (a) Commission independent actuarial assessment from Green & Lewis LLP; (b) Write to TPR for pre-clearance guidance; (c) Require MRI to increase the mitigation contribution to at least GBP 7M if actuarial assessment confirms current shortfall above GBP 14M; (d) Not to consent to the RHEINORGANICS transfer before TPR Clearance is received.

Action: Pemberton Hawkesworth to submit TPR application by 30 April 2026.
Action: Green & Lewis LLP to deliver actuarial assessment by 31 March 2026.

[End of relevant extract. Full minutes: K-UK-5]

<b>Deutsche Zusammenfassung (A. Beerbohm-Sittler, TY):</b>
Der UK-Trustee-Board ist kritisch aber konstruktiv. Der wesentliche Stolperpunkt: Der Trustee-Board will TPR-Clearance BEVOR er der RHEINORGANICS-Transaktion zustimmt. Das ist eine Closing-Bedingung (Condition Precedent) im SPA. Zeitplan: TPR-Clearance bis Juli 2026 geplant. Frist fuer SPA-Signing: 30.06.2026 - Engpass! Albion Bridge muss ggf. Signing-Datum auf August 2026 verschieben. Bitte Otterbach-Veltheim informieren.

<b>Empfehlung Treuenfels Yamamoto:</b>
Die SPA-Closing-Condition muss angepasst werden: Statt 'UK TPR Clearance vor Signing' sollte es 'UK TPR Clearance vor Closing' lauten. Das gibt 3-4 Monate mehr Puffer. Pemberton Hawkesworth unterstuetzt diesen Ansatz (Ploeger-Heinekamp in Deutschland bestaetigt die analoge Situation bei deutschen Einigungsstellen-Voraussetzung). A.v.S.-O.
"""))
    elems.append(handw("Timing UK / DE / JP: alle laufen auf Herbst 2026 zu - Closing vor Dezember 2026 unwahrscheinlich. Albion Bridge muss akzeptieren oder Preis anpassen. A.v.S.-O."))
    elems.append(PageBreak())
    return elems


def build_bafin_memo():
    """BaFin Pensionsfonds Genehmigung"""
    elems = []
    elems += section_header("BaFin-AKTE", "Pensionsfonds-Erweiterung * VA 31-Q 5232-2026/0014 * Genehmigungsverfahren")

    elems.append(P("""<b>SCHREIBEN AN DIE BUNDESANSTALT FUER FINANZDIENSTLEISTUNGSAUFSICHT (BaFin)</b>
Treuenfels Yamamoto Rechtsanwaelte Partnerschaft mbB
Dr. Roman Engelhart-Volz (Counsel Tax)
Aktenzeichen TY: TY-2026-RHEINGOLD-001/BAFIN-01

An die Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin)
Referat VA 31 (Versicherungsaufsicht - Pensionsfonds)
Marie-Curie-Str. 24-28
60439 Frankfurt am Main

Frankfurt, 01. Februar 2026

<b>Betreff: Antrag auf Genehmigung der Erweiterung des Meissner Rheinwerk AG Pensionsfonds</b>
<b>Ihr Aktenzeichen (soweit vorliegend): VA 31-Q 5232-2026/0014</b>
<b>Mandantin: Meissner Rheinwerk AG, Duesseldorf-Reisholz</b>

Sehr geehrte Damen und Herren,

wir zeigen die anwaltliche Vertretung der Meissner Rheinwerk AG an und uebermitteln Ihnen den beigefuegten Antrag auf Genehmigung der Erweiterung des Pensionsfonds der Meissner Rheinwerk AG (Meissner Rheinwerk AG Pensionsfonds e.V., eingetragen im Vereinsregister Duesseldorf VR 3841) gemaess Paragr. 234 VAG.

<b>I. Antragsgegenstand</b>

Der Meissner Rheinwerk AG Pensionsfonds e.V. ist seit 2009 als Pensionsfonds im Sinne von Paragr. 236 VAG zugelassen (BaFin-Erlaubnisbescheid vom 12.06.2009, Gesch.-Z. VA31-I 5342-C-2009-0031). Er dient derzeit als Vehikel fuer die beitragsorientierte Versorgung der im Inlandsbereich taetigen Mitarbeiter (VO 2008, ca. 2.840 aktive Anwaerter).

Die Erweiterung betrifft:
(a) <b>Aufnahme von Versorgungsberechtigten aus den Konzerngesellschaften Meissner Rhine Chemicals GmbH (Hannover) und Meissner Organik GmbH (Leverkusen)</b>, die bislang keinen eigenen Pensionsfonds haben und uber eine Direktversicherung (Paragr. 1b Abs. 2 BetrAVG) abgesichert sind. Die Umstellung auf den Pensionsfonds soll zum 01.01.2027 erfolgen (ca. 340 zusaetzliche Anwaerter).
(b) <b>Erweiterung des Sicherungsvermogens um EUR 180 Mio.</b> durch Einzahlung aus dem CTA Rheinland Trust e.V. (Umschichtung CTA-Mittel in Pensionsfonds-Deckunsrueckstellung, Paragr. 236 Abs. 1 S. 2 VAG).
(c) <b>Aufnahme von Rentnern aus dem Buyout-Programm</b> (ca. 4.300 Rentner, Hanseatica-Transaktion), soweit der Buyout technisch ueber den Pensionsfonds abgewickelt wird (Alternative: direkte Vertragsuebernahme durch Hanseatica Lebensversicherung AG gemaess Paragr. 4 Abs. 4 BetrAVG ohne Pensionsfonds-Durchleitung).

<b>II. Rechtliche Grundlagen</b>

Paragr. 236 VAG: Pensionsfonds-Definition und Erlaubnispflicht
Paragr. 234 VAG: Genehmigung von Satzungsaenderungen und Geschaeftserweiterungen
IORP-II-Richtlinie 2016/2341/EU Art. 5, 12: Genehmigungsanforderungen EbAV
Paragr. 1b Abs. 3 BetrAVG: Pensionsfonds als zulassiger Durchfuehrungsweg

<b>III. Erforderliche Unterlagen (beigefuegt)</b>

Anlage A: Geaenderte Satzung Meissner Rheinwerk AG Pensionsfonds e.V. (Entwurf)
Anlage B: Aktuarielle Tragfahigkeitsbescheinigung (Hellmrich-Vogt, Koeln, 28.01.2026)
Anlage C: Geschaftsplan (aktualisiert 2026)
Anlage D: Fit-and-Proper-Erklaerungen der Vorstandsmitglieder des Pensionsfonds
Anlage E: Kapitalanlageplan und Investmentrichtlinie 2026
Anlage F: Auszug aus dem Versorgungswerk-Vertrag (Meissner Rheinwerk AG / Pensionsfonds e.V.)
Anlage G: Aktuelle Bilanz und GuV des Pensionsfonds (HGB, per 31.12.2025)
Anlage H: Nachweis Solvenzkapitalanforderungen (Paragr. 237 VAG, EUR 12 Mio. Mindestkapital)

<b>IV. Zeitplanung</b>

Wir bitten um Bearbeitung des Antrags im Vorrangverfahren aufgrund der Transaktionsrelevanz (Closing RHEINORGANICS Carve-out geplant Herbst 2026). Eine Vorabanfrage mit dem Referat VA 31 am 18.01.2026 hat ergeben, dass eine Bearbeitungszeit von 4-6 Monaten realistisch ist. Wir erwarten daher die Genehmigung bis spaetestens 31.07.2026.

Mit freundlichen Gruessen

<b>Dr. Roman Engelhart-Volz</b>
Counsel Tax | Treuenfels Yamamoto Rechtsanwaelte Partnerschaft mbB

<b>Prof. Dr. Adalbert von Sompeh-Ostermann, LL.M. (Oxford)</b>
Federf. Partner | Treuenfels Yamamoto Rechtsanwaelte Partnerschaft mbB
"""))

    elems.append(P("""<b>BaFin-RUECKFRAGEN-SCHREIBEN (AUSZUG)</b>
Bundesanstalt fuer Finanzdienstleistungsaufsicht
Referat VA 31
An: Treuenfels Yamamoto Rechtsanwaelte PartmbB

Frankfurt, 14. Maerz 2026
Unser Zeichen: VA 31-Q 5232-2026/0014

Betreff: Rueckfragen zum Genehmigungsantrag Meissner Rheinwerk AG Pensionsfonds e.V.

Sehr geehrter Herr Prof. Dr. von Sompeh-Ostermann,

wir beziehen uns auf Ihren Genehmigungsantrag vom 01. Februar 2026. Folgende Rueckfragen sind vor der Entscheidung zu klaeren:

<b>Rueckfrage 1:</b> Die Tragfahigkeitsbescheinigung (Anlage B) der Hellmrich-Vogt Aktuarpartner GmbH basiert auf einem Diskontzins von 3,40% (Bewertungszeitpunkt: 31.10.2025). Seit dem hat sich der Diskontzins auf 3,85% veraendert. Bitte reichen Sie eine aktualisierte Tragfahigkeitsbescheinigung per 31.12.2025 nach (Frist: 30.04.2026).

<b>Rueckfrage 2:</b> Der Kapitalanlageplan (Anlage E) sieht eine Immobilienquote von 5% vor. Bitte begruenden Sie die Vereinbarkeit mit der Anlageverordnung fuer Pensionsfonds (PFKapAV, Paragr. 3 Abs. 4: max 25% Immobilien) und dem Grundsatz der Anlagesicherheit (IORP-II Art. 19).

<b>Rueckfrage 3:</b> Der geplante Buyout mit der Hanseatica Lebensversicherung AG soll laut Anlage A als 'technische Uebertragung' ueber den Pensionsfonds abgewickelt werden. Bitte klaeren Sie, ob Hanseatica die Zulassung als Rueckversicherer fuer Pensionsfonds gemaess Paragr. 236 Abs. 3 VAG hat oder ob eine direkte Vertragsuebernahme nach Paragr. 4 Abs. 4 BetrAVG vorgesehen ist. Dies hat erhebliche aufsichtsrechtliche Konsequenzen.

<b>Frist fuer Rueckfragen-Beantwortung:</b> 30. April 2026

Mit freundlichem Gruss
gez. Dr. Beate Schaumloeffel-Werner
Referatsleiterin VA 31
Bundesanstalt fuer Finanzdienstleistungsaufsicht

[Intern: K-PSV-12 - in Sonderakte II]
"""))
    elems.append(handw("Engelhart-Volz muss RQ 3 zuerst klaeren - das ist die echte Falltuer. Wenn Hanseatica KEIN Paragr. 236 Abs. 3-Rueckversicherer ist, muessen wir Buyout ohne Pensionsfonds-Durchleitung strukturieren. Klaerung bis 20. April! A.v.S.-O."))
    elems.append(PageBreak())
    return elems


def build_rechtsbehelfsbelehrung():
    """Verfahrensrechtliche Hinweise und Rechtsmittelbelehrung"""
    elems = []
    elems += section_header("VERFAHRENSRECHTLICHE HINWEISE", "Rechtsmittelbelehrungen * Fristen * Aktenvermerke")

    elems.append(P("""<b>AKTENVERMERK: FRISTEN UND RECHTSMITTELFRISTEN (STAND 30.04.2026)</b>
Erstellt von: P. Schumann-Lindqvist (Trainee), geprueft von Prof. Dr. A. von Sompeh-Ostermann
Aktenzeichen: TY-2026-RHEINGOLD-001/FRISTEN-01

<b>I. Gerichtliche Fristen</b>

<b>1. ArbG Duesseldorf 7 BV 412/26 (Einigungsstelle)</b>
  - Status: Einigungsstellenbeschluss erwartet bis 15.05.2026
  - Anfechtungsfrist gegen Einigungsstellenbeschluss: 2 Wochen ab Zugang (Paragr. 76 Abs. 5 S. 4 BetrVG)
  - Anfechtungsfrist endet voraussichtlich: 29.05.2026
  - Zustaendig fuer Anfechtung: Arbeitsgericht Duesseldorf (Beschlussverfahren)
  - GBR-Anwalt Ploeger-Heinekamp hat Anfechtung bisher nicht angekuendigt
  - Risikobewertung: Anfechtungsrisiko gering (10%), da Mehrheitsbeschluss Dr. Wupperhain-Stein rechtssicher begruendet

<b>2. LAG Duesseldorf 14 TaBV 88/26 (Beschwerde Instanz)</b>
  - Status: Ruhendes Verfahren bis Einigungsstellenbeschluss
  - Bei erfolgloser Einigungsstelle: Beschwerde-Beschluss LAG erwartet H2 2026
  - Rechtsbeschwerdefrist BAG: 1 Monat ab Zustellung LAG-Beschluss
  - Aktenzeichen BAG angekuendigt: 3 ABR 14/27

<b>3. Tokyo District Court Heisei 8 (wa) No. 4421</b>
  - Status: Klage eingereicht, Klageantwort Beklagte erwartet bis 30.04.2026
  - Mundliche Verhandlung erwartet: Juni/Juli 2026 (Tokyo Timetable)
  - Rechtsmittel: Koto-Saibansho (High Court) innerhalb 14 Tagen ab Urteil
  - MHLW-Genehmigung separat: Q3 2026 (unabhaengig vom Gerichtsverfahren)

<b>II. Behoerdliche Fristen</b>

<b>4. PSVaG Beitragsbescheid 2026/A-RW-MEISSNER-008842</b>
  - Widerspruch eingelegt: 09.04.2026 (fristgemaess)
  - PSVaG-Entscheidungsfrist: keine gesetzliche Frist (VwVfG nicht anwendbar, PSVaG ist VVaG)
  - Praxis-Erfahrung: Entscheidung 2-4 Monate nach Widerspruch
  - Klage bei Verwaltungsgericht Koeln moeglich (oeff.-rechtl. Streitigkeit) als Alternative
  - Zustaendigkeit: Fraglich - PSVaG-Streitigkeiten laufen ueber ordentliche Gerichte (LG Koeln)

<b>5. BaFin VA 31-Q 5232-2026/0014</b>
  - Rueckfragen-Beantwortung Frist: 30.04.2026 (heute - Engelhart-Volz bearbeitet)
  - Genehmigungsentscheidung BaFin erwartet: Juli 2026
  - Widerspruchsmoelichkeit: Paragr. 48 VAG i.V.m. VwGO
  - Risikobewertung: Genehmigung wird mit Auflagen erteilt werden (Rueckfrage 3 kritisch)

<b>6. MHLW Japan - DB-Plan-Genehmigung (確定給付企業年金法 Art. 4)</b>
  - Antrag eingereicht: 15.03.2026
  - MHLW-Standardbearbeitungszeit: 3-6 Monate
  - Genehmigung erwartet: Q3 2026 (September/Oktober)
  - Hanko-Bestaeigung: separat nach Genehmigung (1-2 Wochen zusaetzlich)
  - Risikobewertung: Genehmigung wahrscheinlich (keine formalen Maengel erkennbar)

<b>III. Vertragliche Fristen</b>

<b>7. SPA RHEINORGANICS - Closing Conditions</b>
  - Einigungsstellen-Beschluss: erwartet 15.05.2026 (Condition: Beschluss rechtskraeftig = 29.05.2026)
  - UK TPR Clearance: erwartet Juli 2026
  - BaFin-Genehmigung: erwartet Juli 2026
  - MHLW-Genehmigung JP: erwartet September 2026
  - PBGC Form 10-Advance US: Frist 30 Tage vor Closing
  - Daraus: Fruehestmoegliches Closing Oktober 2026, wahrscheinlich November/Dezember 2026

<b>8. PSVaG-Beitrag 2026 (korrekte Hoehe)</b>
  - Vorbehaltszahlung geleistet: 08.04.2026, EUR 2.777.060
  - Erstattungsforderung bei erfolgreicher Korrektur: EUR 1.441.380
  - Zeitraum bis Erstattung: 3-6 Monate nach Widerspruchsentscheidung

<b>Handschriftlich ergaenzt [A.v.S.-O.]:</b>"""))
    elems.append(handw("Wichtig: PBGC-Frist 30 Tage vor Closing nicht vergessen! HPL muss Kalender fuehren. Und Tokyo: Urteil kommt vielleicht schon Mai - dann haben wir einen Prazedenzfall fuer MHLW-Antrag. Positiv. A.v.S.-O."))
    elems.append(sp(8))

    elems.append(P("""<b>AKTENVERMERK: RISIKOMATRIX PROJEKT RHEINGOLD 2030</b>
Datum: 28. April 2026
Erstellt: Prof. Dr. Adalbert von Sompeh-Ostermann

<b>MODUL - RISIKO - WAHRSCHEINLICHKEIT - AUSWIRKUNG - MASSNAHME</b>

DE-DB-Schliessung: Anfechtung Einigungsstellenbeschluss (GBR) - Gering (10%) - Hoch (Verzoegerung 6 Mo.) - BAG-Rechtsprechung klar, Vorsitz Dr. Wupperhain-Stein stuetzt AG-Seite

DE-IAS19: Zinssenkung EZB 100 BP - Mittel (30%) - Hoch (DBO+EUR 373 Mio.) - LDI-Hedge CTA, Kaufpreisanpassung SPA Section 12.7

Japan: MHLW verzogert Genehmigung > Q4 2026 - Mittel (25%) - Mittel (Closing-Verzoegerung) - Yamamoto-Brennecke direkte MHLW-Kontakte, Parallelverfahren Tokyo Court

US: PBGC Cessation Event Trigger - Gering (8%) - Mittel (Bussgeld max. USD 1.2 Mio.) - PBGC Form 10-Advance einreichen, HPL Boston begleitet

UK: TPR Clearance verweigert - Sehr gering (3%) - Sehr hoch (Section 75 unkontrolliert) - Proaktive Trustee-Kommunikation, Mitigation GBP 7 Mio.

Carve-out RHEINORGANICS: Albion Bridge zieht zurueck - Gering (12%) - Sehr hoch (EUR 18 Mio. Projektkosten verloren) - Deallogik solide, Closing Conditions einfuegen die Risiken limitieren

PSVaG: Widerspruch scheitert - Gering (15%) - Mittel (EUR 1.4 Mio. Verlust) - Erstattungsklage LG Koeln als Reserve

Tarifrecht: IG BCE verweigert Oeffnungsklausel-Zustimmung - Mittel (20%) - Hoch (Betriebsvereinbarung tarifwidrig) - ACIN-Koordination, IG-BCE-Direktkontakt HR-Vorstand

<b>Gesamtrisiko-Assessment:</b> Projekt RHEINGOLD 2030 ist komplex aber in allen Kernpunkten rechtlich durchfuehrbar. Die Hauptrisiken liegen im Timing (Japan, UK) und im Tarifrecht (IG BCE). Recommendation: Closing-Termin SPA auf Q1 2027 anpassen (statt Q4 2026). Das gibt Puffer fuer alle Genehmigungsverfahren.

Prof. Dr. Adalbert von Sompeh-Ostermann
28.04.2026
"""))
    elems.append(PageBreak())
    return elems


def build_versorgungsrecht_grundlagen():
    """Umfassendes versorgungsrechtliches Grundlagenkapitel"""
    elems = []
    elems += section_header("VERSORGUNGSRECHTLICHE GRUNDLAGEN", "Anwendbares Recht - Paragrafenregister - Rechtsprechungsuebersicht * TY-2026-RHEINGOLD-001/REF-01")

    elems.append(P("""<b>I. GESETZLICHE GRUNDLAGEN DER BETRIEBLICHEN ALTERSVERSORGUNG (DEUTSCHLAND)</b>

Das Betriebsrentengesetz (Gesetz zur Verbesserung der betrieblichen Altersversorgung - BetrAVG) bildet den zentralen Rechtsrahmen fuer die betriebliche Altersversorgung in Deutschland. Nachfolgend werden die im Mandat TY-2026-RHEINGOLD-001 relevanten Vorschriften erlaeutert.

<b>Paragr. 1 BetrAVG - Zusagearten</b>
Absatz 1 definiert die fuenf anerkannten Durchfuehrungswege: Direktzusage (Unmittelbare Versorgungszusage des Arbeitgebers), Direktversicherung (Lebensversicherung zugunsten Arbeitnehmer), Pensionskasse (regulierte Versorgungseinrichtung), Pensionsfonds (VAG-reguliert, Paragr. 236 ff. VAG) und Unterstuetzungskasse (steuerlich bevorrechtigte Einrichtung). Die Meissner Rheinwerk AG nutzt historisch die Direktzusage (VO 1973, VO 1981, VO 1995) und seit 2008 zusaetzlich den Pensionsfonds (VO 2008).

<b>Paragr. 1b BetrAVG - Unverfallbarkeit</b>
Die gesetzliche Unverfallbarkeit greift nach 3 Jahren Betriebszugehoerigkeit und einem Mindestalter von 21 Jahren (seit 01.01.2018, zuvor 5 Jahre / 25 Jahre). Fuer aeltere Zusagen aus VO 1973 / VO 1981 gelten Ubergangsgrenzen gemaess Paragr. 30f BetrAVG. Alle Anwaerter der Meissner Rheinwerk AG mit dem Eintrittsdatum ab 01.01.2018 unterliegen der neuen Unverfallbarkeitsregel.

<b>Paragr. 2 BetrAVG - Hoehe der unverfallbaren Anwartschaft</b>
Die zeitanteilige Berechnung nach Paragr. 2 Abs. 1 BetrAVG (pro-rata-temporis) bildet die Grundlage fuer alle Einfrierungsberechnungen im Rahmen der DB-Schliessung. Die Formel: Unverfallbare Anwartschaft = Vollleistung x (Betriebszugehoerigkeit bis Schliessung / moegliche Gesamtbetriebszugehoerigkeit bis Rentenalter 67). Diese Formel ist zwingend - abweichende Sozialplandregelungen zugunsten der Arbeitnehmer (grober Fehler in frueheren Sozialplandiskussionen) sind primaer zulassig, nicht aber zuungunsten.

<b>Paragr. 3 BetrAVG - Kapitalabfindung von Kleinstanwartschaften</b>
Die Kapitalabfindung ist moeglich, wenn die Anwartschaft die Grenzwerte unterschreitet (2026: EUR 34,65/Monat = 1/120 der Bezuggroesse nach Paragr. 18 SGB IV). Fuer Meissner Rheinwerk AG wurde festgestellt, dass ca. 340 Anwaerter (7,9%) die Kapitalabfindungsgrenze unterschreiten. Volumen: ca. EUR 4,2 Mio. Einmalbeitraege. Durchfuehrung empfohlen nach Sozialplan-Abschluss.

<b>Paragr. 4 BetrAVG - Uebertragung von Anwartschaften</b>
Abs. 4 regelt den Vertrag zugunsten Dritter bei Direktversicherungen und Pensionsfonds. Absatz 5 ermoglicht die Uebertragung von Direktzusagen bei Betriebsubergangen auf den neuen Arbeitgeber, soweit dieser zustimmt. Im Rahmen des RHEINORGANICS-Carve-out ist Paragr. 4 Abs. 5 BetrAVG einschlaegig: Albion Bridge als neuer Arbeitgeber muss der Ubernahme der RHEINORGANICS-Direktzusagen zustimmen (oder ablehnen mit Folge: Verbleib bei Meissner Rheinwerk AG).

<b>Paragr. 6a EStG - Pensionsrueckstellungen (steuerrechtlich)</b>
Die steuerliche Pensionsrueckstellung nach Paragr. 6a EStG unterscheidet sich von der IAS-19-Bewertung: Statt des Marktzinses wird ein fester Rechnungszinssatz von 6% verwendet. Fuer die Meissner Rheinwerk AG ergeben sich erhebliche Differenzen: Steuerliche Rueckstellung ca. EUR 1,1 Mrd. vs. IAS-19-DBO EUR 2,4 Mrd. Der Unterschied (ca. EUR 1,3 Mrd.) repraesentiert stille Lasten. Bei DB-Schliessung ist Paragr. 6a Abs. 4 EStG zu beachten: Die Rueckstellung ist entsprechend anzupassen.

<b>Paragr. 4d EStG - Zuwendungen an Unterstuetzungskassen</b>
Soweit Meissner Rheinwerk AG eine Unterstuetzungskasse unterhalt (historisch: Chemiewerk-Wohlfahrtskasse, seit 1998 liquidiert), sind die Zuwendungsregelungen irrelevant. Dr. Engelhart-Volz hat bestaetigt, dass keine aktive Unterstuetzungskasse mehr besteht.

<b>Paragr. 16 BetrAVG - Anpassungspruefung</b>
Die dreijahrige Anpassungspruefungspflicht des Arbeitgebers bezueglich laufender Renten erfordert eine Gegenuberstellung von Kaufkraftverlust und Unternehmensertrag. Die Formel nach BAG (3 AZR 304/13) beruecksichtigt den Reallohnbezug (Kaufkraftverlust als Obergrenze) und die wirtschaftliche Lage des Arbeitgebers (Ertragslage als Anpassungspflichtgrenze). Sonderfall CTA: Wenn das CTA-Vermoegen ausreicht, den Anpassungsbetrag zu finanzieren, kann der Arbeitgeber zur Anpassung verpflichtet sein, auch wenn die Ertragslage schlecht ist (Arg.: CTA-Mittel sind fuer Versorgungszwecke zweckgebunden).

<b>Paragr. 17 Abs. 3 BetrAVG - Oeffnung fuer Tarifpartner</b>
Tarifvertraege koennen von den gesetzlichen Mindeststandards des BetrAVG nur zugunsten der Arbeitnehmer abweichen (guenstigere Regelungen). Der Chemie-Nord-Versorgungstarifvertrag hat von dieser Oeffnungsklausel Gebrauch gemacht (Paragr. 14 Abs. 2: Betriebsvereinbarungsmoeglichkeit zur Leistungsreduzierung mit IG-BCE-Zustimmung). Dies ist systemwidrig - eigentlich darf der TV nur etwas zugunsten der Arbeitnehmer regeln, aber die IG BCE hat 2007 diese Klausel als 'Flexibilitaetsventil' akzeptiert. Rechtspolitisch umstritten, aber vom BAG noch nicht beanstandet.
"""))
    elems.append(PageBreak())

    elems.append(P("""<b>II. IORP-II-RICHTLINIE 2016/2341/EU - GOVERNANCE-ANFORDERUNGEN (AUSZUG)</b>

Die IORP-II-Richtlinie (Richtlinie des Europaeischen Parlaments und des Rates vom 14. Dezember 2016 ueber die Taetigkeiten und die Beaufsichtigung von Einrichtungen der betrieblichen Altersversorgung, ABl. EU L 354/37 vom 23.12.2016) ist seit dem 13.01.2019 in Deutschland durch das Betriebsrentenstaerkungsgesetz (BRSG 2018) und die VAG-Aenderungen 2019 umgesetzt.

<b>Art. 21 - Allgemeine Grundsaetze der Governance (System of Governance)</b>
Jede EbAV (Einrichtung der betrieblichen Altersversorgung) muss ein wirksames Governance-System einrichten, das eine solide und vorsichtige Unternehmensfuehrung gewaehrleistet. Dazu gehoeren:
- Klare und angemessene Organisationsstruktur mit transparenter Zuweisung von Verantwortung
- Wirksame Methoden zur Sicherstellung der Informationsuebermittlung
- Angemessene interne Kontrollmechanismen
- Wirksame Meldeverfahren fuer alle Risiken

Fuer den Meissner Rheinwerk AG Pensionsfonds e.V. bedeutet dies: Das GPC-Konzept (Global Pension Committee) erfullt Art. 21 nur teilweise. Der Pensionsfonds selbst benoetigt eine eigenstaendige Governance-Struktur (Vorstand mit Fit-and-Proper, Interne Revision, Risikomanagementsystem). Das wird im BaFin-Genehmigungsverfahren VA 31-Q 5232-2026/0014 geprueft.

<b>Art. 22 - Risikomanagement</b>
Die EbAV muss ein wirksames Risikomanagementsystem implementieren, das alle wesentlichen Risiken abdeckt: Versicherungstechnische Risiken, Finanzmarktrisiken, Kreditrisiken, Liquiditaets- und Konzentrationsrisiken, operationelle Risiken, Rechtsrisiken. Das Pension Risk Management Framework (PRMF, Entwurf K-GOV-02) ist bis 30.09.2026 fertigzustellen.

<b>Art. 24 - Versicherungsmathematische Funktion</b>
Die EbAV muss eine versicherungsmathematische Funktion einrichten (interne oder externe Besetzung). Hellmrich-Vogt Aktuarpartner GmbH wurde als externer Aktuar des Pensionsfonds nominiert. Die BaFin-Bestellungsanzeige ist Teil des Genehmigungsantrags (Anlage B).

<b>Art. 25-28 - Ausgliederung (Outsourcing)</b>
Wenn die EbAV Aufgaben an Dritte auslagert (wie hier: Treuenfels Yamamoto als Rechtsberater, LBBW AM als Kapitalanlagegesellschaft), muss ein schriftlicher Outsourcing-Vertrag vorliegen und die Auslagerung der BaFin gemeldet werden. Kritische Funktionen (interne Revision, versicherungsmathematische Funktion) duerfen nur mit BaFin-Zustimmung ausgelagert werden.

<b>Art. 27 - Eigenmittelanforderungen</b>
Pensionsfonds mussen ein Mindestkapital vorhalten: Max aus (Mindestkapital nach nationalem Recht, Paragr. 237 VAG: EUR 12 Mio.) und (0,25% der versicherungstechnischen Brutto-Rueckstellungen). Fuer den Meissner Rheinwerk AG Pensionsfonds e.V. gilt: Brutto-Rueckstellungen ca. EUR 180 Mio. => Solvenzkapital: Max(EUR 12 Mio., EUR 450.000) = EUR 12 Mio. Nachweis erfolgt gemaess Anlage H im BaFin-Antrag.
"""))
    elems.append(PageBreak())

    elems.append(P("""<b>III. MASS-GEBLICHE RECHTSPRECHUNG - REFERENZREGISTER</b>

<b>Drei-Stufen-Theorie (Grundsatzurteil)</b>
BAG, GS 1/82 vom 17.10.1983, AP BetrAVG Paragr. 1 Abloesung Nr. 3 - GRUNDSATZENTSCHEIDUNG des Grossen Senats des BAG zur Drei-Stufen-Theorie. Der Grosse Senat hat festgelegt, dass Verschlechterungen laufender Betriebsrenten und Anwartschaften differenziert nach ihrer Eingriffstiefe zu beurteilen sind. Stufe 1 (Eingriff in laufende Renten): Hoechste Huerde, nur bei existenzbedrohlichen wirtschaftlichen Schwierigkeiten zulassig. Stufe 2 (Eingriff in erdiente Anwartschaftsdynamik): Sachlicher Grund erforderlich. Stufe 3 (Eingriff in kuenftige, noch nicht erdiente Zuwachse): Sachlicher Proportionalitaetsgrund ausreichend. Diese Entscheidung ist unveraendert das Fundament der bAV-Rechtsprechung. Jeder Schriftsatz in einem bAV-Streit beginnt mit GS 1/82.

<b>Zinsaenderungsrisiko und Planschliessungen</b>
BAG, 3 AZR 392/06 vom 15.01.2013, NZA 2013, 795 - Detaillierung der Anforderungen an die sachliche Rechtfertigung auf Stufe 2 der Drei-Stufen-Theorie. Das BAG hat erstmals eine 'kaufmaennische Plausibilitaetspruefung' fuer unternehmerische Entscheidungen zur Eingrenzung von Pensionsverpflichtungen geforderti und konkretisiert. Sachlicher Grund = plausible, sachbezogene wirtschaftliche oder organisatorische Erwaegungen, die einem Drittvergleich standhalten wuerden.

<b>Future-Service-Stopp</b>
BAG, 3 AZR 540/16 vom 12.12.2017, AP BetrAVG Paragr. 1 Nr. 67 - Bestaetigung, dass der Stopp des weiteren Anwachsens von DB-Anwartschaften (Future-Service-Stopp) auf Stufe 3 der Drei-Stufen-Theorie einzuordnen ist und lediglich eines sachlichen Proportionalitaetsgrundes bedarf. Fuehrt zu einer erheblichen Erleichterung der Rechtfertigung gegenueber aelteren BAG-Urteilen.

<b>CTA-Insolvenzfestigkeit</b>
BAG, 3 AZR 18/12 vom 18.07.2013, NZA 2014, 36 - Grundsatzentscheidung zur Insolvenzfestigkeit des Doppeltreuhandmodells. Das BAG hat den CTA-Mechanismus als wirksam anerkannt: Das Sicherungsvermoegen kann im Insolvenzfall der Treugeberin nicht von Insolvenzglaeubigern in Anspruch genommen werden, sofern eine echte dingliche Rechtsposition der Versorgungsberechtigten besteht (echter Treuhandcharakter, Paragr. 47 InsO). Diese Entscheidung ist Grundlage des CTA Rheinland Trust e.V. und saemtlicher Abtretungserklaerungen.

<b>Paragr. 16-Anpassungspflicht</b>
BAG, 3 AZR 304/13 vom 10.03.2015, AP BetrAVG Paragr. 16 Nr. 81 - Prazisierung der Anpassungspruefungspflicht: Der Arbeitgeber ist zur Anpassung verpflichtet, wenn der Kaufkraftverlust es gebietet und die Ertragslage eine Anpassung erlaubt. Bei CTA-Sicherung kann die wirtschaftliche Lage des CTA-Vermogens relevant sein. Fuer Meissner Rheinwerk AG: Die Entscheidung ist massgeblich fuer die Dreijahrespruefung 2026.

<b>Datenschutz in der bAV</b>
EuGH, C-168/18 (Bauer/Willmeroth) vom 06.11.2018 - Wirksame Anwendung des Unionsrechts (Gleichbehandlungsrichtlinie) im Verhaeltnis zwischen Privaten bei Hinterbliebenenversorgung. Relevant fuer die Gestaltung der Hinterbliebenenklauseln in den Versorgungsordnungen.

<b>Insolvenzschutz europaeisch</b>
EuGH, C-396/22 (Generali Leben) vom 12.10.2023 - Prasizierung der Insolvenzschutzpflicht gemaess Richtlinie 2008/94/EG (Arbeitnehmerschutz bei Insolvenz des Arbeitgebers) im Kontext der betrieblichen Altersversorgung. Deutschland erfullt die Anforderungen durch das BetrAVG-Insolvenzsicherungssystem (PSVaG), soweit der Schutz vollstaendig ist.

EuGH, C-680/15 (Asklepios) vom 27.04.2017 - Haftung des Erwerbers bei Betriebsubergang nach Richtlinie 2001/23/EG fuer betriebliche Versorgungszusagen. Einschlaegig fuer den RHEINORGANICS-Carve-out: Albion Bridge als Erwerber haftet grundsaetzlich fuer alle Versorgungszusagen der RHEINORGANICS-Mitarbeiter ab Closing, soweit diese aus Dienstzeiten vor Closing resultieren (zeitanteilig).
"""))
    elems.append(PageBreak())

    elems.append(P("""<b>IV. STEUERRECHTLICHE GRUNDLAGEN (AUSZUG) - DR. ENGELHART-VOLZ</b>

<b>Paragr. 6a EStG - Pensionsrueckstellungen</b>
Die steuerliche Pensionsrueckstellung entsteht nach Paragr. 6a EStG fuer Pensionsverpflichtungen, die schriftlich zugesagt (§ 6a Abs. 1 Nr. 3 EStG) und ernsthaft gemeint sind (§ 6a Abs. 1 Nr. 1). Der Rechnungszinssatz ist gesetzlich auf 6% festgelegt (Paragr. 6a Abs. 3 S. 3 EStG). Die Diskrepanz zum IAS-19-Diskontzins (3,85%) fuehrt zu erheblichen Differenzen in der Rueckstellungshoehe.

Fuer Meissner Rheinwerk AG ergibt sich fuer die deutschen Direktzusagen:
Handelsrechtliche Rueckstellung (HGB, BilMoG-Zinssatz 10-Jahresdurchschnitt): EUR 1,8 Mrd.
Steuerliche Rueckstellung (Paragr. 6a EStG, 6%): EUR 1,1 Mrd.
IAS-19-DBO (IFRS, 3,85%): EUR 2,4 Mrd.

Bedeutung der Differenz: Der Unterschied zwischen steuerlicher Rueckstellung (EUR 1,1 Mrd.) und IAS-19-DBO (EUR 2,4 Mrd.) = EUR 1,3 Mrd. repraesentiert die 'stille Pensionslast' (Hidden Pension Liability). Bei einer Transaktion wird Albion Bridge diese stille Last in seine DCF-Bewertung einbeziehen.

<b>Betriebsausgabenabzug bei DB-Schliessung</b>
Die Kosten der DB-Schliessung (Sozialplan-Abfindungen, Aktuarskosten, Rechtsberatungskosten) sind als Betriebsausgaben nach Paragr. 4 Abs. 4 EStG abzugsfaehig. Die Sozialplan-Abfindungen fuer Versorgungsanwartschaften sind dabei steuerlich als Abloesezahlungen (Paragr. 4e EStG analog) zu behandeln.

Einmalige Sozialplan-Pension-Kosten (Schaetzung): EUR 24,5 Mio. => Steuerlicher Vorteil bei KSt-Satz 15% + Soli + GewSt effektiv ca. 30%: EUR 7,35 Mio. Steuerersparnis.

<b>Handelsbilanzielle Aspekte (HGB, BilMoG)</b>
Die handelsrechtliche Rueckstellung nach HGB Paragr. 249 Abs. 1 i.V.m. Art. 28 EGHGB (Ubergangsregelung BilMoG) weicht von IAS 19 und Paragr. 6a EStG ab. Der BilMoG-Zinssatz (10-Jaehriger Durchschnitt der Bundesbank) betraegt per 31.12.2025 ca. 4,8% (ruecklaufig). Die handelsrechtliche Rueckstellung ist daher hoeher als die steuerliche (6% fix) aber niedriger als IAS 19 (3,85% aktueller Zinssatz).

Relevanz: Bei der HGB-Aufstellung der deutschen Einzelgesellschaften (Meissner Rheinwerk AG Jahresabschluss) ist die HGB-Rueckstellung massgeblich, nicht IAS 19. Fuer Aufsichtsrat-Diskussionen und Pressemitteilungen wird IAS 19 (konzernabschluss) verwendet.
"""))
    elems.append(PageBreak())
    return elems


def build_schlussdokument():
    """Schluss-Dokument und Auftragsbestaetigung"""
    elems = []
    elems += section_header("AUFTRAGSBESTAETIGUNG UND MANDATSSTATUS", "Treuenfels Yamamoto PartmbB * Stand: 30.04.2026 * TY-2026-RHEINGOLD-001")

    elems.append(P("""<b>MANDATSSTATUS-BERICHT: PROJEKT RHEINGOLD 2030</b>
Datum: 30. April 2026
An: Henrick Otterbach-Veltheim (CFO), Dr. Constanze Brindeau-Lorbach (HR-Vorstand)
Von: Prof. Dr. Adalbert von Sompeh-Ostermann, LL.M. (Oxford)
Treuenfels Yamamoto Rechtsanwaelte Partnerschaft mbB

<b>I. Gesamtstatus Projekt RHEINGOLD 2030 (Ampel-Uebersicht)</b>

MODUL DB-Schliessung Deutschland: STATUS GELB
  Einigungsstellenbeschluss erwartet 15.05.2026. GBR-Zustimmung durch Mehrheitsbeschluss gesichert. Anfechtungsrisiko 10%.
  Tarifvertragliche IG-BCE-Zustimmung: noch ausstehend - kritis!

MODUL IAS 19 / Aktuar: STATUS GRUEN
  Hellmrich-Vogt-Bewertung Q1 2026 liegt vor. BaFin-Rueckfragen-Antwort bis 30.04. in Arbeit (Engelhart-Volz).

MODUL CTA-Erweiterung: STATUS GELB
  Nachtrag CTA Rheinland Trust (K-CTA-16) in Entwurf. Eintragung neuer Berechtigte (ca. 1.360) fehlt noch.

MODUL Pension Buyout Hanseatica: STATUS GRUEN
  Term Sheet vereinbart. Feinverhandlungen Annuitaet-Preisstellung laufen. Closing-Ziel: Gleichzeitig mit SPA-Closing.

MODUL PSVaG: STATUS GELB
  Widerspruch eingelegt 09.04.2026. Bearbeitung PSVaG laeuft.

MODUL Japan: STATUS GELB
  MHLW-Genehmigung Q3 2026 erwartet. Tokyo District Court: Urteil erwartet Mai-Juni 2026.

MODUL USA: STATUS GRUEN
  HPL Boston: PBGC Form 10-Advance vorbereitet. 401(k)-Amendment in Entwurf (Board-Beschluss ausstehend).

MODUL UK: STATUS GELB
  TPR Clearance-Antrag vorbereitet (Einreichung April 2026). Trustee-Bedenken adressiert. Mitigation GBP 7 Mio. akzeptiert.

MODUL BaFin Pensionsfonds: STATUS ROT
  Rueckfrage 3 (Hanseatica-Zulatung) kritisch. Engelhart-Volz klaert bis 20. April. Potenzielle Strukturaenderung Buyout erforderlich.

MODUL SPA/M&A RHEINORGANICS: STATUS GELB
  Section 12 weiter in Verhandlung. Albion Bridge auf Closing Q1 2027 vorbereitet. W&I-Versicherung Munich Re zugesagt.

<b>II. Naechste Schritte (Mai 2026)</b>

1. Einigungsstellenbeschluss (erwartet 15.05.2026) - Abschrift an GBR, BaFin, PSVaG
2. BaFin-Rueckfragen-Beantwortung (Frist 30.04.2026) - Engelhart-Volz / Albrecht-Niermann
3. ACIN-Kontakt Arbeitgeberverband NRW (IG-BCE-Oeffnungsklausel) - Sompeh-Ostermann
4. TPR Clearance Application UK - Pemberton Hawkesworth
5. 401(k)-Amendment Board-Beschluss MSC-US - HPL Boston / Meissner US-Rechtsabteilung
6. Nachtrag CTA-Treuhandvertrag (Erweiterung Berechtigte) - Albrecht-Niermann / CTA Rheinland Trust
7. Lenkungskreis RHEINGOLD 2030: 22.04.2026 (verschoben auf 12.05.2026)
8. Nachtrag-Vereinbarung Honorar (EUR 180.000 Ueberschreitung Fee Cap) - Treuenfels-Ostermann / HOV

<b>III. Strategische Empfehlung</b>

Die Komplexitat des Projekts und die zeitliche Dichte der Genehmigungsverfahren (Japan Q3, UK Juli, BaFin Juli) machen deutlich, dass ein SPA-Closing vor Oktober 2026 nicht realistisch ist. Wir empfehlen:

(a) SPA-Closing-Bedingungen auf Oktober 2026 als Zieldatum anpassen
(b) Long-Stop-Date auf 31.03.2027 (wie schon fuer DE-Einigungsstellen-Beschluss diskutiert)
(c) Albion Bridge formal ueber unvermeidbaren Zeitverzug informieren - fruehzeitig, um Preisrisiken zu vermeiden
(d) PSVaG-Erstattungsklage vorbereiten fuer den Fall, dass Widerspruch scheitert (LG Koeln zustaendig)

Prof. Dr. Adalbert von Sompeh-Ostermann, LL.M. (Oxford)
Fachanwalt fuer Arbeitsrecht | Honorarprofessor Universitaet zu Koeln
Treuenfels Yamamoto Rechtsanwaelte Partnerschaft mbB
Koenigsallee 92 | 40212 Duesseldorf
T: +49 211 8870-200 | F: +49 211 8870-299
a.von-sompeh-ostermann@treuenfels-yamamoto.de

<b>Unterschrift / Handzeichen:</b> [handschriftlich] AvSO
"""))
    elems.append(handw("30.04.2026 23:48 Uhr: Bericht fertig. Morgen frueh Anruf HOV. Projekt laeuft - nur Timing ist das Problem. La prudence avant tout. AvSO"))
    elems.append(PageBreak())
    return elems


def build_pdf():
    output_path = "/home/user/workspace/claude-fuer-deutsches-recht/testakten/bav-strategie-konzern-meissner-rheinwerk-ag/Testakte_Meissner_Rheinwerk_AG_bAV.pdf"
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    class PageNumCanvas(canvas.Canvas):
        def __init__(self, *args, **kwargs):
            canvas.Canvas.__init__(self, *args, **kwargs)
            self._saved_page_states = []

        def showPage(self):
            self._saved_page_states.append(dict(self.__dict__))
            self._startPage()

        def save(self):
            num_pages = len(self._saved_page_states)
            for state in self._saved_page_states:
                self.__dict__.update(state)
                self.draw_page_footer(num_pages)
                canvas.Canvas.showPage(self)
            canvas.Canvas.save(self)

        def draw_page_footer(self, page_count):
            self.saveState()
            self.setFont("Helvetica", 7)
            self.setFillColor(colors.Color(0.5, 0.5, 0.5))
            page_num = self._pageNumber
            footer_text = f"TY-2026-RHEINGOLD-001 &#183; Meissner Rheinwerk AG bAV &#183; VERTRAULICH &#183; Seite {page_num} von {page_count}"
            self.drawCentredString(A4[0]/2, 20, footer_text)
            self.setFont("Helvetica-Bold", 7)
            self.setFillColor(DARK_BLUE)
            self.drawString(30, 20, "TY")
            self.setFont("Helvetica", 7)
            self.setFillColor(colors.Color(0.5, 0.5, 0.5))
            self.drawRightString(A4[0]-30, 20, "Stand: 30.04.2026")
            self.restoreState()

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=65,
        rightMargin=55,
        topMargin=62,
        bottomMargin=52,
        title="Testakte Meissner Rheinwerk AG bAV — Projekt RHEINGOLD 2030",
        author="Treuenfels Yamamoto Rechtsanwälte Partnerschaft mbB",
        subject="TY-2026-RHEINGOLD-001 — bAV-Grossmandat MDAX-Konzern",
    )

    print("Building PDF sections...")
    all_elements = []

    sections = [
        ("01 Aktendeckel", build_cover),
        ("02 Inhaltsverzeichnis", build_toc),
        ("03 Engagement Letter", build_engagement_letter),
        ("04 Conflict Check Memo", build_conflict_check),
        ("05 Prozessvollmacht", build_poa),
        ("06 Project Charter RHEINGOLD 2030", build_project_charter),
        ("07 Status-Memo Pensionsverbindlichkeiten DE", build_status_memo_pension),
        ("08 Versorgungsordnung-Inventory", build_vo_inventory),
        ("09 Drei-Stufen-Theorie-Gutachten", build_drei_stufen_gutachten),
        ("09b Gutachten-Supplement (Rechtfertigungsebene)", build_gutachten_supplement),
        ("10 CTA-Treuhandvertrag-Entwurf", build_cta_treuhand),
        ("11 Pension Buyout Term Sheet", build_buyout_term_sheet),
        ("12 PSV-Schriftsatzkette", build_psv_schriftsatzkette),
        ("12b PSVaG-Supplement (Widerspruchsschreiben)", build_psv_supplement),
        ("13 Einigungsstellen-Akte", build_einigungsstelle),
        ("13b Einigungsstellen-Protokolle 2+3", build_einigungsstelle_supplement),
        ("14 Sozialplan-Entwurf", build_sozialplan),
        ("15 Kyoto-Modul", build_kyoto_module),
        ("15b Kyoto-Supplement (Tokyo Court + Glossar)", build_kyoto_supplement),
        ("16 US-Modul", build_us_module),
        ("16b US-Supplement (ERISA/PBGC/401k Detail)", build_erp_supplement),
        ("17 UK-Modul", build_uk_module),
        ("18 M&A-Pension-Annex", build_ma_annex),
        ("19 E-Mail-Kette", build_email_chain),
        ("20 Handschriftliche Notizen", build_handwritten_notes),
        ("20b Pension Governance Memo", build_governance_memo),
        ("07b IAS-19-Tiefenanalyse", build_ias19_deep_dive),
        ("10b CTA-Supplement (Vertragsklauseln)", build_cta_supplement),
        ("14b Sozialplan-Supplement (Berechnungen)", build_sozialplan_supplement),
        ("17b UK-Supplement (Section 75 Detail)", build_uk_supplement),
        ("BaFin-Akte Pensionsfonds", build_bafin_memo),
        ("Fristen und Risikomatrix", build_rechtsbehelfsbelehrung),
        ("Versorgungsrechtliche Grundlagen + Rechtsprechung", build_versorgungsrecht_grundlagen),
        ("Mandatsstatus-Bericht Schlussdokument", build_schlussdokument),
        ("21 Stundenaufstellung", build_timesheet),
        ("22+23 Aktenrand-Notizen + Anlagenverzeichnis", build_annexes_index),
    ]

    for name, func in sections:
        print(f"  -> {name}...")
        try:
            elems = func()
            all_elements.extend(elems)
        except Exception as e:
            print(f"    ERROR in {name}: {e}")
            import traceback
            traceback.print_exc()

    print("Building PDF document...")
    doc.build(all_elements, canvasmaker=PageNumCanvas)
    print(f"PDF saved to: {output_path}")
    return output_path


if __name__ == "__main__":
    path = build_pdf()
    try:
        from pypdf import PdfReader
        r = PdfReader(path)
        pages = len(r.pages)
        print(f"\n=== VALIDATION ===")
        print(f"Output: {path}")
        print(f"Pages:  {pages}")
        import os
        print(f"Size:   {os.path.getsize(path):,} bytes")
        if pages >= 90:
            print(f"STATUS: OK — Ziel (>=90 Seiten) erreicht")
        else:
            print(f"STATUS: WARN — nur {pages} Seiten (Ziel: >=90)")
    except Exception as e:
        print(f"Validation: {e}")






