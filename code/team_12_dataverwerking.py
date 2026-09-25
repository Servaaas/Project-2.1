import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def dataverwerking(csv):
    try:
        data=pd.read_csv(csv)
        t= data['Time (s)'].values
        V= data['Voltage (V)'].values

        plt.scatter(t,V)
        plt.show()
    finally:
        print('done')

dataverwerking(r"data\data.csv")