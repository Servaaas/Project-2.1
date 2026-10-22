# imports

import serial
from time import sleep
from arduino_logger import log
from team_12_dataverwerking import dataverwerking
from team_12_fit_brekingsindex import find_n

# constants

N_0= 0
step_a= 3.6

# ---------------------------------------------------

# initialize serial interface
arduino= serial.Serial(port='COM7',baudrate=115200,timeout=0.1)
arduino.set_buffer_size(rx_size=1048576)

# start execution of first part of code string
for i in range(1,5):
    log(arduino)
    N_0= dataverwerking(N_0=N_0,theta=step_a*i)

# running datafit to find n
find_n(df="data\\peaks.csv")