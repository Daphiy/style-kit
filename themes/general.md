# General design rules (all themes)

These rules apply to every theme. Read this file together with the chosen theme's `design.md` whenever you build a UI. If a theme's `design.md` contradicts a rule here, follow this file, unless `design.md` explicitly says it overrides that rule.

## Text clearance inside shapes

Text must never touch or come close to the edge of the shape it sits in (card, bubble, pill, badge, button, banner, header, etc.).

- Keep **at least 2px of clear space** between every glyph and the nearest edge of its shape, measured to the **visible edge** (the curve), not to the bounding box.
- Watch this especially for **non-rectangular shapes**: large or asymmetric `border-radius` (e.g. `36px 36px 36px 100px`), pills, circles and blobs. A rounded corner cuts into the box, so padding that is fine for a square box can leave text touching or overlapping the curve.
- When a corner has radius `r`, the curve reaches about `0.3 × r` inward at the diagonal. So for text that runs near that corner, set the padding on the adjacent sides to at least `0.3 × r + 2px`, or keep text out of the corner area (e.g. extra `padding-left` / `padding-bottom` next to a large bottom-left radius).
- Check every line of text, including the first and last line and long lines that run toward a curved side. Large display headings need the same clearance as body text.
- After building, look at the rendered result and verify the clearance. If text is close to a curve, increase padding or reduce the radius on that corner.

## Element Alignment 

Elements, e.g. boxes or bubbles, that appear in the same row should be aligned in height. at minimum, their top edge should be the same height. if they are similar in content, e.g. if both show diagrams, the bottom edge should also align even if the content inside one is a bit shorter than the other. 

## Statistical Reports 

Use this section only if you are generating a numerical report, otherwise ignore. 

#### Design 
1. For stacked charts the stacks need to be square with no spaces between them. 

#### Content 
You can use your discretion to select the best charts to provide the requested results. Below are general rules of thumb that are to be treated as recommendations. 

1. To compare distributions across categories, e.g. latency across models, you can use 
a) a strip plot (jitter plot) with median, 75% and 25% plotted on top. namely, a box plot laid over jittered points. 
b) a violin plot if the distribution matters more than percentiles 
2. histograms are useful to present a distribution. you can use them to compare distributions between 1-3 groups as well. use only if you have enough data points. 
3. when comparing two variables against each other, or how an instance scores against two variables, scatter chart can be used. For example, to test correlation between item price and number of purchases, or to plot the tradeoff between model latency and model accuracy of specific AI models. In the second case also add a label for the instances (e.g. models) that are being evaluated. 
4. Pie charts are a simple, useful chart if you want to present the distribution of a caetgorical variable with <10 or so categories. e.g. how many of the sold items were jewlery, home decor or accessories, or number of male vs female employees. 
5. A line chart uses demonstrates changes in value, usually over time, of one or more variables. 
5. Area charts, similar to line charts but with added area shading, are useful in representing cumulated totals using numbers or percentages (stacked area charts in this case) over time. Can be used to compare the progression of groups. 