# Class 17: Team Activity — Replace Your Stub with Real Code

**EK125 Fitness Tracker Project, Part 3**

Work with your project team. You may use the readings, your notes, and your Team Contract. Do **not** use AI. You will be asked to explain your code line by line.

**Today's goal:** By the end of today, your **own** function is real code that passes your own tests, and `main.py` still runs.

**Today's duties:**

| Duty | Who (by function) |
|---|---|
| **Integrator** | Report Writer |
| **Tester** | Data Analyst |
| **Recorder** | Data Loader |

**Before you start:** Download the latest files from your shared Google Drive folder into your PyCharm `FitnessTracker` folder. Have your Class 15 hand calculations (Days 1–5) in front of you.

---

# MORNING CLASS (50 minutes)

## Part A: Write Your Tests First (10 minutes, each person)

In **your own file**, below your function:

1. Add the `check(test_name, expected, actual)` function from the reading.
2. Replace your Class 16 stub test with a test function containing **at least three** `check()` calls:

| Role | Test 1: normal case (from Class 15) | Test 2: edge case | Test 3: edge case |
|---|---|---|---|
| **Data Loader** | Days 1–5 file → the exact dictionary you calculated | A file with a blank row → that day is skipped | The real file → every list has 25 entries |
| **Data Analyst** | Days 1–5 `steps` → the exact results dictionary | Days 1–5 `resting_hr` with `higher_is_better=False` | A **tie**, a value **exactly equal to the goal**, *or* day numbers with a gap (e.g., days `[1, 3, 4]`) |
| **Report Writer** | Two results dictionaries → the report contains the right lines | Your function returns `None` | The first line of the file is your report title |

**Data Loader:** make your tiny test files now (right-click the project → *New → File*):
- `test_days1to5.csv`: the header line plus Days 1–5, copied from `fitness_data.csv`
- `test_with_blank.csv`: the header line plus 3 rows, where the middle row has a blank

**Data Analyst:** build your test dictionaries by hand in the test function. You don't need the Loader's code.

**Report Writer:** build two results dictionaries by hand. After calling `write_report`, open the file, read it back, and check for key phrases with `in`.

**Run your tests now, while your function is still a stub.** Most of them should **FAIL**. That proves your tests can catch something.

---

## Part B: Write the Real Code (22 minutes, each person)

Replace your stub body with real code, **one pseudocode step at a time**:

1. Write the code for **one** pseudocode comment (keep the comment).
2. Run your file. Read the PASS/FAIL output.
3. Repeat.

When all your tests PASS, you're done with this part.

**Tester check-in (about 11 minutes in):** the **Tester** spends 3 minutes reading **one** teammate's code next to their contract section. The Tester asks:
- Does the function still return **exactly** the type, structure, and keys the contract promises?
- Do the messy cases in the contract (blank rows, ties, lower-is-better) appear somewhere in the code or tests?

Write anything you find here:

| Teammate's function | Issue found | Fixed? |
|---|---|---|
| | | |
| | | |

**Rules:** no `global`, `break`, `continue`, or `while True`. Use readable variable names. Keep your pseudocode comments.

---

## Part C: Does `main.py` Still Run? (6 minutes, Integrator leads)

Each person uploads their file to the shared Drive folder, **even if it isn't finished**. A file whose stub body is still in place is fine, as long as it runs.

The **Integrator** downloads all the files and runs `main.py`.

- **If it runs:** open the report. Which numbers are now real?
- **If it crashes:** read the last line of the error. Which seam? Whose function broke a promise? The owner fixes their own file.

| Function | Real or stub right now? | `main.py` runs with it? |
|---|---|---|
| `load_tracker_data` | | |
| `analyze_metric` | | |
| `write_report` | | |

---

## Wrap-Up (4 minutes)

- [ ] Every file is uploaded to Drive (no duplicate copies)
- [ ] The **Recorder** makes a Gradescope submission of what you have now

---

# AFTERNOON LAB (50 minutes)

## Part D: Walkthrough — The Two Trickiest Functions (about 20 minutes, together)

We'll build these together, from pseudocode to code:

1. **The Loader's skip-the-row logic.** What does a blank value look like after `.strip().split(",")`? How do you check a whole row at once?
2. **The Analyst's best-day loop.**
   - How do you track "best so far"?
   - What changes when `higher_is_better` is `False`?
   - How do you turn a list **position** into a **day number**?
3. **Report Writer tip:** formatting numbers with f-strings, e.g., `f"{value:.1f}"`.

Follow along in your own file **only if it's your function.** Everyone else: take notes. You'll need to read and understand this code in Classes 18 and 19, and on Exam 2.

---

## Part E: Finish, Test, and Explain (remaining time)

1. Finish your real function until all your tests PASS.
2. **Add one more test** that you think is the most likely to catch a bug in *your* function.
3. **Explain it to a teammate:** take turns. Each person explains their function to another teammate, line by line, in under 3 minutes. The listener asks at least one "why" question. (TAs will also come around and ask.)
4. Upload your final file to Drive. Run `main.py` one more time.

---

## Homework: Fitness Tracker Part 3, Real Functions and Tests

**The Recorder submits to Gradescope** (group submission, all names) by **Tuesday 11/3, 11:59 PM**:

- `loader.py`, `analyzer.py`, `reporter.py`, `main.py`
- The Loader's test files (`test_days1to5.csv`, `test_with_blank.csv`)
- `test_results.txt`: the PASS/FAIL output from running **each** of the three files, pasted together into one text file

**Submit more than once as you go.**

### Submission checklist

**Your file (each person checks their own):**

- [ ] Real function keeps every promise in the contract: header, return type, structure, keys
- [ ] Handles the messy cases in the contract
- [ ] `check()` function plus a test function with **at least 3** tests: the Class 15 normal case and **2 edge cases**, with expected values worked out by hand
- [ ] All tests PASS
- [ ] Pseudocode comments kept; readable variable names
- [ ] Tests run only under `if __name__ == "__main__":`
- [ ] No `global`, `break`, `continue`, or `while True`

**Team:**

- [ ] `main.py` runs with all three files
- [ ] Running `main.py` doesn't print anyone's test output
- [ ] `test_results.txt` includes the output from all three files

**Next class (Class 18):** you'll put all three real functions together, one at a time, and check the results against the full data set.
