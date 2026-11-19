# style-kit

This repo organises UI design building blocks — **elements**, **color palettes** and **themes** — so Claude can generate UIs (reports, websites, dashboards and other pages) that follow a chosen look.

## Layout

```
color_palettes/   named colors and palettes
  colors.css        named colors as CSS variables (--name: value;)
  palettes.py       palette definitions (pydantic); validates them and writes palettes.md
  palettes.md       generated: palette instructions for Claude (do not edit by hand)
  palettes.css
elements/         general UI elements, not tied to any theme
  <group>/          e.g. buttons, filter, forms, menus, toggles
    <group>.md        spec: variants, sizes, states, which CSS variables themes override
    <name>.css/.html  plain-CSS implementation and its preview page
    <name>.png        rendered preview
    shadcn/*.tsx      original shadcn/ui source the CSS mirrors (where there is one)
  _preview/         render.py + preview.css for regenerating the PNGs
themes/           one folder per theme
  <theme>/
    design.md         colors, fonts, shapes and general styles of the theme, and what the elements look like in it
    elements/         elements styled for this theme, following design.md (optional)
    examples/
      report.html       a data-analysis report built in the theme
      game.html         a small interactive game built in the theme
```

## How it is used

1. Pick a theme from `themes/`.
2. Read its `design.md`. It is the source of truth for the theme's colors, fonts, shapes, borders, separators and overall style, and it describes what each element should look like in that theme.
3. Build the UI from the elements in `elements/`. They provide the structure and behaviour (variants, states, markup). Style them the way `design.md` describes, for example by overriding their CSS variables such as `--btn-*`. Where an element's default look and `design.md` differ, `design.md` wins.
4. If no theme is given, use a palette from `color_palettes/palettes.md`.

When generating a UI, stick to the colors and styles the theme defines; don't introduce new colors, rounded corners, shadows etc. unless the theme allows them.

## Working on the repo

- **Adding a theme:** create `themes/<name>/design.md` covering at least colors (with hex values and names), fonts, shapes/corners, borders and separators, plus how elements (buttons, cards, toggles, forms, ...) should look in the theme. Then add `examples/report.html` (a data analysis) and `examples/game.html` (a simple interactive game, e.g. a word puzzle or picture matching) built strictly from that `design.md`. They show the theme in use and serve as references when generating new UIs. Examples link the general element CSS by relative path (`../../../elements/...`) and restyle it with theme overrides, so they stay in sync with the elements.
- **Adding or changing an element:** keep the `.css`, `.html` preview and `.md` spec in sync, then run `python elements/_preview/render.py` to refresh the PNGs (needs headless Chrome or Edge; Pillow optional).
- **Palettes:** add colors to `colors.css`, define palettes in `palettes.py`, then run `python color_palettes/palettes.py` to validate them and regenerate `palettes.md`.
