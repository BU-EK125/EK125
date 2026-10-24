# Class 17: Writing Real Functions

## Learning Objectives

By the end of this reading, you should be able to:

- Turn pseudocode comments into working code, one step at a time
- Write **tests before code**, using expected values worked out by hand
- Write a small `check()` function that prints PASS or FAIL
- Test your function **without** your teammates' code
- Choose test cases that catch bugs: the normal case, edge cases, and boundaries
- Compare floating-point numbers safely
- Test a function that writes a file

**New syntax today:** none. Everything here uses functions, `if`/`else`, loops, f-strings, and file I/O.

---

## Part 1: Where We Are

Your team has a **running skeleton**. Every function is a stub, and `main.py` runs from start to finish. Today each person replaces **their own** stub with real code.

Back to the theater: the stand-ins rehearsed the whole show. Now the real actors step in, **one at a time**. The show keeps running the whole time, because every actor stands on exactly the same marks the stand-in did. That's your contract.

The most important rule today:

> **Your real function must keep every promise your stub kept**: same header, same return type, same structure, same keys. If it does, your teammates' code keeps working without any changes.

---

## Part 2: Tests First, Then Code

How will you know your function is right? Here's how most beginners do it:

1. Write the code.
2. Run it.
3. Look at the output and think, "Yeah, that looks about right."

Step 3 is the problem. **"Looks about right" is not a test.** If you don't know the right answer *before* you run the code, you'll believe whatever the code tells you.

You already have the right answers. In [Class 15](https://BU-EK125.github.io/EK125/gpps/Class15_TeamActivity.html#part-e-work-out-the-expected-answers-by-hand-about-20-minutes-together) lab, your team worked out **by hand** exactly what each function should return for Days 1–5. Those are your **expected values**. Today, you write them into a test **before** you write the real code.

### A small `check()` function

Comparing expected and actual values over and over gets repetitive, so write a function for it. That's what functions are for!

```python
def check(test_name, expected, actual):
    """Print PASS if expected equals actual; otherwise print FAIL and both values."""
    if expected == actual:
        print(f"PASS: {test_name}")
    else:
        print(f"FAIL: {test_name}")
        print(f"   expected: {expected}")
        print(f"   actual:   {actual}")
```

When a test fails, `check()` shows you **both** values, side by side. That usually tells you exactly what went wrong.

### A test function

Your tests go in a test function, called only when you run your file directly. This is the same pattern you used for stub tests in Class 16:

```python
def test_summarize():
    """Test summarize_temperatures against hand-calculated values."""
    expected = {"average": 72.0, "high": 74.0, "low": 70.0}
    actual = summarize_temperatures([70.0, 72.0, 74.0])
    check("three simple temps", expected, actual)


if __name__ == "__main__":
    test_summarize()
```

**Write the test first.** Run it while your function is still a stub. It will print FAIL, which is fine: it proves your test can fail. Then write the real code and run it again until it prints PASS.

> **Key idea:** Decide what the right answer is *before* you run the code. Then let the computer tell you whether you got it.

---

## Part 3: From Pseudocode to Code

In Class 16 lab, you wrote pseudocode comments above your stub. Now turn each comment into one or two lines of code. **Keep the comments.** They become the explanation of your code.

Here's the weather station reader, from plan to code:

```python
def read_temperatures(filename):
    """Read temperatures in degrees F from a file. Skips blank lines and -999."""
    # 1. Make an empty list for the temperatures
    temps = []
    # 2. Open the file for reading
    with open(filename, "r") as file:
        # 3. For each line in the file:
        for line in file:
            # a. strip the newline
            reading = line.strip()
            # b. if the line is not blank and not "-999", convert it and add it
            if reading != "" and reading != "-999":
                temps.append(float(reading))
    # 4. Return the list
    return temps
```

Work one step at a time. After each step, **run your tests.** If something breaks, you know it was the step you just wrote.

A common beginner move is to write all the code, run it once, and get six errors. Don't! Write a few lines, run, and repeat.

### Style rules still apply

- No `global` variables. Everything your function needs comes in through its parameters.
- No `break` or `continue`. Use an `if` inside the loop to decide what to do with each item, as the weather reader does.
- No `while True`. For these functions, `for` loops are all you need.
- Use readable variable names (`best_position`, not `bp`) and keep your comments.

---

## Part 4: Testing Without Your Teammates

You can test your own function **today**, even if nobody else on your team has written theirs.

**If your function takes a dictionary or list as input:** build a small one by hand, right in your test. The weather `summarize_temperatures` test above never calls the reader; it just passes in `[70.0, 72.0, 74.0]`. Make the input small enough that you can work out the answer in your head or on paper.

**If your function reads a file:** make a tiny test file. In PyCharm, right-click your project folder → *New → File* → `test_temps.txt`, and type a few lines:

```
71.2

70.8
-999
72.5
```

Then test against it:

```python
def test_reader():
    """Test read_temperatures on a tiny file with a blank line and a -999."""
    check("skips blank and -999", [71.2, 70.8, 72.5],
          read_temperatures("test_temps.txt"))
```

**If your function writes a file:** call it, then **open the file and read it back**:

```python
def test_save():
    """Test save_summary by writing a file and reading it back."""
    save_summary({"average": 72.0, "high": 74.0, "low": 70.0}, "test_out.txt")
    with open("test_out.txt", "r") as file:
        text = file.read()
    check("high appears in file", True, "74.0" in text)
    check("file has 3 lines", 3, len(text.strip().split("\n")))   # if the contract promises 3 lines
```

Checking whether a key phrase is `in` the text is usually better than comparing the entire file character by character.

---

## Part 5: Choosing Good Test Cases

One test isn't enough. A function can pass the "normal" test and still be wrong. Good testers deliberately try the cases most likely to break the code.

| Kind of test | What it checks | Weather example |
|---|---|---|
| **Normal case** | Typical data, hand-calculated | `[70.0, 72.0, 74.0]` |
| **Messy data** | The messy cases in your contract | A file with blank lines and `-999` |
| **Tie** | Two values equally "best" | `[74.0, 70.0, 74.0]`: which day is the high? |
| **Boundary** | A value *exactly* equal to a limit | A goal of 72.0 when one value is exactly 72.0 |
| **Direction** | "Higher is better" vs. "lower is better" | A low temperature is "best" on a hot day |
| **Smallest input** | One item | `[71.0]`: average, high, and low are all 71.0 |

### Why boundaries matter

Suppose a contract says "count the days **at or above** the goal," and someone writes:

```python
if value > goal:
```

instead of:

```python
if value >= goal:
```

If none of the test values happens to equal the goal *exactly*, every test passes and the bug survives. A **boundary test** puts a value exactly on the line, on purpose.

> **Key idea:** Normal tests show that your code *can* work. Edge and boundary tests show that it *does* work.

---

## Part 6: Comparing Decimal Numbers

Try this in the Python console:

```python
>>> 0.1 + 0.2
0.30000000000000004
>>> 0.1 + 0.2 == 0.3
False
```

Computers store most decimal numbers as very close approximations, so tiny errors can appear in the last digits. Your function can be **correct** and still fail a test that uses `==`.

Two ways to handle this:

1. **Round where your contract says to round.** If your contract says the average is rounded to 1 decimal place, then `round(...)` happens inside the function, and `==` works on the rounded result: `round(0.1 + 0.2, 1) == 0.3` is `True`.
2. **Round inside the test** when you compare an unrounded value: `check("average", 72.3, round(actual["average"], 1))`.

---

## Part 7: Working in Parallel

Your teammates may finish before you, or after you. That's fine:

- Your tests don't need their code (Part 4).
- `main.py` still runs with **any mix** of real functions and stubs, as long as every piece keeps the contract.

Before you upload your file to the shared Drive folder, run `main.py` with your real function and your teammates' latest files. If `main.py` crashed after your change, your function has broken a promise. Find it before your teammates do!

---

## Summary: Key Concepts

- **Keep every promise the stub kept:** same header, return type, structure, and keys.
- **Tests first:** write expected values (worked out by hand) into a test *before* writing the code.
- **`check(test_name, expected, actual)`:** prints PASS or FAIL, with both values on failure.
- **Pseudocode → code:** one comment at a time; run the tests after each step; keep the comments.
- **Test alone:** hand-built inputs, tiny test files, and reading output files back.
- **Good test cases:** normal, messy data, tie, boundary, direction, smallest input.
- **Floats:** round where the contract says, or round inside the test.

---

## Check Your Understanding

1. Why should you work out the expected value *before* running your code?
2. Your test prints FAIL while your function is still a stub. Is that a problem? Why or why not?
3. Write a `check()` call that tests whether `summarize_temperatures([71.0])` returns `{"average": 71.0, "high": 71.0, "low": 71.0}`.
4. The Analyst wants to test `analyze_metric` before the Loader is finished. How?
5. Give one boundary test for a function that counts days with at least 8000 steps.
6. Why might `check("average", 0.3, 0.1 + 0.2)` print FAIL even though the math is right? How would you fix the test?
7. How can you test a function whose only job is to write a file?
8. Your real function passes all your tests, but `main.py` now crashes in a teammate's file. What should you check first?

---

## Coming Up in Class

You'll write your tests from the Class 15 hand calculations, then replace your stub with real code, one pseudocode step at a time. In lab, we'll build the two trickiest functions together: the Loader's skip-the-row logic and the Analyst's best-day loop.
