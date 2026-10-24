# Class 19: Team Activity — Bug Hunt and Retrospective

**EK125 Fitness Tracker Project, Part 5**

Work with your project team. You may use the readings and your notes. Do **not** use AI. Exam 2 (Friday 11/13) will ask you to find and fix bugs on paper, so do the thinking yourselves.

**Today's goal:** Find and fix all five bugs in another team's program, then look back honestly at how your own team worked.

**Today's duties:**

| Duty | Who (by function) |
|---|---|
| **Integrator** | Data Analyst (runs Team 7's program) |
| **Tester** | Data Loader (compares output to the expected report) |
| **Recorder** | Report Writer (keeps the Bug Log, submits) |

---

# MORNING CLASS (50 minutes)

## Part A: The Bug Hunt (35 minutes)

Download the **Team 7 Bug Hunt** folder below into a **new, separate** PyCharm folder. Don't mix it with your own files!

### Download the Team 7 Bug Hunt

Download: [loader.py](class19_team7_bug_hunt/loader.py), [analyzer.py](class19_team7_bug_hunt/analyzer.py), [main.py](class19_team7_bug_hunt/main.py), [reporter.py](class19_team7_bug_hunt/reporter.py), [expected_report.txt](class19_team7_bug_hunt/expected_report.txt), and [fitness_data.csv](fitness_data.csv)

Team 7 built the same Fitness Tracker program with the **same contract** your instructor used as the model. Their code looks different from yours. Their program has **five bugs**:

- **three** stop the program with an error message
- **two** let it run but give **wrong answers**

The folder also contains `expected_report.txt`: the **correct** report for `fitness_data.csv`. When Team 7's program produces exactly that report, you've found all five.

### How to work

Use the method from the reading:
1. **Reproduce:** run `main.py`.
2. **Locate:** read the traceback bottom-up, or compare the output to the expected report.
3. **Hypothesize:** read the **contract** (the docstring) before the code.
4. **Change ONE thing.**
5. **Run again.**

The Integrator types, but **everyone** reads the code and the tracebacks. Take turns proposing the hypothesis.

> **For the two silent bugs:** once the program runs, compare `fitness_report.txt` to `expected_report.txt` line by line. For each line that's different, ask: which function produced this value? Print at the seam, or print inside the loop, to find where it first goes wrong.

### Bug Log (Recorder fills in)

| # | Symptom (error's last line, or wrong value) | Kind (syntax / runtime / logic) | File and line | Cause (what the code did vs. what the contract says) | Fix | How you found it |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |

---

## Part B: Debrief (10 minutes, whole class)

Be ready to answer:

1. Which bug's error message appeared in a **different file** (or on a different line) from where the mistake actually was?
2. Team 7 ran the Days 1–5 test file and their `resting_hr` numbers looked right. Why didn't that test catch the `resting_hr` goal-counting bug?
3. Which of the five bugs would your **own** team's tests have caught?

## Wrap-Up (5 minutes)

- [ ] The Recorder saves the Bug Log to your shared Drive folder
- [ ] The Recorder makes a Gradescope submission of the Bug Log so far

---

# AFTERNOON LAB (50 minutes)

## Part C: Walkthrough — Hunting Silent Bugs (about 15 minutes, together)

We'll debug Team 7's two logic bugs live, using:
- print-at-the-seam
- a trace table printed from inside a loop
- (optionally) the PyCharm debugger

Follow along. These are the skills Exam 2 tests on paper.

---

## Part D: Add a Regression Test to Your Own Function (10 minutes, each person)

In **your own** file (your team's real project), add **one new `check()` test** that guards against a bug like one of today's:

| Role | Ideas |
|---|---|
| **Data Loader** | A test file where the **first** or **last** data row has a blank; a row where only one value is blank |
| **Data Analyst** | A value **exactly equal to the goal** for *both* directions; day numbers with a gap, so position ≠ day |
| **Report Writer** | Check that the "Days analyzed" line contains the **number** of days (catches str + int mistakes); check every metric appears |

Above the test, write a comment naming the bug it guards against:

```python
    # Regression test: guards against counting with < instead of <=
```

Run your file. The new test must **PASS** on your code. Upload to Drive.

---

## Part E: Team Retrospective (15 minutes, Recorder writes it down)

Open your integration log and Decision Log. They're your evidence. Fill in **at least two items** in each column. Every item must be **specific** and **blame the process, not a person**.

| Continue (worked well) | Stop (caused problems) | Start (try next time) |
|---|---|---|
| 1. | 1. | 1. |
| 2. | 2. | 2. |

Then answer together:

1. Which **contract decision** saved your team the most trouble?
2. Which decision did you **get wrong or leave out**? When did you find out?
3. If you started this project over tomorrow, what's the **one thing** you'd do differently in Class 15?

---

## Part F: Start Your Individual Reflection (remaining time)

Begin your individual reflection (prompts below). Finish it for homework.

---

## Homework: Fitness Tracker Part 5, Bug Log and Reflection

**Due Tuesday 11/10, 11:59 PM.**

**Team (the Recorder submits, group submission):**
- Bug Log (all five bugs) and the fixed Team 7 files
- Team retrospective (Part E)

**Individual (each person submits their own):**
- Your file from your team's project, with your new regression test (Part D)
- Your **individual reflection**: about 300 words, answering **all five** prompts, with specific examples

### Individual reflection prompts

1. **The contract.** Which decision in your Team Contract helped *you* most when writing your function? Give a specific example.
2. **A miss.** Which decision did your team get wrong, or leave out? How and when did you discover it (stub, test, integration, or clinic)?
3. **A bug.** Describe one bug in your function or at your seam: how you found it, what caused it, and how you fixed it. If you had none, describe the test that gave you the most confidence, and why.
4. **Stubs and tests.** How did writing stubs and tests first change the way you worked, compared with earlier homework in this course?
5. **Next time.** You'll work in teams again for Project 2 in MATLAB. Name one specific thing you'll do differently.

### Submission checklist

- [ ] Bug Log: all five bugs with kind, location, cause, fix, and how found (team)
- [ ] Fixed Team 7 program produces `expected_report.txt` exactly (team)
- [ ] Retrospective: at least 2 specific items per column, plus the 3 questions (team)
- [ ] Regression test in your own file, with a comment naming the bug it guards against; it PASSES (individual)
- [ ] Reflection: all 5 prompts, specific examples, about 300 words (individual)

**What's next:**
- **Class 20:** Exam 2 practice.
- **Class 21:** each of you adds a plotting function to your team's program.
