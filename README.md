# Anamoly-Detection


### 1. Anamoly Detection using State Estimation

- The anomaly detection approach combines the Linear Kalman filter and Mahalanobis distance to achieve effective anomaly detection in the measurement data as compared to the traditional thresholding approach.
- The Kalman filter updates the estimation by blending the previous estimate with the current measurement, yielding an adaptive and accurate estimate.
- The Mahalanobis distance is used to quantify the difference between the measurements and the estimates. 
It is a measure of the distance between the measurement and the estimated state, taking into account the uncertainty in the estimation.

### Results

- The below figures illustrate the Kalman filter estimated output vs the Measurement data along with Anomaly score. 
- The higher the score, the more the measurements an anomaly in the corresponding data.


![image](/uploads/684f79fbd49550e09864ccdc6ee1c733/image.png)

![image](/uploads/680a414c3336a3ab452e6fc1e2f5d1d8/image.png)
