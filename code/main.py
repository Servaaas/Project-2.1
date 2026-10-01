# imports

from innit import innit
from arduino_logger import log
from team_12_dataverwerking import dataverwerking
from team_12_fit_brekingsindex import find_n

# ---------------------------------------------------

# initialize serial interface
arduino= innit()

# start execution of first part of code string
log(arduino)