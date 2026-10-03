# Homework 5: Advanced Iteration and Nested Structures

This is a script-based assignment: unlike earlier homeworks, you'll write and
run this entirely in PyCharm as a single `.py` file, not in Colab notebook
cells. Download the file below, open it locally, and run it as you go -- the
instructions are also on this page so you can read them without switching
windows.

Download: [HW5.py](HW5.py)

## Instructions

- Complete ALL problems
- Run your file often and verify your output before finishing
- Use meaningful variable names and add comments to explain your logic
- Graded for submission, not for correctness -- but this material will
  appear on quizzes and exams, so treat it as real practice, not a box to
  check

This assignment covers material from Class 7: `range()`, `enumerate()`,
list comprehensions, and nested lists.

**PyCharm reminders:**
- Run your file with `Shift+F10` (or the green play button)
- Output appears in the terminal at the bottom
- Save frequently with `Ctrl+S` / `Cmd+S`

## Problem 1: Water Quality Lab

A water quality lab records turbidity measurements (in NTU) from 5 different
river monitoring stations. You'll process this data using `range()`,
`enumerate()`, and list comprehensions.

```python
station_names = ["Upstream", "Bridge A", "Mill Pond", "Bridge B", "Downstream"]
turbidity     = [2.1, 3.8, 12.4, 8.7, 5.2]
```

**Part A: Using `enumerate()`**
Print a numbered report of each station and its turbidity reading. Use
`enumerate()` -- do NOT use `range(len(...))`.

Expected output:
```text
Station 1 - Upstream: 2.1 NTU
Station 2 - Bridge A: 3.8 NTU
Station 3 - Mill Pond: 12.4 NTU
Station 4 - Bridge B: 8.7 NTU
Station 5 - Downstream: 5.2 NTU
```

See the reading's [The Enumerate Function](https://BU-EK125.github.io/EK125/class/Class7.html#the-enumerate-function) section for a refresher.

**Part B: List Comprehension -- Unit Conversion**
Turbidity is sometimes reported in FTU (Formazin Turbidity Units). For this
sensor, 1 NTU = 1.05 FTU. Use a **list comprehension** to create a new list
called `ftu_readings` with each value converted to FTU, rounded to 2 decimal
places. Print the result.

Expected output:
```text
[2.21, 3.99, 13.02, 9.13, 5.46]
```

See the reading's [Basic List Comprehensions](https://BU-EK125.github.io/EK125/class/Class7.html#basic-list-comprehensions) section for a refresher.

**Part C: List Comprehension with Condition -- Flagging High Readings**
The safe threshold is 5.0 NTU. Use a **list comprehension** to create a list
called `high_stations` containing only the names of stations ABOVE the
threshold. Print the result.

Expected output:
```text
High turbidity stations: ['Mill Pond', 'Bridge B', 'Downstream']
```

See the reading's [Adding Conditionals](https://BU-EK125.github.io/EK125/class/Class7.html#adding-conditionals) section for a refresher.

**Part D: `range()` with Step -- Scheduled Sampling**
Using `range()` with a step, print every other station name starting from
index 0. Use a `for` loop with `range()` (NOT `enumerate()` or direct
iteration).

Expected output:
```text
Scheduled sampling stations:
Upstream
Mill Pond
Downstream
```

See the reading's [Optional Arguments to Range](https://BU-EK125.github.io/EK125/class/Class7.html#optional-arguments-to-range) section for a refresher.

```{literalinclude} HW5.py
:language: python
:lines: 29-91
```

## Problem 2: Stress Grid Analysis

A structural analysis produces a 4x5 grid of stress values (MPa) across a
surface. Each inner list represents one row of measurements.

```python
stress_grid = [
    [1.1,  2.3,  3.5,  4.7,  5.9],    # Row 0
    [6.2,  7.4,  8.6,  9.8,  10.0],   # Row 1
    [11.1, 12.3, 13.5, 14.7, 15.9],   # Row 2
    [16.2, 17.4, 18.6, 19.8, 20.0],   # Row 3
]
```

**Part A: Printing with `enumerate()`**
Use a nested loop with `enumerate()` to print every value alongside its row
and column index. Format each line as shown.

Expected output (first 3 lines shown):
```text
[Row 0, Col 0]: 1.1
[Row 0, Col 1]: 2.3
[Row 0, Col 2]: 3.5
... (continue for all rows and columns)
```

See the reading's [Using `enumerate()` with Nested Lists](https://BU-EK125.github.io/EK125/class/Class7.html#using-enumerate-with-nested-lists) section for a refresher.

**Part B: Row Averages with a List Comprehension**
Use a list comprehension to build a list called `row_averages`, where each
entry is the average of one row. Round each average to 2 decimal places.
Print the result.

Expected output:
```text
Row averages: [3.5, 8.4, 13.5, 18.4]
```

See the reading's [The sum() Function](https://BU-EK125.github.io/EK125/class/Class7.html#the-sum-function) section for a refresher.

**Part C: Flagging High-Stress Rows**
The safety threshold is 10.0 MPa (average). Use `enumerate()` and a `for`
loop to print the index and average of any row whose average EXCEEDS the
threshold.

Expected output:
```text
Row 2 average (13.5 MPa) exceeds threshold.
Row 3 average (18.4 MPa) exceeds threshold.
```

```{literalinclude} HW5.py
:language: python
:lines: 96-149
```
