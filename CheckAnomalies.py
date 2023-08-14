import csv
import numpy as np

input_file = 'dummy_voltage_data_with_anomalies.csv'

mean_voltage = 230
voltage_range = 5

lower_bound = mean_voltage - voltage_range/2
upper_bound = mean_voltage + voltage_range/2


with open(input_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip header row
    anomalies = []
    for row in csvreader:
        timestamp, voltage = row
        voltage = float(voltage)
        if voltage < lower_bound or voltage > upper_bound:
            anomalies.append((timestamp, voltage))

print("Anomalies:")
for anomaly in anomalies:
    print(f"Timestamp: {anomaly[0]}, Voltage: {anomaly[1]}")

