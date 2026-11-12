# Class 18: Integrating It All Together

## Learning Objectives

By the end of this reading, you should be able to:

- Plan an integration that adds **one real function at a time**
- Run the program on a small file with known answers before running it on the real data
- Read a traceback that passes through several files, and find where the error **started**
- Use **reasonableness checks** to catch a program that runs but gives wrong answers
- Decide whether to fix the **code** or the **contract** when two pieces disagree
- Keep an **integration log**

**New syntax today:** none.

---

## Part 1: One Bulb at a Time

You're stringing holiday lights. Ten bulbs are burned out, so you buy ten new ones, replace all ten at once, and plug the string in. It's still dark. Which bulb is the problem? It could be any of the ten, or more than one.

Now try it differently: replace **one** bulb, plug in, check. Replace the next, plug in, check. The moment the string goes dark, you know exactly which bulb caused it.

Integration works the same way. Your team has three real functions. You *could* drop them all in and run `main.py`. But if it crashes, or worse, runs and gives the wrong answer, you won't know which piece caused it.

> **Key idea:** Add one real function at a time, and run after every change. When something breaks, it was the last thing you added.

---

## Part 2: The Integration Plan

### Order: follow the data

Data flows Loader → Analyst → Report Writer, so integrate in the same order:

| Step | Real functions | Stubs | Why this order |
|---|---|---|---|
| 0 | none | all three | Your Class 16 skeleton. It should still run. |
| 1 | Loader | Analyst, Report Writer | Everything downstream depends on the data being right |
| 2 | Loader, Analyst | Report Writer | Now the numbers are real |
| 3 | all three | none | The real report |

After **every** step: run `main.py`, run `check_seams.py`, and compare the output to what you expect.

### Start small: the Days 1–5 file

Here's the trick that makes integration much easier. **Run `main.py` on your small test file first**, not the real data:

```python
data = load_tracker_data("test_days1to5.csv")    # temporarily
```

You worked out the correct answer for Days 1–5 by hand in [Class 15](https://BU-EK125.github.io/EK125/gpps/Class15_TeamActivity.html#part-e-work-out-the-expected-answers-by-hand-about-20-minutes-together). So after each step, you know **exactly** what the report should say. Only after the small file works perfectly do you switch to `fitness_data.csv`.

---

## Part 3: Reading a Traceback That Crosses Files

When an error happens inside a function, Python shows the **traceback**: the chain of calls that led there. With several files, it can look intimidating:

```
Traceback (most recent call last):
  File "main.py", line 30, in <module>
    main()
  File "main.py", line 25, in main
    write_report(results_list, "fitness_report.txt")
  File "reporter.py", line 31, in write_report
    f"(met on {results['days_meeting_goal']} of "
KeyError: 'days_meeting_goal'
```

Read it **from the bottom up**:

1. **Last line: what went wrong.** `KeyError: 'days_meeting_goal'`. A dictionary doesn't have that key.
2. **The block just above it: where it happened.** In `reporter.py`, line 31, inside `write_report`.
3. **The blocks above that: how we got there.** `main.py` called `main()`, which called `write_report(...)`.

### Where it crashed is not always where the bug is

The crash happened in the **Report Writer's** file. But the dictionary that's missing the key was **made by the Analyst**. So there are two possibilities:

- The Analyst's function returns the wrong key name. The Analyst is off-contract.
- The Report Writer asks for the wrong key name. The Report Writer is off-contract.

**The contract decides.** Look up the Analyst's *Returns* section. If it says `"days_meeting_goal"`, the Analyst needs to fix their code. If it says something else, the Report Writer does.

> **Key idea:** The error appears where a bad value is **used**. The bug is often where that value was **created**. Follow the value back across the seam, and let the contract decide who's wrong.

---

## Part 4: "It Runs" Is Not the Same as "It's Right"

The most dangerous moment in integration is when the program **runs with no errors** for the first time. It feels like you're done. You may not be.

### A program that runs and lies

Suppose the weather station reader skipped blank lines but forgot about `-999`. With the readings 71.2, 70.8, 72.5, -999 and 71.9, the program runs fine and prints:

```
Average: -142.5 F
Low:     -999.0 F
```

No error message. But nobody in Boston has ever recorded a temperature of −999°F. A program can't tell you its answer is ridiculous. **You** have to check.

### Reasonableness checks

When you don't know the exact right answer, you can still check whether an answer is **possible**:

| Check | Question to ask | Fitness tracker example |
|---|---|---|
| **Counts** | Is the number of items what it should be? | 28 rows minus 3 incomplete rows = **25** days analyzed |
| **Lengths** | Are lists that should match the same length? | `len(data["day"]) == len(data["steps"])` |
| **Ranges** | Are values physically possible? | Resting heart rate between about 40 and 100 bpm; sleep between 0 and 24 hours |
| **Consistency** | Do related numbers agree? | Average between minimum and maximum; days meeting goal ≤ days analyzed |
| **Cross-check** | Does one result agree with the raw data? | Find the best step day's row in the CSV. Does its step count equal the maximum? |

The last one is powerful. If the report says the best step day is Day 25, open the CSV and look at Day 25. If its step count isn't the maximum, something is wrong, even though the program ran perfectly.

### Data facts

Your instructor will give you a short list of **data facts** for `fitness_data.csv`: numbers that don't depend on your team's goals or decisions (such as the number of complete days and the maximum step count). Compare your final report against them.

---

## Part 5: Fix the Code, or Fix the Contract?

When two pieces disagree, someone has to change something. Ask in this order:

1. **What does the contract say?** If one side matches the contract and the other doesn't, the side that doesn't match gets fixed. That owner fixes their own file.
2. **Is the contract unclear or silent?** Maybe it never said what happens on a tie, or whether `goal` is an int or a float. Then the **team** decides. The Recorder updates the contract and adds a dated line to the Decision Log. *Then* the code changes to match.
3. **Is the contract wrong?** Maybe you discover the Report Writer needs a value the Analyst never promised. Same as #2: the team agrees, the contract is updated, and then the code changes.

Never "just fix it" quietly in your own file to work around a teammate's mistake. A workaround hides the problem, and the next person to use that function will hit it again.

---

## Part 6: The Integration Log

Engineers keep logs so that problems, and their solutions, aren't forgotten. Your **integration log** records every step:

| Step | Real functions | Data file | Matches expected? | What broke | Cause | Fix (who) |
|---|---|---|---|---|---|---|
| 1 | Loader | Days 1–5 | Yes | — | — | — |
| 2 | Loader + Analyst | Days 1–5 | No | `best_day` was 4 for steps | Returned position, not day number | Analyst: use `days[best_index]` |

The log turns "we fixed some stuff" into evidence of exactly what your team found and how. You'll use it in Class 19's reflection.

---

## Summary: Key Concepts

- **One at a time:** add one real function, run, check. Repeat.
- **Follow the data:** Loader, then Analyst, then Report Writer.
- **Start small:** use the Days 1–5 file first, where you know the exact answer.
- **Tracebacks:** read bottom-up (what, then where, then how we got there). The bug is often upstream, where the value was created.
- **Reasonableness checks:** counts, lengths, ranges, consistency, cross-checks.
- **Code or contract?** The contract decides. If it's unclear, the team decides, updates the contract, logs it, and then the code changes.
- **Integration log:** a written record of each step, what broke, and why.

---

## Check Your Understanding

1. Why integrate one function at a time instead of all three at once?
2. Why run on the Days 1–5 file before the full data file?
3. In the traceback in Part 3, which file and function did the crash happen in? Which teammate's function *created* the dictionary that was missing the key?
4. The report says "Days analyzed: 26." The file has 28 rows, and 3 of them have blanks. What should the number be, and which function would you look at first?
5. The report says the best step day is Day 25. How would you cross-check that against the CSV file?
6. The Report Writer needs the number of days analyzed, but the Analyst's contract never promised it. What should the team do?
7. Give two reasonableness checks you could apply to a resting heart rate average.

---

## Coming Up in Class

You'll integrate your three real functions, one at a time: first on the Days 1–5 file, then on the full data. In lab, you'll meet a program that runs perfectly and is still wrong, and figure out why.
