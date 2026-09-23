import numpy as np
import pyvisa
import csv

timescale= 0.5

rm = pyvisa.ResourceManager()
print(rm.list_resources())

scope = rm.open_resource("USB0::0x1AB1::0x04B0::DS2D241401048::INSTR")
scope.timeout = 10000

print(scope.query("*IDN?"))

# Select channel
scope.write(":WAV:SOUR CHAN1")

# Ask for waveform data
scope.write(":WAV:FORM BYTE")
scope.write(":WAV:MODE NORM")
scope.write(f':TIMebase:MAIN:SCALe {timescale}')

data = scope.query_binary_values(
    ":WAV:DATA?",
    datatype="B",
    container=list
)

pre = scope.query_ascii_values(":WAV:PRE?")

x_increment = pre[4]
x_origin    = pre[5]
x_reference = pre[6]

time = x_origin + (np.arange(len(data)) - x_reference) * x_increment

# Save raw samples
with open("data//data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['time', 'sample'])
    for i in range(len(time)):
        writer.writerow([time[i],data[i]])

print(f"Saved {len(data)} samples")