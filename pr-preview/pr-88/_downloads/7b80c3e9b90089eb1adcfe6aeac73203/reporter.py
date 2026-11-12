"""
reporter.py  --  Owner: Report Writer
Writes the summary report to a text file.  (Class 18 lab: Integration Clinic)
"""


def write_report(results_list, filename):
    """Write a formatted fitness summary report to a text file.

    Parameters:
        results_list (list): list of dictionaries, each one returned by
            analyze_metric
        filename (str): name of the report file to create,
            e.g. "fitness_report.txt"

    Returns:
        None

    Side effects: creates (or overwrites) the file named filename.
    """
    with open(filename, "w") as file:
        file.write("FITNESS TRACKER SUMMARY REPORT\n")
        file.write("==============================\n")
        file.write(f"Days analyzed: {results_list[0]['num_days']}\n\n")
        for results in results_list:
            file.write(f"Metric: {results['metric']}\n")
            file.write(f"  Average: {results['average']}\n")
            file.write(f"  Range:   {results['minimum']} to {results['maximum']}\n")
            file.write(f"  Best day: Day {results['best_day']}\n")
            file.write(f"  Goal: {results['goal']}  "
                       f"(met on {results['days_meeting_goal']} of "
                       f"{results['num_days']} days)\n\n")
