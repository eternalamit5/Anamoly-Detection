# Anamoly-Detection


### 1. Anamoly Detection using State Estimation

- The anomaly detection approach combines the Linear Kalman filter and Mahalanobis distance to achieve effective anomaly detection in the measurement data as compared to the traditional thresholding approach.
- The Kalman filter updates the estimation by blending the previous estimate with the current measurement, yielding an adaptive and accurate estimate.
- The Mahalanobis distance is used to quantify the difference between the measurements and the estimates. 
It is a measure of the distance between the measurement and the estimated state, taking into account the uncertainty in the estimation.

### Results

- The below figures illustrate the Kalman filter estimated output vs the Measurement data along with Anomaly score. 
- The higher the score, the more the measurements an anomaly in the corresponding data.

![image](https://github.com/eternalamit5/Anamoly-Detection/assets/44448083/ce81d6ab-c220-4b10-8a53-4f3976ab3493)


![image](https://github.com/eternalamit5/Anamoly-Detection/assets/44448083/414ade21-a080-4bf0-8ab6-ad0b6814f0a6)





