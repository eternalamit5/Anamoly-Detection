import csv
import random
from datetime import datetime, timedelta

# Function to generate dummy voltage data
def generate_dummy_voltage_data(start_time, end_time, interval_minutes, mean_voltage, voltage_range):
    current_time = start_time
    data = []
    while current_time <= end_time:
        voltage = random.uniform(mean_voltage - voltage_range/2, mean_voltage + voltage_range/2)
        data.append([current_time.strftime('%Y-%m-%d %H:%M:%S'), voltage])
        current_time += timedelta(minutes=interval_minutes)
    return data

# Function to add anomalies to the data
def add_anomalies(data, num_anomalies, anomaly_range):
    random_indexes = random.sample(range(len(data)), num_anomalies)
    for index in random_indexes:
        voltage = data[index][1]
        anomaly_voltage = random.uniform(voltage - anomaly_range/2, voltage + anomaly_range/2)
        data[index][1] = anomaly_voltage
    return data

# Parameters for generating dummy data
start_time_str = '2023-07-24 08:00:00'
end_time_str = '2023-07-25 08:00:00'
interval_minutes = 60  # 1 hour interval
mean_voltage = 230
voltage_range = 5
num_anomalies = 5
anomaly_range = 20  # Range for introducing anomalies

start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')

# Generate dummy data
data = generate_dummy_voltage_data(start_time, end_time, interval_minutes, mean_voltage, voltage_range)

# Add anomalies to the data
data_with_anomalies = add_anomalies(data, num_anomalies, anomaly_range)

# Save data with anomalies to CSV file
output_file = 'dummy_voltage_data_with_anomalies.csv'
with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Timestamp', 'Voltage'])
    csvwriter.writerows(data_with_anomalies)

print(f"Dummy voltage data with anomalies has been saved to {output_file}.")
