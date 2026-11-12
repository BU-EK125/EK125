# Class 15: Collaborating with Others — Problem Definition and Initial Decisions

## Learning Objectives

By the end of this reading, you should be able to:

- Explain why team programs break at the "seams" between people's code
- Define a problem by stating its inputs, outputs, and messy cases
- Break a program into functions using the input → process → output pattern
- Write a **function contract** that a teammate could use without asking you any questions
- Describe the structure of a return value precisely, using an example value
- Recognize the decisions a team must make *before* writing code

**Good news:** there is no new Python syntax in this reading. Everything here uses functions ([Class 13](https://BU-EK125.github.io/EK125/class/Class13.html#part-1-user-defined-functions-morning)), dictionaries ([Class 12](https://BU-EK125.github.io/EK125/class/Class12.html#dictionaries)), and files ([Class 14](https://BU-EK125.github.io/EK125/class/Class14.html#part-2-file-input-and-output-i-o)). Today's new skill is *thinking and communicating* like a programmer on a team.

This reading kicks off the **Fitness Tracker Analyzer**, a team project running from this class through Class 19 -- see the [Project Overview](https://BU-EK125.github.io/EK125/class/FitnessTrackerProject.html) for the full plan.

---

## Part 1: Why Team Programs Break

### A story you will recognize

Three students split a lab report. One writes the methods, one writes the results, one writes the discussion. They each work alone all weekend and paste it together Sunday night. The result:

- The methods section says the sample size was 20. The results section analyzes 25.
- The results section calls the measurement "deflection." The discussion calls it "displacement."
- The discussion refers to "Figure 3," which nobody made.

Each section is fine on its own, but the report doesn't work. The problems are all at the **seams**, where one person's work meets another's.

Team programs fail the same way. Each function can be correct on its own, and the program still crashes when the pieces are put together.

### A small example

A team is writing a weather station program with three functions. Each person writes one:

```python
# Written by Person A
def read_temperatures(filename):
    """Read temperatures from a file."""
    temps = []
    with open(filename, "r") as file:
        for line in file:
            temps.append(float(line.strip()))
    return temps
```

```python
# Written by Person B
def summarize_temperatures(temps):
    """Summarize a list of temperatures."""
    summary = {"avg": sum(temps) / len(temps),
               "hi": max(temps),
               "lo": min(temps)}
    return summary
```

```python
# Written by Person C
def print_summary(summary):
    """Print the temperature summary."""
    print(f"Average: {summary['average']:.1f} F")
    print(f"High:    {summary['high']:.1f} F")
    print(f"Low:     {summary['low']:.1f} F")
```

All three functions are written correctly. Here is what happens when the team runs them together:

```python
temps = read_temperatures("station.txt")
summary = summarize_temperatures(temps)
print_summary(summary)
```

```
KeyError: 'average'
```

Person B named the key `"avg"`. Person C expected `"average"`. Neither of them is wrong, but they never agreed.

It gets worse. Suppose they fix the key names. The program runs and prints:

```
Average: 21.4 F
```

Is 21.4°F a cold day in Boston? Or is the file in Celsius, so it was really a pleasant 70°F? The program *ran*, but nobody agreed on **units**, so the output is wrong without any error message. This kind of bug is the most dangerous: **a program that runs and gives the wrong answer.**

> **Key idea:** When code is written by more than one person, most bugs live at the seams between functions, not inside them.

---

## Part 2: Define the Problem Before You Solve It

Before anyone writes a line of code, the team needs to agree on **what the program is supposed to do.** Engineers call this *problem definition*. Answer these four questions:

1. **What goes in?** What are the inputs? Where do they come from? What do they look like?
2. **What comes out?** What should the program produce: a printed message, a file, a value?
3. **What counts as success?** How will we know the output is right?
4. **What is messy?** What could be missing, wrong, or unusual in the input?

### Always look at the real data first

The fourth question is the one beginners skip. You cannot answer it without **opening the data file and reading it**. Real data is almost never clean. Here is what a few lines of weather station data might actually look like:

```
71.2
70.8

72.5
-999
71.9
```

There is a blank line, and a reading of `-999`. Many sensors write `-999` when they fail to take a measurement. If nobody on the team notices this, the average temperature will be wildly wrong, and every function will appear to "work."

> **Key idea:** Open the data file and look at it before you design anything. Find the messy parts and decide, as a team, what to do with them.

---

## Part 3: Break the Program into Functions

Many programs follow the same three-step pattern:

1. **Get the input(s)**
2. **Calculate the result(s)**
3. **Display or save the result(s)**

That pattern is also a natural way to divide work among three people. One person owns each step:

```
  station.txt
       |
       v
read_temperatures(filename)  -------->  list of temperatures
                                                |
                                                v
                              summarize_temperatures(temps)  -------->  summary dictionary
                                                                               |
                                                                               v
                                                               print_summary(summary)
                                                                               |
                                                                               v
                                                                      text on the screen
```

Notice what travels along each arrow: a **list** goes from the first function to the second, and a **dictionary** goes from the second to the third. Those arrows are the seams, and they are exactly where the team needs to agree.

A short **main program** calls the functions in order and passes values along the arrows:

```python
temps = read_temperatures("station.txt")
summary = summarize_temperatures(temps)
print_summary(summary)
```

You can write this main program on day one, *before any of the functions exist.* It is the team's plan, written in Python. Writing it forces three questions:

- What does each function **need** (its parameters)?
- What does each function **give back** (its return value)?
- Where does each returned value **go next**?

---

## Part 4: The Function Contract

### What is a contract?

Think about the charging port on your phone. Hundreds of companies make chargers, and none of them have ever met the people who designed your phone. The charger still works, because both sides follow one written standard. The standard specifies the plug's shape, voltage, and pin layout. Neither side needs to know how the other is built inside.

A **function contract** is that written standard for one function. It tells a teammate everything they need to *use* your function without ever reading the code inside it.

A complete contract answers five questions:

| Question | Example |
|---|---|
| **1. Name:** what is the function called? | `summarize_temperatures` |
| **2. Inputs:** what are the parameters? What type is each? What units? | `temps`: list of floats, °F |
| **3. Output:** what exactly is returned? What type and structure? | a dictionary with keys `"average"`, `"high"`, `"low"`; each value is a float in °F |
| **4. Side effects:** does it print? Write a file? Change its inputs? | none (does not print, does not change `temps`) |
| **5. Assumptions and messy cases:** what must be true of the input? | `temps` has at least one value; no `-999` values (the reader removes them) |

### Write the contract as a docstring

In [Class 13](https://BU-EK125.github.io/EK125/class/Class13.html#part-1-user-defined-functions-morning) you learned that every function begins with a **docstring**. The docstring is the natural home for the contract, because it travels with the function and anyone can display it with `help()`. Here is the complete contract for Person B's function:

```python
def summarize_temperatures(temps):
    """Calculate the average, high, and low of a list of temperatures.

    Parameters:
        temps (list of float): temperature readings in degrees F.
            Must contain at least one value. Must NOT contain -999
            (read_temperatures removes those).

    Returns:
        dict with exactly these three keys:
            "average" (float): mean temperature, degrees F, NOT rounded
            "high"    (float): largest temperature, degrees F
            "low"     (float): smallest temperature, degrees F

        Example: {"average": 71.6, "high": 72.5, "low": 70.8}

    Side effects: none. Does not print. Does not change temps.
    """
```

Read it as if you were Person C. You know the key is `"average"`, not `"avg"`. You know the values are in °F. You know the values are not rounded, so *you* need to round when you print. You never have to ask Person B a single question. That is the test of a good contract.

### Show an example value

The most useful line in that contract is the one that starts with `Example:`. Words like "a dictionary of statistics" can mean many different things. A literal example value can only mean one thing.

Compare these two descriptions of the same return value:

> **Vague:** "Returns the temperature data."

> **Precise:** "Returns a list of floats, one per valid reading, in the order they appear in the file. Example: `[71.2, 70.8, 72.5, 71.9]`"

From the vague version, a teammate can't tell whether to expect a list, a dictionary, a string, or a tuple, or whether the values are numbers or strings like `"71.2"`. From the precise version, they could write code against it right now.

> **Key idea:** For every return value, write down its type, its structure, and one concrete example value.

### Describing a dictionary of lists

Many engineering programs store table-like data as a **dictionary of lists**: one key per column, and each value is the list of numbers in that column. Suppose a weather station records two measurements per hour:

```
hour,temp_f,humidity
1,71.2,40
2,70.8,42
3,72.5,39
```

As a dictionary of lists, this becomes:

```python
{"hour":     [1, 2, 3],
 "temp_f":   [71.2, 70.8, 72.5],
 "humidity": [40.0, 42.0, 39.0]}
```

To get every temperature, you use `data["temp_f"]`. To get the humidity during hour 2, you use `data["humidity"][1]`. That is index 1, because Python counts from 0.

This structure only works if one rule holds: **all the lists are the same length, and position `i` in every list belongs to the same row.** Position 1 is hour 2 in *every* list. If one list loses an item and the others don't, the columns slide out of line. Every value after that point gets matched to the wrong hour, and Python will not warn you. Any team that uses a dictionary of lists has to decide how it will keep the lists lined up. That rule belongs in the contract.

### Contracts describe *what*, never *how*

A contract does **not** say whether the function uses a `for` loop, NumPy, or `sum()`. That is the owner's choice, and the owner can change it at any time without telling anyone, as long as the inputs and outputs stay exactly the same.

That is what makes parallel work possible. Person C can write `print_summary` on Monday, even though Person B won't finish `summarize_temperatures` until Thursday. Person C only needs the contract.

---

## Part 5: Decisions to Make on Day One

Some decisions affect *everyone's* code. If they aren't made at the start, each person makes them separately, and the decisions don't match. Settle these as a team, before anyone writes code:

| Decision | Example question | Why it matters |
|---|---|---|
| **Names** | Is the key `"average"` or `"avg"`? Is the parameter `temps` or `temperatures`? | A misspelled key causes a `KeyError` |
| **Units** | Are temperatures in °F or °C? Are times in hours or minutes? | Mismatched units give wrong answers *with no error* |
| **Types** | Is `day` an `int` or a `float`? Are numbers stored as numbers or as strings? | `"71.2" + 1` crashes; `71.2 + 1` does not |
| **Messy data** | What happens to blank values? To `-999`? Who handles them: the reader or the analyzer? | If nobody handles them, everybody's results are wrong |
| **Rounding** | Who rounds: the function that calculates, or the function that prints? | Rounding twice, or not at all, gives the wrong digits |
| **Ties and edge cases** | If two days have the same high, which one is "best"? | Two teammates might pick different days |
| **Ownership** | Who writes which function? Which file does it live in? | Prevents two people from editing the same file |

When the team makes a decision, **write it down** in a **Decision Log**: a simple, dated list of what you decided and why. Six days from now, when someone asks "wait, did we say the reader or the analyzer removes blanks?", the answer is in the log, not in three people's memories.

> **Key idea:** A decision that isn't written down hasn't really been made.

---

## Part 6: Working as a Team

### Roles

In your project, each person **owns one function** for the entire project. You are its expert. You write its contract section, its stub, its real code, and its tests, and you must be able to explain every line of it.

On top of that, three **duties** rotate each class, so everyone practices every part of team programming:

- **Integrator:** puts everyone's code together and runs the whole program
- **Tester:** checks each function against the contract
- **Recorder:** keeps the contract and Decision Log up to date, and submits the team's work

### A working agreement

Good teams agree on how they will work, not just what they will build. Before you leave class, agree on:

- **How you will communicate** (a group chat, email, or something else) and how fast you will reply
- **When you will meet** outside class, if you need to
- **Where shared files live** and who may edit each one. In your project, every function has its own `.py` file, and only its owner edits it.
- **What happens if someone is stuck.** Asking for help early is part of the job. Silence until the deadline is not.

---

## Summary: Key Concepts

- **Seams:** the places where one person's code passes data to another's. Most team bugs live here.
- **Problem definition:** inputs, outputs, what counts as success, and what's messy. Always look at the real data first.
- **Decomposition:** splitting a program into functions, often input → process → output, with a main program that calls them in order.
- **Function contract:** name, inputs, output, side effects, and assumptions, written in the docstring.
- **Example value:** a concrete literal that shows exactly what a function returns. It is the most precise part of a contract.
- **Dictionary of lists:** a table stored as one list per column. All lists must stay the same length and stay lined up.
- **What, not how:** a contract never says how the function works inside.
- **Decision Log:** a dated, written record of team decisions.

---

## Check Your Understanding

1. In the weather station example, each function was correct on its own. Why did the program still fail?
2. Why is "the program runs but gives the wrong answer" worse than "the program crashes"?
3. Name the five parts of a function contract.
4. Rewrite this vague contract precisely: *"`read_temperatures` returns the temperatures."*
5. In a dictionary of lists, why must every list stay the same length? What goes wrong if one list loses an item?
6. Person B decides to rewrite `summarize_temperatures` using NumPy instead of `sum()`, `max()`, and `min()`. Does Person C need to change anything? Why or why not?
7. Your teammate's function returns `{"average": 71.6, "high": 72.5, "low": 70.8}`. Write the line of code that prints only the high temperature.
8. Give one example of a team decision that, if it is skipped, causes wrong answers *without* any error message.

---

## Coming Up in Class

In class, your team will:

- open the real fitness tracker data and find its messy parts
- design your program
- divide up the functions
- write your **Team Contract**

Come ready to make decisions!
