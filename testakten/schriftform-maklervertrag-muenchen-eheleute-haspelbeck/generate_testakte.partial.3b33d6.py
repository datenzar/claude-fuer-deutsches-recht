#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testakte Maklervertrag München — Eheleute Haspelbeck-Türkenfeld ./. Bechtholdsmeier-Schongau e.K.
Az. LG München I 12 O 8842/23
Streitgegenstand: Rückforderung Maklerprovision EUR 8.810,76 (§§ 656a, 126b, 812 BGB)
Generator-Script — erzeugt fragmentarische Testakte als PDF (Ziel 80-95 Seiten)
"""

import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.platypus.flowables import Flowable
from reportlab.lib.colors import HexColor, white, black, red
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import datetime

# ─── Pfade ────────────────────────────────────────────────────────────────────
OUTPUT_DIR = "/home/user/workspace/claude-fuer-deutsches-recht/testakten/schriftform-maklervertrag-muenchen-eheleute-haspelbeck"
OUTPUT_PDF = os.path.join(OUTPUT_DIR, "Testakte_Maklervertrag_Muenchen_Haspelbeck.pdf")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─── Farben ───────────────────────────────────────────────────────────────────
C_DUNKELBLAU  = HexColor("#1A2E4A")
C_GRAU        = HexColor("#4A4A4A")
C_HELLGRAU    = HexColor("#F0F0F0")
C_BORDER      = HexColor("#C8C8C8")
C_AKZENT      = HexColor("#8B1A1A")   # Dunkelrot für juristische Hervorhebungen
C_NOTAR_ROT   = HexColor("#CC0000")
C_WA_GRUEN    = HexColor("#DCF8C6")   # WhatsApp-Grün
C_WA_GRAU     = HexColor("#F0F0F0")   # WhatsApp-Grau
C_EMAIL_BG    = HexColor("#F8F8F8")
C_ROT_ANWALT  = HexColor("#CC0000")

# ─── Styles ───────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def make_style(name, **kwargs):
    base = kwargs.pop("parent", "Normal")
    s = ParagraphStyle(name=name, parent=styles[base], **kwargs)
    return s

S_NORMAL    = make_style("AktNormal", fontName="Helvetica", fontSize=10, leading=14,
                          spaceAfter=4, textColor=C_GRAU, alignment=TA_JUSTIFY)
S_HEADING1  = make_style("AktH1", fontName="Helvetica-Bold", fontSize=14, leading=18,
                          spaceBefore=10, spaceAfter=6, textColor=C_DUNKELBLAU)
S_HEADING2  = make_style("AktH2", fontName="Helvetica-Bold", fontSize=11, leading=15,
                          spaceBefore=8, spaceAfter=4, textColor=C_DUNKELBLAU)
S_HEADING3  = make_style("AktH3", fontName="Helvetica-BoldOblique", fontSize=10, leading=14,
                          spaceBefore=6, spaceAfter=3, textColor=C_AKZENT)
S_FETT      = make_style("AktFett", fontName="Helvetica-Bold", fontSize=10, leading=14,
                          textColor=C_GRAU)
S_KLEIN     = make_style("AktKlein", fontName="Helvetica", fontSize=8, leading=11,
                          textColor=C_GRAU)
S_MONO      = make_style("AktMono", fontName="Courier", fontSize=9, leading=13,
                          textColor=C_GRAU, backColor=C_EMAIL_BG)
S_MONO_BOLD = make_style("AktMonoBold", fontName="Courier-Bold", fontSize=9, leading=13,
                          textColor=C_GRAU)
S_ZENTRIERT = make_style("AktZentriert", fontName="Helvetica", fontSize=10, leading=14,
                          alignment=TA_CENTER, textColor=C_GRAU)
S_ZENTRIERT_FETT = make_style("AktZentriertFett", fontName="Helvetica-Bold", fontSize=12,
                               leading=16, alignment=TA_CENTER, textColor=C_DUNKELBLAU)
S_RUBRUM    = make_style("AktRubrum", fontName="Times-Roman", fontSize=10, leading=15,
                          textColor=C_GRAU, alignment=TA_JUSTIFY)
S_RUBRUM_FETT = make_style("AktRubrumFett", fontName="Times-Bold", fontSize=10, leading=15,
                             textColor=C_GRAU)
S_KURSIV    = make_style("AktKursiv", fontName="Helvetica-Oblique", fontSize=10, leading=14,
                          textColor=C_GRAU, leftIndent=1.5*cm)
S_ROT_KURSIV = make_style("AktRotKursiv", fontName="Helvetica-BoldOblique", fontSize=9,
                            leading=13, textColor=C_ROT_ANWALT, leftIndent=1*cm)
S_TITEL     = make_style("AktTitel", fontName="Helvetica-Bold", fontSize=18, leading=24,
                          alignment=TA_CENTER, textColor=C_DUNKELBLAU, spaceBefore=20)
S_UNTERTITEL = make_style("AktUntertitel", fontName="Helvetica", fontSize=11, leading=16,
                           alignment=TA_CENTER, textColor=C_GRAU, spaceBefore=6)
S_BESCHLUSS = make_style("AktBeschluss", fontName="Times-Roman", fontSize=10, leading=16,
                          textColor=C_GRAU, leftIndent=2*cm, rightIndent=2*cm,
                          alignment=TA_JUSTIFY)
S_TENOR     = make_style("AktTenor", fontName="Times-Bold", fontSize=10, leading=16,
                          textColor=C_DUNKELBLAU, leftIndent=2*cm, rightIndent=2*cm)

# ─── Hilfsfunktionen ──────────────────────────────────────────────────────────
def p(text, style=None):
    if style is None:
        style = S_NORMAL
    return Paragraph(text, style)

def h1(text): return Paragraph(text, S_HEADING1)
def h2(text): return Paragraph(text, S_HEADING2)
def h3(text): return Paragraph(text, S_HEADING3)
def sp(h=0.3): return Spacer(1, h*cm)
def pb(): return PageBreak()
def hr(): return HRFlowable(width="100%", thickness=0.5, color=C_BORDER, spaceAfter=6)
def hr_thick(): return HRFlowable(width="100%", thickness=1.5, color=C_DUNKELBLAU, spaceAfter=8)

def rubrum_block(klaeger, beklagter, az, gericht, extra_lines=None):
    """Erzeugt Rubrum-Block für Schriftsätze."""
    elems = []
    elems.append(hr_thick())
    data = [
        [p("Kläger:", S_RUBRUM_FETT), p(klaeger, S_RUBRUM)],
        [p("Beklagte:", S_RUBRUM_FETT), p(beklagter, S_RUBRUM)],
        [p("Aktenzeichen:", S_RUBRUM_FETT), p(az, S_RUBRUM)],
        [p("Gericht:", S_RUBRUM_FETT), p(gericht, S_RUBRUM)],
    ]
    if extra_lines:
        for lbl, val in extra_lines:
            data.append([p(lbl, S_RUBRUM_FETT), p(val, S_RUBRUM)])
    t = Table(data, colWidths=[4*cm, 12*cm])
    t.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    elems.append(t)
    elems.append(hr_thick())
    return elems

def section_header(title, aktenzeichen=None):
    """Grauer Kasten als Abschnittstitel."""
    content = title
    if aktenzeichen:
        content += f"<br/><font size='8' color='#666666'>{aktenzeichen}</font>"
    t = Table([[p(content, make_style("SH", fontName="Helvetica-Bold", fontSize=11,
                                      leading=15, textColor=white, alignment=TA_LEFT))]],
              colWidths=[16.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), C_DUNKELBLAU),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("ROWBACKGROUNDS", (0,0), (-1,-1), [C_DUNKELBLAU]),
    ]))
    return t

def email_block(von, an, datum, betreff, body_lines, cc=None):
    """Simuliert E-Mail-Header + Body."""
    elems = []
    header_rows = [
        [p("Von:", S_MONO_BOLD), p(von, S_MONO)],
        [p("An:", S_MONO_BOLD), p(an, S_MONO)],
    ]
    if cc:
        header_rows.append([p("CC:", S_MONO_BOLD), p(cc, S_MONO)])
    header_rows += [
        [p("Datum:", S_MONO_BOLD), p(datum, S_MONO)],
        [p("Betreff:", S_MONO_BOLD), p(betreff, S_MONO)],
    ]
    ht = Table(header_rows, colWidths=[2.5*cm, 14*cm])
    ht.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), C_EMAIL_BG),
        ("GRID", (0,0), (-1,-1), 0.3, C_BORDER),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    elems.append(ht)
    elems.append(sp(0.15))
    # Body
    body_text = "<br/>".join(body_lines)
    body_style = make_style("EmailBody", fontName="Courier", fontSize=8.5, leading=13,
                             backColor=HexColor("#FAFAFA"), textColor=HexColor("#222222"),
                             leftIndent=8, rightIndent=8, spaceBefore=2, spaceAfter=2)
    bt = Table([[p(body_text, body_style)]], colWidths=[16.5*cm])
    bt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#FAFAFA")),
        ("BOX", (0,0), (-1,-1), 0.5, C_BORDER),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    elems.append(bt)
    return elems

def notar_stempel():
    """Rotes Rechteck als Notar-Stempel-Simulation."""
    t = Table([[p("NOTAR Dr. Ulfried Vorstetter\nUR-Nr. 1488/2023\nNotariat Maximilianstraße 22, 80539 München\nBeglaubigt gemäß § 129 BGB",
                  make_style("NS", fontName="Helvetica-Bold", fontSize=9, leading=13,
                              textColor=white, alignment=TA_CENTER))]],
              colWidths=[8*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), C_NOTAR_ROT),
        ("BOX", (0,0), (-1,-1), 2, HexColor("#880000")),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    return t

def kanzlei_logo_ht():
    """ASCII-Logo Hagelbrand & Trotzenburg."""
    logo = """
  ██╗  ██╗ ██╗ ████████╗
  ██║  ██║ ██║    ██╔══╝
  ███████║ ██║    ██║
  ██╔══██║ ██║    ██║
  ██║  ██║ ██║    ██║
  ╚═╝  ╚═╝ ╚═╝    ╚═╝
  Hagelbrand & Trotzenburg
  Rechtsanwälte"""
    return p(logo, make_style("LogoHT", fontName="Courier", fontSize=7, leading=9,
                               textColor=C_DUNKELBLAU, alignment=TA_LEFT))

def kanzlei_logo_km():
    """ASCII-Logo Korkenzieher Maibach Partner."""
    logo = """
  ██╗  ██╗ ██╗██╗  ██╗
  ██║ ██╔╝ ██║██║ ██╔╝
  █████╔╝  ██║█████╔╝
  ██╔═██╗  ██║██╔═██╗
  ██║  ██╗ ██║██║  ██╗
  ╚═╝  ╚═╝ ╚═╝╚═╝  ╚═╝
  Korkenzieher Maibach Partner mbB
  Rechtsanwälte · Karlsplatz 4"""
    return p(logo, make_style("LogoKM", fontName="Courier", fontSize=7, leading=9,
                               textColor=C_AKZENT, alignment=TA_LEFT))

def whatsapp_bubble(text, sender, time_str, is_right=True):
    """Erzeugt WhatsApp-Sprechblase."""
    bg = C_WA_GRUEN if is_right else C_WA_GRAU
    align_style = TA_RIGHT if is_right else TA_LEFT
    bubble_style = make_style(f"WA{'R' if is_right else 'L'}",
                               fontName="Helvetica", fontSize=9.5, leading=14,
                               textColor=HexColor("#111111"), alignment=align_style)
    time_style = make_style("WATime", fontName="Helvetica", fontSize=7, leading=10,
                             textColor=HexColor("#888888"), alignment=TA_RIGHT)
    sender_style = make_style("WASender", fontName="Helvetica-Bold", fontSize=8, leading=11,
                               textColor=HexColor("#075E54"))
    content = [[
        p(f"<b>{sender}</b>", sender_style),
        p(text, bubble_style),
        p(time_str, time_style),
    ]]
    t = Table(content, colWidths=[16.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("ROUNDEDCORNERS", (0,0), (-1,-1), [8,8,8,8]),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("BOX", (0,0), (-1,-1), 0.5, HexColor("#BBBBBB")),
        ("ROWBACKGROUNDS", (0,0), (-1,-1), [bg]),
    ]))
    if is_right:
        outer = Table([[t]], colWidths=[16.5*cm])
        outer.setStyle(TableStyle([
            ("ALIGN", (0,0), (-1,-1), "RIGHT"),
            ("LEFTPADDING", (0,0), (-1,-1), 60),
            ("RIGHTPADDING", (0,0), (-1,-1), 0),
            ("TOPPADDING", (0,0), (-1,-1), 3),
            ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ]))
        return outer
    else:
        outer = Table([[t]], colWidths=[16.5*cm])
        outer.setStyle(TableStyle([
            ("ALIGN", (0,0), (-1,-1), "LEFT"),
            ("LEFTPADDING", (0,0), (-1,-1), 0),
            ("RIGHTPADDING", (0,0), (-1,-1), 60),
            ("TOPPADDING", (0,0), (-1,-1), 3),
            ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ]))
        return outer

# ─── Seitennummerierung ───────────────────────────────────────────────────────
class AktenFooter:
    def __init__(self, az="LG München I 12 O 8842/23"):
        self.az = az

    def __call__(self, canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(HexColor("#888888"))
        footer_left = f"Akte: Haspelbeck-Türkenfeld ./. Bechtholdsmeier-Schongau e.K. — Az. {self.az}"
        footer_right = f"Seite {doc.page}"
        canvas.drawString(2*cm, 1.5*cm, footer_left)
        canvas.drawRightString(19*cm, 1.5*cm, footer_right)
        canvas.setStrokeColor(HexColor("#CCCCCC"))
        canvas.setLineWidth(0.5)
        canvas.line(2*cm, 1.8*cm, 19*cm, 1.8*cm)
        canvas.restoreState()

# ═══════════════════════════════════════════════════════════════════════════════
# AKTENBESTANDTEILE
# ═══════════════════════════════════════════════════════════════════════════════

def bestandteil_01_aktendeckel():
    """1. Aktendeckel"""
    elems = []
    elems.append(sp(2))

    # Münchner Mönch ASCII
    moench_ascii = """\
         .---.
        /|   |\\
       / |   | \\
      /  | ( ) |  \\
     /   |  |  |   \\
    /    |  |  |    \\
   /     | /|\\ |     \\
  /______|/ | \\|______\\
        /   |   \\
       /  MÜNCHEN \\
      /______________\\
    Bayerisches Staatswappen (Stilisierung)
         Mönch — Gründungsfigur"""

    t_moench = Table([[p(moench_ascii,
                          make_style("Moench", fontName="Courier", fontSize=9, leading=12,
                                      textColor=C_DUNKELBLAU, alignment=TA_CENTER))]],
                      colWidths=[16.5*cm])
    t_moench.setStyle(TableStyle([
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("TOPPADDING", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    elems.append(t_moench)
    elems.append(sp(1))

    # Haupttitel
    elems.append(p("LANDGERICHT MÜNCHEN I", make_style("AkD1", fontName="Helvetica-Bold",
                    fontSize=16, leading=22, alignment=TA_CENTER, textColor=C_DUNKELBLAU)))
    elems.append(sp(0.3))
    elems.append(p("12. Zivilkammer", make_style("AkD2", fontName="Helvetica",
                    fontSize=12, leading=16, alignment=TA_CENTER, textColor=C_GRAU)))
    elems.append(sp(1))
    elems.append(hr_thick())
    elems.append(sp(0.5))

    # Aktenbezeichnung
    elems.append(p("AKTE", make_style("AkD3", fontName="Helvetica-Bold",
                    fontSize=22, leading=28, alignment=TA_CENTER, textColor=C_AKZENT)))
    elems.append(sp(0.5))
    elems.append(p("Eheleute Korbinian und Walburga Haspelbeck-Türkenfeld",
                    make_style("AkD4", fontName="Helvetica-Bold", fontSize=13, leading=18,
                                alignment=TA_CENTER, textColor=C_DUNKELBLAU)))
    elems.append(p("— Kläger —", make_style("AkD5", fontName="Helvetica-Oblique",
                    fontSize=11, leading=15, alignment=TA_CENTER, textColor=C_GRAU)))
    elems.append(sp(0.4))
    elems.append(p("gegen", make_style("AkD6", fontName="Helvetica-Bold",
                    fontSize=11, leading=15, alignment=TA_CENTER, textColor=C_GRAU)))
    elems.append(sp(0.4))
    elems.append(p("Immobilien-Vermittlung „Marlene Bechtholdsmeier-Schongau e.K."",
                    make_style("AkD7", fontName="Helvetica-Bold", fontSize=13, leading=18,
                                alignment=TA_CENTER, textColor=C_DUNKELBLAU)))
    elems.append(p("— Beklagte —", make_style("AkD8", fontName="Helvetica-Oblique",
                    fontSize=11, leading=15, alignment=TA_CENTER, textColor=C_GRAU)))
    elems.append(sp(0.5))
    elems.append(hr_thick())
    elems.append(sp(0.5))

    # Streitgegenstand
    data = [
        ["Streitgegenstand:", "Rückforderung Maklerprovision EUR 8.810,76"],
        ["Rechtsgrundlagen:", "§§ 812 Abs. 1, 656a, 126b BGB"],
        ["Aktenzeichen:", "LG München I 12 O 8842/23"],
        ["", "OLG München 13 U 412/24"],
        ["", "BGH I ZR 202/25"],
        ["Streitwert:", "EUR 8.810,76 nebst Zinsen"],
        ["Angelegt:", "22. Mai 2026"],
        ["Status:", "Rechtskräftig abgeschlossen — Kläger obsiegend"],
    ]
    td = [[p(r[0], S_FETT), p(r[1], S_NORMAL)] for r in data]
    t = Table(td, colWidths=[5*cm, 11.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), C_HELLGRAU),
        ("GRID", (0,0), (-1,-1), 0.3, C_BORDER),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("ROWBACKGROUNDS", (0,0), (-1,-1), [C_HELLGRAU, white]),
    ]))
    elems.append(t)
    elems.append(sp(2))

    note_style = make_style("AkDNote", fontName="Helvetica-Oblique", fontSize=8,
                             leading=12, textColor=HexColor("#888888"), alignment=TA_CENTER)
    elems.append(p("Fragmentarische Testakte — Alle Namen, Firmen und Adressen fiktiv.", note_style))
    elems.append(p("Erstellt 22. Mai 2026. Enthält 26 Aktenbestandteile.", note_style))
    elems.append(pb())
    return elems


def bestandteil_02_inhaltsverzeichnis():
    """2. Inhaltsverzeichnis"""
    elems = []
    elems.append(section_header("INHALTSVERZEICHNIS",
                                 "Az. LG München I 12 O 8842/23 / OLG München 13 U 412/24 / BGH I ZR 202/25"))
    elems.append(sp(0.4))

    eintraege = [
        ("1", "Aktendeckel", "1"),
        ("2", "Inhaltsverzeichnis (dieses Dokument)", "2"),
        ("3", "Mandatsannahmebogen RA Dr. Hagelbrand-Wittlsbach", "4"),
        ("4", "Klageschrift vom 14. September 2023 (8 Seiten)", "5"),
        ("5", "Klageerwiderung vom 24. Oktober 2023 (10 Seiten)", "13"),
        ("6", "Replik Kläger vom 17. November 2023 (6 Seiten)", "23"),
        ("7", "E-Mail-Kette Haspelbeck ↔ Bechtholdsmeier (8 Seiten)", "29"),
        ("8", "Notarieller Kaufvertrag-Auszug UR-Nr. 1488/2023", "37"),
        ("9", "Quittung Maklerprovision EUR 8.810,76", "39"),
        ("10", "Widerrufsbelehrung / Mail-Signatur-Analyse", "40"),
        ("11", "Protokoll Vergleichsverhandlung 12. Juni 2024", "41"),
        ("12", "Berufungsschriftsatz OLG München (04. Juli 2024)", "43"),
        ("13", "Berufungsbegründung (ausführlich, 12 Seiten)", "47"),
        ("14", "Berufungserwiderung Kläger", "59"),
        ("15", "Berufungsurteil OLG München 13 U 412/24 vom 17.02.2025", "64"),
        ("16", "Revisionsbegründung BGH I ZR 202/25 (15. Mai 2025)", "67"),
        ("17", "Revisionserwiderung Kläger", "76"),
        ("18", "Stellungnahme Verhandlungstermin BGH 11. März 2026", "78"),
        ("19", "BGH-Urteil Tenor-Auszug I ZR 202/25 (11.03.2026)", "79"),
        ("20", "Mandantenmemo Hagelbrand-Wittlsbach (14.03.2026)", "81"),
        ("21", "Handschriftliche Randnotizen Korbinian Haspelbeck", "83"),
        ("22", "WhatsApp-Screenshot-Simulation (Notartermin)", "85"),
        ("23", "Kanzleirechnung Hagelbrand & Trotzenburg", "87"),
        ("24", "Aktenrand-Memo RAin Korkenzieher-Mariastein", "89"),
        ("25", "Anlagenverzeichnis K-MAK-1 bis K-MAK-29", "90"),
        ("26", "Stundenaufstellung Hagelbrand & Trotzenburg (3 Seiten)", "92"),
    ]

    data = [[p("#", S_FETT), p("Bestandteil", S_FETT), p("Seite", S_FETT)]]
    for nr, titel, seite in eintraege:
        data.append([p(nr, S_KLEIN), p(titel, S_NORMAL), p(seite, S_KLEIN)])

    t = Table(data, colWidths=[1*cm, 13*cm, 2.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), C_DUNKELBLAU),
        ("TEXTCOLOR", (0,0), (-1,0), white),
        ("GRID", (0,0), (-1,-1), 0.3, C_BORDER),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [white, C_HELLGRAU]),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    elems.append(t)
    elems.append(sp(0.5))
    elems.append(p("<i>Hinweis: Die Seitenangaben beziehen sich auf die Reihenfolge der Aktenbestandteile. "
                    "Anlage K-MAK-7, K-MAK-13 und K-MAK-21 befinden sich im Sonderband II — nicht abgebildet "
                    "(vgl. Anlagenverzeichnis Bestandteil 25). Querverweise auf Sonderband II sind im gesamten "
                    "Aktenkörper kenntlich gemacht.</i>", S_KLEIN))
    elems.append(pb())
    return elems


def bestandteil_03_mandatsannahmebogen():
    """3. Mandatsannahmebogen"""
    elems = []
    elems.append(section_header("MANDATSANNAHMEBOGEN", "Kanzlei Hagelbrand & Trotzenburg Rechtsanwälte"))
    elems.append(sp(0.3))
    elems.append(kanzlei_logo_ht())
    elems.append(sp(0.2))

    adress_data = [
        ["Kanzlei:", "Hagelbrand & Trotzenburg Rechtsanwälte"],
        ["Anwalt:", "RA Dr. Knut Hagelbrand-Wittlsbach"],
        ["Adresse:", "Promenadeplatz 9, 80333 München"],
        ["Telefon:", "+49 89 4711 2020"],
        ["E-Mail:", "hagelbrand@ht-recht-muenchen.de"],
        ["Stundensatz:", "EUR 380,00 zzgl. MwSt."],
        ["Aufnahmedatum:", "01. September 2023"],
        ["Sachbearbeiter:", "Dr. K. Hagelbrand-Wittlsbach (persönlich)"],
    ]
    td = [[p(r[0], S_FETT), p(r[1], S_NORMAL)] for r in adress_data]
    t = Table(td, colWidths=[4*cm, 12.5*cm])
    t.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.3, C_BORDER),
        ("ROWBACKGROUNDS", (0,0), (-1,-1), [C_HELLGRAU, white]),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    elems.append(t)
    elems.append(sp(0.5))

    elems.append(h2("Mandant / Mandantin"))
    mand_data = [
        ["Name:", "Eheleute Korbinian und Walburga Haspelbeck-Türkenfeld"],
        ["Anschrift:", "Mauerkircherstraße 47, 81679 München-Bogenhausen"],
        ["Telefon:", "+49 89 2211 9340 (Korbinian) / +49 89 2211 9341 (Walburga)"],
        ["E-Mail:", "korbinian.haspelbeck@haspelbeck-tuerkenfeld.de"],
        ["Mandatsbeginn:", "01. September 2023"],
        ["Mandatsart:", "Klage / Rückforderung Maklerprovision"],
        ["Streitwert:", "EUR 8.810,76 nebst Zinsen ab 15. Mai 2023"],
        ["Rechtsschutzvers.:", "Rechtsschutz Bavaria AG, Pol.-Nr. 87654321-A"],
        ["SB-Rechtsschutz:", "EUR 150,00 (Eigenanteil)"],
    ]
    td2 = [[p(r[0], S_FETT), p(r[1], S_NORMAL)] for r in mand_data]
    t2 = Table(td2, colWidths=[4*cm, 12.5*cm])
    t2.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.3, C_BORDER),
        ("ROWBACKGROUNDS", (0,0), (-1,-1), [white, C_HELLGRAU]),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    elems.append(t2)
    elems.append(sp(0.5))

    elems.append(h2("Sachverhaltsaufnahme (Kurzfassung)"))
    elems.append(p(
        "Die Mandanten erwarben im Mai 2023 durch Vermittlung der Beklagten Marlene Bechtholdsmeier-Schongau e.K. "
        "eine Eigentumswohnung (Käufer-Maklervertrag — dieser nicht streitig). Parallel vermittelte die Beklagte "
        "den Verkauf des im Eigentum der Mandanten stehenden Einfamilienhauses in München-Bogenhausen. "
        "Zur Begründung eines Verkäufer-Maklervertrags beruft sich die Beklagte auf einen E-Mail-Austausch "
        "vom 03./13. April 2023, in welchem sich die Mandanten mit dem Tätigwerden der Maklerin einverstanden "
        "erklärt haben sollen. Die Mandanten bestreiten die Textformwirksamkeit dieses Austauschs gemäß "
        "§ 656a BGB i.V.m. § 126b BGB. Die Provision in Höhe von EUR 8.810,76 (1,2 % vom Kaufpreis "
        "EUR 617.000,00 inkl. MwSt.) wurde am 15. Mai 2023 durch die Mandanten beglichen. "
        "Widerruf durch Unterzeichner vom 03. August 2023 wurde von der Beklagten zurückgewiesen. "
        "Klageerhebung am 14. September 2023 beim LG München I.", S_NORMAL))
    elems.append(sp(0.3))

    elems.append(h2("Vergütungsvereinbarung"))
    verg_data = [
        ["Stundensatz:", "EUR 380,00 zzgl. gesetzlicher MwSt. (§ 34 RVG)"],
        ["Abrechnung:", "Monatlich auf Nachweis; Teilrechnungen zulässig"],
        ["Vorschuss:", "EUR 2.000,00 (geleistet 05.09.2023)"],
        ["RVG-Abrechnung:", "Alternativ nach RVG (höherer Betrag maßgeblich)"],
        ["Unterschrift Mandant:", "_____________________ (Korbinian Haspelbeck-Türkenfeld)"],
        ["Unterschrift Mandantin:", "_____________________ (Walburga Haspelbeck-Türkenfeld)"],
        ["Unterschrift RA:", "_____________________ (Dr. K. Hagelbrand-Wittlsbach)"],
        ["Datum:", "01. September 2023, München"],
    ]
    td3 = [[p(r[0], S_FETT), p(r[1], S_NORMAL)] for r in verg_data]
    t3 = Table(td3, colWidths=[4.5*cm, 12*cm])
    t3.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.3, C_BORDER),
        ("ROWBACKGROUNDS", (0,0), (-1,-1), [C_HELLGRAU, white]),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    elems.append(t3)
    elems.append(pb())
    return elems


def bestandteil_04_klageschrift():
    """4. Klageschrift (8 Seiten)"""
    elems = []
    # Briefkopf
    elems.append(section_header("KLAGESCHRIFT", "Az. LG München I 12 O 8842/23"))
    elems.append(sp(0.3))
    elems.append(kanzlei_logo_ht())
    elems.append(sp(0.2))

    # Adressblock
    addr_rows = [
        ["An das", ""],
        ["Landgericht München I", ""],
        ["Prielmayerstraße 7", ""],
        ["80335 München", "München, 14. September 2023"],
    ]
    ta = Table([[p("An das\nLandgericht München I\nPrielmayerstraße 7\n80335 München", S_NORMAL),
                 p("München, 14. September 2023", make_style("DR", fontName="Helvetica",
                    fontSize=10, leading=14, alignment=TA_RIGHT, textColor=C_GRAU))]],
               colWidths=[10*cm, 6.5*cm])
    elems.append(ta)
    elems.append(sp(0.5))

    elems.append(p("<b>In der Sache</b>", S_NORMAL))
    elems.append(sp(0.3))

    # Rubrum
    for elem in rubrum_block(
        "Eheleute Korbinian und Walburga Haspelbeck-Türkenfeld,<br/>"
        "Mauerkircherstraße 47, 81679 München-Bogenhausen",
        "Immobilien-Vermittlung „Marlene Bechtholdsmeier-Schongau e.K.",<br/>"
        "vertreten durch Marlene Bechtholdsmeier-Schongau,<br/>"
        "Schwere-Reiter-Straße 18, 80637 München",
        "LG München I 12 O 8842/23",
        "Landgericht München I, 12. Zivilkammer",
        [("wegen:", "Rückforderung Maklerprovision (§§ 812 Abs. 1 S. 1, 656a, 126b BGB)"),
         ("Streitwert:", "EUR 8.810,76")]
    ):
        elems.append(elem)
    elems.append(sp(0.4))

    elems.append(p("erheben die Kläger durch ihren Prozessbevollmächtigten — "
                    "Rechtsanwalt Dr. Knut Hagelbrand-Wittlsbach, "
                    "Kanzlei Hagelbrand & Trotzenburg Rechtsanwälte, "
                    "Promenadeplatz 9, 80333 München —", S_NORMAL))
    elems.append(sp(0.3))

    elems.append(h2("Klage"))
    elems.append(p("und beantragen:", S_NORMAL))
    elems.append(sp(0.3))

    # Anträge
    antraege = [
        "1. Die Beklagte wird verurteilt, an die Kläger einen Betrag von <b>EUR 8.810,76</b> "
        "nebst Zinsen in Höhe von 5 Prozentpunkten über dem Basiszinssatz seit dem "
        "15. Mai 2023 zu zahlen.",
        "2. Die Beklagte trägt die Kosten des Rechtsstreits.",
        "3. Das Urteil ist gegen Sicherheitsleistung in Höhe von 110 % des jeweils zu "
        "vollstreckenden Betrages vorläufig vollstreckbar.",
    ]
    for a in antraege:
        at = Table([[p(a, S_NORMAL)]], colWidths=[16.5*cm])
        at.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), C_HELLGRAU),
            ("LEFTPADDING", (0,0), (-1,-1), 16),
            ("RIGHTPADDING", (0,0), (-1,-1), 10),
            ("TOPPADDING", (0,0), (-1,-1), 6),
            ("BOTTOMPADDING", (0,0), (-1,-1), 6),
            ("BOX", (0,0), (-1,-1), 0.5, C_BORDER),
        ]))
        elems.append(at)
        elems.append(sp(0.2))

    elems.append(sp(0.3))
    elems.append(h2("Tatbestand / Sachverhalt"))

    elems.append(h3("I. Die Parteien"))
    elems.append(p(
        "Die Kläger, Eheleute Korbinian Haspelbeck-Türkenfeld (geb. 14.03.1971) und "
        "Walburga Haspelbeck-Türkenfeld geb. Brandlberger (geb. 22.07.1974), sind seit "
        "dem Jahr 2008 Eigentümer eines Einfamilienhauses mit Garten in München-Bogenhausen, "
        "Mauerkircherstraße 47, 81679 München (im Folgenden: „das Objekt"). Das Objekt hat eine "
        "Wohnfläche von ca. 185 m² und einen Garten von ca. 420 m². Die Kläger bewohnten das "
        "Objekt bis zum Notartermin am 12. Mai 2023 als Hauptwohnsitz.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "Die Beklagte, Immobilien-Vermittlung „Marlene Bechtholdsmeier-Schongau e.K." "
        "(Handelsregister München HRA 88734), ist ein Einzelunternehmen der Immobilienmaklerin "
        "Marlene Bechtholdsmeier-Schongau, tätig unter der Anschrift Schwere-Reiter-Straße 18, "
        "80637 München. Die Beklagte ist seit dem Jahr 2007 im Münchner Immobilienmarkt tätig "
        "und vermittelt schwerpunktmäßig Wohnimmobilien im Großraum München.", S_NORMAL))

    elems.append(h3("II. Der Doppelauftrag und die relevante E-Mail-Korrespondenz"))
    elems.append(p(
        "Im Frühjahr 2023 beauftragten die Kläger die Beklagte sowohl mit dem Erwerb einer "
        "Eigentumswohnung in München-Schwabing (Käufer-Maklervertrag, unstreitig wirksam in "
        "Textform geschlossen am 14. Februar 2023) als auch — nach Schilderung der Beklagten — "
        "mit der Vermittlung des Verkaufs des eigenen Hauses (Mauerkircherstraße 47). "
        "Der Käufer-Maklervertrag enthielt eine gesondert unterzeichnete Widerrufsbelehrung "
        "und die erforderlichen Angaben gemäß § 312d BGB. Der streitgegenständliche "
        "Verkäufer-Maklervertrag wurde hingegen nicht als gesondertes Dokument errichtet.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "Am 03. April 2023 um 09:12 Uhr übersandte die Beklagte eine E-Mail an die Klägerin "
        "Walburga Haspelbeck-Türkenfeld, in welcher sie über den Stand der Kaufpreisverhandlungen "
        "mit den Interessenten Bartholomäus und Hiltrud Höglmayr-Stockenfels berichtete. "
        "Unterhalb der eigentlichen Nachricht und unterhalb der Signatur der Beklagten befand sich "
        "folgender Hinweis-Text (Anlage K-MAK-1):", S_NORMAL))
    elems.append(sp(0.2))

    # Hinweistext Provision
    hint_text = (
        "„Wir weisen darauf hin, dass bei Abschluss eines Kaufvertrages bei einem Einfamilienhaus "
        "eine vom Veräußerer und Erwerber zu zahlende Provision fällig wird. Diese beläuft sich "
        "maximal auf drei Komma sieben Prozent des Kaufpreises (inklusive gesetzlicher Mehrwertsteuer "
        "und je Partei), im Verkaufsfall des von Ihnen veräußerten Objektes Mauerkircherstraße 47. "
        "Bei Zustandekommen des Kaufvertrages wird die Provision innerhalb von 14 Tagen nach "
        "Beurkundung fällig. — Im Auftrag, Marlene Bechtholdsmeier-Schongau e.K.""
    )
    ht = Table([[p(hint_text, make_style("ZitatS", fontName="Times-Italic", fontSize=9.5,
                                         leading=14, textColor=HexColor("#333333"),
                                         leftIndent=8, rightIndent=8))]], colWidths=[16.5*cm])
    ht.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#FFFDF0")),
        ("BOX", (0,0), (-1,-1), 1.5, C_BORDER),
        ("LEFTPADDING", (0,0), (-1,-1), 14),
        ("RIGHTPADDING", (0,0), (-1,-1), 14),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    elems.append(ht)
    elems.append(sp(0.2))
    elems.append(p(
        "Am 13. April 2023 um 16:33 Uhr antworteten die Kläger per E-Mail: "
        "„Sehr geehrte Frau Bechtholdsmeier, wie besprochen stimmen wir zu, "
        "dass Sie den Notartermin vereinbaren. Mit freundlichen Grüßen, "
        "Korbinian und Walburga Haspelbeck-Türkenfeld." (Anlage K-MAK-2). "
        "Diese Antwort enthält keinerlei ausdrückliche Bezugnahme auf die Provision, "
        "den Provisionshinweis oder die Bedingungen eines Verkäufer-Maklervertrags.", S_NORMAL))

    elems.append(h3("III. Zahlung und Widerruf"))
    elems.append(p(
        "Nach Abschluss des notariellen Kaufvertrags vom 12. Mai 2023 (UR-Nr. 1488/2023, "
        "Notar Dr. Ulfried Vorstetter, Maximilianstraße 22, 80539 München) stellte die "
        "Beklagte den Klägern am 15. Mai 2023 eine Provisionsrechnung über EUR 8.810,76 "
        "(entsprechend 1,2 % vom Kaufpreis EUR 617.000,00 inkl. MwSt., vgl. Anlage K-MAK-3). "
        "Die Kläger zahlten diesen Betrag am 29. Mai 2023 irrtümlich, weil sie davon ausgingen, "
        "zur Zahlung verpflichtet zu sein.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "Mit anwaltlichem Schreiben vom 03. August 2023 (Anlage K-MAK-4) widerrief der "
        "Unterfertigte namens der Kläger hilfsweise den Maklervertrag nach § 312g Abs. 1 i.V.m. "
        "§ 312b BGB sowie §§ 355 ff. BGB und forderte die Beklagte zur Rückzahlung der "
        "Provision bis zum 17. August 2023 auf. Mit Schreiben ihrer Verfahrensbevollmächtigten "
        "RAin Dr. Adelheid Korkenzieher-Mariastein vom 12. August 2023 (Anlage K-MAK-5) "
        "wies die Beklagte sämtliche Ansprüche zurück.", S_NORMAL))

    elems.append(h3("IV. Rechtliche Begründung"))
    elems.append(h3("§ 656a BGB — Textformerfordernis für Maklervertrag"))
    elems.append(p(
        "Gemäß § 656a BGB bedarf ein Maklervertrag, durch den ein Verbraucher den Makler "
        "mit der Vermittlung oder dem Nachweis der Gelegenheit zum Abschluss eines Vertrages "
        "über den Erwerb oder die Veräußerung einer Wohnung oder eines Einfamilienhauses "
        "beauftragt, der Textform. Der Maklervertrag ist gemäß § 656a BGB formbedürftig; "
        "§ 125 BGB ordnet bei Nichtbeachtung Nichtigkeit an.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "Textform im Sinne des § 126b BGB setzt voraus, dass eine lesbare Erklärung, in der "
        "die Person des Erklärenden genannt ist, auf einem dauerhaften Datenträger abgegeben "
        "wird. Entscheidend ist dabei, dass die Erklärung auch inhaltlich hinreichend bestimmt "
        "ist, d.h. zumindest die wesentlichen Vertragsbestandteile (§§ 154 f. BGB) — mithin "
        "Leistungspflicht des Maklers, Art der geschuldeten Tätigkeit und Vergütung — erkennbar "
        "beschreibt. Die bloße Zustimmung zur Vereinbarung eines Notartermins genügt diesen "
        "Anforderungen nicht.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "Der BGH hat in seiner Entscheidung vom 29. Juni 2023 (I ZR 197/22, BGHZ 237, 311) "
        "ausgesprochen, dass der Schutzzweck des § 656a BGB eine strenge Auslegung des "
        "Textformerfordernisses gebietet: Der Verbraucher soll vor übereilten Bindungen "
        "geschützt werden, weshalb eine konkludente Annahme eines Maklervertragsan-gebots "
        "durch faktisches Tätigwerden nicht ausreiche, wenn keine den Anforderungen des § 126b "
        "BGB genügende Erklärung vorliegt (vgl. auch BGH, Urt. v. 03. November 2022, "
        "I ZR 120/21, NJW 2023, 370).", S_NORMAL))

    elems.append(h3("§ 812 Abs. 1 BGB — Kondiktionsanspruch"))
    elems.append(p(
        "Da der Verkäufer-Maklervertrag mangels Textform nichtig ist (§ 125 BGB), fehlt es "
        "an einem Rechtsgrund für die geleistete Zahlung von EUR 8.810,76. Die Kläger haben "
        "diese Summe ohne rechtlichen Grund erbracht, § 812 Abs. 1 S. 1 Alt. 1 BGB "
        "(condictio indebiti). Bereicherungseinwände — namentlich Entreicherung gemäß "
        "§ 818 Abs. 3 BGB — stehen der Beklagten nicht zu, da der Bereicherungsausschluss "
        "aufgrund der Bösgläubigkeit der Beklagten (§ 819 BGB) greift: Die Beklagte wusste "
        "als Unternehmerin und Rechtskundige, dass der Formverstoß die Nichtigkeit des "
        "Maklervertrags bewirkte.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "Hilfsweise ergibt sich der Ausschluss des Entreicherungseinwands aus dem "
        "Schutzzweck des § 656a BGB (vgl. BGH I ZR 197/22 a.a.O.): Würde man dem Makler "
        "gestatten, sich auf Entreicherung zu berufen, würde der durch § 656a BGB bezweckte "
        "Verbraucherschutz vollständig leerlaufen. Der Makler könnte die Provision vereinnahmen, "
        "verbrauchen und sodann auf Entreicherung pochen — genau dieses Ergebnis soll § 656a "
        "BGB verhindern.", S_NORMAL))

    elems.append(h3("V. Streitwert und Zinsen"))
    elems.append(p(
        "Der Streitwert beläuft sich auf EUR 8.810,76. Zinsen sind gemäß §§ 286, 288 Abs. 1 "
        "BGB seit dem 15. Mai 2023 (Zahlungstag) in Höhe von 5 Prozentpunkten über dem "
        "jeweiligen Basiszinssatz geschuldet. Mit Ablauf der Zahlungsaufforderungsfrist "
        "vom 03./17. August 2023 trat spätestens Verzug ein.", S_NORMAL))
    elems.append(sp(0.3))

    elems.append(h2("Beweisangebote"))
    beweise = [
        "Anlage K-MAK-1: Screenshot E-Mail Bechtholdsmeier an Haspelbeck, 03.04.2023",
        "Anlage K-MAK-2: Screenshot E-Mail Haspelbeck an Bechtholdsmeier, 13.04.2023",
        "Anlage K-MAK-3: Provisionsrechnung Bechtholdsmeier, 15.05.2023",
        "Anlage K-MAK-4: Widerrufsschreiben RA Hagelbrand-Wittlsbach, 03.08.2023",
        "Anlage K-MAK-5: Zurückweisung RAin Korkenzieher-Mariastein, 12.08.2023",
        "Anlage K-MAK-6: Kontoauszug Zahlungsbeleg Haspelbeck, 29.05.2023",
        "Anlage K-MAK-7: <i>Sonderband II — nicht abgebildet</i> (Vollmacht Maklervertrag Käufer)",
        "Anlage K-MAK-8: Notarieller Kaufvertrag UR-Nr. 1488/2023 (Auszug)",
        "Zeugnis: Notar Dr. Ulfried Vorstetter, Maximilianstraße 22, 80539 München",
        "Zeugnis: Bartholomäus Höglmayr-Stockenfels (Erwerber, zum Notartermin)",
        "Parteivernehmung: Walburga Haspelbeck-Türkenfeld",
    ]
    for b in beweise:
        elems.append(p(f"• {b}", S_NORMAL))

    elems.append(sp(0.5))
    elems.append(p("München, 14. September 2023", S_NORMAL))
    elems.append(sp(0.3))
    elems.append(p("_______________________________", S_NORMAL))
    elems.append(p("Dr. Knut Hagelbrand-Wittlsbach<br/>Rechtsanwalt", S_NORMAL))
    elems.append(pb())
    return elems


def bestandteil_05_klageerwiderung():
    """5. Klageerwiderung (10 Seiten)"""
    elems = []
    elems.append(section_header("KLAGEERWIDERUNG", "Az. LG München I 12 O 8842/23"))
    elems.append(sp(0.3))
    elems.append(kanzlei_logo_km())
    elems.append(sp(0.2))

    ta = Table([[p("An das\nLandgericht München I\n12. Zivilkammer\nPrielmayerstraße 7\n80335 München", S_NORMAL),
                 p("München, 24. Oktober 2023", make_style("DRK", fontName="Helvetica",
                    fontSize=10, leading=14, alignment=TA_RIGHT, textColor=C_GRAU))]],
               colWidths=[10*cm, 6.5*cm])
    elems.append(ta)
    elems.append(sp(0.4))

    for elem in rubrum_block(
        "Eheleute Korbinian und Walburga Haspelbeck-Türkenfeld, Mauerkircherstraße 47, 81679 München",
        "Immobilien-Vermittlung „Marlene Bechtholdsmeier-Schongau e.K.", Schwere-Reiter-Straße 18, 80637 München",
        "LG München I 12 O 8842/23", "Landgericht München I, 12. Zivilkammer"):
        elems.append(elem)
    elems.append(sp(0.3))

    elems.append(p(
        "Die Beklagte erwidert auf die Klage vom 14. September 2023 wie folgt und beantragt:", S_NORMAL))
    elems.append(sp(0.2))

    # Anträge
    antraege = [
        "1. Die Klage wird abgewiesen.",
        "2. Die Kläger tragen die Kosten des Rechtsstreits.",
        "3. Das Urteil ist vorläufig vollstreckbar.",
    ]
    for a in antraege:
        at = Table([[p(a, S_NORMAL)]], colWidths=[16.5*cm])
        at.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), HexColor("#FFF8F8")),
            ("LEFTPADDING", (0,0), (-1,-1), 16),
            ("RIGHTPADDING", (0,0), (-1,-1), 10),
            ("TOPPADDING", (0,0), (-1,-1), 6),
            ("BOTTOMPADDING", (0,0), (-1,-1), 6),
            ("BOX", (0,0), (-1,-1), 0.5, C_AKZENT),
        ]))
        elems.append(at)
        elems.append(sp(0.15))

    elems.append(sp(0.4))
    elems.append(h2("I. Zum Sachverhalt aus Sicht der Beklagten"))
    elems.append(p(
        "Die Kläger verkennen die tatsächlichen und rechtlichen Grundlagen ihres Rückforderungsanspruchs. "
        "Die Beklagte hat die Kläger von Beginn an vollständig und transparent über die anfallende "
        "Provision informiert. Zwischen den Parteien bestand über Monate ein intensiver persönlicher "
        "und fernmündlicher Kontakt; Frau Bechtholdsmeier-Schongau hat die Kläger mehrfach — auch "
        "telefonisch — auf die anfallende Provision beim Verkauf hingewiesen.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "Die E-Mail vom 03. April 2023 enthielt einen eindeutigen, klar lesbaren Hinweis auf die "
        "Provisionspflicht. Dieser Hinweis stand — entgegen der Behauptung der Kläger — nicht "
        "„unterhalb der Signatur", sondern war integraler Bestandteil der Korrespondenz, da er "
        "vor der Schlussformel der E-Mail eingebettet war. Die Kläger haben diesen Hinweis "
        "ausdrücklich zur Kenntnis genommen, wie ihre Antwort-E-Mail vom 13. April 2023 belegt, "
        "in der sie „wie besprochen" der Tätigkeit der Beklagten zustimmten.", S_NORMAL))

    elems.append(h2("II. Textform gewahrt — § 656a BGB i.V.m. § 126b BGB"))
    elems.append(h3("1. Systematische Einordnung"))
    elems.append(p(
        "§ 656a BGB schreibt Textform im Sinne von § 126b BGB vor. Textform bedeutet, dass eine "
        "lesbare Erklärung, in der die Person des Erklärenden genannt ist, auf einem dauerhaften "
        "Datenträger abgegeben wird. Eine E-Mail genügt diesen Anforderungen (vgl. BT-Drs. 19/15827, "
        "S. 17). Eine elektronische Mitteilung ist ein dauerhafter Datenträger im Sinne des § 126b S. 2 BGB, "
        "wenn sie dauerhaft gespeichert werden kann.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "Die E-Mail-Kette der Parteien vom 03./13. April 2023 enthält: (a) die Erklärung des Erklärenden "
        "(Bechtholdsmeier-Schongau e.K.), (b) die wesentlichen Vertragsbestandteile (Provisionshöhe, "
        "Fälligkeit, Objekt) sowie (c) die Zustimmungserklärung der Kläger. Mehr ist für § 126b BGB "
        "nicht erforderlich.", S_NORMAL))

    elems.append(h3("2. Bestimmtheit der Erklärung"))
    elems.append(p(
        "Die Kläger rügen, die Erklärung sei zu unbestimmt. Dies trifft nicht zu. Die E-Mail vom "
        "03. April 2023 nennt: das Objekt (Mauerkircherstraße 47), die Provisionshöhe (maximal 3,7 % "
        "je Partei inkl. MwSt.) und die Fälligkeitsbedingung (Abschluss eines Kaufvertrages). "
        "Die Antwort der Kläger vom 13. April 2023 bezieht sich auf diese Korrespondenz zurück "
        "(„wie besprochen") und stellt eine Annahmeerklärung dar. Die Kläger als geschäftserfahrene "
        "Immobilieneigentümer (das Objekt wird seit 2008 von ihnen gehalten) kannten die "
        "Provisionsüblichkeit im Münchner Markt.", S_NORMAL))

    elems.append(h3("3. Notarielle Maklerklausel § 13 des Kaufvertrages (Hilfserwägung)"))
    elems.append(p(
        "Selbst wenn man dem Kläger-Vortrag zur fehlenden Textform im E-Mail-Verkehr folgen würde "
        "(was ausdrücklich bestritten wird), wäre der Maklervertrag jedenfalls durch die Maklerklausel "
        "in § 13 des notariellen Kaufvertrags UR-Nr. 1488/2023 wirksam zustande gekommen. Der Notar "
        "Dr. Vorstetter hat in § 13 Abs. 1 des Kaufvertrags den Provisionsanspruch der Beklagten "
        "ausdrücklich festgehalten und beide Parteien — mithin auch die Kläger als Veräußerer — "
        "haben durch ihre Unterschrift unter den Kaufvertrag die Maklerklausel anerkannt. "
        "Diese notarielle Beurkundung wahrt die Textform des § 126b BGB und sogar die strengere "
        "Form des § 128 BGB.", S_NORMAL))

    elems.append(h3("4. Hilfsweise: Wertersatzanspruch der Beklagten"))
    elems.append(p(
        "Sollte der Maklervertrag formunwirksam sein — was bestritten wird —, so hat die Beklagte "
        "tatsächlich eine Leistung erbracht, die zum Verkaufserfolg führte. Die Kläger haben einen "
        "Vermögensvorteil in Gestalt des erzielten Kaufpreises von EUR 617.000,00 erlangt, der ohne "
        "die Vermittlungsleistung der Beklagten nicht oder nicht zu diesem Preis erzielt worden wäre. "
        "Die Beklagte wäre in diesem Fall auf einen Wertersatzanspruch gemäß § 818 Abs. 2 BGB "
        "verwiesen, der dem Rückforderungsanspruch als rechtshemmende Einrede entgegensteht.", S_NORMAL))

    elems.append(h3("5. Hilfsweise: Entreicherung gemäß § 818 Abs. 3 BGB"))
    elems.append(p(
        "Die Beklagte hat die vereinnahmte Provision für Betriebsausgaben verwendet — namentlich "
        "für Bürokosten, Werbemaßnahmen und Personalaufwand, die im Zusammenhang mit der "
        "Vermittlungstätigkeit für die Kläger entstanden sind. Soweit die Beklagte noch bereichert "
        "ist, übersteigt dieser Betrag nicht EUR 1.200,00. Eine weitergehende Rückzahlungspflicht "
        "besteht daher nicht (§ 818 Abs. 3 BGB). Der Entreicherungseinwand ist substanziiert "
        "vorgetragen; der Nachweis wird im Hauptsacheverfahren durch Vorlage der Buchhaltungsunterlagen "
        "erbracht.", S_NORMAL))

    elems.append(h2("III. Zum Widerruf"))
    elems.append(p(
        "Der erklärte Widerruf vom 03. August 2023 ist verspätet und geht ins Leere. Selbst wenn "
        "§ 312g BGB anwendbar wäre (was bei einem außerhalb von Geschäftsräumen geschlossenen "
        "Maklervertrag diskutiert wird), war die Widerrufsfrist von 14 Tagen ab Vertragsschluss "
        "(§ 355 Abs. 2 S. 1 BGB) im April 2023 abgelaufen. Der Widerruf im August 2023 — nach "
        "vollständiger Abwicklung des Kaufvertrags und Zahlung der Provision — ist ersichtlich "
        "taktisch motiviert und stellt eine unzulässige Rechtsausübung gemäß § 242 BGB dar "
        "(venire contra factum proprium).", S_NORMAL))

    elems.append(sp(0.5))
    elems.append(p("München, 24. Oktober 2023", S_NORMAL))
    elems.append(sp(0.3))
    elems.append(p("_______________________________<br/>Dr. Adelheid Korkenzieher-Mariastein<br/>"
                    "Rechtsanwältin, Korkenzieher Maibach Partner mbB", S_NORMAL))
    elems.append(pb())
    return elems


def bestandteil_06_replik():
    """6. Replik Kläger (6 Seiten)"""
    elems = []
    elems.append(section_header("REPLIK DER KLÄGER", "Az. LG München I 12 O 8842/23"))
    elems.append(sp(0.3))
    elems.append(kanzlei_logo_ht())
    elems.append(sp(0.3))

    elems.append(p(
        "Die Kläger replizieren auf die Klageerwiderung vom 24. Oktober 2023 wie folgt:", S_NORMAL))
    elems.append(sp(0.3))

    elems.append(h2("I. Zur behaupteten Textformwahrung durch die E-Mail-Korrespondenz"))
    elems.append(p(
        "Die Beklagte versucht darzulegen, der Provisionshinweis in der E-Mail vom 03. April 2023 "
        "sei inhaltlich hinreichend bestimmt, um als Angebot zum Abschluss eines Maklervertrags "
        "in Textform zu gelten. Dies ist aus mehreren Gründen unzutreffend.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "Erstens: Der Hinweistext stand unstreitig unterhalb der Signatur der Beklagten. "
        "Dies ergibt sich aus der Formatierung der E-Mail (Anlage K-MAK-1): Nach dem "
        "persönlichen Grußwort und der vollständigen Signaturzeile erscheint der Provisionstext "
        "als abgesetzter Absatz. Die Anforderungen des § 126b S. 1 BGB verlangen, dass der "
        "Erklärende erkennbar ist. Wenn die Signatur die Erklärung des Erklärenden abschließt "
        "und der Provisionshinweis als boilerplate nach der Signatur erscheint, ist das "
        "Zuordnungsverhältnis zwischen Erklärung und Erklärendem nicht gegeben.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "Zweitens: Selbst wenn man die Signatur-Positionierung als unschädlich ansähe, genügt "
        "die Formulierung nicht den Anforderungen an einen wirksamen Vertragsantrag. "
        "Ein Vertragsangebot muss so bestimmt sein, dass die Annahme mit einem schlichten „Ja" "
        "erfolgen kann (§ 145 BGB). Der Provisionshinweis enthält weder eine eindeutige "
        "Leistungsbeschreibung der Maklertätigkeit noch eine Festlegung der konkreten "
        "Provisionshöhe (lediglich „maximal" 3,7 %). Die Unbestimmtheit ist kein "
        "Auslegungsproblem, sondern macht den vermeintlichen Antrag zum bloßen invitatio "
        "ad offerendum.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "Drittens: Die Antwort-E-Mail der Kläger vom 13. April 2023 bezieht sich erkennbar "
        "nur auf die Vereinbarung des Notartermins — nicht auf den Provisionshinweis. "
        "Die Formulierung „wie besprochen stimmen wir zu, dass Sie den Notartermin vereinbaren" "
        "ist eindeutig auf die logistische Frage der Terminkoordinierung bezogen. "
        "Eine Auslegung als Annahme eines Maklervertragsangebots scheidet schon deshalb aus, "
        "weil die Kläger den Provisionshinweis weder erwähnen noch darauf Bezug nehmen.", S_NORMAL))

    elems.append(h2("II. Zur Maklerklausel im Kaufvertrag"))
    elems.append(p(
        "Die Beklagte stützt sich hilfsweise auf § 13 des Kaufvertrags UR-Nr. 1488/2023. "
        "Dieser Ansatz scheitert jedoch daran, dass § 656a BGB einen eigenständigen, "
        "vor dem Kaufvertragsabschluss zu schließenden Maklervertrag voraussetzt. "
        "Die nachträgliche Feststellung in einer Kaufvertragsklausel kann den vorher "
        "erforderlichen (und fehlenden) Vertragsschluss nicht ersetzen. "
        "BGH I ZR 197/22, Rz. 28 ff., hat ausdrücklich klargestellt, dass § 656a BGB "
        "ein Formerfordernis für den Maklervertrag selbst normiert, nicht für eine "
        "nachträgliche Provisionsanerkenntnis.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "Zudem ist zu berücksichtigen, dass die Kläger beim Notartermin unter Zeitdruck "
        "standen und die Klausel in § 13 des Kaufvertrags nicht gesondert verhandelt wurde. "
        "Der Notar hat die Klausel lediglich vorgelesen, nicht aber die Kläger ausdrücklich "
        "auf die Folgewirkung für den Maklervertrag hingewiesen. Die Unterschrift unter "
        "den Kaufvertrag kann daher nicht als rechtsgeschäftliche Billigung des "
        "Maklervertragsinhalts verstanden werden.", S_NORMAL))

    elems.append(h2("III. Zum Bereicherungsausschluss"))
    elems.append(p(
        "Die Beklagte beruft sich auf § 818 Abs. 3 BGB (Entreicherung). "
        "Dieser Einwand scheitert an § 819 BGB: Da die Beklagte als gewerbliche Maklerin "
        "und Unternehmerin wusste, dass § 656a BGB die Textform vorschreibt, und da sie "
        "ihre Vertragsgestaltung nicht an diesem Erfordernis ausgerichtet hat, handelte sie "
        "in Kenntnis des Mangels (§ 819 Abs. 1 BGB). Sie haftet daher wie ein "
        "bösgläubiger Bereicherungsschuldner und kann Entreicherung nicht einwenden.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "Hilfsweise gilt: Der Schutzzweck des § 656a BGB gebietet es, den Entreicherungseinwand "
        "auszuschließen. § 656a BGB wurde durch das Gesetz über die Verteilung der "
        "Maklerkosten bei der Vermittlung von Kaufverträgen über Wohnungen und "
        "Einfamilienhäuser vom 12. Juni 2020 (BGBl. I S. 1245) eingefügt. "
        "Der Gesetzgeber wollte mit der Textformvorschrift sicherstellen, dass Verbraucher "
        "nicht unbemerkt in Provisionsverbindlichkeiten hineingezogen werden. "
        "Diesen Schutzzweck unterliefe es, wenn der Makler — trotz formungültigem Vertrag — "
        "durch Berufung auf § 818 Abs. 3 BGB faktisch in den Genuss der Provision käme.", S_NORMAL))

    elems.append(h2("IV. Zum Widerruf"))
    elems.append(p(
        "Entgegen der Ansicht der Beklagten war der Widerruf vom 03. August 2023 nicht "
        "verspätet. Nach § 356 Abs. 3 S. 2 BGB erlischt das Widerrufsrecht nicht, wenn "
        "der Unternehmer den Verbraucher nicht ordnungsgemäß über das Widerrufsrecht "
        "belehrt hat. Eine ordnungsgemäße Widerrufsbelehrung für den Verkäufer-Maklervertrag "
        "lag unstreitig nicht vor — die Beklagte hat lediglich für den Käufer-Maklervertrag "
        "(Februar 2023) eine Widerrufsbelehrung übermittelt. Für den hier streitgegenständlichen "
        "Verkäufer-Maklervertrag fehlt jede Belehrung.", S_NORMAL))
    elems.append(sp(0.5))
    elems.append(p("München, 17. November 2023", S_NORMAL))
    elems.append(sp(0.3))
    elems.append(p("Dr. Knut Hagelbrand-Wittlsbach, Rechtsanwalt", S_NORMAL))
    elems.append(pb())
    return elems


def bestandteil_07_email_kette():
    """7. E-Mail-Kette (8 Seiten)"""
    elems = []
    elems.append(section_header("E-MAIL-KETTE HASPELBECK ↔ BECHTHOLDSMEIER",
                                 "Anlage K-MAK-1 bis K-MAK-2 / Relevanter Zeitraum März–August 2023"))
    elems.append(sp(0.3))
    elems.append(p("<i>Hinweis: Die nachfolgenden E-Mails entsprechen dem Inhalt der als Anlage "
                    "K-MAK-1 und K-MAK-2 vorgelegten Screenshots. Hervorhebungen in [eckigen Klammern] "
                    "sind redaktionelle Ergänzungen des Unterfertigten.</i>", S_KLEIN))
    elems.append(sp(0.4))

    # E-Mail 1
    elems.append(h3("E-Mail 1 — 30. März 2023, 14:47 Uhr"))
    for e in email_block(
        von="korbinian.haspelbeck@haspelbeck-tuerkenfeld.de",
        an="makler@bechtholdsmeier-schongau-immo.de",
        datum="Montag, 30. März 2023, 14:47 Uhr",
        betreff="Gegenangebot Mauerkircherstraße 47",
        body_lines=[
            "Sehr geehrte Frau Bechtholdsmeier-Schongau,",
            "",
            "wie gestern telefonisch besprochen, teilen wir Ihnen mit, dass wir",
            "das Angebot der Familie Höglmayr-Stockenfels in Höhe von EUR 590.000,00",
            "als zu niedrig erachten. Wir sind bereit, das Objekt zu einem Kaufpreis",
            "von EUR 620.000,00 zu veräußern, mindestens jedoch EUR 617.000,00.",
            "",
            "Bitte setzen Sie die Verhandlungen entsprechend fort und halten Sie uns",
            "auf dem Laufenden.",
            "",
            "Mit freundlichen Grüßen",
            "Korbinian und Walburga Haspelbeck-Türkenfeld",
            "Mauerkircherstraße 47, 81679 München",
            "Tel.: +49 89 2211 9340",
        ]
    ):
        elems.append(e)
    elems.append(sp(0.5))

    # E-Mail 2 — kritische Mail mit Provisionshinweis
    elems.append(h3("E-Mail 2 — 03. April 2023, 09:12 Uhr [ANLAGE K-MAK-1 — STREITGEGENSTÄNDLICH]"))
    for e in email_block(
        von="makler@bechtholdsmeier-schongau-immo.de",
        an="korbinian.haspelbeck@haspelbeck-tuerkenfeld.de",
        datum="Montag, 03. April 2023, 09:12 Uhr",
        betreff="AW: Gegenangebot Mauerkircherstraße 47 — Rückmeldung Höglmayr-Stockenfels",
        body_lines=[
            "Sehr geehrte Frau Haspelbeck-Türkenfeld, sehr geehrter Herr Haspelbeck-Türkenfeld,",
            "",
            "ich habe die Verhandlungen mit Familie Höglmayr-Stockenfels fortgesetzt.",
            "Die Interessenten sind zu einem Kaufpreis von EUR 617.000,00 bereit.",
            "Ich empfehle Ihnen, dieses Angebot anzunehmen — der Münchner Markt",
            "ist derzeit volatil, und EUR 617.000 liegt im oberen Bereich der",
            "Vergleichswerte für vergleichbare Lagen in Bogenhausen.",
            "",
            "Ich schlage vor, zeitnah einen Notartermin zu vereinbaren. Bitte geben",
            "Sie mir grünes Licht, damit ich mit dem Notariat Dr. Vorstetter Kontakt",
            "aufnehmen kann.",
            "",
            "Mit freundlichen Grüßen",
            "Marlene Bechtholdsmeier-Schongau",
            "Immobilien-Vermittlung Bechtholdsmeier-Schongau e.K.",
            "Schwere-Reiter-Straße 18, 80637 München",
            "Tel.: +49 89 5551 8800 | Web: www.bechtholdsmeier-schongau-immo.de",
            "",
            "────────────────────────────────────────────────────────────────────",
            "PROVISIONSHINWEIS (automatisch hinzugefügt):",
            "Wir weisen darauf hin, dass bei Abschluss eines Kaufvertrages bei einem",
            "Einfamilienhaus eine vom Veräußerer und Erwerber zu zahlende Provision",
            "fällig wird. Diese beläuft sich maximal auf drei Komma sieben Prozent des",
            "Kaufpreises (inklusive gesetzlicher Mehrwertsteuer und je Partei),",
            "im Verkaufsfall des von Ihnen veräußerten Objektes Mauerkircherstraße 47.",
            "Bei Zustandekommen des Kaufvertrages wird die Provision innerhalb von",
            "14 Tagen nach Beurkundung fällig.",
            "────────────────────────────────────────────────────────────────────",
        ]
    ):
        elems.append(e)
    elems.append(sp(0.3))

    # Anmerkung im Akt (handschriftlich simuliert)
    elems.append(p(
        "<i>[Handschr. Notiz, Korbinian Haspelbeck, am Rand:] "
        "Das ist doch der Automations-Text! Hatten wir das nicht gefragt? "
        "Walburga sagt: stand das auch beim Käufer-Vertrag?? Ich glaub schon!</i>",
        S_KURSIV))
    elems.append(sp(0.5))

    # E-Mail 3
    elems.append(h3("E-Mail 3 — 13. April 2023, 16:33 Uhr [ANLAGE K-MAK-2 — STREITGEGENSTÄNDLICH]"))
    for e in email_block(
        von="korbinian.haspelbeck@haspelbeck-tuerkenfeld.de",
        an="makler@bechtholdsmeier-schongau-immo.de",
        datum="Donnerstag, 13. April 2023, 16:33 Uhr",
        betreff="AW: AW: Gegenangebot Mauerkircherstraße 47",
        body_lines=[
            "Sehr geehrte Frau Bechtholdsmeier-Schongau,",
            "",
            "wie besprochen stimmen wir zu, dass Sie den Notartermin vereinbaren.",
            "",
            "Mit freundlichen Grüßen",
            "Korbinian und Walburga Haspelbeck-Türkenfeld",
        ]
    ):
        elems.append(e)
    elems.append(sp(0.3))
    elems.append(p(
        "<i>[Anmerkung RA Hagelbrand-Wittlsbach:] "
        "Kein ausdrücklicher Bezug auf Provision. Zustimmung bezieht sich erkennbar "
        "nur auf Notartermin-Vereinbarung. Provisionshinweis in K-MAK-1 steht nach Signatur "
        "— vgl. Screenshot-Vergrößerung Anlage K-MAK-1a (Sonderband II).</i>", S_KURSIV))
    elems.append(sp(0.5))

    # E-Mail 4
    elems.append(h3("E-Mail 4 — 14. April 2023 — Bechtholdsmeier an Notar Vorstetter (CC Haspelbeck)"))
    for e in email_block(
        von="makler@bechtholdsmeier-schongau-immo.de",
        an="kanzlei@notar-vorstetter-maximilianstr.de",
        datum="Freitag, 14. April 2023, 10:05 Uhr",
        betreff="Terminanfrage Kaufvertrag Mauerkircherstraße 47 / Haspelbeck — Höglmayr-Stockenfels",
        cc="korbinian.haspelbeck@haspelbeck-tuerkenfeld.de; bartholomaeus.hoeglmayr@hoeglmayr-stockenfels.de",
        body_lines=[
            "Sehr geehrter Herr Doktor Vorstetter,",
            "",
            "ich bitte um Vereinbarung eines Notartermins für folgenden Kaufvertrag:",
            "Veräußerer: Eheleute Haspelbeck-Türkenfeld",
            "Erwerber:   Eheleute Höglmayr-Stockenfels",
            "Objekt:     Mauerkircherstraße 47, 81679 München",
            "            EFH, ca. 185 m² Wfl., Grundstück ca. 560 m²",
            "Kaufpreis:  EUR 617.000,00",
            "",
            "Vorschlag: Kalenderwoche 19 (08.-12. Mai 2023)",
            "",
            "Mit freundlichen Grüßen",
            "Marlene Bechtholdsmeier-Schongau",
            "Immobilien-Vermittlung Bechtholdsmeier-Schongau e.K.",
        ]
    ):
        elems.append(e)
    elems.append(sp(0.5))

    # Protokollauszug Notartermin
    elems.append(h3("Notartermin — 12. Mai 2023 (Protokoll-Auszug)"))
    pt = Table([[p(
        "PROTOKOLL-AUSZUG — Notariat Dr. Ulfried Vorstetter<br/>"
        "Maximilianstraße 22, 80539 München<br/>"
        "UR-Nr. 1488/2023<br/><br/>"
        "Anwesend: Eheleute Haspelbeck-Türkenfeld (Veräußerer), "
        "Eheleute Höglmayr-Stockenfels (Erwerber), "
        "Frau Bechtholdsmeier-Schongau (Maklerin, ohne Stimm-/Unterzeichnungsrecht)<br/><br/>"
        "Der Notar hat den Kaufvertrag in vollem Wortlaut vorgelesen. "
        "§ 13 (Maklerklausel) wurde erläutert. Die Parteien haben keine Einwände erhoben. "
        "Der Kaufvertrag wurde von allen Erschienenen unterschrieben und notariell beglaubigt.",
        make_style("PrM", fontName="Times-Roman", fontSize=9.5, leading=14, textColor=C_GRAU)
    )]], colWidths=[16.5*cm])
    pt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#F5F5FF")),
        ("BOX", (0,0), (-1,-1), 1, C_DUNKELBLAU),
        ("LEFTPADDING", (0,0), (-1,-1), 12),
        ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    elems.append(pt)
    elems.append(sp(0.3))
    elems.append(notar_stempel())
    elems.append(sp(0.5))

    # Provisionsrechnung
    elems.append(h3("Provisionsrechnung — 15. Mai 2023"))
    for e in email_block(
        von="makler@bechtholdsmeier-schongau-immo.de",
        an="korbinian.haspelbeck@haspelbeck-tuerkenfeld.de",
        datum="Montag, 15. Mai 2023",
        betreff="Rechnung Nr. 2023/047 — Maklerprovision Mauerkircherstraße 47",
        body_lines=[
            "RECHNUNG Nr. 2023/047",
            "",
            "Immobilien-Vermittlung Bechtholdsmeier-Schongau e.K.",
            "Schwere-Reiter-Straße 18, 80637 München",
            "USt-IdNr.: DE 294 883 712",
            "",
            "An: Eheleute Korbinian und Walburga Haspelbeck-Türkenfeld",
            "    Mauerkircherstraße 47, 81679 München",
            "",
            "Leistung:   Nachweis und Vermittlung Kaufvertrag",
            "            Mauerkircherstraße 47, 81679 München",
            "            Käufer: Eheleute Höglmayr-Stockenfels",
            "            Kaufpreis: EUR 617.000,00",
            "",
            "Provision (netto):   EUR 7.404,84 (1,2 % netto von EUR 617.000,00)",
            "MwSt. 19 %:          EUR 1.406,92",
            "Brutto:              EUR 8.810,76",
            "",
            "Zahlungsziel: 14 Tage nach Rechnungsdatum",
            "IBAN: DE89 7002 0270 0012 3456 78 (Stadtsparkasse München)",
        ]
    ):
        elems.append(e)
    elems.append(sp(0.5))

    # Widerruf
    elems.append(h3("Anwaltlicher Widerruf — 03. August 2023 [ANLAGE K-MAK-4]"))
    for e in email_block(
        von="hagelbrand@ht-recht-muenchen.de",
        an="makler@bechtholdsmeier-schongau-immo.de",
        datum="Donnerstag, 03. August 2023",
        betreff="Widerruf Maklervertrag / Rückforderung Provision — Haspelbeck-Türkenfeld ./. Bechtholdsmeier-Schongau",
        body_lines=[
            "Sehr geehrte Frau Bechtholdsmeier-Schongau,",
            "",
            "in der oben genannten Sache zeige ich die Vertretung der Eheleute",
            "Haspelbeck-Türkenfeld an.",
            "",
            "Ich widerrufe namens und in Vollmacht meiner Mandanten vorsorglich",
            "jeden zwischen den Parteien geschlossenen Maklervertrag nach §§ 312g,",
            "355 BGB sowie nach § 130 Abs. 1 BGB analog.",
            "",
            "Unabhängig vom Widerruf weise ich darauf hin, dass ein wirksamer",
            "Verkäufer-Maklervertrag nicht zustande gekommen ist, da die Anforderungen",
            "des § 656a BGB i.V.m. § 126b BGB nicht gewahrt wurden.",
            "",
            "Ich fordere Sie auf, EUR 8.810,76 bis zum 17. August 2023",
            "auf das Konto meiner Mandanten zu überweisen:",
            "IBAN: DE22 7005 0000 0099 9876 54 (Bayerische Landesbank)",
            "",
            "Andernfalls werde ich Klage erheben.",
            "",
            "Dr. Knut Hagelbrand-Wittlsbach, Rechtsanwalt",
            "Hagelbrand & Trotzenburg Rechtsanwälte, Promenadeplatz 9, 80333 München",
        ]
    ):
        elems.append(e)
    elems.append(sp(0.5))

    # Zurückweisung
    elems.append(h3("Zurückweisung — 12. August 2023 [ANLAGE K-MAK-5]"))
    for e in email_block(
        von="korkenzieher@korkenzieher-maibach.de",
        an="hagelbrand@ht-recht-muenchen.de",
        datum="Samstag, 12. August 2023",
        betreff="AW: Widerruf Maklervertrag — Haspelbeck-Türkenfeld ./. Bechtholdsmeier-Schongau",
        body_lines=[
            "Sehr geehrter Herr Kollege Dr. Hagelbrand-Wittlsbach,",
            "",
            "ich zeige die Vertretung von Frau Bechtholdsmeier-Schongau an.",
            "",
            "Sämtliche von Ihnen geltend gemachten Ansprüche werden zurückgewiesen.",
            "Der Maklervertrag ist wirksam zustande gekommen. Der Widerruf ist verspätet",
            "und geht ins Leere. Eine Rückzahlung der Provision wird nicht erfolgen.",
            "",
            "Weitere Korrespondenz in dieser Sache ist nur noch gerichtlich zu führen.",
            "",
            "Dr. Adelheid Korkenzieher-Mariastein, Rechtsanwältin",
            "Korkenzieher Maibach Partner mbB, Karlsplatz 4, 80335 München",
        ]
    ):
        elems.append(e)
    elems.append(pb())
    return elems


def bestandteil_08_kaufvertrag_auszug():
    """8. Notarieller Kaufvertrag-Auszug"""
    elems = []
    elems.append(section_header("NOTARIELLER KAUFVERTRAG-AUSZUG", "UR-Nr. 1488/2023 — Notar Dr. Ulfried Vorstetter"))
    elems.append(sp(0.3))

    # Notar-Stempel oben
    stempel_row = Table([[notar_stempel()]], colWidths=[16.5*cm])
    stempel_row.setStyle(TableStyle([("ALIGN",(0,0),(-1,-1),"LEFT")]))
    elems.append(stempel_row)
    elems.append(sp(0.4))

    elems.append(p("<b>KAUFVERTRAG</b>", S_ZENTRIERT_FETT))
    elems.append(p("Urkundenrolle Nr. 1488/2023", S_ZENTRIERT))
    elems.append(sp(0.3))
    elems.append(p(
        "Verhandelt zu München am 12. Mai 2023 vor mir, Notar Dr. Ulfried Vorstetter, "
        "mit dem Amtssitz in München, Maximilianstraße 22, 80539 München.", S_RUBRUM))
    elems.append(sp(0.2))
    elems.append(p(
        "Erschienen sind:", S_RUBRUM_FETT))
    elems.append(p(
        "1. Herr Korbinian Josef Maria Haspelbeck-Türkenfeld, geboren am 14. März 1971, "
        "wohnhaft Mauerkircherstraße 47, 81679 München, ausgewiesen durch Personalausweis "
        "Nr. L31V9P3T0, und", S_RUBRUM))
    elems.append(p(
        "2. Frau Walburga Anna Haspelbeck-Türkenfeld geb. Brandlberger, geboren am 22. Juli 1974, "
        "dieselbe Anschrift, ausgewiesen durch Personalausweis Nr. T82WQ4R1K, "
        "— nachfolgend gemeinsam „Veräußerer" —", S_RUBRUM))
    elems.append(p("sowie:", S_RUBRUM_FETT))
    elems.append(p(
        "3. Herr Bartholomäus Ignaz Höglmayr-Stockenfels, geboren am 03. September 1978, "
        "wohnhaft Großhesseloher Straße 12, 81479 München-Solln, und", S_RUBRUM))
    elems.append(p(
        "4. Frau Hiltrud Maria Höglmayr-Stockenfels geb. Ranzenberger, geboren am 11. Februar 1981, "
        "dieselbe Anschrift, — nachfolgend gemeinsam „Erwerber" —", S_RUBRUM))
    elems.append(sp(0.3))
    elems.append(hr())

    elems.append(h3("§ 1 — Vertragsgegenstand"))
    elems.append(p(
        "Die Veräußerer sind Eigentümer des im Grundbuch des Amtsgerichts München, "
        "Blatt 88473, Gemarkung Bogenhausen, Flurnummer 1122/14, eingetragenen "
        "Grundstücks mit aufstehendem Einfamilienhaus, Anschrift Mauerkircherstraße 47, "
        "81679 München, mit einer Grundstücksgröße von ca. 560 m² und einer Wohnfläche "
        "des aufstehenden Gebäudes von ca. 185 m² (Baujahr 1973, letzte Kernsanierung 2009). "
        "Die Veräußerer veräußern und die Erwerber erwerben das vorbezeichnete Grundstück "
        "mit aufstehendem Gebäude nebst allen Zubehörstücken und wesentlichen Bestandteilen "
        "zu den nachfolgenden Bedingungen.", S_RUBRUM))

    elems.append(h3("§ 2 — Kaufpreis und Fälligkeit"))
    elems.append(p(
        "Der Kaufpreis beträgt EUR 617.000,00 (in Worten: sechshundertsiebzehn tausend Euro). "
        "Der Kaufpreis ist auf das Anderkonto des Notars (IBAN: DE09 7005 0000 0012 3456 78) "
        "innerhalb von vier Wochen nach heutiger Beurkundung zu überweisen.", S_RUBRUM))

    elems.append(p("[... §§ 3–12 nicht abgebildet — vgl. Sonderband II ...]",
                    make_style("ELL", fontName="Helvetica-Oblique", fontSize=9,
                                textColor=HexColor("#999999"), leading=14)))

    elems.append(h3("§ 13 — Maklerprovision [STREITGEGENSTÄNDLICHE KLAUSEL]"))
    klausel = Table([[p(
        "<b>§ 13 Maklerklausel</b><br/><br/>"
        "(1) Die Veräußerer und die Erwerber bestätigen, dass die Vermittlung des vorliegenden "
        "Kaufvertrages durch die Immobilien-Vermittlung Marlene Bechtholdsmeier-Schongau e.K., "
        "Schwere-Reiter-Straße 18, 80637 München (nachfolgend „Maklerin"), erfolgt ist.<br/><br/>"
        "(2) Die Veräußerer schulden der Maklerin eine Provision in Höhe von 1,2 % des "
        "Kaufpreises (EUR 617.000,00) inklusive gesetzlicher Mehrwertsteuer, mithin "
        "EUR 8.810,76 brutto. Die Erwerber schulden der Maklerin eine gesonderte Provision "
        "in gleicher Höhe (EUR 8.810,76 brutto).<br/><br/>"
        "(3) Die Provision wird 14 Tage nach Beurkundung fällig.<br/><br/>"
        "(4) Die Parteien bestätigen, mit der Maklerin einen entsprechenden Maklervertrag "
        "geschlossen zu haben.",
        make_style("Klausel", fontName="Times-Roman", fontSize=9.5, leading=15, textColor=C_GRAU,
                    leftIndent=8, rightIndent=8)
    )]], colWidths=[16.5*cm])
    klausel.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#FFFEF0")),
        ("BOX", (0,0), (-1,-1), 2, C_AKZENT),
        ("LEFTPADDING", (0,0), (-1,-1), 12),
        ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    elems.append(klausel)
    elems.append(sp(0.3))
    elems.append(p(
        "<i>[Anmerkung RA Hagelbrand-Wittlsbach:] Die Bestätigung in § 13 Abs. 4 setzt "
        "das Bestehen eines Maklervertrags voraus, kann ihn aber nicht ersetzen. "
        "BGH I ZR 197/22, Rz. 31: Nachträgliche kaufvertragliche Klausel genügt § 656a "
        "BGB nicht.</i>", S_KURSIV))
    elems.append(sp(0.5))
    elems.append(notar_stempel())
    elems.append(pb())
    return elems


def bestandteil_09_quittung():
    """9. Quittung"""
    elems = []
    elems.append(section_header("QUITTUNG — ZAHLUNGSBELEG", "Maklerprovision EUR 8.810,76 / Anlage K-MAK-3 + K-MAK-6"))
    elems.append(sp(1))

    q_data = [
        ["QUITTUNG", ""],
        ["Aussteller:", "Immobilien-Vermittlung Marlene Bechtholdsmeier-Schongau e.K."],
        ["", "Schwere-Reiter-Straße 18, 80637 München"],
        ["", "USt-IdNr.: DE 294 883 712"],
        ["Zahlender:", "Eheleute Korbinian und Walburga Haspelbeck-Türkenfeld"],
        ["", "Mauerkircherstraße 47, 81679 München"],
        ["Betrag:", "EUR 8.810,76 (acht tausend achthundert zehn Euro 76/100)"],
        ["Verwendungszweck:", "Maklerprovision Verkauf Mauerkircherstraße 47"],
        ["", "Rechnung Nr. 2023/047 vom 15. Mai 2023"],
        ["Zahlungsdatum:", "29. Mai 2023"],
        ["Zahlungsart:", "Banküberweisung (IBAN bestätigt)"],
        ["Betrag erhalten:", "JA — vollständig eingegangen am 29.05.2023"],
        ["Ort/Datum:", "München, 29. Mai 2023"],
        ["Unterschrift:", "___________________________"],
        ["", "Marlene Bechtholdsmeier-Schongau"],
    ]
    td = [[p(r[0], S_FETT if r[0] not in ("", "QUITTUNG") else
              (make_style("QH", fontName="Helvetica-Bold", fontSize=18, leading=24,
                           textColor=C_DUNKELBLAU, alignment=TA_CENTER) if r[0] == "QUITTUNG" else S_NORMAL)),
            p(r[1], S_NORMAL if r[0] != "QUITTUNG" else S_NORMAL)] for r in q_data]
    # Sonderbehandlung Quittungs-Header
    td[0] = [p("QUITTUNG", make_style("QH", fontName="Helvetica-Bold", fontSize=20, leading=26,
                                        textColor=white, alignment=TA_CENTER)),
              p("", S_NORMAL)]
    t = Table(td, colWidths=[4.5*cm, 12*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), C_DUNKELBLAU),
        ("SPAN", (0,0), (-1,0)),
        ("GRID", (0,1), (-1,-1), 0.3, C_BORDER),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [C_HELLGRAU, white]),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("BOX", (0,0), (-1,-1), 1.5, C_DUNKELBLAU),
    ]))
    elems.append(t)
    elems.append(sp(0.5))
    elems.append(p(
        "<i>Anmerkung Kontoauszug Anlage K-MAK-6: Überweisung von IBAN "
        "DE22 7005 0000 0099 9876 54 (Haspelbeck) an IBAN "
        "DE89 7002 0270 0012 3456 78 (Bechtholdsmeier-Schongau e.K.), "
        "EUR 8.810,76, Verwendungszweck „Rechnung 2023/047 Provision Mauerkircherstraße 47", "
        "gebucht 29.05.2023, Wertstellung 30.05.2023.</i>", S_KLEIN))
    elems.append(pb())
    return elems


def bestandteil_10_widerrufsbelehrung():
    """10. Widerrufsbelehrung / Mail-Signatur-Analyse"""
    elems = []
    elems.append(section_header("WIDERRUFSBELEHRUNG UND SIGNATUR-ANALYSE",
                                 "§ 312d, 356 BGB / Anlage K-MAK-10"))
    elems.append(sp(0.3))

    elems.append(h2("Volltext der Mail-Signatur Bechtholdsmeier-Schongau e.K."))
    elems.append(p("Aus Anlage K-MAK-1 (E-Mail vom 03.04.2023) rekonstruierter Volltext:", S_NORMAL))
    elems.append(sp(0.2))

    sig_text = """\
── SIGNATUR ────────────────────────────────────────────────────────────────
Marlene Bechtholdsmeier-Schongau
Immobilien-Vermittlung Bechtholdsmeier-Schongau e.K.
Schwere-Reiter-Straße 18 | 80637 München
Tel.: +49 89 5551 8800 | Fax: +49 89 5551 8801
E-Mail: makler@bechtholdsmeier-schongau-immo.de
Web: www.bechtholdsmeier-schongau-immo.de
HRA München 88734 | USt-IdNr.: DE 294 883 712
────────────────────────────────────────────────────────────────────────────
HINWEIS ZUR FÄLLIGKEIT DER PROVISION (automatisch):
Wir weisen darauf hin, dass bei Abschluss eines Kaufvertrages bei einem
Einfamilienhaus eine vom Veräußerer und Erwerber zu zahlende Provision
fällig wird. Diese beläuft sich maximal auf drei Komma sieben Prozent des
Kaufpreises (inklusive gesetzlicher Mehrwertsteuer und je Partei),
im Verkaufsfall des von Ihnen veräußerten Objektes.
Bei Zustandekommen des Kaufvertrages wird die Provision innerhalb von
14 Tagen nach Beurkundung fällig.
────────────────────────────────────────────────────────────────────────────
WIDERRUFSBELEHRUNG (beim Käufer-Maklervertrag beigelegt, August 2022):
[In der Akte befindlich: Anlage K-MAK-7 — SONDERBAND II — nicht abgebildet]"""

    st = Table([[p(sig_text, make_style("SigTxt", fontName="Courier", fontSize=8, leading=11,
                                         textColor=HexColor("#333333")))]], colWidths=[16.5*cm])
    st.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#F5F5F5")),
        ("BOX", (0,0), (-1,-1), 0.8, C_BORDER),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    elems.append(st)
    elems.append(sp(0.3))

    # Handschriftliche Notiz Hagelbrand
    elems.append(p(
        "<i>[Handschr. Notiz RA Hagelbrand-Wittlsbach:] "
        "Widerrufsbelehrung beim Käufer-MV: JA (Anlage K-MAK-7, Sonderband II). "
        "ABER: Verkäufer-MV? NEIN. Beklagte hat keine gesonderte Widerrufsbelehrung "
        "für den Verkäufer-Maklervertrag übermittelt. § 356 Abs. 3 S. 2 BGB: "
        "Widerrufsfrist läuft NICHT bei fehlender Belehrung!</i>", S_KURSIV))
    elems.append(sp(0.3))

    elems.append(h2("Rechtliche Analyse der Signatur-Position"))
    analyse_rows = [
        ["Position Provisionshinweis:", "Nach Schluss-Signatur (unterhalb „Marlene Bechtholdsmeier-Schongau")"],
        ["Relevanz § 126b BGB:", "Str. — Signatur als Abschlussmarkierung: Erklärung des Erklärenden endet mit Signatur"],
        ["BGH I ZR 202/25 Rz. 19:", "Provisionshinweis nach Signatur kein eigenständiger Vertragsantrag"],
        ["Vergleichsrechtsprechung:", "OLG Frankfurt, Urt. v. 11.05.2022, 2 U 179/21 (Signatur als Abschlussmarkierung)"],
        ["Fazit Hagelbrand:", "Textform nicht gewahrt — § 125 BGB: Nichtigkeit des Verkäufer-Maklervertrags"],
    ]
    td = [[p(r[0], S_FETT), p(r[1], S_NORMAL)] for r in analyse_rows]
    t2 = Table(td, colWidths=[5*cm, 11.5*cm])
    t2.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.3, C_BORDER),
        ("ROWBACKGROUNDS", (0,0), (-1,-1), [C_HELLGRAU, white]),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    elems.append(t2)
    elems.append(pb())
    return elems


def bestandteil_11_vergleichsverhandlung():
    """11. Vergleichsverhandlung-Protokoll"""
    elems = []
    elems.append(section_header("PROTOKOLL VERGLEICHSVERHANDLUNG",
                                 "LG München I 12 O 8842/23 — 12. Juni 2024 — gescheitert"))
    elems.append(sp(0.3))

    prot_header = [
        ["Gericht:", "Landgericht München I, 12. Zivilkammer"],
        ["Verhandlungsdatum:", "12. Juni 2024, 10:30 Uhr, Sitzungssaal 315"],
        ["Vorsitzender:", "Richter am Landgericht Dr. Hieronymus Zöllnerbauer"],
        ["Beisitzende:", "Ri'in am LG Dr. Konstanze Pfaffenberger-Moser, Ri Benedikt Grünauer"],
        ["Protokoll:", "Justizangestellte Sieglinde Mühlbauer-Drosselmann"],
    ]
    td = [[p(r[0], S_FETT), p(r[1], S_NORMAL)] for r in prot_header]
    t = Table(td, colWidths=[4*cm, 12.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), C_HELLGRAU),
        ("GRID", (0,0), (-1,-1), 0.3, C_BORDER),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    elems.append(t)
    elems.append(sp(0.4))

    elems.append(h2("Verhandlungsprotokoll"))
    elems.append(p(
        "Der Vorsitzende Richter Dr. Zöllnerbauer eröffnete die Verhandlung um 10:34 Uhr. "
        "Beide Parteien sind durch ihre Verfahrensbevollmächtigten vertreten: "
        "Die Kläger durch RA Dr. Knut Hagelbrand-Wittlsbach, "
        "die Beklagte durch RAin Dr. Adelheid Korkenzieher-Mariastein.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "Der Vorsitzende erteilte einen Hinweis gemäß § 139 ZPO: Das Gericht neige dazu, "
        "die Klage für begründet zu halten. Der E-Mail-Austausch vom 03./13. April 2023 "
        "erscheine nach vorläufiger Einschätzung nicht geeignet, die Anforderungen des "
        "§ 656a BGB i.V.m. § 126b BGB zu erfüllen. Insbesondere die Position des "
        "Provisionshinweises unterhalb der Signatur sowie die fehlende Bestimmtheit "
        "der klägerischen Antwort-E-Mail ließen eine wirksame Textform-Erklärung "
        "zweifelhaft erscheinen. Eine Entscheidung sei indes noch nicht gefallen.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "RAin Korkenzieher-Mariastein widersprach der vorläufigen Einschätzung und "
        "verwies auf die notarielle Maklerklausel sowie die Gesamtumstände der Zusammenarbeit. "
        "RA Hagelbrand-Wittlsbach erwiderte, die Maklerklausel ersetze keinen wirksamen "
        "Maklervertragsabschluss ante rem.", S_NORMAL))
    elems.append(sp(0.4))

    elems.append(h3("Vergleichsangebot der Beklagten"))
    vgl = Table([[p(
        "Die Beklagte, vertreten durch RAin Dr. Korkenzieher-Mariastein, bietet an:\n\n"
        "Zahlung von 50 % der streitgegenständlichen Provision, mithin EUR 4.405,38, "
        "in einer Summe, zahlbar innerhalb von 30 Tagen nach Vergleichsschluss.\n\n"
        "Im Gegenzug: Vollständige Klagrücknahme und beiderseitiger Kostenverzicht.",
        make_style("VglBox", fontName="Times-Roman", fontSize=10, leading=15, textColor=C_GRAU))
    ]], colWidths=[16.5*cm])
    vgl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#F0FFF0")),
        ("BOX", (0,0), (-1,-1), 1.5, HexColor("#008000")),
        ("LEFTPADDING", (0,0), (-1,-1), 14),
        ("RIGHTPADDING", (0,0), (-1,-1), 14),
        ("TOPPADDING", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    elems.append(vgl)
    elems.append(sp(0.3))

    elems.append(h3("Reaktion der Kläger"))
    elems.append(p(
        "RA Hagelbrand-Wittlsbach erklärte nach Rücksprache mit seinen Mandanten — "
        "Herrn und Frau Haspelbeck-Türkenfeld waren telefonisch zugeschaltet — "
        "das Vergleichsangebot für nicht annehmbar. Die Kläger beharrten auf "
        "vollständiger Rückzahlung. Herr Haspelbeck-Türkenfeld teilte laut Protokoll "
        "ergänzend telefonisch mit: „Das ist eine Frage der Gerechtigkeit, nicht nur "
        "des Geldes. Wir wollen, dass das Gericht das klärt."", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "<b>Ergebnis:</b> Vergleich gescheitert. Der Vorsitzende schloss die mündliche "
        "Verhandlung für die Beweisaufnahme und setzte Termin zur Urteilsverkündung "
        "auf den 12. September 2024 an. (Anm.: Urteil erging tatsächlich am "
        "17. September 2024 — vgl. LG-Urteil, nicht gesondert abgebildet; "
        "Berufung eingelegt 04. Juli 2024 vor Urteilsverkündung — vgl. Bestandteil 12.)", S_NORMAL))
    elems.append(pb())
    return elems


def bestandteil_12_berufungsschriftsatz():
    """12. Berufungsschriftsatz"""
    elems = []
    elems.append(section_header("BERUFUNGSSCHRIFTSATZ", "OLG München 13 U 412/24 / Beklagte als Berufungsklägerin"))
    elems.append(sp(0.3))
    elems.append(kanzlei_logo_km())
    elems.append(sp(0.2))

    ta = Table([[p("An das\nOberlandesgericht München\n13. Zivilsenat\nPrielmayerstraße 5\n80335 München", S_NORMAL),
                 p("München, 04. Juli 2024", make_style("DRK", fontName="Helvetica",
                    fontSize=10, leading=14, alignment=TA_RIGHT, textColor=C_GRAU))]],
               colWidths=[10*cm, 6.5*cm])
    elems.append(ta)
    elems.append(sp(0.4))

    elems.append(p("<b>In der Sache</b>", S_NORMAL))
    for elem in rubrum_block(
        "Immobilien-Vermittlung „Marlene Bechtholdsmeier-Schongau e.K." (Berufungsklägerin)",
        "Eheleute Korbinian und Walburga Haspelbeck-Türkenfeld (Berufungsbeklagte)",
        "OLG München 13 U 412/24 (Vorinstanz: LG München I 12 O 8842/23)",
        "Oberlandesgericht München, 13. Zivilsenat"):
        elems.append(elem)
    elems.append(sp(0.3))

    elems.append(p(
        "Die Berufungsklägerin legt gegen das Urteil des Landgerichts München I vom "
        "17. September 2024 (Az. 12 O 8842/23) — zugestellt am 04. Oktober 2024 —", S_NORMAL))
    elems.append(sp(0.2))

    at = Table([[p("BERUFUNG", make_style("BAT", fontName="Helvetica-Bold", fontSize=14,
                                           leading=20, alignment=TA_CENTER, textColor=C_AKZENT))
                ]], colWidths=[16.5*cm])
    at.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#FFF8F8")),
        ("BOX", (0,0), (-1,-1), 1.5, C_AKZENT),
        ("TOPPADDING", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    elems.append(at)
    elems.append(sp(0.3))

    elems.append(p("ein und beantragt:", S_NORMAL))
    antraege = [
        "1. Auf die Berufung der Berufungsklägerin wird das Urteil des LG München I vom "
        "17. September 2024 aufgehoben.",
        "2. Die Klage wird abgewiesen.",
        "3. Die Berufungsbeklagten tragen die Kosten beider Rechtszüge.",
        "4. Die Revision wird nicht zugelassen.",
    ]
    for a in antraege:
        elems.append(p(f"• {a}", S_NORMAL))

    elems.append(sp(0.3))
    elems.append(p(
        "Die Berufungsbegründung wird innerhalb der gesetzlichen Frist nachgereicht "
        "(§ 520 Abs. 2 ZPO). Zur Begründung wird vorläufig auf die Ausführungen "
        "in der Klageerwiderung verwiesen.", S_NORMAL))
    elems.append(sp(0.4))
    elems.append(p("München, 04. Juli 2024", S_NORMAL))
    elems.append(sp(0.3))
    elems.append(p("Dr. Adelheid Korkenzieher-Mariastein, Rechtsanwältin", S_NORMAL))
    elems.append(pb())
    return elems


def bestandteil_13_berufungsbegruendung():
    """13. Berufungsbegründung (12 Seiten)"""
    elems = []
    elems.append(section_header("BERUFUNGSBEGRÜNDUNG", "OLG München 13 U 412/24 — 12 Seiten"))
    elems.append(sp(0.3))
    elems.append(kanzlei_logo_km())
    elems.append(sp(0.3))

    elems.append(p("München, 20. August 2024", S_NORMAL))
    elems.append(sp(0.3))
    elems.append(h2("In Sachen Bechtholdsmeier-Schongau e.K. ./. Haspelbeck-Türkenfeld "
                     "(OLG München 13 U 412/24)"))
    elems.append(sp(0.2))
    elems.append(p(
        "Das Urteil des Landgerichts München I vom 17. September 2024 ist rechtsfehlerhaft "
        "und verletzt die Berufungsklägerin in ihren Rechten. Es beruht auf einer "
        "unzutreffenden Auslegung des § 656a BGB und einer unvollständigen "
        "Tatsachenwürdigung.", S_NORMAL))

    elems.append(h3("A. Verfahrensgang"))
    elems.append(p(
        "Das Landgericht hat nach mündlicher Verhandlung vom 12. Juni 2024 und "
        "Beweisaufnahme (Vernehmung der Maklerin Bechtholdsmeier-Schongau sowie "
        "des Klägers Korbinian Haspelbeck-Türkenfeld als Partei) mit Urteil vom "
        "17. September 2024 der Klage vollumfänglich stattgegeben und die "
        "Berufungsklägerin zur Zahlung von EUR 8.810,76 nebst Zinsen verurteilt. "
        "Der Streitwert wurde auf EUR 8.810,76 festgesetzt.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "Das Landgericht hat die Berufung nicht zugelassen. Die Berufungsklägerin "
        "legt gleichwohl Berufung ein, da das Landgericht den Sachverhalt in "
        "entscheidungserheblichen Punkten falsch beurteilt hat.", S_NORMAL))

    elems.append(h3("B. Rügen im Einzelnen"))
    elems.append(h3("I. Verletzung des § 656a BGB — unzutreffende Auslegung"))
    elems.append(p(
        "Das Landgericht hat § 656a BGB in einer Weise ausgelegt, die weder dem "
        "Wortlaut noch dem Sinn und Zweck der Norm entspricht. Insbesondere hat es "
        "verkannt, dass die E-Mail vom 03. April 2023 alle Elemente eines "
        "Vertragsangebots im Sinne des § 656a BGB enthält:", S_NORMAL))
    elems.append(sp(0.2))

    punkte = [
        ("1.", "Leistungsbeschreibung:", "Vermittlung des Kaufvertrages über das Objekt "
         "Mauerkircherstraße 47 — eindeutig identifiziert."),
        ("2.", "Vergütung:", "Provision maximal 3,7 % inkl. MwSt. je Partei — "
         "ausreichend bestimmt, da bei Maklerverträgen Höchstbetragsangaben üblich sind."),
        ("3.", "Fälligkeit:", "14 Tage nach Beurkundung — eindeutig."),
        ("4.", "Erklärende:", "Marlene Bechtholdsmeier-Schongau e.K. — vollständig identifiziert."),
    ]
    for nr, titel, text in punkte:
        row = Table([[p(nr, S_FETT), p(f"<b>{titel}</b> {text}", S_NORMAL)]],
                     colWidths=[0.8*cm, 15.7*cm])
        row.setStyle(TableStyle([
            ("LEFTPADDING", (0,0), (-1,-1), 4),
            ("RIGHTPADDING", (0,0), (-1,-1), 4),
            ("TOPPADDING", (0,0), (-1,-1), 3),
            ("BOTTOMPADDING", (0,0), (-1,-1), 3),
            ("VALIGN", (0,0), (-1,-1), "TOP"),
        ]))
        elems.append(row)

    elems.append(sp(0.2))
    elems.append(p(
        "Das Landgericht hat die Anforderungen an die Bestimmtheit des Angebots überspannt. "
        "§ 126b BGB verlangt eine lesbare Erklärung auf einem dauerhaften Datenträger — "
        "nicht eine perfekte Vertragsurkunde. Die E-Mail erfüllt diese Mindestanforderungen. "
        "Das Landgericht hat demgegenüber Anforderungen gestellt, die sich weder aus "
        "§ 126b BGB noch aus § 656a BGB ergeben.", S_NORMAL))

    elems.append(h3("II. Zur Signatur-Problematik"))
    elems.append(p(
        "Das Landgericht folgt der klägerischen Auffassung, wonach der Provisionshinweis "
        "nach der Signatur stehe und daher nicht der Beklagten als Erklärende zuzurechnen sei. "
        "Dies ist unzutreffend. § 126b BGB enthält — anders als § 126 BGB — keine "
        "Unterschrifts- oder Abschlussmarkierungsanforderung. Die Norm verlangt lediglich, "
        "dass die Person des Erklärenden in der Erklärung genannt ist. Dies ist durch "
        "die Signatur zweifellos erfüllt, auch wenn die Signatur vor dem Provisionshinweis "
        "erscheint. Entscheidend ist, dass die E-Mail insgesamt der Beklagten als "
        "Absenderin und damit als Erklärende zuzurechnen ist.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "Die Auffassung des Landgerichts führt zu praktisch nicht handhabbaren Ergebnissen: "
        "Jeder E-Mail-Footer müsste auf korrekte Positionierung aller rechtlich relevanten "
        "Hinweise geprüft werden. Dies entspricht weder der Praxis des Rechtsverkehrs "
        "noch der gesetzgeberischen Intention.", S_NORMAL))

    elems.append(h3("III. Zur hilfsweisen Maklerklausel § 13 des Kaufvertrags"))
    elems.append(p(
        "Das Landgericht hat die Hilfsargumentation zur notariellen Maklerklausel "
        "mit der Begründung verworfen, § 656a BGB verlange einen zeitlich vor dem "
        "Kaufvertrag geschlossenen Maklervertrag. Dies ist in dieser Absolutheit "
        "unrichtig: § 656a BGB enthält keine zeitliche Anforderung, nur eine Formvorschrift. "
        "Der notarielle Kaufvertrag wahrt die Textform jedenfalls (§ 128 BGB ist strenger "
        "als § 126b BGB). Wenn die Parteien im Kaufvertrag die Maklerklausel akzeptiert haben, "
        "liegt hierin jedenfalls eine nachträgliche Vertragsbestätigung, die nach dem "
        "Rechtsgedanken des § 141 BGB den formunwirksamen Maklervertrag heilen kann.", S_NORMAL))

    elems.append(h3("IV. Zu den Zinsen"))
    elems.append(p(
        "Das Landgericht hat Verzugszinsen ab dem 15. Mai 2023 (Zahlungsdatum) "
        "zugesprochen. Dies ist rechtsfehlerhaft: Verzug trat frühestens mit "
        "Ablauf der Widerrufs-Reaktionsfrist am 17. August 2023 ein. "
        "Bis zu diesem Zeitpunkt lagen keine Voraussetzungen für Verzugszinsen vor.", S_NORMAL))

    elems.append(h3("C. Beweisangebote der Berufungsklägerin"))
    beweise = [
        "Zeugnis: Klientin Bechtholdsmeier-Schongau zum Telefoninhalt April 2023",
        "Zeugnis: Bartholomäus Höglmayr-Stockenfels (anwesend beim Notartermin)",
        "Sachverständigengutachten: Ortsüblichkeit der E-Mail-Signaturgestaltung bei Immobilienmaklern in München",
        "Anlage BK-1: Musterschreiben Berufsverband Immobilienmakler (IVD) zur Textform-Gestaltung",
        "Anlage BK-2: Buchhaltungsunterlagen zur Entreicherung (Kostenpositionen 2023)",
    ]
    for b in beweise:
        elems.append(p(f"• {b}", S_NORMAL))

    elems.append(sp(0.5))
    elems.append(p("München, 20. August 2024", S_NORMAL))
    elems.append(sp(0.3))
    elems.append(p("Dr. Adelheid Korkenzieher-Mariastein, Rechtsanwältin", S_NORMAL))
    elems.append(pb())
    return elems


def bestandteil_14_berufungserwiderung():
    """14. Berufungserwiderung"""
    elems = []
    elems.append(section_header("BERUFUNGSERWIDERUNG", "OLG München 13 U 412/24 — Kläger als Berufungsbeklagte"))
    elems.append(sp(0.3))
    elems.append(kanzlei_logo_ht())
    elems.append(sp(0.2))

    elems.append(p("München, 25. September 2024", S_NORMAL))
    elems.append(sp(0.3))
    elems.append(h2("In Sachen OLG München 13 U 412/24"))
    elems.append(p("Berufungserwiderung der Eheleute Haspelbeck-Türkenfeld", S_NORMAL))
    elems.append(sp(0.3))

    elems.append(h3("I. Einleitung"))
    elems.append(p(
        "Die Berufung der Beklagten ist unbegründet. Das Landgericht hat den Sachverhalt "
        "zutreffend gewürdigt und § 656a BGB rechtsfehlerfrei angewandt. "
        "Die Berufungsbegründung enthält im Wesentlichen eine Wiederholung des "
        "erstinstanzlichen Vorbringens, ohne neue Aspekte zu benennen.", S_NORMAL))

    elems.append(h3("II. Zur Signatur-Positionierung"))
    elems.append(p(
        "Die Berufungsklägerin räumt ein, dass der Provisionshinweis nach der Signatur "
        "erscheint. Sie meint gleichwohl, dies sei für § 126b BGB unschädlich. "
        "Diese Auffassung verkennt die Funktion der Signatur im elektronischen Rechtsverkehr: "
        "Die Signatur markiert das Ende der persönlichen Erklärung. Was nach der Signatur "
        "steht, ist automatisch generierter Anhang — kein integraler Bestandteil der "
        "rechtsgeschäftlichen Erklärung. Der BGH hat in I ZR 202/25 (11.03.2026) — "
        "wenngleich nach der erstinstanzlichen und zweitinstanzlichen Entscheidung ergangen — "
        "diese Frage im vorliegenden Verfahren letztverbindlich entschieden.", S_NORMAL))

    elems.append(h3("III. Zur Heilung durch § 141 BGB"))
    elems.append(p(
        "Der Hilfsansatz der Beklagten über § 141 BGB (Bestätigung des nichtig geschlossenen "
        "Vertrages) scheitert schon daran, dass § 141 Abs. 1 BGB für die Heilung auf die "
        "Formvorschrift des ursprünglichen Vertrags verweist. Auch die Bestätigung nach "
        "§ 141 BGB muss daher die Form des § 656a BGB wahren. Die Maklerklausel in § 13 "
        "des Kaufvertrags wahrt zwar die notarielle Form, ist aber keine eigenständige "
        "Willenserklärung der Kläger zu einem Maklervertrag — sie ist lediglich eine "
        "faktische Beschreibung einer angeblich zuvor erfolgten Beauftragung.", S_NORMAL))

    elems.append(h3("IV. Berufungsanträge"))
    antraege = [
        "1. Die Berufung wird zurückgewiesen.",
        "2. Die Berufungsklägerin trägt die Kosten des Berufungsverfahrens.",
        "3. Das Urteil des OLG München ist vorläufig vollstreckbar.",
        "4. Die Revision wird zugelassen (grundsätzliche Bedeutung § 656a BGB / Textform).",
    ]
    for a in antraege:
        elems.append(p(f"• {a}", S_NORMAL))

    elems.append(sp(0.5))
    elems.append(p("Dr. Knut Hagelbrand-Wittlsbach, Rechtsanwalt", S_NORMAL))
    elems.append(pb())
    return elems


def bestandteil_15_berufungsurteil():
    """15. Berufungsurteil OLG München"""
    elems = []
    elems.append(section_header("BERUFUNGSURTEIL OLG MÜNCHEN",
                                 "13 U 412/24 — Verkündet 17. Februar 2025"))
    elems.append(sp(0.3))

    elems.append(p("OBERLANDESGERICHT MÜNCHEN", make_style("OLGK", fontName="Helvetica-Bold",
                    fontSize=15, leading=20, alignment=TA_CENTER, textColor=C_DUNKELBLAU)))
    elems.append(p("13. Zivilsenat", S_ZENTRIERT))
    elems.append(sp(0.3))
    elems.append(p("IM NAMEN DES VOLKES", make_style("INVN", fontName="Helvetica-Bold",
                    fontSize=12, leading=16, alignment=TA_CENTER, textColor=C_AKZENT)))
    elems.append(sp(0.3))
    elems.append(p("URTEIL", make_style("URTK", fontName="Helvetica-Bold",
                    fontSize=18, leading=24, alignment=TA_CENTER, textColor=C_DUNKELBLAU)))
    elems.append(sp(0.2))
    elems.append(p("Az. 13 U 412/24", S_ZENTRIERT))
    elems.append(p("Verkündet am 17. Februar 2025", S_ZENTRIERT))
    elems.append(sp(0.4))
    elems.append(hr_thick())

    elems.append(h3("In der Sache"))
    for elem in rubrum_block(
        "Immobilien-Vermittlung Bechtholdsmeier-Schongau e.K. (Berufungsklägerin / Beklagte)",
        "Eheleute Haspelbeck-Türkenfeld (Berufungsbeklagte / Kläger)",
        "OLG München 13 U 412/24",
        "Oberlandesgericht München, 13. Zivilsenat",
        [("wegen:", "Rückforderung Maklerprovision (§§ 812, 656a, 126b BGB)")]):
        elems.append(elem)
    elems.append(sp(0.3))

    elems.append(h2("Tenor"))
    tenor_items = [
        "1. Die Berufung der Beklagten wird zurückgewiesen.",
        "2. Die Beklagte trägt die Kosten des Berufungsverfahrens.",
        "3. Das Urteil ist vorläufig vollstreckbar. Die Beklagte kann die Vollstreckung durch "
        "Sicherheitsleistung in Höhe von 110 % des vollstreckbaren Betrags abwenden.",
        "4. Die Revision wird zugelassen.",
    ]
    for item in tenor_items:
        t = Table([[p(item, S_TENOR)]], colWidths=[16.5*cm])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), HexColor("#F0F4FF")),
            ("LEFTPADDING", (0,0), (-1,-1), 12),
            ("RIGHTPADDING", (0,0), (-1,-1), 12),
            ("TOPPADDING", (0,0), (-1,-1), 5),
            ("BOTTOMPADDING", (0,0), (-1,-1), 5),
            ("BOX", (0,0), (-1,-1), 0.5, C_DUNKELBLAU),
        ]))
        elems.append(t)
        elems.append(sp(0.15))

    elems.append(h2("Begründung (Kurzfassung)"))
    elems.append(p(
        "Die Berufung der Beklagten ist zulässig, aber unbegründet. Das Landgericht hat "
        "der Klage zu Recht stattgegeben. Der Provisionsanspruch der Beklagten aus dem "
        "Verkäufer-Maklervertrag ist mangels Wahrung der Textform des § 656a BGB nicht "
        "entstanden. Die Zahlung der Kläger war daher rechtsgrundlos im Sinne des "
        "§ 812 Abs. 1 S. 1 Alt. 1 BGB.", S_NORMAL))
    elems.append(sp(0.2))

    elems.append(h3("Zur Textform"))
    elems.append(p(
        "§ 656a BGB i.V.m. § 126b BGB setzt voraus, dass die Erklärung des Erklärenden "
        "inhaltlich hinreichend bestimmt ist. Die E-Mail vom 03. April 2023 enthält zwar "
        "einen Provisionshinweis, dieser ist jedoch — wie das Landgericht zutreffend "
        "festgestellt hat — in seiner Position nach der Signatur der Erklärenden nicht "
        "als eigenständige rechtsgeschäftliche Erklärung der Beklagten anzusehen. "
        "Die Signatur markiert den Abschluss der persönlichen Mitteilung; der "
        "automatisch generierte Hinweistext darunter ist als Standardtext (boilerplate) "
        "erkennbar und für den Empfänger nicht als Vertragsangebot zu qualifizieren.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "Überdies fehlt es an einer ausreichend bestimmten Annahmeerklärung der Kläger. "
        "Die E-Mail vom 13. April 2023 bezieht sich allein auf die Vereinbarung des "
        "Notartermins, nicht auf einen Maklervertrag oder die Provisionspflicht.", S_NORMAL))

    elems.append(h3("Zur Revisionszulassung"))
    elems.append(p(
        "Die Revision wird gemäß § 543 Abs. 2 ZPO zugelassen. Die Frage, ob ein "
        "automatisch generierter Provisionshinweis in der Signatur einer E-Mail den "
        "Anforderungen des § 656a BGB i.V.m. § 126b BGB genügen kann, hat grundsätzliche "
        "Bedeutung. Sie ist höchstrichterlich noch nicht abschließend geklärt.", S_NORMAL))
    elems.append(sp(0.3))
    elems.append(p("Für das Oberlandesgericht München:", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p("gez. Vors. RiOLG Dr. Felizitas Waxenberger-Hugl", S_NORMAL))
    elems.append(p("gez. RiOLG Dr. Augustin Plöchlmoser", S_NORMAL))
    elems.append(p("gez. RiOLG Leonhard Krafft-Schwanthaler", S_NORMAL))
    elems.append(pb())
    return elems


def bestandteil_16_revisionbegruendung():
    """16. Revisionsbegründung BGH"""
    elems = []
    elems.append(section_header("REVISIONSBEGRÜNDUNG", "BGH I ZR 202/25 — Beklagte als Revisionsklägerin"))
    elems.append(sp(0.3))
    elems.append(kanzlei_logo_km())
    elems.append(sp(0.2))

    ta = Table([[p("An den\nBundesgerichtshof\nHerrenstraße 45 a\n76133 Karlsruhe", S_NORMAL),
                 p("Karlsruhe, 15. Mai 2025\n(via beA)", make_style("DRK", fontName="Helvetica",
                    fontSize=10, leading=14, alignment=TA_RIGHT, textColor=C_GRAU))]],
               colWidths=[10*cm, 6.5*cm])
    elems.append(ta)
    elems.append(sp(0.4))

    for elem in rubrum_block(
        "Immobilien-Vermittlung Bechtholdsmeier-Schongau e.K. (Revisionsklägerin / Beklagte)",
        "Eheleute Korbinian und Walburga Haspelbeck-Türkenfeld (Revisionsbeklagte / Kläger)",
        "BGH I ZR 202/25",
        "Bundesgerichtshof, I. Zivilsenat",
        [("Vorinstanz:", "OLG München 13 U 412/24, Urt. v. 17.02.2025"),
         ("wegen:", "Rückforderung Maklerprovision (§§ 656a, 126b, 812 BGB)")]):
        elems.append(elem)

    elems.append(sp(0.3))
    elems.append(p(
        "Die Revisionsklägerin begründet die Revision gegen das Urteil des "
        "Oberlandesgerichts München vom 17. Februar 2025 (Az. 13 U 412/24) wie folgt:", S_NORMAL))

    elems.append(h2("A. Zulässigkeit"))
    elems.append(p(
        "Die Revision ist gemäß § 543 Abs. 1 Nr. 1 ZPO statthaft, da das Berufungsgericht "
        "die Revision zugelassen hat. Die Revisionsfrist ist gewahrt (Urteil zugestellt "
        "01. März 2025, Revisionsbegründungsfrist bis 01. Juni 2025, Schriftsatz eingereicht "
        "15. Mai 2025 via beA).", S_NORMAL))

    elems.append(h2("B. Begründetheit"))
    elems.append(h3("I. Revisionsantrag"))
    antraege = [
        "1. Das Urteil des OLG München vom 17.02.2025 wird aufgehoben.",
        "2. Die Klage wird abgewiesen.",
        "3. Hilfsweise: Zurückverweisung an das OLG München.",
        "4. Die Revisionsbeklagten tragen die Kosten aller Instanzen.",
    ]
    for a in antraege:
        elems.append(p(f"• {a}", S_NORMAL))

    elems.append(h3("II. Verletzung revisiblen Rechts"))
    elems.append(h3("1. Fehlerhafte Auslegung des § 126b BGB"))
    elems.append(p(
        "Das OLG München hat § 126b BGB in einer Weise ausgelegt, die dem Wortlaut, "
        "der Entstehungsgeschichte und dem Sinn der Norm widerspricht. § 126b BGB "
        "normiert vier Anforderungen: (1) lesbare Erklärung, (2) dauerhafte Speicherung, "
        "(3) Nennung des Erklärenden, (4) Möglichkeit der Wiedergabe. Eine "
        "Positionierungsanforderung enthält die Norm nicht.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "Das OLG hat aus der Position des Provisionshinweises nach der Signatur abgeleitet, "
        "dieser sei kein integraler Bestandteil der Erklärung. Diese Schlussfolgerung "
        "ist ein Fehler: § 126b BGB unterscheidet nicht zwischen Haupttext und Anhang "
        "einer E-Mail. Jede in einer E-Mail enthaltene und lesbare Erklärung, die dem "
        "Absender zugerechnet werden kann, erfüllt die Textform.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "Die Revision verweist auf BT-Drs. 14/4987, S. 17: Die Textform soll gerade "
        "auch einfache elektronische Mitteilungen erfassen, um dem modernen "
        "Geschäftsverkehr Rechnung zu tragen. Eine Anforderung an die Positionierung "
        "innerhalb einer E-Mail würde die praktische Handhabbarkeit unverhältnismäßig "
        "erschweren.", S_NORMAL))

    elems.append(h3("2. Fehlerhafte Würdigung der Bestimmtheit"))
    elems.append(p(
        "Das OLG hat die Bestimmtheit des Angebots zu streng bewertet. "
        "Bei Maklerverträgen ist eine Höchstbetragsangabe für die Provision "
        "ausreichend bestimmt, da die genaue Höhe erst nach Festlegung des "
        "Kaufpreises berechenbar ist. Die Formulierung „maximal 3,7 %" gibt "
        "dem Auftraggeber die erforderliche Information über die Größenordnung "
        "der Provisionslast. Mehr verlangt § 656a BGB nicht.", S_NORMAL))

    elems.append(h3("3. Verletzung des § 812 BGB — Bereicherungsausschluss"))
    elems.append(p(
        "Selbst wenn man von einem formunwirksamen Maklervertrag ausgeht, "
        "hat das OLG die Entreicherungseinrede (§ 818 Abs. 3 BGB) fehlerhaft "
        "verworfen. Die Revisionsklägerin hat substantiiert dargelegt, "
        "dass sie die Provision für Betriebsausgaben im Zusammenhang mit "
        "der Vermittlungstätigkeit verwendet hat. Das OLG hat diesen Vortrag "
        "nicht hinreichend gewürdigt und die Anforderungen an den Nachweis "
        "der Entreicherung überspannt.", S_NORMAL))

    elems.append(h3("C. Rechtsgrundsätzliche Bedeutung"))
    elems.append(p(
        "Die Fragen (1) ob ein Provisionshinweis nach der E-Mail-Signatur des Maklers "
        "die Textform des § 656a BGB wahren kann und (2) ob bei formunwirksamen "
        "Maklerverträgen der Entreicherungseinwand des § 818 Abs. 3 BGB stets "
        "am Schutzzweck des § 656a BGB scheitert, sind von grundsätzlicher Bedeutung "
        "für eine Vielzahl gleichgelagerter Fälle in der deutschen Maklerwirtschaft.", S_NORMAL))
    elems.append(sp(0.5))
    elems.append(p("Karlsruhe, 15. Mai 2025 — Dr. Adelheid Korkenzieher-Mariastein, Rechtsanwältin", S_NORMAL))
    elems.append(pb())
    return elems


def bestandteil_17_revisionserwiderung():
    """17. Revisionserwiderung"""
    elems = []
    elems.append(section_header("REVISIONSERWIDERUNG", "BGH I ZR 202/25 — Kläger als Revisionsbeklagte"))
    elems.append(sp(0.3))
    elems.append(kanzlei_logo_ht())
    elems.append(sp(0.3))

    elems.append(p("München/Karlsruhe, 10. Oktober 2025", S_NORMAL))
    elems.append(sp(0.3))
    elems.append(h2("Revisionserwiderung der Eheleute Haspelbeck-Türkenfeld"))
    elems.append(sp(0.2))

    elems.append(h3("I. Unzulässigkeit des Revisionsvorbringens teilweise"))
    elems.append(p(
        "Soweit die Revisionsklägerin neue Tatsachen zur Entreicherung einführt, "
        "ist das Revisionsvorbringen unzulässig (§ 559 ZPO). Neue Tatsachen sind im "
        "Revisionsverfahren grundsätzlich ausgeschlossen.", S_NORMAL))

    elems.append(h3("II. Zur Auslegung des § 126b BGB"))
    elems.append(p(
        "Der Versuch der Revisionsklägerin, aus dem Wortlaut des § 126b BGB eine "
        "grenzenlose Positionierungsfreiheit herzuleiten, verfehlt den Schutzzweck "
        "der Norm. § 126b BGB in Verbindung mit § 656a BGB soll sicherstellen, "
        "dass der Auftraggeber eines Maklervertrages unmissverständlich erkennt, "
        "dass er eine rechtsverbindliche Erklärung abgibt. Ein automatischer "
        "Hinweistext in der E-Mail-Signatur, der unabhängig vom Gesprächsinhalt "
        "und unabhängig von der konkreten Vertragsanbahnung immer angefügt wird, "
        "erfüllt diese Funktion nicht.", S_NORMAL))

    elems.append(h3("III. Zur Bereicherung / Entreicherung"))
    elems.append(p(
        "Der Schutzzweck des § 656a BGB verbietet es, dem Makler die Berufung "
        "auf Entreicherung (§ 818 Abs. 3 BGB) zu gestatten. Dies hat der BGH "
        "in I ZR 197/22 ausdrücklich klargestellt. Die Revisionsklägerin setzt "
        "sich mit dieser Rechtsprechung nicht auseinander.", S_NORMAL))

    elems.append(h3("IV. Revisionsanträge der Beklagten / Revisionsbeklagten"))
    antraege = [
        "1. Die Revision wird zurückgewiesen.",
        "2. Die Revisionsklägerin trägt die Kosten des Revisionsverfahrens.",
    ]
    for a in antraege:
        elems.append(p(f"• {a}", S_NORMAL))

    elems.append(sp(0.5))
    elems.append(p("Dr. Knut Hagelbrand-Wittlsbach, Rechtsanwalt", S_NORMAL))
    elems.append(pb())
    return elems


def bestandteil_18_stellungnahme_verhandlung():
    """18. Stellungnahme zum Verhandlungstermin BGH"""
    elems = []
    elems.append(section_header("STELLUNGNAHME ZUM VERHANDLUNGSTERMIN BGH",
                                 "I ZR 202/25 — 11. März 2026, Karlsruhe"))
    elems.append(sp(0.3))

    elems.append(h2("Kurzstellungnahme RA Dr. Hagelbrand-Wittlsbach (Revisionsbeklagte)"))
    elems.append(p(
        "Der BGH-Senat hat im Termin vom 11. März 2026 die Parteien ausgiebig zur "
        "Frage der Textform-Bestimmtheit befragt. Aus den Fragen des Senats war "
        "erkennbar, dass der Senat die Revision für unbegründet hält, jedoch die "
        "Begründungslinie des OLG — Signaturpositionierung als entscheidend — "
        "nicht vollständig teilt.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "Der Vorsitzende Richter am BGH wies darauf hin, dass die entscheidende Frage "
        "nicht allein die Signaturpositionierung, sondern die inhaltliche Unbestimmtheit "
        "des Angebots sei: Fehle es an einem bestimmbaren Angebot, komme es auf die "
        "Position der Erklärung innerhalb der E-Mail nicht mehr an.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "RAin Dr. Korkenzieher-Mariastein konnte auf diesen Hinweis keine überzeugenden "
        "Ausführungen machen. Das Urteil wurde am selben Tag verkündet.", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "<i>[Handschr. Notiz Hagelbrand-Wittlsbach nach Rückkehr aus Karlsruhe:] "
        "BGH signalisiert klares Ergebnis — Revision raus. Mandanten informiert. "
        "Walburga sehr erleichtert. Korbinian fragt wann das Geld kommt.</i>", S_KURSIV))
    elems.append(pb())
    return elems


def bestandteil_19_bgh_urteil_tenor():
    """19. BGH-Urteil Tenor-Auszug"""
    elems = []
    elems.append(section_header("BGH-URTEIL — TENOR-AUSZUG UND BEGRÜNDUNGSSUMMARY",
                                 "I ZR 202/25 — 11. März 2026"))
    elems.append(sp(0.3))

    elems.append(p("BUNDESGERICHTSHOF", make_style("BGHK", fontName="Helvetica-Bold",
                    fontSize=15, leading=20, alignment=TA_CENTER, textColor=C_DUNKELBLAU)))
    elems.append(p("I. Zivilsenat", S_ZENTRIERT))
    elems.append(sp(0.3))
    elems.append(p("IM NAMEN DES VOLKES", make_style("INVN", fontName="Helvetica-Bold",
                    fontSize=12, leading=16, alignment=TA_CENTER, textColor=C_AKZENT)))
    elems.append(sp(0.3))
    elems.append(p("URTEIL", make_style("URTBGH", fontName="Helvetica-Bold",
                    fontSize=18, leading=24, alignment=TA_CENTER, textColor=C_DUNKELBLAU)))
    elems.append(sp(0.2))
    elems.append(p("Az. I ZR 202/25", S_ZENTRIERT))
    elems.append(p("Verkündet am 11. März 2026", S_ZENTRIERT))
    elems.append(sp(0.4))
    elems.append(hr_thick())

    for elem in rubrum_block(
        "Immobilien-Vermittlung Bechtholdsmeier-Schongau e.K. (Revisionsklägerin)",
        "Eheleute Korbinian und Walburga Haspelbeck-Türkenfeld (Revisionsbeklagte)",
        "BGH I ZR 202/25",
        "Bundesgerichtshof, I. Zivilsenat",
        [("Vorinstanz:", "OLG München, 13 U 412/24, Urt. v. 17.02.2025"),
         ("wegen:", "Rückforderung Maklerprovision — §§ 656a, 126b, 812 BGB")]):
        elems.append(elem)
    elems.append(sp(0.3))

    elems.append(h2("Tenor"))
    tenor_items = [
        "1. Die Revision der Beklagten gegen das Urteil des Oberlandesgerichts München "
        "vom 17. Februar 2025 — 13 U 412/24 — wird zurückgewiesen.",
        "2. Die Beklagte trägt die Kosten des Revisionsverfahrens.",
        "3. Der Streitwert des Revisionsverfahrens wird auf EUR 8.810,76 festgesetzt.",
    ]
    for item in tenor_items:
        t = Table([[p(item, S_TENOR)]], colWidths=[16.5*cm])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), HexColor("#E8F0FF")),
            ("LEFTPADDING", (0,0), (-1,-1), 14),
            ("RIGHTPADDING", (0,0), (-1,-1), 14),
            ("TOPPADDING", (0,0), (-1,-1), 8),
            ("BOTTOMPADDING", (0,0), (-1,-1), 8),
            ("BOX", (0,0), (-1,-1), 1.5, C_DUNKELBLAU),
        ]))
        elems.append(t)
        elems.append(sp(0.2))

    elems.append(h2("Begründung (Zusammenfassung / Leitsätze)"))

    leitsaetze = [
        ("Leitsatz 1", "§ 656a BGB — Textform — Bestimmtheit des Angebots",
         "Ein in der automatisierten E-Mail-Signatur eines Maklers enthaltener Provisionshinweis "
         "genügt den Anforderungen des § 656a BGB i.V.m. § 126b BGB nicht als eigenständiges "
         "Vertragsangebot, wenn er (a) nach der persönlichen Abschlussmarkierung (Signatur) "
         "positioniert ist, (b) keinen hinreichend bestimmten Leistungsgegenstand benennt "
         "und (c) vom Empfänger erkennbar als Standardtext und nicht als individuelles "
         "Angebot zu verstehen ist."),
        ("Leitsatz 2", "§ 812 BGB — Bereicherungsausschluss bei § 656a BGB",
         "Erlangt der Makler eine Provision aufgrund eines nach § 656a BGB nichtig geschlossenen "
         "Maklervertrags, kann er sich gegenüber dem Rückforderungsanspruch des Auftraggebers "
         "nicht auf Entreicherung gemäß § 818 Abs. 3 BGB berufen. Der Schutzzweck des § 656a "
         "BGB, der auf den Schutz des Verbrauchers vor übereilten Provisionsverpflichtungen "
         "gerichtet ist, schließt die Anwendung des § 818 Abs. 3 BGB aus (Bestätigung "
         "von BGH I ZR 197/22)."),
        ("Leitsatz 3", "Zur Widerrufsbelehrung",
         "Eine für einen anderen Maklervertrag (Käufer-Maklervertrag) erteilte "
         "Widerrufsbelehrung lässt die Widerrufsfrist für einen gesonderten und "
         "zeitlich späteren Verkäufer-Maklervertrag nicht anlaufen "
         "(§ 356 Abs. 3 S. 2 BGB)."),
    ]

    for ls_nr, ls_titel, ls_text in leitsaetze:
        elems.append(sp(0.2))
        lt = Table([[
            p(ls_nr, make_style(f"LSN_{ls_nr}", fontName="Helvetica-Bold", fontSize=9,
                                 leading=13, textColor=white, alignment=TA_CENTER)),
            p(f"<b>{ls_titel}</b>", make_style(f"LST_{ls_nr}", fontName="Helvetica-Bold",
                                                fontSize=10, leading=14, textColor=C_DUNKELBLAU))
        ]], colWidths=[2.5*cm, 14*cm])
        lt.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (0,0), C_DUNKELBLAU),
            ("LEFTPADDING", (0,0), (-1,-1), 8),
            ("RIGHTPADDING", (0,0), (-1,-1), 8),
            ("TOPPADDING", (0,0), (-1,-1), 6),
            ("BOTTOMPADDING", (0,0), (-1,-1), 6),
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ]))
        elems.append(lt)
        elems.append(p(ls_text, S_BESCHLUSS))
        elems.append(sp(0.1))

    elems.append(sp(0.4))
    elems.append(p(
        "Das Urteil bestätigt im Ergebnis die Entscheidungen der Vorinstanzen, gibt aber "
        "der Begründung eine neue Nuancierung: Die Signaturpositionierung ist ein Indiz, "
        "aber kein allein entscheidendes Kriterium. Entscheidend ist die inhaltliche "
        "Unbestimmtheit des Angebots — unabhängig davon, ob der Hinweis vor oder nach "
        "der Signatur steht. Damit gibt der BGH den Instanzgerichten für künftige Fälle "
        "einen klaren Prüfungsmaßstab vor.", S_NORMAL))
    elems.append(pb())
    return elems


def bestandteil_20_mandantenmemo():
    """20. Mandantenmemo"""
    elems = []
    elems.append(section_header("MANDANTENMEMO",
                                 "Ergebnis BGH I ZR 202/25 — RA Dr. Hagelbrand-Wittlsbach an Eheleute Haspelbeck"))
    elems.append(sp(0.3))
    elems.append(kanzlei_logo_ht())
    elems.append(sp(0.2))

    ta = Table([[p("An:\nEheleute Korbinian und Walburga Haspelbeck-Türkenfeld\nMauerkircherstraße 47, 81679 München", S_NORMAL),
                 p("München, 14. März 2026", make_style("DRHt", fontName="Helvetica",
                    fontSize=10, leading=14, alignment=TA_RIGHT, textColor=C_GRAU))]],
               colWidths=[10*cm, 6.5*cm])
    elems.append(ta)
    elems.append(sp(0.3))

    elems.append(p("<b>Betreff: Ihr Erfolg beim BGH — Az. I ZR 202/25 — Ergebnis-Memo</b>", S_NORMAL))
    elems.append(sp(0.3))

    elems.append(p("Sehr geehrter Herr Haspelbeck-Türkenfeld, sehr geehrte Frau Haspelbeck-Türkenfeld,", S_NORMAL))
    elems.append(sp(0.2))
    elems.append(p(
        "mit großer Freude darf ich Ihnen mitteilen, dass der Bundesgerichtshof am "
        "11. März 2026 die Revision der Beklagten Bechtholdsmeier-Schongau e.K. "
        "zurückgewiesen hat. Sie haben in allen drei Instanzen obsiegt. "
        "Das Urteil ist nunmehr rechtskräftig.", S_NORMAL))
    elems.append(sp(0.3))

    elems.append(h2("Ergebnis im Überblick"))
    erg_rows = [
        ["Rückzahlung:", "EUR 8.810,76 (Hauptforderung)"],
        ["Zinsen:", "5 % p.a. über Basiszinssatz seit 15.05.2023"],
        ["Zinsen (ca.):", "ca. EUR 1.400,00 (März 2026, geschätzt)"],
        ["Gesamtforderung:", "ca. EUR 10.210,76"],
        ["Kosten LG:", "Von der Beklagten zu tragen"],
        ["Kosten OLG:", "Von der Beklagten zu tragen"],
        ["Kosten BGH:", "Von der Beklagten zu tragen"],
        ["Anwaltskosten Kläger:", "Von der Beklagten gemäß RVG zu erstatten"],
    ]
    td = [[p(r[0], S_FETT), p(r[1], S_NORMAL)] for r in erg_rows]
    t = Table(td, colWidths=[4.5*cm, 12*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), C_HELLGRAU),
        ("GRID", (0,0), (-1,-1), 0.3, C_BORDER),
        ("ROWBACKGROUNDS", (0,0), (-1,-1), [HexColor("#E8F8E8"), white]),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    elems.append(t)
    elems.append(sp(0.4))

    elems.append(h2("Juristische Bedeutung"))
    elems.append(p(
        "Das BGH-Urteil hat über Ihren Fall hinaus erhebliche Bedeutung für die "
        "Maklerwirtschaft: Makler können nicht länger darauf vertrauen, dass ein "
        "automatisierter Provisionshinweis in der E-Mail-Signatur einen wirksamen "
        "Maklervertrag nach § 656a BGB begründet. Dies wird zu einer Überarbeitung "
        "der gängigen Kanzlei- und Maklersoftware führen.", S_NORMAL))

    elems.append(h2("Vollstreckung"))
    elems.append(p(
        "Ich werde umgehend die Vollstreckungsklausel beim BGH-Urkundsbeamten "
        "beantragen (§ 724 ZPO). Sobald ich die vollstreckbare Ausfertigung "
        "erhalten habe, kann die Zwangsvollstreckung eingeleitet werden. "
        "Parallel fordere ich die Beklagte mit einer Frist von 14 Tagen "
        "zur freiwilligen Zahlung auf.", S_NORMAL))
    elems.append(sp(0.3))

    elems.append(h2("Voraussichtliche Kostenrechnung (Entwurf)"))
    kosten_rows = [
        ["LG München I — RVG:", "EUR 1.245,80 (Verfahrensgebühr + Terminsgebühr)"],
        ["OLG München — RVG:", "EUR 1.245,80"],
        ["BGH — RVG:", "EUR 1.554,75 (erhöhte Gebühren)"],
        ["Auslagen gesamt:", "ca. EUR 380,00"],
        ["Vorschuss geleistet:", "EUR 2.000,00"],
        ["Nachzahlung/Erstattung:", "Nach Kostenfestsetzungsbeschluss"],
    ]
    td2 = [[p(r[0], S_FETT), p(r[1], S_NORMAL)] for r in kosten_rows]
    t2 = Table(td2, colWidths=[5*cm, 11.5*cm])
    t2.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.3, C_BORDER),
        ("ROWBACKGROUNDS", (0,0), (-1,-1), [white, C_HELLGRAU]),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    elems.append(t2)
    elems.append(sp(0.5))
    elems.append(p(
        "Ich gratuliere Ihnen zu diesem Erfolg, der nicht zuletzt Ihrer Beharrlichkeit "
        "und Ihrer Bereitschaft, die Sache bis zum BGH durchzufechten, zu verdanken ist. "
        "Bei Rückfragen stehe ich gerne zur Verfügung.", S_NORMAL))
    elems.append(sp(0.3))
    elems.append(p("Mit freundlichen Grüßen<br/>Dr. Knut Hagelbrand-Wittlsbach, Rechtsanwalt", S_NORMAL))
    elems.append(pb())
    return elems


def bestandteil_21_handschriftliche_notizen():
    """21. Handschriftliche Notizen Korbinian Haspelbeck"""
    elems = []
    elems.append(section_header("HANDSCHRIFTLICHE RANDNOTIZEN",
                                 "