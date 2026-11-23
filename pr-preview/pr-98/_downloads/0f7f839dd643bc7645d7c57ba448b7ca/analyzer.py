"""
analyzer.py  --  Owner: Data Analyst
STUB VERSION (Class 16 lab: BROKEN SKELETON).
The real code replaces the stub body in Class 17.
"""


def analyze_metric(data, metric, goal, higher_is_better=True):
    """Calculate summary statistics for one metric.

    Parameters:
        data (dict): the dictionary returned by load_tracker_data.
        metric (str): one of "steps", "resting_hr", "sleep_hours",
            "active_minutes".
        goal (float): daily goal in the metric's own units, e.g. 8000.
        higher_is_better (bool): True if a larger value is better;
            False if a smaller value is better. Default True.

    Returns:
        dict with exactly these keys:
            "metric" (str), "num_days" (int), "average" (float, 1 decimal),
            "minimum" (float), "maximum" (float), "best_day" (int, the
            DAY NUMBER), "goal" (float), "days_meeting_goal" (int).

        Example (Days 1-5, metric="steps", goal=8000):
        {"metric": "steps", "num_days": 5, "average": 8327.8,
         "minimum": 4569.0, "maximum": 12192.0, "best_day": 5,
         "goal": 8000, "days_meeting_goal": 3}

    Side effects: none. Does not print. Does not change data.
    """
    # STUB: use the parameters where it is trivial, hard-code the rest
    results = {"metric": metric,
               "num_days": 5,
               "avg": 8327.8,
               "minimum": 4569.0,
               "maximum": 12192.0,
               "best_day": 5,
               "goal": goal,
               "days_meeting_goal": 3}
    print(results)


def test_analyzer():
    """Quick check that the stub keeps its promises."""
    fake_data = {"day": [1, 2], "steps": [8478.0, 9430.0]}
    results = analyze_metric(fake_data, "steps", 8000)
    print("type:", type(results))
    print("keys:", list(results.keys()))


if __name__ == "__main__":
    test_analyzer()
