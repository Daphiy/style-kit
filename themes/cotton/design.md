# Cotton Design Guide
Design style: warm, quiet, minimalist. 
A calm, light, editorial style. White cards sit on a warm off-white page. The type is quiet, the corners are large and soft, there is almost no shadow, and soft pastels carry the meaning.


## Colors

### Neutrals 
The page background is cream, #FAF7F2, and cards are white.

#F0EEE4 is a slightly deeper off-white.
#E0DDD4 is the light grey for borders and dividers.
Text greys, from lightest to darkest: #8C8985 (grey-500) for tertiary text, #756F68 (medium grey) for secondary text, and #1C1B18 (dark grey) for primary text and headings.

### General 
The borders are never in another color. 

Hover is always created with adding a black overlay at 20% opacity, not by adding color. 

### Categories/ Type families 
if you have a few categories, use color to represent them. Each family has a pale fill and a stronger pastel border.

grey is never to be used to signal a category in the report or in the charts. if needed, repeat colors in new shades

#### Pink 
The fill is #FDE0E5 and the border and icon are #F8AAB6.

#### Yellow
The fill is #FFF8CE and the border and icon are #FCCF61.
#FFE495 (swa-yellow-light) and the darker #D3A328 (swa-yellow-1) round out the brand yellows. 

####  Blue 
Shelf Unit, Hanging Boxes and Other. The fill is #E5F3FC and the border and icon are #8DBAED.
Purple (Add-ons): Earrings Spinner, Tray and Other. The fill is #F4ECF5 and the border and icon are #CCA8CF.

#### Green 
the fill is #E4F3E1 and the border and icon are #9CCB8E.

#### Purple 
The fill is #F4ECF5 (swa-purple-light), with #EADBEB as a slightly deeper tint. The core purple, #CCA8CF (swa-purple), is the Add-ons border and icon. A strong violet, #874AF0 (swa-purple-1), is defined but rarely used. 

On the display cards, the outer octagon is filled with the family fill at 55% opacity and has a 2px stroke in the border colour, which thickens to 2.5px on hover. Inside it, 7px in, is a white octagon with a 0.5px stroke in the same border colour, so you see a double frame with a coloured band between the lines. The display-type icon sits at the bottom centre in the border colour, and hovering lays a 23% black wash over the inner octagon. In the display picker, each type is shown as a 48px rounded square filled with the family fill, with the icon in the border colour.

### Main Accent: Pink
Pink is the main accent colour. The lightest shade, #FDE0E5 (swa-pink-lighter), is the Freestanding fill, and #FCC2CC (swa-pink-light) is available as an in-between tint. 

The core pink, #F8AAB6 (swa-pink), is used for:
1. the active segment of the toggle
2. primary buttons such as Apply
3. labels 
4. the border of a selected filter card


### Blue
Blue is used for navigation, filters and action buttons. The lightest shade, #E5F3FC (swa-blue-lightest), is the Window fill, the filter chip background and the action button background. The shades in between are #D6E7F8 (swa-blue-lighter) and #ADCFF1 (swa-blue-light). The core blue, #8DBAED (swa-blue), is the Window border, the active nav-tab underline and text, the "+" add tiles and a chart colour. #4B8FD0 (swa-blue-2) is the filter chip text and the "+" tile hover. The deeper #358ADA and #2E6DA8 are defined but rarely used.

Links are deep blue and underline on hover. Focus shows a 2px deep outline with a 2px offset. Disabled controls use 55% opacity.

### Errors 
Errors use a red ramp from #FEF3F3 through #FDE7E7, #FCD1D1, #F14545 and #EE1717 to #BE1212.

### The overall pattern
Each hue comes as a very pale wash for fills plus a mid-saturation pastel for borders, icons and accents. Text rarely uses the hue colours. Pink and blue carry interaction state. Yellow, purple and green mostly mark display families, with amber also used for warnings and green for confirmations.


## Fonts
There are two typefaces, set in theme.css:

Body / UI: 'Euclid Ignited', 'Euclid Circular B', system-ui, sans-serif. Weight 400 normal and 500 medium. Buttons and labels get letter-spacing: 0.025em.
Display headings: 'ITC Novarese', serif through the .font-novarese class. It's used for page titles ("Store Sales", "By Section", "Displays", "Shelf Productivity Scan") at text-2xl to text-4xl, plus collapsible section titles at text-xl. These headings use no bold, only size and the serif.
Small caps style: the toggle uses text-xs uppercase tracking-wider.

⚠️ Euclid and Novarese only render on machines that have them installed. 
As a fallback, use: 
#### Fallback fonts 
Family: Inter, with fallbacks system-ui, -apple-system, 'Segoe UI', sans-serif. Monospace: ui-monospace, SFMono-Regular, Consolas, monospace.

The heading font should fallback to a serif, e.g. Lora. 
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
- Borders: almost every surface has a 1px border-gray-200. Thin and light, never heavy.
- Shading: soft. The standard is shadow-sm on cards and bubbles. Floating layers (dropdowns, popovers) use shadow-lg, and image cards go up to shadow-md on hover. A comment in the code says outright that every bubble gets shadow-sm so it lifts off the cream background.
- Focus: browser outlines are removed globally. Inputs show focus by recolouring the border (pink or dark grey) or with a faint ring-2 ring-swa-darkgrey/20.
- Motion: content fades in (animate-fadeIn, 0.4s), dismissed items fade and slide out, and loading shows three pulsing dots.

- Panels and stat tiles: 16px radius, white, no border, a very faint shadow 0 1px 3px rgba(28,27,24,0.06). Panels have 32px padding and tiles 24px.
- Small cards: 12px radius, 1px line border, 16px padding, no shadow.

- Charts: no gradients, 3D or gridline clutter.
- Tables: no outer border or zebra stripes. Rows are split by a hairline top border (line at 60%). Cells use 16px vertical padding and 24px right padding.

## Elements

### Toggle Multicategory (A / B / C / D)
Source: PeriodToggle in StoreCatalog.tsx:116. It's a segmented control built from buttons inside one bordered pill:

<div className="inline-flex rounded-lg border border-gray-200 overflow-hidden bg-white shadow-sm">
  {options.map(opt => (
    <button
      aria-pressed={value === opt}
      onClick={() => onChange(opt)}
      className={`px-3 py-1 text-xs uppercase tracking-wider transition-colors ${
        value === opt ? 'bg-swa-pink text-white' : 'text-gray-600 hover:bg-gray-50'
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
The active segment is filled solid pink with white text. Inactive segments are grey text on white.
"Custom" opens a popover (absolute right-0 top-full mt-2 bg-white border rounded-lg shadow-lg p-3 w-64) with two date inputs and Cancel/Apply buttons. Once a range is applied, the button label changes to show that range.
To reuse it for other categories, swap the presets array. The pattern takes any number of options.
Shelf image inside a bubble
Source: StoreCatalog.tsx:274 and the popup at around line 2440. The look comes from a white outer frame with tiny padding, wrapping an inner image with a slightly smaller radius:

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
bg-white rounded-lg border border-gray-200 overflow-hidden. The header is px-5 py-4 hover:bg-gray-50 and holds a Novarese text-xl title, an optional amber rounded-full count badge, a grey subtitle, and a ChevronDown/ChevronUp (lucide, w-4 h-4 text-swa-mediumgrey) on the right. The body is px-5 pb-5 pt-1. Open state is remembered in sessionStorage.
#### Variant 2
the same card plus shadow-sm. The header has a border-b border-gray-100, hovers to bg-swa-cream/40, shows a cream pill badge, and uses ▼/▲ text glyphs instead of icons.

Neither variant animates. The content simply mounts and unmounts.

### Filters
Filtering is done by clicking the stat cards themselves:

Each section card is a <button> with rounded-2xl px-5 py-4 border-2. Unselected cards have border-transparent, selected ones border-swa-pink, and both hover to hover:bg-pink-50. Several can be selected at once.
Active filters show above the grid as removable chips: inline-flex items-center gap-1.5 px-2.5 py-1 text-xs rounded-full bg-swa-blue-lightest text-swa-blue-2 border border-swa-blue/30 with an X icon (w-3 h-3). They're preceded by a grey "Filtered:" label.
When two or more filters are active, a "Clear all" text link appears (text-xs text-gray-500 underline underline-offset-2).
The filtered grid re-keys on the filter set, so it fades in again on every change.
Dropdown menu (store selector)
Source: StoreSelector in App.tsx:45. It's a custom dropdown, deliberately not a native <select>:

Trigger: bg-swa-cream border border-gray-300 rounded-lg px-4 py-2 pr-8 text-sm text-swa-darkgrey, with hover:border-swa-darkgrey and the focus ring ring-2 ring-swa-darkgrey/20. A ChevronDown (w-4 h-4 text-gray-400) is absolutely positioned at right-2. The label shows the store name followed by the Swarovski ID.
Menu: absolute right-0 top-full mt-1 z-30 min-w-full bg-white border border-gray-200 rounded-lg shadow-lg py-1 max-h-72 overflow-auto.
Rows: px-3 py-1.5 text-sm. The selected row gets bg-swa-cream text-swa-darkgrey and other rows hover:bg-gray-50. The ID appears after the name as a text-gray-400 suffix.
Dismiss: clicking outside closes the menu (a document mousedown listener).
Responsive: on iPad and mobile the trigger shrinks to text-xs and is capped at max-w-[140px] / max-w-[110px] with truncation.
The settings menu beside it reuses the same trigger and menu styling, with px-4 py-2 rows and a border-t divider.

## Style instructions

1. Use the warm ground background for the page and white panels for content. Separate content with whitespace (24–32px gaps) rather than lines.
Keep it flat and quiet: one faint shadow level, no gradients, no dark sections. The only dark element is ink, used for the primary button and the active nav item (white text).
2. Colour carries meaning, not decoration. Pair every colour with a text label or a legend, and never rely on colour alone.
3. Use ink text on pastel backgrounds. Never use white text on pastels.
4. Hierarchy comes from size and weight, not colour. Muted grey is for secondary information only.
5. A typical page starts with a title, then a row of stat tiles (label, big number, optional muted sub-line), then detail panels.
6. Put long detail in collapsible sections. The summary line shows a bold title plus a muted "· count" note.
7. Meet WCAG AA contrast and keep the layout responsive: grids wrap on narrow screens and wide tables scroll horizontally.