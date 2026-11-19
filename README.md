# style-kit

UI building blocks — **elements**, **color palettes** and **themes** — that Claude uses to generate reports, websites, dashboards and other pages in a consistent look.

## How it works

- **`elements/`** — theme-neutral UI elements (buttons, forms, filters, menus, toggles). Each has a CSS file, an HTML preview and a `.md` spec listing the CSS variables a theme can override.
- **`themes/general.md`** — general design rules that apply to every theme (e.g. text clearance inside rounded shapes). Always read alongside the theme's `design.md`.
- **`themes/<name>/design.md`** — the source of truth for a theme: colors, fonts, shapes, borders, separators and how each element should look.
- **`color_palettes/palettes.md`** — fallback palettes when no theme is chosen.

To build a UI: pick a theme, read `themes/general.md` and the theme's `design.md`, and assemble the page from `elements/`, restyled via their CSS variables (e.g. `--btn-*`). Where they disagree, **`design.md` wins**. Don't add colors, rounded corners, shadows etc. the theme doesn't allow.

Available themes: `college`, `waterlily`.

## Creating a new theme

1. Create `themes/<name>/design.md` covering:
   - colors (hex values and names)
   - fonts
   - shapes / corners
   - borders and separators
   - how elements look (buttons, cards, toggles, forms, ...)
2. Add two examples built strictly from that `design.md`:
   - `examples/report.html` — a data-analysis report
   - `examples/game.html` — a small interactive game (e.g. word puzzle, picture matching)

   Link the element CSS by relative path (`../../../elements/...`) and apply the theme as overrides, so examples stay in sync with the elements.
3. Optionally add theme-specific element styles in `themes/<name>/elements/`.

Tip: ask Claude to "create a new theme called X" with a few reference images or colors — it will follow these steps.

## Keeping examples in sync

A pre-commit hook regenerates a theme's `examples/` with Claude Code whenever a commit changes its `design.md`, and adds the updated examples to the same commit. Enable it once per clone:

```sh
git config core.hooksPath .githooks
```

- Needs [Claude Code](https://claude.com/claude-code) (`claude`) on your PATH. Without it the hook warns and lets the commit through unchanged.
- Each affected theme takes a few minutes. Skip it for one commit with `SKIP_EXAMPLES=1 git commit ...` (or `git commit --no-verify`).
- The examples are LLM output. Review the regenerated files (`git show`) before pushing.
