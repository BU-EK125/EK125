# Class 13 GPP: User-Defined Functions, Scope, and Copying

This is a script-based exercise: work through the problems directly in
PyCharm/VS Code (not in a notebook). Download the file below, open it
locally, and run it as you go -- the instructions are also on this page so
you can read them without switching windows.

Download: [Class13_GPP.py](Class13_GPP.py)

## Instructions

**Team Members:**
- Your Name
- Partner 1 Name
- Partner 2 Name

**Today's topics:** writing functions with return values, functions that
print (no return), lambda functions, parameter passing (by value vs by
reference), keyword arguments and default parameters, variable scope (the
LEGB rule), and copying lists (shallow vs deep copy).

**Remember:** Functions should either RETURN values OR print, but not both!

**Instructions:**
- You MAY use your reading notes and previous assignments
- Do **NOT** use AI tools (ChatGPT, Claude, Copilot, etc.)
- Not submitted for grading -- but this material **will** appear on quizzes and exams!

**PyCharm reminders:**
- Run your file with `Shift+F10` (or the green play button)
- Output appears in the terminal at the bottom
- Save frequently with `Ctrl+S` / `Cmd+S`

## Part 1: Understanding Parameter Passing

**Problems 1.1-1.3:** Predict the output of three short snippets, then run
them to check your understanding -- passing an integer (immutable), modifying
a list in place (mutable), and reassigning a list inside a function.

See the reading's [The Two Types of Data: Mutable and Immutable](https://BU-EK125.github.io/EK125/class/Class13.html#the-two-types-of-data-mutable-and-immutable), [Immutable Objects: Always Safe](https://BU-EK125.github.io/EK125/class/Class13.html#immutable-objects-always-safe), and [Mutable Objects: Changes Affect the Original](https://BU-EK125.github.io/EK125/class/Class13.html#mutable-objects-changes-affect-the-original) sections for a refresher.

```{literalinclude} Class13_GPP.py
:language: python
:lines: 29-100
```

## Part 2: Functions that Return Values

**Problems 2.1-2.4:** Write functions with docstrings that return values --
an inches-to-feet converter, a sign function, a rectangle area/perimeter
calculator (returning a tuple), and a cumulative product function.

See the reading's [Functions with Return](https://BU-EK125.github.io/EK125/class/Class13.html#functions-with-return) section for a refresher.

```{literalinclude} Class13_GPP.py
:language: python
:lines: 102-159
```

## Part 3: Functions that Print (No Return)

**Problems 3.1-3.3:** Write a function that prints a box of stars, verify
that a function with no `return` statement returns `None`, and write a
function that prints (not returns) a random string from a list.

See the reading's [Functions with no Return](https://BU-EK125.github.io/EK125/class/Class13.html#functions-with-no-return) section for a refresher.

```{literalinclude} Class13_GPP.py
:language: python
:lines: 160-202
```

## Part 4: Working with Keyword Arguments

**Problem 4.1:** Complete a student-record function with default parameter
values, and test it with students that use varying combinations of
defaults and keyword arguments.

See the reading's [Default Parameter Values](https://BU-EK125.github.io/EK125/class/Class13.html#default-parameter-values) and [Keyword Arguments](https://BU-EK125.github.io/EK125/class/Class13.html#keyword-arguments) sections for a refresher.

```{literalinclude} Class13_GPP.py
:language: python
:lines: 203-248
```

## Part 5: Variable Scope (LEGB Rule)

**Problems 5.1-5.2:** Fix code that incorrectly tries to modify a variable
from an enclosing scope, then trace through a nested-function example and
explain the LEGB (Local, Enclosing, Global, Built-in) lookup rule.

See the reading's [What is Scope?](https://BU-EK125.github.io/EK125/class/Class13.html#what-is-scope) and [The LEGB Rule](https://BU-EK125.github.io/EK125/class/Class13.html#the-legb-rule) sections for a refresher.

```{literalinclude} Class13_GPP.py
:language: python
:lines: 249-306
```

## Part 6: Copying Lists

**Problems 6.1-6.2:** Protect the original order of a list of grades using
`.copy()` instead of plain assignment, then explore the difference between
shallow copy and `copy.deepcopy()` on a nested list structure.

See the reading's [Solution 1: Shallow Copy](https://BU-EK125.github.io/EK125/class/Class13.html#solution-1-shallow-copy) and [Solution 2: Deep Copy](https://BU-EK125.github.io/EK125/class/Class13.html#solution-2-deep-copy) sections for a refresher.

```{literalinclude} Class13_GPP.py
:language: python
:lines: 307-374
```

## Part 7: Lambda Functions

**Problems 7.1-7.2:** Write two small lambda functions that append text to
the end of a string.

See the reading's [Lambda Functions](https://BU-EK125.github.io/EK125/class/Class13.html#lambda-functions) section for a refresher.

```{literalinclude} Class13_GPP.py
:language: python
:lines: 375-405
```

## Part 8: Mixed Return and Print Functions

**Problems 8.1-8.2:** Write a menu function that prints options and returns
the user's validated choice, and a function that reverses a string.

```{literalinclude} Class13_GPP.py
:language: python
:lines: 406-443
```

## Part 9: Putting It All Together

**Problem 9.1:** Combine everything from today -- write a function with two
default parameters (`bonusPoints` and `makeBackup`) that conditionally
copies its input before modifying it, depending on `makeBackup`.

See the reading's [Putting It All Together](https://BU-EK125.github.io/EK125/class/Class13.html#putting-it-all-together) section for a refresher.

```{literalinclude} Class13_GPP.py
:language: python
:lines: 444-493
```

## Part 10: Challenge Problems (If You Finish Early)

**Challenges 10.1-10.4:** Linear interpolation between two points, a
positive-number input prompt with error checking, a function whose return
value depends on the type of its argument, and building an identity matrix.

```{literalinclude} Class13_GPP.py
:language: python
:lines: 494-565
```
