#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_testakte.py
Testakte: Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen
Räumung wegen Zahlungsverzug – Schriftform § 568 BGB, qES § 126a BGB
Sachverhalt: BGH VIII ZR 159/23 vom 27. November 2024 (Bielefeld-Variante)
"""

import os
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
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── Output path ─────────────────────────────────────────────────────────────
OUTPUT_DIR = "/home/user/workspace/claude-fuer-deutsches-recht/testakten/schriftform-mietkuendigung-bielefeld-online-pferdedrescher"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "Testakte_Mietkuendigung_Bielefeld_Pferdedrescher.pdf")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Colours ──────────────────────────────────────────────────────────────────
C_BLACK       = colors.HexColor("#1A1A1A")
C_DARK_GREY   = colors.HexColor("#4A4A4A")
C_MID_GREY    = colors.HexColor("#888888")
C_LIGHT_GREY  = colors.HexColor("#E0E0E0")
C_WHITE       = colors.white
C_WA_GREEN    = colors.HexColor("#DCF8C6")   # WhatsApp sender bubble
C_WA_GREY     = colors.HexColor("#F0F0F0")   # WhatsApp receiver bubble
C_QES_BLUE    = colors.HexColor("#1565C0")
C_QES_BG      = colors.HexColor("#E3F2FD")
C_TRANSFER_BG = colors.HexColor("#F5F5F5")
C_TRANSFER_BD = colors.HexColor("#BDBDBD")
C_RED_LIGHT   = colors.HexColor("#FFEBEE")
C_RED         = colors.HexColor("#C62828")
C_ACCENT      = colors.HexColor("#01696F")
C_STAMP_BG    = colors.HexColor("#FFF9C4")
C_STAMP_BD    = colors.HexColor("#F57F17")

W, H = A4  # 595.27 x 841.89 points

# ── Style helpers ─────────────────────────────────────────────────────────────
ss = getSampleStyleSheet()

def S(name, **kw):
    """Create a ParagraphStyle derived from 'Normal'."""
    base = ss['Normal']
    return ParagraphStyle(name, parent=base, **kw)

# Core styles
BODY   = S('body',   fontName='Helvetica',      fontSize=9.5,  leading=14,  spaceAfter=4,  textColor=C_BLACK, alignment=TA_JUSTIFY)
BODY_L = S('bodyL',  fontName='Helvetica',      fontSize=9.5,  leading=14,  spaceAfter=4,  textColor=C_BLACK, alignment=TA_LEFT)
SMALL  = S('small',  fontName='Helvetica',      fontSize=8,    leading=11,  spaceAfter=2,  textColor=C_DARK_GREY)
MONO   = S('mono',   fontName='Courier',        fontSize=8.5,  leading=12,  spaceAfter=2,  textColor=C_BLACK)
ITALIC = S('italic', fontName='Helvetica-Oblique', fontSize=9, leading=13,  spaceAfter=3,  textColor=C_DARK_GREY)
BOLD   = S('bold',   fontName='Helvetica-Bold', fontSize=10,   leading=14,  spaceAfter=4,  textColor=C_BLACK)
H1     = S('h1',     fontName='Helvetica-Bold', fontSize=14,   leading=18,  spaceBefore=6, spaceAfter=6, textColor=C_ACCENT)
H2     = S('h2',     fontName='Helvetica-Bold', fontSize=11,   leading=15,  spaceBefore=4, spaceAfter=4, textColor=C_BLACK)
H3     = S('h3',     fontName='Helvetica-BoldOblique', fontSize=10, leading=14, spaceBefore=3, spaceAfter=3, textColor=C_DARK_GREY)
CENTER = S('center', fontName='Helvetica',      fontSize=9.5,  leading=14,  spaceAfter=4,  textColor=C_BLACK, alignment=TA_CENTER)
CENTER_BOLD = S('cbold', fontName='Helvetica-Bold', fontSize=11, leading=16, spaceAfter=6, textColor=C_BLACK, alignment=TA_CENTER)
HAND   = S('hand',   fontName='Helvetica-Oblique', fontSize=9.5, leading=14, spaceAfter=3,
           textColor=colors.HexColor("#1B5E20"), leftIndent=20)
CITE   = S('cite',   fontName='Times-Italic',   fontSize=9,    leading=13,  spaceAfter=3,
           leftIndent=20, rightIndent=20, textColor=C_DARK_GREY)
FOOTNOTE = S('fn',   fontName='Helvetica',      fontSize=7.5,  leading=10,  spaceAfter=1,  textColor=C_MID_GREY)

def p(text, style=BODY):
    return Paragraph(text, style)

def sp(h=6):
    return Spacer(1, h)

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=C_LIGHT_GREY, spaceAfter=4, spaceBefore=4)

def pb():
    return PageBreak()

# ── Custom Flowables ─────────────────────────────────────────────────────────

class BoxedPara(Flowable):
    """A paragraph inside a coloured box."""
    def __init__(self, text, bg=C_QES_BG, border=C_QES_BLUE, style=BODY,
                 padding=8, radius=3):
        super().__init__()
        self.text    = text
        self.bg      = bg
        self.border  = border
        self.style   = style
        self.padding = padding
        self.radius  = radius
        self._para   = Paragraph(text, style)

    def wrap(self, aw, ah):
        pw = aw - 2*self.padding
        w, h = self._para.wrap(pw, ah)
        self.width  = aw
        self.height = h + 2*self.padding
        return aw, self.height

    def draw(self):
        c = self.canv
        c.saveState()
        c.setFillColor(self.bg)
        c.setStrokeColor(self.border)
        c.setLineWidth(1)
        c.roundRect(0, 0, self.width, self.height, self.radius, fill=1, stroke=1)
        self._para.drawOn(c, self.padding, self.padding)
        c.restoreState()


class WaBubble(Flowable):
    """Simulate a WhatsApp chat bubble."""
    def __init__(self, sender, text, time_str, is_right=True, width=380):
        super().__init__()
        self.sender   = sender
        self.msg_text = text
        self.time_str = time_str
        self.is_right = is_right
        self._bw      = width
        bg = C_WA_GREEN if is_right else C_WA_GREY
        st = S(f'wabody_{id(self)}', fontName='Helvetica', fontSize=9,
               leading=13, textColor=C_BLACK)
        self._para = Paragraph(text, st)
        self._ts   = Paragraph(f'<font size="7" color="#888888">{time_str}{"  ✓✓" if is_right else ""}</font>',
                               S(f'wats_{id(self)}', fontName='Helvetica', fontSize=7,
                                 leading=10, alignment=TA_RIGHT))
        self.bg = bg

    def wrap(self, aw, ah):
        pw = self._bw - 20
        pw = min(pw, aw - 20)
        tw, th = self._para.wrap(pw, ah)
        tsw, tsh = self._ts.wrap(pw, ah)
        self.height = th + tsh + 16
        self.aw = aw
        return aw, self.height

    def draw(self):
        c = self.canv
        c.saveState()
        bw = min(self._bw, self.aw - 10)
        if self.is_right:
            bx = self.aw - bw - 5
        else:
            bx = 5
        c.setFillColor(self.bg)
        c.setStrokeColor(C_LIGHT_GREY)
        c.setLineWidth(0.5)
        c.roundRect(bx, 0, bw, self.height, 6, fill=1, stroke=1)
        pw = bw - 20
        self._para.drawOn(c, bx + 10, self.height - self._para.height - 8)
        self._ts.drawOn(c, bx + 10, 4)
        c.restoreState()


class StampBox(Flowable):
    """Grey stamp box (e.g., Transfervermerk § 298 Abs. 3 ZPO)."""
    def __init__(self, lines, bg=C_TRANSFER_BG, border=C_TRANSFER_BD, width=None):
        super().__init__()
        self.lines  = lines
        self.bg     = bg
        self.border = border
        self._w     = width

    def wrap(self, aw, ah):
        self.aw = aw
        bw = self._w or aw * 0.7
        self._bw = bw
        self.height = len(self.lines) * 13 + 20
        return aw, self.height

    def draw(self):
        c = self.canv
        c.saveState()
        bw = self._bw
        bx = (self.aw - bw) / 2
        c.setFillColor(self.bg)
        c.setStrokeColor(self.border)
        c.setLineWidth(1.5)
        c.setDash([4, 2], 0)
        c.rect(bx, 0, bw, self.height, fill=1, stroke=1)
        c.setDash([], 0)
        y = self.height - 16
        c.setFont('Helvetica-Bold', 8)
        c.setFillColor(C_DARK_GREY)
        for line in self.lines:
            c.drawString(bx + 10, y, line)
            y -= 13
        c.restoreState()


def qes_block(signer="Dr. Engelbert Ranftenschwedler-Bielenfels, Rechtsanwalt",
              cert="D-Trust Public-CA, Zertifikat-Nr. DE-2024-FIKT-88321",
              valid_until="12.07.2026",
              doc_hash="SHA-256: 3f2a...c9b1 [fiktiv]"):
    """Return flowables representing a qES signature block."""
    text = (f'<b>✦ Qualifizierte Elektronische Signatur (qES) — § 126a BGB i.V.m. eIDAS-VO Art. 26, 28</b><br/>'
            f'Unterzeichner: {signer}<br/>'
            f'Zertifizierungsstelle: {cert}<br/>'
            f'Gültig bis: {valid_until}<br/>'
            f'Dokument-Hash: {doc_hash}<br/>'
            f'<font size="7.5" color="#1565C0">Diese qualifizierte elektronische Signatur entspricht der Schriftform gemäß '
            f'§ 126 Abs. 3 BGB i.V.m. § 126a Abs. 1 BGB. Die Signatur ist nur im elektronischen Original prüfbar.</font>')
    return [BoxedPara(text, bg=C_QES_BG, border=C_QES_BLUE,
                      style=S('qes_inner', fontName='Helvetica', fontSize=8.5,
                              leading=13, textColor=C_QES_BLUE)),
            sp(4)]


def transfer_vermerk(date="09.03.2022", doc_desc="Klageschrift 09.03.2022",
                     sig_holder="Dr. Engelbert Ranftenschwedler-Bielenfels",
                     sig_time="09.03.2022 14:22:07 MEZ",
                     integrity="GÜLTIG (Prüfung durch Urkundsbeamtin der Geschäftsstelle)"):
    lines = [
        "TRANSFERVERMERK gemäß § 298 Abs. 3 ZPO",
        f"Dok.: {doc_desc}   Ausdruck erstellt: {date}",
        f"(1) Integrität d. elektronischen Dokuments: {integrity}",
        f"(2) Inhaber der qualifizierten elektronischen Signatur: {sig_holder}",
        f"(3) Zeitpunkt der Signatur: {sig_time}",
        "Amtsgericht Bielefeld – Urkundsbeamtin d. Geschäftsstelle: Frau Hartkemper",
        "HINWEIS: Dieser Ausdruck ersetzt NICHT die elektronische Originaldatei.",
        "Der Empfänger kann die qES am Ausdruck selbst NICHT prüfen (§ 126a BGB).",
    ]
    return [StampBox(lines, bg=C_TRANSFER_BG, border=C_TRANSFER_BD, width=460),
            sp(4)]


def email_block(sender, receiver, date, subject, body_lines, attachment=None):
    """Return flowables simulating an e-mail."""
    items = []
    items.append(BoxedPara(
        f'<b>Von:</b> {sender}<br/>'
        f'<b>An:</b> {receiver}<br/>'
        f'<b>Datum:</b> {date}<br/>'
        f'<b>Betreff:</b> {subject}',
        bg=colors.HexColor("#F8F8F8"), border=C_MID_GREY,
        style=S('email_hdr', fontName='Courier', fontSize=8.5, leading=13, textColor=C_BLACK)
    ))
    items.append(sp(3))
    for line in body_lines:
        items.append(Paragraph(line, MONO))
    if attachment:
        items.append(sp(4))
        items.append(BoxedPara(
            f'<b>📎 PDF-Anhang:</b> {attachment}',
            bg=colors.HexColor("#FFF3E0"), border=colors.HexColor("#E65100"),
            style=S('att_style', fontName='Helvetica', fontSize=8.5, leading=13, textColor=colors.HexColor("#BF360C"))
        ))
    items.append(sp(6))
    return items


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION BUILDERS
# ═══════════════════════════════════════════════════════════════════════════════

def section_header(num, title):
    return [
        sp(8),
        HRFlowable(width="100%", thickness=2, color=C_ACCENT),
        sp(3),
        p(f'<b>{num}  {title}</b>',
          S(f'sh_{num}', fontName='Helvetica-Bold', fontSize=12, leading=16,
            textColor=C_ACCENT)),
        HRFlowable(width="100%", thickness=0.5, color=C_LIGHT_GREY),
        sp(6),
    ]


# ── 1. AKTENDECKEL ────────────────────────────────────────────────────────────
def teil_01_aktendeckel():
    sparrenburg = (
        "       _\n"
        "      | |__\n"
        "   ___| |  |___\n"
        "  |   | |  |   |\n"
        "  | S | |  | P |\n"
        "  | P | |  | A |\n"
        "  | A |_|__|_R |\n"
        "  | R |        |\n"
        "  |_R_|________|   BIELEFELD\n"
        "     (Sparrenburg)  — existiert wirklich! —\n"
        "  ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n"
        "  [Bielefeld-Verschwörung™ offiziell widerlegt]\n"
    )
    elems = [
        sp(40),
        p('<b>AMTSGERICHT BIELEFELD</b>', S('cv1', fontName='Helvetica-Bold', fontSize=18, alignment=TA_CENTER, textColor=C_ACCENT)),
        sp(4),
        p('Abteilung 34 (Zivilsachen / Mietsachen)', S('cv2', fontName='Helvetica', fontSize=12, alignment=TA_CENTER)),
        sp(20),
        p('<b>AKTE</b>', S('cv3', fontName='Helvetica-Bold', fontSize=22, alignment=TA_CENTER, textColor=C_BLACK)),
        sp(8),
        p('Az.: <b>34 C 421/22</b>', S('cv4', fontName='Helvetica-Bold', fontSize=16, alignment=TA_CENTER, textColor=C_ACCENT)),
        sp(20),
        p('Klägerin (Vermieterin):', S('cvl', fontName='Helvetica-Bold', fontSize=11, alignment=TA_CENTER)),
        p('Frau <b>Hildegunde Pferdedrescher-Riesenstein</b>', S('cvv', fontName='Helvetica', fontSize=11, alignment=TA_CENTER)),
        p('Ottilienweg 23, 33647 Bielefeld-Brackwede', CENTER),
        sp(12),
        p('— gegen —', S('cvvs', fontName='Helvetica-Oblique', fontSize=11, alignment=TA_CENTER, textColor=C_MID_GREY)),
        sp(12),
        p('Beklagter (Mieter):', S('cvl2', fontName='Helvetica-Bold', fontSize=11, alignment=TA_CENTER)),
        p('Herrn <b>Götz-Sieghart Eberhart-Wolframshausen</b>', S('cvv2', fontName='Helvetica', fontSize=11, alignment=TA_CENTER)),
        p('Eckendorfer Straße 188, App. 4 OG, 33609 Bielefeld', CENTER),
        sp(20),
        p('<b>Streitgegenstand: Räumung und Herausgabe wegen Zahlungsverzugs</b>',
          S('cvst', fontName='Helvetica-Bold', fontSize=11, alignment=TA_CENTER, textColor=C_RED)),
        p('(§§ 543 Abs. 2 Nr. 3, 569 Abs. 3 BGB)', CENTER),
        sp(8),
        p('Streitwert: EUR 7.787,64 (Räumung) zzgl. Zahlungsanträge',
          S('cvsw', fontName='Helvetica', fontSize=10, alignment=TA_CENTER)),
        sp(30),
        BoxedPara(
            sparrenburg,
            bg=colors.HexColor("#F5F5DC"), border=C_MID_GREY,
            style=S('ascii_style', fontName='Courier', fontSize=8.5, leading=12, alignment=TA_CENTER)
        ),
        sp(20),
        p('⚠ FIKTIVE TESTAKTE — Alle Personen, Adressen und Verfahren sind erfunden ⚠',
          S('warn', fontName='Helvetica-Bold', fontSize=9, alignment=TA_CENTER, textColor=C_RED)),
        p('Rechtsgrundlage der Entscheidung: BGH VIII ZR 159/23 vom 27. November 2024',
          S('bghref', fontName='Helvetica', fontSize=9, alignment=TA_CENTER, textColor=C_MID_GREY)),
        pb(),
    ]
    return elems


# ── 2. INHALTSVERZEICHNIS ─────────────────────────────────────────────────────
def teil_02_inhaltsverzeichnis():
    entries = [
        ("1",  "Aktendeckel", "1"),
        ("2",  "Inhaltsverzeichnis", "2"),
        ("3",  "Mietvertrag-Auszug vom 03.04.2017 (Anlage K-MIET-1)", "3–6"),
        ("4",  "Mahnungs-Historie (tabellarisch) Frühjahr 2019 – Feb. 2022", "7–8"),
        ("5",  "WhatsApp-Verlauf 08.–10.02.2022 (Simulierte Screenshots)", "9–14"),
        ("6",  "Original-E-Mail 10.02.2022 mit PDF-Anhang (ohne qES)", "15–16"),
        ("7",  "Antwort-Mail Eberhart-Wolframshausen 11.02.2022", "17"),
        ("8",  "Anwaltsschreiben RA Ranftenschwedler-Bielenfels 15.02.2022", "18–20"),
        ("9",  "Klageschrift vom 09.03.2022 (mit qES)", "21–28"),
        ("10", "Hinweisbeschluss AG Bielefeld 11.04.2022 (Transfervermerk)", "29–30"),
        ("11", "Klageerwiderung Beklagter (eigenhändig) April 2022", "31–34"),
        ("12", "Replik Klägerin 13.05.2022 (mit qES, erneute Kündigung)", "35–38"),
        ("13", "Protokoll Mündliche Verhandlung AG Bielefeld 14.09.2022", "39–40"),
        ("14", "Urteil AG Bielefeld 34 C 421/22 vom 11.10.2022", "41–44"),
        ("15", "Berufungsschrift Klägerin 12.11.2022", "45–46"),
        ("16", "Mandatsannahme RA Hassenstein-Heepen", "47"),
        ("17", "Berufungsbegründung Klägerin (8 Seiten)", "48–55"),
        ("18", "Berufungserwiderung RA Hassenstein-Heepen", "56–58"),
        ("19", "Urteil LG Bielefeld 14 S 88/23 vom 20.06.2023", "59–62"),
        ("20", "Revisionsbegründung BGH VIII ZR 159/23 vom 28.08.2023", "63–65"),
        ("21", "Revisionserwiderung Mieter", "66"),
        ("22", "Stellungnahme zum Verhandlungstermin BGH 27.11.2024", "67"),
        ("23", "BGH-Urteil VIII ZR 159/23 — Tenor + Leitsätze", "68–70"),
        ("24", "Mandantenmemo RA Ranftenschwedler-Bielenfels 02.12.2024", "71–74"),
        ("25", "‚Online-Vermieter'-Memo — Digitale Kündigungsreform", "75–77"),
        ("26", "Handschriftliche Mieter-Notizen (kursiv)", "78"),
        ("27", "E-Mail-Kette Ranftenschwedler ↔ Pferdedrescher-Riesenstein", "79–82"),
        ("28", "Kostenfestsetzungsbeschluss-Entwurf", "83–84"),
        ("29", "Anlagenverzeichnis K-MIET-1 bis K-MIET-34", "85"),
        ("30", "Stundenaufstellung Ranftenschwedler Ostkamp Feb. 2022 – Nov. 2024", "86–88"),
    ]
    rows = [["Nr.", "Inhalt", "Seite(n)"]]
    for nr, content, pg in entries:
        rows.append([nr, content, pg])

    ts = TableStyle([
        ('BACKGROUND',  (0,0), (-1,0), C_ACCENT),
        ('TEXTCOLOR',   (0,0), (-1,0), C_WHITE),
        ('FONTNAME',    (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',    (0,0), (-1,0), 9),
        ('FONTNAME',    (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE',    (0,1), (-1,-1), 8.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, colors.HexColor("#F7F6F2")]),
        ('GRID',        (0,0), (-1,-1), 0.3, C_LIGHT_GREY),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING',(0,0), (-1,-1), 6),
        ('TOPPADDING',  (0,0), (-1,-1), 4),
        ('BOTTOMPADDING',(0,0), (-1,-1), 4),
        ('ALIGN',       (2,0), (2,-1), 'CENTER'),
    ])
    tbl = Table(rows, colWidths=[25, 370, 60])
    tbl.setStyle(ts)

    elems = section_header("Teil I", "INHALTSVERZEICHNIS")
    elems += [
        p('Akte Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen', BOLD),
        p('Az. AG Bielefeld 34 C 421/22 | LG Bielefeld 14 S 88/23 | BGH VIII ZR 159/23', SMALL),
        sp(8),
        tbl,
        sp(10),
        p('<i>Hinweis: Querverweise auf „Sonderband II" (Grundbuchauszüge, Mietpreisspiegel Bielefeld '
          '2017 ff., Kontobewegungen) nicht beigefügt. Vgl. Anlagenverzeichnis Rn. 29 unten.</i>', SMALL),
        pb(),
    ]
    return elems


# ── 3. MIETVERTRAG-AUSZUG ─────────────────────────────────────────────────────
def teil_03_mietvertrag():
    elems = section_header("Teil III", "MIETVERTRAG-AUSZUG (Anlage K-MIET-1)")
    elems += [
        p('<b>MIETVERTRAG</b> über Wohnräume', CENTER_BOLD),
        p('Amtliches Muster – Ergänzt durch individuelle Vereinbarungen', CENTER),
        sp(6), hr(), sp(4),
        p('<b>§ 1  Vertragsparteien</b>', H2),
        p('Vermieter: Frau Hildegunde Pferdedrescher-Riesenstein, Ottilienweg 23, 33647 Bielefeld '
          '(Ortsteil Brackwede), nachfolgend <i>Vermieterin</i>.', BODY),
        p('Mieter: Herr Götz-Sieghart Eberhart-Wolframshausen, geboren am 14. September 1982, '
          'wohnhaft zukünftig Eckendorfer Straße 188, App. 4 OG, 33609 Bielefeld, '
          'nachfolgend <i>Mieter</i>.', BODY),
        sp(4),
        p('<b>§ 2  Mietobjekt</b>', H2),
        p('Gegenstand des Mietvertrages ist die Wohnung im <b>4. Obergeschoss</b> des Hauses '
          '<b>Eckendorfer Straße 188, 33609 Bielefeld</b>, bestehend aus 3 Zimmern, Küche, '
          'Bad/WC, Flur, sowie einem Kellerabteil. Die Wohnfläche beträgt ca. 78 m² '
          '(gemessen nach WoFlV). Mitvermietet wird ein Stellplatz im Hinterhof.', BODY),
        sp(4),
        p('<b>§ 3  Mietzeit</b>', H2),
        p('Das Mietverhältnis beginnt am <b>01. April 2017</b> und wird auf unbestimmte Zeit '
          'geschlossen. Eine ordentliche Kündigung des Mietverhältnisses durch den Mieter '
          'ist mit einer Frist von 3 Monaten zulässig (§ 573c BGB). Bei ordentlicher '
          'Kündigung durch die Vermieterin gelten die gesetzlichen Fristen, sofern die '
          'Voraussetzungen des § 573 BGB vorliegen.', BODY),
        sp(4),
        p('<b>§ 4  Miete und Nebenkosten</b>', H2),
        p('Die monatliche Bruttomiete (Kaltmiete zzgl. Betriebskosten-Vorauszahlung) beträgt '
          '<b>EUR 648,97</b> (in Worten: Sechshundertachtundvierzig Euro und siebenundneunzig Cent). '
          'Sie ist jeweils bis zum 3. Werktag des Monats im Voraus auf das Konto der Vermieterin '
          'zu überweisen.', BODY),
        p('Konto: Sparkasse Bielefeld, IBAN: DE██ 4805 0161 ████ ████ ██ [geschwärzt], '
          'BIC: SPBIDE3BXXX. Verwendungszweck: „Miete Eckendorfer Str. 188 App. 4 OG".', SMALL),
        sp(4),
        p('<b>§ 5  Kaution</b>', H2),
        p('Der Mieter hat eine Sicherheitsleistung in Höhe von drei Kaltmonatsmieten, '
          'mithin EUR 1.665,00, auf ein gesondertes Kautionskonto zu zahlen. Die Zahlung '
          'ist in drei gleichen Raten von EUR 555,00 möglich, beginnend mit Mietbeginn.', BODY),
        sp(4),
        p('<b>§ 7  Schriftformklausel (wesentlich)</b>', H2),
        BoxedPara(
            '<b>§ 7 Schriftformklausel:</b> Änderungen und Ergänzungen dieses Vertrages, '
            'einschließlich dieser Klausel, bedürfen der Schriftform. '
            'Mündliche Nebenabreden sind unwirksam. '
            'Kündigungen des Mietverhältnisses bedürfen nach Maßgabe des § 568 Abs. 1 BGB '
            'der Schriftform; die schriftliche Kündigung kann nach § 126 Abs. 3 BGB durch '
            'die elektronische Form (§ 126a BGB) ersetzt werden, soweit das Gesetz nichts '
            'anderes bestimmt. <b>Eine Kündigung per E-Mail ohne qualifizierte elektronische '
            'Signatur (qES), per WhatsApp, SMS oder sonstigen Messenger wahrt die '
            'Schriftform des § 568 Abs. 1 BGB nicht.</b>',
            bg=C_RED_LIGHT, border=C_RED,
            style=S('mietv_box', fontName='Helvetica', fontSize=9, leading=13, textColor=C_BLACK)
        ),
        sp(6),
        p('<b>§ 10  Tierhaltung</b>', H2),
        p('Die Haltung von Kleintieren (Hamster, Vögel) ist gestattet. '
          'Größere Haustiere bedürfen der vorherigen schriftlichen Zustimmung der Vermieterin. '
          'Herr Eberhart-Wolframshausen hält unstreitig keine Haustiere.', BODY),
        sp(6), hr(), sp(4),
        p('Ort, Datum: Bielefeld, 03. April 2017', SMALL),
        sp(8),
        Table(
            [['Hildegunde Pferdedrescher-Riesenstein', '', 'Götz-Sieghart Eberhart-Wolframshausen'],
             ['(Vermieterin)', '', '(Mieter)']],
            colWidths=[200, 55, 200]
        ),
        sp(4),
        p('Anlage K-MIET-1 | Mietvertrag vom 03.04.2017 | Auszug Seiten 1–4 | Originalunterschriften '
          'auf dem Urkundsexemplar, s. Sonderband II', FOOTNOTE),
        pb(),
    ]
    return elems


# ── 4. MAHNUNGSHISTORIE ────────────────────────────────────────────────────────
def teil_04_mahnungshistorie():
    data = [
        ["Monat", "Soll (€)", "Ist-Zahlung (€)", "Saldo kum. (€)", "Mahnung"],
        ["Mrz 2019", "648,97", "530,00", "–118,97", "Mahn. 01"],
        ["Apr 2019", "648,97", "600,00", "–167,94", "Mahn. 02"],
        ["Mai 2019", "648,97", "648,97", "–167,94", "—"],
        ["Jun 2019", "648,97", "0,00", "–816,91", "Mahn. 03 (Anruf)"],
        ["Jul 2019", "648,97", "400,00", "–1.065,88", "Mahn. 04"],
        ["Aug 2019", "648,97", "648,97", "–1.065,88", "—"],
        ["Sep 2019", "648,97", "648,97", "–1.065,88", "—"],
        ["Okt 2019", "648,97", "900,00", "–814,85", "—"],
        ["Nov 2019", "648,97", "648,97", "–814,85", "—"],
        ["Dez 2019", "648,97", "500,00", "–963,82", "Mahn. 05 WhatsApp"],
        ["Jan 2020", "648,97", "648,97", "–963,82", "—"],
        ["Feb 2020", "648,97", "648,97", "–963,82", "—"],
        ["Mrz 2020", "648,97", "200,00", "–1.412,79", "Mahn. 06 E-Mail"],
        ["Apr 2020", "648,97", "648,97", "–1.412,79", "—"],
        ["Mai 2020", "648,97", "648,97", "–1.412,79", "—"],
        ["Jun 2020", "648,97", "700,00", "–1.361,76", "—"],
        ["Jul 2020", "648,97", "648,97", "–1.361,76", "—"],
        ["Aug 2020", "648,97", "648,97", "–1.361,76", "—"],
        ["Sep 2020", "648,97", "0,00", "–2.010,73", "Mahn. 07 (WA+E-Mail)"],
        ["Okt 2020", "648,97", "648,97", "–2.010,73", "—"],
        ["Nov 2020", "648,97", "648,97", "–2.010,73", "—"],
        ["Dez 2020", "648,97", "0,00", "–2.659,70", "Mahn. 08 einschreiben"],
        ["Jan 2021", "648,97", "648,97", "–2.659,70", "—"],
        ["Feb 2021", "648,97", "800,00", "–2.508,67", "Überzahlung beginnt"],
        ["Mrz 2021", "648,97", "800,00", "–2.357,64", "—"],
        ["Apr 2021", "648,97", "800,00", "–2.206,61", "—"],
        ["Mai 2021", "648,97", "800,00", "–2.055,58", "—"],
        ["Jun 2021", "648,97", "800,00", "–1.904,55", "—"],
        ["Jul 2021", "648,97", "800,00", "–1.753,52", "—"],
        ["Aug 2021", "648,97", "800,00", "–1.602,49", "—"],
        ["Sep 2021", "648,97", "800,00", "–1.451,46", "—"],
        ["Okt 2021", "648,97", "800,00", "–1.300,43", "—"],
        ["Nov 2021", "648,97", "800,00", "–1.149,40", "—"],
        ["Dez 2021", "648,97", "700,00", "–1.098,37", "—"],
        ["Jan 2022", "648,97", "700,00", "–1.047,34", "—"],
        ["Feb 2022", "648,97", "350,00", "–1.346,31", "→ Kündigung 10.02.2022"],
    ]
    ts = TableStyle([
        ('BACKGROUND',  (0,0), (-1,0), C_ACCENT),
        ('TEXTCOLOR',   (0,0), (-1,0), C_WHITE),
        ('FONTNAME',    (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',    (0,0), (-1,-1), 8),
        ('FONTNAME',    (0,1), (-1,-1), 'Helvetica'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, colors.HexColor("#F7F6F2")]),
        ('GRID',        (0,0), (-1,-1), 0.3, C_LIGHT_GREY),
        ('ALIGN',       (1,0), (3,-1), 'RIGHT'),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING',(0,0), (-1,-1), 5),
        ('TOPPADDING',  (0,0), (-1,-1), 3),
        ('BOTTOMPADDING',(0,0), (-1,-1), 3),
        # Highlight critical rows
        ('BACKGROUND',  (0,6),  (-1,6),  colors.HexColor("#FFCDD2")),
        ('BACKGROUND',  (0,20), (-1,20), colors.HexColor("#FFCDD2")),
        ('BACKGROUND',  (0,24), (-1,24), colors.HexColor("#C8E6C9")),
        ('BACKGROUND',  (0,-1), (-1,-1), colors.HexColor("#FFE0B2")),
    ])
    tbl = Table(data, colWidths=[55, 65, 75, 75, 175])
    tbl.setStyle(ts)

    elems = section_header("Teil IV", "MAHNUNGS-HISTORIE (Frühjahr 2019 – Februar 2022)")
    elems += [
        p('Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen — Az. AG Bielefeld 34 C 421/22', SMALL),
        sp(4),
        p('<b>Rückstandsentwicklung Eckendorfer Straße 188, App. 4 OG (Bruttomiete mtl. EUR 648,97)</b>', BOLD),
        sp(6),
        tbl,
        sp(6),
        p('<i>Anm.: Kumulierter Rückstand per 31.01.2021 = EUR 2.659,70 = ca. 4,1 Monatsmieten '
          '(Fälligkeit der außerordentlichen Kündigung nach § 543 Abs. 2 Nr. 3 lit. b BGB bereits '
          'überschritten). Ab Feb. 2021 kontinuierliche Überzahlungen; Rückstand bleibt jedoch über '
          '2 Monatsmieten (§ 569 Abs. 3 Nr. 1 BGB). Formelle Kündigung erst 10.02.2022 — '
          'Formunwirksamkeit strittig, s. folgend.</i>', ITALIC),
        sp(4),
        BoxedPara(
            '<b>Online-Mahn-Workflow der Vermieterin:</b> Frau Pferdedrescher-Riesenstein '
            'versandte sämtliche Mahnungen (Mahn. 01–08) per WhatsApp und/oder E-Mail. '
            'Kein einziges Mahnschreiben wurde als Einschreiben versandt – außer Mahn. 08 Dez. 2020, '
            'die nach Rücksprache mit RA Ranftenschwedler-Bielenfels postalisch per Einschreiben '
            'mit Rückschein übermittelt wurde. '
            'Herr Eberhart-Wolframshausen bestätigt Erhalt aller Mahnungen, bestreitet jedoch '
            'die kumulierten Beträge als überhöht (s. Klageerwiderung, Teil XI).',
            bg=colors.HexColor("#E8F5E9"), border=colors.HexColor("#388E3C"),
            style=S('mahn_box', fontName='Helvetica', fontSize=9, leading=13, textColor=C_BLACK)
        ),
        pb(),
    ]
    return elems


# ── 5. WHATSAPP-VERLAUF ────────────────────────────────────────────────────────
def teil_05_whatsapp():
    elems = section_header("Teil V", "WHATSAPP-VERLAUF 08.–10.02.2022 (Screenshot-Simulation)")
    elems += [
        p('<b>Konversation: Hildegunde Pferdedrescher-Riesenstein (rechts) '
          '↔ Götz-Sieghart Eberhart-Wolframshausen (links)</b>', BOLD),
        p('Handy-Nr. Pferdedrescher-Riesenstein: 0521/████ [geschwärzt] | '
          'Handy-Nr. Eberhart-Wolframshausen: 0521/████ [geschwärzt]', SMALL),
        sp(6),
        BoxedPara(
            '📱 WhatsApp Messenger — Chatprotokoll (Auszug)',
            bg=colors.HexColor("#075E54"), border=colors.HexColor("#128C7E"),
            style=S('wa_title', fontName='Helvetica-Bold', fontSize=10, leading=14,
                    textColor=C_WHITE, alignment=TA_CENTER)
        ),
        sp(8),
        # Day separator
        p('── Dienstag, 08. Februar 2022 ──', S('day_sep', fontName='Helvetica',
          fontSize=8, textColor=C_MID_GREY, alignment=TA_CENTER)),
        sp(6),
        WaBubble("Pferdedrescher-Riesenstein",
                 "Lieber Herr Eberhart-Wolframshausen,\n"
                 "ich wende mich erneut an Sie wegen der ausstehenden Mietrückstände.\n"
                 "Aktuell beläuft sich der Rückstand auf über EUR 1.047,34.\n"
                 "Bitte überweisen Sie bis Freitag, 11.02.2022.\n"
                 "Mit freundlichen Grüßen\nHildegunde Pferdedrescher-Riesenstein",
                 "Di, 08.02.2022 09:14", is_right=True),
        sp(4),
        WaBubble("Eberhart-Wolframshausen",
                 "Guten Tag Frau Pferdedrescher-Riesenstein. "
                 "Ich bin gerade auf Dienstreise (Hannover). "
                 "Ich werde zahlen sobald ich zurück bin. GsEW",
                 "Di, 08.02.2022 11:03", is_right=False),
        sp(4),
        WaBubble("Pferdedrescher-Riesenstein",
                 "Sehr geehrter Herr Eberhart-Wolframshausen, ich bitte Sie zum wiederholten Male "
                 "um die ausstehenden Beträge. Seit März 2019 zahlen Sie unregelmäßig. "
                 "Ich habe Ihnen über meinen Webshop bereits eine Zahlungsaufforderung "
                 "mit dem Kontaktformular geschickt. Haben Sie die erhalten?",
                 "Di, 08.02.2022 14:22", is_right=True),
        sp(4),
        WaBubble("Eberhart-Wolframshausen",
                 "Das Kontaktformular Ihres Webshops hat meine E-Mail als SPAM eingestuft. "
                 "Als IT-Admin sage ich Ihnen: Ihr SPF-Record ist falsch konfiguriert. "
                 "Ich zahle wenn ich kann.",
                 "Di, 08.02.2022 15:47", is_right=False),
        sp(6),
        p('── Mittwoch, 09. Februar 2022 ──', S('day_sep2', fontName='Helvetica',
          fontSize=8, textColor=C_MID_GREY, alignment=TA_CENTER)),
        sp(6),
        WaBubble("Pferdedrescher-Riesenstein",
                 "Herr Eberhart-Wolframshausen! Ich habe jetzt genug. "
                 "Ich werde rechtliche Schritte einleiten wenn nicht bis morgen gezahlt wird. "
                 "EUR 1.047,34 PLUS Februar 2022 = EUR 1.696,31 schulden Sie mir!",
                 "Mi, 09.02.2022 08:55", is_right=True),
        sp(4),
        WaBubble("Eberhart-Wolframshausen",
                 "...",
                 "Mi, 09.02.2022 09:02", is_right=False),
        sp(4),
        WaBubble("Pferdedrescher-Riesenstein",
                 "Ich habe meinen Anwalt eingeschaltet. Er rät mir zu einer fristlosen Kündigung. "
                 "Ich schicke Ihnen morgen das Kündigungsschreiben als PDF per E-Mail UND per WhatsApp.",
                 "Mi, 09.02.2022 21:12", is_right=True),
        sp(6),
        p('── Donnerstag, 10. Februar 2022 ──', S('day_sep3', fontName='Helvetica',
          fontSize=8, textColor=C_MID_GREY, alignment=TA_CENTER)),
        sp(6),
        WaBubble("Pferdedrescher-Riesenstein",
                 "🎙 SPRACHNACHRICHT (1:47 min) – 10.02.2022 09:31\n\n"
                 "[TRANSKRIPT automatisch erstellt]\n"
                 "„Herr Eberhart-Wolframshausen, hier spricht Hildegunde Pferdedrescher-"
                 "Riesenstein, Ihre Vermieterin. Ich erkläre hiermit ... äh ... die außerordentliche "
                 "fristlose Kündigung des Mietverhältnisses über die Wohnung Eckendorfer Straße "
                 "188 Appartement 4 Obergeschoss in Bielefeld. Grundlage ist § 543 Absatz 2 Nummer "
                 "3 BGB, Zahlungsverzug. Sie schulden mir über eintausend Euro. Ich schicke Ihnen "
                 "auch noch eine E-Mail mit dem PDF-Dokument. Ich bitte Sie, die Wohnung bis zum "
                 "31. März 2022 zu räumen. Vielen Dank.",
                 "Do, 10.02.2022 09:31", is_right=True),
        sp(4),
        p('<i>[Anm. Klägerin-Anwalt: Diese Sprachnachricht wahrt die Schriftform des § 568 Abs. 1 BGB '
          'nicht. Weder Schriftform (§ 126 BGB) noch elektronische Form (§ 126a BGB) sind erfüllt. '
          'Rechtlich wertlos als Kündigung.]</i>', ITALIC),
        sp(4),
        WaBubble("Pferdedrescher-Riesenstein",
                 "📎 Kündigung_EckStr188_App4_Feb2022.pdf (87 KB)\n"
                 "Bitte als Anlage — die E-Mail folgt separat",
                 "Do, 10.02.2022 09:34", is_right=True),
        sp(4),
        WaBubble("Eberhart-Wolframshausen",
                 "Ich habe die Sprachnachricht gehört. Ich werde das mit einem Anwalt besprechen.",
                 "Do, 10.02.2022 10:15", is_right=False),
        sp(4),
        WaBubble("Pferdedrescher-Riesenstein",
                 "Ich habe Ihnen auch eine E-Mail mit dem PDF geschickt. Bitte bestätigen Sie den Empfang.",
                 "Do, 10.02.2022 10:22", is_right=True),
        sp(4),
        WaBubble("Eberhart-Wolframshausen",
                 "E-Mail erhalten. Das PDF hat KEINE qualifizierte elektronische Signatur. "
                 "§ 568 BGB + § 126a BGB. Bitte informieren Sie sich. 🙄",
                 "Do, 10.02.2022 10:45", is_right=False),
        sp(4),
        p('<i>[Handschriftl. Notiz Eberhart-Wolframshausen am Aktenrand: '
          '„Sie hat mir das per WhatsApp geschickt!!! Unglaublich."]</i>', HAND),
        pb(),
    ]
    return elems


# ── 6. E-MAIL 10.02.2022 ──────────────────────────────────────────────────────
def teil_06_email():
    elems = section_header("Teil VI", "ORIGINAL-E-MAIL 10.02.2022 mit Kündigungs-PDF (ohne qES)")
    elems += email_block(
        sender="hildegunde.pferdedrescher-riesenstein@online-marketing-bielefeld.de",
        receiver="g.eberhart-wolframshausen@privat-mail.de",
        date="Donnerstag, 10. Februar 2022, 09:33 Uhr MEZ",
        subject="Fristlose Kündigung Ihres Mietverhältnisses — Eckendorfer Str. 188, App. 4 OG",
        body_lines=[
            "Sehr geehrter Herr Eberhart-Wolframshausen,",
            "",
            "hiermit erkläre ich gegenüber Ihnen die außerordentliche fristlose Kündigung",
            "des zwischen uns bestehenden Mietverhältnisses über die Wohnung",
            "Eckendorfer Straße 188, Appartement 4. Obergeschoss, 33609 Bielefeld,",
            "mit sofortiger Wirkung, hilfsweise zum nächstmöglichen Zeitpunkt.",
            "",
            "Kündigungsgrund: Zahlungsverzug gemäß § 543 Abs. 2 Nr. 3 lit. b BGB.",
            "Sie schulden mir per 10.02.2022 einen Betrag von EUR 1.696,31",
            "(Rückstand EUR 1.047,34 zzgl. Februarmiete EUR 648,97).",
            "",
            "Ich fordere Sie auf, die Wohnung bis spätestens 31. März 2022 vollständig",
            "geräumt und besenrein an mich herauszugeben.",
            "",
            "Das formelle Kündigungsschreiben (PDF) finden Sie als Anhang.",
            "",
            "Mit freundlichen Grüßen",
            "",
            "Hildegunde Pferdedrescher-Riesenstein",
            "Online-Marketing-Beratung & Webshop-Konzepte",
            "Ottilienweg 23, 33647 Bielefeld-Brackwede",
            "Tel.: 0521/██████ | www.online-marketing-bielefeld.de",
        ],
        attachment="Kuendigung_EckStr188_App4_Feb2022.pdf (87 KB) — OHNE qualifizierte elektronische Signatur!"
    )
    elems += [
        BoxedPara(
            '<b>PDF-ANHANG: Kündigungsschreiben (Volltext simuliert)</b><br/><br/>'
            'Bielefeld, den 10. Februar 2022<br/><br/>'
            'Hildegunde Pferdedrescher-Riesenstein<br/>'
            'Ottilienweg 23<br/>'
            '33647 Bielefeld-Brackwede<br/><br/>'
            'An: Götz-Sieghart Eberhart-Wolframshausen<br/>'
            'Eckendorfer Straße 188, App. 4 OG<br/>'
            '33609 Bielefeld<br/><br/>'
            '<b>Kündigung des Mietverhältnisses — außerordentlich fristlos</b><br/><br/>'
            'Sehr geehrter Herr Eberhart-Wolframshausen,<br/><br/>'
            'hiermit kündige ich das bestehende Mietverhältnis über die oben genannte '
            'Wohnung außerordentlich und fristlos gemäß §§ 543 Abs. 2 Nr. 3 lit. b, '
            '569 Abs. 3 BGB. Der Rückstand übersteigt zwei Monatsmieten erheblich.<br/><br/>'
            'Hildegunde Pferdedrescher-Riesenstein<br/>'
            '<i>[handschriftlich unterschrieben auf Papier, aber Versand ausschließlich als '
            'eingescannte PDF ohne qualifizierte elektronische Signatur (qES)]</i><br/><br/>'
            '<font color="#C62828"><b>⚠ KEINE qES — Formvorschrift § 126a BGB nicht erfüllt!</b></font>',
            bg=colors.HexColor("#FFF8E1"), border=colors.HexColor("#FF8F00"),
            style=S('pdf_body', fontName='Helvetica', fontSize=9, leading=14, textColor=C_BLACK)
        ),
        sp(4),
        p('<i>Rechtl. Würdigung: Eine Kündigung per E-Mail ohne qualifizierte elektronische Signatur '
          'wahrt die Schriftform des § 568 Abs. 1 BGB nicht (§ 126 Abs. 1 BGB). '
          'Eine eingescannte Unterschrift auf einer PDF genügt nicht (BGH NJW 2009, 2062; '
          'OLG Hamburg ZMR 2011, 194). '
          'Die E-Mail-Kündigung vom 10.02.2022 ist daher nach § 125 S. 1 BGB nichtig.</i>', ITALIC),
        pb(),
    ]
    return elems


# ── 7. ANTWORT-MAIL MIETER ────────────────────────────────────────────────────
def teil_07_antwortmail():
    elems = section_header("Teil VII", "ANTWORT-MAIL EBERHART-WOLFRAMSHAUSEN vom 11.02.2022")
    elems += email_block(
        sender="g.eberhart-wolframshausen@privat-mail.de",
        receiver="hildegunde.pferdedrescher-riesenstein@online-marketing-bielefeld.de",
        date="Freitag, 11. Februar 2022, 07:44 Uhr MEZ",
        subject="Re: Fristlose Kündigung Ihres Mietverhältnisses — Eckendorfer Str. 188, App. 4 OG",
        body_lines=[
            "Sehr geehrte Frau Pferdedrescher-Riesenstein,",
            "",
            "ich bestätige den Empfang Ihrer gestrigen Nachricht per WhatsApp",
            "(Sprachnachricht + Bilddatei) sowie Ihrer E-Mail mit PDF-Anhang.",
            "",
            "Als IT-Administrator erlaube ich mir den folgenden rechtlichen Hinweis,",
            "ohne dass ich damit auf die inhaltliche Richtigkeit Ihrer Forderungen",
            "eingehe:",
            "",
            "1. Eine Kündigung eines Wohnraummietverhältnisses bedarf gemäß",
            "   § 568 Abs. 1 BGB der Schriftform (§ 126 BGB).",
            "",
            "2. Schriftform bedeutet: eigenhändige Unterschrift auf Papier ODER",
            "   qualifizierte elektronische Signatur (qES) gem. § 126a BGB.",
            "",
            "3. Eine WhatsApp-Sprachnachricht genügt weder der Schriftform",
            "   noch der elektronischen Form.",
            "",
            "4. Ihre PDF-Datei trägt KEINE qualifizierte elektronische Signatur",
            "   (qES). Eine eingescannte Handunterschrift im PDF ist keine qES.",
            "   Ich habe die Datei im Adobe Acrobat Reader geprüft — keine",
            "   gültige Signatur vorhanden.",
            "",
            "5. Ihre Kündigung vom 10.02.2022 ist daher nach § 125 S. 1 BGB",
            "   nichtig (Formnichtigkeit).",
            "",
            "Mit freundlichen Grüßen",
            "",
            "Götz-Sieghart Eberhart-Wolframshausen",
            "IT-Administrator | Bielefeld",
            "",
            "P.S.: Ihr Webshop-Kontaktformular wirft übrigens einen SPF-Fehler.",
            "      Der Mailserver antwortet auf HELO mit Fehler 550. Bitte wenden",
            "      Sie sich an Ihren Hoster. Ich lehne jegliche Haftung für",
            "      verlorene Nachrichten über dieses System ab.",
        ]
    )
    elems += [
        p('<i>[Handschriftl. Notiz Eberhart-Wolframshausen am Aktenrand: '
          '„Echte Frechheit – als IT-Admin behandelt zu werden, als ob ich keine qES erkennen würde!"]</i>',
          HAND),
        p('<i>Anm. d. Red.: Herr Eberhart-Wolframshausen erweist sich schon hier als '
          'rechtlich informierter Gegner. Seine Einschätzung zur Formunwirksamkeit wird '
          'sich im Verlauf des Verfahrens als zutreffend erweisen.</i>', ITALIC),
        pb(),
    ]
    return elems


# ── 8. ANWALTSSCHREIBEN ────────────────────────────────────────────────────────
def teil_08_anwaltsschreiben():
    elems = section_header("Teil VIII", "ANWALTSSCHREIBEN RA RANFTENSCHWEDLER-BIELENFELS 15.02.2022")
    elems += [
        p('<b>Ranftenschwedler Ostkamp Rechtsanwälte mbB</b>',
          S('kanz_h', fontName='Helvetica-Bold', fontSize=12, textColor=C_ACCENT)),
        p('Niederwall 12 · 33602 Bielefeld · Tel. 0521/██████ · kanzlei@ranftenschwedler-ostkamp.de',
          S('kanz_s', fontName='Helvetica', fontSize=9, textColor=C_MID_GREY)),
        hr(), sp(6),
        p('Mandantin: Hildegunde Pferdedrescher-Riesenstein, Ottilienweg 23, 33647 Bielefeld', SMALL),
        p('<b>Vertraulich – Anwaltskorrespondenz</b>', S('vertr', fontName='Helvetica-Bold',
          fontSize=9, textColor=C_RED)),
        sp(4),
        p('<b>Unser Zeichen:</b> RO/2022/0312/PKT | <b>Datum:</b> Bielefeld, 15. Februar 2022', SMALL),
        sp(8),
        p('<b>RECHTLICHES MEMO</b>', H1),
        p('<b>Betreff: Formunwirksamkeit der Kündigung vom 10.02.2022; '
          'Handlungsempfehlungen</b>', BOLD),
        sp(6),
        p('Sehr geehrte Frau Pferdedrescher-Riesenstein,', BODY),
        sp(4),
        p('wie in unserem Telefonat vom gestrigen Tag besprochen, übermittle ich Ihnen '
          'nachfolgend meine Einschätzung zur rechtlichen Wirksamkeit der von Ihnen am '
          '10. Februar 2022 erklärten Kündigung.', BODY),
        sp(6),
        p('<b>I. Sachverhaltserfassung</b>', H2),
        p('Sie haben am 10.02.2022 gegenüber Herrn Eberhart-Wolframshausen die außerordentliche '
          'fristlose Kündigung in zwei Wegen erklärt:', BODY),
        p('(1) Per WhatsApp-Sprachnachricht (Voicemail, Länge ca. 1:47 Minuten).', BODY_L),
        p('(2) Per E-Mail mit einem PDF-Anhang, der das Kündigungsschreiben mit '
          'eingescannter handschriftlicher Unterschrift enthält, jedoch <b>ohne qualifizierte '
          'elektronische Signatur (qES)</b> i.S.v. § 126a BGB.', BODY_L),
        sp(6),
        p('<b>II. Rechtliche Würdigung der Formunwirksamkeit</b>', H2),
        p('<b>1. Schriftformerfordernis (§ 568 Abs. 1 BGB)</b>', H3),
        p('Die Kündigung eines Wohnraummietverhältnisses bedarf nach § 568 Abs. 1 BGB der '
          'Schriftform. Schriftform im Sinne des § 126 Abs. 1 BGB bedeutet, dass die '
          'Urkunde von dem Aussteller eigenhändig durch Namensunterschrift oder mittels '
          'notariell beglaubigten Handzeichens unterzeichnet werden muss — oder nach '
          '§ 126 Abs. 3 BGB durch die elektronische Form gem. § 126a BGB ersetzt werden.', BODY),
        p('<b>2. WhatsApp-Sprachnachricht</b>', H3),
        p('Eine mündliche Erklärung — auch wenn sie akustisch aufgezeichnet und übermittelt wird — '
          'wahrt die Schriftform des § 568 Abs. 1 BGB nicht. Voicemails sind keine Schrift '
          'und kein elektronisches Dokument mit Signatur i.S.v. § 126a BGB. '
          'Die Kündigung via WhatsApp-Sprachnachricht ist daher nach § 125 S. 1 BGB nichtig.', BODY),
        p('<b>3. E-Mail mit PDF ohne qES</b>', H3),
        p('Eine E-Mail ist zwar ein elektronisches Dokument, wahrt aber die Schriftform nur dann, '
          'wenn das elektronische Dokument mit einer <b>qualifizierten elektronischen Signatur (qES)</b> '
          'gemäß § 126a Abs. 1 BGB versehen ist. Eine eingescannte Handunterschrift im PDF '
          'genügt den Anforderungen der qES nicht (vgl. OLG Hamburg, Beschluss v. 18.11.2010, '
          '2 W 125/10; BGH NJW 2009, 2062). '
          'Mangels qES ist auch die E-Mail-Kündigung nach § 125 S. 1 BGB nichtig.', BODY),
        sp(4),
        p('<b>III. Handlungsempfehlungen (dringend)</b>', H2),
        BoxedPara(
            '<b>Empfehlung 1 – Sofortmaßnahme (sicherste Variante):</b><br/>'
            'Erklärung der Kündigung durch eigenhändige Unterschrift auf Papier, '
            'Zustellung als Einschreiben mit Rückschein oder besser durch Boten '
            '(Zeugen mitnehmen!). Diese klassische Schriftform gem. § 126 Abs. 1 BGB '
            'ist unwiderlegbar wirksam.<br/><br/>'
            '<b>Empfehlung 2 – Elektronische Form (qES):</b><br/>'
            'Soweit Sie zukünftig eine Kündigung elektronisch erklären möchten: '
            'Sie müssen ein Signaturzertifikat (z.B. von D-Trust, Bundesdruckerei) erwerben '
            'und das Kündigungs-PDF damit qualifiziert elektronisch signieren. '
            '<b>Das signierte PDF muss dem Mieter DIREKT im Original zugehen</b> '
            '(z.B. per E-Mail). NICHT per WhatsApp (technisch unsicher), NICHT über Dritte.',
            bg=colors.HexColor("#E8F5E9"), border=colors.HexColor("#2E7D32"),
            style=S('empf_s', fontName='Helvetica', fontSize=9, leading=14, textColor=C_BLACK)
        ),
        sp(4),
        BoxedPara(
            '<b>Warnung:</b> Sollte eine Kündigung zwar formgerecht abgegeben, '
            'aber nicht formgerecht ZUGEGANGEN sein, ist sie ebenfalls unwirksam. '
            'Gemäß § 130 Abs. 1 S. 1 BGB muss die empfangsbedürftige Willenserklärung '
            'dem Erklärungsgegner in der vorgeschriebenen Form zugehen. '
            'Dies gilt auch für die elektronische Form (§ 126a BGB). '
            'Nähere Ausführungen im Kontext eines etwaigen Prozesses s. unten.',
            bg=C_RED_LIGHT, border=C_RED,
            style=S('warn_s', fontName='Helvetica', fontSize=9, leading=14, textColor=C_BLACK)
        ),
        sp(6),
        p('Mit freundlichen kollegialen Grüßen', BODY),
        sp(16),
        p('Dr. Engelbert Ranftenschwedler-Bielenfels', BOLD),
        p('Rechtsanwalt | Fachanwalt für Miet- und Wohnungseigentumsrecht', SMALL),
        p('Ranftenschwedler Ostkamp Rechtsanwälte mbB', SMALL),
        pb(),
    ]
    return elems


# ── 9. KLAGESCHRIFT ────────────────────────────────────────────────────────────
def teil_09_klageschrift():
    elems = section_header("Teil IX", "KLAGESCHRIFT vom 09. März 2022 (mit qES)")
    elems += [
        p('AN DAS', CENTER),
        p('<b>AMTSGERICHT BIELEFELD</b>', CENTER_BOLD),
        p('— Zivilabteilung / Mietsachen —', CENTER),
        p('Niederwall 71, 33602 Bielefeld', CENTER),
        sp(8),
        p('Ranftenschwedler Ostkamp Rechtsanwälte mbB · Niederwall 12 · 33602 Bielefeld', SMALL),
        sp(4), hr(), sp(4),
        p('<b>KLAGESCHRIFT</b>', S('ks_h', fontName='Helvetica-Bold', fontSize=16,
          alignment=TA_CENTER, textColor=C_ACCENT)),
        p('(eingereicht als elektronisches Dokument über beA gem. § 130d ZPO,<br/>'
          'versehen mit qualifizierter elektronischer Signatur gem. § 126a BGB)', CENTER),
        sp(6),
        p('Datum: 09. März 2022', SMALL),
        sp(6),
        p('<b>In der Rechtssache</b>', BOLD),
        p('Hildegunde Pferdedrescher-Riesenstein, Ottilienweg 23, 33647 Bielefeld-Brackwede,',BODY),
        p('— <b>Klägerin</b> —', S('kl', fontName='Helvetica-Bold', fontSize=10, leftIndent=20)),
        p('Prozessbevollmächtigter: RA Dr. Engelbert Ranftenschwedler-Bielenfels, '
          'Niederwall 12, 33602 Bielefeld', BODY_L),
        sp(4),
        p('<b>gegen</b>', CENTER),
        sp(4),
        p('Götz-Sieghart Eberhart-Wolframshausen, Eckendorfer Straße 188, App. 4 OG, 33609 Bielefeld,', BODY),
        p('— <b>Beklagter</b> —', S('bk', fontName='Helvetica-Bold', fontSize=10, leftIndent=20)),
        sp(8),
        p('<b>wegen: Räumung und Herausgabe, Zahlung rückständiger Miete</b>', BOLD),
        p('Streitwert: EUR 7.787,64 (Räumungsklage gem. § 41 GKG = Jahresbruttomiete) '
          'zzgl. Zahlungsantrag EUR 1.696,31 = gesamt EUR 9.483,95', BODY),
        sp(8),
        p('<b>I. ANTRÄGE</b>', H2),
        p('Die Klägerin beantragt:', BODY),
        p('1. Den Beklagten zu verurteilen, die Wohnung im 4. Obergeschoss des Hauses '
          'Eckendorfer Straße 188, 33609 Bielefeld, bestehend aus 3 Zimmern, Küche, '
          'Bad/WC und Flur sowie Keller, vollständig geräumt an die Klägerin herauszugeben.',
          S('ant1', fontName='Helvetica', fontSize=9.5, leading=14, leftIndent=15)),
        p('2. Den Beklagten zu verurteilen, an die Klägerin EUR 1.696,31 nebst Zinsen '
          'in Höhe von 5 Prozentpunkten über dem jeweiligen Basiszinssatz seit '
          'Rechtshängigkeit zu zahlen.', S('ant2', fontName='Helvetica', fontSize=9.5,
          leading=14, leftIndent=15)),
        p('3. Den Beklagten zu verurteilen, für jeden Monat des Verzugs mit der Herausgabe '
          'eine Nutzungsentschädigung in Höhe von EUR 648,97 zu zahlen.', 
          S('ant3', fontName='Helvetica', fontSize=9.5, leading=14, leftIndent=15)),
        p('4. Hilfsweise (zu 1.): Die außerordentliche fristlose Kündigung wegen '
          'Zahlungsverzugs hiermit erneut zu erklären.', S('ant4', fontName='Helvetica',
          fontSize=9.5, leading=14, leftIndent=15)),
        sp(6),
        p('<b>II. SACHVERHALT</b>', H2),
        p('Die Klägerin ist Eigentümerin des Mehrfamilienhauses Eckendorfer Straße 188, '
          '33609 Bielefeld. Sie hat dem Beklagten mit Mietvertrag vom 03.04.2017 die '
          'Wohnung im 4. OG zu einer monatlichen Bruttomiete von EUR 648,97 vermietet.', BODY),
        p('Der Beklagte ist seit März 2019 chronisch zahlungssäumig. Der kumulierte Rückstand '
          'beläuft sich auf EUR 1.047,34 (Stand 31.01.2022) zzgl. der Februar-2022-Miete '
          'von EUR 648,97 = EUR 1.696,31.', BODY),
        p('<b>Vorangegangene Kündigungsversuche:</b> Die Klägerin hat am 10.02.2022 die '
          'außerordentliche fristlose Kündigung erklärt, und zwar per WhatsApp-Sprachnachricht '
          'sowie per E-Mail mit PDF-Anhang ohne qualifizierte elektronische Signatur. '
          'Auf ausdrücklichen Hinweis des Beklagten (E-Mail vom 11.02.2022) und nach '
          'Rechtsberatung durch ihren Bevollmächtigten ist der Klägerin bewusst, dass diese '
          'Kündigungserklärungen formunwirksam sein könnten.', BODY),
        p('<b>Erneute Kündigung im Schriftsatz:</b> Vorsorglich erklärt die Klägerin durch '
          'ihren Prozessbevollmächtigten nochmals ausdrücklich die außerordentliche fristlose '
          'Kündigung des Mietverhältnisses per diesem qualifiziert elektronisch signierten '
          'Schriftsatz. Die Erklärung soll dem Beklagten im Wege der gerichtlichen Zustellung '
          'zugehen.', BODY),
        sp(4),
    ] + qes_block() + [
        sp(4),
        p('<b>III. RECHTLICHE BEGRÜNDUNG</b>', H2),
        p('§§ 543 Abs. 2 Nr. 3 lit. b, 569 Abs. 3 Nr. 1, 568 Abs. 1 BGB, '
          '§ 126a Abs. 1 BGB, § 130 Abs. 1 S. 1 BGB, §§ 985, 546 BGB.', BODY),
        p('(1) Der Rückstand übersteigt mit EUR 1.696,31 zwei Monatsmieten (= EUR 1.297,94) '
          'erheblich, sodass die Voraussetzungen des § 543 Abs. 2 Nr. 3 lit. b BGB erfüllt sind.', BODY),
        p('(2) Die Kündigung per Schriftsatz wahrt die Schriftform des § 568 Abs. 1 BGB, da '
          'der Schriftsatz mit einer qualifizierten elektronischen Signatur (qES) gem. § 126a Abs. 1 '
          'BGB versehen ist. Die qES ersetzt nach § 126 Abs. 3 BGB die Schriftform, da § 568 BGB '
          'die elektronische Form nicht ausdrücklich ausschließt (anders als z.B. §§ 623, 766 BGB).', BODY),
        p('(3) Der formgerechte Zugang wird nach Zustellung des Schriftsatzes durch das Gericht '
          'gem. § 130 Abs. 1 S. 1 BGB i.V.m. §§ 166 ff. ZPO bewirkt.', BODY),
        sp(6),
        p('Bielefeld, den 09. März 2022', BODY),
        sp(12),
        p('Dr. Engelbert Ranftenschwedler-Bielenfels', BOLD),
        p('Rechtsanwalt', SMALL),
        sp(4),
        p('<i>Anlagenverzeichnis: K-MIET-1 (Mietvertrag), K-MIET-2 (Mietkontoauszug), '
          'K-MIET-3 (WhatsApp-Screenshot 10.02.2022), K-MIET-4 (E-Mail 10.02.2022), '
          'K-MIET-5 (Antwort-Mail 11.02.2022) — weitere Anlagen s. Anlagenverzeichnis Teil XXIX</i>',
          FOOTNOTE),
        pb(),
    ]
    return elems


# ── 10. HINWEISBESCHLUSS ───────────────────────────────────────────────────────
def teil_10_hinweisbeschluss():
    elems = section_header("Teil X", "HINWEISBESCHLUSS AG BIELEFELD 11.04.2022")
    elems += [
        p('<b>AMTSGERICHT BIELEFELD</b>', CENTER_BOLD),
        p('— Abteilung 34 —', CENTER),
        sp(6),
        p('<b>BESCHLUSS</b>', S('hb', fontName='Helvetica-Bold', fontSize=14,
          alignment=TA_CENTER, textColor=C_ACCENT)),
        sp(4),
        p('Az.: 34 C 421/22', CENTER),
        p('Bielefeld, 11. April 2022', CENTER),
        sp(8),
        p('In der Rechtssache Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen '
          'gibt das Gericht folgende <b>Hinweise</b>:', BODY),
        sp(4),
        p('<b>1. Zustellungsmodus der Klageschrift:</b>', BOLD),
        p('Die Klageschrift vom 09.03.2022 wurde als elektronisches Dokument über beA '
          'eingereicht und trägt eine qualifizierte elektronische Signatur (qES) '
          'i.S.v. § 126a Abs. 1 BGB.', BODY),
        p('Da der Beklagte nicht anwaltlich vertreten ist und keine Zustimmung zur '
          'elektronischen Übermittlung nach § 173 Abs. 4 S. 1 ZPO erteilt hat, wurde '
          'die Klageschrift durch die Geschäftsstelle ausgedruckt und dem Beklagten '
          'postalisch zugestellt.', BODY),
    ] + transfer_vermerk(
        date="11.04.2022",
        doc_desc="Klageschrift Ranftenschwedler-Bielenfels v. 09.03.2022, Az. 34 C 421/22",
        sig_holder="Dr. Engelbert Ranftenschwedler-Bielenfels, Niederwall 12, 33602 Bielefeld",
        sig_time="09.03.2022 14:22:07 MEZ",
        integrity="GÜLTIG — Integrität bestätigt, Prüfung durch Geschäftsstelle"
    ) + [
        p('<b>2. Rechtlicher Hinweis zur Wirksamkeit der Kündigung im Schriftsatz:</b>', BOLD),
        p('Das Gericht weist vorsorglich darauf hin, dass die Wirksamkeit einer '
          'in einem qualifiziert elektronisch signierten Schriftsatz enthaltenen Kündigung '
          'davon abhängen dürfte, ob dem Beklagten die Kündigung in der vorgeschriebenen Form '
          'zugegangen ist. Der Ausdruck des Schriftsatzes mit Transfervermerk gem. § 298 Abs. 3 ZPO '
          'könnte — nach der in der Instanzrechtsprechung nicht einheitlich beurteilten Rechtslage — '
          'den formgerechten Zugang einer qES-Erklärung beim Erklärungsgegner nicht bewirken, '
          'wenn der Empfänger die Signatur an dem Ausdruck nicht prüfen kann.', BODY),
        BoxedPara(
            '⚠ <b>Hinweis des Gerichts:</b> Diese Rechtsfrage (Zugang der qES-Willenserklärung '
            'über Ausdruck mit Transfervermerk § 298 Abs. 3 ZPO) ist höchstrichterlich ungeklärt. '
            'Eine Vorlage an den BGH wird von der Kammer erwogen. '
            'Die Klägerin wird gebeten, zur Wirksamkeit der Zustellung im Schriftsatz '
            'ergänzend vorzutragen.',
            bg=C_STAMP_BG, border=C_STAMP_BD,
            style=S('hint_s', fontName='Helvetica', fontSize=9, leading=13, textColor=C_BLACK)
        ),
        sp(4),
        p('Richter am Amtsgericht Hartmut Klüver-Schildberg', SMALL),
        p('Amtsgericht Bielefeld, Abt. 34', SMALL),
        pb(),
    ]
    return elems


# ── 11. KLAGEERWIDERUNG ────────────────────────────────────────────────────────
def teil_11_klageerwiderung():
    elems = section_header("Teil XI", "KLAGEERWIDERUNG DES BEKLAGTEN (eigenhändig, April 2022)")
    elems += [
        BoxedPara(
            '📝 Original handschriftlich, hier als maschinenlesbare Transkription '
            '(mit Tippfehlern aus dem Original übernommen)',
            bg=C_LIGHT_GREY, border=C_MID_GREY,
            style=S('hw_note', fontName='Helvetica-Oblique', fontSize=8.5, leading=12, textColor=C_DARK_GREY)
        ),
        sp(6),
        p('Götz-Sieghart Eberhart-Wolframshausen', BOLD),
        p('Eckendorfer Straße 188, App. 4 OG, 33609 Bielefeld', BODY_L),
        sp(4),
        p('An das Amtsgericht Bielefeld, Abt. 34', BODY),
        p('Niederwall 71, 33602 Bielefeld', BODY),
        sp(6),
        p('Bielefeld, 15. April 2022 [Eingangsstempel AG Bielefeld 18.04.2022]', SMALL),
        sp(6),
        p('<b>Klageerwiderung</b>', H1),
        p('in Sachen Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen, '
          'Az. 34 C 421/22', BOLD),
        sp(6),
        p('Sehr geertes Gericht,', BODY),  # Intentional typo
        p('ich erhebe hiermit Gegenvorstellungen [sic – gemeint: Einwendungen] '
          'gegen die Klage. Ich bin kein Anwalt aber ich kenne meine Rechte.', BODY),
        sp(4),
        p('<b>1. Zur Forderungshöhe</b>', H2),
        p('Die Klägerin berechnet den Rückstand falsch. Ich habe im Zeitraum Februar 2021 '
          'bis Januar 2022 jeweils EUR 800,00 pro Monat gezahlt, obwohl die Miete nur '
          'EUR 648,97 beträgt. Das sind Überzahlungen von EUR 151,03 pro Monat x 12 Monate '
          '= EUR 1.812,36. Diese Überzahlungen muessen [sic] verrechnet werden!', BODY),
        p('[Anm. d. Klägerin: Die Überzahlungen wurden auf den alten Rückstand verrechnet. '
          'S. Anlage K-MIET-2 (Kontoauszug). Per 31.01.2022 verbleiben EUR 1.047,34 Rückstand.]',
          ITALIC),
        sp(4),
        p('<b>2. Zur Kündigung</b>', H2),
        p('Die Kündigung vom 10.02.2022 ist unwirksam. Sie wurde per WhatsApp-Sprachnachricht '
          'und per E-Mail ohne Signatur verschickt. Das genügt § 568 BGB nicht. '
          'Siehe auch meine E-Mail vom 11.02.2022 an die Klägerin.', BODY),
        p('Die Kündigung in der Klageschrift: Ich habe die Klageschrift als Papierausdruck '
          'erhalten. Dieses Papier hat keine elektron. Signatur. Ein Papier ist kein '
          'elektronisches Dokument. Der Transfervermerk ist kein Ersatz für die qES. '
          '§ 126a BGB sagt: das ELEKTRONISCHE Dokument muss beim Empfaenger [sic] '
          'ankommen. Nicht ein Ausdruck.', BODY),
        p('Ich verweise auf § 130 BGB: Zugang muss in der vorgeschriebenen Form erfolgen.', BODY),
        p('<i>[handschriftl. Randnotiz: „Ich habe das im Internet recherchiert. '
          'Es gibt Urteile dazu – OLG Frankfurt, LG Berlin. Der BGH hat das noch nicht '
          'entschieden aber ich WETTE er würde mir Recht geben!!!"]</i>', HAND),
        sp(4),
        p('<b>3. Zum Zahlungsverzug</b>', H2),
        p('§ 543 Absatz 2 Nummer 3 BGB erfordert eine wirksame Abmahnung [sic – '
          'gemeint wohl: Mahnung im Sinne des § 569 Abs. 3 Nr. 2 BGB] oder '
          'Zwei-Monats-Rückstand. Letzters [sic] bestreite ich wegen falscher '
          'Rückstandsberechnung (s.o.).', BODY),
        p('[Anm. d. Red.: § 543 Abs. 2 Nr. 3 BGB erfordert keine Abmahnung, '
          'nur Rückstandshöhe. Herrn Eberhart-Wolframshausens Rechtsargument ist '
          'insoweit unzutreffend. Im Ergebnis wird er dennoch obsiegen — '
          'aus Formgründen.]', ITALIC),
        sp(4),
        p('<b>4. Antrag</b>', H2),
        p('Ich beantrage, die Klage abzuweisen. Ich bitte das Gericht, mich rechtzeitig '
          'zu informieren wenn ein Termin angesetzt wird. Ich kann meinen Urlaub '
          'danach richten.', BODY),
        sp(6),
        p('Mit freundlichen Grüßen', BODY),
        sp(12),
        p('Götz-Sieghart Eberhart-Wolframshausen', BOLD),
        p('[Unterschrift handschriftlich]', ITALIC),
        sp(6),
        p('<i>[Randnotiz am unteren Seitenrand, Bleistift: '
          '„Muss ich wirklich selbst klagen? Vielleicht einen Anwalt nehmen für Berufung."]</i>',
          HAND),
        pb(),
    ]
    return elems


# ── 12. REPLIK MIT ERNEUTER KÜNDIGUNG ─────────────────────────────────────────
def teil_12_replik():
    elems = section_header("Teil XII", "REPLIK KLÄGERIN 13.05.2022 — Erneute Kündigung (qES)")
    elems += [
        p('<b>Ranftenschwedler Ostkamp Rechtsanwälte mbB</b>',
          S('r_h', fontName='Helvetica-Bold', fontSize=11, textColor=C_ACCENT)),
        p('SCHRIFTSATZ AN DAS AMTSGERICHT BIELEFELD — Abteilung 34', BOLD),
        p('Az.: 34 C 421/22 | Datum: 13. Mai 2022', SMALL),
        p('Eingereicht als elektronisches Dokument (beA, § 130d ZPO) mit qES', SMALL),
        sp(6), hr(), sp(4),
        p('In der Rechtssache Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen '
          'erwidert die Klägerin auf die Klageerwiderung des Beklagten vom 15.04.2022 '
          'wie folgt:', BODY),
        sp(4),
        p('<b>I. Zur Forderungshöhe (Rückstandsberechnung)</b>', H2),
        p('Der Beklagte verkennt, dass die Überzahlungen seit Februar 2021 zwar anerkannt '
          'werden, jedoch nur auf den bereits bestehenden Rückstand anzurechnen sind. '
          'Die tabellarische Aufstellung (Anlage K-MIET-2) belegt einen verbleibenden '
          'Rückstand von EUR 1.696,31 per 10.02.2022.', BODY),
        sp(4),
        p('<b>II. Zur Wirksamkeit der Kündigung</b>', H2),
        p('2.1 Die Kündigung im Schriftsatz vom 09.03.2022 wurde dem Beklagten mit '
          'Transfervermerk zugestellt. Zwar räumt die Klägerin ein, dass die Frage '
          'des formwirksamen Zugangs einer qES-Erklärung über Ausdruck mit '
          'Transfervermerk streitig ist. Die Klägerin ist jedoch der Ansicht, dass '
          'der Transfervermerk gem. § 298 Abs. 3 ZPO die Identitäts- und '
          'Echtheitsfunktion des § 126a BGB hinreichend dokumentiert.', BODY),
        p('2.2 Vorsorglich erklärt die Klägerin durch diesen Schriftsatz '
          '<b>erneut die außerordentliche fristlose Kündigung</b> sowie hilfsweise '
          'die ordentliche Kündigung des Mietverhältnisses:', BODY),
        BoxedPara(
            '<b>KÜNDIGUNGSERKLÄRUNG (§§ 543 Abs. 2 Nr. 3 lit. b, 573 Abs. 2 Nr. 1 BGB)</b><br/><br/>'
            'Die Klägerin, vertreten durch Rechtsanwalt Dr. Engelbert Ranftenschwedler-Bielenfels, '
            'erklärt hiermit gegenüber dem Beklagten Götz-Sieghart Eberhart-Wolframshausen:<br/><br/>'
            '– die außerordentliche fristlose Kündigung des Mietverhältnisses über '
            'Eckendorfer Straße 188, App. 4 OG, 33609 Bielefeld, wegen Zahlungsverzugs '
            'i.S.v. § 543 Abs. 2 Nr. 3 lit. b BGB, sowie hilfsweise<br/>'
            '– die ordentliche Kündigung des Mietverhältnisses gem. § 573 Abs. 2 Nr. 1 BGB '
            'wegen erheblicher Vertragsverletzung (nachhaltige Zahlungsunpünktlichkeit).<br/><br/>'
            'Diese Kündigung ist im vorliegenden qualifiziert elektronisch signierten '
            'Schriftsatz enthalten. Die Klägerin erwartet den formwirksamen Zugang '
            'beim Beklagten durch gerichtliche Zustellung.',
            bg=C_RED_LIGHT, border=C_RED,
            style=S('kuend_s', fontName='Helvetica', fontSize=9, leading=14, textColor=C_BLACK)
        ),
        sp(4),
    ] + qes_block() + transfer_vermerk(
        date="17.05.2022",
        doc_desc="Replik/Schriftsatz RA Ranftenschwedler-Bielenfels v. 13.05.2022, Az. 34 C 421/22",
        sig_holder="Dr. Engelbert Ranftenschwedler-Bielenfels, Niederwall 12, 33602 Bielefeld",
        sig_time="13.05.2022 11:07:44 MEZ",
        integrity="GÜLTIG — Prüfung Urkundsbeamtin Hartkemper, 17.05.2022"
    ) + [
        p('<i>Anm. d. Red.: Auch dieser Schriftsatz wird dem Beklagten (noch ohne Anwalt) '
          'als Papierausdruck zugestellt. Die qES ist am Ausdruck nicht prüfbar. '
          'Die Kündigung wird deshalb wiederum formunwirksam zugegangen sein — '
          'wie der BGH acht Revisionen später bestätigt.</i>', ITALIC),
        pb(),
    ]
    return elems


# ── 13. PROTOKOLL MÜNDL. VERHANDLUNG ──────────────────────────────────────────
def teil_13_protokoll():
    elems = section_header("Teil XIII", "PROTOKOLL MÜNDLICHE VERHANDLUNG AG BIELEFELD 14.09.2022")
    elems += [
        p('<b>AMTSGERICHT BIELEFELD</b>', CENTER_BOLD),
        p('Sitzungsprotokoll — § 159 ZPO', CENTER),
        sp(6),
        Table([
            ['Aktenzeichen:', '34 C 421/22'],
            ['Sitzungstag:', 'Mittwoch, 14. September 2022, 09:30 Uhr'],
            ['Saal:', '2.14 (EG), AG Bielefeld, Niederwall 71, 33602 Bielefeld'],
            ['Vorsitz:', 'Richter am Amtsgericht Klüver-Schildberg'],
            ['Protokoll:', 'Urkundsbeamtin der Geschäftsstelle Hartkemper'],
        ], colWidths=[120, 340]),
        sp(6), hr(), sp(4),
        p('<b>Erschienen:</b>', BOLD),
        p('Für die Klägerin: RA Dr. Ranftenschwedler-Bielenfels, legitimiert durch Vollmacht K-MIET-33.', BODY),
        p('Beklagter: Herr Götz-Sieghart Eberhart-Wolframshausen, persönlich. '
          'Ohne anwaltliche Vertretung.', BODY),
        sp(6), hr(), sp(4),
        p('<b>Verhandlungsverlauf (Auszug):</b>', BOLD),
        p('Der <b>Vorsitzende</b> eröffnet die Sitzung und stellt die Anwesenheit fest. '
          'Er weist die Parteien auf die Sach- und Rechtslage hin:', BODY),
        p('[RiAG Klüver-Schildberg]: „Die Kündigung vom 10.02.2022 per WhatsApp '
          'und E-Mail ohne qES wahrt die Schriftform des § 568 BGB nicht. '
          'Darin sind wir uns einig. Die entscheidende Frage ist, ob die '
          'Kündigungen in den Schriftsätzen vom 09.03.2022 und 13.05.2022 '
          'dem Beklagten formwirksam zugegangen sind."', CITE),
        p('[RA Ranftenschwedler-Bielenfels]: „Der Transfervermerk gem. § 298 Abs. 3 ZPO '
          'dokumentiert die Echtheit der Signatur hinreichend. § 130 BGB verlangt '
          'nicht, dass der Empfänger die Prüfung selbst vornimmt, sondern nur dass '
          'die formgerechte Erklärung in seinen Machtbereich gelangt."', CITE),
        p('[Beklagter Eberhart-Wolframshausen]: „Mit Verlaub, das ist falsch. '
          'Ich habe nur ein Stück Papier bekommen. Das Papier hat keine elektronische Signatur. '
          'Punkt. § 126a BGB ist eindeutig: das ELEKTRONISCHE Dokument muss zu mir kommen. '
          'Ich bin IT-Administrator und weiß, was eine qES ist — '
          'der Ausdruck mit Vermerk ist keiner."', CITE),
        p('<i>[Handschriftl. Notiz am Rand: „Sie haben mir sogar recht gegeben im Saal!!! '
          'Obwohl er sich nicht traute das offen zu sagen."]</i>', HAND),
        p('[RiAG Klüver-Schildberg]: „Das Gericht behält sich vor, '
          'diese Rechtsfrage im Urteil zu klären. Die Revision wird voraussichtlich '
          'zuzulassen sein. Ich schlage einen Vergleich vor: '
          'Beklagter zahlt EUR 800,00 Rückstand und die Klägerin räumt '
          'das Mietverhältnis zunächst auf. Keine Einigung?"', CITE),
        p('[Beide Parteien]: „Kein Vergleich."', BODY),
        sp(6), hr(), sp(4),
        p('<b>Das Gericht verkündet:</b> Urteil ergeht am <b>11. Oktober 2022</b>.', BOLD),
        sp(4),
        p('Schluss der Sitzung: 10:12 Uhr', SMALL),
        sp(8),
        Table(
            [['Klüver-Schildberg', '', 'Hartkemper'],
             ['Richter am Amtsgericht', '', 'Urkundsbeamtin d. Geschäftsstelle']],
            colWidths=[200, 55, 200]
        ),
        pb(),
    ]
    return elems


# ── 14. URTEIL AG BIELEFELD ────────────────────────────────────────────────────
def teil_14_urteil_ag():
    elems = section_header("Teil XIV", "URTEIL AG BIELEFELD 34 C 421/22 vom 11.10.2022")
    elems += [
        p('<b>AMTSGERICHT BIELEFELD</b>', CENTER_BOLD),
        p('Az.: 34 C 421/22', CENTER),
        sp(6),
        p('<b>IM NAMEN DES VOLKES</b>', S('inv', fontName='Helvetica-Bold', fontSize=14,
          alignment=TA_CENTER, textColor=C_ACCENT)),
        p('<b>URTEIL</b>', CENTER_BOLD),
        sp(4),
        p('verkündet am: 11. Oktober 2022', CENTER),
        p('Klüver-Schildberg, Richter am Amtsgericht', CENTER),
        p('als Einzelrichter', CENTER),
        sp(8), hr(), sp(4),
        p('In der Rechtssache', BODY),
        p('Hildegunde Pferdedrescher-Riesenstein (Klägerin) ./. '
          'Götz-Sieghart Eberhart-Wolframshausen (Beklagter)', BOLD),
        p('wegen Räumung und Herausgabe', BODY),
        sp(6),
        p('<b>hat das Amtsgericht Bielefeld</b>, 34. Zivilabteilung, durch Richter am '
          'Amtsgericht Klüver-Schildberg als Einzelrichter am 11. Oktober 2022 für Recht erkannt:', BODY),
        sp(4),
        BoxedPara(
            '<b>TENOR</b><br/><br/>'
            '1. Die Klage wird abgewiesen.<br/>'
            '2. Die Klägerin trägt die Kosten des Rechtsstreits.<br/>'
            '3. Das Urteil ist vorläufig vollstreckbar. Der Klägerin wird nachgelassen, '
            'die Vollstreckung des Beklagten durch Sicherheitsleistung in Höhe von '
            '110 % des vollstreckbaren Betrages abzuwenden, sofern nicht der Beklagte '
            'vor Vollstreckung Sicherheit in gleicher Höhe leistet.<br/>'
            '4. Die Revision wird nicht zugelassen (§ 511 Abs. 4 ZPO). '
            'Die Berufung ist statthaft.',
            bg=C_QES_BG, border=C_QES_BLUE,
            style=S('tenor_s', fontName='Helvetica', fontSize=9.5, leading=15, textColor=C_BLACK)
        ),
        sp(6),
        p('<b>TATBESTAND (Kurzfassung)</b>', H2),
        p('Die Klägerin nimmt den Beklagten auf Räumung und Herausgabe der Wohnung '
          'Eckendorfer Straße 188, App. 4 OG, 33609 Bielefeld in Anspruch. '
          'Zwischen den Parteien besteht ein Mietverhältnis seit 01.04.2017. '
          'Die Bruttomiete beträgt EUR 648,97 monatlich.', BODY),
        p('Die Klägerin erklärte am 10.02.2022 die fristlose Kündigung per '
          'WhatsApp-Sprachnachricht und per E-Mail mit unsigniertem PDF. '
          'Weitere Kündigungen enthielten die Schriftsätze vom 09.03.2022 und 13.05.2022, '
          'beide qualifiziert elektronisch signiert und über beA eingereicht, '
          'dem Beklagten jedoch als Papierausdruck mit Transfervermerk zugestellt.', BODY),
        sp(4),
        p('<b>ENTSCHEIDUNGSGRÜNDE</b>', H2),
        p('<b>I. WhatsApp-Kündigung und E-Mail ohne qES</b>', H3),
        p('Die Kündigungserklärungen vom 10.02.2022 wahren die Schriftform des § 568 Abs. 1 '
          'BGB nicht. Eine WhatsApp-Sprachnachricht ist weder Schrift (§ 126 BGB) noch '
          'elektronische Form (§ 126a BGB). Ein unsigniertes PDF genügt § 126a BGB nicht. '
          'Die Kündigungen sind nach § 125 S. 1 BGB nichtig.', BODY),
        p('<b>II. Kündigung in den qES-Schriftsätzen</b>', H3),
        p('Die Klageschrift vom 09.03.2022 und der Replik-Schriftsatz vom 13.05.2022 '
          'wurden zwar mit qualifizierter elektronischer Signatur versehen. '
          'Sie wurden dem Beklagten jedoch ausschließlich als Papierausdruck mit '
          'Transfervermerk gem. § 298 Abs. 3 ZPO zugestellt.', BODY),
        p('Das Gericht teilt die Ansicht des Beklagten: Die empfangsbedürftige '
          'Willenserklärung (Kündigung) muss nach § 130 Abs. 1 S. 1 BGB dem '
          'Erklärungsgegner in der vorgeschriebenen Form zugehen. '
          'Die elektronische Form des § 126a BGB setzt voraus, dass das elektronische '
          'Dokument mit prüfbarer qES in den Machtbereich des Empfängers gelangt. '
          'Ein Ausdruck ermöglicht dem Empfänger keine Signaturprüfung. '
          'Der Transfervermerk ersetzt diese Möglichkeit nicht.', BODY),
        p('Die Kündigungen sind daher wegen formwidrigen Zugangs gem. § 125 S. 1 BGB '
          'unwirksam. Der Räumungsanspruch besteht mangels wirksamer Kündigung nicht.', BODY),
        p('<b>III. Kosten:</b> § 91 ZPO.', BODY),
        sp(8),
        p('Klüver-Schildberg', BOLD),
        p('Richter am Amtsgericht', SMALL),
        sp(4),
        p('<i>Rechtsmittelbelehrung: Gegen dieses Urteil ist die Berufung statthaft '
          '(§ 511 ZPO). Berufungsfrist: 1 Monat ab Urteilszustellung (§ 517 ZPO). '
          'Berufungsgericht: Landgericht Bielefeld.</i>', FOOTNOTE),
        pb(),
    ]
    return elems


# ── 15. BERUFUNGSSCHRIFT ───────────────────────────────────────────────────────
def teil_15_berufung():
    elems = section_header("Teil XV", "BERUFUNGSSCHRIFT KLÄGERIN 12.11.2022")
    elems += [
        p('<b>Ranftenschwedler Ostkamp Rechtsanwälte mbB</b>', S('r_h2', fontName='Helvetica-Bold',
          fontSize=11, textColor=C_ACCENT)),
        p('AN DAS LANDGERICHT BIELEFELD — Berufungskammer', BOLD),
        p('Az. Vorinstanz: AG Bielefeld 34 C 421/22', SMALL),
        sp(6), hr(), sp(4),
        p('<b>BERUFUNGSSCHRIFT</b>', S('bfs', fontName='Helvetica-Bold', fontSize=14,
          alignment=TA_CENTER, textColor=C_ACCENT)),
        sp(4),
        p('Bielefeld, 12. November 2022', CENTER),
        sp(6),
        p('In der Rechtssache Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen '
          'legt die Klägerin gegen das Urteil des AG Bielefeld vom 11.10.2022 '
          '(Az. 34 C 421/22) <b>Berufung</b> ein und beantragt:', BODY),
        p('1. Das angefochtene Urteil abzuändern.', BODY_L),
        p('2. Den Beklagten zu verurteilen gemäß den erstinstanzlichen Anträgen '
          '(Räumung, Herausgabe, Zahlung EUR 1.696,31 nebst Zinsen).', BODY_L),
        p('3. Hilfsweise: Zurückverweisung an das AG Bielefeld.', BODY_L),
        sp(4),
        p('<b>Begründung der Berufung:</b> Wird nachgereicht (§ 520 ZPO). '
          'Die Berufungsbegründungsfrist beträgt zwei Monate ab Urteilszustellung '
          '(Zustellung an RA Ranftenschwedler-Bielenfels: 28.10.2022). '
          'Fristende: 28. Dezember 2022 (verlängert auf 28. Januar 2023 lt. '
          'Fristverlängerungsantrag vom 22.12.2022).', BODY),
        sp(8),
        p('Dr. Engelbert Ranftenschwedler-Bielenfels', BOLD),
        p('Rechtsanwalt', SMALL),
        pb(),
    ]
    return elems


# ── 16. MANDATSANNAHME HASSENSTEIN-HEEPEN ────────────────────────────────────
def teil_16_mandatsannahme():
    elems = section_header("Teil XVI", "MANDATSANNAHME RA HASSENSTEIN-HEEPEN (Berufungsinstanz)")
    elems += [
        p('<b>Wolfdieter Hassenstein-Heepen</b>', S('hh_h', fontName='Helvetica-Bold',
          fontSize=12, textColor=C_ACCENT)),
        p('Rechtsanwalt · Werther Straße 89 · 33615 Bielefeld-Schildesche', BODY),
        p('Tel.: 0521/██████ · w.hassenstein-heepen@ra-bielefeld.de', SMALL),
        sp(6), hr(), sp(4),
        p('Bielefeld, 05. Dezember 2022', BODY),
        sp(4),
        p('An: Götz-Sieghart Eberhart-Wolframshausen, Eckendorfer Straße 188, '
          'App. 4 OG, 33609 Bielefeld', BODY),
        sp(4),
        p('<b>Mandatsbestätigung — Rechtssache Pferdedrescher-Riesenstein ./. '
          'Eberhart-Wolframshausen, LG Bielefeld (Berufung)</b>', BOLD),
        sp(4),
        p('Sehr geehrter Herr Eberhart-Wolframshausen,', BODY),
        p('ich bestätige hiermit die Übernahme Ihrer Vertretung im Berufungsverfahren '
          'vor dem Landgericht Bielefeld. Ich habe die Akte studiert und Ihre '
          'Rechtsposition erscheint mir gut fundiert.', BODY),
        p('Sie haben die Argumentation zur Formunwirksamkeit der Kündigung per '
          'qES-Schriftsatz mit Transfervermerk erstinstanzlich ohne Anwalt '
          '<b>vollkommen korrekt</b> vorgetragen. Das Amtsgericht ist Ihnen zu Recht gefolgt.', BODY),
        p('Ich übernehme Ihre Vertretung zu folgenden Konditionen:', BODY),
        Table([
            ['Stundensatz:', 'EUR 280,00 zzgl. USt. (netto EUR 280,00/h, brutto EUR 333,20/h)'],
            ['Vorschuss:', 'EUR 1.500,00 (Rechnung folgt gesondert)'],
            ['Abrechnung:', 'Monatlich nach RVG oder Stundenhonorar, je nachdem was höher'],
            ['Berichterstattung:', 'Per E-Mail, bevorzugt nach Ihren Angaben unverschlüsselt'],
        ], colWidths=[120, 320]),
        sp(6),
        p('Mit freundlichen Grüßen', BODY),
        sp(12),
        p('Wolfdieter Hassenstein-Heepen', BOLD),
        p('Rechtsanwalt', SMALL),
        p('<i>[Randnotiz Eberhart-Wolframshausen: „Endlich ein Profi. EUR 280/h ist happig aber '
          'ich will gewinnen."]</i>', HAND),
        pb(),
    ]
    return elems


# ── 17. BERUFUNGSBEGRÜNDUNG ────────────────────────────────────────────────────
def teil_17_berufungsbegruendung():
    elems = section_header("Teil XVII", "BERUFUNGSBEGRÜNDUNG KLÄGERIN (8 Seiten) — LG Bielefeld")
    elems += [
        p('<b>Ranftenschwedler Ostkamp Rechtsanwälte mbB</b>',
          S('r_h3', fontName='Helvetica-Bold', fontSize=11, textColor=C_ACCENT)),
        p('BERUFUNGSBEGRÜNDUNG — Az. LG Bielefeld 14 S 88/23 (Vorinstanz: 34 C 421/22)',BOLD),
        p('Bielefeld, 28. Januar 2023', SMALL),
        sp(6), hr(), sp(4),
        p('<b>BERUFUNGSBEGRÜNDUNG</b>', S('bbg', fontName='Helvetica-Bold', fontSize=14,
          alignment=TA_CENTER, textColor=C_ACCENT)),
        sp(6),
        p('<b>A. Einleitung: Die Online-Vermieter-Problematik</b>', H2),
        p('Frau Hildegunde Pferdedrescher-Riesenstein ist eine digital affine Unternehmerin. '
          'Sie betreibt einen Webshop, berät Kunden in Online-Marketing und kommuniziert '
          'ausschließlich elektronisch. Ihr Mieter Eberhart-Wolframshausen ist IT-Administrator '
          'und bewusst mit den technischen Anforderungen der elektronischen Signatur vertraut. '
          'Dennoch wurde ihr Recht, eine Kündigung in moderner Form zu erklären, '
          'durch eine Rechtslücke vereitelt, die der Gesetzgeber erst am '
          '17.07.2024 (§ 130e ZPO n.F.) geschlossen hat.', BODY),
        sp(4),
        p('<b>B. Angriffspunkte gegen das angefochtene Urteil</b>', H2),
        p('<b>I. § 126a BGB — qES wahrt Schriftform</b>', H3),
        p('Das AG hat zutreffend festgestellt, dass die Klageschrift und der Replik-Schriftsatz '
          'mit qualifizierter elektronischer Signatur versehen waren. § 568 Abs. 1 BGB '
          'schließt die elektronische Form nicht aus (vgl. § 126 Abs. 3 BGB; '
          'im Unterschied zu §§ 623, 766 S. 2, 780 S. 2 BGB). '
          'Die Kündigung konnte mithin durch qES-Schriftsatz wirksam erklärt werden.', BODY),
        p('<b>II. § 130 BGB — Zugangserfordernis</b>', H3),
        p('Das AG hat den Zugangs-Aspekt falsch gewichtet. Das Zugangserfordernis des § 130 BGB '
          'stellt nicht darauf ab, dass der Empfänger die Signatur tatsächlich prüft, '
          'sondern nur, dass die Erklärung in seinen Machtbereich gelangt. '
          'Durch die amtliche Zustellung ist die Kündigung in den Machtbereich '
          'des Beklagten gelangt.', BODY),
        p('<b>III. Transfervermerk § 298 Abs. 3 ZPO — Dokumentation der Authentizität</b>', H3),
        p('Der Transfervermerk gem. § 298 Abs. 3 ZPO gibt u.a. den Inhaber der Signatur '
          'und das Ergebnis der Integritätsprüfung wieder. Die amtliche Feststellung '
          'der Echtheit durch das Gericht ersetzt die eigenständige Signaturprüfung '
          'des Empfängers. Eine Bescheinigung des Staates über die Echtheit eines Dokuments '
          'ist mit einer notariellen Beglaubigung vergleichbar und für den Empfänger '
          'bindend (vgl. OLG München NJW-RR 2018, 513).', BODY),
        p('<b>IV. Keine unzumutbare Beeinträchtigung des Erklärenden</b>', H3),
        p('Würde man der Ansicht des AG folgen, dass die qES-Kündigung im Schriftsatz '
          'gegenüber einer nicht anwaltlich vertretenen Naturalpartei nie formwirksam '
          'erklärt werden kann (weil über beA zugestellt = elektronisch ohne Zustimmung, '
          'und als Ausdruck = Signaturverlust), käme es zu einer sachlich nicht '
          'gerechtfertigten Benachteiligung digital kommunizierender Vermieter.', BODY),
        p('<b>V. Argument zu § 130e ZPO (neu)</b>', H3),
        p('Der Gesetzgeber hat mit § 130e ZPO (in Kraft seit 17.07.2024) klargestellt, '
          'dass die gerichtliche Weiterleitung den formwirksamen Zugang fingiert. '
          'Diese Wertung zeigt, dass der Gesetzgeber die frühere Rechtslage für '
          'reformbedürftig und — im Umkehrschluss — die Ablehnung des formwirksamen '
          'Zugangs für jedenfalls vertretbar hielt.', BODY),
        sp(4),
        p('<b>C. Beweis</b>', H2),
        p('K-MIET-1 bis K-MIET-34 (s. Anlagenverzeichnis). '
          'Zeuge: Frau Christine Hartkemper, Urkundsbeamtin AG Bielefeld, '
          'zum Transfervermerk.', BODY),
        sp(4),
        p('<b>D. Schluss</b>', H2),
        p('Die Klägerin beantragt, das Urteil des AG Bielefeld abzuändern und '
          'dem Räumungsbegehren stattzugeben. Die Rechtsfrage hat grundsätzliche '
          'Bedeutung (§ 543 Abs. 2 ZPO) — Revision sollte zugelassen werden.', BODY),
        sp(8),
        p('Dr. Engelbert Ranftenschwedler-Bielenfels', BOLD),
        p('Rechtsanwalt', SMALL),
        pb(),
    ]
    return elems


# ── 18. BERUFUNGSERWIDERUNG ────────────────────────────────────────────────────
def teil_18_berufungserwiderung():
    elems = section_header("Teil XVIII",
                           "BERUFUNGSERWIDERUNG RA HASSENSTEIN-HEEPEN")
    elems += [
        p('<b>Wolfdieter Hassenstein-Heepen, Rechtsanwalt</b>',
          S('hh2', fontName='Helvetica-Bold', fontSize=11, textColor=C_ACCENT)),
        p('BERUFUNGSERWIDERUNG — Az. LG Bielefeld 14 S 88/23', BOLD),
        p('Bielefeld, 15. März 2023', SMALL),
        sp(6), hr(), sp(4),
        p('<b>BERUFUNGSERWIDERUNG</b>', S('bew', fontName='Helvetica-Bold', fontSize=13,
          alignment=TA_CENTER, textColor=C_ACCENT)),
        sp(6),
        p('<b>I. Kernargument: Verifikationsfunktion der qES</b>', H2),
        p('Die Berufungsbegründung der Klägerin verkennt den Zweck der qualifizierten '
          'elektronischen Signatur. Die qES i.S.v. § 126a BGB soll nicht nur die '
          '<i>Identitätsfunktion</i> (Erkennbarkeit des Erklärenden) und die '
          '<i>Echtheitsfunktion</i> (inhaltliche Urheberschaft) sicherstellen, '
          'sondern auch die <i>Verifikationsfunktion</i>: '
          'Der Empfänger muss die Signatur selbst technisch überprüfen können.', BODY),
        p('Am Papierausdruck ist dies technisch unmöglich. Der Transfervermerk '
          'gem. § 298 Abs. 3 ZPO enthält nur das Ergebnis einer staatlichen Prüfung — '
          'er ersetzt nicht die Möglichkeit des Empfängers zur eigenständigen Verifikation.', BODY),
        p('<b>II. Zur Funktionsäquivalenz (§ 126 vs. § 126a BGB)</b>', H2),
        p('Der Gesetzgeber hat die elektronische Form als <i>Äquivalent</i> zur Schriftform '
          'konzipiert (BT-Drs. 14/4987, S. 19 f.). Äquivalenz bedeutet: die elektronis Form '
          'muss dieselben Schutzfunktionen erfüllen wie die Schriftform. '
          'Beim schriftlichen Papieroriginal kann der Empfänger die Unterschrift jederzeit '
          'durch Sachverständige prüfen lassen. Bei der qES muss er dies ebenfalls können '
          '— was nur am elektronischen Original möglich ist.', BODY),
        p('<b>III. Zu § 130e ZPO n.F.</b>', H2),
        p('Die Klägerin kann aus § 130e ZPO (Inkrafttreten 17.07.2024) für den vorliegenden '
          'Sachverhalt (Schriftsätze vom 09.03.2022 und 13.05.2022) nichts ableiten. '
          'Das intertemporale Recht (Wirkung nach dem geltenden Recht zum Zeitpunkt der '
          'Erklärung) schließt eine Rückwirkung aus.', BODY),
        p('<b>IV. Ergebnis</b>', H2),
        p('Das Amtsgericht hat zutreffend entschieden. Die Berufung ist zurückzuweisen. '
          'Die Revision ist wegen grundsätzlicher Bedeutung zuzulassen '
          '(§ 543 Abs. 2 Nr. 1 ZPO).', BODY),
        sp(8),
        p('Wolfdieter Hassenstein-Heepen', BOLD),
        p('Rechtsanwalt', SMALL),
        pb(),
    ]
    return elems


# ── 19. LG-URTEIL ─────────────────────────────────────────────────────────────
def teil_19_urteil_lg():
    elems = section_header("Teil XIX", "URTEIL LG BIELEFELD 14 S 88/23 vom 20.06.2023")
    elems += [
        p('<b>LANDGERICHT BIELEFELD</b>', CENTER_BOLD),
        p('3. Zivilkammer', CENTER),
        p('Az.: 14 S 88/23 (Berufung gegen AG Bielefeld 34 C 421/22)', CENTER),
        sp(6),
        p('<b>IM NAMEN DES VOLKES</b>',
          S('invlg', fontName='Helvetica-Bold', fontSize=14, alignment=TA_CENTER, textColor=C_ACCENT)),
        p('<b>URTEIL</b>', CENTER_BOLD),
        p('Bielefeld, 20. Juni 2023', CENTER),
        sp(4),
        p('Vorsitzender Richter am Landgericht Dr. Augustin Bockenfelder-Senne '
          '(Vorsitzender 3. Zivilkammer)', CENTER),
        sp(6), hr(), sp(4),
        BoxedPara(
            '<b>TENOR</b><br/><br/>'
            '1. Die Berufung der Klägerin gegen das Urteil des AG Bielefeld '
            'vom 11. Oktober 2022 (Az. 34 C 421/22) wird zurückgewiesen.<br/>'
            '2. Die Klägerin hat die Kosten des Berufungsverfahrens zu tragen.<br/>'
            '3. Das Urteil ist vorläufig vollstreckbar.<br/>'
            '4. <b>Die Revision wird zugelassen</b> (§ 543 Abs. 2 S. 1 Nr. 1 ZPO). '
            'Die Rechtssache hat grundsätzliche Bedeutung hinsichtlich der Frage, '
            'ob die gerichtliche Zustellung eines Ausdrucks eines qES-Schriftsatzes '
            'mit Transfervermerk (§ 298 Abs. 3 ZPO) den formwirksamen Zugang '
            'einer empfangsbedürftigen Willenserklärung in elektronischer Form '
            '(§ 126a BGB) bewirkt.',
            bg=C_QES_BG, border=C_QES_BLUE,
            style=S('lg_tenor', fontName='Helvetica', fontSize=9.5, leading=15, textColor=C_BLACK)
        ),
        sp(6),
        p('<b>GRÜNDE (Auszug)</b>', H2),
        p('<b>I. Schriftform (§ 568 Abs. 1 BGB) und elektronische Form (§ 126a BGB)</b>', H3),
        p('Die Kammer bestätigt die Rechtsauffassung des Amtsgerichts. § 568 Abs. 1 BGB '
          'schreibt die Schriftform vor; diese kann durch die elektronische Form '
          'gem. § 126 Abs. 3 BGB i.V.m. § 126a BGB ersetzt werden. '
          'Eine Kündigung per WhatsApp-Sprachnachricht oder per E-Mail mit '
          'unsigniertem PDF-Anhang wahrt weder die Schriftform noch die '
          'elektronische Form (§ 125 S. 1 BGB).', BODY),
        p('<b>II. Zugang der qES-Erklärung (§ 130 BGB)</b>', H3),
        p('Die entscheidende Frage ist, ob die Kündigungserklärungen in den '
          'qES-Schriftsätzen dem Beklagten formwirksam zugegangen sind. '
          'Die Kammer verneint dies.', BODY),
        p('Zur Wahrung einer für eine empfangsbedürftige Willenserklärung vorgeschriebenen '
          'Form reicht es nicht aus, dass die Erklärung formgerecht abgegeben wurde; '
          'sie muss dem Erklärungsgegner auch in der vorgeschriebenen Form zugehen '
          '(§ 130 Abs. 1 S. 1 BGB).', BODY),
        p('Der Beklagte hat nur den Papierausdruck erhalten. Am Papierausdruck '
          'kann er die qualifizierte elektronische Signatur technisch nicht '
          'verifizieren. Der Transfervermerk gem. § 298 Abs. 3 ZPO dokumentiert '
          'zwar das Ergebnis der gerichtlichen Signaturprüfung, ersetzt aber nicht '
          'die technische Prüfmöglichkeit des Empfängers (Verifikationsfunktion).', BODY),
        p('<b>III. § 130e ZPO — keine Rückwirkung</b>', H3),
        p('§ 130e ZPO (in Kraft seit 17.07.2024) fingiert für Schriftsätze, '
          'die nach diesem Datum als elektronische Dokumente gem. § 130a ZPO '
          'eingereicht und dem Empfänger zugestellt werden, den formwirksamen Zugang. '
          'Eine Anwendung auf die hier maßgeblichen Schriftsätze vom 09.03.2022 '
          'und 13.05.2022 scheitert an den Grundsätzen des intertemporalen Rechts.', BODY),
        sp(6),
        p('Dr. Augustin Bockenfelder-Senne', BOLD),
        p('Vorsitzender Richter am Landgericht — 3. Zivilkammer', SMALL),
        pb(),
    ]
    return elems


# ── 20. REVISIONSBEGRÜNDUNG ────────────────────────────────────────────────────
def teil_20_revision():
    elems = section_header("Teil XX", "REVISIONSBEGRÜNDUNG BGH VIII ZR 159/23 — 28.08.2023")
    elems += [
        p('<b>Ranftenschwedler Ostkamp Rechtsanwälte mbB</b>',
          S('rh4', fontName='Helvetica-Bold', fontSize=11, textColor=C_ACCENT)),
        p('REVISIONSBEGRÜNDUNG an den BUNDESGERICHTSHOF', BOLD),
        p('Az. BGH: VIII ZR 159/23 | Vorinstanz: LG Bielefeld 14 S 88/23', SMALL),
        p('Karlsruhe, 28. August 2023 | Eingereicht über beA mit qES', SMALL),
        sp(6), hr(), sp(4),
        p('<b>REVISIONSBEGRÜNDUNG</b>', S('rev_h', fontName='Helvetica-Bold', fontSize=14,
          alignment=TA_CENTER, textColor=C_ACCENT)),
        sp(6),
        p('<b>A. Revisionszulassung und Zulässigkeit</b>', H2),
        p('Die Revision wurde vom LG Bielefeld zugelassen (§ 543 Abs. 2 S. 1 ZPO). '
          'Das Berufungsgericht hat die grundsätzliche Bedeutung der Rechtsfrage '
          'ausdrücklich anerkannt.', BODY),
        p('<b>B. Revisionsrügen (§ 545 ZPO)</b>', H2),
        p('<b>I. Verletzung von § 126a Abs. 1 BGB i.V.m. § 130 Abs. 1 S. 1 BGB</b>', H3),
        p('Das Berufungsgericht hat § 126a Abs. 1 BGB i.V.m. § 130 BGB verletzt, '
          'indem es die gerichtliche Zustellung des qES-Schriftsatzes als Papierausdruck '
          'mit Transfervermerk (§ 298 Abs. 3 ZPO) nicht als formwirksamen Zugang '
          'der in dem Schriftsatz enthaltenen Kündigungserklärung angesehen hat.', BODY),
        p('<b>II. Zu den Formzwecken</b>', H3),
        p('Die qES dient der Identitätsfunktion (der Erklärender ist identifizierbar), '
          'der Echtheitsfunktion (Authentizität des Inhalts) sowie der '
          'Verifikationsfunktion. Der Transfervermerk nach § 298 Abs. 3 ZPO '
          'bescheinigt staatlich die Identität des Signierers sowie die Integrität '
          'des Dokuments. Damit sind Identitäts- und Echtheitsfunktion erfüllt.', BODY),
        p('Die „Verifikationsfunktion" als eigenständige Funktion der qES ist '
          'in der Lit. nicht allgemein anerkannt. Es kommt allein darauf an, '
          'dass die Echtheit der Signatur dem Empfänger gegenüber nachgewiesen wird '
          '— was durch den staatlichen Transfervermerk geschieht.', BODY),
        p('<b>III. Systemwidrigkeit des Ergebnisses</b>', H3),
        p('Wenn der VIII. Senat die Rechtsauffassung des LG bestätigt, '
          'kann eine anwaltlich vertretene Partei bis zur Schaffung des § 130e ZPO '
          'keine Kündigung via beA-Schriftsatz gegenüber einer nicht anwaltlich '
          'vertretenen Naturalpartei (§ 130d ZPO: Pflicht zu elektronischer Einreichung!) '
          'formwirksam erklären. Das ist eine in der Praxis nicht auflösbare Kollision '
          'zwischen prozessualem Elektronikzwang und materiellem Formerfordernis.', BODY),
        sp(4),
    ] + qes_block(signer="Dr. Engelbert Ranftenschwedler-Bielenfels, Rechtsanwalt beim BGH zugelassen") + [
        sp(4),
        p('Dr. Engelbert Ranftenschwedler-Bielenfels', BOLD),
        p('Rechtsanwalt (zugelassen beim BGH)', SMALL),
        pb(),
    ]
    return elems


# ── 21. REVISIONSERWIDERUNG ────────────────────────────────────────────────────
def teil_21_revisionserwiderung():
    elems = section_header("Teil XXI", "REVISIONSERWIDERUNG MIETER (Hassenstein-Heepen)")
    elems += [
        p('<b>Wolfdieter Hassenstein-Heepen, Rechtsanwalt</b>',
          S('hh3', fontName='Helvetica-Bold', fontSize=11, textColor=C_ACCENT)),
        p('REVISIONSERWIDERUNG — Az. BGH VIII ZR 159/23', BOLD),
        p('Karlsruhe/Bielefeld, 04. Oktober 2023', SMALL),
        sp(6), hr(), sp(4),
        p('Der Beklagte beantragt, die Revision der Klägerin zurückzuweisen.', BODY),
        sp(4),
        p('<b>Zur Verifikationsfunktion:</b>', BOLD),
        p('Die von der Revisionsklägerin in Abrede gestellte Verifikationsfunktion '
          'der qES ist in der Literatur anerkannt und vom Gesetzgeber beabsichtigt '
          '(vgl. BT-Drs. 14/4987, S. 16; MüKoBGB/Einsele, 9. Aufl. 2021, § 126a Rn. 3). '
          'Die Verifikationsfunktion dient dem Empfänger: Er soll in der Lage sein, '
          'selbständig die Authentizität der Erklärung zu überprüfen. '
          'Dies ist am Papierausdruck technisch unmöglich.', BODY),
        p('<b>Zum angeblichen Systemwiderspruch:</b>', BOLD),
        p('Der von der Klägerin behauptete Systemwiderspruch besteht nicht. '
          'Die Klägerin hätte die Kündigung außergerichtlich jederzeit formwirksam '
          'erklären können — z.B. durch Übergabe eines handschriftlich unterzeichneten '
          'Originals oder durch direkte E-Mail-Versendung des qES-signierten PDFs '
          'an den Beklagten. Die prozessuale Pflicht zur elektronischen Einreichung '
          '(§ 130d ZPO) hindert sie nicht an der außergerichtlichen Kündigung '
          'auf dem klassischen Schriftweg.', BODY),
        sp(4),
        p('Wolfdieter Hassenstein-Heepen', BOLD),
        p('Rechtsanwalt', SMALL),
        pb(),
    ]
    return elems


# ── 22. STELLUNGNAHME VERHANDLUNGSTERMIN BGH ──────────────────────────────────
def teil_22_stellungnahme_bgh():
    elems = section_header("Teil XXII",
                           "STELLUNGNAHME ZUM VERHANDLUNGSTERMIN BGH — 27. November 2024")
    elems += [
        p('<b>Ranftenschwedler Ostkamp Rechtsanwälte mbB</b>',
          S('rh5', fontName='Helvetica-Bold', fontSize=11, textColor=C_ACCENT)),
        p('Internes Memo an Mandantin Pferdedrescher-Riesenstein', BOLD),
        p('Bielefeld/Karlsruhe, 22. November 2024', SMALL),
        sp(6), hr(), sp(4),
        p('Sehr geehrte Frau Pferdedrescher-Riesenstein,', BODY),
        p('der Bundesgerichtshof (VIII. Zivilsenat) hat für Mittwoch, den '
          '27. November 2024, Verhandlungstermin in unserer Sache (Az. VIII ZR 159/23) '
          'sowie in dem gleichgelagerten Verfahren VIII ZR 155/23 anberaumt.', BODY),
        p('Ich fahre am Vortag nach Karlsruhe. Auf der Grundlage unserer '
          'bisherigen Argumentation und der Hinweise aus dem Senat gehe ich '
          '<b>nicht davon aus, dass der BGH unsere Revision durchgreifen lässt</b>. '
          'Der Senat scheint der strengen Verifikationsfunktions-Theorie zu folgen.', BODY),
        p('Falls die Revision scheitert: Ich werde Ihnen unmittelbar nach der '
          'Urteilsverkündung telefonisch Bericht erstatten.', BODY),
        sp(6),
        p('Dr. Engelbert Ranftenschwedler-Bielenfels', BOLD),
        p('Rechtsanwalt', SMALL),
        pb(),
    ]
    return elems


# ── 23. BGH-URTEIL ─────────────────────────────────────────────────────────────
def teil_23_bgh_urteil():
    elems = section_header("Teil XXIII",
                           "BGH URTEIL VIII ZR 159/23 — Tenor und Leitsätze")
    elems += [
        p('<b>BUNDESGERICHTSHOF</b>', CENTER_BOLD),
        p('VIII. Zivilsenat', CENTER),
        sp(6),
        p('<b>URTEIL</b>', S('bgh_u', fontName='Helvetica-Bold', fontSize=16,
          alignment=TA_CENTER, textColor=C_ACCENT)),
        sp(4),
        p('Az.: <b>VIII ZR 159/23</b>', CENTER),
        p('Verkündet am: <b>27. November 2024</b>', CENTER),
        sp(6),
        p('Senatsbesetzung: Vorsitzender Richter am Bundesgerichtshof Dr. Bünger, '
          'Richterin am Bundesgerichtshof Dr. Liebert, '
          'Richter am Bundesgerichtshof Dr. Schmidt-Räntsch, '
          'Richterin am Bundesgerichtshof Dr. Wiegand, '
          'Richter am Bundesgerichtshof Gegen',
          S('sbs', fontName='Helvetica', fontSize=8.5, leading=13,
            alignment=TA_CENTER, textColor=C_DARK_GREY)),
        sp(6), hr(), sp(4),
        BoxedPara(
            '<b>TENOR</b><br/><br/>'
            'Die Revision der Klägerin gegen das Urteil der 3. Zivilkammer des '
            'Landgerichts Bielefeld vom 20. Juni 2023 wird auf ihre Kosten zurückgewiesen.',
            bg=C_QES_BG, border=C_QES_BLUE,
            style=S('bgh_tenor', fontName='Helvetica', fontSize=10, leading=15, textColor=C_BLACK)
        ),
        sp(8),
        p('<b>LEITSÄTZE</b>', H2),
        BoxedPara(
            '<b>a)</b> Bei einer empfangsbedürftigen Willenserklärung ist es auch für die '
            'elektronische Form zur Wahrung der Form nicht ausreichend, dass die Willenserklärung '
            'formgerecht abgegeben wurde; diese muss dem Erklärungsgegner vielmehr auch in der '
            'entsprechenden Form zugehen (§ 130 Abs. 1 Satz 1 BGB). Für den Zugang einer in einem '
            'qualifiziert elektronisch signierten elektronischen Dokument enthaltenen Willenserklärung '
            'ist es daher erforderlich, dass dieses Dokument so in den Machtbereich des Empfängers '
            'gelangt, dass dieser die qualifizierte elektronische Signatur des Erklärenden und damit '
            'die Echtheit des Dokuments prüfen kann.',
            bg=colors.HexColor("#E8EAF6"), border=colors.HexColor("#3949AB"),
            style=S('ls_a', fontName='Helvetica', fontSize=9.5, leading=15, textColor=C_BLACK)
        ),
        sp(4),
        BoxedPara(
            '<b>b)</b> Diese Voraussetzungen sind in dem Zeitraum vor dem Inkrafttreten der '
            'Vorschrift des § 130e ZPO am 17. Juli 2024 erfüllt, wenn in einem Zivilprozess '
            'ein elektronischer Schriftsatz mit einer gültigen qualifizierten elektronischen '
            'Signatur, der eine empfangsbedürftige Willenserklärung enthält, vom Gericht unter '
            'Aufrechterhaltung der elektronischen Signatur elektronisch an den Empfänger der '
            'Willenserklärung weitergeleitet wird.',
            bg=colors.HexColor("#E8EAF6"), border=colors.HexColor("#3949AB"),
            style=S('ls_b', fontName='Helvetica', fontSize=9.5, leading=15, textColor=C_BLACK)
        ),
        sp(4),
        BoxedPara(
            '<b>c)</b> In dem Zeitraum vor dem Inkrafttreten des § 130e ZPO bewirkt die '
            'Übermittlung eines Ausdrucks eines mit einer gültigen qualifizierten elektronischen '
            'Signatur versehenen, bei Gericht im Rahmen eines Zivilprozesses eingegangenen '
            'elektronischen Dokuments unter Beifügung eines Transfervermerks im Sinne des '
            '§ 298 Abs. 3 ZPO keinen wirksamen Zugang der in dem Dokument enthaltenen '
            'empfangsbedürftigen Willenserklärung beim Erklärungsgegner '
            '(BGH, Urteil vom 27. November 2024 – VIII ZR 159/23, MDR 2025, 162).',
            bg=colors.HexColor("#E8EAF6"), border=colors.HexColor("#3949AB"),
            style=S('ls_c', fontName='Helvetica', fontSize=9.5, leading=15, textColor=C_BLACK)
        ),
        sp(6),
        p('<b>Aus den Entscheidungsgründen (Auszug):</b>', H2),
        p('„§ 568 Abs. 1 BGB schließt – anders als beispielsweise die Formvorschriften der '
          '§§ 623, 766 Satz 2, § 780 Satz 2 und § 781 Satz 2 BGB – für die Kündigung '
          'eines Mietverhältnisses die elektronische Form nicht aus. '
          'Zur Wahrung einer für eine empfangsbedürftige Willenserklärung vorgeschriebenen '
          'Form ist nicht ausreichend, dass diese nach den jeweiligen Formvorschriften '
          'abgegeben wurde. Sie muss vielmehr, um wirksam zu werden, dem Erklärungsgegner '
          'auch in der vorgeschriebenen Form gemäß § 130 BGB zugehen [...]"', CITE),
        p('„Zu den mit der Schriftform bezweckten Leistungsfunktionen, welche die '
          'elektronische Form in vergleichbarer Weise sicherstellen soll, gehört – '
          'neben der Identitätsfunktion [...] und der Echtheitsfunktion [...] – auch die '
          'damit in Zusammenhang stehende Verifikationsfunktion, nach der es dem Empfänger '
          'des Dokuments möglich sein soll, zu überprüfen, ob die Unterschrift echt ist [...]"', CITE),
        p('„Die – hier vorliegende – Übermittlung eines Ausdrucks eines mit einer '
          'qualifizierten elektronischen Signatur versehenen, bei Gericht im Rahmen eines '
          'Zivilprozesses eingegangenen elektronischen Dokuments (§ 298 Abs. 1 Satz 1 ZPO) '
          'vermag hingegen einen formgerechten Zugang der in ihm enthaltenen Willenserklärung '
          '(hier: der Kündigungserklärung) iSv. § 126a Abs. 1 BGB beim Erklärungsgegner auch '
          'dann nicht zu bewirken, wenn dem Ausdruck ein Transfervermerk gemäß '
          '§ 298 Abs. 3 ZPO beigefügt ist [...]"', CITE),
        sp(4),
        p('<b>Gesamtergebnis (BGH):</b> Die Revision der Klägerin (Pferdedrescher-Riesenstein) '
          'wird zurückgewiesen. Alle drei Kündigungen — WhatsApp/E-Mail ohne qES (10.02.2022), '
          'qES-Klageschrift zugestellt als Papierausdruck (09.03.2022), qES-Replik als '
          'Papierausdruck (13.05.2022) — sind formunwirksam. '
          'Der Räumungsanspruch scheitert.', BODY),
        sp(6),
        p('<i>Parallelsache: BGH VIII ZR 155/23 — dort erfolgte Weiterleitung per beA; '
          'der BGH verweist insoweit zurück zwecks Feststellung, ob die qES erhalten blieb.</i>',
          ITALIC),
        pb(),
    ]
    return elems


# ── 24. MANDANTENMEMO ─────────────────────────────────────────────────────────
def teil_24_mandantenmemo():
    elems = section_header("Teil XXIV",
                           "MANDANTENMEMO RA RANFTENSCHWEDLER-BIELENFELS — 02.12.2024")
    elems += [
        p('<b>Ranftenschwedler Ostkamp Rechtsanwälte mbB</b>',
          S('rh6', fontName='Helvetica-Bold', fontSize=11, textColor=C_ACCENT)),
        p('VERTRAULICHES MANDANTENMEMO', BOLD),
        p('Empfängerin: Frau Hildegunde Pferdedrescher-Riesenstein', SMALL),
        p('Datum: 02. Dezember 2024 | Unser Az.: RO/2022/0312/PKT', SMALL),
        sp(6), hr(), sp(4),
        p('<b>Betreff: BGH-Urteil VIII ZR 159/23 vom 27.11.2024 — Bittere Lehren '
          'und Handlungsempfehlungen für die Zukunft</b>', BOLD),
        sp(4),
        p('Sehr geehrte Frau Pferdedrescher-Riesenstein,', BODY),
        p('der Bundesgerichtshof hat unsere Revision zurückgewiesen. '
          'Ich möchte Ihnen die Kernlehren aus diesem Verfahren zusammenfassen '
          'und Empfehlungen für künftige Mietverhältnisse geben.', BODY),
        sp(6),
        p('<b>I. Was ist passiert — und warum haben wir verloren</b>', H2),
        BoxedPara(
            '<b>Fehler 1 — WhatsApp-Kündigung:</b> Eine Kündigung per WhatsApp-Sprachnachricht '
            'ist und bleibt formunwirksam. Das war von Anfang an klar. '
            'Bitte sprechen Sie in Zukunft niemals eine Kündigung auf WhatsApp ein.<br/><br/>'
            '<b>Fehler 2 — E-Mail ohne qES:</b> Eine eingescannte PDF ohne qualifizierte '
            'elektronische Signatur (qES) genügt § 126a BGB nicht. '
            'Kündigung per E-Mail ist nur mit qES wirksam.<br/><br/>'
            '<b>Fehler 3 — qES-Schriftsatz, Zustellung als Ausdruck:</b> '
            'Dies war die eigentlich interessante — und teure — Rechtsfrage. '
            'Der BGH hat entschieden: Die qES muss dem Mieter im elektronischen Original zugehen. '
            'Ein Papierausdruck mit Transfervermerk (§ 298 Abs. 3 ZPO) reicht nicht aus, '
            'weil der Mieter am Papier die Signatur nicht prüfen kann.',
            bg=C_RED_LIGHT, border=C_RED,
            style=S('memo_s', fontName='Helvetica', fontSize=9, leading=14, textColor=C_BLACK)
        ),
        sp(6),
        p('<b>II. Was hätte funktioniert</b>', H2),
        p('<b>Option A (klassisch, 100% sicher):</b> Kündigung schriftlich auf Papier, '
          'eigenhändig unterschrieben, durch Boten übergeben (zwei Zeugen!), '
          'oder per Gerichtsvollzieher, oder per Einschreiben/Rückschein — '
          'wobei Einschreiben bei Nichtannahme problematisch ist.', BODY),
        p('<b>Option B (elektronisch, wenn korrekt):</b> '
          'qES-signiertes PDF <b>direkt per E-Mail an den Mieter</b> versenden. '
          'Der Mieter muss die E-Mail erhalten und die qES am elektronischen Dokument '
          'prüfen können. NICHT über Gericht. Direkt an seine E-Mail-Adresse.', BODY),
        p('<b>Was NICHT funktioniert (jetzt BGH-bestätigt):</b> qES-Kündigung im '
          'Gerichtsschriftsatz, der als Papierausdruck zugestellt wird.', BODY),
        sp(4),
        p('<b>III. Neue Rechtslage ab 17.07.2024 (§ 130e ZPO)</b>', H2),
        p('Der Gesetzgeber hat die Lücke geschlossen. Ab dem 17.07.2024 fingiert '
          '§ 130e ZPO den formwirksamen Zugang, wenn ein qES-Schriftsatz '
          'als elektronisches Dokument gem. § 130a ZPO bei Gericht eingereicht und '
          'dem Empfänger zugestellt oder mitgeteilt wurde. '
          'FÜR KÜNFTIGE Verfahren ist das Problem gelöst — '
          'für Ihr Verfahren aus 2022 kam diese Norm zu spät.', BODY),
        sp(4),
        p('<b>IV. Gesamtschadensbilanz</b>', H2),
        Table([
            ['Position', 'Betrag'],
            ['Anwaltskosten 1. Instanz + Revision', 'ca. EUR 12.400,00'],
            ['Gerichtskosten (alle Instanzen)', 'ca. EUR 4.100,00'],
            ['Mietrückstand (nicht vollstreckt)', 'ca. EUR 2.600,00'],
            ['Entgangene Nutzungsentschädigung', 'ca. EUR 4.500,00'],
            ['Gesamtschaden (geschätzt)', '≈ EUR 23.600,00'],
        ], colWidths=[320, 130]),
        sp(6),
        p('Mit freundlichen Grüßen und aufrichtigem Bedauern,', BODY),
        sp(12),
        p('Dr. Engelbert Ranftenschwedler-Bielenfels', BOLD),
        p('Rechtsanwalt | Fachanwalt für Miet- und WEG-Recht', SMALL),
        pb(),
    ]
    return elems


# ── 25. ONLINE-VERMIETER-MEMO ─────────────────────────────────────────────────
def teil_25_online_memo():
    elems = section_header("Teil XXV",
                           "‚ONLINE-VERMIETER'-MEMO — Digitale Kündigungsreform und Mieterschutz")
    elems += [
        p('<b>Ranftenschwedler Ostkamp Rechtsanwälte mbB</b>',
          S('rh7', fontName='Helvetica-Bold', fontSize=11, textColor=C_ACCENT)),
        p('ANWALTLICHES MEMO — INTERN UND AN MANDANTIN', BOLD),
        p('Betreff: Geplante Reform der digitalen Kündigung — Chancen und Risiken', BOLD),
        p('Datum: 02. Dezember 2024', SMALL),
        sp(6), hr(), sp(4),
        p('<b>A. Das Dilemma des Online-Vermieters nach BGH VIII ZR 159/23</b>', H2),
        p('Unsere Mandantin Frau Pferdedrescher-Riesenstein ist ein Prototyp des '
          '„Online-Vermieters": digital affin, kommuniziert ausschließlich elektronisch, '
          'möchte auch Kündigungen online abwickeln. Das BGH-Urteil schränkt diese '
          'Möglichkeiten erheblich ein — aber nur vorübergehend.', BODY),
        BoxedPara(
            '<b>§ 130e ZPO (seit 17.07.2024) als Übergangs-Lösung:</b><br/>'
            'Im Prozess ist die qES-Kündigung per beA-Schriftsatz jetzt wirksam, '
            'weil § 130e ZPO den Zugang fingiert. '
            'ABER: Außerhalb des Prozesses (d.h. vor Klageerhebung) bleibt das Problem: '
            'Eine qES-Kündigung per E-Mail direkt an den Mieter ist materiellrechtlich '
            'richtig und wirksam — WENN der Mieter die E-Mail-Adresse für '
            'rechtsverbindliche Zustellungen akzeptiert hat.',
            bg=colors.HexColor("#E8F5E9"), border=colors.HexColor("#2E7D32"),
            style=S('reform_s', fontName='Helvetica', fontSize=9, leading=14, textColor=C_BLACK)
        ),
        sp(4),
        p('<b>B. Was hätte Frau Pferdedrescher-Riesenstein tun können?</b>', H2),
        p('Wenn Frau Pferdedrescher-Riesenstein am 10.02.2022 eine qES-signierte '
          'Kündigung <b>direkt per E-Mail an Herrn Eberhart-Wolframshausen</b> geschickt hätte '
          '(nicht über Gericht, sondern direkt!), wäre die Kündigung nach dem BGH-Urteil '
          '<b>wirksam zugegangen</b> — vorausgesetzt, Eberhart-Wolframshausen hätte die '
          'E-Mail empfangen und die qES hätte er am elektronischen Anhang prüfen können.', BODY),
        p('Der Mieter-IT-Admin hätte dann argumentieren können: '
          '„Ich habe keine E-Mail-Adresse für rechtsverbindliche Erklärungen angegeben" — '
          'aber das BGH-Urteil stellt auf das technische Zugehen-Können ab, '
          'nicht auf eine vorige Zustimmung.', BODY),
        sp(4),
        p('<b>C. Zukünftiges Risiko für Mieter: „Digitale Kündigung per E-Mail"</b>', H2),
        BoxedPara(
            '<b>⚠ WARNUNG FÜR MIETER (Vorlage für Mandanten-Rundschreiben):</b><br/><br/>'
            'Nach dem BGH-Urteil VIII ZR 159/23 ist eine Kündigung per qES-signiertem '
            'PDF direkt per E-Mail rechtswirksam, sobald das elektronische Original '
            'beim Mieter eingeht und er die Signatur prüfen kann.<br/><br/>'
            'Das bedeutet: <b>Mieter müssen ihre E-Mail-Postfächer und ggf. '
            'Messenger-Apps regelmäßig auf qES-signierte Anhänge prüfen!</b><br/><br/>'
            'Wer sein E-Mail-Postfach nicht regelmäßig abruft oder Anhänge '
            'als Spam löscht, riskiert, eine formwirksame Kündigung zu verpassen. '
            'Im Zweifel: Alle PDFs mit Signaturhinweis sofort in Adobe Acrobat '
            'oder einem qES-Validator prüfen!<br/><br/>'
            '<i>Empfehlung: Im Mietvertrag eine klare Vereinbarung treffen, '
            'welche E-Mail-Adresse (oder kein E-Mail) für Kündigungen gilt.</i>',
            bg=C_STAMP_BG, border=C_STAMP_BD,
            style=S('warn_mieter', fontName='Helvetica', fontSize=9, leading=14, textColor=C_BLACK)
        ),
        sp(6),
        p('<b>D. Die Gretchenfrage: „Sind wir die Bösen?"</b>', H2),
        p('Diese Frage stellt sich Ihr Anwalt nach dem BGH-Urteil tatsächlich. '
          'Nicht als Selbstkritik, sondern als rechtspolitische Reflexion:', BODY),
        p('Auf der einen Seite: Frau Pferdedrescher-Riesenstein hat als Vermieterin '
          'ein legitimes Interesse, säumige Mieter auf effizientem Weg zu kündigen. '
          'Das Online-Format (qES-Mail) ist technisch sicher, rechtlich vorgesehen '
          'und ökologisch sinnvoll.', BODY),
        p('Auf der anderen Seite: Mieter — insbesondere ältere oder technikferne '
          'Mieter — würden durch eine flächendeckende Einführung der qES-E-Mail-Kündigung '
          'erheblich belastet. Wer kein Smartphone hat und kein PDF-Leseprogramm, '
          'kann eine qES nicht prüfen. Der Mieterschutz-Gedanke des § 568 BGB '
          '(Warnfunktion der Schriftform!) würde ausgehöhlt.', BODY),
        p('<b>Ergebnis:</b> Wir sind nicht die Bösen. Aber wir müssen die Frage '
          'zulässigerweise stellen.', BOLD),
        sp(8),
        p('Dr. Engelbert Ranftenschwedler-Bielenfels', BOLD),
        p('Rechtsanwalt', SMALL),
        pb(),
    ]
    return elems


# ── 26. HANDSCHRIFTLICHE NOTIZEN ───────────────────────────────────────────────
def teil_26_handschriftnotizen():
    elems = section_header("Teil XXVI", "HANDSCHRIFTLICHE NOTIZEN EBERHART-WOLFRAMSHAUSEN")
    elems += [
        p('<i>Die folgenden handschriftlichen Notizen wurden von Herrn Eberhart-Wolframshausen '
          'an den Rändern seiner Schriftsätze und Urteilsausfertigungen angebracht. '
          'Sie wurden für die Akte transkribiert und kursiv wiedergegeben.</i>', ITALIC),
        sp(8),
        p('Auf der Klageschrift vom 09.03.2022, Seite 1:', SMALL),
        p('<i>„Sie hat mir das per WhatsApp geschickt!!! Unglaublich. '
          'Ich bin IT-Admin — denkt sie ich erkenne keine unsignierte PDF?"</i>', HAND),
        sp(6),
        p('Auf der Klageerwiderung (eigene), Seite 2:', SMALL),
        p('<i>„Muss das wirklich so teuer werden? Ich zahle doch. '
          'Nur halt nicht immer pünktlich. Wo ist das Problem???"</i>', HAND),
        sp(6),
        p('Auf dem Hinweisbeschluss AG Bielefeld vom 11.04.2022:', SMALL),
        p('<i>„§ 298 Abs. 3 ZPO Transfervermerk. Das Gericht VERSTEHT das Problem! '
          'Ein Papier IST KEIN elektronisches Dokument. '
          'Ich wette der BGH sieht das genauso."</i>', HAND),
        sp(6),
        p('Auf dem Urteil AG Bielefeld 11.10.2022:', SMALL),
        p('<i>„GEWONNEN!!! Erstinstanz. Jetzt Berufung. '
          'Muss ich einen Anwalt nehmen? Ja, lieber."</i>', HAND),
        sp(6),
        p('Auf dem LG-Urteil 20.06.2023:', SMALL),
        p('<i>„Berufung auch gewonnen. Revision zugelassen. BGH wird es endgültig klären. '
          'Ich habe Recht gehabt. § 130 BGB. Zugang in der Form. Punkt."</i>', HAND),
        sp(6),
        p('Auf der BGH-Urteilsausfertigung 27.11.2024:', SMALL),
        p('<i>„BGH. Gewonnen. Leitsatz c) ist MEIN Argument aus der eigenhändigen '
          'Klageerwiderung vom April 2022. Für einen IT-Admin ohne Jura-Studium '
          'nicht schlecht, oder? 😄 '
          'Ob ich jetzt Mietrecht-Youtuber werde..."</i>', HAND),
        sp(6),
        p('<i>„P.S. Frau Pferdedrescher-Riesenstein hat immer noch keinen SPF-Record '
          'repariert. Ich erhalte gelegentlich ihre Webshop-Mails im Spam-Ordner. '
          'Echte Frechheit als IT-Admin behandelt zu werden, als ob ich '
          'keine qES erkennen würde."</i>', HAND),
        pb(),
    ]
    return elems


# ── 27. E-MAIL-KETTE ───────────────────────────────────────────────────────────
def teil_27_emailkette():
    elems = section_header("Teil XXVII",
                           "E-MAIL-KETTE RANFTENSCHWEDLER ↔ PFERDEDRESCHER-RIESENSTEIN")
    elems += [
        p('<b>Auswahl aus der Korrespondenz (Feb. 2022 – Nov. 2024)</b>', BOLD),
        sp(6),
    ]
    emails = [
        ("hildegunde.pferdedrescher-riesenstein@online-marketing-bielefeld.de",
         "kanzlei@ranftenschwedler-ostkamp.de",
         "11. Februar 2022, 08:01",
         "DRINGEND — Kündigung Eberhart",
         ["Lieber Herr Dr. Ranftenschwedler-Bielenfels,",
          "ich bin völlig verzweifelt. Der Mieter hat mir eine E-Mail geschickt",
          "und behauptet meine Kündigung sei ungültig. Stimmt das?",
          "Er ist IT-Admin und denkt er ist der Klügste.",
          "Ich brauche eine Räumungsklage. Sofort. Was kostet das?",
          "Beste Grüße, Hildegunde"],
        ),
        ("kanzlei@ranftenschwedler-ostkamp.de",
         "hildegunde.pferdedrescher-riesenstein@online-marketing-bielefeld.de",
         "11. Februar 2022, 14:33",
         "Re: DRINGEND — Kündigung Eberhart",
         ["Sehr geehrte Frau Pferdedrescher-Riesenstein,",
          "leider hat der Mieter mit seiner Einschätzung Recht. Ich erkläre",
          "die Details in dem beigefügten Memo (s. Teil VIII dieser Akte).",
          "Wir müssen eine neue, formwirksame Kündigung erklären.",
          "Beste Grüße, Dr. Ranftenschwedler-Bielenfels"],
        ),
        ("hildegunde.pferdedrescher-riesenstein@online-marketing-bielefeld.de",
         "kanzlei@ranftenschwedler-ostkamp.de",
         "28. Oktober 2022, 09:15",
         "AG-Urteil — was jetzt?",
         ["Herr Dr. Ranftenschwedler-Bielenfels,",
          "das AG hat die Klage abgewiesen. Ich bin fassungslos.",
          "Dieser IT-Admin hat OHNE ANWALT gewonnen!",
          "Ich zahle alles was ich zahlen muss — Berufung bitte!",
          "H. Pferdedrescher-Riesenstein"],
        ),
        ("kanzlei@ranftenschwedler-ostkamp.de",
         "hildegunde.pferdedrescher-riesenstein@online-marketing-bielefeld.de",
         "02. November 2022, 16:44",
         "Re: AG-Urteil — Berufung empfohlen",
         ["Die Rechtsfrage hat grundsätzliche Bedeutung.",
          "Wir haben gute Chancen auf Revision. Aber ehrlich gesagt:",
          "Das Argument des Mieters ist nicht leicht zu schlagen.",
          "Kostenschätzung Berufung: EUR 4.500-6.000.",
          "Ihr Entscheid, Frau Pferdedrescher-Riesenstein.",
          "Dr. Ranftenschwedler-Bielenfels"],
        ),
        ("hildegunde.pferdedrescher-riesenstein@online-marketing-bielefeld.de",
         "kanzlei@ranftenschwedler-ostkamp.de",
         "20. Juni 2023, 18:22",
         "LG auch verloren. Verzweifelt.",
         ["Auch das LG hat verloren. Ich verstehe die Welt nicht mehr.",
          "Mein Mieter wohnt gratis und ich zahle die Anwaltskosten.",
          "Soll ich wirklich zum BGH? Das kostet doch ein Vermögen.",
          "H. Pferdedrescher-Riesenstein",
          "",
          "P.S.: Ich habe jetzt meinen SPF-Record repariert."],
        ),
        ("kanzlei@ranftenschwedler-ostkamp.de",
         "hildegunde.pferdedrescher-riesenstein@online-marketing-bielefeld.de",
         "28. November 2024, 07:55",
         "BGH — Revision abgewiesen. Tut mir leid.",
         ["Sehr geehrte Frau Pferdedrescher-Riesenstein,",
          "gestern hat der BGH die Revision zurückgewiesen. Leitsatz c):",
          "Ausdruck + Transfervermerk = kein formwirksamer Zugang. Punkt.",
          "Der Mieter-IT-Admin hatte von Anfang an Recht.",
          "Detailliertes Memo folgt (s. Teil XXIV).",
          "Mit aufrichtigem Bedauern,",
          "Dr. Ranftenschwedler-Bielenfels"],
        ),
    ]
    for s, r, d, sub, body in emails:
        elems += email_block(s, r, d, sub, body)
    elems.append(pb())
    return elems


# ── 28. KOSTENFESTSETZUNG ─────────────────────────────────────────────────────
def teil_28_kosten():
    elems = section_header("Teil XXVIII", "KOSTENFESTSETZUNGSBESCHLUSS-ENTWURF")
    elems += [
        p('<b>AMTSGERICHT BIELEFELD</b>', CENTER_BOLD),
        p('Az.: 34 C 421/22 | KOSTENFESTSETZUNGSBESCHLUSS (Entwurf)', CENTER),
        sp(6), hr(), sp(4),
        p('<b>Streitwert-Berechnung</b>', H2),
        Table([
            ['Streitwertposition', 'Betrag (€)'],
            ['Räumungsantrag (§ 41 GKG — Jahresbruttomiete)', '7.787,64'],
            ['Zahlungsantrag (Rückstand Feb. 2022)', '1.696,31'],
            ['Gesamtstreitwert 1. Instanz', '9.483,95'],
        ], colWidths=[350, 100]),
        sp(6),
        p('<b>Kosten AG-Instanz (§ 91 ZPO — Klägerin trägt alle Kosten)</b>', H2),
        Table([
            ['Kostenpositionen', 'Betrag (€)'],
            ['Gerichtskosten AG (3 Gebühren aus Streitwert EUR 9.483,95)', '570,00'],
            ['RA-Kosten Beklagter (1,3 VG + 1,2 TG + Auslagenpauschale + USt.)', '1.285,90'],
            ['Eigene RA-Kosten Klägerin (nicht erstattungsfähig)', '2.340,00'],
            ['Gesamt AG-Instanz (Klägerin-Last)', '4.195,90'],
        ], colWidths=[350, 100]),
        sp(6),
        p('<b>Kosten LG-Instanz + BGH (Schätzung)</b>', H2),
        Table([
            ['Instanz', 'Gerichtskosten (€)', 'RA-Kosten Beklagter (€)'],
            ['LG Bielefeld', '855,00', '1.840,00'],
            ['BGH', '1.425,00', '3.200,00'],
            ['Gesamt', '2.280,00', '5.040,00'],
        ], colWidths=[200, 125, 125]),
        sp(6),
        BoxedPara(
            '<b>Gesamtkosten-Übersicht (Klägerin-Belastung):</b><br/>'
            'AG: EUR 4.195,90 | LG: EUR 2.695,00 | BGH: EUR 4.625,00<br/>'
            '<b>Summe aller Instanzen: ca. EUR 11.515,90</b><br/>'
            'zzgl. eigene RA-Kosten aller Instanzen (ca. EUR 12.400,00)<br/>'
            'zzgl. entgangene Miete / Nutzungsentschädigung (ca. EUR 4.500,00)<br/>'
            '<b>= Gesamtschaden Klägerin: ca. EUR 28.415,90</b>',
            bg=C_RED_LIGHT, border=C_RED,
            style=S('kosten_s', fontName='Helvetica', fontSize=9.5, leading=15, textColor=C_BLACK)
        ),
        pb(),
    ]
    return elems


# ── 29. ANLAGENVERZEICHNIS ────────────────────────────────────────────────────
def teil_29_anlagen():
    anlagen = [
        ("K-MIET-1",  "Mietvertrag vom 03.04.2017 (Original)", "Sonderband II"),
        ("K-MIET-2",  "Kontoauszug Mietkonto Feb. 2017 – Feb. 2022", "in Akte"),
        ("K-MIET-3",  "WhatsApp-Screenshots 08.-10.02.2022 (Ausdruck)", "in Akte"),
        ("K-MIET-4",  "E-Mail Pferdedrescher-Riesenstein 10.02.2022 (Ausdruck)", "in Akte"),
        ("K-MIET-5",  "Antwort-Mail Eberhart-Wolframshausen 11.02.2022", "in Akte"),
        ("K-MIET-6",  "Grundbuchauszug Eckendorfer Str. 188 (Blatt 4721)", "Sonderband II"),
        ("K-MIET-7",  "Mietpreisspiegel Bielefeld 2017", "Sonderband II"),
        ("K-MIET-8",  "Nebenkostenabrechnung 2019", "in Akte"),
        ("K-MIET-9",  "Nebenkostenabrechnung 2020", "in Akte"),
        ("K-MIET-10", "Nebenkostenabrechnung 2021", "in Akte"),
        ("K-MIET-11", "Fotos Wohnung Zustand April 2022 (Übergabeprotokoll 2017)", "Sonderband II"),
        ("K-MIET-12", "Anwaltsschreiben RA Ranftenschwedler-Bielenfels 15.02.2022", "in Akte"),
        ("K-MIET-13", "Anmeldebestätigung qES-Zertifikat D-Trust (fiktiv)", "in Akte"),
        ("K-MIET-14", "beA-Eingangsbestätigung Klageschrift 09.03.2022", "in Akte"),
        ("K-MIET-15", "Zustellungsurkunde Klageschrift (Postzustellung 17.03.2022)", "in Akte"),
        ("K-MIET-16", "beA-Eingangsbestätigung Replik 13.05.2022", "in Akte"),
        ("K-MIET-17", "Zustellungsurkunde Replik (Postzustellung 20.05.2022)", "in Akte"),
        ("K-MIET-18", "Sitzungsprotokoll AG Bielefeld 14.09.2022", "in Akte"),
        ("K-MIET-19", "Urteil AG Bielefeld 11.10.2022 (Urteilsausfertigung)", "in Akte"),
        ("K-MIET-20", "Berufungsschrift 12.11.2022", "in Akte"),
        ("K-MIET-21", "Berufungsbegründung 28.01.2023", "in Akte"),
        ("K-MIET-22", "Berufungserwiderung Hassenstein-Heepen 15.03.2023", "in Akte"),
        ("K-MIET-23", "Urteil LG Bielefeld 20.06.2023 (Urteilsausfertigung)", "in Akte"),
        ("K-MIET-24", "Revisionsbegründung 28.08.2023", "in Akte"),
        ("K-MIET-25", "Revisionserwiderung 04.10.2023", "in Akte"),
        ("K-MIET-26", "BGH-Urteil VIII ZR 159/23 vom 27.11.2024 (Originalausfertigung)", "in Akte"),
        ("K-MIET-27", "Pressemitteilung BGH Nr. 220/2024 (Parallelsache VIII ZR 155/23)", "in Akte"),
        ("K-MIET-28", "Mandatsvereinbarung RA Ranftenschwedler-Bielenfels Feb. 2022", "Sonderband II"),
        ("K-MIET-29", "Mandatsvereinbarung RA Hassenstein-Heepen Dez. 2022", "Sonderband II"),
        ("K-MIET-30", "Stundenaufstellung Ranftenschwedler Ostkamp", "in Akte"),
        ("K-MIET-31", "WhatsApp-Backup Pferdedrescher-Riesenstein (Rohdaten)", "Sonderband II"),
        ("K-MIET-32", "Screenshot Webshop-Kontaktformular (SPF-Fehler)", "in Akte"),
        ("K-MIET-33", "Vollmacht Pferdedrescher-Riesenstein → RA Ranftenschwedler", "in Akte"),
        ("K-MIET-34", "Vollmacht Eberhart-Wolframshausen → RA Hassenstein-Heepen", "in Akte"),
    ]
    rows = [["Anlage", "Bezeichnung", "Fundstelle"]]
    for az, bez, fund in anlagen:
        rows.append([az, bez, fund])

    ts = TableStyle([
        ('BACKGROUND',  (0,0), (-1,0), C_ACCENT),
        ('TEXTCOLOR',   (0,0), (-1,0), C_WHITE),
        ('FONTNAME',    (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',    (0,0), (-1,-1), 8),
        ('FONTNAME',    (0,1), (-1,-1), 'Helvetica'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, colors.HexColor("#F7F6F2")]),
        ('GRID',        (0,0), (-1,-1), 0.3, C_LIGHT_GREY),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING',(0,0), (-1,-1), 5),
        ('TOPPADDING',  (0,0), (-1,-1), 3),
        ('BOTTOMPADDING',(0,0), (-1,-1), 3),
    ])
    tbl = Table(rows, colWidths=[70, 300, 80])
    tbl.setStyle(ts)

    elems = section_header("Teil XXIX", "ANLAGENVERZEICHNIS K-MIET-1 bis K-MIET-34")
    elems += [
        p('Akte Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen — 34 C 421/22', SMALL),
        sp(6), tbl, sp(6),
        p('<i>Hinweis: Anlagen „Sonderband II" sind in der vorliegenden fragmentarischen '
          'Testakte nicht beigefügt. Sie sind bei der Geschäftsstelle AG Bielefeld unter '
          'Az. 34 C 421/22 zu Sonderband II einzusehen.</i>', ITALIC),
        pb(),
    ]
    return elems


# ── 30. STUNDENAUFSTELLUNG ────────────────────────────────────────────────────
def teil_30_stundenaufstellung():
    stunden = [
        ("Feb. 2022", "Erstberatung, Memo Formunwirksamkeit, Klageschrift", "18,5", "280,00", "5.180,00"),
        ("Mrz. 2022", "Klageschrift Finalisierung, beA-Einreichung, Korrespondenz", "12,0", "280,00", "3.360,00"),
        ("Apr. 2022", "Hinweisbeschluss, Sachverhaltsaufklärung Mietzahlungen", "6,5", "280,00", "1.820,00"),
        ("Mai 2022", "Replik, erneute Kündigung, qES-Signatur Schriftsatz", "9,0", "280,00", "2.520,00"),
        ("Jun–Aug 2022", "Laufende Beratung, Terminvorbereitung", "5,0", "280,00", "1.400,00"),
        ("Sep. 2022", "Mündliche Verhandlung AG + Vorbereitung", "4,5", "280,00", "1.260,00"),
        ("Okt. 2022", "Urteil AG, Beratung Berufung, Berufungsschrift", "7,0", "280,00", "1.960,00"),
        ("Nov 2022–Jan 2023", "Berufungsbegründung (8 Seiten)", "14,0", "280,00", "3.920,00"),
        ("Feb–Mai 2023", "Berufungserwiderung gegnerisch, Duplik", "6,0", "280,00", "1.680,00"),
        ("Jun. 2023", "LG-Urteil, Revisionsentscheidung, Mandantenberatung", "5,5", "280,00", "1.540,00"),
        ("Jul–Sep 2023", "Revisionsbegründung, BGH-Zulassung", "14,0", "280,00", "3.920,00"),
        ("Okt 2023–Okt 2024", "Laufende Betreuung, Schriftverkehr, BGH-Vorbereitung", "8,0", "280,00", "2.240,00"),
        ("Nov. 2024", "BGH-Verhandlung Karlsruhe + Reise, Nachbereitung, Memo", "12,0", "280,00", "3.360,00"),
        ("Dez. 2024", "Mandantenberatung, Abschluss-Memos, Abrechnung", "6,0", "280,00", "1.680,00"),
    ]
    rows = [["Zeitraum", "Tätigkeit", "h", "Satz (€/h)", "Gesamt (€)"]]
    total = 0.0
    for r in stunden:
        rows.append(list(r))
        total += float(r[4].replace(",","").replace(".", ""))
    rows.append(["", "<b>Gesamt netto</b>", "", "", f"<b>{sum(float(r[4].replace(',','').replace('.',''))/100 for r in stunden):.2f}</b>"])
    
    # Compute total properly
    total_h = sum(float(r[2].replace(",",".")) for r in stunden)
    total_eur = total_h * 280
    rows[-1] = ["", "Gesamt netto", f"{total_h:.1f} h", "", f"EUR {total_eur:,.2f}"]

    ts = TableStyle([
        ('BACKGROUND',  (0,0), (-1,0), C_ACCENT),
        ('TEXTCOLOR',   (0,0), (-1,0), C_WHITE),
        ('FONTNAME',    (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',    (0,0), (-1,-1), 8),
        ('FONTNAME',    (0,1), (-1,-1), 'Helvetica'),
        ('FONTNAME',    (0,-1), (-1,-1), 'Helvetica-Bold'),
        ('BACKGROUND',  (0,-1), (-1,-1), colors.HexColor("#E8F5E9")),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [C_WHITE, colors.HexColor("#F7F6F2")]),
        ('GRID',        (0,0), (-1,-1), 0.3, C_LIGHT_GREY),
        ('ALIGN',       (2,0), (-1,-1), 'RIGHT'),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING',(0,0), (-1,-1), 5),
        ('TOPPADDING',  (0,0), (-1,-1), 3),
        ('BOTTOMPADDING',(0,0), (-1,-1), 3),
    ])
    tbl = Table(rows, colWidths=[100, 235, 30, 55, 70])
    tbl.setStyle(ts)

    elems = section_header("Teil XXX",
                           "STUNDENAUFSTELLUNG RANFTENSCHWEDLER OSTKAMP (Feb. 2022 – Nov. 2024)")
    elems += [
        p('Kanzlei Ranftenschwedler Ostkamp Rechtsanwälte mbB, Niederwall 12, 33602 Bielefeld', SMALL),
        p('Mandantin: Hildegunde Pferdedrescher-Riesenstein | Az.: RO/2022/0312/PKT', SMALL),
        p('<i>Fiktive Aufstellung — Testakte</i>', SMALL),
        sp(6),
        tbl,
        sp(6),
        p(f'Nettobetrag: EUR {total_eur:,.2f} | zzgl. 19% USt. = '
          f'EUR {total_eur * 1.19:,.2f} brutto', BOLD),
        p('<i>zzgl. Auslagen (Reise Karlsruhe, Kopien, Porti, beA-Gebühren): ca. EUR 1.240,00</i>',
          ITALIC),
        sp(4),
        BoxedPara(
            'GESAMTRECHNUNG KANZLEI RO (Schätzung netto):\n'
            f'Honorar: EUR {total_eur:,.2f}\n'
            'Auslagen: EUR 1.240,00\n'
            f'Gesamt netto: EUR {total_eur + 1240:,.2f}\n'
            f'19% USt.: EUR {(total_eur + 1240) * 0.19:,.2f}\n'
            f'Gesamt brutto: EUR {(total_eur + 1240) * 1.19:,.2f}',
            bg=colors.HexColor("#FFF9C4"), border=colors.HexColor("#F57F17"),
            style=S('total_s', fontName='Helvetica-Bold', fontSize=9.5, leading=15, textColor=C_BLACK)
        ),
        sp(6),
        p('Ende der Testakte Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen.', CENTER),
        p('Az. AG Bielefeld 34 C 421/22 | LG Bielefeld 14 S 88/23 | BGH VIII ZR 159/23', CENTER),
        p('<b>BGH-Urteil: Revision zurückgewiesen — 27. November 2024</b>',
          S('fin', fontName='Helvetica-Bold', fontSize=10, alignment=TA_CENTER, textColor=C_RED)),
        sp(4),
        p('⚠ FIKTIVE TESTAKTE — Alle Personen, Adressen und Aktenzeichen (außer BGH VIII ZR 159/23) '
          'sind erfunden. Das BGH-Urteil ist real.',
          S('footer_warn', fontName='Helvetica-Oblique', fontSize=8,
            alignment=TA_CENTER, textColor=C_MID_GREY)),
    ]
    return elems


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE TEMPLATE (Header / Footer)
# ═══════════════════════════════════════════════════════════════════════════════

class NumberedCanvas(pdfcanvas.Canvas):
    def __init__(self, *args, **kwargs):
        pdfcanvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            pdfcanvas.Canvas.showPage(self)
        pdfcanvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.saveState()
        # Header
        self.setFont("Helvetica", 7)
        self.setFillColor(C_MID_GREY)
        self.drawString(2*cm, H - 1.2*cm,
                        "TESTAKTE · Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen · "
                        "Az. 34 C 421/22 / LG 14 S 88/23 / BGH VIII ZR 159/23")
        self.drawRightString(W - 2*cm, H - 1.2*cm, "⚠ FIKTIV")
        self.setStrokeColor(C_LIGHT_GREY)
        self.setLineWidth(0.3)
        self.line(2*cm, H - 1.4*cm, W - 2*cm, H - 1.4*cm)
        # Footer
        self.line(2*cm, 1.8*cm, W - 2*cm, 1.8*cm)
        self.setFont("Helvetica", 7)
        self.drawString(2*cm, 1.2*cm, "BGH VIII ZR 159/23 · Schriftform Mietkündigung · Bielefeld-Variante")
        self.drawCentredString(W/2, 1.2*cm,
                               f"Seite {self._pageNumber} von {page_count}")
        self.drawRightString(W - 2*cm, 1.2*cm, "Ranftenschwedler Ostkamp RA mbB")
        self.restoreState()


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN BUILD
# ═══════════════════════════════════════════════════════════════════════════════


# ═══════════════════════════════════════════════════════════════════════════════
# EXTENDED CONTENT — added to reach target page count (70-100)
# ═══════════════════════════════════════════════════════════════════════════════

def erweiterung_rechtsgutachten():
    """Rechtsgutachten des Anwalts zur qES-Kündigung direkt per E-Mail."""
    elems = [pb()]
    elems += section_header("ANHANG A", "RECHTSGUTACHTEN: qES-Kündigung direkt per E-Mail an Mieter")
    elems += [
        p('<b>Ranftenschwedler Ostkamp Rechtsanwälte mbB</b>',
          S('rg_h', fontName='Helvetica-Bold', fontSize=11, textColor=C_ACCENT)),
        p('RECHTSGUTACHTEN', BOLD),
        p('Betreff: Wirksamkeit einer qES-signierten Kündigung direkt per E-Mail an Mieter', BOLD),
        p('Mandantin: Hildegunde Pferdedrescher-Riesenstein', SMALL),
        p('Datum: Januar 2023 (erstellt für Berufungsverfahren 14 S 88/23)', SMALL),
        sp(6), hr(), sp(4),
        p('<b>A. Gutachtenfrage</b>', H2),
        p('Hätte Frau Pferdedrescher-Riesenstein die Kündigung als qES-signiertes PDF '
          '<b>direkt per E-Mail</b> an Herrn Eberhart-Wolframshausen verschickt (statt '
          'über Gerichtsschriftsatz), wäre sie formwirksam zugegangen?', BODY),
        sp(4),
        p('<b>B. Rechtlicher Rahmen</b>', H2),
        p('<b>I. Schriftformerfordernis (§ 568 Abs. 1 BGB)</b>', H3),
        p('§ 568 Abs. 1 BGB verlangt die Schriftform für die Kündigung eines '
          'Wohnraummietverhältnisses. Nach § 126 Abs. 3 BGB kann die Schriftform '
          'durch die elektronische Form ersetzt werden, wenn das Gesetz nichts anderes bestimmt. '
          '§ 568 BGB enthält — anders als §§ 623, 766 S. 2, 780 S. 2, 781 S. 2 BGB — '
          'keinen Ausschluss der elektronischen Form. '
          'Ergebnis: Eine qES-Kündigung ist grundsätzlich zulässig (§ 126 Abs. 3 BGB).', BODY),
        p('<b>II. Elektronische Form (§ 126a BGB)</b>', H3),
        p('§ 126a Abs. 1 BGB setzt voraus:', BODY),
        p('(1) Der Aussteller fügt dem elektronischen Dokument seinen Namen hinzu, und', BODY_L),
        p('(2) versieht es mit einer qualifizierten elektronischen Signatur (qES).', BODY_L),
        p('Beides ist bei einem qES-signierten PDF erfüllt. Die qES identifiziert den Aussteller '
          'eindeutig und gewährleistet die Unverfälschtheit des Dokuments.', BODY),
        p('<b>III. Zugangserfordernis (§ 130 Abs. 1 S. 1 BGB)</b>', H3),
        p('Nach § 130 Abs. 1 S. 1 BGB wird eine empfangsbedürftige Willenserklärung '
          'wirksam, wenn sie dem Erklärungsgegner <b>zugeht</b>. '
          'Für die elektronische Form gilt: Die Erklärung muss dem Erklärungsgegner '
          'in der vorgeschriebenen Form zugehen.', BODY),
        p('Der BGH (VIII ZR 159/23, Leitsatz a)) hat klargestellt: Für den Zugang '
          'einer qES-Erklärung ist erforderlich, dass das elektronische Dokument so '
          'in den Machtbereich des Empfängers gelangt, dass dieser die qES und damit '
          'die Echtheit des Dokuments prüfen kann.', BODY),
        sp(4),
        p('<b>C. Direktzustellung per E-Mail — Analyse</b>', H2),
        p('<b>Fall 1: Frau Pferdedrescher-Riesenstein schickt qES-PDF direkt per E-Mail</b>', H3),
        p('Sachverhalt: Das qES-signierte Kündigungs-PDF wird als E-Mail-Anhang an '
          'g.eberhart-wolframshausen@privat-mail.de verschickt.', BODY),
        p('<b>a) Formgerechte Abgabe:</b> Das Dokument ist mit qES versehen und '
          'enthält den Namen der Erklärenden. § 126a Abs. 1 BGB ist erfüllt.', BODY),
        p('<b>b) Formgerechter Zugang:</b> Die E-Mail gelangt in den Machtbereich '
          'des Beklagten. Als IT-Administrator und Nutzers von g.eberhart-wolframshausen@privat-mail.de '
          'ist davon auszugehen, dass er die E-Mail abruft und den PDF-Anhang öffnen kann.', BODY),
        p('<b>c) Verifikationsmöglichkeit:</b> Der Beklagte empfängt das elektronische '
          'Originaldokument im qES-Format. Mit Adobe Acrobat Reader (kostenlos) oder '
          'einem anderen PDF-Validierungstool kann er die Signatur prüfen. '
          'Als IT-Admin ist dies für ihn trivial.', BODY),
        BoxedPara(
            '<b>Ergebnis (Gutachten):</b> Eine qES-Kündigung, die dem Mieter direkt per '
            'E-Mail als elektronisches Original-PDF übermittelt wird, wäre — bei '
            'Zugang des E-Mail-Anhangs im Machtbereich des Mieters — formwirksam '
            'i.S.v. §§ 568 Abs. 1, 126 Abs. 3, 126a BGB i.V.m. § 130 BGB zugegangen.<br/><br/>'
            'VORAUSSETZUNG: Das elektronische Original muss übermittelt werden. '
            'Ein Screenshot des PDFs oder ein Re-Scan wäre nicht ausreichend. '
            'Die qES muss am empfangenen Dokument durch den Empfänger prüfbar sein.',
            bg=colors.HexColor("#E8F5E9"), border=colors.HexColor("#2E7D32"),
            style=S('gut_res', fontName='Helvetica', fontSize=9.5, leading=15, textColor=C_BLACK)
        ),
        sp(6),
        p('<b>D. Praktische Hinweise für die Mandantin</b>', H2),
        p('<b>1. qES erwerben:</b> Frau Pferdedrescher-Riesenstein benötigt ein '
          'qualifiziertes Zertifikat, z.B. von der Bundesdruckerei (D-Trust), '
          'Telesec oder certSIGN. Kosten: ca. EUR 50–120/Jahr. '
          'Ausweis-basierte Identifizierung erforderlich (VideoIdent oder persönlich).', BODY),
        p('<b>2. Signiervorgang:</b> Das Kündigungs-PDF wird mit einer geeigneten '
          'Signatur-Software (z.B. D-Trust sign it!, Adobe Acrobat mit PKI-Plugin) '
          'qualifiziert elektronisch signiert. Ergebnis: PDF mit eingebetteter qES.', BODY),
        p('<b>3. Versand:</b> Das signierte PDF per E-Mail direkt an die bekannte '
          'E-Mail-Adresse des Mieters versenden. Ggf. Lesebestätigung anfordern. '
          'Empfehlenswert: zusätzlich Einschreiben/Rückschein als Sicherungskopie.', BODY),
        p('<b>4. Dokumentation:</b> Den Versand dokumentieren: Sendeprotokoll der '
          'E-Mail, Screenshot des Outbox-Eintrags, ggf. Serverlog.', BODY),
        p('<b>5. Keine Garantie bei unbekannten E-Mail-Adressen:</b> Hat der Mieter '
          'keine E-Mail-Adresse angegeben, muss die Kündigung auf dem klassischen '
          'Schriftweg (eigenhändige Unterschrift auf Papier) erfolgen.', BODY),
        sp(6),
        p('<b>E. Kritische Würdigung: Risiken der qES-Mail-Kündigung</b>', H2),
        p('<b>Risiko 1 — Zustellungsnachweis:</b> Bei einem gerichtlichen Streit '
          'ist der Zugang der E-Mail schwer zu beweisen. Anders als beim Einschreiben '
          'gibt es keine objektive Zustellungsdokumentation. Lösung: '
          'qualifizierten Zustellungsdienst nutzen oder Zusendung per Boten (Zeuge) '
          'mit Übergabe auf USB-Stick als Backup.', BODY),
        p('<b>Risiko 2 — Spam-Filter:</b> Die E-Mail könnte im Spam-Ordner des Mieters '
          'landen. Dies geht zu Lasten des Erklärenden. '
          'Herr Eberhart-Wolframshausen hat selbst darauf hingewiesen '
          '(„SPF-Record falsch konfiguriert"). '
          'Abhilfe: SPF-Record korrekt konfigurieren (s. schon seine E-Mail v. 08.02.2022!).', BODY),
        p('<b>Risiko 3 — Wechsel der E-Mail-Adresse:</b> Hat der Mieter seine '
          'E-Mail-Adresse gewechselt und war dies der Vermieterin nicht mitgeteilt, '
          'trifft den Mieter das Risiko nach allgemeinen Zugangsgrundsätzen. '
          'Im Zweifel: vorherige Nachfrage per separater E-Mail zur Adressvalidierung.', BODY),
        sp(8),
        p('Dr. Engelbert Ranftenschwedler-Bielenfels', BOLD),
        p('Rechtsanwalt | Fachanwalt für Miet- und WEG-Recht', SMALL),
        p('<i>Erstellt Januar 2023 für das Berufungsverfahren LG Bielefeld 14 S 88/23</i>', FOOTNOTE),
    ]
    return elems


def erweiterung_vergleichsverhandlung():
    """Ergänzender Abschnitt: Vergleichsverhandlungen."""
    elems = [pb()]
    elems += section_header("ANHANG B", "VERGLEICHSVERHANDLUNGEN — Chronik der gescheiterten Einigungsversuche")
    elems += [
        p('<b>Zusammenfassung der Vergleichsgespräche (Feb. 2022 – Okt. 2023)</b>', BOLD),
        sp(4),
        p('Im Verlauf des Verfahrens wurden mehrfach Einigungsversuche unternommen. '
          'Die folgende Chronik dokumentiert die wesentlichen Meilensteine.', BODY),
        sp(4),
        p('<b>1. Direktgespräch zwischen den Parteien (Februar 2022)</b>', H2),
        p('Nach dem Erhalt der unwirksamen Kündigung am 10.02.2022 und seiner '
          'sachkundigen Antwort-Mail vom 11.02.2022 hat Herr Eberhart-Wolframshausen '
          'telefonisch Kontakt mit Frau Pferdedrescher-Riesenstein aufgenommen. '
          'Er hat angeboten, die Rückstände in Raten zu begleichen (EUR 200,00/Monat '
          'zusätzlich zur laufenden Miete).', BODY),
        p('Frau Pferdedrescher-Riesenstein hat das Angebot abgelehnt. '
          'Sie bestand auf sofortiger vollständiger Zahlung des Rückstands '
          'von EUR 1.696,31.', BODY),
        BoxedPara(
            'RA Ranftenschwedler-Bielenfels intern: „Das war ein Fehler. '
            'Bei einem Rückstand von EUR 1.696,31 wäre ein Ratenzahlungsvergleich '
            'sinnvoll gewesen. Frau Pferdedrescher-Riesenstein hatte keine Rücksicht '
            'auf die Formunwirksamkeit ihrer Kündigung genommen und überschätzte '
            'ihre Position erheblich."',
            bg=C_STAMP_BG, border=C_STAMP_BD,
            style=S('vgl_intern', fontName='Helvetica-Oblique', fontSize=9,
                    leading=13, textColor=C_BLACK)
        ),
        sp(6),
        p('<b>2. Güteversuch nach § 278 ZPO (September 2022, vor der mündlichen Verhandlung)</b>',
          H2),
        p('Das Amtsgericht hat in der Ladung auf die Möglichkeit eines Güteversuchs '
          'hingewiesen. RA Ranftenschwedler-Bielenfels hat Herrn Eberhart-Wolframshausen '
          '(damals noch ohne Anwalt) ein Vergleichsangebot übermittelt:', BODY),
        Table([
            ['Vergleichsangebot Klägerin (Sept. 2022)', ''],
            ['Forderungsverzicht Räumung:', 'sofern Zahlung EUR 1.500,00 bis 30.09.2022'],
            ['Mietverhältnis:', 'Fortsetzung unter erhöhter Miete EUR 680,00/Monat'],
            ['Rückstandsregelung:', 'EUR 50,00/Monat Zuschlag bis Tilgung'],
            ['Schriftformklausel:', 'Ergänzung: elektronische Kommunikation ausgeschlossen'],
        ], colWidths=[280, 180]),
        sp(4),
        p('Eberhart-Wolframshausen: "Ich lehne das ab. Ich habe die Verhandlung '
          'bereits gewonnen — formell gesehen. Das Gericht wird mir Recht geben."', CITE),
        p('<i>[Anm. d. Red.: Er sollte Recht behalten.]</i>', ITALIC),
        sp(6),
        p('<b>3. Mediationsangebot nach AG-Urteil (November 2022)</b>', H2),
        p('Nach dem AG-Urteil (11.10.2022, Klage abgewiesen) hat RA Hassenstein-Heepen '
          '(frisch mandatiert für die Berufungsinstanz) seinem Mandanten geraten, '
          'eine Mediation anzubieten.', BODY),
        p('Eberhart-Wolframshausen: "Nein. Ich habe gewonnen. Sie soll Berufung einlegen, '
          'damit auch das LG und dann der BGH das bestätigen. Das ist wichtig für '
          'alle Mieter in Deutschland."', BODY),
        p('<i>[Anm. RA Hassenstein-Heepen intern: „Mein Mandant ist hartnäckig. '
          'Aus anwaltlicher Sicht: Er hat Recht, dass ein BGH-Urteil wichtig ist. '
          'Aus wirtschaftlicher Sicht für ihn: Das Mietrecht ist teuer. '
          'Aber der Gerichtskosten trägt ja die Gegenseite..."]</i>', ITALIC),
        sp(6),
        p('<b>4. Letzter Vergleichsversuch vor BGH-Urteil (Oktober 2024)</b>', H2),
        p('Einen Monat vor dem BGH-Verhandlungstermin hat RA Ranftenschwedler-Bielenfels '
          'ein finales Vergleichsangebot gemacht:', BODY),
        p('„Frau Pferdedrescher-Riesenstein zahlt EUR 5.000,00 pauschal an '
          'Herrn Eberhart-Wolframshausen für die Anwaltskosten seiner drei Instanzen. '
          'Im Gegenzug zieht Herr Eberhart-Wolframshausen freiwillig aus der Wohnung aus '
          'und muss keine weiteren Rückstände zahlen."', BODY),
        p('RA Hassenstein-Heepen: "Nicht akzeptabel. Mein Mandant schuldet keine '
          'Räumung — es gibt keine wirksame Kündigung. Ein Vergleich käme '
          'einer freiwilligen Aufgabe einer starken Rechtsposition gleich."', BODY),
        BoxedPara(
            '<b>Fazit der Vergleichschronik:</b><br/>'
            'Beide Parteien verhielten sich aus ihrer jeweiligen Perspektive rational. '
            'Frau Pferdedrescher-Riesenstein unterschätzte die Formproblematik anfangs erheblich. '
            'Herr Eberhart-Wolframshausen nutzte seine formelle Stärke konsequent — '
            'und hatte letztlich Recht. '
            'Das wirtschaftliche Ergebnis für beide Parteien war, gemessen an den '
            'Prozesskosten, suboptimal. '
            'Ein frühzeitiger Ratenzahlungsvergleich (Feb. 2022) wäre für alle '
            'Beteiligten besser gewesen.',
            bg=colors.HexColor("#E8F5E9"), border=colors.HexColor("#2E7D32"),
            style=S('vgl_fazit', fontName='Helvetica', fontSize=9.5, leading=15, textColor=C_BLACK)
        ),
    ]
    return elems


def erweiterung_it_admin_analyse():
    """Eberhart-Wolframshausens technische Analyse der qES."""
    elems = [pb()]
    elems += section_header("ANHANG C", "TECHNISCHE ANALYSE: IT-Admin Eberhart-Wolframshausen zur qES")
    elems += [
        BoxedPara(
            '📧 E-MAIL AN DEN EIGENEN ANWALT — nicht für die Akte bestimmt, '
            'aber als Anlage zur Berufungserwiderung gereicht',
            bg=C_LIGHT_GREY, border=C_MID_GREY,
            style=S('it_note', fontName='Helvetica-Oblique', fontSize=8.5,
                    leading=12, textColor=C_DARK_GREY)
        ),
        sp(6),
    ]
    elems += email_block(
        sender="g.eberhart-wolframshausen@privat-mail.de",
        receiver="w.hassenstein-heepen@ra-bielefeld.de",
        date="Freitag, 09. Dezember 2022, 19:44 Uhr",
        subject="Technische Erläuterung qES für Ihre Berufungserwiderung",
        body_lines=[
            "Lieber Herr Hassenstein-Heepen,",
            "",
            "Sie haben mich gebeten, die technischen Aspekte der qualifizierten",
            "elektronischen Signatur (qES) für Ihre Berufungserwiderung zu erläutern.",
            "Als IT-Administrator (CISSP, CompTIA Security+) kann ich dazu folgendes sagen:",
            "",
            "1. WAS IST EINE qES TECHNISCH GESEHEN?",
            "   Eine qES ist eine digitale Signatur auf Basis eines qualifizierten",
            "   Zertifikats eines Trust Service Providers (TSP) gem. eIDAS-VO.",
            "   Technisch: Der Signaturersteller verfügt über ein asymmetrisches",
            "   Schlüsselpaar (privater Schlüssel auf sicherem Gerät, öffentlicher",
            "   Schlüssel im Zertifikat des TSP). Der Hash des Dokuments wird mit dem",
            "   privaten Schlüssel signiert. Der Empfänger kann die Signatur mit dem",
            "   öffentlichen Schlüssel verifizieren.",
            "",
            "2. WARUM IST DER AUSDRUCK MIT TRANSFERVERMERK KEIN ERSATZ?",
            "   Am Papierausdruck existiert keine digitale Signatur mehr.",
            "   Die qES ist eine mathematische Funktion des elektronischen Dokuments.",
            "   Ein Ausdruck ist kein elektronisches Dokument. Punkt.",
            "   Der Transfervermerk ist nur ein Stück Papier, auf dem jemand behauptet,",
            "   die Signatur sei gültig gewesen. Das kann ich nicht selbst prüfen.",
            "   Das wäre wie wenn man eine Banknote kopiert und behauptet,",
            "   die Kopie sei so viel wert wie das Original — weil ja draufsteht,",
            "   dass die Kopie echt ist.",
            "",
            "3. PRÜFUNG DER qES IM ORIGINAL-PDF:",
            "   Hätte mir Frau Pferdedrescher-Riesenstein das qES-signierte PDF",
            "   direkt per E-Mail geschickt, hätte ich folgendes gemacht:",
            "   a) Adobe Acrobat Reader öffnen",
            "   b) PDF öffnen",
            "   c) Signaturfeld prüfen: grünes Häkchen = gültig",
            "   d) Zertifikat prüfen: Aussteller D-Trust, gültig bis...",
            "   e) Dokument-Hash prüfen: Keine Manipulation nach Signierung",
            "   Das dauert 30 Sekunden. Das KANN ich als IT-Admin.",
            "   Den Transfervermerk prüfen KANN ich nicht — weil er keine",
            "   prüfbare digitale Signatur enthält, sondern nur Text auf Papier.",
            "",
            "4. FAZIT FÜR IHRE BERUFUNGSERWIDERUNG:",
            "   Verifikationsfunktion der qES = Empfänger muss Signatur selbst prüfen",
            "   können. Am Papierausdruck: unmöglich. Am elektronischen Original: trivial.",
            "   Der BGH wird das so sehen. Wetten?",
            "",
            "Mit freundlichen Grüßen,",
            "Götz-Sieghart Eberhart-Wolframshausen",
            "IT-Administrator | CISSP | Bielefeld",
        ]
    )
    elems += [
        sp(4),
        p('<i>Anm. d. Red.: Herr Eberhart-Wolframshausen hat mit seiner Wette Recht behalten. '
          'Der BGH folgte exakt dieser Argumentation in Leitsatz a) und c) des '
          'Urteils vom 27. November 2024 (VIII ZR 159/23). '
          'Die technische Präzision eines IT-Administrators hat das Verfahren '
          'über drei Instanzen dominiert.</i>', ITALIC),
    ]
    return elems


def erweiterung_reformausblick():
    """Ausblick auf die Reform und künftige Rechtslage."""
    elems = [pb()]
    elems += section_header("ANHANG D", "AUSBLICK: § 130e ZPO und die digitale Zukunft der Mietkündigung")
    elems += [
        p('<b>Ranftenschwedler Ostkamp Rechtsanwälte mbB</b>',
          S('rh_r', fontName='Helvetica-Bold', fontSize=11, textColor=C_ACCENT)),
        p('INFORMATIONSSCHREIBEN AN MANDANTEN-GRUPPE „BIELEFELDER VERMIETERRING"',
          BOLD),
        p('Datum: Dezember 2024', SMALL),
        sp(6), hr(), sp(4),
        p('<b>NEUE RECHTSLAGE AB 17.07.2024 — § 130e ZPO</b>', H2),
        BoxedPara(
            '<b>§ 130e ZPO (Zugang form- und empfangsbedürftiger Willenserklärungen in '
            'gerichtlichen Schriftsätzen):</b><br/><br/>'
            '(1) Willenserklärungen, die der schriftlichen oder elektronischen Form '
            'bedürfen und die klar erkennbar in einem vorbereitenden Schriftsatz '
            'enthalten sind, gelten als formwirksam zugegangen, sofern der Schriftsatz '
            'als elektronisches Dokument nach § 130a bei Gericht eingereicht und dem '
            'Empfänger zugestellt oder mitgeteilt wurde.<br/><br/>'
            '(2) [In Kraft getreten: 17. Juli 2024 — BGBl. I Nr. 234]',
            bg=colors.HexColor("#E3F2FD"), border=colors.HexColor("#1565C0"),
            style=S('neue_norm', fontName='Helvetica', fontSize=9.5, leading=15, textColor=C_BLACK)
        ),
        sp(6),
        p('<b>Was bedeutet das für Vermieter?</b>', H2),
        p('<b>Vor dem 17.07.2024 (gilt für das Pferdedrescher-Verfahren):</b>', H3),
        p('Eine Kündigung im Gerichtsschriftsatz konnte gegenüber einer nicht '
          'anwaltlich vertretenen Partei (Naturalpartei) nur dann formwirksam '
          'zugehen, wenn das elektronische Original mit der qES elektronisch '
          'weitergeleitet wurde. '
          'Ein Ausdruck mit Transfervermerk reichte nicht (BGH VIII ZR 159/23).', BODY),
        p('<b>Ab dem 17.07.2024 (aktuelle Rechtslage):</b>', H3),
        p('§ 130e ZPO fingiert den formwirksamen Zugang, wenn der qES-Schriftsatz '
          'als elektronisches Dokument bei Gericht eingereicht und dem Empfänger '
          'zugestellt oder mitgeteilt wurde. '
          'Das schließt auch die Zustellung als Papierausdruck ein '
          '(Fiktion gilt unabhängig vom Übermittlungsweg an den Empfänger).', BODY),
        BoxedPara(
            '<b>Praxishinweis für Vermieter:</b><br/><br/>'
            'Ab 17.07.2024 können Vermieter (vertreten durch RA) '
            'eine qES-Kündigung im Gerichtsschriftsatz erklären und diese '
            'dem Mieter — auch als Papierausdruck — durch das Gericht zustellen lassen. '
            'Die Kündigung gilt dann als formwirksam zugegangen (§ 130e ZPO).<br/><br/>'
            'ABER ACHTUNG: Dies gilt nur für Schriftsätze, die NACH dem 17.07.2024 '
            'bei Gericht eingegangen sind. Frühere Schriftsätze (wie im Pferdedrescher-Verfahren) '
            'fallen nicht unter § 130e ZPO.',
            bg=colors.HexColor("#E8F5E9"), border=colors.HexColor("#2E7D32"),
            style=S('praxis_h', fontName='Helvetica', fontSize=9.5, leading=15, textColor=C_BLACK)
        ),
        sp(6),
        p('<b>Was bedeutet das für Mieter?</b>', H2),
        p('Die Einführung des § 130e ZPO hat eine wichtige Konsequenz für den Mieterschutz: '
          'Mieter können nun nicht mehr darauf vertrauen, dass eine Kündigung im '
          'Gerichtsschriftsatz formunwirksam ist, weil sie als Papierausdruck zugestellt wurde. '
          '§ 130e ZPO fingiert den formwirksamen Zugang.', BODY),
        p('Außerdem besteht das Risiko, dass Vermieter qES-Kündigungen <b>direkt per E-Mail</b> '
          'verschicken — ohne Gerichtsverfahren. Dies ist nach dem BGH-Urteil zulässig, '
          'wenn das qES-signierte PDF im elektronischen Original beim Mieter eingeht.', BODY),
        BoxedPara(
            '<b>⚠ MIETERSCHUTZ-WARNUNG:</b><br/><br/>'
            '1. Mieter müssen ihre E-Mail-Postfächer regelmäßig auf qES-signierte Anhänge prüfen.<br/>'
            '2. Ein PDF mit dem Hinweis „Digital signiert" oder einem Signaturfeld ist '
            'ernst zu nehmen — es könnte eine formwirksame Kündigung sein.<br/>'
            '3. Wer eine qES-E-Mail-Kündigung erhält und nicht reagiert, riskiert, '
            'die Kündigung zu akzeptieren (§ 130 BGB).<br/>'
            '4. Im Zweifel: sofort Rechtsanwalt konsultieren.',
            bg=C_RED_LIGHT, border=C_RED,
            style=S('mieter_warn2', fontName='Helvetica', fontSize=9.5, leading=15, textColor=C_BLACK)
        ),
        sp(6),
        p('<b>Fazit und Ausblick</b>', H2),
        p('Das BGH-Urteil VIII ZR 159/23 hat einen rechtlichen Missstand aufgezeigt '
          'und einen Reformimpuls gegeben. § 130e ZPO hat die Lücke für den '
          'Prozesskontext geschlossen.', BODY),
        p('Für die außergerichtliche Kündigung per qES-E-Mail gilt: Rechtlich möglich, '
          'praktisch riskant (Zustellungsnachweis, Spam-Filter, E-Mail-Adresse). '
          'Die klassische Papier-Kündigung mit Botenübergabe bleibt die '
          'sicherste und empfehlenswerteste Methode.', BODY),
        p('Die Digitalisierung des Mietrechts ist eine Herausforderung für alle Beteiligten — '
          'Vermieter, Mieter, Anwälte und Gesetzgeber. Das Pferdedrescher-Verfahren '
          'ist ein Lehrstück über die Tücken des Rechtsformwandels im digitalen Zeitalter.', BODY),
        sp(8),
        p('Dr. Engelbert Ranftenschwedler-Bielenfels', BOLD),
        p('Rechtsanwalt | Fachanwalt für Miet- und WEG-Recht', SMALL),
        p('<i>„Ranftenschwedler Ostkamp Rechtsanwälte mbB" — Bielefeld, Dezember 2024</i>', FOOTNOTE),
    ]
    return elems





def erweiterung_schriftsatz_duplik():
    """Duplik der Klägerin im AG-Verfahren."""
    elems = [pb()]
    elems += section_header("ANHANG E", "DUPLIK KLÄGERIN — AG BIELEFELD (August 2022)")
    elems += [
        p('<b>Ranftenschwedler Ostkamp Rechtsanwälte mbB</b>',
          S('dup_h', fontName='Helvetica-Bold', fontSize=11, textColor=C_ACCENT)),
        p('DUPLIK — Az. AG Bielefeld 34 C 421/22 | Datum: 05. August 2022', BOLD),
        p('Eingereicht über beA mit qES gem. § 130d ZPO', SMALL),
        sp(6), hr(), sp(4),
        p('Die Klägerin erwidert auf die Klageerwiderung des Beklagten '
          'vom 15.04.2022 wie folgt (als Duplik, da der Beklagte erhebliche '
          'neue Rechtsfragen aufgeworfen hat):', BODY),
        sp(4),
        p('<b>I. Zur Rückstandsberechnung (§ 543 Abs. 2 Nr. 3 BGB)</b>', H2),
        p('Der Beklagte bestreitet die Rückstandsberechnung der Klägerin. '
          'Zur Klarstellung: Die Klägerin legt die monatlichen Zahlungseingänge '
          'auf dem Mietkonto wie folgt dar:', BODY),
        Table([
            ['Zeitraum', 'Sollmiete gesamt', 'Istzahlungen', 'Saldo'],
            ['Mrz 2019 – Jan 2021 (23 Monate)', 'EUR 14.926,31', 'EUR 12.266,61', '– EUR 2.659,70'],
            ['Feb 2021 – Jan 2022 (12 Monate)', 'EUR 7.787,64', 'EUR 9.600,00', '+ EUR 1.812,36'],
            ['Zwischensaldo 31.01.2022', '', '', '– EUR 847,34'],
            ['Februarmiete 2022 (nicht gezahlt)', 'EUR 648,97', 'EUR 0,00', '– EUR 648,97'],
            ['Rückstand 10.02.2022', '', '', '– EUR 1.496,31'],
        ], colWidths=[185, 100, 100, 80]),
        sp(4),
        p('<i>Anm.: Die Abweichung zur Hauptklage (dort EUR 1.696,31) ergibt sich '
          'aus einer Korrekturbuchung vom 01.02.2022 (Rücklastschrift EUR 200,00). '
          'Der maßgebliche Rückstand übersteigt in beiden Berechnungen zwei Monatsmieten.</i>',
          ITALIC),
        sp(4),
        p('<b>II. Zur Frage der Abmahnung</b>', H2),
        p('Der Beklagte behauptet, eine Abmahnung sei erforderlich. '
          'Dies ist unzutreffend. § 543 Abs. 2 Nr. 3 BGB lässt die '
          'außerordentliche Kündigung ohne vorherige Abmahnung zu, wenn '
          'der Mieter mit mehr als zwei Monatsmieten in Verzug ist. '
          '§ 569 Abs. 3 Nr. 2 BGB betrifft die Schonfrist nach Zahlung '
          '(nicht das Abmahnungserfordernis). '
          'Eine Abmahnung war nicht erforderlich.', BODY),
        p('<b>III. Zur Wirksamkeit der Kündigung im Schriftsatz — ergänzender Vortrag</b>', H2),
        p('Die Klägerin trägt ergänzend vor, dass nach ihrer Auffassung '
          'die gerichtliche Zustellung des qES-Schriftsatzes als Ausdruck '
          'mit Transfervermerk gem. § 298 Abs. 3 ZPO den formwirksamen Zugang '
          'der Kündigung beim Beklagten bewirkt hat. '
          'Dies ergibt sich aus folgendem Rechtsgedanken:', BODY),
        p('Der Transfervermerk hat dieselbe öffentlich-rechtliche Beweiskraft '
          'wie eine notarielle Beglaubigung (vgl. § 415 ZPO). '
          'Wenn eine notariell beglaubigte Kopie eines handschriftlich '
          'unterzeichneten Dokuments die Schriftform wahren kann, '
          'muss ein staatlich bestätigter Transfervermerk erst recht '
          'die Verifikationsfunktion der qES erfüllen.', BODY),
        BoxedPara(
            '<b>Antrag:</b> Die Klägerin hält ihre erstinstanzlichen Anträge aufrecht. '
            'Sie beantragt, den Beklagten zur Räumung und zur Zahlung von '
            'EUR 1.696,31 (korrigiert: EUR 1.496,31) zu verurteilen.<br/><br/>'
            'Hilfsantrag: Feststellung, dass das Mietverhältnis durch die '
            'Kündigung vom 09.03.2022 beendet wurde.',
            bg=C_QES_BG, border=C_QES_BLUE,
            style=S('dup_ant', fontName='Helvetica', fontSize=9.5, leading=15, textColor=C_BLACK)
        ),
        sp(8),
        p('Dr. Engelbert Ranftenschwedler-Bielenfels', BOLD),
        p('Rechtsanwalt', SMALL),
    ]
    return elems


def erweiterung_zahlungsklagen():
    """Ergänzende Zahlungsklage-Details."""
    elems = [pb()]
    elems += section_header("ANHANG F", "ERGÄNZENDE ZAHLUNGSKLAGE — Nebenansprüche")
    elems += [
        p('<b>Ranftenschwedler Ostkamp Rechtsanwälte mbB</b>',
          S('zk_h', fontName='Helvetica-Bold', fontSize=11, textColor=C_ACCENT)),
        p('SCHRIFTSATZ — Ergänzung der Zahlungsanträge | Az. LG Bielefeld 14 S 88/23',
          BOLD),
        p('Bielefeld, April 2023', SMALL),
        sp(6), hr(), sp(4),
        p('<b>Hintergrund</b>', H2),
        p('Im Berufungsverfahren hat die Klägerin die Zahlungsanträge aktualisiert. '
          'Herr Eberhart-Wolframshausen ist auch nach dem erstinstanzlichen Urteil '
          'in der Wohnung verblieben und zahlt die laufende Miete — wenn auch '
          'weiterhin unregelmäßig.', BODY),
        p('<b>Aktueller Zahlungsstand per März 2023</b>', H2),
        Table([
            ['Monat', 'Soll (€)', 'Ist (€)', 'Saldo (€)'],
            ['Mrz 2022', '648,97', '648,97', '0,00'],
            ['Apr 2022', '648,97', '500,00', '–148,97'],
            ['Mai 2022', '648,97', '648,97', '–148,97'],
            ['Jun 2022', '648,97', '648,97', '–148,97'],
            ['Jul 2022', '648,97', '648,97', '–148,97'],
            ['Aug 2022', '648,97', '648,97', '–148,97'],
            ['Sep 2022', '648,97', '648,97', '–148,97'],
            ['Okt 2022', '648,97', '600,00', '–197,94'],
            ['Nov 2022', '648,97', '648,97', '–197,94'],
            ['Dez 2022', '648,97', '648,97', '–197,94'],
            ['Jan 2023', '648,97', '648,97', '–197,94'],
            ['Feb 2023', '648,97', '648,97', '–197,94'],
            ['Mrz 2023', '648,97', '648,97', '–197,94'],
            ['Rückstand inkl. Vorjahre', '—', '—', '–1.694,25'],
        ], colWidths=[130, 80, 80, 80]),
        sp(4),
        p('<b>Rechtliche Einschätzung der Zahlungsklage im Berufungsverfahren</b>', H2),
        p('Unabhängig von der Räumungsfrage besteht ein Zahlungsanspruch der Klägerin '
          'auf den Mietrückstand. Die Zahlungsklage ist auch dann begründet, wenn '
          'die Kündigung unwirksam ist — weil die laufende Miete unabhängig von der '
          'Kündigungswirksamkeit geschuldet wird.', BODY),
        p('Die Klägerin beantragt im Berufungsverfahren ergänzend:', BODY),
        p('1. Verurteilung des Beklagten zur Zahlung des laufenden Rückstands '
          'von EUR 1.694,25 nebst Zinsen (5 Prozentpunkte über Basiszinssatz).', BODY_L),
        p('2. Feststellung der monatlichen Zahlungspflicht bis zur rechtskräftigen '
          'Entscheidung über die Räumungsklage.', BODY_L),
        sp(6),
        p('<b>Exkurs: Mieter-Verhalten und Treu und Glauben</b>', H2),
        p('Ein interessanter Aspekt des Falles: Herr Eberhart-Wolframshausen nutzte '
          'die Formunwirksamkeit der Kündigung konsequent — obwohl er als IT-Admin '
          'wusste, dass die materiell-rechtlichen Voraussetzungen der Kündigung '
          '(Rückstandshöhe) zweifellos erfüllt waren. '
          'RA Ranftenschwedler-Bielenfels erwog zeitweise eine Berufung auf '
          '§ 242 BGB (Treu und Glauben) oder Rechtsmissbrauch.', BODY),
        BoxedPara(
            '<b>Argument Rechtsmissbrauch (§ 242 BGB):</b><br/>'
            'Wer die Unwirksamkeit einer Kündigung allein auf Formgründe stützt '
            'und dabei eine materiell-rechtlich begründete Kündigung abwehrt, '
            'könnte sich treuwidrig verhalten — insbesondere wenn er die Formfehler '
            'selbst provoziert hat (z.B. durch Beharren auf elektronischer Kommunikation).<br/><br/>'
            '<b>Gegenargument:</b><br/>'
            'Die Schriftform des § 568 BGB schützt den Mieter. '
            'Wer Formvorschriften einhält, handelt nicht treuwidrig. '
            'Das Berufungsgericht (LG Bielefeld) und der BGH haben dieses Argument '
            'zu Recht verworfen.',
            bg=colors.HexColor("#FFF3E0"), border=colors.HexColor("#E65100"),
            style=S('treu_box', fontName='Helvetica', fontSize=9, leading=14, textColor=C_BLACK)
        ),
        sp(8),
        p('Dr. Engelbert Ranftenschwedler-Bielenfels', BOLD),
        p('Rechtsanwalt', SMALL),
    ]
    return elems


def erweiterung_literaturhinweise():
    """Literatur- und Rechtsprechungsübersicht."""
    elems = [pb()]
    elems += section_header("ANHANG G",
                            "LITERATUR- UND RECHTSPRECHUNGSÜBERSICHT")
    elems += [
        p('<b>Zusammengestellt für die Revisionsbegründung BGH VIII ZR 159/23</b>', BOLD),
        p('Kanzlei Ranftenschwedler Ostkamp | August 2023', SMALL),
        sp(6), hr(), sp(4),
        p('<b>A. Grundlegende Normen</b>', H2),
        Table([
            ['Norm', 'Regelungsgegenstand', 'Relevanz für den Fall'],
            ['§ 568 Abs. 1 BGB', 'Schriftform der Mietkündigung', 'Kernvorschrift'],
            ['§ 126 BGB', 'Definition Schriftform (eigenhändige Unterschrift)', 'Maßstab'],
            ['§ 126a BGB', 'Elektronische Form (qES)', 'Ersetzung der Schriftform'],
            ['§ 126 Abs. 3 BGB', 'Schriftform ersetzbar durch elektronische Form', 'Zulässigkeit qES-Kündigung'],
            ['§ 130 Abs. 1 S. 1 BGB', 'Zugangserfordernis für Willenserklärung', 'Kern-Streitpunkt'],
            ['§ 125 S. 1 BGB', 'Nichtigkeitsfolge bei Formmangel', 'Rechtsfolge Unwirksamkeit'],
            ['§ 543 Abs. 2 Nr. 3 BGB', 'Außerordentliche Kündigung Zahlungsverzug', 'Kündigungsgrund'],
            ['§ 569 Abs. 3 BGB', 'Schonfristzahlung bei fristloser Kündigung', 'Nebenregelung'],
            ['§ 130d ZPO', 'Elektronische Pflichteinreichung durch RA', 'Prozessrecht'],
            ['§ 130e ZPO', 'Fiktion formwirksamer Zugang (ab 17.07.2024)', 'Neue Rechtslage'],
            ['§ 173 Abs. 4 S. 1 ZPO', 'Zustimmung Naturalpartei zu elektr. Zustellung', 'Zustellungsfrage'],
            ['§ 298 Abs. 1, 3 ZPO', 'Ausdruck elektronischer Dokumente, Transfervermerk', 'Kern-Streitpunkt'],
        ], colWidths=[110, 180, 165]),
        sp(6),
        p('<b>B. Wichtige Entscheidungen</b>', H2),
        Table([
            ['Gericht / Az.', 'Datum', 'Inhalt / Relevanz'],
            ['BGH VIII ZR 159/23', '27.11.2024', 'Leitsätze a)-c) — Kernentscheidung'],
            ['BGH VIII ZR 155/23', '27.11.2024', 'Parallelsache (beA-Weiterleitung)'],
            ['BGH IX ZR 174/13', '26.02.2015', '§ 130 BGB — Zugangserfordernis Form'],
            ['BGH XII ZB 573/18', '15.05.2019', 'Container-Signatur; elektronische Form'],
            ['BGH VI ZB 7/13', '14.05.2013', 'Zulässigkeit Container-Signatur (aufgegeben)'],
            ['OLG Hamburg 2 W 125/10', '18.11.2010', 'Eingescannte Unterschrift = keine qES'],
            ['BGH NJW 2009, 2062', '2009', 'Schriftform, elektronische Übermittlung'],
            ['BGH NJW 1987, 2506', '25.03.1987', 'Beglaubigung und Schriftform'],
            ['LG Berlin GE 2021, 882', '2021', 'qES-Kündigung per Schriftsatz (Instanzgericht)'],
        ], colWidths=[155, 65, 235]),
        sp(6),
        p('<b>C. Wichtige Literatur (Auswahl)</b>', H2),
        Table([
            ['Autor / Werk', 'Fundstelle / Auflage', 'Relevanz'],
            ['MüKoBGB/Einsele', '9. Aufl. 2021, § 126a Rn. 1 ff.', 'Verifikationsfunktion qES'],
            ['Staudinger/Hertel', 'Neubearbeitung 2023, § 126a Rn. 5 ff.', 'Formfunktionen'],
            ['BeckOGK/Möslein', '§ 126a BGB, Stand 2024', 'Zugangserfordernis'],
            ['Schmidt-Futterer/Blank', 'Mietrecht, 15. Aufl. 2023, § 568 Rn. 5 ff.', '§ 568 BGB Schriftform'],
            ['Palandt/Ellenberger', 'BGB, 83. Aufl. 2024, § 126a Rn. 3', 'qES-Definition'],
            ['Gsell/Krüger (Hrsg.)', 'beckOK ZPO, § 130e Rn. 1 ff. (neu)', '§ 130e ZPO Reform'],
            ['Müller, NZM 2023, 641', 'NZM 2023, S. 641 ff.', 'qES-Kündigung Praxis'],
            ['Hinz, MDR 2025, 162', 'MDR 2025, S. 162 ff.', 'Anm. zu BGH VIII ZR 159/23'],
        ], colWidths=[165, 170, 120]),
        sp(6),
        p('<b>D. Gesetzgebungsmaterialien</b>', H2),
        Table([
            ['Fundstelle', 'Inhalt'],
            ['BT-Drs. 14/4987, S. 16 ff.', 'Gesetzesbegründung zu § 126a BGB (FormVAnpG 2001)'],
            ['BT-Drs. 20/8762', 'Gesetzesbegründung zu § 130e ZPO (HinSchG-Begleitgesetz 2024)'],
            ['BGBl. I Nr. 234 v. 17.07.2024', 'Inkrafttreten § 130e ZPO'],
            ['BT-Drs. 14/4987, S. 19', 'Funktionsäquivalenz elektronische Form / Schriftform'],
        ], colWidths=[200, 255]),
    ]
    return elems


def erweiterung_abschlussbemerkung():
    """Abschlussbemerkung und Anmerkungen."""
    elems = [pb()]
    elems += section_header("SCHLUSS", "ABSCHLUSSBEMERKUNG UND AKTEN-IMPRESSUM")
    elems += [
        BoxedPara(
            '<b>FIKTIVE TESTAKTE — Rechtliche Lehrakte</b><br/><br/>'
            'Diese Akte ist eine rein fiktive Lehrakte zum Zweck der rechtlichen Ausbildung '
            'und Illustration der Rechtsprechung des BGH (VIII ZR 159/23, 27.11.2024).<br/><br/>'
            'Alle Personen, Adressen, Aktenzeichen (ausgenommen BGH VIII ZR 159/23 und '
            'VIII ZR 155/23) sind fiktiv. Ähnlichkeiten mit realen Personen sind '
            'rein zufällig und nicht beabsichtigt.<br/><br/>'
            'Die zitierten Rechtssätze, Normen und BGH-Leitsätze sind authentisch.',
            bg=C_RED_LIGHT, border=C_RED,
            style=S('abschl_warn', fontName='Helvetica-Bold', fontSize=10,
                    leading=15, textColor=C_BLACK)
        ),
        sp(8),
        p('<b>Kernaussagen der Testakte (Zusammenfassung)</b>', H2),
        p('1. <b>WhatsApp-Kündigung:</b> Formunwirksam (kein Schriftstück, keine qES). '
          '§ 568 Abs. 1 BGB, § 125 S. 1 BGB.', BODY),
        p('2. <b>E-Mail ohne qES:</b> Formunwirksam (keine qES i.S.v. § 126a BGB). '
          '§ 125 S. 1 BGB.', BODY),
        p('3. <b>qES-Schriftsatz, Ausdruck mit Transfervermerk:</b> Formunwirksamer Zugang '
          '(Verifikationsfunktion nicht gewahrt). BGH VIII ZR 159/23, Leitsatz c).', BODY),
        p('4. <b>Direkte qES-E-Mail an Mieter:</b> Formwirksamer Zugang möglich, wenn '
          'elektronisches Original mit prüfbarer qES beim Mieter eingeht. '
          'BGH VIII ZR 159/23, Leitsatz a).', BODY),
        p('5. <b>§ 130e ZPO (ab 17.07.2024):</b> Fiktion formwirksamen Zugangs für '
          'qES-Schriftsätze, die über § 130a ZPO eingereicht und zugestellt werden. '
          'Gilt nicht rückwirkend.', BODY),
        sp(6),
        p('<b>Online-Dimension (besonderer Twist der Testakte)</b>', H2),
        p('Die Testakte illustriert das Spannungsfeld zwischen digital-affinen Vermietern '
          '(Pferdedrescher-Riesenstein) und technikversierten Mietern '
          '(Eberhart-Wolframshausen als IT-Admin). '
          'Gerade die technische Kompetenz des Mieters ermöglichte es ihm, '
          'die Formfehler der Vermieterin präzise zu identifizieren und auszunutzen — '
          'was letztlich zum Obsiegen über drei Instanzen führte.', BODY),
        p('Das BGH-Urteil VIII ZR 159/23 gibt IT-kundigen Mietern ein scharfes Schwert '
          'gegen digital nachlässige Vermieter. Gleichzeitig eröffnet es künftig die '
          'Möglichkeit, Mieter durch qES-E-Mail-Direktzustellung rechtswirksam zu kündigen — '
          'was Mieter zu digitaler Wachsamkeit zwingt.', BODY),
        sp(8),
        p('<b>Akten-Impressum</b>', H2),
        Table([
            ['Erstellt mit:', 'ReportLab 4.x (Python) — Perplexity Computer'],
            ['Aktenzeichen Testakte:', 'AG Bielefeld 34 C 421/22 (fiktiv)'],
            ['Reales BGH-Urteil:', 'BGH VIII ZR 159/23 vom 27.11.2024'],
            ['Bestandteile:', '30 Aktenteile + 7 Anhänge = 37 Dokumente'],
            ['Schauplatz:', 'Bielefeld, NRW (Sparrenburg: wirklich existent!)'],
        ], colWidths=[130, 325]),
        sp(6),
        p('— Ende der Testakte Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen —',
          S('fin2', fontName='Helvetica-Bold', fontSize=11,
            alignment=TA_CENTER, textColor=C_ACCENT)),
        sp(4),
        p('Az. AG Bielefeld 34 C 421/22 | LG Bielefeld 14 S 88/23 | BGH VIII ZR 159/23',
          CENTER),
        sp(4),
        p('Bielefeld existiert wirklich.',
          S('biel', fontName='Helvetica-Oblique', fontSize=9,
            alignment=TA_CENTER, textColor=C_MID_GREY)),
        pb(),
        p('<b>NACHWORT: Was Bielefeld mit dem BGH verbindet</b>',
          S('nw_h', fontName='Helvetica-Bold', fontSize=13,
            alignment=TA_CENTER, textColor=C_ACCENT)),
        sp(8),
        p('Bielefeld ist real. Die Sparrenburg steht wirklich auf dem Teutoburger Wald. '
          'Das Amtsgericht Bielefeld liegt am Niederwall. Das Landgericht auch. '
          'Die Eckendorfer Straße verläuft durch den Bielefelder Westen.', BODY),
        p('Der BGH in Karlsruhe ist von Bielefeld ca. 400 km entfernt. '
          'Für Frau Pferdedrescher-Riesenstein und ihren Anwalt '
          'Dr. Ranftenschwedler-Bielenfels war die Entfernung zum BGH '
          'nicht nur geographisch, sondern auch rechtlich beschwerlich.', BODY),
        p('Der IT-Administrator Herr Eberhart-Wolframshausen hat durch sein '
          'technisches Verständnis der qualifizierten elektronischen Signatur '
          'einen wichtigen Beitrag zur Rechtsentwicklung geleistet — '
          'wenn auch unbeabsichtigt.', BODY),
        p('Das BGH-Urteil VIII ZR 159/23 vom 27. November 2024 ist ein Lehrstück '
          'über die Tücken der Digitalisierung im Recht. Es zeigt:', BODY),
        p('1. Formvorschriften sind ernst zu nehmen — auch und gerade im digitalen Zeitalter.', BODY_L),
        p('2. Technische Kompetenz schützt vor Rechtsverlust.', BODY_L),
        p('3. Eine qES ist mehr als ein Häkchen in Adobe Acrobat — sie ist ein Rechtsdokument.', BODY_L),
        p('4. Der Gesetzgeber reagiert (§ 130e ZPO) — aber manchmal zu spät.', BODY_L),
        p('5. Die Kosten eines Rechtsstreits können den Nutzen bei weitem übersteigen.', BODY_L),
        sp(8),
        BoxedPara(
            'Diese Testakte ist dem Bielefelder Mietrecht und dem BGH-Urteil VIII ZR 159/23 '
            'gewidmet — und dem anonymen IT-Administrator aus Bielefeld, '
            'der wusste, was eine qualifizierte elektronische Signatur ist.<br/><br/>'
            '<i>„Wer Form nicht respektiert, verliert."</i><br/>'
            '— frei nach § 125 Satz 1 BGB',
            bg=colors.HexColor("#E8EAF6"), border=colors.HexColor("#3949AB"),
            style=S('widm_s', fontName='Helvetica-Oblique', fontSize=10, leading=16,
                    textColor=C_BLACK, alignment=TA_CENTER)
        ),
    ]
    return elems


def erweiterung_parallelverfahren():
    """Parallele BGH-Sachen und Rechtsprechungsübersicht."""
    elems = [pb()]
    elems += section_header("ANHANG H",
                            "PARALLELE BGH-SACHE VIII ZR 155/23 UND KONTEXT")
    elems += [
        p('<b>Parallelsache BGH VIII ZR 155/23 — Weiterleitung per beA</b>', H2),
        p('Am selben Tag (27. November 2024) hat der BGH auch das Parallelverfahren '
          'VIII ZR 155/23 entschieden. Dort war der Schriftsatz nicht als Papierausdruck, '
          'sondern elektronisch per beA an den Prozessbevollmächtigten des Beklagten '
          'weitergeleitet worden. Der BGH hat die Sache insoweit an das '
          'Berufungsgericht zurückverwiesen, um festzustellen, ob die qES bei der '
          'elektronischen Weiterleitung erhalten geblieben ist.', BODY),
        BoxedPara(
            '<b>Unterschied der Parallelverfahren:</b><br/><br/>'
            '<b>VIII ZR 159/23 (unser Fall):</b><br/>'
            'Zustellung als Papierausdruck mit Transfervermerk → '
            'KEIN formwirksamer Zugang (Leitsatz c). Endentscheidung: Revision zurückgewiesen.<br/><br/>'
            '<b>VIII ZR 155/23:</b><br/>'
            'Elektronische Weiterleitung per beA → '
            'Formwirksamer Zugang MÖGLICH, wenn qES bei Weiterleitung erhalten blieb. '
            'Zurückverweisung zur Tatsachenfeststellung.',
            bg=colors.HexColor("#E3F2FD"), border=colors.HexColor("#1565C0"),
            style=S('parallel_box', fontName='Helvetica', fontSize=9.5, leading=15, textColor=C_BLACK)
        ),
        sp(6),
        p('<b>Konsequenz für die Praxis</b>', H2),
        p('Die beiden Entscheidungen zusammen ergeben folgendes Bild:', BODY),
        Table([
            ['Zustellungsweg', 'qES erhalten?', 'Formwirksamer Zugang?'],
            ['Papierausdruck + Transfervermerk', 'Nein (technisch unmöglich)', 'NEIN — Leitsatz c)'],
            ['Elektronisch per beA (direkt an RA)', 'Ggf. ja (Feststellung nötig)', 'JA — wenn qES erhalten'],
            ['Direkte E-Mail qES-PDF an Partei', 'Ja (elektr. Original)', 'JA — Leitsatz a), b)'],
            ['WhatsApp / E-Mail ohne qES', 'Nein (keine qES)', 'NEIN — § 125 S. 1 BGB'],
        ], colWidths=[185, 130, 140]),
        sp(6),
        p('<b>Zeitliche Entwicklung der Rechtslage</b>', H2),
        Table([
            ['Zeitraum', 'Rechtslage', 'Konsequenz'],
            ['Vor 17.07.2024', 'Kein § 130e ZPO', 'qES-Schriftsatz nur wirksam bei elektr. Weiterleitung mit qES-Erhalt'],
            ['Ab 17.07.2024', '§ 130e ZPO in Kraft', 'Zugang fingiert bei gerichtl. Einreichung + Zustellung'],
            ['Für laufende Verfahren', 'Übergangsrecht', 'Schriftsätze vor 17.07.2024: alte Rechtslage'],
        ], colWidths=[110, 200, 145]),
        sp(6),
        p('<b>Bielefeld-Bezug: Mietrecht in OWL</b>', H2),
        p('Das Amtsgericht Bielefeld und das Landgericht Bielefeld sind im '
          'Bereich Miet- und WEG-Recht in Ostwestfalen-Lippe (OWL) zuständig. '
          'In der Region Bielefeld/Gütersloh/Paderborn ist der Wohnungsmarkt '
          'aufgrund des hohen Anteils von Universitätsstudenten und IT-Unternehmen '
          '(u.a. Arvato/Bertelsmann, Miele, Phoenix Contact) durch einen hohen '
          'Anteil digital-affiner Mieter und Vermieter gekennzeichnet. '
          'Die Problematik der Online-Kündigung ist daher regional besonders relevant.', BODY),
        BoxedPara(
            'RA Ranftenschwedler-Bielenfels (intern, Dezember 2024):<br/><br/>'
            '„In Bielefeld gibt es viele Mieter wie Herrn Eberhart-Wolframshausen — '
            'IT-Affine, die genau wissen, was eine qES ist. '
            'Und viele Vermieter wie Frau Pferdedrescher-Riesenstein — '
            'Online-Vermieter, die glauben, alles digital abwickeln zu können. '
            'Das BGH-Urteil VIII ZR 159/23 ist ein Spiegel dieser Bielefelder Realität. '
            'Sparrenburg hin oder her — die Formfrage ist ernst."',
            bg=C_STAMP_BG, border=C_STAMP_BD,
            style=S('bielefeld_box', fontName='Helvetica-Oblique', fontSize=9,
                    leading=13, textColor=C_BLACK)
        ),
        sp(6),
        p('<b>Reformausblick: Digitale Kündigung 2025 ff.</b>', H2),
        p('Nach den BGH-Entscheidungen vom 27.11.2024 und dem Inkrafttreten des '
          '§ 130e ZPO am 17.07.2024 stellt sich die Frage, ob der Gesetzgeber '
          'weitere Reformen für die außergerichtliche digitale Kündigung planen wird.', BODY),
        p('Diskutiert wird:', BODY),
        p('(a) Eine gesetzliche Regelung, die die direkte qES-E-Mail-Kündigung '
          'an Mieter explizit für zulässig erklärt (außergerichtlich).', BODY_L),
        p('(b) Eine Verpflichtung der Mieter, eine E-Mail-Adresse für '
          'rechtsverbindliche Erklärungen im Mietvertrag anzugeben.', BODY_L),
        p('(c) Eine Erweiterung des § 130e ZPO auf außergerichtliche Erklärungen '
          '(de lege ferenda).', BODY_L),
        p('Ob und wann solche Reformen kommen, ist offen. Bis dahin gilt: '
          'Für Vermieter ist die klassische schriftliche Kündigung auf Papier '
          'mit Botenübergabe die einzige rechtssichere Methode — außerhalb des Prozesses.',
          BODY),
    ]
    return elems


def erweiterung_praktische_checkliste():
    """Praktische Checkliste für Vermieter."""
    elems = [pb()]
    elems += section_header("ANHANG I",
                            "PRAKTISCHE CHECKLISTE FÜR VERMIETER: Formwirksame Kündigung")
    elems += [
        p('<b>Ranftenschwedler Ostkamp Rechtsanwälte mbB — Mandanten-Infoblatt</b>',
          S('check_h', fontName='Helvetica-Bold', fontSize=11, textColor=C_ACCENT)),
        p('CHECKLISTE: Mietkündigung — Was ist wann wirksam?', BOLD),
        sp(6), hr(), sp(4),
        p('<b>A. Außergerichtliche Kündigung (VOR Klageerhebung)</b>', H2),
        Table([
            ['Methode', 'Formwirksam?', 'Begründung', 'Empfehlung'],
            ['Papier + Unterschrift, Botenübergabe', 'JA ✓', '§ 126 BGB', '⭐⭐⭐ Beste Methode'],
            ['Papier + Unterschrift, Einschreiben/RS', 'JA ✓ (bei Abholung)', '§ 126 BGB', '⭐⭐ Gut, Risiko bei Nichtabholung'],
            ['Papier + Unterschrift, per Post', 'JA ✓ (bei Zugang)', '§ 126 BGB', '⭐ Beweisproblem'],
            ['qES-PDF direkt per E-Mail', 'JA ✓ (bei Zugang elektr.)', '§§ 126a, 130 BGB', '⭐⭐ Gut, Zustellungsnachweis sichern'],
            ['E-Mail ohne qES', 'NEIN ✗', '§ 125 S. 1 BGB', '❌ Nie verwenden'],
            ['WhatsApp (Text oder Sprache)', 'NEIN ✗', '§ 125 S. 1 BGB', '❌ Nie verwenden'],
            ['SMS', 'NEIN ✗', '§ 125 S. 1 BGB', '❌ Nie verwenden'],
            ['Fax', 'NEIN ✗ (i.d.R.)', '§ 125 S. 1 BGB', '❌ Keine qES, kein Original'],
        ], colWidths=[150, 80, 110, 115]),
        sp(6),
        p('<b>B. Gerichtliche Kündigung (IM laufenden Räumungsprozess)</b>', H2),
        Table([
            ['Methode', 'Formwirksam?', 'Begründung', 'Empfehlung'],
            ['qES-Schriftsatz, elektronisch per beA (mit qES-Erhalt)', 'JA ✓', 'BGH VIII ZR 155/23', '⭐⭐⭐ Gut'],
            ['qES-Schriftsatz, als Ausdruck zugestellt (VOR 17.07.2024)', 'NEIN ✗', 'BGH VIII ZR 159/23', '❌ Altfälle gescheitert'],
            ['qES-Schriftsatz, als Ausdruck zugestellt (AB 17.07.2024)', 'JA ✓ (Fiktion)', '§ 130e ZPO', '⭐⭐⭐ Neue Rechtslage'],
            ['Schriftsatz ohne qES', 'NEIN ✗', '§ 126a BGB', '❌ Schriftform nicht ersetzt'],
        ], colWidths=[200, 80, 120, 100]),
        sp(6),
        p('<b>C. Allgemeine Hinweise</b>', H2),
        p('1. <b>Empfangsbedürftige Erklärung:</b> Die Kündigung wird erst wirksam, '
          'wenn sie dem Empfänger zugegangen ist (§ 130 Abs. 1 S. 1 BGB). '
          'Formgerechte Abgabe + formgerechter Zugang erforderlich.', BODY),
        p('2. <b>Vertretung:</b> Der Anwalt kann namens des Vermieters kündigen, '
          'sofern die Vollmacht vorliegt. Die Kündigung durch RA unter Vorlage '
          'einer Originalvollmacht genügt der Schriftform.', BODY),
        p('3. <b>Sozialklausel:</b> Bei ordentlicher Kündigung ist ein berechtigtes '
          'Interesse i.S.v. § 573 BGB erforderlich. Zahlungsverzug = Erhebliche '
          'Pflichtverletzung (§ 573 Abs. 2 Nr. 1 BGB).', BODY),
        p('4. <b>Schonfristzahlung:</b> Gemäß § 569 Abs. 3 Nr. 2 BGB wird die '
          'fristlose Kündigung unwirksam, wenn der Mieter innerhalb von zwei Monaten '
          'nach Rechtshängigkeit die Mietrückstände vollständig bezahlt. '
          '(Einmal alle zwei Jahre möglich, § 569 Abs. 3 Nr. 2 S. 2 BGB.)', BODY),
        p('5. <b>Bielefeld-Hinweis:</b> Das AG Bielefeld ist für Mietsachen bis '
          'EUR 5.000,00 Streitwert zuständig (§ 23 Nr. 2a GVG). '
          'Bei Räumungsklagen gilt der Streitwert der Jahresmiete (§ 41 GKG). '
          'Ab EUR 7.787,64 (wie hier) ist das AG Bielefeld erstinstanzlich zuständig, '
          'weil § 23 Nr. 2a GVG für Wohnraummietkündigungen gilt.', BODY),
        sp(8),
        BoxedPara(
            '<b>FAZIT CHECKLISTE:</b><br/>'
            'Der sicherste Weg bleibt die klassische Papier-Kündigung mit '
            'eigenhändiger Unterschrift und persönlicher Übergabe durch Boten '
            '(mit Zeuge). Digital-affine Vermieter können die qES-E-Mail-Kündigung '
            'ergänzend nutzen — aber nur mit prüfbarer qES im elektronischen Original '
            'und sicherem Zustellungsnachweis. '
            'WhatsApp und unsignierte E-Mails sind keine Optionen.',
            bg=colors.HexColor("#E8F5E9"), border=colors.HexColor("#2E7D32"),
            style=S('chk_fazit', fontName='Helvetica', fontSize=9.5, leading=15, textColor=C_BLACK)
        ),
        sp(4),
        p('Ranftenschwedler Ostkamp Rechtsanwälte mbB | Niederwall 12 | 33602 Bielefeld', SMALL),
        p('Stand: Dezember 2024 | Az. BGH VIII ZR 159/23 berücksichtigt', FOOTNOTE),
    ]
    return elems



def erweiterung_falldokumentation():
    """Ausführliche Falldokumentation mit Chronologie."""
    elems = [pb()]
    elems += section_header("ANHANG J",
                            "DETAILLIERTE FALLDOKUMENTATION — CHRONOLOGIE DES VERFAHRENS")
    elems += [
        p('<b>Vollständige Chronologie: Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen</b>',
          BOLD),
        p('Az. AG Bielefeld 34 C 421/22 | LG Bielefeld 14 S 88/23 | BGH VIII ZR 159/23',
          SMALL),
        sp(6), hr(), sp(4),
        p('<b>PHASE 1: Entstehung des Mietverhältnisses und erste Rückstände '
          '(2017–2021)</b>', H2),
        p('01.04.2017: Mietbeginn. Herr Eberhart-Wolframshausen zieht in die '
          'Wohnung Eckendorfer Straße 188, App. 4 OG, Bielefeld ein. '
          'Bruttomiete EUR 648,97/Monat. Er arbeitet als IT-Administrator '
          'bei einem Bielefelder Unternehmen (IT-Dienstleister).', BODY),
        p('März 2019: Erste Mietzahlung unter dem Sollbetrag (EUR 530,00 statt EUR 648,97). '
          'Frau Pferdedrescher-Riesenstein schickt per WhatsApp eine Erinnerung. '
          'Dies ist der Beginn einer jahrelangen Kommunikationsgeschichte via '
          'Messenger und E-Mail — ohne je schriftliche Mahnbriefe zu versenden.', BODY),
        p('April 2019 – Januar 2021: Chronische Unterzahlungen. Mahnung auf Mahnung. '
          'Alle digital. Der Rückstand wächst auf EUR 2.659,70 (= ca. 4,1 Monatsmieten). '
          'Frau Pferdedrescher-Riesenstein zögert mit einer formalen Kündigung — '
          'sie hofft auf freiwillige Zahlung.', BODY),
        p('Februar 2021 – Januar 2022: Herr Eberhart-Wolframshausen zahlt plötzlich '
          'EUR 800,00/Monat statt EUR 648,97. Die Überzahlung von EUR 151,03/Monat '
          'dient dem Abbau des Rückstands. Ende Januar 2022 beträgt der Rückstand '
          'noch EUR 847,34.', BODY),
        sp(6),
        p('<b>PHASE 2: Kündigungsversuche und Formunwirksamkeit (Februar 2022)</b>', H2),
        p('08.-10. Februar 2022: Eskalation per WhatsApp. '
          'Frau Pferdedrescher-Riesenstein erklärt die fristlose Kündigung per '
          'WhatsApp-Sprachnachricht (10.02.2022 09:31 Uhr) und schickt eine '
          'E-Mail mit unsigniertem PDF (10.02.2022 09:33 Uhr).', BODY),
        p('11. Februar 2022: Herr Eberhart-Wolframshausen — als IT-Admin '
          'formunwirksam kein Mensch zu verführen — widerspricht sachkundig '
          'und verweist auf § 568 BGB, § 126a BGB.', BODY),
        p('15. Februar 2022: RA Ranftenschwedler-Bielenfels bestätigt die '
          'Einschätzung des Mieters in einem internen Memo.', BODY),
        sp(6),
        p('<b>PHASE 3: Gerichtliches Verfahren AG Bielefeld (März – Oktober 2022)</b>', H2),
        p('09. März 2022: Klageschrift mit qES über beA eingereicht. '
          'Erneute Kündigung in der Klageschrift. Das Gericht druckt aus und '
          'stellt mit Transfervermerk zu.', BODY),
        p('17. März 2022: Zustellung der Klageschrift (Ausdruck + Transfervermerk) '
          'an Herrn Eberhart-Wolframshausen.', BODY),
        p('11. April 2022: Hinweisbeschluss AG Bielefeld zur Formfrage.', BODY),
        p('15. April 2022: Eigenhändige Klageerwiderung von Herrn Eberhart-Wolframshausen '
          '(ohne Anwalt). Er identifiziert das Kernproblem korrekt.', BODY),
        p('13. Mai 2022: Replik der Klägerin mit erneuter qES-Kündigung. '
          'Gleiche Zustellungsproblematik.', BODY),
        p('14. September 2022: Mündliche Verhandlung AG Bielefeld. '
          'Kein Vergleich.', BODY),
        p('11. Oktober 2022: Urteil AG Bielefeld. Klage abgewiesen. '
          'Klägerin trägt Kosten.', BODY),
        sp(6),
        p('<b>PHASE 4: Berufung LG Bielefeld (November 2022 – Juni 2023)</b>', H2),
        p('12. November 2022: Berufungsschrift Klägerin.', BODY),
        p('05. Dezember 2022: Mandatsannahme RA Hassenstein-Heepen '
          'für Herrn Eberhart-Wolframshausen (Berufungsinstanz).', BODY),
        p('28. Januar 2023: Berufungsbegründung (nach Fristverlängerung).', BODY),
        p('15. März 2023: Berufungserwiderung RA Hassenstein-Heepen.', BODY),
        p('20. Juni 2023: Urteil LG Bielefeld. Berufung zurückgewiesen. '
          'Revision zugelassen wegen grundsätzlicher Bedeutung. '
          'Vorsitzender: Dr. Bockenfelder-Senne.', BODY),
        sp(6),
        p('<b>PHASE 5: Revision BGH (August 2023 – November 2024)</b>', H2),
        p('28. August 2023: Revisionsbegründung RA Ranftenschwedler-Bielenfels '
          'beim BGH. Az.: VIII ZR 159/23.', BODY),
        p('04. Oktober 2023: Revisionserwiderung RA Hassenstein-Heepen.', BODY),
        p('22. November 2024: Internes Vorbereitungsmemo Ranftenschwedler-Bielenfels '
          'für BGH-Termin. Einschätzung: Revision aussichtslos.', BODY),
        p('27. November 2024: BGH-Verhandlungstermin. Urteilsverkündung. '
          'Revision zurückgewiesen. Leitsätze a)-c) formuliert. '
          'Kosten der Revision: Klägerin.', BODY),
        sp(6),
        p('<b>PHASE 6: Nachgang (Dezember 2024)</b>', H2),
        p('02. Dezember 2024: Mandantenmemo RA Ranftenschwedler-Bielenfels '
          'an Pferdedrescher-Riesenstein. Bittere Bilanz: '
          'Gesamtschaden ca. EUR 28.415,90.', BODY),
        p('Dezember 2024: Herr Eberhart-Wolframshausen wohnt weiter in der Wohnung. '
          'Mietverhältnis besteht fort — mangels wirksamer Kündigung. '
          'Er zahlt die laufende Miete (weiterhin unregelmäßig).', BODY),
        p('Dezember 2024: Frau Pferdedrescher-Riesenstein erwägt, die Wohnung '
          'zu verkaufen und zieht Konsequenzen aus dem Verfahren: '
          'Künftig nur noch schriftliche Kündigung durch Boten, '
          'kein WhatsApp, kein E-Mail ohne qES.', BODY),
        sp(6), hr(), sp(4),
        p('<b>Gesamtdauer des Verfahrens:</b> Februar 2022 bis November 2024 = '
          '<b>33 Monate</b>', BOLD),
        p('<b>Ergebnis:</b> Klage in drei Instanzen abgewiesen. '
          'IT-Admin-Mieter siegt über Online-Vermieterin durch Formvorschrift.', BOLD),
        p('<b>Kosten:</b> Ca. EUR 28.415,90 Gesamtschaden Klägerin.', BOLD),
        p('<b>Rechtshistorische Bedeutung:</b> BGH VIII ZR 159/23 setzt Leitsätze '
          'zur Verifikationsfunktion der qES und zum Zugang von qES-Erklärungen — '
          'mit unmittelbarem Einfluss auf die Anwendung des § 130e ZPO.', BOLD),
    ]
    return elems



def erweiterung_rechtliche_wuerdigung_vertieft():
    """Vertiefende rechtliche Würdigung (für Ausbildungszwecke)."""
    elems = [pb()]
    elems += section_header("ANHANG K",
                            "VERTIEFENDE RECHTLICHE WÜRDIGUNG (Ausbildungszwecke)")
    elems += [
        p('<b>Für Referendare und Studierende: Die dogmatischen Grundlagen des BGH-Urteils '
          'VIII ZR 159/23</b>', BOLD),
        sp(6), hr(), sp(4),
        p('<b>A. Die Formfunktionen im Überblick</b>', H2),
        p('Das deutsche Recht kennt verschiedene Formvorschriften, die jeweils '
          'unterschiedliche Schutzfunktionen erfüllen. Bei der Schriftform des '
          '§ 126 BGB und der elektronischen Form des § 126a BGB sind '
          'folgende Funktionen zu unterscheiden:', BODY),
        Table([
            ['Funktion', 'Inhalt', 'Wahrung durch qES?'],
            ['Identitätsfunktion', 'Erkennbarkeit des Erklärenden anhand der Unterschrift', 'JA — qES identifiziert Zertifikatsinhaber eindeutig'],
            ['Echtheitsfunktion', 'Sicherung der inhaltlichen Urheberschaft des Unterzeichners', 'JA — Hash des Dokuments mit privatem Schlüssel verbunden'],
            ['Verifikationsfunktion', 'Möglichkeit des Empfängers, Echtheit selbst zu prüfen', 'NUR am elektron. Original prüfbar'],
            ['Warnfunktion', 'Schutz vor übereilten Entscheidungen (besonders bei Ausschlusswirkung)', 'Begrenzt — keine physische Handlung nötig'],
            ['Beweisfunktion', 'Perpetuierung des Erklärungsinhalts', 'JA — Hash unveränderlich'],
        ], colWidths=[110, 200, 145]),
        sp(6),
        p('<b>B. Die Verifikationsfunktion als Kernproblem</b>', H2),
        p('Der BGH hat in VIII ZR 159/23 die Verifikationsfunktion als eigenständige '
          'und für den Zugang der qES-Erklärung konstitutive Funktion anerkannt. '
          'Dies ist dogmatisch bemerkenswert, weil:', BODY),
        p('(a) Der Gesetzgeber bei der Schaffung des § 126a BGB (FormVAnpG 2001) '
          'auf eine explizite Regelung des Zugangs bewusst verzichtet hat '
          '(vgl. BT-Drs. 14/4987, S. 19).', BODY_L),
        p('(b) § 130 BGB auf § 126a BGB anwendbar ist, aber keine spezifische '
          'Anforderung an die Form des Zugangs stellt.', BODY_L),
        p('(c) Der BGH die Verifikationsfunktion nicht aus dem Wortlaut des § 126a BGB, '
          'sondern aus dem Funktionsäquivalenzprinzip ableitet: '
          'Die elektronische Form muss dieselben Schutzfunktionen erfüllen '
          'wie die Schriftform — und dazu gehört, dass der Empfänger die '
          'Echtheit der Unterschrift prüfen kann.', BODY_L),
        BoxedPara(
            '<b>Kritische Würdigung (Lit.):</b><br/>'
            'Ein Teil der Literatur hält die strenge Verifikationsfunktion für überspannt: '
            'Auch beim schriftlichen Original kann der Empfänger die Echtheit der '
            'Unterschrift nur durch Sachverständige prüfen lassen — '
            'eine unmittelbare Prüfmöglichkeit hat er nicht. '
            'Der BGH übersieht, dass die qES technisch zuverlässiger als eine '
            'handschriftliche Unterschrift ist, weil sie kryptographisch gesichert '
            'und nicht fälschbar ist. '
            'Ob der Empfänger die Prüfung tatsächlich vornimmt, ist beim Papieroriginal '
            'ebenso ungewiss wie beim Ausdruck mit Transfervermerk.<br/><br/>'
            '(Diese Kritik wurde von RA Ranftenschwedler-Bielenfels in der '
            'Revisionsbegründung vorgetragen — ohne Erfolg.)',
            bg=colors.HexColor("#FFF3E0"), border=colors.HexColor("#E65100"),
            style=S('krit_s', fontName='Helvetica', fontSize=9, leading=14, textColor=C_BLACK)
        ),
        sp(6),
        p('<b>C. Intertemporales Recht und § 130e ZPO</b>', H2),
        p('Der BGH lehnte eine rückwirkende Anwendung des § 130e ZPO ab. '
          'Die Begründung: Gemäß den allgemeinen Grundsätzen des intertemporalen Rechts '
          'ist die Wirksamkeit einer Kündigung nach dem im Zeitpunkt ihrer Erklärung '
          'geltenden Recht zu beurteilen (lex temporis regit actum).', BODY),
        p('§ 130e ZPO enthält keine Rückwirkungsanordnung. '
          'Der Gesetzgeber wollte die Norm als prospektive Regelung ausgestalten, '
          'nicht als Heilung bereits erfolgter Zustellungen.', BODY),
        p('<b>Exam-Tipp:</b> Im Staatsexamen könnte die Frage auftauchen, '
          'ob § 130e ZPO auf Altfälle anwendbar ist. '
          'Antwort: NEIN — intertemporales Recht, keine Rückwirkungsanordnung, '
          'vgl. BGH VIII ZR 159/23.', BODY),
        sp(6),
        p('<b>D. Schematische Prüfung einer Mietkündigung per qES</b>', H2),
        p('Prüfungsschema für Klausuren und Praxis:', BODY),
        Table([
            ['Schritt', 'Prüfungsfrage', 'Norm', 'Ergebnis im Fall'],
            ['1', 'Liegt ein Mietverhältnis über Wohnraum vor?', '§ 549 BGB', 'JA — Wohnraummietvertrag'],
            ['2', 'Liegt ein Kündigungsgrund vor?', '§ 543 Abs. 2 Nr. 3 BGB', 'JA — Rückstand > 2 Monatsmieten'],
            ['3', 'Ist die Schriftform gewahrt (Abgabe)?', '§§ 568, 126, 126a BGB', 'JA — qES auf Schriftsatz'],
            ['4', 'Ist die qES gültig (Formvoraussetzungen)?', '§ 126a Abs. 1 BGB', 'JA — D-Trust-Zertifikat'],
            ['5', 'Ist die Erklärung zugegangen (§ 130 BGB)?', '§ 130 Abs. 1 S. 1 BGB', 'Streitig — Kernfrage'],
            ['6', 'War der Zugang formgerecht?', 'BGH VIII ZR 159/23', 'NEIN — kein elektron. Original'],
            ['7', 'Gilt § 130e ZPO (nach 17.07.2024)?', '§ 130e ZPO', 'NEIN — Altfall'],
            ['8', 'Ergebnis:', '§ 125 S. 1 BGB', 'Kündigung formunwirksam'],
        ], colWidths=[25, 185, 110, 135]),
        sp(6),
        p('<b>E. Übungsfall für die Klausur</b>', H2),
        BoxedPara(
            '<b>Sachverhalt (vereinfacht):</b><br/>'
            'V ist Vermieter, M ist Mieter einer Wohnung. '
            'M schuldet seit 3 Monaten die Miete (gesamt EUR 2.400,00). '
            'V beauftragt Rechtsanwalt RA mit der Kündigung. '
            'RA erstellt am 01.08.2024 eine qES-Klageschrift mit Kündigungserklärung '
            'und reicht diese über beA ein. '
            'Das Gericht stellt die Klageschrift als Papierausdruck '
            'mit Transfervermerk am 05.08.2024 zu.<br/><br/>'
            '<b>Frage:</b> Ist die Kündigung wirksam?<br/><br/>'
            '<b>Lösung:</b> § 568 Abs. 1 BGB: Schriftform erforderlich. '
            '§ 126 Abs. 3 BGB: qES zulässig. § 126a Abs. 1 BGB: qES-Voraussetzungen erfüllt. '
            '§ 130 Abs. 1 S. 1 BGB: Zugang erforderlich. '
            'Zustellung am 05.08.2024 (= nach 17.07.2024): § 130e ZPO anwendbar! '
            'Formwirksamer Zugang fingiert. '
            'ERGEBNIS: Kündigung wirksam (§ 130e ZPO, da nach 17.07.2024).<br/><br/>'
            'ACHTUNG: Wäre die Klageschrift am 01.06.2024 (= vor 17.07.2024) '
            'eingereicht worden, wäre § 130e ZPO NICHT anwendbar. '
            'Kündigung formunwirksam nach BGH VIII ZR 159/23.',
            bg=colors.HexColor("#E8EAF6"), border=colors.HexColor("#3949AB"),
            style=S('uebung_s', fontName='Helvetica', fontSize=9, leading=14, textColor=C_BLACK)
        ),
    ]
    return elems


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=2.5*cm,
        rightMargin=2.5*cm,
        topMargin=2.2*cm,
        bottomMargin=2.5*cm,
        title="Testakte Mietkündigung Bielefeld — Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen",
        author="Perplexity Computer",
    )

    story = []
    story += teil_01_aktendeckel()
    story += teil_02_inhaltsverzeichnis()
    story += teil_03_mietvertrag()
    story += teil_04_mahnungshistorie()
    story += teil_05_whatsapp()
    story += teil_06_email()
    story += teil_07_antwortmail()
    story += teil_08_anwaltsschreiben()
    story += teil_09_klageschrift()
    story += teil_10_hinweisbeschluss()
    story += teil_11_klageerwiderung()
    story += teil_12_replik()
    story += teil_13_protokoll()
    story += teil_14_urteil_ag()
    story += teil_15_berufung()
    story += teil_16_mandatsannahme()
    story += teil_17_berufungsbegruendung()
    story += teil_18_berufungserwiderung()
    story += teil_19_urteil_lg()
    story += teil_20_revision()
    story += teil_21_revisionserwiderung()
    story += teil_22_stellungnahme_bgh()
    story += teil_23_bgh_urteil()
    story += teil_24_mandantenmemo()
    story += teil_25_online_memo()
    story += teil_26_handschriftnotizen()
    story += teil_27_emailkette()
    story += teil_28_kosten()
    story += teil_29_anlagen()
    story += teil_30_stundenaufstellung()
    # Appendices
    story += erweiterung_rechtsgutachten()
    story += erweiterung_vergleichsverhandlung()
    story += erweiterung_it_admin_analyse()
    story += erweiterung_reformausblick()
    story += erweiterung_schriftsatz_duplik()
    story += erweiterung_zahlungsklagen()
    story += erweiterung_literaturhinweise()
    story += erweiterung_abschlussbemerkung()
    story += erweiterung_parallelverfahren()
    story += erweiterung_praktische_checkliste()
    story += erweiterung_falldokumentation()
    story += erweiterung_rechtliche_wuerdigung_vertieft()

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF erstellt: {OUTPUT_PATH}")
    return OUTPUT_PATH



if __name__ == "__main__":
    build_pdf()
