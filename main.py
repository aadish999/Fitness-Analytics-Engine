import numpy as np
from src.biometric_filter import BiometricFilter
from src.calorie_planner import CaloriePlanner
from src.performance_solver import PerformanceSolver

def main():
    print("Initializing Smart Health & Fitness Analytics Engine...\n")

    # 1. Initialize Patient / Athlete Parameters
    weight, height, age = 80, 180, 26
    resting_hr, max_hr = 60, 190
    
    bio_filter = BiometricFilter(smoothing_factor=0.2)
    planner = CaloriePlanner()
    
    # 2. Compute Advanced Baseline Metrics
    bmr = planner.calculate_bmr(weight, height, age, gender="male")
    vo2_max = PerformanceSolver.estimate_vo2_max(resting_hr, max_hr)
    
    print(f"--- Static Biomarker Profile Evaluated ---")
    print(f"Basal Metabolic Rate: {bmr:.2f} kcal/day")
    print(f"Estimated Cardiovascular VO2 Max: {vo2_max} ml/kg/min\n")

    # 3. Simulate Live Workout Tracking Stream (With High Sensor Noise)
    print("--- Executing Live Workout Telemetry Processing ---")
    base_workout_hr = 140
    raw_stream = [base_workout_hr + np.random.normal(0, 8) for _ in range(5)]
    
    cleaned_hr_readings = []
    for step, raw_hr in enumerate(raw_stream, 1):
        filtered_hr = bio_filter.process_heart_rate(raw_hr)
        cleaned_hr_readings.append(filtered_hr)
        print(f"Interval {step} | Raw Sensor HR: {raw_hr:.1f} bpm -> Filtered Biometrics: {filtered_hr} bpm")

    # 4. Compute Workout Dynamic Performance
    avg_workout_hr = np.mean(cleaned_hr_readings)
    workout_duration = 45 # minutes
    
    total_burn = planner.predict_total_burn(bmr, workout_duration, avg_workout_hr)
    stress_score = PerformanceSolver().calculate_training_stress(workout_duration, avg_workout_hr, max_hr)
    
    print(f"\n--- Post-Workout Diagnostic Summary ---")
    print(f"Total Cumulative Daily Burn: {total_burn} kcal")
    print(f"Workout Cardiorespiratory Stress Score: {stress_score} points")

if __name__ == "__main__":
    main()
