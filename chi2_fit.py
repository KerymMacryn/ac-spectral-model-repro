
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

pdg = {
    'e': 0.000511, 'mu': 0.10566, 'tau': 1.77686,
    'u': 0.0022, 'd': 0.0047, 's': 0.096, 'c': 1.27, 'b': 4.18, 't': 172.69
}
names = list(pdg.keys())
m = np.array([pdg[k] for k in names])
sigma = 0.01 * np.maximum(m, 1e-3)

def chi2_of_p(p, lam=0.0):
    y = m / max(p, 1e-6)
    res = (m - y*p)/sigma
    return np.sum(res**2) + lam*p**2

Ps = np.linspace(0.1, 300.0, 2000)
chis = np.array([chi2_of_p(p) for p in Ps])
best = np.argmin(chis)
p_best = Ps[best]
y_best = m / p_best

i = max(1, best-1); j = min(len(Ps)-2, best+1)
curvature = (chis[j]-2*chis[best]+chis[i]) / ((Ps[j]-Ps[best])**2)
sigma_p = np.sqrt(2/curvature) if curvature>0 else np.nan

cov = np.diag((sigma/ max(p_best,1e-6))**2)

fig, ax = plt.subplots(1,2, figsize=(9,4))
ax[0].plot(Ps, chis); ax[0].axvline(p_best, ls='--')
ax[0].set_xlabel('p (GeV)'); ax[0].set_ylabel('chi^2')
ax[0].set_title('Fit m_f = y_f p: p*={:.2f} +/- {:.2f} GeV'.format(p_best, sigma_p if np.isfinite(sigma_p) else 0))

im = ax[1].imshow(cov, origin='lower', aspect='auto')
ax[1].set_xticks(range(len(names))); ax[1].set_yticks(range(len(names)))
ax[1].set_xticklabels(names, rotation=90); ax[1].set_yticklabels(names)
ax[1].set_title('Fisher/Covariance (toy)')
fig.colorbar(im, ax=ax[1], fraction=0.046, pad=0.04)

Path('figs').mkdir(exist_ok=True, parents=True)
plt.tight_layout(); plt.savefig('figs/chi2_corner.pdf')
