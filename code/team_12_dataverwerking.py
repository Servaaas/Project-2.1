# imports

import numpy as np
import pandas as pd
import csv as c
# import matplotlib.pyplot as plt

# constants

file= r"data\data.csv"
window= 1
theta= 2.5

# ------------------------------------------------------

def dataverwerking(csv=file,window=window,theta=theta):
    try:
        # reading data csv
        data=pd.read_csv(csv)
        t= data['Time (s)'].values
        V= data['Voltage (V)'].values

        # rolling rms
        V_rms= np.sqrt(np.convolve(V**2, np.ones(window)/window, 'valid'))

        # plotting data for sanity checking
        # plt.plot(t,V_rms)
        # plt.show()

        # finding a peak treshold
        V_avr= np.average(V_rms)
        V_std= np.std(V_rms)
        treshold= V_avr + V_std

        # executing peak detection and cumputing N
        peaks = (V_rms[1:-1] > V_rms[:-2]) & (V_rms[1:-1] > V_rms[2:])
        peak_indices = np.where(peaks)[0] + 1
        peak_indices = peak_indices[peaks[peak_indices] >= treshold]
        N= len(peak_indices)

        # writing the found N to csv file
        with open(r"data\peaks.csv","a",newline='') as f:
            writer= c.writer(f)
            writer.writerow([theta,N])

        # printing peaks for sanity checking
        print(peak_indices)
    finally:
        print('peak detection executed')