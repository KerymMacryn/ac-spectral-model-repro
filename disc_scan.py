
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from pathlib import Path

p = sp.symbols('p', real=True)
a, b, c = sp.symbols('a b c', real=True)

V_poly = a*p**4 + b*p**3 + c*p**2
Vp = sp.diff(V_poly, p)
Vpp = sp.diff(Vp, p)

Disc = sp.resultant(Vp, Vpp, p)

def disc_val(a_, b_, c_):
    return float(Disc.subs({a:a_, b:b_, c:c_}))

A = np.linspace(0.1, 1.0, 60)
B = np.linspace(-1.0, 1.0, 60)
C = np.linspace(-0.5, 0.8, 60)
c0 = float(np.median(C))

Z = np.zeros((len(A), len(B)))
for i, ai in enumerate(A):
    for j, bj in enumerate(B):
        try:
            dv = disc_val(ai, bj, c0)
        except Exception:
            dv = np.nan
        Z[i, j] = dv

safe = (Z > 0).astype(float)

fig = plt.figure(figsize=(6,5))
plt.imshow(safe, origin='lower', extent=[B.min(), B.max(), A.min(), A.max()], aspect='auto')
plt.xlabel('b'); plt.ylabel('a')
plt.title('Safe region (Disc(V\') > 0) at c={:.3f}'.format(c0))
plt.colorbar(label='Safe (1) / Unsafe (0)')
Path('figs').mkdir(exist_ok=True, parents=True)
plt.tight_layout(); plt.savefig('figs/discriminant_map.pdf')
