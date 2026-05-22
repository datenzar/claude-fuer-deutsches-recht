# -*- coding: utf-8 -*-
# Part 39: Final Fragmente — Telefax aus Cap d'Antibes, GV-Protokoll, Aktennotiz, IT-Forensik

def blatt_telefax_capdantibes():
    s = []
    s.append(FaxHeader(
        from_no="+33 4 93 61 ** **",
        to_no="+49 89 28 99 ** **",
        date="21.05.2026, 07:14 CET",
        pages="1 / 1",
        subject="Affaire klôtzzkètté c/ Brezelmann et al.",
        sender="Comtesse B. de Klôtzzkètté-Visconti — Cap d'Antibes",
        recipient="RA Dr. Dr. A. Steinacker-von Tarsis, München"))
    s.append(Spacer(1, 2*mm))
    data = [
        ["VON:", "Maison Klôtzzkètté · Villa »Les Glycines«"],
        ["", "Boulevard du Cap, 06160 Cap d'Antibes, France"],
        ["", "Tél: +33 4 93 61 ** ** &nbsp;·&nbsp; Fax: +33 4 93 61 ** **"],
        ["AN:", "Steinacker Lichtenberg &amp; Partners IP Boutique"],
        ["", "z.Hd. RA Dr. Dr. A. Steinacker-von Tarsis"],
        ["", "Maximiliansplatz 19, D-80333 München"],
        ["DATUM:", "21. Mai 2026 / le 21 mai 2026"],
        ["UHRZEIT:", "07:14 CET (Empfang München: 07:15)"],
        ["SEITEN:", "1 (eine) Seite, einschließlich dieser"],
        ["BETREFF:", "Affaire klôtzzkètté c/ Brezelmann et autres — observations urgentes"],
    ]
    t = Table(data, colWidths=[25*mm, 145*mm])
    t.setStyle(TableStyle([
        ('FONT', (0,0), (-1,-1), "Courier", 9),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 2),
        ('RIGHTPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    s.append(t)
    s.append(HLine())
    s.append(Spacer(1, 2*mm))
    s.append(Paragraph(
        "Cher Maître Steinacker,",
        S_FAX))
    s.append(Paragraph(
        "j'ai relu hier soir, à la lumière du clair de lune sur la Méditerranée, l'ensemble "
        "du dossier que vous avez eu l'amabilité de m'envoyer par valise diplomatique (merci "
        "à votre Madame Brenkenhoff, charmante!). Quelques remarques en vrac:",
        S_FAX))
    s.append(Paragraph(
        "1°) Le rapport Pinkerton est admirable mais — entre nous — la photo n° B-7 où l'on "
        "voit Monsieur Kalman entrer dans le café Sant Ambroeus me semble compromettante "
        "uniquement si l'on PROUVE qui est l'autre monsieur. Demandez-leur la pièce d'identité, "
        "diable!",
        S_FAX))
    s.append(Paragraph(
        "2°) Concernant l'offre de Donauzon à EUR 1,25 mio: refus catégorique. Mon grand-père "
        "Antoine-Louis n'a pas fondé la Maison en 1923 pour qu'on la brade en 2026. "
        "Contre-proposition: EUR 3,8 mio + filtrage permanent + excuses publiques sur la page "
        "d'accueil de Donauzon (au moins 30 jours, police minimum 14 points, en allemand, "
        "français et italien).",
        S_FAX))
    s.append(Paragraph(
        "3°) Au sujet de Maître Whitman: ses honoraires sont absolument scandaleux mais "
        "<i>parfaitement justifiés</i>. Continuez. Mes chéris, n'oubliez pas New York!",
        S_FAX))
    s.append(Paragraph(
        "4°) Le whistleblower — comment dit-on en allemand? <i>Pétard mouillé</i> ou "
        "<i>cheval de Troie</i>? Méfiance. Faites-le surveiller par Madame Kalt-Bandel.",
        S_FAX))
    s.append(Paragraph(
        "5°) Mon fils Augustin-Marie souhaite assister à l'audience de Florence. Je le lui ai "
        "interdit. Il a 23 ans et passerait son temps à boire des Negroni au Caffè Gilli. "
        "Mais — il a tout de même hérité d'une partie du capital, donc tenez-le informé "
        "<i>poliment et brièvement</i>.",
        S_FAX))
    s.append(Paragraph(
        "Très cordialement,<br/><br/>Béatrice de Klôtzzkètté-Visconti<br/>"
        "<i>Présidente du Conseil d'Administration</i>",
        S_FAX))
    s.append(Spacer(1, 2*mm))
    s.append(Paragraph("[Faxstempel Eingang München: 21.05.2026 07:15 — Kürzel »St.-v.T.« "
                       "+ rote Tinte »EILT — sofort Whitman cc.«]", S_TINY))
    return s


def blatt_gv_protokoll():
    s = []
    s.append(Paragraph("GERICHTSVOLLZIEHERPROTOKOLL", S_H1))
    s.append(Paragraph("über die Vornahme einer Sicherheitsleistung &amp; Zustellung "
                       "der einstweiligen Verfügung des LG Frankfurt vom 11.06.2026 — "
                       "Az. 2-03 O 412/26 EV", S_CENTER))
    s.append(HLine())
    s.append(Paragraph("Gerichtsvollzieher: <b>Obergerichtsvollzieher Wolfram Knöllgen</b>, "
                       "Bezirk Bad Mergentheim, GV-Nr. WM-1147", S_NORMAL))
    s.append(Paragraph("Geschäftsstelle: Amtsgericht Bad Mergentheim, Schloß 8, 97980 Bad Mergentheim", S_NORMAL))
    s.append(Paragraph("Auftrag: Steinacker Lichtenberg &amp; Partners (Bevollmächtigte der Klägerin)", S_NORMAL))
    s.append(Paragraph("Tag der Vornahme: <b>Dienstag, 16.06.2026</b>, Beginn 08:47 Uhr", S_NORMAL))
    s.append(Paragraph("Ort: Wurstgasse 4, 97980 Bad Mergentheim (Geschäftslokal Brezelmann Discount KG)", S_NORMAL))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph(
        "<b>I.</b> Der unterzeichnete Gerichtsvollzieher begab sich heute, dem 16.06.2026, um "
        "08:47 Uhr in die Geschäftsräume des Schuldners. In der Eingangstür war ein Schild "
        "»Wegen Inventur geschlossen — wir bitten um Verständnis« angebracht. Auf wiederholtes "
        "Klingeln öffnete eine ältere Dame (sich vorstellend als Frau Edeltraud Brezelmann, "
        "Ehefrau des Geschäftsführers), die zunächst angab, ihr Mann sei »auf Geschäftsreise "
        "in Rumänien«. Auf den Hinweis des unterzeichneten Gerichtsvollziehers, ein PKW Marke "
        "Mercedes Sprinter (KFZ-Kennzeichen TBB-EB 1923, lt. Halterabfrage auf den Schuldner "
        "zugelassen) stehe vor der Tür mit warmem Motor, korrigierte sich Frau Brezelmann "
        "dahingehend, ihr Mann sei »vor wenigen Minuten« zurückgekehrt.",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "<b>II.</b> Es erschien sodann der Schuldner, Herr Egon Brezelmann, in Arbeitskleidung "
        "(Kittel »Brezelmann Discount — alles muss raus!«). Der Schuldner zeigte sich zunächst "
        "verbal aggressiv (»Was wollen Sie denn schon wieder, ich habe doch nichts gemacht!«), "
        "ließ sich aber durch ruhiges Auftreten des Unterzeichneten beruhigen.",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "<b>III.</b> Dem Schuldner wurde sodann zugestellt: (a) die einstweilige Verfügung des "
        "Landgerichts Frankfurt am Main vom 11.06.2026, 14 Seiten, in beglaubigter Abschrift "
        "nebst Übersetzungsanlagen; (b) Aufforderung zur Sicherheitsleistung in Höhe von "
        "EUR 12.000 binnen 14 Tagen. Der Schuldner unterzeichnete die Empfangsbestätigung "
        "<i>unter Vorbehalt</i> mit dem Zusatz: »ich erkenne nix an, Herr Knöllgen, gar nix, "
        "und das wissen Sie auch!«.",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "<b>IV.</b> Im Geschäftslokal befanden sich nach Augenschein des Unterzeichneten "
        "weiterhin Schals und Krawatten der streitgegenständlichen Kollektion in einer "
        "Sammelbox »Sonderposten 14,99« (geschätzt 80-120 Stück). Auf entsprechende Belehrung "
        "verpflichtete sich der Schuldner mündlich, diese Waren unverzüglich aus dem Verkauf "
        "zu nehmen. Eine schriftliche Bestätigung verweigerte er mit der Begründung, sein "
        "Anwalt habe ihm »wegen so was zu unterschreiben« abgeraten.",
        S_NORMAL_LEFT))
    s.append(Paragraph(
        "<b>V.</b> Beendigung der Vornahme: 09:31 Uhr. Dauer: 44 Minuten. Reise- und "
        "Wegegeld: EUR 18,40. Gebühr nach Nr. 100 KV GvKostG: EUR 12,00. Auslagen: EUR 4,50. "
        "Gesamt: EUR 34,90.",
        S_NORMAL_LEFT))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("Bad Mergentheim, den 16.06.2026", S_RIGHT))
    s.append(Paragraph("(W. Knöllgen)<br/>Obergerichtsvollzieher", S_RIGHT))
    s.append(Spacer(1, 2*mm))
    s.append(Paragraph("[Stempel: <b>Gerichtsvollzieher · Amtsgericht Bad Mergentheim · "
                       "GV-Nr. WM-1147</b>]", S_TINY))
    return s


def blatt_it_forensik():
    s = []
    s.append(Paragraph("Dr. Karl-Heinz Vogelstein-Mommsen", S_H2))
    s.append(Paragraph("ö.b.u.v. Sachverständiger für IT-Forensik und digitale "
                       "Markenrechtsverletzungen · IHK Rhein-Neckar", S_CENTER))
    s.append(Paragraph("Hauptstraße 187, 69117 Heidelberg · Tel. 06221 / 778-4044", S_TINY))
    s.append(HLine())
    s.append(Paragraph("<b>FORENSISCHES GUTACHTEN</b> (Zwischenbericht)", S_H3))
    s.append(Paragraph("Aktenzeichen: VM-2026-IT-0117", S_NORMAL))
    s.append(Paragraph("Auftraggeber: Steinacker LLP, München (für klôtzzkètté S.A.)", S_NORMAL))
    s.append(Paragraph("Untersuchungsgegenstand: Domains klotzkettiee.shop, klotzkette-outlet.eu, "
                       "kk-luxe.lt, kkoriginal.de, k-luxe-store.fr, klotzkettie.us; "
                       "zugehörige Donauzon-Shopsysteme; SSL/TLS-Zertifikate; "
                       "WHOIS &amp; passive DNS", S_NORMAL))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("<b>1. FESTSTELLUNGEN</b>", S_H3))
    data = [
        ["#", "Domain", "Registrar", "Reg. seit", "Server-Standort", "Identifizierter Inhaber"],
        ["1", "klotzkettiee.shop", "Namecheap Inc.", "11.01.2026", "Frankfurt (Hetzner)", "Privacy-Service / lt. DNS-TXT: »KK Trading SARL Lux«"],
        ["2", "klotzkette-outlet.eu", "EURid via Gandi", "07.02.2026", "Roubaix (OVH)", "EOOD Sredetz, Sofia (Strohmann?)"],
        ["3", "kk-luxe.lt", "Domreg LT", "23.10.2025", "Vilnius (Telia LT)", "UAB klotzkettie, Vilniaus g. 47"],
        ["4", "kkoriginal.de", "Strato AG", "14.03.2026", "Berlin (Strato)", "Egon Brezelmann, Wurstgasse 4, Bad Mergentheim"],
        ["5", "k-luxe-store.fr", "OVH", "29.01.2026", "Gravelines (OVH)", "Privacy / Rück-Tracing: Donauzon-IP-Block 213.165.94.*"],
        ["6", "klotzkettie.us", "GoDaddy", "02.02.2026", "Phoenix AZ", "Klotzkettie LLC, 251 Little Falls Dr, Wilmington DE"],
    ]
    t = Table(data, colWidths=[7*mm, 32*mm, 22*mm, 18*mm, 30*mm, 60*mm], repeatRows=1)
    t.setStyle(TableStyle([
        ('FONT', (0,0), (-1,0), "Times-Bold", 7.5),
        ('FONT', (0,1), (-1,-1), "Times-Roman", 7),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('GRID', (0,0), (-1,-1), 0.25, colors.grey),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 2),
        ('RIGHTPADDING', (0,0), (-1,-1), 2),
    ]))
    s.append(t)
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("<b>2. NETZWERK-FORENSIK (Auszug)</b>", S_H3))
    s.append(ASCIIBox(r"""
[Passive DNS — A-Records aller 6 Domains, 2026-03-01 bis 2026-05-15]

  klotzkettiee.shop      → 88.198.117.221   (Hetzner FRA)  ★
  klotzkette-outlet.eu   → 51.91.244.118    (OVH RBX)
  kk-luxe.lt             → 78.157.66.42     (Telia VNO)    ★★
  kkoriginal.de          → 81.169.144.99    (Strato BER)
  k-luxe-store.fr        → 51.91.244.118    (OVH RBX)      ← gleicher Server wie #2
  klotzkettie.us         → 184.168.221.71   (GoDaddy PHX)

★    Server hosted weitere 14 Domains — alle markenverdächtig (z.B. cha-nelle-store.shop,
     diior-outlet.shop, gucchi-prive.shop) → eindeutiger Counterfeit-Hub
★★   gemeinsamer SOA-Mailcontact:  mb1923@protonmail.com   (Mindaugas Brezelmanas?)

[SSL-Zertifikate]
   #1, #2, #5, #6: identische Cloudflare-Origin-Cert-Chain → gleiche Backend-Infra
   #4 (kkoriginal.de): self-signed bis 04.03.2026, danach Let's Encrypt

[Donauzon-Shopaccounts — Verknüpfung]
   Account "KK-Luxe-Outlet"       → Auszahlungsbank: Šiaulių Bankas, LT-IBAN-Endung ...4422
   Account "Original-Frankreich"  → gleiche IBAN-Endung ...4422   (!!)
   Account "Klassik-Mode-DE"      → IBAN DE...6611 = Konto Brezelmann Discount KG
"""))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph("<b>3. VORLÄUFIGES FAZIT.</b> Mit an Sicherheit grenzender Wahrscheinlichkeit "
                       "handelt es sich um ein einheitliches, koordiniertes Vertriebsnetzwerk mit "
                       "Schwerpunkten Vilnius (Produktion/Großhandel), Luxembourg (Finanzfluss) und "
                       "Bad Mergentheim (DE-Frontend Brezelmann). Die identische IBAN-Endung "
                       "...4422 für zwei nominell verschiedene Donauzon-Konten ist beweistechnisch "
                       "<i>besonders aussagekräftig</i>.", S_NORMAL_LEFT))
    s.append(Paragraph("Heidelberg, den 18.05.2026", S_RIGHT))
    s.append(Paragraph("(Dr. K.-H. Vogelstein-Mommsen)<br/>öffentlich bestellt &amp; vereidigt", S_RIGHT))
    return s


def blatt_schluss():
    s = []
    s.append(Paragraph("AKTENVERMERK — vorläufiger Schluss", S_H2))
    s.append(Paragraph("(zugleich Querverweisliste für die weitere Bearbeitung)", S_TINY))
    s.append(HLine())
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph(
        "Diese Akte umfasst den Stand bis 22.05.2026. Sie ist <b>fragmentarisch</b> und enthält "
        "(absichtlich oder versehentlich) Querverweise auf Aktenstellen, die in dieser Bändigung "
        "nicht enthalten sind. Insbesondere:",
        S_NORMAL))
    s.append(Paragraph("• Blatt 22 (Rauminhalt-Zeichnung Boutique Madison Ave) — nicht eingeheftet", S_NORMAL))
    s.append(Paragraph("• Blatt 47 (Sieckmann-Hinterlegung Duftmarke »K°° pour Femme«) — wird "
                       "nachgereicht", S_NORMAL))
    s.append(Paragraph("• Blatt 89 (EUIPO B 4 187 932, Tab. d. eingetragenen Klassen) — siehe "
                       "Beistück Bd. II", S_NORMAL))
    s.append(Paragraph("• Blatt 134 (TTAB Disclosure Schedule, kompletter Bates-Range "
                       "KLZK-USP-000001-000477) — auf USB-Stick in Beistück Bd. III", S_NORMAL))
    s.append(Paragraph("• Blatt 178 (Compliance-Memo Pétard, mit Anhängen P-01 bis P-44) — "
                       "in Tresor-Akte (nur Steinacker-Partner-Zugriff)", S_NORMAL))
    s.append(Paragraph("• Blatt 199 (handschriftliche Anmerkungen Comtesse zur Strategie "
                       "Q4/2026) — Original in Cap d'Antibes, Kopie in Vorbereitung", S_NORMAL))
    s.append(Spacer(1, 3*mm))
    s.append(Paragraph(
        "<i>Lite pendente nihil innovetur</i> — aber zwischen Paris, München, Frankfurt, "
        "Florenz, New York, Vilnius, Luxemburg und (bald) Brasília fragt sich, was hier "
        "überhaupt noch <i>nicht</i> innoviert wird.",
        S_ITAL))
    s.append(Spacer(1, 4*mm))
    s.append(Paragraph("München, den 22. Mai 2026", S_RIGHT))
    s.append(Paragraph("Dr. Dr. A. Steinacker-von Tarsis<br/>"
                       "<i>für die Aktenführung:</i> Ref. Dr. Mecklenburg-Pries", S_RIGHT))
    s.append(Spacer(1, 6*mm))
    s.append(Paragraph("— Ende der vorläufigen Bändigung —", S_CENTER))
    s.append(Paragraph("<i>Fortsetzung folgt in Bd. II (Bl. 226 ff.).</i>", S_CENTER))
    return s


story += blatt_telefax_capdantibes()
story.append(PageBreak())
story += blatt_gv_protokoll()
story.append(PageBreak())
story += blatt_it_forensik()
story.append(PageBreak())
story += blatt_schluss()
story.append(PageBreak())
print("[part39] done")
