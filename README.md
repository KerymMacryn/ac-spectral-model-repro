
# Minimal Reproducibility Pack (JHEP submission)

This pack contains reference scripts and a notebook to reproduce the **benchmark figures** referenced in the manuscript.

## Contents
- `veff.ipynb` — Symbolic & numerical computation of the one-/two-loop effective potential for the AC model and plots of V_eff(p).
- `disc_scan.py` — Discriminant map of V'(p) across a parameter grid; exports `figs/discriminant_map.pdf`.
- `chi2_fit.py` — Simple chi^2 fit to PDG fermion masses in the toy relation m_f(p)=y_f p; exports `figs/chi2_corner.pdf`.
- `nucleation_gw.py` — Gravitational-wave spectrum from a first-order phase transition (sound-wave + envelope templates); exports `figs/gw_spectrum.pdf`.
- `figs/` — Output directory for figures.

## Quick start
1. Install Python >=3.10 and `pip install sympy numpy mpmath matplotlib`.
2. Run:
   ```bash
   python disc_scan.py
   python chi2_fit.py
   python nucleation_gw.py
   ```
3. Open `veff.ipynb` in Jupyter and run all cells to produce `figs/veff_benchmark.pdf`.
