#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testakte Krisenfrueherkennung StaRUG — Vier Varianten
======================================================
Erzeugt: Testakte_Krisenfrueherkennung_StaRUG_Varianten.pdf
Datum:   22. Mai 2026
Zweck:   Lehr- und Demonstrations-Akte zu § 1 StaRUG
         (Vorbereitung Restructuring Lounge Hamburg, 28. Mai 2026)
"""

import os
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether, FrameBreak
)
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate, Frame
from functools import partial

# ─── Pfade ────────────────────────────────────────────────────────────────────
BASE = "/home/user/workspace/claude-fuer-deutsches-recht/testakten/krisenfrueherkennung-starug-vier-varianten"
os.makedirs(BASE, exist_ok=True)
OUTPUT = os.path.join(BASE, "Testakte_Krisenfrueherkennung_StaRUG_Varianten.pdf")

# ─── Farben ───────────────────────────────────────────────────────────────────
DUNKELBLAU   = colors.HexColor("#1A2D4F")
MITTELBLAU   = colors.HexColor("#2B4C8C")
HELLBLAU     = colors.HexColor("#D6E4F0")
ROT          = colors.HexColor("#A02020")
GRUEN        = colors.HexColor("#1A5C2E")
GOLD         = colors.HexColor("#B8860B")
GRAU_HELL    = colors.HexColor("#F4F4F4")
GRAU_MID     = colors.HexColor("#CCCCCC")
GRAU_DUNKEL  = colors.HexColor("#555555")
TEXT_SCHWARZ = colors.HexColor("#1A1A1A")
ORANGE       = colors.HexColor("#CC6600")
LILA         = colors.HexColor("#5C2D8A")

# Varianten-Farben
FARBE_A = colors.HexColor("#1A5C2E")   # Gruen  (KI/Forschung)
FARBE_B = colors.HexColor("#1A2D4F")   # Dunkelblau (Textil/Tradition)
FARBE_C = colors.HexColor("#A02020")   # Rot (Batterie/Kapitalmarkt)
FARBE_D = colors.HexColor("#CC6600")   # Orange (Klein-UG)

W, H = A4

# ─── Styles ───────────────────────────────────────────────────────────────────
def make_styles():
    s = {}
    s['title'] = ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=16,
        leading=20, alignment=TA_CENTER, textColor=DUNKELBLAU, spaceAfter=6)
    s['subtitle'] = ParagraphStyle('subtitle', fontName='Helvetica', fontSize=11,
        leading=15, alignment=TA_CENTER, textColor=GRAU_DUNKEL, spaceAfter=10)
    s['h1'] = ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=13,
        leading=17, textColor=DUNKELBLAU, spaceBefore=12, spaceAfter=5)
    s['h2'] = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=11,
        leading=15, textColor=DUNKELBLAU, spaceBefore=9, spaceAfter=4)
    s['h3'] = ParagraphStyle('h3', fontName='Helvetica-Bold', fontSize=10,
        leading=14, textColor=TEXT_SCHWARZ, spaceBefore=7, spaceAfter=3)
    s['body'] = ParagraphStyle('body', fontName='Helvetica', fontSize=10,
        leading=14, alignment=TA_JUSTIFY, textColor=TEXT_SCHWARZ, spaceAfter=5)
    s['body_left'] = ParagraphStyle('body_left', fontName='Helvetica', fontSize=10,
        leading=14, alignment=TA_LEFT, textColor=TEXT_SCHWARZ, spaceAfter=5)
    s['small'] = ParagraphStyle('small', fontName='Helvetica', fontSize=8.5,
        leading=12, textColor=GRAU_DUNKEL, spaceAfter=3)
    s['small_bold'] = ParagraphStyle('small_bold', fontName='Helvetica-Bold', fontSize=8.5,
        leading=12, textColor=TEXT_SCHWARZ, spaceAfter=3)
    s['bold'] = ParagraphStyle('bold', fontName='Helvetica-Bold', fontSize=10,
        leading=14, textColor=TEXT_SCHWARZ, spaceAfter=5)
    s['right'] = ParagraphStyle('right', fontName='Helvetica', fontSize=10,
        leading=14, alignment=TA_RIGHT, textColor=TEXT_SCHWARZ)
    s['center'] = ParagraphStyle('center', fontName='Helvetica', fontSize=10,
        leading=14, alignment=TA_CENTER, textColor=TEXT_SCHWARZ)
    s['italic'] = ParagraphStyle('italic', fontName='Times-Italic', fontSize=10,
        leading=14, alignment=TA_LEFT, textColor=TEXT_SCHWARZ, spaceAfter=4,
        leftIndent=15)
    s['handschrift'] = ParagraphStyle('handschrift', fontName='Times-Italic', fontSize=11,
        leading=16, alignment=TA_LEFT, textColor=colors.HexColor("#1A1A6E"),
        spaceAfter=4, leftIndent=20)
    s['courier'] = ParagraphStyle('courier', fontName='Courier', fontSize=9,
        leading=13, alignment=TA_LEFT, textColor=TEXT_SCHWARZ, spaceAfter=2)
    s['courier_bold'] = ParagraphStyle('courier_bold', fontName='Courier-Bold', fontSize=9,
        leading=13, alignment=TA_LEFT, textColor=TEXT_SCHWARZ)
    s['warn'] = ParagraphStyle('warn', fontName='Helvetica-Bold', fontSize=10,
        leading=14, textColor=ROT, spaceBefore=6, spaceAfter=4)
    s['legal'] = ParagraphStyle('legal', fontName='Helvetica', fontSize=9.5,
        leading=14, alignment=TA_JUSTIFY, textColor=TEXT_SCHWARZ, spaceAfter=4)
    s['legal_bold'] = ParagraphStyle('legal_bold', fontName='Helvetica-Bold', fontSize=9.5,
        leading=14, textColor=TEXT_SCHWARZ, spaceAfter=4)
    s['indent'] = ParagraphStyle('indent', fontName='Helvetica', fontSize=10,
        leading=14, textColor=TEXT_SCHWARZ, leftIndent=25, spaceAfter=4)
    s['indent2'] = ParagraphStyle('indent2', fontName='Helvetica', fontSize=10,
        leading=14, textColor=TEXT_SCHWARZ, leftIndent=45, spaceAfter=4)
    s['footnote'] = ParagraphStyle('footnote', fontName='Helvetica', fontSize=7.5,
        leading=10, textColor=GRAU_DUNKEL, spaceAfter=2)
    s['aktenzeichen'] = ParagraphStyle('aktenzeichen', fontName='Courier-Bold', fontSize=10,
        leading=14, textColor=DUNKELBLAU, spaceAfter=3)
    s['panik'] = ParagraphStyle('panik', fontName='Times-Italic', fontSize=10,
        leading=15, textColor=colors.HexColor("#2E0000"), spaceAfter=4, leftIndent=10)
    return s

S = make_styles()

# ─── Hilfsfunktionen ──────────────────────────────────────────────────────────

def hr(color=GRAU_MID, thickness=0.5, spaceB=6, spaceA=6):
    return HRFlowable(width="100%", thickness=thickness, color=color,
                      spaceAfter=spaceA, spaceBefore=spaceB)

def fax_block(lines):
    """Courier-Block mit ====-Rahmen wie Faxkopf."""
    content = []
    content.append(Paragraph("=" * 70, S['courier']))
    for line in lines:
        content.append(Paragraph(line, S['courier']))
    content.append(Paragraph("=" * 70, S['courier']))
    return content

def kanzlei_kopf_rw():
    """ASCII-Logo Reher Wennstedt Restrukturierung PartmbB."""
    lines = [
        "  ____  __        __",
        " |  _ \\ \\ \\      / /",
        " | |_) | \\ \\ /\\ / / ",
        " |  _ <   \\ V  V /  ",
        " |_| \\_\\   \\_/\\_/   ",
        "",
        " REHER WENNSTEDT RESTRUKTURIERUNG",
        " Partnerschaft mbB",
        " Hohe Bleichen 14 | 20354 Hamburg",
        " Tel.: +49 40 4800 920-0 | Fax: +49 40 4800 920-99",
        " info@reher-wennstedt.de | www.reher-wennstedt.de",
    ]
    content = []
    for line in lines:
        content.append(Paragraph(line, S['courier']))
    return content

def kanzlei_kopf_wandelmoser():
    lines = [
        "  __        __             _      _",
        "  \\ \\      / /__ _ _ _   | |    | |",
        "   \\ \\ /\\ / / _` | '_ \\  | |    | |",
        "    \\ V  V / (_| | | | | | |___ | |___",
        "     \\_/\\_/ \\__,_|_| |_| |_____||_____|",
        "",
        " Rechtsanwaeltin Charlotte Wandelmoser",
        " Kantstrasse 91 | 10627 Berlin-Charlottenburg",
        " Tel.: +49 30 3150 88-0 | c.wandelmoser@ra-wandelmoser.de",
    ]
    content = []
    for line in lines:
        content.append(Paragraph(line, S['courier']))
    return content

def tbl_style_standard():
    return TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DUNKELBLAU),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 8.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, GRAU_HELL]),
        ('GRID', (0,0), (-1,-1), 0.3, GRAU_MID),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ])

def tbl_style_zahlen():
    ts = tbl_style_standard()
    ts.add('ALIGN', (1,1), (-1,-1), 'RIGHT')
    ts.add('FONTNAME', (0,1), (0,-1), 'Helvetica')
    return ts

# ─── Seiten-Templates ────────────────────────────────────────────────────────

def page_standard(canvas_obj, doc, aktenzeichen="", betreff=""):
    canvas_obj.saveState()
    # Kopfzeile
    canvas_obj.setFillColor(DUNKELBLAU)
    canvas_obj.rect(0, H - 22*mm, W, 22*mm, fill=1, stroke=0)
    canvas_obj.setFillColor(colors.white)
    canvas_obj.setFont('Helvetica-Bold', 9)
    canvas_obj.drawString(15*mm, H - 11*mm,
        "KRISENFRUEHERKENNUNG NACH § 1 StaRUG — VIER FALLVARIANTEN")
    canvas_obj.setFont('Helvetica', 8)
    if aktenzeichen:
        canvas_obj.drawString(15*mm, H - 18*mm, f"Az.: {aktenzeichen}")
    if betreff:
        canvas_obj.drawRightString(W - 15*mm, H - 18*mm, betreff)
    # Goldlinie
    canvas_obj.setFillColor(GOLD)
    canvas_obj.rect(0, H - 23*mm, W, 1*mm, fill=1, stroke=0)
    # Fusszeile
    canvas_obj.setFillColor(GRAU_HELL)
    canvas_obj.rect(0, 0, W, 13*mm, fill=1, stroke=0)
    canvas_obj.setFillColor(GRAU_DUNKEL)
    canvas_obj.setFont('Helvetica', 7)
    canvas_obj.drawString(15*mm, 8*mm,
        "VERTRAULICH — Nur zur internen Verwendung der Kanzlei Reher Wennstedt Restrukturierung PartmbB")
    canvas_obj.drawString(15*mm, 4*mm,
        "Fiktive Testakte zu Ausbildungs- und Demonstrationszwecken. Kein realer Mandatsbezug.")
    canvas_obj.drawRightString(W - 15*mm, 8*mm, f"Seite {doc.page}")
    canvas_obj.setStrokeColor(GRAU_MID)
    canvas_obj.setLineWidth(0.3)
    canvas_obj.line(15*mm, 13*mm, W - 15*mm, 13*mm)
    canvas_obj.restoreState()

def page_folie(canvas_obj, doc):
    canvas_obj.saveState()
    canvas_obj.setFillColor(DUNKELBLAU)
    canvas_obj.rect(0, 0, W, H, fill=1, stroke=0)
    # weisser Rahmen
    canvas_obj.setStrokeColor(GOLD)
    canvas_obj.setLineWidth(3)
    canvas_obj.rect(10*mm, 10*mm, W - 20*mm, H - 20*mm, fill=0, stroke=1)
    canvas_obj.setFillColor(colors.white)
    canvas_obj.setFont('Helvetica', 7)
    canvas_obj.drawString(12*mm, 13*mm,
        f"Restructuring Lounge Hamburg — WAYES — 28. Mai 2026 — Seite {doc.page}")
    canvas_obj.restoreState()

# ─── KONVOLUT-AKTENDECKEL ─────────────────────────────────────────────────────

def build_konvolut_deckel(story):
    story.append(Spacer(1, 3*cm))
    # Hauptrahmen
    data = [[
        Paragraph(
            "<b>TESTAKTE</b>",
            ParagraphStyle('big', fontName='Helvetica-Bold', fontSize=22,
                           alignment=TA_CENTER, textColor=colors.white)
        )
    ]]
    tbl = Table(data, colWidths=[16*cm])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), DUNKELBLAU),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 0.5*cm))

    story.append(Paragraph(
        "Krisenfrüherkennung und Krisenmanagement",
        ParagraphStyle('deckT', fontName='Helvetica-Bold', fontSize=18,
                       alignment=TA_CENTER, textColor=DUNKELBLAU, leading=24)
    ))
    story.append(Paragraph(
        "nach <b>§ 1 StaRUG</b>",
        ParagraphStyle('deckT2', fontName='Helvetica-Bold', fontSize=16,
                       alignment=TA_CENTER, textColor=DUNKELBLAU, leading=22, spaceAfter=4)
    ))
    story.append(Paragraph(
        "Vier Fallvarianten im Vergleich",
        ParagraphStyle('deckT3', fontName='Helvetica', fontSize=14,
                       alignment=TA_CENTER, textColor=GRAU_DUNKEL, leading=20, spaceAfter=20)
    ))
    story.append(hr(GOLD, 2))
    story.append(Spacer(1, 0.4*cm))

    # Varianten-Übersicht auf Deckel
    var_data = [
        ['VAR.', 'MANDANT', 'RECHTSFORM', 'KRISENKERN'],
        ['A', 'VEYRA AI Foundation gGmbH', 'gGmbH (gemeinn.)', 'Spendenausfall + GPU-Burn + Förder-Delay'],
        ['B', 'Herrenbluse & Zwirn Hartmannschmidt AG', 'AG (Open Market)', 'Anleihe-Refinanzierung EUR 65 Mio. + Covenant'],
        ['C', 'Nordfels Power Cells SE', 'SE (börsennotiert)', 'Umsatzeinbruch + EUR 550 Mio. Finanzschulden'],
        ['D', 'Salaltbar UG (haftungsbeschränkt)', 'UG (haftungsb.)', '11-Tage-Cash + Mietexplosion + § 15a InsO'],
    ]
    var_tbl = Table(var_data, colWidths=[1.2*cm, 5.8*cm, 4*cm, 6.5*cm])
    var_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), MITTELBLAU),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 8),
        ('BACKGROUND', (0,1), (0,1), FARBE_A),
        ('BACKGROUND', (0,2), (0,2), FARBE_B),
        ('BACKGROUND', (0,3), (0,3), FARBE_C),
        ('BACKGROUND', (0,4), (0,4), FARBE_D),
        ('TEXTCOLOR', (0,1), (0,-1), colors.white),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 8),
        ('ROWBACKGROUNDS', (1,1), (-1,-1), [colors.white, GRAU_HELL]),
        ('GRID', (0,0), (-1,-1), 0.3, GRAU_MID),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(var_tbl)
    story.append(Spacer(1, 0.6*cm))

    story.append(hr(DUNKELBLAU, 1))
    story.append(Spacer(1, 0.3*cm))

    meta = [
        ['Aktenkonvolut-Datum:', '22. Mai 2026'],
        ['Herausgeber/Federführung:', 'RA Dr. Tjark Reher-Bornholmsen'],
        ['Kanzlei:', 'Reher Wennstedt Restrukturierung PartmbB, Hamburg'],
        ['Anlass:', 'Vorbereitung Impulsvortrag — Restructuring Lounge Hamburg'],
        ['Veranstaltung:', 'WAYES Hamburg, 28. Mai 2026, 18:30 Uhr'],
        ['Status:', 'VERTRAULICH — Interne Verwendung / Ausbildungszwecke'],
        ['Klassifikation:', 'Fiktive Testmaterialien — kein realer Mandatsbezug'],
    ]
    meta_tbl = Table(meta, colWidths=[5*cm, 12.5*cm])
    meta_tbl.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.white, GRAU_HELL]),
        ('GRID', (0,0), (-1,-1), 0.2, GRAU_MID),
    ]))
    story.append(meta_tbl)
    story.append(Spacer(1, 1*cm))

    # Kanzlei-Logo
    for line in kanzlei_kopf_rw():
        story.append(line)

    story.append(PageBreak())

# ─── VORBEMERKUNG DES HERAUSGEBERS ────────────────────────────────────────────

def build_vorbemerkung(story):
    story.append(Paragraph("Vorbemerkung des Herausgebers", S['h1']))
    story.append(hr(DUNKELBLAU))
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph(
        "Das vorliegende Aktenkonvolut dient der Vorbereitung auf den Impulsvortrag "
        "\"Krisenfrüherkennung und § 1 StaRUG — Pflicht, nicht Kür\" bei der "
        "Restructuring Lounge Hamburg (WAYES, 28. Mai 2026). Es enthält vier fiktive "
        "Fallvarianten, die unterschiedliche Unternehmensgrößen, Rechtsformen und "
        "Krisenkonstellationen abbilden. Alle Personen, Unternehmen und Aktenzeichen "
        "sind frei erfunden; Ähnlichkeiten mit realen Personen oder Unternehmen "
        "sind nicht beabsichtigt und rein zufällig.", S['body']))

    story.append(Paragraph("I. Kernaussagen dieser Testakte", S['h2']))

    story.append(Paragraph(
        "<b>1. § 1 StaRUG ist Geschäftsführerpflicht — keine bloße Option.</b>",
        S['bold']))
    story.append(Paragraph(
        "Seit Inkrafttreten des StaRUG am 1. Januar 2021 trifft jeden Geschäftsleiter "
        "einer haftungsbeschränkten juristischen Person die gesetzliche Pflicht, "
        "kontinuierlich bestandsgefährdende Entwicklungen zu beobachten, zu erfassen "
        "und geeignete Gegenmaßnahmen einzuleiten. Dies gilt nicht nur für die GmbH "
        "(§ 43 Abs. 1 GmbHG) und die AG (§ 93 AktG), sondern gleichermaßen für die "
        "UG (haftungsbeschränkt), die SE und die gGmbH. Eine aktive Entscheidung "
        "\"kein StaRUG-Verfahren\" befreit den Geschäftsführer nicht von der "
        "Früherkennungspflicht nach § 1 StaRUG.", S['body']))

    story.append(Paragraph(
        "<b>2. Der 24-Monats-Horizont ist der neue Planungsstandard.</b>",
        S['bold']))
    story.append(Paragraph(
        "Die Rechtspraxis hat sich seit 2022 darauf eingespielt, dass eine "
        "ordnungsgemäße Liquiditätsplanung im Sinne des § 1 StaRUG einen rollierenden "
        "24-Monats-Horizont umfassen muss. Der IDW S 11 (Fortbestehensprognose) "
        "nennt einen 12-Monats-Horizont für die Prognose der Zahlungsfähigkeit; "
        "darüber hinaus verlangt die StaRUG-Praxis den erweiterten 24-Monats-Blick "
        "auf drohende Zahlungsunfähigkeit (§ 18 InsO). Ein 13-Wochen-Rollplan ersetzt "
        "die 24-Monats-Planung nicht — er ist komplementär, nicht substituierend. "
        "Variante A zeigt exemplarisch, wie eine gGmbH trotz hoher technischer "
        "Reputation durch fehlende kaufmännische Planung in die Krise schlittert.", S['body']))

    story.append(Paragraph(
        "<b>3. § 102 StaRUG zwingt rechts- und steuerberatende Berufe zur aktiven Warnung.</b>",
        S['bold']))
    story.append(Paragraph(
        "Rechtsanwälte, Steuerberater und Wirtschaftsprüfer, die Kenntnis von "
        "bestandsgefährdenden Tatsachen erlangen, haben den Mandanten nach § 102 StaRUG "
        "hierauf unverzüglich hinzuweisen. Die Warnpflicht gilt unabhängig davon, ob "
        "das eigentliche Mandatsverhältnis Restrukturierungsberatung umfasst. Insbesondere "
        "bei der Jahresabschlusserstellung, der Steuererklärungserstellung und der "
        "laufenden Finanzbuchhaltungsbegleitung entstehen regelmäßig Kenntnisse, die "
        "§ 102 StaRUG auslösen. Das Unterlassen des Hinweises begründet Haftungsrisiken "
        "des Beraters.", S['body']))

    story.append(Paragraph(
        "<b>4. Wer das Heft des Handelns verliert, verliert auch die StaRUG-Werkzeuge.</b>",
        S['bold']))
    story.append(Paragraph(
        "Das StaRUG bietet ein einzigartiges Arsenal: Stabilisierungsanordnung "
        "(§§ 49–59 StaRUG), Moratorium, Cross-Class-Cram-Down (§ 26 StaRUG), "
        "gerichtliche Planbestätigung. Alle diese Werkzeuge setzen voraus, dass der "
        "Schuldner noch handlungsfähig ist und die Zahlungsunfähigkeit nach § 17 InsO "
        "noch nicht eingetreten ist. Wer zu lange wartet, muss in das "
        "Insolvenzplanverfahren oder das Regelverfahren wechseln — mit erheblichem "
        "Kontroll- und Reputationsverlust. Variante D (Salaltbar UG) zeigt diesen "
        "Grenzfall exemplarisch.", S['body']))

    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("II. Aufbau des Konvoluts", S['h2']))
    aufbau = [
        ['Abschnitt', 'Inhalt', 'Seiten ca.'],
        ['Konvolut-Deckel', 'Aktendeckblatt + Variantenübersicht', '1'],
        ['Vorbemerkung', 'Lehrziele und Aufbaustruktur (dieser Abschnitt)', '3'],
        ['Vergleichstabelle', 'Alle vier Varianten auf einen Blick (Querformat)', '2'],
        ['Variante A', 'VEYRA AI Foundation gGmbH — Open-Source-KI, Frankfurt', '22–26'],
        ['Variante B', 'Herrenbluse & Zwirn Hartmannschmidt AG — Bamberg', '22–26'],
        ['Variante C', 'Nordfels Power Cells SE — Ellwangen', '22–26'],
        ['Variante D', 'Salaltbar UG (haftungsb.) — Berlin-Neukölln', '18–22'],
        ['Vorlagen-Annex', 'Standardmuster für alle Varianten (§ 102, Liquiplan, etc.)', '15'],
        ['Foliensatz-Anhang', 'Impulsvortrag Restructuring Lounge 28.05.2026', '8'],
        ['Stundenaufstellung', 'Kosten-Beispiel Reher Wennstedt', '2'],
    ]
    aufbau_tbl = Table(aufbau, colWidths=[4*cm, 9*cm, 2.5*cm])
    aufbau_tbl.setStyle(tbl_style_standard())
    story.append(aufbau_tbl)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("III. Hinweise zur Verwendung", S['h2']))
    story.append(Paragraph(
        "Diese Akte ist ausschließlich für Ausbildungs-, Schulungs- und "
        "Demonstrationszwecke bestimmt. Sie enthält keine realen Mandantendaten. "
        "Alle Fallkonstruktionen sind frei erfunden. Die verwendeten Aktenzeichen "
        "entsprechen dem formalen Format echter Amtsgerichtsregister (AG ... RES .../..., "
        "AG ... IN .../...), sind jedoch ausschließlich für diese Testakte vergeben "
        "und entfalten keine Rechtswirkung.", S['body']))

    story.append(Paragraph(
        "Die Akte darf nicht an Mandanten weitergegeben oder in echten "
        "Verfahren verwendet werden. Bei der Verwendung in Schulungsveranstaltungen "
        "ist der fiktive Charakter der Materialien stets deutlich zu machen.",
        S['body']))

    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph(
        "Hamburg, 22. Mai 2026",
        S['right']))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "RA Dr. Tjark Reher-Bornholmsen",
        ParagraphStyle('sig', fontName='Times-Italic', fontSize=11,
                       alignment=TA_RIGHT, textColor=DUNKELBLAU)
    ))
    story.append(Paragraph(
        "Reher Wennstedt Restrukturierung PartmbB, Hamburg",
        S['right']))
    story.append(PageBreak())

# ─── VERGLEICHSTABELLE (2 Seiten, simuliert Querformat mit breiten Daten) ─────

def build_vergleichstabelle(story):
    story.append(Paragraph("Vergleichstabelle der vier Fallvarianten", S['h1']))
    story.append(Paragraph(
        "Alle vier Varianten auf einen Blick — erstellt 22. Mai 2026",
        S['subtitle']))
    story.append(hr(DUNKELBLAU))
    story.append(Spacer(1, 0.3*cm))

    # Tabelle 1: Stammdaten
    story.append(Paragraph("1. Stammdaten und Unternehmensmerkmale", S['h2']))
    t1_data = [
        ['Kriterium', 'VARIANTE A\nVEYRA AI Foundation', 'VARIANTE B\nHartmannschmidt AG',
         'VARIANTE C\nNordfels Power Cells SE', 'VARIANTE D\nSalaltbar UG'],
        ['Rechtsform', 'gGmbH (gemeinn.)', 'AG (Open Market)', 'SE (börsennotiert)', 'UG (haftungsb.)'],
        ['Sitz', 'Frankfurt am Main', 'Bamberg', 'Ellwangen (Jagst)', 'Berlin-Neukölln'],
        ['Mitarbeiter', 'ca. 32 VZÄ', '720 MA', 'ca. 1.850 MA', '14 MA inkl. GF'],
        ['Umsatz p.a.', 'ca. EUR 4,2 Mio.\n(Zuwendungen+Förder.)', 'ca. EUR 182 Mio.', 'ca. EUR 340 Mio.', 'ca. EUR 680.000'],
        ['Stammkapital', 'EUR 25.000', 'EUR 6,5 Mio. (Grundkap.)', 'EUR 12 Mio. (Grundkap.)', 'EUR 1 (UG-Mindest)'],
        ['Finanzschulden', 'Keine Bankschulden;\nCloud-Verbindl. ca.\nEUR 1,4 Mio./Jahr', 'Anleihe EUR 65 Mio.\n+ Konsortialk. EUR 28 Mio.', 'Anleihe EUR 250 Mio.\n+ Konsortialk. EUR 300 Mio.', 'Lieferantenschulden\nca. EUR 42.000;\nMietrückstand ca.\nEUR 18.000'],
        ['Eigentümerstruktur', 'Gemeinnützig; kein\nGewinnaussch.;\nSpenderbasis', 'Hartmannschmidt\nHolding KG: 55%;\nStreubesitz: 45%', 'Vossbergen Family\nOffice: 41%;\nStreubesitz: 38%;\nWestshore: 11%;\nSaalfeld: 10%', 'Alleingesellschafter:\nT.-Y. Çelebi-Drebenstedt'],
    ]
    t1 = Table(t1_data, colWidths=[3.5*cm, 3.4*cm, 3.4*cm, 3.4*cm, 3.3*cm])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DUNKELBLAU),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 7.5),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 7.5),
        ('BACKGROUND', (1,1), (1,-1), colors.HexColor("#EEF5EE")),
        ('BACKGROUND', (2,1), (2,-1), colors.HexColor("#EEF0F8")),
        ('BACKGROUND', (3,1), (3,-1), colors.HexColor("#FAEAEA")),
        ('BACKGROUND', (4,1), (4,-1), colors.HexColor("#FFF4EA")),
        ('GRID', (0,0), (-1,-1), 0.3, GRAU_MID),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t1)
    story.append(Spacer(1, 0.4*cm))

    # Tabelle 2: Krisenparameter
    story.append(Paragraph("2. Krisenparameter und StaRUG-Instrumente", S['h2']))
    t2_data = [
        ['Kriterium', 'VARIANTE A', 'VARIANTE B', 'VARIANTE C', 'VARIANTE D'],
        ['Krisenstadium', 'Drohende ZU\n(§ 18 InsO)\nab Monat 17', 'Drohende ZU\n+ Covenant-\nBruch', 'Drohende ZU +\nüberschuldungs-\nnah', 'Grenze ZU\n§ 17 InsO;\nDrohende\n§ 15a InsO-Pfl.'],
        ['Krisenursache', 'Spendeneinbruch\n+ EU-Förder-\nDelay 9 Monate\n+ GPU-Kosten', 'Strukturelle\nMargenerosion\n(China-Import)\n+ Anleihe-Fälligkeit', 'Großkunden-\nwechsel +\nKapaziäts-\nüberhang', 'Energiekosten-\nexplosion +\nMietsteigerung\n+ Lieferantensch.'],
        ['Aktenzeichen', 'AG Frankfurt\n810 RES 14/26', 'AG Bamberg\n53 RES 7/26', 'AG Stuttgart\n14 RES 22/26', 'AG Charlottenburg\n36 IN 412/26'],
        ['StaRUG-Tool', 'Restruktur.-\nplan + Stundung\n+ § 102-Warn-\nschreiben', 'Cross-Class-\nCram-Down\n§ 26 StaRUG\n+ Anleihe-Restr.', 'Stabilisierungs-\nanordnung\n§§ 49-59 +\nCram-Down + KE/KH', 'Nur § 102\nWarnschreiben;\nkein StaRUG-\nPlan (zu klein)'],
        ['Berater', 'RA Dr. Reher-\nBornholmsen\n(Reher Wennstedt)', 'Dr. Reher-\nBornholmsen +\nDr. Vellmer-Lutz', 'Reher Wennstedt\n+ Brentwood\nHartfeld mbB', 'RAin Wandel-\nmoser; Verweis\nan Reher\nWennstedt'],
        ['IDW-Standard', '(kein Gutachten\ngefordert;\nIntern-Check)', 'IDW S 11 +\nIDW S 6\n(Kurzfassung)', 'IDW S 11\n+ Schlechter-\nstellungs-Gutachten', '(kein IDW-\nGutachten;\nKlein-Fall)'],
        ['Besonderheit', 'Gemeinnützige\ngGmbH;\nopen-source-\nKI-Forschung', 'Börsennotierte\nAG; HV-Vor-\nbereitung;\nFamilien-Anker', 'Aktivist-HF\nWestshore;\nRB-Bestellung;\nAufsichtsrat', 'EUR 1 Stamm-\nkap.; 14 MA;\npanik-E-Mail\nMandant'],
    ]
    t2 = Table(t2_data, colWidths=[3.5*cm, 3.4*cm, 3.4*cm, 3.4*cm, 3.3*cm])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), MITTELBLAU),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 7.5),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 7.5),
        ('BACKGROUND', (1,1), (1,-1), colors.HexColor("#EEF5EE")),
        ('BACKGROUND', (2,1), (2,-1), colors.HexColor("#EEF0F8")),
        ('BACKGROUND', (3,1), (3,-1), colors.HexColor("#FAEAEA")),
        ('BACKGROUND', (4,1), (4,-1), colors.HexColor("#FFF4EA")),
        ('GRID', (0,0), (-1,-1), 0.3, GRAU_MID),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t2)
    story.append(PageBreak())

# ─── TRENNBLATT ───────────────────────────────────────────────────────────────

def build_trennblatt(story, variante, titel, untertitel, az, farbe):
    story.append(Spacer(1, 4*cm))
    # Farbiger Block mit Varianten-Code
    data = [[
        Paragraph(
            f"VARIANTE {variante}",
            ParagraphStyle('vcode', fontName='Helvetica-Bold', fontSize=36,
                           alignment=TA_CENTER, textColor=colors.white, leading=44)
        )
    ]]
    tbl = Table(data, colWidths=[17*cm], rowHeights=[3.5*cm])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), farbe),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph(titel, ParagraphStyle('vtit', fontName='Helvetica-Bold',
                           fontSize=16, alignment=TA_CENTER, textColor=farbe, leading=22)))
    story.append(Paragraph(untertitel, ParagraphStyle('vsubt', fontName='Helvetica',
                           fontSize=12, alignment=TA_CENTER, textColor=GRAU_DUNKEL,
                           leading=18, spaceAfter=10)))
    story.append(hr(farbe, 2))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(f"Aktenzeichen: <b>{az}</b>",
                           ParagraphStyle('vaz', fontName='Helvetica-Bold', fontSize=11,
                                          alignment=TA_CENTER, textColor=farbe)))
    story.append(PageBreak())

# ─────────────────────────────────────────────────────────────────────────────
# VARIANTE A: VEYRA AI Foundation gGmbH
# ─────────────────────────────────────────────────────────────────────────────

def build_variante_a(story):
    AZ = "AG Frankfurt 810 RES 14/26"
    MANDANT = "VEYRA AI Foundation gGmbH"
    BETREFF = "Krisenfrüherkennung § 1 StaRUG"

    # 1. Gesellschaftsprofil
    story.append(Paragraph("A.1 Gesellschaftsprofil — VEYRA AI Foundation gGmbH", S['h1']))
    story.append(hr(FARBE_A))

    for line in fax_block([
        f"FAX-KOPIE  |  Reher Wennstedt Restrukturierung PartmbB",
        f"Datum: 04. Mai 2026  |  An: Akte Az. {AZ}",
        f"Mandant: {MANDANT}, Frankfurt am Main",
        f"Betreff: Ersterfassung Gesellschaftsprofil (INTERN)",
    ]):
        story.append(line)
    story.append(Spacer(1, 0.3*cm))

    profil = [
        ['Firma:', 'VEYRA AI Foundation gGmbH'],
        ['Sitz:', 'Eschersheimer Landstraße 42, 60322 Frankfurt am Main'],
        ['Handelsregister:', 'HRB 118 847 — Amtsgericht Frankfurt am Main'],
        ['Rechtsform:', 'Gesellschaft mit beschränkter Haftung (gemeinnützig, § 5 Abs. 1 Nr. 9 KStG)'],
        ['Gründungsjahr:', '2018'],
        ['Stammkapital:', 'EUR 25.000,00 (voll eingezahlt)'],
        ['Geschäftsjahr:', '1. Januar bis 31. Dezember'],
        ['Gemeinnützigkeitszweck:', 'Förderung von Wissenschaft und Forschung, speziell Open-Source-KI'],
        ['Steuer-IdNr.:', '045/227/41822 (FA Frankfurt am Main III)'],
        ['Geschäftsführerin:', 'Dr. Mira Hellinghaus-Karpov (alleinvertretungsberechtigt)'],
        ['Aufsichtsrat:', '5 Personen (Satzungspflicht ab 500 Spendersumme EUR 1 Mio. p.a.)'],
        ['Mitarbeiter:', 'ca. 32 VZÄ (davon 24 Forschende, 8 Admin/Infra)'],
        ['Jahreseinnahmen 2025:', 'EUR 4.240.000 (Spenden EUR 2,8 Mio. + EU-Förderung EUR 1,1 Mio. + Sonstiges EUR 340.000)'],
        ['Hauptkreditoren:', 'Nordlicht Cloud GmbH (GPU-Infrastruktur), EUR 118.000/Monat'],
    ]
    ptbl = Table(profil, colWidths=[4.5*cm, 13*cm])
    ptbl.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.white, GRAU_HELL]),
        ('GRID', (0,0), (-1,-1), 0.2, GRAU_MID),
    ]))
    story.append(ptbl)
    story.append(Spacer(1, 0.4*cm))

    story.append(Paragraph("Aufsichtsrat (Stand: 01.01.2026):", S['h3']))
    ar = [
        ['Nr.', 'Name', 'Funktion', 'Hintergrund'],
        ['1', 'Prof. Dr. Heinrich Osterwald-Bonn', 'Vorsitzender', 'KI-Forscher, TU Darmstadt'],
        ['2', 'Dr. Susanne Larrousse-Fiedler', 'Stellv. Vorsitzende', 'Informatikerin, DFKI Saarbrücken'],
        ['3', 'Dipl.-Math. Rolf Söhnchen', 'Mitglied', 'Mathematician, ex-DeepMind (fiktiv)'],
        ['4', 'RA Petra Wemding-Schröder', 'Mitglied', 'Rechtsanwältin, Vereinsrecht'],
        ['5', 'N.N.', 'Mitglied', '(Nachbesetzung offen seit Feb. 2026)'],
    ]
    ar_tbl = Table(ar, colWidths=[0.8*cm, 5.5*cm, 4*cm, 7.2*cm])
    ar_tbl.setStyle(tbl_style_standard())
    story.append(ar_tbl)
    story.append(PageBreak())

    # 2. Vorstandsprotokoll (Aufsichtsratsprotokoll-Format)
    story.append(Paragraph("A.2 Protokoll Krisenklausur des Aufsichtsrats — 7. April 2026", S['h1']))
    story.append(hr(FARBE_A))
    story.append(Spacer(1, 0.2*cm))

    for line in kanzlei_kopf_rw():
        story.append(line)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph(
        "VEYRA AI Foundation gGmbH — Aufsichtsrats-Sonderklausur", S['h2']))
    story.append(Paragraph(
        "Datum: 7. April 2026, 09:30–17:00 Uhr | Ort: Eschersheimer Landstraße 42, Frankfurt/M.",
        S['body_left']))
    story.append(Paragraph(
        "Anwesend: Osterwald-Bonn (Vors.), Larrousse-Fiedler, Söhnchen, Wemding-Schröder; "
        "ferner: Dr. Hellinghaus-Karpov (GF), Dr. Reher-Bornholmsen (Kanzlei, als Gast)",
        S['body_left']))
    story.append(hr())
    story.append(Spacer(1, 0.2*cm))

    tagesordnung = [
        ['TOP', 'Gegenstand'],
        ['1', 'Bericht GF: Liquiditätslage Q1 2026 und Prognose'],
        ['2', 'Spendeneinbruch Januar–März 2026: Ursachenanalyse'],
        ['3', 'EU-Förderprojekt „OPENSENS": Verzögerung der Auszahlung'],
        ['4', 'Nordlicht Cloud GmbH: Vertragsanpassung und Stundungsverhandlung'],
        ['5', 'Früherkennungspflicht § 1 StaRUG: Rechtliche Einordnung durch RA Dr. Reher-Bornholmsen'],
        ['6', 'Beschlüsse und nächste Schritte'],
    ]
    to_tbl = Table(tagesordnung, colWidths=[1.2*cm, 16.3*cm])
    to_tbl.setStyle(tbl_style_standard())
    story.append(to_tbl)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("Zu TOP 1 — Bericht GF Liquiditätslage:", S['h3']))
    story.append(Paragraph(
        "Frau Dr. Hellinghaus-Karpov erläutert, dass der Kassenbestand der Gesellschaft "
        "per 31. März 2026 EUR 830.000 betrug (Vorjahr 31.03.2025: EUR 2,1 Mio.). "
        "Die monatliche Liquiditätsrate sei negativ: Im Durchschnitt Q1 2026 "
        "Abfluss von EUR 210.000 netto. Bei gleichbleibendem Verlauf wäre die Zahlungs-"
        "fähigkeit ca. Monat 17 (August 2027) erschöpft. Ohne Gegenmaßnahmen drohe "
        "drohende Zahlungsunfähigkeit i.S.v. § 18 InsO ab Monat 14 (Mai 2027).",
        S['body']))

    story.append(Paragraph("Zu TOP 2 — Spendeneinbruch:", S['h3']))
    story.append(Paragraph(
        "Der Rückgang der Spendeneinnahmen betrug Q1 2026 gegenüber Q1 2025 EUR –640.000 "
        "(-34%). Ursachen: (a) Medienbericht über KI-Governance-Kontroverse in der "
        "Community (Dezember 2025); (b) Wegfall des Großspenders \"SilverFox Ventures\" "
        "(EUR 350.000/Jahr — Ausstieg erklärt ohne Begründung, Januar 2026); "
        "(c) allgemeine Spendenrezession im Non-Profit-Sektor. Larrousse-Fiedler "
        "kritisiert, dass kein Frühwarnsystem für Spendenentwicklung existiert.",
        S['body']))

    story.append(Paragraph("Zu TOP 3 — EU-Förderprojekt OPENSENS:", S['h3']))
    story.append(Paragraph(
        "Das Förderprojekt \"OPENSENS\" (EU Horizon Europe, Fördersumme EUR 1.100.000) "
        "hat seine Auszahlungsplanung um ca. 9 Monate verschoben. Ursprünglich war "
        "Tranche 1 (EUR 550.000) für Q2 2026 geplant; die EU-Verwaltungsbehörde hat "
        "mitgeteilt, der Bewilligungsbescheid könne frühestens Q4 2026/Q1 2027 erwartet "
        "werden. Söhnchen fragt, ob ein Vorfinanzierungs-Darlehen möglich sei; "
        "GF verneint (keine Sicherheiten vorhanden).",
        S['body']))

    story.append(Paragraph("Zu TOP 5 — § 1 StaRUG (Einführung Dr. Reher-Bornholmsen):", S['h3']))
    story.append(Paragraph(
        "RA Dr. Reher-Bornholmsen erläutert, dass § 1 StaRUG die Geschäftsführerin "
        "verpflichtet, ein \"geeignetes Überwachungssystem\" für bestandsgefährdende "
        "Entwicklungen zu implementieren. Diese Pflicht gilt ausdrücklich auch für "
        "gemeinnützige GmbHs. Der 24-Monats-Liquiditätshorizont sei der aktuelle "
        "Praxisstandard. Er empfiehlt, unverzüglich einen formalen Restrukturierungs-"
        "antrag nach § 31 StaRUG beim AG Frankfurt zu stellen, um den Verhandlungs-"
        "rahmen zu sichern und ggf. eine Stabilisierungsanordnung beantragen zu können.",
        S['body']))

    story.append(Paragraph("Beschlüsse:", S['h3']))
    beschl = [
        ['Nr.', 'Beschluss', 'Stimmverhältnis'],
        ['A/2026/01', 'Beauftragung Reher Wennstedt PartmbB mit StaRUG-Begleitung', 'Einstimmig'],
        ['A/2026/02', 'Anzeige Restrukturierungssache gem. § 31 StaRUG beim AG Frankfurt', 'Einstimmig'],
        ['A/2026/03', 'Sofortige Aufnahme Stundungsverhandlung mit Nordlicht Cloud GmbH', 'Einstimmig'],
        ['A/2026/04', 'GF erstellt 24-Monats-Liquiditätsplan bis 30. April 2026', 'Einstimmig'],
        ['A/2026/05', 'Überarbeitung Spendenstrategie bis 31. Mai 2026', 'Einstimmig'],
    ]
    b_tbl = Table(beschl, colWidths=[2.5*cm, 11*cm, 4*cm])
    b_tbl.setStyle(tbl_style_standard())
    story.append(b_tbl)
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("Unterzeichnet: Prof. Dr. Osterwald-Bonn (Vors. AR), Dr. Hellinghaus-Karpov (GF)", S['small']))
    story.append(PageBreak())

    # 3. 24-Monats-Liquiplan
    story.append(Paragraph("A.3 24-Monats-Liquiditätsplan — VEYRA AI Foundation gGmbH", S['h1']))
    story.append(Paragraph("Stand: 30. April 2026 | Erstellerin: Dr. Mira Hellinghaus-Karpov", S['subtitle']))
    story.append(hr(FARBE_A))
    story.append(Spacer(1, 0.2*cm))

    # Wochen W1-W13 (komprimiert)
    story.append(Paragraph("Teil 1: Kurzfristplan Wochen W1–W13 (Mai–Juli 2026)", S['h2']))
    w_header = ['Woche', 'KW', 'Anfangsbestand', 'Einzahlungen', 'Auszahlungen', 'Saldo', 'Endbestand', 'Ampel']
    w_rows = [
        ['W1', 'KW 19', '830.000', '48.000', '320.000', '-272.000', '558.000', 'GELB'],
        ['W2', 'KW 20', '558.000', '22.000', '185.000', '-163.000', '395.000', 'GELB'],
        ['W3', 'KW 21', '395.000', '95.000', '185.000', '-90.000', '305.000', 'ROT'],
        ['W4', 'KW 22', '305.000', '18.000', '195.000', '-177.000', '128.000', 'ROT'],
        ['W5', 'KW 23', '128.000', '210.000', '180.000', '+30.000', '158.000', 'GELB'],
        ['W6', 'KW 24', '158.000', '15.000', '185.000', '-170.000', '-12.000', 'ROT!'],
        ['W7', 'KW 25', '-12.000', '380.000', '180.000', '+200.000', '188.000', 'GELB'],
        ['W8', 'KW 26', '188.000', '12.000', '190.000', '-178.000', '10.000', 'ROT!'],
        ['W9', 'KW 27', '10.000', '15.000', '185.000', '-170.000', '-160.000', 'ROT!!'],
        ['W10', 'KW 28', '-160.000', '420.000', '180.000', '+240.000', '80.000', 'ROT'],
        ['W11', 'KW 29', '80.000', '12.000', '185.000', '-173.000', '-93.000', 'ROT!!'],
        ['W12', 'KW 30', '-93.000', '15.000', '185.000', '-170.000', '-263.000', 'ROT!!'],
        ['W13', 'KW 31', '-263.000', '280.000', '180.000', '+100.000', '-163.000', 'ROT!!'],
    ]
    w_data = [w_header] + w_rows
    # Spaltenbreiten angepasst
    w_tbl = Table(w_data, colWidths=[1*cm, 1.2*cm, 2.4*cm, 2.4*cm, 2.4*cm, 2.2*cm, 2.4*cm, 1.5*cm])
    w_style = tbl_style_zahlen()
    # Ampel-Einfärbung
    for i, row in enumerate(w_rows, 1):
        ampel = row[-1]
        if '!!' in ampel:
            w_style.add('BACKGROUND', (7,i), (7,i), colors.HexColor("#FFCCCC"))
            w_style.add('TEXTCOLOR', (7,i), (7,i), ROT)
        elif 'ROT' in ampel:
            w_style.add('BACKGROUND', (7,i), (7,i), colors.HexColor("#FFE0E0"))
        elif 'GELB' in ampel:
            w_style.add('BACKGROUND', (7,i), (7,i), colors.HexColor("#FFFACC"))
        # Negative Endbestände rot markieren
        if row[6].startswith('-'):
            w_style.add('TEXTCOLOR', (6,i), (6,i), ROT)
            w_style.add('FONTNAME', (6,i), (6,i), 'Helvetica-Bold')
    w_tbl.setStyle(w_style)
    story.append(w_tbl)
    story.append(Paragraph("Alle Angaben in EUR. Spendeneingänge unregelmäßig, daher hohe Volatilität.", S['footnote']))
    story.append(Spacer(1, 0.4*cm))

    # Monatliche Übersicht M4-M24
    story.append(Paragraph("Teil 2: Monatliche Übersicht M4–M24 (August 2026 – April 2028)", S['h2']))
    m_header = ['Monat', 'Datum', 'Anfangsb.', 'Spenden', 'EU-Förder.', 'Sonstige', 'Personal', 'GPU/Cloud', 'Sonstige Ausg.', 'Netto', 'Endbestand']
    m_rows_base = [
        ['M4', 'Aug 26', '-163.000', '220.000', '0', '28.000', '180.000', '118.000', '45.000', '-95.000', '-258.000'],
        ['M5', 'Sep 26', '-258.000', '250.000', '0', '28.000', '180.000', '118.000', '45.000', '-65.000', '-323.000'],
        ['M6', 'Okt 26', '-323.000', '280.000', '550.000', '28.000', '180.000', '118.000', '45.000', '+515.000', '192.000'],
        ['M7', 'Nov 26', '192.000', '210.000', '0', '28.000', '180.000', '118.000', '45.000', '-105.000', '87.000'],
        ['M8', 'Dez 26', '87.000', '320.000', '0', '28.000', '180.000', '118.000', '45.000', '+5.000', '92.000'],
        ['M9', 'Jan 27', '92.000', '180.000', '0', '25.000', '180.000', '118.000', '45.000', '-138.000', '-46.000'],
        ['M10', 'Feb 27', '-46.000', '190.000', '0', '25.000', '180.000', '118.000', '45.000', '-128.000', '-174.000'],
        ['M11', 'Mrz 27', '-174.000', '200.000', '0', '25.000', '180.000', '118.000', '45.000', '-118.000', '-292.000'],
        ['M12', 'Apr 27', '-292.000', '210.000', '550.000', '25.000', '180.000', '118.000', '45.000', '+442.000', '150.000'],
        ['M13', 'Mai 27', '150.000', '185.000', '0', '25.000', '180.000', '118.000', '45.000', '-133.000', '17.000'],
        ['M14', 'Jun 27', '17.000', '170.000', '0', '25.000', '180.000', '118.000', '45.000', '-148.000', '-131.000'],
        ['M15', 'Jul 27', '-131.000', '160.000', '0', '25.000', '180.000', '118.000', '45.000', '-158.000', '-289.000'],
        ['M16', 'Aug 27', '-289.000', '155.000', '0', '25.000', '180.000', '118.000', '45.000', '-163.000', '-452.000'],
        ['M17', 'Sep 27', '-452.000', '150.000', '0', '25.000', '180.000', '118.000', '45.000', '-168.000', '-620.000'],
        ['M18', 'Okt 27', '-620.000', '160.000', '550.000', '25.000', '180.000', '118.000', '45.000', '+392.000', '-228.000'],
        ['M19', 'Nov 27', '-228.000', '170.000', '0', '25.000', '180.000', '100.000', '40.000', '-125.000', '-353.000'],
        ['M20', 'Dez 27', '-353.000', '280.000', '0', '25.000', '180.000', '100.000', '40.000', '-15.000', '-368.000'],
        ['M21', 'Jan 28', '-368.000', '160.000', '0', '22.000', '160.000', '80.000', '35.000', '-93.000', '-461.000'],
        ['M22', 'Feb 28', '-461.000', '160.000', '0', '22.000', '160.000', '80.000', '35.000', '-93.000', '-554.000'],
        ['M23', 'Mrz 28', '-554.000', '160.000', '0', '22.000', '160.000', '80.000', '35.000', '-93.000', '-647.000'],
        ['M24', 'Apr 28', '-647.000', '160.000', '550.000', '22.000', '160.000', '80.000', '35.000', '+457.000', '-190.000'],
    ]
    m_data = [m_header] + m_rows_base
    m_tbl = Table(m_data, colWidths=[1*cm, 1.3*cm, 1.8*cm, 1.7*cm, 1.7*cm, 1.5*cm,
                                      1.7*cm, 1.8*cm, 1.8*cm, 1.9*cm, 2.3*cm])
    m_style = tbl_style_zahlen()
    for i, row in enumerate(m_rows_base, 1):
        if row[-1].startswith('-'):
            m_style.add('TEXTCOLOR', (10,i), (10,i), ROT)
            m_style.add('FONTNAME', (10,i), (10,i), 'Helvetica-Bold')
    m_tbl.setStyle(m_style)
    story.append(m_tbl)
    story.append(Paragraph(
        "Annahmen: Spendeneinbruch Szenario BASE (-20% ggü. 2025); EU-Förderung OPENSENS "
        "Tranche 1 (EUR 550.000) in M6/Okt 2026, Tranche 2 in M12/Apr 2027, "
        "Tranche 3 in M18/Okt 2027, Tranche 4 in M24/Apr 2028. "
        "GPU-Stundung ab M19: Nordlicht Cloud GmbH akzeptiert 15% Reduktion.",
        S['footnote']))
    story.append(PageBreak())

    # 4. Stress-Szenarien
    story.append(Paragraph("A.4 Stress-Szenarien", S['h1']))
    story.append(hr(FARBE_A))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("Szenario I: Spendeneinbruch 40%", S['h2']))
    story.append(Paragraph(
        "In diesem Szenario werden die Spendeneinnahmen gegenüber 2025 um 40% "
        "(statt 20% im Basis-Szenario) reduziert. Die Einnahmen sinken von "
        "EUR 2.800.000 (2025) auf EUR 1.680.000 p.a. (2026).",
        S['body']))
    sz1 = [
        ['Parameter', 'Basis-Szenario', 'Stress-Szenario I (Spenden -40%)'],
        ['Spenden p.a. (2026)', 'EUR 2.240.000 (-20%)', 'EUR 1.680.000 (-40%)'],
        ['Spenden p.a. (2027)', 'EUR 2.100.000', 'EUR 1.540.000'],
        ['Monat Drohende ZU (§ 18 InsO)', 'M14 (Jun 2027)', 'M8 (Dez 2026)'],
        ['Liquiditätsminimum', '-EUR 647.000 (M24)', '-EUR 1.120.000 (M15)'],
        ['Kumulierter Fehlbetrag M1-M24', '-EUR 420.000', '-EUR 890.000'],
        ['Handlungsbedarf', 'Erheblich', 'KRITISCH — sofortiger Notfallplan'],
    ]
    sz1_tbl = Table(sz1, colWidths=[6*cm, 5.5*cm, 6*cm])
    sz1_tbl.setStyle(tbl_style_standard())
    story.append(sz1_tbl)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("Szenario II: Förder-Delay 12 Monate (OPENSENS)", S['h2']))
    story.append(Paragraph(
        "In diesem Szenario verschiebt sich die EU-Fördermittel-Auszahlung OPENSENS "
        "um weitere 12 Monate (kumuliert 21 Monate Verzögerung gegenüber ursprünglichem Plan).",
        S['body']))
    sz2 = [
        ['Parameter', 'Basis-Szenario', 'Stress-Szenario II (Delay +12M)'],
        ['OPENSENS Tranche 1 (EUR 550.000)', 'Okt 2026 (M6)', 'Okt 2027 (M18)'],
        ['OPENSENS Tranche 2 (EUR 550.000)', 'Apr 2027 (M12)', 'Apr 2028 (M24)'],
        ['Monat Drohende ZU (§ 18 InsO)', 'M14 (Jun 2027)', 'M4 (Aug 2026)'],
        ['Sofortiger Liquiditätsbedarf', 'Ca. EUR 200.000', 'Ca. EUR 800.000'],
        ['Lösung', 'Stundung + Spendenoffensive', 'Überbrückungskredit / Notverkauf Assets / Liquidation'],
    ]
    sz2_tbl = Table(sz2, colWidths=[6*cm, 5.5*cm, 6*cm])
    sz2_tbl.setStyle(tbl_style_standard())
    story.append(sz2_tbl)
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "<b>Fazit:</b> Beide Stress-Szenarien zeigen, dass die finanzielle Stabilität der "
        "VEYRA AI Foundation gGmbH extrem sensitiv auf externe Faktoren reagiert. "
        "Ein robustes Frühwarnsystem nach § 1 StaRUG ist unverzüglich zu implementieren.",
        S['warn']))
    story.append(PageBreak())

    # 5. § 102 StaRUG Warnschreiben
    story.append(Paragraph("A.5 Warnschreiben nach § 102 StaRUG", S['h1']))
    story.append(hr(FARBE_A))
    story.append(Spacer(1, 0.2*cm))

    for line in kanzlei_kopf_rw():
        story.append(line)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("<b>EINSCHREIBEN MIT RÜCKSCHEIN / VERTRAULICH</b>", S['bold']))
    story.append(Spacer(1, 0.2*cm))

    empf = [
        ['An:', 'Frau Dr. Mira Hellinghaus-Karpov'],
        ['', 'Geschäftsführerin der VEYRA AI Foundation gGmbH'],
        ['', 'Eschersheimer Landstraße 42'],
        ['', '60322 Frankfurt am Main'],
        ['Datum:', 'Hamburg, 8. Mai 2026'],
        ['Unser Zeichen:', 'RB/DP-2026-VEYRA-RES'],
        ['Betreff:', 'Früherkennungshinweis nach § 102 StaRUG — VERTRAULICH'],
    ]
    empf_tbl = Table(empf, colWidths=[2.5*cm, 15*cm])
    empf_tbl.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(empf_tbl)
    story.append(hr())
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("Sehr geehrte Frau Dr. Hellinghaus-Karpov,", S['body_left']))
    story.append(Spacer(1, 0.15*cm))

    story.append(Paragraph(
        "wir beziehen uns auf das Aktenzeichen AG Frankfurt 810 RES 14/26 sowie auf "
        "unsere bisherige Beratung und das Protokoll der Aufsichtsratssitzung vom "
        "7. April 2026. Im Rahmen unserer Tätigkeit haben wir Kenntnis von Tatsachen "
        "erlangt, die nach unserer Einschätzung eine bestandsgefährdende Entwicklung "
        "der VEYRA AI Foundation gGmbH im Sinne des § 1 StaRUG begründen.", S['body']))

    story.append(Paragraph("<b>I. Rechtliche Grundlage und Hinweispflicht</b>", S['h3']))
    story.append(Paragraph(
        "§ 102 des Gesetzes über den Stabilisierungs- und Restrukturierungsrahmen für "
        "Unternehmen (StaRUG) verpflichtet Berater und Beraterinnen, die im Rahmen "
        "ihrer beruflichen Tätigkeit von bestandsgefährdenden Entwicklungen Kenntnis "
        "erlangen, den Mandanten unverzüglich hierauf hinzuweisen. Diese Hinweispflicht "
        "gilt gegenüber der Geschäftsleitung unabhängig davon, ob das eigentliche "
        "Mandatsverhältnis Restrukturierungsberatung umfasst.", S['body']))

    story.append(Paragraph("<b>II. Festgestellte bestandsgefährdende Entwicklungen</b>", S['h3']))
    story.append(Paragraph(
        "Auf Grundlage der uns vorliegenden Unterlagen (Kontoauszüge, BWA, "
        "13-Wochen-Plan) stellen wir folgende Risikofaktoren fest:", S['body']))

    risiken = [
        ['Nr.', 'Risikofaktor', 'Bewertung'],
        ['1', 'Spendeneinbruch Q1 2026: -34% ggü. Vorjahr', 'KRITISCH'],
        ['2', 'Verzögerung EU-Förderung OPENSENS: ca. 9 Monate', 'KRITISCH'],
        ['3', 'Monatlicher Netto-Liquiditätsabfluss EUR -210.000', 'KRITISCH'],
        ['4', 'Kassenbestand 31.03.2026: EUR 830.000 (reicht ca. 4 Monate ohne Gegenmassnahmen)', 'KRITISCH'],
        ['5', 'Drohende Zahlungsunfähigkeit § 18 InsO: prognostiziert ab M14 (Jun 2027)', 'ERHEBLICH'],
        ['6', 'Keine formale Liquiditätsplanung mit 24-Monats-Horizont vorhanden', 'ERHEBLICH'],
        ['7', 'Kein institutionalisiertes Krisenfrühwarnsystem nach § 1 StaRUG', 'ERHEBLICH'],
    ]
    r_tbl = Table(risiken, colWidths=[0.8*cm, 12.5*cm, 4.2*cm])
    r_style = tbl_style_standard()
    for i in range(1, 5):
        r_style.add('BACKGROUND', (2,i), (2,i), colors.HexColor("#FFE0E0"))
        r_style.add('TEXTCOLOR', (2,i), (2,i), ROT)
        r_style.add('FONTNAME', (2,i), (2,i), 'Helvetica-Bold')
    r_tbl.setStyle(r_style)
    story.append(r_tbl)
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("<b>III. Empfohlene Sofortmaßnahmen</b>", S['h3']))
    story.append(Paragraph("Wir empfehlen Ihnen dringend folgende Schritte:", S['body']))
    massnahmen = [
        "1. Unverzügliche Erstellung eines 24-Monats-Liquiditätsplans (bis spätestens 30. April 2026 — "
        "Beschluss AR vom 7. April 2026 wird erneut eingefordert).",
        "2. Sofortige Aufnahme von Stundungsverhandlungen mit der Nordlicht Cloud GmbH "
        "(monatliche GPU-Kosten EUR 118.000 sind der größte variable Posten).",
        "3. Implementierung eines formalen Krisenfrühwarnsystems mit monatlichem Reporting "
        "an den Aufsichtsrat.",
        "4. Kontaktaufnahme mit EU-Förderverwalter bezüglich Vorfinanzierungsmöglichkeiten "
        "oder Abschlagszahlungen OPENSENS.",
        "5. Prüfung personalwirtschaftlicher Maßnahmen (Kurzarbeit, befristete Nicht-"
        "Verlängerung von Verträgen).",
    ]
    for m in massnahmen:
        story.append(Paragraph(m, S['indent']))

    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "<b>IV. Hinweis auf Haftungsrisiken</b>",
        S['h3']))
    story.append(Paragraph(
        "Wir weisen darauf hin, dass ein Unterlassen der Krisenfrüherkennung und "
        "ein verspäteter Insolvenzantrag nach § 15a InsO zu einer persönlichen Haftung "
        "der Geschäftsführerin nach § 15b InsO führen kann. Die GmbH-rechtliche "
        "Haftung nach § 43 Abs. 2 GmbHG bleibt daneben bestehen.",
        S['body']))

    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph("Mit freundlichen kollegialen Grüßen", S['body_left']))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph(
        "RA Dr. Tjark Reher-Bornholmsen",
        ParagraphStyle('sig2', fontName='Times-Italic', fontSize=11,
                       textColor=DUNKELBLAU)
    ))
    story.append(Paragraph(
        "Reher Wennstedt Restrukturierung PartmbB",
        S['small']))
    story.append(Spacer(1, 0.5*cm))

    # Empfangsbestätigung
    story.append(hr(FARBE_A))
    story.append(Paragraph(
        "<b>EMPFANGSBESTÄTIGUNG</b> (bitte unterschrieben zurücksenden)",
        S['bold']))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "Ich, Dr. Mira Hellinghaus-Karpov, Geschäftsführerin der VEYRA AI Foundation gGmbH, "
        "bestätige den Empfang des Warnschreibens nach § 102 StaRUG vom 8. Mai 2026 "
        "und nehme zur Kenntnis, dass die dargelegten Risikofaktoren einer sofortigen "
        "Prüfung und Handlung bedürfen.",
        S['body']))
    story.append(Spacer(1, 0.8*cm))
    story.append(Paragraph(
        "Frankfurt, den ________________     _________________________________",
        S['body_left']))
    story.append(Paragraph(
        "                                    Dr. Mira Hellinghaus-Karpov",
        S['small']))
    story.append(PageBreak())

    # 6. Restrukturierungsplan-Entwurf
    story.append(Paragraph("A.6 Restrukturierungsplan-Entwurf (Zusammenfassung)", S['h1']))
    story.append(hr(FARBE_A))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "Im Folgenden ist der Entwurf des Restrukturierungsplans nach §§ 2 ff. StaRUG "
        "für die VEYRA AI Foundation gGmbH dargestellt (Kurzfassung für Aktenüberblick).",
        S['body']))

    story.append(Paragraph("Darstellender Teil", S['h2']))
    story.append(Paragraph(
        "Die VEYRA AI Foundation gGmbH ist eine 2018 gegründete gemeinnützige GmbH "
        "mit Sitz in Frankfurt am Main. Sie betreibt und fördert Open-Source-KI-"
        "Forschung und ist technisch in der europäischen KI-Community anerkannt. "
        "Aufgrund des Spendenrückgangs (Q1 2026: -34% ggü. Vorjahr) und der "
        "Verzögerung des EU-Förderprojekts OPENSENS ist die Gesellschaft ohne "
        "Gegenmaßnahmen ab ca. M14 (Juni 2027) drohend zahlungsunfähig i.S.v. "
        "§ 18 InsO.", S['body']))

    story.append(Paragraph("Gestaltender Teil — Maßnahmen:", S['h2']))
    massn_plan = [
        ['Nr.', 'Maßnahme', 'Gläubiger/Vertragspartner', 'Laufzeit', 'Einsparung EUR p.a.'],
        ['1', 'Stundungsvereinbarung GPU-Kosten (50% Stundung, Nachzahlung ab M18)', 'Nordlicht Cloud GmbH', '18 Monate', '708.000'],
        ['2', 'Personalreduzierung: 4 befristete Stellen nicht verlängern', 'Arbeitnehmer (läuft aus)', 'Ab Okt 26', '280.000'],
        ['3', 'Spendenauflagen-Anpassung: Zweckentbindung EUR 400.000 Rücklagen', 'Finanzamt Frankfurt III', 'Einmalig', '400.000'],
        ['4', 'EU-Abschlagszahlung OPENSENS: Antrag auf Vorfinanzierung EUR 200.000', 'EU-Verwaltungsbehörde', 'Einmalig', '200.000'],
        ['5', 'Neue Großspender-Kampagne (Ziel: EUR 500.000 bis Dez 2026)', 'Potenzielle Spender', 'H2 2026', '500.000'],
    ]
    mp_tbl = Table(massn_plan, colWidths=[0.8*cm, 5.5*cm, 4*cm, 2.5*cm, 4.7*cm])
    mp_tbl.setStyle(tbl_style_zahlen())
    story.append(mp_tbl)
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "Gesamteinsparung und Liquiditätszuführung (M1-M18): <b>EUR 2.088.000</b>. "
        "Bei Durchführung aller Maßnahmen ist die Zahlungsfähigkeit nach aktueller "
        "Planung bis M24 (April 2028) sichergestellt.",
        S['body']))

    # Handschriftliche Notiz
    story.append(Spacer(1, 0.4*cm))
    story.append(hr(FARBE_A, 0.5))
    story.append(Paragraph("Handschriftliche Notiz — Dr. Mira Hellinghaus-Karpov (Original, eingescannt):", S['small']))
    story.append(Spacer(1, 0.1*cm))

    # Simulierter Notizzettel
    notiz_data = [[
        Paragraph(
            "Brauche STAB-Anordnung VOR Q3-Foerderbescheid!!\n\n"
            "Warum?? — EU zahlt erst wenn StaRUG-Plan bestaetigt??\n"
            "Fragen Dr. Reher-Bornholmsen: Kann § 49 StaRUG-Antrag\n"
            "parallel zum Foerderantrag laufen?\n\n"
            "DRINGEND: Nordlicht Cloud droht mit Kuendigung wenn\n"
            "wir bis 15. Mai nicht zahlen!! EUR 354.000 offen!\n\n"
            "Tjark anrufen HEUTE!!",
            ParagraphStyle('notiz', fontName='Times-Italic', fontSize=11,
                          leading=17, textColor=colors.HexColor("#000080"),
                          leftIndent=10)
        )
    ]]
    notiz_tbl = Table(notiz_data, colWidths=[16*cm])
    notiz_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FFFDF0")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#B8860B")),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 15),
        ('RIGHTPADDING', (0,0), (-1,-1), 15),
    ]))
    story.append(notiz_tbl)
    story.append(PageBreak())

    # 7. Restrukturierungssachen-Anzeige
    story.append(Paragraph("A.7 Anzeige der Restrukturierungssache — AG Frankfurt", S['h1']))
    story.append(hr(FARBE_A))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "<b>AN DAS AMTSGERICHT FRANKFURT AM MAIN</b><br/>"
        "Insolvenz- und Restrukturierungsgericht<br/>"
        "Gerichtsstraße 2, 60313 Frankfurt am Main",
        S['body_left']))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("<b>ANZEIGE DER RESTRUKTURIERUNGSSACHE</b>", S['h2']))
    story.append(Paragraph("gemäß § 31 Abs. 1 StaRUG", S['body_left']))
    story.append(hr())
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "Die unterzeichnende Geschäftsführerin zeigt hiermit gemäß § 31 Abs. 1 "
        "des Gesetzes über den Stabilisierungs- und Restrukturierungsrahmen für "
        "Unternehmen (StaRUG) die Inanspruchnahme des Restrukturierungsrahmens an.",
        S['body']))

    az_data = [
        ['Schuldnerin:', 'VEYRA AI Foundation gGmbH, Eschersheimer Landstraße 42, 60322 Frankfurt am Main'],
        ['Aktenzeichen HRB:', 'HRB 118 847 — Amtsgericht Frankfurt am Main'],
        ['Gesetzliche Vertreterin:', 'Dr. Mira Hellinghaus-Karpov (GF, alleinvertretungsberechtigt)'],
        ['Verfahrensbevollmächtigte:', 'RA Dr. Tjark Reher-Bornholmsen, Reher Wennstedt Restrukturierung PartmbB, Hohe Bleichen 14, 20354 Hamburg'],
        ['Anzeigezweck:', 'Inanspruchnahme des Restrukturierungsrahmens gemäß §§ 2 ff. StaRUG; '
                         'beabsichtigte Instrumente: Restrukturierungsplan, ggf. Stabilisierungsanordnung'],
        ['Vom Restrukturierungsplan erfasste Forderungen:', 'Verbindlichkeiten gegenüber Nordlicht Cloud GmbH (EUR 354.000); '
                                                              'Verbindlichkeiten gegenüber sonstigen Gläubigern (EUR ca. 180.000)'],
    ]
    az_tbl = Table(az_data, colWidths=[4.5*cm, 13*cm])
    az_tbl.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.white, GRAU_HELL]),
        ('GRID', (0,0), (-1,-1), 0.2, GRAU_MID),
    ]))
    story.append(az_tbl)
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "Anlagen: (1) Gesellschafterprofil; (2) 24-Monats-Liquiditätsplan (Stand 30.04.2026); "
        "(3) Restrukturierungsplan-Entwurf (Kurz); (4) Vollmacht RA Dr. Reher-Bornholmsen; "
        "(5) Handelsregisterauszug HRB 118 847.",
        S['body']))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph(
        "Frankfurt am Main, 12. Mai 2026",
        S['right']))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph(
        "_________________________",
        S['right']))
    story.append(Paragraph(
        "Dr. Mira Hellinghaus-Karpov",
        ParagraphStyle('sig3', fontName='Times-Italic', fontSize=10, alignment=TA_RIGHT)))
    story.append(Paragraph(
        "Geschäftsführerin VEYRA AI Foundation gGmbH",
        S['right']))
    story.append(PageBreak())

# ─────────────────────────────────────────────────────────────────────────────
# VARIANTE B: HERRENBLUSE & ZWIRN HARTMANNSCHMIDT AG
# ─────────────────────────────────────────────────────────────────────────────

def build_variante_b(story):
    AZ = "AG Bamberg 53 RES 7/26"

    story.append(Paragraph("B.1 Gesellschaftsprofil — Herrenbluse & Zwirn Hartmannschmidt AG", S['h1']))
    story.append(hr(FARBE_B))

    for line in fax_block([
        "MANDATSNOTIZ — Reher Wennstedt Restrukturierung PartmbB",
        f"Az.: {AZ} | Datum: 15. April 2026",
        "Mandant: Herrenbluse & Zwirn Hartmannschmidt AG, Bamberg",
        "Betreff: Ersterfassung + IDW-S-6-Beauftragung (INTERN)",
    ]):
        story.append(line)
    story.append(Spacer(1, 0.3*cm))

    profil = [
        ['Firma:', 'Herrenbluse & Zwirn Hartmannschmidt Aktiengesellschaft'],
        ['Sitz:', 'Luitpoldstraße 88, 96052 Bamberg'],
        ['Handelsregister:', 'HRB 4 771 — Amtsgericht Bamberg'],
        ['Notierung:', 'Freiverkehr (Open Market), Primärmarkt, Börse Frankfurt; ISIN: DE000HZH0042'],
        ['Gründungsjahr:', '1891 (Familienunternehmen seit über 130 Jahren)'],
        ['Grundkapital:', 'EUR 6.500.000 (eingeteilt in 6.500.000 auf den Inhaber lautende Aktien)'],
        ['Mitarbeiter:', 'ca. 720 (davon 480 Produktion, 140 Verwaltung, 100 Außendienst/Vertrieb)'],
        ['Umsatz 2025:', 'EUR 182.400.000 (Rückgang -8,3% ggü. 2024)'],
        ['EBITDA 2025:', 'EUR 8.100.000 (Marge 4,4% — Tief seit 2008)'],
        ['EBIT 2025:', 'EUR 2.300.000'],
        ['Finanzschulden:', 'Anleihe DE000HZH0042: EUR 65.000.000 (fällig Oktober 2027); Konsortialkredit: EUR 28.000.000 (fällig März 2027)'],
        ['Covenant (synth.):', 'Net Debt/EBITDA max. 5,5x; aktuell: 11,5x — BRUCH'],
        ['Ankeraktionär:', 'Hartmannschmidt Holding KG (Bamberg): 55% der Aktien'],
        ['Vorstand:', 'Dipl.-Kfm. Helge Hartmannschmidt (Sprecher); Annika Lüttke-Berens (CFO)'],
        ['Aufsichtsrat:', '6 Personen; Vorsitz: Dr. Ruprecht Hartmannschmidt (Ankeraktionär-Familie)'],
        ['Kanzlei:', 'Reher Wennstedt (federführend, RA Dr. Reher-Bornholmsen); Restrukturierungs-Counsel Dr. Christoph Vellmer-Lutz'],
    ]
    ptbl = Table(profil, colWidths=[4*cm, 13.5*cm])
    ptbl.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.white, GRAU_HELL]),
        ('GRID', (0,0), (-1,-1), 0.2, GRAU_MID),
    ]))
    story.append(ptbl)
    story.append(PageBreak())

    # IDW S 11 Fortbestehensprognose
    story.append(Paragraph("B.2 IDW S 11 — Fortbestehensprognose (Kurzfassung)", S['h1']))
    story.append(hr(FARBE_B))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "Erstellt von: Hartwig Aktuar & Restrukturierung GmbH Wirtschaftsprüfungsgesellschaft, Köln (fiktiv)<br/>"
        "Auftrag: Reher Wennstedt PartmbB im Auftrag Hartmannschmidt AG<br/>"
        "Stand: 30. April 2026 | Vertraulich — nur für Bankenkonsortium",
        S['small']))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("1. Vorbemerkung und Aufgabenstellung", S['h2']))
    story.append(Paragraph(
        "Die vorliegende Fortbestehensprognose nach IDW S 11 wurde im Auftrag der "
        "Hartmannschmidt AG zur Vorlage beim Bankenkonsortium (NorddeutscheLandesbank-Avis "
        "und Sparkasse Oberfranken) erstellt. Gegenstand ist die Prüfung der Frage, "
        "ob die Gesellschaft auf Basis des vorgelegten Sanierungskonzepts als "
        "fortführungsfähig anzusehen ist.", S['body']))

    story.append(Paragraph("2. Ergebnis der Fortbestehensprognose", S['h2']))

    prog_data = [
        ['Prognose-Horizont', 'Ergebnis', 'Voraussetzung', 'Risikostufe'],
        ['12 Monate (bis Apr. 2027)', 'POSITIV — unter Bedingungen', 'Bankenstillhalte + Anleihe-Stundung bis Jul 2027', 'ERHEBLICH'],
        ['24 Monate (bis Apr. 2028)', 'BEDINGT POSITIV', 'Erfolgreiche StaRUG-Planbestätigung bis Dez. 2026', 'HOCH'],
        ['36 Monate (bis Apr. 2029)', 'OFFEN — abhängig von Sanierungserfolg', 'Margen-Erholung > 6% EBITDA ab 2027', 'HOCH'],
    ]
    prog_tbl = Table(prog_data, colWidths=[3.5*cm, 4.5*cm, 5.5*cm, 4*cm])
    p_style = tbl_style_standard()
    p_style.add('BACKGROUND', (3,1), (3,1), colors.HexColor("#FFE080"))
    p_style.add('BACKGROUND', (3,2), (3,2), colors.HexColor("#FFE080"))
    p_style.add('BACKGROUND', (3,3), (3,3), colors.HexColor("#FFE080"))
    prog_tbl.setStyle(p_style)
    story.append(prog_tbl)
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("3. Covenant-Analyse", S['h2']))
    cov_data = [
        ['Covenant', 'Schwelle', 'Aktuell (31.12.2025)', 'Prognose (31.12.2026)', 'Bruch?'],
        ['Net Debt / EBITDA', 'max. 5,5x', '11,5x', '9,2x', 'JA — BRUCH'],
        ['Mindest-EBITDA', 'EUR 15 Mio.', 'EUR 8,1 Mio.', 'EUR 10,2 Mio. (Szenario Base)', 'JA — BRUCH'],
        ['Eigenkapital-Quote', 'min. 20%', '14,2%', '12,8%', 'JA — BRUCH'],
        ['Interest Coverage Ratio', 'min. 2,5x', '0,8x', '1,1x', 'JA — BRUCH'],
        ['Anleihe-Fälligkeit', 'Okt. 2027', '—', '18 Monate bis Fälligkeit', 'RISIKO'],
    ]
    cov_tbl = Table(cov_data, colWidths=[4*cm, 2.5*cm, 3.5*cm, 3.5*cm, 4*cm])
    c_style = tbl_style_standard()
    for i in range(1, 5):
        c_style.add('BACKGROUND', (4,i), (4,i), colors.HexColor("#FFE0E0"))
        c_style.add('TEXTCOLOR', (4,i), (4,i), ROT)
        c_style.add('FONTNAME', (4,i), (4,i), 'Helvetica-Bold')
    c_style.add('BACKGROUND', (4,5), (4,5), colors.HexColor("#FFE080"))
    cov_tbl.setStyle(c_style)
    story.append(cov_tbl)
    story.append(PageBreak())

    # IDW S 6 Sanierungsgutachten
    story.append(Paragraph("B.3 IDW S 6 — Sanierungsgutachten (Kurzfassung)", S['h1']))
    story.append(hr(FARBE_B))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "<b>Hartwig Aktuar & Restrukturierung GmbH WPG, Köln</b><br/>"
        "IDW S 6-Gutachten (Kurzfassung) | Stand: 15. Mai 2026 | Streng vertraulich",
        S['small_bold']))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("A. Krisenursachen-Analyse (IDW S 6 Tz. 1–15)", S['h2']))
    story.append(Paragraph(
        "Die Herrenbluse & Zwirn Hartmannschmidt AG befindet sich in einer "
        "mehrdimensionalen Unternehmenskrise:", S['body']))
    krisen = [
        ['Krisenphase', 'Erscheinungsbild', 'Zeitpunkt Eintritt'],
        ['Strategische Krise', 'Verlust Preissetzungsmacht durch China-Import-Konkurrenz; kein differenziertes Premiumsegment', 'ca. 2018–2020'],
        ['Ertragskrise', 'EBITDA-Marge von 12,1% (2020) auf 4,4% (2025) — Halbierung in 5 Jahren', 'ab 2021'],
        ['Liquiditätskrise', 'Covenant-Bruch; Banken fordern Sanierungsgutachten; Anleihe-Fälligkeit Okt. 2027', 'ab Feb. 2026'],
    ]
    k_tbl = Table(krisen, colWidths=[3.5*cm, 8.5*cm, 5.5*cm])
    k_tbl.setStyle(tbl_style_standard())
    story.append(k_tbl)
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("B. Sanierungsfähigkeit und -konzept (IDW S 6 Tz. 45–88)", S['h2']))
    story.append(Paragraph(
        "Das Gutachten kommt zu dem Ergebnis, dass die Gesellschaft unter der "
        "Voraussetzung einer erfolgreichen Anleihe-Restrukturierung und der Umsetzung "
        "folgender Maßnahmen als sanierungsfähig einzustufen ist:", S['body']))
    san_data = [
        ['Nr.', 'Sanierungsmaßnahme', 'Effekt (EUR p.a.)', 'Umsetzungsfrist'],
        ['1', 'Kostensenkungsprogramm Phase I: Personalabbau 80 Stellen (sozialplanpflichtig)', '+EUR 4,8 Mio. EBITDA', 'Q3/Q4 2026'],
        ['2', 'Wareneinkaufs-Optimierung: Near-shoring Portugal/Türkei', '+EUR 2,2 Mio.', 'ab 2027'],
        ['3', 'Premiumlinie \"Hartmannschmidt Heritage\" — Preis +25%', '+EUR 1,5 Mio.', 'H1 2027'],
        ['4', 'Schließung Vertriebsniederlassung München (Mietkosten)', '+EUR 0,8 Mio.', 'Q2 2027'],
        ['5', 'Anleihe-Restrukturierung: Laufzeitverlängerung 3 Jahre + Zinskupon-Anpassung', 'Liquiditätsentlastung EUR 3,9 Mio./Jahr', 'bis Dez. 2026'],
        ['', 'Gesamt EBITDA-Verbesserung (Zielszenario 2027)', 'EUR +9,3 Mio. (Marge 9,5%)', ''],
    ]
    s_tbl = Table(san_data, colWidths=[0.8*cm, 7*cm, 4.5*cm, 5.2*cm])
    s_style = tbl_style_zahlen()
    s_style.add('FONTNAME', (0,-1), (-1,-1), 'Helvetica-Bold')
    s_style.add('BACKGROUND', (0,-1), (-1,-1), HELLBLAU)
    s_tbl.setStyle(s_style)
    story.append(s_tbl)
    story.append(PageBreak())

    # Bankenrunde Protokoll
    story.append(Paragraph("B.4 Bankenrunde-Protokoll — 5. Mai 2026", S['h1']))
    story.append(hr(FARBE_B))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "Ort: Reher Wennstedt Restrukturierung PartmbB, Hamburg (Videokonferenz + Präsenz)<br/>"
        "Datum: 5. Mai 2026, 10:00–15:30 Uhr<br/>"
        "Vorsitz: RA Dr. Tjark Reher-Bornholmsen",
        S['small']))
    story.append(Spacer(1, 0.2*cm))

    teiln = [
        ['Teilnehmer', 'Institution', 'Funktion'],
        ['Helge Hartmannschmidt', 'Hartmannschmidt AG (Mandant)', 'Vorstandssprecher'],
        ['Annika Lüttke-Berens', 'Hartmannschmidt AG (Mandant)', 'CFO'],
        ['Dr. Tjark Reher-Bornholmsen', 'Reher Wennstedt PartmbB', 'Verfahrensbevollm.'],
        ['Dr. Christoph Vellmer-Lutz', 'Restrukturierungs-Counsel', 'Planwerkstatt-Experte'],
        ['Klaus Hummeldorf', 'NorddeutscheLandesbank-Avis', 'Leiter Restrukturierung'],
        ['Martina Schreibersdorf', 'NorddeutscheLandesbank-Avis', 'Kredit-Management'],
        ['Peter Wachtschmidt', 'Sparkasse Oberfranken', 'Vorstand Firmenkunden'],
        ['RA Ulrich Beetz-von-Riemen', 'Anwalt des Bankenkonsortiums', 'Restrukturierungsrecht'],
    ]
    t_tbl = Table(teiln, colWidths=[5*cm, 6.5*cm, 6*cm])
    t_tbl.setStyle(tbl_style_standard())
    story.append(t_tbl)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("Wesentliche Besprechungspunkte:", S['h3']))
    story.append(Paragraph(
        "<b>Zu Punkt 1 — Liquiditätsstatus:</b> CFO Lüttke-Berens präsentiert den "
        "aktuellen Liquiditätsstatus. Cash-Position 30.04.2026: EUR 4,2 Mio. "
        "(Minimum-Threshold für laufenden Betrieb: EUR 3,5 Mio.). "
        "Reichweite ohne Bankenstillhalte: ca. 6 Wochen.",
        S['body']))
    story.append(Paragraph(
        "<b>Zu Punkt 2 — Standstill-Agreement:</b> Hummeldorf (NLB-Avis) signalisiert "
        "grundsätzliche Bereitschaft zu einem 6-monatigen Standstill. Vorbedingung: "
        "IDW S 6-Gutachten (liegt in Kurzfassung vor), Beauftragung Monitoring-Agent, "
        "kein weiterer Covenant-Bruch bis Standstill-Auslaufen.",
        S['body']))
    story.append(Paragraph(
        "<b>Zu Punkt 3 — StaRUG-Route:</b> Dr. Vellmer-Lutz erläutert, dass die "
        "geplante Anleihe-Restrukturierung via Cross-Class-Cram-Down nach § 26 StaRUG "
        "möglich ist, wenn die betroffene Gläubigergruppe (Anleihe-Gläubiger) nicht "
        "schlechtgestellt wird als in der Vergleichssituation (§ 26 Abs. 1 Nr. 1 StaRUG). "
        "Rechtsanwalt Beetz-von-Riemen kündigt an, die Rechte der Bankgläubiger "
        "genau zu prüfen.",
        S['body']))
    story.append(PageBreak())

    # Cross-Class-Cram-Down Memo
    story.append(Paragraph("B.5 Cross-Class-Cram-Down-Memo — Dr. Vellmer-Lutz", S['h1']))
    story.append(hr(FARBE_B))
    story.append(Spacer(1, 0.2*cm))

    for line in kanzlei_kopf_rw():
        story.append(line)
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "<b>INTERNES RECHTSMEMO</b><br/>"
        "An: Dr. Tjark Reher-Bornholmsen | Von: Dr. Christoph Vellmer-Lutz<br/>"
        "Datum: 10. Mai 2026 | Betreff: Cross-Class-Cram-Down § 26 StaRUG — Hartmannschmidt AG",
        S['small_bold']))
    story.append(hr())
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("I. Rechtliche Grundlage", S['h2']))
    story.append(Paragraph(
        "§ 26 StaRUG ermöglicht es, einen Restrukturierungsplan trotz Ablehnung durch "
        "eine oder mehrere Planbetroffenen-Gruppen zu bestätigen (sog. gruppenübergreifender "
        "Mehrheitsentscheid, auch 'Cross-Class-Cram-Down'). Die Voraussetzungen sind "
        "kumulativ:", S['body']))
    voraus = [
        "a) Mindestens eine zustimmende Gruppe (§ 26 Abs. 1 Nr. 3 StaRUG);",
        "b) Keine Gruppe wird schlechter gestellt als ohne Restrukturierungsplan (§ 26 Abs. 1 Nr. 1 StaRUG — 'Schlechterstellungsverbot');",
        "c) Kein Gläubiger erhält mehr als den vollen Betrag seiner Forderung (§ 26 Abs. 1 Nr. 2 StaRUG);",
        "d) Die Mehrheit der abstimmenden Gruppen hat zugestimmt oder die ablehnende Gruppe erhält nach dem Plan angemessene Beteiligung (§ 26 Abs. 2 StaRUG).",
    ]
    for v in voraus:
        story.append(Paragraph(v, S['indent']))

    story.append(Paragraph("II. Gruppenbildung Anleihe-Restrukturierung Hartmannschmidt AG", S['h2']))
    gruppen_data = [
        ['Gruppe', 'Gläubiger', 'Forderung', 'Geplante Plan-Quote', 'Stimmrecht'],
        ['Gruppe 1', 'NorddeutscheLandesbank-Avis (Konsortialkredit)', 'EUR 28 Mio.', '100% (unverändert, nur Laufzeit +18M)', 'Zustimmend (erwartet)'],
        ['Gruppe 2', 'Sparkasse Oberfranken (Konsortialk. anteilig)', 'EUR 0 Mio. (bereits zurückgezahlt 2025)', '—', 'Keine Abstimmung'],
        ['Gruppe 3', 'Anleihe-Gläubiger (Inhaber ISIN DE000HZH0042)', 'EUR 65 Mio.', 'Laufzeit +3 Jahre; Kupon 3,5% statt 5,2%', 'ABLEHNEND (erwartet)'],
        ['Gruppe 4', 'Lieferanten (> EUR 50.000 ungesichert)', 'Ca. EUR 8 Mio.', '80% sofort, 20% in 24M', 'Zustimmend (erwartet)'],
    ]
    g_tbl = Table(gruppen_data, colWidths=[1.7*cm, 4.5*cm, 2.5*cm, 4.5*cm, 4.3*cm])
    g_style = tbl_style_standard()
    g_style.add('BACKGROUND', (0,3), (-1,3), colors.HexColor("#FFE0E0"))
    g_tbl.setStyle(g_style)
    story.append(g_tbl)
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("III. Schlechterstellungsverbot — Prüfung Gruppe 3 (Anleihe)", S['h2']))
    story.append(Paragraph(
        "Das Schlechterstellungsverbot nach § 26 Abs. 1 Nr. 1 StaRUG ist für Gruppe 3 "
        "kritisch: Die Anleihe-Gläubiger erhalten im Plan eine Laufzeitverlängerung "
        "bei gleichzeitiger Zinskupon-Reduktion von 5,2% auf 3,5%. Dies ist wirtschaftlich "
        "ein Hair-cut in Höhe des Barwertverlusts. Im Vergleichsszenario (Insolvenzplan "
        "oder Regelverfahren) wäre die Quote der Anleihe-Gläubiger nach aktueller "
        "Einschätzung bei ca. 35–45 Cent/EUR. Der Plan-Wert für Gruppe 3 beträgt "
        "rechnerisch ca. 88 Cent/EUR (Barwert bei aktuellen Marktzinsen). "
        "Das Schlechterstellungsverbot ist damit voraussichtlich gewahrt.",
        S['body']))

    story.append(Paragraph("IV. HV-Vorbereitung-Memo für Familien-Anker", S['h2']))
    story.append(Paragraph(
        "Die Hartmannschmidt Holding KG (55% Anteile) muss als indirekt Betroffene "
        "über die geplante Maßnahme informiert werden. Besondere Vorsicht ist geboten, "
        "da eine Kapitalerhöhung im Zuge des Restrukturierungsplans nicht geplant ist "
        "(Kein Anteilsverwässerungs-Risiko für Anker-Aktionär). Die HV-Einberufung "
        "muss gemäß § 121 AktG erfolgen; sofern kein Zustimmungsvorbehalt der HV "
        "greift, ist die Billigung durch den Aufsichtsrat ausreichend (§ 111 Abs. 4 AktG). "
        "<b>WICHTIG: Das Schlechterstellungsverbot gilt nur für Planbetroffene — "
        "die Hartmannschmidt Holding KG als Aktionär ist grundsätzlich Nicht-Planbetroffene, "
        "es sei denn, der Plan greift in Anteilsrechte ein (§ 2 Abs. 3 StaRUG).</b>",
        S['body']))
    story.append(PageBreak())

# ─────────────────────────────────────────────────────────────────────────────
# VARIANTE C: NORDFELS POWER CELLS SE
# ─────────────────────────────────────────────────────────────────────────────

def build_variante_c(story):
    AZ = "AG Stuttgart 14 RES 22/26"

    story.append(Paragraph("C.1 Gesellschaftsprofil — Nordfels Power Cells SE", S['h1']))
    story.append(hr(FARBE_C))

    for line in fax_block([
        "MANDATSNOTIZ — Reher Wennstedt PartmbB / Brentwood Hartfeld Restructuring mbB",
        f"Az.: {AZ} | Datum: 20. April 2026",
        "Mandant: Nordfels Power Cells SE, Ellwangen (Jagst)",
        "Betreff: Erste Mandatssitzung StaRUG — STRENG VERTRAULICH",
    ]):
        story.append(line)
    story.append(Spacer(1, 0.3*cm))

    profil = [
        ['Firma:', 'Nordfels Power Cells Societas Europaea (SE)'],
        ['Sitz:', 'Industriestraße 112, 73479 Ellwangen (Jagst)'],
        ['Handelsregister:', 'HRB 73 112 — Amtsgericht Ellwangen (Jagst)'],
        ['Notierung:', 'Regulierter Markt (Prime Standard), SDAX-Kandidat; ISIN: DE000NPW0017'],
        ['Gründungsjahr:', '1985 (als GmbH); SE-Rechtsform seit 2010'],
        ['Grundkapital:', 'EUR 12.000.000 (eingeteilt in 12.000.000 Namensaktien ohne Nennwert)'],
        ['Mitarbeiter:', 'ca. 1.850 (davon 1.100 Produktion, 450 FuE, 300 Admin/Vertrieb)'],
        ['Umsatz 2025:', 'EUR 340.000.000 (Rückgang -31,2% ggü. 2024: EUR 494 Mio.)'],
        ['EBITDA 2025:', 'EUR -18.400.000 (negativ — operativer Verlust)'],
        ['EBIT 2025:', 'EUR -42.100.000'],
        ['Finanzschulden:', 'Anleihe ISIN DE000NPW0017: EUR 250.000.000 (fällig Juni 2028); Konsortialkredit: EUR 300.000.000 (fällig Sept. 2027)'],
        ['Aktionärsstruktur:', 'Vossbergen Family Office: 41%; Streubesitz: 38%; Westshore Catalyst Partners LLP (Cayman): 11%; Saalfeld Industrial Holding AG (Stuttgart): 10%'],
        ['Vorstand:', 'Lars-Henrik Vossbergen (CEO); Dr. Cornelia Tannert-Brescia (CFO); Otto Bietendüvel (COO)'],
        ['Aufsichtsrat:', '9 Personen inkl. Arbeitnehmervertreter; Vorsitz: Prof. Dr. Werner Hallenschlag-Ruhm'],
        ['Berater:', 'Reher Wennstedt PartmbB (Hamburg) + Brentwood Hartfeld Restructuring mbB (Düsseldorf, Of Counsel Prof. Dr. Engelbert Hartfeld-Marwede)'],
    ]
    ptbl = Table(profil, colWidths=[4*cm, 13.5*cm])
    ptbl.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.white, GRAU_HELL]),
        ('GRID', (0,0), (-1,-1), 0.2, GRAU_MID),
    ]))
    story.append(ptbl)
    story.append(PageBreak())

    # Stabilisierungsanordnung
    story.append(Paragraph("C.2 Antrag auf Stabilisierungsanordnung §§ 49–59 StaRUG", S['h1']))
    story.append(hr(FARBE_C))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "<b>AN DAS AMTSGERICHT STUTTGART</b><br/>"
        "Restrukturierungsgericht<br/>"
        "Hauffstraße 5, 70190 Stuttgart",
        S['body_left']))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "<b>ANTRAG AUF ERLASS EINER STABILISIERUNGSANORDNUNG<br/>"
        "gemäß §§ 49 Abs. 1 i.V.m. 50 StaRUG</b>",
        S['h2']))
    story.append(Paragraph(f"Az.: {AZ}", S['aktenzeichen']))
    story.append(hr())
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("I. Antragsstellerin und Rechtsverhältnis", S['h2']))
    story.append(Paragraph(
        "Antragsstellerin ist die Nordfels Power Cells SE, vertreten durch ihren "
        "Vorstand (Lars-Henrik Vossbergen, Dr. Cornelia Tannert-Brescia, Otto Bietendüvel), "
        "verfahrensbevollmächtigt durch Reher Wennstedt Restrukturierung PartmbB, "
        "Hamburg (RA Dr. Tjark Reher-Bornholmsen) sowie Brentwood Hartfeld Restructuring "
        "mbB, Düsseldorf (Prof. Dr. Engelbert Hartfeld-Marwede).", S['body']))

    story.append(Paragraph("II. Sachverhalt und Begründung der Bestandsgefährdung", S['h2']))
    story.append(Paragraph(
        "Die Nordfels Power Cells SE hat im Geschäftsjahr 2025 einen Umsatzrückgang "
        "von EUR 154 Mio. (-31,2%) erlitten. Ursache ist der strategische Wechsel "
        "des Hauptkunden (Konsumelektronik-Konzern, Anteil: 38% des Gesamtumsatzes 2024) "
        "zu einem Konkurrenzlieferanten aus Südostasien. Dieser Wechsel war trotz "
        "Frühwarnzeichen ab Q3 2024 nicht in ausreichendem Maß antizipiert. Das "
        "EBITDA war 2025 erstmals seit 2008 negativ (EUR -18,4 Mio.).",
        S['body']))

    story.append(Paragraph(
        "Die Gesellschaft ist gegenwärtig nicht zahlungsunfähig im Sinne des § 17 InsO. "
        "Die Zahlungsunfähigkeit droht jedoch im Sinne des § 18 InsO: Nach dem "
        "vorgelegten 24-Monats-Liquiditätsplan wäre ohne Gegenmaßnahmen die "
        "Zahlungsfähigkeit in Monat 8 (Dezember 2026) erschöpft. Zur Überbrückung "
        "dieser Lücke und zur Ermöglichung der StaRUG-Planverhandlungen beantragt "
        "die Schuldnerin eine Stabilisierungsanordnung.", S['body']))

    story.append(Paragraph("III. Beantragter Inhalt der Stabilisierungsanordnung", S['h2']))
    story.append(Paragraph(
        "Gemäß §§ 49 Abs. 1, 50 Abs. 1 StaRUG wird beantragt, folgende "
        "Stabilisierungsanordnung zu erlassen:", S['body']))
    antrag_punkte = [
        "1. Aussetzung der Vollstreckung von Maßnahmen gegen das Vermögen der "
        "Nordfels Power Cells SE durch Maßnahmen der Einzel- oder Gesamtvollstreckung "
        "für die Dauer von drei Monaten ab Erlass der Anordnung (§ 49 Abs. 1 Nr. 1 StaRUG);",

        "2. Untersagung der Verwertung von Sicherheiten durch besicherte Gläubiger "
        "(insbesondere Kreditgeberkonsortium) für die Dauer der Anordnung "
        "(§ 49 Abs. 1 Nr. 2 StaRUG);",

        "3. Anordnung, dass die Aufrechnung gegen Forderungen der Schuldnerin "
        "durch planbetroffene Gläubiger beschränkt ist "
        "(§ 49 Abs. 1 Nr. 3 StaRUG);",

        "4. Anordnung des Inhaberwechsels bei bestehenden Vertragsverhältnissen "
        "nach § 50 Abs. 1 StaRUG ist nicht beantragt.",
    ]
    for p in antrag_punkte:
        story.append(Paragraph(p, S['indent']))

    story.append(Paragraph("IV. Dringlichkeit", S['h2']))
    story.append(Paragraph(
        "Die Dringlichkeit ist gegeben, weil (a) das Kreditgeberkonsortium "
        "angekündigt hat, bei Covenant-Bruch innerhalb von 30 Tagen Vollstreckungsmaßnahmen "
        "einzuleiten; (b) der Aktivist-Hedgefonds Westshore Catalyst Partners LLP "
        "(Cayman) durch einen offenen Brief an den Aufsichtsrat Druck ausübt "
        "(vgl. Anlage C.5); (c) die Anleihe-Gläubigerversammlung zum 15. Juni 2026 "
        "einberufen ist und Verzichterklärungen eingeholt werden müssen.",
        S['body']))

    story.append(Paragraph("V. Anlageninventar", S['h2']))
    anlagen = [
        ['Anlage Nr.', 'Bezeichnung'],
        ['C-1', 'Handelsregisterauszug HRB 73 112 (aktuell)'],
        ['C-2', 'Anzeige Restrukturierungssache § 31 StaRUG (bereits eingereicht)'],
        ['C-3', '24-Monats-Liquiditätsplan (Base/Stress/Severe Stress)'],
        ['C-4', 'Aufsichtsrats-Beschluss zur StaRUG-Anzeige vom 18. April 2026'],
        ['C-5', 'Investor Letter Westshore Catalyst Partners LLP vom 2. Mai 2026'],
        ['C-6', 'Kreditvertrag Konsortialkredit (Auszug Covenant-Klausel)'],
        ['C-7', 'IDW S 11-Fortbestehensprognose (Vorversion, Stand 15.04.2026)'],
        ['C-8', 'Restrukturierungsplan-Entwurf (Kurzfassung, Stand 12.05.2026)'],
    ]
    a_tbl = Table(anlagen, colWidths=[2.5*cm, 15*cm])
    a_tbl.setStyle(tbl_style_standard())
    story.append(a_tbl)
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "Hamburg/Düsseldorf, 20. Mai 2026",
        S['right']))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "RA Dr. Tjark Reher-Bornholmsen / Prof. Dr. Engelbert Hartfeld-Marwede",
        ParagraphStyle('sig4', fontName='Times-Italic', fontSize=10, alignment=TA_RIGHT)))
    story.append(PageBreak())

    # Investor-Letter Westshore
    story.append(Paragraph("C.3 Investor Letter — Westshore Catalyst Partners LLP", S['h1']))
    story.append(hr(FARBE_C))
    story.append(Spacer(1, 0.2*cm))

    # Simulierter englischer Brief-Kopf
    for line in fax_block([
        "WESTSHORE CATALYST PARTNERS LLP",
        "Grand Cayman, KY1-1102, Cayman Islands",
        "Tel.: +1 (345) 949-8888 | office@westshore-catalyst.ky",
        "STRICTLY PRIVATE AND CONFIDENTIAL",
    ]):
        story.append(line)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph(
        "Nordfels Power Cells SE<br/>"
        "Attention: Supervisory Board<br/>"
        "Industriestraße 112, 73479 Ellwangen (Jagst)<br/>"
        "Germany",
        S['body_left']))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("May 2, 2026", S['body_left']))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "<b>RE: Concerns Regarding Proposed StaRUG Restructuring — Bondholder Protection "
        "and Dilution Risk</b>",
        S['bold']))
    story.append(hr())
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "Dear Members of the Supervisory Board,",
        S['body_left']))
    story.append(Spacer(1, 0.15*cm))

    story.append(Paragraph(
        "Westshore Catalyst Partners LLP (\"Westshore\"), which holds approximately "
        "11% of the outstanding ordinary shares of Nordfels Power Cells SE (\"Nordfels\" "
        "or the \"Company\"), writes to express its serious concerns regarding the "
        "Company's announced intention to pursue a restructuring under Germany's "
        "StaRUG framework.",
        S['body']))

    story.append(Paragraph("<b>1. Dilution Risk to Minority Shareholders</b>",
                           S['bold']))
    story.append(Paragraph(
        "Westshore understands that the proposed restructuring plan may involve "
        "a debt-to-equity conversion, a capital reduction (Kapitalherabsetzung) "
        "followed by a capital increase (Kapitalerhöhung) that would materially dilute "
        "existing minority shareholders. We note that the Vossbergen Family Office, "
        "holding approximately 41% of shares, may be positioned to participate in "
        "any new equity issuance while minority holders — including Westshore — "
        "would face disproportionate dilution.",
        S['body']))

    story.append(Paragraph("<b>2. Schlechterstellungsverbot — Cross-Class Cram-Down Risk</b>",
                           S['bold']))
    story.append(Paragraph(
        "We are advised that under § 26 StaRUG, a Cross-Class Cram-Down may be "
        "used to bind dissenting creditor groups. We emphasize that the "
        "non-impairment test ('Schlechterstellungsverbot') must be rigorously "
        "applied. Any attempt to impose a restructuring plan that leaves bondholders "
        "in a materially worse economic position than they would achieve in an "
        "insolvency scenario will be vigorously contested through all available legal "
        "means, including an application to the restructuring court to reject "
        "the plan under § 63 StaRUG.",
        S['body']))

    story.append(Paragraph("<b>3. Demand for Transparency</b>",
                           S['bold']))
    story.append(Paragraph(
        "Westshore respectfully demands that the Supervisory Board ensure: "
        "(i) an independent financial advisor engaged on behalf of minority shareholders; "
        "(ii) full disclosure of the restructuring plan to all affected stakeholders "
        "at least 14 days prior to the vote; "
        "(iii) an independent fairness opinion addressing the Schlechterstellungsverbot "
        "for all plan-affected groups.",
        S['body']))

    story.append(Paragraph("<b>4. Reservation of Rights</b>",
                           S['bold']))
    story.append(Paragraph(
        "Westshore expressly reserves all rights under applicable German and Cayman "
        "Islands law, including but not limited to challenging the restructuring plan "
        "before the AG Stuttgart, seeking injunctive relief, and pursuing damages "
        "claims. This letter shall not constitute a waiver of any such rights.",
        S['body']))

    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("Sincerely,", S['body_left']))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "William C. Harbridge-Fenton\nManaging Partner, Westshore Catalyst Partners LLP",
        ParagraphStyle('sig5', fontName='Times-Italic', fontSize=10, textColor=DUNKELBLAU)
    ))
    story.append(PageBreak())

    # Aufsichtsrats-Beschluss
    story.append(Paragraph("C.4 Aufsichtsrats-Beschluss zur StaRUG-Anzeige", S['h1']))
    story.append(hr(FARBE_C))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "Protokollauszug — Aufsichtsrat Nordfels Power Cells SE<br/>"
        "Sitzung: 18. April 2026, 14:00 Uhr | Ort: Ellwangen + Videokonferenz<br/>"
        "Beschlussfähigkeit: 7 von 9 AR-Mitgliedern anwesend",
        S['small']))
    story.append(Spacer(1, 0.2*cm))

    ar_beschl = [
        ['Beschl.-Nr.', 'Gegenstand', 'Ergebnis'],
        ['AR-2026-04-01', 'Kenntnis vom Liquiditätsbericht CFO Dr. Tannert-Brescia', 'Zur Kenntnis genommen'],
        ['AR-2026-04-02', 'Beauftragung Reher Wennstedt PartmbB + Brentwood Hartfeld mbB als StaRUG-Berater', '7:0 — Einstimmig'],
        ['AR-2026-04-03', 'Anzeige Restrukturierungssache § 31 StaRUG beim AG Stuttgart', '7:0 — Einstimmig'],
        ['AR-2026-04-04', 'Antrag Stabilisierungsanordnung §§ 49-59 StaRUG (nach Vorlage Volltext-Antrag)', '6:1 (AR-Mitglied Arbeitnehmervertr. Stimmenthaltung)'],
        ['AR-2026-04-05', 'Vorschlag Restrukturierungsbeauftragter: Frau Wilhelmine Greve-Tornquist', '7:0 — Einstimmig'],
        ['AR-2026-04-06', 'Information der Hauptversammlung nach § 175 AktG (HV-Vorbereitung)', 'Delegiert an Vorstand'],
    ]
    arb_tbl = Table(ar_beschl, colWidths=[3.5*cm, 8.5*cm, 5.5*cm])
    arb_tbl.setStyle(tbl_style_standard())
    story.append(arb_tbl)
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("Restrukturierungsbeauftragter — Kurzprofil Wilhelmine Greve-Tornquist:", S['h3']))
    story.append(Paragraph(
        "Dipl.-Kffr. Wilhelmine Greve-Tornquist (Jahrgang 1971, Hamburg) — Fachanwältin "
        "für Insolvenz- und Sanierungsrecht, zugelassene Restrukturierungsbeauftragte "
        "nach § 73 StaRUG. Langjährige Erfahrung als Insolvenzverwalterin und "
        "StaRUG-Sachwalter. Eigene Kanzlei Greve-Tornquist PartmbB, Hamburg "
        "(fiktiv). Vorschlag durch Reher Wennstedt PartmbB; keine Interessenkonflikte "
        "erklärt.", S['body']))
    story.append(PageBreak())

    # 24-Monats-Liquiplan mit drei Szenarien
    story.append(Paragraph("C.5 24-Monats-Liquiditätsplan — Drei Szenarien", S['h1']))
    story.append(Paragraph("Nordfels Power Cells SE | Stand: 30. April 2026 | Dr. Cornelia Tannert-Brescia (CFO)", S['subtitle']))
    story.append(hr(FARBE_C))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("Szenario-Annahmen:", S['h3']))
    sz_data = [
        ['Parameter', 'BASE Case', 'STRESS Case', 'SEVERE STRESS'],
        ['Umsatz 2026', 'EUR 270 Mio.', 'EUR 240 Mio.', 'EUR 200 Mio.'],
        ['Umsatz 2027', 'EUR 310 Mio.', 'EUR 265 Mio.', 'EUR 220 Mio.'],
        ['EBITDA-Marge 2026', '-3%', '-8%', '-14%'],
        ['EBITDA-Marge 2027', '+4%', '-2%', '-8%'],
        ['Anleihe-Verlängerung', 'Ja (+3 Jahre)', 'Ja (+2 Jahre)', 'Nein — Fälligkeit Juni 2028'],
        ['Konsortialkredit-Rollover', 'Ja (Sept. 2027 +18M)', 'Teilweise (50%)', 'Nein — Fälligkeit Sept. 2027'],
        ['Kapitalerhöhung geplant', 'EUR 80 Mio. (H1 2027)', 'EUR 50 Mio.', 'Nicht umsetzbar'],
        ['StaRUG-Planbestätigung', 'Dez. 2026', 'Mrz. 2027', 'Scheitert'],
    ]
    sz_tbl = Table(sz_data, colWidths=[5*cm, 4*cm, 4*cm, 4.5*cm])
    s3_style = tbl_style_standard()
    for i in range(1, len(sz_data)):
        s3_style.add('BACKGROUND', (3,i), (3,i), colors.HexColor("#FFE0E0"))
    sz_tbl.setStyle(s3_style)
    story.append(sz_tbl)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("Monatliche Liquiditätsentwicklung (Endbestand, in TEUR):", S['h3']))
    liq_header = ['Monat', 'BASE Case', 'STRESS Case', 'SEVERE STRESS']
    liq_rows = [
        ['Apr 26', '38.400', '32.100', '25.800'],
        ['Mai 26', '22.800', '14.200', '5.400'],
        ['Jun 26', '18.400', '8.600', '-2.100'],
        ['Jul 26', '15.200', '5.100', '-8.900'],
        ['Aug 26', '12.800', '2.400', '-16.200'],
        ['Sep 26', '10.100', '-1.800', '-24.100'],
        ['Okt 26', '8.400', '-5.200', '-32.500'],
        ['Nov 26', '6.900', '-9.100', '-41.200'],
        ['Dez 26', '48.200\n(+KE EUR 80M)', '-14.800', '-51.100'],
        ['Jan 27', '45.800', '-18.900', '-61.500'],
        ['Feb 27', '43.100', '-23.400', '-72.200'],
        ['Mrz 27', '41.200', '-28.100', '-83.900'],
        ['Apr 27', '39.800', '-32.900', '-96.100'],
        ['Mai 27', '38.100', '-38.200', '-109.700'],
        ['Jun 27', '36.800', '-44.100', '-124.500'],
        ['Jul 27', '35.400', '-50.700', '-140.800'],
        ['Aug 27', '33.900', '-57.900', '-158.500'],
        ['Sep 27', '32.800\n(Kredit rolliert)', '-65.800\n(Kredit 50%)', '-177.900\n(Kredit fällig!)'],
        ['Okt 27', '31.200', '-68.200', '-198.100'],
        ['Nov 27', '30.100', '-71.100', '-220.400'],
        ['Dez 27', '29.400', '-74.800', '-244.200'],
        ['Jan 28', '28.900', '-79.100', '-269.500'],
        ['Feb 28', '28.200', '-84.200', '-296.800'],
        ['Mrz 28', '27.800', '-90.100', '-326.200'],
        ['Apr 28', '27.400', '-97.400', '-358.900'],
    ]
    liq_data = [liq_header] + liq_rows
    l_tbl = Table(liq_data, colWidths=[2.5*cm, 4.5*cm, 4.5*cm, 4.5*cm])
    l_style = tbl_style_zahlen()
    for i, row in enumerate(liq_rows, 1):
        if row[2].startswith('-'):
            l_style.add('TEXTCOLOR', (2,i), (2,i), ROT)
            l_style.add('FONTNAME', (2,i), (2,i), 'Helvetica-Bold')
        if row[3].startswith('-'):
            l_style.add('TEXTCOLOR', (3,i), (3,i), ROT)
            l_style.add('FONTNAME', (3,i), (3,i), 'Helvetica-Bold')
            l_style.add('BACKGROUND', (3,i), (3,i), colors.HexColor("#FFE8E8"))
    l_tbl.setStyle(l_style)
    story.append(l_tbl)
    story.append(Paragraph(
        "Alle Angaben in TEUR. Severe Stress: Insolvenzantragspflicht ab Jun. 2026 (M3). "
        "BASE Case: positiver Abschluss dank Kapitalerhöhung Dez. 2026 und Kredit-Rollover.",
        S['footnote']))
    story.append(PageBreak())

# ─────────────────────────────────────────────────────────────────────────────
# VARIANTE D: SALALTBAR UG
# ─────────────────────────────────────────────────────────────────────────────

def build_variante_d(story):
    AZ = "AG Charlottenburg 36 IN 412/26"

    story.append(Paragraph("D.1 Gesellschaftsprofil — Salaltbar UG (haftungsbeschränkt)", S['h1']))
    story.append(hr(FARBE_D))
    story.append(Spacer(1, 0.2*cm))

    for line in kanzlei_kopf_wandelmoser():
        story.append(line)
    story.append(Spacer(1, 0.3*cm))

    for line in fax_block([
        "Rechtsanwaeltin Charlotte Wandelmoser, Kantstrasse 91, 10627 Berlin",
        f"Az. intern: CW-2026-SALALTBAR | Datum: 2. Mai 2026",
        "Mandant: Salaltbar UG (haftungsbeschränkt), Berlin-Neukoelln",
        "Betreff: Ersterfassung — Krisenanzeichen, § 1 StaRUG, § 15a InsO-Schwelle",
    ]):
        story.append(line)
    story.append(Spacer(1, 0.3*cm))

    profil = [
        ['Firma:', 'Salaltbar UG (haftungsbeschränkt)'],
        ['Sitz:', 'Hermannplatz 14, 12049 Berlin (Hauptfiliale + Sitz)'],
        ['Handelsregister:', 'HRB 212 904 B — Amtsgericht Charlottenburg'],
        ['Gründungsjahr:', '2021'],
        ['Stammkapital:', 'EUR 1,00 (UG-Mindestkapital gem. § 5a GmbHG)'],
        ['Rücklagenpflicht § 5a Abs. 3 GmbHG:', 'Rücklage hätte EUR 124 betragen müssen — VERLETZT (keine Rücklage gebildet)'],
        ['Geschäftsführer/Alleingesellschafter:', 'Tarek-Yusuf Çelebi-Drebenstedt (geb. 1990, Berlin)'],
        ['Mitarbeiter:', '14 (inkl. GF); davon 11 Teilzeit (Minijob)'],
        ['Filialen:', '3 Standorte: Hermannplatz 14, Boddinstraße 27, Sonnenallee 89b (Berlin-Neukölln)'],
        ['Konzept:', 'Vegane Salat-Bar, Fast-Casual, Selbstbedienung + Lieferung (Lieferando/Wolt)'],
        ['Umsatz 2025 (geschätzt):', 'EUR 682.000 (Hermannpl. EUR 320.000; Boddinstr. EUR 230.000; Sonnenallee EUR 132.000)'],
        ['Jahresverlust 2025 (geschätzt):', 'EUR -89.000 (ergibt sich aus Buchführungs-Übersicht, noch nicht testiert)'],
        ['Gläubiger:', 'Vermieter Sonnenallee (Mietrückstand EUR 18.400); Lieferant Frische-Kontor Berlin GmbH (EUR 12.800); Finanzamt (USt-Rückstände EUR 8.900); Wolt-Gebühren-Rücklastschrift EUR 3.200'],
        ['Cash:', 'EUR 3.400 auf Geschäftskonto (Stand 01.05.2026)'],
        ['Reichweite:', 'Ca. 11 Tage bei aktuellem Verbrauch (EUR 300/Tag netto Liquiditätsabfluss)'],
    ]
    ptbl = Table(profil, colWidths=[5*cm, 12.5*cm])
    ptbl.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.white, GRAU_HELL]),
        ('GRID', (0,0), (-1,-1), 0.2, GRAU_MID),
        ('BACKGROUND', (1,14), (1,14), colors.HexColor("#FFE0E0")),
        ('TEXTCOLOR', (1,14), (1,14), ROT),
        ('FONTNAME', (1,14), (1,14), 'Helvetica-Bold'),
    ]))
    story.append(ptbl)
    story.append(PageBreak())

    # Filialübersicht
    story.append(Paragraph("D.2 Filialübersicht — Umsatz, Miete, Wareneinsatz", S['h1']))
    story.append(hr(FARBE_D))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("Jahresübersicht 2025 (geschätzt, aus Kassensystem):", S['h3']))
    filial_data = [
        ['Filiale', 'Adresse', 'Eröffnung', 'Umsatz', 'Miete p.a.', 'Wareneinsatz', 'Personal', 'Sonstige Kost.', 'Filial-EBIT', 'Bewertung'],
        ['F1 — Hermannplatz', 'Hermannpl. 14', 'Mrz. 2021', '320.000', '42.000\n(EUR 3.500/M)', '102.400', '88.000', '18.000', '+69.600', 'RENTABEL'],
        ['F2 — Boddinstraße', 'Boddinstr. 27', 'Aug. 2022', '230.000', '36.000\n(EUR 3.000/M)', '73.600', '64.000', '12.000', '+44.400', 'RENTABEL'],
        ['F3 — Sonnenallee', 'Sonnenallee 89b', 'Jan. 2024', '132.000', '62.400\n(EUR 5.200/M)', '42.200', '52.000', '9.800', '-34.400', 'VERLUST!\n(Mieterhöhung +40%)'],
        ['Overhead/HQ', '—', '—', '—', '—', '—', '32.000\n(GF + Admin)', '45.000\n(Lieferando/Wolt 12K;\nBuchhalt. 8K;\nSonstige)', '-77.000', '(Kopfkosten)'],
        ['GESAMT', '—', '—', '682.000', '140.400', '218.200', '236.000', '84.800', '+6.600 / -89.000\n(mit GF-Kosten)', ''],
    ]
    f_tbl = Table(filial_data, colWidths=[2.8*cm, 2.8*cm, 2*cm, 1.8*cm, 1.9*cm, 2.2*cm, 2.2*cm, 2.5*cm, 2.2*cm, 2.1*cm])
    f_style = tbl_style_zahlen()
    f_style.add('FONTSIZE', (0,0), (-1,-1), 7.5)
    f_style.add('BACKGROUND', (9,3), (9,3), colors.HexColor("#FFE0E0"))
    f_style.add('TEXTCOLOR', (9,3), (9,3), ROT)
    f_style.add('FONTNAME', (9,3), (9,3), 'Helvetica-Bold')
    f_tbl.setStyle(f_style)
    story.append(f_tbl)
    story.append(Paragraph(
        "Anm.: Sonnenallee-Filiale verursacht Jahresverlust von EUR 34.400 vor Overhead. "
        "Mieterhöhung Sonnenallee ab Jan. 2024: +40% (EUR 3.700 auf EUR 5.200/Monat). "
        "Kein Sonderkündigungsrecht im Mietvertrag; Vertragslaufzeit bis Dez. 2027.",
        S['footnote']))
    story.append(PageBreak())

    # E-Mail-Kette
    story.append(Paragraph("D.3 E-Mail-Kette: Tarek-Yusuf Çelebi-Drebenstedt an RAin Wandelmoser", S['h1']))
    story.append(hr(FARBE_D))
    story.append(Spacer(1, 0.2*cm))

    def email_block(von, an, datum, betreff, text, farbe=None):
        data = [[
            Paragraph(
                f"<b>Von:</b> {von}<br/>"
                f"<b>An:</b> {an}<br/>"
                f"<b>Datum:</b> {datum}<br/>"
                f"<b>Betreff:</b> {betreff}<br/><br/>"
                f"{text}",
                S['courier'] if farbe else S['body_left']
            )
        ]]
        bg = farbe or colors.HexColor("#F8F8FF")
        tbl = Table(data, colWidths=[17*cm])
        tbl.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), bg),
            ('BOX', (0,0), (-1,-1), 0.5, GRAU_MID),
            ('TOPPADDING', (0,0), (-1,-1), 8),
            ('BOTTOMPADDING', (0,0), (-1,-1), 8),
            ('LEFTPADDING', (0,0), (-1,-1), 10),
            ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ]))
        return tbl

    story.append(email_block(
        "tarek.yusuf.cd@salaltbar.de",
        "info@ra-wandelmoser.de",
        "Mo, 27. April 2026, 23:41 Uhr",
        "DRINGEND bitte helfen!!!",
        "Guten abend frau Wandelmoser,\n\n"
        "ich bin total am Ende. Die Vermieterin Sonnenallee hat mir heut ein schreiben "
        "geschickt das sie fristlos kündigt wenn ich nicht bis 5. mai zahle. "
        "Das sind 18.400 euro die ich definitiv nicht hab. Auf dem Konto sind 3400 euro.\n\n"
        "Ich versteh das nicht ich hab doch meine Steuern fast alle gezahlt. "
        "Na ja also das Finanzamt hat auch noch eine Forderung von 8.900 euro "
        "glaub ich steht auf einem brief von letzter woche.\n\n"
        "Und jetzt hat mir auch der Frische-Kontor angerufen die liefern erstmal nicht "
        "mehr bis ich 12.800 euro zahle. Ohne Lieferung mach ich nix mehr umsatz!!\n\n"
        "bitte ich brauch hilfe!! Was soll ich machen?? Muss ich pleite anmelden??\n\n"
        "Tarek",
        colors.HexColor("#FFF8F0")
    ))
    story.append(Spacer(1, 0.3*cm))

    story.append(email_block(
        "c.wandelmoser@ra-wandelmoser.de",
        "tarek.yusuf.cd@salaltbar.de",
        "Di, 28. April 2026, 08:15 Uhr",
        "Re: DRINGEND bitte helfen!!! — Ersteinschätzung",
        "Sehr geehrter Herr Çelebi-Drebenstedt,\n\n"
        "ich habe Ihre Nachricht erhalten. Die Situation ist ernst, aber noch nicht "
        "hoffnungslos. Ich bitte Sie dringend, heute noch einen Termin in meiner "
        "Kanzlei zu vereinbaren.\n\n"
        "Vorab folgende wichtige Hinweise:\n"
        "1. Machen Sie sofort eine Aufstellung aller Schulden und des verfügbaren Geldes.\n"
        "2. Antworten Sie der Vermieterin NOCH NICHT, bevor wir gesprochen haben.\n"
        "3. Zahlen Sie nichts, bevor wir die Reihenfolge besprochen haben.\n\n"
        "Mein Stundensatz beträgt EUR 280,00 netto (zzgl. 19% MwSt.). "
        "Ich biete Ratenzahlung an. Bitte bringen Sie alle Verträge und Briefe mit.\n\n"
        "Mit freundlichen Grüßen\n"
        "Charlotte Wandelmoser, Rechtsanwältin",
        colors.HexColor("#F0F8FF")
    ))
    story.append(Spacer(1, 0.3*cm))

    story.append(email_block(
        "tarek.yusuf.cd@salaltbar.de",
        "c.wandelmoser@ra-wandelmoser.de",
        "Di, 28. April 2026, 09:02 Uhr",
        "Re: Re: DRINGEND bitte helfen!!!",
        "Danke!! ich komme um 14 uhr wenn das geht? Heute?\n\n"
        "Ich habe noch eine Frage kann man das irgendwie regeln das ich nicht "
        "Insolvenz anmelden muss?? Ich hab gehört da gibt es ein neues gesetz "
        "das man auch ohne insolvenz machen kann? Ein Kollege hat sowas gesagt "
        "aber ich weiss nicht genau.\n\n"
        "Kann ich auch einfach die Sonnenallee-Filiale zumachen?? Dann spare ich "
        "5200 euro im Monat. Aber da ist noch ein Mietvertrag bis 2027...\n\n"
        "Tarek",
        colors.HexColor("#FFF8F0")
    ))
    story.append(PageBreak())

    # Interner Vermerk Wandelmoser
    story.append(Paragraph("D.4 Interner Vermerk — RAin Wandelmoser", S['h1']))
    story.append(hr(FARBE_D))
    story.append(Spacer(1, 0.2*cm))

    for line in kanzlei_kopf_wandelmoser():
        story.append(line)
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "<b>INTERNER VERMERK — NICHT MANDANTENAKT</b>",
        S['warn']))
    story.append(Paragraph(
        "Az.: CW-2026-SALALTBAR | Datum: 28. April 2026<br/>"
        "Betreff: Erstgespräch Çelebi-Drebenstedt — Bewertung + Strategie",
        S['small']))
    story.append(hr())
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("1. Ersteindruck und Mandatsfähigkeit", S['h2']))
    story.append(Paragraph(
        "Der Mandant ist kaufmännisch überfordert — typischer Quereinsteiger aus dem "
        "IT-Bereich. Keine strukturierte Buchführung im engeren Sinne. Keine "
        "Liquiditätsplanung. Kontoauszüge in Papierform, unsortiert. "
        "Keine Kenntnis der Rücklagenpflicht nach § 5a Abs. 3 GmbHG bei UG. "
        "Keine 24-Monats-Planung. Erkennt die Schwere der Situation nicht vollständig.",
        S['body']))

    story.append(Paragraph("2. Rechtliche Erstbewertung", S['h2']))
    story.append(Paragraph(
        "<b>§ 1 StaRUG:</b> Gilt auch für UG-Geschäftsführer. Früherkennungspflicht "
        "wurde flagrant verletzt — kein Überwachungssystem, keine 24-Monats-Planung. "
        "Persönliches Haftungsrisiko nach §§ 43, 15b InsO.", S['body']))
    story.append(Paragraph(
        "<b>§ 15a InsO:</b> Dreiwochen-Frist. Zahlungsunfähigkeit muss geprüft werden. "
        "Kassenstand EUR 3.400, Verbindlichkeiten fällig (ca. EUR 43.300) — "
        "dies ist klassische Zahlungsunfähigkeit nach § 17 InsO, wenn mehr als 90% "
        "der Verbindlichkeiten nicht bezahlbar sind. Zu klären: Stundungen, "
        "Zahlungsvereinbarungen, Liquidierungsmöglichkeiten.",
        S['body']))
    story.append(Paragraph(
        "<b>StaRUG-Plan?</b> Unwahrscheinlich. Zu wenige Gläubiger im 'Plan'-Sinne. "
        "Kosten des StaRUG-Verfahrens (Anwalts-, Gerichtskosten) übersteigen "
        "voraussichtlich Nutzen. Eher: außergerichtliche Einigung oder "
        "Verbraucherinsolvenz analog (Kleinverfahren). Verweis an Reher Wennstedt "
        "nur wenn signifikant mehr Mittel gefunden werden.",
        S['body']))

    story.append(Paragraph("3. Honorar-Entscheidung", S['h2']))
    notiz2_data = [[
        Paragraph(
            "Pro bono?? Nein.\n\n"
            "Fester Stundensatz EUR 280 netto bleibt.\n"
            "ABER: Ratenzahlung angeboten — EUR 100/Woche ab Gespraechstag.\n\n"
            "Gruendsaetzlich: soziale Faelle sind schoen aber ich muss auch "
            "meine Bueromiete zahlen. Mal sehen wie es laeuft.\n\n"
            "Naechster Schritt: § 102-Warnschreiben + Drei-Wochen-Frist-Memo.",
            ParagraphStyle('notiz2', fontName='Times-Italic', fontSize=10,
                          leading=15, textColor=colors.HexColor("#1A0040"),
                          leftIndent=8)
        )
    ]]
    notiz2_tbl = Table(notiz2_data, colWidths=[17*cm])
    notiz2_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FFFDF0")),
        ('BOX', (0,0), (-1,-1), 1, FARBE_D),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(notiz2_tbl)
    story.append(PageBreak())

    # § 102 Warnschreiben Wandelmoser
    story.append(Paragraph("D.5 § 102 StaRUG-Warnschreiben — RAin Wandelmoser", S['h1']))
    story.append(hr(FARBE_D))
    story.append(Spacer(1, 0.2*cm))

    for line in kanzlei_kopf_wandelmoser():
        story.append(line)
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("<b>PER EINSCHREIBEN MIT RÜCKSCHEIN / PERSÖNLICH</b>", S['bold']))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "An:<br/>"
        "Herrn Tarek-Yusuf Çelebi-Drebenstedt<br/>"
        "Geschäftsführer der Salaltbar UG (haftungsbeschränkt)<br/>"
        "Hermannplatz 14<br/>"
        "12049 Berlin",
        S['body_left']))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("Berlin, 29. April 2026", S['right']))
    story.append(Spacer(1, 0.1*cm))
    story.append(Paragraph(
        "<b>Krisenfrüherkennungs-Hinweis gemäß § 102 StaRUG<br/>"
        "Az.: CW-2026-SALALTBAR</b>",
        S['h3']))
    story.append(hr())
    story.append(Spacer(1, 0.1*cm))

    story.append(Paragraph("Sehr geehrter Herr Çelebi-Drebenstedt,", S['body_left']))
    story.append(Spacer(1, 0.1*cm))

    story.append(Paragraph(
        "ich schreibe Ihnen in Ihrer Eigenschaft als alleinvertretungsberechtigter "
        "Geschäftsführer und Alleingesellschafter der Salaltbar UG (haftungsbeschränkt), "
        "Hermannplatz 14, 12049 Berlin (HRB 212 904 B, AG Charlottenburg). "
        "Im Rahmen des Erstgesprächs am 28. April 2026 habe ich Kenntnis von "
        "Tatsachen erlangt, die ich Ihnen gemäß meiner gesetzlichen Pflicht nach "
        "§ 102 des Gesetzes über den Stabilisierungs- und Restrukturierungsrahmen "
        "für Unternehmen (StaRUG) unverzüglich mitteilen muss.", S['body']))

    story.append(Paragraph("<b>A. Festgestellte Risikofaktoren</b>", S['h3']))
    risk_d = [
        ['Nr.', 'Risikofaktor', 'Rechtliche Folge'],
        ['1', 'Kassenbestand EUR 3.400 bei fälligen Verbindlichkeiten EUR 43.300', '§ 17 InsO: Zahlungsunfähigkeit droht / ggf. bereits eingetreten'],
        ['2', 'Kein Liquiditätsplan für 24 Monate (§ 1 StaRUG)', 'Pflichtverstoß als Geschäftsführer, Haftung § 43 GmbHG'],
        ['3', 'Rücklage nach § 5a Abs. 3 GmbHG nicht gebildet', 'Formaler Verstoß; Haftungsrisiko GF'],
        ['4', 'Verlustbringende Filiale Sonnenallee: -EUR 34.400 p.a.', 'Strategische Krise; keine Maßnahme eingeleitet'],
        ['5', 'Mietrückstand Sonnenallee EUR 18.400 (fristlose Kündigung angedroht)', 'Drohender Verlust Mietbesitz = Betriebsunterbrechung'],
        ['6', 'Lieferstopp Frische-Kontor Berlin GmbH (EUR 12.800 offen)', 'Unmittelbarer Betriebsstillstand-Risiko F1 + F2'],
        ['7', 'Steuerrückstände Finanzamt EUR 8.900 (USt)', '§ 69 AO: Haftungsrisiko GF persönlich'],
    ]
    rd_tbl = Table(risk_d, colWidths=[0.8*cm, 7.5*cm, 9.2*cm])
    rd_style = tbl_style_standard()
    for i in range(1, 4):
        rd_style.add('BACKGROUND', (2,i), (2,i), colors.HexColor("#FFE0E0"))
    rd_tbl.setStyle(rd_style)
    story.append(rd_tbl)
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("<b>B. Drei-Wochen-Frist § 15a InsO — ACHTUNG!</b>", S['warn']))
    story.append(Paragraph(
        "Soweit Zahlungsunfähigkeit im Sinne des § 17 InsO bereits eingetreten ist, "
        "sind Sie als Geschäftsführer nach § 15a Abs. 1 InsO verpflichtet, "
        "<b>SPÄTESTENS INNERHALB VON DREI WOCHEN</b> einen Insolvenzantrag beim "
        "zuständigen Insolvenzgericht (Amtsgericht Charlottenburg) zu stellen. "
        "Diese Frist beginnt mit dem Zeitpunkt, zu dem Sie Kenntnis von der "
        "Zahlungsunfähigkeit hatten oder hätten haben müssen.", S['body']))

    story.append(Paragraph(
        "Wenn die Zahlungsunfähigkeit am 28. April 2026 (Datum Erstgespräch) "
        "festgestellt wurde, läuft die Drei-Wochen-Frist am <b>19. Mai 2026</b> ab. "
        "<b>SIE MÜSSEN JETZT ENTSCHEIDEN.</b>",
        S['warn']))

    story.append(Paragraph("<b>C. Handlungsoptionen (Überblick)</b>", S['h3']))
    optionen = [
        ['Option', 'Voraussetzung', 'Empfehlung'],
        ['Außergerichtliche Einigung mit allen Gläubigern', 'Zustimmung aller Gläubiger; Liquiditätszuführung (Darlehen?)', 'PRÜFEN — wenn alle Gläubiger zustimmen'],
        ['StaRUG-Plan (§§ 2 ff. StaRUG)', 'Drohende ZU (§ 18 InsO); ausreichende Gläubigeranzahl; Plankosten', 'UNWAHRSCHEINLICH — Kosten > Nutzen bei dieser Größe'],
        ['Sofortige Schließung Filiale Sonnenallee', 'Auflösung Mietvertrag; Abfindungen; sofortige Kostenersparnis', 'DRINGEND PRÜFEN — spart EUR 5.200/Monat Miete'],
        ['Regelinsolvenz § 11 InsO', 'Stellen des Insolvenzantrags; Verlust der Geschäftsführung', 'Ultima Ratio wenn keine außergerichtliche Lösung'],
        ['Verbraucherinsolvenz GF persönlich', 'Nur wenn GF persönlich haftet und keine Unternehmensrettung', 'Parallel zu prüfen'],
    ]
    opt_tbl = Table(optionen, colWidths=[3.8*cm, 6.5*cm, 7.2*cm])
    opt_tbl.setStyle(tbl_style_standard())
    story.append(opt_tbl)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph(
        "Bitte bestätigen Sie den Empfang dieses Schreibens und melden sich "
        "spätestens bis Freitag, 2. Mai 2026, 17:00 Uhr, bei mir.",
        S['body']))
    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph("Berlin, 29. April 2026", S['right']))
    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph(
        "Charlotte Wandelmoser, Rechtsanwältin",
        ParagraphStyle('sig6', fontName='Times-Italic', fontSize=11,
                       alignment=TA_RIGHT, textColor=DUNKELBLAU)
    ))
    story.append(PageBreak())

    # Cash-Flow-Skizze handschriftlich
    story.append(Paragraph("D.6 Cash-Flow-Skizze (handschriftlich, eingescannt)", S['h1']))
    story.append(hr(FARBE_D))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("Original: Tarek-Yusuf Çelebi-Drebenstedt, geschrieben 28. April 2026 (Erstgespräch):", S['small']))
    story.append(Spacer(1, 0.2*cm))

    skizze_data = [[
        Paragraph(
            "Mein Geld Stand heute (28.4.26):\n\n"
            "Konto:  3.400 EUR\n"
            "Kasse Hermannpl: ca 800 EUR (nicht gezählt)\n"
            "Kasse Boddin: ca 400 EUR\n"
            "Kasse Sonne: ca 200 EUR\n"
            "------------------\n"
            "GESAMT ca. 4.800 EUR\n\n"
            "Was ich zahlen muss:\n"
            "Miete Sonne: 18.400 (SOFORT!!)\n"
            "Frische-Kontor: 12.800 (oder kein liefern)\n"
            "Finanzamt: 8.900\n"
            "Wolt: 3.200\n"
            "Personal Mitte Mai: ca. 7.200\n"
            "------------------\n"
            "GESAMT Schulden: 50.500 EUR\n\n"
            "DIFFERENZ: -45.700 EUR !!! SCHLIMM !!\n\n"
            "Einnahmen nächste Woche ca: 4.200 EUR\n"
            "(Wetter gut, Hermannpl läuft)\n\n"
            "Reichweite: 4800 / 300 tägl. = 16 tage???\n"
            "Ne eigentlich 11 weil Wolt u. Kasse ungenau",
            ParagraphStyle('handskizze', font