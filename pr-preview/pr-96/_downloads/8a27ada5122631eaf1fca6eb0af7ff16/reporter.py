"""
reporter.py  --  Owner: Report Writer
STUB VERSION (Class 16 lab: BROKEN SKELETON). Writes a placeholder report.
The real code replaces the stub body in Class 17.
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
    # STUB: write one placeholder line per metric, touching every key
    # the real report will need, so a key mismatch shows up TODAY.
    with open(filename, "w") as file:
        file.write("STUB REPORT\n")
        for results in results_list:
            file.write(f"{results['metric']} {results['num_days']} "
                       f"{results['average']} {results['minimum']} "
                       f"{results['maximum']} {results['best_day']} "
                       f"{results['goal']} {results['days_meeting_goal']}\n")


def test_reporter():
    """Quick check: write a report from one fake result."""
    fake_results = {"metric": "steps", "num_days": 5, "average": 8327.8,
                    "minimum": 4569.0, "maximum": 12192.0, "best_day": 5,
                    "goal": 8000, "days_meeting_goal": 3}
    write_report([fake_results], "test_report.txt")
    print("Wrote test_report.txt -- open it and check it.")


if __name__ == "__main__":
    test_reporter()
