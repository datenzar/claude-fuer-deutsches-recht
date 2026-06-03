# Projektsteckbrief AeroSense Edge Drift Compensation

## Kurzbeschreibung

Das Vorhaben soll ein robustes Sensorik- und Auswertesystem für industrielle Feuchte-, Temperatur- und Vibrationsmessung schaffen. Ziel ist nicht ein weiteres Dashboard, sondern eine Mess- und Korrekturarchitektur, die Sensordrift unter Kondensat, Staub, Vibration und wechselnder Luftströmung lokal erkennt, bewertet und innerhalb definierter Toleranzen kompensiert.

## Technischer Schmerzpunkt

Die Bestandsprodukte der Mandantin funktionieren in trockenen Produktionslinien hinreichend. In Nass- und Kühlbereichen kommt es dagegen zu Drift, Signalrauschen und Kalibrierungsfehlern. Bisheriger Ansatz: Sensor ausbauen, trocknen, neu kalibrieren. Das ist teuer, erzeugt Stillstand und führt zu falschen Wartungsentscheidungen. Der FuE-Kern liegt im Versuch, die Messverzerrung nicht nur statistisch zu glätten, sondern physikalisch plausibel und reproduzierbar zu erkennen.

## Arbeitshypothesen

| Hypothese | Förderrelevanz | Risiko |
| --- | --- | --- |
| Kondensatfilm erzeugt charakteristische Impedanz- und Temperaturmuster | Neuheits-/Unsicherheitskern | Muster können anlagenspezifisch sein |
| Lokale Edge-Auswertung genügt ohne Cloudmodell | technisches Ziel | Speicher, Energie und Updatefähigkeit begrenzen Modellgröße |
| Transfer zwischen drei Anlagenklassen möglich | Reproduzierbarkeit | Datenmenge zu klein, Overfitting-Gefahr |
| Kombination aus Referenzsensor und Selbstdiagnose senkt Rekalibrierung | wirtschaftlicher Nutzen, aber nicht alleiniger FuE-Grund | Standardlösung könnte als bloße Qualitätsverbesserung erscheinen |

## Nicht tragfähige Fördererzählungen

- "Wir bauen KI ein" ist kein FuE-Argument.
- "Das Produkt ist neu für uns" genügt nicht.
- "Der Markt braucht das" ersetzt keine technische Unsicherheit.
- "Die Konkurrenz kann das nicht" muss mit recherchiertem Stand der Technik unterlegt werden.
