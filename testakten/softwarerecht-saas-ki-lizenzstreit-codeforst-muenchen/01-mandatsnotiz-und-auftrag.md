# Mandatsnotiz - Projekt RouteLuchs

**Mandantin:** Codeforst GmbH, München, 84 Mitarbeitende, Schwerpunkt SaaS für Flotten- und Lieferkettenoptimierung.  
**Gegenseite/Kunde:** Sonnenklee Mobility AG, Hamburg, Betreiberin von Lade-, Werkstatt- und Dispositionssoftware für kommunale E-Fahrzeugflotten.  
**Produkt:** RouteLuchs Cloud mit KI-Modul “DispatchMind”, On-Prem-Gateway “LuchsBox”, SDK für Werkstattpartner und REST-API.

## Sofortauftrag

Die Mandantin will binnen 72 Stunden ein belastbares Memo, ob sie den Kunden auditieren lassen muss, ob die Lizenzüberschreitung haltbar ist, ob sie überhaupt alle Rechte am Kerncode hat und ob die angekündigte Kündigung mit Datenherausgabe/Source-Escrow/Zurückbehaltungsrechten zu stoppen ist.

## Heikle Punkte

- Sales hat im Februar 2025 in einer E-Mail “all IP and unlimited affiliate use” zugesagt; der unterschriebene Vertrag sagt das Gegenteil.
- Die Rechtekette beim Optimizer ist unklar: Arbeitnehmer-Code, privater Vorcode, US-Contractor, polnischer Nearshore-Commit und AGPL-Komponente laufen ineinander.
- Das KI-Modul verarbeitet Telemetrie- und Standortdaten. Im Vertrag steht “anonymous operational data”; in der Implementierung sind Fahrzeug-ID, Depot, Schicht und Fahrerkennung pseudonymisiert, aber rückführbar.
- Der Kunde droht, wegen “critical public transport service” Source-Escrow zu ziehen. Der Escrow-Trigger ist in der Anlage schlecht formuliert.
- Der Investor der Mandantin will in der Series B eine IP-Reps-and-Warranties-Bestätigung. Das ist im jetzigen Zustand mutig.

## Gewünschte Outputs

1. Rechtekettenmatrix mit Ampel.
2. Lizenzmetrik-Analyse Named User/API/Affiliate/Container.
3. OSS-Sofortplan inklusive AGPL-Fund.
4. Briefing an US-Counsel zu work made for hire, assignment, software copyright registration und § 101 Patentfähigkeit.
5. Redline-Paket für SaaS-Vertrag, DPA, Escrow und Auditklausel.
