# Class 14 GPP: Scripts, Comments, and Documentation

This is a script-based exercise: work through the problems directly in
PyCharm/VS Code (not in a notebook). Download the file below, open it
locally, and run it as you go -- the instructions are also on this page so
you can read them without switching windows.

Download: [Class14_GPP.py](Class14_GPP.py)

## Instructions

**Team Members:**
- Your Name
- Partner 1 Name
- Partner 2 Name

**Instructions:**
- Work in groups of **THREE**
- You MAY use your reading notes and previous assignments
- Do **NOT** use AI tools (ChatGPT, Claude, Copilot, etc.)
- Focus on **PROFESSIONAL CODE** today -- documentation matters!
- Not submitted for grading -- but this material **will** appear on quizzes and exams!

**PyCharm reminders:**
- Run your file with `Shift+F10` (or the green play button)
- Output appears in the terminal at the bottom
- Save frequently with `Ctrl+S` / `Cmd+S`

## Problem 1: Good Comments vs. Bad Comments

Four short reference snippets are shown (not meant to be run). For each one,
identify whether the comment is GOOD or BAD, then rewrite the bad ones to
be better. Remember: good comments explain WHY, not WHAT -- they clarify
non-obvious logic. Then find one line in your own previous homework and
write a genuinely good comment for it.

See the reading's [Script Structure Best Practices](https://BU-EK125.github.io/EK125/class/Class14.html#script-structure-best-practices) section for a refresher.

```{literalinclude} Class14_GPP.py
:language: python
:lines: 22-55
```

## Problem 2: Adding Docstrings to Functions

Below is an undocumented function. Add a proper docstring with a brief
description, parameter and return descriptions, and an example of usage.

```{literalinclude} Class14_GPP.py
:language: python
:lines: 60-87
```

## Problem 3: Script Organization

Reorganize a messy block of code following the standard structure: module
docstring, imports, constants, function definitions (with docstrings),
main program code, and the `if __name__ == "__main__":` pattern.

See the reading's [Script Structure Best Practices](https://BU-EK125.github.io/EK125/class/Class14.html#script-structure-best-practices) section for a refresher.

```{literalinclude} Class14_GPP.py
:language: python
:lines: 92-124
```

## Problem 4: Professional Temperature Converter

Write a complete, professionally documented temperature conversion script:
three functions (Celsius-to-Fahrenheit, Fahrenheit-to-Celsius,
Kelvin-to-Celsius), each with a full docstring and example, plus the
`if __name__ == "__main__":` pattern.

See the reading's [The `if __name__ == "__main__":` Pattern](https://BU-EK125.github.io/EK125/class/Class14.html#the-if-name-main-pattern) section for a refresher.

```{literalinclude} Class14_GPP.py
:language: python
:lines: 129-147
```

## Problem 5: Code Review -- Fix the Documentation

The function below has terrible documentation. Add a proper docstring,
rename the variables to be descriptive, and add helpful (non-obvious)
comments.

```{literalinclude} Class14_GPP.py
:language: python
:lines: 152-175
```

## Problem 6: Creating a Module with `if __name__ == "__main__"`

Write a GPA calculator module that works both when imported and when run
directly: `calculate_gpa(grades, credits)`, `letter_grade(gpa)`, a `main()`
that demonstrates both, and the main guard.

See the reading's [The `if __name__ == "__main__":` Pattern](https://BU-EK125.github.io/EK125/class/Class14.html#the-if-name-main-pattern) section for a refresher.

```{literalinclude} Class14_GPP.py
:language: python
:lines: 180-199
```

## Problem 7: Documentation Best Practices

Write `analyze_sensor_data`, a function that computes count, average, min,
max, and high readings from a list of temperatures -- demonstrating every
documentation best practice from today: module docstring, full function
docstring, example usage, WHY-comments, clear names, and formatting.

```{literalinclude} Class14_GPP.py
:language: python
:lines: 204-219
```

## Problem 8: Understanding the `if __name__ == "__main__"` Pattern

Explain in your own words what this pattern means, when Python sets
`__name__` to `"__main__"`, why the pattern is useful, and what happens if
you don't use it. Then write a short example demonstrating it.

See the reading's [The `if __name__ == "__main__":` Pattern](https://BU-EK125.github.io/EK125/class/Class14.html#the-if-name-main-pattern) section for a refresher.

```{literalinclude} Class14_GPP.py
:language: python
:lines: 224-239
```

## Bonus Challenge: Professional Statistics Module

If you finish early, create a complete, production-quality statistics
module: at least four functions (`mean`, `median`, `mode`,
`standard_deviation`), each fully documented, with a `main()` and the
`if __name__ == "__main__":` pattern.

```{literalinclude} Class14_GPP.py
:language: python
:lines: 244-261
```
