# mandantenanfragen-assistent

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`mandantenanfragen-assistent`) | [`mandantenanfragen-assistent.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/mandantenanfragen-assistent.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Mandantenanfragen Q2/2026 — Kanzlei Roosendaal & Tannenfels, Köln** (`mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026`) | [Gesamt-PDF lesen](../testakten/mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026/gesamt-pdf/mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026_gesamt.pdf) | [`testakte-mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Mandantenanfragen Q2/2026 — Kanzlei Roosendaal & Tannenfels, Köln** (`mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026`) | [Gesamt-PDF lesen](../testakten/mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026/gesamt-pdf/mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

**Version:** 3.2.1  
**Author:** Klotzkette  
**Lizenz:** Apache-2.0 OR MIT

---

Assistent für Anwaltskanzleien zur automatisierten Erstantwort auf eingehende Mandantenanfragen per E-Mail. Das Plugin dankt formell für die Anfrage, übernimmt die exakte Anrede aus der eingehenden Mail, weist auf die telefonische Terminvergabe hin und bittet um eine Sachverhaltszusammenfassung per E-Mail. Für Personen, die nicht schreiben können oder möchten, bietet es einen automatisierten Transkriptionsservice an — mit DSGVO-konformem Einwilligungshinweis.

---

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| Mandantenanfragen-Assistent (`mandantenanfragen-assistent`) | [mandantenanfragen-assistent.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/mandantenanfragen-assistent.zip) |

## Installation

1. ZIP aus dem Release herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `mandantenanfragen-assistent.zip` hochladen.
5. Mit einem konkreten Auftrag starten, zum Beispiel: `Beantworte diese Mandantenanfrage: [E-Mail einfügen]`

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

---

## Skills-Übersicht (15 Skills)

| # | Skill-Name | Beschreibung | Lade-Trigger (Beispiele) |
|---|---|---|---|
| 1 | `anfrage-eingang-parser` | Extrahiert aus der Eingangsmail: Anrede, Name, E-Mail, Kontaktdaten, Sachverhaltsfetzen, Dringlichkeitssignale | "Anfrage auswerten", "E-Mail analysieren", "Kontaktdaten extrahieren" |
| 2 | `anrede-uebernehmen` | Übernimmt die EXAKTE Anrede aus der Eingangsmail; Heuristiken für Titel, Doppelnamen, Adelsprädikat, kirchliche Titel, Ehepaar | "Anrede übernehmen", "formelle Anrede", "Titel erkennen" |
| 3 | `erstantwort-generator` | Hauptskill: erstellt die vollständige formelle Erstantwort-Mail mit allen Bausteinen | "Erstantwort schreiben", "Antwortmail erstellen", "Eingangsbestätigung" |
| 4 | `telefon-konfiguration` | Verwaltet Kanzlei-Kontaktdaten (Sekretariat + Transkriptionsservice) aus `kanzlei.json` und setzt sie in Templates ein | "Telefonnummer konfigurieren", "kanzlei.json bearbeiten" |
| 5 | `transkriptionsdienst-erklaerung` | Formuliert den Hinweis auf den automatisierten Transkriptionsservice: Ablauf, Datenschutz, Einwilligungserfordernis | "Transkriptionsservice erklären", "kann nicht schreiben" |
| 6 | `einwilligung-hinweis-datenschutz` | DSGVO-konforme Einwilligungsklausel für die Sprachaufnahme (Art. 6 Abs. 1 lit. a DSGVO, Art. 13 DSGVO) | "DSGVO Einwilligung formulieren", "Datenschutz Transkription" |
| 7 | `mandatsverhaeltnis-hinweis` | Formuliert den Disclaimer: kein Mandatsverhältnis, keine Rechtsberatung, keine Pflichten der Kanzlei | "kein Mandat Hinweis", "Disclaimer Erstanfrage" |
| 8 | `vertraulichkeit-erinnerung` | Hinweis auf anwaltliche Schweigepflicht § 43a Abs. 2 BRAO — gilt erst ab Mandatsbegründung | "Schweigepflicht Anwalt", "wann gilt Verschwiegenheit" |
| 9 | `folgekorrespondenz-vorbereiten` | Erstellt Skeleton-Eintrag für CRM/Akte: Name, Mail, Telefon, Anliegen, Dringlichkeit, Konfliktcheck-Status | "CRM Eintrag erstellen", "Akte anlegen" |
| 10 | `spam-und-massen-anfrage-filter` | Erkennt Spam-Muster: 419-Scams, Massen-Anfragen, Phishing, Recruiter-Mails; kennzeichnet zur Aussortierung | "Spam prüfen", "verdächtige Anfrage", "Scam-Mail" |
| 11 | `dringlichkeitsmarker` | Erkennt Fristen und Eile-Signale; setzt Stufe HOCH/MITTEL/NIEDRIG; bei HOCH: Sofortanruf des Anwalts erforderlich | "Dringlichkeit prüfen", "Frist erkannt", "Eilbedarf" |
| 12 | `konfliktcheck-vorab` | Hinweis auf Konfliktcheck-Pflicht (§ 43a Abs. 4 BRAO, § 3 BORA); instruiert Sekretariat, Gegenseite vor Terminvergabe zu erfragen | "Konfliktcheck", "Interessenkonflikt prüfen" |
| 13 | `mehrsprachige-antwort` | Erkennt Sprache der Anfrage (DE/EN/FR/IT) und schaltet Erstantwort in die entsprechende Sprache um | "Antwort auf Englisch", "mehrsprachige Erstantwort" |
| 14 | `muster-erstantwort` | Vorlage-Skill mit drei vollständigen Musterschreiben (Standard, nur Vorname, Transkriptionsservice-Modus) für Copy-paste | "Musterschreiben zeigen", "Vorlage Erstantwort" |

---

## Beispiel-Prompt

```
Ich habe soeben diese E-Mail erhalten. Bitte erstelle eine formelle Erstantwort:

Von: Dr. Klaus-Dieter Müller-Strauss <kdms@example.de>
Betreff: Frage zur fristlosen Kündigung meines Angestellten

Sehr geehrte Damen und Herren,

mein Name ist Dr. Klaus-Dieter Müller-Strauss, ich führe ein kleines
Unternehmen im Bereich Maschinenbau. Ich möchte einem meiner Mitarbeiter
fristlos kündigen wegen grober Pflichtverletzung. Was muss ich beachten?

Mit freundlichen Grüßen
Dr. Klaus-Dieter Müller-Strauss
```

Das Plugin extrahiert automatisch die Anrede, prüft auf Dringlichkeit und Spam und erstellt die vollständige Erstantwort — einschließlich aller berufsrechtlichen Hinweise.

---

## Konfiguration (kanzlei.json)

Legen Sie im Plugin-Verzeichnis eine Datei `kanzlei.json` an:

```json
{
  "kanzlei": {
    "name": "[KANZLEI-NAME]",
    "adresse": {
      "strasse": "[STRASSE UND HAUSNUMMER]",
      "plz": "[POSTLEITZAHL]",
      "ort": "[ORT]"
    },
    "telefon_sekretariat": "[SEKRETARIATS-TELEFON]",
    "telefon_transkription": "[TRANSKRIPTIONS-TELEFON]",
    "erreichbarkeit": "[Z.B. Mo-Fr 09:00-17:00 Uhr]",
    "email_kanzlei": "[KANZLEI-E-MAIL]",
    "unterzeichnende_ra": "[VORNAME NACHNAME, Rechtsanwalt/Rechtsanwaeltin]"
  }
}
```

---

## Musterschreiben

Vollständig ausformulierte Musterschreiben für drei Szenarien (mit Anrede, ohne klare Anrede, Transkriptionsservice-Variante) finden Sie in:

[references/musteranschreiben.md](references/musteranschreiben.md)

---

## Rechtliche Hinweise

Dieses Plugin ist ein Hilfswerkzeug für Anwaltskanzleien. Es ersetzt nicht die Prüfung durch einen zugelassenen Rechtsanwalt. Alle generierten Texte sind Vorschläge — die abschließende Prüfung und Freigabe jeder Erstantwort liegt beim Sekretariat und der verantwortlichen Rechtsanwältin bzw. dem verantwortlichen Rechtsanwalt.

Das Plugin enthält keine Rechtsberatung. Alle Musterschreiben sind unverbindliche Formulierungshilfen.

Berufsrechtliche Grundlagen: §§ 43 ff. BRAO, §§ 1 ff. BORA, RVG, DSGVO.

---

## Lizenz

Apache-2.0 OR MIT — siehe [LICENSE](../LICENSE), [LICENSE-APACHE](../LICENSE-APACHE), [LICENSE-MIT](../LICENSE-MIT)


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 20 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Mandantenanfragen Assistent-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arb... |
| `anfrage-eingang-parser` | Sekretariat oder Anwalt erhielt E-Mail-Anfrage eines potentiellen Mandanten und will sie schnell strukturiert auswerten. E-Mail-Parser Kanzlei. Prüfraster: Anrede Name Absender E-Mail-Adresse Telefon Sachverhaltsfetzen Stichwörter dringl... |
| `anrede-uebernehmen` | Antwort-E-Mail soll mit exakt richtiger Anrede des potentiellen Mandanten beginnen ohne Fehler bei Titeln oder Doppelnamen. Anredekonventionen Kanzlei. Prüfraster: Titel (Dr. Prof. Mag.) Doppelnamen Adelspraeifikate kirchliche Titel Komp... |
| `dringlichkeitsmarker` | Eingehende Mandantenanfrage enthaelt möglicherweise Fristenproblem oder dringenden Handlungsbedarf. Dringlichkeitscheck Kanzlei-Intake. Prüfraster: Signale Hauptverhandlung naechste Woche Kündigungsfrist Zwangsvollstreckung Insolvenzantr... |
| `einwilligung-hinweis-datenschutz` | Kanzlei bietet telefonischen Transkriptionsservice an und muss DSGVO-konforme Einwilligung einholen. Art. 6 Abs. 1 lit. a DSGVO Art. 13 DSGVO Informationspflicht. Prüfraster: Rechtsgrundlage Einwilligung Informationspflicht Hinweis kein... |
| `erstantwort-generator` | Sekretariat oder Anwalt muss professionelle Erstantwort-E-Mail an potentiellen Mandanten senden. Hauptskill Erstantwort-E-Mail. Prüfraster: Dank für Anfrage exakte Anrede Terminvergabe-Hinweis Transkriptionsservice mit DSGVO-Einwilligung... |
| `folgekorrespondenz-vorbereiten` | Nach Eingang einer Anfrage muss Sekretariat CRM-Eintrag und Akte anlegen. CRM-Eintrag Kanzlei-Intake. Prüfraster: Name Mail Telefon Anliegen-Stichwort Dringlichkeit Datum Sprachkennung Konfliktcheck-Status. Output: Skeleton-Eintrag für C... |
| `konfliktcheck-vorab` | Sekretariat soll vor Terminvergabe Interessenkonflikt prüfen. § 43a Abs. 4 BRAO § 3 BORA Interessenkonflikt-Check. Prüfraster: Gegenseite und Beteiligte erfragen Datenbankabgleich bestehende Mandate. Output: Konfliktcheck-Anweisung und A... |
| `ma-aufnahmegespraech-leitfaden` | Aufnahmegespraechsleitfaden Mandant: Sachverhalt, Eilbedarf, Ziel, Bereits eingeleitete Schritte, Andere beauftragte Anwaelte, Konflikte, Vergueng. Strukturierte Fragen und typische Stolpersteine. Mustertext zur Mandatsbestaetigung. |
| `ma-einfuehrung-erstkontakt-typen` | Erstkontakt-Typen einfuehrend: Telefon, E-Mail, Webformular, Walk-in, Empfehlung. Pro Typ: Risiken, Dokumentation, Datenschutz, Naechster Schritt. Routing-Logik und Eskalation bei sensiblen Faellen. |
| `ma-erstvermerk-mandantenakte` | Erstvermerk fuer die Mandantenakte: Pflichtangaben (Mandant, Sachverhalt, Eilbedarf, Ziel, Honorar, naechster Schritt), interne Hinweise (Konflikte, sensible Punkte). Format und Aufbewahrung in der Akte. |
| `ma-konfliktcheck-konzern` | Spezialfall Konfliktcheck im Konzern: Mandat fuer Tochter eines bestehenden Mandanten, gegenlaeufige Interessen, Chinese Walls, Information Barriers. Pruefraster und Mustertexte fuer Einwilligungen und Hinweis an Mandant. |
| `ma-mandant-mit-betreuung` | Spezialfall Mandant mit gesetzlicher Betreuung oder Vorsorgevollmacht: Pruefen der Vertretungsmacht, Einwilligungsfaehigkeit, Schweigepflicht gegenueber Betreuer, Beauftragung nur fuer den Aufgabenkreis. Mustertexte und Pruefraster. Rout... |
| `mandatsverhaeltnis-hinweis` | Antwortmail muss klar machen dass noch kein Mandatsverhältnis besteht und keine Rechtsberatung erfolgt. § 43 BRAO Haftungsabgrenzung Erstanfrage. Prüfraster: Beantwortung der Anfrage = keine Rechtsberatung kein Mandatsverhältnis kein Pfl... |
| `mehrsprachige-antwort` | Mandantenanfrage kam auf Englisch Franzoesisch oder Italienisch und Antwort soll in derselben Sprache erfolgen. Mehrsprachige Erstantwort Kanzlei. Prüfraster: Sprache erkennen Anredekonventionen Schlussformeln Datenschutzhinweise in Ziel... |
| `muster-erstantwort` | Kanzlei benoetigt fertige ausfuellbare Vorlage für die Erstantwort auf Mandantenanfragen. Template Erstantwort. Prüfraster: Platzhalter KANZLEI-NAME SEKRETARIATS-TELEFON TRANSKRIPTIONS-TELEFON UNTERZEICHNENDE-RA. Drei Varianten Standard... |
| `spam-und-massen-anfrage-filter` | Sekretariat hat Anfrage erhalten die verdaechtig ausschaut. Spam-Erkennung Kanzlei-Eingang. Prüfraster: Spam Werbung 419-Scams automatisierte Recruiter-Mails Massen-Mandantenanfragen Phishing. Output: Spam-Einschaetzung mit Empfehlung Au... |
| `telefon-konfiguration` | Kanzlei muss Telefonnummern für Sekretariat und Transkriptionsservice in den Antwort-Templates hinterlegen. Konfigurationsverwaltung Kanzlei-Nummern. Prüfraster: kanzlei.json Sekretariatsnummer Transkriptionsnummer Lesen und Setzen der P... |
| `transkriptionsdienst-erklaerung` | Mandant kann seinen Fall nicht schriftlich schildern und soll stattdessen anrufen. Transkriptionsservice Erklärung in Erstantwort. Prüfraster: Telefonnummer Ablauf des Anrufs Verarbeitungshinweis DSGVO-Einwilligung Kein-Mandat-Hinweis. O... |
| `vertraulichkeit-erinnerung` | Sekretariat muss wissen ab wann die Anwaltsschwiegepflicht gilt. § 43a Abs. 2 BRAO Schweigepflicht. Prüfraster: Schweigepflicht gilt erst nach Mandatsbeginn vorher allgemeine Diskretion. Übergangs-Instruktion Sekretariat. Output: Instruk... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
