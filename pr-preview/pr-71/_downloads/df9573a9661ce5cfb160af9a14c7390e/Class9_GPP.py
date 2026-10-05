"""
================================================================================
EK125 Group Practice Problems - Class 9
Getting Comfortable with PyCharm

NOTE: The GPP page asks you to create each of these as its own .py file
(greeting.py, calculator.py, etc.) -- that's still the recommended way to
work through them. They are combined into one file here only so there's a
single download with every starter scaffold in it; copy each section into
its own file as you go, or work through them here, whichever you prefer.
================================================================================
"""

# ==============================================================================
# PROBLEM 1: Greeting Program (~10 minutes)
# ==============================================================================
"""
Create a new file called greeting.py.

Write a program that:
1. Uses input() to ask the user for their name.
2. Uses input() to ask the user for their age.
3. Calculates how old they will be in 10 years.
4. Prints a greeting that includes their name and their age in 10 years.

Example run:
    What is your name? Alice
    How old are you? 19
    Hi Alice! In 10 years you will be 29 years old.

Hint: input() always returns a string -- convert the age to an integer
with int() before doing math with it. Use an f-string for the final print().
"""

# Your code here


# ==============================================================================
# PROBLEM 2: Simple Calculator (~15 minutes)
# ==============================================================================
"""
Create a new file called calculator.py.

Write a program that repeatedly asks the user to pick an operation (add,
multiply, or quit), then asks for two numbers and prints the result. Keep
running until the user types "quit".

Your program should:
1. Print a welcome message listing the available operations.
2. Use a while True loop.
3. Inside the loop:
   - Ask the user for an operation with input().
   - If the operation is "quit", print "Goodbye!" and break out of the loop.
   - If the operation is "add" or "multiply", ask for two numbers with
     input(), convert them to floats, then compute and print the result.
   - If the operation is anything else, print "Unknown operation."

Example run:
    === Simple Calculator ===
    Operations: add, multiply, quit

    Enter operation (add/multiply/quit): add
    Enter first number: 10
    Enter second number: 3.5
    Result: 13.5

    Enter operation (add/multiply/quit): quit
    Goodbye!
"""

# Your code here


# ==============================================================================
# PROBLEM 3: Temperature Converter (~15 minutes)
# ==============================================================================
"""
Create a new file called temperature.py.

Write a program that converts temperatures between Celsius and Fahrenheit.
The program should:
1. Ask the user which direction to convert: "C to F" or "F to C".
2. Ask the user for the temperature value.
3. Perform the conversion and print the result rounded to 1 decimal place.
4. Repeat until the user types "quit" instead of a conversion direction.

Conversion formulas:
    Fahrenheit = Celsius * 9/5 + 32
    Celsius = (Fahrenheit - 32) * 5/9

Example run:
    === Temperature Converter ===
    Options: C to F, F to C, quit

    Enter conversion (C to F / F to C / quit): C to F
    Enter temperature: 100
    100.0 C = 212.0 F

    Enter conversion (C to F / F to C / quit): quit
    Goodbye!

Hint: Convert the temperature input to a float, and use round(value, 1) to
round to 1 decimal place. Compare the user's input string directly:
if direction == "C to F":
"""

# Your code here


# ==============================================================================
# PROBLEM 4: Number Guessing Game (~20 minutes)
# ==============================================================================
"""
Create a new file called guessing_game.py.

Write a number guessing game. The program picks a secret number and the
user tries to guess it, getting "Too high" or "Too low" hints after each
guess.

Your program should:
1. Store a secret number in a variable (pick any integer, e.g. 42).
2. Use a variable to count the number of guesses (start at 0).
3. Use a while loop that keeps running until the user guesses correctly.
4. Inside the loop:
   - Ask the user for their guess and convert it to an integer.
   - Increment the guess counter.
   - If the guess is too low, print "Too low! Try again."
   - If the guess is too high, print "Too high! Try again."
   - If the guess is correct, print a congratulations message that
     includes how many guesses it took, then break.

Example run (secret number is 42):
    I'm thinking of a number between 1 and 100.

    Enter your guess: 50
    Too high! Try again.

    Enter your guess: 42
    Correct! You got it in 2 guesses.

CHALLENGE (optional): After the basic version works, try importing the
random module and using random.randint(1, 100) to pick a truly random
secret number each time:
    import random
    secret = random.randint(1, 100)
"""

# Your code here


# ==============================================================================
# PROBLEM 5: Bug Hunt (~15 minutes)
# ==============================================================================
"""
Create a new file called bug_hunt.py.

This program is supposed to compute a student's average score and print
whether they passed or failed (passing is 65 or above). But it has THREE
BUGS hiding in it! Type it in exactly as written below -- don't fix
anything yet -- then use PyCharm's features to find and fix each one.

There are three bugs to find, one of each type:
  - Bug 1 (Syntax Error): PyCharm will underline something in red before
    you even run the code. Look for the red squiggly line and fix the
    syntax.
  - Bug 2 (Runtime Error): After fixing Bug 1, run the program. It will
    crash with a TypeError. Read the error message in the Run panel -- it
    tells you exactly which line has the problem and what went wrong.
  - Bug 3 (Logic Error): After fixing Bug 2, the program runs without
    errors -- but the output is wrong. Compare your output to the expected
    output below and find the line that doesn't do what it should.

Expected correct output:
    Average: 64.0
    Result: FAIL
"""

scores = [85, 42, 78, 65, 50]
total = 0

for score in scores
    total = total + score

average = total / len(score)

if average >= 65:
    result = "PASS"
else:
    result = "PASS"

print(f"Average: {average}")
print(f"Result: {result}")


# ==============================================================================
# PROBLEM 6: Batch Data Processing (~15 minutes)
# ==============================================================================
"""
Create a new file called weather_data.py.

A weather station recorded 14 daily high temperatures in Fahrenheit. Use
list comprehensions to analyze the data.

Step 1: Convert all temperatures to Celsius using a list comprehension.
  Use the formula from Problem 3: Celsius = (Fahrenheit - 32) * 5/9.
  Round each value to 1 decimal place. Print the Celsius list.

Step 2: Use a list comprehension with a condition to create a list of only
  the "warm" days -- temperatures that are 15 degrees C or above. Print the
  warm days list.

Step 3 (Stretch): Compute the day-to-day temperature changes using a list
  comprehension. Each change is the difference between a day's temperature
  and the previous day's temperature. You will need range() and indexing
  inside your comprehension. Round each change to 1 decimal place. Print
  the changes list.
  Hint: if your Celsius list is called temps_c, the change for day i is
  temps_c[i+1] - temps_c[i].

Expected output:
    Celsius: [7.2, 11.1, 8.9, 16.1, 12.8, 2.8, 5.6, 14.4, 17.2, 10.0, 8.3, 15.0, 17.8, 11.7]
    Warm days: [16.1, 17.2, 15.0, 17.8]
    Changes: [3.9, -2.2, 7.2, -3.3, -10.0, 2.8, 8.8, 2.8, -7.2, -1.7, 6.7, 2.8, -6.1]
"""

temps_f = [45, 52, 48, 61, 55, 37, 42, 58, 63, 50, 47, 59, 64, 53]

# Your code here


# ==============================================================================
# PROBLEM 7: The Collatz Conjecture (~20 minutes) -- CHALLENGE
# ==============================================================================
"""
Create a new file called collatz.py.

The Collatz Conjecture is one of the most famous unsolved problems in
mathematics. The rules are simple:
  - Start with any positive integer n.
  - If n is even, divide it by 2.
  - If n is odd, multiply it by 3 and add 1.
  - Repeat until you reach 1.

Part A: Write a program that:
1. Asks the user for a positive integer.
2. Prints the Collatz sequence starting from that number.
3. Prints how many steps it took to reach 1.

Example run:
    Enter a positive integer: 6
    6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    Steps: 8

Hints:
  - Use a while loop that runs as long as n != 1.
  - Use a counter variable for the number of steps.
  - To build the sequence, print as you go (print(n, end=" -> ")) or
    collect values in a list and join them at the end with " -> ".join(...).
  - To check if a number is even, use n % 2 == 0.

CHALLENGE (Part B): After Part A works, find which starting number between
1 and 100 produces the longest Collatz sequence. Print that number and how
many steps it takes. (No user input needed for this part -- just loop
through all 100 starting numbers.)
"""

# Your code here
