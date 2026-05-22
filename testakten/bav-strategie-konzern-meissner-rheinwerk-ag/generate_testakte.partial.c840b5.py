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
S_NORMAL     = make_style("TY_Normal",      fontName="Helvetica",       fontSize=9.5,  leading=14,   spaceAfter=4,  leftIndent=0)
S_BODY       = make_style("TY_Body",        fontName="Times-Roman",     fontSize=9.5,  leading=14.5, spaceAfter=5,  alignment=TA_JUSTIFY)
S_BODY_SM    = make_style("TY_Body_SM",     fontName="Times-Roman",     fontSize=8.5,  leading=13,   spaceAfter=3,  alignment=TA_JUSTIFY)
S_H1         = make_style("TY_H1",          fontName="Helvetica-Bold",  fontSize=14,   leading=18,   spaceBefore=12,spaceAfter=8,  textColor=DARK_BLUE)
S_H2         = make_style("TY_H2",          fontName="Helvetica-Bold",  fontSize=11,   leading=15,   spaceBefore=10,spaceAfter=6,  textColor=DARK_BLUE)
S_H3         = make_style("TY_H3",          fontName="Helvetica-Bold",  fontSize=10,   leading=14,   spaceBefore=7, spaceAfter=4,  textColor=MID_BLUE)
S_H4         = make_style("TY_H4",          fontName="Helvetica-BoldOblique", fontSize=9.5, leading=13, spaceBefore=5, spaceAfter=3, textColor=DARK_BLUE)
S_CENTER     = make_style("TY_Center",      fontName="Helvetica",       fontSize=9.5,  leading=14,   alignment=TA_CENTER)
S_CENTER_B   = make_style("TY_CenterB",     fontName="Helvetica-Bold",  fontSize=10,   leading=15,   alignment=TA_CENTER)
S_TITLE_BIG  = make_style("TY_TitleBig",    fontName="Helvetica-Bold",  fontSize=22,   leading=28,   alignment=TA_CENTER, textColor=DARK_BLUE)
S_TITLE_MED  = make_style("TY_TitleMed",    fontName="Helvetica-Bold",  fontSize=14,   leading=19,   alignment=TA_CENTER, textColor=DARK_BLUE)
S_TITLE_GOLD = make_style("TY_TitleGold",   fontName="Helvetica-Bold",  fontSize=12,   leading=17,   alignment=TA_CENTER, textColor=RHEIN_GOLD)
S_HANDW      = make_style("TY_Handw",       fontName="Times-Italic",    fontSize=9,    leading=15,   leftIndent=10, textColor=HANDW_RED, spaceAfter=4)
S_HANDW_BLK  = make_style("TY_HandwBlk",   fontName="Times-Italic",    fontSize=9,    leading=15,   leftIndent=10, textColor=black, spaceAfter=4)
S_FAX        = make_style("TY_Fax",         fontName="Courier",         fontSize=8.5,  leading=12,   spaceAfter=2,  backColor=FAX_GRAY)
S_FAX_HDR    = make_style("TY_FaxHdr",      fontName="Courier-Bold",    fontSize=8.5,  leading=12,   backColor=FAX_GRAY)
S_TOC_ENTRY  = make_style("TY_TOC",         fontName="Times-Roman",     fontSize=9,    leading=13,   leftIndent=5,  spaceAfter=2)
S_TOC_CAT    = make_style("TY_TOCCAT",      fontName="Helvetica-Bold",  fontSize=9.5,  leading=14,   spaceBefore=6, spaceAfter=2, textColor=DARK_BLUE)
S_FOOTER     = make_style("TY_Footer",      fontName="Helvetica",       fontSize=7.5,  leading=10,   textColor=grey, alignment=TA_CENTER)
S_MONO       = make_style("TY_Mono",        fontName="Courier",         fontSize=8.5,  leading=12)
S_BULLET     = make_style("TY_Bullet",      fontName="Times-Roman",     fontSize=9.5,  leading=14,   leftIndent=15, bulletIndent=5, spaceAfter=3)
S_INDENT     = make_style("TY_Indent",      fontName="Times-Roman",     fontSize=9.5,  leading=14,   leftIndent=20, spaceAfter=4)
S_JP_DE      = make_style("TY_JP_DE",       fontName="Helvetica",       fontSize=8.5,  leading=13,   spaceAfter=3)
S_WARN       = make_style("TY_Warn",        fontName="Helvetica-Bold",  fontSize=9,    leading=13,   textColor=HANDW_RED, spaceAfter=3)
S_TABLE_HDR  = make_style("TY_TblHdr",      fontName="Helvetica-Bold",  fontSize=8.5,  leading=11,   textColor=white, alignment=TA_CENTER)
S_TABLE_CELL = make_style("TY_TblCell",     fontName="Helvetica",       fontSize=8.5,  leading=11,   alignment=TA_LEFT)
S_TABLE_R    = make_style("TY_TblCellR",    fontName="Helvetica",       fontSize=8.5,  leading=11,   alignment=TA_RIGHT)
S_SMALL_GRAY = make_style("TY_SmGray",      fontName="Helvetica",       fontSize=7.5,  leading=10,   textColor=grey)
S_KURSIV     = make_style("TY_Kursiv",      fontName="Times-Italic",    fontSize=9.5,  leading=14.5, spaceAfter=5, alignment=TA_JUSTIFY)
S_LATIN      = make_style("TY_Latin",       fontName="Times-Italic",    fontSize=8.5,  leading=12,   textColor=HexColor("#444444"), spaceAfter=2)

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
    elems.append(Paragraph("Königsallee 92 · 40212 Düsseldorf · Büro Kyoto: Gion-Higashi, Shijō-dōri, 605-0073", S_CENTER))
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
        ["Federführung:", "Prof. Dr. Adalbert von Neufeld-Sompeh, LL.M. (Oxford)"],
        ["", "Fachanwalt f. Arbeitsrecht · Honorarprof. Univ. Köln"],
        ["Co-Partner:", "Dr. Dr. Hartwig Treuenfels-Ostermann (Senior Partner)"],
        ["Kyoto:", "Yuki Yamamoto-Brennecke, bengoshi-Tokyo / RAin Düsseldorf"],
        ["VERTRAULICHKEIT:", "§ 203 StGB · Anwaltliches Beratungsgeheimnis"],
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
    elems += section_header("INHALTSVERZEICHNIS", "Projekt RHEINGOLD 2030 · TY-2026-RHEINGOLD-001")
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
            ("B-3", "Drei-Stufen-Theorie-Gutachten (Prof. von Neufeld-Sompeh, 14 Seiten)", "43-57"),
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
            ("I-2", "Handschriftliche Notizen Prof. von Neufeld-Sompeh (3 Seiten)", "190-193"),
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
    elems += section_header("ENGAGEMENT LETTER", "Treuenfels Yamamoto PartmbB an Meissner Rheinwerk AG · 14.01.2026")

    # Briefkopf
    elems.append(Paragraph("TREUENFELS YAMAMOTO Rechtsanwälte Partnerschaft mbB", S_H2))
    elems.append(Paragraph("Königsallee 92 · 40212 Düsseldorf · Tel.: +49 211 9200-100 · Fax: +49 211 9200-199", S_NORMAL))
    elems.append(Paragraph("E-Mail: rheingold-team@ty-law.de · www.ty-law.de · USt-IdNr.: DE 312 884 719", S_NORMAL))
    elems.append(hr())
    elems.append(sp(6))

    elems.append(Paragraph("Düsseldorf, den 14. Januar 2026", S_NORMAL))
    elems.append(sp(6))
    elems.append(Paragraph("<b>An:</b>", S_NORMAL))
    elems.append(Paragraph("MEISSNER RHEINWERK AG", S_BODY))
    elems.append(Paragraph("z.Hd. Herrn Dipl.-Kfm. Henrick Otterbach-Veltheim, CFO", S_BODY))
    elems.append(Paragraph("und Dr. Constanze Brindeau-Lorbach, HR-Vorstand", S_BODY))
    elems.append(Paragraph("Rheinwerkallee 1 · 40589 Düsseldorf-Reisholz", S_BODY))
    elems.append(sp(8))

    elems.append(Paragraph("<b>Betreff: Mandatsbestätigung Projekt RHEINGOLD 2030 – Konzernweite bAV-Restrukturierung</b>", S_H3))
    elems.append(Paragraph("<b>Unser Zeichen: TY-2026-RHEINGOLD-001</b>", S_NORMAL))
    elems.append(sp(8))

    body = """Sehr geehrter Herr Otterbach-Veltheim, sehr geehrte Frau Dr. Brindeau-Lorbach,

wir freuen uns, das Mandat zur rechtlichen Begleitung des Projekts RHEINGOLD 2030 zu übernehmen und bestätigen die in unserem Gespräch vom 08.01.2026 vereinbarten Konditionen hiermit schriftlich.

<b>I. Mandatsumfang</b>

Das Mandat umfasst die umfassende rechtliche Begleitung der konzernweiten Restrukturierung der betrieblichen Altersversorgung (bAV) der Meissner Rheinwerk AG und ihrer Tochtergesellschaften, insbesondere:

(1) Schließung der leistungsorientierten Versorgungssysteme (Defined Benefit, „DB") in Deutschland mit Stopp des Future Service bei Erhalt der Past-Service-Anwartschaften, unter Wahrung der Drei-Stufen-Rechtsprechung des BAG (GS 1/82, 3 AZR 392/06, 3 AZR 540/16);

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
    elems.append(Paragraph("Prof. Dr. Adalbert von Neufeld-Sompeh     Dr. Dr. Hartwig Treuenfels-Ostermann", S_NORMAL))
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
    elems += section_header("CONFLICT CHECK MEMO", "Intern · Treuenfels Yamamoto PartmbB · Streng Vertraulich")
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
    elems.append(handw("A.v.N.-S. handschriftl.: ‚Engelhart separat halten – er soll BaFin machen, NICHT Hanseatica due diligence. Klar? — A.' (Rotes Unterstreichen in Originalakte)"))
    elems.append(sp(4))
    elems.append(Paragraph("Genehmigt: Prof. Dr. Adalbert von Neufeld-Sompeh / Dr. Dr. Hartwig Treuenfels-Ostermann / 14.01.2026", S_NORMAL))
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
vertreten durch Prof. Dr. Adalbert von Neufeld-Sompeh, LL.M. (Oxford),
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
    elems += section_header("PROJECT CHARTER „RHEINGOLD 2030"", "Vorstandsbeschluss-Abschrift · Meissner Rheinwerk AG · 12.01.2026")
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
        ["Recht (externe Kanzlei)", "Prof. Dr. Adalbert von Neufeld-Sompeh", "Treuenfels Yamamoto"],
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
    elems += section_header("STATUS-MEMO: PENSIONSVERBINDLICHKEITEN DEUTSCHLAND", "Counsel Friederike Albrecht-Niermann · 20.02.2026 · IAS 19 / BetrAVG")

    elems.append(P("""<b>Verfasserin:</b> Friederike Albrecht-Niermann, Counsel (IAS 19 / Bilanzrecht)
<b>An:</b> Prof. Dr. Adalbert von Neufeld-Sompeh / Dipl.-Kfm. Henrick Otterbach-Veltheim
<b>Datum:</b> 20. Februar 2026
<b>Vertraulichkeit:</b> Anwaltlich privilegiert – mandatsbezogene Korrespondenz"""))
    elems.append(sp(4))
    elems.append(handw("Frau Brindeau-Lorbach: bitte vor Aufsichtsrat herausreden! — A.v.N.-S."))
    elems.append(sp(6))

    elems.append(Paragraph("I. Ausgangslage und IAS-19-Bewertung", S_H3))
    elems.append(P("""Die Meissner Rheinwerk AG weist im Konzernabschluss 2024 (IFRS) Pensionsrückstellungen nach IAS 19 „Employee Benefits" (revised 2011, in Kraft IFRS-Fassung 2013) von insgesamt EUR 3,2 Mrd. (DBO = Defined Benefit Obligation) aus. Der überwiegende Teil entfällt mit EUR 2,4 Mrd. auf die deutschen Versorgungszusagen.

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
    tbl2 = Table(sens, colWidths=[3.5*cm, 2.5*cm, 2.5*cm, 3.5*cm, 2cm])
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
    elems.append(handw("A.v.N.-S.: Verbindliche Auskunft anfordern! Frist für FA-Anfrage: Ende März 2026. — A."))
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
    elems += section_header("VERSORGUNGSORDNUNGS-INVENTORY", "Meissner Rheinwerk AG · Versorgungsordnungen 1973–2008 · Stand: 01.02.2026")
    elems.append(Paragraph("Erstellt: Annika Beerbohm-Sittler / Maximilian Pfaffenhausen-Quasthoff · Senior Associates · Treuenfels Yamamoto", S_SMALL_GRAY))
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

Die VO 1973 enthält in § 12 Abs. 3 eine sogenannte „BMW-ähnliche" Gesamtversorgungsobergrenze: Die Gesamtversorgung aus betrieblicher Rente + gesetzlicher Rente soll 75 % des letzten maßgeblichen Bruttogehalts nicht übersteigen. Diese Klausel wurde vom BAG für verschiedene ähnliche Systeme für teilweise unwirksam erklärt (BAG 3 AZR 304/13 zur Anrechnung gesetzlicher Rente, Urteil vom 19.05.2016); Rückabwicklungsansprüche bestehen daher für rd. 180 Rentner (K-VO-8, Risikoliste).

<b>Anpassungshistorie § 16 BetrAVG:</b> Die Meissner Rheinwerk AG hat die Anpassungsprüfung gem. § 16 BetrAVG zuletzt für 2022/2023 durchgeführt und die Renten um 3,2 % erhöht. Für 2025/2026 steht die nächste Prüfung an; bei einem Netto-Eigenkapital von EUR 1,87 Mrd. und EBITDA-Margin >12 % kann die wirtschaftliche Lage eine Nullrunde schwerlich rechtfertigen (BAG 3 AZR 304/13, Rn. 44 ff.). Empfehlung: 2,8 % Erhöhung per 01.01.2026 (K-VO-9).
"""))

    # VO 1981 Detail
    elems.append(Paragraph("VO 1981 – Gesamtversorgungszusage mit Lohnbezug (K-VO-2)", S_H3))
    elems.append(P("""Die Versorgungsordnung 1981 gewährt eine Gesamtversorgung in Höhe von 75 % des letzten Bruttogehalts (abzüglich gesetzlicher Rente und anderer Versorgungsleistungen). Sie enthält eine Gehaltsdynamik-Klausel, die Erhöhungen des versorgungsfähigen Gehalts nach einem festgelegten Tarifband (Chemie-Tarif NRW) automatisch berücksichtigt.

Besonderheit der VO 1981: Sie enthält in § 8 Abs. 2 eine sogenannte „Nachschusspflicht" des Arbeitgebers für den Fall einer Schließung des Systems. Rechtlich umstritten ist, ob diese Klausel auch bei einer Schließung mit Betriebsvereinbarung (Ablöse-BV) greift. Das OLG Düsseldorf hat in einem ähnlichen Fall entschieden, dass derartige Klauseln bei einvernehmlicher BV-Ablösung nicht anwendbar sind (OLG Düsseldorf I-6 U 223/19; nicht rechtskräftig, kein BAG-Urteil bislang). Prof. von Neufeld-Sompeh analysiert diese Konstellation im Drei-Stufen-Gutachten (Abschnitt B-3).
"""))

    # VO 1995, VO 2008
    elems.append(Paragraph("VO 1995 und VO 2008 – DC-Systeme", S_H3))
    elems.append(P("""Die VO 1995 stellt auf ein beitragsorientiertes System mit garantiertem Mindestleistungsversprechen i.S.v. § 1 Abs. 2 Nr. 2 BetrAVG (beitragsorientierte Leistungszusage, „BOLZ") um. Der Arbeitgeber garantiert den Erhalt der eingezahlten Beiträge zuzüglich einer Mindestverzinsung von 1,5 % p.a. Die VO 1995 ist konzernweit der kostenintensivste Übergangs-Baustein.

Die VO 2008 sieht ausschließlich Direktversicherungen gemäß § 1b Abs. 2 BetrAVG und § 3 Nr. 63 EStG vor (Gehaltsumwandlung bis EUR 3.504 p.a. steuerfrei; bei Aufstockung durch AG: bis EUR 7.008). Alle VO-2008-Anwärter werden durch den Future-Service-Stopp weniger stark betroffen, da das DC-System flexibel ablösbar ist.
"""))

    elems.append(Paragraph("Chemie-Nord-Versorgungstarifvertrag", S_H3))
    elems.append(P("""Der Chemie-Nord-Versorgungstarifvertrag vom 12.11.1987 (Verlängerung 2003, 2012) ist zwischen dem Arbeitgeberverband Chemie NRW e.V. und der IG BCE geschlossen. Er bindet die Meissner Rheinwerk AG unmittelbar (§§ 3, 4 TVG). Eine Schließung der durch den TV geregelten Versorgungskomponente erfordert einen Tarifvertrag (§ 17 Abs. 3 BetrAVG). Verhandlungsstand: IG-BCE hat Bereitschaft zu Gesprächen signalisiert, GBR-Vorsitzender Kreidemann lehnt Schließung grundsätzlich ab (vgl. Einigungsstellen-Akte D-1).
"""))
    elems.append(handw("Pfaffenhausen-Quasthoff: TV-Kündigung durch AGB prüfen? → Nein, § 77 Abs. 3 BetrVG Sperrwirkung! Abgestimmt mit A.v.N.-S."))

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
    elems += section_header("DREI-STUFEN-THEORIE-GUTACHTEN", "Prof. Dr. Adalbert von Neufeld-Sompeh · Treuenfels Yamamoto · 28.02.2026")
    elems.append(Paragraph("STRENG VERTRAULICH – Anwaltlich privilegiertes Rechtsgutachten – Mandatsbezogenes Schriftstück", S_WARN))
    elems.append(sp(6))

    elems.append(P("""<b>Verfasser:</b> Prof. Dr. Adalbert von Neufeld-Sompeh, LL.M. (Oxford), Fachanwalt für Arbeitsrecht, Honorarprofessor Universität zu Köln für Versorgungs- und Vergütungsrecht
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
Der „erdiente Besitzstand" ist der Kern der Zusage, der auf bereits erbrachter Arbeitsleistung beruht. Lohn-/Leistungsverhältnis ist insoweit bereits erfüllt. Ein Eingriff in erdiente Besitzstände – d.h. eine Schmälerung des bereits erdienten Teils der Versorgungsleistung – ist nach BAG GS 1/82 nur bei zwingenden Gründen zulässig; in der Praxis de facto ausgeschlossen.

<b>Stufe 2 – Eingriff in dienstzeitabhängige Zuwächse:</b>
Hierbei handelt es sich um Zuwächse, die noch nicht erdient sind, aber auf einer bereits erbrachten Leistung beruhen (z.B. Steigerungsbeträge für die bereits zurückgelegte Dienstzeit, die nach der VO noch zustehen würden). Eingriffe auf dieser Ebene erfordern „triftige Gründe" (BAG 3 AZR 392/06 vom 10.07.2007, Rn. 51: „Die Einschränkung dienstzeitabhängiger Zuwächse bedarf triftiger, sachlich-proportionaler Gründe").

<b>Stufe 3 – Eingriff in künftige, noch nicht erdiente Zuwächse (Future Service):</b>
Der Stopp des Future Service – d.h. die Schließung des Systems für künftige Dienstjahre – greift in noch nicht verdiente, nur expectative Positionen ein. Das BAG (3 AZR 540/16 vom 19.07.2016, Rn. 38 ff.) lässt hierfür „sachlich-proportionale Gründe" ausreichen, d.h. einen nachvollziehbaren, plausiblen Grund für die Systemänderung.
"""))

    elems.append(Paragraph("C. Subsumtion: Future-Service-Stopp Meissner Rheinwerk AG", S_H3))
    elems.append(P("""<b>I. Klassifikation des Eingriffs</b>

Der geplante Schritt – Stopp des Future Service ab 01.01.2027 bei Einfrierung der erdienten Anwartschaft – ist <b>ausschließlich</b> ein Eingriff der dritten Stufe. Ein Eingriff in die erdienten Besitzstände (Stufe 1) oder in die dienstzeitabhängigen Zuwächse der Vergangenheit (Stufe 2) findet nicht statt: Die bereits erdienten Anwartschaften bleiben vollständig erhalten. Es wird lediglich die Neuakkumulation ab dem Schließungsstichtag gestoppt.

<b>WICHTIG:</b> Es darf unter keinen Umständen der Versuch unternommen werden, durch die Schließungsvereinbarung auch Stufe-2-Positionen zu tangieren (z.B. durch Neuberechnung der erdienten Anwartschaft nach niedrigerem Maßstab). Das hätte eine erhebliche Verschärfung des Rechtfertigungsmaßstabs zur Folge.
"""))
    elems.append(handw("A.v.N.-S.: Brindeau: D-3-Stufen NICHT auf Future-Service ausdehnen, sonst BAG zerlegt uns. A."))

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

<b>4.</b> Die Einigungsstelle (ArbG Düsseldorf 7 BV 412/26) bietet das geeignete Verfahren zur kollektiven Einigung; dabei ist zu beachten, dass die Einigungsstelle beim Regelungstatbestand „Versorgungsordnung" Ermessensgrenzen hat (BAG 3 AZR 542/17).

<b>5.</b> Individuelle Sonderzusagen (FK-001 bis FK-047) sind gesondert zu verhandeln; hier gelten die BAG-Grundsätze zum Vertrauensschutz bei einzelvertraglichen Zusagen (BAG 3 AZR 540/16, Rn. 61 ff.).

<i>Prof. Dr. Adalbert von Neufeld-Sompeh, LL.M. (Oxford)</i>
<i>Fachanwalt für Arbeitsrecht · Honorarprofessor Universität zu Köln</i>
<i>Treuenfels Yamamoto Rechtsanwälte PartmbB · 28.02.2026</i>
"""))
    elems.append(latin("quod erat probandum – die rechtliche Zulässigkeit des Future-Service-Stopps ist damit nach geltendem BAG-Recht tragbar begründet"))
    elems.append(PageBreak())
    return elems


def build_cta_treuhand():
    """10. CTA-Treuhandvertrag-Entwurf"""
    elems = []
    elems += section_header("CTA-TREUHANDVERTRAG (ENTWURF)", "Doppeltreuhand · CTA Rheinland Trust e.V. · Stand: 15.03.2026")
    elems.append(Paragraph("ENTWURF – NOCH NICHT BEURKUNDET – ÄNDERUNGEN VORBEHALTEN", S_WARN))
    elems.append(sp(6))

    elems.append(P("""<b>DOPPELTREUHANDVERTRAG</b>

zwischen

<b>MEISSNER RHEINWERK AG</b>, Rheinwerkallee 1, 40589 Düsseldorf-Reisholz
(im Folgenden: „Versorgungsschuldner")

und

<b>CTA RHEINLAND TRUST e.V.</b>, Königsallee 199a, 40212 Düsseldorf
(im Folgenden: „Treuhänder")

— <i>nachfolgend gemeinsam „die Parteien" —</i>

<b>Präambel</b>

Die Meissner Rheinwerk AG hat gegenüber ihren aktiven und ehemaligen Arbeitnehmern sowie Rentnern (im Folgenden: „Versorgungsberechtigte") umfangreiche Versorgungszusagen nach Maßgabe der Versorgungsordnungen 1973, 1981 und des Chemie-Nord-TV abgegeben. Um die Sicherheit dieser Zusagen im Insolvenzfall zu gewährleisten und die handelsbilanziellen Pensionsrückstellungen gem. § 246 Abs. 2 Satz 2 HGB saldieren zu können (Deckungsreserven-Saldierung), errichten die Parteien hiermit einen doppelseitigen Treuhandvertrag (Contractual Trust Arrangement, „CTA").

Das CTA besteht aus zwei Treuhandverhältnissen:
(a) <b>Sicherungstreuhand:</b> Übereignung der Deckungsreserven vom Versorgungsschuldner auf den Treuhänder zum Zweck der insolvenzrechtlich abgesicherten Reservierung der Pensionsgelder (BAG 3 AZR 18/12 vom 16.07.2013); und
(b) <b>Verwaltungstreuhand:</b> Verwaltung der Deckungsreserven durch den Treuhänder im Auftrag des Versorgungsschuldners nach einem vereinbarten Anlagereglement.
"""))

    elems.append(Paragraph("§ 1 Begriffsbestimmungen", S_H3))
    elems.append(P("""„<b>Deckungsreserven</b>" bezeichnen alle Vermögenswerte, die der Versorgungsschuldner auf den Treuhänder überträgt und die zur Deckung der Pensionsverpflichtungen des Versorgungsschuldners dienen.

„<b>Versorgungsverpflichtungen</b>" sind die Verpflichtungen des Versorgungsschuldners gegenüber den Versorgungsberechtigten aus den Versorgungsordnungen 1973, 1981 und dem Chemie-Nord-TV sowie ggf. aus Einzelzusagen.

„<b>Anlagereglement</b>" ist das in Anlage 1 beigefügte Dokument, das die zulässigen Anlageklassen, Risikolimite und Liquiditätskennzahlen für die verwalteten Deckungsreserven festlegt.

„<b>Treuhandkonten</b>" sind die auf den Namen des Treuhänders geführten Konten und Depots, auf denen die Deckungsreserven gehalten werden.

„<b>Ausfall des Versorgungsschuldners</b>" liegt vor im Falle der Eröffnung des Insolvenzverfahrens über das Vermögen des Versorgungsschuldners (§ 27 InsO) oder der Ablehnung mangels Masse (§ 26 InsO).
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
    elems += section_header("PENSION BUYOUT TERM SHEET (ENTWURF)", "Meissner Rheinwerk AG / Hanseatica Lebensversicherung AG · Stand: 28.04.2026")
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
    elems += section_header("PSVaG-SCHRIFTSATZKETTE", "PSVaG Mahnschreiben · Treuenfels Yamamoto Stellungnahme · PSVaG Erwiderung")
    elems.append(sp(4))

    # PSVaG Mahnschreiben
    elems += mini_header("PSVaG – Mahnschreiben vom 22. März 2026")
    elems += fax_block([
        "Pensions-Sicherungs-Verein Versicherungsverein auf Gegenseitigkeit",
        "Postfach 10 07 07 · 50447 Köln · www.psvag.de",
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
        "Tel.: 0221 9803-222 · hfischbach-stern@psvag.de",
        "22.03.2026 · Zeichen PSV 2026-MR-00442",
    ], sender="PSVaG Köln", receiver="Meissner Rheinwerk AG", date="22.03.2026 09:12", pages="2/2")

    # Stellungnahme TY
    elems += mini_header("Treuenfels Yamamoto – Stellungnahme vom 9. April 2026")
    elems.append(P("""Treuenfels Yamamoto Rechtsanwälte PartmbB
Königsallee 92 · 40212 Düsseldorf
Tel.: +49 211 9200-100 · Fax: +49 211 9200-199

<b>Per Einschreiben mit Rückschein und Fax</b>

An:
Pensions-Sicherungs-Verein VVaG
z.Hd. Dr. Hannelore Fischbach-Stern
Postfach 10 07 07 · 50447 Köln

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

Prof. Dr. Adalbert von Neufeld-Sompeh · Treuenfels Yamamoto PartmbB
"""))
    elems.append(sp(4))

    # PSVaG Erwiderung
    elems += mini_header("PSVaG – Erwiderung vom 28. April 2026")
    elems.append(P("""Pensions-Sicherungs-Verein VVaG · Köln, 28.04.2026
Zeichen: PSV 2026-MR-00442-R

An: Treuenfels Yamamoto PartmbB, z.Hd. Prof. Dr. von Neufeld-Sompeh

Sehr geehrter Herr Professor von Neufeld-Sompeh,

wir bestätigen den Zahlungseingang vom 14.04.2026 (EUR 1.284.716,00) und danken für Ihre ausführliche Stellungnahme.

Zur Frage der CTA-Anrechnung: Wir teilen Ihre Rechtsauffassung im Grundsatz (BAG 3 AZR 18/12 ist uns bekannt). Allerdings erfordert die CTA-Anrechnung gemäß unserem Beitragsrundschreiben 2023/4 einen Nachweis in Form des vollständigen CTA-Vertrags sowie eines aktuariellen Gutachtens über die Planvermögen zum Stichtag 31.12.2025.

Wir bitten um Einreichung dieser Unterlagen bis zum 31.05.2026. Nach Prüfung werden wir ggf. eine Beitragskorrektur für 2025 vornehmen.

Mit freundlichen Grüßen
Dr. Hannelore Fischbach-Stern · PSVaG · Sachgebiet Beitragswesen
"""))
    elems.append(handw("A.v.N.-S.: Hellmrich-Vogt auffordern, Aktuargutachten bis 20.05.2026 zu liefern. Dringend! — A."))
    elems.append(PageBreak())
    return elems


def build_einigungsstelle():
    """13. Einigungsstellen-Akte"""
    elems = []
    elems += section_header("EINIGUNGSSTELLEN-AKTE", "ArbG Düsseldorf 7 BV 412/26 · Gesamtbetriebsrat vs. Meissner Rheinwerk AG")
    elems.append(sp(4))

    elems += mini_header("Antrag Gesamtbetriebsrat (Plöger Maibach Rechtsanwälte, Köln) – eingegangen 01.03.2026")
    elems.append(P("""<b>An das Arbeitsgericht Düsseldorf</b>
Kammergericht des Landes NRW · Düsseldorfer Str. 199 · 40545 Düsseldorf

<b>In dem Beschlussverfahren</b>

Antragsteller: Gesamtbetriebsrat der Meissner Rheinwerk AG
— vertreten durch Plöger Maibach Rechtsanwälte, Apostelnstr. 8–10, 50667 Köln —
— RA Dr. Wolfram Plöger-Heinekamp —

gegen

Antragsgegnerin: Meissner Rheinwerk AG, Rheinwerkallee 1, 40589 Düsseldorf-Reisholz
— vertreten durch Treuenfels Yamamoto Rechtsanwälte PartmbB, Königsallee 92, 40212 Düsseldorf —

beantragen wir:

<b>Es wird eine Einigungsstelle gemäß § 76 Abs. 2 BetrVG zum Regelungsgegenstand „Neufassung der Versorgungsordnung / Schließung des DB-Systems" eingesetzt. Als Vorsitzende wird Frau Richterin am Arbeitsgericht a.D. Dr. Hannelore Wupperhain-Stein, Düsseldorf, vorgeschlagen.</b>

<b>Begründung:</b>

Der GBR bestreitet nicht grundsätzlich das Recht der Arbeitgeberin, das DB-System zu schließen. Er fordert jedoch eine mitbestimmungsrechtlich ordnungsgemäße Durchführung nach § 87 Abs. 1 Nr. 8, 10 BetrVG. Die bisherigen Verhandlungen sind gescheitert, weil die Arbeitgeberin den Entwurf des Pensionsbuyout-Vertrages nicht offengelegt hat und die Auswirkungen auf die Versorgungsberechtigten nicht hinreichend dargestellt wurden.

GBR-Vorsitzender Lukas Kreidemann erklärt: „Die Betriebsräte werden keine Schließung unterschreiben, bevor nicht klar ist, was die Rente für jeden einzelnen Kollegen bedeutet."

RA Dr. Wolfram Plöger-Heinekamp · Plöger Maibach Rechtsanwälte · 01.03.2026
"""))
    elems.append(sp(4))

    elems += mini_header("Erwiderung Treuenfels Yamamoto – eingereicht 14.03.2026")
    elems.append(P("""Treuenfels Yamamoto Rechtsanwälte PartmbB · Düsseldorf, 14.03.2026

An das Arbeitsgericht Düsseldorf – 7. Kammer – 7 BV 412/26

<b>Erwiderung der Arbeitgeberin</b>

Die Meissner Rheinwerk AG tritt dem Antrag des GBR nicht entgegen. Sie begrüßt die Einsetzung einer Einigungsstelle, da dies dem beschleunigten Projektfortschritt dienlich ist.

Hinsichtlich der Vorsitzenden: Die Arbeitgeberin stimmt dem Vorschlag Frau Dr. Wupperhain-Stein zu. Als Beisitzer benennt die Arbeitgeberin:
1. Dr. Günther Vossenkamp-Bleeke (Rechtsanwalt, Düsseldorf, Fachmann bAV)
2. Prof. Dr. Karin Stelzmüller-Frei (HS Bochum, Arbeitsrecht)
3. Hendrik Bruns-Meterding (RA, Düsseldorf)

Wir bitten darum, die erste Sitzung auf den 12.03.2026 anzusetzen [Anm.: der Antrag war bereits beschleunigt bearbeitet worden, Termin rückwirkend eingetragen].

Prof. Dr. Adalbert von Neufeld-Sompeh · Treuenfels Yamamoto PartmbB
"""))
    elems.append(sp(4))

    elems += mini_header("Beschluss ArbG Düsseldorf – Einsetzung Einigungsstelle")
    elems.append(P("""<b>ARBEITSGERICHT DÜSSELDORF</b>
<b>Beschluss</b>
7 BV 412/26

Die Einigungsstelle für den Regelungsgegenstand „Schließung der leistungsorientierten Versorgungssysteme / Neuregelung bAV" wird eingesetzt. Den Vorsitz führt <b>Richterin am Arbeitsgericht a.D. Dr. Hannelore Wupperhain-Stein</b>. Jede Seite benennt drei Beisitzer. Die Einigungsstelle kann durch Beschluss mit Mehrheit der Stimmen entscheiden, sofern keine Einigung der Parteien erzielt wird.

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
        "TOP 2: Darstellung AG – Prof. von Neufeld-Sompeh stellt Projekt RHEINGOLD vor.",
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
— Diskussion Drei-Stufen-Theorie (Prof. von Neufeld-Sompeh erläutert GS 1/82 und 3 AZR 392/06; Dr. Plöger-Heinekamp: „Wir bestreiten den sachlichen Grund nicht grundsätzlich, aber die Datenbasis ist unvollständig")
— GBR fordert Einsicht in SPA-Verhandlungen RHEINORGANICS / Albion Bridge
— AG lehnt ab: „Vertraulich, kein Mitbestimmungsrecht bei M&A nach § 106 BetrVG Abs. 3"
— Einigung zu TOP (a): IAS-19-Gutachten wird in geschwärzter Fassung offengelegt (K-VO-7-GBR)
Nächste Sitzung: 14.04.2026
"""))
    elems.append(handw("A.v.N.-S.: Plöger sucht Streit – ignorieren, Einigungsstelle wird's richten. — A."))

    elems += mini_header("Sitzungsprotokoll Nr. 3 – 14. April 2026 (Auszug)")
    elems.append(P("""Sitzung 3 vom 14.04.2026: Partieller Kompromiss erzielt:
— Sozialplan-Grundlagen vereinbart (Wahlmodell A/B/C, vgl. D-8)
— Schließungsdatum auf 01.04.2027 vorgezogen (statt 01.01.2027) nach GBR-Wunsch
— Offene Punkte: Sonderzusagen FK-Gruppe, Anpassung § 16 BetrAVG, Buyout-Garantien
— GBR kündigt Beschwerde LAG Düsseldorf an (14 TaBV 88/26) wegen Verfahrensfragen
— Nächste Sitzung: nach LAG-Termin
Vorsitz Dr. Wupperhain-Stein: „Ich sehe Einigungspotenzial bis Sommer 2026."
"""))
    elems.append(PageBreak())
    return elems


def build_sozialplan():
    """14. Sozialplan-Entwurf"""
    elems = []
    elems += section_header("SOZIALPLAN-ENTWURF (PENSION-BESTANDTEILE)", "Meissner Rheinwerk AG / Gesamtbetriebsrat · Stand: 20.04.2026 (Verhandlungsstand)")
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
    elems += section_header("KYOTO-MODUL: MIGRATION JAPANISCHES DB-SYSTEM → DC", "Memo Yuki Yamamoto-Brennecke · Treuenfels Yamamoto Kyoto · 15.03.2026")

    # Kyoto letterhead
    elems.append(sp(4))
    logo_kyoto = """
    ┌─────────────────────────────────────────────────────────────────┐
    │   トロイエンフェルス・ヤマモト法律事務所                           │
    │   TREUENFELS YAMAMOTO HORITSU JIMUSHO                          │
    │   Gion-Higashi, Shijō-dōri-Ostseite · 605-0073 Kyoto, Japan   │
    │   Tel.: +81-75-XXX-XXXX · Fax: +81-75-XXX-XXXX               │
    │   yuki.yamamoto@ty-law.jp · www.ty-law.de/kyoto               │
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
        "<b>An:</b> Prof. Dr. Adalbert von Neufeld-Sompeh,\nDr. Constanze Brindeau-Lorbach",
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
        '„Treuenfels-sensei e: kakutei-kyuufu-saraba, DC-koso michi nari. — Y. Yamamoto"',
        make_style("jp_note", fontName="Times-Italic", fontSize=11, leading=16, textColor=HANDW_RED, alignment=TA_CENTER)
    ))
    elems.append(Paragraph(
        "(Übersetzung: „An Herrn Treuenfels: Lebewohl der Leistungszusage – der DC-Weg ist der einzig richtige.")",
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
    elems += section_header("US-MODUL: ERISA / PBGC / 401(k)", "Holcombe Pratchett & Lieberman LLP (Boston) · File No. HPL-2026-MRW-0007")
    elems.append(sp(4))

    # US letterhead
    us_header = """
    ╔══════════════════════════════════════════════════════════════════╗
    ║  HOLCOMBE PRATCHETT & LIEBERMAN LLP                             ║
    ║  Federal Street 200 · Boston, MA 02110                         ║
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

TO:     Prof. Dr. Adalbert von Neufeld-Sompeh, Treuenfels Yamamoto (Lead Counsel)
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

<i>Matthew B. Holcombe III · Rebecca J. Lieberman-Strauss</i>
<i>Holcombe Pratchett & Lieberman LLP · Boston, MA · March 22, 2026</i>
"""))
    elems.append(PageBreak())
    return elems


def build_uk_module():
    """17. UK-Modul"""
    elems = []
    elems += section_header("UK-MODUL: SECTION 75 / TPR CLEARANCE", "Pemberton Hawkesworth Solicitors (London) · Meissner Rhine Industries Ltd.")
    elems.append(sp(4))

    uk_header = """
    ┌─────────────────────────────────────────────────────────────┐
    │  PEMBERTON HAWKESWORTH SOLICITORS                           │
    │  120 Aldersgate Street · London EC1A 4JQ                   │
    │  Tel.: +44 20 7XXX XXXX · DX 462 London/City              │
    │  Pensions & Employment Practice                            │
    │  Our ref.: PHW/2026/MRI/P-001                             │
    └─────────────────────────────────────────────────────────────┘
    """
    elems.append(Paragraph("<pre>" + uk_header + "</pre>", S_MONO))
    elems.append(sp(6))

    elems.append(P("""<b>PRIVILEGED AND CONFIDENTIAL</b>

<b>MEMORANDUM</b>

TO:     Prof. Dr. Adalbert von Neufeld-Sompeh, Treuenfels Yamamoto
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
    elems.append(Paragraph("Pemberton Hawkesworth Solicitors · London, 20 March 2026", S_SMALL_GRAY))
    elems.append(PageBreak())
    return elems


def build_ma_annex():
    """18. M&A-Pension-Annex"""
    elems = []
    elems += section_header("M&A-PENSION-ANNEX ZUM SPA", "Carve-out RHEINORGANICS · Albion Bridge Capital Partners LLP · Stand: 15.04.2026")
    elems.append(Paragraph("STRENG VERTRAULICH – TRANSAKTIONSDOKUMENT – ENTWURF", S_WARN))
    elems.append(sp(6))

    elems.append(P("""<b>PENSION SCHEDULE</b>
(als Anlage zu Schedule 12 des Share Purchase Agreement zwischen der Meissner Rheinwerk AG als Verkäuferin und ABCP RHEINORGANICS BIDCO LTD. (Albion Bridge Capital Partners LLP-Tochter) als Käuferin)

<b>Hintergrund:</b>
Die Pension-Verpflichtungen der Sparte RHEINORGANICS sind integraler Bestandteil der SPA-Verhandlungen und wurden von Albion Bridge als potenzielle Dealbreaker identifiziert. Folgende Jurisdiktionen sind betroffen: DE, UK, US (MSC-US), JP.

<b>Section 12.1 – Definitionen</b>

„<b>Pension Liabilities</b>" bezeichnet alle Leistungsverpflichtungen (Defined Benefit und Defined Contribution) der Zielgruppe gegenüber aktiven und ehemaligen Mitarbeitern der Sparte RHEINORGANICS, soweit diese Verpflichtungen auf Dienstzeiten vor dem Closing beruhen.

„<b>Pre-Closing Pension Deficit</b>" ist der Unterschiedsbetrag zwischen der DBO der Pension Liabilities und dem Marktwert der zugeordneten Plan Assets, jeweils bezogen auf den Closing-Stichtag, berechnet nach IFRS IAS 19.

„<b>Carve-out Pension Adjustment</b>" ist eine preisanpassende Zahlung, die sich aus der Differenz zwischen dem vorläufigen Pre-Closing Pension Deficit (geschätzt EUR 84 Mio. für RHEINORGANICS) und dem tatsächlichen Pre-Closing Pension Deficit (gemäß Completion Accounts) ergibt.

<b>Section 12.2 – Pre-Closing Obligations (Verkäuferin)</b>

Die Verkäuferin verpflichtet sich, bis zum Closing:
(a) Die RHEINORGANICS-Anwärter aus dem deutschen DB-System (VO 1973, VO 1981) herauszulösen und in einen separaten Pensionsfonds zu überführen oder eine individual-vertragliche Übertragungsvereinbarung zu treffen;
(b) Den PSVaG über die Transaktion zu informieren (§ 14 Abs. 1 Nr. 9 BetrAVG, Pflichtmitteilung);
(c) Keine neuen DB-Zusagen an RHEINORGANICS-Mitarbeiter zu erteilen;
(d) Eine aktuarielle Bewertung des Pre-Closing Pension Deficit durch Hellmrich-Vogt (für DE/JP) und Green & Sandoval LLC (für US) spätestens 15 Tage vor Closing zu erstellen.
"""))

    elems.append(Paragraph("Section 12