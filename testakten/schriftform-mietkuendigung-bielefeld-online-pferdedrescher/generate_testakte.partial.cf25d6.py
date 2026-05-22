#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_testakte.py
====================
Generiert die fragmentarische Testakte
  „Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen"
  AG Bielefeld 34 C 421/22 → LG Bielefeld 14 S 88/23 → BGH VIII ZR 159/23

Sachverhalt: Wohnraummiete-Kündigung § 568 BGB Schriftform,
qES § 126a BGB möglich, ABER empfangsbedürftige WE muss formgerecht
ZUGEHEN — Gerichtsausdruck mit Transfervermerk § 298 Abs. 3 ZPO genügt NICHT.

BGH-Urteil vom 27. November 2024 — VIII ZR 159/23.

Schauplatz: Bielefeld (Brackwede, Eckendorfer Straße).
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm, mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ─────────────────────────────────────────────
# Ausgabe-Pfad
# ─────────────────────────────────────────────
OUTPUT_PATH = (
    "/home/user/workspace/claude-fuer-deutsches-recht/testakten/"
    "schriftform-mietkuendigung-bielefeld-online-pferdedrescher/"
    "Testakte_Mietkuendigung_Bielefeld_Pferdedrescher.pdf"
)
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# ─────────────────────────────────────────────
# Farben
# ─────────────────────────────────────────────
C_WA_GREEN   = colors.HexColor("#DCF8C6")   # WhatsApp-Bubble Absender
C_WA_GREY    = colors.HexColor("#ECECEC")   # WhatsApp-Bubble Empfänger
C_WA_BG      = colors.HexColor("#E5DDD5")   # WhatsApp Hintergrund
C_QES_BLUE   = colors.HexColor("#003580")   # qES-Signaturblock Rahmen
C_QES_BG     = colors.HexColor("#EEF4FF")   # qES-Signaturblock Hintergrund
C_STAMP_BG   = colors.HexColor("#F0F0F0")   # Stempel-Kasten Hintergrund
C_STAMP_BD   = colors.HexColor("#888888")   # Stempel-Rahmen
C_HEADING    = colors.HexColor("#1A1A2E")   # Überschriften
C_MUTED      = colors.HexColor("#6B6B6B")   # Fließtext-Grau
C_RED_WARN   = colors.HexColor("#8B0000")   # Warnung
C_ACCENT     = colors.HexColor("#004B87")   # Kanzlei-Blau

PAGE_W, PAGE_H = A4

# ─────────────────────────────────────────────
# Styles
# ─────────────────────────────────────────────
base_styles = getSampleStyleSheet()

def make_style(name, parent="Normal", **kw):
    s = ParagraphStyle(name, parent=base_styles[parent])
    for k, v in kw.items():
        setattr(s, k, v)
    return s

sNormal   = make_style("sNormal",   fontName="Helvetica",      fontSize=9,  leading=13, alignment=TA_JUSTIFY)
sNormalL  = make_style("sNormalL",  fontName="Helvetica",      fontSize=9,  leading=13, alignment=TA_LEFT)
sBold     = make_style("sBold",     fontName="Helvetica-Bold",  fontSize=9,  leading=13, alignment=TA_LEFT)
sH1       = make_style("sH1",       fontName="Helvetica-Bold",  fontSize=14, leading=18, alignment=TA_CENTER, textColor=C_HEADING, spaceAfter=6)
sH2       = make_style("sH2",       fontName="Helvetica-Bold",  fontSize=11, leading=15, alignment=TA_LEFT,   textColor=C_HEADING, spaceAfter=4)
sH3       = make_style("sH3",       fontName="Helvetica-Bold",  fontSize=9,  leading=13, alignment=TA_LEFT,   textColor=C_ACCENT)
sMono     = make_style("sMono",     fontName="Courier",         fontSize=8,  leading=11, alignment=TA_LEFT)
sSmall    = make_style("sSmall",    fontName="Helvetica",       fontSize=7.5,leading=10, alignment=TA_LEFT,   textColor=C_MUTED)
sCenter   = make_style("sCenter",   fontName="Helvetica",       fontSize=9,  leading=13, alignment=TA_CENTER)
sItalic   = make_style("sItalic",   fontName="Helvetica-Oblique",fontSize=8.5,leading=12,alignment=TA_LEFT,  textColor=colors.HexColor("#333366"))
sRed      = make_style("sRed",      fontName="Helvetica-Bold",  fontSize=8.5,leading=12, alignment=TA_LEFT,  textColor=C_RED_WARN)
sCoverBig = make_style("sCoverBig", fontName="Helvetica-Bold",  fontSize=20, leading=26, alignment=TA_CENTER, textColor=C_HEADING)
sCoverSub = make_style("sCoverSub", fontName="Helvetica",       fontSize=10, leading=14, alignment=TA_CENTER, textColor=C_MUTED)
sFooter   = make_style("sFooter",   fontName="Helvetica",       fontSize=7,  leading=9,  alignment=TA_CENTER, textColor=C_MUTED)
sRight    = make_style("sRight",    fontName="Helvetica",       fontSize=9,  leading=13, alignment=TA_RIGHT)

# ─────────────────────────────────────────────
# Hilfsfunktionen
# ─────────────────────────────────────────────

def hr(thickness=0.5, color=colors.lightgrey):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=4, spaceBefore=4)

def sp(h=0.3):
    return Spacer(1, h*cm)

def heading(txt, level=1):
    s = sH1 if level == 1 else (sH2 if level == 2 else sH3)
    return Paragraph(txt, s)

def para(txt, style=None):
    return Paragraph(txt, style or sNormal)

def mono(txt):
    return Paragraph(txt, sMono)

def italic(txt):
    return Paragraph(txt, sItalic)

def bold_para(txt):
    return Paragraph(txt, sBold)

def section_break():
    return [sp(0.5), hr(1, C_HEADING), sp(0.3)]

def page_break():
    return PageBreak()

def qes_block(signer="Dr. Engelbert Ranftenschwedler-Bielenfels",
              cert="D-Trust Public-CA 2-3 2022",
              valid="12.07.2026",
              date="09.03.2022"):
    data = [
        [Paragraph("<b>✦ Qualifizierte Elektronische Signatur (qES) — § 126a BGB</b>", sBold)],
        [Paragraph(f"Signaturinhaber: <b>{signer}</b>", sSmall)],
        [Paragraph(f"Zertifikat-Aussteller: {cert}", sSmall)],
        [Paragraph(f"Gültig bis: {valid} | Signaturzeitpunkt: {date}", sSmall)],
        [Paragraph("Integritäts-Hash (SHA-256): a3f9...c07e [fiktiv] | eIDAS konform", sSmall)],
    ]
    t = Table(data, colWidths=[16*cm])
    t.setStyle(TableStyle([
        ("BOX",        (0,0), (-1,-1), 1.5, C_QES_BLUE),
        ("BACKGROUND", (0,0), (-1,-1), C_QES_BG),
        ("TOPPADDING",    (0,0),(-1,-1), 4),
        ("BOTTOMPADDING", (0,0),(-1,-1), 4),
        ("LEFTPADDING",   (0,0),(-1,-1), 8),
        ("RIGHTPADDING",  (0,0),(-1,-1), 8),
    ]))
    return t

def transfervermerk_block(date="09.03.2022", signee="Dr. E. Ranftenschwedler-Bielenfels"):
    data = [
        [Paragraph("<b>TRANSFERVERMERK gem. § 298 Abs. 3 ZPO</b>", sBold)],
        [Paragraph("Das vorliegende Dokument ist ein Ausdruck eines bei Gericht elektronisch eingegangenen Schriftsatzes.", sSmall)],
        [Paragraph(f"(1) Ergebnis der Integritätsprüfung: <b>Signatur gültig</b>", sSmall)],
        [Paragraph(f"(2) Inhaber der Signatur: <b>{signee}</b>", sSmall)],
        [Paragraph(f"(3) Zeitpunkt der Signatur: <b>{date}, 14:23:07 Uhr</b>", sSmall)],
        [Paragraph("Gefertigt durch: Geschäftsstelle AG Bielefeld — Justizangestellte Kemmner", sSmall)],
        [Paragraph("<i>Hinweis: Dieser Ausdruck ersetzt NICHT den formgerechten Zugang der qES-Willenserklärung beim Erklärungsgegner (vgl. BGH VIII ZR 159/23).</i>", sSmall)],
    ]
    t = Table(data, colWidths=[16*cm])
    t.setStyle(TableStyle([
        ("BOX",        (0,0), (-1,-1), 1.0, C_STAMP_BD),
        ("BACKGROUND", (0,0), (-1,-1), C_STAMP_BG),
        ("TOPPADDING",    (0,0),(-1,-1), 4),
        ("BOTTOMPADDING", (0,0),(-1,-1), 3),
        ("LEFTPADDING",   (0,0),(-1,-1), 8),
        ("RIGHTPADDING",  (0,0),(-1,-1), 8),
    ]))
    return t


def wa_bubble(text, sender=True, time_str="10:23", status="✓✓"):
    """Simuliert eine WhatsApp-Nachricht als Tabellen-Zeile."""
    bg = C_WA_GREEN if sender else C_WA_GREY
    align = TA_RIGHT if sender else TA_LEFT
    name = "Pferdedrescher-Riesenstein" if sender else "Eberhart-Wolframshausen"
    name_style = make_style(f"waname_{hash(name)}", fontName="Helvetica-Bold", fontSize=7, leading=9,
                             textColor=C_ACCENT if sender else colors.HexColor("#5B0E91"))
    body_style = make_style(f"wabody_{hash(text[:10])}", fontName="Helvetica", fontSize=8.5, leading=12)
    time_style = make_style(f"watime_{hash(text[:5])}", fontName="Helvetica", fontSize=7, leading=9,
                             textColor=C_MUTED, alignment=TA_RIGHT)
    cell = [
        Paragraph(name, name_style),
        Paragraph(text, body_style),
        Paragraph(f"{time_str} {status}", time_style),
    ]
    if sender:
        data = [["", cell]]
        col_widths = [5*cm, 11*cm]
    else:
        data = [[cell, ""]]
        col_widths = [11*cm, 5*cm]
    t = Table(data, colWidths=col_widths)
    fill_col = 1 if sender else 0
    t.setStyle(TableStyle([
        ("BACKGROUND", (fill_col, 0), (fill_col, 0), bg),
        ("BOX",        (fill_col, 0), (fill_col, 0), 0.5, colors.HexColor("#BBBBBB")),
        ("VALIGN",     (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",    (fill_col,0),(fill_col,0), 5),
        ("BOTTOMPADDING", (fill_col,0),(fill_col,0), 5),
        ("LEFTPADDING",   (fill_col,0),(fill_col,0), 6),
        ("RIGHTPADDING",  (fill_col,0),(fill_col,0), 6),
    ]))
    return t


def email_block(date_str, sender, recipient, subject, body_lines, has_attachment=False, has_qes=False):
    """Simuliert einen E-Mail-Block."""
    rows = [
        [Paragraph("<b>E-MAIL</b>", sBold), Paragraph("", sNormal)],
        [Paragraph("Von:", sSmall), Paragraph(sender, sNormalL)],
        [Paragraph("An:", sSmall), Paragraph(recipient, sNormalL)],
        [Paragraph("Datum:", sSmall), Paragraph(date_str, sNormalL)],
        [Paragraph("Betreff:", sSmall), Paragraph(f"<b>{subject}</b>", sBold)],
    ]
    if has_attachment:
        attach_txt = "📎 Kuendigung_Wohnung_EckStr188_App4.pdf"
        if has_qes:
            attach_txt += " [qES-signiert ✦]"
        else:
            attach_txt += " [OHNE qES — nicht formgerecht i.S.v. § 126a BGB]"
        rows.append([Paragraph("Anlage:", sSmall), Paragraph(attach_txt, sSmall)])
    t = Table(rows, colWidths=[2.5*cm, 13.5*cm])
    t.setStyle(TableStyle([
        ("BOX",       (0,0),(-1,-1), 0.8, C_MUTED),
        ("GRID",      (0,0),(-1,-1), 0.3, colors.HexColor("#DDDDDD")),
        ("BACKGROUND",(0,0),(-1,-1), colors.HexColor("#F8F8F8")),
        ("BACKGROUND",(0,0),(1,0),   C_ACCENT),
        ("TEXTCOLOR", (0,0),(1,0),   colors.white),
        ("FONTNAME",  (0,1),(-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0),(-1,-1), 8),
        ("TOPPADDING",    (0,0),(-1,-1), 3),
        ("BOTTOMPADDING", (0,0),(-1,-1), 3),
        ("LEFTPADDING",   (0,0),(-1,-1), 6),
    ]))
    body_elems = [sp(0.2), t, sp(0.2)]
    body_elems.append(Paragraph("─" * 90, sSmall))
    for line in body_lines:
        body_elems.append(Paragraph(line if line else "&nbsp;", sMono))
    return body_elems


# ─────────────────────────────────────────────
# Seitenrahmen-Callback
# ─────────────────────────────────────────────
def on_page(canvas_obj, doc):
    canvas_obj.saveState()
    # Kopfzeile
    canvas_obj.setFont("Helvetica", 7)
    canvas_obj.setFillColor(C_MUTED)
    canvas_obj.drawString(2.0*cm, PAGE_H - 1.3*cm,
        "TESTAKTE — AG Bielefeld 34 C 421/22 | LG Bielefeld 14 S 88/23 | BGH VIII ZR 159/23")
    canvas_obj.drawRightString(PAGE_W - 2.0*cm, PAGE_H - 1.3*cm,
        "Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen")
    canvas_obj.line(2.0*cm, PAGE_H - 1.5*cm, PAGE_W - 2.0*cm, PAGE_H - 1.5*cm)
    # Fußzeile
    canvas_obj.line(2.0*cm, 1.5*cm, PAGE_W - 2.0*cm, 1.5*cm)
    canvas_obj.setFont("Helvetica", 7)
    canvas_obj.drawCentredString(PAGE_W/2, 1.1*cm,
        f"Seite {doc.page}  |  FIKTIVE TESTAKTE — kein echtes Verfahren — alle Namen frei erfunden")
    canvas_obj.restoreState()


# ─────────────────────────────────────────────
# BESTANDTEILE
# ─────────────────────────────────────────────

def b01_aktendeckel():
    """1. Aktendeckel mit Bielefeld-Sparrenburg-ASCII"""
    sparrenburg = """\
           /\\  /\\
          /  \\/  \\
         | Sparren|
         |  burg  |
        /|________|\\
       / |        | \\
      /  |  1241  |  \\
     /   |________|   \\
    /____| Bielefeld |____\\
    
    [ B I E L E F E L D  — falls es das gibt ]
    """
    elems = []
    elems.append(sp(2))
    elems.append(Paragraph("TESTAKTE", make_style("decktitle", fontName="Helvetica-Bold", fontSize=28,
                                                   alignment=TA_CENTER, textColor=C_HEADING)))
    elems.append(sp(0.3))
    elems.append(Paragraph("Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen", sCoverBig))
    elems.append(sp(0.2))
    elems.append(Paragraph("Räumung und Herausgabe wegen Zahlungsverzug", sCoverSub))
    elems.append(sp(0.5))
    elems.append(hr(2, C_ACCENT))
    elems.append(sp(0.3))
    data = [
        ["Aktenzeichen AG:", "34 C 421/22 (AG Bielefeld)"],
        ["Aktenzeichen LG:", "14 S 88/23 (LG Bielefeld)"],
        ["Aktenzeichen BGH:", "VIII ZR 159/23"],
        ["BGH-Urteil:", "27. November 2024"],
        ["Streitgegenstand:", "Räumung und Herausgabe, § 568 BGB Schriftform, § 126a BGB qES"],
        ["Streitwert:", "EUR 7.787,64 (Räumung) + Zahlungsantrag"],
        ["Status:", "Revision zurückgewiesen — rechtskräftig"],
    ]
    t = Table(data, colWidths=[5*cm, 11*cm])
    t.setStyle(TableStyle([
        ("FONTNAME",  (0,0),(0,-1), "Helvetica-Bold"),
        ("FONTNAME",  (1,0),(1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0),(-1,-1), 9),
        ("GRID",      (0,0),(-1,-1), 0.3, colors.lightgrey),
        ("BACKGROUND",(0,0),(0,-1), colors.HexColor("#F0F4FF")),
        ("TOPPADDING",    (0,0),(-1,-1), 4),
        ("BOTTOMPADDING", (0,0),(-1,-1), 4),
        ("LEFTPADDING",   (0,0),(-1,-1), 6),
    ]))
    elems.append(t)
    elems.append(sp(0.5))
    # Sparrenburg ASCII
    ascii_style = make_style("ascii", fontName="Courier", fontSize=9, leading=12, alignment=TA_CENTER)
    elems.append(Paragraph(sparrenburg.replace("\n", "<br/>"), ascii_style))
    elems.append(sp(0.3))
    elems.append(Paragraph(
        "<i>Bielefeld-Verschwörungstheorie: Diese Stadt existiert möglicherweise nicht. "
        "Auch diese Akte existiert nicht. Alle Personen, Anschriften und Vorgänge sind frei erfunden "
        "und dienen ausschließlich Testzwecken (§ 568 BGB, § 126a BGB, BGH VIII ZR 159/23).</i>",
        make_style("caveat", fontName="Helvetica-Oblique", fontSize=7.5, leading=11,
                   alignment=TA_CENTER, textColor=C_MUTED)))
    elems.append(sp(1))
    elems.append(Paragraph("Ranftenschwedler Ostkamp Rechtsanwälte mbB", sCenter))
    elems.append(Paragraph("Niederwall 12 · 33602 Bielefeld · Tel.: 0521 / 88 44 22-0", sCenter))
    elems.append(page_break())
    return elems


def b02_inhaltsverzeichnis():
    """2. Inhaltsverzeichnis mit nicht-existenten Querverweisen"""
    elems = []
    elems.append(heading("INHALTSVERZEICHNIS", 1))
    elems.append(sp(0.2))
    elems.append(Paragraph("<i>Hinweis: Seitenangaben beziehen sich auf Akten-Folionummern (Bl.), "
                           "nicht PDF-Seiten. Sonderband II wird separat geführt (vgl. Bl. 312 ff.).</i>", sSmall))
    elems.append(sp(0.3))
    toc = [
        ("Nr.", "Bezeichnung", "Bl.", "Datum"),
        ("1", "Aktendeckel", "1", "—"),
        ("2", "Inhaltsverzeichnis (dieses)", "2-3", "lfd."),
        ("3", "Mietvertrag-Auszug (4 Seiten)", "4-7", "03.04.2017"),
        ("4", "Mahnungs-Historie (Tabelle)", "8-9", "lfd. bis 02/2022"),
        ("5", "WhatsApp-Verlauf 08.-10.02.2022 (Screenshot-Simulation)", "10-15", "08.-10.02.2022"),
        ("6", "E-Mail Pferdedrescher-Riesenstein 10.02.2022 + PDF-Anhang", "16-17", "10.02.2022"),
        ("7", "Antwort-Mail Eberhart-Wolframshausen 11.02.2022", "18", "11.02.2022"),
        ("8", "Anwaltsschreiben RA Ranftenschwedler-Bielenfels 15.02.2022", "19-21", "15.02.2022"),
        ("9", "Klageschrift vom 09.03.2022 (qES)", "22-29", "09.03.2022"),
        ("10", "Hinweisbeschluss AG Bielefeld 11.04.2022", "30-31", "11.04.2022"),
        ("11", "Klageerwiderung Mieter (eigenhändig, fragmentarisch)", "32-35", "02.05.2022"),
        ("12", "Replik Klägerin / erneute Kündigung im Schriftsatz 13.05.2022 (qES)", "36-39", "13.05.2022"),
        ("13", "Protokoll MV AG Bielefeld 14.09.2022", "40-41", "14.09.2022"),
        ("14", "Urteil AG Bielefeld 34 C 421/22 — Klage abgewiesen", "42-48", "11.10.2022"),
        ("15", "Berufungsschrift Klägerin", "49-50", "12.11.2022"),
        ("16", "Mandatsannahme RA Hassenstein-Heepen", "51", "15.11.2022"),
        ("17", "Berufungsbegründung Klägerin (8 Seiten)", "52-59", "15.01.2023"),
        ("18", "Berufungserwiderung Mieter (RA Hassenstein-Heepen)", "60-64", "01.03.2023"),
        ("19", "LG-Urteil Bielefeld 14 S 88/23 — Berufung zurückgewiesen", "65-74", "20.06.2023"),
        ("20", "Revisionsbegründung BGH VIII ZR 159/23 (11 Seiten)", "75-85", "28.08.2023"),
        ("21", "Revisionserwiderung Mieter", "86-91", "15.10.2023"),
        ("22", "Stellungnahme zum Verhandlungstermin BGH 27.11.2024", "92-93", "20.11.2024"),
        ("23", "BGH-Urteil-Tenor VIII ZR 159/23 + Volltext-Auszug", "94-99", "27.11.2024"),
        ("24", "Mandantenmemo RA Ranftenschwedler-Bielenfels 02.12.2024", "100-103", "02.12.2024"),
        ("25", "\"Online-Vermieter\"-Memo (3 Seiten)", "104-106", "05.12.2024"),
        ("26", "Handschriftliche Mieter-Notizen Eberhart-Wolframshausen", "Passim", "div."),
        ("27", "E-Mail-Kette Ranftenschwedler ↔ Pferdedrescher-Riesenstein (8 Seiten)", "107-114", "Feb.2022-Nov.2024"),
        ("28", "Kostenfestsetzungsbeschluss-Entwurf", "115-116", "Dezember 2024"),
        ("29", "Anlagenverzeichnis K-MIET-1 bis K-MIET-34", "117-118", "lfd."),
        ("30", "Stundenaufstellung Ranftenschwedler Ostkamp Feb. 2022 - Nov. 2024", "119-121", "Nov. 2024"),
        ("—", "SONDERBAND II (Anlagen, Belege) — vgl. Bl. 312 ff. [nicht beigefügt]", "—", "div."),
    ]
    col_widths = [1*cm, 9.5*cm, 2*cm, 3.5*cm]
    table_data = []
    for row in toc:
        table_data.append([Paragraph(str(c), sSmall) for c in row])
    t = Table(table_data, colWidths=col_widths, repeatRows=1)
    header_bg = C_ACCENT
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0),(-1,0), header_bg),
        ("TEXTCOLOR",  (0,0),(-1,0), colors.white),
        ("FONTNAME",   (0,0),(-1,0), "Helvetica-Bold"),
        ("FONTSIZE",   (0,0),(-1,-1), 8),
        ("GRID",       (0,0),(-1,-1), 0.3, colors.lightgrey),
        ("ROWBACKGROUNDS", (0,1),(-1,-1), [colors.white, colors.HexColor("#F7F9FF")]),
        ("TOPPADDING",    (0,0),(-1,-1), 3),
        ("BOTTOMPADDING", (0,0),(-1,-1), 3),
        ("LEFTPADDING",   (0,0),(-1,-1), 5),
    ]))
    elems.append(t)
    elems.append(page_break())
    return elems


def b03_mietvertrag():
    """3. Mietvertrag-Auszug (4 Seiten)"""
    elems = []
    elems.append(heading("MIETVERTRAG — AUSZUG", 1))
    elems.append(Paragraph("(Originalvertrag: AG Bielefeld 34 C 421/22, Anlage K-MIET-1)", sSmall))
    elems.append(sp(0.3))
    elems += [
        bold_para("MIETVERTRAG über Wohnräume"),
        sp(0.2),
        para("abgeschlossen zwischen"),
        sp(0.1),
        bold_para("Hildegunde Pferdedrescher-Riesenstein"),
        para("wohnhaft: Ottilienweg 23, 33647 Bielefeld-Brackwede"),
        para("— nachfolgend: <b>Vermieterin</b> —"),
        sp(0.1),
        bold_para("und"),
        sp(0.1),
        bold_para("Götz-Sieghart Eberhart-Wolframshausen"),
        para("geb. am 14. März 1981 in Detmold"),
        para("— nachfolgend: <b>Mieter</b> —"),
        sp(0.3),
        hr(),
        heading("§ 1 Mietobjekt", 2),
        para("Die Vermieterin vermietet dem Mieter die im Hause <b>Eckendorfer Straße 188, 33609 Bielefeld</b> "
             "befindliche Wohnung im Obergeschoss, Appartement Nr. 4 (im Folgenden: „die Wohnung"). "
             "Die Wohnung umfasst 3 Zimmer, Küche, Bad/WC, Abstellraum; Nutzfläche ca. 74,5 m², "
             "zuzüglich anteiliger Kellerabteil Nr. 4."),
        sp(0.2),
        heading("§ 2 Mietbeginn und Mietdauer", 2),
        para("Das Mietverhältnis beginnt am <b>01. Mai 2017</b>. Es wird auf unbestimmte Zeit geschlossen. "
             "Es gelten die gesetzlichen Kündigungsfristen."),
        sp(0.2),
        heading("§ 3 Mietzins und Nebenkosten", 2),
        para("(1) Die monatliche Kaltmiete beträgt <b>EUR 520,00</b>."),
        para("(2) Der Mieter zahlt monatliche Vorauszahlungen auf die Betriebs- und Nebenkosten "
             "in Höhe von <b>EUR 128,97</b>."),
        para("(3) Die <b>Bruttomiete (Gesamtmiete)</b> beträgt somit monatlich <b>EUR 648,97</b>."),
        para("(4) Die Miete ist bis zum <b>3. Werktag</b> eines jeden Monats auf das Konto der Vermieterin zu überweisen. "
             "IBAN: DE12 4726 0121 0123 4567 89, Sparkasse Bielefeld."),
        sp(0.2),
        page_break(),
    ]
    elems += [
        heading("Mietvertrag — Auszug (Seite 2 von 4)", 1),
        heading("§ 7 Schriftformklausel", 2),
        para("(1) Änderungen und Ergänzungen dieses Vertrages — <b>einschließlich dieser Klausel</b> — "
             "bedürfen der Schriftform im Sinne von <b>§ 126 BGB</b>. "
             "Mündliche Nebenabreden bestehen nicht und haben keine rechtliche Wirkung."),
        para("(2) Die gesetzliche Schriftform (§ 126 Abs. 1 BGB) kann gemäß § 126 Abs. 3 BGB "
             "durch die elektronische Form (§ 126a BGB) ersetzt werden, sofern nicht das Gesetz "
             "ausdrücklich etwas anderes bestimmt. <b>Für die Kündigung gilt § 568 BGB.</b>"),
        para("(3) Die Vermieterin weist ausdrücklich darauf hin, dass Kündigungen, Mieterhöhungen "
             "und sonstige rechtsgestaltende Erklärungen der Schriftform bedürfen und nur wirksam sind, "
             "wenn sie dem Erklärungsgegner in dieser Form <b>zugehen</b> (§ 130 BGB)."),
        sp(0.2),
        heading("§ 8 Kündigung", 2),
        para("(1) Jede Partei kann das Mietverhältnis ordentlich unter Einhaltung der gesetzlichen "
             "Fristen kündigen (§ 573c BGB). Die Kündigung muss schriftlich erfolgen (§ 568 Abs. 1 BGB)."),
        para("(2) Bei Zahlungsverzug steht der Vermieterin das Recht zur außerordentlichen fristlosen "
             "Kündigung nach § 543 Abs. 2 Nr. 3, § 569 Abs. 3 BGB zu, sofern der Mieter mit mehr als "
             "zwei Monatsmieten in Rückstand ist."),
        para("(3) <b>Besondere Vereinbarung zur elektronischen Kommunikation (§ 7a):</b> "
             "Die Parteien vereinbaren, dass allgemeine Korrespondenz (Mahnungen, Ankündigungen von "
             "Handwerkerterminen etc.) auch per E-Mail an die jeweils zuletzt mitgeteilte Adresse "
             "übermittelt werden kann. <u>Diese Vereinbarung erstreckt sich nicht auf rechtsgestaltende "
             "Willenserklärungen, insbesondere nicht auf Kündigungen.</u>"),
        sp(0.2),
        heading("§ 12 Hausordnung und Nutzung", 2),
        para("Der Mieter verpflichtet sich, die Wohnung pfleglich zu behandeln und die anliegende "
             "Hausordnung zu beachten. Näheres regelt Anlage 2."),
        sp(0.2),
        page_break(),
    ]
    elems += [
        heading("Mietvertrag — Auszug (Seite 3 von 4)", 1),
        heading("§ 14 Besondere Vereinbarungen / Online-Dimension", 2),
        para("(1) <b>Online-Korrespondenz:</b> Die Vermieterin betreibt im Rahmen ihrer selbständigen "
             "Tätigkeit als Online-Marketing-Beraterin einen Webshop und ist digital aufgestellt. "
             "Der Mieter ist als IT-Administrator ebenfalls technisch versiert. Beide Parteien "
             "erklären sich bereit, allgemeine Verwaltungskorrespondenz über digitale Kanäle abzuwickeln."),
        para("(2) <b>Ausdrücklicher Hinweis:</b> Ungeachtet Abs. (1) bleibt es bei der "
             "gesetzlichen Formvorschrift des § 568 Abs. 1 BGB für Kündigungen. "
             "Insbesondere WhatsApp-Nachrichten oder E-Mails ohne qualifizierte elektronische Signatur "
             "(§ 126a BGB) genügen der Schriftform für Kündigungen nicht. "
             "Selbst eine qES-signierte E-Mail muss dem Empfänger so zugehen, dass er die "
             "Signatur überprüfen kann (Verifikationsfunktion, vgl. BGH-Rechtsprechung)."),
        para("(3) Für den Webshop-Kontaktbereich gilt: Nachrichten über das Kontaktformular "
             "der Vermieterin (www.pferdedrescher-online-marketing.de) haben keinen rechtlichen "
             "Erklärungswert für rechtsgestaltende Erklärungen im Mietverhältnis."),
        sp(0.5),
        heading("Unterschriften", 2),
        sp(0.3),
        para("Bielefeld, den <b>03. April 2017</b>"),
        sp(0.4),
        t_unterschrift("Hildegunde Pferdedrescher-Riesenstein", "Vermieterin"),
        sp(0.2),
        t_unterschrift("Götz-Sieghart Eberhart-Wolframshausen", "Mieter"),
        sp(0.3),
        Paragraph("<i>[Anlage K-MIET-1, Bl. 4-7 der Akte — vollständiger Mietvertrag in Sonderband II]</i>", sSmall),
        page_break(),
    ]
    elems += [
        heading("Mietvertrag — Auszug (Seite 4 von 4): Anlage 1 — Hausordnung (Auszug)", 1),
        para("Die Hausordnung regelt das Zusammenleben der Mieter im Hause Eckendorfer Straße 188. "
             "Sie ist Bestandteil des Mietvertrages. Zuwiderhandlungen können nach Abmahnung "
             "zur Kündigung des Mietverhältnisses führen."),
        sp(0.2),
        bold_para("§ 3 Ruhezeiten:"),
        para("Zwischen 22:00 Uhr und 06:00 Uhr sowie an Sonn- und Feiertagen ist Lärm, "
             "der andere Hausbewohner stört, zu unterlassen. "
             "Musikwiedergabe über Lautsprecher ist nach 22:00 Uhr untersagt. "
             "Ausnahmen bedürfen der schriftlichen Genehmigung der Vermieterin."),
        sp(0.2),
        bold_para("§ 7 Digitale Infrastruktur:"),
        para("Das im Haus installierte W-LAN-Netz ist Eigentum der Vermieterin. "
             "Der Mieter darf das Netz für private Zwecke nutzen (SSID: EckStr188-MietNetz, "
             "Passwort: separat mitgeteilt). Die Nutzung für geschäftliche Zwecke ist nicht gestattet. "
             "Der IT-Administrator Eberhart-Wolframshausen ist ausdrücklich nicht berechtigt, "
             "Router-Einstellungen eigenmächtig zu verändern."),
        sp(0.3),
        Paragraph("<i>[Ende Mietvertrag-Auszug — für vollständigen Text vgl. Sonderband II, Bl. 1-22]</i>", sSmall),
        page_break(),
    ]
    return elems


def t_unterschrift(name, rolle):
    data = [[Paragraph(f"___________________________ &nbsp;&nbsp;&nbsp; {name}", sNormalL)],
            [Paragraph(f"({rolle})", sSmall)]]
    t = Table(data, colWidths=[16*cm])
    return t


def b04_mahnungshistorie():
    """4. Mahnungs-Historie als Tabelle"""
    elems = []
    elems.append(heading("MAHNUNGS-HISTORIE", 1))
    elems.append(Paragraph("Mietkonto Eberhart-Wolframshausen, Eckendorfer Str. 188, App. 4 — Frühjahr 2019 bis Februar 2022", sSmall))
    elems.append(sp(0.2))
    elems.append(Paragraph("Bruttomiete monatlich: EUR 648,97 | Kaltmiete: EUR 520,00 | NK-Vorauszahlung: EUR 128,97", sBold))
    elems.append(sp(0.3))

    header = ["Monat/Jahr", "Soll (€)", "Ist (€)", "Saldo (€)", "Rückstand (€)", "Bemerkung"]
    # Daten simuliert gemäß Sachverhalt
    rows_data = [
        ["Feb 2019", "648,97", "0,00",   "-648,97",  "648,97",   "Erstmals kein Zahlungseingang"],
        ["Mär 2019", "648,97", "648,97",  "0,00",    "648,97",   "Zahlung nur lfd. Monat"],
        ["Apr 2019", "648,97", "200,00", "-448,97",  "1.097,94", "Teilzahlung"],
        ["Mai 2019", "648,97", "648,97",  "0,00",    "1.097,94", "Mahnung No. 1 (07.05.2019)"],
        ["Jun 2019", "648,97", "448,97", "-200,00",  "1.297,94", "Teilzahlung"],
        ["Jul 2019", "648,97", "648,97",  "0,00",    "1.297,94", "Mahnung No. 2 (02.07.2019)"],
        ["Aug 2019", "648,97", "648,97",  "0,00",    "1.297,94", ""],
        ["Sep 2019", "648,97", "1.000,00","+351,03", "946,91",   "Überzahlung"],
        ["Okt 2019", "648,97", "648,97",  "0,00",    "946,91",   ""],
        ["Nov 2019", "648,97", "648,97",  "0,00",    "946,91",   "Mahnung No. 3 (04.11.2019)"],
        ["Dez 2019", "648,97", "0,00",   "-648,97",  "1.595,88", "Kein Zahlungseingang"],
        ["Jan 2020", "648,97", "648,97",  "0,00",    "1.595,88", ""],
        ["Feb 2020", "648,97", "648,97",  "0,00",    "1.595,88", "RA-Schreiben 10.02.2020"],
        ["Mär 2020", "648,97", "648,97",  "0,00",    "1.595,88", "COVID-Stundungsanfrage abgelehnt"],
        ["Apr 2020", "648,97", "350,00", "-298,97",  "1.894,85", ""],
        ["Mai 2020", "648,97", "648,97",  "0,00",    "1.894,85", ""],
        ["Jun 2020", "648,97", "800,00", "+151,03",  "1.743,82", ""],
        ["Jul 2020", "648,97", "648,97",  "0,00",    "1.743,82", ""],
        ["Aug 2020", "648,97", "648,97",  "0,00",    "1.743,82", "Mahnung No. 4 per E-Mail"],
        ["Sep 2020", "648,97", "648,97",  "0,00",    "1.743,82", ""],
        ["Okt 2020", "648,97", "500,00", "-148,97",  "1.892,79", ""],
        ["Nov 2020", "648,97", "648,97",  "0,00",    "1.892,79", ""],
        ["Dez 2020", "648,97", "0,00",   "-648,97",  "2.541,76", "Kein Zahlungseingang"],
        ["Jan 2021", "648,97", "0,00",   "-648,97",  "3.190,73", "Rückstand > 2 Monatsmieten!"],
        ["Feb 2021", "648,97", "900,00", "+251,03",  "2.939,70", "Überzahlung, noch > 2 MM Rückstand"],
        ["Mär 2021", "648,97", "900,00", "+251,03",  "2.688,67", "lfd. Überzahlungen"],
        ["Apr 2021", "648,97", "900,00", "+251,03",  "2.437,64", ""],
        ["Mai 2021", "648,97", "900,00", "+251,03",  "2.186,61", ""],
        ["Jun 2021", "648,97", "900,00", "+251,03",  "1.935,58", ""],
        ["Jul 2021", "648,97", "900,00", "+251,03",  "1.684,55", ""],
        ["Aug 2021", "648,97", "900,00", "+251,03",  "1.433,52", ""],
        ["Sep 2021", "648,97", "900,00", "+251,03",  "1.182,49", "Rückstand sinkt, aber > 2 MM"],
        ["Okt 2021", "648,97", "900,00", "+251,03",  "931,46",   "ca. 1,5 Monatsmieten"],
        ["Nov 2021", "648,97", "648,97",  "0,00",    "931,46",   "Überzahlungen enden"],
        ["Dez 2021", "648,97", "648,97",  "0,00",    "931,46",   ""],
        ["Jan 2022", "648,97", "0,00",   "-648,97",  "1.580,43", "Kein Eingang — Eskalation"],
        ["Feb 2022", "648,97", "0,00",   "-648,97",  "2.229,40", "Kündigung 10.02.2022 (formunwirksam!)"],
    ]
    col_widths = [2.2*cm, 2*cm, 2*cm, 2*cm, 2.5*cm, 5.3*cm]
    table_rows = [[Paragraph(h, make_style(f"th{i}", fontName="Helvetica-Bold", fontSize=7.5,
                                           alignment=TA_CENTER)) for i,h in enumerate(header)]]
    for i, row in enumerate(rows_data):
        bg = colors.HexColor("#FFF0F0") if "Kein Zahlungseingang" in row[5] or "formunwirksam" in row[5] else \
             colors.HexColor("#F0FFF0") if "Überzahlung" in row[5] or "+" in row[3] else colors.white
        style = make_style(f"td{i}", fontName="Helvetica", fontSize=7.5, alignment=TA_CENTER)
        last_style = make_style(f"tdl{i}", fontName="Helvetica", fontSize=7, alignment=TA_LEFT)
        table_rows.append([Paragraph(c, style if j < 5 else last_style)
                           for j, c in enumerate(row)])
    t = Table(table_rows, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0),(-1,0), C_ACCENT),
        ("TEXTCOLOR",  (0,0),(-1,0), colors.white),
        ("GRID",       (0,0),(-1,-1), 0.3, colors.lightgrey),
        ("ROWBACKGROUNDS", (0,1),(-1,-1), [colors.white, colors.HexColor("#F7F9FF")]),
        ("TOPPADDING",    (0,0),(-1,-1), 2),
        ("BOTTOMPADDING", (0,0),(-1,-1), 2),
        ("LEFTPADDING",   (0,0),(-1,-1), 3),
        ("RIGHTPADDING",  (0,0),(-1,-1), 3),
    ]))
    elems.append(t)
    elems.append(sp(0.3))
    elems.append(Paragraph(
        "<b>Ergebnis:</b> Per 10. Februar 2022 besteht ein Mietrückstand von <b>EUR 2.229,40</b> "
        "(entspricht ca. 3,4 Monatsmieten). Der Tatbestand des § 543 Abs. 2 Nr. 3 lit. b) BGB "
        "(Rückstand mit mehr als zwei Monatsmieten) ist grundsätzlich erfüllt. "
        "Die Kündigung scheiterte jedoch aus <b>Formgründen</b> (§ 568 Abs. 1 BGB, § 125 Satz 1 BGB).",
        sRed))
    elems.append(page_break())
    return elems


def b05_whatsapp():
    """5. WhatsApp-Verlauf (6 Seiten simuliert)"""
    elems = []
    elems.append(heading("WHATSAPP-VERLAUF", 1))
    elems.append(Paragraph("Pferdedrescher-Riesenstein (Vermieterin) → Eberhart-Wolframshausen (Mieter)", sSmall))
    elems.append(Paragraph("08. – 10. Februar 2022 | Simulation — kein echter Screenshot", sSmall))
    elems.append(sp(0.2))
    # WhatsApp-Hintergrund-Tabelle simuliert
    wa_header = Table(
        [[Paragraph("💬 WhatsApp | Götz-Sieghart Eberhart-Wolframshausen | Online zuletzt: 10.02.2022",
                    make_style("wah", fontName="Helvetica-Bold", fontSize=9, textColor=colors.white))]],
        colWidths=[17*cm])
    wa_header.setStyle(TableStyle([
        ("BACKGROUND", (0,0),(-1,-1), colors.HexColor("#075E54")),
        ("TOPPADDING",    (0,0),(-1,-1), 5),
        ("BOTTOMPADDING", (0,0),(-1,-1), 5),
        ("LEFTPADDING",   (0,0),(-1,-1), 8),
    ]))
    elems.append(wa_header)
    elems.append(sp(0.1))

    messages = [
        (True, "08.02.2022", "Lieber Herr Eberhart-Wolframshausen, ich habe festgestellt, dass Sie für "
               "Januar und Februar 2022 noch keine Miete überwiesen haben. Gesamtrückstand über EUR 2.000,–. "
               "Bitte überweisen Sie umgehend. Freundliche Grüße, Hildegunde Pferdedrescher-Riesenstein",
               "14:05", "✓✓"),
        (False, "08.02.2022", "Frau Pferdedrescher-Riesenstein, ich bin gerade auf einer Fortbildung "
                "in Paderborn. Zahle nächste Woche.", "14:47", "✓✓"),
        (True, "08.02.2022", "Herr Eberhart-Wolframshausen, das haben Sie schon mehrfach gesagt. "
               "Der Rückstand besteht seit Jahren! Bitte spätestens bis 10.02.2022.", "15:12", "✓✓"),
        (False, "09.02.2022", "Ja, ich zahle.", "09:03", "✓✓"),
        (True, "09.02.2022", "Ich habe immer noch keinen Zahlungseingang. Ich mache mir Sorgen. "
               "Sie haben schon mehrfach Zahlungen verschoben. Wenn bis morgen nichts eingeht, "
               "sehe ich mich gezwungen, rechtliche Schritte einzuleiten.", "18:30", "✓✓"),
        (False, "09.02.2022", "OK ich überweise morgen früh.", "18:45", "✓"),
        (True, "10.02.2022", "Es ist 12:00 Uhr. Kein Zahlungseingang. "
               "Herr Eberhart-Wolframshausen, ich habe kein Verständnis mehr für die Situation. "
               "Ich habe selbst laufende Kosten (Hausverwaltung, Versicherung, Grundsteuer). "
               "Mein Anwalt hat mir heute Morgen bestätigt, dass ich kündigen kann.", "12:03", "✓✓"),
        (False, "10.02.2022", "Ich zahle heute Nachmittag, versprochen!", "12:11", "✓✓"),
        (True, "10.02.2022", "Das reicht mir nicht mehr. Ich kündige hiermit das Mietverhältnis "
               "außerordentlich und fristlos wegen Zahlungsverzugs gemäß § 543 Abs. 2 Nr. 3 BGB. "
               "[Sprachnachricht: 00:47] 🎤", "14:17", "✓✓"),
        (True, "10.02.2022", "Anbei die Kündigung auch noch mal als PDF! "
               "Bitte lesen Sie! Das ist ERNST!", "14:18", "✓✓"),
        (True, "10.02.2022", "📎 Kuendigung_10022022.pdf (183 KB)", "14:18", "✓✓"),
        (False, "10.02.2022", "Das ist nicht zulässig. Eine Kündigung per WhatsApp? Das ist nicht "
                "schriftlich. Ich bin IT-Admin, ich kenne mich aus. Googeln Sie mal § 568 BGB.",
                "14:55", "✓✓"),
        (True, "10.02.2022", "Ich habe einen Anwalt. Der kümmert sich darum.", "15:01", "✓✓"),
        (False, "10.02.2022", "Machen Sie das. Ich höre von dem.", "15:12", "✓"),
    ]

    for sender, date, text, time_str, status in messages:
        date_label = Table(
            [[Paragraph(f"— {date} —", make_style(f"datelbl{date}", fontName="Helvetica", fontSize=7,
                                                    alignment=TA_CENTER, textColor=C_MUTED))]],
            colWidths=[16*cm])
        elems.append(date_label)
        elems.append(sp(0.05))
        elems.append(wa_bubble(text, sender, time_str, status))
        elems.append(sp(0.05))

    elems.append(sp(0.3))
    # Transkript Sprachnachricht
    elems.append(heading("TRANSKRIPT SPRACHNACHRICHT (10.02.2022, 14:17 Uhr, Dauer 0:47)", 2))
    elems.append(Paragraph(
        "<i>[Maschinelle Transkription, im Wesentlichen korrekt]</i>", sSmall))
    elems.append(sp(0.1))
    transkript = Table(
        [[Paragraph(
            "Herr Eberhart-Wolframshausen, ich, Hildegunde Pferdedrescher-Riesenstein, "
            "Eigentümerin des Hauses Eckendorfer Straße 188 in Bielefeld, erkläre hiermit "
            "gegenüber Ihnen, Götz-Sieghart Eberhart-Wolframshausen, als Mieter der Wohnung "
            "Appartement 4 Obergeschoss, die außerordentliche fristlose Kündigung des "
            "Mietverhältnisses wegen Zahlungsverzugs nach § 543 Abs. 2 Nr. 3 BGB. "
            "Der Rückstand beträgt über EUR 2.200,–, das sind mehr als zwei Monatsmieten. "
            "Bitte räumen Sie die Wohnung bis zum 28. Februar 2022. [Pause] Äh, ich meine... "
            "ich wünsche Ihnen trotzdem einen guten Tag. Auf Wiederhören.", sNormal)]],
        colWidths=[16*cm])
    transkript.setStyle(TableStyle([
        ("BOX",        (0,0),(-1,-1), 0.5, C_MUTED),
        ("BACKGROUND", (0,0),(-1,-1), colors.HexColor("#FFFAF0")),
        ("TOPPADDING",    (0,0),(-1,-1), 6),
        ("BOTTOMPADDING", (0,0),(-1,-1), 6),
        ("LEFTPADDING",   (0,0),(-1,-1), 8),
        ("RIGHTPADDING",  (0,0),(-1,-1), 8),
    ]))
    elems.append(transkript)
    elems.append(sp(0.3))
    elems.append(Paragraph(
        "<b>Rechtliche Einschätzung zu Bl. 10-15:</b> Die Kündigung per WhatsApp-Sprachnachricht "
        "wahrt weder die Schriftform des § 568 Abs. 1 BGB noch die elektronische Form des § 126a BGB. "
        "Eine Sprachnachricht über einen Messenger ist keine qualifiziert elektronisch signierte "
        "Willenserklärung. Die beigefügte PDF-Datei (s. Bl. 16-17) ist ebenfalls ohne qES versandt worden. "
        "Beide Formate sind formunwirksam i.S.v. § 125 Satz 1 BGB.",
        sRed))
    elems.append(page_break())
    return elems


def b06_email_kuendigung():
    """6. Original-E-Mail vom 10. Februar 2022 + PDF-Anhang"""
    elems = []
    elems.append(heading("E-MAIL PFERDEDRESCHER-RIESENSTEIN VOM 10.02.2022", 1))
    elems.append(Paragraph("Original-E-Mail mit Kündigungs-PDF-Anhang (OHNE qES) — Bl. 16-17 der Akte", sSmall))
    elems.append(sp(0.2))
    body_lines = [
        "Sehr geehrter Herr Eberhart-Wolframshausen,",
        "",
        "wie soeben per WhatsApp angekündigt, übersende ich Ihnen die",
        "formelle Kündigung Ihres Mietverhältnisses als PDF-Anhang.",
        "",
        "Ich kündige hiermit das Mietverhältnis über die Wohnung",
        "Eckendorfer Straße 188, Appartement 4 OG, 33609 Bielefeld",
        "mit Ihnen, Herrn Götz-Sieghart Eberhart-Wolframshausen,",
        "außerordentlich und fristlos, hilfsweise ordentlich zum",
        "nächstmöglichen Termin, wegen Zahlungsverzugs gemäß",
        "§ 543 Abs. 2 Nr. 3, § 569 Abs. 3 BGB.",
        "",
        "Der Mietrückstand beläuft sich auf EUR 2.229,40.",
        "",
        "Bitte räumen Sie die Wohnung bis spätestens 28. Februar 2022.",
        "",
        "Mit freundlichen Grüßen",
        "Hildegunde Pferdedrescher-Riesenstein",
        "Ottilienweg 23, 33647 Bielefeld-Brackwede",
        "hildegunde@pferdedrescher-online-marketing.de",
        "Mobil: 0172 / 4 88 22 33",
    ]
    elems += email_block(
        "10. Februar 2022, 14:18 Uhr",
        "Hildegunde Pferdedrescher-Riesenstein <hildegunde@pferdedrescher-online-marketing.de>",
        "goetz.eberhart@wolframshausen-it.de",
        "Kündigung Mietverhältnis Eckendorfer Str. 188 App. 4",
        body_lines, has_attachment=True, has_qes=False
    )
    elems.append(sp(0.3))
    # PDF-Anhang-Frame
    elems.append(heading("PDF-ANHANG: Kuendigung_10022022.pdf — Volltext", 2))
    elems.append(Paragraph("[SIMULATION PDF-ANHANG — kein tatsächlich signiertes Dokument]", sSmall))
    anhang_lines = [
        "KÜNDIGUNG DES MIETVERHÄLTNISSES",
        "═══════════════════════════════",
        "",
        "Hildegunde Pferdedrescher-Riesenstein",
        "Ottilienweg 23",
        "33647 Bielefeld-Brackwede",
        "",
        "An:",
        "Herrn Götz-Sieghart Eberhart-Wolframshausen",
        "Eckendorfer Straße 188, App. 4 OG",
        "33609 Bielefeld",
        "",
        "Bielefeld, den 10. Februar 2022",
        "",
        "Betr.: Kündigung Mietvertrag v. 03.04.2017, Eckendorfer Str. 188, App. 4",
        "",
        "Sehr geehrter Herr Eberhart-Wolframshausen,",
        "",
        "hiermit kündige ich das zwischen uns bestehende Mietverhältnis",
        "über die oben bezeichnete Wohnung außerordentlich und fristlos",
        "zum sofortigen Zeitpunkt, hilfsweise ordentlich zum nächstmöglichen",
        "gesetzlichen Termin.",
        "",
        "Kündigungsgrund: Zahlungsverzug nach § 543 Abs. 2 Nr. 3 BGB.",
        "Mietrückstand: EUR 2.229,40 (> 2 Monatsmieten gem. § 569 Abs. 3 BGB).",
        "",
        "Hildegunde Pferdedrescher-Riesenstein",
        "",
        "[Keine handschriftliche Unterschrift — kein qES-Siegel]",
        "",
        "⚠ HINWEIS: Diese PDF enthält KEINE qualifizierte elektronische Signatur",
        "   i.S.v. § 126a BGB. Formunwirksam für Kündigungen nach § 568 BGB!",
    ]
    anhang_frame = Table(
        [[Paragraph("<br/>".join(anhang_lines), sMono)]],
        colWidths=[16*cm])
    anhang_frame.setStyle(TableStyle([
        ("BOX",        (0,0),(-1,-1), 1.0, colors.HexColor("#CC0000")),
        ("BACKGROUND", (0,0),(-1,-1), colors.HexColor("#FFF8F8")),
        ("TOPPADDING",    (0,0),(-1,-1), 8),
        ("BOTTOMPADDING", (0,0),(-1,-1), 8),
        ("LEFTPADDING",   (0,0),(-1,-1), 10),
    ]))
    elems.append(anhang_frame)
    elems.append(sp(0.2))
    elems.append(Paragraph(
        "<b>Rechtliche Würdigung:</b> Das PDF ist ohne qualifizierte elektronische Signatur (qES) "
        "versandt worden. Eine qES i.S.v. § 126a Abs. 1 BGB setzt voraus, dass der Aussteller "
        "seinen Namen hinzufügt und das Dokument mit einer qES versieht. "
        "Ein unsigniertes PDF per E-Mail wahrt die Schriftform des § 568 Abs. 1 BGB nicht "
        "(§ 125 Satz 1 BGB: Nichtigkeit). Auch die handschriftliche Unterschrift fehlt. "
        "Der Mieter hat dies umgehend gerügt (vgl. Bl. 18).", sRed))
    elems.append(page_break())
    return elems


def b07_antwortmail():
    """7. Antwort-Mail Eberhart-Wolframshausen (sarkastisch)"""
    elems = []
    elems.append(heading("ANTWORT-MAIL EBERHART-WOLFRAMSHAUSEN VOM 11.02.2022", 1))
    elems.append(Paragraph("Bl. 18 der Akte", sSmall))
    elems.append(sp(0.2))
    body_lines = [
        "Sehr geehrte Frau Pferdedrescher-Riesenstein,",
        "",
        "vielen Dank für Ihre kreative Nutzung digitaler Kommunikationsmittel.",
        "Als IT-Administrator bin ich durchaus in der Lage, zwischen einer",
        "qualifizierten elektronischen Signatur (qES) nach § 126a BGB",
        "und einer schlichten PDF-Datei zu unterscheiden.",
        "",
        "Ihre gestrige Kündigung ist aus folgenden Gründen formunwirksam:",
        "",
        "1. Die WhatsApp-Sprachnachricht (14:17 Uhr): Messengernachrichten",
        "   wahren die Schriftform des § 568 Abs. 1 BGB nicht. Punkt.",
        "",
        "2. Die PDF-Datei (14:18 Uhr): Das Dokument enthält weder eine",
        "   handschriftliche Unterschrift (§ 126 BGB) noch eine qualifizierte",
        "   elektronische Signatur (§ 126a BGB). Ein unsigniertes PDF ist",
        "   nichts weiter als eine Textdatei mit Formatierung.",
        "",
        "Ich empfehle Ihnen, § 568 BGB sowie § 125 BGB zu lesen.",
        "Gerne sende ich Ihnen die entsprechenden Gesetzestexte als",
        "korrekt signierte PDF-Datei — ich weiß nämlich, wie das geht.",
        "",
        "Sollten Sie eine wirksame Kündigung erklären wollen, rate ich",
        "zu einem Brief per Einschreiben oder einer qES-signierten E-Mail.",
        "Bis dahin verbleibe ich in der Wohnung.",
        "",
        "Mit freundlichem Gruß,",
        "Götz-Sieghart Eberhart-Wolframshausen",
        "IT-Administrator | CCNA, LPIC-2",
        "goetz.eberhart@wolframshausen-it.de",
    ]
    elems += email_block(
        "11. Februar 2022, 09:44 Uhr",
        "Götz-Sieghart Eberhart-Wolframshausen <goetz.eberhart@wolframshausen-it.de>",
        "hildegunde@pferdedrescher-online-marketing.de",
        "AW: Kündigung Mietverhältnis Eckendorfer Str. 188 App. 4",
        body_lines, has_attachment=False, has_qes=False
    )
    elems.append(sp(0.3))
    elems.append(italic("[Handschriftliche Randbemerkung Eberhart-Wolframshausen:] "
                        "\"Sie hat mir das per WhatsApp geschickt!!! Ich fasse es nicht.\""))
    elems.append(sp(0.2))
    elems.append(italic("[Weitere Randbemerkung:] \"Echte Frechheit, als IT-Admin so behandelt zu werden, "
                        "als ob ich keine qES erkennen würde. § 126a BGB steht seit 2001 im Gesetz.\""))
    elems.append(page_break())
    return elems


def b08_anwaltsschreiben_feb2022():
    """8. Anwaltsschreiben RA Ranftenschwedler-Bielenfels 15.02.2022 (3 Seiten)"""
    elems = []
    elems.append(heading("ANWALTSSCHREIBEN VOM 15. FEBRUAR 2022", 1))
    elems.append(Paragraph("RA Dr. Engelbert Ranftenschwedler-Bielenfels an Mandantin "
                           "Pferdedrescher-Riesenstein — Bl. 19-21", sSmall))
    elems.append(sp(0.2))
    # Briefkopf
    bk = Table([
        [Paragraph("Ranftenschwedler Ostkamp Rechtsanwälte mbB", make_style("bk1", fontName="Helvetica-Bold",
                   fontSize=11, textColor=C_ACCENT)),
         Paragraph("Niederwall 12 · 33602 Bielefeld\nTel: 0521/88 44 22-0 · Fax: 0521/88 44 22-99\n"
                   "dr.ranftenschwedler@ra-niederwall.de", make_style("bk2", fontName="Helvetica", fontSize=8,
                                                                       alignment=TA_RIGHT, textColor=C_MUTED))]
    ], colWidths=[9*cm, 7*cm])
    elems.append(bk)
    elems.append(hr(1, C_ACCENT))
    elems.append(sp(0.2))
    elems += [
        para("Bielefeld, 15. Februar 2022"),
        sp(0.1),
        bold_para("MANDANTENPOST — PERSÖNLICH/VERTRAULICH"),
        sp(0.1),
        bold_para("Frau Hildegunde Pferdedrescher-Riesenstein"),
        para("Ottilienweg 23 · 33647 Bielefeld-Brackwede"),
        sp(0.2),
        bold_para("Ihr Mietverhältnis mit Herrn Götz-Sieghart Eberhart-Wolframshausen, "
                  "Eckendorfer Straße 188, App. 4, 33609 Bielefeld"),
        sp(0.1),
        bold_para("Ihr Az.: 22/0215-PRE | Unser Az.: ROR-2022-0055"),
        sp(0.2),
        bold_para("Sehr geehrte Frau Pferdedrescher-Riesenstein,"),
        sp(0.1),
        para("ich nehme Bezug auf unser heutiges Telefonat und fasse die wesentlichen "
             "Erkenntnisse zusammen. Ich muss Sie leider über einen gravierenden Formfehler "
             "in Verbindung mit Ihrer Kündigungserklärung vom 10. Februar 2022 informieren."),
        sp(0.2),
        heading("I. Formunwirksamkeit der Kündigung vom 10. Februar 2022", 2),
        para("(1) <b>WhatsApp-Sprachnachricht:</b> Die mündliche Kündigungserklärung per "
             "WhatsApp-Sprachnachricht wahrt die Schriftform des § 568 Abs. 1 BGB nicht. "
             "§ 568 Abs. 1 BGB schreibt für die Kündigung eines Wohnraummietverhältnisses "
             "zwingend die Schriftform vor. Diese erfordert gemäß § 126 Abs. 1 BGB eine "
             "Urkunde mit eigenhändiger Unterschrift des Ausstellers. Eine Sprachnachricht "
             "ist keine Urkunde. Ergebnis: <b>Formunwirksam, § 125 Satz 1 BGB.</b>"),
        para("(2) <b>PDF-Datei ohne qualifizierte elektronische Signatur:</b> Nach § 126 Abs. 3 BGB "
             "kann zwar die Schriftform durch die elektronische Form nach § 126a BGB ersetzt werden. "
             "Dies setzt aber voraus, dass (a) der Aussteller seinen Namen dem elektronischen Dokument "
             "hinzufügt und (b) das Dokument mit einer qualifizierten elektronischen Signatur (qES) "
             "gemäß Art. 3 Nr. 12 eIDAS-VO versieht. Ein schlichtes, unsigniertes PDF — so sorgfältig "
             "es auch inhaltlich formuliert sein mag — erfüllt diese Anforderungen nicht. "
             "Ergebnis: <b>Ebenfalls formunwirksam, § 125 Satz 1 BGB.</b>"),
        sp(0.2),
        page_break(),
    ]
    elems += [
        heading("Anwaltsschreiben 15.02.2022 — Seite 2 von 3", 1),
        heading("II. Bedeutung für Ihre Situation", 2),
        para("Die Formunwirksamkeit hat zur Folge, dass das Mietverhältnis durch die "
             "Erklärungen vom 10. Februar 2022 nicht beendet worden ist. "
             "Herr Eberhart-Wolframshausen ist daher berechtigt, die Wohnung weiter zu bewohnen. "
             "Er hat dies in seiner Antwort-E-Mail vom 11. Februar 2022 korrekt erkannt und "
             "angekündigt, in der Wohnung zu verbleiben."),
        para("Es ist positiv zu vermerken, dass Herr Eberhart-Wolframshausen, obwohl er "
             "die Formunwirksamkeit erkannt hat, noch keine eigenen Ansprüche geltend macht "
             "(z.B. Schadenersatz wegen des Versuchs einer unberechtigten Kündigung). "
             "Dies kann sich aber ändern, wenn Sie die Sache eskalieren."),
        sp(0.2),
        heading("III. Handlungsoptionen", 2),
        bold_para("Option A: Schriftliche Kündigung per Einschreiben mit Rückschein"),
        para("Die sicherste Variante ist nach wie vor die <b>handschriftlich unterzeichnete "
             "Papierkündigung</b>, die Sie Herrn Eberhart-Wolframshausen persönlich übergeben "
             "(Quittung!) oder per Einschreiben mit Rückschein zustellen lassen. "
             "Dies ist die klassische Lösung, die keinerlei technische Fragen aufwirft. "
             "Ich empfehle dringend, die Kündigung von uns aufsetzen zu lassen."),
        sp(0.1),
        bold_para("Option B: Qualifiziert elektronisch signierte E-Mail direkt an den Mieter"),
        para("Nach § 126 Abs. 3 BGB i.V.m. § 126a BGB kann die Schriftform durch die "
             "elektronische Form ersetzt werden. Ich halte es für grundsätzlich möglich, "
             "eine mit einer qES signierte PDF-Kündigung per E-Mail direkt an Herrn "
             "Eberhart-Wolframshausen zu senden — vorausgesetzt, er empfängt sie und "
             "kann die Signatur prüfen. Dies ist eine rechtlich noch nicht vollständig "
             "geklärte Frage. Ich rate gleichwohl zur Vorsicht."),
        para("<b>WICHTIG:</b> Wenn wir die Kündigung in einen Klageschriftsatz aufnehmen, "
             "genügt es nicht, dass der Schriftsatz qES-signiert bei Gericht eingeht. "
             "Das Gericht druckt den Schriftsatz aus und stellt ihn Herrn Eberhart-Wolframshausen "
             "postalisch zu. Mit dem Ausdruck und dem sogenannten Transfervermerk gemäß "
             "§ 298 Abs. 3 ZPO geht die Signaturqualität verloren. Herr Eberhart-Wolframshausen "
             "kann die qES des Originals am Papierausdruck nicht überprüfen. "
             "Die Frage, ob dies für einen formgerechten Zugang ausreicht, ist offen "
             "(s. dazu unter IV.)."),
        sp(0.2),
        page_break(),
    ]
    elems += [
        heading("Anwaltsschreiben 15.02.2022 — Seite 3 von 3", 1),
        heading("IV. Rechtliche Einschätzung: Kündigung im Schriftsatz + Zustellung per Ausdruck", 2),
        para("Ich sehe hier ein erhebliches Risiko. Die Funktionen der Schriftform — "
             "Identitätsfunktion, Echtheitsfunktion, Verifikationsfunktion — werden durch "
             "einen bloßen Ausdruck mit Transfervermerk nicht vollständig gewahrt. "
             "Der Empfänger (hier: Herr Eberhart-Wolframshausen) kann am Papierausdruck "
             "die Echtheit der Signatur nicht selbst überprüfen. Der Transfervermerk des "
             "Gerichts belegt nur, dass das Gericht die Prüfung vorgenommen hat — er "
             "ermöglicht keine eigene Verifikation durch den Erklärungsgegner."),
        para("Ich empfehle daher, <b>parallel</b> zur Klage die Kündigung auch "
             "außergerichtlich formgerecht zu erklären (handschriftlicher Brief per "
             "Einschreiben mit Rückschein oder qES-signierte E-Mail direkt an den Mieter)."),
        sp(0.2),
        heading("V. Nächste Schritte", 2),
        para("(1) Wir erstellen umgehend eine handschriftlich unterzeichnete Kündigung "
             "und senden Sie per Einschreiben mit Rückschein."),
        para("(2) Parallel bereiten wir die Klageschrift vor (Räumungs- und "
             "Zahlungsklage). Die Klageschrift wird eine weitere Kündigung enthalten "
             "und mit meiner qES versehen bei Gericht eingereicht."),
        para("(3) Ich bitte Sie, mir unverzüglich alle Zahlungsbelege der letzten "
             "drei Jahre zu übermitteln. Am besten per E-Mail mit Kontoauszügen."),
        sp(0.2),
        bold_para("Mit freundlichen kollegialen Grüßen"),
        sp(0.1),
        para("Dr. Engelbert Ranftenschwedler-Bielenfels"),
        para("Rechtsanwalt | Fachanwalt für Miet- und WEG-Recht"),
        para("Ranftenschwedler Ostkamp Rechtsanwälte mbB"),
        sp(0.3),
        Paragraph("<i>Dieses Schreiben ist maschinell erstellt und ohne Unterschrift gültig. "
                  "Anwaltliches Schreiben an Mandantin — kein Zugang an Dritten.</i>", sSmall),
        page_break(),
    ]
    return elems


def b09_klageschrift():
    """9. Klageschrift vom 09. März 2022 (8 Seiten, qES)"""
    elems = []
    elems.append(heading("KLAGESCHRIFT VOM 09. MÄRZ 2022", 1))
    elems.append(Paragraph("Mit qualifizierter elektronischer Signatur — Bl. 22-29 der Akte", sSmall))
    elems.append(sp(0.2))
    elems.append(qes_block("Dr. Engelbert Ranftenschwedler-Bielenfels", "D-Trust Public-CA 2-3 2022",
                            "12.07.2026", "09.03.2022 09:47:33"))
    elems.append(sp(0.2))
    elems += [
        bold_para("AN DAS AMTSGERICHT BIELEFELD"),
        sp(0.2),
        para("In der Sache"),
        bold_para("Hildegunde Pferdedrescher-Riesenstein, Ottilienweg 23, 33647 Bielefeld-Brackwede"),
        para("— Klägerin —"),
        bold_para("Prozessbevollmächtigter: RA Dr. Engelbert Ranftenschwedler-Bielenfels, "
                  "Niederwall 12, 33602 Bielefeld"),
        sp(0.1),
        para("gegen"),
        sp(0.1),
        bold_para("Götz-Sieghart Eberhart-Wolframshausen, Eckendorfer Straße 188, App. 4 OG, 33609 Bielefeld"),
        para("— Beklagter —"),
        sp(0.2),
        bold_para("erheben wir im Namen und mit Vollmacht der Klägerin"),
        sp(0.1),
        heading("KLAGE", 1),
        sp(0.1),
        bold_para("und beantragen,"),
        sp(0.1),
        para("1. den Beklagten zu verurteilen, die Wohnung im Obergeschoss, Appartement Nr. 4, "
             "des Hauses Eckendorfer Straße 188, 33609 Bielefeld (3 Zimmer, Küche, Bad, "
             "Abstellraum, ca. 74,5 m²) zu räumen und an die Klägerin herauszugeben;"),
        para("2. den Beklagten zu verurteilen, an die Klägerin rückständige Miete und "
             "Nebenkosten in Höhe von EUR 2.229,40 zuzüglich Zinsen in Höhe von 5 Prozentpunkten "
             "über dem jeweiligen Basiszinssatz seit Rechtshängigkeit zu zahlen;"),
        para("3. die Kosten des Rechtsstreits dem Beklagten aufzuerlegen."),
        sp(0.3),
        heading("STREITWERT:", 2),
        para("Räumungsantrag: EUR 7.787,64 (12 × EUR 648,97 = Jahresmiete)"),
        para("Zahlungsantrag: EUR 2.229,40"),
        para("Gesamt: EUR 10.017,04"),
        sp(0.3),
        heading("BEGRÜNDUNG", 2),
        heading("I. Mietverhältnis", 3),
        para("Die Klägerin ist Eigentümerin und Vermieterin des Hauses Eckendorfer Straße 188, "
             "33609 Bielefeld. Durch Mietvertrag vom 03. April 2017 (Anlage K-MIET-1) hat sie "
             "dem Beklagten die Wohnung im Obergeschoss (App. Nr. 4) vermietet. "
             "Die monatliche Bruttomiete beträgt EUR 648,97."),
        sp(0.2),
        heading("II. Zahlungsverzug", 3),
        para("Der Beklagte ist seit Frühjahr 2019 in erheblichem Zahlungsverzug. "
             "Die Mahnungs-Historie (Anlage K-MIET-2, Bl. 8-9 der Akte) zeigt, dass der "
             "Rückstand bis Januar 2021 auf über EUR 3.000,– angewachsen war. "
             "Zwar hat der Beklagte in der Zeit von Februar 2021 bis Oktober 2021 monatlich "
             "EUR 900,– gezahlt, wodurch der Rückstand auf EUR 931,46 sank. "
             "Seit November 2021 zahlt der Beklagte wieder nur die laufende Miete, seit "
             "Januar 2022 gar keine Miete mehr. Per 10. Februar 2022 besteht ein "
             "Rückstand von EUR 2.229,40."),
        sp(0.2),
        page_break(),
    ]
    elems += [
        heading("Klageschrift 09.03.2022 — Seite 2 von 8", 1),
        heading("III. Kündigung", 3),
        para("(1) Am 10. Februar 2022 hat die Klägerin versucht, das Mietverhältnis "
             "außerordentlich fristlos zu kündigen. Angesichts der insoweit bestehenden "
             "Formzweifel erklärt die Klägerin die Kündigung vorsorglich erneut:"),
        sp(0.2),
        bold_para("KÜNDIGUNG"),
        sp(0.1),
        para("Die Klägerin, vertreten durch den unterzeichnenden Prozessbevollmächtigten, "
             "kündigt hiermit das Mietverhältnis mit dem Beklagten über die Wohnung "
             "Eckendorfer Straße 188, App. 4 OG, 33609 Bielefeld, Mietvertrag vom 03. April 2017,"),
        sp(0.1),
        bold_para("• außerordentlich fristlos gemäß § 543 Abs. 2 Nr. 3, § 569 Abs. 3 BGB,"),
        bold_para("• hilfsweise ordentlich gemäß § 573 Abs. 2 Nr. 1 BGB "
                  "zum nächstmöglichen Termin."),
        sp(0.1),
        para("<b>Kündigungsgrund:</b> Der Beklagte ist mit einem Betrag von EUR 2.229,40 "
             "im Rückstand, was mehr als zwei Monatsmieten (2 × EUR 648,97 = EUR 1.297,94) "
             "entspricht (§ 569 Abs. 3 Nr. 1 BGB)."),
        sp(0.2),
        para("<b>Hinweis zur Form:</b> Diese Kündigung ist in einem qualifiziert elektronisch "
             "signierten Schriftsatz enthalten, der gemäß § 130d ZPO über das beA eingereicht "
             "wird. Die Klägerin geht davon aus, dass die Kündigung dem Beklagten durch "
             "gerichtliche Zustellung zugehen wird."),
        sp(0.3),
        page_break(),
    ]
    # Weitere Seiten der Klageschrift
    for pg_num in range(3, 9):
        elems += [
            heading(f"Klageschrift 09.03.2022 — Seite {pg_num} von 8", 1),
            para(f"[Fortführung der Klagebegründung, Seite {pg_num}]"),
            sp(0.2),
        ]
        if pg_num == 3:
            elems += [
                heading("IV. Rechtliche Grundlagen", 3),
                para("Der Anspruch auf Räumung und Herausgabe ergibt sich aus § 546 Abs. 1 BGB. "
                     "Danach ist der Mieter nach Beendigung des Mietverhältnisses zur Rückgabe "
                     "der Mietsache verpflichtet. Das Mietverhältnis ist durch die in dieser "
                     "Klageschrift erklärte Kündigung beendet worden, jedenfalls aber durch "
                     "den weiteren Schriftsatz vom 13. Mai 2022 (Anlage K-MIET-7)."),
                para("§ 543 Abs. 2 Nr. 3 lit. b) BGB erlaubt die außerordentliche Kündigung, "
                     "wenn der Mieter in einem Zeitraum, der sich über mehr als zwei Termine "
                     "erstreckt, mit der Entrichtung der Miete in Höhe eines Betrages in Verzug "
                     "ist, der die Miete für zwei Monate erreicht. Diese Voraussetzung ist erfüllt."),
                para("§ 569 Abs. 3 Nr. 3 BGB: Wird die Kündigung auf § 543 Abs. 2 Nr. 3 BGB "
                     "gestützt, so ist sie ausgeschlossen, wenn der Vermieter vorher befriedigt "
                     "wird. Eine solche Befriedigung ist nicht erfolgt."),
            ]
        elif pg_num == 4:
            elems += [
                heading("V. Zur Online-Kommunikation im Vorfeld", 3),
                para("Die Klägerin betreibt als Online-Marketing-Beraterin einen Webshop und "
                     "kommuniziert regelmäßig digital. Sie hat den Beklagten über Monate per "
                     "E-Mail gemahnt. Die Mahnungen sind wirksam zugegangen — für Mahnungen "
                     "gilt keine Formvorschrift."),
                para("Die Klägerin räumt ein, dass die Kündigungsversuche vom 10. Februar 2022 "
                     "möglicherweise formunwirksam waren. Aus diesem Grund wird in der "
                     "vorliegenden Klageschrift erneut die Kündigung erklärt, diesmal mit "
                     "qualifizierter elektronischer Signatur."),
                para("Der Beklagte ist IT-Administrator und mit elektronischen Signaturen "
                     "vertraut. Er hat in seiner E-Mail vom 11. Februar 2022 selbst auf die "
                     "Möglichkeit einer qES-signierten Kündigung hingewiesen. "
                     "Die Klägerin bedient sich dieses Weges nunmehr."),
            ]
        elif pg_num in (5, 6, 7):
            elems += [
                heading(f"VI.{pg_num-4} Beweisangebote und Anlagen", 3),
                para("Beweis für die Höhe der Mietrückstände: Kontoauszüge der Sparkasse Bielefeld "
                     "IBAN DE12 4726 0121 0123 4567 89, Anlage K-MIET-3 (Sonderband II)."),
                para("Beweis für den Mietvertrag: Urkunde, Anlage K-MIET-1 (Bl. 4-7)."),
                para("Beweis für die Mahnung: E-Mail-Ausdrucke, Anlage K-MIET-4 bis K-MIET-8."),
                para("Beweis für WhatsApp-Korrespondenz: Screenshot-Druck, Anlage K-MIET-9 (Bl. 10-15)."),
            ]
        elif pg_num == 8:
            elems += [
                heading("VII. Kostenantrag", 3),
                para("Die Klägerin beantragt, dem Beklagten die Kosten des Rechtsstreits "
                     "aufzuerlegen. Der Streitwert berechnet sich wie folgt:"),
                para("Räumungsantrag: 12 × EUR 648,97 = EUR 7.787,64"),
                para("Zahlungsantrag: EUR 2.229,40"),
                para("Gesamtstreitwert: EUR 10.017,04"),
                sp(0.3),
                bold_para("Ranftenschwedler Ostkamp Rechtsanwälte mbB"),
                para("Dr. Engelbert Ranftenschwedler-Bielenfels, Rechtsanwalt"),
                sp(0.2),
                qes_block(),
            ]
        elems.append(page_break())
    return elems


def b10_hinweisbeschluss():
    """10. Hinweisbeschluss AG Bielefeld 11.04.2022"""
    elems = []
    elems.append(heading("HINWEISBESCHLUSS DES AMTSGERICHTS BIELEFELD", 1))
    elems.append(Paragraph("Az.: 34 C 421/22 | 11. April 2022 | Bl. 30-31 der Akte", sSmall))
    elems.append(sp(0.3))
    elems += [
        bold_para("AMTSGERICHT BIELEFELD"),
        bold_para("Abteilung: 34. Zivilabteilung"),
        sp(0.1),
        bold_para("BESCHLUSS"),
        sp(0.1),
        para("In dem Rechtsstreit"),
        para("Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen"),
        para("Az.: 34 C 421/22"),
        sp(0.2),
        bold_para("erteilt das Gericht folgenden Hinweis:"),
        sp(0.2),
        heading("I. Zustellungsform der Klageschrift", 2),
        para("Die Klageschrift vom 09. März 2022 wurde vom Klägervertreter gemäß § 130d ZPO "
             "als elektronisches Dokument mit qualifizierter elektronischer Signatur über das "
             "beA eingereicht. Der Beklagte ist anwaltlich nicht vertreten."),
        para("Das Gericht hat die Klageschrift ausgedruckt (§ 298 Abs. 1 Satz 1 ZPO) und dem "
             "Beklagten mit Transfervermerk gemäß <b>§ 298 Abs. 3 ZPO</b> postalisch zugestellt."),
        sp(0.2),
        transfervermerk_block("09.03.2022 09:47:33", "Dr. E. Ranftenschwedler-Bielenfels"),
        sp(0.2),
        para("Das Gericht weist darauf hin, dass <b>Zweifel bestehen</b>, ob die in der "
             "Klageschrift enthaltene Kündigungserklärung dem Beklagten durch die "
             "Postzustellung des Ausdrucks mit Transfervermerk <b>formgerecht zugegangen</b> ist."),
        para("Insbesondere stellt sich die Frage, ob der Ausdruck mit Transfervermerk "
             "gemäß § 298 Abs. 3 ZPO die Verifikationsfunktion der qES wahrt, d.h. ob der "
             "Beklagte am Papierausdruck die Echtheit der Signatur prüfen kann "
             "(vgl. § 126a Abs. 1 BGB, Funktionsäquivalenz mit § 126 BGB)."),
        sp(0.2),
        heading("II. Bitte um Stellungnahme", 2),
        para("Der Klägervertreter wird gebeten, bis zum 09. Mai 2022 zu folgenden "
             "Punkten Stellung zu nehmen:"),
        para("1. Liegt ein formgerechter Zugang der Kündigung vom 09. März 2022 beim "
             "Beklagten vor (§ 130 BGB, § 126a BGB)?"),
        para("2. Falls nein: Wird eine weitere Kündigung erklärt, und in welcher Form?"),
        para("3. Zur Höhe des Mietrückstands: Aufstellung der einzelnen Forderungen "
             "mit Zahlungsdaten und -beträgen."),
        sp(0.3),
        para("Bielefeld, 11. April 2022"),
        sp(0.1),
        para("Amtsgericht Bielefeld — 34. Zivilabteilung"),
        para("Richter am Amtsgericht Blumenkemper"),
        page_break(),
    ]
    return elems


def b11_klageerwiderung():
    """11. Klageerwiderung Mieter (eigenhändig, fragmentarisch, 4 Seiten)"""
    elems = []
    elems.append(heading("KLAGEERWIDERUNG DES BEKLAGTEN VOM 02. MAI 2022", 1))
    elems.append(Paragraph("Eigenhändig, ohne Anwalt (Naturalpartei) — Bl. 32-35 | Fragment", sSmall))
    elems.append(sp(0.2))
    elems.append(italic("[Handschriftlich / maschinengeschrieben, teilweise unleserlich — "
                         "originale Schreibfehler und Tippfehler beibehalten]"))
    elems.append(sp(0.2))
    handschrift_style = make_style("hw", fontName="Helvetica-Oblique", fontSize=9, leading=14,
                                    textColor=colors.HexColor("#222244"), alignment=TA_LEFT)
    elems += [
        Paragraph("An das Amtsgericht Bielefeld", handschrift_style),
        Paragraph("Gerichtstr. 6, 33602 Bielefeld", handschrift_style),
        sp(0.2),
        Paragraph("Betrifft: Sache Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen, Az. 34 C 421/22", handschrift_style),
        sp(0.1),
        Paragraph("Bielefeld, 2. Mai 2022", handschrift_style),
        sp(0.2),
        Paragraph("Sehr gehertes Amtsgericht,", handschrift_style),
        sp(0.1),
        Paragraph("ich widerspreche der Klage. Die Kündigung ist nicht wirksam. "
                  "Ich bin IT-Adminitrator und kenne mich mit elektronischen Dokumenten "
                  "sehr gut aus. Die Klägerin hat mir eine Künidgung per Whatsapp "
                  "und als unsignierter PDF geschickt. Das ist kein § 568 BGB.", handschrift_style),
        sp(0.1),
        Paragraph("Ausserdem hat sie dann in der Klageschrift eine neue Kündgung erklärt. "
                  "Aber das Amtsgericht hat mir nur einen ausgedrcukten Zettel zugeschickt, "
                  "keinen signierten Computer-Brief. Auf dem Zettel steht irgendwas über "
                  "\"Transfervermerk\" — das ist kein wirksamer Zugang einer qualifzierten "
                  "elektornischen Signatur! Ich kann die Unterschrift nicht prüfen!", handschrift_style),
        sp(0.1),
        Paragraph("[Randbemerkung, kursiv:] \"Sie hat mir das per WhatsApp geschickt!!! "
                  "Ich fasse es nicht.\"", sItalic),
        sp(0.2),
        Paragraph("Zu den Mietrückständen:", handschrift_style),
        Paragraph("Ich gebe zu, dass ich zeitweise zu wenig gezahlt habe. Ich hatte "
                  "finanzielle Schwierigkeiten wegen Corona und wegen meines Arbeitgebers "
                  "(Kurzarbeit 2020). Aber ich habe dann auch Überzahlungen gemacht, fast "
                  "EUR 250 im Monat extra von Feb. 2021 bis Okt. 2021. Das muss man berücksichtigen. "
                  "Jetzt stehe ich bei ca. EUR 1.580. Ich zahle das zurück, brauche aber Zeit.", handschrift_style),
        sp(0.2),
        page_break(),
    ]
    elems += [
        heading("Klageerwiderung — Seite 2 von 4", 1),
        italic("[Seite 2 — maschinengeschrieben]"),
        sp(0.2),
        Paragraph("Zur rechtlichen Frage der elektronischen Kündigung:", handschrift_style),
        Paragraph("Ich habe nachgeschaut: § 126a BGB sagt, dass für eine wirksame elektronische "
                  "Form das Dokument mit einer qualifizierten elektronischen Signatur versehen "
                  "sein muss. Das bedeutet, ich muss die Signatur auch prüfen können. "
                  "Ein Papierausdruck + Transfervermerk reicht nicht, weil ich am Ausdruck "
                  "die Signatur nicht prüfen kann. Das hat das Amtsgericht selbst in seinem "
                  "Hinweisbeschluss angedeutet!", handschrift_style),
        sp(0.1),
        Paragraph("[Randbemerkung:] \"Echte Frechheit als IT-Admin behandelt zu werden, "
                  "als ob ich keine qES erkennen würde.\"", sItalic),
        sp(0.2),
        Paragraph("Ich beantrage daher, die Klage abzuweisen.", handschrift_style),
        Paragraph("Die Kündigung war und ist formunwirksam gem. §§ 125, 568 BGB.", handschrift_style),
        sp(0.2),
        Paragraph("Götz-Sieghart Eberhart-Wolframshausen", handschrift_style),
        Paragraph("Eckendorfer Str. 188, App. 4 OG, 33609 Bielefeld", handschrift_style),
        sp(0.3),
        italic("[Seiten 3-4 der Klageerwiderung: handschriftliche Anlage mit "
               "Kontoumsatz-Ausdrücken, nicht leserlich reproduzierbar — vgl. Sonderband II]"),
        page_break(),
    ]
    return elems


def b12_replik():
    """12. Replik Klägerin mit erneuter Kündigung 13.05.2022 (qES)"""
    elems = []
    elems.append(heading("REPLIK KLÄGERIN / ERNEUTE KÜNDIGUNG VOM 13. MAI 2022", 1))
    elems.append(Paragraph("Mit qualifizierter elektronischer Signatur — Bl. 36-39 der Akte", sSmall))
    elems.append(sp(0.2))
    elems.append(qes_block("Dr. Engelbert Ranftenschwedler-Bielenfels", "D-Trust Public-CA 2-3 2022",
                            "12.07.2026", "13.05.2022 10:12:44"))
    elems.append(sp(0.2))
    elems += [
        bold_para("SCHRIFTSATZ KLÄGERIN"),
        para("Az.: AG Bielefeld 34 C 421/22 | 13. Mai 2022"),
        sp(0.2),
        heading("I. Erwiderung auf die Klageerwiderung", 2),
        para("Der Beklagte hat in seiner Klageerwiderung vom 02. Mai 2022 zu Recht "
             "auf die Formfrage hingewiesen. Ob der Zugang der Kündigungserklärung "
             "aus der Klageschrift vom 09. März 2022 durch Zustellung des Ausdrucks "
             "mit Transfervermerk formgerecht bewirkt wurde, ist eine offene "
             "Rechtsfrage."),
        para("Die Klägerin erklärt die Kündigung vorsorglich erneut in diesem Schriftsatz."),
        sp(0.2),
        heading("II. Erneute Kündigungserklärung", 2),
        bold_para("KÜNDIGUNG"),
        para("Die Klägerin kündigt hiermit erneut das Mietverhältnis mit dem Beklagten "
             "über die Wohnung Eckendorfer Straße 188, App. 4 OG, 33609 Bielefeld,"),
        bold_para("• außerordentlich fristlos gemäß § 543 Abs. 2 Nr. 3, § 569 Abs. 3 BGB,"),
        bold_para("• hilfsweise ordentlich gemäß § 573 Abs. 2 Nr. 1 BGB."),
        sp(0.1),
        para("Kündigungsgrund: Per 13. Mai 2022 besteht weiterhin ein erheblicher "
             "Mietrückstand. Der Beklagte hat seit Januar 2022 keine Miete gezahlt."),
        sp(0.2),
        transfervermerk_block("13.05.2022 10:12:44", "Dr. E. Ranftenschwedler-Bielenfels"),
        sp(0.2),
        para("<b>Hinweis der Klägerin:</b> Auch dieser Schriftsatz wird dem Beklagten "
             "durch Ausdruck mit Transfervermerk zugestellt werden, da er anwaltlich nicht "
             "vertreten ist. Die Formfrage bleibt damit offen. Die Klägerin hält an ihrer "
             "Rechtsauffassung fest, dass der Zugang formgerecht erfolgt ist."),
        sp(0.3),
        bold_para("Ranftenschwedler Ostkamp Rechtsanwälte mbB"),
        para("Dr. Engelbert Ranftenschwedler-Bielenfels, Rechtsanwalt"),
        sp(0.2),
        qes_block(),
        page_break(),
    ]
    return elems


def b13_verhandlungsprotokoll():
    """13. Protokoll Mündliche Verhandlung AG Bielefeld 14.09.2022"""
    elems = []
    elems.append(heading("PROTOKOLL — MÜNDLICHE VERHANDLUNG AG BIELEFELD", 1))
    elems.append(Paragraph("14. September 2022 | Az.: 34 C 421/22 | Bl. 40-41 der Akte", sSmall))
    elems.append(sp(0.2))
    data = [
        ["Gericht:", "Amtsgericht Bielefeld, 34. Zivilabteilung"],
        ["Aktenzeichen:", "34 C 421/22"],
        ["Verhandlungstag:", "14. September 2022, 10:00 Uhr"],
        ["Richter:", "Richter am Amtsgericht Blumenkemper (Vorsitz)"],
        ["Klägervertreter:", "RA Dr. Engelbert Ranftenschwedler-Bielenfels"],
        ["Beklagter:", "Götz-Sieghart Eberhart-Wolframshausen (persönlich erschienen, ohne Anwalt)"],
        ["Urkundsbeamtin:", "Justizangestellte Kemmner"],
    ]
    t = Table([[Paragraph(k, sBold), Paragraph(v, sNormalL)] for k, v in data],
               colWidths=[4*cm, 12*cm])
    t.setStyle(TableStyle([
        ("GRID", (0,0),(-1,-1), 0.3, colors.lightgrey),
        ("BACKGROUND", (0,0),(0,-1), colors.HexColor("#F0F4FF")),
        ("TOPPADDING",    (0,0),(-1,-1), 3),
        ("BOTTOMPADDING", (0,0),(-1,-1), 3),
        ("LEFTPADDING",   (0,0),(-1,-1), 5),
    ]))
    elems.append(t)
    elems.append(sp(0.2))
    elems += [
        heading("PROTOKOLL:", 2),
        para("Der Vorsitzende eröffnet die Verhandlung und ruft die Sache auf."),
        sp(0.1),
        para("<b>RA Ranftenschwedler-Bielenfels:</b> Wir beziehen uns auf unsere "
             "Klageschrift vom 09. März 2022 und den Schriftsatz vom 13. Mai 2022."),
        sp(0.1),
        para("<b>Beklagter Eberhart-Wolframshausen:</b> Herr Richter, ich möchte eines klarstellen: "
             "Ich bin IT-Administrator. Ich weiß genau, was eine qualifizierte elektronische Signatur "
             "ist. Ich habe keinen signierten Schriftsatz erhalten — nur Papierausdrucke mit einem "
             "Vermerk darauf. Das ist kein qES-Zugang. Das ist Papier."),
        sp(0.1),
        para("<b>Richter am AG Blumenkemper:</b> Herr Eberhart-Wolframshausen, ich verstehe Ihre "
             "Argumentation. Die Formfrage, ob der Ausdruck eines qES-signierten Schriftsatzes mit "
             "Transfervermerk den formgerechten Zugang einer Willenserklärung bewirkt, ist rechtlich "
             "ungeklärt. Das Gericht tendiert dazu, dass dies nicht ausreicht."),
        sp(0.1),
        para("<b>RA Ranftenschwedler-Bielenfels:</b> Das Gericht irrt. Der Transfervermerk "
             "gemäß § 298 Abs. 3 ZPO dokumentiert die gerichtliche Prüfung der Signatur. "
             "Das muss ausreichen."),
        sp(0.1),
        para("<b>Richter am AG Blumenkemper:</b> Das werden wir im Urteil klären. "
             "Gibt es Vergleichsmöglichkeiten?"),
        sp(0.1),
        para("<b>Beklagter Eberhart-Wolframshausen:</b> Ich bin bereit, den Rückstand zu zahlen, "
             "wenn ich entsprechend Zeit bekomme und wenn die Kündigung für unwirksam erklärt wird. "
             "Ich will in der Wohnung bleiben."),
        sp(0.1),
        para("<b>RA Ranftenschwedler-Bielenfels:</b> Eine Einigung kommt nur in Betracht, wenn der "
             "Beklagte den gesamten Rückstand zuzüglich Kosten sofort zahlt."),
        sp(0.1),
        para("<b>Richter am AG Blumenkemper:</b> Ein Vergleich kommt nicht zustande. "
             "Das Gericht verkündet das Urteil am 11. Oktober 2022. "
             "Schriftsatznachlass bis 28. September 2022."),
        sp(0.2),
        Paragraph("Bielefeld, 14. September 2022 — Urkundsbeamtin der Geschäftsstelle: Kemmner", sSmall),
        page_break(),
    ]
    return elems


def b14_urteil_ag():
    """14. Urteil AG Bielefeld 34 C 421/22 vom 11.10.2022"""
    elems = []
    elems.append(heading("URTEIL DES AMTSGERICHTS BIELEFELD", 1))
    elems.append(Paragraph("Az.: 34 C 421/22 | 11. Oktober 2022 | Bl. 42-48 der Akte", sSmall))
    elems.append(sp(0.2))
    elems += [
        bold_para("AMTSGERICHT BIELEFELD"),
        bold_para("Im Namen des Volkes"),
        bold_para("URTEIL"),
        sp(0.1),
        para("In dem Rechtsstreit"),
        bold_para("Hildegunde Pferdedrescher-Riesenstein ./. Götz-Sieghart Eberhart-Wolframshausen"),
        para("Az.: 34 C 421/22"),
        sp(0.2),
        bold_para("hat das Amtsgericht Bielefeld, 34. Zivilabteilung, auf die mündliche "
                  "Verhandlung vom 14. September 2022 durch Richter am Amtsgericht Blumenkemper "
                  "für Recht erkannt:"),
        sp(0.2),
        heading("TENOR:", 2),
        bold_para("1. Die Klage wird abgewiesen."),
        bold_para("2. Die Klägerin trägt die Kosten des Rechtsstreits."),
        bold_para("3. Das Urteil ist vorläufig vollstreckbar."),
        sp(0.3),
        heading("TATBESTAND:", 2),
        para("Die Klägerin ist Eigentümerin und Vermieterin des Hauses Eckendorfer Str. 188, "
             "33609 Bielefeld. Die Parteien verbindet ein Wohnraummietvertrag vom 03. April 2017 "
             "über die Wohnung Appartement Nr. 4, OG. Monatliche Bruttomiete: EUR 648,97."),
        para("Der Beklagte geriet seit Frühjahr 2019 in zunehmenden Zahlungsverzug. "
             "Per 10. Februar 2022 betrug der Rückstand EUR 2.229,40. "
             "Die Klägerin erklärte am 10. Februar 2022 die außerordentliche Kündigung "
             "per WhatsApp-Sprachnachricht und unsignierter PDF-E-Mail. "
             "In der Klageschrift vom 09. März 2022 (qES) sowie im Schriftsatz vom "
             "13. Mai 2022 (qES) erklärte die Klägerin jeweils erneut die Kündigung. "
             "Beide Schriftsätze wurden dem Beklagten als Papierausdruck mit Transfervermerk "
             "gemäß § 298 Abs. 3 ZPO zugestellt."),
        sp(0.2),
        heading("ENTSCHEIDUNGSGRÜNDE:", 2),
        heading("I. Formunwirksamkeit der Kündigung vom 10. Februar 2022", 3),
        para("Die Kündigung vom 10. Februar 2022 — sowohl als WhatsApp-Sprachnachricht als "
             "auch als unsigniertes PDF — wahrt die Schriftform des § 568 Abs. 1 BGB nicht "
             "(§ 125 Satz 1 BGB). Insoweit ist dies zwischen den Parteien nicht mehr streitig."),
        sp(0.2),
        page_break(),
    ]
    elems += [
        heading("Urteil AG Bielefeld — Seite 2 von 7", 1),
        heading("II. Formunwirksamkeit der Kündigungen in den qES-Schriftsätzen", 3),
        para("Die Kündigungserklärungen in der Klageschrift vom 09. März 2022 und dem "
             "Schriftsatz vom 13. Mai 2022 sind ebenfalls formunwirksam, weil sie dem "
             "Beklagten nicht formgerecht zugegangen sind."),
        para("Zwar ist die Schriftform nach § 568 Abs. 1 BGB gemäß § 126 Abs. 3 BGB "
             "durch die elektronische Form des § 126a BGB ersetzbar. "
             "Und die Schriftsätze waren mit einer qualifizierten elektronischen Signatur versehen. "
             "Jedoch wahrt dies die Form für eine empfangsbedürftige Willenserklärung nur dann, "
             "wenn die WE dem Erklärungsgegner auch in der vorgeschriebenen Form ZUGEHT "
             "(§ 130 Abs. 1 Satz 1 BGB)."),
        para("Zur Wahrung der elektronischen Form des § 126a BGB muss das Dokument so in den "
             "Machtbereich des Empfängers gelangen, dass dieser die qualifizierte elektronische "
             "Signatur des Erklärenden und damit die Echtheit des Dokuments prüfen kann. "
             "Dies ist die Verifikationsfunktion der qES."),
        para("Diese Voraussetzung ist hier nicht erfüllt. Der Beklagte hat die qES-Schriftsätze "
             "nicht als elektronische Dokumente erhalten, sondern als Papierausdrucke mit "
             "Transfervermerk gemäß § 298 Abs. 3 ZPO. "
             "Am Papierausdruck kann der Beklagte die Echtheit der Signatur nicht selbst prüfen. "
             "Der Transfervermerk dokumentiert nur das Ergebnis der Prüfung durch das Gericht, "
             "ermöglicht aber keine eigenständige Verifikation durch den Beklagten."),
        sp(0.2),
        heading("III. Keine Rückwirkung des § 130e ZPO", 3),
        para("§ 130e ZPO (in Kraft seit 17. Juli 2024) fingiert den formwirksamen Zugang "
             "für empfangsbedürftige Willenserklärungen in qES-signierten Schriftsätzen, "
             "die als elektronisches Dokument bei Gericht eingereicht und dem Empfänger "
             "zugestellt wurden. Diese Vorschrift findet auf die vorliegenden Sachverhalte "
             "aus dem Jahr 2022 keine Anwendung (Grundsätze des intertemporalen Rechts)."),
        sp(0.2),
        heading("IV. Ergebnis", 3),
        para("Da keine wirksame Kündigung vorliegt, ist das Mietverhältnis nicht beendet. "
             "Der Räumungsanspruch (§ 546 BGB) besteht nicht. "
             "Hinsichtlich des Zahlungsantrags: Auch wenn der Rückstand grundsätzlich "
             "bestünde, hat die Klägerin die Forderungshöhe nicht hinreichend substantiiert "
             "dargelegt. Die Klage ist abzuweisen."),
        sp(0.3),
        para("Bielefeld, 11. Oktober 2022"),
        sp(0.1),
        bold_para("Richter am Amtsgericht Blumenkemper"),
        sp(0.2),
        Paragraph("<i>Hinweis: Urteil ist nicht rechtskräftig — Berufung eingelegt, "
                  "vgl. Bl. 49 ff. der Akte.</i>", sSmall),
        page_break(),
    ]
    return elems


def b15_b16_berufung_mandat():
    """15. Berufungsschrift + 16. Mandatsannahme RA Hassenstein-Heepen"""
    elems = []
    elems.append(heading("BERUFUNGSSCHRIFT KLÄGERIN VOM 12. NOVEMBER 2022", 1))
    elems.append(Paragraph("An das Landgericht Bielefeld — Bl. 49-50 der Akte", sSmall))
    elems.append(sp(0.2))
    elems += [
        qes_block("Dr. Engelbert Ranftenschwedler-Bielenfels", "D-Trust Public-CA 2-3 2022",
                  "12.07.2026", "12.11.2022 15:33:00"),
        sp(0.2),
        bold_para("AN DAS LANDGERICHT BIELEFELD — 3. ZIVILKAMMER (BERUFUNGSKAMMER MIETE)"),
        sp(0.1),
        para("In der Sache Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen"),
        para("Vorinstanz: AG Bielefeld 34 C 421/22 — Urteil vom 11. Oktober 2022"),
        sp(0.2),
        bold_para("legen wir namens und in Vollmacht der Klägerin"),
        bold_para("BERUFUNG"),
        bold_para("ein."),
        sp(0.1),
        para("Die Klägerin wendet sich gegen das Urteil des AG Bielefeld vom 11. Oktober 2022. "
             "Das Urteil ist unzutreffend. Die Berufungsbegründung erfolgt gesondert."),
        sp(0.1),
        para("Az. Vorinstanz: AG Bielefeld 34 C 421/22"),
        para("Streitwert: EUR 10.017,04"),
        sp(0.2),
        bold_para("Ranftenschwedler Ostkamp Rechtsanwälte mbB"),
        sp(0.2),
        page_break(),
    ]
    # 16. Mandatsannahme RA Hassenstein-Heepen
    elems.append(heading("MANDATSANNAHME RA HASSENSTEIN-HEEPEN VOM 15. NOVEMBER 2022", 1))
    elems.append(Paragraph("Bl. 51 der Akte", sSmall))
    elems.append(sp(0.2))
    elems += [
        bold_para("Wolfdieter Hassenstein-Heepen, Rechtsanwalt"),
        bold_para("Werther Straße 89 · 33615 Bielefeld"),
        bold_para("Tel.: 0521 / 44 21 00 · hassenstein@ra-heepen.de"),
        sp(0.2),
        para("Bielefeld, 15. November 2022"),
        sp(0.1),
        bold_para("An das Landgericht Bielefeld"),
        para("3. Zivilkammer (Berufungskammer Miete)"),
        sp(0.2),
        bold_para("Mandatsanzeige und Vollmachtsnachweis"),
        sp(0.1),
        para("In der oben bezeichneten Sache zeige ich an, dass ich mit der "
             "Rechtsvertretung des Beklagten, Herrn Götz-Sieghart Eberhart-Wolframshausen, "
             "Eckendorfer Straße 188, App. 4 OG, 33609 Bielefeld, "
             "ab der Berufungsinstanz beauftragt worden bin."),
        sp(0.2),
        data_table("Vergütungsvereinbarung (§ 3a RVG):", [
            ["Stundensatz:", "EUR 280,00 zzgl. gesetzl. MwSt."],
            ["Abrechnung:", "monatlich, nach Zeitaufwand"],
            ["Vorschuss:", "EUR 1.500,00 (erhalten)"],
        ]),
        sp(0.2),
        para("Ich bitte um Übersendung aller Schriftsätze und gerichtlichen Verfügungen "
             "an meine Kanzleiadresse. Vollmachtsurkunde anbei (Anlage)."),
        sp(0.2),
        bold_para("Wolfdieter Hassenstein-Heepen, Rechtsanwalt"),
        page_break(),
    ]
    return elems


def data_table(title, rows):
    t = Table([[Paragraph(title, sBold)] + [""],
               *[[Paragraph(k, sSmall), Paragraph(v, sSmall)] for k, v in rows]],
               colWidths=[4*cm, 8*cm])
    t.setStyle(TableStyle([
        ("SPAN",       (0,0),(-1,0)),
        ("GRID",       (0,0),(-1,-1), 0.3, colors.lightgrey),
        ("BACKGROUND", (0,0),(-1,0), colors.HexColor("#F0F4FF")),
        ("TOPPADDING",    (0,0),(-1,-1), 2),
        ("BOTTOMPADDING", (0,0),(-1,-1), 2),
        ("LEFTPADDING",   (0,0),(-1,-1), 5),
    ]))
    return t


def b17_b18_berufungsbegruendung():
    """17. Berufungsbegründung (8 Seiten) + 18. Berufungserwiderung"""
    elems = []
    elems.append(heading("BERUFUNGSBEGRÜNDUNG KLÄGERIN VOM 15. JANUAR 2023", 1))
    elems.append(Paragraph("Az.: LG Bielefeld 14 S 88/23 | 8 Seiten | Bl. 52-59 der Akte", sSmall))
    elems.append(sp(0.2))
    elems.append(qes_block("Dr. Engelbert Ranftenschwedler-Bielenfels", "D-Trust Public-CA 2-3 2022",
                            "12.07.2026", "15.01.2023 11:05:00"))
    elems.append(sp(0.2))
    elems += [
        heading("I. Rechtliche Ausgangslage", 2),
        para("Das Amtsgericht hat zu Unrecht angenommen, dass die Kündigungserklärungen "
             "in den qES-signierten Schriftsätzen dem Beklagten nicht formgerecht zugegangen sind. "
             "Das Urteil verletzt § 126a BGB sowie § 130 BGB."),
        sp(0.2),
        heading("II. Zur qES-Signatur und ihrer Funktionsäquivalenz", 2),
        para("§ 126a Abs. 1 BGB bestimmt, dass die Schriftform durch die elektronische Form "
             "ersetzt werden kann, wenn der Aussteller seinen Namen hinzufügt und das "
             "elektronische Dokument mit einer qualifizierten elektronischen Signatur versieht. "
             "Diese Voraussetzungen sind hier erfüllt."),
        para("Die Klägerin meint, dass der Transfervermerk gemäß § 298 Abs. 3 ZPO die "
             "Verifikationsfunktion ausreichend wahrt. Der Transfervermerk belegt: "
             "(1) das Ergebnis der Integritätsprüfung, (2) den Inhaber der Signatur, "
             "(3) den Zeitpunkt der Signatur. Diese Informationen ermöglichen dem Beklagten "
             "die Verifikation des Signaturinhabers und des Inhalts."),
        heading("III. Hilfsargument: Einverständnis des Beklagten", 2),
        para("Jedenfalls hat der Beklagte, der als IT-Administrator mit qES vertraut ist, "
             "durch sein Verhalten (Bezugnahme auf § 126a BGB in seiner Klageerwiderung) "
             "konkludent sein Einverständnis mit der elektronischen Kommunikation erklärt "
             "(§ 173 Abs. 4 ZPO analog)."),
        sp(0.3),
        para("Weitere Ausführungen folgen in den nachfolgenden 6 Seiten der Begründung..."),
        page_break(),
    ]
    for extra_page in range(2, 9):
        elems += [
            heading(f"Berufungsbegründung — Seite {extra_page} von 8", 1),
            para(f"[Seite {extra_page} — Fortsetzung der Begründung]"),
            sp(0.2),
            para("Die Klägerin verweist auf die Gesetzesmaterialien zu § 126a BGB (BT-Drs. 14/4987), "
                 "wonach der Gesetzgeber die qES als funktionsäquivalent zur handschriftlichen "
                 "Unterschrift angesehen hat. Eine Einschränkung dahingehend, dass die Signatur "
                 "stets durch den Erklärungsgegner selbst geprüft werden müsse, lässt sich dem "
                 "Gesetz nicht entnehmen.") if extra_page == 2 else
            para(f"Die Klägerin verweist zudem auf die Reformüberlegungen des Gesetzgebers, "
                 f"die später zu § 130e ZPO geführt haben. Die Norm zeigt, dass der Gesetzgeber "
                 f"selbst das Problem erkannt hat — und hat es für die Zukunft gelöst. "
                 f"Hieraus folgt aber nicht, dass die alte Rechtslage gegen die Klägerin wirkt."),
            page_break(),
        ]

    # Berufungserwiderung
    elems.append(heading("BERUFUNGSERWIDERUNG MIETER VOM 01. MÄRZ 2023", 1))
    elems.append(Paragraph("RA Wolfdieter Hassenstein-Heepen | Az.: LG Bielefeld 14 S 88/23 | Bl. 60-64", sSmall))
    elems.append(sp(0.2))
    elems.append(qes_block("Wolfdieter Hassenstein-Heepen", "DATEV eG — Zertifizierungsdienste",
                            "30.06.2025", "01.03.2023 14:22:00"))
    elems.append(sp(0.2))
    elems += [
        heading("I. Verteidigung des erstinstanzlichen Urteils", 2),
        para("Das AG Bielefeld hat zutreffend erkannt, dass die Kündigungserklärungen "
             "dem Beklagten nicht formgerecht zugegangen sind."),
        sp(0.2),
        heading("II. Zur Verifikationsfunktion der qES", 2),
        para("Die Klägerin verkennt das Wesen der qualifizierten elektronischen Signatur. "
             "Die qES hat nach der Systematik des § 126a BGB eine Verifikationsfunktion: "
             "Der Empfänger einer Willenserklärung in elektronischer Form muss in der Lage sein, "
             "die Echtheit der Signatur selbst zu prüfen."),
        para("Ein Papierausdruck mit Transfervermerk ermöglicht keine eigene Verifikation. "
             "Der Beklagte — obwohl als IT-Administrator theoretisch in der Lage — "
             "hat am Papierausdruck keine Möglichkeit, die kryptographische Integrität "
             "der qES zu prüfen. Das Gericht kann nicht die eigene Verifikation durch "
             "den Erklärungsgegner ersetzen."),
        sp(0.2),
        heading("III. Kein konkludentes Einverständnis", 2),
        para("Der Beklagte hat kein Einverständnis im Sinne von § 173 Abs. 4 Satz 1 ZPO "
             "zur elektronischen Übermittlung erteilt. Sein Hinweis auf die Möglichkeit "
             "einer qES in der Klageerwiderung ist kein Einverständnis, sondern eine "
             "rechtliche Belehrung an die Klägerin."),
        sp(0.2),
        bold_para("Wolfdieter Hassenstein-Heepen, Rechtsanwalt"),
        page_break(),
    ]
    return elems


def b19_urteil_lg():
    """19. LG-Urteil Bielefeld 14 S 88/23 vom 20.06.2023"""
    elems = []
    elems.append(heading("URTEIL DES LANDGERICHTS BIELEFELD", 1))
    elems.append(Paragraph("Az.: 14 S 88/23 | 20. Juni 2023 | Bl. 65-74 der Akte", sSmall))
    elems.append(sp(0.2))
    elems += [
        bold_para("LANDGERICHT BIELEFELD"),
        bold_para("3. Zivilkammer"),
        bold_para("Im Namen des Volkes"),
        bold_para("URTEIL"),
        sp(0.2),
        para("In dem Rechtsstreit"),
        bold_para("Hildegunde Pferdedrescher-Riesenstein ./. Götz-Sieghart Eberhart-Wolframshausen"),
        para("Berufungs-Az.: LG Bielefeld 14 S 88/23 | Vorinstanz: AG Bielefeld 34 C 421/22"),
        sp(0.2),
        bold_para("hat die 3. Zivilkammer des Landgerichts Bielefeld, "
                  "vorsitzender Richter Dr. Augustin Bockenfelder-Senne, "
                  "auf die mündliche Verhandlung vom 12. Mai 2023 für Recht erkannt:"),
        sp(0.2),
        heading("TENOR:", 2),
        bold_para("1. Die Berufung der Klägerin wird zurückgewiesen."),
        bold_para("2. Die Klägerin trägt die Kosten des Berufungsverfahrens."),
        bold_para("3. Das Urteil ist vorläufig vollstreckbar."),
        bold_para("4. Die Revision wird zugelassen (§ 543 Abs. 2 ZPO)."),
        sp(0.2),
        heading("GRÜNDE:", 2),
        heading("I. Zulassung der Revision", 3),
        para("Die Revision war wegen grundsätzlicher Bedeutung der Rechtsfrage zuzulassen, "
             "ob die Übermittlung eines Ausdrucks eines qES-signierten Schriftsatzes mit "
             "Transfervermerk gemäß § 298 Abs. 3 ZPO einen formgerechten Zugang der in dem "
             "Schriftsatz enthaltenen empfangsbedürftigen Willenserklärung beim Erklärungsgegner "
             "bewirkt (§ 126a Abs. 1 BGB, § 130 Abs. 1 Satz 1 BGB)."),
        sp(0.2),
        heading("II. Zur Sache", 3),
        para("Das Amtsgericht hat zu Recht entschieden, dass die Kündigungserklärungen "
             "in den qES-Schriftsätzen vom 09. März 2022 und 13. Mai 2022 dem Beklagten "
             "nicht formgerecht zugegangen sind. Die Berufungsangriffe der Klägerin "
             "greifen nicht durch."),
        para("Die Verifikationsfunktion der qES nach § 126a BGB erfordert, dass das Dokument "
             "mit der qES in den Machtbereich des Empfängers gelangt und dieser die Signatur "
             "überprüfen kann. Ein Papierausdruck mit Transfervermerk genügt dieser "
             "Anforderung nicht. Der Transfervermerk ermöglicht keine eigene Verifikation "
             "durch den Beklagten, sondern dokumentiert lediglich das Prüfergebnis des Gerichts."),
        sp(0.2),
        para("Bielefeld, 20. Juni 2023"),
        sp(0.1),
        bold_para("Dr. Augustin Bockenfelder-Senne"),
        para("Vorsitzender Richter am Landgericht"),
        sp(0.2),
        Paragraph("<i>Revision eingelegt zum BGH unter Az. VIII ZR 159/23.</i>", sSmall),
        page_break(),
    ]
    return elems


def b20_b21_revision():
    """20. Revisionsbegründung (11 Seiten) + 21. Revisionserwiderung"""
    elems = []
    elems.append(heading("REVISIONSBEGRÜNDUNG ZUM BGH VOM 28. AUGUST 2023", 1))
    elems.append(Paragraph("Az.: BGH VIII ZR 159/23 | 11 Seiten | Bl. 75-85 der Akte", sSmall))
    elems.append(sp(0.2))
    elems.append(qes_block("Dr. Engelbert Ranftenschwedler-Bielenfels", "D-Trust Public-CA 2-3 2022",
                            "12.07.2026", "28.08.2023 16:44:00"))
    elems.append(sp(0.2))
    elems += [
        heading("I. Revisionszulassung", 2),
        para("Die Revision ist gemäß § 543 Abs. 2 Satz 1 Nr. 1 ZPO wegen grundsätzlicher "
             "Bedeutung zuzulassen, da die Frage, ob der Ausdruck eines qES-signierten "
             "Schriftsatzes mit Transfervermerk gemäß § 298 Abs. 3 ZPO den formgerechten "
             "Zugang einer empfangsbedürftigen Willenserklärung beim Erklärungsgegner bewirkt, "
             "höchstrichterlich noch nicht entschieden ist."),
        sp(0.2),
        heading("II. Verletzung von § 126a BGB, § 130 BGB", 2),
        para("Die Vorinstanzen haben § 126a BGB verletzt, indem sie den formgerechten "
             "Zugang der Kündigungserklärungen verneint haben. Nach der Gesetzessystematik "
             "des § 126a BGB ersetzt die qES die handschriftliche Unterschrift. "
             "Die Identitätsfunktion, die Echtheitsfunktion und die Verifikationsfunktion "
             "sind durch den Transfervermerk gewahrt."),
        sp(0.2),
        heading("III. Systematische Folgen der Gegenmeinung", 2),
        para("Wenn der Zugang einer qES-signierten Kündigung im Schriftsatz durch "
             "Postzustellung des Ausdrucks nicht bewirkt werden kann, entsteht eine "
             "Regelungslücke: Anwälte, die nach § 130d ZPO zwingend elektronisch einreichen "
             "müssen, können gegenüber anwaltlich nicht vertretenen Parteien keine "
             "rechtsgestaltenden Willenserklärungen in Schriftsätzen wirksam erklären. "
             "Das ist mit dem Grundsatz effektiven Rechtsschutzes (Art. 19 Abs. 4 GG) "
             "nicht vereinbar."),
        sp(0.2),
        para("[Weitere Revisionsgründe auf den Seiten 4-11...]"),
        page_break(),
    ]
    for rp in range(2, 12):
        elems += [
            heading(f"Revisionsbegründung — Seite {rp} von 11", 1),
            para(f"[Seite {rp} der Revisionsbegründung]"),
            sp(0.2),
            para("Die Revision stützt sich auf BGH XII ZB 573/18 (BGHZ 222, 105), "
                 "in dem der BGH die Verkehrsfähigkeit der qES bejaht hat. "
                 "Ferner wird auf die Kommentarliteratur zu § 126a BGB verwiesen "
                 "(BeckOK BGB/Wendtland, § 126a Rn. 15 ff.).") if rp == 2 else
            para(f"[Weitere Ausführungen zu Seite {rp} — vgl. vollständiger Schriftsatz in Sonderband II]"),
            page_break(),
        ]

    # Revisionserwiderung
    elems.append(heading("REVISIONSERWIDERUNG MIETER VOM 15. OKTOBER 2023", 1))
    elems.append(Paragraph("RA Wolfdieter Hassenstein-Heepen | Az.: BGH VIII ZR 159/23 | Bl. 86-91", sSmall))
    elems.append(sp(0.2))
    elems.append(qes_block("Wolfdieter Hassenstein-Heepen", "DATEV eG — Zertifizierungsdienste",
                            "30.06.2025", "15.10.2023 10:00:00"))
    elems.append(sp(0.2))
    elems += [
        heading("Zur Revisionsbegründung der Klägerin", 2),
        para("Die Revision ist unbegründet. Die Vorinstanzen haben zutreffend entschieden. "
             "Die Verifikationsfunktion des § 126a BGB erfordert, dass der Erklärungsgegner "
             "die qES am empfangenen Dokument selbst prüfen kann. "
             "Dies ist am Papierausdruck mit Transfervermerk nicht möglich."),
        para("Der Einwand der Klägerin, die Gegenmeinung führe zu einem Rechtsschutz-Defizit, "
             "verfängt nicht. Der Gesetzgeber hat dieses Problem erkannt und durch § 130e ZPO "
             "(ab 17. Juli 2024) gelöst. Hieraus folgt gerade, dass die alte Rechtslage "
             "das behauptete Problem nicht behoben hatte."),
        sp(0.2),
        bold_para("Wolfdieter Hassenstein-Heepen, Rechtsanwalt"),
        page_break(),
    ]
    return elems


def b22_b23_bgh():
    """22. Stellungnahme Verhandlungstermin + 23. BGH-Urteil"""
    elems = []
    elems.append(heading("STELLUNGNAHME ZUM VERHANDLUNGSTERMIN BGH VOM 27. NOVEMBER 2024", 1))
    elems.append(Paragraph("RA Dr. Ranftenschwedler-Bielenfels | 20. November 2024 | Bl. 92-93", sSmall))
    elems.append(sp(0.2))
    elems.append(qes_block("Dr. Engelbert Ranftenschwedler-Bielenfels", "D-Trust Public-CA 2-3 2022",
                            "12.07.2026", "20.11.2024 09:00:00"))
    elems.append(sp(0.2))
    elems += [
        para("Der VIII. Zivilsenat des BGH verhandelt am 27. November 2024 über die Revision "
             "der Klägerin (Az. VIII ZR 159/23). Die Klägerin hält an ihrer Auffassung fest, "
             "dass der Zugang der Kündigungserklärungen durch Postzustellung des Ausdrucks "
             "mit Transfervermerk § 298 Abs. 3 ZPO formgerecht bewirkt worden ist."),
        para("In einem Parallelverfahren (Az. VIII ZR 155/23) verhandelt der Senat über eine "
             "ähnliche Fragestellung, bei der der Schriftsatz per beA weitergeleitet worden ist."),
        sp(0.2),
        bold_para("Dr. Engelbert Ranftenschwedler-Bielenfels, Rechtsanwalt"),
        page_break(),
    ]

    # BGH-Urteil
    elems.append(heading("BGH-URTEIL VOM 27. NOVEMBER 2024 — VIII ZR 159/23", 1))
    elems.append(Paragraph("Tenor und Volltext-Auszug der Leitsätze | Bl. 94-99 der Akte", sSmall))
    elems.append(sp(0.2))
    elems += [
        bold_para("BUNDESGERICHTSHOF"),
        bold_para("VIII. ZIVILSENAT"),
        bold_para("URTEIL"),
        sp(0.2),
        para("Az.: VIII ZR 159/23"),
        para("Verhandlungstermin: 27. November 2024"),
        para("Vorsitz: Vorsitzender Richter am BGH Dr. Bünger"),
        sp(0.2),
        heading("TENOR:", 2),
        bold_para("Die Revision der Klägerin gegen das Urteil des Landgerichts Bielefeld "
                  "(3. Zivilkammer) vom 20. Juni 2023 wird auf Kosten der Klägerin zurückgewiesen."),
        sp(0.2),
        heading("LEITSÄTZE (sinngemäß nach BGH VIII ZR 159/23):", 2),
    ]

    leitsatz_data = [
        ["a)", "Bei einer empfangsbedürftigen Willenserklärung ist es auch für die elektronische "
               "Form zur Wahrung der Form nicht ausreichend, dass die Willenserklärung formgerecht "
               "abgegeben wurde; diese muss dem Erklärungsgegner vielmehr auch in der entsprechenden "
               "Form zugehen (§ 130 Abs. 1 Satz 1 BGB). Für den Zugang einer in einem qualifiziert "
               "elektronisch signierten elektronischen Dokument enthaltenen Willenserklärung ist es "
               "daher erforderlich, dass dieses Dokument so in den Machtbereich des Empfängers gelangt, "
               "dass dieser die qualifizierte elektronische Signatur des Erklärenden und damit die "
               "Echtheit des Dokuments prüfen kann (Verifikationsfunktion)."],
        ["b)", "Die Voraussetzungen des formgerechten Zugangs nach Leitsatz a) sind in dem Zeitraum "
               "vor dem Inkrafttreten der Vorschrift des § 130e ZPO am 17. Juli 2024 erfüllt, wenn in "
               "einem Zivilprozess ein elektronischer Schriftsatz mit einer gültigen qualifizierten "
               "elektronischen Signatur, der eine empfangsbedürftige Willenserklärung enthält, vom "
               "Gericht unter Aufrechterhaltung der elektronischen Signatur elektronisch an den "
               "Empfänger der Willenserklärung weitergeleitet wird."],
        ["c)", "In dem Zeitraum vor dem Inkrafttreten des § 130e ZPO bewirkt die Übermittlung eines "
               "Ausdrucks eines mit einer gültigen qualifizierten elektronischen Signatur versehenen, "
               "bei Gericht im Rahmen eines Zivilprozesses eingegangenen elektronischen Dokuments unter "
               "Beifügung eines Transfervermerks im Sinne des § 298 Abs. 3 ZPO keinen wirksamen Zugang "
               "der in dem Dokument enthaltenen empfangsbedürftigen Willenserklärung beim "
               "Erklärungsgegner (§ 126a Abs. 1 BGB). Der dem Ausdruck beigefügte Transfervermerk, der "
               "lediglich das Ergebnis einer entsprechenden Prüfung durch das Gericht dokumentiert, "
               "ermöglicht es dem Empfänger nicht, die Echtheit der Signatur auch seinerseits zu "
               "überprüfen."],
    ]
    t = Table([[Paragraph(ls[0], sBold), Paragraph(ls[1], sNormal)] for ls in leitsatz_data],
               colWidths=[0.7*cm, 15.3*cm])
    t.setStyle(TableStyle([
        ("BOX",        (0,0),(-1,-1), 1.0, C_QES_BLUE),
        ("BACKGROUND", (0,0),(-1,-1), C_QES_BG),
        ("GRID",       (0,0),(-1,-1), 0.3, colors.lightgrey),
        ("TOPPADDING",    (0,0),(-1,-1), 5),
        ("BOTTOMPADDING", (0,0),(-1,-1), 5),
        ("LEFTPADDING",   (0,0),(-1,-1), 6),
        ("VALIGN",     (0,0),(-1,-1), "TOP"),
    ]))
    elems.append(t)
    elems.append(sp(0.3))
    elems += [
        heading("ENTSCHEIDUNGSGRÜNDE (Auszug):", 2),
        para("Der VIII. Zivilsenat des BGH hat die Revision der Klägerin zurückgewiesen. "
             "Die in den qES-signierten Schriftsätzen vom 09. März 2022 und 13. Mai 2022 "
             "enthaltenen Kündigungserklärungen sind dem Beklagten nicht formgerecht zugegangen."),
        para("Die Schriftform des § 568 Abs. 1 BGB kann nach § 126 Abs. 3 BGB durch die "
             "elektronische Form des § 126a BGB ersetzt werden. § 568 Abs. 1 BGB schließt — "
             "anders als §§ 623, 766 Satz 2, 780 Satz 2, 781 Satz 2 BGB — die elektronische "
             "Form nicht aus."),
        para("Zur Wahrung der Form für eine empfangsbedürftige Willenserklärung genügt es nicht, "
             "dass die WE formgerecht abgegeben wurde. Sie muss dem Erklärungsgegner vielmehr "
             "auch in der vorgeschriebenen Form zugehen (§ 130 Abs. 1 Satz 1 BGB). "
             "Dieses Zugangserfordernis gilt auch für empfangsbedürftige WE in elektronischer Form."),
        para("Die Verifikationsfunktion der qES verlangt, dass der Empfänger die Echtheit der "
             "Signatur prüfen kann. Ein Papierausdruck mit Transfervermerk ermöglicht dies nicht. "
             "§ 130e ZPO (ab 17. Juli 2024) fingiert zwar für die Zukunft den formwirksamen Zugang, "
             "findet aber auf die hier vorliegenden Sachverhalte (2022) keine Anwendung."),
        sp(0.2),
        Paragraph("Karlsruhe, 27. November 2024 — BGH VIII. Zivilsenat", sSmall),
        Paragraph("Vorsitzender Richter am BGH Dr. Bünger", sBold),
        page_break(),
    ]
    return elems


def b24_mandantenmemo():
    """24. Mandantenmemo RA Ranftenschwedler-Bielenfels 02.12.2024"""
    elems = []
    elems.append(heading("MANDANTENMEMO VOM 02. DEZEMBER 2024", 1))
    elems.append(Paragraph("RA Dr. Ranftenschwedler-Bielenfels an Pferdedrescher-Riesenstein | "
                           "Bl. 100-103 der Akte | VERTRAULICH", sSmall))
    elems.append(sp(0.2))
    elems += [
        bold_para("Ranftenschwedler Ostkamp Rechtsanwälte mbB"),
        para("Niederwall 12 · 33602 Bielefeld"),
        sp(0.1),
        para("Bielefeld, 02. Dezember 2024"),
        sp(0.1),
        bold_para("Frau Hildegunde Pferdedrescher-Riesenstein"),
        para("Ottilienweg 23 · 33647 Bielefeld-Brackwede"),
        sp(0.2),
        bold_para("Betr.: BGH VIII ZR 159/23 — Ergebnis der Revision — Bittere Lehren"),
        sp(0.2),
        bold_para("Sehr geehrte Frau Pferdedrescher-Riesenstein,"),
        sp(0.1),
        para("der BGH hat am 27. November 2024 unsere Revision zurückgewiesen. "
             "Ich übermittle Ihnen hiermit die wesentlichen Lehren aus diesem Verfahren — "
             "und ich werde ehrlich sein, auch wenn einige Punkte schmerzen."),
        sp(0.2),
        heading("I. Die WhatsApp-Kündigung war von Anfang an aussichtslos", 2),
        para("Die Kündigung per WhatsApp-Sprachnachricht und unsignierter PDF vom "
             "10. Februar 2022 war formunwirksam — das stand von Beginn an fest. "
             "§ 568 Abs. 1 BGB ist eindeutig. Ich sage das ohne Vorwurf, aber Sie haben "
             "zunächst ohne anwaltliche Beratung gehandelt. Dies kostet uns jetzt "
             "fast drei Jahre Prozess."),
        sp(0.2),
        heading("II. Kündigung per qES ist grundsätzlich möglich — aber der Zugang muss passen", 2),
        para("§ 126a BGB erlaubt die Ersetzung der Schriftform durch die elektronische Form. "
             "Eine qES-signierte Kündigung wäre also wirksam — wenn sie dem Mieter formgerecht "
             "zuginge. Der BGH hat klargestellt:"),
        para("• qES-signierter Schriftsatz, der vom Gericht elektronisch (mit Aufrechterhaltung "
             "der qES) an den Empfänger weitergeleitet wird: <b>formgerechter Zugang ✓</b>"),
        para("• qES-signierter Schriftsatz, der vom Gericht als Papierausdruck mit "
             "Transfervermerk § 298 Abs. 3 ZPO zugestellt wird: "
             "<b>KEIN formgerechter Zugang ✗</b>"),
        sp(0.2),
        heading("III. Was wir hätten tun müssen", 2),
        para("<b>Option 1 (sicherste Lösung, immer noch empfohlen):</b> "
             "Handschriftlich unterzeichneter Brief per Einschreiben mit Rückschein "
             "oder durch Boten mit Empfangsquittung. "
             "Der klassische Weg ist zuverlässig und unproblematisch."),
        para("<b>Option 2 (qES-Mail direkt an Mieter):</b> "
             "Eine qES-signierte PDF per E-Mail direkt an Herrn Eberhart-Wolframshausen — "
             "nicht über das Gericht — wäre möglicherweise formgerecht zugegangen, "
             "wenn er die Signatur prüfen konnte. "
             "Dies setzt voraus, dass er einer E-Mail-Kündigung nicht widerspricht "
             "(Einverständnis mit elektronischem Zugang). "
             "Das ist eine offene Rechtsfrage, die Ihnen niemand garantieren kann."),
        para("<b>Option 3 (ab 17. Juli 2024, § 130e ZPO):</b> "
             "Seit dem 17. Juli 2024 fingiert § 130e ZPO den formwirksamen Zugang, "
             "wenn der qES-signierte Schriftsatz als elektronisches Dokument bei Gericht "
             "eingereicht und dem Empfänger zugestellt wurde. "
             "Für zukünftige Verfahren ist dieses Problem damit gesetzgeberisch gelöst."),
        sp(0.2),
        page_break(),
    ]
    elems += [
        heading("Mandantenmemo 02.12.2024 — Seite 2 von 4", 1),
        heading("IV. Kostenfolgen und Empfehlung", 2),
        para("Sie haben in allen drei Instanzen verloren. Die Gesamtkosten belaufen sich "
             "auf geschätzte EUR 8.000,– bis EUR 12.000,– (Gerichtsgebühren + "
             "Anwaltskosten Kläger + Anwaltskosten Beklagter, die Sie zu tragen haben). "
             "Dies war vermeidbar."),
        para("<b>Empfehlung für die Zukunft (für Ihre anderen Mieter):</b>"),
        para("1. Kündigungen immer per handschriftlich unterzeichnetem Brief, "
             "Einschreiben mit Rückschein oder persönliche Übergabe mit Quittung."),
        para("2. Wenn elektronisch: qES-signiertes Dokument per E-Mail direkt an Mieter, "
             "NICHT über das Gerichtsverfahren als erster Zugang."),
        para("3. Im laufenden Prozess: Kündigung parallel außergerichtlich erklären, "
             "dann Schriftsatz ins Verfahren einführen."),
        para("4. Niemals WhatsApp für rechtsgestaltende Erklärungen. "
             "Nicht einmal für Nachfragen."),
        sp(0.3),
        bold_para("Mit freundlichen Grüßen"),
        para("Dr. Engelbert Ranftenschwedler-Bielenfels"),
        para("Fachanwalt für Miet- und WEG-Recht"),
        page_break(),
    ]
    return elems


def b25_online_vermieter_memo():
    """25. Online-Vermieter-Memo (3 Seiten)"""
    elems = []
    elems.append(heading("\"ONLINE-VERMIETER\"-MEMO", 1))
    elems.append(Paragraph("RA Dr. Ranftenschwedler-Bielenfels | 05. Dezember 2024 | "
                           "Bl. 104-106 der Akte | Vertraulich", sSmall))
    elems.append(sp(0.2))
    elems += [
        bold_para("MEMO: Digitale Kündigung der Zukunft — und ihre Risiken für Mieter"),
        sp(0.2),
        italic("[Dieser Abschnitt enthält Überlegungen zur Rechtsentwicklung, "
               "die keinen abschließenden Rechtsrat darstellen.]"),
        sp(0.2),
        heading("I. Die Ausgangslage: § 130e ZPO und seine Wirkung", 2),
        para("Mit dem Inkrafttreten des § 130e ZPO am 17. Juli 2024 hat der Gesetzgeber "
             "das Problem gelöst, das uns in diesem Verfahren EUR 10.000,– gekostet hat: "
             "Kündigungen in qES-signierten Schriftsätzen, die elektronisch eingereicht "
             "und zugestellt werden, gelten nun als formgerecht zugegangen."),
        para("Das klingt gut für Vermieter. Aber es hat eine Kehrseite."),
        sp(0.2),
        heading("II. Die künftige Online-Kündigung: Mieter müssen ihre Postfächer prüfen", 2),
        para("Wenn Vermieter (und deren Anwälte) künftig qES-Kündigungen direkt per E-Mail "
             "oder über das Gericht in prüfbarer elektronischer Form zustellen können, "
             "bedeutet dies: <b>Mieter müssen ihre elektronischen Postfächer und "
             "Messenger-Dienste fortlaufend auf qES-signierte Anhänge prüfen.</b>"),
        para("Bislang war es undenkbar, dass eine Kündigung per Messenger wirksam war. "
             "Das ändert sich. Wenn eine qES-signierte PDF per E-Mail zugeht und der Mieter "
             "sie öffnen und prüfen kann, ist der Zugang formgerecht — auch wenn der Mieter "
             "die E-Mail nur kurz überflogen hat."),
        sp(0.2),
        heading("III. Mandanten-Warnung-Vorlage (für Pferdedrescher-Riesenstein, "
                "deren Mietergruppe)", 2),
        para("Sie haben mich gebeten, eine Vorlage für ein Rundschreiben an Ihre anderen "
             "fünf Mieter zu erstellen. Hier ein Entwurf:"),
        sp(0.1),
        Table([[Paragraph(
            "<b>HINWEIS AN ALLE MIETER — ECKENDORFER STR. 188, BIELEFELD</b><br/><br/>"
            "Sehr geehrte Mieterinnen und Mieter,<br/><br/>"
            "ich, Hildegunde Pferdedrescher-Riesenstein, teile Ihnen als Hauseigentümerin mit, "
            "dass ich künftig rechtsgestaltende Erklärungen (insbesondere Kündigungen, "
            "Mieterhöhungen) ausschließlich per Einschreiben mit Rückschein übermitteln werde.<br/><br/>"
            "Sollte ich jemals eine qualifiziert elektronisch signierte Erklärung per E-Mail "
            "versenden, werde ich Sie vorab gesondert informieren.<br/><br/>"
            "Ich bitte Sie, Ihre E-Mail-Adresse beim Hauspostfach zu hinterlegen.<br/><br/>"
            "Mit freundlichen Grüßen,<br/>Hildegunde Pferdedrescher-Riesenstein",
            sNormal)]],
            colWidths=[16*cm]),
        ],
        sp(0.2),
        heading("IV. Die Mieterschutz-Frage: \"Sind wir die Bösen?\"", 2),
        para("Frau Pferdedrescher-Riesenstein, Sie haben in unserem letzten Telefonat gefragt: "
             "\"Bin ich eigentlich die Böse in dieser Geschichte?\" — "
             "Ich erlaube mir, diese Frage in aller Sachlichkeit zu beantworten."),
        para("Nein, Sie sind nicht die Böse. Herr Eberhart-Wolframshausen hat über Jahre "
             "zu wenig oder gar nicht gezahlt. Das ist ein echtes Problem für Sie als Vermieterin, "
             "die ihrerseits Verbindlichkeiten hat."),
        para("Aber: Das Formerfordernis des § 568 BGB dient dem Mieterschutz. "
             "Es soll sicherstellen, dass Mieter nicht durch flüchtige Erklärungen "
             "in die Obdachlosigkeit getrieben werden. Die Formstrenge ist bewusst. "
             "Das war die Lektion dieses Verfahrens — nicht die technische Frage der qES, "
             "sondern die grundlegende Frage: Haben Sie alles getan, um Herrn "
             "Eberhart-Wolframshausen rechtssicher zu informieren? Im Februar 2022: nein."),
        para("<b>Fazit:</b> Die Böse sind Sie nicht. Aber Sie waren unvorsichtig. "
             "Das Recht gibt dem schwächeren Teil — dem Mieter — den Vorteil der Formstrenge. "
             "Das ist nicht ungerecht, sondern beabsichtigt."),
        page_break(),
    ]
    return elems


def b26_handschriftliche_notizen():
    """26. Handschriftliche Mieter-Notizen"""
    elems = []
    elems.append(heading("HANDSCHRIFTLICHE MIETER-NOTIZEN — EBERHART-WOLFRAMSHAUSEN", 1))
    elems.append(Paragraph("Randnotizen an Aktenrand der Schriftsätze des Beklagten | Passim", sSmall))
    elems.append(sp(0.2))
    elems.append(italic("[Originalnotizen rekonstruiert aus den Aktenblättern — "
                         "kursive Darstellung gemäß Akte]"))
    elems.append(sp(0.3))

    notizen = [
        ("Bl. 10 (WhatsApp-Verlauf)", "\"Sie hat mir das per WhatsApp geschickt!!! Unglaublich.\""),
        ("Bl. 16 (E-Mail + PDF)", "\"Das PDF hat KEINE Signatur. Ich kann sofort in den Eigenschaften sehen: "
                                   "Keine digitale Unterschrift. Das weiss jedes Kind im IT.\""),
        ("Bl. 30 (Hinweisbeschluss)", "\"Na bitte! Das Amtsgericht sieht das auch so. "
                                       "Transfervermerk = kein qES-Zugang.\""),
        ("Bl. 32 (eigene Klageerwiderung)", "\"Ich muss einen Anwalt nehmen für die Berufung. "
                                             "Aber erst mal schauen ob das AG richtig liegt.\""),
        ("Bl. 42 (AG-Urteil)", "\"Gewonnen!!! Erster Instanz. Formfrage. "
                                "Die Signatur muss beim Empfänger ankommen, nicht beim Gericht.\""),
        ("Bl. 51 (Mandatsannahme Hassenstein-Heepen)", "\"RA Hassenstein klingt gut. "
                                                        "€ 280/h — teuer aber okay wenn wir gewinnen.\""),
        ("Bl. 65 (LG-Urteil)", "\"Zweimal gewonnen! LG Bielefeld bestätigt AG. "
                                 "Revision beim BGH wird kommen. Mal sehen.\""),
        ("Bl. 94 (BGH-Urteil)", "\"BGH: Revision zurückgewiesen. Formfehler der Klägerin. "
                                  "Wir haben Recht behalten. Drei Instanzen. "
                                  "Echte Frechheit als IT-Admin so behandelt zu werden, "
                                  "als ob ich keine qES erkennen würde.\""),
    ]
    for bl, notiz in notizen:
        elems.append(Paragraph(f"<b>{bl}:</b>", sBold))
        elems.append(italic(f"    {notiz}"))
        elems.append(sp(0.15))
    elems.append(page_break())
    return elems


def b27_email_kette():
    """27. E-Mail-Kette Ranftenschwedler ↔ Pferdedrescher-Riesenstein (8 Seiten)"""
    elems = []
    elems.append(heading("E-MAIL-KETTE: RANFTENSCHWEDLER ↔ PFERDEDRESCHER-RIESENSTEIN", 1))
    elems.append(Paragraph("Februar 2022 bis November 2024 | Bl. 107-114 der Akte", sSmall))
    elems.append(sp(0.2))

    emails = [
        ("11.02.2022", "hildegunde@pferdedrescher-online-marketing.de",
         "dr.ranftenschwedler@ra-niederwall.de",
         "DRINGEND — Mietproblem Eckendorfer Str. 188",
         ["Sehr geehrter Herr Ranftenschwedler-Bielenfels,", "",
          "ich habe gestern per WhatsApp und E-Mail gekündigt, aber der Mieter sagt,",
          "das sei nicht gültig. Bitte helfen Sie mir!!! Er zahlt seit Monaten nicht.",
          "Was kann ich tun?", "", "Mit freundlichen Grüßen,",
          "Hildegunde Pferdedrescher-Riesenstein"]),
        ("15.02.2022", "dr.ranftenschwedler@ra-niederwall.de",
         "hildegunde@pferdedrescher-online-marketing.de",
         "AW: DRINGEND — Mietproblem Eckendorfer Str. 188",
         ["Sehr geehrte Frau Pferdedrescher-Riesenstein,", "",
          "ich habe Ihre Situation analysiert. Die WhatsApp-Kündigung ist formunwirksam",
          "(§ 568, § 125 BGB). Ich empfehle sofortige Beauftragung. Bitte kommen Sie",
          "Montag in die Kanzlei. Wir bereiten alles vor.", "", "MfG",
          "Dr. Engelbert Ranftenschwedler-Bielenfels, RA"]),
        ("10.10.2022", "hildegunde@pferdedrescher-online-marketing.de",
         "dr.ranftenschwedler@ra-niederwall.de",
         "Urteil AG Bielefeld — was jetzt???",
         ["Herr Ranftenschwedler-Bielenfels,", "",
          "wir haben verloren!!! Klage abgewiesen. Das kann doch nicht sein.",
          "Der Mann zahlt nicht und wir verlieren? Was machen wir jetzt?", "",
          "Hildegunde Pferdedrescher-Riesenstein"]),
        ("14.10.2022", "dr.ranftenschwedler@ra-niederwall.de",
         "hildegunde@pferdedrescher-online-marketing.de",
         "AW: Urteil AG Bielefeld — Berufung",
         ["Sehr geehrte Frau Pferdedrescher-Riesenstein,", "",
          "das Urteil ist angreifbar. Die Formfrage ist nicht höchstrichterlich geklärt.",
          "Ich empfehle Berufung. Die Erfolgsaussichten schätze ich bei 40-50%.", "",
          "Dr. Engelbert Ranftenschwedler-Bielenfels, RA"]),
        ("20.06.2023", "hildegunde@pferdedrescher-online-marketing.de",
         "dr.ranftenschwedler@ra-niederwall.de",
         "LG Bielefeld — wieder verloren",
         ["Jetzt auch LG verloren. Ist das Ihr Ernst? Revision zum BGH?",
          "Was kostet das? Ich habe schon EUR 5.000 ausgegeben.", "",
          "Pferdedrescher-Riesenstein"]),
        ("25.06.2023", "dr.ranftenschwedler@ra-niederwall.de",
         "hildegunde@pferdedrescher-online-marketing.de",
         "AW: Revision BGH — Kosten und Chancen",
         ["Sehr geehrte Frau Pferdedrescher-Riesenstein,", "",
          "die Revision ist zugelassen worden — das ist eine gute Nachricht, denn es zeigt,",
          "dass das LG selbst die Rechtsfrage für grundsätzlich hält. Kosten:",
          "Gerichtsgebühren ca. EUR 1.500, mein Honorar ca. EUR 3.500. Total ca. EUR 5.000.",
          "Ich rate zur Revision — die Rechtsfrage muss der BGH klären.", "",
          "Dr. Engelbert Ranftenschwedler-Bielenfels, RA"]),
        ("28.11.2024", "hildegunde@pferdedrescher-online-marketing.de",
         "dr.ranftenschwedler@ra-niederwall.de",
         "BGH-Urteil gestern — ich bin am Ende",
         ["Ich habe gerade die Pressemitteilung gelesen. BGH hat uns abgewiesen.",
          "2,5 Jahre Prozess. EUR 10.000 Kosten. Der Mieter wohnt noch da.",
          "Was soll ich jetzt machen?", "", "H. Pferdedrescher-Riesenstein"]),
        ("02.12.2024", "dr.ranftenschwedler@ra-niederwall.de",
         "hildegunde@pferdedrescher-online-marketing.de",
         "AW: BGH-Urteil — Bittere Lehren (Memo separat)",
         ["Sehr geehrte Frau Pferdedrescher-Riesenstein,", "",
          "ich verstehe Ihre Enttäuschung. Das ausführliche Memo habe ich Ihnen",
          "gesondert als qES-signierte PDF zugesandt (diesmal korrekt signiert!).",
          "Bitte lesen Sie es sorgfältig. Für die Zukunft: Handschrift und Einschreiben.",
          "Oder qES-Mail direkt an Mieter. Nicht über Gericht.", "",
          "Dr. Engelbert Ranftenschwedler-Bielenfels, RA"]),
    ]

    for date_str, sender, recipient, subject, body_lines in emails:
        elems += email_block(date_str, sender, recipient, subject, body_lines)
        elems.append(sp(0.2))
    elems.append(page_break())
    return elems


def b28_kostenfestsetzung():
    """28. Kostenfestsetzungsbeschluss-Entwurf"""
    elems = []
    elems.append(heading("KOSTENFESTSETZUNGSBESCHLUSS — ENTWURF", 1))
    elems.append(Paragraph("Bl. 115-116 der Akte | Dezember 2024", sSmall))
    elems.append(sp(0.2))
    elems += [
        bold_para("AMTSGERICHT BIELEFELD"),
        bold_para("KOSTENFESTSETZUNGSBESCHLUSS (Entwurf — nicht rechtskräftig)"),
        sp(0.2),
        para("In der Sache Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen"),
        para("Gesamt-Az.: AG 34 C 421/22 → LG 14 S 88/23 → BGH VIII ZR 159/23"),
        sp(0.2),
        heading("Streitwert-Berechnung:", 2),
        data_table("Streitwert:", [
            ["Räumungsantrag (§ 41 GKG):", "EUR 7.787,64 (= 12 × EUR 648,97)"],
            ["Zahlungsantrag:", "EUR 2.229,40"],
            ["Gesamt-Streitwert:", "EUR 10.017,04"],
        ]),
        sp(0.2),
        heading("Kostenpositionen (alle Instanzen, geschätzt):", 2),
        data_table("Gerichtsgebühren:", [
            ["AG Bielefeld (3,0 Gebühren aus EUR 10.017):", "ca. EUR 618,–"],
            ["LG Bielefeld Berufung (4,0 Gebühren):", "ca. EUR 824,–"],
            ["BGH Revision (5,0 Gebühren):", "ca. EUR 1.030,–"],
            ["Gesamt Gerichtsgebühren:", "ca. EUR 2.472,–"],
        ]),
        sp(0.1),
        data_table("Anwaltsgebühren Klägerin (RA Ranftenschwedler-Bielenfels):", [
            ["AG 1. Instanz (1,3 Verfahrens- + 1,2 Terminsgebühr + Auslagen):", "ca. EUR 1.612,–"],
            ["LG Berufung (1,6 + 1,2 Gebühren):", "ca. EUR 2.003,–"],
            ["BGH Revision (2,3 + 1,5 Gebühren):", "ca. EUR 3.510,–"],
            ["Gesamt Klägerin-RA:", "ca. EUR 7.125,–"],
        ]),
        sp(0.1),
        data_table("Anwaltsgebühren Beklagter (RA Hassenstein-Heepen, Stundensatz):", [
            ["Berufung + Revisionsverfahren (geschätzt 25 Std. à EUR 280):", "EUR 7.000,–"],
            ["Umsatzsteuer 19%:", "EUR 1.330,–"],
            ["Gesamt Beklagter-RA:", "ca. EUR 8.330,–"],
        ]),
        sp(0.2),
        Paragraph("<b>Gesamtkosten-Last der Klägerin (Verliererin):</b> "
                  "ca. EUR 2.472 + EUR 7.125 + EUR 8.330 = ca. <b>EUR 17.927,–</b> "
                  "(plus eigener Zeitaufwand)", sRed),
        sp(0.2),
        Paragraph("<i>Hinweis: Dies ist ein Entwurf zur Kostenschätzung, kein rechtskräftiger Beschluss. "
                  "Der tatsächliche Kostenfestsetzungsbeschluss ergeht durch das Prozessgericht.</i>", sSmall),
        page_break(),
    ]
    return elems


def b29_anlagenverzeichnis():
    """29. Anlagenverzeichnis K-MIET-1 bis K-MIET-34"""
    elems = []
    elems.append(heading("ANLAGENVERZEICHNIS K-MIET-1 BIS K-MIET-34", 1))
    elems.append(Paragraph("Anlage zur Klageschrift / Schriftsätzen — Bl. 117-118 der Akte", sSmall))
    elems.append(sp(0.2))
    elems.append(italic("[Lücken im Anlagenverzeichnis sind aktenkundig — Sonderband II nicht beigefügt]"))
    elems.append(sp(0.2))
    anlagen = [
        ("K-MIET-1", "Mietvertrag v. 03.04.2017 (vollständig)", "Sonderband II, Bl. 1-22", "beigefügt"),
        ("K-MIET-2", "Mahnungs-Historie (Tabelle Frühjahr 2019 - Feb. 2022)", "Bl. 8-9", "beigefügt"),
        ("K-MIET-3", "Kontoauszüge Sparkasse Bielefeld (2019-2022)", "Sonderband II, Bl. 23 ff.", "beigefügt"),
        ("K-MIET-4", "E-Mail Mahnung 02.07.2019", "Bl. 120", "beigefügt"),
        ("K-MIET-5", "E-Mail Mahnung 04.11.2019", "Bl. 121", "beigefügt"),
        ("K-MIET-6", "E-Mail Mahnung 10.02.2020", "Bl. 122", "beigefügt"),
        ("K-MIET-7", "WhatsApp-Screenshots 08.-10.02.2022", "Bl. 10-15", "beigefügt"),
        ("K-MIET-8", "E-Mail + PDF v.