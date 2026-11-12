# Class 19: Debugging and Reflection

## Learning Objectives

By the end of this reading, you should be able to:

- Debug with a **method**, not by guessing
- Tell the three kinds of bugs apart: **syntax**, **runtime**, and **logic**
- Match common error messages to their most likely causes
- Debug code that someone else wrote, starting from its contract
- Use print statements, and optionally the PyCharm debugger, to see what your code is doing
- Write a test that would have caught a bug, so it can never come back
- Run a team **retrospective**

**New syntax today:** none. (The PyCharm debugger is a tool, not syntax, and it's optional.)

---

## Part 1: Debugging Is a Method

When a car makes a strange noise, a good mechanic doesn't start replacing parts at random. They:

1. **Reproduce it:** drive the car until they hear the noise themselves.
2. **Locate it:** narrow it down: front or back? Only when braking?
3. **Form a hypothesis:** "I think it's the brake pads."
4. **Change one thing and test:** replace the pads, then drive again.
5. **Confirm:** if the noise is gone, done. If not, back to step 2.

Debugging code works exactly the same way:

| Step | In code |
|---|---|
| **1. Reproduce** | Run the program and get the error (or the wrong answer) every time |
| **2. Locate** | Read the traceback bottom-up. For wrong answers, print at the seams to find where values first go wrong. |
| **3. Hypothesize** | "I think `best_day` is a list position, not a day number." |
| **4. Change ONE thing** | Make one fix. Run again. |
| **5. Confirm** | Did the error go away *and* is the answer now right? Re-run your tests. |

The most common beginner mistake is changing five things at once. If it then works, you don't know which change fixed it. If it doesn't, you've possibly added new bugs.

> **Key idea:** One change, one run. Every time.

---

## Part 2: Three Kinds of Bugs

### Syntax errors: Python can't even read the code

The program **doesn't start at all.** Python reads the whole file first, and if the grammar is broken, it stops before running anything.

```python
with open(filename, "w") as report       # missing colon
```

```
  File "reporter.py", line 20
    with open(filename, "w") as report
                                      ^
SyntaxError: expected ':'
```

Common causes:
- a missing `:` after `if`, `for`, `def`, or `with`
- unmatched `(` `[` `{` or quotes
- wrong indentation

The error points at the problem, or **just after it**, so look at the line shown *and* the line before it.

If the syntax error is in a file that `main.py` **imports**, `main.py` stops at the `import` line, and the traceback points into the imported file.

### Runtime errors: the program starts, then crashes

Python could read the code, but something went wrong while running it. You get a traceback:

| Error | What it means | Typical cause in this project |
|---|---|---|
| `ValueError: could not convert string to float: ''` | `float()` was given something that isn't a number | Trying to convert a blank value from the CSV |
| `TypeError: can only concatenate str (not "int") to str` | `+` between a string and a number | `"Days: " + 25`. Use an f-string or `str(25)`. |
| `TypeError: 'NoneType' object is not subscriptable` | `x[...]` where `x` is `None` | A function printed instead of returning |
| `KeyError: 'average'` | The dictionary doesn't have that key | Two sides of a seam disagree about names |
| `IndexError: list index out of range` | Asked for position `i`, but the list is shorter | Off-by-one in a loop, or lists of different lengths |
| `NameError: name 'totl' is not defined` | Used a name that doesn't exist (yet) | A typo, or a variable used outside its function (scope!) |
| `FileNotFoundError` | The file isn't where Python is looking | Wrong folder or misspelled file name |
| `ZeroDivisionError` | Divided by zero | Averaging an empty list |

### Logic errors: the program runs and gives the wrong answer

**No error message at all.** These are the hardest bugs, because the computer thinks everything is fine. The only ways to catch them:

- **Tests** with expected values worked out by hand
- **Reasonableness checks** (Class 18): counts, lengths, ranges, consistency
- **Comparing against a known-good answer** (like the data facts)

Two common logic bugs:

```python
if value < goal:        # contract says "at or below": should be <=
```

```python
"best_day": best_position,      # contract says DAY NUMBER: should be days[best_position]
```

> **Key idea:** Syntax errors stop the program before it starts. Runtime errors stop it partway through. Logic errors don't stop it at all, so you have to go looking for them.

---

## Part 3: Debugging Code Someone Else Wrote

On Exam 2, and in your career, you'll often fix code you didn't write. Don't start by reading every line. Start from the **outside** and work in:

1. **Read the contract** (the docstring). What *should* the function do? What does it promise to return?
2. **Read `main.py`.** How is the function called? What happens to its result?
3. **Run it.** Get the error or the wrong output.
4. **Follow the data.** Print at the seams. Find the *first* place where a value doesn't match the contract.
5. **Only now, read that function's code closely.** Compare each line to the contract.

The contract tells you what "right" means. Without it, you're just guessing what the author intended.

---

## Part 4: Tools for Seeing Inside Your Code

### Print statements

The simplest tool, and often the best. Two patterns:

**Print at the seam** (Classes 16 and 18): check type, keys, and lengths of values passed between functions.

**Print inside a loop**, to watch a variable change:

```python
for i in range(len(values)):
    if values[i] > values[best_position]:
        best_position = i
    print(f"i={i}  value={values[i]}  best_position={best_position}")
```

This produces a **trace table**, just like the ones you write by hand on quizzes. Compare it to what you *expected* each line to be. The first line that's different is where the bug is.

**Remove debugging prints when you're done.** Your contract may say "does not print."

### The PyCharm debugger (optional)

PyCharm can pause your program and let you look at every variable:

1. **Click in the gutter** (just left of the code, next to a line number). A red dot appears. That's a **breakpoint**.
2. Run with the **bug icon** (Debug) instead of the green arrow.
3. The program stops at the breakpoint. The **Variables** pane shows every variable's current value.
4. Click **Step Over** (or press F8) to run one line at a time, and watch the values change.

It's like a trace table that writes itself. You won't need it on paper exams, but it can save a lot of time on homework.

---

## Part 5: Fix It So It Stays Fixed

When you find a bug, ask: **"Why didn't my tests catch this?"**

Usually the answer is that no test hit that exact case. In Class 18's clinic, the Days 1–5 test file had no blank rows, so the bug in blank-row handling slipped right past it.

After fixing a bug, **write a test that would have caught it**. Then if anyone ever reintroduces that bug, the test fails immediately. Professional programmers call this a **regression test**: it guards against the code "regressing" back to a broken state.

```python
# Regression test: a value exactly equal to the goal must count
boundary_data = {"day": [1, 2, 3], "resting_hr": [62.0, 63.0, 61.0]}
result = analyze_metric(boundary_data, "resting_hr", 62, False)
check("value equal to goal counts", 2, result["days_meeting_goal"])
```

---

## Part 6: The Retrospective

When a project ends, good engineering teams hold a **retrospective**: a short, honest meeting about **how the team worked**, not just what it built.

The most common format is **Start / Stop / Continue**:

| | Question |
|---|---|
| **Continue** | What worked well that we should keep doing? |
| **Stop** | What caused problems that we should stop doing? |
| **Start** | What should we try next time that we didn't do this time? |

Two ground rules make retrospectives useful:

1. **Blame the process, not the person.** "We never agreed who handles blank values" is useful. "Jordan messed up the loader" is not. Almost every bug in a team project traces back to something the *process* allowed.
2. **Be specific.** "Communication was bad" isn't something anyone can act on. "We didn't check the Drive folder before class, so we used old files in Step 2" is.

Your integration log and Decision Log are your evidence. Use them.

---

## Summary: Key Concepts

- **The debugging method:** reproduce, locate, hypothesize, change one thing, confirm.
- **Syntax errors:** the program doesn't start. Look at the line shown *and* the one before it.
- **Runtime errors:** the program crashes partway. Read the traceback bottom-up and match the error type to its typical cause.
- **Logic errors:** no error message, wrong answer. Caught only by tests, reasonableness checks, and known-good comparisons.
- **Someone else's code:** contract first, then `main.py`, run it, follow the data, *then* read the code.
- **Tools:** print at the seam, print inside loops (trace tables), the optional PyCharm debugger.
- **Regression test:** after fixing a bug, add the test that would have caught it.
- **Retrospective:** Start / Stop / Continue, blaming the process rather than people, and being specific.

---

## Check Your Understanding

1. List the five steps of the debugging method. Why change only one thing at a time?
2. Is each of these a syntax, runtime, or logic error?
   a) `for i in range(5)` with no colon
   b) `float("")`
   c) a function that counts days `> goal` when the contract says "at or above"
3. What does `TypeError: can only concatenate str (not "int") to str` usually mean? Give two ways to fix it.
4. Why might the Days 1–5 test file *not* catch a bug in how `<=` is handled for resting heart rate? (Hint: look at Days 1–5's resting HR values and the goal of 62.)
5. When debugging code you didn't write, why read the contract before the code?
6. What is a regression test?
7. Rewrite this retrospective comment so it's specific and blames the process, not a person: *"Sam was slow and communication was bad."*

---

## Coming Up in Class

You'll hunt down five bugs in another team's version of the Fitness Tracker program, record each one in a Bug Log, and then hold your own team's retrospective.
