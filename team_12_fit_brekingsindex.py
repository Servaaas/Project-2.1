import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from functools import partial

Data= pd.read_csv("team_12_data.csv")

I= np.radians(Data['hoek_graden'].values)
N= Data['aantal_franjes'].values
Sigma= Data['onzekerheid_N'].values

d= 5E-3
ld= 632.8E-9

def model(i,n,d,ld):
    return (2*d)/ld*(np.sqrt(n**2 - np.sin(i)**2)-np.cos(i) + (1-n))
model_N= partial(model,d=d,ld=ld)

popt,pcov = curve_fit(model_N,I,N,sigma=Sigma)
print(popt[0])

plt.errorbar(I,N,yerr=Sigma,fmt='o')
plt.plot(I,model_N(I,popt[0]))
plt.xlabel('hoek van inval (rad)')
plt.ylabel('aantal franjes (-)')
plt.show()