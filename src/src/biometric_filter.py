import numpy as np

class BiometricFilter:
    def __init__(self, smoothing_factor=0.15):
        """Initializes the filter with a smoothing weight for sensor data."""
        self.alpha = smoothing_factor
        self.last_clean_hr = None

    def process_heart_rate(self, raw_heart_rate):
        """Applies a real-time filter to eliminate sudden sensor anomalies."""
        if self.last_clean_hr is None:
            self.last_clean_hr = raw_heart_rate
            return raw_heart_rate
        
        # Low-pass filter formula to remove high-frequency noise spikes
        filtered_hr = (self.alpha * raw_heart_rate) + ((1 - self.alpha) * self.last_clean_hr)
        self.last_clean_hr = filtered_hr
        return round(filtered_hr, 2)
