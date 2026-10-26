# imports

import numpy as np
import pandas as pd
import csv as c
from find_peaks import find_peaks_numpy

# constants

file= r"data\data.csv"
window= 2000
theta= 2.5

# ------------------------------------------------------

def dataverwerking(N_0,csv=file,window=window,theta=theta):
    try:
        # reading data csv
        data=pd.read_csv(csv)
        t= data['Time (s)'].values
        V= data['Voltage (V)'].values

        # rolling rms
        V_rms= np.sqrt(np.convolve(V**2, np.ones(window)/window, 'valid'))

        # executing peak detection and cumputing N
        peaks= find_peaks_numpy(V_rms,prominence=0.01)
        dN= len(peaks)

        # define the total fringes N and sigma
        N= dN + N_0
        Sigma= N / 20

        # writing the found N to csv file
        with open(r"data\peaks.csv","a",newline='') as f:
            writer= c.writer(f)
            writer.writerow([theta,N,Sigma])

        # printing peaks for sanity checking
        print(peaks)

        # returning the previous amount of fringes
        return N
    finally:
        print('peak detection executed')