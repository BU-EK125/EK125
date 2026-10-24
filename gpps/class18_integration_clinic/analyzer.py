"""
analyzer.py  --  Owner: Data Analyst
Calculates summary statistics for one metric.  (Class 18 lab: Integration Clinic)
"""


def analyze_metric(data, metric, goal, higher_is_better=True):
    """Calculate summary statistics for one metric in the tracker data.

    Parameters:
        data (dict): dictionary returned by load_tracker_data
        metric (str): one of the keys in data, e.g. "steps"
        goal (float): daily goal for this metric, e.g. 8000
        higher_is_better (bool): True if a bigger number is better
            (steps); False if a smaller number is better (resting_hr).
            Default True.

    Returns:
        dict with exactly these keys:
            "metric"            (str)   the metric name
            "num_days"          (int)   number of days analyzed
            "average"           (float) mean, rounded to 1 decimal place
            "minimum"           (float) smallest value
            "maximum"           (float) largest value
            "best_day"          (int)   day number of the best value
                                        (first one if there is a tie)
            "goal"              (float) the goal that was passed in
            "days_meeting_goal" (int)   days at or better than the goal

    Side effects: none (does not print).
    """
    values = data[metric]
    days = data["day"]

    best_index = 0
    days_meeting_goal = 0
    for i in range(len(values)):
        if higher_is_better:
            if values[i] > values[best_index]:
                best_index = i
            if values[i] >= goal:
                days_meeting_goal = days_meeting_goal + 1
        else:
            if values[i] < values[best_index]:
                best_index = i
            if values[i] <= goal:
                days_meeting_goal = days_meeting_goal + 1

    results = {
        "metric": metric,
        "num_days": len(values),
        "average": round(sum(values) / len(values), 1),
        "minimum": min(values),
        "maximum": max(values),
        "best_day": days[best_index],
        "goal": goal,
        "days_meeting_goal": days_meeting_goal,
    }
    return results
