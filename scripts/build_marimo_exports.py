from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist" / "notebooks"
NOTEBOOKS = {
    "parallelcoords": ROOT / "content/pyodide/wigglystuff/parallelcoords.py",
    "treemap": ROOT / "content/pyodide/wigglystuff/treemap.py",
    "polynomials": ROOT / "content/pyodide/wigglystuff/polynomials.py",
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


def main() -> None:
    DIST.mkdir(parents=True, exist_ok=True)
    for name, source in NOTEBOOKS.items():
        output = DIST / f"{name}.html"
        export_notebook(source, output)
        patch_html(output)


if __name__ == "__main__":
    main()
