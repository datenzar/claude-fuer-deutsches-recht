# Mietrecht

Mietrecht fuer Mieter und Vermieter mit ausschliesslich amtlichen Mietspiegel-Quellen pro Bundesland und fuer Top- und Universitaetsstaedte. Acht Skills Datenerhebung Mieterhoehungs-Widerspruch Mietsenkungsverlangen Nebenkostenpruefung Mieteranfragen Klageentwurf Amtsgericht.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Mietrecht (`mietrecht`, dieses Plugin) | [mietrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/mietrecht.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus „Code → Download ZIP“ verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `eigenbedarfskuendigung-erstellen` | Vermietersicht — entwerfe eine ordentliche Kuendigung wegen Eigenbedarfs nach § 573 Abs. 2 Nr. 2 BGB. Pruefroutine deckt berechtigtes Interesse (Eigennutzung Familienangehoerige Haushaltsangehoerige) konkrete Begruend… |
| `klageentwurf-amtsgericht` | Beide Rollen — entwirf eine Klageschrift zum Amtsgericht in einer Mietsache. Sachliche Zustaendigkeit fuer Wohnraummietsachen nach § 23 Nr. 2a GVG ohne Ruecksicht auf den Streitwert; bei Geschaeftsraummiete allgemeine… |
| `lage-und-ausstattung-erheben` | Strukturierte Datenerhebung fuer die Einordnung in den Mietspiegel — Adresse Baujahr Wohnflaeche Bad Kueche Heizung Wohnungsausstattung Gebaeudeausstattung. Erfasst alle Merkmale die in qualifizierten Mietspiegeln als… |
| `mahnung-zahlungsverzug-mieter` | Vermietersicht — verfasse Mahnung und ggf. fristlose Kuendigung bei Zahlungsverzug des Mieters. Pruefroutine deckt Verzug nach § 286 BGB Faelligkeit der Miete (§ 556b Abs. 1 BGB) Mahnschreiben Aufrechnungsverbot frist… |
| `mieteranfragen-beantworten` | Vermieter- und Hausverwaltungssicht — beantworte Mieteranfragen sachlich und ehrlich. Deckt typische Themen ab (Mietminderung Mangelanzeige Modernisierungsankuendigung Schoenheitsreparaturen Hausordnung Kaution Eigenb… |
| `mieterhoehung-pruefen-widersprechen` | Mietersicht — pruefe ein Mieterhoehungsverlangen nach ortsueblicher Vergleichsmiete (§§ 558 ff. BGB) auf Form Frist Kappungsgrenze Begruendung und entwirf bei Bedarf eine Zustimmungsverweigerung oder Teilzustimmung. P… |
| `mieterhoehungsverlangen-erstellen` | Vermietersicht — verfasse ein Mieterhoehungsverlangen auf ortsuebliche Vergleichsmiete (§ 558a BGB) in Textform mit ordnungsgemaesser Begruendung (Mietspiegel Sachverstaendigengutachten oder drei Vergleichswohnungen).… |
| `mietsenkungsverlangen` | Mietersicht — pruefe eine laufende oder bei Vertragsschluss vereinbarte Miete auf Verstoss gegen die Mietpreisbremse (§§ 556d ff. BGB) gegen § 5 WiStG (Mietpreisueberhoehung) und gegen § 291 StGB (Wucher). Erzeugt ein… |
| `mietspiegel-quellen` | Verweist auf die mitgelieferte Referenz references/mietspiegel-quellen.md mit ausschliesslich amtlichen Mietspiegel-Quellen (Bundeslaender Top-Staedte Universitaetsstaedte). Nutze diese Referenz immer wenn die ortsueb… |
| `nebenkostenabrechnung-erstellen` | Vermieter- und Hausverwaltungssicht — Workflow fuer rechtssichere Betriebskostenabrechnungen nach § 556 BGB und BetrKV. Deckt Abrechnungszeitraum Zugangsfrist (zwoelf Monate) Umlagefaehigkeit Verteilerschluessel Heizk… |
| `nebenkostenabrechnung-pruefen` | Mietersicht — pruefe eine Betriebskostenabrechnung auf Form (§ 556 Abs. 3 BGB) Frist (Zugang innerhalb von zwoelf Monaten nach Abrechnungszeitraum) Umlagefaehigkeit nach BetrKV Verteilerschluessel rechnerische Richtig… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Alle Aussagen beruhen auf der im Plugin hinterlegten Rechtsprechung und genannter Kommentarliteratur. Die Skills ersetzen keine eigene anwaltliche, steuerberatende oder berufsbetreuerische Prüfung im Einzelfall.
