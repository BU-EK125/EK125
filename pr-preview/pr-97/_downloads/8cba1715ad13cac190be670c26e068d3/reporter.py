"""
reporter.py  --  Team 7, Report Writer
Writes the summary report to a text file.
"""


def write_report(results_list, filename):
    """Write a formatted fitness summary report to a text file.

    Parameters:
        results_list (list of dict): one dictionary per metric, each
            returned by analyze_metric.
        filename (str): name of the report file, e.g. "fitness_report.txt".

    Returns:
        None

    Side effects: creates (or overwrites) the file filename. Does not print.
    """
    with open(filename, "w") as report
        report.write("FITNESS TRACKER SUMMARY REPORT\n")
        report.write("==============================\n")
        report.write("Days analyzed: " + results_list[0]["num_days"] + "\n\n")
        for stats in results_list:
            report.write(f"Metric: {stats['metric']}\n")
            report.write(f"  Average: {stats['average']}\n")
            report.write(f"  Range:   {stats['minimum']} to {stats['maximum']}\n")
            report.write(f"  Best day: Day {stats['best_day']}\n")
            report.write(f"  Goal: {stats['goal']}  "
                         f"(met on {stats['days_meeting_goal']} of "
                         f"{stats['num_days']} days)\n\n")
