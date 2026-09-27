import numpy as np
import pandas as pd
import csv as c
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def dataverwerking(csv,window):
    try:
        data=pd.read_csv(csv)
        t= data['Time (s)'].values
        V= data['Voltage (V)'].values
        
        V_rms= np.sqrt(np.convolve(V**2, np.ones(window)/window, 'valid'))

        plt.plot(t,V_rms)
        plt.show()

        V_avr= np.average(V_rms)
        V_std= np.std(V_rms)

        treshold= V_avr + V_std
        peaks, _ = find_peaks(V_rms, height=treshold)
        peak_t = t[peaks]

        N= np.zeros_like(peak_t)
        N[0]= 1
        with open(r"data\peaks.csv","w",newline='') as f:
            writer= c.writer(f)
            writer.writerow(["N (-)","Time (s)"])
            for i in range(len(N)):
                N[i+1]= N[i] + 1
                writer.writerow([N[i],peak_t[i]])

        print(peak_t)
    finally:
        print('peak detection executed')

dataverwerking(r"data\data.csv",1)