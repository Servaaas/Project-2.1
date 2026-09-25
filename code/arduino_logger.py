import numpy as np
import csv
import serial
from time import sleep

try:
    arduino= serial.Serial(port='COM7',baudrate=115200,timeout=1)
    sleep(1)

    arduino.write(bytes('0','utf-8'))
    sleep(0.1)

    time= np.array([])
    volt= np.array([])
    print("starting logging")
    while True:
        if arduino.in_waiting > 0:
            inp= arduino.readline().decode('utf-8').strip().split(',')
            time= np.append(time,inp[0])
            volt= np.append(volt,inp[1])
except KeyboardInterrupt:
    arduino.write(bytes('1','utf-8'))
    sleep(0.1)
    while arduino.in_waiting > 0:
        exit= arduino.readline().decode('utf-8').strip()
    if exit == 'EXIT_0':
        with open(r"data\data.csv","w",newline='') as f:
            writer= csv.writer(f)
            writer.writerow(["Time (s)","Voltage (V)"])
            for i in range(len(time)):
                writer.writerow([time[i],volt[i]])
            arduino.close()
    else:
        print("arduino runtime error")
        arduino.close()