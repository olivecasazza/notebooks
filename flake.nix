{
  description = "JupyterLite & Marimo environment";

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
            pkgs.uv
            pkgs.python311
            pkgs.nodejs_20
          ];

          shellHook = ''
            export UV_PROJECT_ENVIRONMENT=$PWD/.venv
            if [ ! -d .venv ]; then
              uv venv
              uv pip install -r requirements.txt
            fi
            echo "Environment ready! Use 'uv run marimo ...' or 'uv run jupyter lite ...'"
          '';
        };
      }
    );
}