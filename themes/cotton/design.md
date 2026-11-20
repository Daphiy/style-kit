# Cotton Design Guide
Design style: warm, quiet business report
A calm, light, editorial style. White cards sit on a warm off-white page. The type is quiet, the corners are large and soft, there is almost no shadow, and soft pastels carry the meaning.

## Colors
Neutrals

Token	Hex	Use
ground	#F0EEE4	page background (warm off-white)
surface	#FFFFFF	cards, panels, header bar
cream	#FAF7F2	hover states, subtle inset areas
ink	#1C1B18	body text, primary buttons, active nav item
muted	#5C5A54	secondary text, labels, table headers
line	#E0DDD4	borders, row dividers (often at 60% opacity)
line-strong	#C9C5B8	input borders, table header underline
Accent

Token	Hex	Use
blue	#8DBAED	accent dot, chart highlight
blue-tint	#D6E7F8	info backgrounds, nav hover, highlight ring
action	#358ADA	interactive accent
deep	#2E6DA8	links, focus outline
Status (solid colour for dots and markers, tint for backgrounds)

Status	Solid	Tint
success	#77BB78	#C7E299
warning	#FCCF61	#FFE495
info	#CCA8CF	#EADBEB
error	#F14545	#F9DCE4 (text on it: #8A2A3A)
neutral	#C9C5B8	#E7E3D8
Chart colours (mid-tone pastels for bars and segments)
#A9CBF0 blue, #F1B6C9 pink, #C9E8D4 green, #FFCC8A orange. For a "partial" variant, hatch a colour with its tint: repeating-linear-gradient(135deg, #A9CBF0 0 3px, #DBE9F8 3px 6px).

Categorical pastels (chips and tags). Use them in this order:
#D6E7F8 blue, #E3DBF3 lavender, #D5EFE0 mint, #FBE3CF peach, #F8DBE4 pink, #FFF1BF butter, #D4EEF0 aqua, #E6F0CD lime, #F3D9EF orchid, #F6E0D6 apricot, #DDE3EA slate, #E9E4D5 sand.

## Shapes
Shapes are slighly rounded, sleek and elegant. 

- Panels and stat tiles: 16px radius, white, no border, a very faint shadow 0 1px 3px rgba(28,27,24,0.06). Panels have 32px padding and tiles 24px.
- Small cards: 12px radius, 1px line border, 16px padding, no shadow.
- Highlighted panel: the same panel plus a 2px blue-tint ring.
- Buttons, inputs, nav items, notices: 8px radius, padding about 12×6px.

- Chips: full pill, padding 10×2px, with an 8px round dot of the solid colour before the text.
- Charts: no gradients, 3D or gridline clutter.
- Tables: no outer border or zebra stripes. Rows are split by a hairline top border (line at 60%). Cells use 16px vertical padding and 24px right padding.
- Header: a full-width white bar with a 1px bottom line border. Content is centred, max 1400px wide, with 16px side padding.

## Fonts
Family: Inter, with fallbacks system-ui, -apple-system, 'Segoe UI', sans-serif. Monospace: ui-monospace, SFMono-Regular, Consolas, monospace.
Weights: 400 for body, 500 for subheadings, labels and buttons, 600 for page and section titles and big numbers.
Scale:
body 15px, line-height 1.4
page title 30px semibold, tight tracking
section title 24px semibold
panel title 18px semibold
big KPI number 36px semibold, tight tracking, tabular numerals
secondary text 14px muted
small text and chips 12px
Labels and table headers: 12px, uppercase, letter-spacing 0.025em, normal weight, muted colour.

-> Links are deep blue and underline on hover. Focus shows a 2px deep outline with a 2px offset. Disabled controls use 55% opacity.

## Style instructions

1. Use the warm ground background for the page and white panels for content. Separate content with whitespace (24–32px gaps) rather than lines.
Keep it flat and quiet: one faint shadow level, no gradients, no dark sections. The only dark element is ink, used for the primary button and the active nav item (white text).
2. Colour carries meaning, not decoration. Pair every colour with a text label or a legend, and never rely on colour alone.
3. Use ink text on pastel backgrounds. Never use white text on pastels.
4. Hierarchy comes from size and weight, not colour. Muted grey is for secondary information only.
5. A typical page starts with a title, then a row of stat tiles (label, big number, optional muted sub-line), then detail panels.
6. Put long detail in collapsible sections. The summary line shows a bold title plus a muted "· count" note.
7. Meet WCAG AA contrast and keep the layout responsive: grids wrap on narrow screens and wide tables scroll horizontally.