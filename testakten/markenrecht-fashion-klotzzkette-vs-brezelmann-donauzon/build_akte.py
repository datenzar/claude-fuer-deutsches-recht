#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate the fictional Testakte:
  klôtzzkètté SA ./. Brezelmann Discount KG & Donauzon Marketplace GmbH u.a.
Trademark mega-case file. Target: 130-160 pages, deliberately fragmentary.
"""
import os, sys, random, math, textwrap, datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm, mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak,
    Table, TableStyle, Image, KeepTogether, Flowable, NextPageTemplate,
    XPreformatted, Preformatted, HRFlowable
)
from reportlab.pdfgen import canvas

random.seed(1923)  # year klôtzzkètté was founded

# ---------------------------------------------------------------------
# Font registration
# ---------------------------------------------------------------------
FONT_HAND   = "Helvetica-Oblique"  # fallback
FONT_HAND2  = "Times-Italic"
try:
    pdfmetrics.registerFont(TTFont("Caveat", "/tmp/akte_fonts/Caveat-Regular.ttf"))
    FONT_HAND = "Caveat"
except Exception as e:
    print("Caveat load failed:", e)
try:
    pdfmetrics.registerFont(TTFont("IndieFlower", "/tmp/akte_fonts/IndieFlower-Regular.ttf"))
    FONT_HAND2 = "IndieFlower"
except Exception as e:
    print("IndieFlower load failed:", e)
try:
    pdfmetrics.registerFont(TTFont("ComicSans", "/usr/share/fonts/truetype/msttcorefonts/Comic_Sans_MS.ttf"))
    FONT_HAND3 = "ComicSans"
except Exception:
    FONT_HAND3 = "Helvetica-Oblique"

# ---------------------------------------------------------------------
# Global Page Setup with Aktenpaginierung
# ---------------------------------------------------------------------
PAGE_W, PAGE_H = A4
MARGIN = 2.0 * cm

class BlattCounter:
    n = 0
BC = BlattCounter()

def make_page_callback(label_provider=None):
    def cb(canv, doc):
        BC.n += 1
        canv.saveState()
        # Hole-punch marks left margin (decorative)
        canv.setStrokeColor(colors.HexColor("#bbbbbb"))
        canv.setLineWidth(0.4)
        for y in [PAGE_H*0.18, PAGE_H*0.50, PAGE_H*0.82]:
            canv.circle(0.8*cm, y, 0.18*cm, stroke=1, fill=0)
        # Blatt number bottom right
        canv.setFont("Helvetica", 8)
        canv.setFillColor(colors.HexColor("#444444"))
        canv.drawRightString(PAGE_W - 1.2*cm, 0.8*cm, f"Blatt {BC.n}")
        # Mini-stamp top right occasionally
        if BC.n % 17 == 3:
            canv.saveState()
            canv.translate(PAGE_W - 3*cm, PAGE_H - 1.6*cm)
            canv.rotate(-8)
            canv.setStrokeColor(colors.HexColor("#8a1a1a"))
            canv.setFillColor(colors.HexColor("#8a1a1a"))
            canv.setLineWidth(0.7)
            canv.rect(-0.1*cm, -0.3*cm, 2.4*cm, 0.9*cm, stroke=1, fill=0)
            canv.setFont("Helvetica-Bold", 7)
            canv.drawCentredString(1.1*cm, 0.0*cm, "EINGANG")
            canv.setFont("Helvetica", 6)
            canv.drawCentredString(1.1*cm, -0.22*cm, f"22.05.2026")
            canv.restoreState()
        # Tiny file-spine label left bottom
        canv.setFont("Helvetica-Oblique", 6)
        canv.setFillColor(colors.HexColor("#777777"))
        canv.drawString(1.4*cm, 0.8*cm, "Az. 2-03 O 412/26  •  WBF-2026-KK-0014  •  klôtzzkètté ./. Brezelmann u.a.")
        canv.restoreState()
    return cb

# ---------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------
styles = getSampleStyleSheet()

S_NORMAL = ParagraphStyle("body", parent=styles["Normal"],
    fontName="Times-Roman", fontSize=10.5, leading=14, alignment=TA_JUSTIFY)
S_NORMAL_LEFT = ParagraphStyle("bodyL", parent=S_NORMAL, alignment=TA_LEFT)
S_SMALL = ParagraphStyle("small", parent=S_NORMAL, fontSize=8.5, leading=11)
S_TINY  = ParagraphStyle("tiny", parent=S_NORMAL, fontSize=7.5, leading=9.5)
S_H1 = ParagraphStyle("h1", parent=styles["Heading1"],
    fontName="Times-Bold", fontSize=15, leading=18, spaceAfter=10, alignment=TA_LEFT)
S_H2 = ParagraphStyle("h2", parent=styles["Heading2"],
    fontName="Times-Bold", fontSize=12, leading=15, spaceBefore=8, spaceAfter=4)
S_H3 = ParagraphStyle("h3", parent=styles["Heading3"],
    fontName="Times-Bold", fontSize=10.5, leading=13, spaceBefore=6, spaceAfter=2)
S_CENTER = ParagraphStyle("center", parent=S_NORMAL, alignment=TA_CENTER)
S_RIGHT  = ParagraphStyle("right", parent=S_NORMAL, alignment=TA_RIGHT)
S_ITAL   = ParagraphStyle("it", parent=S_NORMAL, fontName="Times-Italic")
S_MONO   = ParagraphStyle("mono", parent=S_NORMAL, fontName="Courier", fontSize=9, leading=11.5)
S_MONO_SMALL = ParagraphStyle("monos", parent=S_MONO, fontSize=8, leading=10)
S_HAND   = ParagraphStyle("hand", parent=S_NORMAL, fontName=FONT_HAND, fontSize=15, leading=19, textColor=colors.HexColor("#1e3a6e"))
S_HAND2  = ParagraphStyle("hand2", parent=S_NORMAL, fontName=FONT_HAND2, fontSize=14, leading=18, textColor=colors.HexColor("#2c1d4f"))
S_HAND3  = ParagraphStyle("hand3", parent=S_NORMAL, fontName=FONT_HAND3, fontSize=11.5, leading=15, textColor=colors.HexColor("#33334d"))
S_STAMP  = ParagraphStyle("stamp", parent=S_NORMAL, fontName="Helvetica-Bold", fontSize=11, textColor=colors.HexColor("#8a1a1a"))
S_FAX    = ParagraphStyle("fax", parent=S_MONO, fontSize=8.5, leading=11)
S_QUOTE  = ParagraphStyle("quote", parent=S_NORMAL, leftIndent=24, rightIndent=24, fontName="Times-Italic", fontSize=10, leading=13)
S_FOOT   = ParagraphStyle("foot", parent=S_NORMAL, fontSize=7.5, leading=9.5, fontName="Times-Italic", textColor=colors.HexColor("#444444"))

# ---------------------------------------------------------------------
# Custom Flowables
# ---------------------------------------------------------------------
class HLine(Flowable):
    def __init__(self, w=None, color=colors.black, thickness=0.6):
        super().__init__()
        self.w = w; self.color = color; self.thickness = thickness
    def wrap(self, aw, ah):
        self.width = self.w or aw
        return (self.width, self.thickness+2)
    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 1, self.width, 1)

class StampBox(Flowable):
    def __init__(self, text, angle=-10, color=colors.HexColor("#8a1a1a"), w=5.0*cm, h=2.2*cm):
        super().__init__()
        self.text = text; self.angle = angle; self.color = color
        self.w = w; self.h = h
    def wrap(self, aw, ah):
        return (self.w + 2*cm, self.h + 0.4*cm)
    def draw(self):
        c = self.canv
        c.saveState()
        c.translate(1*cm, 0.2*cm)
        c.rotate(self.angle)
        c.setStrokeColor(self.color); c.setFillColor(self.color)
        c.setLineWidth(1.2)
        c.roundRect(0, 0, self.w, self.h, 0.2*cm, stroke=1, fill=0)
        c.setFont("Helvetica-Bold", 9)
        lines = self.text.split("\n")
        for i, line in enumerate(lines):
            c.drawCentredString(self.w/2, self.h - 0.5*cm - i*0.42*cm, line)
        c.restoreState()

class HandNote(Flowable):
    """A handwritten-look note in a slightly rotated box, ruled paper feel."""
    def __init__(self, text, font=FONT_HAND, size=15, color=colors.HexColor("#1e3a6e"),
                 angle=0, w=16*cm, padding=0.4*cm, ruled=True, paper=colors.HexColor("#fffdf3")):
        super().__init__()
        self.text = text; self.font = font; self.size = size; self.color = color
        self.angle = angle; self.w = w; self.padding = padding
        self.ruled = ruled; self.paper = paper
    def wrap(self, aw, ah):
        # compute approximate height
        lines = self.text.split("\n")
        line_h = self.size * 1.3
        h = max(2.5*cm, line_h * len(lines) + 2*self.padding)
        self.h = h
        return (aw, h + 0.4*cm)
    def draw(self):
        c = self.canv
        c.saveState()
        if self.angle:
            c.translate(self.w/2, self.h/2)
            c.rotate(self.angle)
            c.translate(-self.w/2, -self.h/2)
        # paper
        c.setFillColor(self.paper); c.setStrokeColor(colors.HexColor("#d5cba0"))
        c.setLineWidth(0.3)
        c.rect(0, 0, self.w, self.h, stroke=1, fill=1)
        # ruled lines
        if self.ruled:
            c.setStrokeColor(colors.HexColor("#cfd7e3"))
            c.setLineWidth(0.3)
            line_h = self.size * 1.3
            y = self.h - self.padding - self.size
            while y > self.padding:
                c.line(self.padding, y - 2, self.w - self.padding, y - 2)
                y -= line_h
        # text
        c.setFont(self.font, self.size)
        c.setFillColor(self.color)
        line_h = self.size * 1.3
        y = self.h - self.padding - self.size + 2
        for line in self.text.split("\n"):
            c.drawString(self.padding + 2, y, line)
            y -= line_h
        c.restoreState()

class FaxHeader(Flowable):
    def __init__(self, from_no, to_no, date, pages, subject, sender, recipient):
        super().__init__()
        self.from_no=from_no; self.to_no=to_no; self.date=date
        self.pages=pages; self.subject=subject
        self.sender=sender; self.recipient=recipient
    def wrap(self, aw, ah):
        return (aw, 3.6*cm)
    def draw(self):
        c = self.canv
        w = 17*cm
        c.saveState()
        # banner
        c.setFillColor(colors.HexColor("#222222"))
        c.rect(0, 2.8*cm, w, 0.8*cm, stroke=0, fill=1)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 14)
        c.drawString(0.3*cm, 3.0*cm, "F A X   T R A N S M I S S I O N")
        c.setFont("Helvetica-Oblique", 8)
        c.drawRightString(w-0.3*cm, 3.0*cm, "*** thermal printer output ***")
        # body grid
        c.setStrokeColor(colors.HexColor("#666666")); c.setLineWidth(0.4)
        c.rect(0, 0, w, 2.8*cm, stroke=1, fill=0)
        c.line(0, 1.4*cm, w, 1.4*cm)
        c.line(w/2, 0, w/2, 2.8*cm)
        c.setFont("Courier-Bold", 8)
        c.drawString(0.15*cm, 2.55*cm, "FROM:")
        c.drawString(w/2 + 0.15*cm, 2.55*cm, "TO:")
        c.drawString(0.15*cm, 1.15*cm, "DATE / TIME:")
        c.drawString(w/2 + 0.15*cm, 1.15*cm, "RE / PAGES:")
        c.setFont("Courier", 8)
        c.drawString(0.15*cm, 2.25*cm, self.sender[:48])
        c.drawString(0.15*cm, 1.95*cm, f"Fax: {self.from_no}")
        c.drawString(w/2 + 0.15*cm, 2.25*cm, self.recipient[:48])
        c.drawString(w/2 + 0.15*cm, 1.95*cm, f"Fax: {self.to_no}")
        c.drawString(0.15*cm, 0.85*cm, self.date)
        c.drawString(w/2 + 0.15*cm, 0.85*cm, f"Pages: {self.pages}")
        c.drawString(0.15*cm, 0.55*cm, f"Subject: {self.subject[:55]}")
        c.restoreState()

class Briefkopf(Flowable):
    def __init__(self, kanzlei_block, recipient_block, datum, az):
        super().__init__()
        self.kanzlei_block=kanzlei_block; self.recipient_block=recipient_block
        self.datum=datum; self.az=az
    def wrap(self, aw, ah):
        return (aw, 5.2*cm)
    def draw(self):
        c = self.canv
        c.saveState()
        # Letterhead band
        c.setFillColor(colors.HexColor("#1c2e4a"))
        c.rect(0, 4.4*cm, 17*cm, 0.05*cm, stroke=0, fill=1)
        c.setFillColor(colors.HexColor("#1c2e4a"))
        c.setFont("Helvetica-Bold", 14)
        c.drawString(0, 4.7*cm, "STEINACKER  LICHTENBERG  &  PARTNERS")
        c.setFont("Helvetica", 8)
        c.setFillColor(colors.HexColor("#444444"))
        c.drawString(0, 4.42*cm, "Intellectual Property Boutique · Maximiliansplatz 19 · 80333 München · Tel +49 89 21 03 96-0 · Fax -99")
        # left column kanzlei addr
        c.setFont("Helvetica", 7)
        for i, line in enumerate(self.kanzlei_block.split("\n")):
            c.drawString(11.5*cm, 4.1*cm - i*0.28*cm, line)
        # recipient
        c.setFont("Helvetica", 9)
        for i, line in enumerate(self.recipient_block.split("\n")):
            c.drawString(0, 3.4*cm - i*0.36*cm, line)
        # datum & az
        c.setFont("Helvetica", 9)
        c.drawRightString(17*cm, 1.0*cm, f"München, {self.datum}")
        c.setFont("Helvetica-Bold", 9)
        c.drawRightString(17*cm, 0.6*cm, f"Az.: {self.az}")
        # rule
        c.setStrokeColor(colors.HexColor("#1c2e4a")); c.setLineWidth(0.4)
        c.line(0, 0.2*cm, 17*cm, 0.2*cm)
        c.restoreState()

class WBFLetterhead(Flowable):
    """US-style letterhead for Whitman Brennan Forsythe LLP"""
    def __init__(self, recipient, date, file_no, re_line):
        super().__init__()
        self.recipient=recipient; self.date=date; self.file_no=file_no; self.re_line=re_line
    def wrap(self, aw, ah):
        return (aw, 6.2*cm)
    def draw(self):
        c = self.canv
        c.saveState()
        # Centered serif letterhead
        c.setFillColor(colors.HexColor("#3a2c1a"))
        c.setFont("Times-Bold", 18)
        c.drawCentredString(8.5*cm, 5.6*cm, "WHITMAN  BRENNAN  FORSYTHE  LLP")
        c.setFont("Times-Italic", 9)
        c.setFillColor(colors.HexColor("#5b4a2e"))
        c.drawCentredString(8.5*cm, 5.2*cm, "Attorneys & Counselors at Law  —  Established 1908")
        c.setStrokeColor(colors.HexColor("#a08d5f")); c.setLineWidth(0.6)
        c.line(2*cm, 5.0*cm, 15*cm, 5.0*cm)
        c.setFillColor(colors.HexColor("#333333"))
        c.setFont("Times-Roman", 8.5)
        c.drawCentredString(8.5*cm, 4.7*cm,
            "1290 Avenue of the Americas, 41st Floor  ·  New York, NY 10104  ·  T (212) 555-0188  ·  F (212) 555-0190")
        c.drawCentredString(8.5*cm, 4.45*cm,
            "Offices: New York · Washington, D.C. · London · Tokyo · Grand Cayman")
        # recipient block
        c.setFont("Times-Roman", 10)
        c.drawString(0, 3.7*cm, self.date)
        for i, line in enumerate(self.recipient.split("\n")):
            c.drawString(0, 3.0*cm - i*0.4*cm, line)
        # File no
        c.setFont("Times-Bold", 9.5)
        c.drawRightString(17*cm, 3.7*cm, f"File No.: {self.file_no}")
        # Re line
        c.setFont("Times-Bold", 10)
        c.drawString(0, 0.5*cm, f"Re:  {self.re_line}")
        c.setStrokeColor(colors.HexColor("#a08d5f")); c.setLineWidth(0.3)
        c.line(0, 0.2*cm, 17*cm, 0.2*cm)
        c.restoreState()

class ASCIIBox(Flowable):
    """Render monospace ASCII art with a thin box around it."""
    def __init__(self, text, font="Courier-Bold", size=8.5, color=colors.HexColor("#222244"),
                 padding=0.25*cm, w=None, caption=None):
        super().__init__()
        self.text=text; self.font=font; self.size=size; self.color=color
        self.padding=padding; self.w=w; self.caption=caption
    def wrap(self, aw, ah):
        self.width = self.w or (aw - 0.5*cm)
        lines = self.text.split("\n")
        line_h = self.size * 1.05
        h = line_h * len(lines) + 2*self.padding
        if self.caption: h += 0.5*cm
        self.h = h
        return (self.width, h)
    def draw(self):
        c = self.canv
        c.saveState()
        c.setStrokeColor(colors.HexColor("#999999")); c.setLineWidth(0.3)
        c.rect(0, 0, self.width, self.h - (0.5*cm if self.caption else 0), stroke=1, fill=0)
        c.setFont(self.font, self.size); c.setFillColor(self.color)
        line_h = self.size * 1.05
        y_top = (self.h - (0.5*cm if self.caption else 0)) - self.padding - self.size + 2
        for i, line in enumerate(self.text.split("\n")):
            c.drawString(self.padding + 2, y_top - i*line_h, line)
        if self.caption:
            c.setFont("Times-Italic", 7.5); c.setFillColor(colors.HexColor("#555555"))
            c.drawCentredString(self.width/2, self.h - 0.5*cm + 4, self.caption)
        c.restoreState()


# ---------------------------------------------------------------------
# Document Setup
# ---------------------------------------------------------------------
OUT = "/home/user/workspace/claude-fuer-deutsches-recht/testakten/markenrecht-fashion-klotzzkette-vs-brezelmann-donauzon/Akte_klotzzkette_vs_Brezelmann_Donauzon.pdf"

frame = Frame(MARGIN, MARGIN, PAGE_W - 2*MARGIN, PAGE_H - 2*MARGIN,
              leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)

doc = BaseDocTemplate(OUT, pagesize=A4,
                      leftMargin=MARGIN, rightMargin=MARGIN,
                      topMargin=MARGIN, bottomMargin=MARGIN,
                      title="Akte klôtzzkètté ./. Brezelmann u. Donauzon",
                      author="Steinacker Lichtenberg & Partners IP Boutique")

doc.addPageTemplates([
    PageTemplate(id="default", frames=[frame], onPage=make_page_callback())
])

story = []

# We'll build story as a big list, then process at the end.
# All blatt_*() helpers return a list of flowables ending with PageBreak
# (PageBreak appended outside in story assembly).

# ---------------------------------------------------------------------
# Helper text constants
# ---------------------------------------------------------------------
KANZLEI_ADDR = ("Steinacker Lichtenberg & Partners IP Boutique\n"
                "Maximiliansplatz 19 · 80333 München\n"
                "Tel +49 89 21 03 96-0 · Fax -99\n"
                "kanzlei@steinacker-lichtenberg.de\n"
                "Federführend: Dr. Dr. A. Steinacker-von Tarsis LL.M.")

LG_FFM_ADDR = ("An das\nLandgericht Frankfurt am Main\n- Kammer für Markensachen -\n"
               "Gerichtsstraße 2\n60313 Frankfurt am Main\n\n"
               "vorab per beA")

# All page builders below are appended to story sequentially via exec of content_parts.
import glob as _glob
for _pf in sorted(_glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'content_part_*.py'))):
    print('[part]', os.path.basename(_pf))
    with open(_pf, 'r', encoding='utf-8') as _f:
        exec(_f.read(), globals())

print('[build] flowables collected:', len(story))

# Build
doc.build(story)
print('[done] PDF written to', OUT)
print('[done] Total Blatt:', BC.n)

