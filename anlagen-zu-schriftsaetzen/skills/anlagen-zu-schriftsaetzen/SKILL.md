---
name: anlagen-zu-schriftsaetzen
description: "Zuordnung von Anlagen zu gerichtlichen Schriftsaetzen. Liest den Schriftsatz (Klage/Klageerwiderung/Replik), erkennt vorhandene Beweisstuecke, sortiert nach Schriftsatz-Logik, konvertiert alles nach PDF, benennt nach beA-Konvention und stempelt oben rechts Anlage K1/B1/A1 in Arial 12. Verwenden, wenn der Nutzer sagt 'Anlagen zuordnen', 'Anlagen sortieren', 'Anlagenkonvolut erstellen', 'Anlagen stempeln', 'Anlagen K1 K2 vergeben' oder 'Anlagen pruefen'."
---

# Zuordnung von Anlagen zu gerichtlichen Schriftsätzen

## Zweck

Dieser Skill nimmt einen vorliegenden Schriftsatz-Entwurf (Klage, Klageerwiderung, Replik, Duplik, Berufung, Beschwerde) und eine Sammlung kuratierter Anlagen in unterschiedlichen Dateiformaten (PDF, DOCX, XLSX, JPG, PNG, EML, MSG) und macht daraus ein beA-fertiges Anlagenkonvolut:

1. **Reihenfolge** nach der Logik des Schriftsatzes herstellen (chronologisch, nach Zitierreihenfolge, oder gemischt nach Mandantenseite).
2. **PDF-Konvertierung** aller Anlagen, damit alles im selben Format hochgeladen werden kann.
3. **Anlagen-Bezeichnung** nach Parteirolle (K = Kläger, B = Beklagter, A = Antragsteller / Antragsgegner mit Suffix) automatisch vergeben oder aus dem Schriftsatz übernehmen.
4. **Stempel oben rechts** auf jeder PDF-Anlage in **Arial 12 pt**, dezent, z. B. „Anlage K 7".
5. **Datei-Benennung** nach beA-tauglicher Konvention: keine Sonderzeichen, keine Umlaute, kurz, sortierbar.
6. **Anlagenkonvolut** als ein einzelnes Begleit-PDF (Deckblatt + alle Anlagen in Reihenfolge mit Lesezeichen), optional zusätzlich der Schriftsatz vorab gebunden.
7. **Schriftsatz aktualisieren**, wenn die Anlagen im Entwurf noch nicht referenziert sind: der Skill schlägt Einfügestellen vor und nennt die Anlagenbezeichnung samt Fundstelle (Seite/Randnummer im Anlagen-PDF).
8. **Prüfmodus**, wenn der Nutzer schon zugeordnet hat: der Skill validiert vorhandene Zuordnungen, deckt Lücken, doppelte Nummern und nicht-zitierte Anlagen auf.

## Eingaben

- **Schriftsatz-Entwurf** (PDF oder DOCX) — Pflicht.
- **Anlagen-Sammlung** als Ordner oder Liste von Dateien. Formate werden automatisch erkannt.
- **Parteirolle** des Mandanten in genau diesem Schriftsatz:
  - **Kläger / Berufungskläger / Revisionskläger / Antragsteller (Hauptverfahren)** → Präfix **K**
  - **Beklagter / Berufungsbeklagter / Revisionsbeklagter / Antragsgegner (Hauptverfahren)** → Präfix **B**
  - **Antragsteller im einstweiligen Rechtsschutz / selbständigen Beweisverfahren / FamFG-Verfahren** → Präfix **AST** oder kurz **A**
  - **Antragsgegner** → Präfix **AG**
  - **Streithelfer / Nebenintervenient** → Präfix **NI** (oder wie vom Gericht vorgegeben)
  - Eigene Präfixe sind erlaubt; der Nutzer kann z. B. „A" bei reinen Antragsverfahren wählen.
- **Modus** (siehe unten): Auto-Benennung, Schriftsatz folgt, oder Prüfmodus.

## Drei Modi

### Modus 1 — „Auto-Benennung" (Schriftsatz referenziert die Anlagen noch nicht)

Der Schriftsatz erwähnt zwar Beweise und Dokumente, hat aber noch keine festen Anlagen-Nummern. Der Skill:

1. liest den Schriftsatz und identifiziert alle textlichen Anker, die typischerweise eine Anlage tragen: „Vertrag vom 15.03.2024", „Mahnschreiben vom …", „E-Mail des Geschäftsführers vom …", „Sachverständigengutachten Müller", „Kontoauszug der Sparkasse Köln", „Lichtbild Nr. 3" usw.
2. ordnet jeder gefundenen Anlage genau eine Datei aus der Anlagen-Sammlung zu, soweit möglich (über Dateiname, Datum im Dokument, OCR-Text bei Bilddateien).
3. vergibt die Nummerierung **in der Reihenfolge der ersten Erwähnung im Schriftsatz** (so wie es der BGH-Stil empfiehlt, nicht chronologisch nach Datum). Bei Kläger: K 1, K 2, K 3 …
4. erzeugt einen **Vorschlag im Schriftsatz**: an jeder Anker-Stelle wird in Klammern die passende Anlagenbezeichnung samt Fundstelle eingefügt, z. B. *„…wie sich aus dem Vertrag vom 15.03.2024 (**Anlage K 3**, dort S. 2 § 4) ergibt …"*.
5. listet am Schluss alle nicht zugeordneten Anlagen und alle nicht zuordenbaren Anker auf, damit der Nutzer manuell nachsteuern kann.

### Modus 2 — „Schriftsatz folgt" (Anlagen sind im Schriftsatz schon mit K1/B1/… benannt)

Der Schriftsatz nennt bereits „Anlage K 1", „Anlage K 2" usw. Der Skill:

1. extrahiert sämtliche Anlagen-Bezeichnungen aus dem Schriftsatz.
2. ordnet jeder Bezeichnung genau eine Datei aus der Sammlung zu (durch Beschreibung im Klartext: „Vertrag vom 15.03.2024 (Anlage K 1)" → Datei mit passendem Inhalt). Bei Mehrdeutigkeiten fragt der Skill nach.
3. übernimmt **die im Schriftsatz vergebene Nummerierung exakt** — keine Umnummerierung gegen den Schriftsatz.
4. meldet, wenn der Schriftsatz eine Anlagenbezeichnung enthält, zu der keine Datei vorliegt (Lücke), oder wenn Dateien vorliegen, die im Schriftsatz nicht zitiert werden (Überschuss).

### Modus 3 — „Prüfmodus" (alles ist schon zugeordnet, nur kontrollieren)

Der Nutzer hat selbst zugeordnet, gestempelt und benannt und will nur eine zweite Sichtkontrolle. Der Skill:

1. liest die Anlagen-Dateinamen, die Stempel oben rechts und den Schriftsatz.
2. prüft auf folgende Fehlerklassen und meldet jede mit Fundstelle:
   - **Numerierungslücken** (K 1, K 2, K 4 — K 3 fehlt).
   - **Doppelt vergebene Nummern** (zwei Dateien mit Anlage K 5).
   - **Zitierte aber nicht vorhandene Anlagen** (Schriftsatz nennt K 9, Datei fehlt).
   - **Vorhandene aber nicht zitierte Anlagen** (Datei K 11 da, aber im Schriftsatz nicht erwähnt).
   - **Stempel-Fehlanpassungen** (Stempel sagt „K 3", Dateiname sagt „K 4").
   - **Reihenfolge-Inkonsistenz** zwischen erster Erwähnung im Schriftsatz und Anlagen-Nummer.
   - **Format-Fehler**: nicht-PDF-Anlagen, Umlaute / Sonderzeichen im Dateinamen, Leerzeichen, Dateinamen länger als 90 Zeichen (beA-Empfehlung).
3. gibt einen Korrektur-Plan aus. **Korrigiert nichts automatisch**, sondern listet auf, was zu tun ist — der Nutzer entscheidet, ob er das selber macht oder den Skill in Modus 1 / 2 erneut laufen lässt.

## Stempel-Spezifikation („oben rechts")

Auf der **ersten Seite** jeder Anlage wird ein dezenter Stempel gesetzt:

- **Position**: rechter oberer Rand, ca. 1,5 cm vom oberen Seitenrand, ca. 1,5 cm vom rechten Seitenrand.
- **Schrift**: Arial 12 pt regular (kein fett, kein kursiv).
- **Format**: `Anlage K 7` (mit Leerzeichen zwischen Präfix und Zahl — verbreitet im BGH-/Beck-Stil; je nach Kanzlei auch ohne Leerzeichen `Anlage K7` zulässig, der Skill fragt einmal).
- **Mehrseitige Anlagen**: Stempel nur Seite 1 (Standard) — auf Wunsch auch auf jeder Seite (Option `--stempel jede-seite`).
- **Konvolute** (mehrere Dokumente unter einer Anlage, z. B. „Anlage K 5 — Schriftverkehr 03/2024 bis 07/2024"): ein Deckblatt mit Anlagenbezeichnung und Inhaltsverzeichnis, dann die Einzeldokumente; Stempel auf dem Deckblatt **und** jeweils auf Seite 1 jedes Einzeldokuments mit Suffix („Anlage K 5/1", „K 5/2" …).

## Datei-Benennung (beA-tauglich)

Konvention für die einzelnen Anlagen-Dateien im Ausgabe-Ordner:

```
Anlage_K-03_Vertrag-vom-2024-03-15.pdf
Anlage_K-07a_Mahnschreiben-erste-Stufe.pdf
Anlage_B-01_Aufrechnungserklaerung.pdf
```

Regeln:

- **Keine Umlaute, kein scharfes ß**: ae, oe, ue, ss.
- **Keine Leerzeichen** — Bindestrich oder Unterstrich.
- **Zahlen zweistellig** (`K-03`, nicht `K-3`) für sauberes Sortieren bis 99.
- **Maximal ca. 90 Zeichen** insgesamt (beA-Praxis).
- **Datum**, wenn enthalten, im Format **JJJJ-MM-TT** für sortierbare Reihenfolge.
- **Untervarianten** mit Buchstaben (`K-07a`, `K-07b`), wenn eine Anlage in mehrere Einzeldokumente zerfällt.

## Format-Konvertierung

Eingangsformate, die der Skill akzeptiert und nach PDF konvertiert:

| Eingang | Verfahren |
|---|---|
| **DOCX** | über LibreOffice headless / Microsoft-Word-Konvertierung; Schriften einbetten |
| **XLSX** | Druckbereich der relevanten Tabelle festlegen, Querformat wenn breit; Seitenumbruch-Vorschau prüfen; PDF mit eingebetteten Schriften |
| **JPG/PNG** | als ein-/mehrseitiges PDF einbetten, dabei DIN A4 vorlegen, Seitenränder ca. 2 cm |
| **EML/MSG** | E-Mail-Header (Von/An/Datum/Betreff) + Body als sauber formatiertes PDF; Anhänge werden als eigene Unter-Anlagen behandelt (z. B. `K-08a` E-Mail, `K-08b` Anhang) |
| **PDF** | unverändert übernommen; gegebenenfalls neu komprimiert; Lesezeichen werden bei Konvolut-Bildung gesetzt |

## Ausgabe

Im Arbeitsordner des Mandats entsteht:

```
anlagen/
  Anlage_K-01_<Kurzbeschreibung>.pdf
  Anlage_K-02_<Kurzbeschreibung>.pdf
  …
  Anlagenkonvolut.pdf            ← alle Anlagen in Reihenfolge mit Lesezeichen, Deckblatt, Inhaltsverzeichnis
  Anlagenverzeichnis.pdf         ← kurze tabellarische Übersicht (Anlage / Kurzbeschreibung / Datum / Seitenanzahl)
  Anlagenverzeichnis.md          ← gleiche Übersicht als Markdown für Aufnahme in den Schriftsatz
```

Optional, wenn der Nutzer das wünscht: **`Schriftsatz_mit_Anlagen.pdf`** — der Schriftsatz vorab gebunden, danach das Anlagenkonvolut, mit durchlaufenden Lesezeichen.

## Schriftsatz-Update

Wenn in Modus 1 die Anlagen erst durch den Skill benannt werden, erzeugt er zwei Dateien neben dem Original:

- `Schriftsatz_mit_Anlagenmarkierungen.docx` — sichtbare Änderungen markiert; der Anwalt entscheidet, was übernommen wird.
- `Schriftsatz_Anlagenliste.md` — die vorgeschlagene Anlagenliste als eigener Block zum Einfügen am Ende des Schriftsatzes.

## Was der Skill NICHT tut

- **Keine inhaltliche Schwärzung** (DSGVO-Schwärzung von Drittpersonen, Bankdaten, ärztlichen Diagnosen etc.) — dafür gibt es einen eigenen Workflow / einen eigenen Skill in `datenschutzrecht`.
- **Keine Echtheits- oder Authentizitätsprüfung** der Anlagen.
- **Keine OCR-Vollerkennung** mit dem Ziel, den Anlageninhalt zu zitieren — nur so viel OCR, wie für die Zuordnung nötig ist (Datum, Absender, kurze Stichworte).
- **Keine elektronische Signatur** und **kein direktes beA-Hochladen**. Das macht der Anwalt selbst.
- **Keine Anpassung am Schriftsatz-Layout** außer dem Einfügen der Anlagen-Bezeichnungen.

## Hinweis zur Berufspflicht

Auch wenn der Skill technisch zuverlässig stempelt und sortiert: die **Letztverantwortung** für Vollständigkeit, richtige Zitierreihenfolge und Berufspflichten (insbesondere § 43e BRAO, § 203 StGB, DSGVO) liegt beim Anwalt. Vor dem beA-Versand ist der Inhalt jeder Anlage zu prüfen — Schwärzungen, Drittinteressen, Mandatsgeheimnis.

## Beispiele typischer Nutzerformulierungen, die diesen Skill auslösen

- „Ich habe hier den Klage-Entwurf und 20 Dokumente — bitte als Anlagen K 1 ff. zuordnen und stempeln."
- „Sortier die Anlagen für die Klageerwiderung als B 1 bis B 14, alles als PDF, beA-tauglich."
- „Anlagenkonvolut für die Replik bauen, der Schriftsatz nennt schon K 23 bis K 31."
- „Ich habe das selbst zugeordnet — bitte einmal Prüfmodus drüber."
- „Mach ein einziges PDF, Schriftsatz vorne, dann Anlagen, mit Lesezeichen."

## Werkzeug: `werkzeuge/build_anlagenkonvolut.py`

Im Skill-Ordner liegt ein Python-Werkzeug, das aus einem Eingangsordner mit beA-konform benannten Einzel-PDFs (`Anlage_K-01_…pdf`, `Anlage_K-02_…pdf`, …) automatisch:

- den Stempel **Anlage K 7** in Arial 12 pt oben rechts setzt (Seite 1 jeder Anlage),
- alle Anlagen zu einem Konvolut-PDF mit Lesezeichen verkettet,
- ein **Anlagenverzeichnis** als Markdown und als PDF erzeugt.

Aufruf: `python3 werkzeuge/build_anlagenkonvolut.py --eingang ./anlagen --ausgang ./konvolut --praefix K --schriftsatz "Klage Edelholz GmbH"`. Abhängigkeiten: `pypdf`, `reportlab`. Schwärzungen und Echtheitsprüfungen bleiben Sache des Anwalts.
