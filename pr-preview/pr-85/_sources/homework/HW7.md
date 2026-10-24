# Homework 7: Modular Functions and File I/O

**You must complete this assignment in PyCharm, working inside a single
downloaded `.py` file -- not on this web page.** Download `HW7.py` below,
open it in PyCharm, and write and run all of your code directly in that
file. This page's instructions mirror what's in the file so you can read
them without switching windows, but the downloaded file is what you edit,
run, and submit.

## Download the Assignment File

Download: [HW7.py](HW7.py)

## Instructions

- Complete ALL problems
- Run your file often and verify your output before finishing
- Use meaningful variable names and add comments to explain your logic
- Graded for submission, not for correctness -- but this material will
  appear on quizzes and exams, so treat it as real practice, not a box to
  check

This homework has two sections:
- **Section 1 (Problems 1-6):** covers Class 13 material -- modular
  functions. All modular programs should consist of a main program that
  calls the functions. Write the function definitions and the main
  program, with docstrings in every function. Validate user input where
  there is any. Write function stubs when asked.
- **Section 2 (Problems 7-11):** covers Class 14 material -- file I/O.

**PyCharm reminders:**
- Run your file with `Shift+F10` (or the green play button)
- Output appears in the terminal at the bottom
- Save frequently with `Ctrl+S` / `Cmd+S`

## Section 1: Modular Functions

### Problem 1: Degrees to Radians

Write a program of 3 functions: `getangle` (prompts for an angle in
degrees), `convert` (converts it to radians), and `printresult` (prints
the result to two decimal places).

**Step 1:** Write stubs first and run the main program to verify structure
-- `getangle` returns `32`, `convert` returns `deg` divided by 2,
`printresult` simply prints `deg` and `rad`.

**Step 2:** Replace the stubs with full implementations. Include
docstrings for each function.

See the reading's [Function Stubs](https://BU-EK125.github.io/EK125/class/Class13.html#function-stubs) section for a refresher.

```{literalinclude} HW7.py
:language: python
:lines: 38-55
```

### Problem 2: A Box of Characters

Write two functions: `getnchar` (generates a random integer `n` from 5 to
10, prompts for a character, returns both -- if the user enters more than
one character, use only the first) and `printbox` (prints an `n x n`
square box of the character).

**Step 1:** Stubs first -- `getnchar` returns `3` and `'e'`, `printbox`
prints `'e'` three times on one line.

**Step 2:** Replace with full implementations, with docstrings.

```{literalinclude} HW7.py
:language: python
:lines: 60-78
```

### Problem 3: Volume and Surface Area of a Cylinder

Write three functions: `getradht` (prompts for base radius and height),
`volsurf` (calculates volume and surface area), and `printresults` (prints
the results in sentence format to two decimals).

**Step 1:** Stubs first -- `getradht` returns `3` and `10`, `volsurf`
returns `vol` as `rad * 2` and `surf` as `ht * 2`, `printresults` simply
prints `vol` and `surf`.

**Step 2:** Replace with full implementations, with docstrings.

```{literalinclude} HW7.py
:language: python
:lines: 83-100
```

### Problem 4: Arithmetic Menu

Write four functions: `randnums` (generates two random integers),
`printmenu` (displays an add/subtract/multiply/divide menu and returns the
user's choice), `compute` (computes the operation given `x`, `y`, and
`choice`), and `printresult` (prints the result nicely).

**Step 1:** Stubs first -- `randnums` returns `1` and `2`, `printmenu`
returns `3`, `compute` returns `x + y + choice`, `printresult` prints the
result simply.

**Step 2:** Replace with full implementations, with docstrings.

```{literalinclude} HW7.py
:language: python
:lines: 105-125
```

### Problem 5: Local Scope

**Part 1 -- Predict and run:** before running the code below, predict what
will happen and write your prediction as a comment. Then run it and
explain why.

```python
def computeBonus(score):
    """Adds a 10-point bonus to a score and prints it."""
    bonusScore = score + 10
    print(f"Inside function: {bonusScore}")

computeBonus(85)
print(bonusScore)   # What happens here?
```

**Part 2 -- Fix it:** rewrite `computeBonus` so the bonus score is
available outside the function. The main program should store the
returned value in a variable and print it. Include a docstring.

See the reading's [What is Scope?](https://BU-EK125.github.io/EK125/class/Class13.html#what-is-scope) section for a refresher.

```{literalinclude} HW7.py
:language: python
:lines: 130-151
```

### Problem 6: Mutable vs. Immutable Arguments

**Part 1 (immutable):** write `addCurve(score, curve)` that adds curve
points to `score` and prints the result inside the function. Call it with
a score of 72 and a curve of 8, then print the original `score` variable
afterward -- does it change? Why?

**Part 2 (mutable):** write `curveAll(scores, curve)` that adds curve
points to every score in the list using index assignment
(`scores[i] = scores[i] + curve`). Call it with `[72, 85, 90, 68]` and a
curve of 8, then print the original list -- does it change? Why?

**Part 3 (protect the original):** write `curveAllSafe(scores, curve)`
that returns a *new* list with curved scores without modifying the
original. Verify the original is unchanged after calling it.

See the reading's [The Two Types of Data: Mutable and Immutable](https://BU-EK125.github.io/EK125/class/Class13.html#the-two-types-of-data-mutable-and-immutable) section for a refresher.

```{literalinclude} HW7.py
:language: python
:lines: 156-181
```

## Section 2: File I/O

### Problem 7: Writing and Reading Back Sensor Data

A thermometer recorded body temperatures (in F):

```python
readings = [98.6, 99.1, 97.8, 100.4, 98.2]
```

**7.1 Write:** using a `with` statement and `'w'` mode, write each reading
to `body_temps.txt`, one per line. (`.write()` does NOT add newlines for
you.)

**7.2 Read three ways:**
- Open the file and use `.read()`; print the variable and its type.
- Open it again and use `.readlines()`; print the resulting list.
- Open it a third time and iterate over it directly to build a list of
  floats named `temps_read`, using `.strip()` on each line.
- Print the average of `temps_read`, rounded to two decimal places.

**7.3 Test:** use `assert` to confirm `temps_read` equals the original
`readings` list.

Questions to answer (as comments): What type does `.read()` return? What
type does `.readlines()` return? What extra character appears at the end
of each `.readlines()` element, and where did it come from? Why did you
need to reopen the file for each read method instead of doing all three in
one `with` block?

See the reading's [Reading Files: Different Methods](https://BU-EK125.github.io/EK125/class/Class14.html#reading-files-different-methods) section for a refresher.

```{literalinclude} HW7.py
:language: python
:lines: 190-225
```

### Problem 8: Write vs. Append, a Lab Activity Log

**8.1 Start the log:** open `lab_log.txt` in `'w'` mode and write the
header line `Lab Activity Log`. Write a function `log_event(filename,
message)` that opens `filename` in `'a'` mode and writes `message` on its
own line.

**8.2 Log some events:** call `log_event` three times with `'Calibrated
sensor'`, `'Started trial 1'`, `'Trial 1 complete'`. Open `lab_log.txt` in
`'r'` mode and print its contents.

**8.3 Experiment:** run your whole `HW7.py` file a second time and look at
`lab_log.txt` again. Then temporarily change the header in 8.1 to use
`'a'` mode instead of `'w'`, run it twice more, and look again. Change it
back to `'w'` afterward.

Questions to answer (as comments): After running the file twice with the
header in `'w'` mode, how many lines are in `lab_log.txt`? Why isn't it
twice as long? What happened when the header used `'a'` mode instead? Give
one real situation where `'a'` is the right choice and one where `'w'` is.

See the reading's [Appending to Files](https://BU-EK125.github.io/EK125/class/Class14.html#appending-to-files) and [Mistake 2: Using `'w'` Mode Carelessly](https://BU-EK125.github.io/EK125/class/Class14.html#mistake-2-using-w-mode-carelessly) sections for a refresher.

```{literalinclude} HW7.py
:language: python
:lines: 230-262
```

### Problem 9: Reading and Writing CSV Files

Store resting heart-rate trials in a CSV file, read it back, compute a
mean for each subject, and save a summary CSV. This also reviews
dictionaries from HW6.

```python
hr_data = [
    ['Subject', 'Trial1', 'Trial2', 'Trial3'],
    ['S01', 72, 75, 71],
    ['S02', 64, 66, 63],
    ['S03', 81, 78, 80],
    ['S04', 69, 70, 74]
]
```

**9.1 Write the CSV:** use the `csv` module to write `hr_data` to
`heart_rates.csv` (remember `newline=''` when opening the file).

**9.2 Read and process:** open `heart_rates.csv` with a `csv.reader`, use
`next()` to skip and store the header row, then for each remaining row
convert the three trial values to integers and compute their mean. Store
the results in a dictionary `mean_hr` mapping subject ID to mean heart
rate, and print it.

**9.3 Write a summary CSV:** write `heart_rate_summary.csv` with header
`Subject,Mean_HR`, one row per subject with the mean rounded to one
decimal place. Open and print it to verify.

Questions to answer (as comments): What type are the trial values coming
out of `csv.reader`, even though you wrote them as integers? What error do
you get calling `sum(row[1:])` without converting first, and why?

See the reading's [Working with CSV Files](https://BU-EK125.github.io/EK125/class/Class14.html#working-with-csv-files) section for a refresher.

```{literalinclude} HW7.py
:language: python
:lines: 267-319
```

### Problem 10: Organizing Experiment Folders with os

**10.1 Where am I?** import `os` and print the current working directory.
Is `body_temps.txt` from Problem 7 in that folder?

**10.2 Build a folder structure:** use `os.path.join` to build
`HW7_data/raw` and `HW7_data/results`, then `os.makedirs` with
`exist_ok=True` to create both.

**10.3 Save files into a subfolder:** for each subject in `['S01', 'S02',
'S03']`, build a path to `<subject>.txt` inside `HW7_data/raw` and write
`'Subject <subject> raw data'` into it.

**10.4 Check what exists:** use `os.listdir` on `HW7_data/raw`,
`os.path.isdir` on `HW7_data/results`, `os.path.isfile` on
`HW7_data/raw/S01.txt`, and `os.path.exists` on `HW7_data/raw/S04.txt` --
print each result.

Questions to answer (as comments): What would happen the second run
without `exist_ok=True`? Would `os.mkdir(os.path.join('HW7_data', 'raw'))`
work if `HW7_data` didn't exist yet? Why is `os.path.join(...)` better
than hardcoding `'HW7_data/raw'`?

See the reading's [The `os` Module: Working with Files and Directories](https://BU-EK125.github.io/EK125/class/Class14.html#the-os-module-working-with-files-and-directories) section for a refresher.

```{literalinclude} HW7.py
:language: python
:lines: 324-366
```

### Problem 11: A Read-Process-Save Function with a Main Guard

Combine everything into the reading's read -> process -> save pattern,
with error handling and a main guard.

**11.1 Write the function:** `convert_temps(input_path, output_path)`
returns `None` and prints an error if `input_path` doesn't exist
(`os.path.exists` or catch `FileNotFoundError`); otherwise reads
Fahrenheit temperatures one per line, converts each to Celsius
(`C = (F - 32) * 5/9`), writes a `'Temperature (C)'` header plus one value
per line (two decimals) to `output_path`, and returns the list of Celsius
values.

**11.2 Write `main()`:** call `convert_temps` with `input_path` set to
`body_temps.txt` (from Problem 7) and `output_path` set to
`body_temps_C.txt` inside `HW7_data/results` (build the path with
`os.path.join`). Print the returned list. Assert the first value is within
0.01 of 37.0. Call `convert_temps` again with `'missing_file.txt'` and
assert it returns `None`.

**11.3 Add the main guard:**
```python
if __name__ == "__main__":
    main()
```

Questions to answer (as comments): What is `__name__` when you run
`HW7.py` directly? If another file did `import HW7`, would `main()` run?
Would Problems 1-10's code run? Why does `convert_temps` take file paths
as arguments instead of hardcoding them?

See the reading's [Common Patterns and Best Practices](https://BU-EK125.github.io/EK125/class/Class14.html#part-4-common-patterns-and-best-practices) and [The `if __name__ == "__main__":` Pattern](https://BU-EK125.github.io/EK125/class/Class14.html#the-if-name-main-pattern) sections for a refresher.

```{literalinclude} HW7.py
:language: python
:lines: 371-413
```
