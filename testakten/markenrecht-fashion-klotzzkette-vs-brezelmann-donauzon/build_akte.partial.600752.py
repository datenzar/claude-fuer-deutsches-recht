#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Akte klôtzzkètté SA ./. Brezelmann Discount KG & Donauzon Marketplace GmbH u.a.
LG Frankfurt 2-03 O 412/26
Generator-Skript fuer eine fiktive, bewusst fragmentarisch-weirde Testakte.
"""

import os, random
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak,
    Table, TableStyle, KeepTogether, Image, Flowable, NextPageTemplate,
    Preformatted, HRFlowable
)
from reportlab.platypus.flowables import CondPageBreak

random.seed(1923)

# ---------- Fonts ----------
FONT_DIR = "/tmp/akte_fonts"
COMIC_DIR = "/usr/share/fonts/truetype/msttcorefonts"

pdfmetrics.registerFont(TTFont("Caveat", os.path.join(FONT_DIR, "Caveat-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Indie", os.path.join(FONT_DIR, "IndieFlower-Regular.ttf")))
try:
    pdfmetrics.registerFont(TTFont("Comic", os.path.join(COMIC_DIR, "comic.ttf")))
    pdfmetrics.registerFont(TTFont("ComicBold", os.path.join(COMIC_DIR, "comicbd.ttf")))
    HAS_COMIC = True
except Exception:
    HAS_COMIC = False

OUTFILE = "/home/user/workspace/claude-fuer-deutsches-recht/testakten/markenrecht-fashion-klotzzkette-vs-brezelmann-donauzon/Akte_klotzzkette_vs_Brezelmann_Donauzon.pdf"

# ---------- Page numbering ----------
class BlattCounter:
    def __init__(self):
        self.n = 0
    def next(self):
        self.n += 1
        return self.n
BLATT = BlattCounter()

# We use BaseDocTemplate with one frame, and an on_page handler that draws "Blatt N"
# We need to know what BLATT number each physical page corresponds to.
# Since each "document" in the Akte may span several pages, we increment per page.

def on_page(canv, doc):
    canv.saveState()
    page_num = doc.page  # current physical page
    canv.setFont("Helvetica-Oblique", 8)
    canv.setFillColor(colors.grey)
    canv.drawRightString(A4[0]-1.5*cm, 1.0*cm, f"Blatt {page_num}")
    # faint left margin marker like a punched-hole strip
    canv.setStrokeColor(colors.lightgrey)
    canv.setLineWidth(0.3)
    canv.line(2.0*cm, 1.5*cm, 2.0*cm, A4[1]-1.5*cm)
    # punched holes
    canv.setFillColor(colors.lightgrey)
    for y in (A4[1]*0.78, A4[1]*0.50, A4[1]*0.22):
        canv.circle(1.4*cm, y, 0.12*cm, stroke=0, fill=1)
    # tiny case ref
    canv.setFont("Helvetica", 6)
    canv.setFillColor(colors.grey)
    canv.drawString(2.5*cm, 1.0*cm, "Az. 2-03 O 412/26  ·  klôtzzkètté ./. Brezelmann + Donauzon")
    canv.restoreState()

# ---------- Styles ----------
styles = getSampleStyleSheet()

S_NORMAL = ParagraphStyle("N", parent=styles["Normal"], fontName="Times-Roman",
                          fontSize=10.5, leading=13.5, alignment=TA_JUSTIFY)
S_NORMAL_LEFT = ParagraphStyle("NL", parent=S_NORMAL, alignment=TA_LEFT)
S_H1 = ParagraphStyle("H1", parent=S_NORMAL, fontName="Times-Bold",
                      fontSize=14, leading=18, spaceAfter=8, spaceBefore=4)
S_H2 = ParagraphStyle("H2", parent=S_NORMAL, fontName="Times-Bold",
                      fontSize=11.5, leading=15, spaceAfter=4, spaceBefore=6)
S_SMALL = ParagraphStyle("SM", parent=S_NORMAL, fontSize=8.5, leading=11)
S_RIGHT = ParagraphStyle("R", parent=S_NORMAL, alignment=TA_RIGHT)
S_CENTER = ParagraphStyle("C", parent=S_NORMAL, alignment=TA_CENTER)
S_MONO = ParagraphStyle("M", parent=S_NORMAL, fontName="Courier", fontSize=9, leading=11.5, alignment=TA_LEFT)
S_MONO_SMALL = ParagraphStyle("MS", parent=S_MONO, fontSize=8, leading=10)
S_ITAL = ParagraphStyle("I", parent=S_NORMAL, fontName="Times-Italic")
S_HAND = ParagraphStyle("HW", parent=S_NORMAL, fontName="Caveat", fontSize=16, leading=20, alignment=TA_LEFT)
S_HAND_BIG = ParagraphStyle("HWB", parent=S_HAND, fontSize=20, leading=24)
S_INDIE = ParagraphStyle("IND", parent=S_NORMAL, fontName="Indie", fontSize=13, leading=17, alignment=TA_LEFT)
S_COMIC = ParagraphStyle("CO", parent=S_NORMAL, fontName=("Comic" if HAS_COMIC else "Times-Italic"), fontSize=11, leading=14)
S_BRIEFKOPF = ParagraphStyle("BK", parent=S_NORMAL, fontName="Times-Bold", fontSize=12, leading=14, alignment=TA_CENTER)
S_BRIEFKOPF_SUB = ParagraphStyle("BKS", parent=S_NORMAL, fontSize=8, leading=10, alignment=TA_CENTER, textColor=colors.HexColor("#444444"))
S_AKTENVERMERK = ParagraphStyle("AV", parent=S_NORMAL, fontName="Helvetica-Bold", fontSize=11, leading=14)

# ---------- Doc setup ----------
PAGE_W, PAGE_H = A4
MARGIN_L = 2.8*cm
MARGIN_R = 2.0*cm
MARGIN_T = 2.0*cm
MARGIN_B = 2.0*cm

frame_main = Frame(MARGIN_L, MARGIN_B, PAGE_W - MARGIN_L - MARGIN_R,
                   PAGE_H - MARGIN_T - MARGIN_B, id="main",
                   leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
                   showBoundary=0)

doc = BaseDocTemplate(OUTFILE, pagesize=A4,
                      leftMargin=MARGIN_L, rightMargin=MARGIN_R,
                      topMargin=MARGIN_T, bottomMargin=MARGIN_B,
                      title="Akte klôtzzkètté ./. Brezelmann + Donauzon",
                      author="Steinacker Lichtenberg & Partners IP Boutique")

doc.addPageTemplates([PageTemplate(id="main", frames=[frame_main], onPage=on_page)])

story = []

# ---------- Helper flowables ----------
class HLine(Flowable):
    def __init__(self, width=None, thickness=0.5, color=colors.black, space_before=2, space_after=2):
        Flowable.__init__(self)
        self.width = width
        self.thickness = thickness
        self.color = color
        self.space_before = space_before
        self.space_after = space_after
    def wrap(self, availW, availH):
        self._w = self.width if self.width else availW
        self._h = self.thickness + self.space_before + self.space_after
        return self._w, self._h
    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, self.space_after, self._w, self.space_after)

class StampBox(Flowable):
    """A skewed/rotated stamp-like box with text."""
    def __init__(self, text, w=5.5*cm, h=2.2*cm, color=colors.HexColor("#7a1d1d"), angle=-8):
        Flowable.__init__(self)
        self.text = text; self.w=w; self.h=h; self.color=color; self.angle=angle
    def wrap(self, aw, ah):
        return self.w, self.h
    def draw(self):
        c = self.canv
        c.saveState()
        c.translate(self.w/2, self.h/2)
        c.rotate(self.angle)
        c.setStrokeColor(self.color)
        c.setLineWidth(1.5)
        c.rect(-self.w/2+0.2*cm, -self.h/2+0.2*cm, self.w-0.4*cm, self.h-0.4*cm, stroke=1, fill=0)
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(self.color)
        lines = self.text.split("\n")
        y = (len(lines)-1)*5
        for L in lines:
            c.drawCentredString(0, y, L)
            y -= 11
        c.restoreState()

class FaxHeader(Flowable):
    def __init__(self, sender, recipient, date, fax_nr, pages):
        Flowable.__init__(self)
        self.sender=sender; self.recipient=recipient; self.date=date
        self.fax_nr=fax_nr; self.pages=pages
        self.w = 16*cm; self.h = 3.5*cm
    def wrap(self, aw, ah):
        self.w = aw
        return aw, self.h
    def draw(self):
        c = self.canv
        c.setFillColor(colors.black)
        c.rect(0, self.h-0.7*cm, self.w, 0.7*cm, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 13)
        c.drawString(0.3*cm, self.h-0.55*cm, "■ TELEFAX  ■  FACSIMILE TRANSMISSION  ■")
        c.setFillColor(colors.black)
        c.setStrokeColor(colors.black)
        c.setLineWidth(0.7)
        c.rect(0, 0, self.w, self.h-0.7*cm, fill=0, stroke=1)
        c.setFont("Courier-Bold", 9)
        rows = [
            ("VON / FROM:    ", self.sender),
            ("AN  / TO:      ", self.recipient),
            ("FAX-NR.:       ", self.fax_nr),
            ("DATUM/DATE:    ", self.date),
            ("SEITEN/PAGES:  ", self.pages),
        ]
        y = self.h - 1.0*cm
        for k,v in rows:
            c.setFont("Courier-Bold", 9)
            c.drawString(0.3*cm, y, k)
            c.setFont("Courier", 9)
            c.drawString(4.3*cm, y, v)
            y -= 0.4*cm

class HoleStrip(Flowable):
    """Visual: a torn-paper strip like a fax footer with crinkle."""
    def __init__(self, w=16*cm, h=0.4*cm):
        Flowable.__init__(self); self.w=w; self.h=h
    def wrap(self, aw, ah):
        self.w = aw; return aw, self.h
    def draw(self):
        c = self.canv
        c.setStrokeColor(colors.grey); c.setLineWidth(0.3)
        x = 0
        while x < self.w:
            c.line(x, 0, x+0.15*cm, self.h)
            c.line(x+0.15*cm, self.h, x+0.3*cm, 0)
            x += 0.3*cm

# ---------- Briefkopf ----------
def briefkopf_steinacker():
    return [
        Paragraph("STEINACKER · LICHTENBERG &amp; PARTNERS", S_BRIEFKOPF),
        Paragraph("IP Boutique · Rechtsanwälte · Patentanwälte · Marken &amp; Design",
                  S_BRIEFKOPF_SUB),
        Paragraph("Maximiliansplatz 19 · 80333 München · Tel +49 (0)89 / 24 21 88 - 0 · Fax - 99 · kanzlei@steinacker-ip.de",
                  S_BRIEFKOPF_SUB),
        HLine(thickness=0.8, color=colors.HexColor("#1a3552"), space_after=4, space_before=2),
        Spacer(1, 6),
    ]

def briefkopf_donauzon():
    return [
        Paragraph("Donauzon Marketplace GmbH · Legal Department EU/DACH", S_BRIEFKOPF),
        Paragraph("Erdbeerallee 88 · 80807 München · Sitz Luxembourg · RCS B 198.442",
                  S_BRIEFKOPF_SUB),
        HLine(thickness=0.6, color=colors.HexColor("#225522"), space_after=4, space_before=2),
        Spacer(1, 6),
    ]

def briefkopf_brezelmann():
    return [
        Paragraph("BREZELMANN DISCOUNT KG · &quot;DER PREIS PASST IMMER&quot;", S_BRIEFKOPF),
        Paragraph("Wurstgasse 4 · 97980 Bad Mergentheim · Telefon (07931) 4 88 02 · Fax 4 88 03",
                  S_BRIEFKOPF_SUB),
        HLine(thickness=0.6, color=colors.HexColor("#664400"), space_after=4, space_before=2),
        Spacer(1, 6),
    ]

def aktenvermerk_header(titel, datum, verfasser):
    return [
        Paragraph(f"<b>A K T E N V E R M E R K</b>", S_AKTENVERMERK),
        Paragraph(f"Vorgang: {titel}", S_SMALL),
        Paragraph(f"Datum: {datum}  ·  Verfasser/in: {verfasser}", S_SMALL),
        HLine(thickness=0.4, space_after=2, space_before=2),
        Spacer(1, 6),
    ]

def section_separator(label=""):
    return [
        Spacer(1, 6),
        HLine(thickness=0.7, color=colors.HexColor("#444444"), space_after=4, space_before=4),
        Paragraph(f"<font color='#666666' size=7>· · · {label} · · ·</font>", S_CENTER),
        HLine(thickness=0.3, color=colors.HexColor("#888888"), space_after=2, space_before=2),
        Spacer(1, 4),
    ]

# =====================================================================
# BLATT 1 — AKTENRUBRUM (Vorderblatt)
# =====================================================================
def blatt_rubrum():
    s = []
    s.append(Spacer(1, 1.2*cm))
    s.append(Paragraph("STEINACKER · LICHTENBERG &amp; PARTNERS", ParagraphStyle("BK0", parent=S_BRIEFKOPF, fontSize=16, leading=20)))
    s.append(Paragraph("IP Boutique München · Paris · Milano (Korrespondenz)", S_BRIEFKOPF_SUB))
    s.append(Spacer(1, 1.0*cm))
    s.append(HLine(thickness=1.4, color=colors.HexColor("#1a3552"), space_after=8, space_before=4))
    s.append(Paragraph("A&nbsp;&nbsp;K&nbsp;&nbsp;T&nbsp;&nbsp;E", ParagraphStyle("Ak", parent=S_H1, fontSize=28, leading=32, alignment=TA_CENTER)))
    s.append(Spacer(1, 0.4*cm))
    s.append(Paragraph(
        "<b>klôtzzkètté SA</b><br/>"
        "(Paris / Milano)<br/><br/>"
        "<font size=10>./.</font><br/><br/>"
        "<b>Brezelmann Discount KG</b> (Bad Mergentheim)<br/>"
        "<b>Donauzon Marketplace GmbH</b> (Luxembourg / München)<br/>"
        "<i>und Annexverfahren</i>",
        ParagraphStyle("Akr", parent=S_CENTER, fontSize=14, leading=20)))
    s.append(Spacer(1, 0.8*cm))
    s.append(HLine(thickness=0.4, space_after=6, space_before=6))
    data = [
        ["Hauptaktenzeichen Kanzlei", "STK-IP / 26 / 0117 - KLÖ"],
        ["LG Frankfurt am Main", "Az. 2-03 O 412/26 (Kammer f. Markensachen)"],
        ["OLG Frankfurt (zu erwarten)", "noch n. zug."],
        ["EUIPO Alicante – Widerspruch", "B 4 187 932"],
        ["EUIPO Alicante – Riechmarke", "Beschwerde R 0918/2026-5"],
        ["DPMA München – Anti-KI-Marke", "30 2025 218 446"],
        ["BPatG München", "25 W (pat) 88/26"],
        ["BGH – Soundmarke-Rechtsbeschwerde", "I ZB 47/26 (Hinweisbeschluß ergangen)"],
    ]
    t = Table(data, colWidths=[6.0*cm, 8.5*cm])
    t.setStyle(TableStyle([
        ("FONT",(0,0),(-1,-1),"Times-Roman",10),
        ("FONT",(0,0),(0,-1),"Times-Bold",10),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BOTTOMPADDING",(0,0),(-1,-1),3),
        ("TOPPADDING",(0,0),(-1,-1),3),
        ("LINEBELOW",(0,0),(-1,-1),0.2,colors.lightgrey),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.5*cm))
    s.append(HLine(thickness=0.4, space_after=6, space_before=6))
    s.append(Paragraph("<b>Streitwert (vorläufig festgesetzt):</b> EUR 4.800.000,00", S_NORMAL_LEFT))
    s.append(Paragraph("(LG Frankfurt + Annex EUIPO + BPatG; Addition entgegen der ständigen Praxis sub specie litis pendente, vgl. Beschluss vom 19.03.2026, Bl. 23 d.A.)", S_SMALL))
    s.append(Spacer(1, 0.5*cm))
    s.append(Paragraph("<b>Federführung:</b> Frau Dr. Dr. Annabella Steinacker-von Tarsis LL.M. (Cantab.) – Partnerin", S_NORMAL_LEFT))
    s.append(Paragraph("<b>Mitbearbeitung:</b> RA Maximilian Freiherr von Brenkenhoff", S_NORMAL_LEFT))
    s.append(Paragraph("<b>Mandantin:</b> klôtzzkètté SA, 12 rue du Faubourg Saint-Honoré, 75008 Paris (RCS Paris 552 094 471)", S_NORMAL_LEFT))
    s.append(Paragraph("<b>Ansprechpartnerin Mandantin:</b> Mme la Comtesse Béatrice de Klôtzzkètté-Visconti (présidente du conseil)", S_NORMAL_LEFT))
    s.append(Spacer(1, 0.7*cm))
    s.append(StampBox("AKTE EILT!\nLite pendente\n— EILT SEHR —", angle=-12))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("<i>Hinweis: Querverweise siehe Blatt 47 (Skizze Krönchen-Monogramm K°°) sowie Bl. 63 (Pitti-Uomo-Protokoll). Anlage K12 wird nachgereicht.</i>", S_SMALL))
    return s

story += blatt_rubrum()
story.append(PageBreak())

# =====================================================================
# Inhaltsverzeichnis (bewusst ungenau)
# =====================================================================
def blatt_inhalt():
    s = briefkopf_steinacker()
    s.append(Paragraph("Inhalts- und Heftungsverzeichnis (vorläufig, Stand 17.04.2026)", S_H1))
    s.append(Paragraph("<i>— Achtung: Reihenfolge der Heftung folgt dem chronologischen Aufkommen, nicht der sachlogischen Gliederung. Inhalt springt zeitlich. Sekretariat Frau Wenzel-Hugenberg bittet um Nachsicht. —</i>", S_SMALL))
    s.append(Spacer(1, 6))
    rows = [
        ["Blatt", "Gegenstand", "Datum"],
        ["1", "Aktenrubrum / Deckblatt", "lfd."],
        ["2", "Inhaltsverzeichnis (dieses Blatt)", "17.04.2026"],
        ["3–6", "Markenportfolio-Übersicht klôtzzkètté SA", "Stand 02/2026"],
        ["7–8", "Aktenvermerk Erstbesprechung Mme la Comtesse", "08.01.2026"],
        ["9–14", "Abmahnung an Brezelmann Discount KG (Schriftsatz)", "22.01.2026"],
        ["15", "Notizzettel Steinacker (handschriftlich) — &quot;Comtesse will Blut sehen&quot;", "23.01.2026"],
        ["16–18", "E-Mail-Kette Comtesse Béatrice ./. Steinacker (Bd. I)", "24.01.–05.02.2026"],
        ["19", "Fax Brezelmann an Steinacker", "29.01.2026"],
        ["20–28", "Antragsschrift einstw. Verfügung LG Frankfurt", "11.03.2026"],
        ["29–31", "Schutzschriftenregister-Abfrage Hessen", "10.03.2026"],
        ["32–34", "Einstweilige Verfügung LG Frankfurt (Ausfertigung)", "11.03.2026"],
        ["35–39", "Gerichtsvollzieher-Protokoll Pitti Uomo Florenz", "14.–15.03.2026"],
        ["40–42", "Inventarliste beschlagnahmte Ware (handschriftlich)", "15.03.2026"],
        ["43–46", "Detektivbericht Spuernase-Couture GmbH", "20.02.2026"],
        ["47", "<i>Skizze Krönchen-Monogramm K°° (Querverweis-Ziel)</i>", "—"],
        ["48–54", "EUIPO Widerspruchsschrift B 4 187 932 ./. UAB &quot;klotzkettie&quot;", "12.12.2025"],
        ["55–57", "EUIPO Beanstandung Riechmarke (Sieckmann)", "03.09.2025"],
        ["58–60", "Olfaktorik-Gutachten Mlle Hortense Périgord", "18.10.2025"],
        ["61–62", "DPMA-Annahme Anti-KI-Authentizitätsmarke 30 2025 218 446", "11.11.2025"],
        ["63–66", "Klageerwiderung Donauzon (DSA-Argumentation)", "02.04.2026"],
        ["67–72", "Replik Kanzlei mit Coty/Copad-Dior-Pierre-Fabre-Zitaten", "14.04.2026"],
        ["73–74", "BPatG Protokollauszug Verhandlung 25 W (pat) 88/26", "27.03.2026"],
        ["75", "BGH-Hinweisbeschluss I ZB 47/26 (Soundmarke)", "06.04.2026"],
        ["76–78", "E-Mail-Kette atelier@klotzzkette.com ./. Marketing", "Diverse"],
        ["79–80", "Memo Kanzlei zur Gesamtstrategie", "16.04.2026"],
        ["81–82", "Kostennoten I–III RVG", "fortlfd."],
        ["83–84", "Löschungsantrag DPMA gegen &quot;klotzkettiee&quot;", "30.03.2026"],
        ["85", "Notizzettel Steinacker II (handschriftlich)", "10.04.2026"],
        ["86–88", "Beschwerde EUIPO BoA gegen Riechmarken-Zurückweisung", "17.10.2025"],
        ["89–90", "Schlussvermerk / offene Punkte", "lfd."],
    ]
    t = Table(rows, colWidths=[1.6*cm, 11.8*cm, 2.6*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT",(0,0),(-1,0),"Times-Bold",10),
        ("FONT",(0,1),(-1,-1),"Times-Roman",9),
        ("LINEBELOW",(0,0),(-1,0),0.6,colors.black),
        ("LINEBELOW",(0,1),(-1,-1),0.15,colors.lightgrey),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),3),
        ("RIGHTPADDING",(0,0),(-1,-1),3),
        ("TOPPADDING",(0,0),(-1,-1),2),
        ("BOTTOMPADDING",(0,0),(-1,-1),2),
    ]))
    s.append(t)
    s.append(Spacer(1, 8))
    s.append(Paragraph("<i>Anmerkung Sekretariat: Anlage K12 (chem. Spektrogramm Iris pallida) liegt physisch beim DHL-Sondertransport, wird nachgeheftet. Bl. 47 trägt nur die Skizze, das eigentliche Gutachten zum Monogramm folgt Bl. 58 ff. (anders als im Querverweis Bl. 1 angedeutet — Verwirrung!).</i>", S_SMALL))
    return s

story += blatt_inhalt()
story.append(PageBreak())

# =====================================================================
# Markenportfolio-Übersicht (3-4 Seiten)
# =====================================================================
def blatt_portfolio():
    s = briefkopf_steinacker()
    s.append(Paragraph("Markenportfolio klôtzzkètté SA – konsolidierte Übersicht", S_H1))
    s.append(Paragraph("Stand: 02/2026 · erstellt durch RA Frhr. v. Brenkenhoff · geprüft Steinacker", S_SMALL))
    s.append(Spacer(1, 6))
    s.append(Paragraph("Die nachstehende Aufstellung umfasst sämtliche für das Verfahren 2-03 O 412/26 streitgegenständlichen Schutzrechte sowie die im Annex (EUIPO, DPMA, BPatG) anhängigen Anmeldungen. Die Reihenfolge entspricht der internen Aktentaxierung &quot;K-01&quot; bis &quot;K-09&quot;.", S_NORMAL))
    s.append(Spacer(1, 6))
    rows = [
        ["Nr.", "Markentyp", "Zeichen / Beschreibung", "Register / Aktenzeichen", "Klassen / Status"],
        ["K-01", "Wortmarke", "klôtzzkètté", "DPMA 30 2008 044 117\nEUTM 005 412 880", "Kl. 3, 14, 18, 25, 35 · eingetr., rechtskräftig"],
        ["K-02", "Wort-/Bildmarke", "klôtzzkètté + Krönchen-Monogramm &quot;K°°&quot;", "EUTM 010 988 411", "Kl. 3, 9, 14, 18, 25, 35, 41 · eingetr."],
        ["K-03", "Bildmarke", "silbern-emailliertes Krönchen (Pantone 877 C)", "DPMA 30 2014 077 312", "Kl. 14, 18, 25 · eingetr."],
        ["K-04", "Positionsmarke", "seidenes Goldfaden-Krönchen-Insignium auf linker Schuh-Innensohle Pos. 1 cm vom Fersenrand", "EUTM 015 887 442", "Kl. 25 · eingetr. (vgl. EuGH C-163/16 Louboutin)"],
        ["K-05", "Slogan-Marke", "&quot;LE LUXE EST UN DROIT NATUREL&quot;", "EUTM 018 412 776", "Kl. 25, 35 · eingetr."],
        ["K-06", "Soundmarke", "8-Sekunden-Jingle: geknickter Champagnerstiel + Eiswürfel-Klirren + Frauenstimme flüstert &quot;klôtzzkètté&quot; (MP3 hinterlegt)", "EUTM 018 502 311", "Kl. 3, 14, 25, 35, 41 · eingetr.; Rechtsbeschwerde anh. BGH I ZB 47/26"],
        ["K-07", "3D-Formmarke", "Parfumflakon &quot;K°° pour Femme&quot;, hexagonale Karaffe mit asymmetrischem Stopfen, 50 ml", "EUTM 008 776 015", "Kl. 3 · eingetr.; Verkehrsdurchsetzung nachgewiesen"],
        ["K-08", "Authentizitätsmarke", "&quot;klôtzzkètté pure human craft&quot; mit Zertifikatsstempel-Optik (sog. Anti-KI-Marke)", "DPMA 30 2025 218 446", "Kl. 14, 18, 25, 35, 42 · in Anmeldung, akzept. 11.11.2025"],
        ["K-09", "Duftmarke (Riechmarke)", "Akkord aus Iris pallida, weißer Birne und feuchtem Wildleder", "EUTM-Anm. 018 612 901", "Kl. 3 · ZURÜCKGEWIESEN 03.09.2025 (Sieckmann); Beschwerde R 0918/2026-5 anh."],
    ]
    t = Table(rows, colWidths=[1.2*cm, 2.5*cm, 5.4*cm, 3.3*cm, 3.6*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT",(0,0),(-1,0),"Helvetica-Bold",8.5),
        ("FONT",(0,1),(-1,-1),"Times-Roman",8.5),
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#e8eef5")),
        ("GRID",(0,0),(-1,-1),0.25,colors.grey),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),3),
        ("RIGHTPADDING",(0,0),(-1,-1),3),
        ("TOPPADDING",(0,0),(-1,-1),3),
        ("BOTTOMPADDING",(0,0),(-1,-1),3),
    ]))
    s.append(t)
    s.append(Spacer(1, 8))
    s.append(Paragraph("<b>I. Sachlich-rechtliche Bemerkungen zum Portfolio</b>", S_H2))
    s.append(Paragraph(
        "1. Die Wortmarke K-01 genießt aufgrund der seit 1923 ununterbrochenen Benutzung in Paris, "
        "seit 1971 in München und seit 1989 in Mailand notorische Bekanntheit i.S.d. Art. 6<sup>bis</sup> PVÜ "
        "sowie erweiterten Schutz nach §§ 14 Abs. 2 Nr. 3, 14 Abs. 5 MarkenG bzw. Art. 9 Abs. 2 lit. c) UMV. "
        "Eine Bekanntheitsumfrage Allensbach 2023 weist 71,4 % aktive ungestützte Markenkenntnis in der "
        "relevanten Verkehrskreisgruppe der Personen mit HHE &gt; EUR 250.000 p.a. nach (Anlage K-04).",
        S_NORMAL))
    s.append(Paragraph(
        "2. Die Positionsmarke K-04 ist trotz Louboutin-Präjudiz nach EuGH C-163/16 als <i>nicht ausschließlich</i> "
        "durch die Ware bedingte Lage des Krönchens zur Eintragung gelangt. Die Streitfrage, ob die Donauzon-"
        "Listings (insb. der Suchwortverkauf &quot;Krönchen Sohle&quot;) eine markenmäßige Benutzung darstellen, "
        "ist Gegenstand des Verfahrens 2-03 O 412/26.",
        S_NORMAL))
    s.append(Paragraph(
        "3. Die Soundmarke K-06 wurde unter der bemerkenswerten — und auch verfahrensgegenständlichen — "
        "Erwägung eingetragen, dass der Jingle eine spezifisch <i>luxueuse</i> Klangsignatur darstellt "
        "(&quot;Champagner-Schaum-Glissando&quot;, so der Sachverständige Prof. Steinpfeil im Gutachten "
        "Bl. 73 d.A.). Die Brezelmann KG verwendet in ihren TikTok-Werbespots seit 11/2025 nahezu identisch "
        "&quot;klörrr… kettä&quot; mit Eiswürfel-Sample.",
        S_NORMAL))
    s.append(Paragraph(
        "4. Die Riechmarke K-09 wurde durch EUIPO-Prüfer Sr. Iván Castellanos zurückgewiesen unter Berufung auf "
        "EuGH C-273/00 (Sieckmann). Die Beschwerde stützt sich auf eine erweiterte Tetra-Modalitäten-Beschreibung "
        "(verbal + chemisches Spektrogramm GC-MS + Hinterlegung Riechprobe Grasse + 3D-Olfakto-Diagramm Mlle Périgord), "
        "vgl. ausführlich Bl. 58–60 d.A. Erfolgschancen werden mit 28–34 % bewertet (interne Quote).",
        S_NORMAL))
    s.append(Spacer(1, 6))
    s.append(Paragraph("<b>II. Lizenzlage / selektives Vertriebssystem</b>", S_H2))
    s.append(Paragraph(
        "Die klôtzzkètté SA unterhält ein streng selektives Vertriebssystem nach Maßgabe der Maßstäbe von "
        "EuGH C-230/16 (Coty Germany ./. Akzente Distribution) sowie der älteren Pierre-Fabre-Rechtsprechung "
        "(EuGH C-439/09). Verkauf erfolgt ausschließlich über autorisierte Boutiquen in den Städten Paris, "
        "London, München, Mailand, Wien, Genf, Monaco, New York, Dubai, Singapur sowie über die unter eigener "
        "Domain betriebene Website. Plattformverkauf — insbesondere über Marktplätze wie Donauzon — ist "
        "<b>vertraglich ausgeschlossen</b>; ein Verstoß löst Vertragsstrafe i.H.v. EUR 250.000 pro Vorfall aus "
        "(vgl. BGH I ZR 35/19 zur Wirksamkeit gestaffelter Vertragsstrafen, mutatis mutandis).",
        S_NORMAL))
    s.append(Paragraph(
        "<i>venire contra factum proprium</i>: Donauzon wendet ein, klôtzzkètté habe in den Jahren 2018–2020 selbst "
        "(damals unter Marketingleitung Hr. Schäffer-Lentini) Pop-up-Listings auf Donauzon Frankreich getestet. "
        "Hierzu wird der Vertrag vom 14.06.2018 (Anlage B-7) noch zu würdigen sein. Vortrag der Mandantin: nur "
        "Markenüberwachungstest, kein Vertrieb. siehe ferner Bl. 63 d.A.",
        S_NORMAL))
    return s

story += blatt_portfolio()
story.append(PageBreak())

# Continue portfolio onto more pages — additional detail tables (klassen, prio dates)
def blatt_portfolio_p2():
    s = briefkopf_steinacker()
    s.append(Paragraph("Markenportfolio – Detail Klassenzuordnung und Prioritätsdaten", S_H2))
    s.append(Spacer(1, 4))
    rows = [["Marke","Nizza-Klasse","Waren/DL (Kurzfassung)","Prio-Datum","Erneuerung fällig"]]
    items = [
        ("K-01 klôtzzkètté Wort","3","Parfum, Eaux de Toilette, Kosmetika sartoriale","12.04.2008","12.04.2028"),
        ("K-01","14","Schmuck, Uhren, Edelmetalle, Manschettenknöpfe","12.04.2008","12.04.2028"),
        ("K-01","18","Lederwaren, Reisegepäck, Handtaschen, Schirme","12.04.2008","12.04.2028"),
        ("K-01","25","Bekleidung, Schuhwaren (excl. orthopädisch), Kopfbedeckungen, Krawatten","12.04.2008","12.04.2028"),
        ("K-01","35","Einzelhandel, insb. Boutique-Einzelhandel der Klassen 3,14,18,25","12.04.2008","12.04.2028"),
        ("K-02 Wort-/Bild","3,9,14,18,25,35,41","wie K-01 + Brillen + Couture-Events (Kl. 41)","18.09.2012","18.09.2032"),
        ("K-03 Bild Krönchen","14,18,25","Schmuck-Anwendung, Lederwaren-Prägung, Schuh-Insignium","02.07.2014","02.07.2034"),
        ("K-04 Positionsmarke","25","Schuhwaren, insb. Damenschuhe Ledersohle","11.11.2015","11.11.2025 ✓ erneuert"),
        ("K-05 Slogan","25,35","Bekleidung; Werbung, Verkaufsförderung, PR","04.06.2020","04.06.2030"),
        ("K-06 Sound","3,14,25,35,41","Eaux + Schmuck + Bekleidung + Werbung + Events","19.01.2022","19.01.2032"),
        ("K-07 3D-Flakon","3","Parfums, Eaux, Düfte","27.05.2009","27.05.2029"),
        ("K-08 Anti-KI","14,18,25,35,42","Authentizitätszertifikate; SW-DL Echtheitsprüfung","08.10.2025","Anm. lfd."),
        ("K-09 Riechmarke","3","Parfums (Akkord Iris/Birne/Wildleder)","19.03.2025","ZURÜCKGEW. 03.09.2025"),
    ]
    for r in items:
        rows.append(list(r))
    t = Table(rows, colWidths=[3.6*cm, 2.0*cm, 6.0*cm, 2.0*cm, 2.4*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT",(0,0),(-1,0),"Helvetica-Bold",8),
        ("FONT",(0,1),(-1,-1),"Times-Roman",8),
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#e8eef5")),
        ("GRID",(0,0),(-1,-1),0.2,colors.grey),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),2),
        ("RIGHTPADDING",(0,0),(-1,-1),2),
        ("TOPPADDING",(0,0),(-1,-1),2),
        ("BOTTOMPADDING",(0,0),(-1,-1),2),
    ]))
    s.append(t)
    s.append(Spacer(1, 8))
    s.append(Paragraph("<b>III. Internationale Erstreckungen (Madrider Protokoll)</b>", S_H2))
    s.append(Paragraph(
        "Die Wortmarke K-01 wurde unter IR-Nr. 1 042 887 für die Vertragsstaaten CH, NO, IS, LI, MC, GB, US, "
        "JP, KR, SG, AU, CA, AE und unter regionaler Erstreckung Benelux (gestrichen seit EUTM-Eintragung) "
        "erstreckt. K-06 (Sound) konnte mangels Eintragungsfähigkeit in mehreren Vertragsstaaten (insb. JP, KR) "
        "nicht vollständig erstreckt werden — vgl. JPO-Bescheid 26.05.2023 (Anlage K-21).",
        S_NORMAL))
    s.append(Paragraph(
        "<i>Die Bewertung der notorischen Bekanntheit nach Art. 6bis PVÜ in den Märkten Naher Osten (DXB, "
        "DOH, RUH) ist Gegenstand einer separaten Akte STK-IP/26/0118-KLÖ (sog. &quot;Gulf-Strand&quot;), "
        "die hier nicht weiter erörtert wird.</i>",
        S_NORMAL))
    s.append(Spacer(1, 8))
    s.append(Paragraph("<b>IV. Bekanntheitsanalysen — Auszug</b>", S_H2))
    s.append(Paragraph(
        "Allensbach 2023 (n=2.041, qualifizierter Sample HHE&gt;EUR 250k):<br/>"
        "&nbsp;&nbsp;• ungestützte Markenkenntnis &quot;klôtzzkètté&quot;: 71,4 % (CI 95 %: 68,9–73,9)<br/>"
        "&nbsp;&nbsp;• gestützte Markenkenntnis: 92,1 %<br/>"
        "&nbsp;&nbsp;• Zuordnung Krönchen-Bildzeichen: 64,8 %<br/>"
        "&nbsp;&nbsp;• Zuordnung Sound-Jingle (blind): 41,3 %<br/>"
        "&nbsp;&nbsp;• Zuordnung Flakon-Form (blind): 58,7 %<br/>"
        "&nbsp;&nbsp;• Zuordnung Slogan &quot;LE LUXE EST UN DROIT NATUREL&quot;: 36,2 %",
        S_NORMAL))
    return s

story += blatt_portfolio_p2()
story.append(PageBreak())

# =====================================================================
# Aktenvermerk Erstbesprechung Comtesse
# =====================================================================
def blatt_av_erstgespraech():
    s = briefkopf_steinacker()
    s += aktenvermerk_header(
        "Erstbesprechung Mme la Comtesse Béatrice de Klôtzzkètté-Visconti in re Brezelmann Discount KG",
        "08.01.2026, 14:30 – 17:50 Uhr",
        "Dr. Dr. Steinacker-von Tarsis (Federführung); Frhr. v. Brenkenhoff")
    s.append(Paragraph("<b>1. Anwesend</b>", S_H2))
    s.append(Paragraph(
        "Mme la Comtesse Béatrice de Klôtzzkètté-Visconti (Mandantin, persönlich); "
        "Herr Dr. Marc-Antoine Dufresne (CFO klôtzzkètté SA, via Polycom); "
        "Frau Giulia Bottacin (Direttrice atelier Milano); "
        "auf Kanzleiseite die Federführende sowie der Mitbearbeiter; protokollführend Frau Wenzel-Hugenberg.",
        S_NORMAL))
    s.append(Paragraph("<b>2. Sachverhalt nach Schilderung der Mandantin</b>", S_H2))
    s.append(Paragraph(
        "Mme la Comtesse berichtet, sie habe am 27.12.2025 bei einem privaten Besuch in der Filiale der "
        "Brezelmann Discount KG in Bad Mergentheim (Wurstgasse 4) folgende Wahrnehmungen gemacht:",
        S_NORMAL))
    s.append(Paragraph(
        "a) Im Eingangsbereich seien T-Shirts mit der Aufschrift &quot;klötzkette&quot; (sic, ohne Akzente, "
        "mit nur einem &quot;z&quot;) zum Stückpreis von EUR 7,99 angeboten worden, gestapelt auf "
        "Europaletten. Eine Verkäuferin habe auf Befragen geäußert, &quot;das ist diese teure französische "
        "Marke, jetzt eben günstiger&quot;.<br/>"
        "b) An der Kassenzone sei ein Acrylständer mit ca. 40 Parfumflakons aufgestellt gewesen, deren Form "
        "der hexagonalen Karaffe mit asymmetrischem Stopfen (3D-Formmarke K-07) zum Verwechseln ähnlich sei; "
        "Inhalt laut Etikett &quot;Eau de Toilette Königsfräulein No. 5&quot;, Preis EUR 12,99.<br/>"
        "c) Im Lautsprecher der Filiale sei in regelmäßigen Abständen ein Jingle abgespielt worden, der "
        "die typische Champagner-Schaum-Glissando-Signatur der Soundmarke K-06 imitiere; statt &quot;klôtzzkètté&quot; "
        "werde jedoch &quot;klörrr-kettä&quot; gesprochen.<br/>"
        "d) Im Schaufenster sei ein Poster mit dem Slogan &quot;Luxus ist ein Grundrecht&quot; (deutsche "
        "Übersetzung des Slogans K-05) angebracht gewesen.",
        S_NORMAL))
    s.append(Paragraph("<b>3. Erste rechtliche Würdigung</b>", S_H2))
    s.append(Paragraph(
        "Es spricht alles dafür, dass eine flächendeckende, vorsätzliche und gewerbsmäßige Markenrechtsverletzung "
        "i.S.d. §§ 14 Abs. 2 Nr. 1, 2 und 3 MarkenG sowie Art. 9 Abs. 2 lit. a)-c) UMV vorliegt. Die Doppelidentität "
        "scheidet zwar wegen der Schreibvariante &quot;klötzkette&quot; aus, jedoch ist die Verwechslungsgefahr "
        "im Sinne der Lloyd-Schuhfabrik-Rechtsprechung (EuGH C-342/97) evident. Hinsichtlich der Soundmarke und der "
        "3D-Formmarke kommt zusätzlich der erweiterte Bekanntheitsschutz in Betracht.",
        S_NORMAL))
    s.append(Paragraph("<b>4. Strategische Weichenstellung</b>", S_H2))
    s.append(Paragraph(
        "Die Mandantin wünscht ausdrücklich ein <i>überschießendes</i> Vorgehen: Abmahnung, einstweilige "
        "Verfügung, Hauptsacheklage, parallel Strafanzeige gem. § 143 MarkenG, Schadensersatz nach Lizenzanalogie. "
        "Auf den Hinweis der Kanzlei, dass eine Strafanzeige taktisch sub specie causa nuocendi nicht zwingend "
        "geboten sei, bestand die Mandantin auf folgender Formulierung (wörtlich, kursiv): "
        "<i>&quot;Madame, je veux que ces gens du discount comprennent qu'ils ne touchent pas à mon héritage. "
        "Mon arrière-grand-père a fondé cette maison en 1923. Pas un seul T-shirt à 7,99 ne salira ce nom.&quot;</i>",
        S_NORMAL))
    s.append(Paragraph("<b>5. Vergütung</b>", S_H2))
    s.append(Paragraph(
        "Vereinbart wird eine Pauschalvergütung gem. § 3a RVG i.H.v. EUR 120.000 für die erstinstanzliche "
        "Bearbeitung des Hauptverfahrens zzgl. gesetzlicher Gebühren für eV, Annexverfahren EUIPO und BPatG, "
        "Auslagen sowie 19 % USt. Vorschuss EUR 60.000 ist binnen 14 Tagen einzuzahlen (Eingang nachweisbar "
        "12.01.2026, Bl. 81 d.A.).",
        S_NORMAL))
    s.append(Paragraph("<b>6. Ausblick</b>", S_H2))
    s.append(Paragraph(
        "Abmahnung wird bis 22.01.2026 versandt. Recherche zu Brezelmann Discount KG (Detektei Spuernase-Couture "
        "GmbH, Frankfurt) wird zeitgleich beauftragt. Mit Antwort der Gegenseite ist binnen 14 Tagen zu rechnen. "
        "Die Mandantin hat ausdrücklich um wöchentlichen Statusbericht in französischer Sprache gebeten.",
        S_NORMAL))
    s.append(Spacer(1, 10))
    s.append(Paragraph("gez. Dr. Dr. Steinacker-von Tarsis", S_RIGHT))
    return s

story += blatt_av_erstgespraech()
story.append(PageBreak())

# Second page of AV — handwritten side note
def blatt_av_handnotiz():
    s = []
    s.append(Paragraph("[Eingeheftet als Beiblatt zum Aktenvermerk 08.01.2026]", S_SMALL))
    s.append(Spacer(1, 12))
    s.append(Paragraph("Comtesse will Blut sehen.", S_HAND_BIG))
    s.append(Spacer(1, 6))
    s.append(Paragraph("Wirklich. Sie hat zweimal &quot;sang&quot; gesagt. Auch &quot;tête de Brezelmann sur un plateau&quot;.", S_HAND))
    s.append(Spacer(1, 4))
    s.append(Paragraph("Vorschlag MvB: erst Abmahnung, dann eV Pitti Uomo (März 2026 in Florenz!) — dort haben die ihren Hauptstand.", S_HAND))
    s.append(Spacer(1, 4))
    s.append(Paragraph("Strafanzeige nach §143 MarkenG — bitte erst nach Bestandskraft eV einreichen.", S_HAND))
    s.append(Spacer(1, 4))
    s.append(Paragraph("MERKE: Klassiker — &quot;lite pendente&quot; Beruhigung der Mandantin. Niemals zugeben, dass die Riechmarke wackelt!", S_HAND))
    s.append(Spacer(1, 12))
    s.append(Paragraph("— A.S.", S_HAND))
    s.append(Spacer(1, 30))
    s.append(Paragraph("[unten am Rand, in anderer Stiftfarbe, kleiner]", S_SMALL))
    s.append(Paragraph("P.S. Donauzon nicht vergessen!! Plattformhaftung, DSA Art. 6 i.V.m. Art. 14 — Coty/Amazon Lehre.", S_INDIE))
    return s

story += blatt_av_handnotiz()
story.append(PageBreak())

# =====================================================================
# Abmahnung an Brezelmann (mehrere Seiten)
# =====================================================================
def blatt_abmahnung():
    s = briefkopf_steinacker()
    s.append(Spacer(1, 4))
    s.append(Paragraph("Per Einschreiben mit Rückschein <b>und</b> vorab per Telefax (07931/4 88 03)", S_SMALL))
    s.append(Spacer(1, 4))
    s.append(Paragraph(
        "Brezelmann Discount KG<br/>z.Hd. Herrn Geschäftsführer Dipl.-Kfm. Egon Brezelmann<br/>Wurstgasse 4<br/>97980 Bad Mergentheim",
        S_NORMAL_LEFT))
    s.append(Spacer(1, 10))
    s.append(Paragraph("München, 22. Januar 2026", S_RIGHT))
    s.append(Paragraph("Unser Az.: STK-IP/26/0117-KLÖ-ABM-01 · bitte stets angeben", S_RIGHT))
    s.append(Spacer(1, 10))
    s.append(Paragraph(
        "<b>Markenrechtliche Abmahnung mit Aufforderung zur Abgabe einer strafbewehrten Unterlassungserklärung</b>",
        S_H2))
    s.append(Paragraph(
        "in der Marken- und Wettbewerbsrechtssache<br/>"
        "<b>klôtzzkètté SA</b>, 12 rue du Faubourg Saint-Honoré, 75008 Paris (RCS Paris 552 094 471),<br/>"
        "<i>nachstehend &quot;Mandantin&quot;,</i><br/><br/>"
        "vertreten durch die Unterzeichnenden,<br/>"
        "<b>gegen</b><br/>"
        "Brezelmann Discount KG, Wurstgasse 4, 97980 Bad Mergentheim<br/>"
        "<i>nachstehend &quot;Abgemahnte&quot;,</i>",
        S_NORMAL_LEFT))
    s.append(Spacer(1, 8))
    s.append(Paragraph("Sehr geehrter Herr Brezelmann,", S_NORMAL_LEFT))
    s.append(Paragraph(
        "wir zeigen unter Vorlage einer auf uns lautenden Vollmacht (Anlage 1) an, dass die im Rubrum näher "
        "bezeichnete klôtzzkètté SA uns mit der Wahrnehmung ihrer rechtlichen Interessen in folgender Angelegenheit "
        "mandatiert hat. Wir bitten Sie, sich in dieser Sache <b>ausschließlich</b> an die Unterzeichnenden zu "
        "wenden.",
        S_NORMAL))
    s.append(Paragraph("<b>I. Sachverhalt</b>", S_H2))
    s.append(Paragraph(
        "Unsere Mandantin ist Inhaberin eines weltweit eingetragenen Markenportfolios, das u.a. die "
        "Wortmarke &quot;klôtzzkètté&quot; (DPMA 30 2008 044 117 sowie EUTM 005 412 880), die Wort-/Bildmarke "
        "&quot;klôtzzkètté + Krönchen-Monogramm K°°&quot; (EUTM 010 988 411), die 3D-Formmarke betreffend den "
        "hexagonalen Parfumflakon mit asymmetrischem Stopfen (EUTM 008 776 015), die Positionsmarke betreffend "
        "das goldene Krönchen-Insignium auf der linken Schuh-Innensohle Position 1 cm vom Fersenrand "
        "(EUTM 015 887 442), die Soundmarke EUTM 018 502 311, die Slogan-Marke "
        "&quot;LE LUXE EST UN DROIT NATUREL&quot; (EUTM 018 412 776) sowie die Bildmarke betreffend das "
        "silbern-emaillierte Krönchen-Logo (DPMA 30 2014 077 312) umfasst (zusammen: die <b>klôtzzkètté-Marken</b>).",
        S_NORMAL))
    s.append(Paragraph(
        "Die Mandantin ist seit 1923 in der Branche des Luxus-Sartoriale, der Haute Parfumerie und der Haute "
        "Maroquinerie tätig und genießt im relevanten Verkehrskreis eine ganz erhebliche Bekanntheit, die "
        "die Schwelle der Notorietät i.S.d. Art. 6<sup>bis</sup> PVÜ überschreitet.",
        S_NORMAL))
    s.append(Paragraph(
        "Am 27. Dezember 2025 stellte unsere Mandantin in Ihrer Filiale Bad Mergentheim, Wurstgasse 4, "
        "folgende Verletzungshandlungen fest:",
        S_NORMAL))
    items = [
        "Anbot, Bewerbung und Inverkehrbringen von T-Shirts mit der Aufschrift &quot;klötzkette&quot; (sic) "
        "in Klasse 25 zum Stückpreis von EUR 7,99;",
        "Anbot, Bewerbung und Inverkehrbringen von Parfumflakons, deren hexagonale Form mit asymmetrischem "
        "Stopfen die 3D-Formmarke EUTM 008 776 015 zumindest hochgradig nachschafft, unter der Bezeichnung "
        "&quot;Königsfräulein No. 5&quot; zum Stückpreis von EUR 12,99;",
        "Akustische Wiedergabe eines Jingles in den Verkaufsräumen, der die Soundmarke EUTM 018 502 311 "
        "zumindest in den prägenden Bestandteilen (Champagner-Schaum-Glissando, geflüsterte Phonetik der "
        "Wortmarke) nachschafft;",
        "Aushang eines Werbeplakates mit der Aufschrift &quot;Luxus ist ein Grundrecht&quot; — eine "
        "wortgetreue deutsche Übersetzung der Slogan-Marke EUTM 018 412 776 &quot;LE LUXE EST UN DROIT NATUREL&quot;.",
    ]
    for i, it in enumerate(items, 1):
        s.append(Paragraph(f"{i}. {it}", S_NORMAL))
    s.append(Paragraph(
        "Die Wahrnehmungen sind im Aktenvermerk vom 08.01.2026 (Bl. 7 ff. d.A.) ausführlich dokumentiert. "
        "Eine ergänzende Detektivobservation der Spuernase-Couture GmbH (Bericht vom 20.02.2026) bestätigt, "
        "dass die geschilderten Handlungen <b>nicht</b> auf die Filiale Bad Mergentheim beschränkt sind, sondern "
        "auch in den Filialen Crailsheim und Tauberbischofsheim sowie auf der Messe Pitti Uomo (Halle 7, Stand "
        "B-44, geplante Teilnahme 11.–14.03.2026) festzustellen sind.",
        S_NORMAL))
    return s

story += blatt_abmahnung()
story.append(PageBreak())

def blatt_abmahnung_p2():
    s = briefkopf_steinacker()
    s.append(Paragraph("(Fortsetzung Abmahnung vom 22.01.2026, Seite 2)", S_SMALL))
    s.append(Spacer(1, 6))
    s.append(Paragraph("<b>II. Rechtliche Würdigung</b>", S_H2))
    s.append(Paragraph(
        "Die vorstehend geschilderten Handlungen verletzen die klôtzzkètté-Marken in mehrfacher Hinsicht:",
        S_NORMAL))
    s.append(Paragraph("<b>1. Wortmarke</b>", S_H2))
    s.append(Paragraph(
        "Die Verwendung des Zeichens &quot;klötzkette&quot; auf T-Shirts der Klasse 25 stellt eine "
        "kennzeichenmäßige Benutzung i.S.d. § 14 Abs. 2 Nr. 2 MarkenG bzw. Art. 9 Abs. 2 lit. b) UMV dar. "
        "Die phonetische Identität, die hochgradige schriftbildliche Ähnlichkeit (Verzicht auf Akzente und "
        "Doppel-z stellen lediglich orthographische Marginalien dar) sowie die Warenidentität begründen eine "
        "Verwechslungsgefahr im engeren Sinne. Der Schutz erstreckt sich nach der gefestigten Rechtsprechung "
        "(EuGH C-251/95 Sabel, C-342/97 Lloyd, BGH GRUR 2009, 766 – Stofffähnchen) auf phonetisch, "
        "schriftbildlich und begrifflich ähnliche Zeichen, sofern sie für identische oder ähnliche Waren "
        "verwendet werden.",
        S_NORMAL))
    s.append(Paragraph(
        "Hinzu tritt der erweiterte Bekanntheitsschutz nach § 14 Abs. 2 Nr. 3 MarkenG bzw. Art. 9 Abs. 2 "
        "lit. c) UMV. Die Bekanntheit der klôtzzkètté-Marken im relevanten Verkehrskreis ist durch eine "
        "Allensbach-Umfrage 2023 (71,4 % ungestützte Markenkenntnis im qualifizierten Sample HHE&gt;EUR 250.000) "
        "umfassend belegt. Die Ausnutzung der Wertschätzung (sog. <i>free riding</i>) i.S.d. EuGH C-487/07 "
        "L'Oréal/Bellure liegt auf der Hand: Ein T-Shirt zu EUR 7,99 mit Anklang an &quot;klôtzzkètté&quot; "
        "lebt ersichtlich vom Aura-Transfer.",
        S_NORMAL))
    s.append(Paragraph("<b>2. 3D-Formmarke (Parfumflakon)</b>", S_H2))
    s.append(Paragraph(
        "Die hexagonale Karaffe mit asymmetrischem Stopfen ist als 3D-Formmarke EUTM 008 776 015 für die "
        "Klasse 3 eingetragen. Die durch unsere Mandantin bei der Brezelmann KG vorgefundenen Flakons sind "
        "in der ästhetischen Gesamtwirkung quasi-identisch; lediglich der Stopfen weicht in einer marginalen "
        "Neigung von 4° gegenüber dem 7°-Original ab. Eine markenmäßige Benutzung liegt vor (vgl. EuGH C-48/09 "
        "Lego), eine Verkehrsdurchsetzung der Form selbst ist im DPMA-Verfahren positiv beschieden worden.",
        S_NORMAL))
    s.append(Paragraph("<b>3. Soundmarke</b>", S_H2))
    s.append(Paragraph(
        "Die akustische Wiedergabe des Jingles &quot;klörrr-kettä&quot; mit Champagner-Schaum-Glissando und "
        "Eiswürfel-Klirren stellt eine kennzeichenmäßige Benutzung i.S.d. § 14 Abs. 2 Nr. 2 MarkenG dar. "
        "Die Eintragungsfähigkeit von Soundmarken ist durch EuGH C-283/01 Shield Mark anerkannt; die "
        "Rechtsbeständigkeit der Soundmarke EUTM 018 502 311 ist derzeit Gegenstand eines Rechtsbeschwerdeverfahrens "
        "vor dem BGH (I ZB 47/26); ein Hinweisbeschluss vom 06.04.2026 lässt die Aufrechterhaltung erwarten "
        "(vgl. mutatis mutandis BGH I ZB 22/20 &quot;Quadratisch Praktisch Gut&quot;).",
        S_NORMAL))
    s.append(Paragraph("<b>4. Slogan-Marke</b>", S_H2))
    s.append(Paragraph(
        "Die Verwendung des Werbeslogans &quot;Luxus ist ein Grundrecht&quot; stellt eine Übersetzung der "
        "Slogan-Marke EUTM 018 412 776 &quot;LE LUXE EST UN DROIT NATUREL&quot; dar. Die EuGH-Rechtsprechung "
        "zu fremdsprachigen Markenbenutzungen (vgl. C-421/13 Apple Store) sieht eine Übersetzung als "
        "ausreichende Markenbenutzung an, sofern der Aussagegehalt identisch bleibt. Dies ist hier der Fall.",
        S_NORMAL))
    s.append(Paragraph("<b>5. Positionsmarke</b>", S_H2))
    s.append(Paragraph(
        "(Hinsichtlich der Schuhwaren liegt bislang lediglich ein Hinweis aus dem Detektivbericht "
        "Spuernase-Couture vor, jedoch noch keine sichere Feststellung. Insoweit erfolgt Vorbehalt der "
        "Erweiterung des Abmahnungsgegenstandes.)",
        S_NORMAL))
    s.append(Paragraph("<b>6. Wettbewerbsrechtliche Annexansprüche</b>", S_H2))
    s.append(Paragraph(
        "Unbeschadet der markenrechtlichen Ansprüche treten Ansprüche aus §§ 3, 5 Abs. 2, 6 Abs. 2 Nr. 6 UWG "
        "wegen vermeidbarer Herkunftstäuschung und unlauterer vergleichender Werbung hinzu. Die "
        "Anspruchsgrundlagenkonkurrenz wird hier nicht weiter vertieft (vgl. BGH I ZR 110/19 – Schwarze "
        "Spitze).",
        S_NORMAL))
    return s

story += blatt_abmahnung_p2()
story.append(PageBreak())

def blatt_abmahnung_p3():
    s = briefkopf_steinacker()
    s.append(Paragraph("(Fortsetzung Abmahnung vom 22.01.2026, Seite 3)", S_SMALL))
    s.append(Spacer(1, 6))
    s.append(Paragraph("<b>III. Aufforderung</b>", S_H2))
    s.append(Paragraph(
        "Vor diesem Hintergrund fordern wir Sie hiermit auf, bis spätestens",
        S_NORMAL))
    s.append(Paragraph("<b>Donnerstag, 05. Februar 2026, 18:00 Uhr</b>", S_CENTER))
    s.append(Paragraph(
        "die in Anlage 2 beigefügte Unterlassungs- und Verpflichtungserklärung strafbewehrt zu unterzeichnen "
        "und an die Unterzeichnenden zurückzusenden.",
        S_NORMAL))
    s.append(Paragraph(
        "Wir weisen darauf hin, dass die in Anlage 2 vorgesehene Vertragsstrafe in Höhe von EUR 25.001,00 "
        "je Verstoß nach den Maßstäben der Hamburger Brauch-Klausel sowie unter Berücksichtigung der "
        "BGH-Rechtsprechung I ZR 35/19 angemessen ist. Bei mehrfachen, geographisch versprengten Verstößen "
        "wird die Vertragsstrafe je Filiale und Anbietens-Vorgang ausgelöst.",
        S_NORMAL))
    s.append(Paragraph(
        "Für den Fall des fruchtlosen Verstreichens der Frist behalten wir uns ausdrücklich vor, ohne weitere "
        "Ankündigung eine einstweilige Verfügung — voraussichtlich vor dem LG Frankfurt am Main, Kammer für "
        "Markensachen, hilfsweise vor dem LG München I — zu erwirken sowie die Hauptsacheklage anzustrengen. "
        "Strafanzeige gem. § 143 MarkenG bleibt vorbehalten.",
        S_NORMAL))
    s.append(Paragraph("<b>IV. Kosten</b>", S_H2))
    s.append(Paragraph(
        "Die Kosten dieser Abmahnung bemessen sich nach einem Gegenstandswert von EUR 1.500.000,00 "
        "(begründet durch das Volumen der streitgegenständlichen Marken und das gewerbsmäßige Vorgehen). "
        "Die Geschäftsgebühr nach Nr. 2300 VV-RVG (1,8) beläuft sich somit auf EUR 11.682,00 zzgl. "
        "Auslagenpauschale EUR 20,00 sowie 19 % USt., insgesamt EUR 13.925,58. Wir bitten um Zahlung auf "
        "unser Anderkonto bei der Bayerischen LB (IBAN DE17 7005 0000 0815 1234 56) binnen der "
        "vorgenannten Frist.",
        S_NORMAL))
    s.append(Paragraph("<b>V. Schlussbemerkung</b>", S_H2))
    s.append(Paragraph(
        "Sollten Sie unsere Mandantin als Inhaberin einer renommierten und seit nunmehr 103 Jahren bestehenden "
        "Maison de Luxe nicht angemessen würdigen, wird das Verfahren mit allem gebotenen Nachdruck geführt "
        "werden. Wir empfehlen Ihnen dringend, sich umgehend anwaltlich vertreten zu lassen.",
        S_NORMAL))
    s.append(Spacer(1, 14))
    s.append(Paragraph("Mit freundlichen Grüßen", S_NORMAL_LEFT))
    s.append(Spacer(1, 24))
    s.append(Paragraph("<b>Dr. Dr. Annabella Steinacker-von Tarsis, LL.M. (Cantab.)</b><br/>"
                       "Rechtsanwältin · Fachanwältin für gewerblichen Rechtsschutz · Partnerin",
                       S_NORMAL_LEFT))
    s.append(Spacer(1, 10))
    s.append(Paragraph(
        "<b>Anlagen:</b><br/>"
        "Anlage 1 — Vollmacht klôtzzkètté SA<br/>"
        "Anlage 2 — Strafbewehrte Unterlassungs- und Verpflichtungserklärung (Entwurf, 4 Seiten)<br/>"
        "Anlage 3 — Markenregisterauszüge K-01 bis K-07 (39 Seiten, ggf. nur Inhaltsverzeichnis)<br/>"
        "Anlage 4 — Lichtbildmaterial Filiale Bad Mergentheim (12 Aufnahmen)",
        S_SMALL))
    return s

story += blatt_abmahnung_p3()
story.append(PageBreak())

# =====================================================================
# Anlage 2 — Unterlassungserklärung (1 Seite)
# =====================================================================
def blatt_uerklärung():
    s = []
    s.append(Paragraph("<b>Anlage 2 zur Abmahnung vom 22.01.2026</b>", S_SMALL))
    s.append(Spacer(1, 6))
    s.append(Paragraph("Strafbewehrte Unterlassungs- und Verpflichtungserklärung", S_H1))
    s.append(Paragraph(
        "Die Brezelmann Discount KG, vertreten durch den Geschäftsführer Dipl.-Kfm. Egon Brezelmann, "
        "Wurstgasse 4, 97980 Bad Mergentheim, verpflichtet sich hiermit ohne Anerkennung einer "
        "Rechtspflicht, gleichwohl rechtsverbindlich, gegenüber der klôtzzkètté SA, Paris,",
        S_NORMAL))
    s.append(Paragraph("<b>1.</b> es zu unterlassen, im geschäftlichen Verkehr", S_NORMAL))
    for pt in [
        "a) das Zeichen &quot;klötzkette&quot; oder phonetisch, schriftbildlich oder begrifflich verwechselbar ähnliche Zeichen für Waren der Klasse 25 (Bekleidung, Schuhwaren, Kopfbedeckungen) anzubieten, zu bewerben oder zu vertreiben;",
        "b) Parfumflakons in der Form einer hexagonalen Karaffe mit asymmetrischem Stopfen, deren Stopfenwinkel weniger als 12° vom Vertikalen abweicht, für Waren der Klasse 3 anzubieten, zu bewerben oder zu vertreiben;",
        "c) Tonaufnahmen oder Tonzeichen, die eine Folge aus geknickter Glaskarosserie (Champagner-Schaum-Glissando), Eiswürfel-Klirren und geflüsterter Frauenstimme enthalten, in Verkaufs- oder Werberäumen wiederzugeben, sofern diese Tonzeichen dem Klangbild der EUTM 018 502 311 wesentlich ähneln;",
        "d) den Werbeslogan &quot;Luxus ist ein Grundrecht&quot; oder gleichbedeutende fremdsprachige Übersetzungen für Waren der Klassen 25 und 35 zu verwenden;",
    ]:
        s.append(Paragraph(pt, S_NORMAL))
    s.append(Paragraph(
        "<b>2.</b> für jeden Fall der Zuwiderhandlung gegen die unter 1. übernommenen Verpflichtungen an die "
        "klôtzzkètté SA eine Vertragsstrafe in Höhe von <b>EUR 25.001,00</b> zu zahlen, deren angemessene Höhe "
        "im Streitfall vom zuständigen Gericht zu überprüfen ist (sog. Hamburger Brauch).",
        S_NORMAL))
    s.append(Paragraph(
        "<b>3.</b> der klôtzzkètté SA umfassend Auskunft zu erteilen über Art und Umfang der Verletzungshandlungen "
        "i.S.v. Ziff. 1, insbesondere über Lieferanten, Liefermengen, Verkaufspreise, Verkaufszahlen, "
        "Werbeaufwand und Bruttoumsatz.",
        S_NORMAL))
    s.append(Paragraph(
        "<b>4.</b> der klôtzzkètté SA jeden hieraus entstandenen Schaden zu ersetzen.",
        S_NORMAL))
    s.append(Paragraph(
        "<b>5.</b> die Kosten der außergerichtlichen Rechtsverfolgung (EUR 13.925,58) zu erstatten.",
        S_NORMAL))
    s.append(Spacer(1, 30))
    s.append(Paragraph("Ort, Datum: ____________________________", S_NORMAL_LEFT))
    s.append(Spacer(1, 16))
    s.append(Paragraph("Unterschrift: ____________________________  (Egon Brezelmann, Geschäftsführer)", S_NORMAL_LEFT))
    s.append(Spacer(1, 6))
    s.append(Paragraph("Firmenstempel:", S_NORMAL_LEFT))
    s.append(Spacer(1, 80))
    s.append(Paragraph("<i>[Hinweis Sekretariat: an dieser Stelle wurde im Original ein blauer Firmenstempel der Brezelmann KG aufgebracht; siehe Bl. 19 d.A. — Fax-Rücklauf.]</i>", S_SMALL))
    return s

story += blatt_uerklärung()
story.append(PageBreak())

# =====================================================================
# Notizzettel (handschriftlich) zur Abmahnung
# =====================================================================
def blatt_handnotiz_short():
    s = []
    s.append(Spacer(1, 40))
    s.append(Paragraph("Post-It Steinacker, 23.01.2026", S_SMALL))
    s.append(Spacer(1, 10))
    s.append(Paragraph("Brezelmann wird heulen.", S_HAND_BIG))
    s.append(Spacer(1, 6))
    s.append(Paragraph("Egon ist kein Volljurist. Er ruft Schwager an (Notar in Künzelsau).", S_HAND))
    s.append(Spacer(1, 4))
    s.append(Paragraph("Schwager ist KEIN Markenrechtler!! Riesenvorteil für uns.", S_HAND))
    s.append(Spacer(1, 4))
    s.append(Paragraph("Erwartung: Brezelmann wird die UE NICHT unterschreiben — sondern albernes Fax schicken.", S_HAND))
    s.append(Spacer(1, 4))
    s.append(Paragraph("Dann eV-Antrag rauf! Streitwert &gt;= 2 Mio.", S_HAND))
    s.append(Spacer(1, 30))
    s.append(Paragraph("— A.S.", S_HAND))
    s.append(Spacer(1, 80))
    s.append(Paragraph("[Eingeklebt: zweites Post-It, gelb, andere Schrift]", S_SMALL))
    s.append(Paragraph("Annabella — Comtesse hat angerufen, will Update auf Französisch. Bitte heute noch! — Wenzel-Hugenberg", S_INDIE))
    return s

story += blatt_handnotiz_short()
story.append(PageBreak())

# =====================================================================
# E-Mail-Kette Comtesse ./. Steinacker (3 pages)
# =====================================================================
def email_block(frm, to, cc, date, subject, body, signature=""):
    """Return a list of flowables for one email."""
    s = []
    header = (f"From:    {frm}\n"
              f"To:      {to}\n")
    if cc:
        header += f"Cc:      {cc}\n"
    header += (f"Date:    {date}\n"
               f"Subject: {subject}\n")
    s.append(Preformatted(header, S_MONO_SMALL))
    s.append(HLine(thickness=0.3, space_after=2, space_before=2))
    s.append(Preformatted(body, S_MONO_SMALL))
    if signature:
        s.append(Preformatted(signature, S_MONO_SMALL))
    s.append(Spacer(1, 6))
    s.append(HLine(thickness=0.6, color=colors.HexColor("#aaaaaa"), space_after=4, space_before=4))
    return s

def blatt_email_comtesse_1():
    s = []
    s.append(Paragraph("E-Mail-Kette &quot;Béatrice ./. Steinacker&quot; — Band I (24.01. – 05.02.2026)", S_H1))
    s.append(Paragraph("[Heftung gemäß Eingang im Sekretariat; vollständige Wiedergabe inkl. Header]", S_SMALL))
    s.append(Spacer(1, 6))
    s += email_block(
        "Béatrice de Klôtzzkètté-Visconti <bdkv@klotzzkette.com>",
        "Annabella Steinacker-von Tarsis <steinacker@steinacker-ip.de>",
        "Marc-Antoine Dufresne <ma.dufresne@klotzzkette.com>",
        "Sat, 24 Jan 2026 09:14:22 +0100",
        "Brezelmann — Abmahnung versandt — bonne nouvelle",
        "Madame, chère Annabella,\n\n"
        "j'espère que ce courriel vous trouve en bonne santé. Marc-Antoine\n"
        "m'a informée que la lettre de mise en demeure (Abmahnung) a bien\n"
        "été envoyée hier soir par fax et lettre recommandée. Excellent\n"
        "travail.\n\n"
        "Je voudrais juste m'assurer d'une chose: le montant de la peine\n"
        "contractuelle (Vertragsstrafe) — EUR 25.001 — est-il vraiment\n"
        "suffisant? Cela me semble dérisoire pour une affaire de cette\n"
        "envergure. Mon arrière-grand-père aurait demandé 100.000 Reichsmark\n"
        "(rires).\n\n"
        "Cordialement,\n\n"
        "B. de K.-V.\n"
        "_________________________________________________\n"
        "Comtesse Béatrice de Klôtzzkètté-Visconti\n"
        "Présidente du Conseil — klôtzzkètté SA, Paris/Milano\n"
        "12 rue du Faubourg Saint-Honoré, 75008 Paris\n"
        "+33 1 42 60 88 14  ·  bdkv@klotzzkette.com\n"
    )
    s += email_block(
        "Annabella Steinacker-von Tarsis <steinacker@steinacker-ip.de>",
        "Béatrice de Klôtzzkètté-Visconti <bdkv@klotzzkette.com>",
        "Marc-Antoine Dufresne; Maximilian v. Brenkenhoff",
        "Sat, 24 Jan 2026 11:42:08 +0100",
        "AW: Brezelmann — Abmahnung versandt — bonne nouvelle",
        "Madame la Comtesse,\n\n"
        "vielen Dank für Ihre Nachricht. Der Betrag von EUR 25.001 ist nach\n"
        "deutschem Recht der ueblicher Standard fuer den sog. &quot;Hamburger\n"
        "Brauch&quot; und wird je Einzelverstoss faellig. Bei einer Vielzahl\n"
        "von Verstoessen (jede Filiale, jeder Anbietens-Vorgang) summiert\n"
        "sich dies sehr schnell. Wir rechnen mit Brezelmann konservativ mit\n"
        "ca. 38 separaten Verletzungshandlungen, also potenziell\n"
        "EUR 950.000 allein aus der Vertragsstrafenklausel.\n\n"
        "Hinzu treten Schadensersatz nach Lizenzanalogie sowie Auskunft.\n"
        "Wir rechnen mit einem Gesamtvolumen, das EUR 4–5 Mio. nicht\n"
        "unterschreiten wird.\n\n"
        "Mit verbindlichen Gruessen\n"
        "Dr. Dr. Annabella Steinacker-von Tarsis, LL.M. (Cantab.)\n"
        "Partnerin · Steinacker · Lichtenberg & Partners\n"
    )
    return s

story += blatt_email_comtesse_1()
story.append(PageBreak())

def blatt_email_comtesse_2():
    s = []
    s.append(Paragraph("E-Mail-Kette &quot;Béatrice ./. Steinacker&quot; — Band I, Fortsetzung", S_H2))
    s.append(Spacer(1, 4))
    s += email_block(
        "Béatrice de Klôtzzkètté-Visconti <bdkv@klotzzkette.com>",
        "Annabella Steinacker-von Tarsis <steinacker@steinacker-ip.de>",
        "",
        "Wed, 29 Jan 2026 18:53:11 +0100",
        "URGENT — Fax de Brezelmann — INCROYABLE",
        "Annabella,\n\n"
        "je viens de recevoir copie du fax que ce monsieur Brezelmann\n"
        "vous a envoye. Il est d'une vulgarite, d'une crapulerie, d'une\n"
        "ignorance crasse qui depasse l'entendement!! Il ose ecrire que\n"
        "&quot;wir verkaufen schon seit Jahren T-Shirts und niemand hat sich\n"
        "beschwert&quot; — comme si cela constituait un argument!! \n\n"
        "Et il signe avec une faute d'orthographe a son propre nom\n"
        "(&quot;Brezelmann&quot; avec deux &quot;n&quot; sur la signature, un seul sur\n"
        "le entete) — quel niveau de discount!!!\n\n"
        "Je vous prie de demarrer la procedure d'eV IMMEDIATEMENT. Pas\n"
        "de quartier. Pas de mercie. Je veux la tete de ce monsieur sur\n"
        "un plateau d'argent et je veux que cela se passe a Pitti Uomo\n"
        "devant tout le monde, devant Loro Piana, devant Brunello\n"
        "Cucinelli, devant tout Florence!\n\n"
        "B. de K.-V.\n\n"
        "P.S. Marc-Antoine veut faire une analyse cost-benefit. Dites-lui\n"
        "que la dignite n'a pas de prix. C'est une question d'honneur,\n"
        "pas de comptabilite.\n"
    )
    s += email_block(
        "Annabella Steinacker-von Tarsis <steinacker@steinacker-ip.de>",
        "Béatrice de Klôtzzkètté-Visconti <bdkv@klotzzkette.com>",
        "Maximilian v. Brenkenhoff",
        "Thu, 30 Jan 2026 08:11:54 +0100",
        "AW: URGENT — Fax de Brezelmann — INCROYABLE",
        "Madame la Comtesse,\n\n"
        "ich habe Ihre Nachricht zur Kenntnis genommen. Der Fax-Antwort\n"
        "des Herrn Brezelmann liegt eine Schutzschriftenpruefung vor; das\n"
        "Schutzschriftenregister Hessen weist keine Eintragung der Brezelmann\n"
        "Discount KG aus (Stand 30.01.2026, 08:00 Uhr).\n\n"
        "Wir bereiten die Antragsschrift einer einstweiligen Verfuegung\n"
        "vor dem LG Frankfurt am Main vor und werden diese voraussichtlich\n"
        "in der zweiten Maerzwoche bei Gericht einreichen — abgestimmt auf\n"
        "den Beginn der Messe Pitti Uomo am 11. Maerz, damit die Vollziehung\n"
        "vor Ort durch den italienischen Gerichtsvollzieher (via Rechtshilfe-\n"
        "ersuchen) noch waehrend der Messe erfolgen kann. Dies ist taktisch\n"
        "von erheblicher Bedeutung — Pitti Uomo ist der wichtigste Termin\n"
        "des Brezelmann-Geschaeftsjahres.\n\n"
        "Bezueglich der Tete sur le plateau — wir bevorzugen die juristisch\n"
        "praezisere Variante: Beschlagnahme der Verletzungsware unter\n"
        "Hinzuziehung der Carabinieri. Visuell ist die Wirkung mindestens\n"
        "ebenso eindrucksvoll, rechtlich indes sauber.\n\n"
        "Mit ergebensten Gruessen\n"
        "A.S.\n"
    )
    s += email_block(
        "Béatrice de Klôtzzkètté-Visconti <bdkv@klotzzkette.com>",
        "Annabella Steinacker-von Tarsis <steinacker@steinacker-ip.de>",
        "",
        "Thu, 30 Jan 2026 09:02:17 +0100",
        "AW: AW: URGENT — Fax de Brezelmann",
        "Parfait. Les Carabiniers. C'est mieux. Plus theatral.\n\n"
        "B."
    )
    return s

story += blatt_email_comtesse_2()
story.append(PageBreak())

def blatt_email_comtesse_3():
    s = []
    s.append(Paragraph("E-Mail-Kette &quot;Béatrice ./. Steinacker&quot; — Band I, Fortsetzung (Schluss)", S_H2))
    s.append(Spacer(1, 4))
    s += email_block(
        "Béatrice de Klôtzzkètté-Visconti <bdkv@klotzzkette.com>",
        "Annabella Steinacker-von Tarsis <steinacker@steinacker-ip.de>",
        "Marc-Antoine Dufresne",
        "Wed, 05 Feb 2026 23:47:09 +0100",
        "Donauzon — INADMISSIBLE — j'ai trouve des t-shirts en ligne!!!",
        "ANNABELLA!!!\n\n"
        "Je viens de regarder Donauzon sur mon iPad — il y a des T-SHIRTS\n"
        "&quot;Klötzkette&quot; en VENTE en ce moment meme, EUR 9,99,\n"
        "livraison gratuite!!! Vendeur: &quot;Brezelmann_outlet_official&quot;,\n"
        "verifie depuis 2019!! 4,2 etoiles!! 1.847 avis dont 89 % positifs!!\n\n"
        "Comment est-ce possible que Donauzon, qui est une plateforme\n"
        "Soi-Disant Premium, tolere cela?? Ce n'est pas seulement Brezelmann\n"
        "le voleur — c'est aussi Donauzon le complice!!\n\n"
        "Je vous prie d'inclure Donauzon Marketplace GmbH dans la procedure.\n"
        "Coty/Akzente, vous savez bien — un site de vente ne peut pas faire\n"
        "ce qu'il veut. Et j'ai lu quelque chose sur DSA Article 6 — la\n"
        "responsabilite des plateformes. Marc-Antoine vous transmettra\n"
        "les captures d'ecran demain matin.\n\n"
        "Je ne dormirai pas cette nuit.\n\n"
        "Beatrice\n\n"
        "P.S. Et j'ai aussi vu un compte litanien qui s'appelle &quot;klotzkettie&quot;\n"
        "— un seul z, deux e a la fin. C'est encore un autre escroc! Eux\n"
        "aussi: poursuites!!!\n"
    )
    s += email_block(
        "Annabella Steinacker-von Tarsis <steinacker@steinacker-ip.de>",
        "Béatrice de Klôtzzkètté-Visconti <bdkv@klotzzkette.com>",
        "Marc-Antoine Dufresne; Maximilian v. Brenkenhoff",
        "Thu, 06 Feb 2026 06:43:38 +0100",
        "AW: Donauzon — INADMISSIBLE — Strategie",
        "Madame la Comtesse,\n\n"
        "ich habe Ihre Nachricht um 6:00 Uhr morgens zur Kenntnis genommen\n"
        "(wir haben Familie eines Mandanten in CH, daher fruh wach).\n\n"
        "1. Donauzon: Wir erweitern den Antrag der eV auf die Donauzon\n"
        "Marketplace GmbH (Sitz Luxembourg, Niederlassung Erdbeerallee 88,\n"
        "80807 Muenchen). Anspruchsgrundlage: § 14 Abs. 2 MarkenG i.V.m.\n"
        "der Coty-Rechtsprechung (EuGH C-567/18 Coty Germany ./. Amazon),\n"
        "wonach Plattformbetreiber bei aktivem Auftritt — und Donauzon ist\n"
        "schon aufgrund &quot;Fulfilment by Donauzon&quot; (FBD) aktiv — als\n"
        "Mittaeter haften.\n\n"
        "2. DSA Art. 6: Ihre Beobachtung ist scharfsinnig. Art. 6 DSA gibt\n"
        "der Plattform zwar ein Privileg, jedoch nur bei &quot;mere conduit&quot;.\n"
        "Sobald die Plattform Kenntnis hat — und ein Notice-and-Action-\n"
        "Verfahren mit Brezelmann lief bereits seit 09/2025 — entfaellt das\n"
        "Privileg. Wir bauen das in die Antragsschrift ein.\n\n"
        "3. &quot;klotzkettie&quot; Litauen: bereits in Vorbereitung. Widerspruchsschrift\n"
        "vor EUIPO Alicante wird unter B 4 187 932 anhaengig gemacht; die\n"
        "Frist laeuft am 24.02.2026 ab. Wir liefern rechtzeitig.\n\n"
        "Bitte schlafen Sie. Sie haben uns beauftragt; wir tun das Noetige.\n\n"
        "A.S.\n"
    )
    s.append(Paragraph("<i>[Hinweis Sekretariat: weitere Mails der Kette in Band II der E-Mail-Heftung, Bl. 76 ff. d.A.]</i>", S_SMALL))
    return s

story += blatt_email_comtesse_3()
story.append(PageBreak())

# =====================================================================
# Fax Brezelmann
# =====================================================================
def blatt_fax_brezelmann():
    s = []
    s.append(FaxHeader(
        sender="Brezelmann Discount KG · Wurstgasse 4 · 97980 Bad Mergentheim",
        recipient="Steinacker Lichtenberg & Partners · München",
        date="29.01.2026  10:47 Uhr",
        fax_nr="089 / 24 21 88 - 99",
        pages="2 von 2"))
    s.append(Spacer(1, 8))
    s.append(Paragraph("<b>BREZELMANN DISCOUNT KG</b>", S_CENTER))
    s.append(Paragraph("&quot;DER PREIS PASST IMMER&quot;", S_CENTER))
    s.append(HLine(thickness=0.4))
    s.append(Spacer(1, 6))
    fax_body = (
        "An die\n"
        "Anwaltskanzlei Steinacker und Lichtenberg in Muenchen\n"
        "z.Hd. Frau Doktor Doktor Steinacker\n\n"
        "Sehr geehrte Frau Doktor Doktor!\n\n"
        "Wir haben Ihren langen Brief vom 22.01. erhalten. Ich muss sagen,\n"
        "wir sind RICHTIG ERSTAUNT. Wir verkaufen schon seit Jahren T-Shirts\n"
        "und niemand hat sich beschwert. Die Aufschrift &quot;Klötzkette&quot;\n"
        "ist ein deutsches Wort und kann nicht einer franzoesischen Firma\n"
        "gehoeren!! Eine KLÖTZKETTE ist eine Kette aus Klötzen, das hat\n"
        "schon mein Großvater Wilhelm Brezelmann (gegruendet 1934) so\n"
        "verstanden. Wir haben sogar im Wahrig nachgeschaut.\n\n"
        "Auch die Parfumflaschen sind keine Kopien sondern es handelt sich\n"
        "um eine SECHSECKIGE Flasche, die ist seit der Antike bekannt\n"
        "(z.B. Roemerzeit, Spessart-Glashuette). Da kann niemand drauf\n"
        "&quot;Marke&quot; sagen.\n\n"
        "Das Lied im Laden ist auch nicht Ihr Lied. Wir lassen das von\n"
        "unserer Marketingfirma DJ Tobi aus Wuerzburg machen, nicht von\n"
        "klotzzkette. Tobi spielt das Krachen mit einer Bierdose, nicht\n"
        "Sektflasche. Sie sehen also: ALLES ANDERS.\n\n"
        "Hiermit erklaert die Brezelmann Discount KG ausdruecklich, dass\n"
        "wir die Unterlassungserklaerung NICHT unterschreiben werden, weil\n"
        "wir nichts falsch gemacht haben. Auch die 13.925,58 Euro werden\n"
        "wir NICHT bezahlen, das waere eine Frechheit.\n\n"
        "Wir bitten um Verstaendnis und verbleiben\n\n"
        "mit freundlichen Gruessen\n\n"
        "Egon Brezelmann\n"
        "Geschaeftsfuehrer\n"
        "(Dipl.-Kfm., FH Heilbronn 1989)\n\n"
        "P.S.: Mein Schwager, der ist Notar in Kuenzelsau, hat sich das\n"
        "auch angeschaut und sagt, das ist alles &quot;voellig uebertrieben&quot;.\n"
    )
    s.append(Preformatted(fax_body, S_MONO))
    s.append(Spacer(1, 6))
    s.append(HoleStrip())
    s.append(Paragraph("<i>[Original-Fax-Eingang Telefax-Server 29.01.2026 10:47:33 — Auflösung 200×100 dpi — Schriftbild leicht versetzt — manuelle Transkription d. Sekretariats]</i>", S_SMALL))
    return s

story += blatt_fax_brezelmann()
story.append(PageBreak())

# =====================================================================
# Antragsschrift einstweilige Verfügung — mehrere Seiten
# =====================================================================
def blatt_ev_antrag_1():
    s = briefkopf_steinacker()
    s.append(Spacer(1, 4))
    s.append(Paragraph("Per beA und vorab per Telefax", S_SMALL))
    s.append(Spacer(1, 4))
    s.append(Paragraph(
        "Landgericht Frankfurt am Main<br/>Kammer für Markensachen<br/>Konrad-Adenauer-Straße 20<br/>60313 Frankfurt am Main",
        S_NORMAL_LEFT))
    s.append(Spacer(1, 10))
    s.append(Paragraph("München, 11. März 2026", S_RIGHT))
    s.append(Paragraph("Unser Az.: STK-IP/26/0117-KLÖ-eV-01", S_RIGHT))
    s.append(Spacer(1, 10))
    s.append(Paragraph(
        "in der einstweiligen Verfügungssache",
        S_H2))
    s.append(Paragraph(
        "<b>klôtzzkètté SA</b>, 12 rue du Faubourg Saint-Honoré, 75008 Paris, Frankreich,<br/>"
        "vertreten durch ihre Präsidentin des Verwaltungsrates Mme la Comtesse Béatrice de "
        "Klôtzzkètté-Visconti,<br/>"
        "<i>— Antragstellerin —</i><br/><br/>"
        "Prozessbevollmächtigte:<br/>"
        "Steinacker · Lichtenberg &amp; Partners IP Boutique, Maximiliansplatz 19, 80333 München",
        S_NORMAL_LEFT))
    s.append(Spacer(1, 6))
    s.append(Paragraph("<b>gegen</b>", S_CENTER))
    s.append(Spacer(1, 4))
    s.append(Paragraph(
        "1. <b>Brezelmann Discount KG</b>, Wurstgasse 4, 97980 Bad Mergentheim, vertreten durch den "
        "persönlich haftenden Gesellschafter Dipl.-Kfm. Egon Brezelmann,<br/>"
        "<i>— Antragsgegnerin zu 1 —</i><br/><br/>"
        "2. <b>Donauzon Marketplace GmbH</b>, Tour Trintignant, 2540 Luxembourg, Niederlassung "
        "Deutschland Erdbeerallee 88, 80807 München, vertreten durch ihre Geschäftsführer,<br/>"
        "<i>— Antragsgegnerin zu 2 —</i>",
        S_NORMAL_LEFT))
    s.append(Spacer(1, 10))
    s.append(Paragraph(
        "<b>wegen:</b> Unterlassung markenrechtsverletzender Handlungen (§§ 14, 19, 19a MarkenG; Art. 9, 102, 130 UMV)<br/>"
        "<b>Streitwert vorläufig:</b> EUR 2.400.000,00",
        S_NORMAL_LEFT))
    s.append(Spacer(1, 8))
    s.append(Paragraph("erhebe ich namens und im Auftrag der Antragstellerin", S_NORMAL))
    s.append(Paragraph("<b>ANTRAG AUF ERLASS EINER EINSTWEILIGEN VERFÜGUNG</b>", S_CENTER))
    s.append(Paragraph("und beantrage,", S_NORMAL))
    s.append(Paragraph(
        "<b>I.</b> der Antragsgegnerin zu 1 zu untersagen, im geschäftlichen Verkehr ohne Zustimmung der "
        "Antragstellerin in der Bundesrepublik Deutschland und auf dem Gebiet der Europäischen Union",
        S_NORMAL))
    for pt in [
        "a) das Zeichen &quot;klötzkette&quot; oder phonetisch verwechselbar ähnliche Zeichen für Bekleidungsstücke, insbesondere T-Shirts, anzubieten, zu bewerben oder zu vertreiben;",
        "b) Parfumflakons in der Form einer hexagonalen Karaffe mit asymmetrischem Stopfen anzubieten, zu bewerben oder zu vertreiben, sofern der Stopfenwinkel weniger als 12° vom Vertikalen abweicht;",
        "c) den Slogan &quot;Luxus ist ein Grundrecht&quot; oder die französische Originalfassung &quot;LE LUXE EST UN DROIT NATUREL&quot; für Waren der Klassen 25 und 35 zu verwenden;",
        "d) Handtaschen mit dem Krönchen-Monogramm K°° oder mit verwechselbar ähnlichen Aufdrucken anzubieten;",
        "e) Tonsequenzen abzuspielen, die der Soundmarke EUTM 018 502 311 in den prägenden Bestandteilen wesentlich ähneln;",
    ]:
        s.append(Paragraph(pt, S_NORMAL))
    s.append(Paragraph(
        "<b>II.</b> der Antragsgegnerin zu 2 aufzugeben, sämtliche Listings der Antragsgegnerin zu 1 (Verkäufer-"
        "konto &quot;brezelmann_outlet_official&quot;, Verkäufer-ID 1.847.221.984) sowie aller weiteren Drittanbieter, "
        "die in der Listingbeschreibung das Zeichen &quot;klötzkette&quot;, &quot;klotzzkettä&quot;, "
        "&quot;klotzketie&quot; oder &quot;Krönchen K°°&quot; verwenden, binnen 24 Stunden ab Zustellung dieses Beschlusses "
        "von der Plattform donauzon.de und allen weiteren Donauzon-EU-Domains zu entfernen und entfernt zu halten;",
        S_NORMAL))
    s.append(Paragraph(
        "<b>III.</b> für jeden Fall der Zuwiderhandlung gegen die unter I. und II. ausgesprochenen Verpflichtungen "
        "Ordnungsgeld bis zu EUR 250.000,00, ersatzweise Ordnungshaft, oder Ordnungshaft bis zu 6 Monaten "
        "anzudrohen, zu vollziehen an den jeweiligen Geschäftsführern;",
        S_NORMAL))
    s.append(Paragraph(
        "<b>IV.</b> die Antragsgegnerinnen als Gesamtschuldnerinnen die Kosten des Verfahrens aufzuerlegen;",
        S_NORMAL))
    s.append(Paragraph(
        "<b>V.</b> die einstweilige Verfügung ohne mündliche Verhandlung gem. § 937 Abs. 2 ZPO zu erlassen.",
        S_NORMAL))
    return s

story += blatt_ev_antrag_1()
story.append(PageBreak())

def blatt_ev_antrag_2():
    s = briefkopf_steinacker()
    s.append(Paragraph("(Fortsetzung Antrag eV LG Frankfurt 11.03.2026 — Seite 2)", S_SMALL))
    s.append(Spacer(1, 6))
    s.append(Paragraph("<b>Begründung</b>", S_H1))
    s.append(Paragraph("<b>A. Sachverhalt</b>", S_H2))
    s.append(Paragraph("<b>I. Antragstellerin</b>", S_H2))
    s.append(Paragraph(
        "Die Antragstellerin wurde im Jahr 1923 in Paris von Antoine-Louis Klôtzzkètté gegründet und ist seit "
        "drei Generationen — heute in der vierten Generation — im Familienbesitz der Familie de Klôtzzkètté"
        "-Visconti. Sie betreibt unter der Marke &quot;klôtzzkètté&quot; ein streng selektiv vertriebenes "
        "Sortiment hochwertiger Mode-, Lederwaren-, Schmuck- und Parfumartikel. Der Jahresumsatz 2025 betrug "
        "EUR 218,4 Mio. (geprüft KPMG Paris). Die Marke gilt nach allgemeinem Verständnis als Inbegriff "
        "europäischer Boutique-Eleganz und genießt im qualifizierten Verkehrskreis (HHE &gt; EUR 250.000) eine "
        "ungestützte Markenkenntnis von 71,4 % (Allensbach 2023, Glaubhaftmachungsmittel 1).",
        S_NORMAL))
    s.append(Paragraph(
        "Die Antragstellerin ist Inhaberin der im Markenportfolio (Glaubhaftmachungsmittel 2) aufgeführten "
        "Schutzrechte, insbesondere der Wortmarke &quot;klôtzzkètté&quot; (DPMA 30 2008 044 117 / EUTM 005 412 880), "
        "der Wort-/Bildmarke &quot;klôtzzkètté + K°°&quot; (EUTM 010 988 411), der 3D-Formmarke "
        "EUTM 008 776 015 (hexagonaler Flakon), der Soundmarke EUTM 018 502 311 sowie der Slogan-Marke "
        "EUTM 018 412 776.",
        S_NORMAL))
    s.append(Paragraph("<b>II. Antragsgegnerin zu 1: Brezelmann Discount KG</b>", S_H2))
    s.append(Paragraph(
        "Die Antragsgegnerin zu 1 betreibt eine Kette von 41 Discount-Filialen in den Bundesländern Baden-"
        "Württemberg und Bayern (Schwerpunkt Tauberfranken). Sie ist im Handelsregister des Amtsgerichts Bad "
        "Mergentheim unter HRA 4112 eingetragen. Geschäftszweck ausweislich des Handelsregisters: &quot;An- und "
        "Verkauf von Restposten aller Art, insbesondere Bekleidung, Lebensmittel und Haushaltswaren&quot;.",
        S_NORMAL))
    s.append(Paragraph("<b>III. Antragsgegnerin zu 2: Donauzon Marketplace GmbH</b>", S_H2))
    s.append(Paragraph(
        "Die Antragsgegnerin zu 2 betreibt unter der Domain donauzon.de (sowie weiteren EU-Domains) einen "
        "Online-Marktplatz, auf dem Drittanbieter ihre Waren verkaufen können. Sie unterhält ein "
        "&quot;Fulfilment by Donauzon&quot;-Programm (FBD), in dessen Rahmen die Antragsgegnerin zu 2 Lagerung, "
        "Versand, Retourenabwicklung und Kundendienst übernimmt. Hierin liegt ein <b>aktiver Tatbeitrag</b> "
        "i.S.d. EuGH C-567/18 (Coty Germany ./. Amazon), der das Haftungsprivileg nach Art. 6 DSA "
        "(früher Art. 14 ECRL) entfallen lässt.",
        S_NORMAL))
    s.append(Paragraph("<b>IV. Verletzungshandlungen</b>", S_H2))
    s.append(Paragraph(
        "1. Am 27.12.2025 stellte die Präsidentin der Antragstellerin in der Filiale Bad Mergentheim der "
        "Antragsgegnerin zu 1 die in der Abmahnung vom 22.01.2026 im Einzelnen dargelegten "
        "Verletzungshandlungen fest (Glaubhaftmachungsmittel 3: Aktenvermerk).",
        S_NORMAL))
    s.append(Paragraph(
        "2. Eine durch die Detektei Spuernase-Couture GmbH vom 15.02.–20.02.2026 durchgeführte verdeckte "
        "Observation der Filialen Crailsheim, Tauberbischofsheim und Bad Mergentheim ergab, dass die "
        "Verletzungshandlungen <b>flächendeckend</b> erfolgen (Glaubhaftmachungsmittel 4: Detektivbericht "
        "nebst 47 Lichtbildern).",
        S_NORMAL))
    s.append(Paragraph(
        "3. Die Antragsgegnerin zu 1 plant ihre Teilnahme an der Messe Pitti Uomo, Florenz, 11.–14.03.2026, "
        "Halle 7, Stand B-44 (Glaubhaftmachungsmittel 5: Standliste Pitti Immagine s.r.l., Stand 28.02.2026).",
        S_NORMAL))
    s.append(Paragraph(
        "4. Auf der Plattform der Antragsgegnerin zu 2 werden die streitgegenständlichen Waren seit "
        "mindestens September 2025 unter dem Verkäuferkonto &quot;brezelmann_outlet_official&quot; (Verkäufer-"
        "ID 1.847.221.984) angeboten und teils im Rahmen des FBD-Programms ausgeliefert "
        "(Glaubhaftmachungsmittel 6: 12 Screenshots vom 05.02.2026 und 09.02.2026).",
        S_NORMAL))
    s.append(Paragraph(
        "5. Die Antragsgegnerin zu 2 wurde mit Notice-and-Action-Mitteilung vom 11.09.2025 (NA-ID DNZ-"
        "2025-44788) auf die Markenverletzungen aufmerksam gemacht. Reaktion: bisher keine Entfernung "
        "(Glaubhaftmachungsmittel 7).",
        S_NORMAL))
    return s

story += blatt_ev_antrag_2()
story.append(PageBreak())

def blatt_ev_antrag_3():
    s = briefkopf_steinacker()
    s.append(Paragraph("(Fortsetzung Antrag eV LG Frankfurt 11.03.2026 — Seite 3)", S_SMALL))
    s.append(Spacer(1, 6))
    s.append(Paragraph("<b>B. Rechtliche Würdigung</b>", S_H2))
    s.append(Paragraph("<b>I. Zuständigkeit und Eilbedürftigkeit</b>", S_H2))
    s.append(Paragraph(
        "Die örtliche Zuständigkeit des Landgerichts Frankfurt am Main folgt aus § 32 ZPO (Begehungsort umfasst "
        "die Donauzon-Plattform, die im Frankfurter Datacenter gehostet ist — Glaubhaftmachungsmittel 8) sowie "
        "aus § 140 MarkenG i.V.m. der Konzentrationsverordnung Hessen. Die sachliche Zuständigkeit folgt aus "
        "§§ 140 Abs. 2, 141 MarkenG, Art. 124 UMV (Frankfurt ist UMG-Gericht).",
        S_NORMAL))
    s.append(Paragraph(
        "Die <b>Dringlichkeit</b> wird nach § 12 Abs. 1 UWG (analog für Markenrecht nach BGH I ZR 121/12 — "
        "Aida Kreuzfahrten) <b>vermutet</b>. Die Antragstellerin hat von den Verletzungshandlungen am "
        "27.12.2025 Kenntnis erlangt; die Frist von einem Monat ist gewahrt (Antragstellung am 11.03.2026 — "
        "konkret kausal verzögert durch außergerichtliche Verhandlungen und Detektivermittlungen, vgl. BGH "
        "GRUR 2019, 1290 — Cordoba II; KG Berlin 5 U 142/17). Die Vermutung ist im Übrigen <i>tempore</i> der "
        "Pitti-Uomo-Messe (11.–14.03.2026) <b>zwingend zu bejahen</b>: Eine spätere Vollziehung würde dem "
        "Markenrechtsschutz seinen Sinn nehmen.",
        S_NORMAL))
    s.append(Paragraph("<b>II. Verfügungsanspruch</b>", S_H2))
    s.append(Paragraph("<b>1. Gegen Antragsgegnerin zu 1</b>", S_H2))
    s.append(Paragraph(
        "Der Anspruch folgt aus §§ 14 Abs. 2 Nr. 1, 2 und 3 MarkenG sowie Art. 9 Abs. 2 lit. a)–c) UMV.",
        S_NORMAL))
    s.append(Paragraph(
        "a) <b>Wortmarke</b>: Die Verwendung von &quot;klötzkette&quot; auf Bekleidung erfüllt den Tatbestand des "
        "§ 14 Abs. 2 Nr. 2 MarkenG. Phonetische Identität liegt vor; schriftbildliche Ähnlichkeit ist "
        "hochgradig (Verzicht auf Akzente und Doppel-z = orthographische Marginalien). Warenidentität (Kl. 25). "
        "Verwechslungsgefahr nach EuGH C-251/95 (Sabel), C-342/97 (Lloyd), BGH GRUR 2009, 766 (Stofffähnchen) "
        "evident.",
        S_NORMAL))
    s.append(Paragraph(
        "b) <b>Erweiterter Bekanntheitsschutz</b>: § 14 Abs. 2 Nr. 3 MarkenG / Art. 9 Abs. 2 lit. c) UMV. "
        "Bekanntheit nachgewiesen (Allensbach 2023). Ausnutzung der Wertschätzung i.S. EuGH C-487/07 "
        "(L'Oréal/Bellure) sowie unlautere Beeinträchtigung der Unterscheidungskraft i.S. EuGH C-252/07 "
        "(Intel/Sihra). Eine reduzierte Verkehrsdurchsetzung des angegriffenen Zeichens — wie sie etwa in "
        "den Fällen BGH I ZB 22/20 (&quot;Quadratisch Praktisch Gut&quot;) zu prüfen ist — kommt mangels jeglicher "
        "Eigenständigkeit des Zeichens &quot;klötzkette&quot; nicht in Betracht.",
        S_NORMAL))
    s.append(Paragraph(
        "c) <b>3D-Formmarke</b>: Die Flakons der Antragsgegnerin zu 1 sind quasi-identisch (Stopfenwinkel "
        "4° vs. 7°, Höhe 95 mm vs. 92 mm, sonstige Maße identisch). Verkehrsdurchsetzung der Form ist "
        "nachgewiesen.",
        S_NORMAL))
    s.append(Paragraph(
        "d) <b>Soundmarke</b>: Eintragungsfähigkeit nach EuGH C-283/01 (Shield Mark). Klangbildähnlichkeit "
        "wesentlich (Champagner-Schaum-Glissando + Eiswürfel + geflüsterte Wortmarke). Behauptung der "
        "Antragsgegnerin zu 1 (&quot;Bierdose statt Sektflasche&quot;) ist nach klangakustischem Sachverständigengutachten "
        "Prof. Steinpfeil (Glaubhaftmachungsmittel 9) sub specie veritatis fragwürdig — und im Übrigen für "
        "die Verwechslungsgefahr ohne Belang.",
        S_NORMAL))
    s.append(Paragraph(
        "e) <b>Slogan-Marke</b>: Die deutsche Übersetzung &quot;Luxus ist ein Grundrecht&quot; ist nach EuGH "
        "C-421/13 (Apple Store) als markenmäßige Benutzung anzusehen, sofern der Aussagegehalt identisch "
        "bleibt. Dies ist hier der Fall.",
        S_NORMAL))
    s.append(Paragraph("<b>2. Gegen Antragsgegnerin zu 2</b>", S_H2))
    s.append(Paragraph(
        "Die Plattformhaftung der Antragsgegnerin zu 2 folgt aus § 14 Abs. 2 MarkenG i.V.m. der Coty-"
        "Rechtsprechung (EuGH C-567/18 — Coty Germany ./. Amazon). Aufgrund des aktiven Auftritts "
        "(&quot;Fulfilment by Donauzon&quot;) ist die Antragsgegnerin zu 2 als <b>Mittäterin</b>, nicht bloß als "
        "&quot;Vermittlerin&quot; i.S.d. Art. 6 DSA zu qualifizieren. Das Privileg des Art. 6 DSA setzt &quot;rein "
        "passives&quot; Handeln voraus; die durch FBD geleistete Lagerung, Versand und Retourenabwicklung schließt "
        "diese Qualifikation aus.",
        S_NORMAL))
    s.append(Paragraph(
        "Selbst bei Anwendung des Art. 6 DSA wäre das Privileg gem. Art. 6 Abs. 1 lit. b) DSA entfallen, "
        "da die Antragsgegnerin zu 2 spätestens mit der Notice-and-Action-Mitteilung vom 11.09.2025 "
        "(NA-ID DNZ-2025-44788) Kenntnis erlangt hat und gleichwohl die Listings nicht entfernt hat.",
        S_NORMAL))
    s.append(Paragraph("<b>III. Verfügungsgrund</b>", S_H2))
    s.append(Paragraph(
        "Der Verfügungsgrund (Dringlichkeit) ist — wie oben dargelegt — nach § 12 Abs. 1 UWG analog gem. der "
        "BGH-Rechtsprechung zu vermuten und wird durch den unmittelbar bevorstehenden Pitti-Uomo-Termin in "
        "Florenz zusätzlich bekräftigt.",
        S_NORMAL))
    s.append(Paragraph("<b>IV. Glaubhaftmachung</b>", S_H2))
    s.append(Paragraph(
        "Sämtliche tatsächlichen Behauptungen werden glaubhaft gemacht durch die als Glaubhaftmachungsmittel "
        "1–9 vorgelegten Urkunden, Sachverständigengutachten und eidesstattlichen Versicherungen. Die "
        "eidesstattliche Versicherung der Detektivin Karla Kalt-Bandel (Spuernase-Couture GmbH) liegt als "
        "Glaubhaftmachungsmittel 10 bei.",
        S_NORMAL))
    s.append(Spacer(1, 12))
    s.append(Paragraph("Dr. Dr. Annabella Steinacker-von Tarsis, LL.M. (Cantab.)<br/>Rechtsanwältin", S_RIGHT))
    s.append(Spacer(1, 6))
    s.append(Paragraph("<i>[Anlagen folgen physisch in einem gesonderten Anlagenband Bl. K-1 bis K-247; im Akteneintrag nur Inhaltsverzeichnis Bl. 28 d.A.]</i>", S_SMALL))
    return s

story += blatt_ev_antrag_3()
story.append(PageBreak())

# =====================================================================
# Schutzschriftenregister-Abfrage
# =====================================================================
def blatt_schutzschriften():
    s = []
    s.append(Paragraph("<b>Beck-Online / Schutzschriftenregister Hessen — Ausdruck</b>", S_H2))
    s.append(Paragraph("Abfrage am 10.03.2026 um 16:42 Uhr durch RA v. Brenkenhoff (User-ID: brenken_stkip)", S_SMALL))
    s.append(HLine(thickness=0.3))
    s.append(Spacer(1, 4))
    abfrage = (
        "─────────────────────────────────────────────────────────────────\n"
        "SCHUTZSCHRIFTENREGISTER HESSEN — TREFFERLISTE\n"
        "─────────────────────────────────────────────────────────────────\n"
        "Suchparameter:\n"
        "  Antragsgegner: 'Brezelmann Discount KG' OR 'Brezelmann'\n"
        "  Zeitraum:      01.01.2025 - 10.03.2026\n"
        "  Gericht:       LG Frankfurt am Main\n"
        "  Sachgebiet:    Markenrecht / Wettbewerbsrecht / IP-Recht\n"
        "─────────────────────────────────────────────────────────────────\n"
        "ERGEBNIS:    0 Treffer.\n"
        "─────────────────────────────────────────────────────────────────\n"
        "Hinweise:\n"
        " • Die Suche umfasst auch die Schutzschriftenregister anderer\n"
        "   Bundeslaender (zentrales Schutzschriftenregister, ZSSR).\n"
        " • Eine Hinterlegung einer Schutzschrift kann auch nach\n"
        "   Antragseingang noch erfolgen; eine erneute Abfrage am Tag\n"
        "   der mdl. Verhandlung wird empfohlen.\n"
        " • Bei der Antragsgegnerin Donauzon Marketplace GmbH liegen 14\n"
        "   Schutzschriften in der Datenbank vor, jedoch keine zum hier\n"
        "   streitgegenstaendlichen Sachverhalt.\n"
        "─────────────────────────────────────────────────────────────────\n"
        "Ende der Trefferliste. Signatur: ZSSR/HE/2026/03/10/16:42:18\n"
        "─────────────────────────────────────────────────────────────────\n"
    )
    s.append(Preformatted(abfrage, S_MONO))
    s.append(Spacer(1, 8))
    s.append(Paragraph("<b>Bewertung:</b> Es liegt keine Schutzschrift vor; eine ex parte-Entscheidung des LG Frankfurt ist demnach möglich. Der Antrag wurde am 11.03.2026 um 09:12 Uhr per beA eingereicht.", S_NORMAL))
    s.append(Spacer(1, 6))
    s.append(Paragraph("Brenkenhoff", S_HAND))
    return s

story += blatt_schutzschriften()
story.append(PageBreak())

# =====================================================================
# Einstweilige Verfügung — Ausfertigung
# =====================================================================
def blatt_ev_beschluss():
    s = []
    s.append(Paragraph("<b>LANDGERICHT FRANKFURT AM MAIN</b>", S_CENTER))
    s.append(Paragraph("Kammer für Markensachen — Vorsitzender Richter VRiLG Dr. Hoffacker-Wendel", S_CENTER))
    s.append(HLine(thickness=1.0))
    s.append(Spacer(1, 4))
    s.append(Paragraph("<b>BESCHLUSS</b>", S_CENTER))
    s.append(Spacer(1, 4))
    s.append(Paragraph("In der Verfügungssache", S_NORMAL))
    s.append(Paragraph(
        "<b>klôtzzkètté SA</b>, vertreten durch die Präsidentin Mme la Comtesse Béatrice de Klôtzzkètté-"
        "Visconti, 12 rue du Faubourg Saint-Honoré, 75008 Paris, Frankreich,<br/>"
        "<i>— Antragstellerin —</i><br/><br/>"
        "Prozessbevollmächtigte: Steinacker · Lichtenberg &amp; Partners IP Boutique, Maximiliansplatz 19, 80333 München<br/><br/>"
        "<b>gegen</b><br/><br/>"
        "1. Brezelmann Discount KG, Wurstgasse 4, 97980 Bad Mergentheim<br/>"
        "2. Donauzon Marketplace GmbH, Erdbeerallee 88, 80807 München<br/>"
        "<i>— Antragsgegnerinnen —</i>",
        S_NORMAL_LEFT))
    s.append(Paragraph("<b>wegen Markenrechtsverletzung</b>", S_NORMAL))
    s.append(Paragraph("Aktenzeichen: <b>2-03 O 412/26</b>", S_NORMAL))
    s.append(Spacer(1, 6))
    s.append(Paragraph(
        "hat die 3. Zivilkammer des Landgerichts Frankfurt am Main durch den Vorsitzenden Richter am "
        "Landgericht Dr. Hoffacker-Wendel als Einzelrichter am <b>11. März 2026</b> ohne mündliche Verhandlung "
        "gemäß § 937 Abs. 2 ZPO entschieden:",
        S_NORMAL))
    s.append(Paragraph("<b>Tenor</b>", S_H2))
    s.append(Paragraph(
        "<b>I.</b> Im Wege der einstweiligen Verfügung — der Dringlichkeit wegen ohne mündliche Verhandlung — "
        "wird der Antragsgegnerin zu 1 bei Vermeidung eines vom Gericht für jeden Fall der Zuwiderhandlung "
        "festzusetzenden Ordnungsgeldes bis zu EUR 250.000,00, ersatzweise Ordnungshaft, oder Ordnungshaft "
        "bis zu sechs Monaten, zu vollziehen an dem persönlich haftenden Gesellschafter Dipl.-Kfm. Egon "
        "Brezelmann, <b>untersagt</b>, im geschäftlichen Verkehr in der Bundesrepublik Deutschland und auf dem "
        "Gebiet der Europäischen Union ohne Zustimmung der Antragstellerin",
        S_NORMAL))
    for pt in [
        "1. das Zeichen &quot;klötzkette&quot; oder phonetisch verwechselbar ähnliche Zeichen für Bekleidungsstücke, insbesondere T-Shirts, anzubieten, zu bewerben oder zu vertreiben;",
        "2. Parfumflakons in der Form einer hexagonalen Karaffe mit asymmetrischem Stopfen anzubieten, zu bewerben oder zu vertreiben, sofern der Stopfenwinkel weniger als 12° vom Vertikalen abweicht;",
        "3. den Slogan &quot;Luxus ist ein Grundrecht&quot; für Waren der Klassen 25 und 35 zu verwenden;",
        "4. Tonsequenzen abzuspielen, die der Soundmarke EUTM 018 502 311 in den prägenden Bestandteilen wesentlich ähneln.",
    ]:
        s.append(Paragraph(pt, S_NORMAL))
    s.append(Paragraph(
        "<b>II.</b> Der Antragsgegnerin zu 2 wird aufgegeben, sämtliche Listings des Verkäuferkontos "
        "&quot;brezelmann_outlet_official&quot; (Verkäufer-ID 1.847.221.984) sowie aller weiteren Drittanbieter, die "
        "in der Listingbeschreibung die Zeichen &quot;klötzkette&quot;, &quot;klotzzkettä&quot; oder &quot;Krönchen K°°&quot; "
        "verwenden, binnen 24 Stunden ab Zustellung dieses Beschlusses von der Plattform donauzon.de und "
        "allen weiteren Donauzon-EU-Domains zu entfernen und entfernt zu halten.",
        S_NORMAL))
    s.append(Paragraph(
        "<b>III.</b> Die Antragsgegnerinnen haben als Gesamtschuldnerinnen die Kosten des Verfahrens zu tragen.",
        S_NORMAL))
    s.append(Paragraph(
        "<b>IV.</b> Der Streitwert wird auf EUR 2.400.000,00 festgesetzt.",
        S_NORMAL))
    s.append(Spacer(1, 6))
    s.append(Paragraph("<b>Gründe</b>", S_H2))
    s.append(Paragraph(
        "Der Antrag auf Erlass einer einstweiligen Verfügung ist zulässig und begründet. Die örtliche und "
        "sachliche Zuständigkeit der erkennenden Kammer folgt aus §§ 32 ZPO, 140, 141 MarkenG i.V.m. der "
        "Konzentrationsverordnung Hessen. Die Antragstellerin hat sowohl Verfügungsanspruch als auch Verfügungs"
        "grund glaubhaft gemacht; auf die Antragsschrift vom 11.03.2026 wird in vollem Umfang Bezug genommen. "
        "Eine mündliche Verhandlung war wegen der besonderen Dringlichkeit im Hinblick auf den am 11.03.2026 "
        "beginnenden Messetermin Pitti Uomo (Florenz) nicht durchzuführen, § 937 Abs. 2 ZPO.",
        S_NORMAL))
    s.append(Paragraph(
        "<b>Rechtsbehelfsbelehrung</b>: Gegen diesen Beschluss ist Widerspruch (§ 924 ZPO) statthaft. Über "
        "den Widerspruch entscheidet das Gericht durch Endurteil aufgrund mündlicher Verhandlung.",
        S_NORMAL))
    s.append(Spacer(1, 14))
    s.append(Paragraph("Frankfurt am Main, 11.03.2026", S_NORMAL))
    s.append(Spacer(1, 10))
    s.append(Paragraph("gez. Dr. Hoffacker-Wendel<br/>Vorsitzender Richter am Landgericht", S_NORMAL_LEFT))
    s.append(Spacer(1, 10))
    s.append(StampBox("Ausgefertigt\n11.03.2026\nLG Frankfurt a.M.", angle=-6, color=colors.HexColor("#225522")))
    return s

story += blatt_ev_beschluss()
story.append(PageBreak())

# =====================================================================
# Gerichtsvollzieher-Protokoll Pitti Uomo (mehrere Seiten)
# =====================================================================
def blatt_gv_protokoll_1():
    s = []
    s.append(Paragraph("<b>PROTOKOLLO DI ESECUZIONE / GERICHTSVOLLZIEHER-PROTOKOLL</b>", S_CENTER))