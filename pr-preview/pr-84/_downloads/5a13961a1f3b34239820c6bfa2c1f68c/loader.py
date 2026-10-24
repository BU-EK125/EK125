"""
loader.py  --  Owner: Data Loader
STUB VERSION (Class 16 lab: BROKEN SKELETON). Returns the contract's example value.
The real code replaces the stub body in Class 17.
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

        Example (file containing Days 1-2 only):
        {"day": [1, 2], "steps": [8478.0, 9430.0],
         "resting_hr": [61.0, 67.0], "sleep_hours": [8.1, 7.8],
         "active_minutes": [50.0, 34.0]}

    Side effects: none. Does not print.

    Assumptions and messy cases: the first line is the header. Any row
        with a blank value is skipped entirely.
    """
    # STUB: return the example value from the contract
    data = {"day": [1, 2],
            "steps": [8478.0, 9430.0],
            "resting_hr": [61.0, 67.0],
            "sleep_hours": [8.1, 7.8],
            "active_minutes": [50.0, 34.0]}
    return data


def test_loader():
    """Quick check that the stub keeps its promises."""
    data = load_tracker_data("fitness_data.csv")
    print("type:", type(data))
    print("keys:", list(data.keys()))
    print("lengths:", len(data["day"]), len(data["steps"]))


if __name__ == "__main__":
    test_loader()
