# imports

import serial

# -----------------------------------------------------------------

def innit():
    # initialising serial comunication with arduino
    arduino= serial.Serial(port='COM7',baudrate=115200,timeout=1)
    return arduino