
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def Omega_sw(f, alpha=0.1, betaH=100, vw=0.6, Tn=100):
    fp = 1e-3 * betaH * (Tn/100.0) 
    x = f/fp
    Omega0 = 1e-11 * (alpha/(1+alpha))**2 * (vw**2) * (100.0/betaH)
    return Omega0 * (x**3) / (1 + 3*(x**2))**(3.5)

def Omega_env(f, alpha=0.1, betaH=100, vw=0.6, Tn=100):
    fp = 3e-3 * betaH * (Tn/100.0)
    x = f/fp
    Omega0 = 1e-12 * (alpha/(1+alpha))**2 * (100.0/betaH)
    return Omega0 * (x**2) / (1 + x)**4

f = np.logspace(-4, 0, 400)
Omega = Omega_sw(f) + Omega_env(f)

plt.figure(figsize=(6,4))
plt.loglog(f, Omega)
plt.xlabel('f [Hz]'); plt.ylabel('Omega_GW h^2')
plt.title('GW Spectrum (sound-wave + envelope)')
plt.grid(True, which='both', ls=':')
Path('figs').mkdir(exist_ok=True, parents=True)
plt.tight_layout(); plt.savefig('figs/gw_spectrum.pdf')
