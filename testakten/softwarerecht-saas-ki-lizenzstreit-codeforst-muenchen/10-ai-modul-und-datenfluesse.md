# DispatchMind - KI-Modul und Datenflüsse

DispatchMind prognostiziert für Flottenkunden die Reihenfolge von Ladefenstern, Wartungsfenstern und Fahrerwechseln. Das Modell nutzt historische Fahrzeugtelemetrie, Depotdaten, Wetterdaten, Störungslogs, Werkstattkapazitäten und manuelle Disponentenentscheidungen. Die Mandantin beschreibt es im Vertrieb als “KI”, in der technischen Dokumentation als “hybriden Optimierer mit ML-Ranking”.

## Datenkategorien

- Fahrzeug-ID, Depot, Schicht-ID, Werkstatt-ID, Route, Ladefenster, Ausfallwahrscheinlichkeit.
- Fahrerkennung: in der Cloud als Hashwert gespeichert; im Kunden-ERP rückführbar.
- Trainingsdaten: monatlich aggregiert, aber nicht vollständig anonymisiert.
- Feedbackdaten: Disponenten markieren Vorschläge als “brauchbar”, “riskant”, “unmöglich”.

## Offene rechtliche Punkte

- Rollenklärung: Codeforst als Auftragsverarbeiter, eigenständig Verantwortlicher oder Mischlage für Produktverbesserung?
- Datenlizenz: Darf Codeforst Kunden-Telemetrie für allgemeines Modelltraining nutzen?
- Data Act: Ist der Datenzugang bei vernetzten Fahrzeug-/Ladeprodukten einschlägig oder betrifft es nur Kundendaten im SaaS-Vertrag?
- KI-VO: Zweckbestimmung liegt bei Flottenoptimierung, nicht Personalbeurteilung. Wenn Sonnenklee das Tool faktisch für Schichtdisziplin verwendet, braucht es Governance gegen Zweckentfremdung.
