#!/usr/bin/env bash
set -euo pipefail

TEX="second_order_organization_admissible_trajectories.tex"
OUTDIR="build"
JOBNAME="${TEX%.tex}"

mkdir -p "$OUTDIR"

# Prefer latexmk if available (best UX)
if command -v latexmk >/dev/null 2>&1; then
  # -pdf: build PDF
  # -interaction=nonstopmode -halt-on-error: fail fast but keep useful log context
  # -file-line-error: clickable/greppable error locations
  # -synctex=1: editor sync support
  latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -synctex=1 \
    -outdir="$OUTDIR" \
    -jobname="$JOBNAME" \
    "$TEX"
else
  # Fallback: pdflatex twice for refs/figs
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -synctex=1 \
    -output-directory="$OUTDIR" \
    -jobname="$JOBNAME" \
    "$TEX"
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -synctex=1 \
    -output-directory="$OUTDIR" \
    -jobname="$JOBNAME" \
    "$TEX"
fi

echo
echo "Built:"
echo "  $OUTDIR/$JOBNAME.pdf"
