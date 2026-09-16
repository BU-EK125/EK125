"""
================================================================================
EK125 — Class 14: Scope, Argument Passing, and Copying
Group Practice Problems (Teams of 3)
Spring 2026

Team Members:
- Your Name
- Partner 1 Name  
- Partner 2 Name

Instructions:
- Work in groups of THREE
- You MAY use references (readings, slides, internet)
- Do NOT use AI to write code - you need to learn yourself!
- Save frequently (Ctrl+S / Cmd+S)
- Test your code as you go!

IMPORTANT: This is our first day using VS Code!
- Remember to save your file before running
- Run your code using the Run button or F5
- Check the terminal at the bottom for output
================================================================================
"""

# ==============================================================================
# PROBLEM 1: Understanding Local Scope
# ==============================================================================
"""
What will this code print? Predict first, then run it.
Explain why it produces this output.
"""

def test_scope():
    x = 10
    print(f"Inside function: x = {x}")

x = 5
print(f"Before function: x = {x}")
test_scope()
print(f"After function: x = {x}")

# Your prediction:
# 




# Explanation of what happened:
# 




print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 2: Modifying Lists (Mutable Arguments)
# ==============================================================================
"""
Predict what will happen when we run this code.
Then modify the function to NOT change the original list.
"""

def add_item(my_list, item):
    """Add an item to the list."""
    my_list.append(item)
    return my_list

# Test it
original = [1, 2, 3]
print(f"Original list: {original}")
result = add_item(original, 4)
print(f"Returned list: {result}")
print(f"Original after function: {original}")

# Why did the original list change?
# 



# Fixed version that doesn't modify original:
def add_item_safe(my_list, item):
    """Add an item to a COPY of the list."""
    # Your code here:
    
    
    


# Test fixed version
original2 = [1, 2, 3]
print(f"\nOriginal list: {original2}")
result2 = add_item_safe(original2, 4)
print(f"Returned list: {result2}")
print(f"Original after function: {original2}")

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 3: Shallow vs Deep Copy
# ==============================================================================
"""
Create a nested list and demonstrate the difference between
shallow copy and deep copy.

You'll need to import the copy module!
"""

import copy

# Original nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# TODO: Create a shallow copy




# TODO: Create a deep copy




# TODO: Modify the original (change the first element to 999)




# TODO: Print all three and observe what changed
print("Original matrix:", )
print("Shallow copy:", )
print("Deep copy:", )

# Explanation - what's the difference?
# 




print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 4: Avoiding Global Variables
# ==============================================================================
"""
This code uses a global variable (BAD PRACTICE!).
Rewrite it to use function parameters instead.

CRITICAL: We NEVER use global variables in this course - zero credit if you do!
"""

# Bad code with global variable:
total = 0  # Global variable - BAD!

def add_bad(x):
    """Bad function that uses global variable."""
    global total  # Using global - BAD!
    total += x
    return total

# TODO: Write a better version without global variables
# HINT: Pass the current total as a parameter and return the new total




# Test your good version:
my_total = 0
my_total = # call your function to add 5
my_total = # call your function to add 3
my_total = # call your function to add 7
print(f"Total: {my_total}")

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 5: Multiple Return Values and Scope
# ==============================================================================
"""
Write a function that takes a list of numbers and returns THREE values:
- The minimum value
- The maximum value  
- The average

Do NOT use the built-in min(), max(), or sum() functions.
Write your own logic using loops!

Test with: [23, 5, 67, 12, 89, 34, 56, 8]
"""

def analyze_list(numbers):
    """
    Analyze a list of numbers.
    
    Parameters:
        numbers (list): List of numbers to analyze
    
    Returns:
        tuple: (minimum, maximum, average)
    """
    # Your code here:
    
    
    
    
    
    


# Test your function
test_nums = [23, 5, 67, 12, 89, 34, 56, 8]
min_val, max_val, avg_val = analyze_list(test_nums)
print(f"Numbers: {test_nums}")
print(f"Minimum: {min_val}")
print(f"Maximum: {max_val}")
print(f"Average: {avg_val:.2f}")

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 6: Student Grade Tracker
# ==============================================================================
"""
Create a grade tracking system that demonstrates proper use of copying.

Write two functions:

1. calculate_curved_grades(grades, curve_percent)
   - Takes a list of grades and a curve percentage (e.g., 5 for 5%)
   - Returns a NEW list with curved grades
   - Does NOT modify the original list
   - Cap grades at 100

2. drop_lowest_grade(grades)
   - Takes a list of grades
   - Returns a NEW list with the lowest grade removed
   - Does NOT modify the original list

Test both functions and verify the original list is unchanged!
"""

def calculate_curved_grades(grades, curve_percent):
    """
    Apply a curve to grades without modifying the original list.
    
    Parameters:
        grades (list): List of grade values
        curve_percent (float): Percentage to add (e.g., 5 for 5%)
    
    Returns:
        list: New list with curved grades (capped at 100)
    """
    # Your code here:
    
    
    
    


def drop_lowest_grade(grades):
    """
    Remove the lowest grade without modifying the original list.
    
    Parameters:
        grades (list): List of grade values
    
    Returns:
        list: New list with lowest grade removed
    """
    # Your code here:
    
    
    
    


# Test your functions
original_grades = [78, 85, 92, 68, 88, 95]
print(f"Original grades: {original_grades}")

curved = calculate_curved_grades(original_grades, 5)
print(f"Curved grades: {curved}")
print(f"Original after curving: {original_grades}")

dropped = drop_lowest_grade(original_grades)
print(f"After dropping lowest: {dropped}")
print(f"Original after dropping: {original_grades}")

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 7: Nested Scope Challenge
# ==============================================================================
"""
Trace through this code carefully. Predict what it will print,
then run it to verify.

This demonstrates nested function scope!
"""

def outer():
    x = "outer"
    
    def inner():
        x = "inner"
        print(f"In inner: {x}")
    
    inner()
    print(f"In outer: {x}")

x = "global"
print(f"Global: {x}")
outer()
print(f"After outer: {x}")

# Trace through and explain the output:
# 




print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 8: Deep Copy with Dictionaries (Challenge)
# ==============================================================================
"""
You're managing student data where each student is represented as a dictionary
with a list of quiz scores.

Demonstrate the difference between shallow and deep copy with this structure!
"""

import copy

# Original data
students = [
    {'name': 'Alice', 'scores': [85, 90, 88]},
    {'name': 'Bob', 'scores': [78, 82, 80]},
    {'name': 'Charlie', 'scores': [92, 88, 95]}
]

# TODO: Create a shallow copy




# TODO: Create a deep copy




# TODO: Modify Alice's first score in the original to 100




# TODO: Print all three versions
print("Original:", students)
print("Shallow:", )
print("Deep:", )

# Explanation - what happened and why?
# 




print("\n" + "="*60 + "\n")


# ==============================================================================
# If you finish early, create your own problem!
# ==============================================================================
"""
Design a problem about scope or copying and challenge another group!

Your problem:
"""
