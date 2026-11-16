"""
main.py  --  Owner: today's Integrator
Runs the whole fitness tracker program.  (Class 18 lab: Integration Clinic)
"""
from loader import load_tracker_data
from analyzer import analyze_metric
from reporter import write_report


def main():
    """Load the data, analyze four metrics, and write the report."""
    data = load_tracker_data("fitness_data.csv")

    # (metric, goal, higher_is_better) -- decided by the team in Class 15
    plan = [("steps", 8000, True),
            ("resting_hr", 62, False),
            ("sleep_hours", 7.0, True),
            ("active_minutes", 30, True)]

    results_list = []
    for metric, goal, higher_is_better in plan:
        results = analyze_metric(data, metric, goal, higher_is_better)
        results_list.append(results)

    write_report(results_list, "fitness_report.txt")
    print("Report written to fitness_report.txt")


if __name__ == "__main__":
    main()
