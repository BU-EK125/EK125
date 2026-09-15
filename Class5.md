# Class 5: Importing Modules and Basic Loops

## Introduction

In this reading, you'll learn two powerful concepts that will expand what you can do with Python:

1. **Importing modules** - accessing additional functions and capabilities beyond basic Python
2. **Loops** - repeating code automatically to handle repetitive tasks

These two concepts work together beautifully: loops let you repeat operations, and modules give you interesting operations to repeat! We'll start with imports so you can use them in today's practice problems.

---

## Part 1: Importing Modules - Expanding Python's Power

### What is a Module?

So far, you've been using Python's built-in functions like `print()`, `input()`, `len()`, and `type()`. These are always available. But Python has many more functions organized into **modules** (also called **libraries**) that you can access when you need them.

A **module** is a Python file containing functions, variables, and classes that add specific capabilities to your programs. Think of modules as specialized toolboxes:
- `math` - mathematical functions like square root, trigonometry, constants like π
- `random` - generating random numbers and making random choices
- `time` - working with dates, times, and adding delays
- `os` - interacting with your operating system and files
- `sys` - system-specific parameters and functions

Python comes with a **Standard Library** containing dozens of useful modules that are pre-installed and ready to use.

---

### How to Import: Basic Syntax

To use functions from a module, you must first **import** it. There are several ways to do this, but we'll focus on the most common approaches.

#### Method 1: Import Specific Functions (Recommended for Beginners)

```python
from module_name import function_name
```

This imports just the function(s) you need, and you can use them directly:

```python
from random import randint

# Now you can use randint directly
dice_roll = randint(1, 6)
print("You rolled:", dice_roll)
```

**Benefits:**
- Clear and simple - you import exactly what you need
- Functions can be used directly by name
- Your code is easy to read

**To import multiple functions from the same module:**

```python
from random import randint, random, choice

# Now you can use all three functions
num1 = randint(1, 10)      # Random integer from 1 to 10
num2 = random()            # Random float from 0.0 to 1.0
fruit = choice(['apple', 'banana', 'orange'])  # Random choice from list
```

#### Method 2: Import the Entire Module

```python
import module_name
```

This imports the whole module, and you use functions by prefixing them with the module name:

```python
import random

# Use the module name before each function
dice_roll = random.randint(1, 6)
probability = random.random()
print("Rolled:", dice_roll)
print("Probability:", probability)
```

**Benefits:**
- Makes it clear where each function comes from
- Avoids naming conflicts if two modules have functions with the same name

#### Method 3: Import with an Alias (Nickname)

```python
import module_name as nickname
```

This is common for modules with long names:

```python
import random as rnd

dice_roll = rnd.randint(1, 6)
```

---

### ⚠️ Important: Avoid `from module import *`

You might see code like this:

```python
from random import *  # DON'T DO THIS!
```

This imports **everything** from the module. While it seems convenient, it's considered **bad practice** because:
1. It "pollutes your namespace" - you don't know what names you've imported
2. It makes debugging harder - where did that function come from?
3. Functions from different modules might have the same name and override each other

**Exception:** `from math import *` is sometimes acceptable because `math` is well-designed to avoid conflicts, but even then, the other methods are preferred.

---

### The `random` Module (You'll Use This Today!)

The `random` module is perfect for beginners because it creates interesting, unpredictable programs. Here are the key functions you'll use today:

#### `randint(a, b)` - Random Integer

Generates a random integer from `a` to `b` (inclusive on both ends):

```python
from random import randint

# Roll a six-sided die
roll = randint(1, 6)
print("Rolled:", roll)  # Could be 1, 2, 3, 4, 5, or 6

# Random age between 18 and 65
age = randint(18, 65)
print("Random age:", age)
```

**Key point:** Both endpoints are included! `randint(1, 6)` can return 1, 2, 3, 4, 5, **or 6**.

#### `random()` - Random Float

Generates a random floating-point number from 0.0 (inclusive) to 1.0 (exclusive):

```python
from random import random

# Random probability
prob = random()
print("Probability:", prob)  # Between 0.0 and 0.999...

# Random decimal between 0 and 100
percentage = random() * 100
print("Percentage:", percentage)
```

**Note:** Confusingly, the function `random()` is in the module `random`. So you write `from random import random` or `random.random()` depending on import style!

#### Using Both Functions

```python
from random import randint, random

# Roll dice
dice = randint(1, 6)
print(f"Dice roll: {dice}")

# Generate probability
chance = random()
print(f"Win probability: {chance:.2f}")
```

---

### The `math` Module - Mathematical Functions

For more advanced math operations:

```python
from math import sqrt, pi

# Calculate area of a circle
radius = 5
area = pi * radius**2
print(f"Area: {area:.2f}")

# Calculate square root
number = 16
root = sqrt(number)
print(f"Square root of {number} is {root}")
```

Common `math` functions:
- `sqrt(x)` - square root
- `pi` - the constant π (3.14159...)
- `e` - the constant e (2.71828...)
- `sin(x)`, `cos(x)`, `tan(x)` - trigonometric functions (x in radians)
- `log(x)` - natural logarithm
- `floor(x)`, `ceil(x)` - round down or up to nearest integer

---

### Getting Help on Modules

You can use the `help()` function to learn about any module or function:

```python
from random import randint
help(randint)
```

This will display documentation about how `randint` works, what parameters it takes, and what it returns.

---

### When to Import

**General rule:** Place all your `import` statements at the **top of your program**, before any other code:

```python
# Good practice - imports at the top
from random import randint, random
from math import sqrt, pi

# Then your code
number = randint(1, 100)
root = sqrt(number)
print(f"Random number: {number}, Square root: {root:.2f}")
```

This makes it easy to see what modules your program uses.

---

### Practice with Imports

Before moving on to loops, try these quick examples:

**Example 1: Random dice game**
```python
from random import randint

print("Rolling two dice...")
die1 = randint(1, 6)
die2 = randint(1, 6)
total = die1 + die2

print(f"Die 1: {die1}")
print(f"Die 2: {die2}")
print(f"Total: {total}")

if total == 7:
    print("Lucky seven!")
```

**Example 2: Random float for probability**
```python
from random import random

chance = random()
print(f"Random chance: {chance:.3f}")

if chance > 0.5:
    print("Heads!")
else:
    print("Tails!")
```

---

### What's Coming in the Afternoon

Today's afternoon session will cover:
- More import styles and when to use each
- Additional useful modules (`time`, `sys`, `os`)
- How modules help organize and reuse code
- Common pitfalls and best practices

For now, you know enough to use `from module import function` in today's practice problems!

---

## Part 2: For Loops

Loops are statements that repeat other statements (called the action). For loops are generally used as counted loops, in which the number of repetitions is specified ahead of time. In Python, `for` loops are frequently used to perform the same operation(s) on everything stored in a sequence. `while` loops are **conditional** loops, which repeat statements as long as an expression is `True`, or until something happens.

### Loops using range

For loops are used to repeat other statements (called the action) a specified number of times. The easiest way to specify how many times is to use the `range` function (which we will revisit later in the course). The `range` function generates a sequence of numbers. Called with an integer `n`, `range(n)` creates a sequence of `n` integers. By using an iterator variable (a variable the defines where along the sequence you want to loop over you currently are) and the `in` operator along with the `range` function, we can specify how many times to repeat an action. The general form to specify repeating an action n times is:

```python
for itervar in range(n):
    action
# rest of code
```

This says to repeat the action n times. The iterator variable `itervar` iterates through all of the numbers generated by the range function, and for each value of the iterator variable, the action is executed. The action can be any number of valid statements. All of the statements in the action must be indented to the same level (typically 4 spaces). For historical reasons, the iterator variable (`itervar`) is frequently named `i`.

For example, the following for loop specifies repeating the action of printing a single '!' 5 times.

```python
for i in range(5): 
    print('!', end='') 
print('\nOK')
```

This produces the output:

```
!!!!!
OK
```

The iterator variable `i` iterates through the 5 values produced by the `range` function, and for each of those five values it prints a single exclamation point, on the same line. Specifying `end = ''` keeps all of the exclamation points on the same line, with nothing printed in between them. After the loop, printing the newline character moves down to the next line, where 'OK' is printed.

Note that in this example, the iterator variable `i` was not used in the action; it simply specified how many times to execute the action. In some cases, however, using the value of the iterator variable in the action is desired.

The sequence that is produced by `range` begins with 0, and ends at n-1. For example, `range(4)` creates a sequence of 4 integers: 0, 1, 2, 3.

The following loop prints the integers 0 to 3 in a column, and then 'OK' after the loop.

```python
for i in range(4): 
    print(i) 
print('OK')
```

```
0
1
2
3
OK
```

In this example, the iterator variable `i` iterates through the values in the sequence produced by the `range` function. For every value of the iterator variable, the action is executed. The action in this case was to print the value of `i` (and the newline character, which print does by default). So, when `i` had the value 0, 0 was printed. Then, the iterator variable `i` got the value of 1, and 1 was printed. Then, `i` got the value of 2 and 2 was printed. Then, `i` got the value of 3 and 3 was printed. Once the iterator variable has iterated through all of the values in the sequence, the loop is over. Once the action was repeated 4 times, for every value in the sequence 0, 1, 2, 3, the next statement in the code after the loop was executed, which printed 'OK'.

The following prints the integers 0 to 2, each of which is followed by a colon, space, and '!'.

```python
for num in range(3):
    print(f'{num}: !')
```

```
0: !
1: !
2: !
```

Although frequently named `i`, the iterator variable can have any name. In this case, the iterator variable num iterated through the values 0, 1, and 2. The action that was executed for each value of `num` was to print `num` in a formatted line including a colon and exclamation mark.

So, again, sometimes the iterator variable is just used to specify how many times to repeat an action, as in:

```python
for i in range(3):  
    print('*')
```

```
*
*
*
```

Sometimes the value of the iterator variable is used in the action, as in:

```python
for i in range(3): 
    print(i)
```

```
0
1
2
```

### Looping through sequences

A `for` loop can be used in Python to iterate through the items in any sequence, and perform the same action for each one. The general form is

```python
for itervar in sequence:
    action
# rest of code
```

There is a variable, `itervar`, that iterates through all of the items in the sequence in order. For each item, the action is executed.

The following loops through all of the items in the list somenums and prints each in a sentence.

```python
somenums = [4, 33, 11] 
for n in somenums: 
    print('The number is', n)
```

```
The number is 4
The number is 33
The number is 11
```

At the beginning of the loop, the iterator variable `n` gets the value of the first number in the list, which is 4, so the action prints 'The number is 4'. Then, after the action has been executed in its entirety (in this case, it is just one statement), the iterator variable gets the next number in the list, 33. This is printed, and then `n` gets the value 11, which is printed. Once the action has been executed for all of the numbers in the list, the loop ends.

After the loop, the iterator variable n stores the last item from the list.

```python
somenums = [4, 33, 11] 
for n in somenums: 
    print('The number is', n)
print('n is', n)
```

```
The number is 4
The number is 33
The number is 11
n is 11
```

The list does not need to be stored in a variable. The following will produce identical results.

```python
for n in [4, 33, 11]: 
    print('The number is', n)
print('n is', n)
```

Another example illustrates looping through a list that stores different types of items, and displaying the type of each:

```python
mixedlist = [33, 'hi', False]
for m in mixedlist: 
    print(type(m))
```

```
<class 'int'>
<class 'str'>
<class 'bool'>
```

Since strings are sequences, for loops can iterate through the characters in a string. For example, the following prints each character in a string followed by a space:

```python
myword = 'hello' 
for c in myword: 
    print(c, end = ' ') 
```

```
h e l l o
```

### Calculating Running Sums

A useful application of a loop is to calculate a running sum. A running sum typically starts at 0, and then numbers are added to the sum one at a time. For example, the sum 0+1+2+3+4+5 would start at 0, then 0+1 which is 1, then 1+2 which is 3, then 3 + 3 which is 6, then 6 + 4 which is 10 and finally 10 + 5 which is 15.

The following code accomplishes this, using a running sum variable `runsum`, and then printing the overall sum.

```python
runsum = 0 
for i in range(6): 
    runsum = runsum + i 
print('The sum is', runsum)
```

```
The sum is 15
```

As the iterator variable `i` iterates through the values 0 through 5, each is added to the result that has already been stored in `runsum`. The action of the loop is simply to add to the running sum. Printing is only done after the loop, when the overall sum has been calculated.

In another example, the user is prompted for 4 numbers. Each of the numbers that the user enters is added to a running sum.

```python
runsum = 0 
for i in range(4): 
    num = float(input('Enter a number: '))  
    runsum = runsum + num 
print('The sum is', runsum)
```

```
Enter a number: 33
Enter a number: 4.5
Enter a number: -5
Enter a number: 2.8
The sum is 35.3
```

In this case, instead of adding the iterator variable `i` to the running sum, the numbers that the user enters into the variable num are added to the running sum.

A running sum can also be calculated from the numbers in a list.

```python
runsum = 0 
for n in [4, 33, 11]: 
    runsum = runsum + n 
print('The sum is', runsum)
```

```
The sum is 48
```

### Combining Loops with Random Numbers

Now that you know about both imports and loops, you can create programs with interesting random behavior:

```python
from random import randint

# Simulate rolling a die 5 times
print("Rolling a die 5 times:")
for i in range(5):
    roll = randint(1, 6)
    print(f"Roll {i+1}: {roll}")
```

Output (will vary each time):
```
Rolling a die 5 times:
Roll 1: 4
Roll 2: 6
Roll 3: 2
Roll 4: 6
Roll 5: 1
```

This combination of loops and random numbers is powerful for simulations, games, and testing!

---

## Part 3: Conditional Loops

### While and while-else

A loop is a statement that repeats other statement(s), which are called the action of the loop. A **conditional loop** repeats the action as long as an expression is `True`, or until something happens. In Python, the `while` statement is used as the conditional loop. The general form is:

```python
while expression:
    action
# rest of code
```

The `while` loop begins by evaluating the expression (which is also sometimes called the **condition**). If the expression is `True`, then the action is executed. So far, that is exactly like an `if` statement! But, after the action has been executed in its entirety, control goes back to the top of the loop, and the expression is evaluated again. If the expression is `True` this time, the action is executed again. Then, the expression is evaluated, and if it is `True`, the action is executed again. This continues as long as the expression is `True`. When the expression becomes `False`, the `while` loop ends and control goes to the rest of the code after the `while` loop. Just like selection statements and the `for` loop, the action can consist of any number of statements, which must be indented to the same level (typically 4 spaces).

For example, the while loop

```python
x = 2 
while x < 5: 
    x = x + 1 
    print(x) 
print('!')
```

would result in this output:

```
3
4
5
!
```

To begin with, the value of the variable `x` is 2, which is less than 5. So, the action is executed which increments `x` to get the value of 3, and this (3) is printed. 3 is less than 5, so the action is executed again, incrementing `x` to get the value of 4, and printing 4. 4 is still less than 5, so the action is executed again, incrementing `x` to get the value of 5, and printing 5. Then, when the expression is evaluated, 5 is not less than 5 so the expression is `False` and the `while` loop ends. The statement that prints '!' is after the loop, so it only executes once. Note that in this example the two statements in the action are indented 4 spaces.

Since the expression is always evaluated before the action in a `while` loop, it is possible that the action will not be executed at all. This could occur if the expression is `False` the first time that it is evaluated. The code

```python
x = 20 
while x < 5: 
    x = x + 1 
    print(x) 
print('!')
```

would result in this output:

```
!
```

Since 20 is not less than 5, the action of the loop is skipped and the code just prints '!'.

It is important that the action must change something in the expression so that eventually it becomes `False`. If this never happens, an infinite loop occurs. To exit from an infinite loop, hit `Control-C` in Windows or Linux, or `Command-C` on Macs for most Python environments. Others may be different; for example, in Jupyter notebooks it is necessary to choose Kernel and then `Interrupt`, or hit the square "interrupt the kernel" icon.

An optional `else` clause can be added to a `while` loop, which specifies an action to be executed when the condition becomes `False`. The general form is

```python
while expression:
    whileaction
else:
    elseaction
# rest of code
```

For example, we could print the value of `x` that ends the action of the while loop:

```python
x = 2 
while x < 5: 
    x = x + 1 
    print(x) 
else: 
    print('We are done at', x) 
print('!')
```

```
3
4
5
We are done at 5
!
```

The `else` clause only works if the condition becomes `False`. Any other method of ending the loop would not result in the execution of the `else` clause.

### Error Checking

When there is user input into a program, there is almost always a valid range of values. For example, if the user is prompted to enter the length of the sides of a square, the user should enter a positive number. There might be a tighter range than that; for example, it may be specified that the sides should be in the range from 5 to 7 meters. Error-checking means checking the user's entry for errors. More specifically, error-checking generally involves continuing to prompt the user and read in the user's entry until a valid value is entered. In Python, this can be accomplished using a while loop.

For example, the following code prompts the user for a positive number, and loops to continue prompting the user until the user does enter a positive number. For now, we will assume that the user enters a number, although we will see functions in Chapter 5 that will allow us to check to make sure that the user in fact entered a number.

```python
number = input('Enter a positive number: ') 
number = float(number) 
while (number <= 0): 
    number = input('Seriously! Enter a positive number: ') 
    number = float(number) 
print('Thanks for entering', number)
```

Running the code might result in the following.

```
Enter a positive number: -5
Seriously! Enter a positive number: -11.1
Seriously! Enter a positive number: 3
Thanks for entering 3.0
```

The user was prompted for a positive number, but entered -5. Since the input function returns a string, the user's input is cast to the type `float`. Since that was a negative number (less than or equal to 0), the action of the loop was executed. In the action, the user was again prompted for a positive number ('Seriously!'), but again the user entered a negative number. So, the action was executed again but this time the user entered 3. Since 3 is not less than or equal to 0, the `False` condition causes the loop to cease executing. The code after the loop then printed the positive number that the user finally entered. Notice that prompting the user is repeated before the loop, and also in the action of the loop. This is so that there will be a new value of number every time the condition is evaluated.

Of course, it is possible that the user will follow instructions the first time and enter a positive number. In that case, running the code might result in the following.

```
Enter a positive number: 5.2
Thanks for entering 5.2
```

Since the condition is evaluated at the top of the loop, and it was already `False`, the action of the loop was skipped entirely.

### Counting in a while loop

With conditional loops, it is not known ahead of time how many times the action of the loop will be executed. However, it is often useful to count how many times the action ended up being executed.

This can be accomplished by creating a counter variable, initializing it before the loop, and incrementing it by one in the action of the loop (so it is incremented every time the action is executed). For example, when error-checking we may want to know how many tries it took before the user entered a correct value.

```python
counter = 0
number = input('Enter a positive number: ') 
number = float(number) 
counter = counter + 1 
while (number <= 0): 
    number = input('Seriously! Enter a positive number: ')  
    number = float(number) 
    counter = counter + 1 
print('Thanks for entering', number) 
print('It took you', counter, 'tries.')
```

```
Enter a positive number: -9
Seriously! Enter a positive number: 33
Thanks for entering 33.0
It took you 2 tries.
```

---

## Key Takeaways

**Imports:**
- Modules extend Python with additional functions and capabilities
- Use `from module import function` to import specific functions
- The `random` module provides `randint()` and `random()` for generating random numbers
- Always put imports at the top of your program
- You'll learn more about modules in this afternoon's session!

**For Loops:**
- Use `for` loops when you know how many times to repeat
- `range(n)` creates a sequence of n numbers (0 to n-1)
- Iterator variables step through sequences automatically
- Great for calculating running sums and processing lists

**While Loops:**
- Use `while` loops when you repeat until a condition becomes false
- The condition is checked before each iteration
- Perfect for error-checking user input
- Always make sure the loop can end (avoid infinite loops!)
- Can count iterations with a counter variable

**Together:**
- Loops + random numbers = simulations and games
- Loops + user input = interactive programs
- Proper use of these tools makes programs powerful and flexible

---

## Coming Up in Class

In today's Group Practice Problems, you'll:
- Use `from random import randint` and `from random import random`
- Write for loops with `range()`
- Create while loops for error checking
- Combine loops with conditional logic
- Build programs that use random numbers in interesting ways

Come to class ready to experiment and practice!
