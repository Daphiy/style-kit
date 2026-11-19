## Colors 

Page background: white #FFFFFF and if there isa second panel, make it very light grey #F6F6F7
Text color: black #000000 

Elements may be in the form of cards which are college-blue-greylight: #C8D8DF, with a thin navy blue #0A2747  border or a thin medium blue: #5881AF border. 

Theme colors
Navy #0A2747 for primary buttons and card borders.

Medium blue #5881AF for secondary card borders, focus borders and the dashed lines.

Muted red #C76666 to signal or highlight certain elements with a minimalistic dot or something of the sort. use for small touches of color not large elements. can also be used for dashed lines if fitting. 

--college-red: #CF4F4F;
   --college-reddish: #C76666;

   --college-pink: #FFC3B4;
   --college-pinkish: #ED9681;
   --college-pinkish-lighter: #FBB9A8;
   --college-lightpink: #FFE6DF;
   
   --college-ochre: #D8AB31;
   --college-yellow: #F9E789;
   --college-yellowish: #E8D24A;
   --college-light-yellow: #FFF8C4;
   
   --college-blue: #5099DC;
   --college-blueish: #5881AF;
   --college-blue-navy: #0A2747;
   --college-blue-light: #DFF0F8;
  --college-blue-greylight #DCEBF8	
   
   --college-green: #89C889;
   --college-green: #D8F2BF;
   --college-green: #E1F5CE;

## Shapes 

#### Elements
page elements are rectangles, with straight corners. 
no rounded corners other than for toggle. 

Corners: square everywhere, on cards, buttons, inputs and filter chips. There are no shadows on cards.

#### Dashed Lines 
separators use thin dashed lines in blue #5881AF

The two dashed line styles

Both are drawn with a CSS gradient background rather than a border-style: dashed, so the dash lengths stay exact. Each line is 1px high and runs edge to edge: the element uses a negative side margin equal to the card's padding, then adds that padding back.

A. Dash-dot line (single), under the card titles. The pattern repeats every 15px: a 7px dash, a 3px gap, a 2px dot, then a 3px gap.
background: linear-gradient(to right,
    #5881AF 0 7px, transparent 7px 10px,
    #5881AF 10px 12px, transparent 12px)
  left bottom / 15px 1px repeat-x;
B. Double dashed line, the separators in the popup. Two parallel dashed lines sit 3px apart, so the element is 4px tall with a line on its top row and its bottom row. The pattern repeats every 12px: a 7px dash, then a 5px gap. The dashes of the two lines are aligned, not staggered.
height: 4px;
background:
  linear-gradient(to right, #5881AF 7px, transparent 7px) left top    / 12px 1px repeat-x,
  linear-gradient(to right, #5881AF 7px, transparent 7px) left bottom / 12px 1px repeat-x;
#### Dots 

Use circular color dots to describe categories and labels if relevant. 

## Fonts 
Headings: pick one of three (only one)

Option	Look	Font	Weight	Case	Size
1. Varsity	blocky college-jersey lettering	Graduate	400 (its only weight)	all capitals (text-transform: uppercase, letter spacing about .5px)	34px page headings, 32px popup titles
2. Slab	sturdy slab serif, like typewriter or letterpress	Rokkitt	400	normal upper and lower case	42px page headings, 38px popup titles, line height 1.15
3. Elegant	classic book serif	Lora	400	normal upper and lower case	32–34px (34px page headings, 32px popup titles), line height 1.2
All three load from Google Fonts. Keep Lora, then Georgia, then serif as the fallback after the chosen font.

All other text is IBM Plex Sans at 14px with a 16px line height, in black.

## Style Instructions 

The page is minimalistic and editorial, like square post-it notes on white paper.


## General UI Guidelines 

