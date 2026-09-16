import csv
import pyvisa

# 1. Initialize the VISA Resource Manager using the pure-Python backend
rm = pyvisa.ResourceManager()

# List connected resources to find your scope's address
print("Connected devices:", rm.list_resources())

# 2. Connect to the Rigol DS2102A (replace with your actual resource string)
# Example USB string looks like: 'USB0::0x1AB1::0x04B0::DS2AXXXXXXXXXX::INSTR'
scope_address = "USB0::0x1AB1::0x04B0::DS2D242101472::INSTR"
scope = rm.open_resource(scope_address)
scope.timeout = 10000  # 10 seconds timeout for larger data dumps

# Verify connection
print("Connected to:", scope.query("*IDN?").strip())

# 3. Configure the Waveform Data Format
scope.write(":WAVeform:SOURce CHANnel1")
scope.write(":WAVeform:MODE NORMal")  # Use 'RAW' for deep memory if stopped
scope.write(":WAVeform:FORMat ASCii")

# 4. Request the waveform preamble data to calculate the time axis
# Preamble returns 10 values containing: format, type, points, count, xincrement, xorigin, xreference, yincrement, yorigin, yreference
preamble = scope.query(":WAVeform:PREamble?").split(",")
x_increment = float(preamble[4])
x_origin = float(preamble[5])
x_reference = float(preamble[6])

# 5. Fetch raw ASCII data values
print("Fetching waveform data...")
raw_data = scope.query(":WAVeform:DATA?")

# Clean Rigol's TMC block header (usually something like #9000001200...)
# and parse comma-separated voltage values
voltages = [float(v) for v in raw_data.split(",") if v.strip()]

# 6. Calculate Time-steps and Save to CSV
output_file = "ds2102a_output.csv"
with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Time (s)", "Voltage (V)"])  # Header

    for i, volt in enumerate(voltages):
        # Calculate time relative to the trigger point
        time_val = (i - x_reference) * x_increment + x_origin
        writer.writerow([time_val, volt])

print(f"Successfully exported {len(voltages)} points to {output_file}")

# Close the session cleanly
scope.close()
