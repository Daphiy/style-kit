# Cotton Design Guide
Design style: MINIMALIST, ELEGANT AND SLEEK. Warm and quiet, with colour used sparingly. 

## First principle: minimal, no redundant elements
Every element on the page must carry information the reader needs. Before adding anything, ask whether the page would lose information without it. If not, leave it out.
- No eyebrows or kickers, decorative chips, badges, icons, dividers, ornaments or "label" pills.
- Don't say the same thing twice. If a title says it, the subtitle doesn't repeat it. If a line is already highlighted, it doesn't also get a "Red flag" chip.
- Prefer plain text to a component. A status, a count, a category name or a date is usually best as a word in a sentence.
- Fewer, larger, calmer elements beat many small ones. When in doubt, remove.
A calm, light, editorial style. White cards sit on a warm off-white page. The type is quiet, the corners are large and soft, there is almost no shadow, and soft pastels carry the meaning.

## Colors

### Neutrals 
The page background is cream, #FAF7F2, and cards are white.

The top header bar for navigation is white. 

#F0EEE4 is a slightly deeper off-white.
#E0DDD4 is the light grey for borders and dividers.
Text greys, from lightest to darkest: #8C8985 (grey-500) for tertiary text, #756F68 (medium grey) for secondary text, and #1C1B18 (dark grey) for primary text and headings.

### General 

#### Use colour sparingly (hard rule)
This theme is minimalist, elegant and sleek. Most of every page is neutral: cream ground, white surfaces, grey lines and ink text. Colour appears only where it means something:
- a category
- a state (selected, active, highlighted)
- the main pink accent

Colour is never decoration. If you're unsure whether an element needs colour, leave it neutral. A page where most elements are coloured is wrong.

**One meaning per colour.** On a page, each colour stands for exactly one thing. Once colours encode the page's categories (for example cotton species), don't reuse the palette for anything else.

**Don't make status labels.** Status, level, risk, priority, rating and similar (Low / Medium / High risk, New, Recommended …) are not chips, pills or badges. Write them into the item's text instead, for example "High risk. The most common premium claim…" or "Cotton type · high risk".
- Use ink text, optionally at weight 500. No fill, no dot, no border and no colour.
- If the order matters, show it by sorting or in words, not with traffic-light colours.

Coloured status labels compete with the category colours and only add clutter.

**No decorative chips.** A chip or pill must do a job: either it's a filter you can click, or it names a category whose colour the reader matches against a chart or legend. Everything else is clutter. In particular:
- **No eyebrow or kicker labels above titles** ("Home textiles & basics", "Report", "New", the topic or section name). Leave them out. If the context really matters, put it in the subtitle or intro sentence as plain text.
- **No pills for metadata** such as dates, authors, sources, counts or read time. Write these as muted plain text.

Before adding any chip, badge or coloured element, ask whether the page would lose information without it. If not, don't add it.

#### Borders (hard rule)
The default border is 1px #E0DDD4 grey. A border may only be coloured in two cases:

1. **The element already carries that colour.** A chip or badge with a pale pink fill may have a pink border, and a pale yellow chip may have a yellow border. The border repeats the element's own hue.
2. **It shows a highlight.** That means an active, selected or linked item, such as the card that matches the label line you point at. The highlight border uses the element's own hue:
   - A coloured element highlights in its own colour.
   - A neutral element that already holds a pink detail (for example a white card with a pink numbered badge) may highlight in pink.
   - A neutral element with no colour in it (the white "All" filter bubble, a plain white card) highlights in a darker neutral, never pink. Use a #8C8985 border and a #F0EEE4 fill.

Never colour the border of a neutral, static element: cards, panels, tiles, image frames, inputs, popovers or dropdowns at rest. These stay grey #E0DDD4.

**Never combine hues on one element.** Fill, border, dot, icon and highlight all come from the same family. A pink highlight ring on a yellow chip is wrong; highlight the yellow chip in yellow instead. This also covers fakes: no `box-shadow` or `outline` ring in a second hue.

The active nav tab has a 2px blue underline (#8DBAED). Keyboard focus uses a 2px ink outline (#1C1B18), not a colour.

#### Hover
Hover is always a **darker version of the element's own colour**. It never switches to another hue.
1. If the theme defines a darker shade of that colour, use it. For example, a #E5F3FC blue button hovers to #D6E7F8, and a #8DBAED blue element hovers to #4B8FD0.
2. Otherwise, lay a 20% black overlay on it (`box-shadow: inset 0 0 0 100vmax rgba(0,0,0,0.2)`).

Hover never introduces a new colour. A pink hover on a blue button, a pink ring around a hovered card, or a grey background swap (`hover:bg-gray-50`) are all wrong. Text and border keep their family too. Hovering a blue button darkens the blue and nothing else.

**Implementation note.** The shared button CSS (`elements/buttons/buttons.css`) sets `.btn:hover { background: var(--btn-primary) }`, and in this theme `--btn-primary` is pink. If a variant sets `background:` directly (`.btn--action { background: blue }`), the `:hover` rule is more specific and wins, so the button turns pink on hover. To avoid that, set the variant's colour through the variables (`.btn--action { --btn-primary: <its fill>; --btn-primary-fg: <its text> }`), or give the variant its own `:hover` rule. After building, hover over every coloured control and check that it only gets darker.

### Categories/ Type families 
if you have a few categories, use color to represent them. Each family has a pale fill and a stronger "core" pastel. The core pastel colours the dot, the icon, chart marks and that family's own border.

How a category chip or filter bubble looks. Every part uses one family only:
- **Label or unselected filter bubble:** pale family fill, 1px border in the core colour, an 8px dot in the core colour, ink text.
- **Selected filter bubble:** the same chip with a 2px border in its own core colour and ink text at weight 500. A selected yellow chip gets a yellow border, never a pink one.
- **"All" or another neutral bubble:** white fill and a grey #E0DDD4 border when unselected. When selected, it gets a #F0EEE4 fill and a 2px #8C8985 border, which is a darker neutral. It is never pink: the bubbles next to it are green, purple and yellow, and pink would add a fourth, unrelated colour.
- **Numbered badges** (1, 2, 3 …): pale pink fill, pink border, ink number.

grey is never to be used to signal a category in the report or in the charts. if needed, repeat colors in new shades

A label that names one of the page's categories takes that category's colour. All other labels are neutral (see "Don't colour-code status labels" above). 

#### Pink 
The fill is #FDE0E5. The core colour (dot, icon, chart, and the border of this family's own chips) is #F8AAB6.

#### Yellow
The fill is #FFF8CE. The core colour (dot, icon, chart, and the border of this family's own chips) is #FCCF61.
#FFE495 (swa-yellow-light) and the darker #D3A328 (swa-yellow-1) round out the brand yellows. 

####  Blue 
The fill is #E5F3FC. The core colour (dot, icon, chart, and the border of this family's own chips) is #8DBAED.

#### Green 
The fill is #E4F3E1. The core colour (dot, icon, chart, and the border of this family's own chips) is #9CCB8E.

#### Purple 
The fill is #F4ECF5 (swa-purple-light), with #EADBEB as a slightly deeper tint. The core colour (dot, icon, chart, and the border of this family's own chips) is #CCA8CF (swa-purple). A strong violet, #874AF0 (swa-purple-1), is defined but rarely used. 


### Main Accent: Pink
Pink is the main accent colour. The lightest shade, #FDE0E5 (swa-pink-lighter), is the Freestanding fill, and #FCC2CC (swa-pink-light) is available as an in-between tint. 

The core pink, #F8AAB6 (swa-pink), is used for:
1. the active segment of the toggle
2. primary buttons such as Apply
3. labels 
4. the highlight border of an active element that already holds pink, such as a card with a pink numbered badge. It is never used on an element of another hue, and never on a plain neutral element like the "All" bubble.


### Blue
Blue is used for navigation, filters and action buttons. The lightest shade, #E5F3FC (swa-blue-lightest), is the Window fill, the filter chip background and the action button background. The shades in between are #D6E7F8 (swa-blue-lighter) and #ADCFF1 (swa-blue-light). The core blue, #8DBAED (swa-blue), is the blue family's dot and icon colour, the active nav-tab underline and text, the "+" add tiles and a chart colour. #4B8FD0 (swa-blue-2) is the filter chip text and the "+" tile hover. The deeper #358ADA and #2E6DA8 are defined but rarely used.

Links are deep blue and underline on hover. Focus shows a 2px ink (#1C1B18) outline with a 2px offset. Disabled controls use 55% opacity.


### The overall pattern
Each hue comes as a very pale wash for fills plus a mid-saturation pastel for dots, icons, chart marks and that element's own border. Neutral elements have grey borders unless they are highlighted. One hue per element. Text rarely uses the hue colours. Pink and blue carry interaction state. Yellow, purple and green mark category families only. They are not used for status, risk or warning labels.


## Fonts
There are two typefaces, set in theme.css:

Body / UI: 'Euclid Ignited', 'Euclid Circular B', system-ui, sans-serif. Weight 400 normal and 500 medium. Buttons and labels get letter-spacing: 0.025em.
Display headings: 'ITC Novarese', serif through the .font-novarese class. It's used for page titles ("Store Sales", "By Section", "Displays", "Shelf Productivity Scan") at text-2xl to text-4xl, plus collapsible section titles at text-xl. These headings use no bold, only size and the serif.
Small caps style: the toggle uses text-xs uppercase tracking-wider.

⚠️ Euclid and Novarese only render on machines that have them installed. 
As a fallback, use: 
#### Fallback fonts 
Family: Inter, with fallbacks system-ui, -apple-system, 'Segoe UI', sans-serif. Monospace: ui-monospace, SFMono-Regular, Consolas, monospace.

The heading font Novarese should fallback to a serif, e.g. Lora. 

#### weights 
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


## Shapes
Shapes are slighly rounded, sleek and elegant. 

- Base radius: --radius: 0.625rem (10px). rounded-lg (10px) is by far the most common (~137 uses), followed by rounded-md (8px) for inner elements and rounded-full for chips, badges and spinners.
- Larger radius: rounded-2xl (16px) only on the clickable section filter cards.
- Borders: 1px #E0DDD4 by default. Thin and light, never heavy. They are coloured only on an element that already has that hue, or as a highlight (see "Borders" under Colors).
- Shading: soft. The standard is shadow-sm on cards and bubbles. Floating layers (dropdowns, popovers) use shadow-lg, and image cards go up to shadow-md on hover. A comment in the code says outright that every bubble gets shadow-sm so it lifts off the cream background.
- Focus: keyboard focus shows a 2px ink (#1C1B18) outline with a 2px offset. Never recolour a border to show focus.
- Motion: content fades in (animate-fadeIn, 0.4s), dismissed items fade and slide out, and loading shows three pulsing dots.

- Panels and stat tiles: 16px radius, white, no border, a very faint shadow 0 1px 3px rgba(28,27,24,0.06). Panels have 32px padding and tiles 24px.
- Small cards: 12px radius, 1px line border, 16px padding, no shadow.

- Charts: no gradients, 3D or gridline clutter.
- Tables: no outer border or zebra stripes. Rows are split by a hairline top border (line at 60%). Cells use 16px vertical padding and 24px right padding.

## Elements


### Toggle Multicategory (A / B / C / D)
It's a segmented control built from buttons inside one bordered pill:

<div className="inline-flex rounded-lg border border-gray-200 overflow-hidden bg-white shadow-sm">
  {options.map(opt => (
    <button
      aria-pressed={value === opt}
      onClick={() => onChange(opt)}
      className={`px-3 py-1 text-xs uppercase tracking-wider transition-colors ${
        value === opt ? 'bg-swa-pink text-swa-darkgrey' : 'text-gray-600'   /* hover = 20% black overlay */
      }`}>
      {opt}
    </button>
  ))}
  {/* last segment gets a divider */}
  <button className="... border-l border-gray-200">Custom</button>
</div>
How it works:

overflow-hidden on the wrapper clips the segments to the rounded corners, so the segments themselves need no radius.
There are no gaps or dividers between the presets. Only the "Custom" segment gets a border-l.
The active segment is filled solid pink with ink text (never white text on pink). Inactive segments are grey text on white. The outer border and the "Custom" divider are grey #E0DDD4.
"Custom" opens a popover (absolute right-0 top-full mt-2 bg-white border rounded-lg shadow-lg p-3 w-64) with two date inputs and Cancel/Apply buttons. Once a range is applied, the button label changes to show that range.
To reuse it for other categories, swap the presets array. The pattern takes any number of options.

### Filter 
A filter can also use rounded filter bubbles per category, or a dropdown menu, rather than a toggle. 

Filter bubbles are fully rounded pills, 6px 14px padding, 13px text at weight 500. Borders, fills and the selected state follow "Categories / Type families" above. A selected bubble is highlighted in its own hue only.

### Embedded images (image inside a bubble)
The look comes from a white outer frame with tiny padding, wrapping an inner image with a slightly smaller radius:

<div className="bg-white rounded-lg shadow-sm border border-gray-200 p-1.5">   {/* frame */}
  <div className="relative rounded-md overflow-hidden bg-gray-100" style={{aspectRatio:'5 / 3'}}>
    <img className="absolute inset-0 w-full h-full object-cover" />
    {/* bottom gradient + label */}
    <div className="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent" />
    <div className="absolute bottom-0 inset-x-0 p-3 text-white text-sm font-semibold drop-shadow-sm">Shelf name</div>
  </div>
</div>
The 6px white p-1.5 acts as the slim mat or border. The outer rounded-lg (10px) and inner rounded-md (8px) keep the two corners visually concentric.
On hover, the gradient and label fade out and a centred dark overlay (bg-black/44) appears with the name, product count and sales.
In the popup version the image stays at its natural aspect ratio, and a caption sits underneath: text-xs text-swa-mediumgrey "Scanned on…".


### Expandable elements
There are two variants, both a white card with a full-width header button:

#### Variant 1
bg-white rounded-lg border border-gray-200 overflow-hidden. The header is px-5 py-4 (hover = 20% black overlay) and holds a Novarese text-xl title, an optional neutral rounded-full count badge (cream fill, grey border, muted text), a grey subtitle, and a ChevronDown/ChevronUp (lucide, w-4 h-4 text-swa-mediumgrey) on the right. The body is px-5 pb-5 pt-1. Open state is remembered in sessionStorage.
#### Variant 2
the same card plus shadow-sm. The header has a 1px #E0DDD4 bottom border, hovers with the 20% black overlay, shows a cream pill badge, and uses ▼/▲ text glyphs instead of icons.

Neither variant animates. The content simply mounts and unmounts.


## Headings

Page titles and section titles span the full width of the content column:
- no `max-width` narrower than the column
- no indent, side column or number gutter beside the title
- the title starts at the same left edge as the panels below it
- any intro paragraph under a title starts at that same left edge

A title never takes more than two lines at any screen width.
- Size it with `clamp()` so it shrinks on narrow screens. For example, page title `clamp(28px, 4vw, 44px)` and section title `clamp(24px, 3vw, 32px)`.
- If it would still wrap to a third line at the smallest size, the title is too long. Shorten it and move the rest into the subtitle or intro paragraph. Don't shrink it further, cap its width or let it run to three lines.
- After building, check the rendered page at desktop, tablet and 400px widths.

## Style instructions

1. Use the warm ground background for the page and white panels for content. Separate content with whitespace (24–32px gaps) rather than lines.
Keep it flat and quiet: one faint shadow level, no gradients, no dark sections. The only dark element is ink, used for the primary button and the active nav item (white text).
2. Colour carries meaning, not decoration. Pair every colour with a text label or a legend, and never rely on colour alone.
3. Use ink text on pastel backgrounds. Never use white text on pastels.
4. Hierarchy comes from size and weight, not colour. Muted grey is for secondary information only.
5. A typical page starts with a title, then a row of stat tiles (label, big number, optional muted sub-line), then detail panels.
6. Put long detail in collapsible sections. The summary line shows a bold title plus a muted "· count" note.
7. Meet WCAG AA contrast and keep the layout responsive: grids wrap on narrow screens and wide tables scroll horizontally.