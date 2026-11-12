# Class 18: Team Activity — Integrate, One Piece at a Time

**EK125 Fitness Tracker Project, Part 4**

Work with your project team. You may use the readings, your notes, and your Team Contract. Do **not** use AI.

**Today's goal:** By the end of today, `main.py` runs with **all three real functions** on the full data set, and the report agrees with the data facts.

**Today's duties:**

| Duty | Who (by function) |
|---|---|
| **Integrator** | Data Loader |
| **Tester** | Report Writer |
| **Recorder** | Data Analyst |

**Before you start:**
- The **Integrator** makes a new PyCharm folder called `Integration`.
- Copy in `main.py`, `check_seams.py`, `fitness_data.csv`, `test_days1to5.csv`, and the **Class 16 stub versions** of all three files. Drive's *Manage versions* has them, or teammates can re-upload them with "stub" in the name.
- Everyone else: make sure your latest real file is in the shared Drive folder.

---

# MORNING CLASS (50 minutes)

## Integration Log

The **Recorder** fills this in during every step. Use the expected values from your Class 15 hand calculations (Days 1–5).

| Step | Real functions | Data file | Matches expected? | What broke (last line of error, or wrong value) | Cause | Fix (who) |
|---|---|---|---|---|---|---|
| 0 | none (all stubs) | Days 1–5 | | | | |
| 1 | Loader | Days 1–5 | | | | |
| 2 | Loader + Analyst | Days 1–5 | | | | |
| 3 | all three | Days 1–5 | | | | |
| 4 | all three | **full file** | | | | |

---

## Step 0: Confirm the Skeleton Still Runs (3 minutes)

In `main.py`, **temporarily** change the data file to `"test_days1to5.csv"`. Run `main.py` with all three stubs. It should run exactly as it did in Class 16.

## Step 1: Swap In the Real Loader (8 minutes)

1. The **Integrator** replaces the Loader stub with the real `loader.py` from Drive.
2. Run `main.py`, then run `check_seams.py` (also pointed at `test_days1to5.csv`).
3. The **Tester** compares Seam 1 (Loader → Analyst) to the Class 15 hand-calculated dictionary: the keys, the lengths (5 each), and the values.

> The report itself won't change yet, because the Analyst is still a stub. That's expected! At this step you're checking the **seam**, not the report.

## Step 2: Swap In the Real Analyst (8 minutes)

1. Replace the Analyst stub with the real `analyzer.py`.
2. Run `main.py` and `check_seams.py`.
3. **Tester:** compare one result dictionary at Seam 2 to the Class 15 expected values, key by key. Steps should give: average 8327.8, minimum 4569.0, maximum 12192.0, best day 5. Goal-related numbers depend on your goals.

## Step 3: Swap In the Real Report Writer (8 minutes)

1. Replace the Report Writer stub with the real `reporter.py`.
2. Run `main.py`. Open the report.
3. **Tester:** compare it to the example report in your contract (Section 4c), line by line.

## Step 4: The Full Data Set (8 minutes)

Change the data file in `main.py` back to `"fitness_data.csv"`. Run it. The **Tester** fills in the table below from your report and compares each value to the **data facts**. These facts don't depend on your team's goals.

| Data fact (from `fitness_data.csv`) | Correct value | Your report |
|---|---|---|
| Days analyzed (complete days) | **25** | |
| Steps: average (1 decimal) | **8843.4** | |
| Steps: minimum / maximum | **4569 / 14773** | |
| Steps: best day (higher is better) | **Day 27** | |
| Resting HR: average | **63.0** | |
| Resting HR: minimum / maximum | **58 / 67** | |
| Resting HR: best day (lower is better) | **Day 14** | |
| Sleep hours: minimum / maximum | **5.7 / 8.9** | |
| Sleep hours: best day | **Day 7** | |
| Active minutes: average | **41.4** | |
| Active minutes: best day | **Day 7** | |

If your team analyzes a different set of metrics, check the ones you have. If your contract rounds differently, the averages may differ in the last digit, and that's fine.

## Wrap-Up (5 minutes)

- [ ] The **Integrator** uploads the final `main.py` (pointed at `fitness_data.csv`) and `check_seams.py` to Drive
- [ ] The **Recorder** updates the Decision Log with **every** contract change made today, with dates
- [ ] The **Recorder** makes a Gradescope submission

**If something broke:** remember the rules. Read the traceback bottom-up. Ask "which seam?" Let the contract decide who's off-contract. Only the owner edits their file.

---

# AFTERNOON LAB (50 minutes)

## Part A: Integration Clinic — "It Runs. Is It Right?" (about 20 minutes)

Download the **Integration Clinic** folder below into a **new, separate** PyCharm folder.

### Download the Integration Clinic

Download: [loader.py](class18_integration_clinic/loader.py), [analyzer.py](class18_integration_clinic/analyzer.py), [main.py](class18_integration_clinic/main.py), [reporter.py](class18_integration_clinic/reporter.py), and [fitness_data.csv](fitness_data.csv)

Another team's program runs perfectly, with no errors. Run `main.py` and open the report.

1. Compare their report to the **data facts** table above. List every value that's wrong:

| Report line | Their value | Correct value |
|---|---|---|
| | | |
| | | |
| | | |

2. **Find the seam.** Add seam prints (type, keys, **lengths**) after `load_tracker_data`. What do you notice?

3. **Find the bug.** Which function is off-contract? Which line of code causes the problem? (Read the contract in its docstring!)

4. **Explain it.** In one or two sentences: why does this bug make the best day for steps come out as **Day 25** instead of **Day 27**, even though the maximum step count (14773) is correct?

5. **Fix it**, run again, and confirm every data fact matches.

---

## Part B: Finish Your Own Integration (remaining time)

1. Finish any step of your integration that isn't complete. Every row of your log should say "Yes" in *Matches expected?*
2. Run each team member's tests one more time (`python loader.py`, etc.). Do they all still PASS? If your team changed the contract today, update your tests too.
3. **Write a reasonableness check into `check_seams.py`:** after loading the full file, use `check()` (or an `if`) to confirm that **all five lists have the same length** and that **the length is 25**.
4. Upload everything to Drive.

---

## Homework: Fitness Tracker Part 4, Working Program

**The Recorder submits to Gradescope** (group submission, all names) by **Sunday 11/8, 11:59 PM**:

- `loader.py`, `analyzer.py`, `reporter.py`, `main.py` (pointed at `fitness_data.csv`)
- `check_seams.py`, including the reasonableness check from Part B
- `fitness_report.txt`: the report from the full data
- Integration log (this page, steps 0–4) and an updated Team Contract with the Decision Log (PDF)

### Submission checklist

**Your file (each person checks their own):**

- [ ] Your function works in the integrated program on the full data
- [ ] Every value crossing your seam matches the contract (type, keys, lengths)
- [ ] Any fixes you made today are in the integration log, with the cause
- [ ] Your docstring matches the **final** contract
- [ ] Your tests still PASS against the final contract
- [ ] No `global`, `break`, `continue`, or `while True`

**Team:**

- [ ] `main.py` runs on `fitness_data.csv`, and the report matches the data facts
- [ ] The integration log is complete for steps 0–4
- [ ] The Decision Log records every contract change, with dates

**Next class (Class 19):** you'll hunt down five bugs in a program you've never seen, then look back on how your team's project went.
