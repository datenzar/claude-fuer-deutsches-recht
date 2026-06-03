# Source-Escrow-Trigger - Checkliste

- Ist die Escrow-Anlage Vertragsbestandteil oder nur im Datenraum erwähnt?
- Gibt es einen Trigger bei “critical failure” oder nur bei Insolvenz, Supportende und dauerhafter Nichterfüllung?
- Muss der hinterlegte Stand buildfähig sein? Welche Third-Party-Komponenten sind enthalten?
- Darf Sonnenklee den Code selbst nutzen oder nur einem Ersatzdienstleister übergeben?
- Sind OSS- und Contractor-Rechte von der Herausgabe gedeckt?
- Wer prüft die Trigger: Escrow-Agent, Schiedsgutachter, Gericht oder beide Parteien?
- Welche Geheimnisschutzmaßnahmen gelten nach Herausgabe?

Kurzbefund: Der Trigger “failure to provide business-critical availability” ist zu weich. Codeforst sollte technische Verifikation, Cure Period, eingeschränkte Nutzung, Vertraulichkeit und Rechtekettenvorbehalte nachziehen.
