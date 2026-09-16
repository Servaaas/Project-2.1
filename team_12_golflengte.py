import numpy as np
import matplotlib as plt

N = np.array([106, 121, 95, 111]) # aantal getelde franjes
d = 0.02778 # verschuiving spiegel in mm

λ = ((2 * d) / N) * 1_000_000

λ_gem = np.mean(λ) 
σ = np.std(λ,ddof=1)

print("Golflengtes per meting (nm):", np.round(λ, 1))
print("Gemiddelde golflengte (nm):", np.round(λ_gem,1))
print("Standaardafwijking (nm):", np.round(σ,1))