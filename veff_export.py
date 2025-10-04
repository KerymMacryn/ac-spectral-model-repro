# veff_export.py
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import json

rng_seed = 7
np.random.seed(rng_seed)

# Ejemplo simple: Veff ~ a p^4 + b p^3 + c p^2
p = np.linspace(0, 600, 800)
a, b, c = 0.1, -3.0, 1.0
V = a*p**4 + b*p**3 + c*p**2

Path('figs').mkdir(exist_ok=True)

np.savetxt('figs/veff_benchmark.csv', np.column_stack((p,V)), delimiter=',', header='p,Veff', comments='')
with open('figs/veff_meta.json','w') as f:
    json.dump({'seed': rng_seed, 'a': a, 'b': b, 'c': c}, f, indent=2)

plt.figure(figsize=(6,4))
plt.plot(p, V)
plt.xlabel('p [GeV]')
plt.ylabel('V_eff(p)')
plt.title('Benchmark Effective Potential')
plt.grid(True)
plt.tight_layout()
plt.savefig('figs/veff_benchmark.pdf')
print("Saved figs/veff_benchmark.pdf")
