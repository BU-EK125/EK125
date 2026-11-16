# EK125 Team Project: Fitness Tracker Analyzer

**Classes 15-19 (Mon 10/26 -- Mon 11/9), with a plotting add-on in Class 21 (Mon 11/16)**

---

## Why We Are Doing This

So far, every program you have written has been yours alone. Real engineering software is almost never written that way. Teams split a program into pieces, each person builds a piece, and then the pieces have to fit together.

The fitting-together part is where most problems happen. This project teaches you how to make it go smoothly:

1. **Agree first.** Write down exactly what each function receives and returns *before* anyone writes code.
2. **Build a skeleton.** Get the whole program running with placeholder functions (stubs).
3. **Fill it in.** Replace your stub with real code, one function at a time.
4. **Integrate and debug.** Put the real pieces together, find what broke, and fix it.

You already know every piece of Python this project needs: file I/O ([Class 14](https://BU-EK125.github.io/EK125/class/Class14.html#part-2-file-input-and-output-i-o)), functions ([Class 13](https://BU-EK125.github.io/EK125/class/Class13.html#part-1-user-defined-functions-morning)), dictionaries ([Class 12](https://BU-EK125.github.io/EK125/class/Class12.html#dictionaries)), lists, loops, and conditionals. **There is no new Python syntax in Classes 15-19.** What is new is *working together*.

---

## The Problem

A friend has worn a fitness tracker for 28 days and exported the data as a CSV file, `fitness_data.csv`:

```
day,steps,resting_hr,sleep_hours,active_minutes
1,8478,61,8.1,50
2,9430,67,7.8,34
...
9,,,5.6,
...
```

| Column | Meaning | Units |
|---|---|---|
| `day` | Day number (1-28) | -- |
| `steps` | Steps walked that day | steps |
| `resting_hr` | Resting heart rate | beats per minute (bpm) |
| `sleep_hours` | Sleep the night before | hours |
| `active_minutes` | Minutes of moderate or vigorous activity | minutes |

Some days have blank values (the tracker was not worn, or the battery died). Your team must decide how to handle them.

Your team will write a program that **reads the file, analyzes several metrics, and writes a summary report to a text file.**

---

## The Program: Three Functions and a Main Program

Each team member **owns one function** for the whole project. These three function headers are fixed. Every team uses the same names and parameters:

| Function owner | Function header | What it does |
|---|---|---|
| **Data Loader** | `load_tracker_data(filename)` | Reads the CSV file and returns the data as a dictionary of lists |
| **Data Analyst** | `analyze_metric(data, metric, goal, higher_is_better=True)` | Calculates statistics for one metric and returns them in a dictionary |
| **Report Writer** | `write_report(results_list, filename)` | Writes a formatted report to a text file |

A short **main program** (`main.py`) connects them:

```
data  -->  analyze_metric (once per metric)  -->  results_list  -->  write_report
  ^                                                                      |
load_tracker_data("fitness_data.csv")                       "fitness_report.txt"
```

Your team decides everything else, including:

- the exact keys in the results dictionary
- what to do with blank values
- which metrics and goals to analyze
- how the report looks

You write all of these decisions down in your **Team Contract**.

### File structure and sharing

Your team keeps all project files in a **shared Google Drive folder** (use your BU Google account and share it with all teammates). Each function lives in its own file so that no two people ever edit the same file:

```
FitnessTracker/
├── fitness_data.csv     (provided)
├── loader.py            (Data Loader edits this)
├── analyzer.py          (Data Analyst edits this)
├── reporter.py          (Report Writer edits this)
└── main.py              (today's Integrator edits this)
```

**How the shared folder works:**

- Download the files into your own PyCharm `FitnessTracker` folder to run them.
- When your file changes, upload the new version to the Drive folder. Replace the old file; don't create `loader (1).py`.
- **Only upload your own file.** Only the Integrator uploads `main.py`.
- Drive keeps every earlier version of each file (right-click → *Manage versions*), so nothing is ever lost.

---

## Roles

### Function owner (fixed for the whole project)

You are responsible for your function: its contract section, its stub, its real code, its tests, and explaining it. **You must be able to explain every line of your function out loud.** Your instructor or TA may ask you to do this at any time.

### Team duties (rotate every class)

| Duty | What you do that class |
|---|---|
| **Integrator** | Owns `main.py`, collects everyone's files, runs the whole program |
| **Tester** | Checks each function against the contract: right inputs, right return value, right keys |
| **Recorder** | Updates the Team Contract and Decision Log, and submits the team's work to Gradescope |

Rotation (write your names in during Class 15):

| Class | Integrator | Tester | Recorder |
|---|---|---|---|
| 15 (10/26) | Data Loader | Report Writer | Data Analyst |
| 16 (10/28) | Data Analyst | Data Loader | Report Writer |
| 17 (11/2) | Report Writer | Data Analyst | Data Loader |
| 18 (11/4) | Data Loader | Report Writer | Data Analyst |
| 19 (11/9) | Data Analyst | Data Loader | Report Writer |

---

## Schedule and Deliverables

| Class | Topic | In class | Submit (Gradescope) | Due |
|---|---|---|---|---|
| **15** Mon 10/26 | Problem definition and initial decisions | Explore the data, design the program, write the contract | **Part 1: Team Contract** (PDF) | Tue 10/27, 11:59 PM |
| **16** Wed 10/28 | Stub building | Turn the contract into stubs; get `main.py` running end to end | **Part 2: Running Skeleton** (4 `.py` files) | Sun 11/1, 11:59 PM |
| **17** Mon 11/2 | Writing real functions | Replace *your own* stub; test it against teammates' stubs | **Part 3: Real Functions + Tests** | Tue 11/3, 11:59 PM |
| **18** Wed 11/4 | Integrating it all together | Swap in real functions one at a time | **Part 4: Working Program + Report** | Sun 11/8, 11:59 PM |
| **19** Mon 11/9 | Debugging and reflection | Fix planted bugs; team retrospective | **Part 5: Bug Log + Reflection** | Tue 11/10, 11:59 PM |
| **21** Mon 11/16 | Visualizing data | Each person adds one plotting function to the program | Part of Class 21 homework | See Class 21 |

**Submit early and often.** Gradescope keeps every submission. Several submissions showing your code growing over time are expected and count in your favor (see "Use of AI" below).

---

## How You Are Graded

Each Part is worth **20 points**, split into two components:

- **Individual, 15 points (your function):** Does *your* section of the contract, *your* stub, or *your* function meet the requirements? Can you explain it?
- **Team, 5 points (integration):** Does the team's submission as a whole meet the requirements? Do the pieces fit together?

Every Part comes with an explicit checklist of what is required. Use it before you submit.

---

## Rules

1. **Course style rules apply.** No global variables, no `break` or `continue`, and no `while True` loops. Code that uses any of these receives a zero for that function.
2. **Every function has a docstring** that matches the Team Contract.
3. **Only edit your own file.** If you need a change in a teammate's function, ask them. Do not edit their file.
4. **Contract changes are team decisions.** If the contract needs to change, the whole team agrees and the Recorder logs the change in the Decision Log, with the date.

---

## Use of AI

Do not use AI tools to write your function or your contract. Exams 2 and 3 are on paper and will ask you to:

- read a contract
- write a stub
- trace a function
- find a bug

These are exactly the skills this project practices. Expect these checks during the project:

- **In-class spot checks.** A TA points to a line of your function and asks, "Why is this here?"
- **Gradescope history.** Code that develops over several submissions looks very different from code that appears all at once.
- **Debugging tasks.** In Class 19 you will fix bugs in code you have never seen. You can only do that if you understand the code you wrote.

---

## Looking Ahead

- **Class 21 (Python plotting):** each team member adds **one plotting function** to the program you built here, so your team produces three different figures:
  - **Data Loader:** a line plot of one metric over time, with the daily goal shown
  - **Data Analyst:** a bar chart comparing how often each goal was met
  - **Report Writer:** a histogram showing the distribution of one metric
- **Class 22 (Python to MATLAB):** you will reproduce your plot in MATLAB, so you can see the same problem solved in both languages.
