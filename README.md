# notebooks

Browser-native interactive notebooks for casazza.info.

This repository now publishes standalone marimo WASM apps to GitHub Pages.
The goal is a lightweight, app-like presentation surface for interactive Python
notebooks instead of shipping the full JupyterLite IDE.

Live site:
- https://olivecasazza.github.io/notebooks/

Current published demos:
- Parallel Coordinates
- Treemap
- Polynomials on the Complex Plane

Source layout:
- content/pyodide/wigglystuff/*.py — marimo notebooks exported as standalone apps
- content/pyodide/wigglystuff/*.ipynb — original notebook/source material kept for reference
- scripts/build_marimo_exports.py — build/export pipeline plus theme patching

Local development:
- nix develop
- uv pip install -r requirements.txt
- python scripts/build_marimo_exports.py

This produces static HTML/WASM artifacts in dist/notebooks/ ready for GitHub Pages.

Why marimo instead of JupyterLite:
- faster and cleaner notebook-as-app publishing
- better read-mode UX for embedded/public demos
- easier to theme to match the main info site
- less IDE chrome for users who just want the interactive artifact
