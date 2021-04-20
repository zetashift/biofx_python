{ pkgs ? import <nixpkgs> {} }:

with pkgs;

let
  packageOverrides = pkgs.callPackage ./python-packages.nix {  };
  python = pkgs.python39.override { inherit packageOverrides; };

in mkShell {
  buildInputs = [ python ];
}
