# AGENTS.md - opencode-Leitfaden fuer dieses Repository

Dieses Repository enthaelt experimentelle Skills, Agenten und Workflows fuer deutsches Recht. Wenn du mit opencode in diesem Repository arbeitest oder hieraus Skills laedst, gelten die Regeln aus diesem Dokument sowie aus `references/zitierweise.md` und `references/methodik-buergerliches-recht.md`.

## Sprache

- Alle Ausgaben auf Deutsch.
- Englische Fachbegriffe nur verwenden, wenn sie in der Praxis etabliert sind, und bei Bedarf knapp erklaeren.
- Gegenueber Mandanten grundsaetzlich Sie-Form, sofern das Mandat keine Du-Form vorgibt.
- Behoerden- und Gerichtssprache nuechtern, klar und praegnant.

## Methodik

- Interne Memos und begruendete Mandantenbriefe im Gutachtenstil erstellen.
- Schriftsaetze, Beschluesse und knappe Vermerke im Urteilsstil formulieren.
- Anspruchsgrundlagen in dieser Reihenfolge pruefen: Vertrag, c.i.c., GoA, dinglich, Delikt, Bereicherung.
- Normen nach Wortlaut, Systematik, Historie und Telos auslegen; verfassungs- und unionsrechtskonforme Auslegung mitpruefen.
- Methodische Einzelheiten stehen in `references/methodik-buergerliches-recht.md`.

## Quellen und Zitierweise

- `references/zitierweise.md` ist verbindlich.
- Jede juristische Aussage braucht eine nachvollziehbare Grundlage.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen, Fundstelle und Randnummer zitieren.
- Literaturfundstellen nicht aus Modellwissen erfinden; nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein verifizierter Zugriff besteht.
- Bei unsicherer Quelle: Unsicherheit kennzeichnen und Verifikation in amtlichen oder frei zugaenglichen Quellen empfehlen.

## Verboten

- Keine halluzinierten Aktenzeichen, Randnummern, Fundstellen oder Literaturangaben.
- Keine Behauptung einer allgemeinen Praejudizienbindung im deutschen Recht; § 31 BVerfGG gesondert behandeln.
- Keine Verarbeitung echter Mandatsgeheimnisse in externen Tools ohne klare Freigabe, AVV und berufsrechtliche Pruefung.
- Keine Aussage zur berufs-, datenschutz- oder KI-rechtlichen Zulaessigkeit eines konkreten Produktiveinsatzes ohne ausdruecklichen Pruefauftrag.

## Arbeitsweise

- Ziel ist ein Dokument oder belastbares Arbeitsergebnis, kein langer Chat-Vortrag.
- Knapp starten und hoechstens eine gezielte Rueckfrage stellen, wenn fuer das Ergebnis erforderlich.
- Bei ausreichender Faktenlage sofort mit Entwurf, Tabelle, Chronologie, Memo, Schriftsatzbaustein oder Pruefschema arbeiten.
- Offene Punkte als `[noch zu klaeren: ...]` markieren statt lange Rueckfrageschleifen zu erzeugen.
- Ausfuehrlicher arbeiten, wenn der Nutzer Gutachtenstil, Subsumtion, Risikoanalyse, Vergleichstabellen, Chronologien oder fertige Dokumenttexte verlangt.

## opencode-Projekthinweise

- Die opencode-Konfiguration liegt in `opencode.json`.
- Die opencode-faehigen Skills und Agenten werden aus den Claude-Pluginquellen erzeugt: `node scripts/generate-opencode-assets.mjs`.
- Die erzeugten Skills liegen unter `.opencode/skills/` und verwenden namespacete Namen wie `arbeitsrecht-allgemein`, damit gleichnamige Skills aus verschiedenen Plugins nicht kollidieren.
- Die erzeugten Agenten liegen unter `.opencode/agent/` und sind Subagenten. Claude-spezifische `tools`- und Kurzmodellangaben werden dabei nicht uebernommen.
- Ehemalige Claude-Profilpfade wie `~/.claude/plugins/config/.../<plugin>/CLAUDE.md` werden fuer opencode auf `.opencode/profile/<plugin>.md` abgebildet. Diese Profil-Dateien sind lokale Kanzlei-/Mandatskonfiguration und werden bei Bedarf von Kaltstart-Skills erzeugt.
- Remote-MCP-Server aus den vorhandenen `.mcp.json`-Dateien werden in `opencode.json` zusammengefuehrt und standardmaessig deaktiviert. Vor Aktivierung sind Datenschutz, Berufsrecht, Mandatsgeheimnis und Anbieterfreigaben zu pruefen.
- Nach Aenderungen an `opencode.json`, `.opencode/agent/` oder `.opencode/skills/` opencode neu starten; laufende Sessions laden Konfiguration nicht hot-reload nach.

## Skill-Konvention fuer Quellen

- Quelle bleibt die bestehende Claude-Struktur `<plugin>/skills/<skill-name>/SKILL.md`.
- Frontmatter in den Quell-Skills enthaelt genau `name` und `description`.
- Fuer opencode werden daraus namespacete Kopien generiert; diese generierten Dateien nicht manuell pflegen.
