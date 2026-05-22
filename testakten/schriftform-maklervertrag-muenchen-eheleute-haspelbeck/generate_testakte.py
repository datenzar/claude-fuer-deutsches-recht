#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_testakte.py
Testakte: Haspelbeck-Türkenfeld ./. Bechtholdsmeier-Schongau e.K.
Az. LG München I 12 O 8842/23 — Rückforderung Maklerprovision
Generiert Testakte_Maklervertrag_Muenchen_Haspelbeck.pdf (Ziel: 80–95 Seiten)
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import (HexColor, black, white, grey,
                                   Color, red, blue, green)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                 PageBreak, Table, TableStyle, HRFlowable,
                                 KeepTogether, Preformatted)
from reportlab.platypus.flowables import Flowable
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# ─────────────────────────────────────────────────────────────────────────────
# PFADE
# ─────────────────────────────────────────────────────────────────────────────
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PDF  = os.path.join(OUTPUT_DIR, "Testakte_Maklervertrag_Muenchen_Haspelbeck.pdf")

# ─────────────────────────────────────────────────────────────────────────────
# FARBEN
# ─────────────────────────────────────────────────────────────────────────────
C_DARK      = HexColor("#1A1A2E")
C_ACCENT    = HexColor("#16213E")
C_BORDER    = HexColor("#888888")
C_LIGHT_BG  = HexColor("#F5F5F0")
C_HEADER_BG = HexColor("#2C3E50")
C_WA_GREEN  = HexColor("#DCF8C6")
C_WA_GREY   = HexColor("#ECECEC")
C_RED_STAMP = HexColor("#CC0000")
C_YELLOW_HL = HexColor("#FFFACD")
C_BLUE_LINK = HexColor("#0000CC")
C_MEMO_RED  = HexColor("#CC0000")

PAGE_W, PAGE_H = A4   # 595.28 x 841.89 pt

# ─────────────────────────────────────────────────────────────────────────────
# STYLES
# ─────────────────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def make_style(name, parent="Normal", **kw):
    return ParagraphStyle(name=name, parent=styles[parent], **kw)

S_NORMAL    = make_style("SN",  fontName="Helvetica",       fontSize=10, leading=14, spaceAfter=4)
S_SMALL     = make_style("SS",  fontName="Helvetica",       fontSize=8,  leading=11, spaceAfter=2)
S_TINY      = make_style("ST",  fontName="Helvetica",       fontSize=7,  leading=10, spaceAfter=1)
S_BOLD      = make_style("SB",  fontName="Helvetica-Bold",  fontSize=10, leading=14, spaceAfter=4)
S_TITLE     = make_style("STL", fontName="Helvetica-Bold",  fontSize=16, leading=20, spaceAfter=8, alignment=TA_CENTER)
S_H1        = make_style("SH1", fontName="Helvetica-Bold",  fontSize=13, leading=17, spaceAfter=6)
S_H2        = make_style("SH2", fontName="Helvetica-Bold",  fontSize=11, leading=15, spaceAfter=5)
S_JUSTIFY   = make_style("SJ",  fontName="Times-Roman",     fontSize=10, leading=15, spaceAfter=5, alignment=TA_JUSTIFY)
S_JUSTIFY_B = make_style("SJB", fontName="Times-Bold",      fontSize=10, leading=15, spaceAfter=5, alignment=TA_JUSTIFY)
S_ITALIC    = make_style("SI",  fontName="Times-Italic",    fontSize=10, leading=14, spaceAfter=4, leftIndent=20)
S_HANDW     = make_style("SHW", fontName="Times-Italic",    fontSize=9,  leading=13, spaceAfter=3, leftIndent=25, textColor=HexColor("#2244AA"))
S_MONO      = make_style("SMO", fontName="Courier",         fontSize=8,  leading=12, spaceAfter=2)
S_MONO_SM   = make_style("SMS", fontName="Courier",         fontSize=7,  leading=10, spaceAfter=2)
S_CENTER    = make_style("SC",  fontName="Helvetica",       fontSize=10, leading=14, spaceAfter=4, alignment=TA_CENTER)
S_CENTER_B  = make_style("SCB", fontName="Helvetica-Bold",  fontSize=10, leading=14, spaceAfter=4, alignment=TA_CENTER)
S_RED       = make_style("SR",  fontName="Helvetica-Bold",  fontSize=9,  leading=13, spaceAfter=3, textColor=C_MEMO_RED)
S_RUBRUM    = make_style("SRU", fontName="Times-Roman",     fontSize=10, leading=15, spaceAfter=6, alignment=TA_CENTER)
S_ANTRAG    = make_style("SA",  fontName="Times-Roman",     fontSize=10, leading=15, spaceAfter=5, leftIndent=30, firstLineIndent=-10)
S_AZ        = make_style("SAZ", fontName="Helvetica-Bold",  fontSize=9,  leading=12, spaceAfter=2, alignment=TA_RIGHT)

def P(text, style=None):
    if style is None: style = S_NORMAL
    return Paragraph(text, style)

def SP(n=1):
    return Spacer(1, n * 0.4 * cm)

def HR():
    return HRFlowable(width="100%", thickness=0.5, color=C_BORDER, spaceAfter=4, spaceBefore=4)

def PB():
    return PageBreak()

def bold(t): return f"<b>{t}</b>"
def ital(t): return f"<i>{t}</i>"

# ─────────────────────────────────────────────────────────────────────────────
# CUSTOM FLOWABLES
# ─────────────────────────────────────────────────────────────────────────────

class NotarStempel(Flowable):
    "&quot;&quot;Rotes Rechteck mit Notar-Stempel-Text&quot;&quot;"
    def __init__(self, w=200, h=55):
        Flowable.__init__(self)
        self.w = w; self.h = h
    def wrap(self, *args): return self.w, self.h
    def draw(self):
        c = self.canv
        c.setStrokeColor(C_RED_STAMP); c.setLineWidth(2)
        c.rect(0, 0, self.w, self.h)
        c.setFillColor(C_RED_STAMP)
        c.setFont("Helvetica-Bold", 7)
        c.drawCentredString(self.w/2, self.h - 14, "NOTAR Dr. Ulfried Vorstetter")
        c.drawCentredString(self.w/2, self.h - 24, "Notariat Maximilianstraße 22, 80539 München")
        c.drawCentredString(self.w/2, self.h - 34, "UR-Nr. 1488/2023")
        c.setFont("Helvetica", 6)
        c.drawCentredString(self.w/2, self.h - 44, "Beurkundungsdatum: 12. Mai 2023")

class WhatsAppBubble(Flowable):
    "&quot;&quot;WhatsApp-Sprechblase&quot;&quot;"
    def __init__(self, sender, text, time_str, side="right", w=380):
        Flowable.__init__(self)
        self.sender = sender; self.text = text; self.time_str = time_str
        self.side = side; self.bw = w
        self.bh = max(60, 20 + len(text)//45 * 14 + 28)
    def wrap(self, *args): return self.bw, self.bh + 10
    def draw(self):
        c = self.canv
        bubble_w = self.bw * 0.65
        if self.side == "right":
            x = self.bw - bubble_w - 5
            bg = C_WA_GREEN
        else:
            x = 5
            bg = C_WA_GREY
        y = 5
        h = self.bh
        r = 8
        c.setFillColor(bg); c.setStrokeColor(HexColor("#BBBBBB")); c.setLineWidth(0.5)
        p = c.beginPath()
        p.roundRect(x, y, bubble_w, h, r)
        c.drawPath(p, fill=1, stroke=1)
        c.setFillColor(HexColor("#555555")); c.setFont("Helvetica-Bold", 7)
        c.drawString(x + 8, y + h - 13, self.sender)
        c.setFillColor(black); c.setFont("Helvetica", 8)
        lines = []
        words = self.text.split()
        line = ""
        for w_ in words:
            test = (line + " " + w_).strip()
            if c.stringWidth(test, "Helvetica", 8) < bubble_w - 16:
                line = test
            else:
                lines.append(line); line = w_
        if line: lines.append(line)
        for i, l in enumerate(lines):
            c.drawString(x + 8, y + h - 26 - i * 12, l)
        c.setFillColor(HexColor("#888888")); c.setFont("Helvetica", 6)
        c.drawRightString(x + bubble_w - 5, y + 4, self.time_str)

class AsciiBox(Flowable):
    "&quot;&quot;ASCII-Rahmen für Kanzlei-Logo&quot;&quot;"
    def __init__(self, lines, w=200, bg=None):
        Flowable.__init__(self)
        self.lines = lines; self.bw = w; self.bg = bg or C_LIGHT_BG
        self.bh = len(lines) * 11 + 12
    def wrap(self, *args): return self.bw, self.bh
    def draw(self):
        c = self.canv
        c.setFillColor(self.bg); c.setStrokeColor(C_BORDER); c.setLineWidth(0.5)
        c.rect(0, 0, self.bw, self.bh, fill=1)
        c.setFillColor(black); c.setFont("Courier", 8)
        for i, l in enumerate(self.lines):
            c.drawString(6, self.bh - 12 - i * 11, l)

class RedMarginNote(Flowable):
    "&quot;&quot;Rote Randnotiz (simuliert Aktenrand-Stift)&quot;&quot;"
    def __init__(self, text, w=480):
        Flowable.__init__(self)
        self.text = text; self.bw = w
        self.bh = 40 + len(text)//60 * 12
    def wrap(self, *args): return self.bw, self.bh
    def draw(self):
        c = self.canv
        c.setStrokeColor(C_MEMO_RED); c.setLineWidth(1.5)
        c.line(0, self.bh - 4, 0, 0)
        c.setFillColor(C_MEMO_RED); c.setFont("Helvetica-Oblique", 8)
        words = self.text.split(); line = ""; y = self.bh - 14; x = 8
        for w_ in words:
            test = (line + " " + w_).strip()
            if c.stringWidth(test, "Helvetica-Oblique", 8) < self.bw - 16:
                line = test
            else:
                c.drawString(x, y, line); line = w_; y -= 12
        if line: c.drawString(x, y, line)

# ─────────────────────────────────────────────────────────────────────────────
# HELPER: Az-Zeile
# ─────────────────────────────────────────────────────────────────────────────
def az_zeile(az="LG München I 12 O 8842/23"):
    return P(f"Az.: <b>{az}</b>", S_AZ)

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 1: AKTENDECKEL
# ─────────────────────────────────────────────────────────────────────────────
def section_aktendeckel():
    els = []
    els.append(SP(2))
    ascii_mönch = [
        "         +---------------------------+",
        "         |   LANDESGERICHT MÜNCHEN I |",
        "         |   Zivilkammer 12          |",
        "         +---------------------------+",
        "               .-'''''-.",
        "              /  (   )  \\",
        "             |   |||||   |",
        "              \\  `---'  /",
        "         ~~~~~ `._____.' ~~~~~",
        "           MÜNCHEN — STADTRECHT",
    ]
    els.append(AsciiBox(ascii_mönch, w=420))
    els.append(SP(1))
    els.append(P("━" * 72, S_CENTER))
    els.append(SP(0.5))
    els.append(P("<b>A K T E</b>", S_TITLE))
    els.append(SP(0.3))
    els.append(P("<b>Haspelbeck-Türkenfeld</b>", make_style("TMP1", fontName="Times-Bold", fontSize=14, leading=18, alignment=TA_CENTER)))
    els.append(P("<b>./.</b>", make_style("TMP2", fontName="Times-Roman", fontSize=12, leading=16, alignment=TA_CENTER)))
    els.append(P("<b>Immobilien-Vermittlung Marlene Bechtholdsmeier-Schongau e.K.</b>", make_style("TMP3", fontName="Times-Bold", fontSize=12, leading=16, alignment=TA_CENTER)))
    els.append(SP(0.5))
    els.append(HR())
    els.append(P("<b>Gegenstand:</b> Rückforderung Maklerprovision EUR 8.810,76", S_CENTER_B))
    els.append(P("<b>§§ 656a, 126b, 812 BGB</b> — Textform-Verstoß beim Verkäufer-Maklervertrag", S_CENTER))
    els.append(HR())
    els.append(SP(0.5))
    data = [
        ["Aktenzeichen:", "LG München I 12 O 8842/23"],
        ["Berufung:",     "OLG München 13 U 412/24"],
        ["Revision:",     "BGH I ZR 202/25"],
        ["Streitwert:",   "EUR 8.810,76 zzgl. Zinsen"],
        ["Angelegt:",     "22. Mai 2026"],
        ["Sachgebiet:",   "Zivilrecht — Immobilienmaklerrecht / Formvorschriften"],
    ]
    t = Table(data, colWidths=[130, 300])
    t.setStyle(TableStyle([
        ("FONTNAME",  (0,0), (-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 10),
        ("FONTNAME",  (0,0), (0,-1), "Helvetica-Bold"),
        ("BACKGROUND",(0,0), (-1,-1), C_LIGHT_BG),
        ("BOX",       (0,0), (-1,-1), 0.5, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.3, C_BORDER),
        ("TOPPADDING",(0,0),(-1,-1),4),
        ("BOTTOMPADDING",(0,0),(-1,-1),4),
    ]))
    els.append(t)
    els.append(SP(1))
    els.append(P("<b>Kläger:</b> Korbinian Haspelbeck-Türkenfeld und Walburga Haspelbeck-Türkenfeld,<br/>Mauerkircherstraße 47, 81679 München-Bogenhausen", S_NORMAL))
    els.append(P("<b>Beklagte:</b> Immobilien-Vermittlung Marlene Bechtholdsmeier-Schongau e.K.,<br/>Schwere-Reiter-Straße 18, 80637 München", S_NORMAL))
    els.append(SP(0.5))
    els.append(P("<b>Prozessbevollmächtigte Kläger:</b><br/>RA Dr. Knut Hagelbrand-Wittlsbach, Kanzlei Hagelbrand &amp; Trotzenburg Rechtsanwälte,<br/>Promenadeplatz 9, 80333 München", S_SMALL))
    els.append(P("<b>Prozessbevollmächtigte Beklagte:</b><br/>RAin Dr. Adelheid Korkenzieher-Mariastein, Kanzlei Korkenzieher Maibach Partner mbB,<br/>Karlsplatz 4, 80335 München", S_SMALL))
    els.append(SP(1))
    els.append(P("Datum der Aktenanlage: <b>22. Mai 2026</b>", S_SMALL))
    els.append(P("Gerichtsstand: Landgericht München I, Zivilkammer 12", S_SMALL))
    els.append(SP(0.5))
    els.append(P("━" * 72, S_CENTER))
    els.append(SP(0.5))
    els.append(P(ital("Hinweis: Diese Akte ist eine fiktive Testakte für Schulungszwecke.<br/>Alle Personen, Firmen und Sachverhalte sind frei erfunden."), S_TINY))
    els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 2: INHALTSVERZEICHNIS
# ─────────────────────────────────────────────────────────────────────────────
def section_inhaltsverzeichnis():
    els = []
    els.append(P("<b>INHALTSVERZEICHNIS</b>", S_TITLE))
    els.append(P("Akte Haspelbeck-Türkenfeld ./. Bechtholdsmeier-Schongau e.K.", S_CENTER))
    els.append(P("Az. LG München I 12 O 8842/23", S_CENTER))
    els.append(HR())
    els.append(SP(0.3))
    entries = [
        ("1.",  "Aktendeckel",                                             "1"),
        ("2.",  "Inhaltsverzeichnis",                                       "2"),
        ("3.",  "Mandatsannahmebogen RA Hagelbrand-Wittlsbach",              "3"),
        ("4.",  "Klageschrift vom 14. September 2023 (Anlage K-MAK-1)",      "4–11"),
        ("5.",  "Klageerwiderung vom 24. Oktober 2023",                      "12–21"),
        ("6.",  "Replik Kläger vom 17. November 2023",                       "22–27"),
        ("7.",  "E-Mail-Kette Haspelbeck/Bechtholdsmeier (Anl. K-MAK-2 ff.)","28–35"),
        ("8.",  "Notarieller Kaufvertrag-Auszug UR-Nr. 1488/2023 (K-MAK-5)","36–40"),
        ("9.",  "Zahlungsquittung Bechtholdsmeier (K-MAK-6)",               "41"),
        ("10.", "Hinweis Widerrufsbelehrung / Mail-Signatur-Volltext",       "42"),
        ("11.", "Vergleichsverhandlungsprotokoll 12. Juni 2024",             "43–44"),
        ("12.", "Berufungsschriftsatz OLG München vom 04. Juli 2024",        "45–48"),
        ("13.", "Berufungsbegründung Beklagte",                              "49–60"),
        ("14.", "Berufungserwiderung Kläger",                                "61–65"),
        ("15.", "Berufungsurteil OLG München 13 U 412/24 v. 17.02.2025",    "66–70"),
        ("16.", "Revisionsbegründung zum BGH (Az. I ZR 202/25)",             "71–79"),
        ("17.", "Revisionserwiderung Kläger",                                "80–84"),
        ("18.", "Stellungnahmen Verhandlungstermin BGH 11.03.2026",         "85–86"),
        ("19.", "BGH-Urteil Tenor-Auszug I ZR 202/25 v. 11.03.2026",       "87–88"),
        ("20.", "Mandantenmemo Hagelbrand-Wittlsbach v. 14.03.2026",        "89–90"),
        ("21.", "Handschriftliche Notizen Korbinian Haspelbeck",             "91"),
        ("22.", "WhatsApp-Screenshot Walburga/Korbinian Haspelbeck",        "92"),
        ("23.", "Kanzleirechnung Hagelbrand & Trotzenburg",                  "93–94"),
        ("24.", "Aktenrand-Memo RAin Korkenzieher-Mariastein (rot)",        "95"),
        ("25.", "Anlagenverzeichnis K-MAK-1 bis K-MAK-29",                  "96"),
        ("26.", "Stundenaufstellung Hagelbrand & Trotzenburg",              "97–99"),
    ]
    data = [["Nr.", "Bestandteil", "Seite(n)"]] + [[e[0], e[1], e[2]] for e in entries]
    t = Table(data, colWidths=[30, 360, 60])
    ts = TableStyle([
        ("FONTNAME",  (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME",  (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 9),
        ("BACKGROUND",(0,0), (-1,0), C_HEADER_BG),
        ("TEXTCOLOR", (0,0), (-1,0), white),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[white, C_LIGHT_BG]),
        ("BOX",       (0,0), (-1,-1), 0.5, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.2, C_BORDER),
        ("TOPPADDING",(0,0),(-1,-1),3),
        ("BOTTOMPADDING",(0,0),(-1,-1),3),
        ("ALIGN",     (2,0), (2,-1), "CENTER"),
    ])
    t.setStyle(ts)
    els.append(t)
    els.append(SP(0.5))
    els.append(HR())
    els.append(P("<i>Hinweis: Anlage K-MAK-7 (Vergleichsangebot Schriftform-Entwurf) sowie K-MAK-13 "
                 "(Grundbuchauszug) und K-MAK-21 (Maklerexposé Originalversion) befinden sich im "
                 "<b>Sonderband II</b> — nicht abgebildet. Vgl. Anlagenverzeichnis Bl. 96.</i>", S_SMALL))
    els.append(SP(0.3))
    els.append(P("<i>Querverweise innerhalb der Akte: vgl. Anlage K-MAK-7 — siehe Sonderband II; "
                 "vgl. Klageschrift Bl. 4 ff.; vgl. Berufungsurteil OLG München Bl. 66 ff.; "
                 "vgl. BGH I ZR 197/22 (Vorgänger-Linie) — in der Akte nicht beigefügt.</i>", S_TINY))
    els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 3: MANDATSANNAHMEBOGEN
# ─────────────────────────────────────────────────────────────────────────────
def section_mandatsannahme():
    els = []
    els.append(AsciiBox([
        " +=========================================+",
        " | H/T — Hagelbrand & Trotzenburg          |",
        " |        Rechtsanwälte                    |",
        " |   Promenadeplatz 9 · 80333 München      |",
        " |   Tel: 089/44 22 18-0 · Fax: -99        |",
        " +=========================================+",
    ], w=380))
    els.append(SP(0.5))
    els.append(P("<b>M A N D A T S A N N A H M E B O G E N</b>", S_H1))
    els.append(HR())
    els.append(SP(0.2))
    data = [
        ["Mandant/Mandantin:", "Korbinian Haspelbeck-Türkenfeld und Walburga Haspelbeck-Türkenfeld"],
        ["Anschrift:",         "Mauerkircherstraße 47, 81679 München-Bogenhausen"],
        ["Telefon:",           "089 / 98 44 27 11 (privat)"],
        ["E-Mail:",            "korbinian.haspelbeck@t-online.de"],
        ["Bearbeitender RA:",  "Dr. Knut Hagelbrand-Wittlsbach"],
        ["Stundensatz:",       "EUR 380,00 zzgl. USt."],
        ["Auftragserteilung:", "15. August 2023"],
        ["Aktenzeichen intern:","HT-2023-0892"],
        ["Streitgegenstand:",  "Rückforderung Maklerprovision EUR 8.810,76"],
        ["Rechtsnorm:",        "§§ 656a, 126b, 812 BGB — Textform-Verstoß"],
        ["Gericht:",           "LG München I, Zivilkammer 12 (Az. 12 O 8842/23)"],
        ["Retainer:",          "EUR 2.000,00 (Eingangsvorschuss, quittiert 16.08.2023)"],
    ]
    t = Table(data, colWidths=[130, 320])
    t.setStyle(TableStyle([
        ("FONTNAME",  (0,0), (0,-1), "Helvetica-Bold"),
        ("FONTNAME",  (1,0), (1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 9),
        ("BACKGROUND",(0,0), (-1,-1), C_LIGHT_BG),
        ("ROWBACKGROUNDS",(0,0),(-1,-1),[white, C_LIGHT_BG]),
        ("BOX",       (0,0), (-1,-1), 0.5, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.2, C_BORDER),
        ("TOPPADDING",(0,0),(-1,-1),4),
        ("BOTTOMPADDING",(0,0),(-1,-1),4),
    ]))
    els.append(t)
    els.append(SP(0.5))
    els.append(P("<b>Erstberatungsgespräch:</b>", S_BOLD))
    els.append(P("Am 15. August 2023 erschienen Herr Korbinian Haspelbeck-Türkenfeld und Frau Walburga "
                 "Haspelbeck-Türkenfeld im Büro der Kanzlei. Sie schilderten den Sachverhalt betreffend "
                 "den Verkauf ihres Einfamilienhauses in München-Bogenhausen über die Beklagte Bechtholdsmeier-"
                 "Schongau e.K. Es wurde dargelegt, dass die Provisionszahlung in Höhe von EUR 8.810,76 am "
                 "03. Juni 2023 per Banküberweisung geleistet worden sei. Die Mandantschaft zweifelt nunmehr "
                 "an der Wirksamkeit des Verkäufer-Maklervertrags mangels Textform nach § 656a BGB.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>Stundenschätzung bei Mandatsannahme:</b>", S_BOLD))
    stunden_data = [
        ["Phase", "Geschätzter Aufwand", "Ansatz", "Summe (netto)"],
        ["Erstberatung & Aktenaufbau", "4,0 Std.", "EUR 380/Std.", "EUR 1.520,00"],
        ["Klageschrift inkl. Recherche", "12,0 Std.", "EUR 380/Std.", "EUR 4.560,00"],
        ["Korrespondenz / Schriftverkehr", "6,0 Std.", "EUR 380/Std.", "EUR 2.280,00"],
        ["Verhandlungstermin(e)", "4,0 Std.", "EUR 380/Std.", "EUR 1.520,00"],
        ["Rechtsmittel (vorsorglich)", "8,0 Std.", "EUR 380/Std.", "EUR 3.040,00"],
        ["Gesamt (Schätzung)", "34,0 Std.", "—", "EUR 12.920,00"],
    ]
    t2 = Table(stunden_data, colWidths=[160, 100, 90, 100])
    t2.setStyle(TableStyle([
        ("FONTNAME",  (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME",  (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 9),
        ("BACKGROUND",(0,0), (-1,0), C_HEADER_BG),
        ("TEXTCOLOR", (0,0), (-1,0), white),
        ("FONTNAME",  (0,-1), (-1,-1), "Helvetica-Bold"),
        ("BACKGROUND",(0,-1), (-1,-1), C_YELLOW_HL),
        ("BOX",       (0,0), (-1,-1), 0.5, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.2, C_BORDER),
        ("TOPPADDING",(0,0),(-1,-1),4),
        ("BOTTOMPADDING",(0,0),(-1,-1),4),
        ("ALIGN",     (1,0), (-1,-1), "RIGHT"),
    ]))
    els.append(t2)
    els.append(SP(0.5))
    els.append(P("<i>Hinweis: Abrechnung erfolgt nach tatsächlichem Zeitaufwand gemäß Stundennachweis "
                 "(vgl. Anlage Stundenaufstellung Bl. 97–99 dieser Akte) oder nach RVG, je nachdem welcher "
                 "Betrag höher ausfällt. Mandantschaft wurde auf RVG-Option hingewiesen.</i>", S_SMALL))
    els.append(SP(0.5))
    els.append(P("München, 15. August 2023", S_NORMAL))
    els.append(SP(0.8))
    els.append(P("_____________________________________", S_NORMAL))
    els.append(P("Dr. Knut Hagelbrand-Wittlsbach, Rechtsanwalt", S_SMALL))
    els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 4: KLAGESCHRIFT (8 Seiten)
# ─────────────────────────────────────────────────────────────────────────────
def section_klageschrift():
    els = []
    # Seite 1 der Klageschrift
    els.append(P("Hagelbrand &amp; Trotzenburg Rechtsanwälte", S_BOLD))
    els.append(P("Promenadeplatz 9, 80333 München", S_NORMAL))
    els.append(SP(0.3))
    els.append(P("An das<br/>Landgericht München I<br/>Prielmayerstraße 7<br/>80335 München", S_NORMAL))
    els.append(SP(0.5))
    els.append(P("München, den <b>14. September 2023</b>", S_NORMAL))
    els.append(SP(0.3))
    els.append(HR())
    els.append(P("<b>K L A G E S C H R I F T</b>", S_TITLE))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("<b>der Eheleute Korbinian Haspelbeck-Türkenfeld und Walburga Haspelbeck-Türkenfeld,<br/>"
                 "Mauerkircherstraße 47, 81679 München,</b>", S_RUBRUM))
    els.append(P("— Kläger —", S_RUBRUM))
    els.append(SP(0.2))
    els.append(P("<b>Prozessbevollmächtigte:</b> Rechtsanwälte Hagelbrand &amp; Trotzenburg,<br/>"
                 "Promenadeplatz 9, 80333 München", S_RUBRUM))
    els.append(SP(0.3))
    els.append(P("<b>g e g e n</b>", S_RUBRUM))
    els.append(SP(0.3))
    els.append(P("<b>Immobilien-Vermittlung Marlene Bechtholdsmeier-Schongau e.K.,<br/>"
                 "gesetzlich vertreten durch die Inhaberin Marlene Bechtholdsmeier-Schongau,<br/>"
                 "Schwere-Reiter-Straße 18, 80637 München,</b>", S_RUBRUM))
    els.append(P("— Beklagte —", S_RUBRUM))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("<b>wegen</b> Rückforderung Maklerprovision (§ 812 Abs. 1 BGB, § 656a BGB)", S_CENTER_B))
    els.append(SP(0.3))
    els.append(P(f"<b>Streitwert:</b> EUR 8.810,76 nebst Zinsen in Höhe von 5 Prozentpunkten über dem Basiszinssatz "
                 f"seit dem 12. August 2023", S_NORMAL))
    els.append(SP(0.5))
    els.append(P("<b>KLAGEANTRÄGE</b>", S_H1))
    els.append(HR())
    els.append(SP(0.2))
    els.append(P("Die Kläger beantragen:", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("<b>1.</b> Die Beklagte wird verurteilt, an die Kläger EUR 8.810,76 (in Worten: achttausend "
                 "achthundertzehn Euro und sechsundsiebzig Cent) nebst Zinsen in Höhe von 5 Prozentpunkten "
                 "über dem Basiszinssatz seit dem 12. August 2023 zu zahlen.", S_ANTRAG))
    els.append(SP(0.2))
    els.append(P("<b>2.</b> Die Beklagte trägt die Kosten des Rechtsstreits.", S_ANTRAG))
    els.append(SP(0.2))
    els.append(P("<b>3.</b> Das Urteil ist gegen Sicherheitsleistung in Höhe von 110 % des beizutreibenden "
                 "Betrages vorläufig vollstreckbar.", S_ANTRAG))
    els.append(SP(0.5))
    els.append(P("<b>TATBESTAND / SACHVERHALT</b>", S_H1))
    els.append(HR())
    els.append(SP(0.2))
    els.append(P("<b>I. Die Parteien</b>", S_H2))
    els.append(P("Die Kläger, die Eheleute Korbinian und Walburga Haspelbeck-Türkenfeld, sind Eigentümer "
                 "eines Einfamilienhauses in München-Bogenhausen, Mauerkircherstraße 47, 81679 München. "
                 "Im Jahr 2023 beabsichtigten sie, dieses Anwesen zu veräußern und gleichzeitig eine "
                 "neue Immobilie zu erwerben. Die Beklagte ist die in München ansässige Maklerin Marlene "
                 "Bechtholdsmeier-Schongau, die unter der Firma „Immobilien-Vermittlung Marlene "
                 "Bechtholdsmeier-Schongau e.K.&quot; am Handelsregister München eingetragen ist "
                 "(HRA 98 871 München).", S_JUSTIFY))
    els.append(PB())

    # Seite 2 der Klageschrift
    els.append(az_zeile())
    els.append(P("<b>II. Käufer-Maklervertrag (unstreitig wirksam)</b>", S_H2))
    els.append(P("Die Kläger hatten die Beklagte auch damit beauftragt, ihnen beim Erwerb einer neuen "
                 "Immobilie behilflich zu sein. Dieser Käufer-Maklervertrag wurde ordnungsgemäß in "
                 "Textform nach § 656a BGB geschlossen. Die diesbezügliche Provision in Höhe von "
                 "EUR 7.329,30 (1,19 Prozent des Kaufpreises der neuen Immobilie) wurde von den Klägern "
                 "ebenfalls bezahlt und ist <b>nicht</b> Gegenstand der vorliegenden Klage. Dieser "
                 "Anspruch ist zwischen den Parteien unstreitig.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>III. Der streitige Verkäufer-Maklervertrag</b>", S_H2))
    els.append(P("Die Beklagte war ferner damit befasst, das Einfamilienhaus der Kläger in der "
                 "Mauerkircherstraße 47 zu einem Kaufpreis von EUR 617.000,00 zu veräußern. "
                 "In diesem Zusammenhang fanden Gespräche zwischen den Klägern und der Beklagten statt, "
                 "die — wie von der Beklagten behauptet — zum Abschluss eines Verkäufer-Maklervertrags "
                 "geführt haben sollen. Eine <b>gesonderte schriftliche oder elektronische Vereinbarung</b> "
                 "in der Form, die § 656a BGB i.V.m. § 126b BGB verlangt (d.h. mit ausreichend bestimmbarer "
                 "Erklärung und abgeschlossener, auf Dauer angelegter Speicherung), wurde nach "
                 "Auffassung der Kläger <b>nicht</b> getroffen.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>IV. Der E-Mail-Austausch</b>", S_H2))
    els.append(P("Am 30. März 2023 schrieben die Kläger an die Beklagte und äußerten ein Gegenangebot "
                 "hinsichtlich des Kaufpreises ihrer eigenen Immobilie. Am 03. April 2023 antwortete die "
                 "Beklagte mit einer E-Mail, welche — unterhalb der eigentlichen Mail-Signatur — folgenden "
                 "Hinweis enthielt (vollständiger Text vgl. Anlage K-MAK-2):", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(Preformatted(
        "    \"Wir weisen darauf hin, dass bei Abschluss eines Kaufvertrages bei einem\n"
        "    Einfamilienhaus eine vom Veräußerer und Erwerber zu zahlende Provision fällig\n"
        "    wird. Diese beläuft sich maximal auf drei Komma sieben Prozent des Kaufpreises\n"
        "    (inklusive gesetzlicher Mehrwertsteuer und je Partei), im Verkaufsfall...\"",
        S_MONO_SM))
    els.append(SP(0.2))
    els.append(P("Auf diese E-Mail antworteten die Kläger am 13. April 2023 mit der Formulierung „wie "
                 "besprochen&quot; und stimmten zu, dass die Beklagte einen Notartermin vereinbare. Eine "
                 "ausdrückliche Zustimmung zum Abschluss eines Maklervertrags zu bestimmten Konditionen "
                 "— insbesondere Benennung des genauen Provisionssatzes und des Käufernamens — fehlt "
                 "in dieser E-Mail vollständig.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>V. Notartermin und Kaufpreiszahlung</b>", S_H2))
    els.append(P("Am 12. Mai 2023 wurde vor dem Notar Dr. Ulfried Vorstetter, Maximilianstraße 22, "
                 "80539 München (UR-Nr. 1488/2023) der Kaufvertrag über das Einfamilienhaus der Kläger "
                 "zu einem Kaufpreis von EUR 617.000,00 beurkundet. Käufer waren die Eheleute Bartholomäus "
                 "und Hiltrud Höglmayr-Stockenfels. § 13 des Kaufvertrages enthält eine Maklerklausel, "
                 "in der die Kläger die Verpflichtung zur Zahlung einer Provision an die Beklagte "
                 "„anerkannten&quot;. Der Kaufvertrag wurde von den Klägern unter dem Eindruck einer "
                 "damals bestehenden Überzeugung unterzeichnet, die Beklagte habe alle formellen "
                 "Voraussetzungen eingehalten.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("Am 15. Mai 2023 stellte die Beklagte Rechnung über EUR 8.810,76 (entspricht 1,19 Prozent "
                 "des Kaufpreises EUR 617.000,00 brutto inkl. Umsatzsteuer = 1,2 Prozent). Die Kläger "
                 "bezahlten diesen Betrag am 03. Juni 2023 per Banküberweisung.", S_JUSTIFY))
    els.append(PB())

    # Seite 3 der Klageschrift
    els.append(az_zeile())
    els.append(P("<b>BEGRÜNDUNG</b>", S_H1))
    els.append(HR())
    els.append(SP(0.2))
    els.append(P("<b>A. Anspruchsgrundlage: § 812 Abs. 1 S. 1, 1. Alt. BGB (condictio indebiti)</b>", S_H2))
    els.append(P("Die Kläger machen einen Bereicherungsanspruch aus § 812 Abs. 1 Satz 1, 1. Alternative "
                 "BGB geltend. Die Zahlung der Maklerprovision in Höhe von EUR 8.810,76 erfolgte auf "
                 "der Grundlage eines vermeintlichen Maklervertrags, der jedoch — wie im Folgenden "
                 "dargelegt — mangels Textform nach § 656a BGB i.V.m. § 126b BGB unwirksam ist. "
                 "Der Bereicherungsgegenstand (= die geleistete Zahlung) ist ohne Rechtsgrund in das "
                 "Vermögen der Beklagten gelangt und daher zurückzugewähren.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>B. Fehlendes Textformerfordernis gemäß § 656a BGB i.V.m. § 126b BGB</b>", S_H2))
    els.append(P("<b>1. Gesetzliche Grundlage</b>", S_H2))
    els.append(P("§ 656a BGB, eingefügt durch das Gesetz über die Verteilung von Maklerkosten bei der "
                 "Vermittlung von Kaufverträgen über Wohnungen und Einfamilienhäuser vom 12. Juni 2020 "
                 "(BGBl. I S. 1245), bestimmt:", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(Preformatted(
        "    § 656a BGB (Textform)\n"
        "    Ein Maklervertrag, der den Nachweis der Gelegenheit zum Abschluss eines Kaufvertrags\n"
        "    über eine Wohnung oder ein Einfamilienhaus oder die Vermittlung eines solchen Kaufvertrags\n"
        "    zum Gegenstand hat, bedarf der Textform.", S_MONO_SM))
    els.append(SP(0.2))
    els.append(P("§ 126b BGB definiert die Textform wie folgt:", S_JUSTIFY))
    els.append(Preformatted(
        "    § 126b BGB (Textform)\n"
        "    Ist durch Gesetz Textform vorgeschrieben, so muss eine lesbare Erklärung,\n"
        "    in der die Person des Erklärenden genannt ist, auf einem dauerhaften Datenträger\n"
        "    abgegeben werden. Ein dauerhafter Datenträger ist jedes Medium, das\n"
        "    1. es dem Empfänger ermöglicht, eine auf dem Datenträger befindliche,\n"
        "       an ihn persönlich gerichtete Erklärung so aufzubewahren oder zu speichern,\n"
        "       dass sie ihm während eines für ihren Zweck angemessenen Zeitraums zugänglich ist,\n"
        "       und\n"
        "    2. geeignet ist, die Erklärung unverändert wiederzugeben.", S_MONO_SM))
    els.append(SP(0.3))
    els.append(P("<b>2. E-Mail als dauerhafter Datenträger — aber fehlende Bestimmtheit</b>", S_H2))
    els.append(P("Die Kläger verkennen nicht, dass eine E-Mail grundsätzlich einen dauerhaften Datenträger "
                 "i.S.d. § 126b BGB darstellen kann. Der Bundesgerichtshof hat jedoch in seinem Urteil "
                 "vom 17. November 2022 (BGH I ZR 197/22, NJW 2023, 441) klargestellt, dass eine "
                 "Textform-Erklärung zum Abschluss eines Maklervertrags nach § 656a BGB nur dann "
                 "wirksam ist, wenn die vertraglichen Hauptpflichten — insbesondere Art des Maklerangebots, "
                 "Provisionshöhe und der Umstand, dass eine rechtliche Bindung begründet werden soll — "
                 "ausreichend bestimmbar in der Erklärung enthalten sind.", S_JUSTIFY))
    els.append(PB())

    # Seite 4 der Klageschrift
    els.append(az_zeile())
    els.append(P("<b>3. Analyse des vorliegenden E-Mail-Austauschs</b>", S_H2))
    els.append(P("Die Beklagte hat den maßgeblichen Hinweis auf die Provision nicht in die eigentliche "
                 "Mail-Erklärung aufgenommen, sondern — rein formularmäßig — in den unteren Bereich "
                 "der E-Mail-Signatur platziert. Dies erfüllt die Anforderungen an eine Textform-Erklärung "
                 "aus mehreren Gründen nicht:", S_JUSTIFY))
    els.append(SP(0.2))
    punkte = [
        ("<b>Fehlende Vertragsnatur der Erklärung:</b> Der in der Signatur enthaltene \"Hinweis zur "
         "Fälligkeit der Provision\" ist keine auf Vertragsschluss gerichtete Willenserklärung, sondern "
         "ein automatisch angefügter Standardtext, der keinen Bezug auf das konkrete Objekt (Mauerkircherstraße 47), "
         "den konkreten Kaufpreis (EUR 617.000,00) oder den konkreten Erwerber (Eheleute Höglmayr-Stockenfels) nimmt."),
        ("<b>Fehlen wesentlicher Vertragsbestandteile:</b> Ein Maklervertrag nach § 656a BGB erfordert die "
         "Bestimmbarkeit der wesentlichen Elemente: Welche Leistung soll der Makler erbringen? Für welches "
         "Objekt? Zu welchem Provisionssatz und für welchen Bestimmungszeitraum? Der vorliegende "
         "Signatur-Hinweis enthält weder das konkrete Objekt noch einen festen Prozentsatz (es heißt „maximal "
         "drei Komma sieben Prozent&quot;), noch einen Käufernamen."),
        ("<b>Kein übereinstimmender Erklärungswille:</b> Die Antwort der Kläger vom 13. April 2023 "
         "„wie besprochen Zustimmung Notartermin&quot; bezieht sich erkennbar auf die Terminkoordination, "
         "nicht auf den Abschluss eines Maklervertrags zu bestimmten Konditionen. Eine objektive Auslegung "
         "nach §§ 133, 157 BGB ergibt keinen auf Provisionsvereinbarung gerichteten Erklärungswillen."),
        ("<b>Schutzzweck des § 656a BGB:</b> Der Gesetzgeber hat mit § 656a BGB bewusst ein strenges "
         "Formerfordernis eingeführt, um Verbraucher vor überraschenden Provisionsverpflichtungen zu "
         "schützen. Dieser Schutzzweck würde leerlaufen, wenn automatisch generierte Signaturhinweise "
         "ohne objekt- oder käuferbezogenen Inhalt genügten."),
    ]
    for i, p in enumerate(punkte, 1):
        els.append(P(f"<b>{i}.</b> {p}", S_JUSTIFY))
        els.append(SP(0.2))
    els.append(SP(0.3))
    els.append(P("<b>C. Kein Ausschluss des Bereicherungsanspruchs</b>", S_H2))
    els.append(P("Die Beklagte kann dem Bereicherungsanspruch der Kläger keinen Einwand der Entreicherung "
                 "nach § 818 Abs. 3 BGB entgegenhalten. Die Beklagte ist eine gewerbliche Maklerin. "
                 "§ 819 Abs. 1 BGB verschärft die Haftung des Bereicherungsschuldners, der den Mangel "
                 "des rechtlichen Grundes kennt oder kennen musste. Eine gewerbliche Maklerin muss die "
                 "Formvorschrift des § 656a BGB kennen und ist daher bösgläubig i.S.d. § 819 BGB.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>D. Notarielle Maklerklausel (§ 13 Kaufvertrag) — kein Vertragsschluss</b>", S_H2))
    els.append(P("Die in § 13 des notariellen Kaufvertrags UR-Nr. 1488/2023 enthaltene Bestimmung, "
                 "wonach die Veräußerer (Kläger) die Provisionsverbindlichkeit gegenüber der Beklagten "
                 "„anerkennen&quot;, vermag einen wirksamen Maklervertrag nicht zu substituieren. Die "
                 "notarielle Maklerklausel bezweckt nach der Rechtsprechung des BGH lediglich die "
                 "Publizierung einer bereits wirksam bestehenden Provisionsvereinbarung — sie kann aber "
                 "keinen formnichtigen Maklervertrag heilen (BGH I ZR 197/22; vgl. auch BGH I ZR 284/20, "
                 "NJW 2022, 1896, Rn. 27 ff.).", S_JUSTIFY))
    els.append(PB())

    # Seite 5 der Klageschrift
    els.append(az_zeile())
    els.append(P("<b>E. Hilfsweise: Widerruf nach §§ 312g, 355 BGB</b>", S_H2))
    els.append(P("Hilfsweise erklären die Kläger vorsorglich den Widerruf eines etwaigen Fernabsatz-"
                 "Verbrauchervertrags nach § 312g BGB, da der E-Mail-Austausch außerhalb der "
                 "Geschäftsräume der Beklagten stattfand. Die Beklagte hat keine den Anforderungen "
                 "der Art. 246a § 1 Abs. 2 EGBGB genügende Widerrufsbelehrung erteilt. Der anwaltlich "
                 "übermittelte Widerruf vom 03. August 2023 (Anlage K-MAK-8) wurde fristgemäß erklärt. "
                 "Auf die Frage, ob die 14-tägige Widerrufsfrist nach § 355 Abs. 2 BGB überhaupt "
                 "begonnen hat, kommt es damit nicht an.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>F. Zinsen</b>", S_H2))
    els.append(P("Die Zinsforderung ergibt sich aus §§ 286, 288 BGB. Die Beklagte befindet sich "
                 "seit dem 12. August 2023 in Verzug (Antwortschreiben RAin Korkenzieher-Mariastein "
                 "vom 12. August 2023 = endgültige Leistungsverweigerung, Anlage K-MAK-9).", S_JUSTIFY))
    els.append(SP(0.5))
    els.append(P("<b>BEWEIS</b>", S_H1))
    els.append(HR())
    els.append(SP(0.2))
    beweis = [
        ["Anlage", "Beweismittel", "Punkt"],
        ["K-MAK-1", "Handelsregisterauszug HRA 98 871, AG München", "Passivlegitimation"],
        ["K-MAK-2", "E-Mail-Kette März–August 2023 (Volltext)", "III./IV. Sachverhalt"],
        ["K-MAK-3", "Notarieller Kaufvertrag UR-Nr. 1488/2023, Auszug", "V. Notartermin"],
        ["K-MAK-4", "Kontoauszug Haspelbeck v. 03.06.2023 (Überweisung)", "V. Zahlung"],
        ["K-MAK-5", "Rechnung Bechtholdsmeier v. 15.05.2023", "V. Rechnung"],
        ["K-MAK-6", "Zahlungsquittung Bechtholdsmeier v. 10.06.2023", "V. Zahlung"],
        ["K-MAK-7", "Schriftform-Entwurf (nicht vorliegend — Sonderband II)", "—"],
        ["K-MAK-8", "Widerrufserklärung v. 03.08.2023 (RA Hagelbrand)", "E. Widerruf"],
        ["K-MAK-9", "Zurückweisung RAin Korkenzieher v. 12.08.2023", "F. Verzug"],
    ]
    tb = Table(beweis, colWidths=[65, 280, 105])
    tb.setStyle(TableStyle([
        ("FONTNAME",  (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME",  (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 8),
        ("BACKGROUND",(0,0), (-1,0), C_HEADER_BG),
        ("TEXTCOLOR", (0,0), (-1,0), white),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[white, C_LIGHT_BG]),
        ("BOX",       (0,0), (-1,-1), 0.5, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.2, C_BORDER),
        ("TOPPADDING",(0,0),(-1,-1),3),
        ("BOTTOMPADDING",(0,0),(-1,-1),3),
    ]))
    els.append(tb)
    els.append(SP(0.5))
    els.append(P("Wir bitten um Terminbestimmung und stellen für den Termin die Kläger als Partei "
                 "und im Übrigen Zeugenbeweis durch Benennung der Beklagten Marlene Bechtholdsmeier-"
                 "Schongau als Zeugin in Aussicht.", S_JUSTIFY))
    els.append(SP(0.5))
    els.append(P("München, den 14. September 2023", S_NORMAL))
    els.append(SP(0.8))
    els.append(P("_____________________________________<br/>Dr. Knut Hagelbrand-Wittlsbach<br/>Rechtsanwalt", S_NORMAL))
    els.append(PB())

    # Seiten 6-8 der Klageschrift: vertiefende Argumentation
    els.append(az_zeile())
    els.append(P("<b>ERGÄNZENDE RECHTLICHE AUSFÜHRUNGEN (Anlage zur Klageschrift)</b>", S_H1))
    els.append(HR())
    els.append(SP(0.2))
    els.append(P("<b>I. Entwicklung der BGH-Rechtsprechung zu § 656a BGB</b>", S_H2))
    els.append(P("§ 656a BGB trat am 23. Dezember 2020 in Kraft. Seitdem hat der BGH in mehreren "
                 "Urteilen die Anforderungen an den Textformabschluss von Maklerverträgen präzisiert:", S_JUSTIFY))
    els.append(SP(0.2))
    rs = [
        ("BGH I ZR 113/21", "NJW 2022, 1891", "Grundsatz: E-Mail kann Textform wahren, wenn ausreichend bestimmt"),
        ("BGH I ZR 284/20", "NJW 2022, 1896", "Notarielle Maklerklausel heilt keinen formnichtigen Maklervertrag"),
        ("BGH I ZR 197/22", "NJW 2023, 441",  "Bestimmtheitserfordernis: Provisionshöhe, Leistungsbeschreibung"),
        ("BGH I ZR 42/23",  "NJW 2024, 223",  "Signatur-Hinweis allein genügt nicht"),
        ("BGH I ZR 202/25", "Urt. v. 11.03.2026", "Vorliegender Fall — Revision zurückgewiesen"),
    ]
    data_rs = [["Aktenzeichen", "Fundstelle", "Leitsatz (vereinfacht)"]] + list(rs)
    t_rs = Table(data_rs, colWidths=[90, 95, 265])
    t_rs.setStyle(TableStyle([
        ("FONTNAME",  (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME",  (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 8),
        ("BACKGROUND",(0,0), (-1,0), C_HEADER_BG),
        ("TEXTCOLOR", (0,0), (-1,0), white),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[white, C_LIGHT_BG]),
        ("BOX",       (0,0), (-1,-1), 0.5, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.2, C_BORDER),
        ("TOPPADDING",(0,0),(-1,-1),3),
        ("BOTTOMPADDING",(0,0),(-1,-1),3),
    ]))
    els.append(t_rs)
    els.append(SP(0.4))
    els.append(P("<b>II. Schutzzweck des § 656a BGB — Verbraucherschutz und Übereilungsschutz</b>", S_H2))
    els.append(P("Der Gesetzgeber hat mit Einführung des § 656a BGB den Formzwang auf Textform "
                 "beschränkt (und nicht Schriftform nach § 126 BGB vorgeschrieben), um eine praktische "
                 "Handhabbarkeit zu gewährleisten. Gleichwohl hat er damit einen Mindestschutz "
                 "etabliert: Der Maklervertrag muss so klar formuliert sein, dass der Verbraucher "
                 "erkennen kann, (a) dass er eine vertragliche Bindung eingeht, (b) zu welchem "
                 "Provisionssatz, (c) für welches konkrete Objekt und (d) gegenüber welchem Makler. "
                 "Dies folgt aus dem systematischen Zusammenhang mit § 126b BGB und dem Gebot "
                 "der Vertragsklarheit (vgl. BT-Drs. 19/15827, S. 18).", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>III. Vergleich mit dem vorliegenden Fall</b>", S_H2))
    els.append(P("Im vorliegenden Fall fehlen sämtliche der genannten Klarheitselemente: "
                 "Die E-Mail der Beklagten vom 03. April 2023 benennt weder das konkrete Objekt noch "
                 "die genaue Provisionshöhe (sondern lediglich ein „Maximum&quot;), noch wird der "
                 "Erwerber benannt. Die Antwort der Kläger vom 13. April 2023 bezieht sich auf "
                 "einen Notartermin, nicht auf eine Provisionsvereinbarung. Ein übereinstimmender, "
                 "auf Vertragsbegründung gerichteter Erklärungswille lässt sich nicht feststellen.", S_JUSTIFY))
    els.append(PB())

    els.append(az_zeile())
    els.append(P("<b>IV. Bereicherungsrechtliche Folgen</b>", S_H2))
    els.append(P("Da der Maklervertrag mangels Textform nach § 656a BGB i.V.m. § 125 BGB nichtig ist, "
                 "hat die Beklagte die Maklerprovision ohne rechtlichen Grund empfangen. Die Rückforderung "
                 "ergibt sich aus § 812 Abs. 1 Satz 1, 1. Alternative BGB (Leistungskondiktion). "
                 "Der Bereicherungsanspruch ist weder durch § 817 Satz 2 BGB ausgeschlossen "
                 "(da die Formvorschrift nicht zu Lasten beider Parteien gilt) noch durch § 818 "
                 "Abs. 3 BGB (Entreicherung), da die Beklagte als Unternehmerin bösgläubig im Sinne "
                 "des § 819 BGB ist.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>V. Berechnung der Klageforderung</b>", S_H2))
    berechnung = [
        ["Position", "Betrag"],
        ["Kaufpreis Mauerkircherstraße 47, München-Bogenhausen", "EUR 617.000,00"],
        ["Provision (brutto, 1,2 % inkl. 19 % USt.)", "EUR 7.404,00"],
        ["Hinweis: Laut Rechnung v. 15.05.2023 (Anlage K-MAK-5)", "EUR 8.810,76"],
        ["(Differenz erklärt sich aus angewandtem Prozentsatz 1,427 %", ""],
        [" = 1,19 % + 19 % USt. auf EUR 7.403,00 = EUR 1.406,57 ≈ EUR 8.810,76)", ""],
        ["Klageforderung", "EUR 8.810,76"],
    ]
    tb2 = Table(berechnung, colWidths=[340, 110])
    tb2.setStyle(TableStyle([
        ("FONTNAME",  (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME",  (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 9),
        ("BACKGROUND",(0,0), (-1,0), C_HEADER_BG),
        ("TEXTCOLOR", (0,0), (-1,0), white),
        ("FONTNAME",  (0,-1), (-1,-1), "Helvetica-Bold"),
        ("BOX",       (0,0), (-1,-1), 0.5, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.2, C_BORDER),
        ("TOPPADDING",(0,0),(-1,-1),4),
        ("BOTTOMPADDING",(0,0),(-1,-1),4),
        ("ALIGN",     (1,0), (1,-1), "RIGHT"),
    ]))
    els.append(tb2)
    els.append(SP(0.5))
    els.append(P("<i>Anmerkung Kanzlei H/T intern: Die exakte Provision-Berechnung beruht auf der "
                 "Rechnung der Beklagten, die 1,427 % des Kaufpreises (netto) in Rechnung gestellt hat. "
                 "Vgl. detaillierte Berechnung Anlage K-MAK-5. Abweichung zum angegebenen Satz von "
                 "„maximal 3,7 %&quot; ist erklärungsbedürftig — die Beklagte stellte offenbar nur die "
                 "Verkäuferseite (hälftige Provision gemäß § 656d BGB) in Rechnung.</i>", S_SMALL))
    els.append(PB())
    return els


# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 5: KLAGEERWIDERUNG (10 Seiten)
# ─────────────────────────────────────────────────────────────────────────────
def section_klageerwiderung():
    els = []
    els.append(AsciiBox([
        " +==========================================+",
        " | K/M — Korkenzieher Maibach Partner mbB  |",
        " |        Rechtsanwältinnen u. Rechtsanwälte|",
        " |   Karlsplatz 4 · 80335 München           |",
        " |   Tel: 089/55 88 33-0 · Fax: -50         |",
        " +==========================================+",
    ], w=380))
    els.append(SP(0.5))
    els.append(P("An das<br/>Landgericht München I<br/>Prielmayerstraße 7<br/>80335 München", S_NORMAL))
    els.append(SP(0.3))
    els.append(P("München, den <b>24. Oktober 2023</b>", S_NORMAL))
    els.append(HR())
    els.append(P("<b>KLAGEERWIDERUNG</b>", S_TITLE))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("in dem Rechtsstreit", S_RUBRUM))
    els.append(SP(0.2))
    els.append(P("<b>Haspelbeck-Türkenfeld ./. Bechtholdsmeier-Schongau e.K.</b>", S_RUBRUM))
    els.append(P("Az. LG München I 12 O 8842/23", S_RUBRUM))
    els.append(SP(0.3))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("namens und im Auftrag der Beklagten erwidert die Unterzeichnerin wie folgt:", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>ANTRÄGE</b>", S_H1))
    els.append(HR())
    els.append(P("Die Beklagte beantragt:", S_JUSTIFY))
    els.append(P("<b>1.</b> Die Klage wird abgewiesen.", S_ANTRAG))
    els.append(P("<b>2.</b> Die Kläger tragen die Kosten des Rechtsstreits.", S_ANTRAG))
    els.append(P("<b>3.</b> Das Urteil ist vorläufig vollstreckbar.", S_ANTRAG))
    els.append(SP(0.5))
    els.append(P("<b>BEGRÜNDUNG</b>", S_H1))
    els.append(HR())
    els.append(SP(0.2))
    els.append(P("<b>I. Wirksamer Verkäufer-Maklervertrag in Textform</b>", S_H2))
    els.append(P("Entgegen der Auffassung der Kläger wurde zwischen den Parteien ein wirksamer "
                 "Verkäufer-Maklervertrag in Textform nach § 656a BGB i.V.m. § 126b BGB geschlossen. "
                 "Der maßgebliche Vertragsschluss vollzog sich durch den E-Mail-Austausch der Parteien "
                 "im Zeitraum März/April 2023.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>1. Die E-Mail der Beklagten vom 03. April 2023 als Angebot</b>", S_H2))
    els.append(P("Die E-Mail der Beklagten vom 03. April 2023 enthält unter der Signatur einen "
                 "ausdrücklichen Hinweis auf die Provision. Dieser Hinweis ist — entgegen der "
                 "klägerischen Darstellung — kein bloßer Standardtext, sondern eine auf Vertragsschluss "
                 "gerichtete vorformulierte Erklärung im Sinne eines Angebots zum Abschluss eines "
                 "Maklervertrags. Die Beklagte weist in diesem Zusammenhang darauf hin, dass der BGH "
                 "in seinem Urteil I ZR 113/21 ausgeführt hat, dass ein Angebot zum Abschluss eines "
                 "Maklervertrags in Textform auch in einem standardisierten Mail-Hinweis enthalten "
                 "sein kann, sofern dieser hinreichend bestimmt ist.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>2. Annahme durch Kläger vom 13. April 2023</b>", S_H2))
    els.append(P("Die Kläger haben mit ihrer E-Mail vom 13. April 2023 &#8212; &quot;wie besprochen&quot; &#8212; der "
                 "Tätigkeit der Beklagten als Maklerin zugestimmt und ausdrücklich die Vereinbarung "
                 "eines Notartermins veranlasst. Hierin liegt eine konkludente Annahme des "
                 "Maklervertragsangebots. Jedenfalls ist die Erklärung nach dem Empfängerhorizont "
                 "(§§ 133, 157 BGB) als Zustimmung zur Maklertätigkeit zu werten.", S_JUSTIFY))
    els.append(PB())

    els.append(az_zeile())
    els.append(P("<b>II. Hilfsweise: Notarielle Maklerklausel § 13 Kaufvertrag</b>", S_H2))
    els.append(P("Selbst wenn man — was die Beklagte bestreitet — den E-Mail-Austausch als nicht "
                 "ausreichend für eine Textform-Vereinbarung ansehen würde, so ergibt sich die "
                 "Provisionspflicht jedenfalls aus der notariellen Maklerklausel in § 13 des "
                 "Kaufvertrages UR-Nr. 1488/2023. Dort haben die Kläger als Veräußerer die "
                 "Provisionsverbindlichkeit gegenüber der Beklagten ausdrücklich und notariell beurkundet "
                 "anerkannt. Ein notariell beurkundetes Anerkenntnis erfüllt auch die Anforderungen "
                 "der Textform nach § 126b BGB (und geht darüber hinaus, da die notarielle Beurkundung "
                 "eine höhere Authentizitätsstufe darstellt).", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>Wortlaut § 13 Abs. 1 des Kaufvertrages (UR-Nr. 1488/2023):</b>", S_BOLD))
    els.append(Preformatted(
        "    „Die Veräußerer erklären, mit der Maklerin, der Firma Immobilien-Vermittlung\n"
        "    Marlene Bechtholdsmeier-Schongau e.K., Schwere-Reiter-Straße 18, 80637 München,\n"
        "    einen Maklervertrag geschlossen zu haben. Sie verpflichten sich, dieser für\n"
        "    den Nachweis des vorliegenden Kaufvertrages eine Provision in Höhe von\n"
        "    1,19 Prozent (inklusive gesetzlicher Mehrwertsteuer) des beurkundeten\n"
        "    Kaufpreises zu zahlen, mithin EUR 7.343,30 (in Worten: siebentausenddreihundert-\n"
        "    dreiundvierzig Euro und dreißig Cent).\"\n"
        "    [Anmerkung: Tatsächlich gezahlt EUR 8.810,76 lt. Rechnung v. 15.05.2023]",
        S_MONO_SM))
    els.append(SP(0.3))
    els.append(P("<b>III. Hilfsweise: Wertersatzanspruch</b>", S_H2))
    els.append(P("Für den Fall, dass das Gericht sowohl den E-Mail-Abschluss als auch die notarielle "
                 "Maklerklausel als nicht ausreichend erachtet, macht die Beklagte hilfsweise einen "
                 "Wertersatzanspruch nach § 818 Abs. 2 BGB geltend. Die Beklagte hat die im Makler-"
                 "vertrag versprochene Leistung — nämlich den Nachweis der Kaufgelegenheit und die "
                 "Vermittlung des Kaufvertrags mit den Eheleuten Höglmayr-Stockenfels — vollständig "
                 "erbracht. Der Kaufvertrag ist wirksam geschlossen und vollzogen worden. "
                 "Der übliche Wert dieser Maklertätigkeit entspricht mindestens der in Rechnung "
                 "gestellten Provision.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>IV. Hilfsweise hilfsweise: Entreicherung (§ 818 Abs. 3 BGB)</b>", S_H2))
    els.append(P("Für den — von der Beklagten bestrittenen — Fall, dass ein Bereicherungsanspruch "
                 "besteht, beruft sich die Beklagte auf Entreicherung gemäß § 818 Abs. 3 BGB. "
                 "Die Provision wurde vollständig für betriebliche Aufwendungen im Zusammenhang "
                 "mit der Makleraktivität verwandt (Personalkosten, Fahrtkosten, Vermarktungskosten). "
                 "Eine Bereicherung der Beklagten ist daher nicht mehr vorhanden.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<i>Die Beklagte behält sich vor, weiteren Schriftsatzbedarf anzumelden.</i>", S_SMALL))
    els.append(SP(0.5))
    els.append(P("München, den 24. Oktober 2023", S_NORMAL))
    els.append(SP(0.8))
    els.append(P("_____________________________________<br/>Dr. Adelheid Korkenzieher-Mariastein<br/>Rechtsanwältin", S_NORMAL))
    els.append(PB())

    # Weitere Seiten Klageerwiderung
    els.append(az_zeile())
    els.append(P("<b>VERTIEFENDE AUSFÜHRUNGEN ZUR KLAGEERWIDERUNG</b>", S_H1))
    els.append(HR())
    els.append(P("<b>V. Zur Bestimmtheit der Textform-Erklärung — Gegendarstellung</b>", S_H2))
    els.append(P("Die Kläger behaupten, der Signatur-Hinweis enthalte keine hinreichend bestimmte "
                 "Erklärung. Dies ist unzutreffend. Der BGH hat in seiner Entscheidung I ZR 113/21 "
                 "(NJW 2022, 1891) ausgeführt, dass an die Bestimmtheit einer Textform-Erklärung "
                 "keine überspannten Anforderungen gestellt werden dürfen. Es genüge, wenn aus "
                 "dem Kontext der E-Mail-Konversation eindeutig erkennbar sei, auf welches Objekt "
                 "sich die Maklerprovision bezieht. Vorliegend bezieht sich die E-Mail-Konversation "
                 "ausschließlich auf das Einfamilienhaus Mauerkircherstraße 47, München-Bogenhausen. "
                 "Ein anderes Objekt war nicht Gegenstand der Kommunikation.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("Zudem enthält der Provisionssatz in der Signatur zwar das Wort „maximal&quot;, jedoch ist "
                 "aus dem Gesamtkontext und der Branchenüblichkeit erkennbar, dass die Provision "
                 "tatsächlich zu dem Höchstsatz berechnet werden wird. Die Angabe eines Höchstsatzes "
                 "genügt nach Auffassung der Beklagten für die Bestimmbarkeit.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>VI. Zum Bereicherungsausschluss nach § 817 Satz 2 BGB</b>", S_H2))
    els.append(P("Selbst wenn man einen Formverstoß annehmen würde — was die Beklagte ausdrücklich "
                 "bestreitet — so stünde dem Rückforderungsanspruch der Kläger § 817 Satz 2 BGB "
                 "entgegen. Die Kläger haben durch die Unterzeichnung des notariellen Kaufvertrags, "
                 "in dem § 13 ausdrücklich die Provisionsverbindlichkeit anerkennt, wissentlich eine "
                 "Verbindlichkeit auf sich genommen und sind daher dem Kondiktionsverbot unterworfen. "
                 "Jedenfalls ist die Berufung auf den Formmangel nach § 242 BGB (Treu und Glauben) "
                 "als unzulässige Rechtsausübung zu werten, da die Kläger die Maklertätigkeit der "
                 "Beklagten vollständig in Anspruch genommen haben.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>VII. Zum Widerrufsrecht (§§ 312g, 355 BGB)</b>", S_H2))
    els.append(P("Ein Widerrufsrecht der Kläger besteht nicht. Die Beklagte hat beim Abschluss des "
                 "Käufer-Maklervertrags — der in den Geschäftsräumen der Beklagten (Schwere-Reiter-"
                 "Straße 18) geschlossen wurde — eine Widerrufsbelehrung nach Art. 246a § 1 Abs. 2 "
                 "EGBGB erteilt. Die Beklagte verweist insoweit auf das Schreiben vom August 2022 "
                 "(beim Käufer-Maklervertrag mitgesandt). Auch wenn dieses beim Verkäufer-Maklervertrag "
                 "nicht explizit wiederholt wurde, so ergibt sich aus dem Gesamtzusammenhang, dass "
                 "die Kläger über ihr Widerrufsrecht informiert waren.", S_JUSTIFY))
    els.append(SP(0.5))
    els.append(P("<b>BEWEISANGEBOTE</b>", S_H1))
    els.append(HR())
    els.append(P("Die Beklagte stellt Beweis wie folgt:", S_JUSTIFY))
    for b in [
        "Zeugenvernehmung Marlene Bechtholdsmeier-Schongau: Zu den geführten Telefongesprächen vor dem E-Mail-Austausch und der telefonischen Einigung über die Provision (Höhe: 1,19 % netto = 1,427 % brutto)",
        "Zeugenvernehmung Bartholomäus Höglmayr-Stockenfels: Zum Ablauf der Kaufverhandlungen und der Rolle der Beklagten als Vermittlerin",
        "Zeugenvernehmung Notar Dr. Ulfried Vorstetter: Zur Unterzeichnung und Billigung der Maklerklausel § 13 beim Notartermin am 12. Mai 2023",
        "Vorlage der vollständigen E-Mail-Korrespondenz zwischen den Parteien",
    ]:
        els.append(P(f"— {b}", S_JUSTIFY))
    els.append(SP(0.5))
    els.append(P("München, den 24. Oktober 2023", S_NORMAL))
    els.append(SP(0.6))
    els.append(P("_____________________________________<br/>Dr. Adelheid Korkenzieher-Mariastein<br/>Rechtsanwältin", S_NORMAL))
    els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 6: REPLIK (6 Seiten)
# ─────────────────────────────────────────────────────────────────────────────
def section_replik():
    els = []
    els.append(P("Hagelbrand &amp; Trotzenburg Rechtsanwälte · Promenadeplatz 9 · 80333 München", S_BOLD))
    els.append(SP(0.3))
    els.append(P("An das<br/>Landgericht München I", S_NORMAL))
    els.append(SP(0.3))
    els.append(P("München, den <b>17. November 2023</b>", S_NORMAL))
    els.append(HR())
    els.append(P("<b>R E P L I K</b>", S_TITLE))
    els.append(P("in der Sache Haspelbeck-Türkenfeld ./. Bechtholdsmeier-Schongau e.K., Az. 12 O 8842/23", S_CENTER))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("<b>I. Zur behaupteten Bestimmtheit der Signatur-Erklärung</b>", S_H2))
    els.append(P("Die Beklagte beruft sich zu Unrecht auf BGH I ZR 113/21. In jenem Fall enthielt "
                 "das Maklerangebot ausdrücklich den Namen des Maklerkunden, die Objektbezeichnung und "
                 "den Provisionssatz als feste Größe. Der vorliegende Fall ist anders gelagert: "
                 "Der Signatur-Hinweis der Beklagten verwendet das Wort „maximal&quot; und benennt weder "
                 "das konkrete Objekt (Mauerkircherstraße 47) noch den Erwerber "
                 "(Höglmayr-Stockenfels). Eine maximale Provision ist keine bestimmte Provision. "
                 "Die Rechtsprechung des BGH (vgl. I ZR 197/22, Rn. 23 ff.) verlangt Bestimmtheit, "
                 "keine bloße Bestimmbarkeit durch Auslegung.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>II. Zum Schutzzweck des § 656a BGB</b>", S_H2))
    els.append(P("§ 656a BGB wurde eingeführt, um Verbraucher vor überraschenden Provisionsforderungen "
                 "zu schützen. Dieser Schutzzweck würde vollständig unterlaufen, wenn jeder "
                 "automatisch generierten Mail-Signatur mit Provisionshinweis Vertragsqualität "
                 "zukäme. Der BGH hat in I ZR 42/23 (NJW 2024, 223) explizit festgestellt, dass "
                 "ein „Hinweis&quot; in der Signatur — ohne ausdrücklichen Vertragsschlusswillen — "
                 "die Anforderungen des § 656a BGB nicht erfüllt. Dies gilt erst recht, wenn der "
                 "Hinweis mit einem Höchstsatz formuliert ist.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>III. Zur notariellen Maklerklausel (§ 13 Kaufvertrag)</b>", S_H2))
    els.append(P("Die Beklagte verkennt die Funktion der notariellen Maklerklausel. Diese dient "
                 "allein der Absicherung des Maklers gegenüber dem Käufer (§ 328 BGB-Aspekt) "
                 "und vermag einen formunwirksamen Maklervertrag nicht zu heilen. Dies hat der "
                 "BGH in I ZR 284/20 (NJW 2022, 1896, Rn. 27–35) eindeutig entschieden. "
                 "Die notarielle Beurkundung einer Anerkenntnisklausel substituiert nicht die "
                 "nach § 656a BGB erforderliche vorherige Textform-Vereinbarung.", S_JUSTIFY))
    els.append(PB())

    els.append(az_zeile())
    els.append(P("<b>IV. Zum Wertersatzanspruch (§ 818 Abs. 2 BGB)</b>", S_H2))
    els.append(P("Der hilfsweise geltend gemachte Wertersatzanspruch der Beklagten scheitert am "
                 "Schutzzweck des § 656a BGB. Das Formerfordernis der Textform soll gerade "
                 "sicherstellen, dass der Verbraucher sich bewusst auf eine Provisionsverbindlichkeit "
                 "einlässt. Würde ein Wertersatzanspruch die Formunwirksamkeit kompensieren, "
                 "wäre § 656a BGB wirkungslos. Die herrschende Literatur und die Rechtsprechung "
                 "des BGH (I ZR 197/22, Rn. 41) verneinen einen Wertersatz bei Verstoß gegen "
                 "§ 656a BGB.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>V. Zur Entreicherung (§ 818 Abs. 3 BGB) — Bösgläubigkeit der Beklagten</b>", S_H2))
    els.append(P("§ 819 BGB verschärft die Haftung des Bereicherungsschuldners, wenn dieser die "
                 "Nichtigkeit des Rechtsgrunds kannte oder kennen musste. Als gewerbliche Maklerin "
                 "ist die Beklagte verpflichtet, die gesetzlichen Anforderungen an den Abschluss "
                 "eines Maklervertrags zu kennen. § 656a BGB gilt seit dem 23. Dezember 2020 und "
                 "war bei dem hier streitigen Vertragsschluss im April 2023 bereits mehr als zwei "
                 "Jahre in Kraft. Die Beklagte wusste oder musste wissen, dass ihr Signaturhinweis "
                 "den formellen Anforderungen möglicherweise nicht genügt.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>VI. Zum behaupteten Widerrufsrecht-Ausschluss</b>", S_H2))
    els.append(P("Die Beklagte verweist pauschal auf eine Widerrufsbelehrung beim Käufer-Maklervertrag "
                 "aus August 2022. Dieser Verweis ist unerheblich. Das Widerrufsrecht nach §§ 312g, "
                 "355 BGB ist an den jeweiligen Vertragsschluss gebunden. Eine Widerrufsbelehrung "
                 "für den Käufer-Maklervertrag erstreckt sich nicht auf einen anderen, später "
                 "geschlossenen Verkäufer-Maklervertrag. Die entsprechende handschriftliche Notiz "
                 "von RA Dr. Hagelbrand-Wittlsbach am Aktenrand (vgl. Bl. 42 dieser Akte) fasst "
                 "diesen Sachverhalt präzise zusammen.", S_JUSTIFY))
    els.append(SP(0.5))
    els.append(P("Im Übrigen verweisen die Kläger auf ihre Klageschrift.", S_JUSTIFY))
    els.append(SP(0.5))
    els.append(P("München, den 17. November 2023", S_NORMAL))
    els.append(SP(0.8))
    els.append(P("_____________________________________<br/>Dr. Knut Hagelbrand-Wittlsbach<br/>Rechtsanwalt", S_NORMAL))
    els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 7: E-MAIL-KETTE (8 Seiten)
# ─────────────────────────────────────────────────────────────────────────────
def email_block(von, an, datum, betreff, body_lines):
    "&quot;&quot;Erzeugt einen formatierten E-Mail-Block&quot;&quot;"
    els = []
    header = (f"Von:      {von}\n"
              f"An:       {an}\n"
              f"Datum:    {datum}\n"
              f"Betreff:  {betreff}")
    els.append(Preformatted(header, S_MONO_SM))
    els.append(HRFlowable(width="100%", thickness=0.3, color=C_BORDER))
    for line in body_lines:
        els.append(Preformatted(line, S_MONO_SM))
    els.append(SP(0.4))
    return els

def section_email_kette():
    els = []
    els.append(P("<b>ANLAGE K-MAK-2 — E-MAIL-KETTE HASPELBECK / BECHTHOLDSMEIER</b>", S_H1))
    els.append(P("Zeitraum: 30. März 2023 bis 12. August 2023", S_NORMAL))
    els.append(HR())
    els.append(SP(0.3))

    # E-Mail 1
    els.append(P("<b>[E-Mail 1/8] 30. März 2023, 14:47 Uhr</b>", S_BOLD))
    els += email_block(
        "korbinian.haspelbeck@t-online.de",
        "m.bechtholdsmeier@immovetop-muenchen.de",
        "30. März 2023, 14:47 Uhr",
        "RE: Unsere Immobilie Mauerkircherstraße 47 — Gegenangebot",
        [
            "Sehr geehrte Frau Bechtholdsmeier-Schongau,",
            "",
            "vielen Dank für Ihren Anruf von heute Mittag. Wie telefonisch besprochen,",
            "teilen wir Ihnen hiermit mit, dass wir bei einem Kaufpreis unter",
            "EUR 617.000,00 nicht bereit sind, zu verkaufen. Bitte geben Sie",
            "dieses Gegenangebot an die Interessenten (Familie Höglmayr) weiter.",
            "",
            "Wir bitten um Rückmeldung bis Dienstag nächster Woche.",
            "",
            "Mit freundlichen Grüßen",
            "Korbinian und Walburga Haspelbeck-Türkenfeld",
        ])

    # E-Mail 2
    els.append(P("<b>[E-Mail 2/8] 03. April 2023, 09:12 Uhr</b>", S_BOLD))
    els += email_block(
        "m.bechtholdsmeier@immovetop-muenchen.de",
        "korbinian.haspelbeck@t-online.de",
        "03. April 2023, 09:12 Uhr",
        "AW: Unsere Immobilie Mauerkircherstraße 47 — Kaufpreisverhandlung",
        [
            "Sehr geehrte Familie Haspelbeck-Türkenfeld,",
            "",
            "ich habe Ihr Gegenangebot an die Familie Höglmayr-Stockenfels übermittelt.",
            "Diese zeigen grundsätzliches Interesse an Ihrem Kaufpreis von EUR 617.000,00.",
            "Ich schlage vor, dass wir uns zu einem Gespräch zusammenfinden, um die",
            "weiteren Schritte abzustimmen. Alternativ kann ich gerne direkt einen",
            "Notartermin anfragen, wenn Sie das bevorzugen.",
            "",
            "Für Rückfragen stehe ich jederzeit zur Verfügung.",
            "",
            "Beste Grüße",
            "Marlene Bechtholdsmeier-Schongau",
            "Immobilien-Vermittlung Marlene Bechtholdsmeier-Schongau e.K.",
            "Schwere-Reiter-Straße 18, 80637 München",
            "",
            "──────────────────────────────────────────────────────────────────────",
            "HINWEIS ZUR FÄLLIGKEIT DER PROVISION:",
            "Wir weisen darauf hin, dass bei Abschluss eines Kaufvertrages bei einem",
            "Einfamilienhaus eine vom Veräußerer und Erwerber zu zahlende Provision",
            "fällig wird. Diese beläuft sich maximal auf drei Komma sieben Prozent",
            "des Kaufpreises (inklusive gesetzlicher Mehrwertsteuer und je Partei),",
            "im Verkaufsfall auf Seiten des Veräußerers anteilig gemäß § 656c BGB.",
            "──────────────────────────────────────────────────────────────────────",
        ])
    els.append(P("<b><i>Handschriftliche Notiz Korbinian Haspelbeck am Rand (blau):</i></b>", S_ITALIC))
    els.append(P(ital("„Haben wir das gelesen?! Walburga sagt nein — ich ehrlich gesagt auch nicht wirklich. "
                       "Dachten das ist Standardtext. Warum steht das da unten?&quot;"), S_HANDW))
    els.append(PB())

    # E-Mail 3
    els.append(az_zeile())
    els.append(P("<b>[E-Mail 3/8] 13. April 2023, 16:33 Uhr</b>", S_BOLD))
    els += email_block(
        "walburga.haspelbeck@t-online.de",
        "m.bechtholdsmeier@immovetop-muenchen.de",
        "13. April 2023, 16:33 Uhr",
        "RE: AW: Unsere Immobilie Mauerkircherstraße 47",
        [
            "Hallo Frau Bechtholdsmeier-Schongau,",
            "",
            "wie besprochen: wir stimmen zu, dass Sie den Notartermin anfragen.",
            "Bitte setzen Sie uns in CC.",
            "",
            "Mit freundlichen Grüßen",
            "W. und K. Haspelbeck-Türkenfeld",
        ])

    # E-Mail 4
    els.append(P("<b>[E-Mail 4/8] 14. April 2023, 10:05 Uhr</b>", S_BOLD))
    els += email_block(
        "m.bechtholdsmeier@immovetop-muenchen.de",
        "kanzlei@notar-vorstetter-muenchen.de; CC: korbinian.haspelbeck@t-online.de",
        "14. April 2023, 10:05 Uhr",
        "Terminanfrage Notariat — Kaufvertrag Mauerkircherstraße 47 München",
        [
            "Sehr geehrter Herr Dr. Vorstetter,",
            "",
            "ich bitte um Terminvereinbarung für die Beurkundung des Kaufvertrags",
            "Mauerkircherstraße 47, 81679 München-Bogenhausen.",
            "",
            "Parteien: Veräußerer: Eheleute Haspelbeck-Türkenfeld (CC gesetzt)",
            "         Erwerber:   Eheleute Bartholomäus und Hiltrud Höglmayr-Stockenfels",
            "Kaufpreis: EUR 617.000,00",
            "",
            "Wir stehen für einen Termin ab 08. Mai 2023 zur Verfügung.",
            "",
            "Mit freundlichen kollegialen Grüßen",
            "Marlene Bechtholdsmeier-Schongau",
        ])

    # E-Mail 5 — Notartermin-Protokoll-Auszug
    els.append(P("<b>[Dokument 5/8] 12. Mai 2023 — Notartermin (Protokollauszug UR-Nr. 1488/2023)</b>", S_BOLD))
    els.append(Preformatted(
        "    Notariat Dr. Ulfried Vorstetter · Maximilianstraße 22 · 80539 München\n"
        "    Beurkundungsnummer: UR-Nr. 1488/2023\n"
        "    Datum der Beurkundung: 12. Mai 2023\n\n"
        "    Erschienen:\n"
        "    1) Korbinian Haspelbeck-Türkenfeld, geb. 14.07.1968, Mauerkircherstr. 47, München\n"
        "    2) Walburga Haspelbeck-Türkenfeld geb. Zöttl, geb. 02.03.1971, gleiche Anschrift\n"
        "    3) Bartholomäus Höglmayr-Stockenfels, geb. 22.11.1975, Ismaninger Str. 88, München\n"
        "    4) Hiltrud Höglmayr-Stockenfels geb. Raufbold, geb. 19.04.1978, gleiche Anschrift\n\n"
        "    Der Notar stellte die Identität der Erschienenen anhand der vorgelegten\n"
        "    Personalausweise fest und belehrte die Parteien über den Inhalt der\n"
        "    Urkunde einschließlich § 13 (Maklerklausel).\n\n"
        "    [Protokollauszug — vollständige Urkunde nicht beigefügt, vgl. Anlage K-MAK-3]",
        S_MONO_SM))
    els.append(PB())

    # E-Mail 6 — Rechnung
    els.append(az_zeile())
    els.append(P("<b>[Dokument 6/8] 15. Mai 2023 — Rechnung Bechtholdsmeier</b>", S_BOLD))
    els.append(Preformatted(
        "    Immobilien-Vermittlung Marlene Bechtholdsmeier-Schongau e.K.\n"
        "    Schwere-Reiter-Straße 18, 80637 München\n"
        "    USt-ID: DE 298 441 592\n\n"
        "    RECHNUNG Nr. 2023-0088\n"
        "    Datum: 15. Mai 2023\n\n"
        "    An: Korbinian und Walburga Haspelbeck-Türkenfeld\n"
        "        Mauerkircherstraße 47, 81679 München\n\n"
        "    Leistungsbeschreibung:\n"
        "    Maklercourtage für Nachweis/Vermittlung Kaufvertrag\n"
        "    Objekt: Einfamilienhaus Mauerkircherstraße 47, 81679 München-Bogenhausen\n"
        "    Beurkundungsdatum: 12.05.2023, UR-Nr. 1488/2023\n"
        "    Veräußererprovision: 1,19 % netto des Kaufpreises EUR 617.000,00\n\n"
        "    Nettobetrag:     EUR  7.342,30\n"
        "    USt. 19 %:       EUR  1.395,04  [Hinweis: Differenz zu tats. Gesamtbetrag s.u.]\n"
        "    Rechnungsbetrag: EUR  8.737,34  [Achtung: gezahlt EUR 8.810,76 lt. Kontoauszug]\n\n"
        "    Zahlungsziel: 14 Tage\n"
        "    Bankverbindung: IBAN DE49 7002 0270 0032 1788 00 (HypoVereinsbank München)",
        S_MONO_SM))
    els.append(SP(0.3))
    els.append(P("<i>Anm. Kanzlei H/T: Differenz EUR 8.810,76 zu EUR 8.737,34 = EUR 73,42 unklar — "
                 "mglw. Auslagen oder Rundungsfehler. Beklagte hat EUR 8.810,76 erhalten und damit "
                 "abgerechnet (vgl. Quittung K-MAK-6).</i>", S_HANDW))

    # E-Mail 7 — Widerruf
    els.append(P("<b>[Dokument 7/8] 03. August 2023 — Anwaltlicher Widerruf</b>", S_BOLD))
    els += email_block(
        "kanzlei@hagelbrand-trotzenburg.de",
        "m.bechtholdsmeier@immovetop-muenchen.de",
        "03. August 2023, 14:22 Uhr",
        "WIDERRUF Maklervertrag — Haspelbeck-Türkenfeld — Az. HT-2023-0892",
        [
            "Sehr geehrte Frau Bechtholdsmeier-Schongau,",
            "",
            "in der vorbezeichneten Angelegenheit erklären wir namens und im",
            "Auftrag unserer Mandantschaft hiermit vorsorglich den WIDERRUF",
            "des zwischen den Parteien angeblich geschlossenen Verkäufer-Makler-",
            "vertrags nach §§ 312g, 355 BGB.",
            "",
            "Darüber hinaus fordern wir Sie auf, den gezahlten Betrag in Höhe von",
            "EUR 8.810,76 bis zum 11. August 2023 auf das Konto unserer Mandantschaft",
            "zurückzuzahlen (IBAN: DE11 7005 0000 0049 1266 73, Stadtsparkasse München).",
            "",
            "Dr. Knut Hagelbrand-Wittlsbach, Rechtsanwalt",
        ])

    # E-Mail 8 — Zurückweisung
    els.append(P("<b>[Dokument 8/8] 12. August 2023 — Zurückweisung RAin Korkenzieher</b>", S_BOLD))
    els += email_block(
        "kanzlei@korkenzieher-maibach.de",
        "kanzlei@hagelbrand-trotzenburg.de",
        "12. August 2023, 10:44 Uhr",
        "RE: WIDERRUF — Haspelbeck ./. Bechtholdsmeier-Schongau",
        [
            "Sehr geehrter Herr Kollege Dr. Hagelbrand-Wittlsbach,",
            "",
            "namens und im Auftrag unserer Mandantin weisen wir den erklärten",
            "Widerruf sowie die Rückzahlungsforderung zurück. Ein Widerrufsrecht",
            "bestand nicht. Unsere Mandantin hat sämtliche vertraglich vereinbarten",
            "Leistungen erbracht. Eine Rückzahlung erfolgt nicht.",
            "",
            "Dr. Adelheid Korkenzieher-Mariastein, Rechtsanwältin",
        ])
    els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 8: NOTARIELLER KAUFVERTRAG-AUSZUG
# ─────────────────────────────────────────────────────────────────────────────
def section_notar_kaufvertrag():
    els = []
    els.append(P("<b>ANLAGE K-MAK-3 — AUSZUG NOTARIELLER KAUFVERTRAG</b>", S_H1))
    els.append(P("UR-Nr. 1488/2023 — Notar Dr. Ulfried Vorstetter, München", S_NORMAL))
    els.append(HR())
    els.append(SP(0.3))
    els.append(NotarStempel(w=280, h=60))
    els.append(SP(0.5))
    els.append(P("<b>Kaufvertrag</b>", S_H1))
    els.append(P("(Auszug — §§ 1–4 und § 13; vollständige Urkunde im Notararchiv)", S_SMALL))
    els.append(HR())
    els.append(SP(0.2))
    els.append(P("<b>§ 1 Vertragsparteien</b>", S_H2))
    els.append(P("(1) Veräußerer: Korbinian Haspelbeck-Türkenfeld, geboren am 14. Juli 1968, "
                 "und Walburga Haspelbeck-Türkenfeld geborene Zöttl, geboren am 02. März 1971, "
                 "beide wohnhaft Mauerkircherstraße 47, 81679 München (im Folgenden: „Veräußerer&quot;).", S_JUSTIFY))
    els.append(P("(2) Erwerber: Bartholomäus Höglmayr-Stockenfels, geboren am 22. November 1975, "
                 "und Hiltrud Höglmayr-Stockenfels geborene Raufbold, geboren am 19. April 1978, "
                 "beide wohnhaft Ismaninger Straße 88, 81675 München (im Folgenden: „Erwerber&quot;).", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>§ 2 Kaufgegenstand</b>", S_H2))
    els.append(P("Die Veräußerer verkaufen hiermit an die Erwerber das Grundstück, Flurstück 488/3, "
                 "Flur 12 der Gemarkung München-Bogenhausen, Mauerkircherstraße 47, 81679 München, "
                 "eingetragen im Grundbuch des Amtsgerichts München, Grundbuchamt, Gemarkung "
                 "Bogenhausen, Blatt 7 241, mit dem darauf errichteten Einfamilienhaus, "
                 "Baujahr 1968, Wohnfläche ca. 162 m², nebst Doppelgarage und Gartenanlage, "
                 "so wie der Kaufgegenstand den Erwerbern bekannt ist.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>§ 3 Kaufpreis</b>", S_H2))
    els.append(P("(1) Der Kaufpreis beträgt EUR 617.000,00 (in Worten: sechzehnhundertsiebzehntausend "
                 "Euro), zahlbar innerhalb von 30 Tagen nach Vorliegen der Fälligkeitsvoraus-"
                 "setzungen, insbesondere der Eintragung einer Auflassungsvormerkung und der "
                 "Unbedenklichkeitsbescheinigung des Finanzamts.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>§ 4 Besitzübergang</b>", S_H2))
    els.append(P("Der Besitz- und Gefahrübergang erfolgt mit vollständiger Kaufpreiszahlung, "
                 "frühestens jedoch am 01. August 2023.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(HR())
    els.append(P("<b>§ 13 Maklercourtage</b>", S_H2))
    box_text = [
        "    § 13 Abs. 1 — Verkäuferseite:",
        "    Die Veräußerer erklären, mit der Maklerin, der Firma",
        "    Immobilien-Vermittlung Marlene Bechtholdsmeier-Schongau e.K.,",
        "    Schwere-Reiter-Straße 18, 80637 München (HRA 98 871 München),",
        "    einen Maklervertrag über die Vermittlung des vorliegenden Kaufvertrages",
        "    geschlossen zu haben. Sie verpflichten sich, dieser für den Nachweis",
        "    der Gelegenheit zum Abschluss des vorliegenden Kaufvertrages eine",
        "    Provision in Höhe von 1,19 Prozent (inklusive gesetzlicher",
        "    Mehrwertsteuer) des vorstehend vereinbarten Kaufpreises zu zahlen,",
        "    mithin EUR 7.342,30 (in Worten: siebentausenddreihundertzweiundvierzig",
        "    Euro und dreißig Cent).",
        "",
        "    § 13 Abs. 2 — Erwerberseite:",
        "    Die Erwerber erklären, ebenfalls mit der vorstehend genannten Maklerin",
        "    einen Maklervertrag in Textform (E-Mail vom 20. Februar 2023) geschlossen",
        "    zu haben und eine entsprechende Provision gemäß § 656d BGB zu schulden.",
        "",
        "    § 13 Abs. 3:",
        "    Der Notar hat die Parteien darauf hingewiesen, dass die Wirksamkeit",
        "    dieser Klausel von dem wirksamen Abschluss des jeweiligen Maklervertrages",
        "    abhängt und durch diese Klausel kein neuer Maklervertrag begründet wird.",
    ]
    for line in box_text:
        els.append(Preformatted(line, S_MONO_SM))
    els.append(SP(0.3))
    els.append(P("<b><i>Handschriftliche Notiz Korbinian Haspelbeck (blau, Aktenrand):</i></b>", S_ITALIC))
    els.append(P(ital("„Walburga hatte ich nicht GENAU GEFRAGT?! Bechtholdsmeier hatte gesagt es "
                       "sei alles in Ordnung. Der Notar hat was von ‚hängt vom Maklervertrag ab' "
                       "gesagt aber ich hab das nicht verstanden wegen der Aufregung.&quot;"), S_HANDW))
    els.append(SP(0.5))
    els.append(P("Die vorstehende Urkunde wurde den Erschienenen vorgelesen, von ihnen genehmigt und "
                 "eigenhändig unterschrieben.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("[Unterschriften aller vier Erschienenen und Notar-Siegel]", S_ITALIC))
    els.append(NotarStempel(w=280, h=60))
    els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 9: ZAHLUNGSQUITTUNG
# ─────────────────────────────────────────────────────────────────────────────
def section_quittung():
    els = []
    els.append(P("<b>ANLAGE K-MAK-6 — ZAHLUNGSQUITTUNG</b>", S_H1))
    els.append(HR())
    els.append(SP(0.5))
    els.append(P("<b>Q U I T T U N G</b>", S_TITLE))
    els.append(SP(0.3))
    data = [
        ["Ausstellerin:", "Marlene Bechtholdsmeier-Schongau, Inh. Immobilien-Vermittlung"],
        ["",             "Marlene Bechtholdsmeier-Schongau e.K., Schwere-Reiter-Str. 18, 80637 München"],
        ["Datum:",       "10. Juni 2023"],
        ["Zahlerin:",    "Korbinian und Walburga Haspelbeck-Türkenfeld, Mauerkircherstraße 47, 81679 München"],
        ["Betrag:",      "EUR 8.810,76 (in Worten: achttausend achthundertzehn Euro und sechsundsiebzig Cent)"],
        ["Verwendung:",  "Maklerprovision Verkauf EFH Mauerkircherstraße 47 — Rechnung Nr. 2023-0088"],
        ["Zahlungsart:", "Banküberweisung, eingegangen am 03. Juni 2023"],
        ["IBAN Zahlerin:","DE11 7005 0000 0049 1266 73"],
    ]
    t = Table(data, colWidths=[110, 340])
    t.setStyle(TableStyle([
        ("FONTNAME",  (0,0), (0,-1), "Helvetica-Bold"),
        ("FONTNAME",  (1,0), (1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 10),
        ("BACKGROUND",(0,0), (-1,-1), C_LIGHT_BG),
        ("BOX",       (0,0), (-1,-1), 1.0, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.3, C_BORDER),
        ("TOPPADDING",(0,0),(-1,-1),5),
        ("BOTTOMPADDING",(0,0),(-1,-1),5),
    ]))
    els.append(t)
    els.append(SP(1))
    els.append(P("Hiermit wird bestätigt, dass der vorstehende Betrag vollständig und ordnungsgemäß "
                 "eingegangen ist. Die Zahlerin wurde damit von der Provisionsverbindlichkeit "
                 "gemäß Rechnung Nr. 2023-0088 vom 15. Mai 2023 befreit.", S_JUSTIFY))
    els.append(SP(1))
    els.append(P("München, den 10. Juni 2023", S_NORMAL))
    els.append(SP(1.5))
    els.append(P("_____________________________________<br/>Marlene Bechtholdsmeier-Schongau<br/>"
                 "Immobilien-Vermittlung Marlene Bechtholdsmeier-Schongau e.K.", S_NORMAL))
    els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 10: HINWEIS WIDERRUFSBELEHRUNG / MAIL-SIGNATUR
# ─────────────────────────────────────────────────────────────────────────────
def section_widerruf():
    els = []
    els.append(P("<b>ANLAGE K-MAK-10 — VOLLTEXT MAIL-SIGNATUR MIT PROVISIONSHINWEIS</b>", S_H1))
    els.append(P("(Rekonstruiert aus E-Mail v. 03. April 2023, Anlage K-MAK-2)", S_NORMAL))
    els.append(HR())
    els.append(SP(0.3))
    signatur = [
        "Mit freundlichen Grüßen / Best regards",
        "",
        "Marlene Bechtholdsmeier-Schongau",
        "Inhaberin · Immobilien-Vermittlung Marlene Bechtholdsmeier-Schongau e.K.",
        "Schwere-Reiter-Straße 18 · 80637 München",
        "Tel: +49 (0)89 33 44 77-0 · Mobil: +49 (0)172 3388 441",
        "E-Mail: m.bechtholdsmeier@immovetop-muenchen.de",
        "Web: www.immovetop-muenchen.de",
        "HRA 98 871, Amtsgericht München · USt-ID: DE 298 441 592",
        "",
        "──────────────────────────────────────────────────────────────────────────",
        "HINWEIS ZUR FÄLLIGKEIT DER PROVISION:",
        "Wir weisen darauf hin, dass bei Abschluss eines Kaufvertrages bei einem",
        "Einfamilienhaus eine vom Veräußerer und Erwerber zu zahlende Provision",
        "fällig wird. Diese beläuft sich maximal auf drei Komma sieben Prozent",
        "des Kaufpreises (inklusive gesetzlicher Mehrwertsteuer und je Partei),",
        "im Verkaufsfall auf Seiten des Veräußerers anteilig gemäß § 656c BGB.",
        "──────────────────────────────────────────────────────────────────────────",
        "HINWEIS ZUM WIDERRUFSRECHT:",
        "Als Verbraucher haben Sie das Recht, binnen 14 Tagen ohne Angabe von",
        "Gründen diesen Vertrag zu widerrufen. Die Widerrufsfrist beträgt 14 Tage",
        "ab dem Tag des Vertragsabschlusses. Um Ihr Widerrufsrecht auszuüben,",
        "müssen Sie uns mittels einer eindeutigen Erklärung (z.B. Brief, Telefax",
        "oder E-Mail) über Ihren Entschluss, diesen Vertrag zu widerrufen,",
        "informieren. Muster-Widerrufsformular: auf Anfrage oder unter",
        "www.immovetop-muenchen.de/widerruf.pdf erhältlich.",
        "──────────────────────────────────────────────────────────────────────────",
        "Diese E-Mail und ihre Anhänge sind vertraulich. [...]",
    ]
    for line in signatur:
        els.append(Preformatted(line, S_MONO_SM))
    els.append(SP(0.5))
    els.append(P("<b>Handschriftliche Notiz RA Dr. Hagelbrand-Wittlsbach am Aktenrand:</b>", S_BOLD))
    els.append(P(ital("→ Widerrufsbelehrung in Signatur: beim Käufer-MV (Aug. 2022) explizit mitgesandt — "
                       "beim Verkäufer-MV?! Hier nur in Signatur, kein separates Dokument. "
                       "Ausreichend? BGH I ZR 197/22 Rn. 31: separates Dokument nicht erforderlich, "
                       "aber Erkennbarkeit als Belehrung muss gegeben sein. Hier: kaum erkennbar wegen "
                       "Signatur-Position. → Widerrufsfrist hat nie begonnen (§ 356 Abs. 3 S. 1 BGB)?!"), S_HANDW))
    els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 11: VERGLEICHSVERHANDLUNG
# ─────────────────────────────────────────────────────────────────────────────
def section_vergleich():
    els = []
    els.append(P("<b>PROTOKOLL VERGLEICHSVERHANDLUNG</b>", S_H1))
    els.append(P("Landgericht München I, Zivilkammer 12, Az. 12 O 8842/23", S_NORMAL))
    els.append(P("Termin: 12. Juni 2024, 10:00–12:30 Uhr, Sitzungssaal 112", S_NORMAL))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("<b>Erschienen:</b>", S_BOLD))
    for e in [
        "Kläger: Korbinian Haspelbeck-Türkenfeld und Walburga Haspelbeck-Türkenfeld, persönlich",
        "Kläger-RA: Dr. Knut Hagelbrand-Wittlsbach, Rechtsanwalt",
        "Beklagte: Marlene Bechtholdsmeier-Schongau, persönlich",
        "Beklagten-RAin: Dr. Adelheid Korkenzieher-Mariastein, Rechtsanwältin",
        "Vorsitzender Richter: Dr. Benedikt Greifswald-Haunsberg, LGDir.",
    ]:
        els.append(P(f"• {e}", S_NORMAL))
    els.append(SP(0.3))
    els.append(P("<b>Verlauf:</b>", S_BOLD))
    els.append(P("Der Vorsitzende erläuterte die Sach- und Rechtslage und wies beide Parteien "
                 "auf die nach Auffassung der Kammer erheblichen Zweifel an der Wirksamkeit des "
                 "Verkäufer-Maklervertrags hin. Die Kammer neige dazu, dem Schutzzweck-Argument "
                 "der Kläger zu folgen.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("Die Beklagte unterbreitete folgenden Vergleichsvorschlag:", S_BOLD))
    els.append(P("Zahlung von EUR 4.405,38 (50 Prozent der Klageforderung) an die Kläger "
                 "innerhalb von 14 Tagen nach Vergleichsschluss; gegenseitiger Kostenausgleich "
                 "(jede Partei trägt ihre eigenen Kosten); Vergleichsschluss beendet den "
                 "Rechtsstreit vollständig.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>Stellungnahme der Kläger:</b>", S_BOLD))
    els.append(P("RA Hagelbrand-Wittlsbach erklärte nach Rücksprache mit seinen Mandanten, "
                 "dass die Kläger den Vergleichsvorschlag ablehnen. Nach der Interessenlage "
                 "der Kläger sei eine vollständige Rückzahlung der EUR 8.810,76 zumutbar und "
                 "rechtlich geboten. Man sei bereit, das Urteil abzuwarten.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>Ergebnis: Kein Vergleich. Rechtsstreit wird fortgesetzt.</b>", S_BOLD))
    els.append(SP(0.3))
    els.append(P("München, den 12. Juni 2024", S_NORMAL))
    els.append(SP(0.6))
    els.append(P("_____________________________<br/>Dr. Greifswald-Haunsberg<br/>Vorsitzender Richter, LGDir.", S_NORMAL))
    els.append(PB())
    return els



def section_korrespondenz_zusatz():
    """Zusätzliche Korrespondenz und Schriftsätze"""
    els = []
    
    # Schriftsatz 1: Beklagte ergänzend nach Verhandlung
    els.append(P("Korkenzieher Maibach Partner mbB · Karlsplatz 4 · 80335 München", S_BOLD))
    els.append(P("München, den <b>20. Januar 2024</b>", S_NORMAL))
    els.append(HR())
    els.append(P("<b>SCHRIFTSATZ</b> (ergänzend nach Verfügung v. 08.02.2024)", S_TITLE))
    els.append(P("LG München I 12 O 8842/23", S_CENTER))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("Namens der Beklagten tragen wir ergänzend vor:", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>Zur Bestimmtheit des Provisionshinweises — vertiefende Darstellung</b>", S_H2))
    els.append(P("Die Kammer hat in der Verhandlung vom 08. Februar 2024 darauf hingewiesen, "
                 "dass der Provisionshinweis in der Mail-Signatur möglicherweise nicht ausreichend "
                 "bestimmt sei. Wir möchten hierzu folgende ergänzende Ausführungen machen:", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("<b>1. Sachverhaltsergänzung — Telefonische Vorvereinbarung:</b>", S_H2))
    els.append(P("Unsere Mandantin trägt vor, dass vor dem E-Mail-Austausch im März/April 2023 "
                 "mehrere Telefongespräche stattfanden, in denen die Parteien die Provision "
                 "explizit besprochen haben. In diesen Telefonaten soll Frau Bechtholdsmeier-"
                 "Schongau ausdrücklich erklärt haben, dass eine Provision von 1,19 % netto "
                 "des Kaufpreises für die Verkäuferseite anfallen werde, sofern der Verkauf "
                 "über ihre Vermittlung zustande komme. Die Kläger hätten dies akzeptiert.", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("Die Beklagte beantragt die Vernehmung von Frau Marlene Bechtholdsmeier-Schongau "
                 "als Zeugin zu diesen Telefonaten sowie — vorsorglich — die Einholung eines "
                 "Sachverständigengutachtens zur branchenüblichen Bedeutung von Provisionshinweisen "
                 "in E-Mail-Signaturen.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>2. Zur Auslegung der Kläger-E-Mail vom 13. April 2023:</b>", S_H2))
    els.append(P("Die Formulierung &quot;wie besprochen&quot; in der Kläger-E-Mail vom 13. April 2023 "
                 "ist nach dem objektiven Empfängerhorizont (§§ 133, 157 BGB) als Bestätigung "
                 "der telefonisch getroffenen Provisionsvereinbarung zu verstehen. Im kaufmännischen "
                 "und halbkaufmännischen Verkehr ist es üblich, mündlich oder telefonisch "
                 "getroffene Absprachen durch die Formulierung &quot;wie besprochen&quot; per E-Mail "
                 "zu bestätigen. Eine solche Bestätigung stellt eine rechtserhebliche "
                 "Erklärung dar, auch wenn sie nicht ausdrücklich als &quot;Vertragsannahme&quot; "
                 "bezeichnet wird.", S_JUSTIFY))
    els.append(SP(0.5))
    els.append(P("München, den 20. Januar 2024", S_NORMAL))
    els.append(SP(0.6))
    els.append(P("_____________________________________<br/>Dr. Adelheid Korkenzieher-Mariastein", S_NORMAL))
    els.append(PB())
    
    # Schriftsatz 2: Kläger kurze Stellungnahme
    els.append(P("Hagelbrand &amp; Trotzenburg Rechtsanwälte · Promenadeplatz 9 · 80333 München", S_BOLD))
    els.append(P("München, den <b>28. Januar 2024</b>", S_NORMAL))
    els.append(HR())
    els.append(P("<b>STELLUNGNAHME</b> zum Schriftsatz der Beklagten v. 20.01.2024", S_TITLE))
    els.append(P("LG München I 12 O 8842/23", S_CENTER))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("Die Kläger erwidern auf den Schriftsatz der Beklagten vom 20. Januar 2024 kurz "
                 "wie folgt:", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("<b>1. Zu den behaupteten Telefonaten:</b>", S_H2))
    els.append(P("Die Kläger bestreiten ausdrücklich, dass in den Telefonaten eine ausdrückliche "
                 "Einigung über die Provision von &quot;1,19 % netto&quot; erzielt worden sei. "
                 "Herr Haspelbeck-Türkenfeld erklärt hierzu: &quot;Es wurde über den Immobilienverkauf "
                 "gesprochen, aber nie in einer Weise, die ich als verbindliche Vereinbarung "
                 "über eine Provision verstanden hätte.&quot; Im Übrigen: Selbst wenn telefonisch "
                 "eine Einigung erzielt worden wäre, so wäre diese mangels Textform "
                 "nach § 656a BGB unwirksam.", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("<b>2. Zur Auslegung der E-Mail vom 13. April 2023:</b>", S_H2))
    els.append(P("&quot;Wie besprochen&quot; bezieht sich auf die Vereinbarung eines Notartermins — "
                 "nicht auf eine Provisionsvereinbarung. Soweit die Beklagte behauptet, die "
                 "Formulierung beziehe sich auf eine frühere telefonische Provisionsabrede, "
                 "ist dies unzutreffend. Es gibt keine Protokollierung dieses Telefonats, "
                 "keine schriftliche Zusammenfassung und keine sonstige Bestätigung.", S_JUSTIFY))
    els.append(SP(0.5))
    els.append(P("München, den 28. Januar 2024", S_NORMAL))
    els.append(SP(0.6))
    els.append(P("_____________________________________<br/>Dr. Knut Hagelbrand-Wittlsbach", S_NORMAL))
    els.append(PB())
    
    # Schriftsatz 3: abschließende Stellungnahme Beklagte nach schriftlichem Verfahren
    els.append(P("Korkenzieher Maibach Partner mbB · Karlsplatz 4 · 80335 München", S_BOLD))
    els.append(P("München, den <b>01. April 2024</b>", S_NORMAL))
    els.append(HR())
    els.append(P("<b>ABSCHLIESSENDER SCHRIFTSATZ (§ 128 Abs. 2 ZPO)</b>", S_TITLE))
    els.append(P("LG München I 12 O 8842/23", S_CENTER))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("Namens der Beklagten nehmen wir zum Verfahrensstand abschließend Stellung "
                 "und fassen die wesentlichen Argumente zusammen:", S_JUSTIFY))
    els.append(SP(0.2))
    for nr, txt in [
        ("A.", "Der E-Mail-Austausch genügt den Anforderungen des § 656a BGB: Er ist schriftlich "
         "fixiert, identifiziert die Parteien, enthält einen Provisionshinweis und bezieht sich "
         "kontextuell auf das Objekt Mauerkircherstraße 47."),
        ("B.", "Hilfsweise: Die notarielle Maklerklausel in § 13 des Kaufvertrages begründet "
         "eine eigenständige Rechtsgrundlage für die Provisionspflicht."),
        ("C.", "Hilfsweise: Die Beklagte hat werthaltige Maklertätigkeit erbracht, "
         "für die ein Wertersatzanspruch besteht."),
        ("D.", "Äußerst hilfsweise: Die Kläger handeln treuwidrig (§ 242 BGB), wenn sie "
         "nach Inanspruchnahme der Maklertätigkeit und notariellem Anerkenntnis die "
         "Provision zurückfordern."),
    ]:
        els.append(P(f"<b>{nr}</b> {txt}", S_JUSTIFY))
        els.append(SP(0.1))
    els.append(SP(0.5))
    els.append(P("München, den 01. April 2024", S_NORMAL))
    els.append(SP(0.6))
    els.append(P("_____________________________________<br/>Dr. Adelheid Korkenzieher-Mariastein", S_NORMAL))
    els.append(PB())
    
    # Schriftsatz 4: Abschlusserklärung Kläger
    els.append(P("Hagelbrand &amp; Trotzenburg Rechtsanwälte · Promenadeplatz 9 · 80333 München", S_BOLD))
    els.append(P("München, den <b>15. April 2024</b>", S_NORMAL))
    els.append(HR())
    els.append(P("<b>ABSCHLIESSENDE STELLUNGNAHME KLÄGER</b>", S_TITLE))
    els.append(P("LG München I 12 O 8842/23", S_CENTER))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("Die Kläger haben alles Erforderliche vorgetragen. Die Rechtslage ist durch "
                 "BGH I ZR 197/22 und I ZR 42/23 eindeutig: Ein Signaturhinweis mit Höchstprovisionssatz "
                 "ohne Objektnennung und ohne erkennbaren Vertragsbindungswillen genügt den "
                 "Anforderungen des § 656a BGB nicht. Die Kläger beantragen das angekündigte Urteil.", S_JUSTIFY))
    els.append(SP(0.5))
    els.append(P("München, den 15. April 2024", S_NORMAL))
    els.append(SP(0.6))
    els.append(P("_____________________________________<br/>Dr. Knut Hagelbrand-Wittlsbach", S_NORMAL))
    els.append(PB())
    return els


# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 12: BERUFUNGSSCHRIFTSATZ
# ─────────────────────────────────────────────────────────────────────────────
def section_berufung_schriftsatz():
    els = []
    els.append(P("Korkenzieher Maibach Partner mbB · Karlsplatz 4 · 80335 München", S_BOLD))
    els.append(SP(0.3))
    els.append(P("An das<br/>Oberlandesgericht München<br/>Prielmayerstraße 5<br/>80335 München", S_NORMAL))
    els.append(SP(0.3))
    els.append(P("München, den <b>04. Juli 2024</b>", S_NORMAL))
    els.append(HR())
    els.append(P("<b>BERUFUNGSSCHRIFTSATZ</b>", S_TITLE))
    els.append(HR())
    els.append(SP(0.2))
    els.append(P("in dem Rechtsstreit", S_RUBRUM))
    els.append(P("<b>Haspelbeck-Türkenfeld ./. Bechtholdsmeier-Schongau e.K.</b>", S_RUBRUM))
    els.append(P("Vorinstanz: LG München I, Az. 12 O 8842/23 (Urteil v. 06. Juni 2024)<br/>"
                 "Berufungsaz.: OLG München 13 U 412/24", S_RUBRUM))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("Namens und im Auftrag der Beklagten legen wir hiermit gegen das Urteil des "
                 "Landgerichts München I vom 06. Juni 2024 — Az. 12 O 8842/23 — fristgemäß", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("<b>BERUFUNG</b>", S_TITLE))
    els.append(SP(0.2))
    els.append(P("ein. Das Urteil wurde der Beklagten am 18. Juni 2024 zugestellt. Die "
                 "Berufungsfrist läuft somit bis zum 18. Juli 2024 (§ 517 ZPO). Die vorliegende "
                 "Berufungsschrift geht fristgemäß ein.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>BERUFUNGSANTRAG</b>", S_H1))
    els.append(HR())
    els.append(P("Die Beklagte beantragt:", S_JUSTIFY))
    els.append(P("Das Urteil des Landgerichts München I vom 06. Juni 2024, Az. 12 O 8842/23, "
                 "wird abgeändert. Die Klage wird abgewiesen. Die Kosten des Rechtsstreits "
                 "einschließlich der Kosten des Berufungsverfahrens tragen die Kläger.", S_ANTRAG))
    els.append(SP(0.5))
    els.append(P("<b>VORLÄUFIGE BEGRÜNDUNG</b>", S_H1))
    els.append(HR())
    els.append(P("Die Berufungsbegründung erfolgt gesondert innerhalb der Begründungsfrist "
                 "nach § 520 Abs. 2 ZPO. Vorläufig wird auf die erstinstanzlichen Schriftsätze "
                 "Bezug genommen. Das Landgericht hat den Schutzzweck des § 656a BGB überdehnt "
                 "und die Anforderungen an die Bestimmtheit der Textform-Erklärung überspannt.", S_JUSTIFY))
    els.append(SP(0.5))
    els.append(P("München, den 04. Juli 2024", S_NORMAL))
    els.append(SP(0.8))
    els.append(P("_____________________________________<br/>Dr. Adelheid Korkenzieher-Mariastein<br/>Rechtsanwältin", S_NORMAL))
    els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 13: BERUFUNGSBEGRÜNDUNG (12 Seiten — erweitert)
# ─────────────────────────────────────────────────────────────────────────────
def section_berufungsbegruendung():
    els = []
    els.append(P("Korkenzieher Maibach Partner mbB · Karlsplatz 4 · 80335 München", S_BOLD))
    els.append(P("München, den <b>05. August 2024</b>", S_NORMAL))
    els.append(HR())
    els.append(P("<b>BERUFUNGSBEGRÜNDUNG</b>", S_TITLE))
    els.append(P("OLG München 13 U 412/24 — Vorinstanz LG München I 12 O 8842/23", S_CENTER))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("<b>A. Einführung und Berufungsrügen</b>", S_H1))
    els.append(HR())
    els.append(P("Das Urteil des Landgerichts München I vom 06. Juni 2024 leidet an mehreren "
                 "Rechtsfehlern (§ 546 ZPO), die zur Abänderung des Urteils führen müssen:", S_JUSTIFY))
    for i, rüge in enumerate([
        "Verletzung materiellen Rechts: Das LG hat die Anforderungen an die Bestimmtheit einer Textform-Erklärung nach § 656a BGB i.V.m. § 126b BGB überspannt (Rüge 1, dazu B.I.);",
        "Verletzung materiellen Rechts: Das LG hat die Wirkung der notariellen Maklerklausel in § 13 des Kaufvertrages verkannt (Rüge 2, dazu B.II.);",
        "Verletzung materiellen Rechts: Das LG hat den Bereicherungsausschluss nach § 817 Satz 2 BGB und den Grundsatz von Treu und Glauben (§ 242 BGB) nicht ausreichend berücksichtigt (Rüge 3, dazu B.III.);",
        "Verletzung verfahrensrechtlicher Vorschriften: Das LG hat das Beweisangebot der Beklagten (Zeugin Bechtholdsmeier-Schongau zu Telefonaten) übergangen (Rüge 4, dazu B.IV.).",
    ], 1):
        els.append(P(f"<b>{i}.</b> {rüge}", S_JUSTIFY))
        els.append(SP(0.1))
    els.append(PB())

    els.append(az_zeile())
    els.append(P("<b>B. Vertiefte Ausführungen zu den Berufungsrügen</b>", S_H1))
    els.append(HR())
    els.append(P("<b>B.I. Rüge 1: Überspannte Bestimmtheitsanforderungen (§ 656a BGB)</b>", S_H2))
    els.append(P("Das Landgericht führt auf S. 12 des Urteils aus, der Signaturhinweis enthalte "
                 "„keine ausreichend objektbezogene und bestimmte Erklärung zum Abschluss eines "
                 "Maklervertrags&quot;. Diese Bewertung ist rechtsfehlerhaft.", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("Die Rechtsprechung des BGH zur Bestimmtheit von Maklerverträgen hat sich schrittweise "
                 "entwickelt. In I ZR 113/21 hat der BGH ausgeführt, dass ein E-Mail-Angebot "
                 "„hinreichend bestimmt&quot; ist, wenn aus dem Gesamtkontext der Korrespondenz "
                 "deutlich wird, auf welches Objekt sich die Provision bezieht. Der BGH hat "
                 "dort nicht gefordert, dass das Objekt ausdrücklich im Provisionshinweis "
                 "selbst benannt sein müsse.", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("Im vorliegenden Fall ist der Gesamtkontext eindeutig: Die E-Mail-Konversation "
                 "vom 30. März bis 13. April 2023 bezieht sich ausschließlich auf das Objekt "
                 "Mauerkircherstraße 47. Kein anderes Objekt war Gegenstand der Kommunikation. "
                 "Der Provisionssatz von „maximal 3,7 %&quot; ist nach der Branchenüblichkeit "
                 "(vgl. Immobilienverband IVD Bayern, Provisionsrichtlinien 2023) hinreichend "
                 "bestimmt, da im Markt eine Provision von genau 3,57 % netto (= 4,25 % brutto "
                 "je Partei) üblich ist.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>B.II. Rüge 2: Notarielle Maklerklausel</b>", S_H2))
    els.append(P("Das Landgericht folgt der Ansicht des BGH in I ZR 284/20, dass die notarielle "
                 "Maklerklausel einen formnichtigen Maklervertrag nicht heilen könne. Die Beklagte "
                 "hält diese Rechtsprechung — jedenfalls für den vorliegenden Fall — für zu eng. "
                 "§ 13 des Kaufvertrages enthält nicht nur eine Anerkenntnisklausel, sondern eine "
                 "eigenständige Schuldurkunde, in der alle wesentlichen Vertragsbestandteile "
                 "(Parteien, Objekt, Provisionshöhe, Fälligkeit) benannt sind. Diese Schuldurkunde "
                 "erfüllt — auch ohne die vorherige E-Mail — die Anforderungen des § 656a BGB.", S_JUSTIFY))
    els.append(PB())

    els.append(az_zeile())
    els.append(P("<b>B.III. Rüge 3: § 817 Satz 2 BGB / § 242 BGB</b>", S_H2))
    els.append(P("Die Kläger haben die Maklerprovision in voller Kenntnis der Maklerklausel in "
                 "§ 13 des notariellen Kaufvertrages gezahlt. Ein Notar hat sie über die "
                 "Provisionsverbindlichkeit belehrt. Die anschließende Berufung auf einen "
                 "Formfehler stellt sich als widersprüchliches Verhalten dar (venire contra "
                 "factum proprium, § 242 BGB). Wer im Notartermin die Provisionsverbindlichkeit "
                 "ausdrücklich anerkennt und anschließend die Formnichtigkeit geltend macht, "
                 "handelt rechtsmissbräuchlich.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>B.IV. Rüge 4: Übergangenes Beweisangebot</b>", S_H2))
    els.append(P("Das Landgericht hat das Angebot der Beklagten auf Vernehmung von Frau "
                 "Bechtholdsmeier-Schongau als Zeugin zu den Telefonaten vor dem E-Mail-Austausch "
                 "ohne Begründung übergangen (§ 286 ZPO). Diese Telefonate, in denen die "
                 "Provisionskonditionen besprochen wurden, hätten ergeben, dass zwischen den "
                 "Parteien telefonisch Einigkeit über die Provision erzielt worden war und der "
                 "E-Mail-Austausch lediglich zur Bestätigung des telefonisch Vereinbarten diente.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>C. Beweisangebote in der Berufungsinstanz</b>", S_H1))
    els.append(HR())
    els.append(P("Die Beklagte wiederholt sämtliche erstinstanzlichen Beweisangebote und ergänzt:", S_JUSTIFY))
    for b in [
        "Zeugnis Marlene Bechtholdsmeier-Schongau: Telefonische Einigung über Provision vor E-Mail-Austausch",
        "Zeugnis Bartholomäus Höglmayr-Stockenfels: Kenntnis von Provisionsvereinbarung bei Kaufvertragsverhandlungen",
        "Sachverständigengutachten zu branchenüblichen Provisionsangaben (hilfsweise)",
        "Vorlage vollständiger E-Mail-Header-Daten (technische Authentizität)",
    ]:
        els.append(P(f"— {b}", S_JUSTIFY))
    els.append(SP(0.5))
    els.append(P("München, den 05. August 2024", S_NORMAL))
    els.append(SP(0.8))
    els.append(P("_____________________________________<br/>Dr. Adelheid Korkenzieher-Mariastein<br/>Rechtsanwältin", S_NORMAL))
    els.append(PB())

    # Weitere Seiten Berufungsbegründung
    for i in range(4):
        els.append(az_zeile())
        els.append(P(f"<b>BERUFUNGSBEGRÜNDUNG — FORTSETZUNG (Teil {i+2})</b>", S_H1))
        els.append(HR())
        topics = [
            ("D. Literaturüberblick zur Textform des § 656a BGB",
             "Die Literatur ist gespalten. Blank/Börstinghaus (Miete, 6. Aufl. 2022 Anhang §§ 652 ff. BGB Rn. 44) "
             "verlangen für einen wirksamen Textform-Maklervertrag eine objektbezogene und partnerbezogene Erklärung. "
             "Demgegenüber vertreten Staudinger/Arnold (BGB, Neubearbeitung 2021, § 656a Rn. 15 ff.) die Auffassung, "
             "dass eine generalklauselartige E-Mail-Formulierung im Kontext einer laufenden Objektverhandlung "
             "ausreiche. MünchKomm/Roth (BGB, 9. Aufl. 2024, § 656a Rn. 8) differenziert danach, ob die E-Mail "
             "erkennbar eine rechtliche Bindung begründen soll oder lediglich informativen Charakter hat. "
             "Die Beklagte folgt der letztgenannten Auffassung: Aus Sicht eines objektiven Empfängers stellt "
             "der Signaturhinweis — im Kontext der fortgeschrittenen Kaufverhandlung — eine auf Vertragsbegründung "
             "gerichtete Erklärung dar."),
            ("E. Europarechtskonformität des § 656a BGB",
             "Rein vorsorglich weist die Beklagte darauf hin, dass § 656a BGB im Lichte der Verbraucher-"
             "rechterichtlinie 2011/83/EU auszulegen ist. Art. 7 Abs. 1 der Richtlinie verlangt, dass "
             "bei Fernabsatzverträgen bestimmte Informationen klar und verständlich mitgeteilt werden. "
             "Die Beklagte hat diesen Anforderungen durch ihren Signaturhinweis Rechnung getragen. Eine "
             "übermäßig strenge nationale Auslegung könnte gegen den Grundsatz der Verhältnismäßigkeit "
             "verstoßen, wenn sie dazu führt, dass jede branchenübliche E-Mail-Formulierung als "
             "formnichtig behandelt wird."),
            ("F. Wirtschaftliche Auswirkungen auf den Maklermarkt",
             "Die Beklagte weist — ohne hieraus einen selbstständigen Einwand zu konstruieren — auf die "
             "wirtschaftlichen Auswirkungen einer übermäßig strengen Auslegung hin: Wenn jeder nicht "
             "gesondert ausgeführte Provisionshinweis in einer E-Mail zur Formnichtigkeit des "
             "Maklervertrags führt, werden Makler gezwungen, bei jeder einzelnen E-Mail einen separaten "
             "formal korrekten Maklervertrags-Entwurf beizulegen. Dies verursacht erheblichen Mehraufwand "
             "und benachteiligt kleine Maklerbüros gegenüber großen Immobilienportalen. Eine "
             "teleologische Reduktion des § 656a BGB auf klare Fälle der Überrumpelung ist angemessen."),
            ("G. Zum BGH-Beschluss I ZR 202/25 und dessen Bedeutung",
             "Die vorliegende Sache ist — soweit ersichtlich — eine der ersten Fälle, in denen der BGH "
             "nach der Leitentscheidung I ZR 197/22 die Frage der Bestimmtheit des Signatur-Hinweises "
             "in einem Berufungsverfahren behandelt. Die Beklagte erwartet, dass der BGH die Gelegenheit "
             "nutzen wird, die bisherige Rechtsprechungslinie zu präzisieren und eine praktikable "
             "Abgrenzung zwischen wirksamen und unwirksamen Textform-Erklärungen vorzunehmen."),
        ]
        title, body = topics[i]
        els.append(P(f"<b>{title}</b>", S_H2))
        els.append(P(body, S_JUSTIFY))
        els.append(SP(0.5))
        els.append(P("Fortsetzung folgt / Schriftsatz zu den Akten des OLG München Az. 13 U 412/24", S_SMALL))
        els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 14: BERUFUNGSERWIDERUNG
# ─────────────────────────────────────────────────────────────────────────────
def section_berufungserwiderung():
    els = []
    els.append(P("Hagelbrand &amp; Trotzenburg Rechtsanwälte · Promenadeplatz 9 · 80333 München", S_BOLD))
    els.append(P("München, den <b>16. September 2024</b>", S_NORMAL))
    els.append(HR())
    els.append(P("<b>BERUFUNGSERWIDERUNG</b>", S_TITLE))
    els.append(P("OLG München 13 U 412/24 — Beklagtenseite Berufungsführerin", S_CENTER))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("<b>I. Vorbemerkung</b>", S_H2))
    els.append(P("Die Berufung der Beklagten ist unbegründet. Das Landgericht München I hat den "
                 "vorliegenden Fall zutreffend entschieden. Die Ausführungen der Berufungsbegründung "
                 "geben keine Veranlassung zur Abänderung des erstinstanzlichen Urteils.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>II. Zur Berufungsrüge 1 (Bestimmtheit)</b>", S_H2))
    els.append(P("Die Berufungsbegründung verkennt, dass BGH I ZR 113/21 für den dortigen Fall "
                 "eine explizite Objektnennung vorlag. Das OLG kann den vorliegenden Fall ohne "
                 "weiteres von dieser Entscheidung unterscheiden. Der entscheidende Unterschied: "
                 "Im Referenzfall enthielt die maßgebliche E-Mail eine klare Vertragsofferte mit "
                 "festem Provisionssatz und Objektbenennung. Hier enthält der Signaturhinweis "
                 "lediglich einen Höchstsatz ohne Objektnennung.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>III. Zur Berufungsrüge 2 (Notarielle Maklerklausel)</b>", S_H2))
    els.append(P("Die Berufungsbegründung versucht, die notarielle Maklerklausel als eigenständige "
                 "Schuldanerkenntnisklausel umzudeuten. Dies ist nach der eindeutigen Rechtsprechung "
                 "des BGH (I ZR 284/20, Rn. 27 ff.) nicht möglich. § 780 BGB (abstraktes "
                 "Schuldversprechen) setzt eine entsprechende ausdrückliche Parteivereinbarung "
                 "voraus, die hier fehlt. Die notarielle Klausel enthält ein akzessorisches "
                 "Anerkenntnis, kein konstitutives.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>IV. Zur Berufungsrüge 3 (§ 242 BGB)</b>", S_H2))
    els.append(P("Das Argument des widersprüchlichen Verhaltens (venire contra factum proprium) "
                 "greift nicht, wenn sich die Partei auf eine gesetzliche Formvorschrift beruft. "
                 "§ 656a BGB ist ein zwingendes Verbraucherschutzrecht. Die Berufung auf eine "
                 "Formvorschrift kann grundsätzlich nicht gegen § 242 BGB verstoßen, es sei denn, "
                 "die Partei hat durch Täuschung oder Arglist auf den Formverstoß hingewirkt — "
                 "was hier nicht der Fall ist.", S_JUSTIFY))
    els.append(SP(0.5))
    els.append(P("München, den 16. September 2024", S_NORMAL))
    els.append(SP(0.8))
    els.append(P("_____________________________________<br/>Dr. Knut Hagelbrand-Wittlsbach<br/>Rechtsanwalt", S_NORMAL))
    els.append(PB())

    # Extra Seiten Berufungserwiderung
    els.append(az_zeile())
    els.append(P("<b>BERUFUNGSERWIDERUNG — FORTSETZUNG</b>", S_H1))
    els.append(HR())
    els.append(P("<b>V. Zur Berufungsrüge 4 (Übergangenes Beweisangebot)</b>", S_H2))
    els.append(P("Das Landgericht hat das Beweisangebot der Beklagten (Zeugnis Bechtholdsmeier-"
                 "Schongau) nicht übergangen, sondern als nicht entscheidungserheblich bewertet. "
                 "Diese Bewertung ist zutreffend: Selbst wenn telefonisch eine Einigung über die "
                 "Provision erzielt worden sein sollte, wäre ein solches telefonisches Übereinkommen "
                 "mangels Textform nach § 656a BGB unwirksam. § 656a BGB gilt auch für telefonisch "
                 "getroffene Vereinbarungen (wie erst recht für die hieraus abgeleiteten E-Mail-"
                 "Bestätigungen). Eine rein telefonische Vereinbarung kann die gesetzliche "
                 "Textform nicht ersetzen.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>VI. Zur wirtschaftlichen Argumentation (Berufungsbegründung Abschnitt F)</b>", S_H2))
    els.append(P("Die wirtschaftlichen Argumente der Beklagten sind nicht geeignet, "
                 "eine andere Auslegung des § 656a BGB zu rechtfertigen. Das Textform-"
                 "Erfordernis dient dem Schutz der Verbraucher vor überraschenden Provisions-"
                 "forderungen. Dieser Schutzzweck muss — so der Gesetzgeber bewusst — "
                 "notfalls auf Kosten der wirtschaftlichen Bequemlichkeit der Makler "
                 "verwirklicht werden. § 656a BGB ist insoweit als lex specialis zu verstehen, "
                 "die teleologische Reduktion ist ausgeschlossen.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>VII. Ergebnis</b>", S_H2))
    els.append(P("Die Kläger beantragen, die Berufung der Beklagten zurückzuweisen und "
                 "ihr die Kosten des Berufungsverfahrens aufzuerlegen. Das erstinstanzliche "
                 "Urteil ist rechtsfehlerfrei. Eine Revisionszulassung ist nach Auffassung "
                 "der Kläger nicht erforderlich, da die Rechtslage durch BGH I ZR 197/22 "
                 "und I ZR 42/23 hinreichend geklärt ist.", S_JUSTIFY))
    els.append(SP(0.5))
    els.append(P("München, den 16. September 2024", S_NORMAL))
    els.append(SP(0.8))
    els.append(P("_____________________________________<br/>Dr. Knut Hagelbrand-Wittlsbach<br/>Rechtsanwalt", S_NORMAL))
    els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 15: BERUFUNGSURTEIL OLG MÜNCHEN
# ─────────────────────────────────────────────────────────────────────────────
def section_berufungsurteil():
    els = []
    els.append(P("OBERLANDESGERICHT MÜNCHEN", S_TITLE))
    els.append(P("13. Zivilsenat", S_CENTER))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("<b>URTEIL</b>", S_TITLE))
    els.append(SP(0.2))
    els.append(P("Az.: <b>13 U 412/24</b>", S_CENTER_B))
    els.append(P("Verkündet am: <b>17. Februar 2025</b>", S_CENTER))
    els.append(HR())
    els.append(SP(0.2))
    els.append(P("In dem Rechtsstreit", S_RUBRUM))
    els.append(P("<b>Korbinian Haspelbeck-Türkenfeld und Walburga Haspelbeck-Türkenfeld,</b><br/>"
                 "Mauerkircherstraße 47, 81679 München,<br/>— Kläger und Berufungsbeklagte —", S_RUBRUM))
    els.append(P("gegen", S_RUBRUM))
    els.append(P("<b>Immobilien-Vermittlung Marlene Bechtholdsmeier-Schongau e.K.,</b><br/>"
                 "Schwere-Reiter-Straße 18, 80637 München,<br/>— Beklagte und Berufungsführerin —", S_RUBRUM))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("<b>T E N O R</b>", S_H1))
    els.append(HR())
    els.append(P("Die Berufung der Beklagten gegen das Urteil des Landgerichts München I "
                 "vom 06. Juni 2024 (Az. 12 O 8842/23) wird zurückgewiesen.", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("Die Kosten des Berufungsverfahrens trägt die Beklagte.", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("Das Urteil ist vorläufig vollstreckbar. Die Beklagte kann die "
                 "Vollstreckung abwenden durch Sicherheitsleistung in Höhe von 110 % "
                 "des beizutreibenden Betrages, wenn nicht die Kläger vor der "
                 "Vollstreckung Sicherheit in gleicher Höhe leisten.", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("<b>Die Revision wird zugelassen.</b>", S_JUSTIFY_B))
    els.append(SP(0.3))
    els.append(HR())
    els.append(P("<b>GRÜNDE</b>", S_H1))
    els.append(HR())
    els.append(SP(0.2))
    els.append(P("<b>I. Sachverhalt und Verfahren</b>", S_H2))
    els.append(P("Der Senat nimmt auf die tatsächlichen Feststellungen im Urteil des "
                 "Landgerichts München I Bezug (§ 540 Abs. 1 Satz 1 Nr. 1 ZPO). Das "
                 "Landgericht hat die Beklagte zur Rückzahlung von EUR 8.810,76 nebst "
                 "Zinsen verurteilt. Die Berufung der Beklagten hat keinen Erfolg.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>II. Zur Textform des § 656a BGB</b>", S_H2))
    els.append(P("Der Senat teilt die Rechtsauffassung des Landgerichts. Der Signaturhinweis "
                 "der Beklagten erfüllt die Anforderungen des § 656a BGB i.V.m. § 126b BGB nicht. "
                 "Die Erklärung muss nach § 126b BGB eine klare Willenserklärung enthalten, die "
                 "auf den Abschluss eines Maklervertrags mit bestimmtem Inhalt gerichtet ist. "
                 "Ein Hinweis, der lediglich informatorischen Charakter hat und einen Höchstsatz "
                 "nennt, genügt dem nicht.", S_JUSTIFY))
    els.append(PB())

    els.append(az_zeile())
    els.append(P("<b>III. Zur notariellen Maklerklausel</b>", S_H2))
    els.append(P("Der Senat folgt der Rechtsprechung des BGH (I ZR 284/20). Die notarielle "
                 "Maklerklausel in § 13 des Kaufvertrages vermag einen formunwirksamen "
                 "Maklervertrag nicht zu heilen. Sie setzt einen wirksam geschlossenen "
                 "Maklervertrag voraus und ersetzt diesen nicht.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>IV. Zur Revisionszulassung</b>", S_H2))
    els.append(P("Die Revision war nach § 543 Abs. 2 ZPO zuzulassen. Die Frage, unter welchen "
                 "Voraussetzungen ein E-Mail-Signaturhinweis mit Provisionsangabe die Anforderungen "
                 "des § 656a BGB erfüllt, ist noch nicht abschließend höchstrichterlich geklärt. "
                 "Die Entscheidung des BGH in I ZR 197/22 lässt Raum für unterschiedliche "
                 "Auslegungen, insbesondere hinsichtlich der Frage, ob ein Kontextbezug "
                 "ausreicht oder eine explizite Objektnennung erforderlich ist. Die Rechtsfrage "
                 "hat grundsätzliche Bedeutung (§ 543 Abs. 2 Nr. 1 ZPO).", S_JUSTIFY))
    els.append(SP(0.5))
    els.append(P("München, den 17. Februar 2025", S_NORMAL))
    els.append(SP(0.8))
    els.append(P("Dr. Vogelhuber-Tegernsee   Dr. Schirmbeck-Augsburg   Seiffert-Nymphenburg", S_NORMAL))
    els.append(P("Vorsitzende Richterin       Richter am OLG             Richterin am OLG", S_SMALL))
    els.append(PB())

    # Extra Seite Berufungsurteil
    els.append(az_zeile())
    els.append(P("<b>BERUFUNGSURTEIL OLG MÜNCHEN 13 U 412/24 — FORTSETZUNG DER GRÜNDE</b>", S_H1))
    els.append(HR())
    els.append(P("<b>V. Zu den weiteren Berufungsrügen</b>", S_H2))
    els.append(P("Die Berufungsrügen der Beklagten (§ 520 Abs. 3 ZPO) haben allesamt keinen Erfolg:", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("<b>Rüge 1 (Bestimmtheit):</b> Die Bezugnahme der Berufungsbegründung auf BGH I ZR 113/21 "
                 "verfängt nicht. Der Senat sieht sich durch diese Entscheidung nicht gebunden, da der "
                 "dortige Sachverhalt wesentlich stärker ausgeprägte Vertragselemente enthielt. "
                 "Im vorliegenden Fall fehlt jede Objektnennung im Signaturhinweis.", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("<b>Rüge 2 (§ 780 BGB):</b> Ein abstraktes Schuldversprechen i.S.d. § 780 BGB "
                 "setzt ausdrückliche Abrede voraus. Eine solche liegt nicht vor.", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("<b>Rüge 3 (§ 242 BGB):</b> Die Berufung auf einen Gesetzesverstoß (Formvorschrift) "
                 "kann grundsätzlich nicht nach § 242 BGB ausgeschlossen werden, solange kein "
                 "qualifiziertes Fehlverhalten des Berechtigten vorliegt.", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("<b>Rüge 4 (Zeugnis):</b> Selbst wenn telefonisch eine Einigung erzielt worden wäre, "
                 "wäre diese mangels Textform unwirksam. Das übergangene Beweisangebot ist daher "
                 "nicht entscheidungserheblich.", S_JUSTIFY))
    els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 16: REVISIONSBEGRÜNDUNG (9 Seiten)
# ─────────────────────────────────────────────────────────────────────────────
def section_revision_begruendung():
    els = []
    els.append(P("Korkenzieher Maibach Partner mbB · Karlsplatz 4 · 80335 München", S_BOLD))
    els.append(P("München, den <b>15. Mai 2025</b>", S_NORMAL))
    els.append(HR())
    els.append(P("<b>REVISIONSBEGRÜNDUNG</b>", S_TITLE))
    els.append(P("BGH Az. I ZR 202/25 — Vorinstanz OLG München 13 U 412/24", S_CENTER))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("<b>REVISIONSANTRAG</b>", S_H1))
    els.append(HR())
    els.append(P("Die Beklagte beantragt:", S_JUSTIFY))
    els.append(P("Das Berufungsurteil des Oberlandesgerichts München vom 17. Februar 2025 "
                 "(Az. 13 U 412/24) wird aufgehoben. Das Urteil des Landgerichts München I "
                 "vom 06. Juni 2024 (Az. 12 O 8842/23) wird abgeändert. Die Klage wird "
                 "abgewiesen. Die Kläger tragen die Kosten des Rechtsstreits.", S_ANTRAG))
    els.append(SP(0.5))
    els.append(P("<b>REVISIONSGRÜNDE</b>", S_H1))
    els.append(HR())
    els.append(SP(0.2))
    els.append(P("<b>I. Verletzung von § 656a BGB i.V.m. § 126b BGB (§ 545 Abs. 1 ZPO)</b>", S_H2))
    els.append(P("Das Berufungsurteil verletzt Bundesrecht. Das OLG München hat die "
                 "Anforderungen des § 656a BGB i.V.m. § 126b BGB dahingehend überspannt, "
                 "als es für eine wirksame Textform-Erklärung eine explizite Objektnennung "
                 "innerhalb des Provisionshinweises fordert. Eine solche Anforderung ergibt "
                 "sich weder aus dem Wortlaut des § 126b BGB noch aus der Rechtsprechung "
                 "des BGH.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>II. Auslegung des § 126b BGB — Wortlaut und Systematik</b>", S_H2))
    els.append(P("§ 126b BGB verlangt (1) eine lesbare Erklärung, (2) Nennung der Person des "
                 "Erklärenden und (3) einen dauerhaften Datenträger. Die Norm stellt keine "
                 "Anforderungen an die Bestimmtheit des Vertragsgegenstands — dies ist eine "
                 "Frage des allgemeinen Vertragsrechts (§§ 145, 155, 157 BGB). Wenn §§ 145 ff. "
                 "BGB ausreichend bestimmte Erklärungen voraussetzen, so richtet sich das nach "
                 "allgemeinen Grundsätzen, nicht nach § 126b BGB.", S_JUSTIFY))
    els.append(PB())

    els.append(az_zeile())
    els.append(P("<b>III. BGH-Linie zur Bestimmtheit — Fortentwicklungsbedarf</b>", S_H2))
    els.append(P("Die Revisionsbegründung gibt dem BGH Gelegenheit, seine bisherige "
                 "Rechtsprechung zu § 656a BGB zu konsolidieren und klarzustellen:", S_JUSTIFY))
    revision_punkte = [
        ("BGH I ZR 113/21:", "Hat die Bestimmtheit einer E-Mail-Erklärung grundsätzlich bejaht. "
         "Offen gelassen: Reicht Kontextbezug aus?"),
        ("BGH I ZR 284/20:", "Notarielle Maklerklausel als Heilungsmittel abgelehnt. "
         "Aber: Kann sie als eigenständiger Vertragsschluss gewertet werden?"),
        ("BGH I ZR 197/22:", "Bestimmtheitserfordernis formuliert. Offen: "
         "Wann reicht ein Höchstsatz ohne konkrete Bezifferung?"),
        ("BGH I ZR 42/23:", "Signatur-Hinweis &quot;allein&quot; genügt nicht — was heißt &quot;nicht allein&quot;? "
         "Wieviel Kontext ist erforderlich?"),
        ("BGH I ZR 202/25:", "Vorliegende Sache — Die Beklagte erwartet Klarstellung, dass "
         "Kontextualisierung durch laufende Korrespondenz ausreicht."),
    ]
    for az, text in revision_punkte:
        els.append(P(f"<b>{az}</b> {text}", S_JUSTIFY))
        els.append(SP(0.1))
    els.append(SP(0.3))
    els.append(P("<b>IV. Zur Anwendbarkeit des § 242 BGB in Formvorschriftsfällen</b>", S_H2))
    els.append(P("Der BGH hat in verschiedenen Zusammenhängen anerkannt, dass § 242 BGB auch "
                 "zur Einschränkung von Formmängeln herangezogen werden kann (vgl. BGH NJW 1996, "
                 "1468 zur Schriftform in Mietverträgen; BGH NJW 2004, 2382). Die Revisionsbegründung "
                 "regt an, dass der BGH für § 656a BGB klären möge, ob und unter welchen "
                 "Voraussetzungen § 242 BGB eine Korrektur des Formmangels ermöglicht.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>V. Streitwert und Kosteninteresse</b>", S_H2))
    stwert = [
        ["Hauptforderung", "EUR 8.810,76"],
        ["Zinsen (5 % p.a. über Basiszins seit 12.08.2023 bis Revisions-Einlage)", "ca. EUR 780,00"],
        ["Verfahrenskosten gesamt (geschätzt)", "ca. EUR 12.000,00"],
        ["Gesamtinteresse Beklagte", "ca. EUR 21.590,76"],
    ]
    t = Table(stwert, colWidths=[340, 110])
    t.setStyle(TableStyle([
        ("FONTNAME",  (0,0), (-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 9),
        ("BOX",       (0,0), (-1,-1), 0.5, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.2, C_BORDER),
        ("ALIGN",     (1,0), (1,-1), "RIGHT"),
        ("TOPPADDING",(0,0),(-1,-1),3),
        ("BOTTOMPADDING",(0,0),(-1,-1),3),
    ]))
    els.append(t)
    els.append(SP(0.5))
    els.append(P("München, den 15. Mai 2025", S_NORMAL))
    els.append(SP(0.8))
    els.append(P("_____________________________________<br/>Dr. Adelheid Korkenzieher-Mariastein<br/>Rechtsanwältin", S_NORMAL))
    els.append(PB())

    # Weitere Seiten Revisionsbegründung
    for i in range(4):
        els.append(az_zeile())
        els.append(P(f"<b>REVISIONSBEGRÜNDUNG — TEIL {i+2}/5</b>", S_H1))
        els.append(HR())
        subtopics = [
            ("VI. Vergleichende Analyse anderer Formvorschriften im BGB",
             "§ 656a BGB ist nicht die einzige Textform-Vorschrift im BGB. Vergleichbare Regelungen "
             "finden sich in § 491a BGB (Verbraucherdarlehensverträge), § 492 BGB (Schriftform), "
             "§ 505b BGB (Immobiliar-Verbraucherdarlehensverträge) und § 550 BGB (Mietverträge). "
             "Bei § 550 BGB hat der BGH wiederholt entschieden, dass die wesentlichen Vertragsbestandteile "
             "erkennbar sein müssen, dass aber im Wege der Auslegung Lücken geschlossen werden können "
             "(BGH XII ZR 131/13, NJW 2015, 1087). Eine Parallelwertung für § 656a BGB erscheint sach- "
             "gerecht: Wenn der Kontext einer fortlaufenden E-Mail-Korrespondenz eindeutig ergibt, auf "
             "welches Objekt sich der Provisionshinweis bezieht, sollte dies ausreichen."),
            ("VII. Zur Europarechtskonformität des § 656a BGB (ergänzend)",
             "Die Richtlinie 2011/83/EU über Verbraucherrechte (Art. 7 Abs. 1) fordert bei Fernabsatz-"
             "verträgen die Mitteilung wesentlicher Informationen „klar und verständlich&quot;. Die Beklagte hat "
             "diese Informationen in ihrer E-Mail-Signatur bereitgestellt. Eine nationale Auslegung, die "
             "über das Richtlinienminimum hinausgeht, ist im Lichte des Verhältnismäßigkeitsgrundsatzes "
             "einer Überprüfung bedürftig. Die Beklagte regt eine Vorlage an den EuGH nach Art. 267 AEUV "
             "vor, falls der BGH erhebliche Zweifel an der Richtlinienkonformität hegt — was jedoch nach "
             "Auffassung der Beklagten nicht der Fall sein sollte."),
            ("VIII. Zu den wirtschaftlichen Konsequenzen",
             "Eine bestätigende BGH-Entscheidung (Revision zurückgewiesen) würde den Maklermarkt erheblich "
             "belasten. Bundesweit dürften Zehntausende von E-Mail-Korrespondenzen, in denen Makler "
             "Provisionsinformationen in der Signatur bereitgestellt haben, als formnichtig anzusehen sein. "
             "Die Schäden für die Maklerbranche wären erheblich. Demgegenüber haben die Käufer und Verkäufer "
             "die Maklertätigkeit tatsächlich in Anspruch genommen und würden nun von einem Formfehler "
             "profitieren, ohne dass eine Informationsasymmetrie oder Überrumpelung vorgelegen hätte."),
            ("IX. Gesamtergebnis und Schlussantrag",
             "Die Revisionsbegründung hat dargelegt, dass das Berufungsurteil des OLG München "
             "Bundesrecht verletzt. § 656a BGB i.V.m. § 126b BGB setzt keine explizite Objektnennung "
             "im Provisionshinweis voraus. Ein hinreichend kontextuierter Signaturhinweis in einer "
             "laufenden E-Mail-Korrespondenz über eine konkrete Immobilienvermittlung erfüllt die "
             "Textformanforderungen. Das BGH-Urteil sollte die bisherige Rechtsprechungslinie "
             "präzisieren und klarstellen, dass Kontextbezug ausreicht. Die Revision ist begründet."),
        ]
        title, body = subtopics[i]
        els.append(P(f"<b>{title}</b>", S_H2))
        els.append(P(body, S_JUSTIFY))
        els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 17: REVISIONSERWIDERUNG
# ─────────────────────────────────────────────────────────────────────────────
def section_revisionserwiderung():
    els = []
    els.append(P("Hagelbrand &amp; Trotzenburg Rechtsanwälte · Promenadeplatz 9 · 80333 München", S_BOLD))
    els.append(P("München, den <b>10. Juli 2025</b>", S_NORMAL))
    els.append(HR())
    els.append(P("<b>REVISIONSERWIDERUNG</b>", S_TITLE))
    els.append(P("BGH Az. I ZR 202/25 — Kläger als Revisionsbeklagte", S_CENTER))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("<b>I. Zur Revisionsbegründung</b>", S_H2))
    els.append(P("Die Revision der Beklagten ist unbegründet. Das Berufungsurteil des OLG München "
                 "vom 17. Februar 2025 hält der revisionsrechtlichen Nachprüfung stand. "
                 "Die Anforderungen des § 656a BGB i.V.m. § 126b BGB sind klar: Die Textform-"
                 "Erklärung muss eine auf Vertragsschluss gerichtete Willenserklärung enthalten. "
                 "Ein informatorischer Hinweis auf die grundsätzliche Möglichkeit einer "
                 "Provisionserhebung ist keine Willenserklärung.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>II. Wortlaut und Schutzzweck des § 656a BGB</b>", S_H2))
    els.append(P("§ 656a BGB setzt für die Textform einen Maklervertrag voraus — also einen Vertrag, "
                 "nicht eine Information. Vertragsschluss setzt übereinstimmende Willenserklärungen "
                 "(Angebot und Annahme) voraus. Eine Signatur mit Provisionshinweis ist kein Angebot "
                 "im Rechtssinn, weil sie nicht erkennen lässt, dass der Absender sich rechtsgeschäftlich "
                 "binden will (fehlender animus contrahendi). Ohne erkennbaren Bindungswillen "
                 "liegt kein Angebot vor, ohne Angebot kein Vertragsschluss.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>III. Zum Schutzzweck — BGH-Linie</b>", S_H2))
    els.append(P("Die BGH-Linie (I ZR 197/22; I ZR 42/23) ist eindeutig: § 656a BGB schützt "
                 "Verbraucher vor überraschenden Provisionsbelastungen. Dieser Schutz erfordert, "
                 "dass der Verbraucher aus der Textform-Erklärung klar erkennen kann, dass er "
                 "eine rechtlich bindende Provisionsverbindlichkeit eingeht. Dies ist bei einem "
                 "Signaturhinweis mit Höchstsatz nicht der Fall.", S_JUSTIFY))
    els.append(SP(0.5))
    els.append(P("München, den 10. Juli 2025", S_NORMAL))
    els.append(SP(0.8))
    els.append(P("_____________________________________<br/>Dr. Knut Hagelbrand-Wittlsbach<br/>Rechtsanwalt", S_NORMAL))
    els.append(PB())

    # Extra Seiten
    els.append(az_zeile())
    els.append(P("<b>REVISIONSERWIDERUNG — FORTSETZUNG</b>", S_H1))
    els.append(HR())
    els.append(P("<b>IV. Zum EuGH-Vorlageantrag der Revisionsbegründung</b>", S_H2))
    els.append(P("Die Revisionsbegründung regt eine Vorlage an den EuGH an. Diese ist nicht veranlasst: "
                 "Die Verbraucherrechterichtlinie 2011/83/EU enthält Mindeststandards, nicht "
                 "Höchststandards. Den Mitgliedstaaten ist es unbenommen, für den nationalen "
                 "Maklermarkt strengere Informationspflichten einzuführen (Art. 4 RL 2011/83/EU: "
                 "Vollharmonisierung — aber § 656a BGB betrifft nicht die in Art. 6 ff. geregelten "
                 "Informationspflichten, sondern die Formvorschriften für den Vertragsschluss, "
                 "welche nach Art. 3 Abs. 3 lit. e RL 2011/83/EU aus dem Anwendungsbereich der "
                 "Richtlinie ausgenommen sind).", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>V. Ergebnis</b>", S_H2))
    els.append(P("Die Kläger beantragen, die Revision der Beklagten zurückzuweisen und ihr "
                 "die Kosten des Revisionsverfahrens aufzuerlegen.", S_JUSTIFY))
    els.append(SP(0.5))
    els.append(P("München, den 10. Juli 2025", S_NORMAL))
    els.append(SP(0.8))
    els.append(P("_____________________________________<br/>Dr. Knut Hagelbrand-Wittlsbach<br/>Rechtsanwalt", S_NORMAL))
    els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 18: STELLUNGNAHMEN VOR BGH-VERHANDLUNG
# ─────────────────────────────────────────────────────────────────────────────
def section_stellungnahmen():
    els = []
    els.append(P("<b>STELLUNGNAHMEN ZUM BGH-VERHANDLUNGSTERMIN 11. MÄRZ 2026</b>", S_H1))
    els.append(P("BGH Az. I ZR 202/25, I. Zivilsenat, Verhandlungstag: 11. März 2026", S_NORMAL))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("<b>Stellungnahme Beklagte (RAin Korkenzieher-Mariastein, 28. Februar 2026):</b>", S_BOLD))
    els.append(P("Die Beklagte hält ihre bisherigen Rechtsstandpunkte vollumfänglich aufrecht. "
                 "Sie erwartet, dass der BGH die Gelegenheit nutzen wird, die Anforderungen an "
                 "§ 656a BGB praxistauglich zu gestalten. Insbesondere regt die Beklagte an, "
                 "einen Kriterienkatalog für die Bestimmtheit von Textform-Maklerverträgen zu "
                 "entwickeln. Für den Verhandlungstermin wird die persönliche Anwesenheit von "
                 "Frau Bechtholdsmeier-Schongau angeboten (sofern der BGH eine Parteivernehmung "
                 "erwägt, was im Revisionsverfahren jedoch unüblich ist).", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>Stellungnahme Kläger (RA Hagelbrand-Wittlsbach, 02. März 2026):</b>", S_BOLD))
    els.append(P("Die Kläger beantragen die Zurückweisung der Revision. Sie werden durch "
                 "RA Dr. Hagelbrand-Wittlsbach persönlich am BGH vertreten und bitten den "
                 "I. Zivilsenat, die bisherige Rechtsprechungslinie zu bestätigen. "
                 "Die Kläger weisen darauf hin, dass eine Stattgabe der Revision erhebliche "
                 "Rechtsunsicherheit in einem bereits weitgehend geklärten Rechtsgebiet "
                 "erzeugen würde.", S_JUSTIFY))
    els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 19: BGH-URTEIL TENOR-AUSZUG
# ─────────────────────────────────────────────────────────────────────────────
def section_bgh_urteil():
    els = []
    els.append(P("BUNDESGERICHTSHOF", S_TITLE))
    els.append(P("I. Zivilsenat", S_CENTER))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("<b>U R T E I L</b>", S_TITLE))
    els.append(SP(0.2))
    els.append(P("Az.: <b>I ZR 202/25</b>", S_CENTER_B))
    els.append(P("Verkündet am: <b>11. März 2026</b>", S_CENTER))
    els.append(HR())
    els.append(SP(0.2))
    els.append(P("In dem Rechtsstreit", S_RUBRUM))
    els.append(P("<b>Immobilien-Vermittlung Marlene Bechtholdsmeier-Schongau e.K.</b><br/>"
                 "— Beklagte, Berufungsführerin und Revisionsklägerin —", S_RUBRUM))
    els.append(P("gegen", S_RUBRUM))
    els.append(P("<b>Korbinian Haspelbeck-Türkenfeld und Walburga Haspelbeck-Türkenfeld</b><br/>"
                 "— Kläger, Berufungsbeklagte und Revisionsbeklagte —", S_RUBRUM))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("<b>T E N O R</b>", S_H1))
    els.append(HR())
    els.append(P("Die Revision der Beklagten gegen das Urteil des 13. Zivilsenats des "
                 "Oberlandesgerichts München vom 17. Februar 2025 wird zurückgewiesen.", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("Die Beklagte trägt die Kosten des Revisionsverfahrens.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("<b>GRÜNDE (Auszug — vollständige Urteilsgründe folgen)</b>", S_H1))
    els.append(HR())
    els.append(SP(0.2))
    els.append(P("<b>I. Leitsätze (vorläufig, Pressemitteilung BGH)</b>", S_H2))
    leitsätze = [
        ("1.", "Ein in der E-Mail-Signatur enthaltener genereller Hinweis auf die Fälligkeit einer "
         "Maklerprovision, der lediglich einen Höchstsatz ohne konkrete Bezugnahme auf das zu "
         "vermittelnde Objekt oder den Erwerber nennt, erfüllt die Anforderungen des § 656a BGB "
         "i.V.m. § 126b BGB nicht. Eine Erklärung im Sinne des § 126b BGB muss auf den Abschluss "
         "eines bestimmten Maklervertrages gerichtet sein und die wesentlichen Vertragselemente — "
         "zumindest das konkrete Objekt — bestimmbar machen."),
        ("2.", "Die notarielle Maklerklausel in einem Kaufvertrag (§ 13 des Kaufvertrages) ist "
         "nicht geeignet, einen mangels Textform nichtigen Maklervertrag zu heilen. Sie setzt "
         "einen bereits wirksam geschlossenen Maklervertrag voraus (Bestätigung von BGH I ZR 284/20)."),
        ("3.", "Der Bereicherungsanspruch des Maklerkunden (§ 812 Abs. 1 BGB) ist bei Verstoß "
         "gegen § 656a BGB nicht durch § 818 Abs. 2 BGB (Wertersatz für erbrachte Maklertätigkeit) "
         "ausgeschlossen. Der Schutzzweck des § 656a BGB würde leerlaufen, wenn der Formverstoß "
         "durch einen Wertersatzanspruch kompensiert werden könnte."),
        ("4.", "§ 242 BGB (Treu und Glauben) schließt die Geltendmachung der Formnichtigkeit "
         "nach § 656a BGB nicht aus, solange kein qualifiziertes Fehlverhalten des "
         "Berechtigten vorliegt, das den Formverstoß erst verursacht hätte."),
    ]
    for nr, text in leitsätze:
        els.append(P(f"<b>{nr}</b> {text}", S_JUSTIFY))
        els.append(SP(0.2))
    els.append(SP(0.3))
    els.append(P("<b>II. Entscheidungsbegründung (Kurzfassung)</b>", S_H2))
    els.append(P("Der I. Zivilsenat hat die Revision der Beklagten zurückgewiesen. Der Senat "
                 "bestätigt die Rechtsprechungslinie aus BGH I ZR 197/22 und I ZR 42/23: "
                 "§ 656a BGB verlangt für einen wirksamen Maklervertrag eine in Textform "
                 "abgefasste, auf Vertragsschluss gerichtete Willenserklärung, die die "
                 "wesentlichen Vertragsbestandteile erkennbar macht. Ein automatisch generierter "
                 "Signaturhinweis mit Höchstprovisionssatz und ohne Objektbezug erfüllt dies nicht.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("Karlsruhe, den 11. März 2026", S_NORMAL))
    els.append(SP(0.8))
    els.append(P("Prof. Dr. Bergmann-Kaiserswerth (Vorsitzender)   Dr. Kirchhoff-Allgäu   Dr. Fischbacher-Wörth<br/>"
                 "Dr. Löffler-Rupprecht   Dr. Hennecke-Bodensee", S_SMALL))
    els.append(P("Richter am BGH", S_SMALL))
    els.append(PB())
    return els


# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 20: MANDANTENMEMO
# ─────────────────────────────────────────────────────────────────────────────
def section_mandantenmemo():
    els = []
    els.append(AsciiBox([
        " +=========================================+",
        " | H/T — Hagelbrand & Trotzenburg          |",
        " |        Rechtsanwälte                    |",
        " |   Promenadeplatz 9 · 80333 München      |",
        " +=========================================+",
    ], w=380))
    els.append(SP(0.5))
    els.append(P("<b>MANDANTENMEMO — STRENG VERTRAULICH</b>", S_H1))
    els.append(HR())
    els.append(P("München, den <b>14. März 2026</b>", S_NORMAL))
    els.append(SP(0.2))
    els.append(P("<b>An:</b> Herr Korbinian Haspelbeck-Türkenfeld und Frau Walburga Haspelbeck-Türkenfeld<br/>"
                 "<b>Von:</b> RA Dr. Knut Hagelbrand-Wittlsbach<br/>"
                 "<b>Re:</b> BGH I ZR 202/25 — Urteil vom 11. März 2026", S_NORMAL))
    els.append(HR())
    els.append(SP(0.2))
    els.append(P("<b>1. Ergebnis des BGH-Verfahrens</b>", S_H2))
    els.append(P("Der Bundesgerichtshof hat am 11. März 2026 in Ihrer Sache entschieden. "
                 "Die Revision der Beklagten wurde zurückgewiesen. Das Urteil des OLG München "
                 "(und mittelbar des LG München I) ist damit rechtskräftig: Die Beklagte "
                 "Marlene Bechtholdsmeier-Schongau e.K. ist verpflichtet, Ihnen "
                 "EUR 8.810,76 nebst Zinsen zurückzuzahlen.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>2. Bedeutung des Urteils</b>", S_H2))
    els.append(P("Das BGH-Urteil I ZR 202/25 hat über Ihren Einzelfall hinaus erhebliche "
                 "Bedeutung für den gesamten deutschen Immobilienmaklermarkt. Der BGH hat "
                 "klargestellt, dass ein bloßer E-Mail-Signaturhinweis mit Höchstprovisionssatz "
                 "die Textformanforderungen des § 656a BGB nicht erfüllt. Dies schützt "
                 "künftig Immobilienkäufer und -verkäufer vor unklaren Provisionsvereinbarungen.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>3. Vollstreckung</b>", S_H2))
    els.append(P("Mit Rechtskraft des Urteils können wir die Vollstreckung betreiben. "
                 "Wir empfehlen folgende Vorgehensweise:", S_JUSTIFY))
    for s in [
        "Wir fordern die Beklagte innerhalb der nächsten Woche schriftlich zur Zahlung auf (Frist: 14 Tage).",
        "Sollte keine Zahlung erfolgen, beantragen wir die Erteilung einer vollstreckbaren Ausfertigung des BGH-Urteils.",
        "Bei Nichterfüllung: Pfändungs- und Überweisungsbeschluss auf die Konten der Beklagten.",
        "Die Beklagte haftet auch für die Kosten des Vollstreckungsverfahrens.",
    ]:
        els.append(P(f"— {s}", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>4. Kostenabrechnung (vorläufig)</b>", S_H2))
    kosten = [
        ["Position", "Betrag (netto)"],
        ["RVG-Verfahrensgebühr Nr. 3100 VV (Streitwert EUR 8.810,76)", "EUR 729,00"],
        ["RVG-Terminsgebühr Nr. 3104 VV (Verhandlung LG)", "EUR 729,00"],
        ["RVG-Einigungsgebühr (nicht angefallen — Vergleich gescheitert)", "EUR 0,00"],
        ["RVG-Revisions-Verfahrensgebühr Nr. 3104 VV (BGH)", "EUR 729,00"],
        ["Stundenaufwand gesamt 45,5 h × EUR 380 (abzgl. RVG-Guthaben)", "EUR 4.756,00"],
        ["Auslagen, Reisekosten, Kopien", "EUR 380,00"],
        ["Summe netto", "EUR 7.323,00"],
        ["USt. 19 %", "EUR 1.391,37"],
        ["Summe brutto", "EUR 8.714,37"],
        ["./. bereits bezahlter Vorschuss", "EUR 2.000,00"],
        ["Restbetrag", "EUR 6.714,37"],
    ]
    t = Table(kosten, colWidths=[340, 110])
    t.setStyle(TableStyle([
        ("FONTNAME",  (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME",  (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 9),
        ("BACKGROUND",(0,0), (-1,0), C_HEADER_BG),
        ("TEXTCOLOR", (0,0), (-1,0), white),
        ("FONTNAME",  (0,-3), (-1,-1), "Helvetica-Bold"),
        ("BACKGROUND",(0,-1),(-1,-1), C_YELLOW_HL),
        ("BOX",       (0,0), (-1,-1), 0.5, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.2, C_BORDER),
        ("TOPPADDING",(0,0),(-1,-1),4),
        ("BOTTOMPADDING",(0,0),(-1,-1),4),
        ("ALIGN",     (1,0), (1,-1), "RIGHT"),
    ]))
    els.append(t)
    els.append(SP(0.3))
    els.append(P("<i>Hinweis: Volle RVG-Kostenerstattung durch die Beklagte (soweit gerichtlich "
                 "tituliert) separat geltend zu machen. Übersteigende Stunden-Differenz von "
                 "EUR 4.756,00 (Honorarvereinbarung vs. RVG) ist aus dem Rückzahlungsbetrag "
                 "der Beklagten zu begleichen.</i>", S_SMALL))
    els.append(SP(0.5))
    els.append(P("Mit freundlichen Grüßen", S_NORMAL))
    els.append(SP(0.6))
    els.append(P("_____________________________________<br/>Dr. Knut Hagelbrand-Wittlsbach<br/>Rechtsanwalt", S_NORMAL))
    els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 21: HANDSCHRIFTLICHE NOTIZEN
# ─────────────────────────────────────────────────────────────────────────────
def section_handschriftliche_notizen():
    els = []
    els.append(P("<b>HANDSCHRIFTLICHE NOTIZEN — Korbinian Haspelbeck-Türkenfeld</b>", S_H1))
    els.append(P("(Kursiv-Simulation — gefunden an verschiedenen Schriftsatz-Rändern)", S_SMALL))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("Folgende handschriftliche Randnotizen (blau, Kugelschreiber) wurden an den "
                 "Aktenbestandteilen vorgefunden und wurden zur Dokumentation in Schriftform "
                 "übertragen:", S_NORMAL))
    els.append(SP(0.3))
    notizen = [
        ("Am Rand der Klageschrift (Seite 2, Abschnitt IV):",
         "Walburga: hatte ich nicht GENAU GEFRAGT?! Bechtholdsmeier hatte gesagt es sei alles in Ordnung. "
         "Ich hab ihr vertraut. Jetzt das. (Datum unleserlich)"),
        ("Am Rand der E-Mail vom 03.04.2023 (Provision-Signatur):",
         "Das haben wir nicht gesehen!!! War ganz unten. In sehr kleiner Schrift. Wer liest das?? "
         "Ich hätte nie zugestimmt wenn ich gewusst hätte. Frag Walburga."),
        ("Am Rand des Notarvertrag-Auszugs (§ 13 Maklerklausel):",
         "Der Notar hat das super schnell vorgelesen. Ich hab nicht verstanden was 'hängt vom Maklervertrag ab' "
         "bedeutet. Hätte ich fragen sollen? Wir waren aufgeregt wegen dem Verkauf."),
        ("Am Rand der Klageerwiderung (Abschnitt I, 'wirksamer Maklervertrag'):",
         "Das stimmt nicht. Die hatte nie explizit gesagt 'wir schließen jetzt einen Maklervertrag'. "
         "Das war immer nur 'ich kümmere mich'. Grrrr."),
        ("Am Rand des Vergleichsprotokolls (Angebot 50%):",
         "50% finde ich zu wenig. Walburga auch. Wir haben das Geld bezahlt ohne es zu schulden. "
         "Wieso sollen wir die hälfte schenken? Dr. Hagelbrand sagt wir gewinnen. Ich vertrau ihm."),
        ("Am Rand des BGH-Urteil-Tenors:",
         "GEWONNEN! Gott sei Dank. Walburga hat geweint (vor Freude glaube ich). "
         "3 Jahre!! Aber es war richtig dass wir nicht aufgegeben haben. Danke Dr. H.!"),
    ]
    for ort, text in notizen:
        els.append(P(f"<b>{ort}</b>", S_BOLD))
        els.append(P(ital(f"„{text}&quot;"), S_HANDW))
        els.append(SP(0.3))
    els.append(HR())
    els.append(P("<i>Kanzlei-Vermerk: Alle oben aufgeführten Notizen sind identisch mit den "
                 "handschriftlichen Originalen, die an den jeweiligen Schriftsätzen zu finden sind. "
                 "Schreibfehler wurden nicht korrigiert. — H/T, 15. März 2026</i>", S_TINY))
    els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 22: WHATSAPP-SIMULATION
# ─────────────────────────────────────────────────────────────────────────────
def section_whatsapp():
    els = []
    els.append(P("<b>ANLAGE — WHATSAPP-NACHRICHTEN WALBURGA ↔ KORBINIAN HASPELBECK</b>", S_H1))
    els.append(P("Rekonstruiert aus Screenshots — Datum: 12. Mai 2023 (Notartermin-Tag)", S_NORMAL))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("<i>Kontext: Die nachfolgenden WhatsApp-Nachrichten wurden während des "
                 "Notartermins am 12. Mai 2023 zwischen Walburga und Korbinian Haspelbeck-"
                 "Türkenfeld ausgetauscht. Korbinian wartete im Vorzimmer, während Walburga "
                 "in der Besprechung saß (oder umgekehrt — aus der Nachricht nicht eindeutig "
                 "erkennbar).</i>", S_SMALL))
    els.append(SP(0.4))

    # WhatsApp-Bubbles
    msgs = [
        ("Walburga", "Hast du das mit der Provision geklärt? Steht das auch im Vertrag?", "12:14", "left"),
        ("Korbinian", "Die Bechtholdsmeier sagt das ist normal. Standard bei jedem Verkauf.", "12:17", "right"),
        ("Walburga", "Wieviel genau? Hast du gefragt?", "12:19", "left"),
        ("Korbinian", "1,19% netto vom Kaufpreis hab ich verstanden. Hab unterschrieben", "12:22", "right"),
        ("Walburga", "Waaaas?! Ohne mich zu fragen?? Ich komm gleich raus.", "12:23", "left"),
        ("Korbinian", "Zu spät, der Notar liest gerade §13 vor. Ist doch ok oder? Alle zahlen das.", "12:25", "right"),
        ("Walburga", "Wir reden DANACH. Ich bin nicht happy.", "12:26", "left"),
        ("Korbinian", "Sorry. Ich dachte wir haben das besprochen.", "12:28", "right"),
    ]
    for sender, text, time, side in msgs:
        els.append(WhatsAppBubble(sender, text, time, side, w=440))
        els.append(SP(0.1))

    els.append(SP(0.4))
    els.append(HR())
    els.append(P("<i>Kanzlei H/T: Diese Nachrichten belegen, dass die Kläger beim Notartermin "
                 "keine klare Vorstellung von der Provisionsverbindlichkeit hatten und diese "
                 "jedenfalls nicht bewusst und informiert eingegangen sind. Relevant für "
                 "Schutzzweck § 656a BGB.</i>", S_SMALL))
    els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 23: KANZLEIRECHNUNG RVG
# ─────────────────────────────────────────────────────────────────────────────
def section_kanzleirechnung():
    els = []
    els.append(AsciiBox([
        " +=========================================+",
        " | H/T — Hagelbrand & Trotzenburg          |",
        " |   RECHNUNG                              |",
        " |   Promenadeplatz 9 · 80333 München      |",
        " |   Steuernummer: 143/234/50180            |",
        " +=========================================+",
    ], w=380))
    els.append(SP(0.5))
    els.append(P("<b>RECHNUNG NACH RVG</b>", S_H1))
    els.append(HR())
    els.append(P("Rechnungsnummer: HT-2026-0112<br/>Datum: 20. März 2026", S_NORMAL))
    els.append(SP(0.2))
    els.append(P("<b>An:</b> Korbinian und Walburga Haspelbeck-Türkenfeld,<br/>"
                 "Mauerkircherstraße 47, 81679 München", S_NORMAL))
    els.append(HR())
    els.append(SP(0.2))
    els.append(P("<b>Gegenstand:</b> Rechtliche Vertretung im Rechtsstreit gegen Immobilien-Vermittlung "
                 "Marlene Bechtholdsmeier-Schongau e.K. wegen Rückforderung Maklerprovision<br/>"
                 "<b>Aktenzeichen:</b> LG München I 12 O 8842/23 / OLG München 13 U 412/24 / BGH I ZR 202/25<br/>"
                 "<b>Streitwert:</b> EUR 8.810,76", S_NORMAL))
    els.append(SP(0.3))
    # RVG-Rechnung
    # Streitwert EUR 8.810,76 → Gebührenstufe nach Anlage 2 RVG: bis EUR 9.000 = EUR 486 (einfache Gebühr 1,0)
    rvg_data = [
        ["Nr.", "Gebührentatbestand", "Faktor", "Basis (EUR)", "Betrag (EUR)"],
        ["3100 VV RVG", "Verfahrensgebühr 1. Instanz", "1,3", "486,00", "631,80"],
        ["3104 VV RVG", "Terminsgebühr 1. Instanz (Verhandlung 12.06.2024)", "1,2", "486,00", "583,20"],
        ["3200 VV RVG", "Verfahrensgebühr Berufung", "1,6", "486,00", "777,60"],
        ["3202 VV RVG", "Terminsgebühr Berufung", "1,2", "486,00", "583,20"],
        ["3206 VV RVG", "Verfahrensgebühr Revision", "1,6", "486,00", "777,60"],
        ["3210 VV RVG", "Terminsgebühr Revision (BGH 11.03.2026)", "1,2", "486,00", "583,20"],
        ["7000 VV RVG", "Dokumentenpauschale (je Kopie)", "—", "—", "89,50"],
        ["7002 VV RVG", "Kommunikationspauschale", "—", "—", "20,00"],
        ["7003–7006 VV RVG", "Reisekosten BGH-Termin Karlsruhe", "—", "—", "284,00"],
        ["", "<b>Summe RVG netto</b>", "", "", "<b>4.330,10</b>"],
        ["", "davon erstattet durch Gericht (nach Kostenfestsetzung)", "", "", "−3.500,00"],
        ["", "<b>Noch zu zahlen (RVG netto)</b>", "", "", "<b>830,10</b>"],
        ["", "", "", "", ""],
        ["", "Stundenmehraufwand (45,5 h × EUR 380 = EUR 17.290 ./. RVG EUR 4.330 = EUR 12.960)", "", "", "12.960,00"],
        ["", "<b>Gesamt netto</b>", "", "", "<b>13.790,10</b>"],
        ["", "USt. 19 %", "", "", "2.620,12"],
        ["", "<b>Rechnungsbetrag brutto</b>", "", "", "<b>16.410,22</b>"],
        ["", "./. Vorschuss v. 16.08.2023", "", "", "−2.000,00"],
        ["", "./. Vorschuss v. 14.02.2025", "", "", "−3.000,00"],
        ["", "<b>Restzahlbetrag</b>", "", "", "<b>11.410,22</b>"],
    ]
    t = Table(rvg_data, colWidths=[90, 220, 40, 65, 75])
    t.setStyle(TableStyle([
        ("FONTNAME",  (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME",  (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 8),
        ("BACKGROUND",(0,0), (-1,0), C_HEADER_BG),
        ("TEXTCOLOR", (0,0), (-1,0), white),
        ("BOX",       (0,0), (-1,-1), 0.5, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.2, C_BORDER),
        ("TOPPADDING",(0,0),(-1,-1),3),
        ("BOTTOMPADDING",(0,0),(-1,-1),3),
        ("ALIGN",     (2,0), (-1,-1), "RIGHT"),
    ]))
    els.append(t)
    els.append(SP(0.3))
    els.append(P("<i>Zahlbar innerhalb von 14 Tagen. IBAN: DE88 7009 2300 0041 2356 12 (München)</i>", S_SMALL))
    els.append(SP(0.3))
    els.append(P("Hinweis: Aus dem durch die Beklagte zurückzuzahlenden Betrag von EUR 8.810,76 zzgl. "
                 "Zinsen sowie der gerichtlichen Kostenerstattung wird ein erheblicher Teil der "
                 "Anwaltskosten gedeckt. Die Mandantschaft hat wirtschaftlich de facto keine eigenen "
                 "Kosten zu tragen — das Ergebnis des Rechtsstreits war damit für sie vollständig "
                 "vorteilhaft.", S_JUSTIFY))
    els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 24: AKTENRAND-MEMO RAin KORKENZIEHER
# ─────────────────────────────────────────────────────────────────────────────
def section_aktenrandmemo():
    els = []
    els.append(P("<b>AKTENRAND-MEMO RAin Korkenzieher-Mariastein an Mandantin Bechtholdsmeier</b>", S_H1))
    els.append(P("(Rote Handschrift, auf dem Aktendeckel der Beklagten-Akte)", S_SMALL))
    els.append(HR())
    els.append(SP(0.3))
    els.append(RedMarginNote(
        "FRAU BECHTHOLDSMEIER: Bitte E-Mail-Templates dringend anpassen — "
        "Schluss-Markierung (§ 126b S. 1 BGB!) muss NACH dem Provisionshinweis stehen, "
        "damit dieser als eigenständige Erklärung gilt, nicht nur als Signatur! "
        "Außerdem: Objektbenennung UND konkreter Prozentsatz (kein 'maximal')! "
        "BGH hat jetzt dreimal Nein gesagt. Beim nächsten Fall gibt es KEINE Verteidigung mehr! "
        "— AdKM, 14.03.2026",
        w=450
    ))
    els.append(SP(1))
    els.append(P("<b>Erläuterung (Kanzlei K/M intern):</b>", S_BOLD))
    els.append(P("§ 126b Satz 1 BGB verlangt eine „lesbare Erklärung&quot; auf einem dauerhaften "
                 "Datenträger. Die Anforderung der Lesbarkeit impliziert nach der Rechtsprechung "
                 "des BGH, dass die Erklärung als solche erkennbar sein muss — d.h. der Empfänger "
                 "muss verstehen können, dass es sich um eine rechtserhebliche Erklärung handelt, "
                 "nicht um allgemeine Informationen. Um dies sicherzustellen:", S_JUSTIFY))
    for r in [
        "Der Provisionshinweis muss VOR der allgemeinen Signatur stehen oder klar abgetrennt sein",
        "Er muss das konkrete Objekt benennen (z.B. 'für das Objekt Mauerkircherstraße 47')",
        "Er muss einen festen Provisionssatz (nicht nur ein Maximum) angeben",
        "Er muss explizit als 'Angebot zum Abschluss eines Maklervertrages' bezeichnet sein",
        "Er muss eine Annahmemöglichkeit vorsehen (z.B. 'Bitte bestätigen Sie per Rückantwort')",
    ]:
        els.append(P(f"→ {r}", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<i>— Dr. Adelheid Korkenzieher-Mariastein, Rechtsanwältin, 14. März 2026 —</i>", S_ITALIC))
    els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 25: ANLAGENVERZEICHNIS
# ─────────────────────────────────────────────────────────────────────────────
def section_anlagenverzeichnis():
    els = []
    els.append(P("<b>ANLAGENVERZEICHNIS KLÄGER</b>", S_H1))
    els.append(P("Akte Haspelbeck-Türkenfeld ./. Bechtholdsmeier-Schongau e.K. — Az. LG München I 12 O 8842/23", S_NORMAL))
    els.append(HR())
    els.append(SP(0.3))
    anlagen = [
        ("K-MAK-1",  "Handelsregisterauszug HRA 98 871, AG München", "1 Seite", "Ja"),
        ("K-MAK-2",  "E-Mail-Kette März–August 2023 (Volltext, 8 E-Mails)", "8 Seiten", "Ja"),
        ("K-MAK-3",  "Notarieller Kaufvertrag UR-Nr. 1488/2023 (Auszug §§ 1–4, 13)", "5 Seiten", "Ja"),
        ("K-MAK-4",  "Kontoauszug Haspelbeck v. 03.06.2023", "1 Seite", "Ja"),
        ("K-MAK-5",  "Rechnung Bechtholdsmeier Nr. 2023-0088 v. 15.05.2023", "1 Seite", "Ja"),
        ("K-MAK-6",  "Zahlungsquittung Bechtholdsmeier v. 10.06.2023", "1 Seite", "Ja"),
        ("K-MAK-7",  "FEHLT — Schriftform-Entwurf — SONDERBAND II", "—", "NEIN"),
        ("K-MAK-8",  "Widerrufserklärung RA Hagelbrand v. 03.08.2023", "2 Seiten", "Ja"),
        ("K-MAK-9",  "Zurückweisung RAin Korkenzieher v. 12.08.2023", "1 Seite", "Ja"),
        ("K-MAK-10", "Volltext Mail-Signatur mit Provisionshinweis", "1 Seite", "Ja"),
        ("K-MAK-11", "WhatsApp-Screenshots Haspelbeck v. 12.05.2023", "1 Seite", "Ja"),
        ("K-MAK-12", "LG-Urteil 12 O 8842/23 v. 06.06.2024 (vollständig)", "12 Seiten", "Ja"),
        ("K-MAK-13", "FEHLT — Grundbuchauszug — SONDERBAND II", "—", "NEIN"),
        ("K-MAK-14", "Verhandlungsprotokoll LG München I v. 08.02.2024", "3 Seiten", "Ja"),
        ("K-MAK-15", "Berufungsschriftsatz Beklagte v. 04.07.2024", "4 Seiten", "Ja"),
        ("K-MAK-16", "Berufungsbegründung Beklagte v. 05.08.2024", "18 Seiten", "Ja"),
        ("K-MAK-17", "Berufungserwiderung Kläger v. 16.09.2024", "8 Seiten", "Ja"),
        ("K-MAK-18", "OLG München Urteil 13 U 412/24 v. 17.02.2025", "10 Seiten", "Ja"),
        ("K-MAK-19", "Revisionsbegründung Beklagte v. 15.05.2025", "16 Seiten", "Ja"),
        ("K-MAK-20", "Revisionserwiderung Kläger v. 10.07.2025", "7 Seiten", "Ja"),
        ("K-MAK-21", "FEHLT — Maklerexposé Originalversion — SONDERBAND II", "—", "NEIN"),
        ("K-MAK-22", "BGH I ZR 197/22, NJW 2023, 441 (Kopie)", "8 Seiten", "Ja"),
        ("K-MAK-23", "BGH I ZR 42/23, NJW 2024, 223 (Kopie)", "7 Seiten", "Ja"),
        ("K-MAK-24", "BGH I ZR 284/20, NJW 2022, 1896 (Kopie)", "9 Seiten", "Ja"),
        ("K-MAK-25", "Immobilieninserat Bechtholdsmeier (Mauerkircherstraße 47)", "2 Seiten", "Ja"),
        ("K-MAK-26", "Honorarvereinbarung Kläger/RA Hagelbrand v. 15.08.2023", "2 Seiten", "Ja"),
        ("K-MAK-27", "Lichtbilder Objekt Mauerkircherstraße 47 (8 Fotos)", "2 Seiten", "Ja"),
        ("K-MAK-28", "Vergleichsprotokoll LG München I v. 12.06.2024", "2 Seiten", "Ja"),
        ("K-MAK-29", "BGH I ZR 202/25, Pressemitteilung v. 11.03.2026", "1 Seite", "Ja"),
    ]
    data = [["Anlage", "Beschreibung", "Umfang", "Vorhanden"]] + list(anlagen)
    t = Table(data, colWidths=[65, 290, 65, 55])
    t.setStyle(TableStyle([
        ("FONTNAME",  (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME",  (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 8),
        ("BACKGROUND",(0,0), (-1,0), C_HEADER_BG),
        ("TEXTCOLOR", (0,0), (-1,0), white),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[white, C_LIGHT_BG]),
        # Rot für fehlende
        ("TEXTCOLOR", (0,7), (-1,7), C_MEMO_RED),
        ("TEXTCOLOR", (0,13), (-1,13), C_MEMO_RED),
        ("TEXTCOLOR", (0,21), (-1,21), C_MEMO_RED),
        ("BOX",       (0,0), (-1,-1), 0.5, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.2, C_BORDER),
        ("TOPPADDING",(0,0),(-1,-1),3),
        ("BOTTOMPADDING",(0,0),(-1,-1),3),
    ]))
    els.append(t)
    els.append(SP(0.3))
    els.append(P("<i>Hinweis: K-MAK-7, K-MAK-13 und K-MAK-21 befinden sich im Sonderband II der Akte. "
                 "Dieser Band ist dem vorliegenden Aktenbestandteil nicht beigefügt. Bei Bedarf "
                 "Rücksprache mit Kanzlei Hagelbrand &amp; Trotzenburg.</i>", S_SMALL))
    els.append(PB())
    return els

# ─────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 26: STUNDENAUFSTELLUNG (3 Seiten)
# ─────────────────────────────────────────────────────────────────────────────
def section_stundenaufstellung():
    els = []
    els.append(P("<b>STUNDENAUFSTELLUNG — Hagelbrand &amp; Trotzenburg Rechtsanwälte</b>", S_H1))
    els.append(P("Mandat: Haspelbeck-Türkenfeld ./. Bechtholdsmeier-Schongau e.K.<br/>"
                 "Internes Az.: HT-2023-0892 | Zeitraum: 15. August 2023 bis 20. März 2026", S_NORMAL))
    els.append(HR())
    els.append(SP(0.3))

    stunden = [
        # 2023
        ("2023-08-15", "Erstgespräch Mandantschaft (2h), Aktenaufbau (1h)", "3,0", "380", "1.140,00"),
        ("2023-08-16", "Recherche § 656a BGB, BGH-Rechtsprechung", "4,0", "380", "1.520,00"),
        ("2023-08-18", "Konzept Klageschrift", "2,0", "380", "760,00"),
        ("2023-09-01", "Entwurf Klageschrift Teil I", "3,5", "380", "1.330,00"),
        ("2023-09-05", "Entwurf Klageschrift Teil II, Anlagen", "3,5", "380", "1.330,00"),
        ("2023-09-10", "Abstimmung Mandantschaft, finale Klageschrift", "2,0", "380", "760,00"),
        ("2023-10-28", "Lektüre Klageerwiderung, Analyse", "2,5", "380", "950,00"),
        ("2023-11-10", "Entwurf Replik", "3,0", "380", "1.140,00"),
        ("2023-11-15", "Finale Replik, Einreichung", "1,5", "380", "570,00"),
        # 2024
        ("2024-02-08", "Terminsvorb. Verhandlung LG", "1,5", "380", "570,00"),
        ("2024-02-09", "Verhandlung LG München I, Fahrt, Protokoll", "4,0", "380", "1.520,00"),
        ("2024-05-15", "Urteilseingang, Analyse LG-Urteil", "2,0", "380", "760,00"),
        ("2024-06-10", "Terminsvorb. Vergleichsverhandlung", "1,0", "380", "380,00"),
        ("2024-06-12", "Vergleichsverhandlung LG, kein Ergebnis", "3,0", "380", "1.140,00"),
        ("2024-07-01", "Berufungserwiderung Entwurf I", "2,5", "380", "950,00"),
        ("2024-08-20", "Lektüre Berufungsbegründung Beklagte", "3,0", "380", "1.140,00"),
        ("2024-09-10", "Berufungserwiderung Entwurf final", "2,5", "380", "950,00"),
        ("2025-01-20", "Terminsvorb. OLG München", "2,0", "380", "760,00"),
        ("2025-01-22", "OLG-Verhandlung, Fahrt, Protokoll", "4,5", "380", "1.710,00"),
        ("2025-02-20", "Urteilseingang OLG, Analyse Revisionszulassung", "2,0", "380", "760,00"),
        # 2025-2026
        ("2025-04-10", "Revisionserwiderung Entwurf I", "3,0", "380", "1.140,00"),
        ("2025-06-05", "Finale Revisionserwiderung, Einreichung BGH", "2,0", "380", "760,00"),
        ("2025-12-15", "Lektüre BGH-Verfügung, Terminvorbereitung", "1,5", "380", "570,00"),
        ("2026-03-09", "Terminsvorb. BGH Karlsruhe (umfassend)", "4,0", "380", "1.520,00"),
        ("2026-03-11", "BGH-Verhandlung Karlsruhe (Reisetag)", "8,0", "380", "3.040,00"),
        ("2026-03-12", "Urteilsauswertung, Mandantenmemo Entwurf", "2,0", "380", "760,00"),
        ("2026-03-14", "Mandantenmemo final, Vollstreckungsplanung", "1,5", "380", "570,00"),
    ]
    data = [["Datum", "Tätigkeit", "Std.", "EUR/h", "Betrag"]] + list(stunden)
    # Summe
    total = sum(float(s[2].replace(",", ".")) for s in stunden)
    # total_betrag not needed separately
    # Berechne einfach: 45.5 * 380
    total_betrag_eur = 45.5 * 380
    data.append(["", "<b>Gesamtstunden</b>", f"<b>{total:.1f}</b>", "", f"<b>EUR {total_betrag_eur:,.2f}</b>".replace(",", ".")])

    t = Table(data, colWidths=[70, 250, 35, 45, 80])
    style = [
        ("FONTNAME",  (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME",  (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 8),
        ("BACKGROUND",(0,0), (-1,0), C_HEADER_BG),
        ("TEXTCOLOR", (0,0), (-1,0), white),
        ("ROWBACKGROUNDS",(0,1),(-1,-2),[white, C_LIGHT_BG]),
        ("FONTNAME",  (0,-1), (-1,-1), "Helvetica-Bold"),
        ("BACKGROUND",(0,-1), (-1,-1), C_YELLOW_HL),
        ("BOX",       (0,0), (-1,-1), 0.5, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.2, C_BORDER),
        ("TOPPADDING",(0,0),(-1,-1),3),
        ("BOTTOMPADDING",(0,0),(-1,-1),3),
        ("ALIGN",     (2,0), (-1,-1), "RIGHT"),
    ]
    t.setStyle(TableStyle(style))
    els.append(t)
    els.append(SP(0.3))
    els.append(P(f"<b>Gesamtstunden: {total:.1f} h</b> | Gesamtbetrag netto: EUR {total_betrag_eur:,.2f}".replace(",", "."), S_BOLD))
    els.append(SP(0.3))
    els.append(P("<i>Diese Stundenaufstellung wurde erstellt nach § 10 RVG (bei Abrechnung nach "
                 "Zeithonorar). Alle Zeiten wurden unmittelbar nach der jeweiligen Tätigkeit "
                 "in das Zeiterfassungssystem der Kanzlei eingetragen. Die vollständigen "
                 "Arbeitsnachweise liegen bei der Kanzlei vor und können auf Anfrage eingesehen werden.</i>",
                 S_SMALL))
    els.append(SP(0.3))
    els.append(HR())
    els.append(P("München, den 20. März 2026", S_NORMAL))
    els.append(SP(0.6))
    els.append(P("_____________________________________<br/>Dr. Knut Hagelbrand-Wittlsbach<br/>Rechtsanwalt", S_NORMAL))
    els.append(PB())
    return els

def section_gerichtliches_hinweisschreiben():
    """Gerichtliche Hinweise und Zwischenverfügungen"""
    els = []
    els.append(P("<b>ZWISCHENVERFÜGUNGEN UND HINWEISE DES GERICHTS</b>", S_H1))
    els.append(P("LG München I 12 O 8842/23 — Zivilkammer 12", S_NORMAL))
    els.append(HR())
    els.append(SP(0.3))
    
    # Erste Verfügung
    els.append(P("<b>VERFÜGUNG vom 22. September 2023</b>", S_BOLD))
    els.append(HR())
    els.append(P("In der Sache Haspelbeck-Türkenfeld ./. Bechtholdsmeier-Schongau e.K. "
                 "ergeht folgende Verfügung des Vorsitzenden:", S_JUSTIFY))
    els.append(SP(0.2))
    for nr, txt in [
        ("1.", "Die Klageschrift wird der Beklagten zugestellt. Frist zur Klageerwiderung: "
         "4 Wochen ab Zustellung (§ 277 Abs. 3 ZPO)."),
        ("2.", "Das Gericht weist vorsorglich darauf hin, dass es für einen schlüssigen Vortrag "
         "zur Formnichtigkeit nach § 656a BGB ausreichend sein könnte, wenn der klägerische "
         "Vortrag die konkrete E-Mail nebst Signatur als Anlage vorlegt."),
        ("3.", "Streitwert wird vorläufig auf EUR 8.810,76 festgesetzt."),
    ]:
        els.append(P(f"<b>{nr}</b> {txt}", S_ANTRAG))
    els.append(SP(0.2))
    els.append(P("München, den 22. September 2023", S_NORMAL))
    els.append(SP(0.5))
    els.append(P("Dr. Greifswald-Haunsberg<br/>Vorsitzender Richter, LGDir.", S_SMALL))
    els.append(SP(0.5))
    
    # Zweite Verfügung: nach Klageerwiderung
    els.append(P("<b>VERFÜGUNG vom 05. Dezember 2023</b>", S_BOLD))
    els.append(HR())
    els.append(P("Nach Eingang der Replik der Kläger wird Termin zur mündlichen Verhandlung bestimmt "
                 "auf Donnerstag, den <b>08. Februar 2024, 09:30 Uhr, Sitzungssaal 103</b> "
                 "des Landgerichts München I, Prielmayerstraße 7, 80335 München.", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("Das Gericht weist vorläufig darauf hin:", S_BOLD))
    els.append(P("Nach gegenwärtigem Sach- und Streitstand neigt die Kammer dazu, die Klage als "
                 "begründet anzusehen. Der Signaturhinweis in der E-Mail der Beklagten vom "
                 "03. April 2023 erscheint nach vorläufiger Prüfung nicht ausreichend, um die "
                 "Anforderungen des § 656a BGB an einen Textform-Maklervertrag zu erfüllen. "
                 "Es fehlt insbesondere eine ausreichend objektbezogene und auf Vertragsschluss "
                 "gerichtete Erklärung. Die Parteien erhalten Gelegenheit, hierzu vor dem Termin "
                 "ergänzend vorzutragen.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("München, den 05. Dezember 2023", S_NORMAL))
    els.append(SP(0.5))
    els.append(P("Dr. Greifswald-Haunsberg<br/>Vorsitzender Richter, LGDir.", S_SMALL))
    els.append(PB())
    
    # Kostenfestsetzungsbeschluss
    els.append(az_zeile())
    els.append(P("<b>KOSTENFESTSETZUNGSBESCHLUSS</b>", S_H1))
    els.append(P("LG München I, Az. 12 O 8842/23", S_NORMAL))
    els.append(HR())
    els.append(SP(0.2))
    els.append(P("In dem Kostenfestsetzungsverfahren nach §§ 103, 104 ZPO setzt der Rechtspfleger "
                 "die von der Beklagten an die Kläger zu erstattenden Kosten wie folgt fest:", S_JUSTIFY))
    els.append(SP(0.2))
    kf_data = [
        ["Kostenposition", "Betrag"],
        ["Verfahrensgebühr Nr. 3100 VV RVG (1,3 × EUR 486)", "EUR 631,80"],
        ["Terminsgebühr Nr. 3104 VV RVG (1,2 × EUR 486)", "EUR 583,20"],
        ["Post- und Telekommunikationspauschale Nr. 7002 VV RVG", "EUR 20,00"],
        ["Gerichtskostenvorschuss", "EUR 462,00"],
        ["Einigungsgebühr (nicht angefallen)", "EUR 0,00"],
        ["USt. 19 % auf Anwaltsgebühren (EUR 1.215,00)", "EUR 230,85"],
        ["<b>Summe erstattungsfähige Kosten 1. Instanz</b>", "<b>EUR 1.927,85</b>"],
    ]
    t = Table(kf_data, colWidths=[340, 110])
    t.setStyle(TableStyle([
        ("FONTNAME",  (0,0), (-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 9),
        ("FONTNAME",  (0,-1), (-1,-1), "Helvetica-Bold"),
        ("BACKGROUND",(0,-1),(-1,-1), C_YELLOW_HL),
        ("BOX",       (0,0), (-1,-1), 0.5, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.2, C_BORDER),
        ("TOPPADDING",(0,0),(-1,-1),4),
        ("BOTTOMPADDING",(0,0),(-1,-1),4),
        ("ALIGN",     (1,0), (1,-1), "RIGHT"),
    ]))
    els.append(t)
    els.append(SP(0.3))
    els.append(P("Die Beklagte hat die vorstehend festgesetzten Kosten innerhalb von 2 Wochen "
                 "an die Kläger zu erstatten. Gegen diesen Beschluss findet die sofortige "
                 "Beschwerde statt (§ 104 Abs. 3 ZPO).", S_JUSTIFY))
    els.append(SP(0.5))
    els.append(P("München, den 15. Juli 2024", S_NORMAL))
    els.append(SP(0.6))
    els.append(P("Müller-Aschheim<br/>Rechtspfleger", S_SMALL))
    els.append(PB())
    
    # Seite 3: Berufungsprotokoll
    els.append(az_zeile())
    els.append(P("<b>PROTOKOLL BERUFUNGSVERHANDLUNG OLG MÜNCHEN</b>", S_H1))
    els.append(P("OLG München, 13. Zivilsenat, Az. 13 U 412/24, 22. Januar 2025, 10:15 Uhr", S_NORMAL))
    els.append(HR())
    els.append(SP(0.2))
    els.append(P("<b>Erschienen:</b>", S_BOLD))
    for p in [
        "Kläger-RA: Dr. Knut Hagelbrand-Wittlsbach",
        "Beklagten-RAin: Dr. Adelheid Korkenzieher-Mariastein",
        "Vorsitzende: Dr. Regina Vogelhuber-Tegernsee, Vorsitzende Richterin am OLG",
        "Beisitzer: Dr. Winfried Schirmbeck-Augsburg, Richter am OLG",
        "Beisitzerin: Claudia Seiffert-Nymphenburg, Richterin am OLG",
    ]:
        els.append(P(f"• {p}", S_NORMAL))
    els.append(SP(0.3))
    els.append(P("<b>Hinweis des Senats (§ 522 Abs. 2 ZPO-analog):</b>", S_BOLD))
    els.append(P("Die Vorsitzende erläuterte, dass der Senat nach vorläufiger Beratung die "
                 "Berufung für offensichtlich unbegründet halte. Der Senat folge der "
                 "Rechtsprechung des BGH zu § 656a BGB und sehe keine Veranlassung, "
                 "davon abzuweichen. Insbesondere fehle dem Signaturhinweis der Beklagten "
                 "eine auf Vertragsschluss gerichtete Willenserklärung und eine ausreichend "
                 "bestimmte Objektbezeichnung.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>Revisionsankündigung:</b>", S_BOLD))
    els.append(P("RAin Dr. Korkenzieher-Mariastein erklärte, dass die Beklagte für den Fall "
                 "einer ihr nachteiligen Berufungsentscheidung Revision zum BGH einzulegen "
                 "beabsichtige. Die Beklagte halte die Rechtsfrage der Bestimmtheit von "
                 "E-Mail-Signaturhinweisen für grundsätzlich bedeutsam.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>Ergebnis:</b> Kein Vergleich. Urteilsverkündung auf 17. Februar 2025 terminiert.", S_BOLD))
    els.append(PB())
    return els



# ─────────────────────────────────────────────────────────────────────────────
# PAGE TEMPLATE — Kopf- und Fußzeile
# ─────────────────────────────────────────────────────────────────────────────
class PageTemplate:
    def __init__(self):
        self.page = 0

    def on_first_page(self, canvas_obj, doc):
        self.draw_page(canvas_obj, doc)

    def on_later_pages(self, canvas_obj, doc):
        self.draw_page(canvas_obj, doc)

    def draw_page(self, c, doc):
        c.saveState()
        # Kopfzeile (außer erster Seite)
        if c.getPageNumber() > 1:
            c.setFont("Helvetica", 7)
            c.setFillColor(HexColor("#666666"))
            c.drawString(cm, PAGE_H - 0.7*cm,
                         "Testakte: Haspelbeck-Türkenfeld ./. Bechtholdsmeier-Schongau e.K. "
                         "— Az. LG München I 12 O 8842/23 / OLG München 13 U 412/24 / BGH I ZR 202/25")
            c.line(cm, PAGE_H - 0.8*cm, PAGE_W - cm, PAGE_H - 0.8*cm)

        # Fußzeile
        c.setFont("Helvetica", 7)
        c.setFillColor(HexColor("#666666"))
        c.line(cm, 1.0*cm, PAGE_W - cm, 1.0*cm)
        c.drawString(cm, 0.6*cm,
                     "FIKTIVE TESTAKTE — Nur für Schulungszwecke — Alle Angaben erfunden — "
                     "Kein echtes Rechtsdokument")
        c.drawRightString(PAGE_W - cm, 0.6*cm, f"Seite {c.getPageNumber()}")
        c.restoreState()

# ─────────────────────────────────────────────────────────────────────────────
# ZUSÄTZLICHE ABSCHNITTE: Erstinstanzliche Verhandlungsprotokolle + Gutachten
# ─────────────────────────────────────────────────────────────────────────────
def section_erstinstanz_verlauf():
    """Erstinstanzlicher Verfahrensverlauf — Protokolle, Hinweise, Beschlüsse"""
    els = []
    els.append(P("<b>VERFAHRENSVERLAUF ERSTINSTANZ — LG MÜNCHEN I 12 O 8842/23</b>", S_H1))
    els.append(P("Übersicht der prozessualen Vorgänge und Beschlüsse", S_NORMAL))
    els.append(HR())
    els.append(SP(0.3))
    
    # Chronologische Übersicht
    verlauf = [
        ("14.09.2023", "Klageschrift eingereicht", "Hagelbrand & Trotzenburg"),
        ("22.09.2023", "Klagezustellung an Beklagte (§ 253 ZPO)", "Gerichtsvollzieher"),
        ("24.10.2023", "Klageerwiderung eingereicht (Frist verlängert)", "Korkenzieher Maibach"),
        ("17.11.2023", "Replik Kläger eingereicht", "Hagelbrand & Trotzenburg"),
        ("05.12.2023", "Beschluss: Termin zur mündlichen Verhandlung auf 08.02.2024", "LG München I"),
        ("20.01.2024", "Schriftsatz Beklagte: Ergänzende Zeugennennung", "Korkenzieher Maibach"),
        ("28.01.2024", "Kurze Stellungnahme Kläger zu Zeugennennung", "Hagelbrand & Trotzenburg"),
        ("08.02.2024", "Mündliche Verhandlung (Protokoll s.u.)", "LG München I"),
        ("15.03.2024", "Beschluss: Schriftliches Verfahren nach § 128 Abs. 2 ZPO", "LG München I"),
        ("01.04.2024", "Abschließender Schriftsatz Beklagte", "Korkenzieher Maibach"),
        ("15.04.2024", "Abschließender Schriftsatz Kläger", "Hagelbrand & Trotzenburg"),
        ("12.06.2024", "Vergleichsverhandlung (gescheitert)", "LG München I"),
        ("06.06.2024", "Urteil verkündet", "LG München I, Vors. Dr. Greifswald-Haunsberg"),
    ]
    data = [["Datum", "Vorgang", "Beteiligte/r"]] + verlauf
    t = Table(data, colWidths=[80, 250, 120])
    t.setStyle(TableStyle([
        ("FONTNAME",  (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME",  (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 9),
        ("BACKGROUND",(0,0), (-1,0), C_HEADER_BG),
        ("TEXTCOLOR", (0,0), (-1,0), white),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[white, C_LIGHT_BG]),
        ("BOX",       (0,0), (-1,-1), 0.5, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.2, C_BORDER),
        ("TOPPADDING",(0,0),(-1,-1),4),
        ("BOTTOMPADDING",(0,0),(-1,-1),4),
    ]))
    els.append(t)
    els.append(SP(0.5))
    
    els.append(P("<b>PROTOKOLL MÜNDLICHE VERHANDLUNG</b>", S_H1))
    els.append(P("LG München I, Az. 12 O 8842/23, 08. Februar 2024, 09:30 Uhr, Saal 103", S_NORMAL))
    els.append(HR())
    els.append(SP(0.3))
    els.append(P("Der Vorsitzende Richter Dr. Benedikt Greifswald-Haunsberg eröffnete die Sitzung "
                 "und stellte die Parteien sowie deren Bevollmächtigte fest. Anwesend: "
                 "Kläger Korbinian und Walburga Haspelbeck-Türkenfeld, RA Dr. Hagelbrand-Wittlsbach; "
                 "Beklagte Marlene Bechtholdsmeier-Schongau, RAin Dr. Korkenzieher-Mariastein.", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("<b>Richterlicher Hinweis (§ 139 ZPO):</b>", S_BOLD))
    els.append(P("Der Vorsitzende wies darauf hin, dass die Kammer nach vorläufiger Beratung "
                 "erhebliche Bedenken gegen die Wirksamkeit des Verkäufer-Maklervertrags hat. "
                 "Insbesondere fehle es an einer ausreichend bestimmten Erklärung zum Abschluss "
                 "eines Maklervertrags. Die Kammer tendiere dazu, dem klägerischen Standpunkt "
                 "zu folgen. Die Beklagte erhalte Gelegenheit, ergänzend zur Frage der Bestimmtheit "
                 "des Signaturhinweises vorzutragen (Frist: 4 Wochen nach Sitzung).", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>Parteierklärungen:</b>", S_BOLD))
    els.append(P("RA Dr. Hagelbrand-Wittlsbach erklärte, die Kläger hielten ihren Klageantrag "
                 "vollumfänglich aufrecht. Die Rechtslage sei durch BGH I ZR 197/22 eindeutig "
                 "geklärt. Eine weitere Beweisaufnahme sei nicht erforderlich.", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("RAin Dr. Korkenzieher-Mariastein erklärte, die Beklagte bestreite eine "
                 "Textform-Verletzung. Der Signaturhinweis sei ausreichend bestimmt. "
                 "Sie bitte um die Möglichkeit weiteren Vortrags sowie um Terminbestimmung "
                 "zur Zeugenvernehmung von Frau Bechtholdsmeier-Schongau.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>Beschluss der Kammer:</b>", S_BOLD))
    els.append(P("Die Kammer beschließt, das Verfahren im schriftlichen Verfahren nach "
                 "§ 128 Abs. 2 ZPO fortzuführen und kündigt Termin zur Urteilsverkündung an. "
                 "Die beantragte Zeugenvernehmung wird abgelehnt, da eine etwaige telefonische "
                 "Einigung über die Provision ebenfalls an der Textform-Anforderung des "
                 "§ 656a BGB scheitern würde.", S_JUSTIFY))
    els.append(PB())
    
    # Seite 2: LG-Urteil vollständige Gründe
    els.append(az_zeile())
    els.append(P("<b>ERSTINSTANZLICHES URTEIL — GRÜNDE (AUSZUG)</b>", S_H1))
    els.append(P("LG München I, Urteil v. 06. Juni 2024, Az. 12 O 8842/23", S_NORMAL))
    els.append(HR())
    els.append(SP(0.2))
    els.append(P("<b>Tenor (Wiederholung):</b>", S_BOLD))
    els.append(P("Die Beklagte wird verurteilt, an die Kläger EUR 8.810,76 nebst Zinsen in Höhe "
                 "von 5 Prozentpunkten über dem Basiszinssatz seit dem 12. August 2023 zu zahlen. "
                 "Die Beklagte trägt die Kosten des Rechtsstreits.", S_JUSTIFY))
    els.append(SP(0.3))
    els.append(P("<b>Entscheidungsgründe (Auszug aus Urteil Bl. 1-12):</b>", S_BOLD))
    els.append(P("Die zulässige Klage ist begründet. Den Klägern steht gegen die Beklagte "
                 "ein Bereicherungsanspruch aus § 812 Abs. 1 Satz 1, 1. Alt. BGB zu. "
                 "Die Beklagte hat die Maklerprovision von EUR 8.810,76 ohne Rechtsgrund erhalten, "
                 "da zwischen den Parteien kein wirksamer Verkäufer-Maklervertrag nach § 656a BGB "
                 "zustande gekommen ist.", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("1. Der zwischen den Parteien ausgetauschte E-Mail-Verkehr erfüllt die "
                 "Anforderungen des § 656a BGB nicht. Die Beklagte hat lediglich in der "
                 "Signatur ihrer E-Mail vom 03. April 2023 auf die grundsätzliche Möglichkeit "
                 "einer Provisionserhebung hingewiesen. Dieser Hinweis enthält weder eine "
                 "auf Vertragsschluss gerichtete Willenserklärung (fehlendes Angebot i.S.d. "
                 "§ 145 BGB) noch die wesentlichen Vertragsbestandteile (Objekt, fester "
                 "Provisionssatz, Parteibezeichnung). Eine Erklärung ist nur dann eine "
                 "Willenserklärung, wenn ihr ein Geschäftswille zu entnehmen ist "
                 "(BGH NJW 2023, 441, Rn. 18 ff.).", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("2. Die notarielle Maklerklausel in § 13 des Kaufvertrages vermag den "
                 "Formmangel nicht zu heilen (BGH NJW 2022, 1896). Sie setzt einen bereits "
                 "wirksam geschlossenen Maklervertrag voraus.", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("3. Ein Wertersatzanspruch der Beklagten nach § 818 Abs. 2 BGB besteht "
                 "nicht. Der Schutzzweck des § 656a BGB würde durch eine Wertersatzpflicht "
                 "leerlaufen (vgl. BGH NJW 2023, 441, Rn. 41).", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("4. Die Beklagte kann sich nicht auf Entreicherung (§ 818 Abs. 3 BGB) "
                 "berufen, weil sie als gewerbliche Maklerin die Formanforderungen des "
                 "§ 656a BGB kannte oder kennen musste (§ 819 Abs. 1 BGB).", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("5. Die Berufung auf die Formnichtigkeit durch die Kläger ist nicht nach "
                 "§ 242 BGB ausgeschlossen, da kein qualifiziertes Fehlverhalten der Kläger "
                 "vorliegt, das den Formverstoß erst verursacht hätte.", S_JUSTIFY))
    els.append(SP(0.5))
    els.append(P("München, den 06. Juni 2024", S_NORMAL))
    els.append(SP(0.6))
    els.append(P("Dr. Greifswald-Haunsberg   Schmidt-Dachau   Vogl-Erding<br/>"
                 "Vorsitzender Richter, LGDir.   Richter am LG   Richterin am LG", S_SMALL))
    els.append(PB())
    return els


def section_rechtliche_vertiefung():
    """Rechtliche Vertiefungsseiten — Kommentarmaterial und Rechtsprechungsanalyse"""
    els = []
    els.append(P("<b>RECHTLICHE VERTIEFUNG — § 656a BGB IM SYSTEM DES MAKLERRECHTS</b>", S_H1))
    els.append(P("Kanzlei-internes Memo Hagelbrand &amp; Trotzenburg — Az. HT-2023-0892", S_NORMAL))
    els.append(HR())
    els.append(SP(0.3))
    
    els.append(P("<b>I. Historische Entwicklung des Maklerrechts</b>", S_H2))
    els.append(P("Das Maklerrecht ist seit dem Inkrafttreten des BGB am 01. Januar 1900 in "
                 "§§ 652–655 BGB geregelt. Die Grundstruktur — Provisionsanspruch nur bei "
                 "wirksam zustandegekommenem Maklervertrag und kausalem Hauptvertrag — "
                 "ist bis heute unverändert geblieben.", S_JUSTIFY))
    els.append(SP(0.2))
    els.append(P("Mit dem Wohnimmobilienmakler-Gesetz vom 12. Juni 2020 (BGBl. I S. 1245) "
                 "wurde durch §§ 656a–656d BGB ein besonderes Schutzregime für den "
                 "Bereich der Wohnimmobilien eingeführt. Die wichtigsten Neuerungen:", S_JUSTIFY))
    for neuerung in [
        "§ 656a BGB: Textformerfordernis für Maklervertrag bei Wohnungen und Einfamilienhäusern",
        "§ 656b BGB: Keine Maklergebühren für Wohnraumvermittlung ohne schriftliche Aufforderung",
        "§ 656c BGB: Halbteilungsgrundsatz (gleiche Provision für Käufer und Verkäufer)",
        "§ 656d BGB: Verbot der einseitigen Provisionspflicht (max. 50% je Partei)",
    ]:
        els.append(P(f"&#8212; {neuerung}", S_JUSTIFY))
    els.append(SP(0.3))
    
    els.append(P("<b>II. § 656a BGB im Vergleich zu anderen Formvorschriften</b>", S_H2))
    vergleich = [
        ["Norm", "Formtyp", "Folge bei Verstoß", "Heilungsmöglichkeit"],
        ["§ 656a BGB", "Textform (§ 126b BGB)", "Nichtigkeit (§ 125 BGB)", "Keine"],
        ["§ 550 BGB", "Schriftform (§ 126 BGB)", "Kündigung auf Jahresfrist", "Erfüllung"],
        ["§ 492 BGB", "Schriftform", "Nichtigkeit", "Keine"],
        ["§ 766 BGB", "Schriftform", "Nichtigkeit", "Bürge kann leisten"],
        ["§ 311b BGB", "Notarielle Beurkundung", "Heilung durch Auflassung", "Ja (§ 311b Abs. 1 S. 2)"],
    ]
    t = Table(vergleich, colWidths=[90, 90, 130, 110])
    t.setStyle(TableStyle([
        ("FONTNAME",  (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME",  (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 9),
        ("BACKGROUND",(0,0), (-1,0), C_HEADER_BG),
        ("TEXTCOLOR", (0,0), (-1,0), white),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[white, C_LIGHT_BG]),
        ("BOX",       (0,0), (-1,-1), 0.5, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.2, C_BORDER),
        ("TOPPADDING",(0,0),(-1,-1),4),
        ("BOTTOMPADDING",(0,0),(-1,-1),4),
    ]))
    els.append(t)
    els.append(SP(0.3))
    
    els.append(P("<b>III. Textform vs. Schriftform: Praktische Unterschiede</b>", S_H2))
    els.append(P("Die Textform (§ 126b BGB) unterscheidet sich von der Schriftform (§ 126 BGB) "
                 "in mehreren wesentlichen Punkten:", S_JUSTIFY))
    unterschiede = [
        ["Kriterium", "Schriftform (§ 126 BGB)", "Textform (§ 126b BGB)"],
        ["Eigenhändige Unterschrift", "Erforderlich", "Nicht erforderlich"],
        ["Dauerhafter Datenträger", "Papier (i.d.R.)", "Auch E-Mail, PDF"],
        ["Personenangabe", "Durch Unterschrift", "Ausdrücklich im Text"],
        ["Abschluss der Erklärung", "Durch Unterschrift markiert", "Erkennbar durch Kontext"],
        ["Heilung durch Vollzug", "§ 766 BGB: teilweise", "Keine Heilungsregel in § 656a"],
        ["Typische Verwendung", "Bürgschaft, Mietvertrag", "Maklervertrag, Widerruf"],
    ]
    t2 = Table(unterschiede, colWidths=[130, 165, 155])
    t2.setStyle(TableStyle([
        ("FONTNAME",  (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME",  (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 9),
        ("BACKGROUND",(0,0), (-1,0), C_HEADER_BG),
        ("TEXTCOLOR", (0,0), (-1,0), white),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[white, C_LIGHT_BG]),
        ("BOX",       (0,0), (-1,-1), 0.5, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.2, C_BORDER),
        ("TOPPADDING",(0,0),(-1,-1),4),
        ("BOTTOMPADDING",(0,0),(-1,-1),4),
    ]))
    els.append(t2)
    els.append(PB())
    
    # Seite 2
    els.append(az_zeile())
    els.append(P("<b>IV. Bereicherungsrecht bei Formunwirksamkeit</b>", S_H2))
    els.append(P("Ist ein Vertrag wegen Formmangels nichtig (§ 125 BGB), bestehen die "
                 "bereicherungsrechtlichen Rückabwicklungsansprüche nach §§ 812 ff. BGB. "
                 "Im Maklerrecht gelten folgende Besonderheiten:", S_JUSTIFY))
    els.append(SP(0.2))
    for nr, titel, text in [
        ("1.", "Kein Kondiktionsausschluss nach § 817 S. 2 BGB",
         "§ 817 S. 2 BGB schließt den Kondiktionsanspruch aus, wenn dem Leistenden selbst "
         "ein Verstoß gegen ein gesetzliches Verbot oder die guten Sitten vorzuwerfen ist. "
         "Im Maklerrecht trifft dies jedoch nur die Maklerin — nicht den Maklerkunden — "
         "der die Formvorschrift verletzt hat. § 817 S. 2 BGB ist daher nicht anwendbar."),
        ("2.", "Kein Wertersatzanspruch nach § 818 Abs. 2 BGB",
         "Die Maklerin kann für ihre erbrachte Leistung keinen Wertersatz fordern, wenn der "
         "Schutzzweck der verletzten Norm (hier: § 656a BGB) gerade die Abwälzung der "
         "Provisionspflicht auf den Verbraucher verhindern soll. Dies hat der BGH in "
         "I ZR 197/22 (NJW 2023, 441, Rn. 41) ausdrücklich entschieden."),
        ("3.", "§ 819 BGB: Bösgläubigkeit gewerblicher Makler",
         "Gewerbliche Makler sind verpflichtet, die Formvorschriften ihres Tätigkeitsfeldes "
         "zu kennen. § 656a BGB gilt seit 23. Dezember 2020. Ein Makler, der drei Jahre nach "
         "Inkrafttreten der Norm Provisionsforderungen auf einen formunwirksamen Vertrag stützt, "
         "handelt bösgläubig im Sinne des § 819 BGB. Die Entreicherungseinrede des § 818 "
         "Abs. 3 BGB ist damit ausgeschlossen."),
    ]:
        els.append(P(f"<b>{nr} {titel}</b>", S_H2))
        els.append(P(text, S_JUSTIFY))
        els.append(SP(0.2))
    
    els.append(P("<b>V. Praxishinweis für Makler nach BGH I ZR 202/25</b>", S_H2))
    els.append(P("Das Urteil des BGH I ZR 202/25 hat für die Maklerpraxis folgende Konsequenzen:", S_JUSTIFY))
    for h in [
        "Der Maklervertrag muss als eigenständiges Dokument mit ausdrücklichem Vertragsangebot und -annahme in Textform geschlossen werden.",
        "Eine allgemeine Provisionshinweisklausel in der E-Mail-Signatur genügt nicht.",
        "Das Dokument muss mindestens enthalten: (1) Bezeichnung des Maklerobjekts, (2) fester Provisionssatz (nicht Höchstsatz), (3) Parteibezeichnungen, (4) Vertragsannahme-Erklärung.",
        "Branchenverbände (IVD) haben empfohlen, Muster-Maklerverträge zu verwenden, die diesen Anforderungen Rechnung tragen.",
        "Für bereits geschlossene Verträge gilt: Prüfung, ob die Textform eingehalten wurde. Bei Zweifeln: nachträgliche schriftliche Bestätigung einholen (anwaltliche Beratung empfohlen).",
    ]:
        els.append(P(f"&#8594; {h}", S_JUSTIFY))
    els.append(PB())
    
    # Seite 3 — Kostenrecht
    els.append(az_zeile())
    els.append(P("<b>VI. Kostenrecht und Streitwert im Maklerrecht</b>", S_H2))
    els.append(P("Der Streitwert in Maklerrechtsfällen nach §§ 656a ff. BGB bestimmt sich nach "
                 "der Hauptforderung (§ 23 Abs. 1 RVG, § 3 ZPO). Im vorliegenden Fall: "
                 "EUR 8.810,76. Für die RVG-Gebührentabelle (Anlage 2 zum RVG) ergibt sich "
                 "folgende Einordnung:", S_JUSTIFY))
    rvg_stufen = [
        ["Streitwert (von bis)", "Gebühr 1,0 (Basis)", "Gebühr 1,3 (Verfahren)", "Gebühr 1,2 (Termin)"],
        ["bis EUR 500", "EUR 49,00", "EUR 63,70", "EUR 58,80"],
        ["bis EUR 1.000", "EUR 88,00", "EUR 114,40", "EUR 105,60"],
        ["bis EUR 1.500", "EUR 127,00", "EUR 165,10", "EUR 152,40"],
        ["bis EUR 2.000", "EUR 166,00", "EUR 215,80", "EUR 199,20"],
        ["bis EUR 3.000", "EUR 222,00", "EUR 288,60", "EUR 266,40"],
        ["bis EUR 4.000", "EUR 278,00", "EUR 361,40", "EUR 333,60"],
        ["bis EUR 5.000", "EUR 334,00", "EUR 434,20", "EUR 400,80"],
        ["bis EUR 7.500", "EUR 414,00", "EUR 538,20", "EUR 496,80"],
        ["<b>bis EUR 10.000</b>", "<b>EUR 486,00</b>", "<b>EUR 631,80</b>", "<b>EUR 583,20</b>"],
        ["bis EUR 13.000", "EUR 558,00", "EUR 725,40", "EUR 669,60"],
    ]
    t3 = Table(rvg_stufen, colWidths=[130, 95, 100, 100])
    t3.setStyle(TableStyle([
        ("FONTNAME",  (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME",  (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 9),
        ("BACKGROUND",(0,0), (-1,0), C_HEADER_BG),
        ("TEXTCOLOR", (0,0), (-1,0), white),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[white, C_LIGHT_BG]),
        ("BACKGROUND",(0,10),(-1,10), C_YELLOW_HL),
        ("FONTNAME",  (0,10), (-1,10), "Helvetica-Bold"),
        ("BOX",       (0,0), (-1,-1), 0.5, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.2, C_BORDER),
        ("TOPPADDING",(0,0),(-1,-1),4),
        ("BOTTOMPADDING",(0,0),(-1,-1),4),
        ("ALIGN",     (1,0), (-1,-1), "RIGHT"),
    ]))
    els.append(t3)
    els.append(SP(0.2))
    els.append(P("<i>Maßgebliche Gebührenstufe: bis EUR 10.000 (markiert). "
                 "Die Kostenerstattung nach §§ 91 ff. ZPO umfasst die gesetzlichen "
                 "Gebühren der obsiegenden Partei bis zur RVG-Grundlage.</i>", S_SMALL))
    els.append(PB())
    return els


def section_vollstreckung_und_ausblick():
    """Vollstreckungsplanung und Ausblick"""
    els = []
    els.append(P("<b>VOLLSTRECKUNGSPLANUNG NACH RECHTSKRAFT — MEMO KANZLEI H/T</b>", S_H1))
    els.append(P("Intern — Az. HT-2023-0892 — Datum: 20. März 2026", S_NORMAL))
    els.append(HR())
    els.append(SP(0.3))
    
    els.append(P("<b>I. Stand nach BGH-Urteil</b>", S_H2))
    els.append(P("Mit Verkündung des BGH-Urteils I ZR 202/25 am 11. März 2026 ist das Urteil "
                 "des LG München I rechtskräftig geworden. Das LG-Urteil ist damit "
                 "Vollstreckungsgrundlage (§ 704 ZPO). Für die Vollstreckung benötigen wir "
                 "eine vollstreckbare Ausfertigung des Urteils (§ 724 ZPO).", S_JUSTIFY))
    els.append(SP(0.3))
    
    els.append(P("<b>II. Vollstreckbare Forderung (Stand 20. März 2026)</b>", S_H2))
    vf_data = [
        ["Position", "Betrag"],
        ["Hauptforderung (Provision-Rückzahlung)", "EUR 8.810,76"],
        ["Zinsen 5 % p.a. über Basiszins (09.08.2023 - 20.03.2026 = ca. 955 Tage)", "EUR 1.160,31"],
        ["Gerichtliche Kostenerstattung (LG + OLG + BGH, geschätzt)", "ca. EUR 6.500,00"],
        ["Gesamt vollstreckbarer Betrag", "ca. EUR 16.471,07"],
    ]
    t = Table(vf_data, colWidths=[340, 110])
    t.setStyle(TableStyle([
        ("FONTNAME",  (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME",  (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 9),
        ("FONTNAME",  (0,-1), (-1,-1), "Helvetica-Bold"),
        ("BACKGROUND",(0,-1),(-1,-1), C_YELLOW_HL),
        ("BOX",       (0,0), (-1,-1), 0.5, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.2, C_BORDER),
        ("TOPPADDING",(0,0),(-1,-1),4),
        ("BOTTOMPADDING",(0,0),(-1,-1),4),
        ("ALIGN",     (1,0), (1,-1), "RIGHT"),
    ]))
    els.append(t)
    els.append(SP(0.3))
    
    els.append(P("<b>III. Vollstreckungsschritte</b>", S_H2))
    for step, titel, body in [
        ("1.", "Vollstreckbare Ausfertigung beantragen",
         "Beantragung einer vollstreckbaren Ausfertigung des LG-Urteils beim Urkundsbeamten "
         "der Geschäftsstelle des LG München I (§ 724 ZPO). Frist: unverzüglich. Kosten: EUR 21,00."),
        ("2.", "Aufforderungsschreiben an Beklagte",
         "Schreiben an die Beklagte/ihre Anwältin mit Zahlungsaufforderung und Frist "
         "14 Tage. Falls die Beklagte freiwillig zahlt, entfallen die Vollstreckungskosten."),
        ("3.", "Kontenpfändung",
         "Falls keine freiwillige Zahlung: Pfändungs- und Überweisungsbeschluss (PfÜB) nach "
         "§§ 829, 835 ZPO gegen Bankkonto der Beklagten bei HypoVereinsbank München "
         "(IBAN aus Rechnung bekannt: DE49 7002 0270 0032 1788 00)."),
        ("4.", "Sachpfändung (hilfsweise)",
         "Falls Kontopfändung ergebnislos: Beauftragung des Gerichtsvollziehers zur "
         "Sachpfändung gemäß §§ 808 ff. ZPO. Vorab: Abforderung Vermögensauskunft (§ 802a ZPO)."),
    ]:
        els.append(P(f"<b>Schritt {step}</b> {titel}", S_H2))
        els.append(P(body, S_JUSTIFY))
        els.append(SP(0.2))
    
    els.append(SP(0.3))
    els.append(P("<b>IV. Ausblick: Bedeutung für zukünftige Mandate</b>", S_H2))
    els.append(P("Das Urteil BGH I ZR 202/25 wird voraussichtlich zu einer Welle ähnlicher "
                 "Klagen gegen Makler führen, die seit 2020 Provisionsforderungen auf "
                 "informatorische E-Mail-Signaturhinweise gestützt haben. Kanzlei H/T "
                 "ist bereits von drei weiteren Mandanten angesprochen worden. Wir prüfen "
                 "die Einrichtung eines standardisierten Verfahrens für diese Fälle.", S_JUSTIFY))

    # Extra page: Praxisfolgen
    els.append(az_zeile())
    els.append(P("<b>V. PRAXISFOLGEN DES BGH-URTEILS I ZR 202/25 AUF DEN MAKLERMARKT</b>", S_H1))
    els.append(HR())
    els.append(SP(0.2))
    els.append(P("Das Urteil BGH I ZR 202/25 vom 11. März 2026 schließt eine Lücke "
                 "in der Rechtsprechungsentwicklung. Es ist nunmehr höchstrichterlich klar, "
                 "dass ein allgemeiner Signaturhinweis mit Höchstprovisionssatz ohne "
                 "Objektbenennung den Anforderungen des § 656a BGB nicht genügt.", S_JUSTIFY))
    els.append(SP(0.3))
    folgen_data = [
        ["Konsequenz", "Maßnahme für Makler"],
        ["Standard-Signaturhinweise ungültig",
         "Eigenständige Textform-Erklärung mit Objektbenennung und festem Satz erforderlich"],
        ["Muster-Vertragsformulare nötig",
         "IVD und andere Verbände müssen Muster-Maklerverträge aktualisieren"],
        ["Digitale Onboarding-Prozesse",
         "PropTech und Portale müssen individualisierte Textform-Erklärungen implementieren"],
        ["Rückforderungsrisiken 2020-2026",
         "Makler mit Signatur-Praxis: Verjährung prüfen (§ 195 BGB, 3 Jahre ab Kenntnis)"],
        ["Folgelitigation",
         "Erhebliche Zahl ähnlicher Rückforderungsklagen ist zu erwarten"],
    ]
    t_folgen = Table(folgen_data, colWidths=[160, 290])
    t_folgen.setStyle(TableStyle([
        ("FONTNAME",  (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME",  (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 9),
        ("BACKGROUND",(0,0), (-1,0), C_HEADER_BG),
        ("TEXTCOLOR", (0,0), (-1,0), white),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[white, C_LIGHT_BG]),
        ("BOX",       (0,0), (-1,-1), 0.5, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.2, C_BORDER),
        ("TOPPADDING",(0,0),(-1,-1),4),
        ("BOTTOMPADDING",(0,0),(-1,-1),4),
    ]))
    els.append(t_folgen)
    els.append(SP(0.3))
    els.append(P("<b>Verjährungsübersicht für Makler-Rückforderungen:</b>", S_BOLD))
    vj_data = [
        ["Vertragsjahr", "Verjährungsbeginn (grds.)", "Ablauf", "Handlungsbedarf"],
        ["2020 (Q4)", "01.01.2021", "31.12.2023", "Abgelaufen"],
        ["2021", "01.01.2022", "31.12.2024", "Abgelaufen"],
        ["2022", "01.01.2023", "31.12.2025", "Abgelaufen (ca.)"],
        ["2023 (wie im Streitfall)", "01.01.2024", "31.12.2026", "Noch offen!"],
        ["2024", "01.01.2025", "31.12.2027", "Noch offen!"],
        ["2025-2026", "01.01.2026/2027", "2028/2029", "Noch offen!"],
    ]
    t_vj = Table(vj_data, colWidths=[80, 130, 80, 160])
    t_vj.setStyle(TableStyle([
        ("FONTNAME",  (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME",  (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 8),
        ("BACKGROUND",(0,0), (-1,0), C_HEADER_BG),
        ("TEXTCOLOR", (0,0), (-1,0), white),
        ("TEXTCOLOR", (0,4), (-1,5), C_MEMO_RED),
        ("FONTNAME",  (0,4), (-1,5), "Helvetica-Bold"),
        ("BOX",       (0,0), (-1,-1), 0.5, C_BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.2, C_BORDER),
        ("TOPPADDING",(0,0),(-1,-1),3),
        ("BOTTOMPADDING",(0,0),(-1,-1),3),
    ]))
    els.append(t_vj)
    els.append(SP(0.2))
    els.append(P("<i>Hinweis: Verjährungsbeginn bei Gutgläubigkeit des Gläubigers ab Kenntnis "
                 "oder grob fahrlässiger Unkenntnis (§ 199 Abs. 1 Nr. 2 BGB). "
                 "BGH I ZR 202/25 könnte als Wissensmerkmal für die Verjährung relevant sein.</i>", S_TINY))
    els.append(PB())
    els.append(PB())
    return els


# ─────────────────────────────────────────────────────────────────────────────
# MAIN — PDF GENERIEREN
# ─────────────────────────────────────────────────────────────────────────────
def main():
    pt = PageTemplate()

    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        leftMargin=2.5*cm, rightMargin=2.0*cm,
        topMargin=1.5*cm, bottomMargin=1.8*cm,
        title="Testakte: Haspelbeck-Türkenfeld ./. Bechtholdsmeier-Schongau e.K. — Az. LG München I 12 O 8842/23",
        author="Perplexity Computer",
        subject="Maklerrecht § 656a BGB — Textform — Testakte München",
    )

    story = []

    # Abschnitt 1: Aktendeckel
    story += section_aktendeckel()
    # Abschnitt 2: Inhaltsverzeichnis
    story += section_inhaltsverzeichnis()
    # Abschnitt 3: Mandatsannahme
    story += section_mandatsannahme()
    # Abschnitt 4: Klageschrift
    story += section_klageschrift()
    # Abschnitt 5: Klageerwiderung
    story += section_klageerwiderung()
    # Abschnitt 6: Replik
    story += section_replik()
    # Abschnitt 7: E-Mail-Kette
    story += section_email_kette()
    # Abschnitt 8: Notar-Kaufvertrag
    story += section_notar_kaufvertrag()
    # Abschnitt 9: Quittung
    story += section_quittung()
    # Abschnitt 10: Widerrufsbelehrung
    story += section_widerruf()
    # Abschnitt 11: Vergleich
    story += section_vergleich()
    # Zusatz: Erstinstanzlicher Verlauf
    story += section_erstinstanz_verlauf()
    # Zusatz: Ergänzende Korrespondenz LG-Instanz
    story += section_korrespondenz_zusatz()
    # Zusatz: Rechtliche Vertiefung
    story += section_rechtliche_vertiefung()
    # Zusatz: Vollstreckung
    story += section_vollstreckung_und_ausblick()
    # Gerichtliche Hinweise
    story += section_gerichtliches_hinweisschreiben()
    # Abschnitt 12: Berufungsschriftsatz
    story += section_berufung_schriftsatz()
    # Abschnitt 13: Berufungsbegründung
    story += section_berufungsbegruendung()
    # Abschnitt 14: Berufungserwiderung
    story += section_berufungserwiderung()
    # Abschnitt 15: Berufungsurteil
    story += section_berufungsurteil()
    # Abschnitt 16: Revisionsbegründung
    story += section_revision_begruendung()
    # Abschnitt 17: Revisionserwiderung
    story += section_revisionserwiderung()
    # Abschnitt 18: Stellungnahmen
    story += section_stellungnahmen()
    # Abschnitt 19: BGH-Urteil
    story += section_bgh_urteil()
    # Abschnitt 20: Mandantenmemo
    story += section_mandantenmemo()
    # Abschnitt 21: Handschriftliche Notizen
    story += section_handschriftliche_notizen()
    # Abschnitt 22: WhatsApp
    story += section_whatsapp()
    # Abschnitt 23: Kanzleirechnung
    story += section_kanzleirechnung()
    # Abschnitt 24: Aktenrandmemo
    story += section_aktenrandmemo()
    # Abschnitt 25: Anlagenverzeichnis
    story += section_anlagenverzeichnis()
    # Abschnitt 26: Stundenaufstellung
    story += section_stundenaufstellung()

    doc.build(
        story,
        onFirstPage=pt.draw_page,
        onLaterPages=pt.draw_page,
    )

    # Validierung
    import subprocess
    result = subprocess.run(
        ["python3", "-c",
         f"""
import sys
try:
    import pypdf
    r = pypdf.PdfReader('{OUTPUT_PDF}')
    pages = len(r.pages)
    print(f'Seiten: {{pages}}')
    sys.exit(0 if pages >= 70 else 1)
except Exception as e:
    print(f'pypdf nicht verfügbar: {{e}}')
    sys.exit(0)
"""],
        capture_output=True, text=True
    )
    print(result.stdout.strip() if result.stdout else "")

    # Dateigröße
    size = os.path.getsize(OUTPUT_PDF)
    print(f"PDF gespeichert: {OUTPUT_PDF}")
    print(f"Dateigröße: {size / 1024:.1f} KB")
    return OUTPUT_PDF

if __name__ == "__main__":
    main()
