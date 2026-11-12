"""
loader.py  --  Owner: Data Loader
Class 18 lab INTEGRATION CLINIC version.  This program RUNS -- but is it right?
"""


def load_tracker_data(filename):
    """Read a fitness tracker CSV file and return its data as a dictionary.

    Returns:
        dict with one key per column: "day", "steps", "resting_hr",
        "sleep_hours", "active_minutes". Each value is a list with one
        entry per COMPLETE day, in file order. "day" values are ints;
        all others are floats. All lists are always the same length.

    Assumptions and messy cases: any row with a blank value is skipped
        entirely.
    """
    data = {}
    with open(filename, "r") as file:
        column_names = file.readline().strip().split(",")
        for name in column_names:
            data[name] = []

        for line in file:
            values = line.strip().split(",")
            for col in range(len(column_names)):
                name = column_names[col]
                # Skip blank values
                if values[col] != "":
                    if name == "day":
                        data[name].append(int(values[col]))
                    else:
                        data[name].append(float(values[col]))
    return data
