"""Palettes defined in Python, built from the named colors in colors.css.

Any color in a palette can be given as:
  - a name from colors.css     "swa-info-blue-dark"  (leading "--" optional)
  - a hex value                "#1a2b3c"             (no name needed)

A palette has background/text fields (some optional) plus `colors`,
an ordered, unnamed list, e.g. chart series colors.

Run `python palettes.py` to validate every palette and write palettes.md:
instructions Claude follows when styling reports, websites and other UI.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, model_validator

HERE = Path(__file__).parent
COLORS_CSS = HERE / "colors.css"
PALETTES_MD = HERE / "palettes.md"

_VAR_RE = re.compile(r"--([\w-]+)\s*:\s*([^;]+);")
_REF_RE = re.compile(r"var\(--([\w-]+)\)")
_HEX_RE = re.compile(r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})")


def load_colors(path: Path = COLORS_CSS) -> dict[str, str]:
    """Read `--name: value;` lines from colors.css into {name: value}.

    var(--other) references inside a value are replaced with the other
    color's value, so every entry can be read on its own.
    """
    text = re.sub(r"/\*.*?\*/", "", path.read_text(encoding="utf-8"), flags=re.DOTALL)
    colors: dict[str, str] = {}
    for name, value in _VAR_RE.findall(text):
        if name in colors:
            print(f"warning: --{name} is defined more than once in colors.css; the last one wins")
        colors[name] = value.strip()
    for name, value in colors.items():
        colors[name] = _REF_RE.sub(lambda m: colors.get(m.group(1), m.group(0)), value)
    return colors


COLORS = load_colors()


class Color(BaseModel):
    """One color: a value, plus its colors.css name if it has one."""

    model_config = ConfigDict(frozen=True)

    value: str
    name: str | None = None

    @model_validator(mode="before")
    @classmethod
    def _from_string(cls, data: Any) -> Any:
        if not isinstance(data, str):
            return data
        ref = data.strip()
        name = ref.removeprefix("--")
        if name in COLORS:
            return {"name": name, "value": COLORS[name]}
        if _HEX_RE.fullmatch(ref):
            return {"value": ref.upper()}
        raise ValueError(f"{data!r} is neither a color name in colors.css nor a hex value")

    def __str__(self) -> str:
        return self.value


class Palette(BaseModel):
    name: str
    description: str = ""
    background_default: Color = Field(description="Main page background")
    background_darkmode: Color | None = Field(None, description="Page background in dark mode")
    background_secondary: Color | None = Field(None, description="Cards, panels, table headers, sidebars")
    text_default: Color = Field(description="Body text and headings")
    text_darkmode: Color | None = Field(None, description="Body text in dark mode")
    text_highlights: Color | None = Field(None, description="Links, key numbers, emphasis")
    colors: list[Color] = Field([], description="Data and accent colors, used in this order (e.g. chart series)")

    def to_md(self) -> str:
        out = [f"## {self.name}", ""]
        if self.description:
            out += [self.description, ""]
        out += ["| Use | Color | Value |", "|---|---|---|"]
        for field, info in type(self).model_fields.items():
            value = getattr(self, field)
            if isinstance(value, Color):
                label = field.replace("_", " ").capitalize()
                out.append(f"| **{label}**: {info.description} | {_name(value)} | `{value}` |")
        if self.colors:
            out += ["", f"**Colors**: {type(self).model_fields['colors'].description}:", ""]
            out += [f"{i}. {_name(c)} `{c}`" for i, c in enumerate(self.colors, 1)]
        return "\n".join(out)


def _name(color: Color) -> str:
    return f"`{color.name}`" if color.name else "-"


# ==========================================================================
# Palettes: edit here. The first one is the default.
# ==========================================================================

PALETTES: list[Palette] = [
    Palette(
        name="default",
        description="Swarovski brand palette. Use when no other palette is requested.",
        background_default="white",
        background_darkmode="swa-grey--900",
        background_secondary="swa-grey--50",
        text_default="swa-grey--900",
        text_darkmode="swa-grey--100",
        text_highlights="swa-info-blue-dark",
        colors=["swa-pink--100", "swa-blue--100", "swa-yellow--100", "swa-green--100"],
    ),
]


INSTRUCTIONS = """\
# Color palettes

Instructions for styling reports, websites, slides and other UI.

- Pick the palette the user asks for by name. If none is named, use the first one.
- Use the values exactly as listed. Don't invent new colors or tweak these ones.
- Use each color only for the job described next to it.
- Use the dark mode colors only when dark mode is asked for or when the output
  supports it (e.g. `prefers-color-scheme: dark` on a web page).
- For charts and other data, use **Colors** in the order listed.
- Fields a palette leaves out aren't part of that palette, so don't fill them in.
"""


def write_md(palettes: list[Palette], path: Path = PALETTES_MD) -> None:
    note = "<!-- GENERATED by palettes.py. Edit palettes.py and run `python palettes.py`. -->\n\n"
    body = "\n\n".join(p.to_md() for p in palettes)
    path.write_text(note + INSTRUCTIONS + "\n" + body + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_md(PALETTES)
    print(f"{len(PALETTES)} palettes OK, wrote {PALETTES_MD.name}")
