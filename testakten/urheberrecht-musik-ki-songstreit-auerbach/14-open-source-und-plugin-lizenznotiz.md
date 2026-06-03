# Open-Source- und Plugin-Lizenznotiz Kieselglas

## Fundstück

Im Projektordner des internen Synthesizer-Plugins liegt ein Paketverweis auf `grain-spark-lite`, Version 1.8.2. Die Lizenzdatei liegt nicht im exportierten Ordner. Im Commit-Kommentar vom 12.01.2026 steht: „MIT? check later“.

## Relevanz für die Musikakte

Der Open-Source-Punkt entscheidet nicht unmittelbar über den Nachtbogen-Claim. Er kann aber die Rechtekette am Plugin und damit die Erklärung schwächen, der Klang sei vollständig intern und frei verwertbar. Wenn das Plugin aus fremdem Code besteht, kann zusätzlich ein Softwarelizenzproblem entstehen.

## Prüfprogramm

1. Tatsächliche Lizenz und Version des Pakets beschaffen.
2. Prüfen, ob Code nur intern genutzt oder in ein extern geliefertes Plugin eingebunden wurde.
3. Prüfen, ob Lizenzhinweise, Source-Code-Angebote oder Copyleft-Pflichten ausgelöst sind.
4. Prüfen, ob Presetdaten oder Parameterlisten überhaupt unter der Softwarelizenz stehen.
5. Prüfen, ob der Werbekunde Zusicherungen zu Softwarebestandteilen verlangt hat.

## Vorläufige Einschätzung

Wenn `grain-spark-lite` tatsächlich MIT-lizenziert ist, wird das eher ein Attribution- und Dokumentationsthema. Wenn die Lizenz aber anders lautet oder der Code aus einem nicht freigegebenen Repository stammt, entsteht ein eigener Mangel im Release-Paket.

## Nachforderung

Auerbach soll vollständige `package-lock.json`, Lizenzdateien, Git-Historie und Build-Artefakte liefern. Henning Valtin soll erklären, ob er Code oder nur Presets beigesteuert hat.
