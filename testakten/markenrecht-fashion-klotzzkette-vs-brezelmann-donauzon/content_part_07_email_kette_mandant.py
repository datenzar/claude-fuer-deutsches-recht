# Part 07: E-Mail-Kette Comtesse <-> RAin Steinacker (5 Mails)
def _mailheader(_from, _to, _date, _subj, _cc=None):
    head = (f"From:    {_from}\n"
            f"To:      {_to}\n"
            + (f"Cc:      {_cc}\n" if _cc else "")
            + f"Date:    {_date}\n"
            f"Subject: {_subj}\n"
            f"--------------------------------------------------------------------------------\n")
    return head

def blatt_email_kette_1():
    s = []
    s.append(Paragraph("<b>E-Mail-Korrespondenz Mandantin ./. Federführende Partnerin (chronol.)</b>",
                        S_CENTER))
    s.append(HLine())
    s.append(Paragraph("— Ausdruck aus beA-PostfachExport am 22.05.2026, 17:48 Uhr —", S_RIGHT))
    s.append(Spacer(1, 0.2*cm))
    mails = [
        ("=== MAIL 1 von 5 ===",
"""From:    Comtesse B. de Klôtzzkètté-Visconti <comtesse@klotzzkette.com>
To:      Dr. Dr. A. Steinacker-von Tarsis <steinacker@steinacker-lichtenberg.de>
Date:    13.01.2026  08:42  CET
Subject: Confirmation de mandat — affaire Brezelmann
--------------------------------------------------------------------------------

Madame le Docteur,

je vous remercie pour notre conversation très enrichissante d'hier. Veuillez
trouver ci-joint la procuration signée. Je vous prie de procéder avec toute
la fermeté nécessaire — la Maison ne tolère aucune contrefaçon. Onkel Cosimo
sendet ebenfalls Grüße.

Avec mes salutations distinguées,

Béatrice de Klôtzzkètté-Visconti
Comtesse, Présidente d'honneur klôtzzkètté S.A."""),
        ("=== MAIL 2 von 5 ===",
"""From:    Dr. Dr. A. Steinacker-von Tarsis <steinacker@steinacker-lichtenberg.de>
To:      Comtesse B. de Klôtzzkètté-Visconti <comtesse@klotzzkette.com>
Cc:      M. v. Brenkenhoff <brenkenhoff@steinacker-lichtenberg.de>
Date:    13.01.2026  09:55  CET
Subject: AW: Confirmation de mandat — affaire Brezelmann
--------------------------------------------------------------------------------

Sehr geehrte Madame la Comtesse,

vielen herzlichen Dank für die zugeleitete Vollmacht. Wir haben unverzüglich
folgende Maßnahmen eingeleitet:

  (1) förmliche Abmahnung an Brezelmann Discount KG, Frist 06.02.2026;
  (2) Vorbereitung Widerspruch EUIPO gg. UAB klotzkettie (Frist 14.04.2026);
  (3) Recherche zur DSA-Notice ggü. Donauzon Marketplace;
  (4) Abstimmungsgespräch mit Hr. Whitman III (NYC) für 14.01.2026, 16:00 MEZ
      (= 10:00 EST) vereinbart.

Ich werde Sie über jeden Verfahrensschritt umgehend informieren.

Mit verbindlichen Grüßen
Dr. Dr. Annabella Steinacker-von Tarsis, LL.M. (Cantab.)
Partnerin · Steinacker Lichtenberg & Partners IP Boutique"""),
        ("=== MAIL 3 von 5 ===",
"""From:    Comtesse B. de Klôtzzkètté-Visconti <comtesse@klotzzkette.com>
To:      Dr. Dr. A. Steinacker-von Tarsis <steinacker@steinacker-lichtenberg.de>
Date:    04.02.2026  19:21  CET
Subject: ces gens sont d'une vulgarité…
--------------------------------------------------------------------------------

Chère Annabella,

je viens de recevoir copie du télécopie de ces… personnes. Brezelmann!! Le
nom seul suffit déjà à m'écœurer. Quelle insolence!! Et leur post-scriptum
sur les T-shirts à moins de 10 euros — mon dieu, c'est d'une vulgarité
sans nom!!

Je vous prie instamment, ma chère, de NE PAS reculer. Que toutes les
mesures soient prises — sans pitié! Il faut que ces vendeurs de saucisses
apprennent qu'on ne joue pas avec la Maison K°°!!

J'ai déjà fait préparer le jet privé pour assister à l'audience à
Francfort — ne me dites pas que cela ne se fait pas, je serai présente
qu'on le veuille ou non.

Béatrice

P.S.: Onkel Cosimo a vu d'autres flacons hexagonaux dans un magasin
      à Bologne. Je vais l'envoyer y faire un repérage."""),
    ]
    for label, body in mails:
        s.append(Paragraph(f"<b>{label}</b>", S_NORMAL_LEFT))
        s.append(Preformatted(body, S_MONO_SMALL))
        s.append(Spacer(1, 0.2*cm))
    return s

story += blatt_email_kette_1()
story.append(PageBreak())

def blatt_email_kette_2():
    s = []
    s.append(Paragraph("<b>E-Mail-Kette (Forts. 4-5)</b>", S_CENTER))
    s.append(HLine())
    s.append(Spacer(1, 0.2*cm))
    mails = [
        ("=== MAIL 4 von 5 ===",
"""From:    Dr. Dr. A. Steinacker-von Tarsis <steinacker@steinacker-lichtenberg.de>
To:      Comtesse B. de Klôtzzkètté-Visconti <comtesse@klotzzkette.com>
Date:    05.02.2026  10:14  CET
Subject: AW: ces gens sont d'une vulgarité…
--------------------------------------------------------------------------------

Sehr geehrte Madame la Comtesse,

vielen Dank für Ihre Nachricht. Lassen Sie mich Ihre Sorgen sofort zerstreuen:
Wir bereiten den Antrag auf Erlass einer einstweiligen Verfügung bei dem
LG Frankfurt am Main vor (Vors. RaG Dr. Hoffacker-Wendel — bekannt für
markenrechtsfreundliche Linie). Vollziehung in Florenz auf Pitti Uomo
(11.-15.03.2026) ist taktisches Ziel.

Hinsichtlich Ihrer Anwesenheit bei einer ggf. mündlichen Verhandlung: wir
werden ohne mündliche Verhandlung beantragen (§ 937 Abs. 2 ZPO), so dass
sich Ihre Reise erübrigt. Sollte die Gegenseite Widerspruch einlegen, kommt
es zu einer mündlichen Verhandlung — dann gerne mit Ihrer (sehr willkommenen!)
Begleitung.

Bzgl. des Hinweises auf Bologna — bitte lassen Sie Onkel Cosimo Fotos
machen und unmittelbar an die Detektei Spürnase-Couture GmbH (Fr. Kalt-Bandel)
schicken. Die Mailadresse lautet: k.kaltbandel@spuernase-couture.de

Mit verbindlichen Grüßen
Annabella St-vT"""),
        ("=== MAIL 5 von 5 ===",
"""From:    Comtesse B. de Klôtzzkètté-Visconti <comtesse@klotzzkette.com>
To:      Dr. Dr. A. Steinacker-von Tarsis <steinacker@steinacker-lichtenberg.de>
Cc:      atelier@klotzzkette.com; M. v. Brenkenhoff
Date:    12.03.2026  16:08  CET
Subject: PITTI — VICTOIRE!!! 🥂
--------------------------------------------------------------------------------

Chère Annabella, cher Maximilien,

QUELLE JOIE!!! La nouvelle vient de m'arriver de Florence. Le carabinier
Garibaldi a été MAGNIFIQUE!!! On m'a envoyé une photo où l'on voit
Brezelmann (cet horrible homme) en train de tenter de voler ses propres
flacons de la table des saisies!!! Je vais l'encadrer.

Annabella, ma chère, vous êtes UN GÉNIE. Je vous fais envoyer demain par
courrier express un cadeau personnel de l'atelier (un foulard K°° Touch
Royal — ne refusez pas, c'est un ordre).

Et n'oubliez pas: l'Amérique est la prochaine étape!! Mes chéris, n'oubliez
pas New York! L'Amérique aussi doit s'agenouiller devant K°°!!

Béatrice

P.S. — J'envoie Onkel Cosimo à NYC la semaine prochaine pour rencontrer
       Mr. Whitman III. Il parle anglais avec un accent vénitien qui
       fait son charme."""),
    ]
    for label, body in mails:
        s.append(Paragraph(f"<b>{label}</b>", S_NORMAL_LEFT))
        s.append(Preformatted(body, S_MONO_SMALL))
        s.append(Spacer(1, 0.2*cm))
    s.append(HandNote(
        "→ Onkel Cosimo nach NYC?? Whitman III bitte vorwarnen!\n→ Geschenk-Foulard: dankend annehmen — Geschenk-Annahme-Erlass §17 BORA prüfen.\n→ ASt",
        font=FONT_HAND, size=13, color=colors.HexColor("#345"), w=15*cm, angle=-0.3))
    return s

story += blatt_email_kette_2()
story.append(PageBreak())

print("[part07] done")
