# Ticket und Git Review Auszüge

## Ticketbild

Die Entwicklung wird in Jira und GitLab dokumentiert. Die Akte enthält keine vollständigen Repository-Daten, aber Auszüge mit typischen Ticketbeschreibungen. Die Tickets müssen in der Belegmatrix den Stunden zugeordnet werden.

| Ticket | Titel | Kommentar | FuE-Bewertung |
| --- | --- | --- | --- |
| AE-214 | Condensate state vector v2 | mathematische Modellvariante, später verworfen | förderstark |
| AE-239 | UI trend color palette | reine Anzeige und Usability | nicht fördern |
| AE-251 | Edge memory compression | technische Modellreduktion | förderstark |
| AE-268 | Customer demo package | Vertrieb/Marketing | nicht fördern |
| AE-277 | Vibration artefact split | Trennung Messfehler/Prozessänderung | förderstark |
| AE-301 | Lissabon raw data parser | Datenaufbereitung für Messreihen | teilweise, wenn unmittelbar FuE |
| AE-319 | Launch readiness dashboard | Produktisierung | streichen |

## Git-Review-Notiz

Code-Review vom 17.03.2025 zeigt, dass die Modellreduktion nicht nur eine Performanceoptimierung war. Das Team musste entscheiden, welche Zustandsvariablen technisch unverzichtbar sind. Diese Entscheidung berührt die Reproduzierbarkeit und Fehlalarmquote. Der Review kann daher AP3 stützen.

## Schwacher Beleg

Mehrere Tickets haben nur Titel wie "Research Sprint" oder "AeroSense Improvements". Diese sollten nicht als Beleg verwendet werden, bevor sie nicht mit konkreten technischen Tätigkeiten verknüpft sind.
