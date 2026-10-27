# imports

import serial
from time import sleep
from arduino_logger import log
from team_12_dataverwerking import dataverwerking
from team_12_fit_brekingsindex import find_n

# constants

N_0= 0
step_a= 1.8

# ---------------------------------------------------

# initialize serial interface
arduino= serial.Serial(port='COM7',baudrate=115200,timeout=0.1)
arduino.set_buffer_size(rx_size=1048576)

# execute arduino code and compute N 4 times
for i in range(2,6):
    log(arduino)
    N_0= dataverwerking(N_0=N_0,theta=step_a*i)

# running datafit to find n
find_n(df="data\\peaks.csv")