"""
analyzer.py  --  Team 7, Data Analyst
Calculates summary statistics for one metric.
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
            "metric" (str), "num_days" (int),
            "average" (float, rounded to 1 decimal place),
            "minimum" (float), "maximum" (float),
            "best_day" (int: the DAY NUMBER, not the list position;
                        the earliest day if tied),
            "goal" (float, as passed in),
            "days_meeting_goal" (int: days at or better than the goal).

    Side effects: none. Does not print. Does not change data.
    """
    values = data[metric]
    total = 0
    best_position = 0
    goal_count = 0

    for i in range(len(values)):
        total = total + values[i]
        if higher_is_better:
            if values[i] > values[best_position]:
                best_position = i
            if values[i] >= goal:
                goal_count = goal_count + 1
        else:
            if values[i] < values[best_position]:
                best_position = i
            if values[i] < goal:
                goal_count = goal_count + 1

    summary = {
        "metric": metric,
        "num_days": len(values),
        "average": round(total / len(values), 1),
        "minimum": min(values),
        "maximum": max(values),
        "best_day": best_position,
        "goal": goal,
        "days_meeting_goal": goal_count,
    }
    return summary
