# Homework 5: Advanced Iteration, Nested Structures, and Slicing

**You must complete this assignment in PyCharm, working inside a single
downloaded `.py` file -- not on this web page.** Unlike earlier homeworks,
there's no notebook to fill in here: download `HW5.py` below, open it in
PyCharm, and write and run all of your code directly in that file. This
page's instructions mirror what's in the file so you can read them without
switching windows, but the downloaded file is what you edit, run, and
submit.

## Download the Assignment File

Download: [HW5.py](HW5.py)

## Instructions

- Complete ALL problems
- Run your file often and verify your output before finishing
- Use meaningful variable names and add comments to explain your logic
- Graded for submission, not for correctness -- but this material will
  appear on quizzes and exams, so treat it as real practice, not a box to
  check

This homework has two sections:
- **Section 1 (Problems 1-2):** covers Class 7 material -- `range()`,
  `enumerate()`, list comprehensions, nested lists.
- **Section 2 (Problems 3-7):** covers Class 10 material -- slicing,
  negative indices, the step parameter, and slice assignment.

**PyCharm reminders:**
- Run your file with `Shift+F10` (or the green play button)
- Output appears in the terminal at the bottom
- Save frequently with `Ctrl+S` / `Cmd+S`

This is your first graded assignment in PyCharm -- if you need a refresher on
the PyCharm workflow itself (not the Python concepts below), see the Class 9
reading's [Key Things to Remember](https://BU-EK125.github.io/EK125/class/Class9.html#key-things-to-remember)
table. In particular, watch out for the reading's
[What Will Be Different](https://BU-EK125.github.io/EK125/class/Class9.html#what-will-be-different)
🚩 common mistake: a bare expression on its own line (like Colab) displays
nothing in a `.py` file -- you must `print()` everything you want to see.

## Section 1: Class 7 Material

### Problem 1: Water Quality Lab

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
:lines: 32-95
```

### Problem 2: Stress Grid Analysis

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
:lines: 99-153
```

## Section 2: Class 10 Material

### Problem 3: Stress Reading Slices

A structural engineer is reviewing a log of 10 stress measurements (in MPa)
taken at equal intervals along a beam:

```python
stress_readings = [12.4, 15.1, 18.7, 14.3, 22.6, 19.8, 16.2, 21.0, 13.5, 17.9]
```

Use **slicing** to answer each part below. Each answer should be a single
slice expression -- no loops needed. Print a label with each result.

- (a) Extract the first 3 readings.
- (b) Extract the last 4 readings.
- (c) Extract readings at positions 3 through 6 (inclusive). Remember: the
  end index in a slice is NOT included.
- (d) Extract all readings EXCEPT the first and last.
- (e) Print the entire list in REVERSE ORDER using a slice.
- (f) Extract every other reading starting from the first (indices 0, 2, 4, ...).

Expected output:
```text
(a) First 3 readings: [12.4, 15.1, 18.7]
(b) Last 4 readings: [16.2, 21.0, 13.5, 17.9]
(c) Positions 3-6: [14.3, 22.6, 19.8, 16.2]
(d) All except first and last: [15.1, 18.7, 14.3, 22.6, 19.8, 16.2, 21.0, 13.5]
(e) Reversed: [17.9, 13.5, 21.0, 16.2, 19.8, 22.6, 14.3, 18.7, 15.1, 12.4]
(f) Every other: [12.4, 18.7, 22.6, 16.2, 13.5]
```

See the reading's [Simplest Slice Notation](https://BU-EK125.github.io/EK125/class/Class10.html#simplest-slice-notation) section for part (c), [Common Slicing Patterns](https://BU-EK125.github.io/EK125/class/Class10.html#common-slicing-patterns) for parts (a), (b), (d), and (f), and [Negative Steps (Reversing)](https://BU-EK125.github.io/EK125/class/Class10.html#negative-steps-reversing) for part (e).

```{literalinclude} HW5.py
:language: python
:lines: 158-201
```

### Problem 4: Air Quality Index Slices

An environmental monitoring system records hourly air quality index (AQI)
values for a 24-hour period:

```python
aqi_data = [42, 45, 48, 51, 55, 60, 72, 85, 93, 88, 80, 75,
            68, 64, 70, 78, 85, 90, 88, 80, 70, 60, 52, 47]
```

Each index corresponds to one hour (index 0 = midnight, index 23 = 11 PM).

Use **slicing** with negative indices or step values to answer the
following. Add a comment above each slice explaining what you're doing.

- (a) Extract the final 6 hours of data (6 PM through 11 PM).
- (b) Extract data from the 5th-to-last hour through the 2nd-to-last hour
  (inclusive). Use ONLY negative indices for both start and end. Hint: be
  careful -- the end index in a slice is not included!
- (c) Extract every 3rd reading across the full 24 hours (simulating a
  sample every 3 hours).
- (d) Extract the "peak hours" -- hours 7 through 18 (indices 7 to 18
  inclusive) but in REVERSE order, using a single slice with a negative step.
- (e) PREDICT (without running it first), then verify: what does
  `aqi_data[-1]` give you? What does `aqi_data[-1:]` give you? Why are these
  different? Print both and write your explanation as a comment.

Expected output:
```text
(a) Final 6 hours: [88, 80, 70, 60, 52, 47]
(b) 5th-to-last through 2nd-to-last: [80, 70, 60, 52]
(c) Every 3rd reading: [42, 51, 72, 88, 68, 78, 88, 60]
(d) Peak hours reversed: [88, 90, 85, 78, 70, 64, 68, 75, 80, 88, 93, 85]
(e) aqi_data[-1] = 47, aqi_data[-1:] = [47]
```

See the reading's [Negative Indices in Slices](https://BU-EK125.github.io/EK125/class/Class10.html#negative-indices-in-slices), [The Step Parameter](https://BU-EK125.github.io/EK125/class/Class10.html#the-step-parameter), and [The confusing behavior of -1](https://BU-EK125.github.io/EK125/class/Class10.html#the-confusing-behavior-of-1) sections for a refresher -- that last one is exactly part (e).

```{literalinclude} HW5.py
:language: python
:lines: 206-258
```

### Problem 5: Tensile Test Data Cleaning

A materials testing lab collected force measurements (in Newtons) during a
tensile test. The first 3 readings and the last 2 readings are known to be
instrument calibration artifacts -- not real data. You need to clean the
dataset.

```python
force_data = [0.0, 0.0, 0.0, 45.2, 67.8, 89.1, 112.4, 98.3, 76.5, 0.0, 0.0]
```

- (a) Use a slice to extract just the VALID data (indices 3 through 8
  inclusive). Store this in a variable called `valid_data`. Print it.
- (b) Calculate the average of `valid_data` using `sum()` and `len()`. Store
  this in a variable called `fill_value`. Round it to 1 decimal place. Print
  it with a label.
- (c) Use **slice assignment** to replace the first 3 elements of
  `force_data` with `fill_value` repeated 3 times. Hint: you can repeat a
  value in a list using the `*` operator: `[value] * 3`.
- (d) Use **slice assignment** to replace the last 2 elements of
  `force_data` with `fill_value` repeated 2 times.
- (e) Print the modified `force_data` with a label.

Expected output:
```text
Valid data: [45.2, 67.8, 89.1, 112.4, 98.3, 76.5]
Fill value: 81.5
Cleaned data: [81.5, 81.5, 81.5, 45.2, 67.8, 89.1, 112.4, 98.3, 76.5, 81.5, 81.5]
```

See the reading's [Slice Assignment (Lists Only)](https://BU-EK125.github.io/EK125/class/Class10.html#slice-assignment-lists-only) section, and [The sum() Function](https://BU-EK125.github.io/EK125/class/Class7.html#the-sum-function) section from Class 7, for a refresher.

```{literalinclude} HW5.py
:language: python
:lines: 263-307
```

### Problem 6: Conveyor Belt Rearrangement

A robotics team programs a conveyor belt that carries parts in a specific
order. After a maintenance window, they need to rearrange and combine
datasets.

```python
line_A = [101, 102, 103, 104, 105]   # Part IDs from Line A
line_B = [201, 202, 203, 204, 205]   # Part IDs from Line B
```

**Part A: Rotation**
The team needs to "rotate" `line_A` left by 2 positions, so that the element
at index 2 becomes the new first element.
Example: `[101, 102, 103, 104, 105]` → `[103, 104, 105, 101, 102]`.

Use TWO slices and the `+` operator to build the rotated list. Store it in
`rotated_A` and print it.

See the reading's [Building New Sequences from Slices](https://BU-EK125.github.io/EK125/class/Class10.html#building-new-sequences-from-slices) section for a refresher.

**Part B: Interleaving**
The team wants to alternate parts from `line_A` and `line_B` in a single
list: `[101, 201, 102, 202, 103, 203, 104, 204, 105, 205]`.

Do this in two steps:
1. Create a new list called `combined` with 10 zeros using the `*` operator.
2. Use TWO slice assignments (one with step 2 starting at 0, one with step 2
   starting at 1) to place `line_A` and `line_B` into the correct positions.

Print `combined` to verify.

See the reading's [Slice Assignment (Lists Only)](https://BU-EK125.github.io/EK125/class/Class10.html#slice-assignment-lists-only) section for the step-assignment length rule, and [Building New Sequences from Slices](https://BU-EK125.github.io/EK125/class/Class10.html#building-new-sequences-from-slices) for this exact interleaving pattern.

**Part C: Using `.index()` with Slicing**
Part ID 203 has been flagged as defective. Extract all part IDs that come
AFTER 203 in `line_B` using a single slice. Use the `.index()` method to
find the position of 203 dynamically -- do not hardcode the index number.
Print the result with a label.

Expected output:
```text
Parts after defective 203: [204, 205]
```

See the reading's [Slicing with Variables](https://BU-EK125.github.io/EK125/class/Class10.html#slicing-with-variables) section for a refresher.

```{literalinclude} HW5.py
:language: python
:lines: 312-361
```

### Problem 7: Bridge Temperature Moving Average

A civil engineering team is monitoring daily temperatures (°C) at a bridge
site to detect thermal expansion risks. They want to compute a **moving
average** with a window of 5 days to smooth out daily fluctuations.

```python
daily_temps = [8.2, 9.1, 11.4, 10.3, 13.6, 15.2, 14.8, 16.1,
               17.3, 15.9, 14.2, 12.8, 11.1, 9.7, 10.5]
```

A moving average works like this: with window size 5, the first average is
the average of days 0-4 (stored at index 0), the second is the average of
days 1-5 (stored at index 1), and so on until you reach the last complete
window.

**Part A: Pseudocode**
Before writing any code, write pseudocode as Python comments. Break the
problem into steps. Think about:
- How many complete windows are there? (Hint: `len(data) - window_size + 1`)
- How do you extract each window as a slice?
- How do you compute the average of the window?
- How do you collect the results?

**Part B: Code**
Write code that:
1. Creates an empty list called `moving_averages`.
2. Uses a `for` loop with `range()` to iterate through each valid window
   start position.
3. For each iteration, extracts a window slice of size 5 and computes its
   average.
4. Appends each average (rounded to 2 decimal places) to `moving_averages`.
5. After the loop, prints each moving average with its window label.

Expected output:
```text
Days 0-4:   average = 10.52
Days 1-5:   average = 11.92
Days 2-6:   average = 13.06
Days 3-7:   average = 14.0
Days 4-8:   average = 15.4
Days 5-9:   average = 15.86
Days 6-10:   average = 15.66
Days 7-11:   average = 15.26
Days 8-12:   average = 14.26
Days 9-13:   average = 12.74
Days 10-14:   average = 11.66
```

See the reading's [Windowing through sequences](https://BU-EK125.github.io/EK125/class/Class10.html#windowing-through-sequences) section -- it walks through this exact pattern.

**Part C: Reflection**
The `moving_averages` list has fewer entries than `daily_temps`. How many
fewer? Write a comment explaining WHY, using the formula from your
pseudocode.

```{literalinclude} HW5.py
:language: python
:lines: 365-430
```
