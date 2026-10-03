"""
Homework 5: Advanced Iteration and Nested Structures
EK125 - Spring 2026

This is a script-based assignment -- unlike earlier homeworks, you'll write
and run this entirely in PyCharm as a single .py file, not in Colab notebook
cells. Everything runs top to bottom in one shot.

Covers Class 7 material: range(), enumerate(), list comprehensions, and
nested lists.

Graded for submission, not for correctness -- but this material will appear
on quizzes and exams, so treat it as real practice, not a box to check.

INSTRUCTIONS:
  - Complete ALL problems
  - Run your file often and verify your output before finishing
  - Use meaningful variable names and add comments to explain your logic

PYCHARM REMINDERS:
  - Run your file with Shift+F10 (or the green play button)
  - Output appears in the terminal at the bottom
  - Save frequently with Ctrl+S / Cmd+S
"""

# ==============================================================================
# PROBLEM 1: Range, Enumerate, and List Comprehensions
# ==============================================================================
"""
A water quality lab records turbidity measurements (in NTU) from 5 different
river monitoring stations. You'll process this data using range(), enumerate(),
and list comprehensions.

    station_names = ["Upstream", "Bridge A", "Mill Pond", "Bridge B", "Downstream"]
    turbidity     = [2.1, 3.8, 12.4, 8.7, 5.2]

Part A: Using enumerate()
  Print a numbered report of each station and its turbidity reading.
  Use enumerate() - do NOT use range(len(...)).

  Expected output:
    Station 1 - Upstream: 2.1 NTU
    Station 2 - Bridge A: 3.8 NTU
    Station 3 - Mill Pond: 12.4 NTU
    Station 4 - Bridge B: 8.7 NTU
    Station 5 - Downstream: 5.2 NTU

Part B: List Comprehension - Unit Conversion
  Turbidity is sometimes reported in FTU (Formazin Turbidity Units).
  For this sensor, 1 NTU = 1.05 FTU.
  Use a LIST COMPREHENSION to create a new list called ftu_readings with
  each value converted to FTU, rounded to 2 decimal places.
  Print the result.

  Expected output:
    [2.21, 3.99, 13.02, 9.13, 5.46]

Part C: List Comprehension with Condition - Flagging High Readings
  The safe threshold is 5.0 NTU. Use a LIST COMPREHENSION to create a list
  called high_stations containing only the names of stations ABOVE the threshold.
  Print the result.

  Expected output:
    High turbidity stations: ['Mill Pond', 'Bridge B', 'Downstream']

Part D: range() with Step - Scheduled Sampling
  Using range() with a step, print every other station name starting from
  index 0. Use a for loop with range() (NOT enumerate or direct iteration).

  Expected output:
    Scheduled sampling stations:
    Upstream
    Mill Pond
    Downstream
"""

station_names = ["Upstream", "Bridge A", "Mill Pond", "Bridge B", "Downstream"]
turbidity     = [2.1, 3.8, 12.4, 8.7, 5.2]

print("=" * 60)
print("PROBLEM 1: Water Quality Lab")
print("=" * 60)

# Part A: Numbered report using enumerate()

# Part B: List comprehension - NTU to FTU conversion

# Part C: List comprehension with condition - high stations

# Part D: range() with step - scheduled sampling


# ==============================================================================
# PROBLEM 2: Nested Lists with enumerate() and Comprehensions
# ==============================================================================
"""
A structural analysis produces a 4x5 grid of stress values (MPa) across
a surface. Each inner list represents one row of measurements.

    stress_grid = [
        [1.1,  2.3,  3.5,  4.7,  5.9],    # Row 0
        [6.2,  7.4,  8.6,  9.8,  10.0],   # Row 1
        [11.1, 12.3, 13.5, 14.7, 15.9],   # Row 2
        [16.2, 17.4, 18.6, 19.8, 20.0],   # Row 3
    ]

Part A: Printing with enumerate()
  Use a nested loop with enumerate() to print every value alongside its
  row and column index. Format each line as shown.

  Expected output:
    [Row 0, Col 0]: 1.1
    [Row 0, Col 1]: 2.3
    [Row 0, Col 2]: 3.5
    ... (continue for all rows and columns)

Part B: Row Averages with a List Comprehension
  Use a list comprehension to build a list called row_averages, where each
  entry is the average of one row. Round each average to 2 decimal places.
  Print the result.

  Expected output:
    Row averages: [3.5, 8.4, 13.5, 18.4]

Part C: Flagging High-Stress Rows
  The safety threshold is 10.0 MPa (average). Use enumerate() and a for loop
  to print the index and average of any row whose average EXCEEDS the threshold.

  Expected output:
    Row 2 average (13.5 MPa) exceeds threshold.
    Row 3 average (18.4 MPa) exceeds threshold.
"""

stress_grid = [
    [1.1,  2.3,  3.5,  4.7,  5.9],
    [6.2,  7.4,  8.6,  9.8,  10.0],
    [11.1, 12.3, 13.5, 14.7, 15.9],
    [16.2, 17.4, 18.6, 19.8, 20.0],
]

print("\n" + "=" * 60)
print("PROBLEM 2: Stress Grid Analysis")
print("=" * 60)

# Part A: Print every value with its row and column index

# Part B: List comprehension for row averages

# Part C: Flag rows exceeding the threshold using enumerate()
