# Class 6 Preread: Nested Loops

## Nested loops

A nested loop is one loop inside of another. In other words, the action of a loop contains another loop. Frequently, a nested loop is a nested `for` loop, in which one for loop is part of the action of another for loop.

In the following example, a list of words is created. A `for` loop loops through all of the words, and then for each word, another for loop loops to print each character followed by a space.

```python
wordlist = ['hello', "hi", 'ciao'] 
for myword in wordlist: 
    for c in myword: 
        print(c, end = ' ') 
    print() 
print("That's it!")
```
```
h e l l o
h i
c i a o
That's it!
```

The first loop is called the outer loop. The action of the outer loop consists of two statements: 
- loop to print each character and a space
- a `print()` to move the cursor down for the next word

The second loop, that loops over the characters, is called the inner loop. The action of the inner loop is a single `print` statement. After the nested loop, there is another `print` statement to print "That's it!". The outer loop iterates over the words in the list. For each word, the inner loop iterates over the characters in that word.

So, the first time in the outer loop the variable myword will store 'hello'. The inner loop variable will then iterate through all of the characters in the variable `myword`, and for each it will print the character and then a space (all on the same line). After the inner loop has completed, the `print()` statement will print a newline character, and that is it for the action of the outer loop. Once this action has completed, the variable `myword` will store the second string in the list, "hi". The inner loop will then iterate through all of its characters and print each one followed by a space. After both characters have been printed, the `print()` moves the cursor down to the next line. Finally, myword gets the value 'ciao', and the inner loop prints all of its characters on one line and then a newline at the end. Once the variable myword has iterated through all 3 words in the list, the outer loop is done so the code prints "That's it!" after the nested loop has completed.

The following is an example of a nested loop, in which the outer loop repeats 3 times. Each time the action is executed, the next integer (0 then 1 then 2) is printed, followed by a colon and a space. The inner loop then prints, 5 times, a single '*'. The second argument, end='', keeps all of the *'s on the same line and does not print anything between them. The `print()` after the inner loop prints the newline character by default, so each of the 3 actions from the outer loop is on a separate line.

```python
for num in range(3): 
    print(f'{num}:', end=' ')  
    for n in range(5): 
        print('*', end='')  
    print()
```
```
0: *****
1: *****
2: *****
```

The outer loop specifies that the action will be repeated 3 times. The action of the outer loop consists of 3 statements:

- A `print` statement to print the value of the outer loop variable
- A `for` loop to repeat the action of printing a single '*' 5 times on the same line 
- A `print` statement to move the cursor down for the next value of the outer loop variable

Instead of looping 5 times to print a '*', the following inner loop repeats `num` times, where `num` is the value of the outer loop variable (plus 1, so it repeats once, then twice, then three times).

```python
for num in range(3): 
    print(f'{num}:', end=' ')  
    for n in range(num+1):  
        print('*', end='')  
    print()
```
```
0: *
1: **
2: ***
```

If instead of printing 0, 1, and 2 in the beginning of the lines, we wanted 1, 2, and 3, the code would instead look like this:

```python
for num in range(3): 
    print(f'{num+1}:', end=' ')  
    for n in range(num+1):  
        print('*', end='')  
    print()
```
```
1: *
2: **
3: ***
```

These were examples of nested `for` loops. Nested loops can also contain `while` loops.
For example, let's say we want the user to enter 3 positive numbers. That means we will use a `for` loop to repeat the action 3 times. Each time, we will error-check using a `while` loop to make sure that each time a positive number is entered. The algorithm is:

- Loop 3 times
    - Prompt the user for a positive number
    - While the number is not positive
        - Print error message
        - Prompt again
    - Print the positive number

Here is an implementation of the algorithm:

```python
for i in range(3): 
    number = input('Enter a positive number: ')  
    number = float(number) 
    while (number <= 0): 
        print('Please follow directions!')  
        number = input('Enter a positive number: ') 
        number = float(number) 
    print('Thanks for entering', number) 
    print()
```
```
Enter a positive number: 4
Thanks for entering 4.0

Enter a positive number: -3.3
Please follow directions!
Enter a positive number: 5.1
Thanks for entering 5.1

Enter a positive number: -6
Please follow directions!
Enter a positive number: 11
Thanks for entering 11.0
```

An extra `print()` was added to the action of the outer for loop in order to separate each of the actions of the `for` loop.

## Using `if` Inside a Loop  

So far we have seen loops that repeat the same action every time. In practice, we often want the action to change depending on the current value of the loop variable. This is where an `if` statement inside a loop becomes useful.  

### Example: Even and Odd Numbers  

Let's look at the numbers from 0 through 9. For each number, we want to decide whether it is even or odd. To do this, we use the **modulus operator `%`**, which gives the remainder after division. If a number divided by 2 has no remainder (`n % 2 == 0`), the number is even. Otherwise, it is odd.  

```python
for n in range(10):          # loop through the numbers 0,1,2,...,9
    if n % 2 == 0:           # condition: is n evenly divisible by 2?
        print(n, "is even")  # runs when the condition is true
    else:                    
        print(n, "is odd")   # runs when the condition is false
```

### Step-by-step behavior
- On the first iteration, `n = 0`. Since `0 % 2 == 0`, the `if` branch runs and prints `0 is even`.  
- On the next iteration, `n = 1`. Since `1 % 2 == 0` is false, the `else` branch runs and prints `1 is odd`.  
- The loop continues this way for each number up to `9`.  

Output
```
0 is even
1 is odd
2 is even
3 is odd
4 is even
5 is odd
6 is even
7 is odd
8 is even
9 is odd
```

### Why this is important  
Combining loops with conditionals lets us write much more powerful programs.  
- The **loop** controls how many times the block of code runs.  
- The **if/else** decides which action to take on each iteration.  

This combination is used constantly in programming. With the same idea, you could:  
- Print only the negative numbers in a list.  
- Count how many numbers are above a certain threshold.  
- Skip or handle special cases differently while processing data.  

In short: loops let us repeat work, and `if` statements let us choose actions. Together, they form one of the most common and useful patterns in Python.

---

## Randomness and Reproducibility in Python

### Why Randomness Matters in Engineering

In engineering, results must be repeatable for trust and verification. However, Python programs often use randomness in:
- **Simulation** - approximating equations numerically
- **Testing** - random inputs can reveal hidden bugs
- **Optimization problems** - random initial guesses
- **Data analysis** - sampling datasets

The key challenge: How do we make "random" results reproducible?

### What is Reproducibility?

**Definition:** Running the same code twice and getting the same results.

**Why it matters in engineering:**
- **Verification** - check correctness of results
- **Debugging** - reproduce failures to fix them
- **Collaboration** - others must see what you saw

**Without reproducibility:**
- Results are confusing
- Bugs appear and vanish mysteriously
- Others can't verify your work

### Pseudo-Random Numbers in Python

When you use Python's `random` module, you're actually getting **pseudo-random numbers**:

```python
import random
print(random.randint(1, 6))  # Simulates a die roll
```

**Pseudo-random numbers:**
- Look random but are generated by a mathematical formula
- Each call steps forward in a fixed sequence
- Need a "seed" to start the sequence
- Same seed → same sequence of numbers
- Different seeds → different sequences

This is actually good! It means randomness can be **repeatable**.

### Setting the Seed for Reproducibility

To make random results reproducible, set a **seed** at the beginning of your program:

```python
import random

random.seed(42)  # Any integer works as a seed
print(random.randint(1, 6))
print(random.randint(1, 6))
print(random.randint(1, 6))
```

**What happens:**
- Run this code multiple times → **identical results every time**
- Change the seed to a different number → **different results, but still reproducible**
- Don't set a seed → **different results every run**

**Best practice:** Set the seed at the very beginning of your program or test.

### Example: Random Testing to Find Bugs

Random inputs are powerful for testing. Here's an example that tests division:

```python
import random

random.seed(7)  # Set seed for reproducibility

for i in range(5):
    a = random.randint(-5, 5)
    b = random.randint(-5, 5)
    
    if b == 0:
        print(f'Crash! Tried {a}/{b}')
    else:
        print(f'{a}/{b} = {a/b}')
```

**Why this is useful:**
- Different seeds → sometimes crash, sometimes not (finds the bug!)
- Fixed seed → crash repeats every run (reproducible for debugging!)

**Key idea:** Randomness helps **find** bugs → Reproducibility helps **fix** them!

### Combining Loops with Random Numbers

Now that you know about both loops and randomness, you can create interesting simulations:

```python
import random

random.seed(10)  # Set seed for reproducibility

# Simulate rolling a die 5 times
print("Rolling a die 5 times:")
for i in range(5):
    roll = random.randint(1, 6)
    print(f"Roll {i+1}: {roll}")
```

Output (will be the same every time with seed=10):
```
Rolling a die 5 times:
Roll 1: 3
Roll 2: 6
Roll 3: 3
Roll 4: 3
Roll 5: 2
```

**Important:** If you want different random numbers each time you run your program for an actual application (not testing), simply don't set a seed!

### When to Use Seeds

**Use a seed when:**
- Testing your code
- Debugging a problem
- Creating examples for others
- Doing reproducible scientific simulations
- Submitting homework that requires specific outputs

**Don't use a seed when:**
- Creating games (you want different outcomes each time!)
- Real-world applications where true randomness is needed
- Security applications (use `secrets` module instead)

### Summary: Randomness + Reproducibility = Power!

- **Pseudo-random:** Random numbers in Python ARE reproducible
- **Reproducibility:** Set a seed to get identical output
- **Testing power:** Random inputs reveal hidden bugs
- **Debugging power:** Reproducible sequences help fix bugs
- **Engineering principle:** Results must be verifiable and repeatable

Remember: Randomness and reproducibility work together to make your engineering code both powerful and trustworthy!
