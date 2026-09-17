import numpy as np
import matplotlib.pyplot as plt

N = np.array([106, 121, 95, 111]) # aantal getelde franjes
d = 0.02778 # verschuiving spiegel in mm
λ = ((2 * d) / N) * 1_000_000
λ_gem = np.mean(λ) 
σ = np.std(λ,ddof=1)

print("Golflengtes per meting (nm):", np.round(λ, 1))
print("Gemiddelde golflengte (nm):", np.round(λ_gem,1))
print("Standaardafwijking (nm):", np.round(σ,1))

plt.figure(figsize=(8, 5))
plt.scatter(N, λ, color='darkblue', zorder=5, label='Individuele metingen')
plt.axhline(λ_gem, color='crimson', linestyle='--', linewidth=2, label=f'Gemiddelde ({λ_gem:.1f} nm)')
plt.axhspan(λ_gem - σ, λ_gem + σ, color='crimson', alpha=0.15, label=f'Standaardafwijking (± {σ:.1f} nm)')
plt.xticks(N, ['Meting 1', 'Meting 2', 'Meting 3', 'Meting 4'])
plt.ylabel('Berekende golflengte $\lambda$ (nm)', fontsize=12)
plt.title('Michelson Interferometer: Golflengte per meting', fontsize=14, fontweight='bold')
plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.legend(loc='upper right')
plt.ylim(λ_gem - 2*σ, λ_gem + 2*σ)
plt.show()