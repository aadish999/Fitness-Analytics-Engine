import numpy as np

class PerformanceSolver:
    @staticmethod
    def estimate_vo2_max(resting_hr, max_hr):
        """Estimates VO2 Max using the Uth-Sørensen-Overgaard-Pedersen formula."""
        if resting_hr <= 0:
            raise ValueError("Resting HR must be greater than zero.")
        return round(15.3 * (max_hr / resting_hr), 2)

    def calculate_training_stress(self, duration_minutes, average_hr, max_hr):
        """Computes a Training Stress Score based on cardiac threshold strain."""
        intensity_factor = average_hr / max_hr
        stress_score = (duration_minutes * average_hr * intensity_factor) / 100
        return round(stress_score, 2)
