# Part 22: Transatlantic email chain Steinacker (München) ↔ Whitman III (NYC)
# with timezone conflicts MEZ/EST/EDT

def email_block(headers, body_lines, style=None):
    style = style or S_MONO_SMALL
    s = []
    s.append(HLine(thickness=0.5, color=colors.HexColor("#666")))
    for k, v in headers:
        s.append(Paragraph(f"<b>{k}</b>  {v}", style))
    s.append(HLine(thickness=0.3, color=colors.HexColor("#aaa")))
    s.append(Spacer(1, 0.1*cm))
    for ln in body_lines:
        s.append(Paragraph(ln, style))
    s.append(Spacer(1, 0.25*cm))
    return s

def blatt_transatlantic_1():
    s = []
    s.append(Paragraph("<b>E-Mail-Korrespondenz München ↔ New York</b>", S_H2))
    s.append(Paragraph("Anlage zur Akte WBF-2026-KK-0014 / Az. 2-03 O 412/26 — "
                        "<i>für die Akte ausgedruckt 22.05.2026, 09:14 MEZ</i>", S_SMALL))
    s.append(HLine())
    s.append(Spacer(1, 0.2*cm))
    s.extend(email_block([
        ("From:", "Dr. Dr. A. Steinacker-von Tarsis &lt;steinacker@steinacker-lichtenberg.de&gt;"),
        ("To:", "J. Halston Whitman III &lt;jhwiii@whitman-brennan.com&gt;"),
        ("Cc:", "P. Forsythe-Vanderhof &lt;pfv@whitman-brennan.com&gt;, M. v. Brenkenhoff "
                "&lt;brenkenhoff@steinacker-lichtenberg.de&gt;"),
        ("Date:", "Tue, 17 Mar 2026 22:48:11 +0100 (CET)"),
        ("Subject:", "URGENT — Coordination US/EU enforcement strategy — klôtzzkètté matter"),
    ], [
        "Dear Halston,",
        "",
        "I write at this rather impractical hour as the Comtesse has just left our office at",
        "Maximiliansplatz, and the situation has escalated. Three matters need transatlantic",
        "alignment by EOB your time tomorrow:",
        "",
        "(1) eV LG Frankfurt (Az. 2-03 O 412/26) erlassen 04.03.2026 gegen Brezelmann +",
        "    Donauzon. Beschluss anbei (PDF, 18 S.). Brezelmann hat Widerspruch eingelegt,",
        "    Termin 11.06.2026, 10:00 Uhr. Donauzon hat sich noch nicht erklärt.",
        "",
        "(2) Donauzon Logistics USA LLC hat — wir vermuten als Folge der eV — den Container",
        "    der UAB klotzkettie über LA/Long Beach umgeleitet. CBP-Detention wäre möglich,",
        "    sobald TMK-26-08812 aktiv ist. Wie weit sind Sie mit der CBP-Recordation?",
        "",
        "(3) Comtesse besteht auf TTAB-Opposition GEGEN Klotzkettie LLC binnen 30 Tagen.",
        "    Ich halte das fristtechnisch für machbar, bin aber für US-Verfahren nicht",
        "    qualifiziert. Können Sie eine Notice of Opposition vorbereiten?",
        "",
        "Bezüglich Punkt (2): Donauzon ist ein delikater Mandant — gemeint: ein delikater",
        "Gegner. Die DSA-Compliance-Argumentation ist auf EU-Ebene ein zweischneidiges",
        "Schwert. Wir sollten US-seitig zunächst auf direkte Lanham-§ 32 / § 43-Ansprüche",
        "abstellen, ohne Vermittlerhaftungs-Anker. — Aber das ist Ihr Gebiet.",
        "",
        "Ich bin morgen früh ab 08:00 MEZ erreichbar.",
        "",
        "Mit den besten Grüßen,",
        "Annabella",
        "",
        "--",
        "Dr. Dr. Annabella Steinacker-von Tarsis, LL.M. (Cantab.)",
        "Steinacker Lichtenberg &amp; Partners IP Boutique",
        "Maximiliansplatz 19 · 80333 München · DE",
        "T +49 89 21 03 96-12 · M +49 172 884 11 39",
        "",
        "CONFIDENTIAL — ATTORNEY-CLIENT PRIVILEGED — DO NOT FORWARD",
    ]))
    s.extend(email_block([
        ("From:", "J. Halston Whitman III &lt;jhwiii@whitman-brennan.com&gt;"),
        ("To:", "Dr. Dr. A. Steinacker-von Tarsis &lt;steinacker@steinacker-lichtenberg.de&gt;"),
        ("Cc:", "P. Forsythe-Vanderhof &lt;pfv@whitman-brennan.com&gt;"),
        ("Date:", "Tue, 17 Mar 2026 19:14:33 -0400 (EDT)"),
        ("Subject:", "Re: URGENT — Coordination US/EU enforcement strategy — klôtzzkètté matter"),
    ], [
        "Annabella —",
        "",
        "Got your message at 5:48 my time, just as I was leaving the office. Quick replies",
        "below; we'll do a proper call tomorrow your morning / my late night.",
        "",
        "&gt; (1) eV LG Frankfurt erlassen 04.03.2026 ...",
        "",
        "Congratulations on the ex parte. Tracks with our SDNY playbook. Send the Beschluss",
        "PDF with English summary — Priscilla will draft a domestication motion just in case",
        "we need to enforce in NY (28 USC § 1738 doesn't apply to foreign judgments, but New",
        "York's Recognition Act, CPLR Art. 53, may).",
        "",
        "&gt; (2) CBP recordation",
        "",
        "Filed March 18 (today my time). Acceptance typically takes 8–10 business days.",
        "Tracking: TMK-26-08812 (anticipated). Once accepted, we can ask LA/LB CEE to",
        "&quot;watch&quot; the Donauzon Logistics importer of record (EIN 84-3771224). Para. Pruitt-",
        "Calhoun is preparing the PIG (Product ID Guide) for CBP officers — silk weave",
        "authentication is non-trivial, but the holographic seal helps.",
        "",
        "&gt; (3) TTAB Opposition",
        "",
        "Done. Notice of Opposition under preparation, filing target April 3. Opp. number",
        "will be assigned upon ESTTA submission. Caveat: Klotzkettie LLC is a Wilmington",
        "shell. Service may be problematic. If it goes default, all the better.",
        "",
        "One question for you: the Comtesse's note (forwarded by Maximilian) mentioned a",
        "&quot;Mes chéris, n'oubliez pas New York!&quot; — is this a formal instruction or a",
        "Comtesse-ism? Asking because the US damages model (treble + statutory + fees)",
        "could approach USD 8.7 million if we take it to verdict. I'd like authority.",
        "",
        "Best,",
        "Halston",
        "",
        "J. Halston Whitman III, Esq.",
        "Whitman Brennan Forsythe LLP — 1290 Ave of the Americas, 41st Fl., NYC 10104",
        "T (212) 555-0188 · Mobile (646) 388-7711",
        "",
        "*** This email may contain attorney-client privileged and/or attorney work-product",
        "*** material. If you are not the intended recipient, delete and notify sender.",
    ]))
    return s

story += blatt_transatlantic_1()
story.append(PageBreak())

def blatt_transatlantic_2():
    s = []
    s.extend(email_block([
        ("From:", "Dr. Dr. A. Steinacker-von Tarsis &lt;steinacker@steinacker-lichtenberg.de&gt;"),
        ("To:", "J. Halston Whitman III &lt;jhwiii@whitman-brennan.com&gt;"),
        ("Date:", "Wed, 18 Mar 2026 08:02:44 +0100 (CET)"),
        ("Subject:", "Re[2]: URGENT — Coordination ..."),
    ], [
        "Halston,",
        "",
        "Re Comtesse: it is a FORMAL instruction. Her handwritten note (Kopie in der Akte,",
        "Bl. 71, anbei) lautet:",
        "",
        "    « Mes chéris, n'oubliez pas New York !",
        "      L'Amérique aussi doit s'agenouiller devant K°°.",
        "      Pas de compromis. Pas de pitié. — B. »",
        "",
        "Translation for the file: „My dears, do not forget New York! America too must",
        "kneel before K°°. No compromise. No mercy. — B.“",
        "",
        "Sie hat heute Morgen um 06:14 MEZ telefonisch bestätigt: full USD 8.7 mio damages",
        "model, treble where available. Retainer aufgestockt um EUR 250.000 (Überweisung",
        "erfolgt heute, valuta 19.03., über Banque Pictet Genève).",
        "",
        "Eine Bitte: bei der Notice of Opposition möglichst NICHT den Begriff „shell entity“",
        "verwenden, falls vermeidbar — Klotzkettie LLC könnte sonst eine pre-emptive",
        "Declaratory-Judgment-Klage in Delaware einreichen, wo unsere Akte schwächer ist.",
        "(Beraten Sie sich gern mit Reginald Brennan IV, der das Delaware Chancery genauer",
        "kennt als ich.)",
        "",
        "Bis später,",
        "A.",
    ]))
    s.extend(email_block([
        ("From:", "J. Halston Whitman III &lt;jhwiii@whitman-brennan.com&gt;"),
        ("To:", "Dr. Dr. A. Steinacker-von Tarsis &lt;steinacker@steinacker-lichtenberg.de&gt;"),
        ("Date:", "Wed, 18 Mar 2026 11:22:08 -0400 (EDT)"),
        ("Subject:", "Re[3]: ... CONFIDENTIAL — INTERNAL STRATEGY"),
    ], [
        "Annabella —",
        "",
        "Understood and noted. The Comtesse's instruction is unambiguous. Priscilla will",
        "redraft using „Delaware-incorporated entity with limited operational footprint“",
        "instead of „shell entity“ — same litigative effect, less DJ-action invitation.",
        "",
        "Pictet wire confirmed in our Trust Account at 11:14 EDT. The Madame's expedience",
        "is, as always, exquisite.",
        "",
        "Re. timezone management: can we set up a recurring Wednesday call at 15:00 your",
        "time / 10:00 mine? We're losing too many cycles to async on the haptic-mark",
        "filings — those need US-side examiner conversations and your TU Darmstadt expert",
        "(Tastenberger) coordinated. The TEAS form for haptic marks (Application Type:",
        "&quot;non-visual mark&quot;) requires a written description that mirrors the German one",
        "exactly, otherwise Madrid Protocol § 66(a) basing fails.",
        "",
        "PS — there is one cultural matter I should raise discreetly. The TTAB practice is",
        "famously sclerotic — these proceedings routinely run 24–36 months. The Comtesse's",
        "instruction „pas de pitié“ is a Continental sentiment that translates poorly when",
        "the Board grants every motion for extension. Manage expectations.",
        "",
        "Halston",
    ]))
    s.extend(email_block([
        ("From:", "M. v. Brenkenhoff &lt;brenkenhoff@steinacker-lichtenberg.de&gt;"),
        ("To:", "P. Forsythe-Vanderhof &lt;pfv@whitman-brennan.com&gt;"),
        ("Cc:", "Dr. Dr. A. Steinacker-von Tarsis, J. H. Whitman III"),
        ("Date:", "Thu, 19 Mar 2026 16:47:51 +0100 (CET)"),
        ("Subject:", "Discovery Disclosures — TTAB Opp. 91/289.412 — Koordination"),
    ], [
        "Sehr geehrte Frau Kollegin Forsythe-Vanderhof,",
        "",
        "in Vorbereitung der TTAB Initial Disclosures (Frist 03.07.2026) möchte ich auf",
        "folgende EU-rechtliche Komplikation hinweisen:",
        "",
        "Soweit Discovery-Requests Unterlagen erfassen, die personenbezogene Daten",
        "EU-ansässiger Personen enthalten (Mandantin Sitz Paris; mehrere Zeuginnen mit",
        "Wohnsitz Frankreich/Italien/Schweiz), greift DS-GVO Art. 48: Auskunftsverlangen",
        "ausländischer Gerichte sind nur dann zulässig, wenn sie auf einer internationalen",
        "Übereinkunft beruhen (Haager Beweisaufnahmeübereinkommen 1970, sofern einschlägig).",
        "",
        "Praktische Konsequenz: Wenn Klotzkettie LLC bzw. dahinterstehende Personen",
        "(Brezelmann/Brezelmanas) per Interrogatory die Identität unserer Detektive,",
        "Testkäufer und/oder Sachverständigen abfragen, müssen wir entweder",
        "",
        "  (a) eine Letters-Rogatory-Prozedur über Den Haag laufen lassen (12–18 Monate), oder",
        "  (b) im protective order eine EU-data-protection-Klausel verankern.",
        "",
        "Bitte stimmen wir das vor der Discovery Conference am 03.06.2026 ab.",
        "",
        "Mit kollegialen Grüßen",
        "Maximilian Freiherr von Brenkenhoff",
        "Rechtsanwalt · Steinacker Lichtenberg",
    ]))
    return s

story += blatt_transatlantic_2()
story.append(PageBreak())

def blatt_transatlantic_3():
    s = []
    s.extend(email_block([
        ("From:", "P. Forsythe-Vanderhof &lt;pfv@whitman-brennan.com&gt;"),
        ("To:", "M. v. Brenkenhoff &lt;brenkenhoff@steinacker-lichtenberg.de&gt;"),
        ("Date:", "Thu, 19 Mar 2026 14:55:32 -0400 (EDT)"),
        ("Subject:", "Re: Discovery Disclosures — TTAB — GDPR question"),
    ], [
        "Maximilian —",
        "",
        "Thanks. I will draft the protective order to include a paragraph 14(b):",
        "",
        "    &quot;14(b) GDPR Carve-out. To the extent any document responsive to discovery",
        "          requests contains personal data of a natural person residing in the",
        "          European Economic Area, the producing party shall be entitled to redact",
        "          such personal data subject to the receiving party's right to challenge",
        "          such redaction. Production of personal data shall be deemed to satisfy",
        "          GDPR Art. 6(1)(f) (legitimate interests) and Art. 49(1)(e) (legal",
        "          claims), without prejudice to any further argument.&quot;",
        "",
        "I will circulate the full PO draft Monday. One question back at you: is your",
        "Mandantin willing to consent to a Sedona Conference-style production from her",
        "side? It might neuter the Lithuanian shell's reciprocal requests if we lead with",
        "voluntary transparency.",
        "",
        "Best,",
        "Priscilla",
    ]))
    s.extend(email_block([
        ("From:", "Dr. Dr. A. Steinacker-von Tarsis &lt;steinacker@steinacker-lichtenberg.de&gt;"),
        ("To:", "J. Halston Whitman III &lt;jhwiii@whitman-brennan.com&gt;"),
        ("Date:", "Sat, 21 Mar 2026 02:14:09 +0100 (CET)"),
        ("Subject:", "URGENT 02:14 — Comtesse called me from Capri at 01:48"),
    ], [
        "Halston,",
        "",
        "She just called me from Capri at 01:48 MEZ (so 20:48 EDT your time, which she",
        "apparently took to be a reasonable hour). The instruction is:",
        "",
        "  (a) Verdoppelung der Haptik-Anmeldungen: zusätzlich zum Schal-Twill und",
        "      Bergkristall-Flakon ANCHE die Innenseide-Textur der Donna-Konfektion",
        "      (Frühjahr/Sommer 2026 — „Soie d'Aube“).",
        "  (b) Erweiterung der TTAB Opposition: zweiter Antrag gegen jegliche US-Anmeldung",
        "      der Hauswaren-Solingen mit „Klotz“-Komponente.",
        "  (c) NB: Comtesse wünscht einen „discreet retainer raise“ wegen Komplikationen.",
        "",
        "Ich werde sie morgen — heute, in einigen Stunden — höflich darauf hinweisen, dass",
        "(b) gegen Heinrich-Klotz Hauswaren GmbH inhaltlich aussichtslos ist (keine",
        "wirtschaftliche Überschneidung). Doch wir benötigen Ihre US-Anwaltsmeinung",
        "schriftlich, um die instructio formell ablehnen zu können.",
        "",
        "Mit verspätetem Gruss aus München,",
        "A.",
    ]))
    s.extend(email_block([
        ("From:", "J. Halston Whitman III &lt;jhwiii@whitman-brennan.com&gt;"),
        ("To:", "Dr. Dr. A. Steinacker-von Tarsis &lt;steinacker@steinacker-lichtenberg.de&gt;"),
        ("Date:", "Sat, 21 Mar 2026 07:42:11 -0400 (EDT)"),
        ("Subject:", "Re: URGENT 02:14 — opinion request"),
    ], [
        "A. —",
        "",
        "Affirmative responses:",
        "",
        "(a) Yes — third haptic application (Soie d'Aube) we can file via TEAS Plus before",
        "    April 30. Adds ~USD 9,400 to budget.",
        "(b) Confirmed: opposing Heinrich-Klotz Hauswaren GmbH's KLOTZ KETTLE COOKWARE",
        "    registration is BAD POLICY. We need that registration as a § 2(d) bar against",
        "    further unauthorized „Klotz“-marks in cookware, but not for ourselves. Formal",
        "    written opinion follows under separate cover (engagement memo 26-OPN-014).",
        "(c) Retainer raise: yes, but on the next quarterly invoice not today.",
        "",
        "One housekeeping item: at 02:14 your time, you should be asleep. The matter will",
        "still be here at 09:00. (Said with affection, between counsel of like temperament.)",
        "",
        "JHW",
    ]))
    s.append(Spacer(1, 0.2*cm))
    s.append(HandNote(
        "Annabella — die Comtesse ruft Halston jetzt direkt an,\n"
        "20:48 NYC. Halston sagt, sie habe vergessen,\n"
        "dass Capri und NY 6 Stunden auseinander sind.\n"
        "Bitte: Anweisung an Sekretariat —\n"
        "Comtesse-Calls ab 22:00 MEZ → an Sprachbox.\n"
        "— M. v. Brenkenhoff, 21.03.",
        font=FONT_HAND2, size=13, angle=0.6, w=15*cm))
    return s

story += blatt_transatlantic_3()
story.append(PageBreak())

print("[part22] done")
