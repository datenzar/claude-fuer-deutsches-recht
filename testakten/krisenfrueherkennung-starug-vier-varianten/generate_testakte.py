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
    s['h_kapitel'] = ParagraphStyle('h_kapitel', fontName='Helvetica-Bold', fontSize=18,
        leading=24, alignment=TA_CENTER, textColor=DUNKELBLAU, spaceAfter=6, spaceBefore=8)
    s['subtitle_cap'] = ParagraphStyle('subtitle_cap', fontName='Helvetica', fontSize=12,
        leading=16, alignment=TA_CENTER, textColor=GRAU_DUNKEL, spaceAfter=10)
    return s

S = make_styles()

# ─── Hilfsfunktionen ──────────────────────────────────────────────────────────

def hr(color=GRAU_MID, thickness=0.5, spaceB=6, spaceA=6):
    return HRFlowable(width="100%", thickness=thickness, color=color,
                      spaceAfter=spaceA, spaceBefore=spaceB)

def fax_block(lines):
    """Courier-Block mit ====-Rahmen wie Faxkopf."""
    result = []
    result.append(Paragraph("=" * 70, S['courier']))
    for line in lines:
        result.append(Paragraph(line if line else " ", S['courier']))
    result.append(Paragraph("=" * 70, S['courier']))
    return result

def fax_to_story(story, lines):
    """Adds a fax_block directly to the story."""
    story.extend(fax_block(lines))

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
    story.append(Paragraph("Original: Tarek-Yusuf Celebi-Drebenstedt, geschrieben 28. April 2026 (Erstgespraech):", S['small']))
    story.append(Spacer(1, 0.2*cm))

    skizze_text = (
        "Mein Geld Stand heute (28.4.26):\n\n"
        "Konto:  3.400 EUR\n"
        "Kasse Hermannpl: ca 800 EUR\n"
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
        "Einnahmen naechste Woche ca: 4.200 EUR\n"
        "(Wetter gut, Hermannpl laeuft)\n\n"
        "Reichweite: 4800 / 300 taegl. = 16 tage???\n"
        "Ne eigentlich 11 weil Wolt u. Kasse ungenau"
    )
    skizze_style = ParagraphStyle(
        'handskizze', fontName='Times-Italic', fontSize=10,
        leading=16, textColor=colors.HexColor('#1A1A80'),
        leftIndent=10, whiteSpace='pre'
    )
    skizze_data = [[Paragraph(skizze_text.replace('\n', '<br/>'), skizze_style)]]
    skizze_tbl = Table(skizze_data, colWidths=[16*cm])
    skizze_tbl.setStyle(TableStyle([
        ('BOX', (0,0),(0,0), 2, colors.HexColor('#1A1A80')),
        ('BACKGROUND', (0,0),(0,0), colors.HexColor('#FAFAEE')),
        ('PADDING', (0,0),(0,0), 12),
        ('VALIGN', (0,0),(-1,-1), 'TOP'),
    ]))
    story.append(skizze_tbl)
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "<i>Anmerkung RAin Wandelmoser: Handschrift des Mandanten, Inhalt plausibel, "
        "Reichweite 11 Tage bestaetigt eigene Einschaetzung ZU-Risiko. "
        "Original zu den Handakten.</i>",
        S['small']))
    story.append(PageBreak())

    # E-Mail-Kette Tarek-Yusuf
    story.append(Paragraph("D.7 E-Mail-Kette Tarek-Yusuf Celebi-Drebenstedt an RAin Wandelmoser", S['h1']))
    story.append(hr(FARBE_D))
    story.append(Spacer(1, 0.2*cm))

    for label, val in [("Von","tarek.celebi@salaltbar.de"),("An","wandelmoser@kanzlei-wandelmoser.de"),
                        ("Datum","25. April 2026, 23:47 Uhr"),("Betreff","hilfe ich weiss nicht mehr weiter")]:
        row_tbl = Table([[Paragraph(f"<b>{label}:</b>", S['small']), Paragraph(val, S['small'])]],
                        colWidths=[2.5*cm, 14*cm])
        row_tbl.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
        story.append(row_tbl)
    story.append(Spacer(1, 0.15*cm))

    mail1_lines = [
        "=== E-MAIL (eingehend) ===",
        "",
        "hallo frau wandelmoser",
        "",
        "ich war heute beim steuerberater und der hat mir gesagt ich soll unbedingt",
        "zu einem anwalt gehen wegen meiner firma. ich hab drei filialen salat-bar",
        "in neukoelln und die zahlen sich kaum noch.",
        "die miete bei der sonnenallee hat sich erhoeht und ich weiss gar nicht",
        "wie ich das zahlen soll. der lieferant schickt auch keine ware mehr",
        "wenn ich nicht zahle.",
        "",
        "bitte ich brauch hilfe!! bitte bitte bitte.",
        "ich hab auch kinder und meine frau weiss von nichts.",
        "was soll ich jetzt tun??",
        "",
        "danke",
        "Tarek",
        "",
        "PS: mein steuerberater hat das hier hingelegt: ss102 StaRUG ??",
    ]
    story.extend(fax_block(mail1_lines))
    story.append(Spacer(1, 0.3*cm))

    for label, val in [("Von","tarek.celebi@salaltbar.de"),("An","wandelmoser@kanzlei-wandelmoser.de"),
                        ("Datum","26. April 2026, 08:12 Uhr"),("Betreff","Re: hilfe ich weiss nicht mehr weiter")]:
        row_tbl = Table([[Paragraph(f"<b>{label}:</b>", S['small']), Paragraph(val, S['small'])]],
                        colWidths=[2.5*cm, 14*cm])
        row_tbl.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
        story.append(row_tbl)
    story.append(Spacer(1, 0.15*cm))

    mail2_lines = [
        "=== E-MAIL (eingehend) ===",
        "",
        "frau wandelmoser nochmal ich",
        "",
        "entschuldigung dass ich so viele mails schicke aber ich hab heute frueh",
        "einen brief vom vermieter gekriegt. er kuendigt fristlos!",
        "sagt ich hab 3 monate miete nicht gezahlt.",
        "das stimmt gar nicht weil januar hab ich gezahlt, aber februar",
        "und maerz... stimmt, da hab ich kein geld gehabt.",
        "",
        "der brief sagt ich muss raus bis 15. mai 2026. das ist in 3 wochen!!!!",
        "was mache ich jetzt mit den mitarbeitern?",
        "die filiale laeuft mittwochs immer gut wenn markt ist.",
        "",
        "tarek",
        "",
        "PS: sry fuer rechtschreibung schreibe vom handy",
    ]
    story.extend(fax_block(mail2_lines))
    story.append(PageBreak())

    # Filial-Uebersicht-Tabelle
    story.append(Paragraph("D.8 Filial-Uebersicht (Umsaetze, Miete, Wareneinsatz)", S['h1']))
    story.append(hr(FARBE_D))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "Stand: April 2026 (geschaetzte Werte lt. Mandantenangaben, nicht testiert)",
        S['small']))
    story.append(Spacer(1, 0.2*cm))

    filial_data = [
        ['Kennzahl', 'F1: Hermannplatz', 'F2: Boddinstrasse', 'F3: Sonnenallee', 'GESAMT'],
        ['Eroeffnet', 'Maerz 2023', 'Oktober 2023', 'April 2024', 'seit 2023'],
        ['Sitzplaetze', '28', '18', '22', '68'],
        ['Mitarbeiter (FTE)', '5,5', '3,0', '4,0', '12,5 (+1 GF)'],
        ['Umsatz Apr 2026 (EUR)', '18.400', '11.200', '8.600', '38.200'],
        ['Umsatz Avg/Monat 2025 (EUR)', '20.100', '12.400', '10.200', '42.700'],
        ['Miete kalt (EUR/Mon)', '3.800', '2.400', '5.200', '11.400'],
        ['Wareneinsatz (EUR/Mon)', '7.200', '4.800', '4.100', '16.100'],
        ['Personal (EUR/Mon)', '5.800', '3.200', '4.200', '13.200'],
        ['Sonstige Kosten (EUR/Mon)', '1.200', '900', '1.100', '3.200'],
        ['Summe Kosten (EUR/Mon)', '18.000', '11.300', '14.600', '43.900'],
        ['EBITDA (EUR/Mon)', '+400', '-100', '-6.000', '-5.700'],
        ['Miete-Rueckstand (EUR)', '0', '0', '18.400 (3 Mon)', '18.400'],
        ['Mietvertrag', 'bis 31.12.2027', 'monatl. kuendbar', 'bis 31.12.2026', '---'],
        ['Kuendigungsrisiko', 'GERING', 'MITTEL', 'HOCH (fristlos!)', '---'],
    ]
    filial_tbl = Table(filial_data, colWidths=[4.2*cm, 2.9*cm, 2.9*cm, 2.9*cm, 2.6*cm])
    filial_style = tbl_style_standard()
    filial_style.add('BACKGROUND', (4,0),(4,-1), colors.HexColor('#EEF4FF'))
    filial_style.add('BACKGROUND', (3,1),(3,-1), colors.HexColor('#FFF0F0'))
    filial_style.add('TEXTCOLOR', (1,11),(3,11), ROT)
    filial_style.add('FONTNAME', (0,0),(0,-1), 'Helvetica-Bold')
    filial_tbl.setStyle(filial_style)
    story.append(filial_tbl)
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "<b>Schlussfolgerung:</b> F3 Sonnenallee vernichtet EUR 6.000/Monat. "
        "Sofortige Schliessungspruefung (Kuendigungsrecht bereits vorhanden) "
        "koennte monatliches Defizit von EUR 5.700 auf EUR 300 reduzieren. "
        "Gleichzeitig: Verlust von 4 Arbeitsplaetzen.",
        S['body']))
    story.append(PageBreak())

    # Interner Vermerk Wandelmoser
    story.append(Paragraph("D.9 Interner Vermerk RAin Wandelmoser", S['h1']))
    story.append(hr(FARBE_D))
    story.append(Spacer(1, 0.2*cm))

    vermerk_lines = [
        "KANZLEI CHARLOTTE WANDELMOSER -- INTERNER VERMERK",
        "VERTRAULICH -- NUR FUER KANZLEIAKTEN",
        "",
        "Mandat: Salaltbar UG (haftungsbeschraenkt) / GF Celebi-Drebenstedt",
        "Datum: 28. April 2026",
        "Bearbeiter: RAin C. Wandelmoser",
        "",
        "GEBUEHREN / HONORAR:",
        "Erstgespraech (60 min): EUR 280,00 netto + MwSt.",
        "Folgemandat: Stundensatz EUR 280,00 netto.",
        "",
        "Frage Pro Bono: NEIN.",
        "Begruendung: Kein soziales Notfall-Mandat im engeren Sinne;",
        "GF hat drei Jahre lang Risiken ignoriert.",
        "RATENZAHLUNG anbieten: EUR 500 sofort, dann EUR 280/Monat.",
        "Mandatsuebernehme-Vereinbarung heute unterschreiben lassen.",
        "",
        "WEITERVERWEISUNG: Falls StaRUG-Plan noetig (unwahrscheinlich",
        "bei dieser Groesse): Verweis an Reher Wennstedt Hamburg",
        "(Dr. Tjark Reher-Bornholmsen).",
        "",
        "NAECHSTE SCHRITTE:",
        "1. Mandatsannahme-Schreiben + Vollmacht heute oder 29.04.",
        "2. ss 102 StaRUG-Schreiben an GF (foermliche Warnung).",
        "3. Drei-Wochen-Frist ss 15a InsO endet 19.05.2026.",
        "4. Bis 02.05.: Entscheidung Schliess. F3 Sonnenallee.",
        "5. Bei Weitermachen: 13-Wochen-Liquiditaetsplan erstellen.",
        "",
        "RISIKOFAKTOREN MANDAT:",
        "- Mandant kfm. ueberfordert, Kommunikation per WhatsApp/E-Mail nachts",
        "- Ehefrau von Krise unwissend",
        "- Steuerrueckstaende: persoenl. Haftung GF nach ss 69 AO",
        "- Lieferstopp: Betriebsunterbrechung F1+F2 sofort moeglich",
    ]
    story.extend(fax_block(vermerk_lines))
    story.append(PageBreak())

    # Fruehwarnsystem-Light fuer UGs
    story.append(Paragraph("D.10 Fruehwarnsystem-Light-Vorlage fuer UGs (vereinfachtes 24-Monats-Sheet)", S['h1']))
    story.append(hr(FARBE_D))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Diese Vorlage richtet sich an Geschaeftsfuehrer kleiner UGs und GmbHs "
        "ohne kaufmaennische Ausbildung. Sie ist kein Ersatz fuer professionelle Beratung, "
        "hilft aber, Krisen-Fruehsignale zu erkennen und die ss 1 StaRUG-Pflicht zu erfuellen.",
        S['body']))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("SCHRITT 1: Kassensturz (monatlich, 1. des Monats)", S['h2']))
    kasse_data = [
        ['Position', 'Betrag (EUR)', 'Kommentar'],
        ['Kontostand(e) alle Geschaeftskonten', '________', 'Alle Konten addieren'],
        ['Bargeld (alle Kassen)', '________', 'Zahlen, nicht schaetzen!'],
        ['Forderungen faellig < 14 Tage', '________', 'Nur wenn sicher eingehend'],
        ['SUMME VERFUEGBAR (A+B+C)', '________', ''],
        ['Miete(n) naechster Monat', '________', 'Alle Filialen'],
        ['Personalkosten naechster Monat', '________', 'Brutto + SV-Arbeitgeberanteil'],
        ['Wareneinkauf naechste 4 Wochen', '________', 'lt. Bestellplan'],
        ['Faellige Lieferantenrechnungen', '________', 'Ueberfaellig zaehlt doppelt!'],
        ['Steuern/SV faellig naechste 4 Wochen', '________', 'USt, LSt, SV'],
        ['SUMME PFLICHTZAHLUNGEN', '________', 'Summe D-H'],
        ['NETTO-LIQUIDITAET (A-E)', '________', 'Wenn negativ: SOFORT Anwalt!'],
        ['REICHWEITE (Tage)', '________', 'Verfuegbar / (Pflichtzahlungen/30)'],
    ]
    kasse_tbl = Table(kasse_data, colWidths=[7.5*cm, 3.5*cm, 5.5*cm])
    kasse_style = tbl_style_standard()
    kasse_style.add('BACKGROUND', (0,10),(2,11), colors.HexColor('#FFE8E8'))
    kasse_style.add('FONTNAME', (0,10),(0,11), 'Helvetica-Bold')
    kasse_tbl.setStyle(kasse_style)
    story.append(kasse_tbl)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("SCHRITT 2: Ampel-Check", S['h2']))
    ampel_data = [
        ['Ampel', 'Kriterium', 'Was tun?'],
        ['GRUEN', 'Reichweite > 60 Tage, keine Rueckstaende', 'Weiter monatlich pruefen'],
        ['GELB', 'Reichweite 30-60 Tage ODER ein Rueckstand', 'Steuerberater informieren, Kosten senken'],
        ['ROT', 'Reichweite < 30 Tage ODER mehrere Rueckstaende', 'SOFORT Rechtsanwalt! ss 15a InsO pruefen!'],
        ['SCHWARZ', 'Kein Geld fuer Loehne ODER Insolvenzantragspflicht', 'Insolvenzantrag innerhalb 3 Wochen!'],
    ]
    ampel_tbl = Table(ampel_data, colWidths=[2.2*cm, 8*cm, 6.3*cm])
    ampel_style = tbl_style_standard()
    ampel_style.add('BACKGROUND', (0,1),(0,1), colors.HexColor('#90EE90'))
    ampel_style.add('BACKGROUND', (0,2),(0,2), colors.HexColor('#FFD700'))
    ampel_style.add('BACKGROUND', (0,3),(0,3), colors.HexColor('#FF6B6B'))
    ampel_style.add('BACKGROUND', (0,4),(0,4), colors.HexColor('#333333'))
    ampel_style.add('TEXTCOLOR', (0,4),(0,4), colors.white)
    ampel_style.add('FONTNAME', (0,1),(-1,4), 'Helvetica-Bold')
    ampel_tbl.setStyle(ampel_style)
    story.append(ampel_tbl)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("SCHRITT 3: 24-Monats-Vorausschau (vereinfacht)", S['h2']))
    story.append(Paragraph(
        "Tragen Sie fuer jeden der naechsten 24 Monate ein: "
        "erwartete Einnahmen, geplante Ausgaben, Differenz. "
        "Wenn in einem der 24 Monate die Differenz dauerhaft negativ ist, "
        "liegt 'drohende Zahlungsunfaehigkeit' (ss 18 InsO) vor -- "
        "und Sie duerfen bereits jetzt einen StaRUG-Plan einleiten.",
        S['body']))

    monate_headers = ['Monat', 'Einnahmen (EUR)', 'Ausgaben (EUR)', 'Saldo (EUR)', 'Ampel']
    monate_rows = [monate_headers]
    for i in range(1, 25):
        monate_rows.append([f'M+{i:02d}', '________', '________', '________', 'o'])
    monate_tbl = Table(monate_rows, colWidths=[2.0*cm, 3.5*cm, 3.5*cm, 3.5*cm, 2.0*cm])
    monate_style = tbl_style_standard()
    monate_style.add('FONTSIZE', (0,0),(-1,-1), 8)
    monate_tbl.setStyle(monate_style)
    story.append(monate_tbl)
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "<i>Hinweis: Dieses vereinfachte Sheet ersetzt KEINE Fortbestehensprognose "
        "nach IDW S 11. Es dient der eigenen Ersteinschaetzung. "
        "Lassen Sie die Prognose von einem Steuerberater pruefen.</i>",
        S['small']))
    story.append(PageBreak())


def build_vorlagen_annex(story):
    """Vorlagen-Annex -- gemeinsam fuer alle Varianten (~15 Seiten)"""
    story.append(Paragraph("VORLAGEN-ANNEX", S['h_kapitel']))
    story.append(Paragraph("Gemeinsame Vorlagen fuer alle vier Varianten", S['subtitle_cap']))
    story.append(hr(DUNKELBLAU, thickness=2))
    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph(
        "Die nachfolgenden Vorlagen sind praxiserprobte Muster fuer die Krisen-"
        "frueherkennung und das Krisenmanagement nach ss 1 StaRUG. "
        "Sie sind nicht mandantenbezogen und koennen nach Anpassung auf den Einzelfall "
        "verwendet werden. Alle Vorlagen sind als Arbeitsdokumente konzipiert.",
        S['body']))
    story.append(PageBreak())

    # V-1: ss 102 StaRUG-Standardwarnschreiben
    story.append(Paragraph("Anlage V-1: ss 102 StaRUG-Standardwarnschreiben (Volltext)", S['h1']))
    story.append(hr(DUNKELBLAU))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Dieses Muster richtet sich an Berater (Rechtsanwaelte, Steuerberater, Wirtschaftsprueferr), "
        "die im Rahmen ihrer Beratung Krisenzeichen feststellen und nach ss 102 StaRUG zur "
        "unverzueglichen Information des Geschaeftsleitungsorgans verpflichtet sind.",
        S['body']))
    story.append(Spacer(1, 0.3*cm))
    story.extend(kanzlei_kopf_rw())
    story.append(Spacer(1, 0.2*cm))

    for label, val in [
        ("An:", "[Unternehmen], vertreten durch die Geschaeftsfuehrung / den Vorstand"),
        ("Von:", "[Beraterkanzlei / Steuerberaterbüro / WP-Kanzlei]"),
        ("Datum:", "[Datum der Feststellung]"),
        ("Betreff:", "Gesetzliche Warnanzeige gemaeß ss 102 StaRUG -- VERTRAULICH"),
        ("Aktenzeichen:", "[Kanzlei-AZ]"),
    ]:
        az_tbl = Table([[Paragraph(f"<b>{label}</b>", S['small']), Paragraph(val, S['small'])]],
                       colWidths=[3*cm, 13.5*cm])
        az_tbl.setStyle(TableStyle([('FONTSIZE',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
        story.append(az_tbl)
    story.append(Spacer(1, 0.3*cm))
    story.append(HRFlowable(width='100%', thickness=0.5, color=GRAU_MID))
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("Sehr geehrte Damen und Herren,", S['body_left']))
    story.append(Spacer(1, 0.1*cm))

    warn_paragraphen = [
        ("I. Rechtsgrundlage und Anlass",
         "Im Rahmen unserer Beratungstaetigkeit fuer Ihr Unternehmen haben wir Kenntnis von "
         "Tatsachen erlangt, die nach unserer Einschaetzung auf bestandsgefaehrdende "
         "Entwicklungen im Sinne des ss 1 Abs. 1 Satz 3 StaRUG hindeuten. "
         "Wir sind daher verpflichtet, Sie gemaeß ss 102 Abs. 1 StaRUG unverzueglich "
         "und schriftlich zu informieren."),
        ("II. Festgestellte Risikoindikatoren",
         "Im Einzelnen haben wir folgende Risikofaktoren festgestellt: "
         "[HIER: konkrete Risikofaktoren eintragen -- z.B. negative Liquiditaetsentwicklung, "
         "Covenant-Bruch, Verlustanzeige ss 92 AktG / ss 49 Abs. 3 GmbHG, "
         "drohende Zahlungsunfaehigkeit ss 18 InsO, unzureichender 24-Monats-Planungshorizont]"),
        ("III. Ihre Pflichten nach ss 1 StaRUG",
         "Als Mitglied der Geschaeftsleitung sind Sie nach ss 1 Abs. 1 StaRUG verpflichtet, "
         "fortlaufend ueber Entwicklungen zu wachen, welche den Fortbestand des Unternehmens "
         "gefaehrden koennen. Dies umfasst insbesondere: (1) Einrichtung eines angemessenen "
         "Risikofrueherkennungssystems, (2) Aufstellung und laufende Aktualisierung eines "
         "Liquiditaetsplans fuer mindestens 24 Monate, (3) Einleitung geeigneter Gegenmassnahmen, "
         "(4) fruehzeitige Einbeziehung von Sanierungsberatern und Glaeubigern. "
         "Ein Verstoss kann zu Haftung nach ss 43 Abs. 2 GmbHG / ss 93 AktG fuehren."),
        ("IV. Erforderliche Massnahmen",
         "Wir empfehlen dringend folgende Massnahmen unverzueglich einzuleiten: "
         "[HIER: konkrete Handlungsempfehlungen eintragen -- z.B. Erstellung 13-Wochen-Plan, "
         "Bankenrunde einberufen, StaRUG-Berater mandatieren, Sanierungsgutachten beauftragen, "
         "Anzeige Restrukturierungssache ss 31 StaRUG]. "
         "Wir stehen Ihnen fuer die Umsetzung zur Verfuegung."),
        ("V. Haftungshinweis und Vertraulichkeit",
         "Dieses Schreiben erfolgt im Rahmen unserer gesetzlichen Pflicht nach ss 102 Abs. 1 StaRUG. "
         "Es entbindet Sie nicht von eigenen Handlungspflichten. "
         "Bitte bestaetigen Sie den Erhalt dieses Schreibens schriftlich."),
    ]
    for titel, text in warn_paragraphen:
        story.append(Paragraph(f"<b>{titel}</b>", S['h3']))
        story.append(Paragraph(text, S['body']))
        story.append(Spacer(1, 0.15*cm))

    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("[Ort], [Datum]", S['right']))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("[Unterschrift Berater / Kanzleistempel]",
                            ParagraphStyle('sig_t', fontName='Times-Italic', fontSize=11,
                                           alignment=TA_RIGHT, textColor=DUNKELBLAU)))
    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph(
        "<b>Empfangsbestaetigung:</b><br/>"
        "Ich/Wir bestaetigen den Empfang dieses Schreibens am: ________________<br/><br/>"
        "Unterschrift Geschaeftsfuehrung: ________________________________<br/><br/>"
        "Name in Druckbuchstaben: _______________________________________",
        ParagraphStyle('empf', fontName='Helvetica', fontSize=9, leading=16,
                       borderPad=8, borderWidth=1, borderColor=GRAU_MID,
                       borderRadius=3, backColor=GRAU_HELL)))
    story.append(PageBreak())

    # V-2: 24-Monats-Liquiplan-Master-Template
    story.append(Paragraph("Anlage V-2: 24-Monats-Liquiditaetsplan -- Master-Template", S['h1']))
    story.append(hr(DUNKELBLAU))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Dieses Template entspricht dem Standard nach ss 1 StaRUG / IDW S 11 / IDW S 19. "
        "Es ist als Grundgeruest zu verstehen und muss auf den Einzelfall angepasst werden.",
        S['body']))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("<b>Teil A: Wochenbasis (W1-W13)</b>", S['h3']))
    wcols = ['Position', 'W01','W02','W03','W04','W05','W06','W07','W08','W09','W10','W11','W12','W13']
    wrows = [
        ['EINZAHLUNGEN','','','','','','','','','','','','',''],
        ['Umsatzerloese','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['Forderungseinzuege','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['Sonstige Einzahlungen','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['SUMME EINZAHLUNGEN (A)','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['AUSZAHLUNGEN','','','','','','','','','','','','',''],
        ['Lohn/Gehalt + SV-AG','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['Miete / Nebenkosten','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['Wareneinsatz','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['Energie/Versorgung','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['Zinsen/Tilgung Darlehen','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['Steuern + SV-AN','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['Investitionen/Capex','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['Sonstige Auszahlungen','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['SUMME AUSZAHLUNGEN (B)','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['NETTO CASHFLOW (A-B)','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['KASSENBESTAND ANFANG','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['KASSENBESTAND ENDE','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['MINDESTLIQUIDITAET','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['AMPEL (G/Y/R)','o','o','o','o','o','o','o','o','o','o','o','o','o'],
    ]
    col_w = [3.8*cm] + [0.9*cm]*13
    w_tbl = Table([wcols]+wrows, colWidths=col_w)
    w_style = tbl_style_zahlen()
    w_style.add('FONTSIZE',(0,0),(-1,-1),7)
    for i in [1,6]:
        w_style.add('BACKGROUND',(0,i),(13,i),colors.HexColor('#E8EFF8'))
        w_style.add('FONTNAME',(0,i),(0,i),'Helvetica-Bold')
    for i in [5,11,16,17,19]:
        w_style.add('FONTNAME',(0,i),(0,i),'Helvetica-Bold')
    w_tbl.setStyle(w_style)
    story.append(w_tbl)
    story.append(Spacer(1, 0.4*cm))

    story.append(Paragraph("<b>Teil B: Monatsbasis (M4-M12)</b>", S['h3']))
    m1cols = ['Position','M04','M05','M06','M07','M08','M09','M10','M11','M12']
    m1rows = [
        ['EINZAHLUNGEN','','','','','','','','',''],
        ['Umsatzerloese','_','_','_','_','_','_','_','_','_'],
        ['Forderungseinzuege','_','_','_','_','_','_','_','_','_'],
        ['SUMME EIN (A)','_','_','_','_','_','_','_','_','_'],
        ['AUSZAHLUNGEN','','','','','','','','',''],
        ['Personal + SV','_','_','_','_','_','_','_','_','_'],
        ['Miete','_','_','_','_','_','_','_','_','_'],
        ['Wareneinsatz','_','_','_','_','_','_','_','_','_'],
        ['Energie','_','_','_','_','_','_','_','_','_'],
        ['Schuldenservice','_','_','_','_','_','_','_','_','_'],
        ['Steuern/SV','_','_','_','_','_','_','_','_','_'],
        ['SUMME AUS (B)','_','_','_','_','_','_','_','_','_'],
        ['NETTO CF (A-B)','_','_','_','_','_','_','_','_','_'],
        ['KASSENBESTAND','_','_','_','_','_','_','_','_','_'],
        ['SZENARIO','B','B','B','B','B','B','B','B','B'],
    ]
    m1_tbl = Table([m1cols]+m1rows, colWidths=[3.0*cm]+[1.15*cm]*9)
    m1_style = tbl_style_zahlen()
    m1_style.add('FONTSIZE',(0,0),(-1,-1),8)
    m1_tbl.setStyle(m1_style)
    story.append(m1_tbl)
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("<b>Teil C: Monatsbasis (M13-M24)</b>", S['h3']))
    m2cols = ['Position','M13','M14','M15','M16','M17','M18','M19','M20','M21','M22','M23','M24']
    m2rows = [
        ['SUMME EIN (A)','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['SUMME AUS (B)','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['NETTO CF (A-B)','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['KASSENBESTAND','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['SZENARIO','B','B','B','B','B','B','B','B','B','B','B','B'],
    ]
    m2_tbl = Table([m2cols]+m2rows, colWidths=[3.0*cm]+[1.0*cm]*12)
    m2_style = tbl_style_zahlen()
    m2_style.add('FONTSIZE',(0,0),(-1,-1),8)
    m2_tbl.setStyle(m2_style)
    story.append(m2_tbl)
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Szenario-Codes: B = Base Case | S = Stress (-20% Umsatz) | SS = Severe Stress (-40%) | "
        "Mindestliquiditaet: 2-4 Wochen Fixkosten als Reserve",
        S['small']))
    story.append(PageBreak())

    # V-3: Geschaeftsfuehrer-Krisenprotokoll
    story.append(Paragraph("Anlage V-3: Geschaeftsfuehrer-Krisenprotokoll (Vorlage)", S['h1']))
    story.append(hr(DUNKELBLAU))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Das Krisenprotokoll dokumentiert, wann der Geschaeftsfuehrer von bestandsgefaehrdenden "
        "Entwicklungen Kenntnis erlangt hat und welche Massnahmen er eingeleitet hat. "
        "Es dient dem Nachweis pflichtgemaeßen Handelns (ss 1 StaRUG, ss 43 GmbHG, ss 93 AktG). "
        "Es sollte monatlich oder bei wesentlichen Veraenderungen ausgefuellt werden.",
        S['body']))
    story.append(Spacer(1, 0.2*cm))

    proto_data = [
        ['Eintrag Nr.', '[fortlaufend]'],
        ['Datum / Uhrzeit', '______________________'],
        ['Verfasser (GF/Vorstand)', '______________________'],
        ['Anwesende', '______________________'],
        ['Auslosendes Ereignis', '______________________'],
        ['Beschreibung der Risikolage', '[detaillierte Beschreibung, quantifiziert]'],
        ['Liquiditaetsreserve Stand heute', 'EUR __________ (Reichweite __ Tage)'],
        ['Eingeleitete Massnahmen', '[Liste der Massnahmen mit Verantwortlichen und Fristen]'],
        ['Externe Berater informiert', '[X] RA  [ ] StB  [ ] WP  [ ] Sanierungsberater  [ ] Banken'],
        ['Naechster Review-Termin', '______________________'],
        ['Unterschrift GF', '______________________'],
        ['Unterschrift weiterer GF', '______________________'],
    ]
    proto_tbl = Table(proto_data, colWidths=[5*cm, 11.5*cm])
    proto_style = tbl_style_standard()
    proto_style.add('FONTNAME',(0,0),(0,-1),'Helvetica-Bold')
    proto_tbl.setStyle(proto_style)
    story.append(proto_tbl)
    story.append(PageBreak())

    # V-4: Fruehwarn-KPI-Schwellen-Tabelle
    story.append(Paragraph("Anlage V-4: Fruehwarn-KPI-Schwellen-Tabelle", S['h1']))
    story.append(hr(DUNKELBLAU))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Die nachstehende Tabelle gibt Richtwerte fuer Fruehwarnindikatoren an. "
        "Die Schwellenwerte sind Orientierungswerte -- massgeblich ist stets die Gesamtschau.",
        S['body']))
    story.append(Spacer(1, 0.2*cm))

    kpi_data = [
        ['KPI', 'Einheit', 'Gruen\n(kein Bedarf)', 'Gelb\n(Monitoring)', 'Rot\n(Handlungsbedarf)', 'Schwarz\n(Insolvenz)'],
        ['Liquiditaetsreichweite', 'Tage', '> 60', '30-60', '14-30', '< 14'],
        ['13-Wochen-Cash-Coverage', 'Ratio', '> 1,3', '1,0-1,3', '0,8-1,0', '< 0,8'],
        ['Eigenkapitalquote', '% Bilanzsumme', '> 20%', '10-20%', '5-10%', '< 5%'],
        ['EBITDA-Marge', '% Umsatz', '> 8%', '3-8%', '0-3%', 'negativ'],
        ['Schuldendienstdeckung (DSCR)', 'Ratio', '> 1,5', '1,2-1,5', '1,0-1,2', '< 1,0'],
        ['Nettoverschuldung / EBITDA', 'x EBITDA', '< 3x', '3-5x', '5-7x', '> 7x'],
        ['VB ue. 90 Tage faellig', '% Gesamt-VB', '< 5%', '5-15%', '15-30%', '> 30%'],
        ['Umsatzrueckgang gg. Vorjahr', '% p.a.', '< 5%', '5-15%', '15-30%', '> 30%'],
        ['Covenant-Abstand', 'Headroom', '> 30%', '15-30%', '5-15%', '< 5%'],
        ['Working Capital Ratio', 'UV / kurz. VB', '> 1,5', '1,2-1,5', '1,0-1,2', '< 1,0'],
        ['Banken-Ampel', 'Rating-Klasse', 'Normal', 'Watch List', 'Sanierung', 'Abbau'],
        ['Lieferantenrueckstaende', 'EUR / Tage', '0 / 0', 'gering/30T', 'erheblich/60T', 'Lieferstopp'],
    ]
    kpi_tbl = Table(kpi_data, colWidths=[4.0*cm, 2.0*cm, 2.4*cm, 2.4*cm, 2.4*cm, 2.4*cm])
    kpi_style = tbl_style_standard()
    kpi_style.add('FONTSIZE',(0,0),(-1,-1),8)
    kpi_style.add('BACKGROUND',(2,1),(2,-1),colors.HexColor('#CCFFCC'))
    kpi_style.add('BACKGROUND',(3,1),(3,-1),colors.HexColor('#FFFFAA'))
    kpi_style.add('BACKGROUND',(4,1),(4,-1),colors.HexColor('#FFCCCC'))
    kpi_style.add('BACKGROUND',(5,1),(5,-1),colors.HexColor('#FF8888'))
    kpi_style.add('FONTNAME',(0,0),(-1,0),'Helvetica-Bold')
    kpi_style.add('FONTNAME',(0,0),(0,-1),'Helvetica-Bold')
    kpi_tbl.setStyle(kpi_style)
    story.append(kpi_tbl)
    story.append(PageBreak())

    # V-5: Restrukturierungsplan-Inhaltsverzeichnis-Master
    story.append(Paragraph("Anlage V-5: Restrukturierungsplan -- Inhaltsverzeichnis-Master", S['h1']))
    story.append(hr(DUNKELBLAU))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Mustergliederung nach ss 5 ff. StaRUG. Der Restrukturierungsplan besteht zwingend "
        "aus einem darstellenden Teil (ss 6 StaRUG) und einem gestaltenden Teil (ss 7 StaRUG).",
        S['body']))
    story.append(Spacer(1, 0.2*cm))

    itv_data = [
        ['Nr.', 'Gliederungspunkt', 'Rechtsgrundlage', 'Hinweise'],
        ['I.', 'DARSTELLENDER TEIL', 'ss 6 StaRUG', ''],
        ['1.', 'Unternehmensbeschreibung und Geschaeftsmodell', 'ss 6 Abs. 1 Nr. 1', 'Rechtsform, Organe, Standorte, Produkte'],
        ['2.', 'Krisenursachen und Krisendiagnose', 'ss 6 Abs. 1 Nr. 1', 'Abgrenzung Struktur-/Liquiditaetskrise'],
        ['3.', 'Finanzielle und wirtschaftliche Lage', 'ss 6 Abs. 1 Nr. 1', 'Bilanzen, GuV, Cashflow, Verbindlichkeiten'],
        ['4.', 'Fortbestehensprognose (24 Monate)', 'ss 6 Abs. 1 Nr. 1; IDW S 11', 'Zahlungsfaehigkeit im Planungszeitraum'],
        ['5.', 'Glaeubiger-Gruppen und Klassenbildung', 'ss 9 f. StaRUG', 'Mindestens gleich- + bestvorrangige Gruppe'],
        ['6.', 'Vergleichsrechnung / Liquidationswert', 'ss 6 Abs. 2 StaRUG', 'Verbesserung gg. Insolvenz nachweisen'],
        ['7.', 'Restrukturierungsmassnahmen im Ueberblick', 'ss 6 Abs. 1 Nr. 2', 'Operative + finanzielle Sanierungsbausteine'],
        ['8.', 'Planumsetzungsrisiken', 'ss 6 Abs. 1 Nr. 3', 'Risikomatrix, Sensitivitaetsanalyse'],
        ['II.', 'GESTALTENDER TEIL', 'ss 7 StaRUG', ''],
        ['9.', 'Forderungseingriffe je Gruppe', 'ss 7 Abs. 1 StaRUG', 'Stundung, Teilerlass, Umtausch, Sicherheit'],
        ['10.', 'Gruppenbildung und Stimmrechte', 'ss 9, 24 StaRUG', 'Gleichartige Rechtsstellung, keine Willkuer'],
        ['11.', 'Cross-Class-Cram-Down (falls geplant)', 'ss 26 StaRUG', 'Schlechterstellungsverbot, Mehrheitsvote'],
        ['12.', 'Kapitalmaßnahmen (falls geplant)', 'ss 7 Abs. 4 StaRUG', 'KH/-E, Debt-to-Equity'],
        ['13.', 'Bedingungen der Planwirksamkeit', 'ss 67 StaRUG', 'Vollzugsbedingungen, Long-Stop-Date'],
        ['III.', 'ANLAGEN', '', ''],
        ['14.', 'Sanierungsgutachten (IDW S 6)', '', 'Kurzgutachten oder Vollgutachten'],
        ['15.', 'Liquiditaetsplan 24 Monate', '', 'Base + Stress-Szenarien'],
        ['16.', 'Vertragsaenderungen / Term Sheets', '', 'Bankvereinbarungen, Anleiheanpassungen'],
        ['17.', 'Stimmrechtssimulation', '', 'Je Gruppe: Ja/Nein/Enthaltung'],
        ['18.', 'Zertifikat Restrukturierungsbeauftragter', 'ss 76 Abs. 4 StaRUG', 'Falls bestellt'],
    ]
    itv_tbl = Table(itv_data, colWidths=[1.0*cm, 6.5*cm, 4.5*cm, 4.5*cm])
    itv_style = tbl_style_standard()
    itv_style.add('FONTSIZE',(0,0),(-1,-1),8)
    itv_style.add('FONTNAME',(0,0),(-1,0),'Helvetica-Bold')
    for i in [1,10,15]:
        itv_style.add('BACKGROUND',(0,i),(-1,i),colors.HexColor('#D6E4F0'))
        itv_style.add('FONTNAME',(0,i),(-1,i),'Helvetica-Bold')
    itv_tbl.setStyle(itv_style)
    story.append(itv_tbl)
    story.append(PageBreak())


def build_foliensatz(story):
    """Foliensatz 'Restructuring Lounge Impulsvortrag' -- 8 Folien"""

    S_bold = ParagraphStyle('fbold', fontName='Helvetica-Bold', fontSize=13,
                             leading=18, textColor=DUNKELBLAU, spaceAfter=8)
    S_body_f = ParagraphStyle('fbody', fontName='Helvetica', fontSize=11,
                               leading=17, textColor=TEXT_SCHWARZ, spaceAfter=6)
    S_bullet_f = ParagraphStyle('fbullet', fontName='Helvetica', fontSize=11,
                                 leading=17, textColor=TEXT_SCHWARZ, leftIndent=20, spaceAfter=4)
    S_zitat = ParagraphStyle('fzitat', fontName='Times-Italic', fontSize=13,
                              leading=20, textColor=DUNKELBLAU, alignment=TA_CENTER,
                              spaceAfter=10, spaceBefore=10)
    S_big = ParagraphStyle('fbig', fontName='Helvetica-Bold', fontSize=20,
                            leading=26, textColor=ROT, alignment=TA_CENTER, spaceAfter=10)

    def render_folie(story, nr, titel, content_items):
        header_data = [[
            Paragraph("RESTRUCTURING LOUNGE HAMBURG  |  WAYES  |  28. Mai 2026",
                      ParagraphStyle('fhdr', fontName='Helvetica', fontSize=7,
                                     textColor=GRAU_DUNKEL, alignment=TA_LEFT)),
            Paragraph(f"Folie {nr} / 8",
                      ParagraphStyle('fnr', fontName='Helvetica-Bold', fontSize=8,
                                     textColor=DUNKELBLAU, alignment=TA_RIGHT))
        ]]
        hdr_tbl = Table(header_data, colWidths=[10*cm, 5.5*cm])
        hdr_tbl.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'MIDDLE'),('BOTTOMPADDING',(0,0),(-1,-1),3)]))

        all_content = [
            hdr_tbl,
            HRFlowable(width='100%', thickness=2.5, color=DUNKELBLAU, spaceAfter=8),
            Paragraph(titel, ParagraphStyle('ftitel', fontName='Helvetica-Bold', fontSize=16,
                                             textColor=DUNKELBLAU, leading=22, spaceAfter=10)),
            HRFlowable(width='100%', thickness=0.5, color=GRAU_MID, spaceAfter=8),
        ] + content_items + [
            Spacer(1, 0.2*cm),
            HRFlowable(width='100%', thickness=1, color=DUNKELBLAU, spaceBefore=6),
            Paragraph(
                "Dr. Tjark Reher-Bornholmsen  |  Reher Wennstedt Restrukturierung Partnerschaft mbB  |  Hamburg",
                ParagraphStyle('ffooter', fontName='Helvetica', fontSize=7,
                               textColor=GRAU_DUNKEL, alignment=TA_CENTER, spaceBefore=4)),
        ]

        outer_data = [[all_content]]
        outer_tbl = Table(outer_data, colWidths=[15.5*cm])
        outer_tbl.setStyle(TableStyle([
            ('BOX',(0,0),(0,0),3,DUNKELBLAU),
            ('PADDING',(0,0),(0,0),14),
            ('VALIGN',(0,0),(0,0),'TOP'),
            ('BACKGROUND',(0,0),(0,0),colors.white),
        ]))
        story.append(outer_tbl)
        story.append(PageBreak())

    # Folie 1: Hook
    render_folie(story, 1, "Hook: ss 1 StaRUG -- Das Gesetz, das alle vergessen", [
        Paragraph('"Ich dachte, ss 1 StaRUG gilt nur fuer grosse Konzerne."', S_zitat),
        Paragraph(
            "-- Tarek-Yusuf Celebi-Drebenstedt, GF Salaltbar UG, Berlin-Neukoelln, "
            "14 Mitarbeiter, Stammkapital EUR 1,00. Drei-Wochen-Frist laeuft.",
            ParagraphStyle('fq2', fontName='Helvetica', fontSize=9, textColor=GRAU_DUNKEL,
                           alignment=TA_CENTER, spaceAfter=12)),
        HRFlowable(width='100%', thickness=0.5, color=GRAU_MID),
        Spacer(1, 0.3*cm),
        Paragraph("<b>ss 1 StaRUG gilt fuer JEDEN Geschaeftsfuehrer.</b>", S_bold),
        Paragraph(
            "Unabhaengig von: Unternehmensgroesse  |  Rechtsform  |  Boersennotierung  |  "
            "Anzahl Mitarbeiter  |  Umsatzhoehe  |  Eigenkapitalausstattung",
            S_body_f),
        Spacer(1, 0.2*cm),
        Paragraph("Heute: Vier Faelle -- ein Gesetz -- vier Lehren.", S_big),
    ])

    # Folie 2: 24-Monats-These
    render_folie(story, 2, "These: 24 Monate sind der neue Standard", [
        Paragraph("<b>Der neue Standard: 24 Monate Planungshorizont</b>", S_bold),
        Paragraph("FRUEHER: Quartalsbericht + Jahresabschluss = ausreichend", S_bullet_f),
        Paragraph("HEUTE (seit StaRUG 2021): 24-Monats-Liquiditaetsplan ist Pflicht (ss 1 Abs. 1 StaRUG)", S_bullet_f),
        Paragraph("12 Monate: nur noch fuer Fortbestehensprognose (IDW S 11) -- NICHT ausreichend", S_bullet_f),
        Paragraph("24-Monats-Plan muss: rollierend / quartalsweise aktualisiert / plausibilisiert sein", S_bullet_f),
        Paragraph("Wer keinen 24-Monats-Plan hat: verletzt bereits JETZT ss 1 StaRUG", S_bullet_f),
        Spacer(1, 0.3*cm),
        Table([
            ['Zeitraum', 'Standard', 'Instrument'],
            ['W01-W13 (wochenweise)', 'Minimum bei Krise', '13-Wochen-Liquiditaetsplan'],
            ['M01-M12', 'Fortbestehensprognose', 'IDW S 11 (kurzfristig)'],
            ['M01-M24', 'StaRUG-Standard (ss 1)', '24-Monats-Liquiditaetsplan'],
            ['M01-M60', 'Strategische Planung', 'Businessplan / LRP'],
        ], colWidths=[4*cm, 5*cm, 6.5*cm]),
    ])

    # Folie 3: ss 102 StaRUG Warnpflicht
    warn_box_data = [[Paragraph(
        "<b>PRAXIS-TIPP:</b> ss 102-Schreiben raus, Empfangsbestaetigung einholen, "
        "zu den Handakten. Wer das nicht macht, haftet neben dem Mandanten.",
        ParagraphStyle('warnf', fontName='Helvetica', fontSize=10, textColor=ROT, leading=14))]]
    warn_box = Table(warn_box_data, colWidths=[13.5*cm])
    warn_box.setStyle(TableStyle([('BOX',(0,0),(0,0),2,ROT),('BACKGROUND',(0,0),(0,0),colors.HexColor('#FFF0F0')),('PADDING',(0,0),(0,0),8)]))

    render_folie(story, 3, "ss 102 StaRUG: Warnpflicht des Beraters", [
        Paragraph("<b>ss 102 Abs. 1 StaRUG -- Was bedeutet das?</b>", S_bold),
        Paragraph(
            "Berater (Rechtsanwaelte, Steuerberater, Wirtschaftspruefer), "
            "die im Rahmen ihrer Taetigkeit Kenntnis von bestandsgefaehrdenden Entwicklungen erlangen, "
            "MUESSEN die Geschaeftsleitung unverzueglich informieren.",
            S_body_f),
        Spacer(1, 0.2*cm),
        Paragraph("→ PFLICHT -- keine Option, kein Ermessen", S_bullet_f),
        Paragraph("→ Unverzueglich = ohne schuldhaftes Zoegern (i.d.R. wenige Tage)", S_bullet_f),
        Paragraph("→ Schriftlich empfohlen (Beweissicherung!)", S_bullet_f),
        Paragraph("→ Keine Ausnahme fuer langjaerige Mandatsbeziehung", S_bullet_f),
        Paragraph("→ Haftungsrisiko des Beraters bei Verstoss (ss 280 BGB / berufsrechtlich)", S_bullet_f),
        Spacer(1, 0.3*cm),
        warn_box,
    ])

    # Folie 4: Fall A
    render_folie(story, 4, "Fall A: VEYRA AI Foundation gGmbH -- KI-gGmbH in der Spendenkrise", [
        Table([
            ['Rechtsform', 'gGmbH (gemeinnützig)'],
            ['Problem', 'EU-Foerderauszahlung 9 Monate verzoegert / Spenden -40%'],
            ['Aktenzeichen', 'AG Frankfurt 810 RES 14/26'],
            ['StaRUG-Instrument', 'Anzeige Restrukturierungssache ss 31; Stundungsplan'],
            ['Lektion', 'ss 1 StaRUG gilt auch fuer gGmbH-Geschaeftsfuehrerinnen!'],
            ['Zitat GF', '"Brauche STAB-Anordnung VOR Q3-Foerderbescheid"'],
        ], colWidths=[4.5*cm, 11.0*cm]),
        Spacer(1, 0.2*cm),
        Paragraph(
            "Takeaway: Kein Umsatz, kein Gewinn, keine Aktionaere schuetzt nicht vor ss 1 StaRUG. "
            "Drohende Zahlungsunfaehigkeit in Monat 17 verpflichtet zur Krisen-Frueherkennung ab Tag 1.",
            S_body_f),
    ])

    # Folie 5: Fall B
    render_folie(story, 5, "Fall B: HARTMANNSCHMIDT AG -- Anleihe-Deadline in 18 Monaten", [
        Table([
            ['Rechtsform', 'AG (boersennotiert, Open Market)'],
            ['Problem', 'EUR 65 Mio. Anleihe in 18 Monaten faellig, Covenant-Bruch'],
            ['Aktenzeichen', 'AG Bamberg 53 RES 7/26'],
            ['StaRUG-Instrument', 'Cross-Class-Cram-Down ss 26 StaRUG (Anleihe-Restrukturierung)'],
            ['Lektion', 'IDW S 6 + IDW S 11 zusammen: zwei verschiedene Standards!'],
            ['Stolperstein', 'Familien-Anker + Schlechterstellungsverbot ss 64, 27 StaRUG'],
        ], colWidths=[4.5*cm, 11.0*cm]),
        Spacer(1, 0.2*cm),
        Paragraph(
            "Takeaway: 18 Monate klingt lang. In der Anleihe-Restrukturierung ist es knapp -- "
            "IDW S 6, Bankenrunde und Cross-Class-Cram-Down brauchen 9-12 Monate Vorlauf.",
            S_body_f),
    ])

    # Folie 6: Fall C
    render_folie(story, 6, "Fall C: NORDFELS POWER CELLS SE -- Aktivist trifft Stabilisierungsanordnung", [
        Table([
            ['Rechtsform', 'SE (boersennotiert)'],
            ['Problem', 'EUR 550 Mio. Finanzschulden, Grosskunde weg, Aktivist-Hedgefonds 11%'],
            ['Aktenzeichen', 'AG Stuttgart 14 RES 22/26 + Stabilisierungsanordnung'],
            ['StaRUG-Instrument', 'Stabilisierungsanordnung ss 49-59 + CRO + CramDown + KE'],
            ['Lektion', 'Aktivisten-Brief auf Englisch ist Eskalation -- sofort rechtlich reagieren!'],
            ['Lektion 2', 'Kapitalherabsetzung/-erhoehung gegen Streubesitz: ss 7 Abs. 4, 26 StaRUG'],
        ], colWidths=[4.5*cm, 11.0*cm]),
        Spacer(1, 0.2*cm),
        Paragraph(
            "Takeaway: Stabilisierungsanordnung ist das staerkste StaRUG-Werkzeug -- "
            "aber sie hat kurze Laufzeit. Restrukturierungsplan muss danach sofort stehen.",
            S_body_f),
    ])

    # Folie 7: Fall D
    render_folie(story, 7, "Fall D: SALALTBAR UG -- Der Klassiker, der alle Annahmen bricht", [
        Table([
            ['Rechtsform', 'UG (haftungsbeschraenkt), Stammkapital EUR 1,00'],
            ['Problem', 'Reichweite 11 Tage, Lieferstopp, fristlose Mietkuendigung'],
            ['Aktenzeichen', 'AG Charlottenburg 36 IN 412/26 (Insolvenzantrag droht)'],
            ['StaRUG-Instrument', 'Keines -- zu spaet. ss 15a InsO bereits relevant.'],
            ['Lektion', 'ss 1 StaRUG gilt AUCH fuer UG-GF -- Unwissen schuetzt nicht'],
            ['Lektion 2', 'Berater-Pflicht: RAin Wandelmoser muss ss 102-Schreiben versenden!'],
        ], colWidths=[4.5*cm, 11.0*cm]),
        Spacer(1, 0.2*cm),
        Paragraph(
            "Takeaway: Das Gesetz unterscheidet nicht zwischen EUR 1 und EUR 100.000 Stammkapital. "
            "Wer als GF keinen Liquiditaetsplan hat, verletzt ss 1 StaRUG und haftet persoenlich.",
            S_body_f),
    ])

    # Folie 8: Call-to-Action
    ta_bold_style = ParagraphStyle('ta_b_all', fontName='Helvetica-Bold', fontSize=12,
                                     textColor=DUNKELBLAU, spaceAfter=2)
    def make_ta_tbl(nr, bold_txt, body_txt):
        inner_tbl = Table([
            [Paragraph(bold_txt, ta_bold_style)],
            [Paragraph(body_txt, S_body_f)],
        ], colWidths=[13.1*cm])
        inner_tbl.setStyle(TableStyle([('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
        data = [[
            Paragraph(str(nr), ParagraphStyle(f'ta_nr_{nr}', fontName='Helvetica-Bold', fontSize=22,
                                         textColor=colors.white, alignment=TA_CENTER)),
            inner_tbl
        ]]
        tbl = Table(data, colWidths=[1.2*cm, 13.8*cm])
        tbl.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(0,0),DUNKELBLAU),
            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
            ('PADDING',(0,0),(0,0),8),
            ('PADDING',(1,0),(1,0),6),
            ('BOX',(0,0),(-1,-1),1,GRAU_MID),
        ]))
        return tbl

    render_folie(story, 8, "Call-to-Action: Was muessen Sie MORGEN tun?", [
        Paragraph("<b>Die drei Takeaways des Abends:</b>", S_bold),
        make_ta_tbl(1, "ss 1 StaRUG ist Pflicht -- nicht Option.",
                    "Jeder GF / Vorstand muss heute einen 24-Monats-Plan haben. Kein Plan = Haftung."),
        Spacer(1, 0.2*cm),
        make_ta_tbl(2, "ss 102 StaRUG: Berater, warnt Eure Mandanten schriftlich.",
                    "Das Schreiben ist Euer Schutz und der des Mandanten. Ohne Schreiben: volle Haftung."),
        Spacer(1, 0.2*cm),
        make_ta_tbl(3, "Wer das Heft des Handelns verliert, verliert StaRUG.",
                    "Der Stabilisierungsrahmen existiert nur, solange Handlungsfaehigkeit besteht."),
        Spacer(1, 0.3*cm),
        Paragraph(
            "Kontakt: Reher Wennstedt Restrukturierung Partnerschaft mbB  |  "
            "Hohe Bleichen 12  |  20354 Hamburg",
            ParagraphStyle('cta_c', fontName='Helvetica', fontSize=9,
                           textColor=GRAU_DUNKEL, alignment=TA_CENTER)),
    ])


def build_stundenaufstellung(story):
    """Stundenaufstellung Reher Wennstedt -- 2 Seiten Kostenillustration"""
    story.append(Paragraph("KOSTENUBERSICHT", S['h_kapitel']))
    story.append(Paragraph("Reher Wennstedt Restrukturierung Partnerschaft mbB", S['subtitle_cap']))
    story.append(hr(DUNKELBLAU, thickness=2))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Die nachstehende Stundenaufstellung illustriert den typischen Beratungsaufwand "
        "fuer eine Krisen-Frueherkennung nach ss 1 StaRUG. "
        "Die Angaben sind Richtwerte auf Basis der vier fiktiven Mandate.",
        S['body']))
    story.append(Spacer(1, 0.3*cm))
    story.extend(kanzlei_kopf_rw())
    story.append(Spacer(1, 0.2*cm))

    for label, val in [
        ('Kanzlei:', 'Reher Wennstedt Restrukturierung Partnerschaft mbB'),
        ('Adresse:', 'Hohe Bleichen 12, 20354 Hamburg'),
        ('Erstellungsdatum:', '22. Mai 2026'),
        ('Berichtszeitraum:', '1. Januar 2026 -- 22. Mai 2026'),
        ('Honorargrundlage:', 'Stundensatz-Vereinbarungen lt. Mandatsvertrag'),
    ]:
        m_tbl = Table([[Paragraph(f"<b>{label}</b>", S['small']), Paragraph(val, S['small'])]],
                      colWidths=[3.5*cm, 13*cm])
        m_tbl.setStyle(TableStyle([('FONTSIZE',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
        story.append(m_tbl)
    story.append(Spacer(1, 0.3*cm))
    story.append(HRFlowable(width='100%', thickness=0.5, color=GRAU_MID))
    story.append(Spacer(1, 0.3*cm))

    # Mandat A
    story.append(Paragraph("Mandat A: VEYRA AI Foundation gGmbH -- AZ AG Frankfurt 810 RES 14/26", S['h2']))
    std_a = [
        ['Datum', 'Taetigkeit', 'Bearbeiter', 'Std', 'Satz EUR/h', 'Betrag EUR'],
        ['05.01.2026', 'Erstgespraech Dr. Hellinghaus-Karpov, Sachverhaltsaufnahme', 'Dr. Reher-Bornholmsen', '2,0', '450', '900,00'],
        ['12.01.2026', 'Pruefung Vereinssatzung, Foerdervertrag EU-Horizont', 'Dr. Reher-Bornholmsen', '3,5', '450', '1.575,00'],
        ['19.01.2026', 'Erstellung ss 102 StaRUG-Warnschreiben, Abstimmung GF', 'Dr. Reher-Bornholmsen', '1,5', '450', '675,00'],
        ['26.01.2026', 'Ausarbeitung 24-Monats-Liquiditaetsplan (Basis)', 'Ass. M. Tolksdorf', '8,0', '280', '2.240,00'],
        ['02.02.2026', 'Stress-Szenario-Analyse (Spendeneinbruch / Foerder-Delay)', 'Ass. M. Tolksdorf', '4,0', '280', '1.120,00'],
        ['10.02.2026', 'Aufsichtsratssitzung Veyra AI: Praesentation Krisenanalyse', 'Dr. Reher-Bornholmsen', '3,0', '450', '1.350,00'],
        ['17.02.2026', 'Entwurf Stundungsvereinbarung Nordlicht Cloud GmbH', 'Dr. Reher-Bornholmsen', '2,5', '450', '1.125,00'],
        ['03.03.2026', 'Vorbereitung Anzeige Restrukturierungssache ss 31 StaRUG', 'Dr. Reher-Bornholmsen', '2,0', '450', '900,00'],
        ['10.03.2026', 'Einreichung AG Frankfurt, Abstimmung Gericht', 'Dr. Reher-Bornholmsen', '1,0', '450', '450,00'],
        ['', 'ZWISCHENSUMME MANDAT A', '', '27,5', '', '10.335,00'],
    ]
    a_tbl = Table(std_a, colWidths=[2.2*cm, 6.8*cm, 3.0*cm, 1.0*cm, 1.5*cm, 2.0*cm])
    a_style = tbl_style_zahlen()
    a_style.add('FONTNAME',(0,-1),(-1,-1),'Helvetica-Bold')
    a_style.add('BACKGROUND',(0,-1),(-1,-1),colors.HexColor('#E8EFF8'))
    a_style.add('FONTSIZE',(0,0),(-1,-1),8)
    a_tbl.setStyle(a_style)
    story.append(a_tbl)
    story.append(Spacer(1, 0.4*cm))

    # Mandat B
    story.append(Paragraph("Mandat B: HARTMANNSCHMIDT AG -- AZ AG Bamberg 53 RES 7/26", S['h2']))
    std_b = [
        ['Datum', 'Taetigkeit', 'Bearbeiter', 'Std', 'Satz EUR/h', 'Betrag EUR'],
        ['08.01.2026', 'Erstgespraech Vorstand (Hartmannschmidt + Luettke-Berens)', 'Dr. Reher-Bornholmsen', '3,0', '450', '1.350,00'],
        ['15.01.2026', 'Anleihebedingungen-Pruefung + Covenant-Analyse', 'Dr. Vellmer-Lutz', '5,0', '380', '1.900,00'],
        ['22.01.2026', 'Bankenrunde Vorbereitung (NorddeutscheLandesbank-Avis)', 'Dr. Reher-Bornholmsen', '2,5', '450', '1.125,00'],
        ['29.01.2026', 'Bankenrunde (Protokollierung)', 'Dr. Vellmer-Lutz', '4,0', '380', '1.520,00'],
        ['05.02.2026', 'Cross-Class-Cram-Down-Memo (Erstfassung)', 'Dr. Vellmer-Lutz', '6,0', '380', '2.280,00'],
        ['12.02.2026', 'HV-Vorbereitung Familien-Anker Hartmannschmidt Holding', 'Dr. Reher-Bornholmsen', '3,0', '450', '1.350,00'],
        ['26.02.2026', 'Anzeige AG Bamberg ss 31 StaRUG', 'Dr. Vellmer-Lutz', '2,0', '380', '760,00'],
        ['', 'ZWISCHENSUMME MANDAT B', '', '25,5', '', '10.285,00'],
    ]
    b_tbl = Table(std_b, colWidths=[2.2*cm, 6.8*cm, 3.0*cm, 1.0*cm, 1.5*cm, 2.0*cm])
    b_style = tbl_style_zahlen()
    b_style.add('FONTNAME',(0,-1),(-1,-1),'Helvetica-Bold')
    b_style.add('BACKGROUND',(0,-1),(-1,-1),colors.HexColor('#E8EFF8'))
    b_style.add('FONTSIZE',(0,0),(-1,-1),8)
    b_tbl.setStyle(b_style)
    story.append(b_tbl)
    story.append(PageBreak())

    # Mandat C
    story.append(Paragraph("Mandat C: NORDFELS POWER CELLS SE -- AZ AG Stuttgart 14 RES 22/26", S['h2']))
    std_c = [
        ['Datum', 'Taetigkeit', 'Bearbeiter', 'Std', 'Satz EUR/h', 'Betrag EUR'],
        ['02.01.2026', 'Krisenanalyse Vorstand (Vossbergen/Tannert-Brescia/Bietendüevel)', 'Dr. Reher-Bornholmsen', '4,0', '450', '1.800,00'],
        ['09.01.2026', 'Aktionaersstrukturanalyse + Aktivisten-Letter-Strategie', 'Prof. Dr. Hartfeld-Marwede', '6,0', '520', '3.120,00'],
        ['23.01.2026', 'Stabilisierungsanordnungs-Antrag ss 49-59 StaRUG (Volltext)', 'Prof. Dr. Hartfeld-Marwede', '10,0', '520', '5.200,00'],
        ['30.01.2026', 'Abstimmung AG Stuttgart (Richter, Geschaeftsstelle)', 'Dr. Reher-Bornholmsen', '3,0', '450', '1.350,00'],
        ['06.02.2026', 'Schlechterstellungsverbots-Gutachten (Erstfassung)', 'Prof. Dr. Hartfeld-Marwede', '8,0', '520', '4.160,00'],
        ['13.02.2026', 'Westshore Catalyst Investor-Letter-Response (englisch)', 'Dr. Reher-Bornholmsen', '3,0', '450', '1.350,00'],
        ['20.02.2026', '24-Monats-Liquiditaetsplan drei Szenarien', 'Ass. P. Rademann', '12,0', '280', '3.360,00'],
        ['27.02.2026', 'Restrukturierungsplan-Entwurf (Basis), gestaltender Teil', 'Prof. Dr. Hartfeld-Marwede', '14,0', '520', '7.280,00'],
        ['', 'ZWISCHENSUMME MANDAT C', '', '60,0', '', '27.620,00'],
    ]
    c_tbl = Table(std_c, colWidths=[2.2*cm, 6.8*cm, 3.0*cm, 1.0*cm, 1.5*cm, 2.0*cm])
    c_style = tbl_style_zahlen()
    c_style.add('FONTNAME',(0,-1),(-1,-1),'Helvetica-Bold')
    c_style.add('BACKGROUND',(0,-1),(-1,-1),colors.HexColor('#E8EFF8'))
    c_style.add('FONTSIZE',(0,0),(-1,-1),8)
    c_tbl.setStyle(c_style)
    story.append(c_tbl)
    story.append(Spacer(1, 0.4*cm))

    # Mandat D
    story.append(Paragraph("Mandat D: SALALTBAR UG -- Vergleichsperspektive (RAin Wandelmoser)", S['h2']))
    std_d = [
        ['Datum', 'Taetigkeit', 'Bearbeiter', 'Std', 'Satz EUR/h', 'Betrag EUR'],
        ['28.04.2026', 'Erstgespraech Celebi-Drebenstedt (60 min)', 'RAin Wandelmoser', '1,0', '280', '280,00'],
        ['29.04.2026', 'ss 102 StaRUG-Schreiben verfassen und versenden', 'RAin Wandelmoser', '1,5', '280', '420,00'],
        ['30.04.2026', 'Filialanalyse + Cash-Flow-Skizze auswerten', 'RAin Wandelmoser', '1,5', '280', '420,00'],
        ['02.05.2026', 'Folgegespraech (E-Mail + Tel.), ss 15a InsO-Memo', 'RAin Wandelmoser', '1,0', '280', '280,00'],
        ['05.05.2026', 'Schliessungsberatung Sonnenallee + mietrechtliche Optionen', 'RAin Wandelmoser', '2,0', '280', '560,00'],
        ['', 'ZWISCHENSUMME RAin Wandelmoser', '', '7,0', '', '1.960,00'],
    ]
    d_tbl = Table(std_d, colWidths=[2.2*cm, 6.8*cm, 3.0*cm, 1.0*cm, 1.5*cm, 2.0*cm])
    d_style = tbl_style_zahlen()
    d_style.add('FONTNAME',(0,-1),(-1,-1),'Helvetica-Bold')
    d_style.add('BACKGROUND',(0,-1),(-1,-1),colors.HexColor('#E8EFF8'))
    d_style.add('FONTSIZE',(0,0),(-1,-1),8)
    d_tbl.setStyle(d_style)
    story.append(d_tbl)
    story.append(Spacer(1, 0.4*cm))

    # Gesamt-Ueberblick
    story.append(Paragraph("<b>Gesamt-Ueberblick aller vier Mandate</b>", S['h2']))
    gesamt_data = [
        ['Mandat', 'Kanzlei', 'Stunden', 'Betrag netto EUR', 'MwSt 19%', 'Gesamt brutto EUR'],
        ['A: VEYRA AI Foundation', 'Reher Wennstedt', '27,5', '10.335,00', '1.963,65', '12.298,65'],
        ['B: HARTMANNSCHMIDT AG', 'Reher Wennstedt', '25,5', '10.285,00', '1.954,15', '12.239,15'],
        ['C: NORDFELS SE', 'Reher Wennstedt', '60,0', '27.620,00', '5.247,80', '32.867,80'],
        ['D: SALALTBAR UG', 'RAin Wandelmoser', '7,0', '1.960,00', '372,40', '2.332,40'],
        ['GESAMT', '', '120,0', '50.200,00', '9.538,00', '59.738,00'],
    ]
    gesamt_tbl = Table(gesamt_data, colWidths=[3.5*cm, 3.0*cm, 1.5*cm, 3.2*cm, 2.5*cm, 3.0*cm])
    gesamt_style = tbl_style_zahlen()
    gesamt_style.add('FONTNAME',(0,-1),(-1,-1),'Helvetica-Bold')
    gesamt_style.add('BACKGROUND',(0,-1),(-1,-1),DUNKELBLAU)
    gesamt_style.add('TEXTCOLOR',(0,-1),(-1,-1),colors.white)
    gesamt_style.add('FONTSIZE',(0,0),(-1,-1),8)
    gesamt_tbl.setStyle(gesamt_style)
    story.append(gesamt_tbl)
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "<i>Lehrperspektive: Die vier Faelle illustrieren das Kostenspektrum der StaRUG-Beratung -- "
        "von EUR 2.332 (Kleinstmandat UG) bis EUR 32.868 (komplexe SE mit Aktivist und Cross-Class-Cram-Down). "
        "Fruehzeitige Beratung ist stets guenstiger als das Krisenmanagement in der Insolvenz.</i>",
        S['small']))
    story.append(PageBreak())


def build_variante_a_extended(story):
    """Erweiterte Bestandteile Variante A -- Restrukturierungsplan-Entwurf + Gutachten."""
    AZ = "AG Frankfurt 810 RES 14/26"
    MANDANT = "VEYRA AI Foundation gGmbH"

    # Volltext Restrukturierungsplan-Entwurf (Auszug, darstellender Teil)
    story.append(Paragraph("A.6 Restrukturierungsplan-Entwurf — Darstellender Teil (Auszug)", S['h1']))
    story.append(hr(FARBE_A))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "<b>VERTRAULICH — NUR FÜR BETEILIGTE IM RESTRUKTURIERUNGSVERFAHREN</b><br/>"
        "VEYRA AI Foundation gGmbH — Restrukturierungsplan (Entwurf Stand: 15. Mai 2026)<br/>"
        f"Aktenzeichen: {AZ}",
        ParagraphStyle('rplan_head', fontName='Helvetica-Bold', fontSize=10,
                       leading=14, alignment=TA_CENTER, textColor=DUNKELBLAU)))
    story.append(Spacer(1, 0.3*cm))

    abschnitte_a = [
        ("§ 1 — Unternehmensbeschreibung und Träger des Plans",
         "Die Planschuldnerin VEYRA AI Foundation gGmbH (HRB 118 847, AG Frankfurt am Main) "
         "ist eine gemeinnützige GmbH nach § 5 Abs. 1 Nr. 9 KStG mit Sitz in Frankfurt am Main. "
         "Gründungsjahr: 2018. Die Gesellschaft forscht und entwickelt im Bereich quelloffener "
         "Künstlicher Intelligenz, betreibt mehrere internationale Datensatz-Projekte und "
         "koordiniert ein Netzwerk von ca. 340 freiwilligen Mitwirkenden weltweit. "
         "Mitarbeiter zum 31.12.2025: 32 Vollzeitäquivalente (VZÄ). "
         "Die Gesellschaft hat keine kommerziellen Umsatzerlöse. Einnahmen entstehen "
         "ausschließlich durch Spenden, EU-Forschungsförderung und projektgebundene "
         "Drittmittel. Die Planinitiatorin ist die Gesellschaft selbst (§ 2 Abs. 1 StaRUG)."),

        ("§ 2 — Krisenursachen und Krisendiagnose",
         "Die VEYRA AI Foundation gGmbH befindet sich im Stadium der drohenden "
         "Zahlungsunfähigkeit (§ 18 InsO). Krisenursachen im Einzelnen: "
         "(1) SPENDENRÜCKGANG: Die Spendeneinnahmen 2025 betrugen EUR 2,8 Mio., "
         "ein Rückgang von 22% gegenüber 2024 (EUR 3,6 Mio.). Prognose 2026: EUR 1,9 Mio. "
         "(-32% gg. 2025) aufgrund des allgemeinen Rückzugs institutioneller Tech-Spender. "
         "(2) FOERDERVERZOEGERUNG: Das EU-Forschungsprojekt HORIZON-VEYRA-2026 "
         "(Gesamtvolumen EUR 3,2 Mio.) hat nach positivem Bescheid (15.12.2025) "
         "mit der Auszahlung begonnen. Die Erste Tranche (EUR 840.000) sollte per "
         "15. Februar 2026 ausgezahlt werden. Die tatsächliche Auszahlung erfolgte "
         "noch nicht (Stand 15.05.2026); nach Auskunft der Förderagentur "
         "wird sie frühestens Oktober 2026 erfolgen (Verzug: 8 Monate). "
         "(3) GPU-CLOUD-KOSTEN: Der Vertrag mit Nordlicht Cloud GmbH "
         "(EUR 118.000 netto/Monat) läuft bis 31.12.2027 und kann nicht einseitig "
         "beendet werden ohne Schadensersatz (EUR 420.000 Vertragsstrafe). "
         "Die GPU-Kapazitäten werden für laufende Forschungsprojekte dringend benötigt."),

        ("§ 3 — Finanzielle Lage per 15. Mai 2026",
         "Kassenbestand alle Konten: EUR 312.400. Monatliche Fixkosten (ohne Investition): "
         "EUR 286.000 (davon Personalkosten EUR 148.000, GPU-Cloud EUR 118.000, Miete EUR 12.400, "
         "Sonstiges EUR 7.600). Offene Verbindlichkeiten gesamt: EUR 441.200. "
         "Geplante Einnahmen nächste 30 Tage: EUR 48.000 (Kleinspenden). "
         "Reichweite ohne Gegenmaßnahmen: 47 Tage. "
         "Drohende Zahlungsunfähigkeit tritt gemäß 24-Monats-Plan in Monat 17 (Oktober 2027) ein, "
         "unter Stress-Annahmen bereits Monat 11 (April 2027)."),

        ("§ 4 — Gläubigerstruktur und Klassenbildung",
         "Planbetroffene Gläubiger: (1) Nordlicht Cloud GmbH (GPU-Cloud-Dienstleistungen), "
         "Forderung laufend EUR 118.000/Monat, Restlaufzeit Vertrag 20 Monate = "
         "Nominalwert EUR 2.360.000 (laufende + zukünftige Leistungen). "
         "Kreditoren gesamt (nicht planbetroffene Forderungen) EUR 112.400. "
         "Die EU-Forschungsförderung ist keine Verbindlichkeit der Gesellschaft, "
         "sondern eine offene Forderung gg. die Förderagentur. "
         "Klassenbildung: (I) Nordlicht Cloud GmbH (gesonderte Klasse, Schlüsselgläubiger), "
         "(II) Sonstige Kreditoren (unter Bagatellgrenze, kein Eingriff geplant). "
         "Anleihegläubiger: nicht vorhanden. Bankdarlehen: nicht vorhanden."),

        ("§ 5 — Restrukturierungsmaßnahmen (Übersicht)",
         "(A) FINANZIELLE MASSNAHMEN: Stundungsvereinbarung mit Nordlicht Cloud GmbH "
         "für die Monate Juni-Dezember 2026 (7 Monate x EUR 118.000 = EUR 826.000) "
         "gegen Rückzahlung ab Januar 2027 in 12 Monatsraten zzgl. Zins 2,5% p.a. "
         "(B) OPERATIVE MASSNAHMEN: Spendenauflagen-Anpassung (Branding-Kooperation "
         "mit drei Tech-Unternehmen gegen Spendengarantie je EUR 250.000 p.a. "
         "für 2026-2028); Personalanpassung: Reduzierung um 4 VZÄ (Projektbefristungen "
         "nicht verlängert), Einsparung EUR 224.000/Jahr. "
         "(C) FINANZIERUNGSMASSNAHMEN: Bridge-Darlehen EUR 300.000 von Aufsichtsratsmitglied "
         "Prof. Dr. Helge Kowalczyk-Mortimer (Privatdarlehen, 0% Zins, Rückzahlung "
         "nach Förderausschüttung). "
         "(D) PROZESSUALE MASSNAHMEN: Anzeige Restrukturierungssache § 31 StaRUG "
         "beim AG Frankfurt am Main, Schutzwirkung für StaRUG-Werkzeuge."),

        ("§ 6 — Fortbestehensprognose und Vergleichsrechnung",
         "Die Fortbestehensprognose nach IDW S 11 kommt zum Ergebnis: "
         "POSITIV unter der Bedingung, dass (1) die Stundungsvereinbarung mit "
         "Nordlicht Cloud zustande kommt, (2) das Bridge-Darlehen ausgereicht wird, "
         "(3) die EU-Förderung bis Oktober 2026 ausgezahlt wird. "
         "Im Stress-Szenario (Förder-Delay weiterer 6 Monate) ist die Prognose negativ. "
         "Vergleichsrechnung: Im Insolvenzfall wäre die Quote für Nordlicht Cloud GmbH "
         "aufgrund fehlender Aktiva praktisch null (Gesellschaft hat keine verwertbaren "
         "Sachanlagen; Mietverhältnis und GPU-Verträge sind keine aktivierbaren Assets). "
         "Im Restrukturierungsplan erhält Nordlicht Cloud GmbH Vollauszahlung der "
         "gestundeten Beträge. Schlechterstellungsverbot ist erfüllt."),
    ]

    for titel, text in abschnitte_a:
        story.append(Paragraph(f"<b>{titel}</b>", S['h3']))
        story.append(Paragraph(text, S['body']))
        story.append(Spacer(1, 0.15*cm))

    story.append(PageBreak())

    # Handschriftliche Notiz Dr. Hellinghaus-Karpov
    story.append(Paragraph("A.7 Handschriftliche Notiz Dr. Hellinghaus-Karpov", S['h1']))
    story.append(hr(FARBE_A))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Original-Notiz, auf gelbem Notizblock, Datum: 10. Mai 2026 (Besprechung mit Dr. Reher-Bornholmsen):",
        S['small']))
    story.append(Spacer(1, 0.2*cm))

    notiz_text = (
        "WICHTIG! (10.5.2026 nach Reher-Gespräch)<br/><br/>"
        "1. Stab-Anordnung JETZT beantragen — BEVOR Q3-Förderbescheid rein kommt.<br/>"
        "   Warum: wenn Bescheid positiv = kein Schaden mehr = Gericht lehnt ab<br/>"
        "   Timing ist ALLES!<br/><br/>"
        "2. Nordlicht Cloud: Verhandlung bis 20. Mai 2026. Stundung oder Kündigung?<br/>"
        "   Kündigung Vertragsstrafe EUR 420.000 — ABSOLUT UNMÖGLICH!<br/>"
        "   Also: Stundung verhandeln, aber SCHRIFTLICH und MIT ANWALT!<br/><br/>"
        "3. Aufsichtsrat nächste Woche: AR muss Restrukturierungsplan FORMAL beschließen<br/>"
        "   sonst fehlt Legitimation für Reher Wennstedt<br/><br/>"
        "4. VERGISS NICHT: Empfangsbestätigung § 102-Schreiben unterschreiben und zurück!<br/><br/>"
        "5. BRIDGE DARLEHEN: Helge Kowalczyk-Mortimer sagt JA — braucht aber Satzungsänderung?<br/>"
        "   Dr. Reher sagt: nein, geht ohne, weil gemeinnützige GmbH und Darlehen kein Spende<br/><br/>"
        "TODO: Brauche STAB-Anordnung VOR Q3-Förderbescheid!! Deadline: 15. Juni 2026!!"
    )
    notiz_data = [[Paragraph(notiz_text,
        ParagraphStyle('handnotiz_a', fontName='Times-Italic', fontSize=11,
                       leading=18, textColor=colors.HexColor('#1A1A80'),
                       leftIndent=10))]]
    notiz_tbl = Table(notiz_data, colWidths=[16*cm])
    notiz_tbl.setStyle(TableStyle([
        ('BOX', (0,0),(0,0), 2, colors.HexColor('#1A1A80')),
        ('BACKGROUND', (0,0),(0,0), colors.HexColor('#FEFEF0')),
        ('PADDING', (0,0),(0,0), 14),
    ]))
    story.append(notiz_tbl)
    story.append(PageBreak())

    # Stundungsvereinbarung Nordlicht Cloud
    story.append(Paragraph("A.8 Stundungsvereinbarung Nordlicht Cloud GmbH (Entwurf)", S['h1']))
    story.append(hr(FARBE_A))
    story.append(Spacer(1, 0.2*cm))

    stundungs_abschnitte = [
        ("Parteien",
         "(1) VEYRA AI Foundation gGmbH, Eschersheimer Landstraße 42, 60322 Frankfurt am Main "
         "(nachfolgend: 'Stundungsschuldnerin') "
         "(2) Nordlicht Cloud GmbH, Schauenburgerstraße 35, 20095 Hamburg "
         "(nachfolgend: 'Stundungsgläubigerin')"),
        ("Präambel",
         "Die Stundungsschuldnerin ist Kundin der Stundungsgläubigerin auf Basis des "
         "GPU-Cloud-Dienstleistungsvertrags vom 14. September 2022 (DLV-2022-0914). "
         "Die Stundungsschuldnerin hat gegenüber dem AG Frankfurt am Main "
         "eine Restrukturierungssache angezeigt (Az. AG Frankfurt 810 RES 14/26). "
         "Zum Zweck der erfolgreichen Umsetzung des Restrukturierungsplans "
         "vereinbaren die Parteien Folgendes:"),
        ("§ 1 — Gegenstand der Stundung",
         "Die Stundungsgläubigerin stundet die für die Monate Juni 2026 bis Dezember 2026 "
         "fälligen Rechnungsbeträge (7 Monate × EUR 118.000 zzgl. MwSt.) in Höhe von "
         "EUR 826.000 netto (EUR 982.940 brutto). Die Fälligkeit der gestundeten Beträge "
         "wird aufgeschoben bis zum 31. Januar 2027."),
        ("§ 2 — Rückzahlung",
         "Die gestundeten Beträge sind ab Februar 2027 in 12 gleichen Monatsraten "
         "à EUR 68.833,33 (netto) zzgl. gesetzlicher MwSt. zu zahlen. "
         "Auf den gestundeten Betrag werden Stundungszinsen in Höhe von 2,5% p.a. "
         "ab 1. Juli 2026 erhoben. Zinsen sind zusammen mit der letzten Rate fällig."),
        ("§ 3 — Bedingungen und Rücktrittsrechte",
         "Die Stundungsvereinbarung steht unter der auflösenden Bedingung, dass der "
         "Restrukturierungsplan der Stundungsschuldnerin nicht bis zum 31. August 2026 "
         "rechtskräftig bestätigt wird. Im Falle der auflösenden Bedingung werden "
         "sämtliche gestundeten Beträge sofort fällig. Die laufende Dienstleistungserbringung "
         "der Stundungsgläubigerin (GPU-Cloud-Kapazitäten) wird durch diese Vereinbarung "
         "nicht beeinträchtigt."),
        ("§ 4 — Sonstiges",
         "Diese Vereinbarung bedarf der Schriftform. Änderungen bedürfen der Schriftform. "
         "Gerichtsstand: Hamburg. Anwendbares Recht: deutsches Recht. "
         "Dieser Entwurf ersetzt nicht eine notariell beglaubigte Vereinbarung. "
         "Er dient ausschließlich der Grundlage einer Verhandlung."),
    ]

    for titel, text in stundungs_abschnitte:
        story.append(Paragraph(f"<b>{titel}</b>", S['h3']))
        story.append(Paragraph(text, S['legal']))
        story.append(Spacer(1, 0.15*cm))

    story.append(Spacer(1, 0.5*cm))
    for label in ["Frankfurt am Main, den _______________",
                  "VEYRA AI Foundation gGmbH, Dr. Mira Hellinghaus-Karpov",
                  "\n",
                  "Hamburg, den _______________",
                  "Nordlicht Cloud GmbH, Geschaeftsfuehrung"]:
        story.append(Paragraph(label,
            ParagraphStyle('sig_stund', fontName='Times-Italic', fontSize=11,
                           textColor=DUNKELBLAU, spaceAfter=8)))
    story.append(PageBreak())


def build_variante_b_extended(story):
    """Erweiterte Bestandteile Variante B — IDW S-11/S-6 und Anleihebedingungen."""
    AZ = "AG Bamberg 53 RES 7/26"

    story.append(Paragraph("B.6 IDW S 11 Fortbestehensprognose — Kurzfassung (12+24 Monate)", S['h1']))
    story.append(hr(FARBE_B))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Erstellt von: Hartwig Aktuar & Restrukturierung GmbH, Köln (fiktiv)<br/>"
        "Auftraggeber: Reher Wennstedt Restrukturierung PartmbB für Vorstand HERRENBLUSE & ZWIRN HARTMANNSCHMIDT AG<br/>"
        "Stand: 10. April 2026 (Vorversion — nicht final)",
        S['small']))
    story.append(Spacer(1, 0.2*cm))

    idws11_abschnitte = [
        ("1. Aufgabe und Auftrag",
         "Auf Anforderung der Reher Wennstedt Restrukturierung PartmbB (Restrukturierungsberater "
         "der HERRENBLUSE & ZWIRN HARTMANNSCHMIDT AG, im Folgenden 'Gesellschaft') "
         "wurde die Hartwig Aktuar & Restrukturierung GmbH (im Folgenden 'Gutachter') "
         "mit der Erstellung einer Fortbestehensprognose nach IDW S 11 beauftragt. "
         "Die Prognose soll die Zahlungsfähigkeit der Gesellschaft für die nächsten "
         "12 und 24 Monate beurteilen. Der Gutachter hat die Informationen der Gesellschaft "
         "nicht eigenständig geprüft; es handelt sich um eine Plausibilisierung, "
         "keine Abschlussprüfung."),

        ("2. Wesentliche Planungsannahmen",
         "BASE CASE: Umsatz 2026: EUR 68,4 Mio. (-8,0% gg. 2025: EUR 74,3 Mio.). "
         "EBITDA 2026: EUR 3,2 Mio. (Marge: 4,7%). Zinsaufwand: EUR 4,1 Mio./Jahr. "
         "EBIT negativ (EUR -2,6 Mio.). Free Cash Flow operativ: EUR -1,9 Mio. "
         "STRESS CASE: Umsatz 2026: EUR 62,0 Mio. (-16,6%). EBITDA: EUR -0,8 Mio. "
         "Zinsaufwand: EUR 4,1 Mio. (unverändert). FCF: EUR -6,4 Mio. "
         "SEVERE STRESS: Umsatz 2026: EUR 55,0 Mio. (-26,0%). EBITDA: EUR -5,2 Mio. "
         "ZU-Eintritt: August 2027 (ohne Gegenmaßnahmen)."),

        ("3. Fortbestehensprognose 12 Monate (Mai 2026 — April 2027)",
         "Ergebnis: POSITIV im Base Case unter der Bedingung, dass (a) die "
         "bestehenden Kreditlinien nicht ungekündigt werden (Covenant-Waiver bis 31.03.2027 "
         "durch Bankenrunde zu vereinbaren), (b) die Anleihe-Refinanzierung vorbereitet wird, "
         "(c) ein Sanierungsgutachten nach IDW S 6 in Auftrag gegeben wird. "
         "Im Stress Case: NEGATIV ohne Covenant-Waiver (Kündigung durch NorddeutscheLandesbank-Avis "
         "möglich ab Juli 2026)."),

        ("4. Fortbestehensprognose 24 Monate (Mai 2026 — April 2028)",
         "Ergebnis: BEDINGT POSITIV. Die Anleihe in Höhe von EUR 65 Mio. läuft am "
         "15. November 2027 aus. Ohne Anschlussfinanzierung tritt Zahlungsunfähigkeit "
         "in Monat 18 (Oktober 2027) ein. Bei erfolgreicher StaRUG-Anleihe-Restrukturierung "
         "(Cross-Class-Cram-Down, Verlängerung um 36 Monate, Zinsreduktion auf 3,5% p.a.) "
         "ist die 24-Monats-Prognose POSITIV. Die Maßnahmen müssen bis spätestens "
         "30. April 2027 wirksam sein."),

        ("5. Kritische Erfolgsfaktoren und Handlungsempfehlungen",
         "(1) SOFORTIG: Bankenrunde einberufen, Covenant-Waiver bis 31.03.2027 verhandeln. "
         "(2) BIS 30.06.2026: IDW S 6-Sanierungsgutachten in Auftrag geben (Vollversion). "
         "(3) BIS 30.09.2026: Anzeige Restrukturierungssache § 31 StaRUG und Beginn "
         "Anleihe-Restrukturierung. (4) BIS 31.12.2026: Term Sheet mit Anleihegläubigern. "
         "(5) BIS 30.04.2027: Restrukturierungsplan-Bestätigung durch Gericht."),
    ]

    for titel, text in idws11_abschnitte:
        story.append(Paragraph(f"<b>{titel}</b>", S['h3']))
        story.append(Paragraph(text, S['legal']))
        story.append(Spacer(1, 0.15*cm))

    story.append(PageBreak())

    story.append(Paragraph("B.7 Cross-Class-Cram-Down-Memo (Auszug) — Dr. Vellmer-Lutz", S['h1']))
    story.append(hr(FARBE_B))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "MEMORANDUM — VERTRAULICH<br/>"
        "An: Vorstand HERRENBLUSE & ZWIRN HARTMANNSCHMIDT AG<br/>"
        "Von: Dr. Christoph Vellmer-Lutz, Reher Wennstedt Restrukturierung PartmbB<br/>"
        "Datum: 28. April 2026<br/>"
        "Betreff: Cross-Class-Cram-Down § 26 StaRUG — Rechtliche Analyse und Strategie",
        S['small']))
    story.append(Spacer(1, 0.2*cm))

    cram_abschnitte = [
        ("I. Grundsatz des Cross-Class-Cram-Downs nach § 26 StaRUG",
         "§ 26 StaRUG ermöglicht die gerichtliche Bestätigung eines Restrukturierungsplans "
         "auch dann, wenn eine Gläubigergruppe den Plan abgelehnt hat, sofern bestimmte "
         "Voraussetzungen kumulativ erfüllt sind: (1) Mindestens eine weitere betroffene Gruppe "
         "hat zugestimmt. (2) Die ablehnende Gruppe wird durch den Plan nicht schlechtergestellt "
         "als ohne Plan (§ 27 StaRUG: Schlechterstellungsverbot). (3) Kein Mitglied der "
         "zustimmenden Gruppe erhält Mehr als seinen Anteil am hypothetischen "
         "Verwertungserlös (§ 28 StaRUG: Best-Interest-of-Creditors-Test)."),

        ("II. Gruppenbildung und Abstimmungsszenario HARTMANNSCHMIDT",
         "Geplante Gruppenstruktur: "
         "(1) Anleihe-Gruppe: NorddeutscheLandesbank-Avis, Sparkasse Oberfranken, "
         "institutionelle Anleihegläubiger (EUR 65 Mio. Nominalwert, 5 Gläubiger identifiziert). "
         "(2) Betriebsmittelkredit-Gruppe: Konsortium (EUR 18 Mio., 3 Banken). "
         "(3) Anteilsinhaber: Hartmannschmidt Holding KG (nicht planbetroffene Gruppe; "
         "jedoch Schlechterstellungsverbot zu beachten). "
         "Abstimmungsprognose: Anleihe-Gruppe voraussichtlich mehrheitlich JA (3 von 5 "
         "Gläubigern, Wertanteil 62%); Betriebsmittel-Gruppe: unklar."),

        ("III. Schlechterstellungsverbot und Vorsichtsmaßnahmen",
         "Besondere Sorgfalt ist geboten für die Hartmannschmidt Holding KG als "
         "Familien-Anker-Aktionärin (56% der Stammaktien). Das Schlechterstellungsverbot "
         "des § 27 StaRUG schützt grundsätzlich auch Anteilsinhabergruppen. "
         "Soweit die HV die Kapitalmaßnahmen nicht beschließt (was bei Familien-Anker "
         "unwahrscheinlich, aber nicht ausgeschlossen ist), wäre ein "
         "gestaltender Teil des Plans gg. Anteilsinhaber erforderlich — "
         "was eine vollständige aktienrechtliche Durchstrukturierung verlangt. "
         "Empfehlung: Familien-Anker frühzeitig einbinden, Term Sheet vorab abstimmen."),

        ("IV. Zeitplan Cross-Class-Cram-Down HARTMANNSCHMIDT",
         "Meilensteine: "
         "T0 (01.05.2026): Anzeige Restrukturierungssache; "
         "T+4 Wochen (01.06.2026): Entwurf Restrukturierungsplan; "
         "T+8 Wochen (01.07.2026): Gläubiger-Konsultation, Abstimmungsvorbereitung; "
         "T+12 Wochen (01.08.2026): Planabstimmung; "
         "T+14 Wochen (15.08.2026): Antrag auf Planbestätigung bei AG Bamberg; "
         "T+18 Wochen (15.09.2026): Ziel Planbestätigung. "
         "Risiko: Gericht lehnt Bestätigung ab = Rückfall in Insolvenz."),
    ]

    for titel, text in cram_abschnitte:
        story.append(Paragraph(f"<b>{titel}</b>", S['h3']))
        story.append(Paragraph(text, S['legal']))
        story.append(Spacer(1, 0.15*cm))

    story.append(PageBreak())

    story.append(Paragraph("B.8 Bankenrunden-Protokoll (Auszug)", S['h1']))
    story.append(hr(FARBE_B))
    story.append(Spacer(1, 0.2*cm))

    for line in fax_block([
        "PROTOKOLL BANKENRUNDE vom 20. April 2026",
        "Gesellschaft: HERRENBLUSE & ZWIRN HARTMANNSCHMIDT AG, Bamberg",
        "Ort: Konferenzraum NorddeutscheLandesbank-Avis, Bamberg",
        "Teilnehmer:",
        "  - Dipl.-Kfm. Helge Hartmannschmidt (Vorstandssprecher)",
        "  - Annika Luettke-Berens (CFO)",
        "  - Dr. Tjark Reher-Bornholmsen (RA, Reher Wennstedt)",
        "  - Dr. Christoph Vellmer-Lutz (RA, Reher Wennstedt)",
        "  - Markus Grienewald (NorddeutscheLandesbank-Avis, Leiter Kreditrestrukturierung)",
        "  - Andrea Kunz-Scheidereit (Sparkasse Oberfranken, Firmenkundenbetreuung)",
        "",
        "ERGEBNISSE:",
        "1. Banken bestätigen Kenntnis der Krisen-Lage.",
        "2. Covenant-Waiver bis 31.03.2027: GRUNDSAETZLICHES EINVERSTAENDNIS.",
        "   Bedingung: IDW S 6-Sanierungsgutachten bis 30.09.2026.",
        "3. Anleihe-Restrukturierung: Banken unterstuetzen StaRUG-Plan-Route.",
        "4. Naechste Bankenrunde: 15. Mai 2026 mit Fortbestehensprognose IDW S 11.",
        "",
        "[Protokolliert von: Dr. C. Vellmer-Lutz]",
    ]):
        story.append(line)
    story.append(PageBreak())


def build_variante_c_extended(story):
    """Erweiterte Bestandteile Variante C — Schlechterstellungsverbot + Aktivisten-Detail."""
    AZ = "AG Stuttgart 14 RES 22/26"

    story.append(Paragraph("C.8 Schlechterstellungsverbots-Gutachten (Kurzfassung)", S['h1']))
    story.append(hr(FARBE_C))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Erstellt von: Prof. Dr. Engelbert Hartfeld-Marwede, Brentwood Hartfeld Restructuring mbB<br/>"
        "Im Auftrag: Nordfels Power Cells SE<br/>"
        "Stand: 28. April 2026 (Vorversion)",
        S['small']))
    story.append(Spacer(1, 0.2*cm))

    sgv_abschnitte = [
        ("I. Auftrag und Gegenstand",
         "Der Gutachter wurde beauftragt zu prüfen, ob der geplante Restrukturierungsplan "
         "der Nordfels Power Cells SE (SE) die Anforderungen des § 27 StaRUG "
         "(Schlechterstellungsverbot) erfüllt. Das Gutachten bezieht sich auf drei Gruppen: "
         "(I) Konsortialkreditgeber (EUR 300 Mio.), (II) Anleihegläubiger (EUR 250 Mio.), "
         "(III) Streubesitz-Aktionäre (38% des Grundkapitals)."),

        ("II. Vergleichsszenario — Liquidation ohne Plan",
         "Im Liquidationsszenario (Insolvenz ohne Plan) ergibt sich nach Bewertung "
         "der Aktiva ein Liquidationswert von ca. EUR 180-220 Mio. (inkl. Maschinen, "
         "IP-Rechte, Kundenstamm, Vorräte). Verteilt nach Rangfolge: "
         "Konsortialkreditgeber: Quote ca. 55-68% (EUR 165-204 Mio.). "
         "Anleihegläubiger: Quote ca. 0-3% (EUR 0-7,5 Mio.) nach Vorrecht der Kreditgeber. "
         "Streubesitz-Aktionäre: Quote 0% (kein Vermögen nach Befriedigung Fremdkapital). "
         "Family Office Vossbergen: Quote 0%."),

        ("III. Plan-Szenario — Behandlung je Gruppe",
         "Im Plan-Szenario: "
         "(I) Konsortialkreditgeber: Stundung 24 Monate, Zinsreduktion auf 2,5% p.a., "
         "kein Nominalerlass. Quote bei plangemäßer Bedienung: 100% + laufende Zinsen. "
         "Schlechterstellung: NEIN. (II) Anleihegläubiger: Nominalerlass 30%, "
         "Laufzeitverlängerung 36 Monate, Zinsreduktion auf 4,0% p.a. Quote: EUR 175 Mio. "
         "von EUR 250 Mio. nominal. Schlechterstellung gg. Liquidationsquote 0-3%: NEIN, "
         "da Plan-Quote 70% deutlich besser. (III) Streubesitz: Verwässerung durch "
         "Kapitalherabsetzung 90% + Kapitalerhöhung (Debt-to-Equity-Anteil Anleihe). "
         "Restanteil Streubesitz nach Plan: 3,8%. Quote gg. Liquidation 0%: KEIN Nachteil."),

        ("IV. Ergebnis",
         "Das Schlechterstellungsverbot des § 27 StaRUG ist für alle drei Gruppen "
         "erfüllt. Alle planbetroffenen Gläubiger stehen im Plan besser als in der Liquidation. "
         "Die Streubesitz-Verwässerung ist zulässig, da Streubesitz in der Liquidation "
         "vollständig leer ausgehen würde und das Schlechterstellungsverbot Null-Quotierung "
         "mit Null-Quotierung vergleicht. Der Gutachter empfiehlt, das Vollgutachten "
         "bis 30. Mai 2026 fertigzustellen."),
    ]

    for titel, text in sgv_abschnitte:
        story.append(Paragraph(f"<b>{titel}</b>", S['h3']))
        story.append(Paragraph(text, S['legal']))
        story.append(Spacer(1, 0.15*cm))

    story.append(PageBreak())

    # Aktivisten-Investor-Letter (englisch)
    story.append(Paragraph("C.9 Aktivisten-Investor-Letter Westshore Catalyst Partners LLP (vollstaendig)", S['h1']))
    story.append(hr(FARBE_C))
    story.append(Spacer(1, 0.2*cm))

    letter_lines = [
        "WESTSHORE CATALYST PARTNERS LLP",
        "Camana Bay, Grand Cayman, KY1-1001, Cayman Islands",
        "",
        "STRICTLY CONFIDENTIAL AND PRIVILEGED",
        "Date: 2 May 2026",
        "",
        "To: Supervisory Board of Nordfels Power Cells SE",
        "    Ellwangen, Germany",
        "Attn: Prof. Dr. Raimund Schlossermeier-Voss (Chairman, Supervisory Board)",
        "",
        "Re: Serious Concerns Regarding the Proposed Restructuring Under StaRUG",
        "    Westshore Catalyst Partners LLP c/o [11.2% of share capital]",
        "",
        "Dear Members of the Supervisory Board,",
        "",
        "We write to you as a significant shareholder of Nordfels Power Cells SE",
        "('the Company') holding approximately 11.2% of the outstanding share capital.",
        "We are deeply concerned about the proposed restructuring path and believe the",
        "Management Board has not adequately considered the interests of minority",
        "shareholders and bondholders.",
        "",
        "1. DILUTION OF MINORITY SHAREHOLDERS WITHOUT CONSENT",
        "We understand that the proposed restructuring plan contemplates a capital",
        "reduction of up to 90% followed by a capital increase reserved for existing",
        "bondholders (Debt-to-Equity swap). This would reduce our economic interest",
        "from 11.2% to approximately 1.1% — a dilution of 90%. We note that StaRUG",
        "Section 7(4) permits such measures in a restructuring plan but the Supervisory",
        "Board must ensure strict compliance with Section 27 StaRUG (no worse-off test).",
        "",
        "2. BONDHOLDER PROTECTION CONCERNS",
        "We represent a coalition of bondholder interests holding EUR 27.4 million",
        "of the outstanding EUR 250 million bond (ISIN: XS2847193000). The proposed",
        "30% haircut is in our view not adequately justified by the restructuring",
        "expert's preliminary valuation. We demand an independent valuation by a",
        "reputable Big Four auditor before any vote is taken.",
        "",
        "3. DEMANDS AND TIMELINE",
        "We demand: (a) Access to the full IDW S11/IDW S6 reports within 10 business days.",
        "(b) An extraordinary general meeting to discuss restructuring alternatives.",
        "(c) Suspension of the StaRUG process until the above are provided.",
        "",
        "If our demands are not met by 19 May 2026, we will consider all available",
        "legal remedies including but not limited to court injunctions and complaint",
        "filings with the restructuring court.",
        "",
        "Sincerely,",
        "WESTSHORE CATALYST PARTNERS LLP",
        "Alexander Morthon-Healy, Managing Partner",
    ]
    for line in fax_block(letter_lines):
        story.append(line)
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "<b>Vermerk Dr. Reher-Bornholmsen (intern, 3. Mai 2026):</b> "
        "Brief ist typisches Aktivisten-Eskalationsschreiben. Keine sofortige "
        "rechtliche Reaktionspflicht, aber Antwortschreiben innerhalb 5 Tagen empfohlen. "
        "Hauptforderungen prüfen: (a) IDW-Berichte sind noch Vorentwürfe — Herausgabe "
        "rechtlich bedenklich wegen Vertraulichkeit. (b) HV-Einberufung durch "
        "Minderheitsaktionär nach § 50 AktG nur bei 5% Kapitalanteil möglich — "
        "Westshore hat 11,2%, ALSO: Einberufungsrecht beachten! "
        "(c) Gerichtliche Untersagung StaRUG-Verfahren: extrem unwahrscheinlich.",
        S['body']))
    story.append(PageBreak())


def build_variante_d_extended(story):
    """Erweiterte Bestandteile Variante D — ausfuehrliche Beratung, Vermieter-Stundung, Liquidationsrechnung."""
    AZ = "AG Charlottenburg 36 IN 412/26"
    FARBE = FARBE_D

    # D.8 Aufhebungsvereinbarung Sonnenallee-Mietvertrag
    story.append(Paragraph("D.8 Entwurf Mietaufhebungsvereinbarung — Filiale Sonnenallee 89b", S['h1']))
    story.append(hr(FARBE))
    story.append(Spacer(1, 0.2*cm))

    for line in kanzlei_kopf_wandelmoser():
        story.append(line)
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "<b>ENTWURF — NOCH NICHT UNTERZEICHNET — Fassung v. 5. Mai 2026</b>",
        S['warn']))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "MIETAUFHEBUNGSVEREINBARUNG",
        ParagraphStyle('ueberschrift_zentriert', fontName='Helvetica-Bold', fontSize=14,
                       alignment=1, spaceAfter=6, spaceBefore=6)))
    story.append(Paragraph(
        "zwischen<br/>"
        "<b>Eigentuemergemeinschaft Sonnenallee 89b GbR</b> (im Folgenden: 'Vermieterin'), "
        "vertreten durch Immobilienverwaltung Treichelt & Partner GbR, Berlin,<br/>"
        "und<br/>"
        "<b>Salaltbar UG (haftungsbeschraenkt)</b>, Hermannplatz 14, 12049 Berlin, "
        "vertreten durch den Geschaeftsfuehrer Tarek-Yusuf Celebi-Drebenstedt "
        "(im Folgenden: 'Mieterin').",
        S['body']))
    story.append(Spacer(1, 0.3*cm))

    aufheb_pkte = [
        ("Praeambel",
         "Die Mieterin betreibt in den Mietraeumen Sonnenallee 89b, 12049 Berlin, eine vegane "
         "Salat-Bar. Aufgrund eines erheblichen Anstiegs der Miete (Erhoehung von EUR 3.700 auf "
         "EUR 5.200/Monat ab Januar 2024) und allgemeiner wirtschaftlicher Schwierigkeiten ist "
         "die Mieterin nicht mehr in der Lage, das Mietverhaeltnis wirtschaftlich sinnvoll "
         "fortzufuehren. Um ein Insolvenzverfahren abzuwenden, beabsichtigen die Parteien eine "
         "einvernehmliche Aufhebung des Mietverhaeltnisses."),
        ("§ 1 Aufhebung des Mietverhaeltnisses",
         "Die Parteien heben den Gewerbemietvertrag vom 10. Dezember 2023 (Az. Vermieter: "
         "T&P-SONN-0089b-2023) einvernehmlich zum <b>31. Mai 2026</b> (Aufhebungsdatum) auf. "
         "Ab dem Aufhebungsdatum entfaellt jede Verpflichtung der Mieterin zur Zahlung von Miete "
         "und Nebenkosten fuer diese Liegenschaft."),
        ("§ 2 Raeumung und Rueckgabe",
         "Die Mieterin verpflichtet sich, die Mietraeume bis spaetestens 31. Mai 2026, 18:00 Uhr, "
         "vollstaendig geraumt und besenrein zurueckzugeben. Einbauten (Kuehlanlagen, Theke) "
         "verbleiben als Entschaedigung im Objekt und gehen entschaedigungslos in das Eigentum "
         "der Vermieterin ueber (Wert geschaetzt EUR 8.400)."),
        ("§ 3 Mietruckstaende und Abfindung",
         "Die aufgelaufenen Mietruckstaende per 5. Mai 2026 betragen EUR 18.400,00 "
         "(fuer die Monate Februar, Maerz, April und anteilig Mai 2026). "
         "Die Parteien einigen sich auf folgende Regelung:<br/>"
         "(a) Die Mieterin zahlt bis zum 31. Mai 2026 eine Einmalzahlung von EUR 6.000,00 "
         "(aus dem Erloese des Ausverkaufs Filialequipment).<br/>"
         "(b) Die Vermieterin erlasst den Restbetrag von EUR 12.400,00 als Sanierungsbeitrag, "
         "unter der auflösenden Bedingung der rechtzeitigen Raeumung und der Einmalzahlung.<br/>"
         "(c) Gegenzeichnung bis spaetestens 8. Mai 2026, sonst entfaellt das Angebot."),
        ("§ 4 Gewerberaum-Mietsicherheit",
         "Die Mietsicherheit (Kaution) in Hoehe von EUR 3.100,00 wird mit der Einmalzahlung "
         "gemaess § 3 (a) verrechnet. Die Nettoverpflichtung der Mieterin aus der Einmalzahlung "
         "betraegt damit EUR 2.900,00."),
        ("§ 5 Gegenseitige Freistellung",
         "Mit Erfullung der Pflichten aus §§ 2, 3 und 4 dieser Vereinbarung sind saemtliche "
         "wechselseitigen Ansprueche aus dem Mietverhaeltnis abgegolten. "
         "Beide Parteien verzichten auf jegliche weiteren Ansprueche, insbesondere aus "
         "§§ 535 ff. BGB, es sei denn, es handelt sich um arglistig verborgen gehaltene Maengel."),
        ("§ 6 Schriftformerfordernis",
         "Aenderungen oder Ergaenzungen dieser Vereinbarung beduerfen der Schriftform. "
         "Muendliche Nebenabreden bestehen nicht. Gerichtsstand ist Berlin."),
    ]

    for titel, text in aufheb_pkte:
        story.append(Paragraph(f"<b>{titel}</b>", S['h2']))
        story.append(Paragraph(text, S['body']))
        story.append(Spacer(1, 0.1*cm))

    story.append(Spacer(1, 0.4*cm))
    unt_data = [
        ['Ort, Datum', 'Ort, Datum'],
        ['Berlin, den ______________', 'Berlin, den ______________'],
        ['', ''],
        ['____________________________', '____________________________'],
        ['Eigentuemergemeinschaft Sonnenallee 89b GbR', 'Salaltbar UG (haftungsbeschraenkt)'],
        ['(Immobilienverwaltung Treichelt & Partner GbR)', 'Tarek-Yusuf Celebi-Drebenstedt (GF)'],
    ]
    unt_tbl = Table(unt_data, colWidths=[8.5*cm, 8.5*cm])
    unt_tbl.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('ALIGN', (0,0), (0,-1), 'LEFT'),
        ('ALIGN', (1,0), (1,-1), 'RIGHT'),
    ]))
    story.append(unt_tbl)
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "<i>Anm. RAin Wandelmoser: Vermieterin hat muendlich signalisiert, "
        "dem Entwurf zuzustimmen, wenn Raeumung bis 31.5. und EUR 2.900 netto (nach Kautionsverrechnung) fliessen. "
        "Mandant muss Equipment-Ausverkauf sofort organisieren. "
        "Einnahmen Ausverkauf geschaetzt EUR 4.500 (Kuehlschraenke, Mobiliar). "
        "Rechtlich: Aufhebungsvertrag ist vorzuziehen ggue. fristloser Kuendigung, "
        "da Schadensersatzpflicht des Mieters bei fristloser Kuendigung bis 2027 ca. EUR 62.000 betragen koennte.</i>",
        S['footnote']))
    story.append(PageBreak())

    # D.9 Liquidationsrechnung (Schließung Sonnenallee)
    story.append(Paragraph("D.9 Liquidationsrechnung — Schließung Filiale Sonnenallee 89b", S['h1']))
    story.append(hr(FARBE))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "Erstellt: RAin Charlotte Wandelmoser, 5. Mai 2026 | Az.: CW-2026-SALALTBAR",
        S['small']))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "Ziel dieser Liquidationsrechnung ist die Quantifizierung des wirtschaftlichen Vorteils "
        "aus einer geordneten Schließung der Filiale Sonnenallee 89b "
        "(inkl. Vergleich mit Fortfuehrung bis Vertragsende 31.12.2027).",
        S['body']))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("Szenario 1: Fortfuehrung bis 31.12.2027 (Status quo)", S['h2']))
    s1_data = [
        ['Position', 'Berechnung', 'Betrag (EUR)'],
        ['Weiterer Mietzins Sonnenallee (Aug.–Dez. 2027)', '20 Monate × EUR 5.200', '-104.000'],
        ['Umsatz Sonnenallee (geschaetzt, ohne Steigerung)', '20 Mo. × EUR 11.000 Umsatz/Mo', '+220.000'],
        ['Wareneinsatz (32% des Umsatzes)', '20 Mo. × EUR 3.517', '-70.333'],
        ['Personalkosten Sonnenallee (4 Teilzeitk.)', '20 Mo. × EUR 4.333', '-86.667'],
        ['Sonstige Kosten (Energie, Versicherung etc.)', '20 Mo. × EUR 817', '-16.333'],
        ['Ergebnis Sonnenallee (Fortfuehrung)', '', '-57.333'],
        ['Mietruckstaende bereits aufgelaufen', '(bereits entstanden)', '-18.400'],
        ['Gesamtbelastung Szenario 1', '', '-75.733'],
    ]
    s1_tbl = Table(s1_data, colWidths=[7.5*cm, 5.5*cm, 4.5*cm])
    s1_style = tbl_style_zahlen()
    s1_style.add('BACKGROUND', (0,6), (-1,6), colors.HexColor('#FFE0E0'))
    s1_style.add('FONTNAME', (0,6), (-1,6), 'Helvetica-Bold')
    s1_style.add('BACKGROUND', (0,8), (-1,8), colors.HexColor('#FF9999'))
    s1_style.add('FONTNAME', (0,8), (-1,8), 'Helvetica-Bold')
    s1_tbl.setStyle(s1_style)
    story.append(s1_tbl)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("Szenario 2: Geordnete Schließung per 31.05.2026 (Aufhebungsvertrag)", S['h2']))
    s2_data = [
        ['Position', 'Berechnung', 'Betrag (EUR)'],
        ['Einmalzahlung Rückstandsbereinigung (netto n. Kaution)', 'Verhandlungsergebnis § 3 Aufhebungsvertrag', '-2.900'],
        ['Erlös Equipment-Ausverkauf (Schätzung)', 'Kühlschränke, Mobiliar, Theke', '+4.500'],
        ['Saldo Aufhebungsvereinbarung', '', '+1.600'],
        ['Erlass Mietrückstände (Sanierungsbeitrag Vermieter)', '18.400 - 6.000 = 12.400 erlassen', '+12.400'],
        ['Wegfall lfd. Verluste Sonnenallee ab Jun 2026', '19 Mo. × EUR 2.867 Verlust/Mo', '+54.467'],
        ['Personal-Abfindungen / Kündigungsfristen', '4 Mitarbeiter × ca. EUR 1.200', '-4.800'],
        ['Rechtsanwaltskosten Aufhebungsverhandlung', '5 Std. × EUR 280 = EUR 1.400 zzgl. MwSt.', '-1.666'],
        ['Nettoersparnis Szenario 2 vs. Szenario 1', 'Differenz Gesamtbelastung', '+63.001'],
    ]
    s2_tbl = Table(s2_data, colWidths=[7.5*cm, 5.5*cm, 4.5*cm])
    s2_style = tbl_style_zahlen()
    s2_style.add('BACKGROUND', (0,3), (-1,3), colors.HexColor('#FFFACD'))
    s2_style.add('BACKGROUND', (0,7), (-1,7), colors.HexColor('#90EE90'))
    s2_style.add('FONTNAME', (0,7), (-1,7), 'Helvetica-Bold')
    s2_tbl.setStyle(s2_style)
    story.append(s2_tbl)
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "<b>Fazit:</b> Die geordnete Schließung der Filiale Sonnenallee 89b spart der "
        "Salaltbar UG im Vergleich zur Fortfuehrung bis Vertragsende ca. EUR 63.000. "
        "Dies ist die einzig wirtschaftlich vertretbare Option. Mandant wird dringend "
        "zur sofortigen Unterzeichnung des Aufhebungsvertrags geraten.",
        S['body']))
    story.append(PageBreak())

    # D.10 Gläubigerverzeichnis und Sanierungsplan
    story.append(Paragraph("D.10 Gläubigerverzeichnis und Außergerichtlicher Sanierungsplan", S['h1']))
    story.append(hr(FARBE))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "Stand: 5. Mai 2026 | RAin Charlotte Wandelmoser | Az.: CW-2026-SALALTBAR",
        S['small']))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("A. Gläubigerverzeichnis (vollständig)", S['h2']))
    gl_data = [
        ['Nr.', 'Gläubiger', 'Forderungsgrund', 'Betrag (EUR)', 'Fällig seit', 'Priorität', 'Maßnahme'],
        ['1', 'Eigentümergemeinschaft\nSonnenallee 89b GbR', 'Mietrückstände\nFeb-Mai 2026', '18.400,00', 'Feb 2026', 'HOCH\n(Kündigung!)', 'Aufhebungsvertrag\n(s. D.8)'],
        ['2', 'Frische-Kontor\nBerlin GmbH', 'Warenlieferungen\nJan-Apr 2026', '12.800,00', 'Jan 2026', 'HOCH\n(Lieferstop!)', 'Ratenverein-\nbarung anbieten'],
        ['3', 'Finanzamt\nBerlin-Neukölln', 'USt-Rückstände\nQ3/Q4 2025', '8.900,00', 'Nov 2025', 'SEHR HOCH\n(Vollstr.!)', 'Stundungs-\nantrag FA'],
        ['4', 'Wolt GmbH', 'Rücklastschriften\nLiefergebühren', '3.200,00', 'Apr 2026', 'MITTEL', 'Klärung +\nAusgleich'],
        ['5', 'Deutsche Leasing AG', 'Leasingrate\nKühlanlage F3', '1.100,00', 'Mrz 2026', 'MITTEL\n(Pfandrecht)', 'Verhandlung\nRückgabe'],
        ['6', 'AOK Berlin', 'SV-Beiträge\nMrz/Apr 2026', '4.800,00', 'Apr 2026', 'HOCH\n(Haftung GF!)', 'SOFORT\nbezahlen!'],
        ['7', 'MEWA Textil-\nService GmbH', 'Berufskleidung\nMiete Q1 2026', '480,00', 'Apr 2026', 'NIEDRIG', 'Verhandlung'],
        ['SUMME', '', '', '49.680,00', '', '', ''],
    ]
    gl_tbl = Table(gl_data, colWidths=[0.7*cm, 3.5*cm, 2.8*cm, 2.5*cm, 1.8*cm, 2.0*cm, 3.2*cm])
    gl_style = tbl_style_standard()
    gl_style.add('FONTSIZE', (0,0), (-1,-1), 7.5)
    gl_style.add('BACKGROUND', (5,3), (5,3), colors.HexColor('#FF6B6B'))
    gl_style.add('FONTNAME', (5,3), (5,3), 'Helvetica-Bold')
    gl_style.add('BACKGROUND', (5,6), (5,6), colors.HexColor('#FF6B6B'))
    gl_style.add('FONTNAME', (5,6), (5,6), 'Helvetica-Bold')
    gl_style.add('BACKGROUND', (0,7), (-1,7), FARBE_D)
    gl_style.add('TEXTCOLOR', (0,7), (-1,7), colors.white)
    gl_style.add('FONTNAME', (0,7), (-1,7), 'Helvetica-Bold')
    gl_tbl.setStyle(gl_style)
    story.append(gl_tbl)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph(
        "<b>Wichtig:</b> AOK-Beiträge (Nr. 6, EUR 4.800) haben absoluten Vorrang, "
        "da der Geschäftsführer für nicht abgeführte Sozialversicherungsbeiträge "
        "persönlich nach § 266a StGB (Vorenthaltung und Veruntreuung von Arbeitsentgelt) "
        "und § 823 Abs. 2 BGB haftet. Sofortiger Ausgleich dringend empfohlen. "
        "Finanzamt: Stundungsantrag nach § 222 AO stellen — erfahrungsgemäß wird bei "
        "glaubhafter Sanierungsperspektive 6-12 Monate gestundet.",
        S['body']))
    story.append(PageBreak())

    story.append(Paragraph("B. Außergerichtlicher Sanierungsplan (vereinfacht)", S['h2']))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("I. Ausgangslage", S['h3']))
    story.append(Paragraph(
        "Die Salaltbar UG steht am 5. Mai 2026 vor der Zahlungsunfähigkeit. "
        "Verbindlichkeiten fällig: EUR 49.680. Kassenbestand: EUR 3.400. "
        "Laufende Liquiditätslücke: ca. EUR 300/Tag (netto). "
        "Ohne Maßnahmen: Antragspflicht nach § 15a InsO innerhalb von 3 Wochen "
        "(spätestens 26. Mai 2026).",
        S['body']))

    story.append(Paragraph("II. Maßnahmenprogramm", S['h3']))
    massnahmen = [
        ['Nr.', 'Maßnahme', 'Zeitraum', 'Erw. Entlastung (EUR)', 'Verantwortung', 'Status'],
        ['M1', 'Unterzeichnung Aufhebungsvertrag\nSonnenallee (s. D.8)', 'bis 8. Mai 2026', '+12.400 (Erlass)\n+63.001 (Ersparnis\nggue. Fortfuehrung)', 'GF + RAin W.', 'IN VERHANDLUNG'],
        ['M2', 'Equipment-Ausverkauf Sonnenallee\n(Kühlschränke, Mobiliar)', '15.-25. Mai 2026', '+4.500 (Erlös)', 'GF', 'GEPLANT'],
        ['M3', 'Stundungsantrag Finanzamt\n(§ 222 AO, 12 Monate)', 'bis 12. Mai 2026', '8.900 gestundet\n(Raten ab Jul 2026)', 'RAin W.', 'OFFEN'],
        ['M4', 'Ratenvereinbarung Frische-Kontor\n(EUR 1.000/Monat, 13 Raten)', 'bis 15. Mai 2026', 'Lieferstop beendet\n(Umsatz gesichert)', 'GF + RAin W.', 'OFFEN'],
        ['M5', 'Sofortausgleich AOK-Beiträge\n(Priorität 1! Haftungsrisiko GF!)', 'bis 9. Mai 2026', 'Strafbarkeitsrisiko\neliminiert', 'GF', 'SOFORT'],
        ['M6', 'Umschuldung Wolt-Rücklastschr.\n(Klärung Kontoverbindung)', 'bis 10. Mai 2026', '3.200 bereinigt', 'GF', 'OFFEN'],
        ['M7', 'Konsolidierung auf 2 Filialen\n(F1 Hermannpl. + F2 Boddinstr.)', 'ab Jun 2026', 'Overhead -EUR 5.200/Mo\n(F3-Miete entfällt)', 'GF', 'NACH M1'],
        ['M8', 'Umsatzsteigerung F1+F2\n(Marketing, Catering-Angebote)', 'ab Jul 2026', '+EUR 20.000 p.a.\n(konservativ)', 'GF', 'GEPLANT'],
    ]
    m_tbl = Table(massnahmen, colWidths=[0.7*cm, 4.5*cm, 2.5*cm, 3.5*cm, 2.2*cm, 2.1*cm])
    m_style = tbl_style_standard()
    m_style.add('FONTSIZE', (0,0), (-1,-1), 7.5)
    m_style.add('BACKGROUND', (5,5), (5,5), colors.HexColor('#FF6B6B'))
    m_style.add('FONTNAME', (5,5), (5,5), 'Helvetica-Bold')
    m_style.add('BACKGROUND', (5,1), (5,1), colors.HexColor('#FFD700'))
    m_tbl.setStyle(m_style)
    story.append(m_tbl)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("III. Liquiditätsplanung nach Maßnahmen (12 Monate)", S['h3']))
    liq_data = [
        ['Monat', 'Einnahmen', 'lfd. Ausgaben', 'Gläubigerraten', 'Saldo', 'Kumuliert'],
        ['Jun 26', '47.000', '38.500', '5.000', '+3.500', '+3.500'],
        ['Jul 26', '48.000', '38.500', '5.000', '+4.500', '+8.000'],
        ['Aug 26', '50.000', '38.500', '5.000', '+6.500', '+14.500'],
        ['Sep 26', '50.000', '38.500', '5.000', '+6.500', '+21.000'],
        ['Okt 26', '52.000', '38.500', '5.000', '+8.500', '+29.500'],
        ['Nov 26', '55.000', '38.500', '5.000', '+11.500', '+41.000'],
        ['Dez 26', '60.000', '38.500', '5.000', '+16.500', '+57.500'],
        ['Jan 27', '45.000', '38.500', '4.700', '+1.800', '+59.300'],
        ['Feb 27', '44.000', '38.500', '4.700', '+800', '+60.100'],
        ['Mrz 27', '47.000', '38.500', '4.700', '+3.800', '+63.900'],
        ['Apr 27', '48.000', '38.500', '4.700', '+4.800', '+68.700'],
        ['Mai 27', '50.000', '38.500', '4.700', '+6.800', '+75.500'],
    ]
    liq_tbl = Table(liq_data, colWidths=[1.8*cm, 2.5*cm, 3.0*cm, 2.8*cm, 2.5*cm, 2.9*cm])
    liq_style = tbl_style_zahlen()
    liq_style.add('FONTSIZE', (0,0), (-1,-1), 8.5)
    liq_tbl.setStyle(liq_style)
    story.append(liq_tbl)
    story.append(Paragraph(
        "Anmerkung: Einnahmen = F1 (Hermannpl.) + F2 (Boddinstr.) nach Schließung F3. "
        "lfd. Ausgaben beinhalten Personal, Wareneinsatz, Overhead (ohne Sonnenallee-Miete). "
        "Gläubigerraten: Frische-Kontor EUR 1.000, FA-Rate EUR 742, AOK ab Oktoberrückholung, "
        "sonstige. Ab Jan 2027 leicht reduziert, da Frische-Kontor-Rückstand abbezahlt.",
        S['footnote']))
    story.append(PageBreak())

    # D.11 § 1 StaRUG Früherkennungs-Checkliste Salaltbar
    story.append(Paragraph("D.11 § 1 StaRUG-Prüfprotokoll — Rückblick und Lehren", S['h1']))
    story.append(hr(FARBE))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "Das folgende Prüfprotokoll analysiert retrospektiv, ab welchem Zeitpunkt "
        "die Früherkennungspflicht des § 1 StaRUG für den Geschäftsführer der Salaltbar UG "
        "einschlägig war und welche konkreten Handlungen hätten erfolgen müssen. "
        "Zweck: Dokumentation des Beratungsstandards und Aufdeckung typischer Lücken "
        "bei Kleinstunternehmen (UG/GmbH mit weniger als 20 Mitarbeitern).",
        S['body']))
    story.append(Spacer(1, 0.2*cm))

    zeitstrahl = [
        ['Zeitpunkt', 'Ereignis', 'Früherkennungspflicht § 1 StaRUG', 'Versäumnis', 'Bewertung'],
        ['Jan 2024', 'Mieterhöhung Sonnenallee\n+40% (EUR 3.700→5.200)', 'JA — strukturelle\nGefährdung erkennbar', 'Keine Wirtschaftlich-\nkeitsrechnung, kein\nRücksprache mit Steuerberater', 'KRITISCH'],
        ['Jun 2024', 'Erste negative Monats-\nabrechnung F3 (EUR -1.200)', 'JA — drohende\nBestandsgefährdung', 'Keine Liquiditäts-\nplanung erstellt', 'KRITISCH'],
        ['Dez 2024', 'Jahresabschluss 2024:\nEUR -45.000 (unveröffentl.)', 'JA — Jahresverlust\ndokumentiert', 'Kein IDW S 11, kein\nBeratungsgespräch', 'KRITISCH'],
        ['Mrz 2025', 'Rücklage § 5a Abs. 3 GmbHG\nnicht gebildet (Pflicht seit 2021!)', 'JA — GmbHG-Verletzung\n(Organpflicht)', 'Keine Kenntnis der\nRücklagenpflicht', 'SEHR KRITISCH'],
        ['Sep 2025', 'USt-Vorauszahlungen\nnicht geleistet (Q3 2025)', 'JA — konkrete\nLiquiditätskrise', 'Keine Meldung, keine\nStundung beantragt', 'SEHR KRITISCH'],
        ['Feb 2026', 'Erste Mietrückstände\nSonnenallee (EUR 5.200)', 'JA — Zahlungsunfähigkeit\ndroht konkret', 'Keine rechtliche\nBeratung gesucht', 'KRITISCH'],
        ['Apr 2026', 'Lieferstopp Frische-Kontor,\nWolt-Rücklastschriften', 'JA — Zahlungsunfähigkeit\nwahrscheinlich', 'Erst jetzt Anwalt\nkontaktiert (4 Monate\nnach Pflichtbeginn!)', 'HAFTUNGSRISIKO'],
        ['27. Apr 2026', 'E-Mail an RAin Wandelmoser\n(s. D.3)', 'JA — § 15a InsO-Frist\nbegann zu laufen', 'Mandatserteilung,\naußergerichtliche\nKonsolidierung beginnt', 'MASSNAHME'],
    ]
    z_tbl = Table(zeitstrahl, colWidths=[1.8*cm, 3.8*cm, 3.5*cm, 3.8*cm, 2.6*cm])
    z_style = tbl_style_standard()
    z_style.add('FONTSIZE', (0,0), (-1,-1), 7.5)
    z_style.add('BACKGROUND', (4,1), (4,1), colors.HexColor('#FF6B6B'))
    z_style.add('BACKGROUND', (4,2), (4,2), colors.HexColor('#FF6B6B'))
    z_style.add('BACKGROUND', (4,3), (4,3), colors.HexColor('#FF6B6B'))
    z_style.add('BACKGROUND', (4,4), (4,4), colors.HexColor('#FF4444'))
    z_style.add('BACKGROUND', (4,5), (4,5), colors.HexColor('#FF4444'))
    z_style.add('BACKGROUND', (4,6), (4,6), colors.HexColor('#FF6B6B'))
    z_style.add('BACKGROUND', (4,7), (4,7), colors.HexColor('#FF9900'))
    z_style.add('BACKGROUND', (4,8), (4,8), colors.HexColor('#90EE90'))
    z_style.add('FONTNAME', (4,1), (4,8), 'Helvetica-Bold')
    z_tbl.setStyle(z_style)
    story.append(z_tbl)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("Rechtliche Bewertung — Haftungsrisiken des Geschäftsführers", S['h2']))
    haftungs_punkte = [
        ("§ 43 GmbHG (Sorgfaltspflichtverletzung)",
         "Der Geschäftsführer einer UG/GmbH hat die Sorgfalt eines ordentlichen Kaufmanns anzuwenden. "
         "Die fehlende Rücklagenbildung (§ 5a Abs. 3 GmbHG), das Unterlassen einer 24-Monats-Planung "
         "und das späte Erkennen der Krise begründen Schadensersatzansprüche gegen den GF nach § 43 GmbHG. "
         "Im vorliegenden Fall wäre Schadensersatzpotenzial theoretisch bis EUR 49.680 (Gläubigerschaden)."),
        ("§ 15b InsO (Zahlungsverbote in der Krise)",
         "Ab dem Zeitpunkt, ab dem Zahlungsunfähigkeit vorlag (spätestens Februar 2026), "
         "hätte der Geschäftsführer keine Zahlungen mehr leisten dürfen, die die Gläubigergesamtheit "
         "benachteiligen (§ 15b Abs. 1 InsO). Ausnahmen: Zahlungen, die zur Aufrechterhaltung des "
         "Geschäftsbetriebs unbedingt notwendig waren (§ 15b Abs. 1 S. 2 InsO). "
         "Prüfung erforderlich, ob Zahlungen an einzelne Gläubiger anfechtbar (§§ 129 ff. InsO)."),
        ("§ 266a StGB (Vorenthaltung von Arbeitsentgelt)",
         "Das Vorenthalten von Sozialversicherungsbeiträgen (hier: AOK EUR 4.800 für März/April 2026) "
         "ist strafbar nach § 266a StGB (Freiheitsstrafe bis 5 Jahre oder Geldstrafe). "
         "Der Geschäftsführer haftet persönlich. Rat: Sofortiger Ausgleich hat absoluten Vorrang "
         "vor allen anderen Zahlungen — auch vor Mietrückständen."),
        ("§ 1 StaRUG (Früherkennungspflicht — persönliche Verantwortung)",
         "§ 1 Abs. 1 StaRUG richtet sich persönlich an die Mitglieder des zur Geschäftsführung "
         "berufenen Organs — beim GmbH/UG-GF direkt an diesen. "
         "Die Pflicht zum Aufbau eines Überwachungssystems wird durch Größe und Komplexität "
         "des Unternehmens skaliert — auch ein 3-Filial-Betrieb mit EUR 682.000 Umsatz ist "
         "erfasst. Das vollständige Fehlen jeglichen Systems begründet bei Insolvenzeintritt "
         "Schadensersatzansprüche der Gläubiger nach § 1 Abs. 2 StaRUG i.V.m. § 43 GmbHG."),
    ]
    for titel, text in haftungs_punkte:
        story.append(Paragraph(f"<b>{titel}</b>", S['h3']))
        story.append(Paragraph(text, S['body']))
    story.append(PageBreak())

    # D.12 Stundungsantrag Finanzamt
    story.append(Paragraph("D.12 Stundungsantrag an Finanzamt Berlin-Neukölln", S['h1']))
    story.append(hr(FARBE))
    story.append(Spacer(1, 0.2*cm))

    for line in kanzlei_kopf_wandelmoser():
        story.append(line)
    story.append(Spacer(1, 0.3*cm))

    fa_adresse = [
        "Finanzamt Berlin-Neukoelln",
        "Stundungsabteilung",
        "Karl-Marx-Str. 83-85",
        "12040 Berlin",
    ]
    for z in fa_adresse:
        story.append(Paragraph(z, S['body_left']))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        f"Berlin, den 8. Mai 2026",
        S['body_left']))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "<b>Stundungsantrag gem. § 222 AO</b><br/>"
        "Steuernummer: 27/351/04127 (USt) | Mandant: Salaltbar UG (haftungsbeschränkt)",
        S['h3']))
    story.append(hr())
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "Sehr geehrte Damen und Herren,",
        S['body_left']))
    story.append(Spacer(1, 0.1*cm))
    story.append(Paragraph(
        "in der oben bezeichneten Steuersache stelle ich namens und in Vollmacht der "
        "Salaltbar UG (haftungsbeschränkt), vertreten durch Herrn Tarek-Yusuf Çelebi-Drebenstedt, "
        "hiermit den Antrag, die rückständige Umsatzsteuer für die Voranmeldezeiträume "
        "Q3/2025 und Q4/2025 in Höhe von insgesamt <b>EUR 8.900,00</b> gem. § 222 AO für "
        "die Dauer von <b>12 Monaten</b> (ab dem 1. Juni 2026) zu stunden und "
        "in monatlichen Raten von je <b>EUR 742,00</b> (zuzüglich der gesetzlichen Stundungszinsen "
        "nach § 238 AO) zurückzuführen.",
        S['body_left']))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("Begründung:", S['h3']))
    story.append(Paragraph(
        "1. <b>Wirtschaftliche Lage:</b> Die Mandantin betreibt drei Filialen "
        "(vegane Salat-Bar) und erwirtschaftet einen Gesamtumsatz von ca. EUR 682.000 p.a. "
        "Aufgrund einer außerordentlichen Mieterhöhung in der Filiale Sonnenallee (EUR +1.500/Monat "
        "ab Januar 2024) und mehreren umsatzschwachen Quartalen in 2025 sind rückständige "
        "Steuerzahlungen entstanden. Die Mandantin ist grundsätzlich sanierungsfähig, "
        "befindet sich aber in einer vorübergehenden Liquiditätskrise.",
        S['body_left']))
    story.append(Paragraph(
        "2. <b>Sanierungsmaßnahmen:</b> Mit anwaltlicher Unterstützung werden "
        "derzeit folgende Maßnahmen umgesetzt: (a) Aufhebung Mietvertrag Sonnenallee "
        "(Entlastung EUR 5.200/Monat ab Juni 2026); (b) Ratenvereinbarung mit Hauptlieferant; "
        "(c) Konsolidierung auf zwei rentable Standorte. Die Liquiditätsplanung für die "
        "Folgemonate weist ab Juni 2026 einen positiven Saldo von mindestens EUR 3.500/Monat aus.",
        S['body_left']))
    story.append(Paragraph(
        "3. <b>Stundungsvoraussetzungen (§ 222 AO):</b> Die sofortige Einziehung der "
        "Steuerforderung würde die Fortführung des Unternehmens gefährden (erhebliche Härte "
        "i.S.d. § 222 AO). Der Anspruch des Fiskus ist nach der Sanierung vollständig "
        "erfüllbar. Die Stundungszinsen werden akzeptiert.",
        S['body_left']))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Ich bitte um Bearbeitung dieses Antrags bevorzugt und um Bestätigung der "
        "Stundung bis spätestens 15. Mai 2026, um die Gesamtsanierung zu koordinieren. "
        "Ich stehe für Rückfragen jederzeit zur Verfügung.",
        S['body_left']))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "Mit freundlichen Grüßen",
        S['body_left']))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph(
        "Charlotte Wandelmoser<br/>Rechtsanwältin",
        S['body_left']))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Anlage: Liquiditätsplanung (D.10.III), Aufhebungsvertrag Entwurf (D.8), "
        "Buchhaltungsübersicht Q1-Q4/2025",
        S['footnote']))
    story.append(PageBreak())

    # D.13 Abschluss-Vermerk: § 1 StaRUG-Compliance für Kleinstunternehmen
    story.append(Paragraph("D.13 Kanzlei-Vermerk: § 1 StaRUG bei Kleinstunternehmen — Praxishinweise", S['h1']))
    story.append(hr(FARBE))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "Verfasserin: RAin Charlotte Wandelmoser | Datum: 10. Mai 2026 | Intern",
        S['small']))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "Das vorliegende Mandat Salaltbar UG illustriert exemplarisch, wie die Früherkennungspflicht "
        "des § 1 StaRUG in der Praxis bei Kleinstunternehmen systematisch verletzt wird — nicht aus "
        "Böswilligkeit, sondern aus Unkenntnis. Dieser Vermerk fasst die praxisrelevanten Lehren "
        "für zukünftige Mandate zusammen.",
        S['body']))

    kapitel_d13 = [
        ("1. Der Adressatenkreis des § 1 StaRUG",
         "§ 1 Abs. 1 StaRUG gilt für alle juristischen Personen unabhängig von ihrer Größe. "
         "Auch eine UG mit EUR 1 Stammkapital und 14 Mitarbeitern ist verpflichtet, ein Früherkennungssystem "
         "zu unterhalten. Das Gesetz macht keine Ausnahme für Kleinstunternehmen (anders z.B. § 267a HGB "
         "für die Rechnungslegungserleichterungen). Die herrschende Meinung in der Literatur hält § 1 StaRUG "
         "auch für Kleinstunternehmen anwendbar (vgl. Braun, StaRUG, 2. Aufl. 2022, § 1 Rn. 12 ff.; "
         "Bork/Hölzle, Handbuch Insolvenzrecht, 2022, Kap. 25 Rn. 7). Das OLG Frankfurt hat in einem "
         "Hinweisbeschluss vom 14. Januar 2025 (14 U 88/24, n.v.) angedeutet, dass die "
         "Sorgfaltspflichtverletzung nach § 1 StaRUG i.V.m. § 43 GmbHG auch bei Kleinstunternehmen "
         "schadensersatzbegründend wirken kann."),
        ("2. Mindestanforderungen an das Früherkennungssystem",
         "Die Anforderungen des § 1 StaRUG sind proportional zur Unternehmensgröße zu interpretieren. "
         "Für ein Kleinstunternehmen wie die Salaltbar UG genügt nach herrschender Meinung: "
         "(a) Monatliche Liquiditätsplanung (mind. 3 Monate rollierend); "
         "(b) Halbjährliche betriebswirtschaftliche Auswertung (BWA) mit Steuerberater; "
         "(c) Jährliche Fortbestehensprognose (vereinfacht) für 24 Monate; "
         "(d) Dokumentation der Prüfung im Geschäftsführer-Protokoll. "
         "Nicht erforderlich: Vollständiges IDW S 11-Gutachten, Risikomanagementausschuss, BSC. "
         "Entscheidend ist die Dokumentation — 'Tue Gutes und schreib es auf'."),
        ("3. Die Rücklagenpflicht der UG (§ 5a Abs. 3 GmbHG) als Frühwarnindikator",
         "Häufig übersehen: Die UG ist nach § 5a Abs. 3 GmbHG verpflichtet, in jedem "
         "Geschäftsjahr 1/4 des Jahresgewinns in die gesetzliche Rücklage einzustellen, "
         "bis das Stammkapital EUR 25.000 erreicht. Im vorliegenden Fall hätte die Rücklage "
         "seit 2021 EUR 124 p.a. betragen (1/4 von EUR 498 Jahresgewinn 2021). "
         "Wichtiger als der absolute Betrag: In Jahren mit Verlust ist die Rücklage null — "
         "dies hätte als frühes Warnsignal erkannt werden müssen. "
         "Praxistipp: Mandanten, die als UG kommen, sofort auf § 5a Abs. 3 GmbHG hinweisen. "
         "Rücklagenpflicht-Checkliste in Erstberatungsbogen aufnehmen."),
        ("4. Das Timing der Rechtspflichten: § 1 StaRUG vs. § 15a InsO vs. § 15b InsO",
         "§ 1 StaRUG greift bei drohender Zahlungsunfähigkeit (§ 18 InsO) oder negativer "
         "Fortbestehensprognose — also deutlich früher als die Insolvenzantragspflicht (§ 15a InsO). "
         "Im Fall Salaltbar: Früherkennungspflicht bereits ab Januar 2024 (Mieterhöhung); "
         "Antragspflicht § 15a InsO frühestens ab April 2026 (Zahlungsunfähigkeit). "
         "Der 'Timing-Gap' von ca. 27 Monaten ist der Kernbereich der Beratungsleistung nach StaRUG. "
         "In diesem Zeitfenster können außergerichtliche Sanierungen, StaRUG-Pläne und "
         "Schutzschirmverfahren eingeleitet werden — wenn der GF seinen Pflichten nachkommt."),
        ("5. Empfehlung für Kleinstunternehmer-Beratung",
         "In der Erstberatung von GmbH/UG-Geschäftsführern sollte standardmäßig auf Folgendes "
         "hingewiesen werden: (1) § 1 StaRUG und Früherkennungspflicht (kurze Erläuterung); "
         "(2) Rücklagenpflicht § 5a Abs. 3 GmbHG bei UGs; "
         "(3) Sozialversicherungsbeitrags-Vorrang (§ 266a StGB); "
         "(4) Dreiwochenfrist § 15a InsO; "
         "(5) Möglichkeit außergerichtlicher Sanierung bei frühzeitigem Handeln. "
         "Schriftliche Dokumentation dieser Hinweise in Mandatsannahmeprotokoll. "
         "Haftungsschutz für die Kanzlei: Aufklärungspflicht des Anwalts nach § 280 BGB i.V.m. "
         "dem Anwaltsvertrag kann verletzt werden, wenn auf § 1 StaRUG nicht hingewiesen wurde."),
    ]
    for titel, text in kapitel_d13:
        story.append(Paragraph(f"<b>{titel}</b>", S['h2']))
        story.append(Paragraph(text, S['body']))
        story.append(Spacer(1, 0.1*cm))
    story.append(PageBreak())

    # D.14 Checkliste Erstberatung UG/GmbH-GF § 1 StaRUG
    story.append(Paragraph("D.14 Praxis-Checkliste: Erstberatung GmbH/UG-Geschäftsführer — § 1 StaRUG", S['h1']))
    story.append(hr(FARBE_D))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Kanzlei Wandelmoser | Internes Arbeitsmittel | Version 1.3 | Mai 2026",
        S['small']))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Diese Checkliste ist als Gesprächsleitfaden für das Erstberatungsgespräch mit "
        "GmbH- und UG-Geschäftsführern zu verwenden, bei denen ein Krisenfrüherkennungsdefizit "
        "nach § 1 StaRUG vermutet wird. Bitte alle Punkte dokumentieren.",
        S['body']))
    story.append(Spacer(1, 0.2*cm))

    checkliste_data = [
        ['#', 'Prüfpunkt', 'Ergebnis / Antwort', 'Risikoampel'],
        ['1', 'Rechtsform und Registrierung\n(GmbH, UG, AG, SE?)', '', 'o'],
        ['2', 'Stammkapital / Grundkapital\n(UG: Rücklagenpflicht § 5a GmbHG?)', '', 'o'],
        ['3', 'Letzte testierte Bilanz\n(Wann? Durch wen?)', '', 'o'],
        ['4', 'Jahresergebnis letztes GJ\n(Gewinn/Verlust?)', '', 'o'],
        ['5', 'Vorliegende Verlustjahre\n(wie viele, in Folge?)', '', 'o'],
        ['6', 'Liquiditätsplanung vorhanden?\n(Zeitraum, Aktualität)', '', 'o'],
        ['7', 'Bekannte Zahlungsrückstände\n(Fälligkeit, Betrag, Gläubiger)', '', 'o'],
        ['8', 'Finanzamtsrückstände / Steuerrückstände\n(USt, LSt, KSt)', '', 'o'],
        ['9', 'SV-Beiträge aktuell?\n(§ 266a StGB-Risiko!)', '', 'o'],
        ['10', 'Kreditlinien / Bankverbindlichkeiten\n(Kündigung droht?)', '', 'o'],
        ['11', 'Laufende Leasingverträge\n(Rückstände? Kündigung?)', '', 'o'],
        ['12', 'Mietverträge (Gewerbe)\n(Rückstände? Laufzeit?)', '', 'o'],
        ['13', 'Wichtige Lieferanten\n(Lieferstop? Rückstände?)', '', 'o'],
        ['14', 'Bekannte Restrukturierungs-\nmaßnahmen bereits eingeleitet?', '', 'o'],
        ['15', 'Steuerberater involviert?\n(Name, Kontakt)', '', 'o'],
        ['16', 'Andere Anwälte / Berater\n(potentielle Interessenkonflikte?)', '', 'o'],
        ['17', '§ 1 StaRUG bekannt?\n(GF informiert über Früherkennungspflicht?)', '', 'o'],
        ['18', 'Bisherige GF-Protokolle / Berichte\n(Sitzungsprotokoll Gesellschafter?)', '', 'o'],
        ['19', 'Persönliche Bürgschaften / Haftungen\n(Umfang?)', '', 'o'],
        ['20', 'Insolvenzantrag bereits erwogen?\n(§ 15a InsO Frist geprüft?)', '', 'o'],
    ]
    ck_tbl = Table(checkliste_data, colWidths=[0.7*cm, 6.8*cm, 6.8*cm, 3.2*cm])
    ck_style = tbl_style_standard()
    ck_style.add('FONTSIZE', (0,0), (-1,-1), 8)
    ck_style.add('BACKGROUND', (3,9), (3,9), colors.HexColor('#FF6B6B'))  # SV-Beiträge
    ck_style.add('FONTNAME', (3,9), (3,9), 'Helvetica-Bold')
    ck_tbl.setStyle(ck_style)
    story.append(ck_tbl)
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "Ampellegende: GRÜN = kein Risiko | GELB = Beobachtung erforderlich | ROT = sofortiger Handlungsbedarf | SCHWARZ = Insolvenzantragspflicht. "
        "Felder 'Ergebnis / Antwort' sind im Gespräch auszufüllen und im Mandatsprotokoll zu dokumentieren. "
        "Checkliste ist Teil der Beratungsakte und dient als Haftungsschutz-Nachweis.",
        S['footnote']))
    story.append(PageBreak())


def main():
    """Hauptfunktion: Erzeugt das komplette Konvolut-PDF."""
    story = []

    # 1. Konvolut-Aktendeckel
    build_konvolut_deckel(story)

    # 2. Vorbemerkung
    build_vorbemerkung(story)

    # 3. Vergleichstabelle
    build_vergleichstabelle(story)

    # 4. Variante A
    build_trennblatt(story, "A",
                     "VEYRA AI Foundation gGmbH",
                     "KI-Forschungs-gGmbH  |  Frankfurt am Main",
                     "AG Frankfurt 810 RES 14/26", FARBE_A)
    build_variante_a(story)
    build_variante_a_extended(story)

    # 5. Variante B
    build_trennblatt(story, "B",
                     "HERRENBLUSE & ZWIRN HARTMANNSCHMIDT AG",
                     "Hemdenmanufaktur  |  Bamberg",
                     "AG Bamberg 53 RES 7/26", FARBE_B)
    build_variante_b(story)
    build_variante_b_extended(story)

    # 6. Variante C
    build_trennblatt(story, "C",
                     "NORDFELS POWER CELLS SE",
                     "Batteriehersteller  |  Ellwangen",
                     "AG Stuttgart 14 RES 22/26", FARBE_C)
    build_variante_c(story)
    build_variante_c_extended(story)

    # 7. Variante D
    build_trennblatt(story, "D",
                     "SALALTBAR UG (haftungsbeschraenkt)",
                     "Vegane Salat-Bar-Kette  |  Berlin-Neukoelln",
                     "AG Charlottenburg 36 IN 412/26", FARBE_D)
    build_variante_d(story)
    build_variante_d_extended(story)  # Erweiterung: Mietaufhebung, Liquidationsrechnung, Sanierungsplan

    # 8. Trennblatt Vorlagen-Annex
    story.append(PageBreak())
    build_vorlagen_annex(story)

    # 9. Trennblatt Foliensatz
    story.append(PageBreak())
    story.append(Paragraph("FOLIENSATZ", S['h_kapitel']))
    story.append(Paragraph(
        "Impulsvortrag Restructuring Lounge Hamburg  |  WAYES  |  28. Mai 2026",
        S['subtitle_cap']))
    story.append(hr(DUNKELBLAU, thickness=2))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "Die nachfolgenden acht Folien entsprechen der Praesentations-Folie des Impulsvortrags "
        "von Dr. Tjark Reher-Bornholmsen auf der WAYES Restructuring Lounge Hamburg am 28. Mai 2026 "
        "zum Thema 'Krisen-Frueherkennung nach ss 1 StaRUG -- Pflicht, nicht Option'. "
        "Jede Folie ist als eigenstaendige Seite mit Folien-Rahmen dargestellt.",
        S['body']))
    story.append(PageBreak())
    build_foliensatz(story)

    # 10. Stundenaufstellung
    build_stundenaufstellung(story)

    # PDF erzeugen
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        rightMargin=2.0*cm,
        leftMargin=2.0*cm,
        topMargin=2.5*cm,
        bottomMargin=2.0*cm,
        title="Testakte Krisen-Frueherkennung StaRUG -- Vier Varianten",
        author="Reher Wennstedt Restrukturierung Partnerschaft mbB (fiktiv)",
        subject="ss 1 StaRUG Krisen-Frueherkennung -- Lehrakte",
        creator="generate_testakte.py"
    )

    def on_page(canvas_obj, doc_obj):
        page_standard(canvas_obj, doc_obj,
                      aktenzeichen="Konvolut: AG Frankfurt / Bamberg / Stuttgart / Charlottenburg",
                      betreff="Krisen-Frueherkennung ss 1 StaRUG -- Vier Varianten")

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)

    import os as _os
    fsize = _os.path.getsize(OUTPUT)
    print(f"PDF erzeugt: {OUTPUT}")
    print(f"Dateigroesse: {fsize:,} Bytes ({fsize/1024/1024:.1f} MB)")

    # Seitenanzahl schaetzen
    with open(OUTPUT, 'rb') as f:
        content = f.read()
    import re
    pages_found = len(re.findall(b'/Type\\s*/Page[^s]', content))
    print(f"Seitenanzahl (geschaetzt): {pages_found}")

    print("")
    print("VALIDIERUNG:")
    print(f"  Pfad:          {OUTPUT}")
    print(f"  Variante A:    VEYRA AI Foundation gGmbH | AG Frankfurt 810 RES 14/26")
    print(f"  Variante B:    HERRENBLUSE & ZWIRN HARTMANNSCHMIDT AG | AG Bamberg 53 RES 7/26")
    print(f"  Variante C:    NORDFELS POWER CELLS SE | AG Stuttgart 14 RES 22/26")
    print(f"  Variante D:    SALALTBAR UG | AG Charlottenburg 36 IN 412/26")
    print(f"  Seiten >= 90:  {'JA' if pages_found >= 90 else 'PRUEFEN -- ' + str(pages_found)}")


if __name__ == "__main__":
    main()
