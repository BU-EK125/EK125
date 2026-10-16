# Homework 6: NumPy and Dictionaries

**You must complete this assignment in PyCharm, working inside a single
downloaded `.py` file -- not on this web page.** Download `HW6.py` below,
open it in PyCharm, and write and run all of your code directly in that
file. This page's instructions mirror what's in the file so you can read
them without switching windows, but the downloaded file is what you edit,
run, and submit.

## Download the Assignment File

Download: [HW6.py](HW6.py)

## Instructions

- Complete ALL problems
- Run your file often and verify your output before finishing
- Use meaningful variable names and add comments to explain your logic
- Graded for submission, not for correctness -- but this material will
  appear on quizzes and exams, so treat it as real practice, not a box to
  check

This homework has two sections:
- **Section 1 (Problems 1-6):** covers Class 11 material -- NumPy arrays
  and testing your code with `assert`.
- **Section 2 (Problems 7-10):** covers Class 12 material -- dictionaries.

**PyCharm reminders:**
- Run your file with `Shift+F10` (or the green play button)
- Output appears in the terminal at the bottom
- Save frequently with `Ctrl+S` / `Cmd+S`

## Section 1: NumPy and Code Testing

### Problem 1: Basic NumPy Operations and Assertions

Create a NumPy array `arr` with the values 3, 6, 9, 12, 15.

- Multiply every element by 2 and store it in a new array `doubled`.
- Add 5 to each element of the original array and store it in `plus_five`.
- Write 3 assertions (using `assert`) to test:
  1. The length of `arr` is 5
  2. The second value of `doubled` is 12
  3. The last value of `plus_five` is 20

See the reading's [assert: Python's simplest testing tool](https://BU-EK125.github.io/EK125/class/Class11.html#assert-python-s-simplest-testing-tool) section for a refresher.

```{literalinclude} HW6.py
:language: python
:lines: 34-49
```

### Problem 2: Testing Floating Point Array Equality

Explore how tiny rounding errors can affect equality comparisons between
floating point arrays -- even when the math looks the same.

Your task:
1. Create two 2x3 NumPy arrays that should contain the same values:
   - One using `array / np.sqrt(2)`
   - The other using `np.sqrt(0.5) * array`
2. Compute the sum of each array using `np.sum()`.
3. Compare the two sums using both `==` (direct equality) and
   `np.isclose()` (tolerance-based comparison).
4. Use `assert` to check if the sums match.

Questions to answer (as comments): What happens when you run the two
`assert` statements? Why does one of them fail? How small is the
difference between the two sums? Why is `np.isclose()` the preferred way
to compare floating point results?

See the reading's [Floating point error](https://BU-EK125.github.io/EK125/class/Class11.html#floating-point-error) section for a refresher.

```{literalinclude} HW6.py
:language: python
:lines: 54-78
```

### Problem 3: Manual and NumPy Equality Testing

We want to check whether two arrays are exactly equal.

**Part A (manual test):** Create `a = np.array([1, 2, 3])` and
`b = np.array([1, 2, 3])`. Use a `for` loop to compare each element, set
`all_equal = True` if all elements match (otherwise `False`), then
`assert all_equal`.

**Part B (NumPy testing):** Do the same check using
`np.testing.assert_array_equal`, which checks whether two arrays have
exactly the same shape and elements, raising an `AssertionError` if they
differ.

See the reading's [The array `assert` gotcha](https://BU-EK125.github.io/EK125/class/Class11.html#the-array-assert-gotcha) and [NumPy's specialized testing tools](https://BU-EK125.github.io/EK125/class/Class11.html#numpy-s-specialized-testing-tools) sections for a refresher.

```{literalinclude} HW6.py
:language: python
:lines: 83-100
```

### Problem 4: Shape and dtype Testing

Create a NumPy array of size `(n x n)` filled with numbers from 0 up to
`n^2 - 1`.

- Test that the array has the correct shape `(n, n)` using both `assert`
  and `np.testing.assert_array_equal`.
- Test that the array's `dtype` is `int64` using `assert`.

See the reading's [The array function and attributes of arrays](https://BU-EK125.github.io/EK125/class/Class11.html#the-array-function-and-attributes-of-arrays) section for a refresher.

```{literalinclude} HW6.py
:language: python
:lines: 105-115
```

### Problem 5: Edge Case Testing

Write code that computes the mean of a NumPy array.

- Test the result on a normal case like `[1, 2, 3]`.
- Test the result on the edge case of an empty array, confirming that the
  result is `np.nan`.
- Use `assert` (and `np.isnan` where needed).

See the reading's [What to test -- and what not to](https://BU-EK125.github.io/EK125/class/Class11.html#what-to-test-and-what-not-to) section for a refresher.

```{literalinclude} HW6.py
:language: python
:lines: 120-130
```

### Problem 6: Array Equality with np.testing

For an array of values between 0 and pi, compute `sin^2(x) + cos^2(x)`.

- Test that all results equal 1 within a small tolerance.
- Use `np.testing.assert_allclose` for the test -- it checks whether two
  arrays are approximately equal, allowing small differences; the `atol`
  parameter sets the maximum absolute difference allowed between elements.

See the reading's [NumPy's specialized testing tools](https://BU-EK125.github.io/EK125/class/Class11.html#numpy-s-specialized-testing-tools) section for a refresher.

```{literalinclude} HW6.py
:language: python
:lines: 135-148
```

## Section 2: Dictionaries

### Problem 7: Course Profile

You are building a simple profile to track one student's information for
this course.

**7.1: Create and access** -- Create a dictionary named `courseProfile`
with the keys `'name'` (your name), `'course'` (`'EK125'`), `'year'` (your
graduation year, as an integer), and `'gpa'` (`3.5`). Print the value
associated with `'name'`, and print the number of key-value pairs using
`len()`.

See the reading's [Dictionaries](https://BU-EK125.github.io/EK125/class/Class12.html#dictionaries) section for a refresher.

```{literalinclude} HW6.py
:language: python
:lines: 157-173
```

### Problem 7.2: Checking Keys and Updating Values

Using `courseProfile`:
- Check whether `'major'` is in the dictionary, and whether `'gpa'` is NOT
  in the dictionary, printing both results.
- Add a new key-value pair `'major'` with your intended major.
- Update `'gpa'` to `3.8`, then print the updated dictionary.

```{literalinclude} HW6.py
:language: python
:lines: 178-189
```

### Problem 7.3: Removing Entries and Using get() Safely

Using `courseProfile`:
- Remove the `'gpa'` key with `del`.
- Retrieve `'gpa'` with `get()` and print the result (should be `None`).
- Retrieve it again, this time supplying a default value of `-1`, and
  print the result.
- Print the final dictionary to confirm `gpa` is gone.

```{literalinclude} HW6.py
:language: python
:lines: 194-205
```

### Problem 8: Lab Sensor Readings

A dictionary stores the most recent temperature reading (in Celsius) from
sensors placed around a lab:

```python
sensorReadings = {
    'sensor_A': 22.1,
    'sensor_B': 24.7,
    'sensor_C': 21.8,
    'sensor_D': 26.3,
    'sensor_E': 23.5
}
```

**8.1: Iterate using keys() and values()** -- Use `.keys()` to print each
sensor's name on its own line. Use `.values()` to compute and print the
average temperature across all sensors, rounded to 2 decimal places.

```{literalinclude} HW6.py
:language: python
:lines: 210-239
```

### Problem 8.2: Iterate Using items() and Flag High Readings

Using `sensorReadings`, use `.items()` to loop over all key-value pairs.
Print each sensor name and reading as `sensor_A: 22.1 C`; inside the same
loop, if a reading is above `25.0`, also print a warning like
`WARNING: sensor_D is above threshold!`.

```{literalinclude} HW6.py
:language: python
:lines: 244-255
```

### Problem 9: List of Dictionaries

The list below stores information about members of an engineering project
team, each represented as a dictionary:

```python
team = [
    {'name': 'Amara',  'year': 2, 'role': 'Mechanical', 'gpa': 3.9},
    {'name': 'Ben',    'year': 1, 'role': 'Electrical',  'gpa': 3.4},
    {'name': 'Celia',  'year': 3, 'role': 'Civil',       'gpa': 3.7},
    {'name': 'Dario',  'year': 1, 'role': 'Mechanical',  'gpa': 3.2},
    {'name': 'Evelyn', 'year': 2, 'role': 'Electrical',  'gpa': 3.8},
]
```

**9.1: Access and display** -- Print the name and role of the first team
member using indexing. Loop over the list and print each member's name and
GPA as `Amara - GPA: 3.9`.

```{literalinclude} HW6.py
:language: python
:lines: 260-288
```

### Problem 9.2: Filter and Compute

Using the `team` list:
- Print the name of every member whose GPA is 3.7 or above.
- Calculate and print the average GPA of all first-year students
  (`year == 1`), rounded to 2 decimal places -- or a message saying there
  are none, if that's the case.

```{literalinclude} HW6.py
:language: python
:lines: 293-303
```

### Problem 10: Dictionary with List Values

A dictionary stores the quiz scores (out of 20) for each student over four
quizzes:

```python
quizScores = {
    'Alice':   [18, 15, 19, 17],
    'Bob':     [12, 14, 11, 16],
    'Charlie': [20, 18, 17, 19],
    'Dana':    [15, 16, 14, 18]
}
```

**10.1: Access and iterate** -- Print Alice's list of scores, and her score
on the third quiz (index 2) alone. Loop over `quizScores` with `.items()`
to print each student's name and average quiz score, rounded to 1 decimal
place, as `Alice: avg = 17.2`.

```{literalinclude} HW6.py
:language: python
:lines: 308-335
```

### Problem 10.2: Dictionary Comprehension

Using `quizScores`, create a dictionary `avgScores` via a **dictionary
comprehension**, mapping each student name to their average quiz score
(rounded to 1 decimal place). Print `avgScores`.

Then, using `avgScores`, use a dictionary comprehension to create
`honorRoll`, containing only the students whose average score is 17.0 or
above. Print `honorRoll`.

See the reading's [Dictionaries](https://BU-EK125.github.io/EK125/class/Class12.html#dictionaries) section (the dictionary comprehension example near the end) for a refresher.

```{literalinclude} HW6.py
:language: python
:lines: 340-353
```
