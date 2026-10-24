# Class 16: Stub Building

## Learning Objectives

By the end of this reading, you should be able to:

- Import a function from a Python file you (or a teammate) wrote
- Explain what happens when Python imports a file, and where test code belongs
- Write a **faithful stub** from a function contract
- Explain why a team should get the whole program running *before* writing any real code
- Check the values that pass between functions ("print at the seam")
- Recognize the four errors you are most likely to see today, and what each one means

**New syntax today:** only importing from your own files. Everything else you already know.

---

## Part 1: Where We Are

On Monday your team wrote a **contract**: the exact name, parameters, return value, and example value for each of your three functions. Today you turn that contract into a **program that runs**, even though none of the real code exists yet.

### The stand-in

Before a play opens, the lighting crew needs to rehearse. But the lead actor is still learning lines. So a **stand-in** walks the actor's path across the stage and stops on every mark. The stand-in can't act, but stands in exactly the right places at exactly the right times. Because of that, the lighting crew can do their job before the actor is ready.

A **stub** is a stand-in for a function. It doesn't do the real work. But it accepts exactly the right inputs and hands back exactly the right *kind* of output, so every other part of the program can be built and tested around it.

You met stubs at the end of the [Class 13](https://BU-EK125.github.io/EK125/class/Class13.html#function-stubs) reading. Today you'll use them for what they're best at: **letting three people build one program at the same time.**

---

## Part 2: Importing From Your Own Files

### Every `.py` file is a module

You've been importing since [Class 5](https://BU-EK125.github.io/EK125/class/Class5.html#what-is-a-module):

```python
import math
import numpy as np
```

`math` and `numpy` are **modules**, which are files of Python code that someone else wrote. Any `.py` file you write is also a module, and it can be imported the same way.

In your project, each function lives in its own file:

```
FitnessTracker/
├── fitness_data.csv
├── loader.py        contains load_tracker_data
├── analyzer.py      contains analyze_metric
├── reporter.py      contains write_report
└── main.py          imports and calls all three
```

At the top of `main.py`:

```python
from loader import load_tracker_data
from analyzer import analyze_metric
from reporter import write_report
```

Read the first line as: *"From the file `loader.py`, bring in the function `load_tracker_data`."*

After that line, `main.py` can call `load_tracker_data(...)` exactly as if the function were written in `main.py` itself.

### Three rules for importing your own files

1. **Same folder.** The file you import must be in the same folder as the file doing the importing.
2. **No `.py`.** Write `from loader import ...`, not `from loader.py import ...`.
3. **Exact spelling.** The file name and the function name must match *exactly*, including capitalization and underscores. This is the contract again: the name in the header is the name everyone types.

### What happens when Python imports a file

When `main.py` runs `from loader import load_tracker_data`, Python **runs `loader.py` from top to bottom, once.** Running a `def` block doesn't call the function. It only defines it, so normally importing a file just makes its functions available.

But suppose `loader.py` has this line at the bottom, outside any function:

```python
print(load_tracker_data("fitness_data.csv"))     # quick test
```

That line runs **every time any file imports `loader.py`**. Your teammates would see your test output in the middle of *their* program.

### Where test code belongs

You saw this pattern in [Class 14](https://BU-EK125.github.io/EK125/class/Class14.html#the-if-name-main-pattern):

```python
def test_loader():
    """Quick check that load_tracker_data keeps its promises."""
    data = load_tracker_data("fitness_data.csv")
    print("type:", type(data))
    print("keys:", list(data.keys()))


if __name__ == "__main__":
    test_loader()
```

- When you **run `loader.py` directly** (green arrow in PyCharm), `__name__` is `"__main__"`, so `test_loader()` runs.
- When **`main.py` imports `loader.py`**, `__name__` is `"loader"`, so the test is skipped.

Putting the test inside a function (`test_loader`) also keeps its variables local. That follows the course rule: **no global variables.**

> **Key idea:** You can run your own file to test it, and your teammates can import it without seeing your tests.

---

## Part 3: Writing a Faithful Stub

A stub that is *wrong* is worse than no stub at all, because it hides problems instead of revealing them. A **faithful stub** follows five rules.

### Rule 1: Copy the header and docstring exactly

The header is the contract's promise to everyone else. Paste the header and docstring in from your Team Contract, unchanged.

### Rule 2: Return the contract's example value

Your contract already contains an example value. That is exactly what the stub returns. It has the right type, the right structure, the right keys, and realistic numbers.

### Rule 3: Use the parameters where it's easy

If a parameter can be passed straight into the return value, use it. Hard-code everything else. This lets you see that the arguments are actually arriving.

### Rule 4: Return. Never print instead.

A stub that prints its dictionary *looks* like it works: you see the right values on the screen. But a function with no `return` hands back `None`, and the next function crashes.

### Rule 5: If it uses inputs from a teammate, touch every key it will need

A stub whose job is to *use* someone else's data should look up every key the real version will need. If a key name doesn't match, you find out **today**, not in Class 18.

### Example: the weather station, stubbed

Here are faithful stubs for the three weather station functions from the [Class 15](https://BU-EK125.github.io/EK125/class/Class15.html#a-small-example) reading.

```python
def read_temperatures(filename):
    """Read temperatures in degrees F from a file.

    Returns: list of float, one per valid reading.
        Example: [71.2, 70.8, 72.5, 71.9]
    """
    # STUB: return the example value from the contract
    return [71.2, 70.8, 72.5, 71.9]
```

```python
def summarize_temperatures(temps):
    """Calculate the average, high, and low of a list of temperatures.

    Returns: dict with keys "average", "high", "low" (floats, degrees F).
        Example: {"average": 71.6, "high": 72.5, "low": 70.8}
    """
    # STUB: return the example value from the contract
    summary = {"average": 71.6, "high": 72.5, "low": 70.8}
    return summary
```

```python
def save_summary(summary, filename):
    """Write the temperature summary to a text file.

    Returns: None.  Side effects: creates the file filename.
    """
    # STUB: touch every key the real version will use
    with open(filename, "w") as file:
        file.write(f"STUB {summary['average']} {summary['high']} {summary['low']}\n")
```

Notice what these stubs do **not** do. They don't open the data file, calculate an average, or format anything nicely. That's Class 17's job. They only keep the promises in the contract.

### Rule 3 in action

For a function with a parameter that's easy to pass through, use it:

```python
def convert_units(value, units):
    """Convert a temperature. Returns: dict with keys "value" (float) and "units" (str).
        Example: {"value": 22.0, "units": "C"}
    """
    # STUB: pass the units straight through; hard-code the number
    return {"value": 22.0, "units": units}
```

If the main program calls `convert_units(71.6, "K")` and the result shows `"units": "K"`, you know the argument arrived where it should.

### Good stub vs. bad stubs

Contract: *returns a list of floats. Example: `[71.2, 70.8]`*

| Stub body | Faithful? | Why |
|---|---|---|
| `return [71.2, 70.8]` | Yes | Right type, right structure, example value |
| `return "71.2, 70.8"` | No | That's a string, not a list |
| `return [71, 70]` | No | Those are ints, not floats |
| `print([71.2, 70.8])` | No | No `return`, so the function returns `None` |
| `pass` | No | Also returns `None` |

---

## Part 4: Running the Skeleton

Once every stub exists, the team runs `main.py`. If everything is faithful, the program runs from start to finish, and the output is obviously fake:

```
STUB REPORT
steps 5 8327.8 4569.0 12192.0 5 8000 3
resting_hr 5 8327.8 4569.0 12192.0 5 62 3
```

Every metric shows the same numbers, because the Analyst's stub always returns the same example. **That is a success.** It proves:

- every import works
- every function is called with the right number of arguments
- every return value has the shape the next function expects
- every key the Report Writer uses exists

You now have a **running skeleton**. From now on, your team only ever goes from *a working program* to *a slightly more real working program*. You never have to put three untested pieces together and hope.

---

## Part 5: Checking the Seams

A program that runs isn't automatically correct. The **Tester**'s job today is to look at every value as it crosses from one function to the next, and compare it to the contract. The simplest tool is a temporary `print` at each seam:

```python
data = load_tracker_data("fitness_data.csv")
print("SEAM 1 type:", type(data))
print("SEAM 1 keys:", list(data.keys()))
print("SEAM 1 lengths:", len(data["day"]), len(data["steps"]))

results = analyze_metric(data, "steps", 8000)
print("SEAM 2 type:", type(results))
print("SEAM 2 keys:", list(results.keys()))
```

Three questions answer most seam problems:

| Check | Code | Compare to |
|---|---|---|
| Is it the right **type**? | `type(x)` | The contract's *Returns* type |
| Does it have the right **keys**? | `list(x.keys())` | Every key named in the contract |
| Are the lists the right **length**? | `len(x["day"])`, `len(x["steps"])` | All the same length |

These prints are temporary. Put them in a separate copy of `main.py` (your team will call it `check_seams.py`), so the real `main.py` stays clean.

---

## Part 6: The Four Errors You'll Most Likely See Today

| Error message | What it usually means today | Where to look |
|---|---|---|
| `ModuleNotFoundError: No module named 'loader'` | Python can't find the *file*. It's in a different folder, or the file name is spelled differently. | Is `loader.py` in the same folder as `main.py`? Is it spelled exactly the same? |
| `ImportError: cannot import name 'load_data' from 'loader'` | The *file* was found, but the *function name* doesn't match. | Compare the name in the `import` line to the name in the `def` line. |
| `TypeError: 'NoneType' object is not subscriptable` | Someone did `x["key"]` on a value that is `None`. Usually a function **printed instead of returning**. | Find the function that produced `x`. Does it have a `return`? |
| `KeyError: 'average'` | The dictionary exists but doesn't have that key. The two sides of a seam disagree about key names. | Compare the key in the error with the keys in the contract. Who is off-contract? |

Notice that **three of these four are seam errors**: each piece is fine, but two pieces don't match. That's exactly what stubs are designed to catch, while the code is still small and easy to fix.

> **Key idea:** When an error appears, ask "which seam?" before you ask "which line?"

---

## Part 7: Sharing Files Through Google Drive

Your team's files live in your **shared Google Drive folder**. Today's workflow:

1. Each owner writes their stub in their own PyCharm `FitnessTracker` folder and runs it to test it.
2. Each owner uploads **only their own file** to the shared Drive folder. Replace the old version; don't upload a second copy.
3. The Integrator downloads all the files into one PyCharm folder and runs `main.py`.
4. If a file needs to change, its **owner** changes it and re-uploads it. Nobody edits a teammate's file.

> **Watch out:** if Drive shows `loader (1).py`, someone uploaded a second copy instead of replacing the file. Python will import `loader.py`, not `loader (1).py`, so the new code is silently ignored. Delete the duplicate and upload again as a new version.

---

## Summary: Key Concepts

- **Module:** any `.py` file. Import from it with `from filename import function_name`.
- **Import rules:** same folder, no `.py`, exact spelling.
- **Importing runs the file.** Test code goes in a test function, called under `if __name__ == "__main__":`.
- **Faithful stub:** exact header and docstring, returns the contract's example value, uses easy parameters, never prints instead of returning, touches every key it needs.
- **Running skeleton:** the whole program runs with stubs. Fake output is a success.
- **Print at the seam:** check type, keys, and lengths of every value crossing between functions.
- **Seam errors:** `ImportError`, `NoneType ... not subscriptable`, and `KeyError` usually mean two pieces don't match.

---

## Check Your Understanding

1. Your teammate's file is `analyzer.py` and contains `analyze_metric`. Write the line that imports it into `main.py`.
2. What's the difference between `ModuleNotFoundError` and `ImportError: cannot import name`?
3. Why does test code belong inside `if __name__ == "__main__":`?
4. A contract says a function returns `{"high": 72.5, "low": 70.8}`. Write a faithful stub body (one or two lines).
5. A stub prints its dictionary instead of returning it. The stub *looks* fine when you run it. What goes wrong when the next function uses its result?
6. The skeleton runs, and every metric in the report shows exactly the same numbers. Is that a bug? Why or why not?
7. You see `KeyError: 'avg'`. What two things should you compare?
8. Why is it better to find a key-name mismatch in Class 16 than in Class 18?

---

## Coming Up in Class

Each of you will write your stub, the Integrator will get the full skeleton running, and the Tester will check every seam against the contract. In lab, you'll diagnose a skeleton someone *else* broke.
