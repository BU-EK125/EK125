"""
================================================================================
EK125 — Class 13: User-Defined Functions, Scope, and Copying
Group Exercise (Teams of 3)

Team Members:
- Your Name
- Partner 1 Name
- Partner 2 Name

Work together to complete the following tasks!

Today's topics:
- Writing functions with return values
- Writing functions that print (no return)
- Lambda functions
- Parameter passing (by value vs by reference)
- Keyword arguments and default parameters
- Variable scope (LEGB rule)
- Copying lists (shallow vs deep copy)

Remember: Functions should either RETURN values OR print, but not both!
================================================================================
"""

# ==============================================================================
# PART 1: Understanding Parameter Passing
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 1.1: Predict the Output (Immutable Types)
#
# Before running any code, predict what each snippet will print.
# Then run it to check your understanding.
#
# Snippet A: What happens when we pass an integer to a function?
# ------------------------------------------------------------------------------

def updateScore(score):
    score = score + 10
    print(f"Inside function: {score}")

playerScore = 50
updateScore(playerScore)
print(f"Outside function: {playerScore}")

# Your prediction:
# Inside function: __________
# Outside function: __________
#
# Explanation (why did this happen?):
#


# ------------------------------------------------------------------------------
# Problem 1.2: Predict the Output (Mutable Types - Modifying)
#
# Snippet B: What happens when we modify a list inside a function?
# ------------------------------------------------------------------------------

def updateScores(scores):
    scores.append(100)
    print(f"Inside function: {scores}")

playerScores = [85, 90, 78]
updateScores(playerScores)
print(f"Outside function: {playerScores}")

# Your prediction:
# Inside function: __________
# Outside function: __________
#
# Explanation (why is this different from Snippet A?):
#


# ------------------------------------------------------------------------------
# Problem 1.3: Predict the Output (Mutable Types - Reassigning)
#
# Snippet C: What happens when we reassign a list inside a function?
# ------------------------------------------------------------------------------

def resetScores(scores):
    scores = [0, 0, 0]
    print(f"Inside function: {scores}")

playerScores = [85, 90, 78]
resetScores(playerScores)
print(f"Outside function: {playerScores}")

# Your prediction:
# Inside function: __________
# Outside function: __________
#
# Explanation (why is this different from Snippet B?):
#


# ==============================================================================
# PART 2: Functions that Return Values
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 2.1: Inches to Feet Converter
#
# Write a function that converts integer inches to feet (1 foot equals 12 inches).
# Include a docstring. Use `help(your_function_name)` to display your docstring.
# ------------------------------------------------------------------------------

# Your solution:


# Test your function:


# ------------------------------------------------------------------------------
# Problem 2.2: Sign Function
#
# Write a sign function. The sign of a positive number is 1, the sign of 0 is 0,
# and the sign of a negative number is -1. Be sure to test all three cases.
# ------------------------------------------------------------------------------

# Your solution:


# Test your function with all three cases:


# ------------------------------------------------------------------------------
# Problem 2.3: Rectangle Calculator
#
# Write a function that will receive two arguments: the length and width of a
# rectangle. The function will return the area and perimeter in a tuple.
# Test calling the function and storing the area and perimeter in separate variables.
# ------------------------------------------------------------------------------

# Your solution:


# Test your function and unpack the results:


# ------------------------------------------------------------------------------
# Problem 2.4: Cumulative Product
#
# Write a cumulative product function. The function will receive a list of numbers,
# and will create a new list which is a list of the running products.
# For example, if the input is [4, 2, 5], the returned list would be [4, 8, 40].
# ------------------------------------------------------------------------------

# Your solution:


# Test your function:


# ==============================================================================
# PART 3: Functions that Print (No Return)
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 3.1: Star Box Printer
#
# Write a function that will print a box of *'s. Two arguments will be passed to
# the function: the number of rows to print, and the number of columns
# (the number of *'s in each row).
# ------------------------------------------------------------------------------

# Your solution:


# Test your function:


# ------------------------------------------------------------------------------
# Problem 3.2: Understanding None
#
# Call your star box function and assign the result to a variable.
# Verify that the value of the variable is None.
# This will always be the case for functions that do not have a return statement.
# ------------------------------------------------------------------------------

# Your code:


# ------------------------------------------------------------------------------
# Problem 3.3: Random String Selector
#
# Write a function that will receive a list of strings and will print a random
# string from the list. Remember: this function is printing, not returning.
# Hint: import random and use random.choice()
# ------------------------------------------------------------------------------

# Your solution:


# Test your function:


# ==============================================================================
# PART 4: Working with Keyword Arguments
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 4.1: Student Record System
#
# Complete the function below that creates student records with default values.
#
# Test your function with the following students:
#   1. Alice Smith, ID 12345, with all defaults
#   2. Bob Jones, ID 23456, Computer Science major (keep other defaults)
#   3. Charlie Brown, ID 34567, GPA 3.8, 45 credits (keep major default)
#   4. Diana Prince, ID 45678, Biology major, 3.9 GPA, 60 credits
#
# Question: Why are keyword arguments useful here?
# ------------------------------------------------------------------------------

def createStudent(name, studentId, gpa=0.0, major="Undeclared", credits=0):
    """
    Create a student record dictionary.

    Args:
        name: Student's full name
        studentId: Unique student ID number
        gpa: Grade point average (default: 0.0)
        major: Declared major (default: "Undeclared")
        credits: Completed credits (default: 0)

    Returns:
        Dictionary with student information
    """
    return {
        'name': name,
        'id': studentId,
        'gpa': gpa,
        'major': major,
        'credits': credits
    }

# Create the four test students:


# Print all students to verify:


# ==============================================================================
# PART 5: Variable Scope (LEGB Rule)
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 5.1: Fix the Broken Code
#
# This code has scope errors. Fix it so it works correctly.
# The goal is to track how many students have been processed.
# ------------------------------------------------------------------------------

# Goal: Track how many students have been processed
studentsProcessed = 0

def processStudent(name):
    print(f"Processing {name}")
    studentsProcessed = studentsProcessed + 1  # This line causes an error!
    return f"Processed: {name}"

# Uncomment to test (it will error):
# processStudent("Alice")
# processStudent("Bob")
# processStudent("Charlie")
# print(f"Total processed: {studentsProcessed}")  # Should print 3

# Your fixed version:


# ------------------------------------------------------------------------------
# Problem 5.2: Understanding Variable Lookup (LEGB)
#
# Predict what the code below prints. Then run it and explain the LEGB rule
# in your own words.
# ------------------------------------------------------------------------------

x = 10

def outer():
    x = 20

    def inner():
        print(f"Inner sees x = {x}")

    inner()
    print(f"Outer sees x = {x}")

outer()
print(f"Global sees x = {x}")

# Your prediction:
# Inner sees x = __________
# Outer sees x = __________
# Global sees x = __________
#
# Explain the LEGB rule in your own words:
#


# ==============================================================================
# PART 6: Copying Lists
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 6.1: Protecting Your Data
#
# You're analyzing student grades and need to sort them, but you want to keep
# the original order too.
# ------------------------------------------------------------------------------

# Method 1: Try this (wrong way)
grades = [85, 92, 78, 90, 88]
sortedGrades1 = grades
sortedGrades1.sort()
print(f"Original: {grades}")
print(f"Sorted: {sortedGrades1}")

# What went wrong?
# Answer:


# Now fix it using .copy():
grades = [85, 92, 78, 90, 88]

# Your fixed code:


# ------------------------------------------------------------------------------
# Problem 6.2: Shallow vs Deep Copy Challenge
#
# Run this code and explain what happens with shallow copy vs deep copy.
# ------------------------------------------------------------------------------

import copy

# Student records with nested lists
students = [
    ["Alice", [85, 90, 88]],
    ["Bob", [78, 82, 80]]
]

# Try shallow copy
shallowCopy = students.copy()
shallowCopy[0][1].append(95)  # Add a grade to Alice's record

print(f"Original: {students}")
print(f"Shallow copy: {shallowCopy}")

# What happened to the original?
# Answer:


# Now try with deep copy:
students = [
    ["Alice", [85, 90, 88]],
    ["Bob", [78, 82, 80]]
]

# Your code using copy.deepcopy():


# Print to compare:


# Explanation of the difference:


# ==============================================================================
# PART 7: Lambda Functions
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 7.1: Lambda Basics
#
# Write a lambda function named `add_eh` which adds ", eh?" to the end of a string.
# ------------------------------------------------------------------------------

# Your solution:


# Test it:


# ------------------------------------------------------------------------------
# Problem 7.2: Lambda with Exclamation
#
# Write a lambda function named `add_excite` that takes a string as input and
# returns the string with "!!!" added to the end.
#
# Example: print(add_excite("Wow")) should output "Wow!!!"
# ------------------------------------------------------------------------------

# Your solution:


# Test it:


# ==============================================================================
# PART 8: Mixed Return and Print Functions
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 8.1: Menu Function
#
# Write a function that will print a menu and return the user's choice from
# the menu. Error-check to make sure that the user's choice is valid.
# Note that no arguments need to be passed to this function.
#
# The function should:
# - Print a menu (e.g., "1. Option A", "2. Option B", "3. Option C")
# - Get user input
# - Return the valid choice (as an integer)
# - Keep looping until valid input is received
# ------------------------------------------------------------------------------

# Your solution:


# Test your function:


# ------------------------------------------------------------------------------
# Problem 8.2: String Reverser
#
# Since strings are immutable, we cannot use the reverse method with strings.
# Write a function string_rev that will receive a string parameter and will
# reverse the characters in the string and return the result.
# ------------------------------------------------------------------------------

# Your solution:


# Test your function:


# ==============================================================================
# PART 9: Putting It All Together
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 9.1: Class Roster with Bonus Points
#
# Write a function that processes a class roster and adds bonus points.
# This combines everything we've learned today!
#
# The function should:
# - Receive a list of [name, score] pairs
# - Have a default parameter bonusPoints=5
# - Have a default parameter makeBackup=True
# - If makeBackup is True, create a copy so the original isn't modified
# - If makeBackup is False, modify the original list directly
# - Return the list with bonus points added
# ------------------------------------------------------------------------------

def addBonus(students, bonusPoints=5, makeBackup=True):
    """
    Add bonus points to all students.

    Args:
        students: List of [name, score] pairs
        bonusPoints: Points to add (default: 5)
        makeBackup: If True, don't modify original (default: True)

    Returns:
        List with bonus points added
    """
    # Your implementation:
    pass


# Test cases:
roster = [["Alice", 85], ["Bob", 90]]

# Test 1: With backup (default)
result1 = addBonus(roster)
print(f"Original: {roster}")  # Should be unchanged
print(f"Result: {result1}")    # Should have bonus

# Test 2: Without backup
roster2 = [["Charlie", 78], ["Diana", 92]]
result2 = addBonus(roster2, bonusPoints=10, makeBackup=False)
print(f"Original: {roster2}")  # Should be modified
print(f"Result: {result2}")    # Should be same object


# ==============================================================================
# PART 10: Challenge Problems (If you finish early)
# ==============================================================================

# ------------------------------------------------------------------------------
# Challenge 10.1: Interpolate Function
#
# Write an "interpolate" function, which takes two tuples, (x0,y0) and (x1,y1),
# and an input x_i. It will then return the "interpolated" y value, that is to
# say the one which would correspond to x_i as if it were on a line.
#
# In other words, if (x0,y0) = (0,0), and if (x1,y1) = (1,0.5), then passing
# x_i=0.5 would result in returning y_i=0.25. And passing x_i=0.9 would return
# y_i = 0.45.
#
# It should return an error for any x value outside the range [x0,x1].
# ------------------------------------------------------------------------------

# Your solution:


# Test your function:


# ------------------------------------------------------------------------------
# Challenge 10.2: Prompt for Positive Number
#
# Write a function that will prompt the user for a positive number and error-check
# until the user enters a valid value. The function will receive one string argument,
# which specifies what the user is to enter.
# For example, if the string is "length", the function prompts the user for a length.
# ------------------------------------------------------------------------------

# Your solution:


# Test your function:


# ------------------------------------------------------------------------------
# Challenge 10.3: Type-Dependent Return
#
# Write a function that will return different things, depending on the type of
# the parameter. The parameter could be an integer, a float, a list, or a string.
# Test your function on all types of parameters.
#
# Example behavior:
# - If int: return the square of the number
# - If float: return the number rounded to 2 decimal places
# - If list: return the length of the list
# - If string: return the string in uppercase
# ------------------------------------------------------------------------------

# Your solution:


# Test with different types:


# ------------------------------------------------------------------------------
# Challenge 10.4: Identity Matrix
#
# Write a function that will return an Identity matrix. An identity matrix is
# a square matrix (same number of rows and columns) of all 0's, with 1's on
# the diagonal. The function will receive one parameter which is the number of
# rows and columns. The matrix will be represented by a nested list.
# ------------------------------------------------------------------------------

# Your solution:


# Test your function:


"""
===============================================================================
KEY TAKEAWAYS FOR TODAY:

1. PARAMETER PASSING:
   - Immutable types (int, float, string): passed "by value" (copies)
   - Mutable types (list, dict): passed "by reference" (can be modified)
   - BUT reassignment always creates a new local variable

2. FUNCTIONS SHOULD HAVE ONE PURPOSE:
   - Either calculate and RETURN values
   - OR accomplish a task like printing
   - NOT both!

3. KEYWORD ARGUMENTS:
   - Allow default values for parameters
   - Make function calls more flexible and readable
   - Can specify arguments in any order

4. SCOPE (LEGB RULE):
   - Local → Enclosing → Global → Built-in
   - Python searches in this order
   - Use parameters to pass values, not global variables!

5. COPYING LISTS:
   - Assignment (=) creates an alias, not a copy
   - .copy() creates a shallow copy (safe for simple lists)
   - copy.deepcopy() creates a deep copy (safe for nested structures)

6. LAMBDA FUNCTIONS:
   - Short, anonymous functions for simple operations
   - Syntax: lambda parameters: expression
   - Good for one-liners, not complex logic
===============================================================================
"""
