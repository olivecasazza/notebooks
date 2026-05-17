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
            pkgs.python3
            pkgs.python3.pkgs.pip
            pkgs.python3.pkgs.virtualenv
            pkgs.nodejs_20
          ];

          shellHook = ''
            python -m venv .venv
            source .venv/bin/activate
            pip install -r requirements.txt
            echo "JupyterLite environment ready!"
            echo "Run 'jupyter lite build --contents content --output-dir dist' to build."
            echo "Run 'jupyter lite serve --contents content --output-dir dist' to serve locally."
          '';
        };
      }
    );
}
