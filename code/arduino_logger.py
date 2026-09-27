#inports

import numpy as np
import csv
import serial
from time import sleep
from team_12_dataverwerking import dataverwerking

# constants

file= r"data\data.csv"

# --------------------------------------------------------------------

def log(file=file):
    try:
        # initialising serial comunication with arduino
        arduino= serial.Serial(port='COM7',baudrate=115200,timeout=1)
        sleep(1)

        # writing execute code to arduino
        arduino.write(bytes('0','utf-8'))
        sleep(0.1)

        # constantly read the arduino output and write to data arrays until keyboard interrupt occours
        time= np.array([])
        volt= np.array([])
        print("starting logging")
        while True:
            if arduino.in_waiting > 0:
                inp= arduino.readline().decode('utf-8').strip().split(',')
                time= np.append(time,inp[0])
                volt= np.append(volt,inp[1])
    except KeyboardInterrupt:
        # write cease execution code to arduino
        arduino.write(bytes('1','utf-8'))
        sleep(0.1)

        # read the arduino output until last output is read. This will be the exit code if everything went well
        while arduino.in_waiting > 0:
            exit= arduino.readline().decode('utf-8').strip()

        # if the correct exit code is send continue code execution
        if exit == 'EXIT_0':
            #write all the data to data csv for dataverwerking
            with open(file,"w",newline='') as f:
                writer= csv.writer(f)
                writer.writerow(["Time (s)","Voltage (V)"])
                for i in range(len(time)):
                    writer.writerow([time[i],volt[i]])

            #close arduino serial connection and execute dataverwerking code
            arduino.close()
            dataverwerking()
        else:
            #catch runtime errors if exit code is not recieved
            print("arduino runtime error")
            arduino.close()