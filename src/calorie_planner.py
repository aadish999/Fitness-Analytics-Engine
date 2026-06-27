class CaloriePlanner:
    @staticmethod
    def calculate_bmr(weight_kg, height_cm, age, gender="male"):
        """Computes Basal Metabolic Rate using the Harris-Benedict Formula."""
        if gender.lower() == "male":
            return 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
        else:
            return 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)

    def predict_total_burn(self, bmr, active_minutes, average_hr):
        """Predicts active energy expenditure based on cardiovascular intensity."""
        intensity_modifier = 1.2 if average_hr < 120 else 1.55
        active_burn = active_minutes * (average_hr * 0.05)
        return round((bmr * intensity_modifier) + active_burn, 2)
