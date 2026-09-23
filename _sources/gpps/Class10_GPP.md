# Class 10 GPP: Mastering Slicing in Python

This is a script-based exercise: work through the problems directly in
PyCharm/VS Code (not in a notebook). Download the file below, open it
locally, and run it as you go -- the instructions are also on this page so
you can read them without switching windows.

Download: [Class_10_GPP.py](Class10_GPP.py)

## Instructions

**Team Members:**
- Your Name
- Partner 1 Name
- Partner 2 Name

**Instructions:**
- Work in groups of **THREE**
- You MAY use your preread notes and previous assignments
- Do **NOT** use AI tools (ChatGPT, Claude, Copilot, etc.)
- Not submitted for grading -- but this material **will** appear on quizzes and exams!

**PyCharm reminders:**
- Run your file with `Shift+F10` (or the green play button)
- Output appears in the terminal at the bottom
- Save frequently with `Ctrl+S` / `Cmd+S`
- Nothing prints automatically -- you must use `print()`

## Warm-Up: Quick Slicing Drills

Complete these quick exercises to practice basic slicing. Each answer
should be a single slice expression on one line.

Given:
```python
word = "Python"
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
```

Write slices to extract:
1. `"Pyt"` from `word`
2. `"hon"` from `word`
3. `"th"` from `word`
4. `[10, 20, 30]` from `numbers`
5. `[40, 50, 60]` from `numbers`
6. `[70, 80, 90]` from `numbers`
7. `[10, 30, 50, 70, 90]` from `numbers` (every other, starting at index 0)
8. `[20, 40, 60, 80]` from `numbers` (every other, starting at index 1)
9. `90` as a single value (using a negative index)
10. `[70, 80, 90]` as a list (using a negative index)

See the reading's [Simplest Slice Notation](https://BU-EK125.github.io/EK125/class/Class10.html#simplest-slice-notation) section for a refresher.

```{literalinclude} Class10_GPP.py
:language: python
:lines: 47-63
```

## Warm-Up 2: Negative Index Drills

Given:
```python
data = [5, 10, 15, 20, 25, 30, 35, 40]
text = "HelloWorld"
```

Write slices to extract:
1. `[30, 35, 40]` using negative indices
2. `[5, 10, 15, 20, 25]` (all but last 3) using negative indices
3. `"World"` from `text` using negative indices
4. `"Hello"` from `text` using negative indices
5. `[40]` as a **list** using negative indices
6. `40` as a single **value** using a negative index

See the reading's [Negative Indices in Slices](https://BU-EK125.github.io/EK125/class/Class10.html#negative-indices-in-slices) section for a refresher.

```{literalinclude} Class10_GPP.py
:language: python
:lines: 83-95
```

## Problem 1: Basic Slice Practice

Ask the user for a word, then print:
1. The first 3 characters
2. The last 3 characters
3. Characters from index 2 to 5 (not including 5)
4. Every other character

Example run:
```text
Enter a word: Programming
First 3 characters: Pro
Last 3 characters: ing
Characters 2 to 5: ogr
Every other character: Pormig
```

See the reading's [The Step Parameter](https://BU-EK125.github.io/EK125/class/Class10.html#the-step-parameter) section for the "every other character" pattern.

```{literalinclude} Class10_GPP.py
:language: python
:lines: 116-130
```

## Problem 2: Working with Negative Indices

Given the list below, use **negative** indices or slices to print:
1. The last element (as a single value)
2. The last 4 elements (as a list)
3. All but the last 2 elements
4. The second-to-last element

Expected output:
```text
Last element: 80
Last 4 elements: [50, 60, 70, 80]
All but last 2: [10, 20, 30, 40, 50, 60]
Second-to-last: 70
```

See the reading's [Negative Indices in Slices](https://BU-EK125.github.io/EK125/class/Class10.html#negative-indices-in-slices) section for a refresher.

```{literalinclude} Class10_GPP.py
:language: python
:lines: 150-162
```

## Problem 3: Step Practice

Given the string `"abcdefghijklmnop"`, print:
1. Every 2nd character
2. Every 3rd character
3. Every 2nd character starting from index 1
4. Every 4th character starting from index 2

Expected output:
```text
Every 2nd character: acegikmo
Every 3rd character: adgjmp
Every 2nd starting from 1: bdfhjlnp
Every 4th starting from 2: cgko
```

See the reading's [The Step Parameter](https://BU-EK125.github.io/EK125/class/Class10.html#the-step-parameter) section for a refresher.

```{literalinclude} Class10_GPP.py
:language: python
:lines: 182-194
```

## Problem 4: Reversing Practice

Ask the user for a word, then print:
1. The word reversed
2. The first half of the word, reversed
3. The second half of the word, reversed
4. Every other character, reversed

**Hint:** `len(word) // 2` gives you the midpoint index.

Example run:
```text
Enter a word: Python
Reversed: nohtyP
First half reversed: tyP
Second half reversed: noh
Every other character reversed: nhy
```

See the reading's [Negative Steps (Reversing)](https://BU-EK125.github.io/EK125/class/Class10.html#negative-steps-reversing) section for the `[::-1]` idiom.

```{literalinclude} Class10_GPP.py
:language: python
:lines: 217-229
```

## Problem 5: Palindrome Checker

Ask the user for a word and check if it is a palindrome -- a word that
reads the same forwards and backwards.

Use slicing to reverse the word, then compare it to the original.

Example runs:
```text
Enter a word: radar
"radar" is a palindrome!

Enter a word: python
"python" is not a palindrome.

Enter a word: racecar
"racecar" is a palindrome!
```

```{literalinclude} Class10_GPP.py
:language: python
:lines: 252-258
```

## Problem 6: Extracting Parts of a Sentence

Ask the user for a sentence with at least 3 words, then use slicing and
`.index()` / `.rfind()` to extract:
1. The first word (everything before the first space)
2. The last word (everything after the last space)
3. The middle portion (everything between the first and last space)

**Hint:** `str.index(' ')` finds the first space. `str.rfind(' ')` finds the last.

Example run:
```text
Enter a sentence: The quick brown fox
First word: The
Last word: fox
Middle: quick brown
```

See the reading's [Slicing with Variables](https://BU-EK125.github.io/EK125/class/Class10.html#slicing-with-variables) section (the "Finding and extracting" example) for this exact pattern.

```{literalinclude} Class10_GPP.py
:language: python
:lines: 280-292
```

## Problem 7: Combining Slices

Given the list below, build a **new** list that contains:
- The first 3 elements
- Every 2nd element from the middle section (indices 3 to 8)
- The last 2 elements

Use slicing and the `+` operator to combine the pieces.

Expected output:
```text
Result: [1, 2, 3, 4, 6, 8, 9, 10]
```

See the reading's [Building New Sequences from Slices](https://BU-EK125.github.io/EK125/class/Class10.html#building-new-sequences-from-slices) section for a refresher.

```{literalinclude} Class10_GPP.py
:language: python
:lines: 310-316
```

## Problem 8: Slice Assignment

Use **slice assignment** to modify three different lists in place.

**Task 1:** On `list1`, replace indices 2, 3, 4 with the single value `99`.
```text
Original: [10, 20, 30, 40, 50, 60]
After:    [10, 20, 99, 60]
```

**Task 2:** On `list2`, replace every third element (indices 0, 3, 6) with `"SKIP"`.
```text
Original: ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
After:    ["SKIP", "b", "c", "SKIP", "e", "f", "SKIP", "h", "i"]
```

**Task 3:** On `list3`, insert `[100, 200, 300]` between indices 3 and 4.
```text
Original: [1, 2, 3, 4, 5]
After:    [1, 2, 3, 100, 200, 300, 4, 5]
```

After each modification, print the before and after. Use the labels shown
in the expected output above.

**Hint for Task 2:** slice assignment with a step requires the replacement
list to be the same length as the slice.
**Hint for Task 3:** assigning to an empty slice (`list3[3:3]`) inserts
without removing anything.

See the reading's [Slice Assignment (Lists Only)](https://BU-EK125.github.io/EK125/class/Class10.html#slice-assignment-lists-only) section for a refresher.

```{literalinclude} Class10_GPP.py
:language: python
:lines: 346-369
```
