"""Render element preview images from the real element CSS.

Usage:  python elements/_preview/render.py

Every elements/<group>/<name>.html is screenshotted to <name>.png next to it.
Each preview page links its own <name>.css, so re-running this after editing
the CSS keeps the images in the .md docs in sync with the code.

Requires Google Chrome or Microsoft Edge (headless). Pillow is optional: if it
is installed, the screenshots are trimmed to the preview content.
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ELEMENTS = Path(__file__).resolve().parent.parent
SCALE = 2                     # device pixel ratio for crisp images
VIEWPORT = (900, 900)         # just larger than any preview; output is trimmed
PAGE_BG = (0xF4, 0xF4, 0xF5)  # matches html/body background in preview.css
MARGIN = 12 * SCALE

# Chrome first: headless Edge can hang on managed corporate machines.
BROWSERS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "google-chrome", "chromium", "chrome", "msedge",
]


def find_browser():
    for b in BROWSERS:
        if Path(b).exists() or shutil.which(b):
            return b
    sys.exit("No Chrome/Edge found for headless rendering.")


def trim(png: Path):
    try:
        from PIL import Image, ImageChops
    except ImportError:
        return
    img = Image.open(png).convert("RGB")
    box = ImageChops.difference(img, Image.new("RGB", img.size, PAGE_BG)).getbbox()
    if box:
        l, t, r, b = box
        img.crop((max(l - MARGIN, 0), max(t - MARGIN, 0),
                  min(r + MARGIN, img.width), min(b + MARGIN, img.height))).save(png)


def main():
    browser = find_browser()
    pages = sorted(p for p in ELEMENTS.glob("*/*.html") if not p.parent.name.startswith("_"))
    # Separate throwaway profile so headless doesn't attach to an open browser window.
    with tempfile.TemporaryDirectory() as profile:
        for html in pages:
            out = html.with_suffix(".png")
            subprocess.run([
                browser, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                "--no-first-run", "--no-default-browser-check",
                f"--user-data-dir={profile}",
                f"--force-device-scale-factor={SCALE}",
                f"--window-size={VIEWPORT[0]},{VIEWPORT[1]}",
                f"--screenshot={out}",
                html.as_uri(),
            ], check=True, timeout=60,
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            trim(out)
            print(f"rendered {out.relative_to(ELEMENTS)}")


if __name__ == "__main__":
    main()
