{
  description = "JupyterLite environment for notebooks";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            (pkgs.python3.withPackages (ps: with pkgs.python3Packages; [
              # Core
              jupyterlite-core
              jupyterlab
              
              # Kernels
              jupyterlite-pyodide-kernel
              jupyterlite-javascript-kernel
              
              # Dependencies mapped from requirements.txt
              ipywidgets
              ipyevents
              ipympl
              ipycanvas
              ipyleaflet
              plotly
              bqplot
              matplotlib
              numpy
              pillow
              scipy
              scikit-image
              scikit-learn
              pandas
              sympy
              tornado
              requests
              psutil
            ]))
            pkgs.nodejs_20
          ];

          shellHook = ''
            echo "JupyterLite environment ready!"
            echo "Run 'jupyter lite build --contents content --output-dir dist' to build."
            echo "Run 'jupyter lite serve --contents content --output-dir dist' to serve locally."
          '';
        };
      }
    );
}
