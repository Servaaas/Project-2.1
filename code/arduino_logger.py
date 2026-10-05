# imports

import sys
import numpy as np
import csv
from time import sleep

# constants

file= r"data\data.csv"

# --------------------------------------------------------------------

def log(arduino,file=file):
    try:
        # writing execute code to arduino
        arduino.write(bytes('0','utf-8'))

        # constantly read the arduino output and write to data arrays until keyboard interrupt occours
        time= np.array([])
        volt= np.array([])
        print("starting logging")
        while True:
            if arduino.in_waiting > 0:
                inp= arduino.readline().decode('utf-8').strip().split(',')
                if inp[0] == "EXIT_0":
                    # when arduino finished logging write all data into csv
                    with open(file,"w",newline='') as f:
                        writer= csv.writer(f)
                        writer.writerow(["Time (s)","Voltage (V)"])
                        for i in range(len(time)):
                            writer.writerow([time[i],volt[i]])
                    
                    #close arduino serial connection and exit function
                    arduino.close()
                    break
                else:
                    time= np.append(time,inp[0])
                    volt= np.append(volt,inp[1])
    except KeyboardInterrupt:
        # write cease execution code to arduino
        arduino.write(bytes('1','utf-8'))
        sleep(0.1)
        print("runtime error")
        arduino.close()
        return sys.exit()