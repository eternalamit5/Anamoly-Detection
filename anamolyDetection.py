import math
import csv

class AnomalyDetect:
    def __init__(self, measurement_err=1, model_err=0.1):
        self.measurement_error = measurement_err
        self.estimation_error = measurement_err
        self.model_error = model_err
        self.current_estimate = 0
        self.last_estimate = 0
        self.gain = 0
        self.mahalanobis_distance = 0
        self.forgetting_factor = 0.2
        self.shape_param = 0.6

#The Mahalanobis distance is used to quantify the difference between the measurements and the estimates
    


    def update_detection(self, measurement):
        self.gain = self.estimation_error / (self.estimation_error + self.measurement_error)
        self.current_estimate = self.last_estimate + self.gain * (measurement - self.last_estimate)
        self.estimation_error = (1.0 - self.gain) * self.estimation_error + abs(self.last_estimate - self.current_estimate) * self.model_error
        self.last_estimate = self.current_estimate
        self.mahalanobis_distance = (self.mahalanobis_distance * self.forgetting_factor) + ((1 - self.forgetting_factor) * math.sqrt(((measurement - self.last_estimate) * (measurement - self.last_estimate)) / self.estimation_error))
        return 1 / (1 + math.exp(-self.mahalanobis_distance + self.shape_param))


# def read_csv_file(file_path):
#     data = []
#     with open(file_path, 'r') as csvfile:
#         csvreader = csv.reader(csvfile)
#         header = next(csvreader)  # Skip header row
#         for row in csvreader:
#             voltage = float(row[1])
#             data.append(voltage)
#     return data

# if __name__ == "__main__":
#     file_path = 'dummy_voltage_data_with_anomalies.csv'
#     voltage_data = read_csv_file(file_path)

#     # Assuming measurement error is 1 (you can adjust as needed)
#     anomaly_detector = AnomalyDetect(measurement_err=1, model_err=0.1)

#     # Detect anomalies in the voltage data
#     anomaly_scores = [anomaly_detector.update_detection(voltage) for voltage in voltage_data]

#     # Print the anomaly scores for each data point
#     for i, score in enumerate(anomaly_scores):
#         print(f"Timestamp {i}: Anomaly Score: {score}")


def read_csv_file(file_path):
    timestamps = []
    voltage_data = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Skip header row
        for row in csvreader:
            timestamp, voltage = row
            timestamps.append(timestamp)
            voltage_data.append(float(voltage))
    return timestamps, voltage_data

if __name__ == "__main__":
    file_path = 'dummy_voltage_data_with_anomalies.csv'
    timestamps, voltage_data = read_csv_file(file_path)

    # Assuming measurement error is 1 (you can adjust as needed)
    anomaly_detector = AnomalyDetect(measurement_err=1, model_err=0.1)

    # Detect anomalies in the voltage data
    anomaly_scores = [anomaly_detector.update_detection(voltage) for voltage in voltage_data]

    # Print the timestamp and anomaly score for each data point
    for timestamp, score in zip(timestamps, anomaly_scores):
        print(f"Timestamp: {timestamp}, Anomaly Score: {score}")
