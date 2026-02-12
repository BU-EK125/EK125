# Class 7 Preread: Advanced Iteration and Nested Structures

## Overview

In the past few weeks, you've built a strong foundation with **loops**, **lists**, and **basic indexing**. You've learned how to repeat actions with for loops, how to store values in lists, and how to process data element by element.

This week, we're taking the next major step: working with **nested structures** and mastering more powerful ways to create and manipulate them. A nested structure is simply a list (or tuple) that contains other lists (or tuples). This creates data that looks like a grid or table—just like seats in a theater, squares in a chessboard, or entries in a multiplication table. 

⚠️ **Important Note:** These structures are **not strictly** organized into a grid (that's an **array**, which we'll study later!) but rather, the nesting structure can be **interpreted** as coordinates along a grid.

This preread introduces you to several interconnected skills:

1. **Powerful iteration tools**: `range`, `enumerate`, and iteration through sequences
2. **Tuples**: Quick refresher on this immutable sequence type
3. **List comprehensions**: A compact way to build lists in one line
4. **Nested comprehensions**: Building 2D structures compactly
5. **Multi-level indexing**: Accessing values in nested structures
6. **Slicing**: Extracting "windows" of values at once

Everything we do this week builds directly on what you already know. We're just adding more tools to your toolkit!

---

## Part 1: Foundational Tools

### Range and Enumerate

We've seen that the `range` function generates a sequence of integers. When called as `range(n)`, it generates the sequence of integers from 0 through n-1. The type returned from range is `range`, although it can be passed to the `list` function if a list consisting of the individual items is desired.

```python
>>> mr = range(6)
>>> print(mr, type(mr))
range(0, 6) <class 'range'>
```

```python
>>> ml = list(mr)
>>> print(ml, type(ml))
[0, 1, 2, 3, 4, 5] <class 'list'>
```

So, `range` does not create a list; it creates an **iterator**. An interesting aspect of iterators is that the values are created one at a time; the entire iterator is not created all at once.

#### Optional Arguments to Range

If two arguments are passed to the `range` function, they specify the first value (instead of the default of 0) and the last (minus 1). For example, `range(3,7)` generates the sequence of integers 3, 4, 5, 6.

```python
>>> mr = range(3, 7)
>>> ml = list(mr)
>>> print(ml)
[3, 4, 5, 6]
```

An integer "step" value can also be specified as a third argument (instead of the default of 1).

```python
>>> mr = range(3, 10, 2)
>>> ml = list(mr)
>>> print(ml)
[3, 5, 7, 9]
```

Step values can also be negative.

```python
>>> ml = list(range(10, 2, -2))
>>> print(ml)
[10, 8, 6, 4]
```

#### The Enumerate Function

The `range` function is frequently used with `for` loops to specify how many times to execute the action of a loop. But what if you need both the **index** and the **value** at the same time?

The `enumerate` function returns both an index and an item from a sequence such as a list.

```python
numlist = [4, 52, 33, 11, -3]
for i, item in enumerate(numlist):
    print('Item', i, 'is', item)
```

**Output:**

```
Item 0 is 4
Item 1 is 52
Item 2 is 33
Item 3 is 11
Item 4 is -3
```

Notice that this gives us two iterator variables: `i`, which is the index, and `item`, which is the value at that position in the list.

**Why This Matters:** Sometimes you need to know **where** you are in a sequence, not just **what** the value is. `enumerate()` saves you from having to manually manage counter variables.

#### Pause and Think
- What would `list(range(5, 1))` produce? Why?
- When would you use `enumerate()` instead of just iterating through the list directly?

---

### Tuples: A Quick Refresher

We talked about tuples in Weeks 1 and 2, but we haven't used them much. Let's refresh our memory and introduce a few points about tuples we haven't yet discussed.

Tuples are similar to lists, but are **immutable** (cannot be changed after creation). Tuples are generally created by putting values in parentheses, separated by commas.

```python
>>> mytup = (2, 11, 33)
```

Functions such as `len` and indexing/slicing work the same on tuples as on lists.

```python
>>> len(mytup)
3
```

```python
>>> mytup[1]
11
```

#### Creating Tuples

Parentheses are not always necessary:

```python
>>> newtuple = 5, 19
>>> newtuple
(5, 19)
```

The concatenation operator can be used to join two tuples together.

```python
>>> mytup + newtuple
(2, 11, 33, 5, 19)
```

An empty tuple is created using parentheses with nothing inside:

```python
>>> emptup = ()
>>> len(emptup)
0
```

To create a tuple with one entry, the value must be followed by a comma, and both must be in parentheses.

```python
>>> onetup = (7,)
>>> onetup
(7,)
```

The parentheses and comma here are necessary. If the comma is omitted, the value is just an integer:

```python
>>> print(type((7,)), type((7)))
<class 'tuple'> <class 'int'>
```

#### Converting Between Types

The `list` function can be used to create a list from a tuple:

```python
>>> tl = list(mytup)
>>> tl
[2, 11, 33]
```

The `tuple` function can be used to create a tuple from another sequence type such as a string or a list:

```python
>>> wordlist = ['howdy', 'hi']
>>> wordtuple = tuple(wordlist)
>>> chartuple = tuple(wordlist[0])
>>> print(wordlist, wordtuple, chartuple)
['howdy', 'hi'] ('howdy', 'hi') ('h', 'o', 'w', 'd', 'y')
```

#### Packing and Unpacking

Putting values into a tuple is called "packing":

```python
>>> mytup = 2, 11, 33
```
or

```python
>>> mytup = (2, 11, 33)
```

The reverse is called "unpacking". In order to unpack a tuple, it is necessary to know how many values are in the tuple and to have that many variables on the left-hand side of the assignment operator.

```python
>>> a, b, c = mytup
>>> print(mytup, a, b, c)
(2, 11, 33) 2 11 33
```

**Why This Matters:** Unpacking is very useful! You'll see it used with `enumerate()` and when looping through nested structures.

Here's a practical example of why unpacking matters. Suppose you have coordinate pairs:

```python
coordinates = [(0, 5), (10, 15), (20, 25)]
```

**Without unpacking**, you'd need extra lines to extract each value:

```python
for coord in coordinates:
    x_value = coord[0]
    y_value = coord[1]
    print(f"x: {x_value}, y: {y_value}")
```

**With unpacking**, it's much cleaner:

```python
for x, y in coordinates:
    print(f"x: {x}, y: {y}")
```

**Output:**

```
x: 0, y: 5
x: 10, y: 15
x: 20, y: 25
```

This makes your code more readable and less error-prone. Instead of remembering "index 0 is x and index 1 is y," you just use meaningful variable names directly.

Unpacking is also possible for other sequence types such as lists and strings.

#### Pause and Think
- What's the difference between `(7)` and `(7,)`?
- When would you choose a tuple over a list?

---

## Part 2: List Comprehensions

### Basic List Comprehensions

In general, `for` loops are used to iterate through data structures such as Python sequences in order to perform the same operation on every element. A common pattern is:

```python
result = []
for i in range(5):
    result.append(i**3)
```

**Vectorizing code** means getting rid of loops, and instead using built-in functions and compact expressions. One powerful way to vectorize Python code when creating lists is to use **list comprehensions**.

Comprehensions do not add any power to the language, but provide a convenient, succinct way to create sequences. The simplest general form of a list comprehension is:

```python
[expression for i in iterable]
```

which creates a list of the expressions for all values of `i`. For example:

```python
>>> [i ** 3 for i in range(5)]
[0, 1, 8, 27, 64]
```

This creates a list of the cubes of all values of `i` in the range from 0 to 4 inclusive. Assigning this to a list variable:

```python
>>> cubelist = [i**3 for i in range(5)]
```

is equivalent to the loop we showed earlier:

```python
cubelist = []
for i in range(5):
    cubelist.append(i**3)
```

### Adding Conditionals

Conditionals (such as `if-else`) can be added to the list comprehension to determine which expressions to include in the list. For example:

```python
>>> cubelisteven = [i**3 for i in range(7) if i%2==0]
```

creates a list of cubes of the even integers in the range from 0 to 6 inclusive, and is equivalent to:

```python
cubelisteven = []
for i in range(7):
    if i%2 == 0:
        cubelisteven.append(i**3)
```

📎 **Recall:** This was your first glimpse of **vectorization**. Instead of looping step by step, you could build the whole list in one expression.

#### Pause and Think
- How would you create a list of squares of all odd numbers from 1 to 10 using a list comprehension?
- What's shorter: a loop with append, or a list comprehension?

---

## Part 3: Nested Structures

### Why Nested Structures Matter

So far, your comprehensions have created flat lists—just a single row of values. But what if you want a table or grid? That's where **nesting** comes in.

Nested structures come naturally out of nested loops (Week 4). Instead of just printing values row by row, you can now **store** them in memory in a way that preserves their row/column relationships.

### Nested List Comprehensions

The key idea is this:

- The **inner comprehension** builds one **row**.
- The **outer comprehension** repeats that row for each iteration.

This mirrors what you did with **nested for loops** in Week 4—one loop for rows, one loop for columns. With nesting, you're compacting that logic into a single expression.

```python
[[col for col in range(3)] for row in range(2)]
```

**Output:**

```python
[[0, 1, 2], [0, 1, 2]]
```

**Step by step:**

1. The inner comprehension `[col for col in range(3)]` creates `[0, 1, 2]`.
2. The outer comprehension repeats that inner list twice, once for each row.

The final result is a list with two entries in the outer list, and three entries *within* each location of that outer list.

### Comparison to Nested Loops

You can do the same thing with a nested loop:

```python
nested = []
for row in range(2):
    inner = []
    for col in range(3):
        inner.append(col)
    nested.append(inner)
print(nested)
```

**Output:**

```python
[[0, 1, 2], [0, 1, 2]]
```

Both approaches are identical in logic. The comprehension is just a shorthand.

### Example: Product Table

```python
products = [[r * c for c in range(1, 5)] for r in range(1, 4)]
for row in products:
    print(row)
```

**Output:**

```python
[1, 2, 3, 4]
[2, 4, 6, 8]
[3, 6, 9, 12]
```

**Comparison to Nested Loop:**

```python
products = []
for r in range(1, 4):
    row = []
    for c in range(1, 5):
        row.append(r * c)
    products.append(row)

for row in products:
    print(row)
```

**Output:**

```python
[1, 2, 3, 4]
[2, 4, 6, 8]
[3, 6, 9, 12]
```

**Why this matters:** Nested comprehensions let you **construct** the very structures that nested loops would otherwise only **print**, or that would be constructed in a nested loop via `.append()`. That's the big shift this week.

#### Pause and Think
- How many items will this comprehension build in the *inner* comprehension: `[[c for c in range(4)] for r in range(3)]`?
- How many elements in total will the result contain?
- What happens if you swap the inner and outer loops?

---

### Working with Nested Lists

#### A Nested List Example

```python
seats = [['A1', 'A2'], ['B1', 'B2']]
```

**Looping through:**

```python
for row in seats:
    for seat in row:
        print(seat)
```

**Output:**

```
A1
A2
B1
B2
```

#### Using `enumerate()` with Nested Lists

Sometimes, just looping through values isn't enough—you also want to know **where** you are in the list. That's where `enumerate()` comes in: it gives you both the **index (position)** and the **value** at the same time.

This is especially useful for nested lists, where you often care about both the **outer list index number** and the **inner list index number**.

```python
for i, row in enumerate(seats):
    for j, seat in enumerate(row):
        print(f"Row {i}, Col {j}: {seat}")
```

**Output:**

```
Row 0, Col 0: A1
Row 0, Col 1: A2
Row 1, Col 0: B1
Row 1, Col 1: B2
```

#### `enumerate()` in a List Comprehension

Remember: comprehensions are just another way of expressing loops. That means you can combine `enumerate()` with **comprehensions** to directly build a new structured list in one step.

This is especially useful when you want to **tag** values with their positions or transform data into a new form without writing extra loop code.

```python
indexed = [(i, j, seat) 
           for i, row in enumerate(seats) 
           for j, seat in enumerate(row)]

print(indexed)
```

**Output:**

```python
[(0, 0, 'A1'), (0, 1, 'A2'), 
 (1, 0, 'B1'), (1, 1, 'B2')]
```

Now each seat is tagged with both row and column indices—this is structured data in action.

### Nested Tuples

Tuples are immutable but can still nest:

```python
blocks = ((8, 10), (11, 1), (2, 4))
print(blocks[1][0])
```

**Output:**

```python
11
```

And can be looped over. Notice that here we are **unpacking** each tuple into two separate variables, `start` and `end`, so they can be used directly:

```python
for start, end in blocks:
    print(f"Starts at {start}, ends at {end}")
```

**Output:**

```
Starts at 8, ends at 10
Starts at 11, ends at 1
Starts at 2, ends at 4
```

#### Pause and Think
- What's the difference between `[(8, 10), (11, 1)]` and `[[8, 10], [11, 1]]`?
- Which one is better if the values need to change?

---

## Part 4: Multi-Level Indexing

### Why This Matters

Nested loops build nested structures. But once those structures exist, you don't need to loop over everything—you can jump straight to the element you want with **multi-level indexing**.

This is like replacing a journey through the whole theater with a direct seat ticket: "Row 2, Seat 3."

### Indexing Into a Grid

```python
grid = [[10, 20], [30, 40], [50, 60]]

print(grid[0])      # First row
print(grid[2])      # Third row
print(grid[2][0])   # Third row, first element
```

**Output:**

```python
[10, 20]
[50, 60]
50
```

Think of each bracket as peeling away a layer:

```
grid        → entire 2D structure
grid[2]     → one row: [50, 60]
grid[2][0]  → one number: 50
```

⚠️ **Important:** Recall again that this grid is not **literally** a square, but rather an interpretation of a grid where the outer list represents rows and the inner lists represent columns. For example, in this structure, each row does not have to have the same number of entries (which would be true for an actual grid). Later we will discuss **arrays** that are **literally grids**.

### Visualizing Multi-Level Indexing

```
Grid = [
  [10, 20],   # Row 0
  [30, 40],   # Row 1
  [50, 60]    # Row 2
]

Indexes:   Row   Col
           [2]   [0]

Result:    50
```

Here, `grid[2][0]` means:

1. Go to **row 2** → `[50, 60]`.
2. Then go to **column 0** inside that row → `50`.

### Comparing to Loops

```python
for row in grid:
    for val in row:
        print(val)
```

**Output:**

```
10
20
30
40
50
60
```

Pinpointing with indexing:

```python
print(grid[1][1])  # Second row, second column
```

**Output:**

```
40
```

### Modifying Values

Recall that lists are *mutable* (tuples are not) so you can modify individual entries within a nested list:

```python
grid[0][1] = 99
print(grid)
```

**Output:**

```python
[[10, 99], [30, 40], [50, 60]]
```

#### Pause and Think
- If `grid` has 3 rows, what happens if you ask for `grid[3][0]`?
- If `grid[2]` is `[50, 60]`, what type is `grid[2]`? What type is `grid[2][0]`?
- Why does indexing always go **row first**, then **column**?

---

## Part 5: Slicing

### Why This Matters

Indexing gives you one element. **Slicing** gives you a **window** of elements in one step. This is both convenient and powerful: it's your **next** taste of **vectorization**.

📎 **Recall:** Comprehensions were your first vectorization step. You could replace a loop with one line that built the whole list. Slicing is another, simpler vectorization: instead of looping to collect values into a new list, slicing produces that new list immediately.

### The Basics

- In slicing, the colon `:` separates the **start index** from the **end index**.
- The slice **includes** the element at the **start** index,
- but it **stops right before** the **end** index (**exclusive**).

Think of it as: *start at the first number, go up to but not including the second.*

```python
nums = [5, 10, 15, 20, 25]
print(nums[1:4])   # Indices 1 through 3
print(nums[:3])    # Start from the beginning through index 2
print(nums[2:])    # Start from index 2 to the end of the list
print(nums[-1])    # Last element
print(nums[:-1])   # Everything but the last element
```

**Output:**

```python
[10, 15, 20]
[5, 10, 15]
[15, 20, 25]
25
[5, 10, 15, 20]
```

**Visual diagram for `nums[1:4]`:**

```
Index:   0    1    2    3    4
Value:   5   10   15   20   25
Slice:       [----|----|----)   
             ^              ^
             start=1        end=4 (exclusive)
```

Here, the slice starts at index `1` (value `10`) and goes up to but not including index `4`. That's why you get `[10, 15, 20]`.

👉 **Note:** A very common beginner mistake is to expect the slice `[1:4]` to include the element at index `4`. Remember: **end is exclusive**.

### Loops vs Slicing

Why compare loops to slicing? Because they solve the same problem: extracting a subset of values from a list.

- A loop does it **step by step**: you move through indices one by one, appending values to a new list.
- Slicing does it in **one vectorized expression**: you describe the block of data you want, and Python hands it back.

This shift from "step-by-step instructions" to "whole-block operations" is at the heart of vectorized thinking.

**Loop approach:**

```python
subset = []
for i in range(1, 4):
    subset.append(nums[i])
print(subset)
```

**Output:**

```python
[10, 15, 20]
```

**Vectorized with slicing:**

```python
print(nums[1:4])
```

**Output:**

```python
[10, 15, 20]
```

### Negative Indices

Negative indexing (or working backwards from the end of a list) is not limited to -1:

```python
print(nums[-1])   # Last element
print(nums[-2])   # Second to last
print(nums[:-1])  # All but last
```

**Output:**

```python
25
20
[5, 10, 15, 20]
```

⚠️ **Important:** We'll keep slicing simple in this preread—only working with **flat lists**, not nested ones. Advanced slicing (like selecting whole rows or columns of a grid) will come later.

#### Pause and Think
- What is the length of `nums[2:5]`?
- What happens with `nums[1:10]`?
- Why might negative indices be safer than hardcoding `len(nums)-1`?

---

## Summary Table

| Concept                 | Example                                           | Result                |
|-------------------------|---------------------------------------------------|-----------------------|
| Range with step         | `list(range(2, 10, 3))`                           | `[2, 5, 8]`           |
| Enumerate               | `for i, x in enumerate(['a', 'b'])`               | `(0, 'a'), (1, 'b')`  |
| Tuple unpacking         | `a, b = (5, 10)`                                  | `a=5, b=10`           |
| Basic list comp         | `[x for x in range(3)]`                           | `[0, 1, 2]`           |
| Nested list comp        | `[[x for x in range(2)] for _ in range(3)]`       | `[[0, 1], [0, 1], [0, 1]]` |
| Nested list indexing    | `seats[1][0]`                                     | `'B1'`                |
| Tuple in list           | `((8, 10), (11, 1))[1][0]`                        | `11`                  |
| Slice of list           | `nums[1:4]`                                       | `[10, 15, 20]`        |
| Negative index          | `nums[-1]`                                        | `25`                  |

---

## Why This All Matters

This week is about moving from **procedural thinking** (loops that do everything step by step) to **structural thinking** (building and working with data structures efficiently).

- **Range and enumerate** give you more control over iteration
- **Tuples** provide immutable sequences for fixed data
- **List comprehensions** let you build lists compactly in one line
- **Nested comprehensions and loops** let you build **2D data**
- **Multi-level indexing** lets you access **exactly** what you need from that data
- **Slicing** lets you work with **spans of data** at once—your first step into **vectorization**

These skills are foundational for later work in **tabular data**, **2D arrays**, and libraries that rely heavily on vectorized operations (like **NumPy** and **pandas**). They also reappear in **string processing**, since strings can be sliced just like lists.

---

## Quick Check: Did You Understand This?

- Can I explain what `enumerate()` does and why it's useful?
- Can I create both a tuple and a list, and explain when to use each?
- Can I write a simple list comprehension to replace a for loop?
- Can I explain how a nested list comprehension builds **rows vs columns**?
- Can I trace exactly what `grid[1][2]` refers to and **why**?
- Can I predict the **length** of `nums[1:4]` without running it?
- Can I write both a **nested loop** and a **nested comprehension** to create the same **2D structure**?
- Can I use `enumerate()` to **track row/column positions** in a nested loop?
- Can I explain **why slicing is considered a simple form of vectorization**?
