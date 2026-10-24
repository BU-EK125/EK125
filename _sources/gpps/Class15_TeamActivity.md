# Class 15: Team Activity — Define the Problem and Write the Contract

**EK125 Fitness Tracker Project, Part 1** -- see the [Project Overview](https://BU-EK125.github.io/EK125/class/FitnessTrackerProject.html) for the full arc.

Work with your project team of 3. You may use the reading and your notes. Do **not** use AI. Every decision today should come from your team.

**Today runs across both sessions:** the morning class (Parts A-D) and the afternoon lab (Parts E-G).

**Today's goal:** By the end of today, your team has a **Team Contract** precise enough that each of you could write your own function *without ever seeing your teammates' code.*

## Download the Project Data

Download: [fitness_data.csv](fitness_data.csv)

## Download the Team Contract Template

Download: [Team_Contract_Template.md](Team_Contract_Template.md)

**Before you start:**

1. In PyCharm, create a new project folder named `FitnessTracker`.
2. Download `fitness_data.csv` (above) into that folder.
3. One person creates your team's **shared Google Drive folder** (BU account) and shares it with the team. Put `fitness_data.csv` and the Team Contract in it.
4. Open the **Team Contract Template** (above). Today's Recorder types into it while the team talks.

---

# MORNING CLASS (50 minutes)

## Part A: Meet the Data (7 minutes)

Open `fitness_data.csv` in PyCharm and **read it** (double-click it in the project panel). Do not write any code yet. Answer as a team:

**A1.** How many rows of data (days) are in the file? ______

**A2.** List every day that has at least one blank value, and which columns are blank:

| Day | Blank column(s) |
|---|---|
| | |
| | |
| | |

**A3.** If you skip every row that has *any* blank value, how many complete days are left? ______

**A4.** For each metric, is a **higher** number better or a **lower** number better? (Hint: think about what a lower resting heart rate means for fitness.)

| Metric | Higher or lower is better? |
|---|---|
| `steps` | |
| `resting_hr` | |
| `sleep_hours` | |
| `active_minutes` | |

---

## Part B: Design the Program and Divide the Work (8 minutes)

**C1. Claim your functions.** Each person owns one function for the whole project. Write names in **Section 1** of the contract.

| Function owner | Function header (fixed, do not change) | File |
|---|---|---|
| Data Loader | `load_tracker_data(filename)` | `loader.py` |
| Data Analyst | `analyze_metric(data, metric, goal, higher_is_better=True)` | `analyzer.py` |
| Report Writer | `write_report(results_list, filename)` | `reporter.py` |

**C2. Fill in the duty rotation** in Section 1 (Integrator, Tester, Recorder for Classes 15-19).

**C3. Write the main program.** Today's **Integrator** leads this. On paper first, write the lines of Python that `main.py` will run, using the three function headers above. Your main program must:

- load the data from `fitness_data.csv`
- call `analyze_metric` once for **each** metric your team analyzes, and collect every result in a list named `results_list`
- write the report to a file

You do **not** need the functions to exist yet. You are writing the plan. Copy it into **Section 3** of the contract.

> **Hint:** You can call `analyze_metric` four separate times and `.append()` each result. Or you can loop over a list of tuples like `("steps", 8000, True)`. Both are fine. Pick one and write it down.

---

## Part C: Make the Team Decisions (10 minutes)

Decide each of the following together. The Recorder logs each decision in the **Decision Log** (Section 5), with today's date and a one-line reason.

1. **Blank values:** what happens to a row with a blank value? (Reread "[Describing a dictionary of lists](https://BU-EK125.github.io/EK125/class/Class15.html#describing-a-dictionary-of-lists)" in the reading before you decide.)
2. **Metrics and goals:** which metrics will you analyze (at least 3, and `resting_hr` must be one of them)? What is the daily goal for each?
3. **Types:** is `day` stored as an `int` or a `float`? What about the other columns?
4. **Results keys:** what are the exact key names in the dictionary that `analyze_metric` returns? It must include at least the average, minimum, maximum, best day, and number of days the goal was met. **Report Writer:** what *else* do you need in order to write the report? Ask for it now.
5. **Rounding:** does `analyze_metric` round, or does `write_report` round? To how many decimal places?
6. **Ties:** if two days tie for the best value, which day is reported?
7. **Report:** what is the report's file name, and what will it look like? Sketch 3-4 lines.

---

## Part D: Draft Your Own Contract Section (15 minutes)

In **Section 4**, each owner writes the full docstring contract for their own function. Every contract needs all five parts from the reading:

- [ ] **Name and header** (copied exactly)
- [ ] **Parameters:** each one with its type, units, and an example
- [ ] **Returns:** type, exact structure (every key, if it's a dictionary), and **a concrete example value** (you can fill this in during lab)
- [ ] **Side effects:** does it print? Write a file? Change its input?
- [ ] **Assumptions and messy cases:** what must be true of the input? What happens with blank values?

**The two seams to get right:**

- The **Data Loader**'s *Returns* and the **Data Analyst**'s `data` *parameter* must describe the **same** dictionary.
- The **Data Analyst**'s *Returns* and the **Report Writer**'s `results_list` *parameter* must use the **same** key names.

Before you leave, read each other's sections and check these two seams. Don't worry about the **Example** values yet. You'll work those out in lab.

---

# AFTERNOON LAB (50 minutes)

## Part E: Work Out the Expected Answers by Hand (about 20 minutes, together)

We'll work through this as a class, step by step.

**Warm-up: what does Python actually see?**

**W1.** When Python reads line 2 of this file, it gets the string `"1,8478,61,8.1,50\n"`. After `.strip().split(",")`, what list do you get? Are the items numbers or strings?



**Answer:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_


**W2.** What does the line for Day 9 become after `.strip().split(",")`?



**Answer:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Now the functions.** Using **only Days 1-5** of `fitness_data.csv`, work out by hand (calculator allowed) what your functions should produce:

1. **Data Loader:** write the exact dictionary `load_tracker_data` would return for a file containing only Days 1-5.
2. **Data Analyst:** using that dictionary, write the exact dictionary `analyze_metric` would return for `steps` with your goal. Then do the same for `resting_hr` with your goal (remember: **lower** is better).
3. **Report Writer:** write the exact report text `write_report` would produce from those two results.

Put these into your contract as the **Example** values. **Keep this work.** In Class 17, these hand-calculated answers become your **test cases**: they're how you'll know your real function is correct.

---

## Part F: Contract Stress Test (10 minutes)

Swap Team Contracts with a neighboring team. Using **only their contract**, without talking to them, answer these on a sheet of paper:

1. Write the line of code that loads their data file.
2. Write the line of code that analyzes `steps` with their goal.
3. Write the line of code that prints the **average** from that result.
4. Write the **exact value** their `load_tracker_data` would return if the file contained only Days 1 and 2.
5. List **every question** you wanted to ask them because their contract didn't say.

Return the sheet. **Your team's job:** for every question the other team listed, add the missing detail to your contract. Log any changes in the Decision Log.

> A perfect contract gets **zero** questions in this stress test. Each question you receive shows something your own teammates might have guessed wrong.

---

## Part G: Finish the Contract (remaining time)

1. Answer the four problem-definition questions in **Section 2**: What goes in? What comes out? What counts as success (how would you check the report is right)? What is messy (use Part A)?
2. Fix everything the stress test turned up, and log changes in the Decision Log.
3. Fill in the working agreement (Section 6).
4. Go through the submission checklist at the end of the template.

---

## Before You Leave Lab

- [ ] Every section of the Team Contract has a draft, including Example values
- [ ] Each person knows which function they own and which duty they have in Class 16
- [ ] Your team has agreed on a communication plan (Section 6)

**Homework:** Finish the Team Contract. The Recorder submits it as a **PDF** to Gradescope (**Fitness Tracker Part 1: Team Contract**) as a group submission with all three names, by **Tuesday 10/27, 11:59 PM.** Use the checklist at the end of the template before submitting.

**Next class (Class 16):** you'll turn this contract into **stubs** and get the whole program running before any real code is written.
