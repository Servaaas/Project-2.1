# imports

import serial
from arduino_logger import log
from team_12_dataverwerking import dataverwerking
from team_12_fit_brekingsindex import find_n

# ---------------------------------------------------

# initialize serial interface
arduino= serial.Serial(port='COM7',baudrate=115200,timeout=0.1)

# start execution of first part of code string
log(arduino)
dataverwerking()