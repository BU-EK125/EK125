"""
loader.py  --  Team 7, Data Loader
Reads the fitness tracker CSV file.
"""


def load_tracker_data(filename):
    """Read a fitness tracker CSV file and return its data as a dictionary.

    Parameters:
        filename (str): name of the CSV file, e.g. "fitness_data.csv".

    Returns:
        dict with one key per column: "day", "steps", "resting_hr",
        "sleep_hours", "active_minutes". Each value is a list with one
        entry per COMPLETE day, in file order. "day" values are ints;
        all others are floats. All lists are always the same length.

    Side effects: none. Does not print.

    Assumptions and messy cases: the first line is the header. Any row
        with a blank value is skipped entirely.
    """
    with open(filename, "r") as csv_file:
        lines = csv_file.readlines()

    headers = lines[0].strip().split(",")
    tracker = {}
    for header in headers:
        tracker[header] = []

    for line in lines[1:]:
        row = line.strip().split(",")
        # only keep complete rows
        if row != "":
            tracker["day"].append(int(row[0]))
            for position in range(1, len(headers)):
                tracker[headers[position]].append(float(row[position]))
    return tracker
