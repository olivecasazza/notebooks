from __future__ import annotations

import subprocess
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist" / "notebooks"
NOTEBOOKS = {
    "altair": ROOT / "content/pyodide/altair.py",
    "folium": ROOT / "content/pyodide/folium.py",
    "interactive-widgets": ROOT / "content/pyodide/interactive-widgets.py",
    "ipycanvas": ROOT / "content/pyodide/ipycanvas.py",
    "ipyleaflet": ROOT / "content/pyodide/ipyleaflet.py",
    "matplotlib": ROOT / "content/pyodide/matplotlib.py",
    "plotly": ROOT / "content/pyodide/plotly.py",
    "python": ROOT / "content/python.py",
    "renderers": ROOT / "content/pyodide/renderers.py",
    "parallelcoords": ROOT / "content/pyodide/wigglystuff/parallelcoords.py",
    "treemap": ROOT / "content/pyodide/wigglystuff/treemap.py",
    "polynomials": ROOT / "content/pyodide/wigglystuff/polynomials.py",
    "kinematics": ROOT / "content/SDSU-CS556-Workspace/a4/p4.py",
    "inverse-kinematic-approximations": ROOT / "content/SDSU-CS556-Workspace/a3/Assignment 3, Part 2.py",
    "pyb2d-tutorial": ROOT / "content/pyodide/pyb2d/0_tutorial.py",
    "pyb2d-color-mixing": ROOT / "content/pyodide/pyb2d/color_mixing.py",
    "pyb2d-angry-shapes": ROOT / "content/pyodide/pyb2d/games/angry_shapes.py",
    "pyb2d-billiard": ROOT / "content/pyodide/pyb2d/games/billiard.py",
    "pyb2d-goo": ROOT / "content/pyodide/pyb2d/games/goo.py",
    "pyb2d-rocket": ROOT / "content/pyodide/pyb2d/games/rocket.py",
    "pyb2d-gauss-machine": ROOT / "content/pyodide/pyb2d/gauss_machine.py",
    "pyb2d-newtons-cradle": ROOT / "content/pyodide/pyb2d/newtons_cradle.py",
}

INFO_THEME_CSS = r'''
<style>
:root {
  --slate-950: #09090b;
  --slate-900: #111114;
  --slate-800: #18181b;
  --slate-700: #27272a;
  --slate-600: #3f3f46;
  --slate-500: #71717a;
  --slate-300: #d4d4d8;
  --slate-200: #e4e4e7;
  --pink-400: #f472b6;
  --pink-300: #f9a8d4;
  --cyan-300: #67e8f9;
}
html, body {
  background:
    radial-gradient(circle at top, rgba(244, 114, 182, 0.08), transparent 30%),
    linear-gradient(180deg, #09090b 0%, #111114 100%) !important;
  color: var(--slate-200) !important;
}
body, #root,
main,
[data-testid="app-container"],
[data-testid="read-mode-root"],
[data-testid="notebook-container"],
[data-testid="page"] {
  background: transparent !important;
}
body, h1, h2, h3, h4, h5, h6, p, li, span, label, div {
  color: var(--slate-200) !important;
}
a { color: var(--pink-300) !important; }
a:hover { color: var(--cyan-300) !important; }
.marimo-cell,
[data-testid="cell"] {
  background: rgba(24, 24, 27, 0.72) !important;
  border: 1px solid rgba(244, 114, 182, 0.16) !important;
  border-radius: 16px !important;
  backdrop-filter: blur(14px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.28);
}
[data-testid="output-area"],
[data-testid="cell-output"] {
  background: transparent !important;
}
button { border-radius: 10px !important; }
code, pre {
  background: rgba(39, 39, 42, 0.82) !important;
}
</style>
'''


def export_notebook(source: Path, output: Path) -> None:
    subprocess.run(
        [
            "marimo",
            "export",
            "html-wasm",
            str(source),
            "-o",
            str(output),
            "--mode",
            "run",
            "--no-show-code",
        ],
        check=True,
        cwd=ROOT,
    )


def patch_html(output: Path) -> None:
    html = output.read_text()
    html = html.replace('"theme": "light"', '"theme": "dark"')
    html = html.replace('</head>', f'{INFO_THEME_CSS}\n</head>', 1)
    output.write_text(html)


def write_index() -> None:
    cards = []
    for name in NOTEBOOKS:
        title = name.replace('-', ' ').title()
        cards.append(
            f'<a class="card" href="./notebooks/{escape(name)}.html">'
            f'<h2>{escape(title)}</h2>'
            f'<p>Open interactive marimo notebook</p>'
            '</a>'
        )

    index_html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>notebooks</title>
  {INFO_THEME_CSS}
  <style>
    body {{
      font-family: Inter, ui-sans-serif, system-ui, sans-serif;
      margin: 0;
      min-height: 100vh;
    }}
    .wrap {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 48px 24px 80px;
    }}
    h1 {{ font-size: 2.5rem; margin-bottom: 0.5rem; }}
    .sub {{ color: var(--slate-300); max-width: 70ch; margin-bottom: 2rem; }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
    }}
    .card {{
      display: block;
      text-decoration: none;
      padding: 20px;
      background: rgba(24, 24, 27, 0.72);
      border: 1px solid rgba(244, 114, 182, 0.16);
      border-radius: 16px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.28);
      backdrop-filter: blur(14px);
    }}
    .card:hover {{ border-color: rgba(103, 232, 249, 0.35); transform: translateY(-1px); }}
    .card h2 {{ margin: 0 0 0.5rem; font-size: 1.1rem; }}
    .card p {{ margin: 0; color: var(--slate-300) !important; }}
  </style>
</head>
<body>
  <main class="wrap">
    <h1>notebooks</h1>
    <p class="sub">Interactive browser-native Python notebooks published as marimo WASM apps. Legacy non-Python notebooks are not yet ported.</p>
    <div class="grid">{''.join(cards)}</div>
  </main>
</body>
</html>'''
    (ROOT / 'dist' / 'index.html').write_text(index_html)


def main() -> None:
    DIST.mkdir(parents=True, exist_ok=True)
    for name, source in NOTEBOOKS.items():
        output = DIST / f"{name}.html"
        export_notebook(source, output)
        patch_html(output)
    write_index()


if __name__ == "__main__":
    main()
