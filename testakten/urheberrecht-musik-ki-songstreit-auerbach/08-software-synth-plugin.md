# Synthesizer-Plugin „Kieselglas“

Auerbach Soundworks nutzt ein internes Audio-Plugin mit der Bezeichnung „Kieselglas“. Es erzeugt kurze glasige Percussion-Impulse und modulierte Flächen. Henning Valtin behauptet, die Presets `GlassStep Berlin 07` und `Dachlicht 3` stammten von ihm. Auerbach verweist auf internen Code und alte Presetlisten.

## Dateiauszug Quellcode

```javascript
// Kieselglas prototype, internal audio sketch
export function impulse(seed, tone, scatter) {
  const base = Math.sin(seed * 12.9898) * 43758.5453;
  const grain = base - Math.floor(base);
  return {
    pitch: tone + Math.round((grain - 0.5) * scatter),
    decay: 0.18 + grain * 0.31,
    shimmer: 0.42 + (1 - grain) * 0.26
  };
}
```

## Streitpunkte

- Codeausdruck: Auerbach behauptet, der Algorithmus sei intern im Januar entstanden.
- Funktionalität: Henning beschreibt nur „glasige urbane Percussion auf 2 und 4“; das ist eher Idee oder Soundziel.
- GUI: Screenshot zeigt runde Regler „Split“, „Frost“, „Beton“, „Glanz“. Unklar, ob GUI grafisch schutzfähig oder nur funktional ist.
- Presets: Presetnamen und Parameterlisten können eigenständige Werkqualität kaum tragen, sind aber Beweis für Produktionsbeitrag.
- Open Source: Ein npm-Paket `grain-spark-lite` ist eingebunden; Lizenztext fehlt.

## Zu prüfen

Software-Schutz nach §§ 69a ff. UrhG betrifft den Ausdruck des Programms. Funktion, Soundidee, Programmiersprache oder Datenformat sind gesondert zu prüfen. Für die Musikakte ist außerdem relevant, ob das Plugin das angebliche Nachtbogen-Soundelement eigenständig erzeugen kann.
