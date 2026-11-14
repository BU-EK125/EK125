# Class 16: Team Activity — Build a Running Skeleton

**EK125 Fitness Tracker Project, Part 2**

Work with your project team. You may use the reading, your notes, and your Team Contract. Do **not** use AI.

**Today's goal:** By the end of today, `main.py` runs from start to finish and writes a (fake) report, using only stubs. Every value that crosses a seam matches your contract.

**Today's duties:**

| Duty | Who (by function) |
|---|---|
| **Integrator** | Data Analyst |
| **Tester** | Data Loader |
| **Recorder** | Report Writer |

**Before you start:** Open your team's shared Google Drive folder and your Team Contract. Make sure everyone has `fitness_data.csv` in their own PyCharm `FitnessTracker` folder.

---

# MORNING CLASS (50 minutes)

## Part A: Write Your Stub (12 minutes, each person)

In your own PyCharm `FitnessTracker` folder, create **your** file (`loader.py`, `analyzer.py`, or `reporter.py`) and write a faithful stub.

Your file must contain, in this order:

1. **A file docstring** at the top: file name, your role, your name, and "STUB VERSION."
2. **Your function**, with the header and docstring copied **exactly** from Section 4 of your Team Contract.
3. **A stub body** that follows the five rules:
   - [ ] returns the contract's **example value**: right type, right structure, every key
   - [ ] uses a parameter directly where that's easy (Data Analyst: `metric` and `goal`)
   - [ ] **returns**; never prints instead
   - [ ] Report Writer: writes a placeholder file that looks up **every key** the real report will use
   - [ ] no `global`, `break`, `continue`, or `while True`
4. **A test function** (`test_loader`, `test_analyzer`, or `test_reporter`) that calls your function once and prints the `type()` and keys of the result. The Report Writer's test writes a test report instead.
5. **The test call**, under `if __name__ == "__main__":`

**Run your file directly** (green arrow). Check the output against your contract. Then **upload your file** to the shared Drive folder.

> **Data Analyst hint:** Your test function needs a `data` dictionary to pass in. Build a tiny one by hand, such as `{"day": [1, 2], "steps": [8478.0, 9430.0]}`. You don't need the Loader's file to test your stub.

---

## Part B: Assemble and Run the Skeleton (10 minutes, Integrator leads)

1. **Integrator:** download all three files from the Drive folder into one PyCharm folder.
2. Create `main.py` from **Section 3** (Main Program Plan) of your contract. Put your main program inside a function named `main()`, and call it under `if __name__ == "__main__":`.
3. **Run `main.py`.** Then open the report file it created.

**If it crashes:** read the **last line** of the error first, then use the table in Part 6 of the reading. Write each error and its fix in the log below (the Recorder keeps it). Remember: **only a file's owner edits that file.** The owner fixes it, re-uploads it, and the Integrator downloads it again.

| # | Error (last line) | Which seam / file? | Cause | Fixed by (owner) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

**Success looks like:** the program runs with no errors and the report file exists, even though every number in it is fake.

---

## Part C: Check the Seams (13 minutes, Tester leads)

A running program can still break the contract. The **Tester** makes a copy of `main.py` named `check_seams.py` and adds a temporary `print` after each function call:

- After `load_tracker_data`: print the `type()`, the list of keys, and `len()` of the `"day"` list and one other list
- After **one** call to `analyze_metric`: print the `type()` and the list of keys
- After building `results_list`: print `len(results_list)`

Run `check_seams.py` and fill in the table. In the **Contract says** column, copy what your contract promises.

| Seam | Check | Contract says | Program shows | Match? |
|---|---|---|---|---|
| Loader → Analyst | type of `data` | | | |
| Loader → Analyst | keys of `data` | | | |
| Loader → Analyst | all lists the same length? | | | |
| Analyst → Report Writer | type of one result | | | |
| Analyst → Report Writer | keys of one result | | | |
| Analyst → Report Writer | length of `results_list` | | | |

For **every "No"**, decide as a team: **is the stub wrong, or is the contract wrong?**
- If the stub is wrong, its owner fixes it.
- If the contract is wrong, the Recorder updates the contract **and** logs the change in the Decision Log.

At the bottom of `check_seams.py`, paste the output from your final run inside a comment block (`"""..."""`).

---

## Wrap-Up (5 minutes)

- [ ] All four files (`loader.py`, `analyzer.py`, `reporter.py`, `main.py`) are in the shared Drive folder, with no duplicate copies
- [ ] The **Recorder** makes a first Gradescope submission of what you have right now. It doesn't need to be finished. This is your starting point for code-evolution tracking.

---

# AFTERNOON LAB (50 minutes)

## Part D: Diagnose a Broken Skeleton (about 20 minutes)

We'll start with a short demo together. Then download the **Broken Skeleton** folder below into a **new, separate** PyCharm folder. Don't mix these files with your own!

### Download the Broken Skeleton

Download: [loader.py](class16_broken_skeleton/loader.py), [analyzer.py](class16_broken_skeleton/analyzer.py), [main.py](class16_broken_skeleton/main.py), [reporter.py](class16_broken_skeleton/reporter.py), and [fitness_data.csv](fitness_data.csv)

Someone else's team built this skeleton for the same project, and it has **three bugs**. Each bug is in a different place. Run `main.py`, fix **one** bug at a time, run again, and record each one:

| # | Error message (last line) | File and line | What was wrong | How you fixed it |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

When `main.py` runs and writes a report, you're done. Then answer:

1. Which of the three bugs could a **faithful stub** have prevented? Which rule from the reading would have prevented each one?
2. Which bug produced an error message on a line that was **not** where the real mistake was? Why did that happen?

---

## Part E: Finish and Prepare for Class 17 (remaining time)

1. **Finish anything left from the morning:** the skeleton runs, `check_seams.py` is complete, and every "No" is resolved.
2. **Pseudocode for your real function (each person).** In your own file, *above* your stub body, write comments describing the steps your real function will take. Write one comment per step, in plain English. For example, for the weather station's `read_temperatures`:

```python
    # PLAN:
    # 1. Make an empty list for the temperatures
    # 2. Open the file for reading
    # 3. For each line in the file:
    #      a. strip the newline
    #      b. if the line is not blank and not "-999", convert it to float and add it to the list
    # 4. Return the list
```

Your pseudocode must handle the messy cases your contract describes. **Leave the stub body in place.** The program must still run.

3. Upload your updated file to Drive.

---

## Homework: Fitness Tracker Part 2, Running Skeleton

**The Recorder submits to Gradescope** (group submission, all names) by **Sunday 11/1, 11:59 PM**:

- `loader.py`, `analyzer.py`, `reporter.py`, `main.py`
- `check_seams.py`, with your final seam-check output pasted in a comment at the bottom
- An updated Team Contract (PDF), **only** if your contract changed today

**Submit more than once as you go.** Gradescope keeps your history.

### Submission checklist

**Your file (each person checks their own):**

- [ ] File docstring with role, name, and "STUB VERSION"
- [ ] Header and docstring match the Team Contract exactly
- [ ] Stub returns the contract's example value: right type, structure, and keys
- [ ] Uses easy parameters directly; never prints instead of returning (Report Writer: looks up every key)
- [ ] Test function, called only under `if __name__ == "__main__":`, runs without errors
- [ ] Pseudocode comments for the real function, including the messy cases
- [ ] No `global`, `break`, `continue`, or `while True`

**Team:**

- [ ] `main.py` runs from start to finish with no errors, using all three stubs
- [ ] The report file is created
- [ ] `check_seams.py` checks both seams, and every check matches the contract

**Next class (Class 17):** you'll replace **your own** stub with real code, and test it against the Days 1–5 answers you worked out by hand in Class 15.
