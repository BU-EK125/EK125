# EK125 Exam 1 - Top 30 GPP Problems for Paper Practice

**How to use this document:**

1. Work through problems in order (they're organized by difficulty per topic)
2. Try each problem ON PAPER first
3. Check your solution by typing it into Python
4. Mark problems you struggled with → those concepts go on your note sheet!

---

## 5-Day Practice Plan

**Day 1: Basics & Fundamentals** (Problems 1-6)
Focus on variables, operators, and basic syntax

**Day 2: Sequences & Logic** (Problems 7-12)
Work with strings, lists, and Boolean expressions

**Day 3: Conditionals** (Problems 13-18)
Master if/elif/else and nested conditionals

**Day 4: Loops** (Problems 19-24)
Practice for loops, while loops, and patterns

**Day 5: Advanced & Review** (Problems 25-30)
Nested loops and combining concepts

---

## Day 1: Basics & Fundamentals

### Problem 1: Simultaneous Assignment

**Class 1, Problem 1.4**

Write a simultaneous assignment statement that assigns:

- 0 to a variable named `mysum`
- 1 to a variable named `myproduct`

Display both results.

**Why this problem?** Tests basic variable assignment syntax that appears on every exam.

---

### Problem 2: Division Operators

**Class 1, Problem 1.12**

Given `x = 17` and `y = 5`, predict the output of each BEFORE running:

a) `x / y`

b) `x // y`

c) `x % y`

Then write code to verify your predictions.

**Why this problem?** Division operators trip up many students on exams. Know the difference!

---

### Problem 3: Bagel Cost Calculation

**Class 1, Problem 1.14**

Create a variable for the cost of a bagel ($2.25) and a constant for the tax rate (3%). Calculate the total cost and round to 2 decimal places.

**Why this problem?** Combines variables, constants, arithmetic, and rounding - all common exam requirements.

---

### Problem 4: Type Prediction

**Class 1, Problem 1.11**

WITHOUT running code, what type would the expression `5 - 4.0` return?

Write your prediction: ___________

Then verify with code using `type()`.

**Why this problem?** Type conversions are tested on every exam.

---

### Problem 5: Testing `round()`

**Class 1, Problem 1.7**

Test the `round()` function with:

- 4.2, 4.5, 4.8
- Negative numbers
- Integers

Then predict: What does `round(-5.7)` return?

**Why this problem?** Understanding built-in functions is critical for exams.

---

### Problem 6: Creative Math

**Class 1, Problem 1.15**

Using ONLY the integers 2 and 3, come up with at least 4 different expressions that equal 9.

**Why this problem?** Tests operator precedence and creativity with operations.

---

## Day 2: Sequences & Logic

### Problem 7: String Basics

**Class 2, Task 1.1**

Given:

```python
sentence = "The quick brown fox jumps over the lazy dog"
```

Write code to:

1. Print the first character
2. Print the last character
3. Print the length
4. Check if `"fox"` is in the sentence

**Why this problem?** String indexing and operators are exam staples.

---

### Problem 8: String Transformation

**Class 2, Task 1.2**

Given `name = "john doe"`, write separate statements to:

1. Convert to title case ("John Doe")
2. Replace spaces with underscores
3. Convert to uppercase
4. Count how many 'o' letters appear

**Why this problem?** String methods are heavily tested. Know them cold!

---

### Problem 9: List Modification Challenge

**Class 2, Task 2.2**

Start with:

```python
numbers = [10, 20, 30, 40, 50]
```

Use list methods to transform it to: `[5, 10, 20, 35, 50]`

You need to:

1. Change 30 to 35
2. Add 60 to end
3. Insert 5 at beginning
4. Remove 40
5. Remove last element

**Why this problem?** Comprehensive test of list methods - frequently appears on exams.

---

### Problem 10: Boolean Expression Evaluation

**Class 3, Part 1**

Given `x = 10`, `y = 5`, `z = 8`, evaluate on paper:

1. `(x > y) and (y < z)`
2. `(x < y) or (z > y)`
3. `not (x == 10)`
4. `(x > 5) and (y <= 5) and (z < 10)`

**Why this problem?** Boolean logic is tested on EVERY exam. Master this!

---

### Problem 11: Weather Decision System

**Class 3, Part 2**

Given:

```python
temperature = 68
is_raining = True
```

Write code to print ONE message based on these rules:

- temp < 50: "Wear a heavy jacket"
- 50 ≤ temp ≤ 70 AND raining: "Wear a light jacket"
- 50 ≤ temp ≤ 70 AND not raining: "Wear a sweater"
- temp > 70 AND raining: "Bring an umbrella!"
- temp > 70 AND not raining: "T-shirt weather!"

**Why this problem?** Complex Boolean logic with nested conditions - this is exam gold!

---

### Problem 12: Data Cleaning

**Class 2, Task 3.1**

Given:

```python
responses = ["yes", "NO", "maybe", "YES", "no", "Maybe", "yes"]
```

Write code to:

1. Convert all to lowercase
2. Count how many "yes", "no", and "maybe" responses
3. Create separate lists for each type

**Why this problem?** Combines string methods, loops, and counting - common exam pattern.

---

## Day 3: Conditionals

### Problem 13: Grade Classifier

**Class 4, Problem 2.3 Extended**

Given `score = 87`, write an `if/elif/else` chain that prints:

- "A" for 90-100
- "B" for 80-89
- "C" for 70-79
- "D" for 60-69
- "F" for below 60

**Why this problem?** Classic if/elif/else - appears on nearly every programming exam.

---

### Problem 14: Number Sign Checker

**Class 4, Problem 2.3**

Write code that takes a number from the user and prints:

- "Positive" if > 0
- "Negative" if < 0
- "Zero" if == 0

**Why this problem?** Simple but tests fundamental if/elif/else structure.

---

### Problem 15: Age Classification

**Class 4, Problem 3.2**

Given:

```python
age = 16
has_drivers_license = False
```

Write nested conditionals:

- If age < 13: Print "Child"
- If 13 ≤ age < 18:
  - If has_license: Print "Teen driver"
  - If not: Print "Teen"
- If age ≥ 18: Print "Adult"

**Why this problem?** Nested conditionals are a key exam skill.

---

### Problem 16: Pet Comparison

**Class 4, Problem 3.3**

Ask user for number of cats and dogs, then print:

1. "You have both cats and dogs!" if at least 1 of each
2. "You're more of a cat person" if more cats than dogs
3. "You're more of a dog person" if more dogs than cats
4. "Perfect balance!" if equal (and > 0)
5. "No pets yet!" if both are 0

**Why this problem?** Tests complex conditional logic and proper ordering.

---

### Problem 17: Quadratic Discriminant

**Class 4, Problem 3.4 Simplified**

Given coefficients `a = 1`, `b = -5`, `c = 6`:

Calculate discriminant: `b² - 4ac`

Then print:

- "Two real roots" if discriminant > 0
- "One real root" if discriminant == 0
- "No real roots" if discriminant < 0

**Why this problem?** Combines math with conditionals - common exam pattern.

---

### Problem 18: Material Length Table

**Class 4, Problem 1.1**

Given `length_feet = 12.5`, create formatted output showing:

```
Material Length Report
=====================
Feet:   12.5
Inches: [feet × 12]
Yards:  [feet ÷ 3]
```

Use f-strings with 2 decimal places.

**Why this problem?** Tests f-string formatting - frequently tested!

---

## Day 4: Loops

### Problem 19: Exploring `range()`

**Class 5, Problem 1.1**

1. Create `myr = range(6)`
2. Convert to list and print
3. Print the length

**Why this problem?** Understanding `range()` is essential for loop mastery.

---

### Problem 20: Rounded Values

**Class 5, Problem 1.4**

Create a list of floats:

```python
prices = [19.99, 24.50, 15.75, 32.00, 8.99]
```

Write a for loop that prints the rounded value of each number.

**Why this problem?** Basic for loop pattern - must know this!

---

### Problem 21: Two Loop Styles

**Class 5, Problem 1.5**

Given:

```python
strlist = ['hello', 'ciao', 'howdy', 'hi']
```

Write TWO for loops that print each greeting:

1. One that iterates directly over the list
2. One that uses indices with `range(len(strlist))`

**Why this problem?** Shows you understand both loop patterns - exam favorite!

---

### Problem 22: Running Sum with Random

**Class 5, Problem 1.6**

1. Generate random integer n from 2 to 5
2. Loop n times, asking user for a float
3. Print running sum after each input (1 decimal place)

Use `from random import randint`

**Why this problem?** Combines multiple concepts: random, loops, accumulator pattern.

---

### Problem 23: Debug the Running Product

**Class 5, Problem 1.7**

The following should calculate a running product of the integers from 1 to 5.
This code has a bug:

```python
runprod = 1
for i in range(6):
    runprod = runprod * i
    print('The product so far is', runprod)
```

Find and fix the bug!

**Why this problem?** Debugging is a KEY exam skill. Also tests `range()` understanding.

---

### Problem 24: Loops + Selection

**Class 5, Problem 1.8**

Generate 5 random integers (1 to 30). For each, print:

- The number
- Whether it's less than 15

**Why this problem?** Combining loops with conditionals - very common on exams!

---

## Day 5: Advanced & Review

### Problem 25: Circle Calculations

**Class 5, Problem 1.10**

Ask user for radius, then calculate and print (2 decimal places):

- Area: π × r²
- Circumference: 2 × π × r

Use `from math import pi`

**Why this problem?** Tests modules, math, formatting - comprehensive!

---

### Problem 26: Square Roots Loop

**Class 5, Problem 1.11**

Generate 5 random integers (1-100). For each:

- Print the number
- Print square root (2 decimals)
- Print if square root > 5

Use `from math import sqrt` and `from random import randint`

**Why this problem?** Combines loops, random, math, conditionals, formatting!

---

### Problem 27: While Loop Basics

**Class 5, Problem 2.1**

Given this while loop:

```python
count = 5
while count > 0:
    print("Counting down:", count)
    count = count - 1
print("Done!")
```

Questions:

1. What value for `count` makes loop run exactly once?
2. What value makes loop never run?

**Why this problem?** Understanding while loop conditions is crucial!

---

### Problem 28: While with Random

**Class 5, Problem 2.2**

Generate random integers (1-20) until you get one > 15. Print each number as you go, then print the final number that ended the loop.

**Why this problem?** Sentinel-controlled loops are exam favorites!

---

### Problem 29: Error Checking Loop

**Class 5, Problem 2.4**

Prompt user for a number between 1 and 10. Keep prompting until they enter a valid number. Use a `while` loop with compound Boolean condition.

**Why this problem?** Input validation with while loops - very common exam question!

---

### Problem 30: Pattern Printing

**Class 6, Problem 2**

- Loop over the numbers 0 through 4.
- On each line, first print the number, followed by a colon (`:`).
- After the colon, print as many asterisks (`*`) as the number itself.
- Each line should show the number and its matching stars.

The output should look like the following:

```
0:
1:*
2:**
3:***
4:****
```

**Why this problem?** Nested loops with pattern printing - classic exam problem!

---

## Exam Strategy Guide

### Time Management

- **Basics (Problems 1-6)**: 2-3 min each → 12-18 min total
- **Sequences & Logic (Problems 7-12)**: 3-4 min each → 18-24 min total
- **Conditionals (Problems 13-18)**: 4-5 min each → 24-30 min total
- **Loops (Problems 19-24)**: 5-6 min each → 30-36 min total
- **Advanced (Problems 25-30)**: 6-8 min each → 36-48 min total

**Total: ~2-2.5 hours if you do all 30**

### Paper Writing Tips

**Show Indentation Clearly**

```
for i in range(3):
....print(i)
....if i > 1:
........print("Big")
```

**Write Comments for Complex Logic**

```python
# Check if temperature is in valid range AND it's raining
if temp >= 50 and temp <= 70 and is_raining:
    print("Wear light jacket")
```

**Check Your Syntax**

Before moving to next problem, verify:

- ✓ Colons after `if`, `for`, `while`
- ✓ Matching parentheses
- ✓ Matching quotes
- ✓ `==` not `=` in conditions
- ✓ Consistent indentation

### Common Paper Exam Mistakes

1. **Forgetting colons** → `:` after `if`, `for`, `while`
2. **Wrong comparison** → `==` not `=`
3. **Off-by-one** → `range(5)` gives 0-4, not 1-5
4. **Uninitialized accumulator** → Must set to 0 before loop
5. **Infinite loops** → Forgetting to update condition variable
6. **Wrong operator** → `/` vs `//` vs `%`

---

## Final Checklist

Before the exam:

**Knowledge:**

- Can write all operators from memory
- Know all string methods
- Know all list methods
- Can write for loops in both styles
- Understand while loop conditions
- Can nest conditionals correctly
- Can nest loops correctly

**Skills:**

- Practiced writing code on paper 5+ times
- Can show indentation clearly
- Check syntax automatically
- Trace through code mentally
- Debug common errors quickly

**Preparation:**

- Created comprehensive note sheet
- Tested self on these 30 problems
- Identified weak areas
- Practiced weak areas extra
- Got good sleep before exam
